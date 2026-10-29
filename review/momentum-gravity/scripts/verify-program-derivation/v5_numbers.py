"""Verifier recomputation of the program agent's numbers (P2, P4, P6, P16-P20), constants typed
from CODATA 2018 / IAU (by hand), H0 = 67.4 km/s/Mpc as the agent used."""
import math as m

hbarc_MeVfm = 197.3269804          # MeV fm
hbarc_eVm = hbarc_MeVfm*1e6*1e-15  # eV m
hbar_eVs = 6.582119569e-16
c = 299792458.0
G = 6.67430e-11
MPl_GeV = 1.220890e19               # non-reduced Planck mass
MPlred_eV = MPl_GeV*1e9/m.sqrt(8*m.pi)
pc = 3.0856775814913673e16
AU = 1.495978707e11
GMsun = 1.32712440018e20
Msun = 1.98841e30
GeV_cm2 = 0.389379372e-27           # (hbar c)^2 in GeV^2 cm^2 -> 1 GeV^-2 = 3.8938e-28 cm^2
GeV_g = 1.78266192e-24              # 1 GeV/c^2 in grams
kms = 1e3/c

mchi = 0.070                        # GeV
mN = 0.93827                        # GeV (proton)
print("=== P2 ===")
Gm2 = (mchi/MPl_GeV)**2
print(f"G m_chi^2/(hbar c) = {Gm2:.4e};  alpha~/(G m_chi^2) at alpha~ = 1: {1/Gm2:.4e}")
print(f"range hbar/(m_chi c) = {hbarc_MeVfm/(mchi*1e3)*1e-15:.4e} m")
sig0 = 30*mchi*GeV_g                # cm^2  (sigma0/m = 30 cm^2/g)
print(f"sigma0 = 30 cm^2/g x m_chi = {sig0:.4e} cm^2")
g_contact = 4*m.pi/mchi**2
print(f"calc note #2's g = 4 pi alpha~/m_phi^2 at m_phi = m_chi = 70 MeV: {g_contact:.4e} GeV^-2;  sqrt(pi sigma0/m^2) = {m.sqrt(m.pi*sig0/GeV_cm2/mchi**2):.4e} GeV^-2")

print("=== P4 (chi-nucleon via single X exchange, contact Born, factorised couplings) ===")
mu_cN = mchi*mN/(mchi + mN); mu_cc = mchi/2
alpha_X = 4/3
ratio = (mu_cN/mu_cc)**2*alpha_X*(mN/MPl_GeV)**2/1.0
print(f"(mu_chiN/(m/2))^2 = {(mu_cN/mu_cc)**2:.4f}; alpha G m_N^2 = {alpha_X*(mN/MPl_GeV)**2:.4e}; sigma_chiN/sigma_chichi = {ratio:.4e}; sigma_chiN = {ratio*sig0:.4e} cm^2")

print("=== P6 ===")
for v in (30, 120, 1000):
    q = mchi*1e9*v*kms           # eV
    lam = hbarc_eVm/q
    print(f"v = {v:5d} km/s: m_chi v = {q/1e3:.3f} keV; hbar/(m_chi v) = {lam:.3e} m; 37.7 um / that = {37.7e-6/lam:.3e}")

print("=== P17, P18 ===")
lam_kpc = 1e3*pc
MX = hbarc_eVm/lam_kpc
H0 = 67.4e3/(1e6*pc)
hH0 = hbar_eVs*H0
print(f"lambda = 1 kpc: M_X c^2 = {MX:.4e} eV; hbar H0 = {hH0:.4e} eV; (M_X/H0)^2 = {(MX/hH0)**2:.4e}; c/H0 = {c/H0/(1e9*pc):.3f} Gpc")
for name, Mass in (("Sun", Msun), ("1e10 Msun", 1e10*Msun)):
    rS = 2*G*Mass/c**2
    rV = (rS*(1 + 1**2)*lam_kpc**2)**(1/3)
    print(f"Vainshtein r_V = (r_S (1+u^2) lambda^2)^(1/3), u = 1, lambda = 1 kpc, {name}: {rV:.3e} m = {rV/AU:.3e} AU = {rV/pc:.3e} pc")
L3_red = (MX**2*MPlred_eV)**(1/3)
L3_full = (MX**2*MPl_GeV*1e9)**(1/3)
print(f"Lambda_3 = (M_X^2 M_Pl)^(1/3): reduced M_Pl -> {L3_red:.3e} eV, 1/Lambda_3 = {hbarc_eVm/L3_red:.2f} m; non-reduced -> 1/Lambda_3 = {hbarc_eVm/L3_full:.2f} m")
rSE = 2*3.986004418e14/c**2
print(f"Earth Vainshtein radius for lambda = 1 kpc, u = 1: {(rSE*2*lam_kpc**2)**(1/3):.3e} m")

print("=== P19: strength a long-range chi-chi force needs to give sigma_T = sigma0 at 30 km/s ===")
mu = mchi/2                       # GeV
v = 30*kms
lam_nat = lam_kpc/(hbarc_eVm*1e-9)  # GeV^-1
sig0_nat = sig0/GeV_cm2             # GeV^-2
def sigT_class(A): return 4*m.pi*A**2/(mu**2*v**4)*m.log(mu*v**2*lam_nat/A)
def sigT_born(A, lam=lam_nat):
    x = (2*mu*v*lam)**2
    return 2*m.pi*A**2/(mu**2*v**4)*(m.log1p(x) - x/(1 + x))
def solve(fun):
    lo, hi = 1e-20, 1e-3
    for _ in range(200):
        mid = m.sqrt(lo*hi)
        if fun(mid) > sig0_nat: hi = mid
        else: lo = mid
    return mid
Ac = solve(sigT_class); Ab = solve(sigT_born)
print(f"classical-log solution: A = {Ac:.4e}, ln = {m.log(mu*v**2*lam_nat/Ac):.1f}, A/(G m^2) = {Ac/Gm2:.4e}")
print(f"Born (quantum) solution: A = {Ab:.4e}, ln(2 mu v lambda) - 1/2 = {m.log(2*mu*v*lam_nat) - 0.5:.1f}, A/(G m^2) = {Ab/Gm2:.4e}")
print(f"Sommerfeld/Born parameter A/(hbar v) = {Ab/v:.2e}  (<< 1: Born regime, the classical Coulomb log does not apply)")
AX = alpha_X*Gm2
lamX = 37.7e-6/(hbarc_eVm*1e-9)
sc = 4*m.pi*AX**2/(mu**2*v**4)*m.log(mu*v**2*lamX/AX)
sb = sigT_born(AX, lamX)
print(f"X at alpha = 4/3, 37.7 um, 30 km/s: classical log sigma_T = {sc*GeV_cm2:.3e} cm^2 (ratio {sc*GeV_cm2/sig0:.2e}); Born sigma_T = {sb*GeV_cm2:.3e} cm^2 (ratio {sb*GeV_cm2/sig0:.2e}); A/(hbar v) = {AX/v:.1e}")

print("=== P16 ===")
vstar = 120.0
for name, phi in (("Earth orbit (v_orb = 29.8)", 29.8**2), ("MW at Sun (v_c = 230)", 230**2), ("classical dwarf 3 sigma^2, sigma = 10", 3*10**2), ("UFD 3 sigma^2, sigma = 4", 3*4**2)):
    print(f"{name:40s}: eps/beta = 2|Phi|/v*^2 = {2*phi/vstar**2:.4f}")
fr = (vstar/155)**3/(2*m.pi)**1.5
print(f"record's co-moving fraction (calc note #2) at sigma = 155: {fr:.4f}; times MW eps/beta = {fr*2*230**2/vstar**2:.4f}")
fr2 = (vstar/155)**3/8
print(f"alternative convention (Gaussian gate exp(-v_rel^2/v*^2) over the relative-velocity Maxwellian, dispersion sqrt2 sigma): {fr2:.4f}")

print("=== P20 Mercury ===")
a = 0.387098*AU; e = 0.205630
x = GMsun/(a*(vstar*1e3)**2)
gated = -4*m.pi*x/(1 - e**2)
gr = 6*m.pi*GMsun/(a*c**2*(1 - e**2))
print(f"GM/(a v*^2) = {x:.4f}; gated leading-order = {gated:.4f} beta rad/orbit; GR = {gr:.4e} rad/orbit; beta for equality = {gr/abs(gated):.2e}")
print(f"Mercury orbital speed range: {m.sqrt(GMsun*(1+e)/(a*(1-e)))/1e3:.1f} to {m.sqrt(GMsun*(1-e)/(a*(1+e)))/1e3:.1f} km/s")

print("=== extra: Jeans-type length of a gated 1/r attraction of strength beta G among co-movers (narrow gate) ===")
Gpc = 4.30091e-3      # pc (km/s)^2 / Msun
GeVcm3_to_Msunpc3 = 1/37.97   # 1 Msun/pc^3 = 37.97 GeV/cm^3
for name, rho, sig in (("MW solar circle", 0.4, 155.0), ("MW inner 1 kpc", 10.0, 120.0), ("classical dwarf core", 1.0, 30.0), ("UFD (Segue 1-like)", 100.0, 3.7)):
    rho_pc = rho*GeVcm3_to_Msunpc3
    frac = min(1.0, (vstar/sig)**3/(2*m.pi)**1.5)
    s_eff = min(sig, vstar)
    lamJ = 2*m.pi*s_eff/m.sqrt(4*m.pi*Gpc*rho_pc*frac)
    lamJ_grav = 2*m.pi*sig/m.sqrt(4*m.pi*Gpc*rho_pc)
    print(f"{name:22s}: co-moving fraction {frac:.3f}; gated Jeans length (beta = 1) = {lamJ/1e3:.2f} kpc; ordinary Jeans length = {lamJ_grav/1e3:.2f} kpc")
