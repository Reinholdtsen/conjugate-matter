"""Velocity-space structure diagnostics for the corner N-body runs (round 3, label "corner").

Per snapshot (centre = shrinking-sphere centre; core = innermost 25% of particles):
  r10, r50, r90        Lagrangian radii
  sig_c, sig_k         core 1D dispersion of the canonical momentum per mass w and of xdot
  r_c = sig_c / v*     the gate ratio actually realized in the core
  kurt                 1D kurtosis of the core w components (Plummer centre: 2.571; Maxwellian: 3)
  Xi(d, u)             6D pair excess: among pairs with |dx| < d, the fraction with |dw| < u, divided
                       by the same fraction after the velocities are reassigned within radial shells of
                       100 particles (donor's v_r and |v_t| kept, tangential direction randomized),
                       minus 1.  Detects spatially compact co-moving groups (the gate's 'lumps carried
                       by a velocity-selected population').  d = 0.25 r50, u = v* and v*/2; also with xdot.
  S_l (l = 1..4)       velocity-direction clustering in radial shells of 200 particles,
                       S_l = (1/N_s) sum_{i,j} P_l(w_i^.w_j^), minus 1 (expectation 0 for an isotropic
                       smooth distribution).  Detects streams (shared velocity directions across a shell)
                       and bulk flows (l = 1).
  R_v                  bulk-flow power in cells: mean over 4^3 cells (cube of half-side r50, n >= 8) of
                       n |<w>_cell - <w>|^2 / (3 var_cell); about 1 for Poisson noise.  Detects coherent
                       flows, including gate-only transverse-velocity-dipole modes.
  b/a, c/a             axis ratios of the inertia tensor inside r50 (bar or lopsided modes)
  D_e                  rms change of the per-particle mean-field energy e_i = w_i^2/2 + phi_i since the
                       end of the ramp, in units of |<e>|: a relaxation measure (smooth static potential
                       conserves e_i; two-body relaxation scales as 1/N).
Aggregation: mean and standard error over seeds for each (reading, eps, r_g, N).
"""
import ast
import glob
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(12345)


def centre(x, it=8):
    c = np.median(x, axis=0)
    rad = np.percentile(np.linalg.norm(x - c, axis=1), 70)
    for _ in range(it):
        sel = np.linalg.norm(x - c, axis=1) < rad
        c = x[sel].mean(axis=0)
        rad *= 0.85
        if sel.sum() < 200:
            break
    return c


def reassign(x, w, shell=100):
    """Velocities reassigned within radial shells keeping v_r and |v_t| of a random donor."""
    r = np.linalg.norm(x, axis=1)
    rh = x / r[:, None]
    vr = np.sum(w * rh, axis=1)
    vt = np.linalg.norm(w - vr[:, None] * rh, axis=1)
    order = np.argsort(r)
    wn = np.empty_like(w)
    for s in range(0, len(r), shell):
        idx = order[s:s + shell]
        donors = rng.permutation(idx)
        # random tangent direction at the recipient
        a = rng.normal(size=(len(idx), 3))
        a -= np.sum(a * rh[idx], axis=1)[:, None] * rh[idx]
        a /= np.linalg.norm(a, axis=1)[:, None]
        wn[idx] = vr[donors][:, None] * rh[idx] + vt[donors][:, None] * a
    return wn


def pair_counts(x, w, d, us):
    n = len(x)
    cnt_close = 0
    cnt_u = np.zeros(len(us))
    for i0 in range(0, n, 400):
        xi = x[i0:i0 + 400]
        dx = np.linalg.norm(xi[:, None, :] - x[None, :, :], axis=2)
        jj = np.arange(n)[None, :] > (np.arange(i0, i0 + len(xi))[:, None])
        close = (dx < d) & jj
        ii, kk = np.nonzero(close)
        cnt_close += len(ii)
        dw = np.linalg.norm(w[i0 + ii] - w[kk], axis=1)
        for q, u in enumerate(us):
            cnt_u[q] += np.sum(dw < u)
    return cnt_close, cnt_u


def Xi(x, w, d, us, nshuf=4):
    nc, nu = pair_counts(x, w, d, us)
    ref = np.zeros(len(us))
    for _ in range(nshuf):
        _, ru = pair_counts(x, reassign(x, w), d, us)
        ref += ru / nshuf
    return nu / np.maximum(ref, 1e-30) - 1.0, nc, nu


def S_l(x, w, lmax=4, shell=200):
    r = np.linalg.norm(x, axis=1)
    order = np.argsort(r)
    out = []
    for s in range(0, len(r) - shell + 1, shell):
        idx = order[s:s + shell]
        u = w[idx] / np.linalg.norm(w[idx], axis=1)[:, None]
        c = np.clip(u @ u.T, -1, 1)
        row = []
        for l in range(1, lmax + 1):
            coef = np.zeros(l + 1); coef[l] = 1.0
            row.append(np.polynomial.legendre.legval(c, coef).sum() / shell - 1.0)
        out.append(row)
    return np.mean(out, axis=0)


def R_v(x, w, L, ncell=4):
    edges = np.linspace(-L, L, ncell + 1)
    ix = np.digitize(x, edges) - 1
    ok = np.all((ix >= 0) & (ix < ncell), axis=1)
    key = ix[ok, 0] * ncell * ncell + ix[ok, 1] * ncell + ix[ok, 2]
    wv = w[ok]
    wmean = w.mean(axis=0)
    vals = []
    for k in np.unique(key):
        sel = key == k
        n = sel.sum()
        if n < 8:
            continue
        wc = wv[sel]
        var = np.mean(np.var(wc, axis=0, ddof=1))
        vals.append(n * np.sum((wc.mean(axis=0) - wmean) ** 2) / (3 * var))
    return np.mean(vals) if vals else np.nan


def axis_ratios(x, r50):
    sel = np.linalg.norm(x, axis=1) < r50
    I = x[sel].T @ x[sel] / sel.sum()
    ev = np.sort(np.linalg.eigvalsh(I))[::-1]
    return np.sqrt(ev[1] / ev[0]), np.sqrt(ev[2] / ev[0])


def analyse(fn, times=None):
    d = np.load(fn)
    meta = eval(str(d['meta'][0]), {'np': np})
    X, Wc, V, PH, log = d['x'].astype(float), d['w'].astype(float), d['v'].astype(float), d['phi'].astype(float), d['log']
    vs = float(meta['vstar'])
    tt = log[:, 0]
    k_ramp = int(np.argmin(np.abs(tt - meta['T_ramp'])))
    e_ref = 0.5 * np.sum(Wc[k_ramp] ** 2, axis=1) + PH[k_ramp]
    rows = []
    ks = range(len(tt)) if times is None else [int(np.argmin(np.abs(tt - t))) for t in times]
    for k in ks:
        x = X[k]; w = Wc[k]; v = V[k]
        c = centre(x)
        x = x - c
        r = np.linalg.norm(x, axis=1)
        rs = np.sort(r)
        n = len(r)
        r10, r50, r90 = rs[int(0.1 * n)], rs[int(0.5 * n)], rs[int(0.9 * n)]
        core = r < rs[int(0.25 * n)]
        wcm = w[core] - w[core].mean(axis=0)
        vcm = v[core] - v[core].mean(axis=0)
        sig_c = np.sqrt(np.mean(wcm**2)); sig_k = np.sqrt(np.mean(vcm**2))
        comp = wcm.ravel()
        kurt = np.mean(comp**4) / np.mean(comp**2) ** 2
        dd = 0.25 * r50
        xi_w, nclose, _ = Xi(x, w, dd, [vs, 0.5 * vs])
        xi_v, _, _ = Xi(x, v, dd, [vs])
        sl = S_l(x, w)
        rv = R_v(x, w, r50)
        ba, ca = axis_ratios(x, r50)
        e_now = 0.5 * np.sum(w**2, axis=1) + PH[k]
        De = np.sqrt(np.mean((e_now - e_ref) ** 2)) / abs(np.mean(e_ref)) if tt[k] >= meta['T_ramp'] - 1e-9 else np.nan
        rows.append(dict(t=tt[k], r10=r10, r50=r50, r90=r90, sig_c=sig_c, sig_k=sig_k, r_c=sig_c / vs, kurt=kurt,
                         xi_u1=xi_w[0], xi_u05=xi_w[1], xi_v=xi_v[0], npair=nclose, S1=sl[0], S2=sl[1], S3=sl[2], S4=sl[3],
                         Rv=rv, ba=ba, ca=ca, De=De))
    return meta, rows


TIMES = [0, 5, 10, 15] + list(range(20, 41, 2))


def load_all_caches():
    import pickle
    out = {}
    legacy = os.path.join(HERE, "diag_cache.pkl")
    if os.path.exists(legacy):
        for (name, mt), v in pickle.load(open(legacy, "rb")).items():
            out[name] = v
    for fn in glob.glob(os.path.join(HERE, "diag_cache", "*.pkl")):
        name, v = pickle.load(open(fn, "rb"))
        out[name] = v
    return out


if __name__ == "__main__":
    import pickle
    if len(sys.argv) > 2 and sys.argv[1] == "--one":
        fn = sys.argv[2]
        os.makedirs(os.path.join(HERE, "diag_cache"), exist_ok=True)
        meta, rows = analyse(fn, times=TIMES)
        pickle.dump((os.path.basename(fn), (meta, rows)), open(os.path.join(HERE, "diag_cache", os.path.basename(fn) + ".pkl"), "wb"))
        print("analysed", os.path.basename(fn), flush=True)
        sys.exit(0)
    cache = load_all_caches()
    groups = {}
    for name, (meta, rows) in cache.items():
        g = (meta['reading'], meta['eps'], meta['r_g'] if meta['eps'] != 0 else 0.0, meta['N'])
        groups.setdefault(g, []).append(rows)
    cols = ['r50', 'r10', 'sig_c', 'sig_k', 'r_c', 'kurt', 'xi_u1', 'xi_u05', 'xi_v', 'S1', 'S2', 'S3', 'S4', 'Rv', 'ba', 'ca', 'De']
    tsel = [0, 10, 15, 20, 30, 40]
    for g in sorted(groups):
        runs = groups[g]
        print(f"\n=== reading {g[0]}, eps = {g[1]:g}, r_g = {g[2]:g}, N = {g[3]}, seeds = {len(runs)}; "
              f"columns: mean (s.e. over seeds) ===")
        print("   t " + " ".join(f"{c:>13s}" for c in cols))
        for t in tsel:
            vals = []
            for c in cols:
                arr = []
                for rows in runs:
                    rr = [row for row in rows if abs(row['t'] - t) < 1e-6]
                    if rr:
                        arr.append(rr[0][c])
                arr = np.array(arr, float)
                if len(arr) == 0 or np.all(np.isnan(arr)):
                    vals.append(f"{'-':>13s}")
                else:
                    nn = np.sum(~np.isnan(arr))
                    m = np.nanmean(arr); se = np.nanstd(arr, ddof=1) / np.sqrt(nn) if nn > 1 else 0
                    vals.append(f"{m:7.3f}({se:5.3f})")
            print(f"{t:4d} " + " ".join(vals))
        post = {}
        for c in ['xi_u1', 'xi_u05', 'xi_v', 'S1', 'S2', 'S3', 'S4', 'Rv', 'kurt', 'r_c', 'sig_c', 'sig_k', 'r50', 'De']:
            per = []
            for rows in runs:
                a = [row[c] for row in rows if 20 <= row['t'] <= 40 and abs(row['t'] - round(row['t'] / 2) * 2) < 1e-6]
                per.append(np.nanmean(a))
            per = np.array(per)
            post[c] = (per.mean(), per.std(ddof=1) / np.sqrt(len(per)) if len(per) > 1 else 0.0)
        print("   post-ramp average over t = 20, 22, ..., 40: " + "; ".join(f"{c} = {m:+.4f} +- {s:.4f}" for c, (m, s) in post.items()))
        for c in ('xi_u05', 'S2'):
            sl = []
            for rows in runs:
                t_ = np.array([row['t'] for row in rows if row['t'] >= 15]); y_ = np.array([row[c] for row in rows if row['t'] >= 15])
                sl.append(np.polyfit(t_, y_, 1)[0])
            sl = np.array(sl)
            print(f"   d({c})/dt over t >= 15: {sl.mean():+.5f} +- {sl.std(ddof=1)/np.sqrt(len(sl)) if len(sl)>1 else 0:.5f} per unit time")
