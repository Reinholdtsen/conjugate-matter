"""Referee A: internal consistency of section 8.2 (alpha = 4/3 at equal Planck masses) with section 8.4
(a^-6 step with M~ = M_P at the self-dual point a = sqrt(C), C = 1, placed at ~1e14 T_P for lambda = lP).
The Hassan-Rosen Yukawa strength is alpha = (4/3) (M_f c / M_g)^2 with c the ratio of the two background
scale factors (Lueben et al. 2020 eq. 9; Enander-Moertsell 2013 eq. 4.1; re-derived in derivations.py (g)).
Hypothesis tested: the momentum frame's background scale factor is atilde = C/a (a . atilde = C), so c = atilde/a."""
import numpy as np

A0 = 5.193e92                      # num_check.py: radiation rectangle aspect ratio today, Planck units
a_sd_over_a0 = 1 / np.sqrt(A0)     # num_check.py: a/a0 at the square, no g_s (4.39e-47)
print("Normalisation 1 (section 8.4): a = sqrt(C) = 1 at the self-dual epoch ~4.4e14 T_P")
a0 = 1 / a_sd_over_a0
at0 = 1 / a0
c0 = at0 / a0
print(f"  a0 = {a0:.3e}, atilde0 = {at0:.3e}, c0 = atilde0/a0 = {c0:.3e}  (= 1/A0 = {1/A0:.3e})")
print(f"  Yukawa strength today alpha = (4/3) c0^2 = {4/3*c0**2:.2e}  -> torsion balances give no bound")
print(f"  a^-6 term today relative to GR term (M~ = M_P): a0^-6 = {a0**-6:.1e}  (harmless)")
print()
print("Normalisation 2 (what alpha = 4/3 needs): c0 = 1, i.e. a0 = atilde0 = 1 today")
print("  then with M~ = M_P the a^-6 term equals the GR term today; H(z)/H_LCDM = 1/sqrt(1 + a^-6):")
for z in [0.0, 0.5, 1.0, 2.0, 1100.0]:
    a = 1 / (1 + z)
    print(f"    z = {z:6.1f}: a^-6 = {a**-6:9.3e}, H/H_LCDM = {1/np.sqrt(1 + a**-6):.3e}")
print("  -> grossly excluded by distance measurements (and by the CMB): the two sections need different normalisations")
