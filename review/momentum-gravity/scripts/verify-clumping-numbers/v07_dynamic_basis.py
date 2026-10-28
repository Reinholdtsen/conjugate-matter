"""Verifier v07: generator-eigenvalue method (as v06) with
 - composite Gauss-Legendre panels in v_z (dense near v_z = 0, where purely growing and slow
   modes have their resonance of width Gamma/kappa), half-space with P_z parity;
 - v_perp represented in the numerically computed eigenbasis of the m-th harmonic of the
   perpendicular gate operator (top Nperp vectors) plus, for m = 0, the exact remainder of the
   gravity vector u_perp (Galerkin; gravity is represented exactly).
Modes e^{-i Omega t}: Omega^2 = eigenvalues of kappa^-2 D (kappa^2 - K_o) D (kappa^2 - K_e).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v06_dynamic_L import Ie

def zpanels(panels):
    zs, ws = [], []
    for (a, b, n) in panels:
        x, w = np.polynomial.legendre.leggauss(n)
        zs.append(0.5 * (b - a) * (x + 1) + a)
        ws.append(0.5 * (b - a) * w)
    return np.concatenate(zs), np.concatenate(ws)

MW_PANELS = [(0, 0.6, 80), (0.6, 2.0, 40), (2.0, 4.5, 25), (4.5, 8.0, 12)]

class DynB:
    def __init__(self, r, m=0, panels=MW_PANELS, nr=48, P=7.5, Nperp=10, perp_tol=None):
        z, wz = zpanels(panels)
        xr, wr = np.polynomial.legendre.leggauss(nr)
        rho, wr = 0.5 * P * (xr + 1), 0.5 * P * wr
        sz = (2 * np.pi) ** -0.25 * np.exp(-z**2 / 4) * np.sqrt(wz)
        sr = (2 * np.pi) ** -0.5 * np.exp(-rho**2 / 4) * np.sqrt(2 * np.pi * rho * wr)
        Ar = np.exp(-0.5 * r**2 * (rho[:, None] - rho[None, :]) ** 2) * Ie(m, r**2 * rho[:, None] * rho[None, :])
        R = sr[:, None] * Ar * sr[None, :]
        mu, E = np.linalg.eigh(R)
        idx = np.argsort(mu)[::-1]
        mu, E = mu[idx], E[:, idx]
        if perp_tol is not None:
            Nperp = int(np.sum(mu > perp_tol * mu[0]))
        E = E[:, :Nperp]
        B = E
        if m == 0:
            uperp = sr.copy()   # p0^1/2 perp part with sqrt weights; sum uperp^2 ~ 1
            rem = uperp - E @ (E.T @ uperp)
            nrem = np.linalg.norm(rem)
            if nrem > 1e-13:
                B = np.hstack([E, (rem / nrem)[:, None]])
            self.gam = B.T @ uperp
            self.uperp_norm2 = uperp @ uperp
        else:
            self.gam = None
        self.Mp = B.T @ R @ B
        self.mu_perp = mu[:Nperp]
        As = np.exp(-0.5 * r**2 * (z[:, None] - z[None, :]) ** 2)
        Ar_ = np.exp(-0.5 * r**2 * (z[:, None] + z[None, :]) ** 2)
        self.Ze = sz[:, None] * (As + Ar_) * sz[None, :]
        self.Zo = sz[:, None] * (As - Ar_) * sz[None, :]
        self.sz = sz
        self.z = z
        self.nb = B.shape[1]
        self.n = len(z) * self.nb
        self.D = np.kron(z, np.ones(self.nb))
        self.m = m

    def L2(self, kap2, gt):
        Ke = gt * np.kron(self.Ze, self.Mp)
        Ko = gt * np.kron(self.Zo, self.Mp)
        if self.gam is not None:
            ue = np.sqrt(2.0) * np.kron(self.sz, self.gam)
            Ke += np.outer(ue, ue)
        n = self.n
        Ae = -Ke; Ae[np.diag_indices(n)] += kap2
        Ao = -Ko; Ao[np.diag_indices(n)] += kap2
        return (self.D[:, None] * Ao) @ (self.D[:, None] * Ae) / kap2

    def omegas(self, kap2, gt):
        w2 = np.linalg.eigvals(self.L2(kap2, gt))
        Om = np.sqrt(w2.astype(complex))
        return np.where(Om.imag < 0, -Om, Om)

    def growing(self, kap2, gt, tol=1e-5):
        Om = self.omegas(kap2, gt)
        g = Om[Om.imag > tol]
        g = g[np.argsort(-g.imag)]
        return g

    def static_top(self, gt, parity='e'):
        Ke = gt * np.kron(self.Ze if parity == 'e' else self.Zo, self.Mp)
        if self.gam is not None and parity == 'e':
            ue = np.sqrt(2.0) * np.kron(self.sz, self.gam)
            Ke += np.outer(ue, ue)
        return np.linalg.eigvalsh(Ke)[::-1][:4]

def fmt(g, k=4):
    return "[" + ", ".join(f"{c.real:+.4f}{c.imag:+.4f}i" for c in g[:k]) + "]"

if __name__ == "__main__":
    import time
    from mpmath import findroot, sqrt, pi, exp, erfc
    t0 = time.time()
    for kap in [0.5, 0.8, 0.95]:
        xi = findroot(lambda X: 1 - sqrt(pi) * X * exp(X**2) * erfc(X) - kap**2, 0.3)
        G = float(sqrt(2) * kap * xi)
        D = DynB(1.2917, m=0)
        g = D.growing(kap**2, 0.0)
        print(f"anchor gt=0 kappa={kap}: closed-form Gamma={G:.6f}; L-matrix: {fmt(g,2)}  (n={D.n}, nb={D.nb})")
    D = DynB(1.2917, m=0)
    print("static check (even sector top, odd sector top) at gt=10:", D.static_top(10.0)[:2], D.static_top(10.0, 'o')[:2])
    print("   expected Lambda_0=2.305034, odd l=1: 10*0.0700901=0.700901")
    print(f"time {time.time()-t0:.1f}s")
