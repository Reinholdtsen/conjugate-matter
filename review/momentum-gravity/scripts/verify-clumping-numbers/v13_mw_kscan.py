"""Verifier v13: MW (r=155/120) k-scan over kappa^2 >= Q = pi^2/2 at gt = 56.14 and 280.7, all sectors
m = 0, 1, 2 (generator-eigenvalue method, v07), to test C11's 'fastest found 52.7 Myr'."""
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v07_dynamic_basis import DynB, MW_PANELS

r = 155 / 120
Ds = {m: DynB(r, m=m, panels=MW_PANELS, Nperp=12) for m in [0, 1, 2]}
t0 = time.time()
for gt, k2list in [(56.14, [5.5, 6.5, 8.0, 9.0]),
                   (280.7, [6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 22.0, 26.0, 30.0, 34.0, 38.0, 41.0])]:
    print(f"--- gt = {gt} ---")
    best = (0, None, None)
    for k2 in k2list:
        row = []
        for m, D in Ds.items():
            g = D.growing(k2, gt)
            c = g[0] if len(g) else 0j
            row.append(f"m={m}: {c.real:+.4f}{c.imag:+.4f}i")
            if c.imag > best[0]:
                best = (c.imag, m, k2)
        print(f"  kappa^2={k2:5.1f}: " + " | ".join(row), flush=True)
    print(f"  max Gamma = {best[0]:.4f} (m={best[1]}, kappa^2={best[2]}), e-fold = {40.98/best[0]:.1f} Myr  ({time.time()-t0:.0f}s)")
