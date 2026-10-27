"""Referee A: small checks of conventions and wording-level numbers."""
import numpy as np

print("(1) CKN factor conventions, Lambda_UV / sqrt(M_P/L) for several ways of writing the black-hole bound")
convs = {
    "reduced Planck mass in L^3 Lambda^4 <= L Mbar^2": (8 * np.pi)**-0.25,
    "sphere radius L, energy (4pi/3)L^3 Lambda^4 <= M_BH = L M_P^2/2": (3 / (8 * np.pi))**0.25,
    "cube side L, BH radius L: L^3 Lambda^4 <= L M_P^2/2": 0.5**0.25,
    "cube side L, BH radius L/2: L^3 Lambda^4 <= L M_P^2/4": 0.25**0.25,
    "sphere of diameter L: (pi/6) L^3 Lambda^4 <= (L/2) M_P^2/2": (3 / (2 * np.pi))**0.25,
    "sphere radius L, rho = Lambda^4/(16 pi^2) (one-loop vacuum energy)": (6 * np.pi)**0.25,
}
for k, v in convs.items():
    print(f"   {v:6.3f}   {k}")
print("   manuscript: 'factors between 0.45 and 2.1' -> 0.45 reproduced; 2.1 only with the rho = Lambda^4/16pi^2 assumption")
print()
print("(2) section 2 table, row 'One cell': sides = one wavelength w and hbar/w")
w = 1.0; hbar = 1.0; h = 2 * np.pi * hbar
print(f"   area = w * hbar/w = hbar = {hbar/h:.4f} h  (table says 1 in units of h; 1 only if the momentum side is h/w)")
print()
print("(3) section 7 'This halves the exponent'")
lam_over_lP = 3.2033e30; Lam_lP2 = 2.849e-122; LL_over_lP = 1.0260e61
print(f"   log10(Lambda lP^2) = {np.log10(Lam_lP2):.2f}; log10(lambda/lP) = {np.log10(lam_over_lP):.2f} (a quarter of 121.5);"
      f" log10(L_L/lP) = {np.log10(LL_over_lP):.2f} (half of it is {np.log10(LL_over_lP)/2:.2f})")
print()
print("(4) section 6 |Z| = 1 reading: aspect ratio (principal axes) e^d with d = s on Z = tanh s + i sech s")
s = np.log(1e92)
print(f"   s = ln(1e92) = {s:.2f}: X = tanh s = 1 - {1-np.tanh(s):.1e}, Y = sech s = {1/np.cosh(s):.2e}")
print()
print("(5) Hubble rectangle near a loop-quantum-cosmology bounce (Planck units; rho_c = 0.41 rho_P assumed, SM g* = 106.75)")
from scipy.special import zeta as _z
rho_c = 0.41
H2 = lambda rho: 8 * np.pi / 3 * rho * (1 - rho / rho_c)
rho_m = rho_c / 2
Hmax = np.sqrt(H2(rho_m))
Tm = (30 * rho_m / (np.pi**2 * 106.75))**0.25
mean = np.pi**4 / (30 * _z(3))
print(f"   H_max = {Hmax:.3f} / t_P at rho = rho_c/2, T = {Tm:.3f} T_P; Hubble rectangle A = (2/H)/(2 <E> T) = {(2/Hmax)/(2*mean*Tm):.2f}; at the bounce H = 0 -> A infinite")
