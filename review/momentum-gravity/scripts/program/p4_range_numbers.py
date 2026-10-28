#!/usr/bin/env python3
"""P4 (label: program). Numbers for: can the program supply a long-range (kpc+) part of momentum gravity?

Inputs and what fixes them:
 - hbar c, G, M_sun, AU, pc, c: CODATA/IAU values typed here (standard constants).
 - H0 = 67.4 km/s/Mpc (Planck 2018 central value, cited in the record's diameter note).
 - Record values: lambda_X < 37.7 um at u = 1 (verify/phase_space_diameter.py output), alpha = (4/3) u^2;
   chi benchmark m = 70 MeV, sigma0/m = 30 cm^2/g, v* = 120 km/s, alpha~ ~ 1, m_phi ~ m (#1 sec. 5.1, Debt 3a);
   g = 2.48e3 GeV^-2 (review/wiki-build-checks/debt3a_check.py output).
 - Cassini: gamma - 1 = (2.1 +/- 2.3) x 10^-5 (Bertotti, Iess, Tortora 2003 [S]).
 - Massive spin-2 PPN gamma with Newtonian strength alpha, unscreened, r << lambda: gamma - 1 = -alpha/(2(1+alpha))
   (p2_spin2_velocity.py, sec. 7b; anchored on the vDVZ 3/4).
 - Vainshtein radius convention as in verify/phase_space_diameter.py: r_V = (r_S (1 + u^2) lambda^2)^(1/3).
"""
import numpy as np

hbarc_eVm = 1.973269804e-7       # eV m
G = 6.67430e-11; c = 2.99792458e8
Msun = 1.98847e30; AU = 1.495978707e11; pc = 3.0856775814913673e16
GeV_to_g = 1.78266192e-24; GeVinv2_to_cm2 = 0.389379e-27
MP = 1.220890e19                 # GeV, Planck mass sqrt(hbar c / G)
H0 = 67.4e3/(1e6*pc)             # 1/s
hbarH0_eV = 6.582119569e-16*H0   # eV
print(f"hbar H0 = {hbarH0_eV:.3e} eV ; c/H0 = {c/H0/(1e9*pc):.2f} Gpc")

print("\n== 1. Mass for a given range, and the non-aligned vacuum's vacuum energy ~ M_X^2")
for name, lam in [("37.7 um (record bound, u = 1)", 37.7e-6), ("1 AU", AU), ("1 pc", pc), ("1 kpc", 1e3*pc),
                  ("100 kpc", 1e5*pc), ("1 Mpc", 1e6*pc), ("c/H0", c/H0)]:
    MX = hbarc_eVm/lam
    print(f"  lambda = {name:30s}: M_X c^2 = {MX:.3e} eV ; (M_X/H0)^2 = {(MX/hbarH0_eV)**2:.2e}")

print("\n== 2. Weakening X's coupling to ordinary matter so its range can be long (alpha = (4/3) u^2 at M_f = M_g)")
g_lo = 2.1e-5 - 2*2.3e-5          # 2-sigma lower end of Cassini gamma - 1 (massive spin-2 pushes gamma below 1)
alpha_max = 2*abs(g_lo)/(1 - 2*abs(g_lo))  # solve alpha/(2(1+alpha)) = |g_lo|
print(f"  Cassini 2-sigma lower end: gamma - 1 > {g_lo:.1e}  ->  alpha < {alpha_max:.2e}  ->  u < {np.sqrt(0.75*alpha_max):.2e}"
      "  (unscreened, lambda_X >> 1 AU)")
print(f"  at alpha = 4/3 (u = 1): gamma - 1 = {-(4/3)/(2*(1+4/3)):.4f}")

print("\n== 3. Vainshtein radius r_V = (r_S (1+u^2) lambda^2)^(1/3) for lambda_X = 1 kpc")
lam = 1e3*pc
for name, M in [("Sun", Msun), ("galaxy mass inside 1 kpc, 1e10 Msun (illustrative)", 1e10*Msun),
                ("dwarf, 1e7 Msun (illustrative)", 1e7*Msun)]:
    rS = 2*G*M/c**2
    for u in [1.0, 6e-3]:
        rV = (rS*(1 + u**2)*lam**2)**(1/3)
        print(f"  {name:50s} u = {u:<6}: r_V = {rV:.2e} m = {rV/AU:.2e} AU = {rV/pc:.2e} pc")

print("\n== 4. The record's chi-chi strength against gravity")
m = 0.070                          # GeV
alt = 1.0
Gm2 = (m/MP)**2
print(f"  G m_chi^2 = {Gm2:.2e} (dimensionless, hbar = c = 1); alpha~/(G m^2) = {alt/Gm2:.2e}")
g = 2.48e3                         # GeV^-2, Debt 3a
print(f"  Debt-3a contact coupling g = {g:.2e} GeV^-2 vs G = 1/M_P^2 = {1/MP**2:.2e} GeV^-2: ratio {g*MP**2:.2e}")
sigma0 = 30.0*m*GeV_to_g           # cm^2
print(f"  sigma0 = (30 cm^2/g) m_chi = {sigma0:.2e} cm^2 = {sigma0/GeVinv2_to_cm2:.2e} GeV^-2")

print("\n== 5. Momentum transfer in halo scattering vs X's range (the 'integrate X out' step needs q << M_X)")
for vk in [30.0, 120.0, 1000.0]:
    q_eV = m*1e9*vk*1e3/c
    print(f"  v = {vk:6.0f} km/s: m_chi v = {q_eV/1e3:.2f} keV ; hbar/(m_chi v) = {hbarc_eVm/q_eV:.2e} m ;"
          f" 37.7 um / (hbar/(m v)) = {37.7e-6/(hbarc_eVm/q_eV):.2e}")
print(f"  benchmark transfer mediator m_phi ~ m_chi: range hbar/(m_phi c) = {hbarc_eVm/(m*1e9):.2e} m")

print("\n== 6. A long-range chi-chi force that made dwarf cores by scattering: required strength vs gravity")
# screened Coulomb, momentum-transfer cross-section: sigma_T = (4 pi A^2/(mu^2 v^4)) ln(mu v^2 lambda/A), A = coupling
mu = m/2
for vk, lamm in [(30.0, 1e3*pc), (30.0, 37.7e-6)]:
    v = vk*1e3/c
    lam_GeV = lamm/(hbarc_eVm*1e-9)        # GeV^-1
    s0 = sigma0/GeVinv2_to_cm2
    A = 1e-9
    for _ in range(60):                     # fixed-point solve sigma_T(A) = sigma0
        lnL = np.log(mu*v**2*lam_GeV/A)
        A = mu*v**2*np.sqrt(s0/(4*np.pi*lnL))
    print(f"  v = {vk} km/s, range {lamm:.2e} m: required A = {A:.2e} (ln = {lnL:.0f}); A/(G m^2) = {A/Gm2:.2e}")
# X at gravitational strength (alpha = 4/3), range 37.7 um: its chi-chi transfer cross-section at 30 km/s
A_X = (4/3)*Gm2; v = 30e3/c; lam_GeV = 37.7e-6/(hbarc_eVm*1e-9)
sT = 4*np.pi*A_X**2/(mu**2*v**4)*np.log(mu*v**2*lam_GeV/A_X)
print(f"  X at alpha = 4/3, 37.7 um, v = 30 km/s: sigma_T = {sT*GeVinv2_to_cm2:.2e} cm^2 ; sigma_T/sigma0 = {sT*GeVinv2_to_cm2/sigma0:.2e}")

print("\n== 7. chi-nucleon X exchange if chi's X coupling is what makes sigma0 (assumptions in the claim)")
mN = 0.9383; muN = m*mN/(m + mN)
ratio = (muN/mu)**2*(4/3)*(mN/MP)**2/alt
print(f"  sigma_chiN/sigma_chichi = (mu_chiN/(m/2))^2 alpha G m_N^2/alpha~ = {ratio:.2e} ; sigma_chiN = {ratio*sigma0:.2e} cm^2")

print("\n== 8. Size of the inertia change in a velocity-gated Newtonian potential: eps = 2 beta |Phi|/v*^2 (v* = 120 km/s)")
vstar = 120.0
for name, phi_kms2 in [("Earth around the Sun, |Phi| = v_orb^2, v_orb = 29.8 km/s", 29.8**2),
                       ("Milky Way at the Sun, |Phi| ~ v_c^2, v_c = 230 km/s", 230.0**2),
                       ("classical dwarf, |Phi| ~ 3 sigma^2, sigma = 10 km/s", 3*10.0**2),
                       ("ultra-faint dwarf, |Phi| ~ 3 sigma^2, sigma = 3.7 km/s", 3*3.7**2)]:
    print(f"  {name:60s}: eps/beta = {2*phi_kms2/vstar**2:.3f}")
fr = (vstar/155.0)**3/(2*np.pi)**1.5
print(f"  co-moving fraction in the MW halo (sigma = 155 km/s), n_gate/n = (v*/sigma)^3/(2 pi)^1.5 = {fr:.3f};"
      f" eps/beta with only that fraction gated = {fr*2*230.0**2/vstar**2:.3f}")
print(f"  inertia singularity of the Lagrangian form, r_* = 2 beta GM/v*^2, for the Sun (beta = 1): {2*G*Msun/(vstar*1e3)**2/AU:.3f} AU")

print("\n== 9. Illustration: the same gate acting on ordinary matter (excluded by the record: no gate for SM)")
a_m = 0.387098*AU; e_m = 0.205630
x = G*Msun/(a_m*(vstar*1e3)**2)
dw_gated = -4*np.pi*x/(1 - e_m**2)          # per orbit, per unit beta, leading order in GM/(a v*^2)
dw_GR = 6*np.pi*G*Msun/(a_m*c**2*(1 - e_m**2))
print(f"  Mercury: GM/(a v*^2) = {x:.3f}; gated precession per orbit = {dw_gated:.3e} beta rad (leading order);"
      f" GR = {dw_GR:.3e} rad; ratio = {dw_gated/dw_GR:.3e} beta")
print(f"  beta for which |gated| = GR precession: {abs(dw_GR/dw_gated):.1e}")

print("\n== 10. Strong-coupling scale of a light massive spin-2, Lambda_3 = (M_X^2 M_Pl)^(1/3), M_Pl reduced = 2.435e18 GeV (literature form, dagger)")
MPl_red_eV = 2.435e27
for name, lamm in [("37.7 um", 37.7e-6), ("1 kpc", 1e3*pc), ("c/H0", c/H0)]:
    MX = hbarc_eVm/lamm
    L3 = (MX**2*MPl_red_eV)**(1/3)
    print(f"  range {name:8s}: M_X = {MX:.2e} eV, Lambda_3 = {L3:.2e} eV, 1/Lambda_3 = {hbarc_eVm/L3:.2e} m")
