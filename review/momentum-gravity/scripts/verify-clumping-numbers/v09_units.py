"""Verifier v09: unit conversions and order-of-magnitude numbers (C6, C10, C11, C13-C16, C20),
from SI constants (CODATA 2018 values typed here; Msun nominal IAU; R0, v_c as the agent states, dagger)."""
import numpy as np

G = 6.67430e-11; c = 2.99792458e8; hbar_c_GeVm = 1.973269804e-16; hbar_c_eVm = 1.973269804e-7
GeV_kg = 1.78266192e-27; pc = 3.0856775814913673e16; kpc = 1e3 * pc; Msun = 1.98847e30
Myr = 1e6 * 365.25 * 86400.0; kms = 1e3

def rho_SI(rho_GeVcm3):
    return rho_GeVcm3 * GeV_kg / 1e-6

envs = {'dwarf': (1.0, 30.0), 'MW': (0.4, 155.0), 'cluster': (0.03, 1000.0)}
m_GeV = 0.07; vstar = 120.0
print("Local scales (t_ff = 1/sqrt(4 pi G rho); lambda_J = 2 pi sigma t_ff; r_c = 3 sigma t_ff; t_cross = r_c/sigma)")
loc = {}
for k, (rho, sig) in envs.items():
    tff = 1 / np.sqrt(4 * np.pi * G * rho_SI(rho))
    lamJ = 2 * np.pi * sig * kms * tff
    rc = 3 * sig * kms * tff
    loc[k] = (tff / Myr, lamJ / kpc, rc / kpc, 3 * tff / Myr)
    print(f"  {k:8s}: t_ff={tff/Myr:.2f} Myr  lambda_J={lamJ/kpc:.3f} kpc  r_c={rc/kpc:.3f} kpc  t_cross={3*tff/Myr:.1f} Myr")
R0, vc = 8.2, 230.0
torb = 2 * np.pi * R0 * kpc / (vc * kms) / Myr
Qsun = (loc['MW'][1] / R0) ** 2
print(f"  solar orbit period 2 pi R0/v_c = {torb:.1f} Myr; (lambda_J/R0)^2 = {Qsun:.4f}")
print(f"  margins: (pi/3)^2={(np.pi/3)**2:.4f} (2pi/3)^2={(2*np.pi/3)**2:.4f} pi^2/2={np.pi**2/2:.4f} 2pi^2={2*np.pi**2:.4f}")

print("\nC11 e-fold conversions t_e = t_ff/Gamma")
for env, G_, ref in [('MW', 0.44210, 'gt=56.14'), ('MW', 0.56618, 'gt=280.7'), ('MW', 0.7783, 'k2=30'),
                     ('MW', 0.6866, 'gt=255 k2=19.7'), ('cluster', 0.06569, '304.4'), ('cluster', 0.02721, '1598'),
                     ('cluster', 0.01885, '1522'), ('dwarf', 0.07069, '0.2304'), ('dwarf', 0.50993, '1.152')]:
    tff, _, _, tcr = loc[env]
    te = tff / G_
    print(f"  {env:7s} {ref:16s}: Gamma={G_} -> t_e={te:.1f} Myr, t_e/t_orb(219)={te/torb:.3f}, t_e/t_cross={te/tcr:.3f}")

print("\nC6: Debt 3a inputs and shortfalls")
m_g = m_GeV * GeV_kg * 1e3                 # grams
sigma0 = 30.0 * m_g                        # cm^2
GeVm2_cm2 = (hbar_c_GeVm * 100) ** 2
g = np.sqrt(np.pi * (sigma0 / GeVm2_cm2) / m_GeV**2)
print(f"  g = sqrt(pi sigma0/m^2) = {g:.1f} GeV^-2")
cm3_GeV3 = (hbar_c_GeVm * 100) ** 3         # 1 cm^-3 = cm3_GeV3 GeV^3
def lamg(r):
    return (0.5 + r * r + np.sqrt(1 + 4 * r * r) / 2) ** -1.5
for k, (rho, sig) in envs.items():
    n = rho / m_GeV                          # cm^-3
    r = sig / vstar
    beta_s, beta_v = sig * kms / c, vstar * kms / c
    ngate = n * min(1.0, (vstar / sig) ** 3 / (2 * np.pi) ** 1.5) if sig > vstar else n
    eps3a = g * ngate * cm3_GeV3
    kin3a = m_GeV * min(beta_s, beta_v) ** 2
    lin = g * n * cm3_GeV3 * lamg(r) / (m_GeV * beta_s**2)
    print(f"  {k:8s}: 3a eps_gate={eps3a:.3e} GeV, m min(sig,v*)^2={kin3a:.3e} GeV, 3a ratio={eps3a/kin3a:.3e}; linearized g n Lam_g/(m sig^2)={lin:.3e}")
for r in [155/120, 8.333, 32.0, 0.25]:
    print(f"  required-g ratio exact/3a-narrow (2pi)^-1.5/(r Lam_g) at r={r:.4f}: {(2*np.pi)**-1.5/(r*lamg(r)):.4f};  exact/3a-broad 1/Lam_g: {1/lamg(r):.4f};  (2pi)^-1.5 r^2 = {(2*np.pi)**-1.5*r*r:.4f}")

print("\nC10 cap: Lam_g/<W> at r=64:", (lamg(64.0) / (1 + 2 * 64.0**2) ** -1.5), " limit 2^1.5 =", 2**1.5)

print("\nC13-C15: dwarf core, m = 70 MeV")
rho, sig = envs['dwarf']
tff = 1 / np.sqrt(4 * np.pi * G * rho_SI(rho))
rc = 3 * sig * kms * tff
M = 4 / 3 * np.pi * rc**3 * rho_SI(rho)
m_kg = m_GeV * GeV_kg
N = M / m_kg
eps_grav = G * M * m_kg / rc / (GeV_kg * c**2)    # GeV
n = rho / m_GeV
eps_contact = g * n * cm3_GeV3
kin = m_GeV * (sig * kms / c) ** 2
print(f"  r_c={rc/kpc:.3f} kpc, M(<r_c)={M/Msun:.4e} Msun, N={N:.4e}, lnN={np.log(N):.1f}")
print(f"  G M m/r_c = {eps_grav:.4e} GeV; contact g n = {eps_contact:.4e} GeV; ratio={eps_grav/eps_contact:.3e}; m sigma^2={kin:.4e} GeV")
for k, (rho, sig) in envs.items():
    rho_nat = rho * cm3_GeV3                  # GeV^4
    Nocc = rho_nat / (m_GeV**4 * (sig * kms / c) ** 3)
    print(f"  N_occ {k}: {Nocc:.4e}")
v = 30e3
b90 = 2 * G * m_kg / v**2
sT = 4 * np.pi * b90**2 * np.log(N)          # m^2
sT_m = sT * 1e4 / (m_kg * 1e3)
print(f"  Rutherford: b90={b90:.4e} m, sigma_T/m={sT_m:.4e} cm^2/g; G~/G for 30 cm^2/g = {np.sqrt(30/sT_m):.4e}")
# same with mean relative speed of a Maxwellian (sigma=30): <v_rel> = 4 sigma/sqrt(pi)
vrel = 4 * 30e3 / np.sqrt(np.pi)
b90r = 2 * G * m_kg / vrel**2
sTr = 4 * np.pi * b90r**2 * np.log(N) * 1e4 / (m_kg * 1e3)
print(f"  (at mean relative speed {vrel/1e3:.1f} km/s: sigma_T/m={sTr:.3e} cm^2/g)")
print(f"  t_relax/t_cross ~ N/(8 lnN) = {N/(8*np.log(N)):.4e}")

print("\nC16: X range")
lx = 37.7e-6
print(f"  lambda_X/1kpc = {lx/kpc:.4e}; hbar c/1kpc = {hbar_c_eVm/kpc:.4e} eV; hbar c/37.7um = {hbar_c_eVm/lx*1e3:.4f} meV; ratio={hbar_c_eVm/lx/(hbar_c_eVm/kpc):.4e}")
