"""Narrow-gate dynamic check (cluster conditions, sigma/v* = 1000/120) where a Gauss-Laguerre
v_perp grid cannot resolve the gate. The m=0 perpendicular kernel is diagonalised NUMERICALLY
on a fine Gauss-Legendre v_perp grid (no Mehler formula used; the closed-form eigenvalues
lambda0^2 q^(2j) are printed only as a cross-check), giving channels chi_j with eigenvalues mu_j
and gravity overlaps a_j = <p_perp^(1/2), chi_j>. In the channel basis (units as dynamic_eig.py):
  omega u_j = kap v_z u_j - (v_z/kap) p_z(v_z) [ a_j Sum_i a_i Int u_i dv_z'
                                                + gt mu_j Int Wz(v_z - v_z') u_j(v_z') dv_z' ]
v_z on a sinh-mapped grid v_z = v0 + alpha sinh(s) (trapezoid in s). Brute-force eigenvalues.
Validation: at MW conditions (r = 155/120) it must reproduce dynamic_eig.py's 0.44211i."""
import numpy as np, sys, time
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-clumping-derivation')
from dynamic_eig import i0e, fmt

def perp_channels(r, J, nperp=300, vmax=7.0):
    vs = 1.0 / r
    x, w = np.polynomial.legendre.leggauss(nperp)
    b = 0.5 * vmax * (x + 1); w = 0.5 * vmax * w
    om = 2 * np.pi * b * w
    pp = np.exp(-b**2 / 2) / (2 * np.pi)
    X = b[:, None] * b[None, :] / vs**2
    Wp = np.exp(-(b[:, None] - b[None, :])**2 / (2 * vs**2)) * i0e(X)
    S = np.sqrt(om * pp)[:, None] * Wp * np.sqrt(om * pp)[None, :]
    mu, E = np.linalg.eigh(S)
    idx = np.argsort(mu)[::-1][:J]
    mu = mu[idx]; E = E[:, idx]
    a = (np.sqrt(om * pp)) @ E
    return mu, a

def build(kap, gt, r, J=14, v0=0.0, alpha=0.05, ds=0.1, Lz=5.0):
    vs = 1.0 / r
    mu, a = perp_channels(r, J)
    smin = np.arcsinh((-Lz - v0) / alpha); smax = np.arcsinh((Lz - v0) / alpha)
    ns = int(np.ceil((smax - smin) / ds)) + 1
    s = np.linspace(smin, smax, ns); dss = s[1] - s[0]
    vz = v0 + alpha * np.sinh(s); wz = alpha * np.cosh(s) * dss
    pz = np.exp(-vz**2 / 2) / np.sqrt(2 * np.pi)
    Wz = np.exp(-(vz[:, None] - vz[None, :])**2 / (2 * vs**2))
    N = ns * J
    # index (i, j) -> i*J + j
    Lm = np.kron(Wz * wz[None, :], np.diag(gt * mu))
    Lm += np.kron(np.ones((ns, ns)) * wz[None, :], np.outer(a, a))
    Lm *= (-(1.0 / kap) * np.kron(vz * pz, np.ones(J)))[:, None]
    Lm[np.diag_indices(N)] += kap * np.kron(vz, np.ones(J))
    return Lm, ns, mu, a

def run(kap, gt, r, thr=0.01, **kw):
    t0 = time.time()
    Lm, ns, mu, a = build(kap, gt, r, **kw)
    ev = np.linalg.eigvals(Lm); del Lm
    ev = ev[ev.imag > thr]; ev = ev[np.argsort(-ev.imag)]
    return ev, ns, mu, a, time.time() - t0

if __name__ == '__main__':
    which = sys.argv[1]
    if which == 'validate':
        r = 155/120
        mu, a = perp_channels(r, 6)
        A = 0.25; B = r**2/2; C = np.sqrt(A*A + 2*A*B); Aa = A + B + C
        lam0 = np.sqrt(2*A/Aa); q = B/Aa
        print("MW perp channels mu_j:", np.round(mu, 7), " closed lam0^2 q^(2j):", np.round(lam0**2 * q**(2*np.arange(6)), 7))
        print("  sum a_j^2 (J=6) =", round(float((a**2).sum()), 6))
        ev, ns, mu, a, dt = run(np.sqrt(4.9348), 56.14, r, J=8, alpha=0.3, ds=0.08)
        print(f"MW kap^2=4.9348 gt=56.14 channels J=8: {fmt(ev)} [ns={ns}, {dt:.0f}s] (brute force 0.44211i)")
        ev, ns, mu, a, dt = run(np.sqrt(19.7392), 1000.0, r, J=8, alpha=0.3, ds=0.08)
        print(f"MW kap^2=19.7392 gt=1000 channels J=8: {fmt(ev)} [ns={ns}, {dt:.0f}s] (brute force 1.22219i)")
    elif which == 'cluster':
        r = 1000/120
        mu, a = perp_channels(r, 30)
        A = 0.25; B = r**2/2; C = np.sqrt(A*A + 2*A*B); Aa = A + B + C
        lam0 = np.sqrt(2*A/Aa); q = B/Aa
        print("cluster perp mu_j (first 5):", mu[:5], " closed:", lam0**2 * q**(2*np.arange(5)))
        print("cumulative a_j^2 at J=10,14,20,30:", [round(float((a[:J]**2).sum()), 5) for J in [10, 14, 20, 30]])
        k2 = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0966
        gts = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [304.4]
        J = int(sys.argv[4]) if len(sys.argv) > 4 else 14
        for gt in gts:
            ev, ns, mu, a, dt = run(np.sqrt(k2), gt, r, J=J, alpha=0.05, ds=0.1, thr=0.005)
            print(f"cluster kap^2={k2} gt={gt:g} J={J}: {fmt(ev)} [ns={ns}, N={ns*J}, {dt:.0f}s]"); sys.stdout.flush()
