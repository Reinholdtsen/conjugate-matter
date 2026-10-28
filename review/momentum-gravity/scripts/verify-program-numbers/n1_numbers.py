# Independent recomputation of the simple numbers in the 'program' agent's claims P1-P20.
# Written without reading the agent's scripts. SI throughout, converted at the end;
# a different route from natural-unit arithmetic where the agent likely used it.
from math import pi, sqrt, log, exp, atan, asin, log10

# --- constants (CODATA 2018 exact / recommended; IAU nominal) -------------------------
c = 299792458.0
hbar = 1.054571817e-34
G = 6.67430e-11
eV = 1.602176634e-19
GeV = 1e9 * eV
GM_sun = 1.32712440018e20          # m^3 s^-2 (IAU)
AU = 1.495978707e11
pc = 3.0856775814913673e16
kpc = 1e3 * pc
Mpc = 1e6 * pc
M_sun = GM_sun / G
hbarc_eVm = hbar * c / eV          # eV m
M_Pl_kg = sqrt(hbar * c / G)
M_Pl_eV = M_Pl_kg * c**2 / eV      # unreduced
M_Pl_red_eV = M_Pl_eV / sqrt(8 * pi)
kms = 1e3
print(f"hbar c = {hbarc_eVm:.6e} eV m ; M_Pl = {M_Pl_eV/1e9:.6e} GeV ; reduced = {M_Pl_red_eV/1e9:.4e} GeV")

def mass_eV_for_range(lam_m):
    return hbarc_eVm / lam_m

# --- P1: range bound <-> mass ---------------------------------------------------------
print("\n== P1")
for lam in (37.68e-6, 56.98e-6, 42.53e-6, 30.83e-6):
    print(f"lambda = {lam*1e6:.2f} um -> M c^2 = {mass_eV_for_range(lam)*1e3:.4f} meV")

# --- P2: G m_chi^2, range of m_phi = m_chi --------------------------------------------
print("\n== P2")
m_chi_eV = 70e6
m_chi_kg = m_chi_eV * eV / c**2
Gm2 = G * m_chi_kg**2 / (hbar * c)   # dimensionless gravitational coupling
print(f"G m_chi^2/(hbar c) = {Gm2:.4e} ; 1/that = {1/Gm2:.4e}  (alpha~ = 1)")
print(f"range hbar/(m_chi c) = {hbar/(m_chi_kg*c):.4e} m")
# Debt 3a coupling and shortfall, recomputed in SI then converted
sig0_over_m = 30e-4 / 1e-3        # 30 cm^2/g -> m^2/kg
sig0 = sig0_over_m * m_chi_kg     # m^2
print(f"sigma0 = {sig0*1e4:.4e} cm^2")
# g = sqrt(pi sigma0)/m in natural units; convert: g [GeV^-2] = sqrt(pi*sigma0[GeV^-2])/m[GeV]
GeVinv_m = hbar * c / GeV          # 1 GeV^-1 in metres
sig0_GeV = sig0 / GeVinv_m**2
g_nat = sqrt(pi * sig0_GeV) / (m_chi_eV / 1e9)
print(f"g = sqrt(pi sigma0)/m = {g_nat:.4e} GeV^-2  (record 2.48e3)")
def eps_ratio(rho_GeV_cm3, sigma_kms, vstar_kms=120.0):
    n_cm3 = rho_GeV_cm3 / (m_chi_eV / 1e9)
    n_GeV3 = n_cm3 * (GeVinv_m * 100) ** 3     # cm^-3 -> GeV^3
    s = sigma_kms * kms / c
    vs = vstar_kms * kms / c
    if sigma_kms > vstar_kms:
        n_GeV3 *= (vstar_kms / sigma_kms) ** 3 / (2 * pi) ** 1.5
    eps = g_nat * n_GeV3
    kin = (m_chi_eV / 1e9) * min(s, vs) ** 2
    return eps, kin, eps / kin
for name, rho, sg in (("dwarf core", 1.0, 30.0), ("MW local", 0.4, 155.0)):
    e, k, r = eps_ratio(rho, sg)
    print(f"{name}: eps_gate = {e:.3e} GeV, m min(sig,v*)^2 = {k:.3e} GeV, ratio = {r:.3e}")

# --- P4: chi-N / chi-chi contact Born ratio -------------------------------------------
print("\n== P4")
m_N_eV = 0.938e9
mu_chiN = m_chi_eV * m_N_eV / (m_chi_eV + m_N_eV)
alpha_X = 4.0 / 3.0
GmN2 = G * (m_N_eV * eV / c**2) ** 2 / (hbar * c)
ratio = (mu_chiN / (m_chi_eV / 2)) ** 2 * alpha_X * GmN2 / 1.0
print(f"(mu_chiN/(m/2))^2 = {(mu_chiN/(m_chi_eV/2))**2:.4f}; alpha G m_N^2 = {alpha_X*GmN2:.4e}; ratio = {ratio:.4e}; sigma_chiN = {ratio*sig0*1e4:.3e} cm^2")
# record's benchmark normalization sigma0 = 16 pi alpha~^2 m^2/m_phi^4 at m_phi = m_chi: which alpha~ gives 30 cm^2/g at 70 MeV?
sig_alpha1 = 16 * pi / (m_chi_eV / 1e9) ** 2 * GeVinv_m**2  # m^2 at alpha~=1
print(f"record normalization: sigma0(alpha~=1, m_phi=m_chi=70 MeV) = {sig_alpha1*1e4:.4e} cm^2 -> sigma0/m = {sig_alpha1/m_chi_kg*10:.2f} cm^2/g; alpha~ for 30 cm^2/g = {sqrt(sig0/sig_alpha1):.3f}")

# --- P6: momentum transfer scale ------------------------------------------------------
print("\n== P6")
for v in (30.0, 120.0, 1000.0):
    q_eV = m_chi_eV * v * kms / c
    l = hbarc_eVm / q_eV
    print(f"v = {v:6.0f} km/s: m v = {q_eV/1e3:.3f} keV ; hbar/(m v) = {l:.4e} m ; 37.7 um/that = {37.7e-6/l:.3e}")

# --- P8: (v/c)^2 ----------------------------------------------------------------------
print("\n== P8")
for v in (100.0, 120.0, 300.0):
    print(f"v = {v:5.0f} km/s: (v/c)^2 = {(v*kms/c)**2:.4e}")

# --- P9: Cassini ----------------------------------------------------------------------
print("\n== P9")
gm1_lo = 2.1e-5 - 2 * 2.3e-5
# gamma - 1 = -alpha/(2(1+alpha)) > gm1_lo  ->  alpha < 2|g|/(1-2|g|)
x = -gm1_lo
alpha_max = 2 * x / (1 - 2 * x)
print(f"2-sigma lower end gamma-1 = {gm1_lo:.2e}; alpha_max = {alpha_max:.4e}; u_max = sqrt(3 alpha/4) = {sqrt(0.75*alpha_max):.4e}")
print(f"gamma at alpha = 4/3: {(4/3+2)/(2*(4/3+1)):.6f} (5/7 = {5/7:.6f}); Enander-Mortsell form (1+2c^2/3)/(1+4c^2/3) at c=1: {(1+2/3)/(1+4/3):.6f}")

# --- P13/P20: precession ratio and Mercury --------------------------------------------
print("\n== P13 / P20")
vstar = 120.0 * kms
print(f"(2/3)(c/v*)^2 = {(2/3)*(c/vstar)**2:.4e}")
a_M = 0.387098 * AU; e_M = 0.205630
xM = GM_sun / (a_M * vstar**2)
gated = -4 * pi * xM / (1 - e_M**2)
gr = 6 * pi * GM_sun / (a_M * c**2 * (1 - e_M**2))
print(f"Mercury: GM/(a v*^2) = {xM:.4f}; gated = {gated:.4f} beta rad/orbit; GR = {gr:.4e} rad/orbit; beta at equality = {gr/abs(gated):.3e}")
print(f"  GR per century: {gr*36525/87.9691*206264.806:.2f} arcsec (anchor: 42.98 arcsec/cy)")

# --- P16: inertia parameter -----------------------------------------------------------
print("\n== P16")
for name, phi in (("Earth orbit v=29.8", (29.8*kms)**2), ("MW v_c=230", (230*kms)**2),
                  ("MW, |Phi| = v_esc^2/2 with v_esc = 550 (illustrative)", 0.5*(550*kms)**2),
                  ("dwarf 3 sigma^2, sigma=10", 3*(10*kms)**2), ("UFD 3 sigma^2, sigma=4", 3*(4*kms)**2),
                  ("UFD 3 sigma^2, sigma=3.7", 3*(3.7*kms)**2)):
    print(f"{name:55s}: eps/beta = 2|Phi|/v*^2 = {2*phi/vstar**2:.4f}")
frac = (120/155)**3/(2*pi)**1.5
print(f"co-moving fraction (v*/sigma)^3/(2 pi)^1.5 at sigma = 155: {frac:.4f}; times 7.347 = {frac*2*(230*kms)**2/vstar**2:.4f}")
# Gaussian-gate weighted fraction for a Maxwellian (relative velocity dispersion sqrt(2) sigma per axis)
s = 155.0; vs = 120.0
wfrac = (vs**2/(vs**2 + 4*s**2))**1.5
print(f"alternative definition, <exp(-v_rel^2/v*^2)> over the pair distribution: {wfrac:.4f}")

# --- P17/P18: light X -----------------------------------------------------------------
print("\n== P17 / P18")
H0 = 67.4 * kms / Mpc
hbarH0_eV = hbar * H0 / eV
MX_kpc = mass_eV_for_range(kpc)
print(f"M_X(1 kpc) = {MX_kpc:.4e} eV ; hbar H0 = {hbarH0_eV:.4e} eV ; (M_X/H0)^2 = {(MX_kpc/hbarH0_eV)**2:.4e} ; c/H0 = {c/H0/(1e3*Mpc):.3f} Gpc")
for name, M in (("Sun", M_sun), ("1e10 Msun", 1e10*M_sun), ("Earth", 5.9722e24), ("1 kg", 1.0)):
    rS = 2 * G * M / c**2
    rV = (rS * (1 + 1.0**2) * kpc**2) ** (1/3)
    print(f"r_V({name}, lambda = 1 kpc, u = 1) = {rV:.4e} m = {rV/AU:.4e} AU = {rV/pc:.4e} pc")
# screening criterion for an extended body: r_S(<r)(1+u^2) lambda^2 / r^3 > 1
for name, M, R in (("Earth surface", 5.9722e24, 6.371e6), ("Sun at 1 AU", M_sun, AU),
                   ("MW (1e11 Msun) at 8 kpc", 1e11*M_sun, 8*kpc), ("galaxy 1e10 Msun within 1 kpc", 1e10*M_sun, kpc)):
    rS = 2*G*M/c**2
    print(f"{name:32s}: r_S(1+u^2) lambda^2 / r^3 at lambda = 1 kpc = {rS*2*kpc**2/R**3:.3e}  (screened if >> 1); "
          f"lambda at which = 1: {sqrt(R**3/(2*rS)):.3e} m")
for M_label, Mp in (("reduced", M_Pl_red_eV), ("unreduced", M_Pl_eV)):
    L3 = (MX_kpc**2 * Mp) ** (1/3)
    print(f"Lambda_3 ({M_label} M_Pl) = {L3:.4e} eV ; 1/Lambda_3 = {hbarc_eVm/L3:.4e} m")
L3H = (hbarH0_eV**2 * M_Pl_red_eV) ** (1/3)
print(f"anchor: m = H0 gives 1/Lambda_3 = {hbarc_eVm/L3H/1e3:.0f} km (Hinterbichler: ~10^3 km)")
# Enander-Mortsell excluded window in kpc
rH = c / H0
print(f"Enander-Mortsell window 1e-6 < lambda/r_H < 1e-3 with r_H = c/H0 (H0 = 67.4): {1e-6*rH/kpc:.2f} kpc to {1e-3*rH/Mpc:.2f} Mpc")

# --- P14: Gaussian smoothing tail -----------------------------------------------------
print("\n== P14")
dmax = 1 * exp(-0.5)
print(f"|d/dr exp(-r^2/2)| at r = 10 over its max: {10*exp(-50)/dmax:.4e}")

# --- P19: strength mismatch, classical vs Born Coulomb log ---------------------------
print("\n== P19")
mu_eV = m_chi_eV / 2
v = 30.0 * kms / c
sig0_eV = sig0 / hbarc_eVm**2                 # eV^-2
def sigT_classical(A, lam_m):
    lam = lam_m / hbarc_eVm                   # eV^-1
    b90 = A / (mu_eV * v**2)
    return 2 * pi * b90**2 * log(1 + (lam / b90) ** 2)
def sigT_born(A, lam_m):
    lam = lam_m / hbarc_eVm
    k = mu_eV * v
    X = (2 * k * lam) ** 2
    return 2 * pi * A**2 / (mu_eV**2 * v**4) * (log(1 + X) - X / (1 + X))
def solveA(f, lam_m):
    lo, hi = 1e-30, 1.0
    for _ in range(300):
        mid = sqrt(lo * hi)
        if f(mid, lam_m) < sig0_eV: lo = mid
        else: hi = mid
    return sqrt(lo * hi)
for name, f in (("classical log", sigT_classical), ("Born (exact Yukawa sigma_T)", sigT_born)):
    A = solveA(f, kpc)
    print(f"{name:28s}: A needed = {A:.4e}; A/(G m^2) = {A/Gm2:.4e}")
print(f"Sommerfeld parameter A/v at A = 1.1e-9: {1.1e-9/v:.2e} (<< 1: Born regime, classical log not applicable)")
lam_b90 = None
A = solveA(sigT_classical, kpc)
print(f"classical log value ln(lambda mu v^2/A) = {log((kpc/hbarc_eVm)*mu_eV*v**2/A):.2f}; Born log ln(2 mu v lambda) - 1/2 = {log(2*mu_eV*v*kpc/hbarc_eVm)-0.5:.2f}")
AX = alpha_X * Gm2
for name, f in (("classical log", sigT_classical), ("Born (exact)", sigT_born)):
    s_ = f(AX, 37.7e-6) * hbarc_eVm**2 * 1e4
    print(f"X at alpha = 4/3, 37.7 um, 30 km/s, {name:14s}: sigma_T = {s_:.3e} cm^2 ; /sigma0 = {s_/(sig0*1e4):.3e}")
