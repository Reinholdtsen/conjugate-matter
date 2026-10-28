"""Segue 1 heating by early, dense chi clumps in the corner (round 3, label "corner"); refines part D
of obs_corner.py with a mass integral.

Heating limit for compact clumps (obs_corner.py D): sum over clumps of f(M) M < 7.88 Msun, where f(M) dM
is the DM mass fraction in clumps of mass M.  Clump fraction proxy (Graham & Ramani 2024 [S]): the
Press-Schechter collapsed fraction F(>M, z) = erfc(1.686/(sqrt2 sigma(M, z))), evaluated at the minimum
collapse redshift z_min = 87.7 for which the clump scale density 86.3 rho_m(z) exceeds Segue 1's mean
DM density (2.40 Msun/pc^3).  Heating moment H = Int_{M_lo}^{M_hi} M (-dF/dM) dM, with M_hi = 1e5 Msun
(about a sixth of the mass inside Segue 1's half-light radius; heavier objects are not 'clumps' there).
Survival of the clumps inside Segue 1 and their compactness are assumed, as in Graham & Ramani.
"""
import os
import sys
import numpy as np
from math import erfc, sqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import linear_corner as L   # noqa: E402
C = L.C

z_min = 87.7
kk = np.logspace(-2, 3.6, 260)
P0 = C.P_lin(kk, z_min)
Ms = np.logspace(0, 5, 26)


def H_moment(T):
    s = np.array([L.sigma_M(M, kk, P0 * T) for M in Ms])
    F = np.array([erfc(1.686 / (sqrt(2) * x)) for x in s])
    Mmid = np.sqrt(Ms[1:] * Ms[:-1])
    return np.sum(Mmid * (F[:-1] - F[1:])), F, s


H0, F0, s0 = H_moment(np.ones_like(kk))
print(f"LCDM: sigma(1, 1e5 Msun; z = {z_min}) = {s0[0]:.3f}, {s0[-1]:.3f}; F(>1 Msun) = {F0[0]:.2e}; heating moment H = {H0:.3e} Msun "
      "(limit 7.88)")
for reading in ("H", "K4"):
    for vs in (3, 5, 10, 20):
        row = []
        for e in (0.3, 1.0, 2.0):
            T = L.T2(kk, e, vs, reading, [z_min])[z_min]
            Hm, F, s = H_moment(T)
            row.append(f"eps={e:g}: F(>1)={F[0]:.3g} F(>1e3)={F[15]:.3g} H={Hm:.3g} Msun{' >limit' if Hm > 7.88 else ''}")
        print(f"{reading:2s} v*={vs:2d}: " + " | ".join(row))
