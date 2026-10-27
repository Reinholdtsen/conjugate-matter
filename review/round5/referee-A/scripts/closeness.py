"""Referee A: test the claim (section 4) that the closeness of the radiation per-axis count S^(1/3) ~ 1.0e30
to the horizon count S_dS^(1/4) ~ 4.3e30 'is today's coincidence ... it holds at no other epoch'.
Three readings of 'the two counts at another epoch'. Planck 2018 (H0 = 67.4, Om = 0.315), T0 = 2.7255 K."""
import numpy as np
from scipy.integrate import quad
from scipy.special import zeta

h = 6.62607015e-34; hbar = h / (2 * np.pi); c = 299792458.0; kB = 1.380649e-23; G = 6.67430e-11
Mpc = 3.0856775814913673e22; Gly = 9.4607304725808e24
lP = np.sqrt(hbar * G / c**3)
H0 = 67.4e3 / Mpc; Om = 0.315; T0 = 2.7255
a_rad = np.pi**2 * kB**4 / (15 * hbar**3 * c**3)
rho_crit = 3 * H0**2 / (8 * np.pi * G)
Og = a_rad * T0**4 / c**2 / rho_crit
Or = Og * (1 + 7/8 * (4/11)**(4/3) * 3.046)
OL = 1 - Om - Or
E = lambda a: np.sqrt(Or / a**4 + Om / a**3 + OL)
chi = lambda a: c / H0 * quad(lambda x: 1 / (x**2 * E(x)), 0, a, limit=800, points=[1e-8, 1e-6, 1e-4, 1e-2])[0]
gs0 = 2 + 7/8 * 6 * 4/11
s_today = (2 * np.pi**2 / 45) * gs0 * (kB * T0 / (hbar * c))**3        # entropy density today, units k_B / m^3
chi0 = chi(1.0)
S0 = s_today * 4/3 * np.pi * chi0**3
L_L = c / (H0 * np.sqrt(OL))
S_dS = np.pi * L_L**2 / lP**2
print(f"today: S^(1/3) = {S0**(1/3):.3e}, S_dS^(1/4) = {S_dS**0.25:.3e}, ratio = {S0**(1/3)/S_dS**0.25:.3f}")
print()
print("Reading (i): the fixed comoving region (today's observable universe) and S_dS: S is conserved")
print("  (total radiation entropy, all species, since reheating), S_dS is constant -> ratio = %.3f at every epoch" % (S0**(1/3) / S_dS**0.25))
print()
print("Reading (ii): radiation entropy inside the particle horizon at epoch a, against S_dS")
print("   a          z            chi(a) [Gly comoving]   S_ph^(1/3)      ratio to S_dS^(1/4)")
for a in [1e-9, 1e-6, 1e-4, 1/1101, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0, 1e4]:
    ch = chi(a)
    Sph = s_today * 4/3 * np.pi * ch**3          # comoving entropy density is conserved (ignoring g_s steps before 1 MeV)
    print(f"  {a:9.3g}  {1/a - 1:12.4g}   {ch/Gly:12.4f}            {Sph**(1/3):.3e}       {Sph**(1/3)/S_dS**0.25:.3e}")
chi_inf = chi(1.0) + c / H0 * quad(lambda x: 1 / (x**2 * E(x)), 1.0, np.inf, limit=800)[0]
Sinf = s_today * 4/3 * np.pi * chi_inf**3
print(f"  a -> inf: chi_inf = {chi_inf/Gly:.3f} Gly, ratio -> {Sinf**(1/3)/S_dS**0.25:.3f}")
print()
print("Reading (iii): radiation in the Hubble sphere at epoch a against that sphere's horizon entropy pi (c/H)^2/lP^2")
print("   (photons+neutrinos only, conserved comoving entropy density; g_s steps ignored)")
for a in [1e-9, 1e-6, 1e-4, 1/3400, 1/1101, 0.1, 1.0, 10.0]:
    RH = c / (H0 * E(a))
    s_a = s_today / a**3
    Srad = s_a * 4/3 * np.pi * RH**3
    SH = np.pi * RH**2 / lP**2
    print(f"  a = {a:9.3g}:  S_rad,H^(1/3) = {Srad**(1/3):.3e}   S_H^(1/4) = {SH**0.25:.3e}   ratio = {Srad**(1/3)/SH**0.25:.3f}")
print()
# decomposition of today's ratio: 0.852 (T0/rho_L^(1/4)) (R/L_L)
rhoL_q = (3 * OL * H0**2 / (8 * np.pi * G) * c**2 * (hbar * c)**3)**0.25 / kB   # in kelvin
pref = ((8 * np.pi**3 * gs0 / 135)**(1/3)) / ((8 * np.pi**2 / 3)**0.25)
print(f"decomposition today: prefactor {pref:.3f} x (T0/rho_L^(1/4) = {T0/rhoL_q:.4f}) x (R/L_L = {chi0/L_L:.3f}) = {pref*T0/rhoL_q*chi0/L_L:.3f}")
