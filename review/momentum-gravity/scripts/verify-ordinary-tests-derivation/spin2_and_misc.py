"""(a) Relative-velocity dependence of one-X exchange between ordinary bodies (a reading the agent's
scope left out); (b) arithmetic spot checks of O10, O14, O15, O16, O20; (c) chi-sector strength scale.
"""
import numpy as np
import sympy as sp

print("=== (a) spin-2 exchange between point masses with relative Lorentz factor gamma ===")
# conserved sources T^{mu nu} = m u^mu u^nu (u.u = 1), propagator numerators on conserved sources [T, dagger]:
#   massless (linearized GR):  T1.T2 - (1/2) T1 T2      massive Fierz-Pauli:  T1.T2 - (1/3) T1 T2
g, b = sp.symbols('gamma beta', positive=True)
massless = g**2 - sp.Rational(1, 2)
massive = g**2 - sp.Rational(1, 3)
r_rest = sp.simplify((massive/massless).subs(g, 1))
print("  massive/massless numerator ratio at rest:", r_rest, " (the 4/3 of alpha = (4/3)(M_f u/M_g)^2)")
rel = sp.simplify((massive/massless)/r_rest)
print("  ratio relative to rest, as gamma -> oo:", sp.limit(rel, g, sp.oo))
ser = sp.series(rel.subs(g, 1/sp.sqrt(1 - b**2)), b, 0, 5)
print("  ratio relative to rest, small beta = v_rel/c:", ser)
print("  each exchange alone, relative to rest: massless", sp.series((massless/massless.subs(g, 1)).subs(g, 1/sp.sqrt(1 - b**2)), b, 0, 4),
      "; massive", sp.series((massive/massive.subs(g, 1)).subs(g, 1/sp.sqrt(1 - b**2)), b, 0, 4))
for v in (30.0, 120.0, 625.0):
    bb = v/299792.458
    print(f"  v_rel = {v} km/s: fractional change of the X/graviton ratio = {float(ser.removeO().subs(b, bb) - 1):.3e}")

print()
print("=== (b) arithmetic spot checks ===")
GM_SUN = 132712440041.94
# O10: speed ranges, standard elements (dagger)
for name, a, e in [('Mercury', 57.909e6, 0.2056), ('Venus', 108.210e6, 0.0068), ('Earth', 149.598e6, 0.0167),
                   ('Mars', 227.956e6, 0.0935), ('Jupiter', 778.479e6, 0.0487), ('Saturn', 1432.041e6, 0.0520)]:
    vc = np.sqrt(GM_SUN/a)
    print(f"  Sun-{name}: {vc*np.sqrt((1-e)/(1+e)):.2f} - {vc*np.sqrt((1+e)/(1-e)):.2f} km/s")
vc = np.sqrt(403503.2355/384400.0)
print(f"  Earth-Moon: {vc*np.sqrt((1-0.0549)/(1+0.0549)):.3f} - {vc*np.sqrt((1+0.0549)/(1-0.0549)):.3f} km/s")
print(f"  Earth-LAGEOS: {np.sqrt(398600.4418/12270.0):.3f} km/s")
GMdp = (1.338185 + 1.248868)*GM_SUN
Pb = 0.10225156248*86400
adp = (GMdp*Pb**2/(4*np.pi**2))**(1/3)
vc = np.sqrt(GMdp/adp)
print(f"  double pulsar: {vc*np.sqrt((1-0.0877775)/(1+0.0877775)):.1f} - {vc*np.sqrt((1+0.0877775)/(1-0.0877775)):.1f} km/s")
# O14: GM_E comparisons (agent's sourced values)
for nm, val, sg in [('Ries 1992', 398600.4356, 0.0004), ('Dunn 1999', 398600.4360, 0.0002)]:
    d = 398600.4354 - val
    s = np.hypot(0.0005, sg)
    print(f"  GM_E LLR - SLR({nm}) = {d:+.4f} km^3/s^2 -> relative {d/398600.4354:+.3e} +- {s/398600.4354:.3e}")
print(f"  Eros: 2-sigma interval for -eps: [{0.076-2*0.269:+.3f}, {0.076+2*0.269:+.3f}] -> |eps| < {0.076+2*0.269:.3f}")
# O15
lo, hi = 2.1e-5 - 2*2.3e-5, 2.1e-5 + 2*2.3e-5
print(f"  Cassini: gamma_fit - 1 in [{lo:.2e}, {hi:.2e}] -> eps K = -(gamma_fit-1)/2 in [{-hi/2:.3e}, {-lo/2:.3e}]")
lo, hi = 0.97 - 1 - 2*0.09, 0.97 - 1 + 2*0.09
print(f"  Collett: eps<K> in [{-hi/2:.3f}, {-lo/2:.3f}]")
# O16: coefficient ratio |W'(u_E)| c^2/(3 v_E v*) at v* = 30 km/s, Gaussian
vE, c = 29.78, 299792.458
for vstar in (30.0, 120.0, 1000.0):
    uE = vE/vstar
    Wp = 2*uE*np.exp(-uE**2)
    coef = Wp*c**2/(3*vE*vstar)
    print(f"  O16 v*={vstar}: |W'(u_E)| c^2/(3 v_E v*) = {coef:.3g} -> |eps| < {1e-3/coef:.2g} if the EIH cross term is fitted to 0.1%")
# O20: orbital part / boost part at V = 370 km/s
V = 370.0
mE_ms, mM_mE = 3.003e-6, 1/81.30
mMars_ms = 3.227e-7
print(f"  O20 Sun-Earth: {2*mE_ms*29.78/(V*(1 - mE_ms)):.3g}; Sun-Mars: {2*mMars_ms*24.13/(V*(1 - mMars_ms)):.3g};"
      f" Earth-Moon: {2*(mM_mE/(1+mM_mE))*1.023/(V*(1 - mM_mE)):.3g}")

print()
print("=== (c) chi-sector scale: gated interaction vs chi-chi gravity at the #11 sec. 8 benchmark ===")
M_P = 1.220890e19     # GeV (dagger)
m_chi = 0.070         # GeV (#11 sec. 8 benchmark, alpha~ = 1)
alpha_G = (m_chi/M_P)**2
print(f"  alpha_G = (m_chi/M_P)^2 = {alpha_G:.3g}; alpha~/alpha_G at alpha~ = 1: {1/alpha_G:.3g}")
print(f"  range hbar/(m_phi c) for m_phi ~ m_chi: {0.1973269804/m_chi:.3g} fm")
