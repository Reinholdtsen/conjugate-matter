"""Verifier v10: MW (r=155/120) growth at strong gating, all sectors m=0..3, to test C12's
'strong gating does not give fast growth: fastest rates found ~0.78 per t_ff'.
Also: growth of the gate-only m=1 mode vs kappa^2 at fixed gt, and the C11 near-threshold case
Q = (lambda_J/R0)^2 = 24.77 at 2x the no-revir threshold (gt = 322.4)."""
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v07_dynamic_basis import DynB, MW_PANELS

r = 155 / 120
Lg = (0.5 + r * r + np.sqrt(1 + 4 * r * r) / 2) ** -1.5
q = 2 * r * r / (1 + 2 * r * r + np.sqrt(1 + 4 * r * r))
cache = {}
def get(m):
    if m not in cache:
        cache[m] = DynB(r, m=m, panels=MW_PANELS, Nperp=12)
    return cache[m]

def best(kap2, gt, ms=(0, 1, 2, 3)):
    res = {}
    for m in ms:
        g = get(m).growing(kap2, gt)
        res[m] = g[0] if len(g) else 0j
    return res

t0 = time.time()
print(f"Lambda_g={Lg:.6f}, q={q:.6f}; static sector eigenvalues gt*Lg*q^l")
for kap2 in [2 * np.pi**2, np.pi**2 / 2]:
    print(f"--- kappa^2 = {kap2:.4f}  (m=0 odd threshold gt = {kap2/(Lg*q):.1f}) ---")
    for gt in [320, 400, 600, 1000, 2000, 5000]:
        res = best(kap2, gt)
        s = " | ".join(f"m={m}: {c.real:+.4f}{c.imag:+.4f}i" for m, c in res.items())
        mx = max(res.items(), key=lambda kv: kv[1].imag)
        print(f"  gt={gt:6.0f}: {s}   -> fastest m={mx[0]} Gamma={mx[1].imag:.4f}", flush=True)
print(f"time {time.time()-t0:.0f}s")
print("--- C11: Q=24.7714, gt = 2 x 161.2 = 322.4 ---")
res = best(24.7714, 322.4)
print("  ", {m: f"{c.real:+.5f}{c.imag:+.5f}i" for m, c in res.items()}, f" e-fold = 40.98/Gamma = {40.98/res[0].imag:.1f} Myr" if res[0].imag > 0 else "")
print(f"time {time.time()-t0:.0f}s")
