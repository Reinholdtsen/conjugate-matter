"""Self-consistent isotropic equilibrium of a cored chi halo with the gated long-range term
(round 3, label "corner").

Model [P, hypothetical; not in the record]: pair energy per unit masses
    U = -G m m' [1 + eps W(|w - w'|/v*)] / |x - x'|,  W(s) = exp(-s^2/2),
read as a Hamiltonian with the gate on the canonical momentum per mass w = p/m.
Mean-field one-particle energy (per unit mass):
    e(r, w) = w^2/2 + Phi(r) + Phig(r, |w|),
    Phig(r, w) = -eps G Int d^3x' d^3w' W(|w-w'|/v*) f(x', w') / |x - x'|.
Distribution function: f = A (-e)_+^(7/2)  (the Plummer family; eps = 0 gives the Plummer sphere).
Isotropy reduces the gate to the angle-averaged kernel
    K(w, w') = exp(-(w-w')^2/(2v*^2)) (1 - exp(-2ww'/v*^2)) / (2ww'/v*^2),
and the spatial part to the spherical shell theorem, so the problem lives on a 2D (r, |w|) grid.
Units: G = M = 1.  The gate scale is tied to the gravitational velocity scale of the model,
v* = sigma_g / r_g, sigma_g^2 = -Phi_grav(0)/6 (for eps = 0 this is the Plummer central 1D
dispersion; it is the scale that stars embedded in the halo would show, since stars feel only G).
With v* tied to the potential the problem is scale-free, so the half-mass radius is pinned to that
of the a = 1 Plummer sphere, r_h = 1.3048, at every iteration (exact symmetry: x -> lam x,
w -> w/sqrt(lam), potentials -> potentials/lam, v* -> v*/sqrt(lam)).
Reported: sigma_c (central canonical 1D dispersion), sigma_kin (central 1D dispersion of xdot, which
differs from w by the anomalous velocity dPhig/dw), r_c = sigma_c/v*.

Anchors (independent of this code):
  * eps = 0 must reproduce the Plummer sphere rho = (3/4pi)(1+r^2)^(-5/2), Phi = -(1+r^2)^(-1/2)
    (textbook [T]) after rescaling to r_h = 1.3048 = (2^(2/3)-1)^(-1/2) [T].
  * Generalized virial theorem for H = sum p^2/2m + sum U(x_ij, p_ij), U homogeneous of degree -1
    in x [D; derivation: d/dt sum x.p = 0 in a steady state]: 2K + V_s + W_grav + W_gate = 0.
"""
import numpy as np

PL_RH = (2.0 ** (2.0 / 3.0) - 1.0) ** -0.5   # Plummer half-mass radius for a = 1 [T]


def grids(nr=420, rmax=80.0, s=0.25, nw=360, wmax=None):
    u = np.linspace(0.0, np.arcsinh(rmax / s), nr)
    r = s * np.sinh(u)
    w = np.linspace(0.0, wmax, nw)
    return r, w


def trap_weights(x):
    wts = np.zeros_like(x)
    dx = np.diff(x)
    wts[:-1] += dx / 2
    wts[1:] += dx / 2
    return wts


def cumtrap(y, x, axis=0):
    """cumulative trapezoid along axis 0 (y may be 2D)."""
    dx = np.diff(x)
    if y.ndim == 1:
        c = np.concatenate([[0.0], np.cumsum(0.5 * (y[1:] + y[:-1]) * dx)])
    else:
        c = np.concatenate([np.zeros((1,) + y.shape[1:]),
                            np.cumsum(0.5 * (y[1:] + y[:-1]) * dx[:, None], axis=0)], axis=0)
    return c


def shell_potential(rho, r):
    """Phi(r) = -4 pi G [ (1/r) Int_0^r rho r'^2 dr' + Int_r^inf rho r' dr' ]  (G = 1),
    rho may be (nr,) or (nr, ncol)."""
    if rho.ndim == 1:
        inner = cumtrap(rho * r**2, r)
        outer_c = cumtrap(rho * r, r)
        outer = outer_c[-1] - outer_c
        with np.errstate(divide='ignore', invalid='ignore'):
            t1 = np.where(r > 0, inner / np.where(r > 0, r, 1.0), 0.0)
        return -4 * np.pi * (t1 + outer)
    inner = cumtrap(rho * (r**2)[:, None], r)
    outer_c = cumtrap(rho * r[:, None], r)
    outer = outer_c[-1][None, :] - outer_c
    rr = np.where(r > 0, r, 1.0)[:, None]
    t1 = np.where(r[:, None] > 0, inner / rr, 0.0)
    return -4 * np.pi * (t1 + outer)


def gate_kernel(w, vs):
    a = np.outer(w, w) / vs**2
    d2 = (w[:, None] - w[None, :]) ** 2 / (2 * vs**2)
    with np.errstate(divide='ignore', invalid='ignore'):
        fac = np.where(a > 1e-10, -np.expm1(-2 * a) / (2 * np.where(a > 1e-10, a, 1.0)), 1.0 - a)
    return np.exp(-d2) * fac


def _interp_weights(xq, x):
    k = np.clip(np.searchsorted(x, xq) - 1, 0, len(x) - 2)
    t = np.clip((xq - x[k]) / (x[k + 1] - x[k]), 0.0, None)
    return k, t


def _rescale(r, w, Phi, Phig, lam):
    """Apply the scaling symmetry x -> lam x, w -> w/sqrt(lam), potentials -> potentials/lam,
    sampled back on the fixed grids (Kepler extrapolation beyond r_max, zero gate beyond w_max)."""
    rq = r / lam
    k, t = _interp_weights(rq, r)
    out_r = rq > r[-1]
    Pn = ((1 - t) * Phi[k] + t * Phi[k + 1])
    Pn = np.where(out_r, Phi[-1] * r[-1] / np.where(rq > 0, rq, 1.0), Pn) / lam
    G1 = (1 - t)[:, None] * Phig[k] + t[:, None] * Phig[k + 1]
    G1 = np.where(out_r[:, None], Phig[-1][None, :] * r[-1] / np.where(rq > 0, rq, 1.0)[:, None], G1)
    wq = w * np.sqrt(lam)
    kw, tw = _interp_weights(wq, w)
    out_w = wq > w[-1]
    G2 = (1 - tw)[None, :] * G1[:, kw] + tw[None, :] * G1[:, kw + 1]
    G2 = np.where(out_w[None, :], 0.0, G2) / lam
    return Pn, G2


def solve(eps, r_g, n_index=3.5, nr=420, nw=360, rmax=80.0, alpha=0.35, maxit=4000, tol=1e-9,
          verbose=False):
    """Self-consistent model for given eps and r_g = sigma_g / v*, where sigma_g^2 = -Phi_grav(0)/6
    (the gravitational velocity scale; = the Plummer central 1D dispersion when eps = 0).
    The half-mass radius is pinned to PL_RH every iteration (scaling symmetry), G = M = 1."""
    wmax = 1.25 * np.sqrt(2.0 * (1.0 + eps))
    r, w = grids(nr=nr, rmax=rmax, nw=nw, wmax=wmax)
    wr = trap_weights(r)
    ww = trap_weights(w)
    Phi = -1.0 / np.sqrt(1.0 + r**2)
    Phig = np.zeros((nr, nw))
    hist = []
    for it in range(maxit):
        e = 0.5 * w[None, :] ** 2 + Phi[:, None] + Phig
        f = np.clip(-e, 0.0, None) ** n_index
        rho = 4 * np.pi * (f * (w**2 * ww)[None, :]).sum(axis=1)
        M = 4 * np.pi * np.sum(rho * r**2 * wr)
        f /= M
        rho /= M
        vs = np.sqrt(-Phi[0] / 6.0) / r_g
        Phi_new = shell_potential(rho, r)
        if eps != 0.0:
            K = gate_kernel(w, vs)
            h = 4 * np.pi * (f * (w**2 * ww)[None, :]) @ K.T     # h[r, w] = Int K(w,w') f(r,w') d^3w'
            Phig_new = eps * shell_potential(h, r)
        else:
            Phig_new = np.zeros_like(Phig)
        dP = np.max(np.abs(Phi_new - Phi)); dG = np.max(np.abs(Phig_new - Phig))
        Phi = (1 - alpha) * Phi + alpha * Phi_new
        Phig = (1 - alpha) * Phig + alpha * Phig_new
        # pin the half-mass radius (scaling symmetry; v* is tied to Phi(0), so this is exact)
        Mr = 4 * np.pi * cumtrap(rho * r**2, r)
        rh = np.interp(0.5, Mr / Mr[-1], r)
        lam = PL_RH / rh
        if abs(lam - 1) > 1e-12:
            Phi, Phig = _rescale(r, w, Phi, Phig, lam)
        hist.append((dP, dG, lam))
        if verbose and it % 200 == 0:
            print(f"   it {it}: dPhi {dP:.2e} dPhig {dG:.2e} lam-1 {lam-1:.2e} vs {vs:.5f}")
        if max(dP, dG) < tol and abs(lam - 1) < tol:
            break
    e = 0.5 * w[None, :] ** 2 + Phi[:, None] + Phig
    f = np.clip(-e, 0.0, None) ** n_index
    rho = 4 * np.pi * (f * (w**2 * ww)[None, :]).sum(axis=1)
    M = 4 * np.pi * np.sum(rho * r**2 * wr)
    f /= M; rho /= M
    vs = np.sqrt(-Phi[0] / 6.0) / r_g
    return dict(eps=eps, r_g=r_g, iters=it + 1, conv=hist[-1], r=r, w=w, Phi=Phi, Phig=Phig,
                f=f, rho=rho, vstar=vs, n_index=n_index)


def properties(m):
    r, w, f, Phi, Phig = m['r'], m['w'], m['f'], m['Phi'], m['Phig']
    wr = trap_weights(r); ww = trap_weights(w)
    rho = 4 * np.pi * (f * (w**2 * ww)[None, :]).sum(axis=1)
    Mtot = 4 * np.pi * np.sum(rho * r**2 * wr)
    Mr = 4 * np.pi * cumtrap(rho * r**2, r)
    rh = np.interp(0.5, Mr / Mr[-1], r)
    # canonical and kinematic central dispersions
    dPg = np.gradient(Phig, w, axis=1)
    vkin = w[None, :] + dPg                       # |xdot| along w-hat
    sig_c = np.sqrt(np.sum(f[0] * w**4 * ww) / (3 * np.sum(f[0] * w**2 * ww)))
    sig_k = np.sqrt(np.sum(f[0] * vkin[0]**2 * w**2 * ww) / (3 * np.sum(f[0] * w**2 * ww)))
    kurt_c = 1.8 * np.sum(f[0] * w**6 * ww) * np.sum(f[0] * w**2 * ww) / np.sum(f[0] * w**4 * ww) ** 2
    # mass-weighted global dispersions
    K = 0.5 * np.sum(4 * np.pi * r**2 * wr * (4 * np.pi * (f * (w**4 * ww)[None, :]).sum(axis=1)))
    Wgrav = 0.5 * np.sum(4 * np.pi * r**2 * wr * rho * Phi)
    Wgate = 0.5 * np.sum(4 * np.pi * r**2 * wr * (4 * np.pi * (f * Phig * (w**2 * ww)[None, :]).sum(axis=1)))
    Vs = np.sum(4 * np.pi * r**2 * wr * (4 * np.pi * (f * dPg * (w**3 * ww)[None, :]).sum(axis=1)))
    # central gate depth relative to sigma_c^2 and the central anomalous speed-up of a w = sigma_c particle
    iw = np.searchsorted(w, sig_c)
    speedup = vkin[0, iw] / w[iw]
    return dict(Mtot=Mtot, rh=rh, rho0=rho[0], sig_c=sig_c, sig_k=sig_k, kurt_c=kurt_c,
                K=K, Wgrav=Wgrav, Wgate=Wgate, Vs=Vs, virial=(2 * K + Vs + Wgrav + Wgate) / abs(Wgrav + Wgate),
                gate_depth0=-Phig[0, 0] / sig_c**2, phi0=-Phi[0] / sig_c**2, speedup=speedup,
                vstar=m['vstar'], r_c=sig_c / m['vstar'], sig_g=np.sqrt(-Phi[0] / 6.0))


def sample(m, N, seed):
    """Draw N particles (x, w) from f(r, |w|) with isotropic directions; COM removed."""
    rng = np.random.default_rng(seed)
    r, w, f = m['r'], m['w'], m['f']
    ww = trap_weights(w)
    rho = 4 * np.pi * (f * (w**2 * ww)[None, :]).sum(axis=1)
    Mr = 4 * np.pi * cumtrap(rho * r**2, r)
    Mr /= Mr[-1]
    u = rng.random(N)
    rs = np.interp(u, Mr, r)
    k = np.clip(np.searchsorted(r, rs) - 1, 0, len(r) - 2)
    t = (rs - r[k]) / (r[k + 1] - r[k])
    ws = np.empty(N)
    for i in range(N):
        pdf = ((1 - t[i]) * f[k[i]] + t[i] * f[k[i] + 1]) * w**2
        cdf = cumtrap(pdf, w)
        cdf /= cdf[-1]
        ws[i] = np.interp(rng.random(), cdf, w)

    def iso(n):
        z = rng.uniform(-1, 1, n); ph = rng.uniform(0, 2 * np.pi, n); s = np.sqrt(1 - z**2)
        return np.stack([s * np.cos(ph), s * np.sin(ph), z], axis=1)
    x = rs[:, None] * iso(N)
    v = ws[:, None] * iso(N)
    x -= x.mean(axis=0); v -= v.mean(axis=0)
    return x, v


if __name__ == "__main__":
    import sys
    # Anchor 1: eps = 0 reproduces Plummer
    m0 = solve(0.0, 1.0)
    p0 = properties(m0)
    r = m0['r']
    rho_pl = (3 / (4 * np.pi)) * (1 + r**2) ** -2.5
    phi_pl = -(1 + r**2) ** -0.5
    sel = r < 10
    print(f"Anchor eps=0: iterations {m0['iters']}, final (dPhi, dPhig, lam) = {m0['conv']}")
    print(f"  max |rho/rho_Plummer - 1| (r<10) = {np.max(np.abs(m0['rho'][sel]/rho_pl[sel]-1)):.2e}; "
          f"max |Phi - Phi_Plummer| (r<10) = {np.max(np.abs(m0['Phi'][sel]-phi_pl[sel])):.2e}")
    print(f"  sigma_c = {p0['sig_c']:.5f} (Plummer central 1D dispersion sqrt(1/6) = {np.sqrt(1/6):.5f}); "
          f"r_h = {p0['rh']:.5f} (target {PL_RH:.5f}); virial residual = {p0['virial']:.2e}; "
          f"central 1D kurtosis = {p0['kurt_c']:.4f}")
    # Anchor 2: the canonical Plummer DF normalization from Eddington: F = (24 sqrt2/(7 pi^3)) (-E)^(7/2) for G=M=a=1
    A_tb = 24 * np.sqrt(2) / (7 * np.pi**3)
    e = 0.5 * m0['w'][None, :]**2 + m0['Phi'][:, None]
    A_num = np.median((m0['f'][e < -0.05] / (-e[e < -0.05]) ** 3.5))
    print(f"  DF normalization A: model {A_num:.6f} vs textbook 24 sqrt2/(7 pi^3) = {A_tb:.6f}")
    print()
    print("columns: r_g = sigma_g/v*; v*; sigma_g; sigma_c (canonical); sigma_kin (xdot); r_c = sigma_c/v*; central 1D kurtosis of w;"
          " rho0; -Phig(0,0)/sigma_g^2; speed-up |xdot|/|w| at the centre for |w| = sigma_c; generalized virial residual")
    print(f"{'eps':>5} {'r_g':>5} | {'iters':>5} {'v*':>8} {'sig_g':>8} {'sig_c':>8} {'sig_kin':>8} {'r_c':>6} {'kurt_c':>7} {'rho0':>8} "
          f"{'gate0/sg2':>9} {'speedup':>7} {'virial':>9}")
    import pickle, os
    here = os.path.dirname(os.path.abspath(__file__))
    for eps in (0.0, 1.0, 3.0, 10.0):
        for rt in ((1.0,) if eps == 0 else (0.4, 1.0, 2.0)):
            m = solve(eps, rt)
            p = properties(m)
            print(f"{eps:5.1f} {rt:5.2f} | {m['iters']:5d} {p['vstar']:8.5f} {p['sig_g']:8.5f} {p['sig_c']:8.5f} {p['sig_k']:8.5f} "
                  f"{p['r_c']:6.3f} {p['kurt_c']:7.4f} {p['rho0']:8.5f} {-m['Phig'][0,0]/p['sig_g']**2:9.4f} {p['speedup']:7.4f} "
                  f"{p['virial']:9.2e}   conv {m['conv'][0]:.1e},{m['conv'][1]:.1e},{m['conv'][2]-1:.1e}")
            with open(os.path.join(here, f"model_eps{eps:g}_rt{rt:g}.pkl"), "wb") as fh:
                pickle.dump(m, fh)
