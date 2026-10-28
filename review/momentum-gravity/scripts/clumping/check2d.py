"""Independent check of the growth-rate solver: direct 2D Nystrom in (v_perp, v_z), azimuthal sector m = 0,
no Cartesian factorization.  Gaussian gate W = exp(-r^2 |v-v'|^2/2) (sigma = 1, v* = 1/r).
Azimuthal average: Wbar = exp(-r^2 dz^2/2) exp(-r^2 (vp - vp')^2/2) [e^{-a} I0(a)], a = r^2 vp vp'.
v_perp: Gauss-Laguerre in s = vp^2/2 (weight e^{-s}); v_z: composite Gauss-Legendre with refinement at 0.
Eigen-equation: de_i = kappa^-2 sum_j [1 + gt Wbar_ij] c_j de_j,  c_j = (2pi)^-1/2 e^{-z_j^2/2} wL_j wz_j zeta(z_j).
For w = i Gamma, det(kappa^2 - M) is real (parity z -> -z maps M to its conjugate); its sign changes in Gamma
mark eigenvalue crossings of all m = 0 modes.  Also reports the decoupled-block growth rates of the
factorized solver (zeros of det(1 - lambda_N T_z)) for comparison."""
import sys, math, time
import numpy as np
from numpy.polynomial.laguerre import laggauss
from numpy.polynomial.legendre import leggauss
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from static_threshold import top_eigs

def zgrid(Gamma, kappa, L=7.0, h=0.35, order=6):
    br = set(np.round(np.linspace(-L, L, int(round(2*L/h)) + 1), 12).tolist())
    s = Gamma/kappa/4
    while s < h:
        br.add(s); br.add(-s); s *= 2
    br.add(0.0)
    br = np.array(sorted(br))
    x, w = leggauss(order)
    a, b = br[:-1, None], br[1:, None]
    return (0.5*(b - a)*x + 0.5*(a + b)).ravel(), (0.5*(b - a)*w).ravel()

def build(r, gt, kappa, Gamma, nperp=20, **zk):
    s, wL = laggauss(nperp)
    vp = np.sqrt(2*s)
    z, wz = zgrid(Gamma, kappa, **zk)
    VP = np.repeat(vp, len(z)); WL = np.repeat(wL, len(z))
    Z = np.tile(z, len(vp)); WZ = np.tile(wz, len(vp))
    zeta = kappa*Z/(kappa*Z - 1j*Gamma)
    c = (2*np.pi)**-0.5*np.exp(-Z**2/2)*WL*WZ*zeta
    a = r*r*np.outer(VP, VP)
    Wb = np.exp(-0.5*(r*(Z[:, None] - Z[None, :]))**2 - 0.5*(r*(VP[:, None] - VP[None, :]))**2)*np.exp(-a)*np.i0(a)
    M = (1.0 + gt*Wb)*c[None, :]
    return M

def detsign(r, gt, kappa, Gamma, **kw):
    M = build(r, gt, kappa, Gamma, **kw)
    sgn, ld = np.linalg.slogdet(kappa**2*np.eye(M.shape[0]) - M)
    return sgn.real, abs(sgn.imag), M.shape[0]

def top_root_2d(r, gt, kappa, Gs, **kw):
    vals = []
    for G in Gs:
        sg, im, n = detsign(r, gt, kappa, G, **kw)
        vals.append(sg)
    roots = []
    for i in range(len(Gs) - 1):
        if vals[i] != vals[i + 1]:
            a, b, fa = Gs[i], Gs[i + 1], vals[i]
            for _ in range(25):
                m = math.sqrt(a*b); fm = detsign(r, gt, kappa, m, **kw)[0]
                if fm == fa: a = m
                else: b = m
            roots.append(math.sqrt(a*b))
    return roots, n

def block_root(model, kappa, N, Gs):
    """largest Gamma with det(1 - lambda_N T_z(i Gamma)) = 0 (pure-gate block N of the factorized solver)"""
    def f(G):
        Dv, tau, lam = model.D(kappa, 1j*G, return_parts=True)
        lN = (model.gt/kappa**2)*model.t0**2*model.q**N
        return np.prod(1 - lN*tau).real
    vals = [f(G) for G in Gs]
    for i in range(len(Gs) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            a, b, fa = Gs[i], Gs[i + 1], vals[i]
            for _ in range(30):
                m = math.sqrt(a*b); fm = f(m)
                if np.sign(fm) == np.sign(fa): a, fa = m, fm
                else: b = m
            return math.sqrt(a*b)
    return 0.0

def static2d(r, gt, nperp=16, h=0.35, order=6, L=7.0):
    s, wL = laggauss(nperp)
    vp = np.sqrt(2*s)
    x, w = leggauss(order)
    br = np.linspace(-L, L, int(round(2*L/h)) + 1)
    a, b = br[:-1, None], br[1:, None]
    z = (0.5*(b - a)*x + 0.5*(a + b)).ravel(); wz = (0.5*(b - a)*w).ravel()
    VP = np.repeat(vp, len(z)); WL = np.repeat(wL, len(z))
    Z = np.tile(z, len(vp)); WZ = np.tile(wz, len(vp))
    c = (2*np.pi)**-0.5*np.exp(-Z**2/2)*WL*WZ
    aa = r*r*np.outer(VP, VP)
    Wb = np.exp(-0.5*(r*(Z[:, None] - Z[None, :]))**2 - 0.5*(r*(VP[:, None] - VP[None, :]))**2)*np.exp(-aa)*np.i0(aa)
    sq = np.sqrt(c)
    S = sq[:, None]*(1.0 + gt*Wb)*sq[None, :]
    return np.linalg.eigvalsh(S)[-1], len(Z)

if __name__ == '__main__':
    r = 1.2917
    print("=== 0. 2D static limit (zeta=1, symmetric) vs radial Nystrom (r=1.2917) ===")
    for gt in [10.0, 281.0]:
        e2, n = static2d(r, gt)
        L0 = top_eigs(r, gt, 0, nev=1)[0][0]
        print(f"gt={gt}: 2D top eigenvalue = {e2:.5f} (n={n})  radial Nystrom Lambda_0 = {L0:.5f}")
    sys.stdout.flush()
    kw = dict(nperp=12, h=0.5)
    print("\n=== 1. Jeans anchor in 2D (gt=0): kappa=0.5 -> closed form Gamma = 0.68720193 ===")
    roots, n = top_root_2d(r, 0.0, 0.5, np.geomspace(3.0, 0.05, 30), **kw)
    print(f"2D roots: {roots} (n={n})")
    sys.stdout.flush()
    print("\n=== 2. Strong coupling, MW r=1.2917 ===")
    for k2, gt in [(4.9348, 56.14), (4.9348, 280.7), (19.7392, 255.0), (19.7392, 1275.0)]:
        t1 = time.time()
        k = math.sqrt(k2)
        Gs = np.geomspace(8.0, 0.05, 40)
        roots, n = top_root_2d(r, gt, k, Gs, **kw)
        model = Gated(r, gt)
        br = [block_root(model, k, N, Gs) for N in (0, 1, 2)]
        print(f"kappa^2={k2}, gt={gt}: 2D m=0 sign-change roots (Gamma, descending) = {[round(x,4) for x in roots]} (n={n}); "
              f"factorized pure-gate block top roots N=0,1,2: {[round(x,4) for x in br]}  ({time.time()-t1:.0f}s)")
        sys.stdout.flush()
