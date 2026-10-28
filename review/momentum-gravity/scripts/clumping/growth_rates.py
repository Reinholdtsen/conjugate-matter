"""Growth rates of the homogeneous long-range gated + gravity problem (Gaussian gate only).
Units: sigma = 1, k_J = sqrt(4 pi G rho)/sigma = 1, time unit t_ff = 1/sqrt(4 pi G rho).
Eigen-equation:  de(v) = kappa^-2 Int [1 + gt W(v-v')] p0(v') zeta(v'_z) de(v') d^3v',
                 zeta(u) = kappa u/(kappa u - w),  kappa = k/k_J,  w = omega/(k_J sigma)
Gaussian W factorizes over Cartesian axes; perpendicular axes use the exact Mehler eigenbasis
(eigenvalues t0 q^n, overlaps a_n), the axis along k is discretized (Nystrom, composite
Gauss-Legendre with refinement where zeta varies fast).  Gravity-coupled modes satisfy
    D(w) = kappa^2 - sum_N A_N F_z(lambda_N; w) = 0,  lambda_N = (gt/kappa^2) t0^2 q^N,
    F_z(lambda) = <g zeta, (1 - lambda T_z)^-1 1>,  A_N = sum_{n+m=N} a_n^2 a_m^2.
Anchor (independent of this solver): stellar Jeans dispersion relation for gt = 0,
    kappa^2 = 1 - sqrt(pi) xi exp(xi^2) erfc(xi),  xi = Gamma/(sqrt2 kappa)   (w = i Gamma)
"""
import sys, math
import numpy as np
from numpy.polynomial.legendre import leggauss
import mpmath as mp
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from static_threshold import Lam_g_closed, q_closed, top_eigs
from static_combined import hermite_overlaps

class Gated:
    def __init__(self, r, gt, nmax=None, L=9.0, order=8):
        self.r, self.gt, self.L, self.order = r, gt, L, order
        self.vstar = 1.0/r
        self.t0 = (0.5 + r*r + 0.5*math.sqrt(1 + 4*r*r))**-0.5
        self.q = q_closed(r)
        if nmax is None:
            nmax = int(80 + 60*r)
        a = hermite_overlaps(r, nmax)
        c = a*a
        self.A = np.convolve(c, c)[:nmax + 1]
        self.N = np.arange(nmax + 1)
        keep = self.A > 1e-16
        self.A, self.N = self.A[keep], self.N[keep]
        self.sumA = self.A.sum()

    def zgrid(self, kappa, w):
        h = min(0.5, self.vstar)
        L = self.L
        br = set(np.round(np.linspace(-L, L, int(round(2*L/h)) + 1), 13).tolist())
        z0 = (w.real/kappa) if kappa > 0 else 0.0
        d = abs(w.imag)/kappa if kappa > 0 else 1.0
        if abs(z0) < L:
            br.add(z0)
            s = d/4
            while s < h:
                for sg in (1, -1):
                    zz = z0 + sg*s
                    if -L < zz < L: br.add(zz)
                s *= 2
        br = np.array(sorted(br))
        x, wq = leggauss(self.order)
        a, b = br[:-1, None], br[1:, None]
        return (0.5*(b - a)*x + 0.5*(a + b)).ravel(), (0.5*(b - a)*wq).ravel()

    def spectral(self, kappa, w):
        z, W = self.zgrid(kappa, w)
        g = np.exp(-z*z/2)/math.sqrt(2*math.pi)
        zeta = kappa*z/(kappa*z - w)
        col = g*zeta*W
        T = np.exp(-0.5*(self.r*(z[:, None] - z[None, :]))**2)*col[None, :]
        tau, V = np.linalg.eig(T)
        b = np.linalg.solve(V, np.ones_like(z, dtype=complex))
        u = col @ V
        return tau, u*b

    def D(self, kappa, w, return_parts=False):
        tau, ub = self.spectral(kappa, w)
        lam = (self.gt/kappa**2)*self.t0**2*self.q**self.N
        F = np.array([np.sum(ub/(1 - l*tau)) for l in lam])
        Dv = kappa**2 - np.sum(self.A*F)
        if return_parts:
            return Dv, tau, lam
        return Dv

def jeans_closed(kappa):
    """purely growing root of kappa^2 = 1 - sqrt(pi) xi e^{xi^2} erfc(xi), xi = Gamma/(sqrt2 kappa)"""
    if kappa >= 1: return 0.0
    f = lambda xi: 1 - mp.sqrt(mp.pi)*xi*mp.exp(xi**2)*mp.erfc(xi) - kappa**2
    xi = mp.findroot(f, (mp.mpf('1e-12'), mp.mpf(10000)), solver='bisect')
    return float(xi*math.sqrt(2)*kappa)

def growth_rate(model, kappa, Ghi=4.0, Glo=1e-5, nscan=60):
    """largest Gamma > 0 with D(i Gamma) = 0 (purely growing mode); 0 if none above Glo"""
    Gs = np.geomspace(Ghi, Glo, nscan)
    vals = [model.D(kappa, 1j*G).real for G in Gs]
    for i in range(len(Gs) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            a, b, fa, fb = Gs[i], Gs[i + 1], vals[i], vals[i + 1]
            for _ in range(60):
                m = math.sqrt(a*b)
                fm = model.D(kappa, 1j*m).real
                if np.sign(fm) == np.sign(fa): a, fa = m, fm
                else: b, fb = m, fm
                if a/b - 1 < 1e-10: break
            m = math.sqrt(a*b)
            Dm = model.D(kappa, 1j*m)
            # reject poles: at a true root |D| is small compared with neighbouring values
            scale = max(abs(vals[i]), abs(vals[i + 1]))
            if abs(Dm) < 1e-6*max(1.0, scale) or abs(Dm) < 1e-8:
                return m, abs(Dm)
            else:
                continue
    return 0.0, None

if __name__ == '__main__':
    print("=== 1. Anchor: gt = 0 (Jeans) solver vs closed-form stellar Jeans relation ===")
    m0 = Gated(1.2917, 0.0)
    print("sum A_N =", m0.sumA)
    for kappa in [0.2, 0.5, 0.8, 0.95]:
        G_num, res = growth_rate(m0, kappa)
        G_cf = jeans_closed(kappa)
        print(f"kappa={kappa}: Gamma solver={G_num:.8f}  closed form={G_cf:.8f}  |D|={res}")
    print("kappa->0 limit of the closed form (free-fall rate): Gamma(0.01) =", jeans_closed(0.01))

    print("\n=== 2. Static limit of the dynamic solver vs radial Nystrom Lambda_0 ===")
    for r, gt in [(1.2917, 10.0), (0.25, 1.0), (4.0, 1000.0)]:
        L0 = top_eigs(r, gt, 0, nev=1)[0][0]
        m = Gated(r, gt)
        print(f"r={r}, gt={gt}: Nystrom Lambda_0 = {L0:.8f}")
        for frac in [0.9, 0.99, 0.999]:
            k2 = frac*L0
            G, res = growth_rate(m, math.sqrt(k2))
            print(f"   kappa^2 = {frac}*Lambda_0: Gamma = {G:.6e}  Gamma/(1-frac) = {G/(1-frac):.4f}  |D|={res}")
        G, res = growth_rate(m, math.sqrt(1.001*L0))
        print(f"   kappa^2 = 1.001*Lambda_0 (stable side): Gamma = {G}")
