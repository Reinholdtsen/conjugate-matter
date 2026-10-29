"""Where the Hamiltonian-reading linear system (critic c4b) leaves its regular regime: the coefficient
(1 + b) of theta in delta_c' = -(1 + b) theta - ..., with b = (eps/2) Om_c(a) R_a(y), vanishes when
eps = -2/(Om_c R_a(y)).  R_a is most negative near y ~ 1 (c4b: R_a(1) = -0.87168).  Om_c = f_c Om_m(a)
evaluated at z = 3 and z = 50 (dark-tests cosmo.py, Planck 2018).  Also the ratio of the record's gate
scale v* = 120 km/s (calc note #2) to the corner's 10-30 km/s."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import linear_corner as L
C = L.C
ys = np.linspace(0.05, 6, 1200)
Ra = np.array([L.I('Ra', y) for y in ys])
i = np.argmin(Ra)
print(f"min R_a = {Ra[i]:.5f} at y = {ys[i]:.3f}; R_a(1) = {L.I('Ra', 1.0):.5f}")
for z in (50.0, 3.0):
    a = 1 / (1 + z); Omc = C.f_c * C.Omega_m_a(a)
    print(f"z = {z}: Om_c = {Omc:.4f}; (1+b) = 0 at y = {ys[i]:.2f} for eps = {-2/(Omc*Ra[i]):.3f}; at y = 1 for eps = {-2/(Omc*L.I('Ra',1.0)):.3f}")
for vs in (10, 30):
    print(f"record v* = 120 km/s over corner v* = {vs} km/s: ratio {120/vs:.1f}")
