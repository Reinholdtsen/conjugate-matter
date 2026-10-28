"""verify-critic-numbers, claim c6E: Vainshtein radii of the Sun for the program's X.

Formulas, all from Enander and Mortsell, JHEP (2013), arXiv:1306.1086, sec. 5 [S, eqs. read on ar5iv]:
  m1^2 = m^2 (beta1 + beta2 c), m2^2 = m^2 (beta2 c + beta3 c^2), m_g^2 = (1/c + c)(m1^2 + m2^2)   (eqs. 38-39)
  eq. 40 (all fields except F):  r_V^3 = GM (1 + c^2)^3 m2^2 /(c^3 m_g^4)
  eq. 41 (field F):              r_V^3 = GM (1 + c^2)^3 (7 m1^2 + 8 m2^2)/(c^3 m_g^4)
  eq. 43 (m1 = 0, 'common to all fields'): r_V^3 = GM c^2 (1 + c^-2)^2 / m_g^2
with lambda_X = 1/m_g (hbar = c = 1; restore c: GM -> GM/c^2).  c is the background ratio (u in the
diameter note).  The program's vacuum: c = u = 1 and palindromic beta3 = beta1, hence m1 = m2.
Planet semi-major axes (dagger, standard values): Saturn 9.5826 AU, Pluto 39.482 AU.
"""
import numpy as np

G = 6.67430e-11; C = 299792458.0; Msun = 1.98847e30; AU = 1.495978707e11; pc = 3.085677581e16
rS = 2 * G * Msun / C**2
GMc2 = G * Msun / C**2


def coef(cbg=1.0, m1sq=1.0, m2sq=1.0, which='40'):
    """returns K with r_V^3 = K * (GM/c^2) * lambda^2"""
    mg2 = (1 / cbg + cbg) * (m1sq + m2sq)
    if which == '40':
        return (1 + cbg**2) ** 3 * m2sq / (cbg**3 * mg2**2) * mg2
    if which == '41':
        return (1 + cbg**2) ** 3 * (7 * m1sq + 8 * m2sq) / (cbg**3 * mg2**2) * mg2
    if which == '43':
        return cbg**2 * (1 + cbg**-2) ** 2


cases = [("eq.43 (m1 = 0), c = 1  [critic, repo]", coef(1.0, 0.0, 1.0, '43')),
         ("eq.40, c = 1, m1 = m2 (palindromic)", coef(1.0, 1.0, 1.0, '40')),
         ("eq.41 field F, c = 1, m1 = m2", coef(1.0, 1.0, 1.0, '41')),
         ("eq.40, c = 1, m1 = 0 (consistency with 43)", coef(1.0, 0.0, 1.0, '40'))]
print(f"r_S(Sun) = {rS:.2f} m")
for name, K in cases:
    lam_sat = np.sqrt((9.5826 * AU) ** 3 / (K * GMc2))
    lam_plu = np.sqrt((39.482 * AU) ** 3 / (K * GMc2))
    rV1k = (K * GMc2 * (1e3 * pc) ** 2) ** (1 / 3) / AU
    rV1k2 = (K * 2 * GMc2 * (1e3 * pc) ** 2) ** (1 / 3) / AU
    print(f"{name:44s}: r_V^3 = {K:5.2f} GM lambda^2/c^2 = {K/2:5.2f} r_S lambda^2 | Saturn needs lambda > {lam_sat/pc:6.3f} pc,"
          f" Pluto {lam_plu/pc:6.3f} pc | lambda = 1 kpc: r_V(Sun) = {rV1k:6.0f} AU, r_V(2 Msun) = {rV1k2:6.0f} AU")
r1 = (2 * (2 * G * 1.0 / C**2) * (50e-6) ** 2) ** (1 / 3)
r1b = ((2 * G * 1.0 / C**2) * (50e-6) ** 2) ** (1 / 3)
r1c = (15 * (2 * G * 1.0 / C**2) * (50e-6) ** 2) ** (1 / 3)
print(f"\n1 kg, lambda = 50 um: eq.43 {r1:.2e} m; eq.40 palindromic {r1b:.2e} m; eq.41 palindromic {r1c:.2e} m")
