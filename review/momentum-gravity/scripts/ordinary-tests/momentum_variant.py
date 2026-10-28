"""(1) EIH two-body interaction in the CM frame (prior art: a relative-velocity-dependent correction to Newton).
(2) Momentum-difference variant |m1 v1 - m2 v2|: boost behaviour, CM-frame reduction, numbers.
"""
import sympy as sp
import numpy as np

# ---------------------------------------------------------------- (1) EIH in the CM frame
m1, m2, G, c, r = sp.symbols('m1 m2 G c r', positive=True)
vx, vy, vz, nx, ny, nz = sp.symbols('v_x v_y v_z n_x n_y n_z', real=True)
M = m1 + m2
nu = m1 * m2 / M**2
v = sp.Matrix([vx, vy, vz])
n = sp.Matrix([nx, ny, nz])
v1 = m2 / M * v
v2 = -m1 / M * v
# EIH interaction bracket (Landau-Lifshitz sec. 106, from memory):
#   (G m1 m2 / (2 c^2 r)) [3(v1^2 + v2^2) - 7 v1.v2 - (n.v1)(n.v2)]
br = 3 * (v1.dot(v1) + v2.dot(v2)) - 7 * v1.dot(v2) - n.dot(v1) * n.dot(v2)
target = (3 + nu) * v.dot(v) + nu * n.dot(v)**2
print("EIH bracket in CM frame equals (3+nu) v^2 + nu (n.v)^2 :", sp.simplify(br - target) == 0)
print("  -> 1PN interaction (G m1 m2/r)[1 + ((3+nu) v^2 + nu (n.v)^2)/(2c^2)], v = v1 - v2, nu = m1 m2/M^2")

# ---------------------------------------------------------------- (2) momentum variant
V = sp.Matrix(sp.symbols('V_x V_y V_z', real=True))
dp = m1 * (v1 + V) - m2 * (v2 + V)
print("m1 v1 - m2 v2 in a frame where the CM moves at V:", sp.simplify(dp - ((m1 - m2) * V + 2 * m1 * m2 / M * v)) == sp.zeros(3, 1),
      "  [ = (m1 - m2) V + 2 mu v ]")

# numbers
c_kms = 299792.458
keV_c = 1.602176634e-16 / 2.99792458e8      # kg m/s per keV/c
p_gate = 20.0 * keV_c                        # chi benchmark fiber width mu ~ 20 keV/c (lab notebook #1 sec. 5.1, not machine-checked)
m_N = 1.67492750e-27
m_e = 9.1093837e-31
pairs = {
    'nucleon-nucleon (mu = m_N/2)': m_N / 2,
    'electron-electron (mu = m_e/2)': m_e / 2,
    '1 kg - 1 kg (mu = 0.5 kg)': 0.5,
    'Earth-Moon (mu = 7.2e22 kg)': 5.97e24 * 0.073e24 / (5.97e24 + 0.073e24),
}
print(f"\nGalilean-invariant relative momentum k = mu |v1 - v2| (the variable of #11 sec. 8). With p* = 20 keV/c = {p_gate:.3e} kg m/s,")
print("the equivalent velocity gate v*_pair = p*/mu:")
for name, mu_ in pairs.items():
    print(f"  {name:32s}: v*_pair = {p_gate/mu_:.3e} m/s")

# boost dominance for the literal variant in the CMB frame
V_cmb = 370.0  # km/s (Will 2014: Earth moves at about 370 km/s relative to the CMB frame)
m_sun = 1.989e30
cases = {
    'Sun-Earth': (m_sun, 5.97e24, 29.78),
    'Sun-Mars': (m_sun, 0.642e24, 24.13),
    'Earth-Moon': (5.97e24, 0.073e24, 1.025),
    'Earth-LAGEOS(407 kg)': (5.97e24, 407.0, 5.70),
}
print(f"\nLiteral variant |m1 v1 - m2 v2| in a frame where the pair's CM moves at V = {V_cmb} km/s:")
for name, (a_, b_, vrel) in cases.items():
    mu_ = a_ * b_ / (a_ + b_)
    ratio = 2 * mu_ * vrel / ((a_ - b_) * V_cmb)
    print(f"  {name:22s}: orbital part / boost part = 2 mu v/((m1-m2) V) = {ratio:.2e}")
