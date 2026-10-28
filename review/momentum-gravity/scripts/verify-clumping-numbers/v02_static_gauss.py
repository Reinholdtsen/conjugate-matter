"""Verifier v02: static operator K = u u^T + gt * Kg (Gaussian gate), 3D, isotropic Maxwellian.
Method A: numerically diagonalize the 1D kernel on a uniform grid; build the 3D
          Cartesian product spectrum; solve the rank-one secular equation (no Mehler formula).
Method B: 3D tensor-product grid, power iteration with separable matvec (no secular equation).
Outputs: Lambda_0, second l=0 eigenvalue, overlap with density mode u, rms speed of
delta f = p0^(1/2) phi (linear weighting), critical gt at given kappa^2.
Units: velocities in sigma; r = sigma/v*.
"""
import numpy as np

def oned(r, n=None, L=12.0):
    if n is None:
        n = int(max(400, 2 * L * r * 12))   # >= 12 points per kernel width 1/r
    x, h = np.linspace(-L, L, n, retstep=True)
    u1 = np.sqrt(h) * (2 * np.pi) ** -0.25 * np.exp(-x**2 / 4)
    K = u1[:, None] / np.sqrt(h) * np.exp(-0.5 * r**2 * (x[:, None] - x[None, :]) ** 2) * u1[None, :] / np.sqrt(h) * h
    lam, psi = np.linalg.eigh(K)
    idx = np.argsort(lam)[::-1]
    lam, psi = lam[idx], psi[:, idx]
    c = psi.T @ u1
    d = psi.T @ (x**2 * u1)
    return x, h, u1, K, lam, psi, c, d

class Static3D:
    def __init__(self, r, J=None, n=None):
        self.r = r
        x, h, u1, K, lam, psi, c, d = oned(r, n=n)
        if J is None:
            # keep even modes until lam_j/lam_0 < 1e-7
            J = int(np.searchsorted(-lam / lam[0], -1e-7))
        ev = np.arange(0, J, 2)                   # odd ones have c = 0 by parity
        self.lam1, self.c1, self.d1 = lam[ev], c[ev], d[ev]
        L3 = self.lam1[:, None, None] * self.lam1[None, :, None] * self.lam1[None, None, :]
        a3 = self.c1[:, None, None] * self.c1[None, :, None] * self.c1[None, None, :]
        b3 = (self.d1[:, None, None] * self.c1[None, :, None] * self.c1[None, None, :]
              + self.c1[:, None, None] * self.d1[None, :, None] * self.c1[None, None, :]
              + self.c1[:, None, None] * self.c1[None, :, None] * self.d1[None, None, :])
        self.L3, self.a3, self.b3 = L3.ravel(), a3.ravel(), b3.ravel()
        # group numerically equal levels (exact regrouping of identical pole values; speeds up sums)
        key = np.round(np.log(np.abs(self.L3) + 1e-300), 9)
        uk, inv = np.unique(key, return_inverse=True)
        self.gL = np.zeros(len(uk)); self.gA = np.zeros(len(uk))
        np.add.at(self.gA, inv, self.a3**2)
        cnt = np.zeros(len(uk)); np.add.at(cnt, inv, 1.0)
        np.add.at(self.gL, inv, self.L3)
        self.gL /= cnt
        self.Lam_g = lam[0] ** 3
        self.norm_u = np.sum(self.a3**2)
        self.lam_full = lam

    def sec(self, Lam, gt):
        return np.sum(self.a3**2 / (Lam - gt * self.L3)) - 1.0

    def top(self, gt):
        # Newton from the right on the convex decreasing secular function (grouped levels)
        A, Lg = self.gA, self.gL
        L = 1.0 + gt * Lg.max() + 1e-12
        for _ in range(200):
            d = L - gt * Lg
            f = np.sum(A / d) - 1.0
            fp = -np.sum(A / d**2)
            step = f / fp
            L_new = L - step
            if L_new <= gt * Lg.max():
                L_new = 0.5 * (L + gt * Lg.max())
            if abs(L_new - L) < 1e-15 * max(1.0, abs(L)):
                L = L_new
                break
            L = L_new
        return L

    def second_l0(self, gt):
        # distinct pole values (levels); root between the 2nd and 1st distinct poles with weight
        poles = np.unique(np.round(gt * self.L3[self.a3**2 > 1e-30], 12))[::-1]
        p0, p1 = poles[0], poles[1]
        lo, hi = p1 * (1 + 1e-13), p0 * (1 - 1e-13)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if self.sec(mid, gt) > 0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    def mode_stats(self, gt):
        Lam = self.top(gt)
        phi = self.a3 / (Lam - gt * self.L3)
        overlap = np.sum(self.a3 * phi) / np.sqrt(np.sum(phi**2))
        rms = np.sqrt(np.sum(self.b3 * phi) / np.sum(self.a3 * phi))
        return Lam, overlap, rms

    def gt_crit(self, kap2):
        lo, hi = 0.0, 1.0
        while self.top(hi) < kap2:
            hi *= 2
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            if self.top(mid) < kap2:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

def power_tensor(r, gt, n=64, L=8.0, iters=400):
    x, h = np.linspace(-L, L, n, retstep=True)
    u1 = np.sqrt(h) * (2 * np.pi) ** -0.25 * np.exp(-x**2 / 4)
    A = u1[:, None] / np.sqrt(h) * np.exp(-0.5 * r**2 * (x[:, None] - x[None, :]) ** 2) * u1[None, :] / np.sqrt(h) * h
    u = np.einsum('i,j,k->ijk', u1, u1, u1)
    v = u.copy() + 0.01 * np.random.default_rng(1).standard_normal(u.shape) * u
    lam = 0
    for it in range(iters):
        w = u * np.sum(u * v) + gt * np.einsum('ia,jb,kc,abc->ijk', A, A, A, v, optimize=True)
        lam_new = np.sum(w * v) / np.sum(v * v)
        v = w / np.linalg.norm(w)
        if abs(lam_new - lam) < 1e-12 * abs(lam_new):
            break
        lam = lam_new
    return lam_new, it

if __name__ == "__main__":
    np.set_printoptions(linewidth=150)
    cases = [(1.2917, 10.0), (1.2917, 281.0), (0.25, 1.0), (1.2917, 1.0), (1.2917, 100.0),
             (4.0, 1e4), (8.333, 1e4), (0.25, 0.0)]
    cache = {}
    print(" r       gt       Lambda_0(secular)  2nd l=0     overlap   rms/sigma | Lambda_0(tensor power) | 1+gt*Lam_g bound")
    for r, gt in cases:
        if r not in cache:
            cache[r] = Static3D(r)
        S = cache[r]
        Lam, ov, rms = S.mode_stats(gt)
        sec2 = S.second_l0(gt) if gt > 0 else float('nan')
        tp = ''
        if r < 2:
            lt, it = power_tensor(r, gt)
            tp = f"{lt:.8f} ({it} it)"
        print(f" {r:7.4f} {gt:8.1f}  {Lam:.8f}    {sec2:.6f}  {ov:.5f}   {rms:.4f}   | {tp:22s} | {1+gt*S.Lam_g:.6f}")
    print("\n|u|^2 in truncated basis (should be ~1):", {r: round(cache[r].norm_u, 10) for r in cache})
