"""Referee A: independent recomputation of every number in the manuscript.
Constants: CODATA 2018 (exact SI h, c, k_B, e; G = 6.67430e-11), Planck 2018
(H0 = 67.4 km/s/Mpc, Om = 0.315 as the manuscript states; also 67.36/0.3153 for
sensitivity), T0 = 2.7255 K (Fixsen 2009), N_eff = 3.046.
Each line prints: label | manuscript value | my value.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import zeta

# ---------------- constants (CODATA 2018 / IAU) ----------------
h = 6.62607015e-34
hbar = h / (2 * np.pi)
c = 299792458.0
kB = 1.380649e-23
e = 1.602176634e-19
G = 6.67430e-11
eps0 = 8.8541878128e-12
me = 9.1093837015e-31
alpha_fs = 7.2973525693e-3
a0_bohr = 5.29177210903e-11
Mpc = 3.0856775814913673e22
ly = 9.4607304725808e15
Gly = 1e9 * ly
au = 1.495978707e11
eV = e
g_n = 9.80665

lP = np.sqrt(hbar * G / c**3)
mP = np.sqrt(hbar * c / G)
TP = np.sqrt(hbar * c**5 / G) / kB
EP_eV = mP * c**2 / eV
hbarc_eVm = hbar * c / eV
z3 = zeta(3)

def show(label, ms, mine, fmt="{:.4g}"):
    print(f"{label:70s} | ms: {ms:>14s} | mine: " + fmt.format(mine))

print("Planck units: lP = %.6e m, mP = %.6e kg, TP = %.6e K, EP = %.5e eV" % (lP, mP, TP, EP_eV))
print()

# ---------------- kappa ----------------
mean_E_over_kT = np.pi**4 / (30 * z3)
kappa = 3**(1/3) * np.pi**(10/3) / (30 * z3**(4/3))
show("kappa (sphere, D_p = 2<|p|>)", "1.708", kappa, "{:.5f}")
show("<E>/kT", "pi^4/30zeta3", mean_E_over_kT, "{:.5f}")
show("kappa with D_p = kT/c", "0.316", kappa / (2 * mean_E_over_kT), "{:.5f}")
show("kappa with D_p = <|p|>", "0.854", kappa / 2, "{:.5f}")
show("kappa for cube of side D_x", "1.377", kappa / (6/np.pi)**(1/3), "{:.5f}")
print()

# ---------------- cosmology ----------------
def cosmo(H0kms=67.4, Om=0.315, T0=2.7255, Neff=3.046):
    H0 = H0kms * 1e3 / Mpc
    hh = H0kms / 100
    # photon density parameter
    a_rad = np.pi**2 * kB**4 / (15 * hbar**3 * c**3)  # energy density = a_rad T^4  (J/m^3)
    rho_gamma = a_rad * T0**4 / c**2
    rho_crit = 3 * H0**2 / (8 * np.pi * G)
    Og = rho_gamma / rho_crit
    Or = Og * (1 + 7/8 * (4/11)**(4/3) * Neff)
    OL = 1 - Om - Or
    E = lambda a: np.sqrt(Or / a**4 + Om / a**3 + OL)
    chi_ph = c / H0 * quad(lambda a: 1 / (a**2 * E(a)), 0, 1, limit=500, points=[1e-6, 1e-4, 1e-2])[0]
    ceh = c / H0 * quad(lambda a: 1 / (a**2 * E(a)), 1, np.inf, limit=500)[0]
    chi_inf = chi_ph + ceh
    return dict(H0=H0, Og=Og, Or=Or, OL=OL, chi_ph=chi_ph, ceh=ceh, chi_inf=chi_inf, E=E)

C = cosmo()
H0 = C["H0"]; OL = C["OL"]
show("Omega_r (photons + 3.046 massless nu)", "-", C["Or"], "{:.4e}")
show("Omega_Lambda = 1 - Om - Or", "(0.685)", OL, "{:.5f}")
show("particle horizon today [Gly]", "46.1", C["chi_ph"] / Gly, "{:.3f}")
show("particle horizon today [m]", "4.36e26", C["chi_ph"], "{:.4e}")
show("chi H0/c", "3.18", C["chi_ph"] * H0 / c, "{:.4f}")
show("cosmic event horizon today [Gly]", "16.7", C["ceh"] / Gly, "{:.3f}")
show("comoving particle horizon at t->inf [Gly]", "-", C["chi_inf"] / Gly, "{:.3f}")
C2 = cosmo(67.36, 0.3153)
show("  sensitivity: particle horizon for 67.36/0.3153 [Gly]", "-", C2["chi_ph"] / Gly, "{:.3f}")
show("  sensitivity: CEH for 67.36/0.3153 [Gly]", "-", C2["ceh"] / Gly, "{:.3f}")
print()

T0 = 2.7255
n_gamma = 2 * z3 / np.pi**2 * (kB * T0 / (hbar * c))**3
show("n_gamma today [cm^-3]", "-", n_gamma * 1e-6, "{:.2f}")
R = 46.1 * Gly  # manuscript's radius
V = 4/3 * np.pi * R**3
Ng = n_gamma * V
show("N_gamma (R = 46.1 Gly)", "1.43e89", Ng, "{:.4e}")
Rmine = C["chi_ph"]
show("N_gamma (R = my particle horizon)", "-", n_gamma * 4/3*np.pi*Rmine**3, "{:.4e}")
gs0 = 2 + 7/8 * 2 * 3 * (4/11)   # 3.909
s_per_photon_gamma = 2 * np.pi**4 / (45 * z3)
show("g_s today", "3.909", gs0, "{:.4f}")
show("entropy per photon, photons only", "3.60", s_per_photon_gamma, "{:.4f}")
show("entropy per photon, photons + neutrinos", "7.04", s_per_photon_gamma * gs0 / 2, "{:.4f}")
S = s_per_photon_gamma * gs0 / 2 * Ng
show("S (photons + neutrinos), units k_B", "1.01e90", S, "{:.4e}")
show("S photons only (R = 46.1 Gly)", "(E&L: 5.40e89)", s_per_photon_gamma * Ng, "{:.4e}")
Dx = 2 * R
Dp = 2 * mean_E_over_kT * kB * T0 / c
show("D_x [m]", "8.73e26", Dx, "{:.4e}")
show("D_p [kg m/s]", "6.78e-31", Dp, "{:.4e}")
area_h = Dx * Dp / h
show("D_x D_p / h", "8.9e29", area_h, "{:.4e}")
show("kappa N^(1/3) (consistency)", "8.9e29", kappa * Ng**(1/3), "{:.4e}")
show("S^(1/3)", "1.0e30", S**(1/3), "{:.4e}")
show("N_gamma^(1/3)", "-", Ng**(1/3), "{:.4e}")
show("(11/4)^(1/3)", "1.40", (11/4)**(1/3), "{:.4f}")
show("(106.75/3.909)^(1/3)", "3.01", (106.75/gs0)**(1/3), "{:.4f}")
print()

# ---------------- section 4 ----------------
L_H = c / H0
show("c/H0 [m]", "1.37e26", L_H, "{:.5e}")
show("L/lP (Hubble)", "8.49e60", L_H / lP, "{:.4e}")
show("(L/lP)^3", "6.12e182", (L_H / lP)**3, "{:.4e}")
L_L = c / (H0 * np.sqrt(OL))
show("L_Lambda = c/(H0 sqrt(OL)) [m]", "1.66e26", L_L, "{:.5e}")
S_dS = np.pi * L_L**2 / lP**2
show("Gibbons-Hawking pi L_Lambda^2/lP^2", "3.31e122", S_dS, "{:.4e}")
S_ceh = np.pi * C["ceh"]**2 / lP**2
show("pi R_CEH^2/lP^2 (my CEH)", "3.0e122", S_ceh, "{:.4e}")
S_ceh_ms = np.pi * (16.7 * Gly)**2 / lP**2
show("pi R^2/lP^2 at 16.7 Gly", "3.0e122", S_ceh_ms, "{:.4e}")
# Bousso N = 3 pi / Lambda (Planck units), Lambda = 3/L_L^2
Lam = 3 / L_L**2
show("Bousso N = 3 pi/(Lambda lP^2)", "= S_dS", 3 * np.pi / (Lam * lP**2), "{:.4e}")
ckn = np.sqrt(EP_eV * hbarc_eVm / L_H)
show("CKN sqrt(M_P/L), L = c/H0 [meV]", "4.19", ckn * 1e3, "{:.4f}")
show("CKN with L = 1e26 m [eV, log10]", "~10^-2.5", np.log10(np.sqrt(EP_eV * hbarc_eVm / 1e26)), "{:.3f}")
# Born 1938 b c from classical electron radius
r_e = 2.8179403262e-15
show("hbar c / r_e [eV]", "(b c ~ 1.4e8 eV)", hbarc_eVm / r_e, "{:.4e}")
show("2 hbar c / r_e [eV]", "(b c ~ 1.4e8 eV)", 2 * hbarc_eVm / r_e, "{:.4e}")
show("m_e c^2 [eV]", "-", me * c**2 / eV, "{:.4e}")
show("GW Omega = (lP/L)^2 for L = c/H0", "1.4e-122", (lP / L_H)**2, "{:.4e}")
show("S_dS^(1/4)", "4.3e30", S_dS**0.25, "{:.4e}")
kT0_meV = kB * T0 / eV * 1e3
show("k_B T0 [meV]", "0.235", kT0_meV, "{:.4f}")
rhoL = 3 * OL * H0**2 / (8 * np.pi * G) * c**2   # J/m^3
rhoL_q = (rhoL * (hbar * c)**3)**0.25 / eV * 1e3
show("rho_Lambda^(1/4) [meV]", "2.24", rhoL_q, "{:.4f}")
show("rho_Lambda^(1/4) as length hbar c/E [um]", "88.1", hbarc_eVm / (rhoL_q * 1e-3) * 1e6, "{:.3f}")
show("ratio rho_L^(1/4)/kT0", "<10", rhoL_q / kT0_meV, "{:.3f}")
print()

# ---------------- section 5 ----------------
Z = 0.3 + 0.7j
show("-1/Z for Z = 0.3+0.7i", "-0.5172+1.2069i", 0, "{}")
print("   ", -1 / Z)
A0 = (Dx / lP) / (Dp / (mP * c))
show("A0 radiation rectangle, Planck units", "5.2e92", A0, "{:.4e}")
show("log10 A0", "92.72", np.log10(A0), "{:.4f}")
show("ln A0", "213.5", np.log(A0), "{:.4f}")
show("sqrt(3) ln A0", "369.8", np.sqrt(3) * np.log(A0), "{:.4f}")
show("e-folds since square ln(A0)/2", "106.7", np.log(A0) / 2, "{:.4f}")
print()

# ---------------- section 6 ----------------
x_sq = 1 / np.sqrt(A0)
show("a/a0 at square (no g_s)", "4.4e-47", x_sq, "{:.4e}")
show("T/TP at square (no g_s)", "4.4e14", T0 / x_sq / TP, "{:.4e}")
gsSM = 106.75
f = (gs0 / gsSM)**(1/3)
# A = A0 (T0/T)^2 f ; a/a0 = (T0/T) f
TT = np.sqrt(A0 * f)   # T/T0 at square
show("a/a0 at square (g_s = 106.75)", "2.5e-47", f / TT, "{:.4e}")
show("T/TP at square (g_s = 106.75)", "2.5e14", TT * T0 / TP, "{:.4e}")
show("sqrt(2 pi kappa)", "3.28", np.sqrt(2 * np.pi * kappa), "{:.4f}")
c_T = np.sqrt(2 * np.pi * kappa) / (2 * mean_E_over_kT)
show("T_sq coefficient", "0.61", c_T, "{:.4f}")
show("0.61 N^(1/6) TP check", "4.4e14", c_T * Ng**(1/6), "{:.4e}")
show("N_gamma^(1/6)", "~1e15", Ng**(1/6), "{:.4e}")
A_TP = A0 * (T0 / TP)**2 * f
show("A at T = TP (SM counting)", "6.4e28", A_TP, "{:.4e}")
# reheating
As = 2.1e-9
Mbar = mP * c**2 / eV / 1e9 / np.sqrt(8 * np.pi)  # GeV
Einf_r036 = (1.5 * np.pi**2 * As * 0.036)**0.25 * Mbar
show("V^(1/4) for r = 0.036, A_s = 2.1e-9 [GeV]", "1.39e16 (Soman)", Einf_r036, "{:.4e}")
Einf = 1.39e16
Trh = Einf * (30 / (np.pi**2 * gsSM))**0.25
show("T_rh instantaneous from E_inf = 1.39e16 GeV [GeV]", "5.7e15", Trh, "{:.4e}")
T0_GeV = kB * T0 / eV / 1e9
A_rh = A0 * (T0_GeV / Trh)**2 * f
show("A at reheating", "2.9e35", A_rh, "{:.4e}")
print()

# Hubble rectangle in radiation era, Planck units (hbar=c=G=kB=1)
gstar = 106.75
coefH = np.sqrt(8 * np.pi**3 * gstar / 90)   # H = coefH T^2
# A = (2/H)/(2 <E>/T * T) = 2/(coefH T^2 * 2*mean*T)
T_sqH = (2 / (coefH * 2 * mean_E_over_kT))**(1/3)
show("Hubble rectangle square: T/TP", "0.28", T_sqH, "{:.4f}")
RH = 1 / (coefH * T_sqH**2)
show("Hubble radius there [lP]", "0.75", RH, "{:.4f}")
gN = 28 + 0.75 * 90   # SM number-density dof
nq = z3 / np.pi**2 * gN * T_sqH**3
show("quanta in Hubble sphere (all SM)", "0.45", nq * 4/3 * np.pi * RH**3, "{:.4f}")
NH = n_gamma * 4/3 * np.pi * L_H**3
show("N_H photons in Hubble sphere today", "4.4e87", NH, "{:.4e}")
AH0 = (2 * L_H / lP) / (Dp / (mP * c))
show("Hubble-sphere aspect ratio today", "1.6e92", AH0, "{:.4e}")
# two regions at T = T_sqH
x2 = (T0 / TP) / T_sqH * f
Dx2 = Dx * x2 / lP
show("obs. universe diameter at T=0.28TP [lP]", "~1e30", Dx2, "{:.4e}")
show("number of Hubble patches in it", "~6e89", (Dx2 / 2 / RH)**3, "{:.4e}")
show("its rectangle A", "~8e29", Dx2 / (2 * mean_E_over_kT * T_sqH), "{:.4e}")
print()

# ---------------- section 7 ----------------
for name, L, ms in [("Hubble c/H0", L_H, "47.1 um / 4.19 meV"), ("de Sitter L_L", L_L, "51.8 um / 3.81 meV"),
                    ("particle horizon 4.36e26", 4.36e26, "84.0 um / 2.35 meV"),
                    ("particle horizon (mine)", C["chi_ph"], "-")]:
    lam = np.sqrt(lP * L)
    print(f"  lambda = sqrt(lP L) for {name:28s}: {lam*1e6:7.3f} um, hbar c/lambda = {hbarc_eVm/lam*1e3:6.4f} meV   (ms: {ms})")
show("(3 OL / 8 pi)^(1/4)", "0.535", (3 * OL / (8 * np.pi))**0.25, "{:.4f}")
show("reduced-Planck factor (8pi)^(-1/4)", "0.45", (8 * np.pi)**-0.25, "{:.4f}")
show("BH-mass factor (3/(8 pi))^(1/4) [sphere, M = L M_P^2/2]", "-", (3 / (8 * np.pi))**0.25, "{:.4f}")
show("(6 pi)^(1/4) [rho = Lambda^4/16pi^2]", "2.1?", (6 * np.pi)**0.25, "{:.4f}")
show("sqrt(OL) today", "0.83", np.sqrt(OL), "{:.4f}")
show("lambda/lP = sqrt(L_L/lP)", "3.2e30", np.sqrt(L_L / lP), "{:.4e}")
show("Lambda lP^2 = 3 lP^2/L_L^2", "~1e-122", 3 * lP**2 / L_L**2, "{:.4e}")
lamL = np.sqrt(lP * L_L)
Alam0 = hbar * Dx / (lamL**2 * Dp)
show("A in units of lambda=sqrt(lP L_L) today", "-", Alam0, "{:.4e}")
show("T_sq in units of that lambda (no g_s) [TeV]", "1.7", np.sqrt(Alam0) * kB * T0 / eV / 1e12, "{:.4f}")
show("T_sq in units of that lambda (g_s=106.75) [TeV]", "-", np.sqrt(Alam0 * f) * kB * T0 / eV / 1e12, "{:.4f}")
show("sqrt(kT0 * E_P) [TeV]", "-", np.sqrt(kB*T0/eV * EP_eV) / 1e12, "{:.4f}")
lam_sq = np.sqrt(hbar * Dx / Dp)
show("sqrt(hbar Dx/Dp) [m]", "3.7e11", lam_sq, "{:.4e}")
show("  in au", "2.5", lam_sq / au, "{:.4f}")
print()

# ---------------- section 8 ----------------
F_P = c**4 / G
show("c^4/G [N]", "1.21e44", F_P, "{:.4e}")
ct_H = F_P * lP / L_H
ct_L = F_P * lP / L_L
show("c~ for L = c/H0 [N]", "1.4e-17", ct_H, "{:.4e}")
show("c~ for L_L [N]", "1.2e-17", ct_L, "{:.4e}")
show("check hbar c/lambda^2 = (c^4/G)(lP/L)", "-", hbar * c / (lP * L_H) / ct_H, "{:.6f}")
F_C = e**2 / (4 * np.pi * eps0 * a0_bohr**2)
show("Coulomb force at a0 [N]", "8.24e-8", F_C, "{:.4e}")
show("ratio F_C / c~", "5.8e9", F_C / ct_H, "{:.4e}")
show("weight of 1 kg / c~", "6.9e17", g_n / ct_H, "{:.4e}")
show("L/lP Hubble (8.1)", "8.5e60", L_H / lP, "{:.4e}")
show("(L/lP)^2", "~1e122", (L_H / lP)**2, "{:.4e}")
# Vainshtein radius r_V = (r_s lambda^2)^(1/3)
for M, lam in [(1.0, 50e-6), (1.0, 37.7e-6)]:
    rs = 2 * G * M / c**2
    print(f"  Vainshtein (r_s lambda^2)^(1/3), M = {M} kg, lambda = {lam*1e6:.1f} um: {(rs*lam**2)**(1/3):.3e} m (ms: ~1e-12 m)")
show("M_X c^2 > hbar c/(37.7 um) [meV]", "5.2", hbarc_eVm / 37.7e-6 * 1e3, "{:.4f}")
show("hbar c/(38.6 um) [meV]", "5.1 (Lee)", hbarc_eVm / 38.6e-6 * 1e3, "{:.4f}")
show("5.2 meV / rho_L^(1/4)", "2.3", hbarc_eVm / 37.7e-6 * 1e3 / rhoL_q, "{:.4f}")
# 8.3 conjugate
show("conjugate position extent Dp/(mP c) [lP]", "1.0e-31", Dp / (mP * c), "{:.4e}")
show("conjugate momentum extent Dx/lP [mP c]", "5.4e61", Dx / lP, "{:.4e}")
# 8.5 lever arm
p_bohr = me * alpha_fs * c
show("lP^2 p_Bohr/hbar [m/rad]", "4.9e-60", lP**2 * p_bohr / hbar, "{:.4e}")
show("lambda^2 p_Bohr/hbar at lambda=sqrt(lP c/H0) [m/rad]", "42", lP * L_H * p_bohr / hbar, "{:.4f}")
show("  same at lambda = sqrt(lP L_L)", "-", lP * L_L * p_bohr / hbar, "{:.4f}")
# section 6: (M_X/H0)^2
hbarH0_eV = hbar * H0 / eV
show("(M_X/H0)^2 for M_X = 5.2 meV", "~1e61", (5.2e-3 / hbarH0_eV)**2, "{:.4e}")
show("  divided by 3 (rho_crit = 3 Mbar^2 H0^2)", "-", (5.2e-3 / hbarH0_eV)**2 / 3, "{:.4e}")
