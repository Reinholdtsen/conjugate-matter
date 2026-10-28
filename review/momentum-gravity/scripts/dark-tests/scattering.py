"""Pairwise scattering of chi by the long-range gated potential U = -Gt m^2 W(v/v*)/r.

Coulomb-like potential V = -kappa/r, kappa = Gt m^2 W, reduced mass m/2, relative speed v.
Rutherford dsigma/dOmega = (kappa/(2 mu v^2))^2 / sin^4(theta/2) [T] (exact classically and in
quantum mechanics for a pure Coulomb potential; Born amplitude times the gate F for the gated case).
Transfer cross-section: sigma_T = int (1 - cos theta) dsigma = 4 pi (kappa/(mu v^2))^2 ln(1/sin(theta_min/2))
[D here, checked numerically below]; theta_min from the maximum impact parameter b_max (screening by
the finite system): tan(theta/2) = kappa/(mu v^2 b)  ->  Lambda = b_max mu v^2/kappa.
Coulomb (Sommerfeld) parameter eta = kappa/(hbar v): eta << 1 is the quantum (Born) regime.
"""
import numpy as np

G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
eV = 1.602176634e-19
m = 70e6 * eV / c**2          # 70 MeV in kg
mu = m / 2
pc = 3.0856775814913673e16


def sigmaT_over_m(Gt, v, bmax, regime="born"):
    """Transfer cross-section per mass. 'born' (eta << 1, the case here): screened-Coulomb Born result
    sigma_T = 2 pi (kappa/(mu v^2))^2 [ln(1 + (2 k b)^2) - (2kb)^2/(1+(2kb)^2)], k = mu v/hbar [D; the
    angular integral is checked numerically below]; 'classical' (eta >> 1): lnLambda = ln(b mu v^2/kappa)."""
    kappa = Gt * m**2
    if regime == "born":
        x = (2 * mu * v * bmax / hbar) ** 2
        lnL = 0.5 * (np.log1p(x) - x / (1 + x))
    else:
        lnL = np.log(bmax * mu * v**2 / kappa)
    sT = 4 * np.pi * (kappa / (mu * v**2)) ** 2 * lnL
    return sT / m * 10.0, lnL                   # m^2/kg -> cm^2/g (x10)


# numerical check of the transfer-cross-section integral for Rutherford with a cutoff angle
th_min = 1e-6
th = np.geomspace(th_min, np.pi, 2000001)
integrand = (1 - np.cos(th)) / np.sin(th / 2) ** 4 * 2 * np.pi * np.sin(th)
num = np.trapezoid(integrand, th)
ana = 16 * np.pi * np.log(1 / np.sin(th_min / 2))
print("Check: int (1-cos)/sin^4(th/2) dOmega from th_min=1e-6: numeric %.6f, 16 pi ln(1/sin(th_min/2)) = %.6f" % (num, ana))
print("  (so sigma_T = (kappa/(2 mu v^2))^2 * 16 pi lnL = 4 pi (kappa/(mu v^2))^2 lnL)")
# Born, screened Coulomb: dsigma/dOmega ∝ 1/(q^2 + b^-2)^2, q^2 = 2k^2(1-x);
# 2 pi int (1-x)/(q^2+a^2)^2 dx = (pi/2)/k^4 [ln(1+4k^2b^2) - 4k^2b^2/(1+4k^2b^2)]
kk, bb = 1.0, 1e6
t = np.geomspace(1e-20, 2.0, 2000001)
numB = 2 * np.pi * np.trapezoid(t / (2 * kk**2 * t + 1 / bb**2) ** 2, t)
yB = 4 * kk**2 * bb**2
anaB = (np.pi / 2) / kk**4 * (np.log1p(yB) - yB / (1 + yB))
print("Check (Born screened Coulomb transfer integral, k=1, b=1e6): numeric %.8f analytic %.8f" % (numB, anaB))

print("m_chi = 70 MeV = %.4e kg" % m)
for v_kms in [10, 30, 100, 300]:
    v = v_kms * 1e3
    eta = G * m**2 / (hbar * v)
    print("v = %4d km/s: Coulomb parameter eta (Gt=G) = %.3e  (quantum/Born regime: eta << 1)" % (v_kms, eta))
    for bmax_pc in [1.0, 1e3, 1e5]:
        s, lnL = sigmaT_over_m(G, v, bmax_pc * pc)
        sc, lnLc = sigmaT_over_m(G, v, bmax_pc * pc, regime="classical")
        print("    b_max = %7.0e pc: Born lnLambda = %6.1f, sigma_T/m (Gt = G) = %.3e cm^2/g   [classical-log value would be %.3e, lnL %.1f]" % (bmax_pc, lnL, s, sc, lnLc))

# Gt needed to reach 30 cm^2/g at v = 30 km/s, b_max = 1 kpc (iterate lnLambda)
v = 30e3; bmax = 1e3 * pc
Gt = G
for _ in range(50):
    s, lnL = sigmaT_over_m(Gt, v, bmax)
    Gt = Gt * np.sqrt(30.0 / s)
s, lnL = sigmaT_over_m(Gt, v, bmax)
print("To reach sigma_T/m = 30 cm^2/g at v = 30 km/s (b_max = 1 kpc): Gt/G = %.3e (lnLambda = %.1f, check %.2f cm^2/g)" % (Gt / G, lnL, s))
print("  ratio sigma_T/m(Gt=G)/30 at v=30 km/s, b_max=1 kpc: %.3e" % (sigmaT_over_m(G, v, bmax)[0] / 30))
# angular structure: fraction of sigma_T from theta > 90 deg
for v_kms in [30]:
    s, lnL = sigmaT_over_m(G, v_kms * 1e3, 1e3 * pc)
    frac = np.log(1 / np.sin(np.pi / 4)) / lnL
    print("Fraction of sigma_T from theta > 90 deg (Rutherford, lnLambda=%.1f): %.4f -> forward-peaked" % (lnL, frac))
