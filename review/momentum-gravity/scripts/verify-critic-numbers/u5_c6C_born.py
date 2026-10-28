"""verify-critic-numbers, claim c6C: strength of a long-range (1/r) chi-chi attraction that gives
sigma_T/m = 30 cm^2/g at v = 30 km/s (dwarf cores), in the Born regime; and the Sommerfeld parameter.

Potential V = -alpha e^{-r/b}/r, alpha = Gt m^2, screening length b = the system size (the 1/r force has no
other cutoff).  Born amplitude f = 2 mu alpha/(hbar^2 (q^2 + 1/b^2)), mu = m/2, k = mu v/hbar.  Then exactly
    sigma_T = int (1 - cos th) |f|^2 dOmega = (2 pi alpha^2/(mu^2 v^4)) [ln(1 + 4k^2 b^2) - 4k^2b^2/(1 + 4k^2b^2)]
[D, my integration; checked numerically below].  The classical (Rutherford with cutoffs b90, b) form
replaces the log by 2 ln(b/b90) with b90 = alpha/(mu v^2).  Regime: eta = alpha/(hbar v) = b90 k; eta << 1 is Born.
Inputs: m = 70 MeV (record benchmark), v = 30 km/s relative, sigma_T/m = 30 cm^2/g, b = 2.385 kpc
(the clumping analysis's dwarf isothermal core radius; also 1 and 5 kpc), CODATA constants.
"""
import numpy as np
import mpmath as mp

G = 6.67430e-11; hbar = 1.054571817e-34; c = 299792458.0; MeV = 1.602176634e-13; kpc = 3.085677581e19
m = 70 * MeV / c**2
mu = m / 2
S = 30e-4 / 1e-3           # 30 cm^2/g in m^2/kg
v = 30e3


def sigmaT_born(Gt, b, v=v):
    al = Gt * m**2
    k = mu * v / hbar
    x = 4 * k**2 * b**2
    return 2 * np.pi * al**2 / (mu**2 * v**4) * (np.log1p(x) - x / (1 + x))


def sigmaT_born_numeric(Gt, b, v=v):
    al = Gt * m**2
    k = mu * v / hbar
    kap = 1 / b
    # sigma_T = (2 mu al/hbar^2)^2 (pi/k^4) int_0^{2k} q^3/(q^2+kap^2)^2 dq ; substitute q = kap*exp(y)
    pref = (2 * mu * al / hbar**2) ** 2 * mp.pi / k**4
    f = lambda y: (kap * mp.e**y) ** 4 / ((kap * mp.e**y) ** 2 + kap**2) ** 2
    ymax = mp.log(2 * k / kap)
    return float(pref * mp.quad(f, [-60, 0, ymax]))


def sigmaT_classical(Gt, b, v=v):
    al = Gt * m**2
    b90 = al / (mu * v**2)
    return 4 * np.pi * b90**2 * np.log(b / b90)   # = (4 pi al^2/(mu^2 v^4)) ln(b/b90)


def solve(fun, b):
    lo, hi = 1e20, 1e45
    for _ in range(300):
        mid = np.sqrt(lo * hi)
        if fun(mid * G, b) / m < S:
            lo = mid
        else:
            hi = mid
    return np.sqrt(lo * hi)


b0 = 2.385 * kpc
Gt_test = 3.5e31 * G
print(f"check of the closed form vs numerical q-integral at Gt/G = 3.5e31, b = 2.385 kpc: "
      f"{sigmaT_born(Gt_test, b0):.6e} vs {sigmaT_born_numeric(Gt_test, b0):.6e} m^2")
for bk in (1.0, 2.385, 5.0, 40.8):
    b = bk * kpc
    gB = solve(sigmaT_born, b)
    gC = solve(sigmaT_classical, b)
    k = mu * v / hbar
    eta = gB * G * m**2 / (hbar * v)
    print(f"b = {bk:6.3f} kpc: Born Gt/G = {gB:.4e} (ln-factor/2 = {0.5*(np.log1p(4*k**2*b**2) - 1):.2f}); "
          f"classical (self-consistent log) Gt/G = {gC:.4e}; eta(Born solution) = {eta:.3e}")
lnN = 155.1
gt_lnN = np.sqrt(S * m * mu**2 * v**4 / (4 * np.pi * (G * m**2) ** 2 * lnN))
print(f"classical with ln Lambda = ln N = 155.1 held fixed (C14's choice): Gt/G = {gt_lnN:.4e}")
print(f"Sommerfeld parameter Gt m^2/(hbar v) at Gt/G = 3.56e31, v = 30 km/s: {3.56e31*G*m**2/(hbar*v):.4e}")
print(f"(m/M_Planck)^2 = G m^2/(hbar c) = {G*m**2/(hbar*c):.4e}")
