"""Physical scales for the corner N-body runs and the satellite gate factors (round 3, label "corner").
N-body units G = M = a = 1 (Plummer).  Central free-fall time t_ff = 1/sqrt(4 pi G rho0), rho0 = 3/(4 pi) [T].
Half-mass relaxation time (Spitzer form, BT eq. 7.108 [T, dagger]): t_rh = 0.138 N r_h^1.5 / (sqrt(G M) ln(0.4 N)).
Dwarf densities: classical dSph rho_DM(150 pc) = 0.79-2.36e8 Msun/kpc^3 (Read, Walker & Steger 2019 [S]);
Segue 1 mean DM density inside r_1/2: 2.40 Msun/pc^3 (obs_corner.py D, from Simon et al. 2011 [S]).
Satellite gate factor (critic c5 formula, Gaussian gate, host Maxwellian of 1D dispersion s, satellite speed V):
<W> = (v*^2/(v*^2+s^2))^(3/2) exp(-V^2/(2 (v*^2+s^2))); host s = 149.9 km/s, Sgr V = 311.1 km/s (dark-tests K13 [S]).
"""
import numpy as np
G = 4.30091e-3                                   # pc (km/s)^2 / Msun [T]
pc_kms_Myr = 0.977792                            # 1 pc/(km/s) in Myr [T]
tff_pl = 1 / np.sqrt(4 * np.pi * 3 / (4 * np.pi))
rh = (2 ** (2 / 3) - 1) ** -0.5
print(f"Plummer central t_ff = {tff_pl:.4f} N-body units; post-ramp window 25 units = {25/tff_pl:.1f} t_ff; whole run 40 units = {40/tff_pl:.1f} t_ff")
for N in (1000, 2000):
    print(f"N = {N}: t_rh (Spitzer, gravity only) = {0.138 * N * rh**1.5 / np.log(0.4 * N):.1f} N-body units")
for name, rho in (("classical dSph, 0.79e8 Msun/kpc^3", 0.79e8 / 1e9), ("classical dSph, 2.36e8 Msun/kpc^3", 2.36e8 / 1e9), ("Segue 1, 2.40 Msun/pc^3", 2.40)):
    t = 1 / np.sqrt(4 * np.pi * G * rho) * pc_kms_Myr
    print(f"{name}: t_ff = {t:.2f} Myr; 43 t_ff = {43 * t / 1e3:.3f} Gyr; 10 Gyr = {1e4 / t:.0f} t_ff")
s = 149.9; V = 311.1
for vs in (5, 10, 20, 30, 120):
    W = (vs**2 / (vs**2 + s**2)) ** 1.5 * np.exp(-V**2 / (2 * (vs**2 + s**2)))
    print(f"v* = {vs:3d} km/s: Sgr-host <W> = {W:.3e}; 10% EP limit -> eps < {0.1 / W:.3g}")
print(f"Segue 1 gate ratio r = sigma/v* (sigma = 3.7 km/s [S]): v* = 5, 10, 30 -> {3.7/5:.2f}, {3.7/10:.2f}, {3.7/30:.3f}")
