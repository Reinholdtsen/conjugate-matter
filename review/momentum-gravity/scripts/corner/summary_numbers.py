"""Derived numbers for the corner write-up, computed from the per-run diagnostic caches (no hand arithmetic):
kinematic/canonical dispersion ratios, r50 change, differences from the eps = 0 control (N = 2000) with
combined standard errors, relaxation ratios between N = 1000 and N = 2000."""
import numpy as np, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import diagnostics as D
cache = D.load_all_caches()
groups = {}
for name, (meta, rows) in cache.items():
    g = (meta['reading'], meta['eps'], meta['r_g'] if meta['eps'] != 0 else 0.0, meta['N'])
    groups.setdefault(g, []).append(rows)
def post(rows, c):
    return np.nanmean([r[c] for r in rows if 20 <= r['t'] <= 40 and abs(r['t'] - round(r['t'] / 2) * 2) < 1e-6])
def stat(g, c):
    a = np.array([post(rows, c) for rows in groups[g]])
    return a.mean(), a.std(ddof=1) / np.sqrt(len(a))
ctrl = ('H', 0.0, 0.0, 2000)
r50_0 = np.mean([[r['r50'] for r in rows if r['t'] == 0][0] for rows in groups[ctrl]])
print(f"initial r50 (eps=0 runs, t=0) = {r50_0:.4f}")
for g in sorted(groups):
    if g[3] != 2000 or g == ctrl:
        continue
    sc, _ = stat(g, 'sig_c'); sk, _ = stat(g, 'sig_k'); r50, _ = stat(g, 'r50')
    out = [f"{g[0]} eps={g[1]:g} r_g={g[2]:g}: sig_k/sig_c = {sk/sc:.2f}; r50/r50(t=0) = {r50/r50_0:.3f}"]
    for c in ('xi_u1', 'xi_u05', 'S1', 'S2', 'Rv'):
        m, s = stat(g, c); m0, s0 = stat(ctrl, c)
        out.append(f"d{c} = {m-m0:+.4f} +- {np.hypot(s, s0):.4f}")
    print("; ".join(out))
for e in (0.0, 10.0):
    g1 = ('H', e, 0.0 if e == 0 else 1.0, 1000); g2 = ('H', e, 0.0 if e == 0 else 1.0, 2000)
    a, _ = stat(g1, 'De'); b, _ = stat(g2, 'De')
    print(f"eps={e:g}: D_e(N=1000)/D_e(N=2000) = {a/b:.3f} (sqrt2 = {np.sqrt(2):.3f})")
a, _ = stat(('H', 10.0, 1.0, 2000), 'De'); b, _ = stat(ctrl, 'De')
print(f"(D_e(eps=10, r_g=1)/D_e(eps=0))^2 at N=2000 = {(a/b)**2:.2f}")
a, _ = stat(('F', 3.0, 1.0, 2000), 'De')
print(f"(D_e(F, eps=3)/D_e(eps=0))^2 at N=2000 = {(a/b)**2:.2f}")
