# P20: what the observed bound on Mercury's supplementary perihelion advance implies for a
# v* = 120 km/s velocity gate acting on ordinary matter (model b), using the measured first-order-in-beta
# gated precession at Mercury's parameters from n5 (-1.44967e-2 rad/orbit at beta = 0.01).
from math import pi
P_merc_days = 87.9691
orbits_per_cy = 36525.0/P_merc_days
mas_to_rad = pi/(180*3600*1000)
gated_per_beta = 1.44967e-2/0.01          # rad/orbit per unit beta (n5, beta = 0.01, first order in beta)
gr_per_orbit = 5.0187e-7                  # rad/orbit (n1; 42.98 arcsec/cy)
print(f"GR check: {gr_per_orbit*orbits_per_cy/mas_to_rad/1000:.2f} arcsec/cy")
for label, sig in (("INPOP15a criterion 1, 1 sigma", 3.1), ("INPOP15a mean, 1 sigma", 2.075), ("INPOP15a criterion 1, 2 sigma", 6.2)):
    lim = sig*mas_to_rad/orbits_per_cy
    print(f"{label:32s}: |anomalous advance| < {sig} mas/cy = {lim:.3e} rad/orbit ({sig/42980:.1e} of GR) -> beta < {lim/gated_per_beta:.1e}")
print(f"agent's illustrative criterion (gated shift < GR's own precession): beta < {gr_per_orbit/2.08824:.2e} (leading order), "
      f"{gr_per_orbit/gated_per_beta:.2e} (measured first-order-in-beta precession)")
