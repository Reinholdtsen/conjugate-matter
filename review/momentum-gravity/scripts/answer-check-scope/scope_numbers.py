"""Arithmetic behind the scope check of the round-3 draft answer.

Every input is copied from a printed output named in the comment beside it.
"""
from math import sqrt, log10

c = 299792.458  # km/s

# Margins quoted in the draft (thresholds from VCN u2 via critic3/c4_numbers.out; bounds from critic3/c1)
thr_mw, thr_cl = 28.07, 692.8
lya_gas, lya_matter, lya_F_gas = 0.1063, 0.0570, 0.1755
sgr_loose = 2.46
print(f"MW margin vs H gas bound: {thr_mw/lya_gas:.1f}; cluster: {thr_cl/lya_gas:.0f}; MW vs Sgr loosest: {thr_mw/sgr_loose:.1f}")
print(f"MW margin vs force-law gas bound 0.1755 (bracket the draft omits): {thr_mw/lya_F_gas:.0f}; cluster: {thr_cl/lya_F_gas:.0f}")
print(f"minimum clumping threshold 1.000003 vs widest allowed eps at 120 km/s (0.1755): {1.000003/lya_F_gas:.1f}x")

# Second gate scale ratios (draft: 4x at 30, 40x at 3); corner printed 12.0 and 4.0 only
for vs in (30.0, 10.0, 3.0):
    print(f"120/{vs:g} = {120.0/vs:.1f}")

# Spin-2 velocity factors at 120 km/s (critic3/c4 (d))
b2 = (120.0/c)**2
g2 = 1.0/(1.0 - b2)
print(f"X (3g^2-1)/2 - 1 = {(3*g2-1)/2-1:.3e}; graviton 2g^2-1-1 = {2*g2-1-1:.3e}")

# Gate convention (task statement): v_a = sqrt2 v*
print(f"v_a at record v* = 120: {sqrt(2)*120:.1f} km/s; ordinary-tests scan 0.3-3000 km/s in v_a is v* = {0.3/sqrt(2):.2f}-{3000/sqrt(2):.0f} km/s")

# Ordinary-tests bounds (VON vot_bounds.out): at v_a = 120, Mars 1.82e-11, Mercury 6.37e-11; at v_a = 170, Mars 3.5e-11
print(f"Mars 3.5e-11 / 1.82e-11 = {3.5e-11/1.82e-11:.2f} (convention shift alone); Mercury at v_a=120 is 6.37e-11, not 2e-11")

# Planck tau significance (critic3/c2_corner_recheck.out; Planck 0.054 +- 0.007)
for tau in (0.073, 0.078, 0.090, 0.099):
    print(f"tau(ii) = {tau}: {(tau-0.054)/0.007:.1f} sigma above Planck")

# eBOSS compressed fit (critic3/c1 (5)): chi2 26.31 -> 1.90 at eps = 0.0535
d = 26.31 - 1.90
print(f"eBOSS delta chi^2 = {d:.2f} (naive one-parameter significance {sqrt(d):.1f} sigma)")

# Window of the N-body in physical time (corner phys_scales.out)
print("43 t_ff: Segue 1 0.117 Gyr; classical dSph 0.372-0.643 Gyr (printed) -> draft '0.1-0.6 Gyr'")

# Debt 3a vs linearized criterion, MW (debt3a_check.out 2.9e-31; clumping C6 8.7e-31)
print(f"linearized / 3a (MW) = {8.7e-31/2.9e-31:.1f}; dwarf {3.27e-28/3.9e-28:.2f}")

# Vainshtein radius of 1 kg at range 50 um, r_V^3 = K r_S lambda^2 (script line 383 uses K = 2)
G, C = 6.67430e-11, 2.99792458e8
rS = 2*G*1.0/C**2
for K in (1, 2, 15):
    rV = (K*rS*(50e-6)**2)**(1/3)
    print(f"K = {K:2d}: r_V = {rV:.2e} m, round(log10) = {round(log10(rV))}")
