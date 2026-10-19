#!/usr/bin/env python3
"""
knot_numbers.py — every number quoted in papers/knot-dark-matter-standalone.md
(#14, v3), recomputed and checked at the precision the manuscript quotes it.

    .venv/bin/python verify/knot_numbers.py

Exit code 1 if any check fails. Anchor checks come first: each formula is
tested against a known case before its estimate is trusted. The v2 figures
this file used to check are in git history (commit d15cd4a).

Round 3 (review/round3-adjudication.md) found two physics inputs here wrong:
the Kibble normalization p (one defect per Hubble volume is p = 104, not
0.023; it is the causal minimum, not an upper end) and the psi relic count
(psi-bar and both doublet members omitted; sigma v for psi psi-bar -> 2 gamma'
is exact, so no kappa bracket). Both are corrected below, so the checks of
v3's claims that rest on them FAIL. That is the intended state until v3 is
revised or withdrawn. An earlier Kibble "anchor" that reproduced v2's own
number was circular and has been replaced with independent ones.

Model (v3): SU(2)_d -> U(1)_d by an adjoint Higgs with vev v, at least one
Dirac doublet psi of dark charge g_d/2. Hypothesis H: the smallest dark
charge equals ours, (g_d/2)^2/4pi = alpha. Monopole mass M = 4 pi f v / g_d,
f = 1 (BPS) to 1.787 (large Higgs self-coupling); W' mass g_d v; transition
temperature T_c ~ v. Freeze-out: s-wave, Kolb & Turner eqs. 5.43-5.45, with
the annihilation coefficient kappa in sigma v = kappa pi alpha^2/m^2
bracketed, not computed. Reference constants (PDG, Planck 2018) are from
model memory except the N_eff bound (Planck 2018 VI, live-checked).
"""
import sys
from math import pi, log, log10, sqrt

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def sig(x, n=1):
    return float(f"{x:.{n-1}e}")

# Reference values
M_PL = 1.22089e19        # GeV, Planck mass
M_PL_RED = 2.43536e18    # GeV, reduced Planck mass
S0 = 2891.2              # cm^-3, present entropy density
RHO_DM = 0.120*1.05371e-5   # GeV cm^-3, mean cold dark matter density
GEV_G = 1.78266e-24      # g per GeV/c^2
GEV2_CM2 = 3.8938e-28    # cm^2 per GeV^-2
C_CM = 2.99792458e10     # cm/s
CM3S_PER_GEV2 = GEV2_CM2*C_CM
ALPHA = 1/137.035999
KM3_CM3 = 1e15
MZ = 91.1876; ALPHA_EM_INV_MZ = 127.951; SIN2W_MZ = 0.23122
GS_SM_HIGH = 106.75; GS_NU_DEC = 10.75
DNEFF_BOUND = 2.99 + 0.34 - 3.044   # Planck 2018 95% upper N_eff, minus the SM's 3.044
# Manuscript inputs
RHO_LOCAL = 0.4          # GeV cm^-3
V_HALO = 1e-3            # c
PARKER = 1e-15           # cm^-2 s^-1 sr^-1, PDG 2024, M < 1e17 GeV
MACRO_LOW_M = 2.8e-16    # MACRO, m > 1e10 GeV, beta > 1e-4
M_BENCH = 3e13           # GeV
F_RANGE = (1.0, 1.787)
GSTAR = 100.0
H_COEFF = sqrt(8*pi**3*GSTAR/90)       # H = H_COEFF T^2 / M_Pl in the radiation era
P_HORIZON = H_COEFF**3*45/(2*pi**2*GSTAR)                       # one defect per H^-3: n/s = p (T/M_Pl)^3
P_HORIZON_RED = sqrt(pi**2*GSTAR/90)**3*45/(2*pi**2*GSTAR)      # the same, in reduced-Planck units

def omega_h2(m, sigma0, g, gstar):
    xf = 20.0
    for _ in range(100):
        xf = log(0.038*g*M_PL*m*sigma0/sqrt(gstar)) - 0.5*log(xf)
    return 1.07e9*xf/(sqrt(gstar)*M_PL*sigma0)
def delta_neff(g_eff, r):
    return (4/7)*g_eff*r**4
b = {"Y": 41/6, "2": -19/6}
inv0 = {"Y": ALPHA_EM_INV_MZ*(1-SIN2W_MZ), "2": ALPHA_EM_INV_MZ*SIN2W_MZ}
def inv_em(mu):
    return sum(inv0[i] - b[i]/(2*pi)*log(mu/MZ) for i in "Y2")

print("== Anchors")
check("freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)",
      0.06 <= omega_h2(100.0, 2.2e-26/CM3S_PER_GEV2, 2, 90) <= 0.24,
      f"{omega_h2(100.0, 2.2e-26/CM3S_PER_GEV2, 2, 90):.3f}")
check("Delta N_eff: one extra neutrino species at T_nu gives 1", abs(delta_neff(7/4, 1.0)-1) < 1e-12)
check("running: alpha_em^-1(MZ) = 127.95 from alpha_Y and alpha_2", round(inv_em(MZ),2)==127.95)
check("Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl", round(sqrt(8*pi**3/90),2)==1.66)
check("Kibble: one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)",
      50 <= P_HORIZON <= 200, f"p = {P_HORIZON:.1f}")

print("\n== Sec. 2: couplings")
g_d = 2*sqrt(4*pi*ALPHA)
alpha_w = g_d**2/(4*pi)
alpha_m = 1/alpha_w
check("alpha_W' = 4 alpha ~ 1/34", round(1/alpha_w)==34, f"1/{1/alpha_w:.2f}")
check("monopole coupling alpha_m = 1/(4 alpha) ~ 34", round(alpha_m)==34, f"{alpha_m:.2f}")
check("matching the W' instead: alpha_m = 1/alpha ~ 137", round(1/ALPHA)==137)
check("matching at mu = 1e12 GeV: 1/(4 alpha(mu)) ~ 29", round(inv_em(1e12)/4)==29,
      f"alpha^-1 = {inv_em(1e12):.1f}")

print("\n== Sec. 3: the soliton")
r_lo, r_hi = (4*pi*f/g_d for f in F_RANGE)
check("M/v = 4 pi f / g_d ~ 21-37", round(r_lo)==21 and round(r_hi)==37, f"{r_lo:.2f}-{r_hi:.2f}")
v_lo, v_hi = M_BENCH/r_hi, M_BENCH/r_lo
check("benchmark v ~ (0.8-1.4)e12 GeV", round(v_lo/1e11)==8 and round(v_hi/1e11)==14, f"{v_lo:.2e}-{v_hi:.2e}")
mw_lo, mw_hi = alpha_w*M_BENCH/F_RANGE[1], alpha_w*M_BENCH/F_RANGE[0]
check("benchmark m_W' ~ (5-9)e11 GeV", round(mw_lo/1e11)==5 and round(mw_hi/1e11)==9, f"{mw_lo:.2e}-{mw_hi:.2e}")

check("mean rho_DM = 1.26 keV/cm^3", round(RHO_DM*1e6,2)==1.26, f"{RHO_DM*1e6:.4f}")
check("one defect per horizon volume: p ~ 0.023", round(P_HORIZON,3)==0.023, f"{P_HORIZON:.4f}")
def m_star(r, p, mpl=M_PL, xi=1.0):
    v = (RHO_DM*mpl**3*xi**3/(r*p*S0))**0.25
    return r*v
# One defect per Hubble volume is the causal minimum; Kibble-Zurek or bubble counting only adds.
stars = [m_star(r, P_HORIZON) for r in (r_lo, r_hi)]
lo, hi = min(stars), max(stars)
check("Kibble-consistent M* ~ (0.9-3.7)e13 GeV over f and p", round(lo/1e12)==9 and round(hi/1e12,-0)==37,
      f"{lo:.2e}-{hi:.2e} at minimum production, p = {P_HORIZON:.1f}")
check("benchmark 3e13 lies inside the band", lo <= M_BENCH <= hi,
      f"benchmark overproduced x{(M_BENCH/hi)**4:.1e}-{(M_BENCH/lo)**4:.1e} even at minimum production")
check("the band spans a factor of four", round(hi/lo)==4, f"x{hi/lo:.2f}")
ratio = m_star(r_lo, P_HORIZON)/m_star(r_lo, P_HORIZON_RED, M_PL_RED)
check("conventions agree when p is normalized consistently", abs(ratio-1) < 0.01, f"x{ratio:.4f}")
check("reduced-Planck convention lowers M* by ~3", round(ratio)==3, f"x{ratio:.2f}")
D = (1e16/sqrt(lo*hi))**4
check("M = 1e16 GeV needs entropy dilution ~1e10", round(log10(D))==10, f"{D:.2e}")

print("\n== Sec. 3: the minimal (adjoint-only) model fails")
over = []
for f in F_RANGE:
    m_w = alpha_w*M_BENCH/f
    for kappa in (1.0, 10.0):
        over.append(2*omega_h2(m_w, kappa*pi*alpha_w**2/m_w**2, 3, GS_SM_HIGH+9)/0.12)
check("stable W'+- overclose by 1e16-1e17", round(log10(min(over)))==16 and round(log10(max(over)))==17,
      f"{min(over):.1e}-{max(over):.1e} x observed")
def m_for_omega(target):
    # psi and psi-bar for both doublet members (x4); sigma v = pi alpha^2/m^2 is exact s-wave
    lo_m, hi_m = 1.0, 1e9
    for _ in range(200):
        m = sqrt(lo_m*hi_m)
        oh2 = 4*omega_h2(m, pi*ALPHA**2/m**2, 2, GS_SM_HIGH)
        lo_m, hi_m = (m, hi_m) if oh2 < target else (lo_m, m)
    return m
m10, m100 = m_for_omega(0.012), m_for_omega(0.12)
check("psi is <10% of the dark matter for m_psi < 0.1-0.3 TeV", 100 <= m10 <= 300, f"{m10:.0f} GeV")
check("psi would be all of it at 0.3-1 TeV", 300 <= m100 <= 1000, f"{m100:.0f} GeV")

print("\n== Sec. 3: benchmark densities (M = 3e13 GeV)")
n_mean = RHO_DM/M_BENCH; n_loc = RHO_LOCAL/M_BENCH
check("mean n ~ 4.2e-20 /cm^3", sig(n_mean,2)==4.2e-20, f"{n_mean:.3e}")
vol = 1/n_loc/KM3_CM3; spacing_m = (1/n_loc)**(1/3)/100
check("local: one per ~0.075 km^3, spacing ~420 m", round(vol,3)==0.075 and round(spacing_m,-1)==420,
      f"{vol:.4f} km^3, {spacing_m:.0f} m")

print("\n== Sec. 4: the counterfactual (if these were monopoles of our U(1))")
F = n_loc*V_HALO*C_CM/(4*pi)
check("F = n v / 4 pi ~ 3e-8 /cm^2/s/sr", sig(F)==3e-8, f"{F:.2e}")
check("exceeds Parker by 7.5 orders", round(log10(F/PARKER),1)==7.5, f"{log10(F/PARKER):.2f}")
check("exceeds MACRO (2.8e-16) by eight", round(log10(F/MACRO_LOW_M))==8, f"{log10(F/MACRO_LOW_M):.2f}")
ext = (M_BENCH/1e17 + 3e-6)*1e-16
check("exceeds extended Parker by twelve", round(log10(F/ext))==12, f"{log10(F/ext):.2f}")

print("\n== Sec. 2/4: kinetic mixing, dark radiation")
eps_lo, eps_hi = v_lo/M_PL, v_hi/M_PL_RED
check("dimension-5 mixing eps ~ v/M ~ 1e-7 to 1e-6", round(log10(eps_lo))==-7 and round(log10(eps_hi))==-6,
      f"{eps_lo:.1e}-{eps_hi:.1e}")
r_late = (GS_NU_DEC/GS_SM_HIGH)**(1/3)*((9 + 7/8*8)/2)**(1/3)
dn = delta_neff(2.0, r_late)
xi_max = (DNEFF_BOUND/dn)**0.25
check("one light doublet, equal temperatures: Delta N_eff ~ 0.86", round(dn,2)==0.86, f"{dn:.3f}")
check("Planck bound needs xi < 0.77", round(xi_max,2)==0.77, f"{xi_max:.3f}")
check("colder dark sector moves M* by xi^(3/4) ~ x0.8", round(xi_max**0.75,1)==0.8, f"x{xi_max**0.75:.2f}")

print("\n== Sec. 4: self-interaction and gravitational waves")
def sigma_over_M(M, a, v, lnL):
    return 8*pi*a**2*lnL/((M/2)**2*v**4)*GEV2_CM2/(M*GEV_G)
s_lo, s_hi = (sigma_over_M(M_BENCH, alpha_m, V_HALO, L) for L in (10, 30))
check("sigma_T/M ~ 1e-26 cm^2/g for ln Lambda = 10-30", round(log10(s_lo))==-26 and round(log10(s_hi))==-26,
      f"{s_lo:.1e}-{s_hi:.1e}")
def f_peak(T, fH, gstar=GS_SM_HIGH):
    return 1.65e-5*fH*(T/100)*(gstar/100)**(1/6)
f_lo, f_hi = f_peak(v_lo, 1.0), f_peak(v_hi/xi_max, 100.0)
check("GW peak ~1e5-1e7 Hz for f*/H* = 1-100", round(log10(f_lo))==5 and round(log10(f_hi))==7,
      f"{f_lo:.1e}-{f_hi:.1e}")

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — every number #14 v3 quotes reproduces.")
