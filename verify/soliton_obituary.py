#!/usr/bin/env python3
"""
soliton_obituary.py — every number that review/round3-adjudication.md quotes
for the withdrawn soliton candidate (#14 v3), recomputed and checked.

    .venv/bin/python verify/soliton_obituary.py

Exit code 1 if any check fails. Anchors come first and are independent of the
manuscript (a textbook identity; a published value).

This replaces knot_numbers.py. That file checked v3's own claims. v3 was
withdrawn after round 3, so it makes no current claims; its checks are in git
history (last at 96f58da). What is checked here is the corrected record.

Model (as in v3): SU(2)_d -> U(1)_d by an adjoint Higgs with vev v; Dirac
doublet psi of dark charge g_d/2 = e (hypothesis H); monopole mass
M = 4 pi f v / g_d, f = 1 (BPS) to 1.787; T_c ~ v. Kibble with one defect per
Hubble volume, the causal minimum. Freeze-out: s-wave, Kolb & Turner eqs.
5.43-5.45. Reference constants: PDG and Planck 2018 values.
"""
import sys
from math import pi, log, log10, sqrt

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)

M_PL = 1.22089e19; M_PL_RED = 2.43536e18          # GeV
S0 = 2891.2                                       # cm^-3
RHO_DM = 0.120*1.05371e-5                         # GeV cm^-3
ALPHA = 1/137.035999
CM3S_PER_GEV2 = 3.8938e-28*2.99792458e10
GS_SM_HIGH = 106.75; GS_NU_DEC = 10.75
GSTAR = 100.0
M_BENCH = 3e13                                    # v3's withdrawn benchmark, GeV
F_RANGE = (1.0, 1.787)

def omega_h2(m, sigma0, g, gstar):
    xf = 20.0
    for _ in range(100):
        xf = log(0.038*g*M_PL*m*sigma0/sqrt(gstar)) - 0.5*log(xf)
    return 1.07e9*xf/(sqrt(gstar)*M_PL*sigma0)
def delta_neff(g_eff, r):
    return (4/7)*g_eff*r**4

print("== Anchors")
H_COEFF = sqrt(8*pi**3*GSTAR/90)
check("Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl", round(sqrt(8*pi**3/90),2)==1.66)
P_H = H_COEFF**3*45/(2*pi**2*GSTAR)
P_H_RED = sqrt(pi**2*GSTAR/90)**3*45/(2*pi**2*GSTAR)
check("one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)",
      50 <= P_H <= 200, f"p = {P_H:.2f}")
check("freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)",
      0.06 <= omega_h2(100.0, 2.2e-26/CM3S_PER_GEV2, 2, 90) <= 0.24)
check("Delta N_eff: one extra neutrino species at T_nu gives 1", abs(delta_neff(7/4, 1.0)-1) < 1e-12)

print("\n== Kibble normalization (ruling 1)")
check("p = 104.31 with M_Pl", round(P_H,2)==104.31, f"{P_H:.4f}")
check("p = 0.828 with reduced M_Pl", round(P_H_RED,3)==0.828, f"{P_H_RED:.4f}")
check("v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3", round(H_COEFF**3, -2)==4600 and
      round(P_H/H_COEFF**3,4)==0.0228, f"{H_COEFF**3:.1f}")

print("\n== Mass and overproduction (ruling 2)")
g_d = 2*sqrt(4*pi*ALPHA)
def m_star(r, p, mpl=M_PL):
    return r*(RHO_DM*mpl**3/(r*p*S0))**0.25
stars = [m_star(4*pi*f/g_d, P_H) for f in F_RANGE]
lo, hi = min(stars), max(stars)
check("M* at minimum production = 2.9-4.4e12 GeV", round(lo/1e11)==29 and round(hi/1e11)==44,
      f"{lo:.3e}-{hi:.3e}")
check("the two Planck conventions agree when p is normalized consistently",
      abs(m_star(20.0, P_H)/m_star(20.0, P_H_RED, M_PL_RED) - 1) < 0.01)
over_lo, over_hi = (M_BENCH/hi)**4, (M_BENCH/lo)**4
check("the 3e13 benchmark is overproduced 2.1e3-1.2e4 times", round(over_lo/100)==21 and round(over_hi/1e3)==12,
      f"{over_lo:.2e}-{over_hi:.2e}")

print("\n== psi relic window (ruling 4): psi, psi-bar, both doublet members; sigma v = pi alpha^2/m^2")
def m_for(target, gstar):
    lo_m, hi_m = 1.0, 1e6
    for _ in range(200):
        m = sqrt(lo_m*hi_m)
        lo_m, hi_m = (m, hi_m) if 4*omega_h2(m, pi*ALPHA**2/m**2, 2, gstar) < target else (lo_m, m)
    return m
m10 = [m_for(0.012, gs) for gs in (80.0, GS_SM_HIGH)]
m100 = [m_for(0.12, gs) for gs in (80.0, GS_SM_HIGH)]
check("10% of the dark matter at 45-49 GeV", round(m10[0])==45 and round(m10[1])==49,
      f"{m10[0]:.1f}-{m10[1]:.1f}")
check("100% at 146-158 GeV", round(m100[0])==146 and round(m100[1])==158, f"{m100[0]:.1f}-{m100[1]:.1f}")

print("\n== Dark radiation (ruling 5)")
bound = 2.99 + 0.34 - 3.044
r_late = (GS_NU_DEC/GS_SM_HIGH)**(1/3)*((9 + 7/8*8)/2)**(1/3)
xi_max = (bound/delta_neff(2.0, r_late))**0.25
check("95% bound Delta N_eff < 0.286", round(bound,3)==0.286, f"{bound:.3f}")
check("xi < 0.760", round(xi_max,3)==0.760, f"{xi_max:.4f}")
v_hi = M_BENCH/(4*pi*F_RANGE[0]/g_d)
f_top = 1.65e-5*100*(v_hi/xi_max/100)*(GS_SM_HIGH/100)**(1/6)
check("knock-on: GW upper end 3.2e7 Hz at the withdrawn benchmark", round(f_top/1e6)==32, f"{f_top:.2e}")

print("\n== Minimal adjoint-only sector (survives, benchmark-conditional)")
alpha_w = g_d**2/(4*pi)
over = [2*omega_h2(alpha_w*M_BENCH/f, k*pi*alpha_w**2/(alpha_w*M_BENCH/f)**2, 3, GS_SM_HIGH+9)/0.12
        for f in F_RANGE for k in (1.0, 10.0)]
check("stable W'+- overclose by 1e16-1e17", round(log10(min(over)))==16 and round(log10(max(over)))==17,
      f"{min(over):.1e}-{max(over):.1e}")

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — every number the round-3 record quotes reproduces.")
