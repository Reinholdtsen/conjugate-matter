"""Verifier v16: (a) dwarf (r=0.25) growth rates of C11 at kappa^2=(pi/3)^2: gt=0.2304 (claimed 0.07069), gt=1.152 (0.50993);
(b) refine the MW m=0 maximum over kappa^2 at gt=280.7 near kappa^2 = 26 (v13 found 0.8801)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v07_dynamic_basis import DynB, MW_PANELS
D = DynB(0.25, m=0, panels=MW_PANELS, Nperp=10)
for gt, cl in [(0.2304, 0.07069), (1.152, 0.50993)]:
    g = D.growing(np.pi**2 / 9, gt)
    print(f"dwarf gt={gt}: Gamma = {g[0].imag:.5f} (claimed {cl}); Re = {g[0].real:.1e}")
D = DynB(155 / 120, m=0, panels=MW_PANELS, Nperp=12)
best = (0, 0)
for k2 in [23.0, 24.0, 25.0, 26.0, 27.0, 28.0]:
    g = D.growing(k2, 280.7)
    G = g[0].imag if len(g) else 0.0
    print(f"MW gt=280.7 kappa^2={k2}: Gamma={G:.4f} (Re {g[0].real:.1e})")
    best = max(best, (G, k2))
print(f"max ~ {best[0]:.4f} at kappa^2={best[1]} -> e-fold {40.98/best[0]:.1f} Myr = {40.98/best[0]/219.0:.3f} t_orb")
