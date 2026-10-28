"""K7 variant: DESI bound at v*=120 (kernel B + anti-drag, Gaussian, matter ratio) with the EH98 no-wiggle
baseline of vpk.py (0.3368, -2.3072, no baseline error) instead of the published Planck-based one,
and the same for the reading-A kernel."""
import numpy as np
import vlya as L
for dens in ["B", "A"]:
    Tm, Tb = L.run(120.0, dens=dens)
    saved = L.BASE.copy()
    L.BASE[:] = [0.3368, -2.3072]
    b = L.bound(L.chi2_curve(Tm, L.DESI, add_base=False), L.eps_grid)
    L.BASE[:] = saved
    print("kernel %s: EH98 baseline (no baseline errors): eps_max = %.4f" % (dens, b))
