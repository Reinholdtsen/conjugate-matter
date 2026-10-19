"""Cross-check the gamma gamma -> W+W- tree formula (Baillargeon-Belanger-Boudjema hep-ph/9405359 eqs. 5.15/5.16),
then get W+W- -> gamma gamma at threshold by detailed balance. Units: pi alpha^2/M^2."""
import numpy as np
from scipy.integrate import quad
def dsig(c, g):  # in units of pi alpha^2/M^2
    b = np.sqrt(1-4/g); D = 4/(1-b**2*c**2)
    return 3*b/g*(1 - D*(2/3+1/g) + 2*D**2*(1/3+1/g**2))
def sig_int(g): return quad(dsig, -1, 1, args=(g,))[0]
def sig_516(g, sign=-1, binv=True):
    b = np.sqrt(1-4/g)
    pref = 6/(b*g**2) if binv else 6*b/g**2
    return 8*b*((1+3/(4*g)+3/g**2) + sign*pref*(1-2/g)*np.arccosh(np.sqrt(g)/2))
for g in [4.0001, 4.01, 5, 10, 100, 1e4]:
    print(f"gamma={g:<8} int(5.15)={sig_int(g):.5f}  (5.16,-,1/b)={sig_516(g,-1,True):.5f}  (5.16,-,b)={sig_516(g,-1,False):.5f} (5.16,+,1/b)={sig_516(g,+1,True):.5f}  ratio int/beta={sig_int(g)/np.sqrt(1-4/g):.4f}")
# detailed balance near threshold: sigma(WW->gg) = sigma(gg->WW) * (p_g/p_W)^2 * (g_gamma^2/g_W^2) * (1/2 identical photons)
g = 4.0001; b = np.sqrt(1-4/g)
sgg = sig_int(g)
sWW = sgg * (1/b**2) * (4/9) * 0.5
vrel = 2*b
print(f"near threshold: sigma(gg->WW)/beta = {sgg/b:.4f} pi a^2/M^2 ; sigma v_rel (W+W- -> gg) = {sWW*vrel:.4f} pi a^2/M^2")
