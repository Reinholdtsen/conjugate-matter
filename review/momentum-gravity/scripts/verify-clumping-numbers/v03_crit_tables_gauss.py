"""Verifier v03: critical gt tables for the Gaussian gate (C5, C8 crossover, C10),
using the independent secular solver of v02. Re-virialized condition (agent's model):
Lambda_0(gt) = Q (1 + gt <W>), <W> = pair average of W over relative velocity ~ N(0, 2 sigma^2):
computed here by direct numerical quadrature, not by the closed form."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v02_static_gauss import Static3D

def pairavg_W_gauss(r):
    # <exp(-r^2 |w|^2 / 2)>, w ~ N(0, 2 I_3)  (sigma units); radial quadrature
    w = np.linspace(0, 40, 400001)
    pdf = 4 * np.pi * w**2 * (4 * np.pi) ** -1.5 * np.exp(-w**2 / 4)
    return np.trapezoid(pdf * np.exp(-0.5 * r**2 * w**2), w)

kap2s = [1.1, 2.0, 4.4, 10.0, 25.0]
print("C5 Gaussian gate: critical gt at kappa^2 =", kap2s)
for r in [0.25, 1.2917, 4.0, 8.333]:
    S = Static3D(r)
    print(f"  r={r:7.4f}:", ", ".join(f"{S.gt_crit(k):.4g}" for k in kap2s))

print("\nC8 crossover 1/Lambda_g and C10 tables")
Qs = {'dwarf': (0.25, [np.pi**2 / 9, 4 * np.pi**2 / 9]),
      'MW': (155 / 120, [np.pi**2 / 2, 2 * np.pi**2, None]),
      'cluster': (1000 / 120, [np.pi**2 / 9, 4 * np.pi**2 / 9])}
for name, (r, qlist) in Qs.items():
    S = Static3D(r)
    W = pairavg_W_gauss(r)
    print(f"  {name}: r={r:.4f}, Lambda_g={S.Lam_g:.6e}, 1/Lambda_g={1/S.Lam_g:.4g}, <W>(quad)={W:.6e}, closed (1+2r^2)^-1.5={(1+2*r*r)**-1.5:.6e}, Lam_g/<W>={S.Lam_g/W:.4f}")
    for Q in qlist:
        if Q is None:
            continue
        gnr = S.gt_crit(Q)
        # revir: find gt with Lambda_0(gt) - Q(1+gt W) = 0, if any
        f = lambda g: S.top(g) - Q * (1 + g * W)
        grid = np.concatenate([[0], np.logspace(-3, 7, 400)])
        vals = np.array([f(g) for g in grid])
        idx = np.where((vals[:-1] < 0) & (vals[1:] >= 0))[0]
        if len(idx) == 0:
            rv = 'inf'
            asym = vals[-1] / grid[-1]
        else:
            lo, hi = grid[idx[0]], grid[idx[0] + 1]
            for _ in range(100):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
            rv = f"{0.5*(lo+hi):.4g}"
            asym = None
        print(f"     Q={Q:.4f}: no-revir gt_c={gnr:.4g}; revir gt_c={rv}")
# MW solar circle margin
R0, sig, rho = 8.2, 155.0, 0.4
G = 4.30091e-3  # pc (km/s)^2 / Msun
rho_msun_pc3 = rho * 1.78266192e-24 / 1.98847e33 * (3.0856776e18) ** 3
kJ = np.sqrt(4 * np.pi * G * rho_msun_pc3) / sig  # 1/pc
lamJ = 2 * np.pi / kJ / 1000
Q_sun = (lamJ / R0) ** 2
S = Static3D(155 / 120)
print(f"  MW solar circle: lambda_J={lamJ:.3f} kpc, Q=(lambda_J/R0)^2={Q_sun:.4f}, no-revir gt_c={S.gt_crit(Q_sun):.4g}")
