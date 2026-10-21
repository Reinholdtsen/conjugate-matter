"""Scratch re-check of notes/debt3a-stream-stability.md numbers (not part of verify/).
Natural units, GeV. Inputs exactly as 3a states them."""
import math
cm = 5.0677e13          # 1 cm in GeV^-1
g_ = 5.6096e23          # 1 gram in GeV
c = 2.99792458e5        # km/s
cm2_per_g = cm**2 / g_  # cm^2/g in GeV^-3
m = 0.070               # 70 MeV
vstar = 120 / c
S = 30 * cm2_per_g      # sigma0/m
g = math.sqrt(math.pi * S / m)   # sqrt(pi sigma0/m^2), sigma0 = S m
print(f"g = {g:.3g} GeV^-2")
for name, rho_gev_cm3, sig_kms in [("dwarf core", 1.0, 30), ("MW local", 0.4, 155)]:
    rho = rho_gev_cm3 / cm**3
    sig = sig_kms / c
    n = rho / m
    if sig < vstar:
        neff, s2 = n, sig**2
    else:
        neff, s2 = n * (vstar/sig)**3 / (2*math.pi)**1.5, vstar**2
    eps = g * neff
    kin = m * s2
    print(f"{name}: eps_gate = {eps:.2g} GeV, m min(sig,v*)^2 = {kin:.2g} GeV, ratio = {eps/kin:.2g}")
rho = 0.4 / cm**3; sig = 155 / c
mcrit = (math.sqrt(math.pi*S) * rho / sig**2) ** 0.4
print(f"m_crit = {mcrit:.2g} GeV = {mcrit*1e9*1e3:.2g} meV")
print(f"N_occ(m_crit) = {rho/(mcrit**4*sig**3):.2g}")
# Same corollary with the narrow-gate form of the criterion (sigma > v* for MW conditions)
mcrit_narrow = (math.sqrt(math.pi*S) * rho * vstar / (sig**3 * (2*math.pi)**1.5)) ** 0.4
print(f"m_crit (narrow-gate form) = {mcrit_narrow:.2g} GeV; ratio to broad-gate form = {mcrit_narrow/mcrit:.2g}")
print(f"N_occ at narrow-gate m_crit = {rho/(mcrit_narrow**4*sig**3):.2g}")
