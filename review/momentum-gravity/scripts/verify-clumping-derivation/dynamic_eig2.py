"""Extension of dynamic_eig.py: (i) a sinh-mapped v_z grid, v_z = v0 + alpha*sinh(s) with s
uniform, which keeps the trapezoid rule's exponential convergence while resolving a
resonance at v_z ~ v0 (needed for slowly growing modes); (ii) scans in gate strength for the
fastest unstable mode at fixed k, MW conditions (sigma/v* = 155/120).
Same operator and units as dynamic_eig.py (m = 0 sector)."""
import numpy as np, sys, time
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-clumping-derivation')
from dynamic_eig import i0e, fmt

def build_mapped(kap, gt, r, v0=0.0, alpha=0.3, ds=0.04, Lz=5.5, npp=10):
    vs = 1.0 / r
    smin = np.arcsinh((-Lz - v0) / alpha); smax = np.arcsinh((Lz - v0) / alpha)
    ns = int(np.ceil((smax - smin) / ds)) + 1
    s = np.linspace(smin, smax, ns); dss = s[1] - s[0]
    vz = v0 + alpha * np.sinh(s); wz = alpha * np.cosh(s) * dss
    t, wgl = np.polynomial.laguerre.laggauss(npp)
    vp = np.sqrt(2 * t)
    pz = np.exp(-vz**2 / 2) / np.sqrt(2 * np.pi)
    Wz = np.exp(-(vz[:, None] - vz[None, :])**2 / (2 * vs**2))
    x = vp[:, None] * vp[None, :] / vs**2
    Wp = np.exp(-(vp[:, None] - vp[None, :])**2 / (2 * vs**2)) * i0e(x)
    N = ns * npp
    Lm = np.kron(Wz, Wp); Lm *= gt; Lm += 1.0
    wb = np.kron(wz, wgl); lhs = np.kron(vz * pz, np.ones(npp))
    Lm *= wb[None, :]; Lm *= (-(1.0 / kap) * lhs)[:, None]
    Lm[np.diag_indices(N)] += kap * np.kron(vz, np.ones(npp))
    return Lm, ns

def unstable_mapped(kap, gt, r, thr=0.01, **kw):
    t0 = time.time()
    Lm, ns = build_mapped(kap, gt, r, **kw)
    ev = np.linalg.eigvals(Lm); del Lm
    ev = ev[ev.imag > thr]; ev = ev[np.argsort(-ev.imag)]
    return ev, ns, time.time() - t0

if __name__ == '__main__':
    which = sys.argv[1]
    r = 155/120
    if which == 'trav':
        k2 = 19.7392; kap = np.sqrt(k2)
        # check grid convergence on a known purely growing case first
        ev, ns, dt = unstable_mapped(kap, 272.0, r, v0=0.0, alpha=0.4, ds=0.05)
        print(f"kap^2={k2} gt=272 mapped(v0=0): {fmt(ev)} [ns={ns}, {dt:.0f}s]  (uniform-grid result 0.46906i)")
        for gt in [280.7, 283.0, 290.0]:
            ev, ns, dt = unstable_mapped(kap, gt, r, v0=0.0, alpha=0.15, ds=0.05)
            print(f"kap^2={k2} gt={gt} mapped(v0=0, alpha=0.15): {fmt(ev)} [ns={ns}, {dt:.0f}s]  (agent: 0.1597i at 280.7; none at 283, 290)")
            sys.stdout.flush()
        for gt in [320.0]:
            for a, d in [(0.3, 0.05), (0.2, 0.04)]:
                ev, ns, dt = unstable_mapped(kap, gt, r, v0=0.249, alpha=a, ds=d)
                print(f"kap^2={k2} gt={gt} mapped(v0=0.249, alpha={a}, ds={d}): {fmt(ev)} [ns={ns}, {dt:.0f}s]  (agent: +-1.1059+0.1743i)")
                sys.stdout.flush()
    elif which == 'scan':
        for k2 in [4.9348, 19.7392]:
            kap = np.sqrt(k2)
            for gt in [100., 300., 1000., 3000., 1e4, 3e4]:
                ev, ns, dt = unstable_mapped(kap, gt, r, v0=0.0, alpha=1.0, ds=0.05, Lz=5.0, npp=10)
                print(f"kap^2={k2} gt={gt:g}: unstable (Im>0.01) {fmt(ev)} [ns={ns}, {dt:.0f}s]")
                sys.stdout.flush()
