"""Verifier v11: cluster (r = 1000/120, narrow gate) dynamic checks of C11 with the generator
eigenvalue method, composite panels in v_z and v_perp, sectors m = 0..3.
Claimed (C11): kappa^2 = 1.0966: gt=304.4 Gamma=0.06569; gt=1522 0.01885; gt=1598 0.02721 (purely
growing, gravity-coupled); kappa^2 = 4.3865, gt = 5858: no purely growing mode."""
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v06_dynamic_L import Ie
from v07_dynamic_basis import zpanels

class DynP:
    def __init__(self, r, m, zp, rp, Nperp):
        z, wz = zpanels(zp)
        rho, wr = zpanels(rp)
        sz = (2 * np.pi) ** -0.25 * np.exp(-z**2 / 4) * np.sqrt(wz)
        sr = (2 * np.pi) ** -0.5 * np.exp(-rho**2 / 4) * np.sqrt(2 * np.pi * rho * wr)
        Ar = np.exp(-0.5 * r**2 * (rho[:, None] - rho[None, :]) ** 2) * Ie(m, r**2 * rho[:, None] * rho[None, :])
        R = sr[:, None] * Ar * sr[None, :]
        mu, E = np.linalg.eigh(R)
        idx = np.argsort(mu)[::-1]
        mu, E = mu[idx], E[:, idx]
        self.mu_all = mu
        E = E[:, :Nperp]
        B = E
        self.gam = None
        if m == 0:
            rem = sr - E @ (E.T @ sr)
            nrem = np.linalg.norm(rem)
            B = np.hstack([E, (rem / nrem)[:, None]])
            self.gam = B.T @ sr
        self.Mp = B.T @ R @ B
        As = np.exp(-0.5 * r**2 * (z[:, None] - z[None, :]) ** 2)
        Arf = np.exp(-0.5 * r**2 * (z[:, None] + z[None, :]) ** 2)
        self.Ze = sz[:, None] * (As + Arf) * sz[None, :]
        self.Zo = sz[:, None] * (As - Arf) * sz[None, :]
        self.sz, self.z = sz, z
        self.nb = B.shape[1]
        self.n = len(z) * self.nb
        self.D = np.kron(z, np.ones(self.nb))

    def static_top(self, gt):
        Ke = gt * np.kron(self.Ze, self.Mp)
        if self.gam is not None:
            ue = np.sqrt(2.0) * np.kron(self.sz, self.gam)
            Ke += np.outer(ue, ue)
        return np.linalg.eigvalsh(Ke)[-1]

    def growing(self, kap2, gt, tol=1e-5):
        Ke = gt * np.kron(self.Ze, self.Mp)
        Ko = gt * np.kron(self.Zo, self.Mp)
        if self.gam is not None:
            ue = np.sqrt(2.0) * np.kron(self.sz, self.gam)
            Ke += np.outer(ue, ue)
        Ke *= -1; Ke[np.diag_indices(self.n)] += kap2
        Ko *= -1; Ko[np.diag_indices(self.n)] += kap2
        L2 = (self.D[:, None] * Ko) @ (self.D[:, None] * Ke)
        L2 /= kap2
        del Ke, Ko
        w2 = np.linalg.eigvals(L2)
        Om = np.sqrt(w2.astype(complex))
        Om = np.where(Om.imag < 0, -Om, Om)
        g = Om[Om.imag > tol]
        return g[np.argsort(-g.imag)]

ZP = [(0, 0.4, 60), (0.4, 1.5, 50), (1.5, 3.0, 35), (3.0, 5.0, 22), (5.0, 8.0, 10)]
RP = [(0, 1.5, 60), (1.5, 3.5, 45), (3.5, 7.5, 25)]
r = 1000 / 120
if __name__ == "__main__":
    t0 = time.time()
    Lg = (0.5 + r * r + np.sqrt(1 + 4 * r * r) / 2) ** -1.5
    q = 2 * r * r / (1 + 2 * r * r + np.sqrt(1 + 4 * r * r))
    D0 = DynP(r, 0, ZP, RP, Nperp=14)
    print(f"n={D0.n}; perp eigenvalues (m=0) / closed lam0^2 q^(2j):",
          np.round(D0.mu_all[:4] / (Lg ** (2 / 3) * q ** (2 * np.arange(4))), 6))
    print(f"static check gt=1598: Lambda_0 = {D0.static_top(1598.0):.4f} (claimed 2.5553)", flush=True)
    cases = [(np.pi**2 / 9, 304.4), (np.pi**2 / 9, 1522.0), (np.pi**2 / 9, 1598.0), (4 * np.pi**2 / 9, 5858.0)]
    for m in [0, 1, 2, 3]:
        D = D0 if m == 0 else DynP(r, m, ZP, RP, Nperp=14)
        for kap2, gt in cases:
            g = D.growing(kap2, gt)
            s = ", ".join(f"{c.real:+.5f}{c.imag:+.5f}i" for c in g[:3])
            print(f"m={m} kap2={kap2:.4f} gt={gt:7.1f}: n_grow={len(g)} top: [{s}]   ({time.time()-t0:.0f}s)", flush=True)
