"""
v3_compare.py -- term-by-term comparison of the linear systems, at the DESI pivot and
across scales, and the state (T^2, dn) at each reading's DESI boundary.
Readings: agent (dark-tests K4 as implemented in growth.py), iii (force law, correct
density kernel R1), i (Hamiltonian), ii (Lagrangian), c4b (critic's transcription).
"""
import numpy as np
from v3_cosmo import grow, kpivot
from v3_lya import transfer

print("=== Pivot, v* = 120 km/s, eps = 0.1 (z = 3) ===")
for rd in ('agent', 'agent_noad', 'iii', 'i', 'ii', 'c4b'):
    t = transfer(rd, 120, np.array([0.1]))
    print(f"  {rd:10s}: T_m^2 = {t['m'][0][0]:.4f}  dn_m = {t['m'][1][0]:+.4f} | T_b^2 = {t['b'][0][0]:.4f}  dn_b = {t['b'][1][0]:+.4f}")
print("  (c4b's own output: reading c: T_m^2 = 0.9861, dn_m = +0.0047; T_b^2 = 0.9926, dn_b = -0.0092)")

print("\n=== IC and step sensitivity, reading i, v*=120, eps=0.1 ===")
kp = kpivot()
for ic in (0.1, 0.5, 1.0):
    for ns in (3000, 6000, 12000):
        dc, db, dm = grow(np.array([kp]), 0.1, 120, 'i', a_end=0.25, ic_slope=ic, nstep=ns)
        dc0, db0, dm0 = grow(np.array([kp]), 0.0, 120, 'lcdm', a_end=0.25, ic_slope=ic, nstep=ns)
        print(f"  ic_slope={ic}, nstep={ns}: T_m^2(k_p) = {(dm[0]/dm0[0])**2:.6f}")

print("\n=== Scale dependence, v* = 120, eps = 0.1, z = 3: T_m^2(k) ===")
ks = np.array([0.1, 0.3, kp, 1.5, 3.0, 10.0, 30.0])
row = "  k [1/Mpc]: " + " ".join(f"{k:7.3f}" for k in ks)
print(row)
for rd in ('agent', 'iii', 'i', 'ii', 'c4b'):
    dc, db, dm = grow(ks, 0.1, 120, rd, a_end=0.25)
    dc0, db0, dm0 = grow(ks, 0.0, 120, 'lcdm', a_end=0.25)
    print(f"  {rd:9s}  " + " ".join(f"{(a/b)**2:7.4f}" for a, b in zip(dm, dm0)))
print("  y(z=3) = k v*/(aH): " + " ".join(f"{k*120/(0.25*307.65):7.3f}" for k in ks))
