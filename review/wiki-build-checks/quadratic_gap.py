# Lead for #1 §4's "quadratic effects at M_B ~ M_P sit ~10 orders below current sensitivity".
# Inputs from model memory (†), not from any program source:
#   M_P (non-reduced) = 1.22e19 GeV; reduced M_P = 2.44e18 GeV
#   Fermi-LAT quadratic-dispersion lower limit E_QG,2 ~ 1.3e11 GeV (Vasileiou et al. 2013, GRB 090510) †
from math import log10
EQG2 = 1.3e11
for name, M in (("M_P", 1.22e19), ("reduced M_P", 2.44e18)):
    gap_mass = log10(M / EQG2)          # orders in the energy scale
    gap_effect = 2 * gap_mass           # quadratic effect ∝ (E/M)^2: orders in the size of the effect
    print(f"{name}: scale gap = {gap_mass:.1f} orders; effect-size gap = {gap_effect:.1f} orders")
