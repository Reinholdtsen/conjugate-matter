#!/usr/bin/env python3
"""
knot_numbers.py — every number quoted in papers/knot-dark-matter-standalone.md
(#14), recomputed, plus the numbers the round-2 review disputes.

    .venv/bin/python verify/knot_numbers.py

Two kinds of output:
  PASS/FAIL  a figure the manuscript quotes, checked at the precision it is
             quoted. Exit code 1 if any fails.
  NOTE       a figure the manuscript does not yet quote: round-2 adjudication
             inputs for v3. Printed, not gated. When v3 quotes one, it moves
             to a check.

Inputs are standard reference values (PDG, Planck 2018), from model memory and
listed below; the flux limits are the manuscript's own and are being
source-checked separately.
"""
import sys
from math import pi, log, log10

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def note(name, detail):
    print(f"NOTE  {name}  [{detail}]")
def sig(x, n=1):
    return float(f"{x:.{n-1}e}")

# Reference values
M_PL = 1.22089e19        # GeV, Planck mass
M_PL_RED = 2.43536e18    # GeV, reduced Planck mass
S0 = 2891.2              # cm^-3, present entropy density
RHO_CRIT_H2 = 1.05371e-5 # GeV cm^-3, critical density / h^2
OMEGA_C_H2 = 0.120       # cold dark matter, Planck 2018
GEV_G = 1.78266e-24      # g per GeV/c^2
GEV2_CM2 = 3.8938e-28    # cm^2 per GeV^-2
C_CM = 2.99792458e10     # cm/s
ALPHA = 1/137.035999
KM3_CM3 = 1e15
MZ = 91.1876; ALPHA_EM_INV_MZ = 127.951; SIN2W_MZ = 0.23122; ALPHA_S_MZ = 0.1180
# Manuscript inputs
RHO_LOCAL = 0.4          # GeV cm^-3
V_HALO = 1e-3            # in units of c
PARKER = 1e-15; MACRO = 1.4e-16   # cm^-2 s^-1 sr^-1
ALPHA_D = 34

print("== Sec. 2: the coupling")
check("alpha_d = 1/(4 alpha) ~ 34 (Dirac normalization)", round(1/(4*ALPHA))==34, f"{1/(4*ALPHA):.2f}")
note("convention spread", f"1/(4a) = {1/(4*ALPHA):.2f} for eg = 2 pi n; 1/a = {1/ALPHA:.2f} for eg = 4 pi n "
     "(the 't Hooft-Polyakov charge 4 pi/e)")

print("\n== Sec. 3: abundance (Kibble, n/s = p (Lambda_c/M_Pl)^3, M = 100 Lambda_c)")
rho_dm = OMEGA_C_H2*RHO_CRIT_H2
check("mean rho_DM = 1.26 keV/cm^3", round(rho_dm*1e6,2)==1.26, f"{rho_dm*1e6:.4f} keV/cm^3")
def kibble_lambda(mpl, p=1.0, ratio=100.0):
    return (rho_dm*mpl**3/(ratio*p*S0))**0.25
lam = kibble_lambda(M_PL); m_star = 100*lam
check("Lambda_c ~ 3e11 GeV", sig(lam)==3e11, f"{lam:.3e}")
check("M ~ 3e13 GeV", sig(m_star)==3e13, f"{m_star:.3e}")
shift = lam/kibble_lambda(M_PL_RED)
check("reduced-Planck convention shifts both down by ~3", round(shift)==3, f"x{shift:.2f}")
p_horizon = 45/(2*pi**2*100)
note("p sensitivity", f"one defect per horizon with g*=100 gives p = {p_horizon:.4f}; "
     f"Lambda_c, M scale as p^(-1/4): M = {100*kibble_lambda(M_PL, p_horizon):.2e} GeV")
for M in [1e13, m_star, 1e15, 1e16, 1e17]:
    D = (M/m_star)**4
    verdict = ("matches" if 2/3 < D < 1.5 else
               "needs that much entropy dilution" if D > 1 else "under-produced")
    note(f"window M = {M:.1e} GeV", f"Kibble p=1 abundance / observed = {D:.1e} ({verdict})")

print("\n== Sec. 3: benchmark M = 1e16 GeV")
M = 1e16
n_mean = rho_dm/M; n_loc = RHO_LOCAL/M
check("mean n ~ 1.3e-22 /cm^3", sig(n_mean,2)==1.3e-22, f"{n_mean:.3e}")
check("local: one soliton per ~25 km^3", round(1/n_loc/KM3_CM3)==25, f"{1/n_loc/KM3_CM3:.2f} km^3")

print("\n== Sec. 4: flux and exclusion (our U(1), counterfactual)")
def flux(M):
    return (RHO_LOCAL/M)*V_HALO*C_CM/(4*pi)
F = flux(1e16)
check("F = n v / 4 pi ~ 1e-10 /cm^2/s/sr", round(log10(F))==-10, f"{F:.3e}")
check("exceeds Parker (~1e-15) by five orders", round(log10(F/PARKER))==5, f"{log10(F/PARKER):.2f}")
check("exceeds MACRO (1.4e-16) by six", round(log10(F/MACRO))==6, f"{log10(F/MACRO):.2f}")
eps = PARKER/F
check("mixing threshold eps ~ 1e-5 (Parker, bound taken as 1/charge)", round(log10(eps))==-5, f"{eps:.2e}")
note("dimension-5 mixing Phi F B / M, <Phi> ~ Lambda_c", f"eps ~ {lam/M_PL:.1e} (M = M_Pl), "
     f"{lam/M_PL_RED:.1e} (M = reduced M_Pl); threshold {eps:.1e}")
for M in [m_star, 1e16, 1e17]:
    Fm = flux(M); Fext = 1e-16*(M/1e17)
    note(f"extended Parker at M = {M:.1e}", f"F = {Fm:.2e}; 1e-16 (M/1e17 GeV) = {Fext:.1e}; "
         f"excess {log10(Fm/Fext):.2f} orders (vs Parker {log10(Fm/PARKER):.2f})")

print("\n== Sec. 4: self-interaction")
def sigma_over_M(M, a, v, lnL):
    sigma = 8*pi*a**2*lnL/((M/2)**2*v**4)          # GeV^-2
    return sigma*GEV2_CM2/(M*GEV_G)                 # cm^2/g
lnL_implied = 3e-34/sigma_over_M(1e16, ALPHA_D, V_HALO, 1.0)
check("sigma_T/M ~ 3e-34 cm^2/g at v=1e-3 c (implied ln Lambda in 5..40)", 5 <= lnL_implied <= 40,
      f"ln Lambda = {lnL_implied:.1f}; ln Lambda=10..30 gives {sigma_over_M(1e16,ALPHA_D,V_HALO,10):.1e}"
      f"..{sigma_over_M(1e16,ALPHA_D,V_HALO,30):.1e}")
check("some thirty orders below ~1 cm^2/g", 30 <= -log10(sigma_over_M(1e16,ALPHA_D,V_HALO,lnL_implied)) < 35)

print("\n== Sec. 4: gravitational waves (f0 = 1.65e-5 Hz (f*/H*)(T/100 GeV)(g*/100)^(1/6))")
def f_peak(T, fH=1.0, gstar=100.0):
    return 1.65e-5*fH*(T/100)*(gstar/100)**(1/6)
check("f ~ 1e4 Hz at Lambda_c = 1e11 GeV (f*/H* = 1)", round(log10(f_peak(1e11)))==4, f"{f_peak(1e11):.2e}")
check("f ~ 1e7 Hz at Lambda_c = 1e14 GeV (f*/H* = 1)", round(log10(f_peak(1e14)))==7, f"{f_peak(1e14):.2e}")
note("f*/H* spread", f"f*/H* = 10, 100 multiplies by 10, 100: up to {f_peak(1e14,100):.1e} Hz")

print("\n== Round 2: does running drag alpha_d from 34 toward ~6-8? (one-loop SM, no thresholds)")
inv0 = {"Y": ALPHA_EM_INV_MZ*(1-SIN2W_MZ), "2": ALPHA_EM_INV_MZ*SIN2W_MZ, "3": 1/ALPHA_S_MZ}
b = {"Y": 41/6, "2": -19/6, "3": -7.0}
def inv(i, mu):
    return inv0[i] - b[i]/(2*pi)*log(mu/MZ)
def inv_em(mu):
    return inv("Y",mu) + inv("2",mu)    # 1/e^2 = 1/g'^2 + 1/g^2
check("running code reproduces alpha_em^-1(MZ) = 127.95", round(inv_em(MZ),2)==127.95, f"{inv_em(MZ):.3f}")
for mu in [1e11, 3e11, 1e14, 1e16]:
    a_em_inv = inv_em(mu)
    note(f"mu = {mu:.0e} GeV", f"alpha_em^-1 = {a_em_inv:.1f} -> 1/(4a) = {a_em_inv/4:.1f}; "
         f"alpha_2^-1 = {inv('2',mu):.1f} -> {inv('2',mu)/4:.1f}; alpha_3^-1 = {inv('3',mu):.1f} -> {inv('3',mu)/4:.1f}")

print("\n== Soliton mass vs which coupling (M ~ Lambda_c / alpha_e, alpha_m ~ 1/alpha_e)")
note("alpha_e = 1/137", f"M/Lambda_c ~ {1/ALPHA:.0f} (the manuscript's ~100); monopole alpha_m ~ {1/ALPHA:.0f}")
note("alpha_e = 34", f"M/Lambda_c ~ {1/ALPHA_D:.3f}; semiclassical soliton not heavy, formula unreliable")

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — every number #14 v2 quotes reproduces.")
