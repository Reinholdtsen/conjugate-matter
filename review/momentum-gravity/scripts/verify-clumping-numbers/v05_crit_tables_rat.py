"""Verifier v05: rational gate W = (1+s^2/2)^-2 critical gt tables (C5 brackets, C10 rational),
Fourier-space l=0 operator of v04, top eigenvalue by Schur complement:
Lambda - 1 = gt * sum_j beta_j^2 / (Lambda - gt g_j), with G = V diag(g) V^T, beta = V^T b."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v04_static_kspace import KStatic

class Fast:
    def __init__(self, kind, r):
        S = KStatic(kind, r)
        g, V = np.linalg.eigh(S.G)
        self.g = g
        self.beta2 = (V.T @ S.b1) ** 2
        self.gmax = g.max()
        self.S = S

    def top(self, gt):
        if gt == 0:
            return 1.0
        f = lambda L: (L - 1.0) - gt * np.sum(self.beta2 / (L - gt * self.g))
        lo = gt * self.gmax * (1 + 1e-13)
        hi = 1.0 + gt * self.gmax + 1e-9
        hi = max(hi, lo * 1.0000001)
        while f(hi) < 0:
            hi *= 1.5
        for _ in range(120):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
        return 0.5 * (lo + hi)

    def gt_crit(self, kap2):
        lo, hi = 0.0, 1.0
        while self.top(hi) < kap2:
            hi *= 2
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if self.top(mid) < kap2 else (lo, mid)
        return 0.5 * (lo + hi)

def pairavg(kind, r):
    w = np.linspace(0, 40, 400001)
    pdf = 4 * np.pi * w**2 * (4 * np.pi) ** -1.5 * np.exp(-w**2 / 4)
    s = r * w
    W = np.exp(-s**2 / 2) if kind == 'gauss' else (1 + s**2 / 2) ** -2
    return np.trapezoid(pdf * W, w)

if __name__ == "__main__":
    # sanity: Fast top vs full eigvalsh
    F = Fast('rat2', 1.2917)
    print("sanity rat2 r=1.2917 gt=10: Schur top =", F.top(10.0), " full eig =", F.S.top(10.0))
    kap2s = [1.1, 2.0, 4.4, 10.0, 25.0]
    print("C5 rational (1+s^2/2)^-2: critical gt at kappa^2 =", kap2s)
    for r in [0.25, 1.2917, 4.0, 8.333]:
        F = Fast('rat2', r)
        print(f"  r={r:7.4f}:", ", ".join(f"{F.gt_crit(k):.4g}" for k in kap2s))
    print("\nC10 rational: no-revir and revir thresholds")
    R0 = 8.2
    Qsun = 24.7714  # recomputed in v03 / v08
    envs = {'dwarf': (0.25, [np.pi**2 / 9, 4 * np.pi**2 / 9]),
            'MW': (155 / 120, [np.pi**2 / 2, 2 * np.pi**2, Qsun]),
            'cluster': (1000 / 120, [np.pi**2 / 9, 4 * np.pi**2 / 9])}
    for name, (r, Qs) in envs.items():
        F = Fast('rat2', r)
        W = pairavg('rat2', r)
        print(f"  {name}: r={r:.4f} Lam_g(rat2)={F.S.Lam_g:.5e} <W>_rat2={W:.5e} ratio={F.S.Lam_g/W:.4f}")
        for Q in Qs:
            gnr = F.gt_crit(Q)
            f = lambda g: F.top(g) - Q * (1 + g * W)
            grid = np.concatenate([[0], np.logspace(-3, 7, 300)])
            vals = np.array([f(g) for g in grid])
            idx = np.where((vals[:-1] < 0) & (vals[1:] >= 0))[0]
            if len(idx) == 0:
                rv = 'inf'
            else:
                lo, hi = grid[idx[0]], grid[idx[0] + 1]
                for _ in range(80):
                    mid = 0.5 * (lo + hi)
                    lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
                rv = f"{0.5*(lo+hi):.4g}"
            print(f"     Q={Q:.4f}: no-revir {gnr:.4g}, revir {rv}")
