"""
v3_k5_k3extra.py -- (1) K5's scale comparison at eps = 0.3, v* = 120: T_m (not squared)
at k_p, 3 and 10 /Mpc, z = 3, per reading; (2) K3's illustrative chi thermal velocity:
kinetic decoupling at T_kd = m/20 from a bath at the photon temperature, m = 70 MeV,
with and without the (4/11)^(1/3) factor from later e+e- annihilation heating photons
(not chi).
"""
import numpy as np
from v3_cosmo import grow, kpivot

ks = np.array([kpivot(), 3.0, 10.0])
d0 = grow(ks, 0.0, 120, 'lcdm', a_end=0.25)[2]
for rd in ('agent', 'iii', 'i', 'ii'):
    d1 = grow(ks, 0.3, 120, rd, a_end=0.25)[2]
    print(f"eps=0.3, v*=120, {rd:5s}: T_m(k_p) = {d1[0]/d0[0]:.4f}, T_m(3/Mpc) = {d1[1]/d0[1]:.4f}, T_m(10/Mpc) = {d1[2]/d0[2]:.4f}")

c = 299792.458
m_eV = 70e6; Tkd = m_eV/20
T0 = 8.617333262e-5*2.7255           # eV
v_kd = np.sqrt(3*Tkd/m_eV)*c         # rms 3D at decoupling (nonrelativistic estimate)
for lab, fac in (("no e+e- factor", 1.0), ("with (4/11)^(1/3)", (4/11)**(1/3))):
    a_kd = T0/Tkd*fac
    print(f"{lab:20s}: a_kd = {a_kd:.3e}; v_rms today = {v_kd*a_kd:.2e} km/s; at z=1089.92: {v_kd*a_kd*1090.92:.2e} km/s")
