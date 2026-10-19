#!/usr/bin/env python3
"""
dark_sector.py — order-of-magnitude checks on the dual gauge sector's
elementary states and radiation (review/v3-worklog.md, items O1 and O2).

    .venv/bin/python verify/dark_sector.py

PASS/FAIL lines test the formulas against known anchors (a standard thermal
relic; one extra neutrino species). NOTE lines are the estimates. Exit code
1 if an anchor fails.

Model: SU(2)_d -> U(1)_d by an adjoint Higgs (R6), elementary coupling
alpha_e,d = alpha (F2). Monopole mass M = 4 pi v f / g, W' mass g v, so
m_W' = alpha M / f with f = 1 (BPS) to 1.787 (large Higgs self-coupling).
Freeze-out by the s-wave formula of Kolb & Turner, The Early Universe,
eqs. 5.43-5.45. The annihilation coefficient kappa in
sigma v = kappa pi alpha^2 / m^2 is bracketed, not computed. Constants and
the N_eff bound are from model memory.
"""
import sys
from math import pi, log, sqrt

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def note(name, detail):
    print(f"NOTE  {name}  [{detail}]")

M_PL = 1.22089e19            # GeV
S0 = 2891.2                  # cm^-3
RHO_DM = 0.120*1.05371e-5    # GeV cm^-3
ALPHA = 1/137.035999
CM3S_PER_GEV2 = 3.8938e-28*2.99792458e10   # sigma v: GeV^-2 -> cm^3/s
GS_SM_HIGH = 106.75          # SM g*s above the electroweak scale
GS_NU_DEC = 10.75            # SM g*s at neutrino decoupling
DNEFF_BOUND = 0.3            # approximate Planck 2018 upper limit on Delta N_eff

def omega_h2(m, sigma0, g, gstar):
    """s-wave freeze-out relic abundance of one species (Kolb & Turner)."""
    xf = 20.0
    for _ in range(100):
        xf = log(0.038*g*M_PL*m*sigma0/sqrt(gstar)) - 0.5*log(xf)
    return 1.07e9*xf/(sqrt(gstar)*M_PL*sigma0), xf

print("== Anchors")
oh2, xf = omega_h2(100.0, 2.2e-26/CM3S_PER_GEV2, g=2, gstar=90)
check("freeze-out formula: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)",
      0.06 <= oh2 <= 0.24, f"Omega h^2 = {oh2:.3f}, x_f = {xf:.1f}")
def delta_neff(g_eff, r):
    """Delta N_eff of radiation with g_eff (7/8 included for fermions) at T_d = r T_nu."""
    return (4/7)*g_eff*r**4
check("Delta N_eff formula: one extra neutrino species at T_nu gives 1",
      abs(delta_neff(7/8*2, 1.0) - 1.0) < 1e-12, f"{delta_neff(7/8*2, 1.0):.3f}")

print("\n== O1: the dark W'+- in the minimal model (no lighter dark-charged matter)")
lam = (RHO_DM*M_PL**3/(100*S0))**0.25
m_star = 100*lam
note("benchmark M* (Kibble, p = 1)", f"{m_star:.2e} GeV")
for f in [1.0, 1.787]:
    m_w = ALPHA*m_star/f
    for kappa in [1.0, 10.0]:
        sigma0 = kappa*pi*ALPHA**2/m_w**2
        oh2, xf = omega_h2(m_w, sigma0, g=3, gstar=GS_SM_HIGH+9)
        oh2 *= 2                                   # W'+ and W'-
        note(f"f = {f}, kappa = {kappa:g}", f"m_W' = {m_w:.2e} GeV; sigma v = {sigma0*CM3S_PER_GEV2:.1e} cm^3/s; "
             f"Omega h^2 = {oh2:.1e} = {oh2/0.12:.1e} x observed")

print("\n== O1: if W' decays to a lighter dark-charged fermion, how heavy may that relic be?")
def m_for_omega(target, kappa=1.0, g=4, gstar=GS_SM_HIGH+9):
    lo, hi = 1.0, 1e9
    for _ in range(200):
        m = sqrt(lo*hi)
        oh2, _ = omega_h2(m, kappa*pi*ALPHA**2/m**2, g, gstar)
        lo, hi = (m, hi) if oh2 < target else (lo, m)
    return m
for target, label in [(0.12, "all of the dark matter"), (0.012, "10% of it")]:
    note(f"dark-charged Dirac fermion relic = {label}",
         f"m = {m_for_omega(target):.2e} GeV (kappa = 1), {m_for_omega(target, 10.0):.2e} GeV (kappa = 10)")

print("\n== O2: dark radiation (sectors in equilibrium at high T with ratio xi, then separate)")
def r_late(xi, gd_high, gd_late):
    return xi*(GS_NU_DEC/GS_SM_HIGH)**(1/3)*(gd_high/gd_late)**(1/3)
scenarios = [("minimal: SU(2) gauge + adjoint, 9 -> 2", 9.0),
             ("+ one dark Dirac doublet, 16 -> 2", 9.0 + 7/8*8),
             ("+ two dark Dirac doublets, 23 -> 2", 9.0 + 2*7/8*8)]
for label, gd_high in scenarios:
    dn = delta_neff(2.0, r_late(1.0, gd_high, 2.0))
    xi_max = (DNEFF_BOUND/dn)**0.25
    note(label, f"xi = 1: Delta N_eff = {dn:.2f}; bound {DNEFF_BOUND} needs xi < {xi_max:.2f}; "
         f"Kibble M* then scales by xi^(3/4) = {xi_max**0.75:.2f}")

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — anchors pass; estimates above are NOTE-tier.")
