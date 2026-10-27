"""Referee B: independent recomputation of every number in the manuscript.

Inputs chosen by the referee (not taken from the manuscript):
  CODATA 2018 exact/recommended constants; Planck 2018 (TT,TE,EE+lowE+lensing)
  H0 = 67.4 km/s/Mpc, Omega_m = 0.315; FIRAS T0 = 2.7255 K (Fixsen 2009);
  N_eff = 3.046 for the radiation density; A_s = 2.1e-9 (Planck 2018, ln(1e10 A_s) = 3.044).
Each line prints: label | manuscript value | referee value.
"""
import mpmath as mp

mp.mp.dps = 30

# --- constants (CODATA 2018) ---
c = mp.mpf('299792458')
hbar = mp.mpf('1.054571817e-34')
h = 2 * mp.pi * hbar
kB = mp.mpf('1.380649e-23')
G = mp.mpf('6.67430e-11')
e = mp.mpf('1.602176634e-19')
eps0 = mp.mpf('8.8541878128e-12')
a_bohr = mp.mpf('5.29177210903e-11')
me = mp.mpf('9.1093837015e-31')
r_e = mp.mpf('2.8179403262e-15')
eV = e
Mpc = mp.mpf('3.0856775814913673e22')
ly = mp.mpf('9.4607304725808e15')
Gly = 1e9 * ly
au = mp.mpf('1.495978707e11')
g_n = mp.mpf('9.80665')

lP = mp.sqrt(hbar * G / c**3)
mP = mp.sqrt(hbar * c / G)
EP = mP * c**2
TP = EP / kB
pP = mP * c
zeta3 = mp.zeta(3)


def row(label, ms, val, fmt='{:.4g}'):
    try:
        v = fmt.format(float(val))
    except Exception:
        v = str(val)
    print(f'{label:<62s} | ms: {ms:<14s} | ref: {v}')


print('Planck units: lP=%.6e m, mP=%.6e kg, TP=%.6e K, EP=%.6e GeV' % (lP, mP, TP, EP / eV / 1e9))

# --- cosmology (Planck 2018) ---
H0_kms = mp.mpf('67.4')
H0 = H0_kms * 1e3 / Mpc
Om = mp.mpf('0.315')
T0 = mp.mpf('2.7255')
Neff = mp.mpf('3.046')
# photon density parameter
rho_gamma = (mp.pi**2 / 15) * (kB * T0)**4 / (hbar * c)**3  # J/m^3
rho_crit = 3 * H0**2 * c**2 / (8 * mp.pi * G)  # J/m^3
Og = rho_gamma / rho_crit
Or = Og * (1 + mp.mpf(7) / 8 * (mp.mpf(4) / 11)**(mp.mpf(4) / 3) * Neff)
OL = 1 - Om - Or
print('Omega_gamma=%.4e Omega_r=%.4e Omega_L=%.5f' % (Og, Or, OL))


def Hof(a):
    return H0 * mp.sqrt(Or / a**4 + Om / a**3 + OL)


chi_ph = c * mp.quad(lambda a: 1 / (a**2 * Hof(a)), [0, 1e-6, 1e-3, 1])
chi_eh = c * mp.quad(lambda a: 1 / (a**2 * Hof(a)), [1, 10, mp.inf])
L_H = c / H0
L_L = c / (H0 * mp.sqrt(OL))

print('\n=== Section 3 ===')
kappa = 3**(mp.mpf(1) / 3) * mp.pi**(mp.mpf(10) / 3) / (30 * zeta3**(mp.mpf(4) / 3))
row('kappa (sphere, Dp = 2<|p|>)', '1.708', kappa)
meanp = mp.pi**4 / (30 * zeta3)  # <|p|> in units of kT/c
row('<|p|>/(kT/c)', '(2.701)', meanp)
row('kappa with Dp = kT/c', '0.316', kappa / (2 * meanp))
row('kappa with Dp = <|p|>', '0.854', kappa / 2)
row('kappa for cube of side Dx', '1.377', kappa / (6 / mp.pi)**(mp.mpf(1) / 3))

row('comoving particle horizon [Gly]', '46.1', chi_ph / Gly)
row('comoving particle horizon [m]', '4.36e26', chi_ph)
n_gamma = (2 * zeta3 / mp.pi**2) * (kB * T0 / (hbar * c))**3
row('n_gamma [cm^-3]', '(410.7)', n_gamma / 1e6)
V_obs = 4 * mp.pi / 3 * chi_ph**3
N_gamma = n_gamma * V_obs
row('N_gamma, observable universe', '1.43e89', N_gamma)
s_per_gamma_photons = (2 * mp.pi**4 / (45 * zeta3))  # photon entropy per photon: (4pi^2/45)/(2 zeta3/pi^2)
gs0 = 2 + mp.mpf(7) / 8 * 2 * 3 * mp.mpf(4) / 11
row('g_s today (photons + 3 nu)', '3.909', gs0)
row('entropy per photon, photons only', '3.60', s_per_gamma_photons)
row('entropy per photon, photons+neutrinos', '7.04', s_per_gamma_photons * gs0 / 2)
S_tot = N_gamma * s_per_gamma_photons * gs0 / 2
row('S (photons+neutrinos) [k_B]', '1.01e90', S_tot)
S_photons = N_gamma * s_per_gamma_photons
row('S (photons only) [k_B]', '(cf E&L 5.40e89?)', S_photons)
Dx = 2 * chi_ph
Dp = 2 * meanp * kB * T0 / c
row('Dx [m]', '8.73e26', Dx)
row('Dp [kg m/s]', '6.78e-31', Dp)
row('Dx*Dp/h', '8.9e29', Dx * Dp / h)
row('kappa*N^(1/3)', '8.9e29', kappa * N_gamma**(mp.mpf(1) / 3))
row('S^(1/3)', '1.0e30', S_tot**(mp.mpf(1) / 3))
row('(11/4)^(1/3)', '1.40', (mp.mpf(11) / 4)**(mp.mpf(1) / 3))
row('(106.75/3.909)^(1/3)', '3.01', (mp.mpf('106.75') / gs0)**(mp.mpf(1) / 3))

print('\n=== Section 4 ===')
row('c/H0 [m]', '1.37e26', L_H)
row('lP [m]', '1.616e-35', lP)
row('L/lP (c/H0)', '8.49e60', L_H / lP)
row('(L/lP)^3', '6.12e182', (L_H / lP)**3)
row('L_Lambda = c/(H0 sqrt(OL)) [m]', '1.66e26', L_L)
row('S_GH(L_Lambda) = pi L^2/lP^2', '3.31e122', mp.pi * (L_L / lP)**2)
row('event horizon today (proper) [Gly]', '16.7', chi_eh / Gly)
row('S_GH(event horizon today)', '3.0e122', mp.pi * (chi_eh / lP)**2)
# CKN: Lambda_UV = sqrt(M_P / L) natural units, M_P unreduced
LamCKN = mp.sqrt(EP * hbar * c / L_H)
row('CKN cutoff sqrt(E_P hbar c/L), L=c/H0 [meV]', '4.19', LamCKN / eV * 1e3)
row('Born b c from hbar c / r_e [eV]', '1.4e8 ?', hbar * c / r_e / eV)
row('Born b c from 2 hbar c / r_e [eV]', '1.4e8 ?', 2 * hbar * c / r_e / eV)
row('GW Omega = (lP/L)^2, L = c/H0', '1.4e-122', (lP / L_H)**2)
S_dS = mp.pi * (L_L / lP)**2
row('S_dS^(1/4)', '4.3e30', S_dS**(mp.mpf(1) / 4))
row('k_B T0 [meV]', '0.235', kB * T0 / eV * 1e3)
rho_L = OL * rho_crit  # J/m^3
rhoL14 = (rho_L * (hbar * c)**3)**(mp.mpf(1) / 4)  # J
row('rho_Lambda^(1/4) [meV]', '2.24', rhoL14 / eV * 1e3)
row('ratio rho_L^(1/4)/kT0', '(<10)', rhoL14 / (kB * T0))

print('\n=== Section 5 ===')
Z = mp.mpc('0.3', '0.7')
row('-1/Z real', '-0.5172', (-1 / Z).real)
row('-1/Z imag', '1.2069', (-1 / Z).imag)
A0 = (Dx / lP) / (Dp / pP)
row('A0 (Planck units)', '5.2e92', A0)
row('log10 A0', '92.72', mp.log10(A0))
row('ln A0', '213.5', mp.log(A0))
row('sqrt(3) ln A0', '369.8', mp.sqrt(3) * mp.log(A0))
row('ln A0 / 2 (e-folds)', '106.7', mp.log(A0) / 2)

print('\n=== Section 6 ===')
a_sq = A0**(-mp.mpf(1) / 2)
row('a_sq/a0 (no g_s)', '4.4e-47', a_sq)
row('T_sq/T_P (no g_s)', '4.4e14', T0 / a_sq / TP)
gsSM = mp.mpf('106.75')
a_sq_g = A0**(-mp.mpf(1) / 2) * (gs0 / gsSM)**(mp.mpf(1) / 6)
T_sq_g = T0 / a_sq_g * (gs0 / gsSM)**(mp.mpf(1) / 3)
row('a_sq/a0 (g_s=106.75)', '2.5e-47', a_sq_g)
row('T_sq/T_P (g_s=106.75)', '2.5e14', T_sq_g / TP)
row('sqrt(2 pi kappa)', '3.28', mp.sqrt(2 * mp.pi * kappa))
Tsq_coef = mp.sqrt(2 * mp.pi * kappa) / (2 * meanp)
row('T_sq/(N^(1/6) T_P)', '0.61', Tsq_coef)
row('N_gamma^(1/6)', '~1e15', N_gamma**(mp.mpf(1) / 6))
row('0.61 N^(1/6)', '4.4e14', Tsq_coef * N_gamma**(mp.mpf(1) / 6))


def A_at_T(T_K, gs):
    """Aspect ratio (Planck units) of the observable-universe radiation rectangle at photon temperature T."""
    a = (T0 / T_K) * (gs0 / gs)**(mp.mpf(1) / 3)
    return (Dx * a / lP) / (2 * meanp * kB * T_K / c / pP)


row('A at T = T_P (SM g_s)', '6.4e28', A_at_T(TP, gsSM))
# inflation scale from r < 0.036
As = mp.mpf('2.1e-9')
Mbar = mP / mp.sqrt(8 * mp.pi)
Mbar_GeV = Mbar * c**2 / eV / 1e9
for r in [mp.mpf('0.036')]:
    V14 = (3 * mp.pi**2 * As * r / 2)**(mp.mpf(1) / 4) * Mbar_GeV
    row('E_inf = V^(1/4) for r<0.036 [GeV], A_s=2.1e-9', '1.39e16', V14)
for As_ in [mp.mpf('2.0989e-9'), mp.mpf('2.1e-9'), mp.mpf('2.2e-9')]:
    V14 = (3 * mp.pi**2 * As_ * mp.mpf('0.036') / 2)**(mp.mpf(1) / 4) * Mbar_GeV
    print('   A_s=%.4e -> E_inf=%.4e GeV' % (As_, V14))
Einf = mp.mpf('1.39e16')
Treh = Einf * (30 / (mp.pi**2 * gsSM))**(mp.mpf(1) / 4)
row('T_reh instantaneous (g*=106.75) [GeV]', '5.7e15', Treh)
Treh_K = Treh * 1e9 * eV / kB
row('A at reheating', '2.9e35', A_at_T(Treh_K, gsSM))

# Hubble rectangle in radiation era (Planck units, kB = c = hbar = G = 1 with unreduced Planck units)
# H^2 = 8 pi rho / 3 (Planck units), rho = pi^2/30 g* T^4
gstar = gsSM


def hubble_A(tau):
    H = mp.sqrt(8 * mp.pi / 3 * mp.pi**2 / 30 * gstar * tau**4)
    Dx_H = 2 / H
    Dp_H = 2 * meanp * tau
    return Dx_H / Dp_H, 1 / H


tau_sq = mp.findroot(lambda t: hubble_A(t)[0] - 1, 0.3)
row('Hubble rectangle square at T/T_P', '0.28', tau_sq)
row('Hubble radius there [lP]', '0.75', hubble_A(tau_sq)[1])
gnum = mp.mpf(28) + mp.mpf(3) / 4 * 90  # number-density dof
n_SM = zeta3 / mp.pi**2 * gnum * tau_sq**3
N_in = n_SM * 4 * mp.pi / 3 * hubble_A(tau_sq)[1]**3
row('quanta in Hubble sphere there (all SM)', '0.45', N_in)
N_H = n_gamma * 4 * mp.pi / 3 * L_H**3
row('N_H photons in Hubble sphere today', '4.4e87', N_H)
A_H0 = (2 * L_H / lP) / (Dp / pP)
row('Hubble-rectangle aspect ratio today', '1.6e92', A_H0)
# two regions
a_at = (T0 / (tau_sq * TP)) * (gs0 / gsSM)**(mp.mpf(1) / 3)
Dx_then = Dx * a_at / lP
row('obs. universe diameter at T=0.28TP [lP]', '~1e30', Dx_then)
row('number of Hubble patches in it', '6e89', (Dx_then / 2 / hubble_A(tau_sq)[1])**3)
row('its aspect ratio then', '8e29', Dx_then / (2 * meanp * tau_sq))
# M_X / H0
MX_eV = hbar * c / mp.mpf('37.7e-6') / eV
H0_eV = hbar * H0 / eV
row('(M_X/H0)^2 for M_X = hbar c/37.7um', '~1e61', (MX_eV / H0_eV)**2)
row('M_X^2/(3 H0^2)', '(~1e61)', (MX_eV / H0_eV)**2 / 3)

print('\n=== Section 7 ===')
for lab, L, ms1, ms2 in [('c/H0', L_H, '47.1', '4.19'), ('L_Lambda', L_L, '51.8', '3.81'),
                         ('particle horizon', chi_ph, '84.0', '2.35')]:
    lam = mp.sqrt(lP * L)
    row(f'lambda = sqrt(lP L), L = {lab} [um]', ms1, lam * 1e6)
    row(f'hbar c/lambda, L = {lab} [meV]', ms2, hbar * c / lam / eV * 1e3)
# CKN factor variants
base = mp.sqrt(EP * hbar * c / L_H)
print('  CKN variants (ratio to sqrt(E_P/L)):')
variants = {
    'reduced Planck mass': (1 / (8 * mp.pi))**(mp.mpf(1) / 4),
    'sphere vol (4pi/3)L^3 rho=Lam^4 <= L MP^2/2': (3 / (8 * mp.pi))**(mp.mpf(1) / 4),
    'rho = Lam^4/(16pi^2), sphere, Schwarzschild M=L/2': (6 * mp.pi)**(mp.mpf(1) / 4),
    'rho = Lam^4/(16pi^2), cube L^3 <= L/2': (8 * mp.pi**2)**(mp.mpf(1) / 4),
    'rho = Lam^4, cube L^3 <= L MP^2/2': (mp.mpf(1) / 2)**(mp.mpf(1) / 4),
}
for k, v in variants.items():
    print('     %-55s %.3f' % (k, v))
row('(3 OL/8pi)^(1/4)', '0.535', (3 * OL / (8 * mp.pi))**(mp.mpf(1) / 4))
row('rho_L^(1/4) / (hbar c/sqrt(lP c/H0))', '0.535', rhoL14 / (hbar * c / mp.sqrt(lP * L_H)))
row('rho_L^(1/4) as a length hbar c/rho^(1/4) [um]', '88.1', hbar * c / rhoL14 * 1e6)
row('chi H0/c', '3.18', chi_ph / L_H)
row('sqrt(Omega_L) today', '0.83', mp.sqrt(OL))
row('lambda/lP = sqrt(L_L/lP)', '3.2e30', mp.sqrt(L_L / lP))
row('Lambda lP^2 = 3 (lP/L_L)^2', '~1e-122', 3 * (lP / L_L)**2)
row('log10(L_L/lP)', '(61)', mp.log10(L_L / lP))
row('log10(lambda/lP)', '(30.5)', mp.log10(mp.sqrt(L_L / lP)))
row('log10(Lambda lP^2)', '(-122)', mp.log10(3 * (lP / L_L)**2))
# square in units of lambda = sqrt(lP L_L)
lam = mp.sqrt(lP * L_L)
A_lam = hbar * Dx / (lam**2 * Dp)
a_sq_lam = A_lam**(-mp.mpf(1) / 2)
row('T square in units lambda (no g_s) [TeV]', '1.7', kB * T0 / a_sq_lam / eV / 1e12)
a_sq_lam_g = A_lam**(-mp.mpf(1) / 2) * (gs0 / gsSM)**(mp.mpf(1) / 6)
row('T square in units lambda (g_s=106.75) [TeV]', '(1.7)', kB * T0 / a_sq_lam_g * (gs0 / gsSM)**(mp.mpf(1) / 3) / eV / 1e12)
row('sqrt(MP MDE) electroweak see-saw [TeV]', '(BHM)', mp.sqrt(EP * rhoL14) / eV / 1e12)
lam_sq = mp.sqrt(hbar * Dx / Dp)
row('Born length making today rectangle square [m]', '3.7e11', lam_sq)
row('  in au', '2.5', lam_sq / au)

print('\n=== Section 8 ===')
F_P = c**4 / G
row('c^4/G [N]', '1.21e44', F_P)
row('ctilde at lambda=sqrt(lP c/H0) [N]', '1.4e-17', F_P * lP / L_H)
row('ctilde at lambda=sqrt(lP L_L) [N]', '1.2e-17', F_P * lP / L_L)
row('check hbar c/lambda^2 = F_P lP/L', '(same)', hbar * c / (lP * L_H))
F_C = e**2 / (4 * mp.pi * eps0 * a_bohr**2)
row('Coulomb force in H ground state [N]', '8.24e-8', F_C)
row('ratio Coulomb/ctilde', '5.8e9', F_C / (F_P * lP / L_H))
row('ratio kg weight/ctilde', '6.9e17', g_n / (F_P * lP / L_H))
row('A = L/lP (Hubble)', '8.5e60', L_H / lP)
row('A^2', '(~1e122)', (L_H / lP)**2)
# Vainshtein radius r_V = (r_s lambda^2)^(1/3)
for M in [mp.mpf(1), mp.mpf('0.01')]:
    rs = 2 * G * M / c**2
    for lamX in [mp.mpf('50e-6'), mp.mpf('37.7e-6')]:
        rV3 = (rs * lamX**2)**(mp.mpf(1) / 3)
        rV5 = (rs * lamX**4)**(mp.mpf(1) / 5)
        print('  M=%g kg, lambda_X=%g um: r_V(cubic)=%.3e m, r_V(quintic)=%.3e m' % (M, lamX * 1e6, rV3, rV5))
row('M_X c^2 = hbar c/37.7um [meV]', '5.2', MX_eV * 1e3)
row('hbar c/38.6um [meV]', '5.1', hbar * c / mp.mpf('38.6e-6') / eV * 1e3)
row('ratio M_X/rho_L^(1/4)', '2.3', MX_eV / (rhoL14 / eV))
# conjugate image of today's rectangle under rho_{lP}
row('conjugate position extent [lP] = Dp/(mP c)', '1.0e-31', Dp / pP)
row('conjugate momentum extent [mP c] = Dx/lP', '5.4e61', Dx / lP)
# lever arm: displacement theta lambda^2 p/hbar per radian, p = hbar/a_bohr
row('lever arm at lambda = lP [m/rad]', '4.9e-60', lP**2 / a_bohr)
row('lever arm at lambda = sqrt(lP c/H0) [m/rad]', '42', lP * L_H / a_bohr)
row('lever arm at lambda = sqrt(lP L_L) [m/rad]', '(42?)', lP * L_L / a_bohr)
