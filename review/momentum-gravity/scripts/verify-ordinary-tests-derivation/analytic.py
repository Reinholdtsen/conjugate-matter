"""Independent analytic checks of the ordinary-tests claims O5, O6, O7, O9 (derivation lens).

Model (task statement): pair Lagrangian per unit reduced mass, GM = total mass parameter,
    L = s^2/2 + (GM/r) [1 + eps W(s/v*)],   s = |v1 - v2|.
Everything here is derived from scratch; nothing is imported from the agent's scripts.
"""
import sympy as sp
import mpmath as mp

u, x, eps, vs, GM, r, a, e, E, c = sp.symbols('u x epsilon v_s GM r a e E c', positive=True)
Wf = sp.Function('W')

print("=== O5: circular-orbit Kepler constant ===")
# planar polar coordinates; rdot, thetadot
R, Rd, Td = sp.symbols('R Rd Td', positive=True)
s = sp.sqrt(Rd**2 + R**2*Td**2)
L = s**2/2 + (GM/R)*(1 + eps*Wf(s/vs))
dL_dRd = sp.diff(L, Rd)
dL_dR = sp.diff(L, R)
# on a circular orbit Rd = 0 and Rdd = 0; d/dt(dL/dRd) is proportional to Rd and Rdd -> 0
# check: dL/dRd is Rd * (something), so its time derivative vanishes when Rd=Rdd=0
print("dL/dRd / Rd simplifies to a finite expression (so d/dt term vanishes on circle):",
      sp.simplify(dL_dRd/Rd).subs(Rd, 0) is not sp.nan)
radial = sp.simplify(dL_dR.subs(Rd, 0))
# speed v = R Td; solve radial eq = 0 for GM
v = sp.symbols('v', positive=True)
radial_v = sp.simplify(radial.subs(Td, v/R))
GMsol = sp.solve(sp.Eq(radial_v, 0), GM)[0]
ratio = sp.simplify(v**2*R/GMsol)    # = 1 + eps*K
print("v^2 r / GM on circular orbit =", ratio)
Kexpr = sp.simplify((ratio - 1)/eps)
print("K =", Kexpr, "   [expected W(u) - u W'(u), u = v/v*]")
for name, W in [("Gaussian", sp.exp(-u**2)), ("Lorentzian", 1/(1 + u**2))]:
    K = sp.simplify(W - u*sp.diff(W, u))
    crit = sp.solve(sp.diff(K, u), u)
    crit = [cc for cc in crit if cc.is_positive]
    print(f"  {name}: K = {sp.factor(K)}; stationary u = {crit}; K_max = {[sp.nsimplify(K.subs(u, cc)) for cc in crit]} = {[sp.N(K.subs(u, cc), 10) for cc in crit]}")
    # redo the circular-orbit derivation with this concrete W (no Function substitution)
    Lc = s**2/2 + (GM/R)*(1 + eps*W.subs(u, s/vs))
    radc = sp.simplify(sp.diff(Lc, R).subs(Rd, 0).subs(Td, v/R))
    GMc = sp.solve(sp.Eq(radc, 0), GM)[0]
    Kc = sp.simplify((sp.simplify(v**2*R/GMc) - 1)/eps)
    print(f"  {name}: direct derivation with this W gives K = W - uW': {sp.simplify(Kc - K.subs(u, v/vs)) == 0}")

print()
print("=== O6: first-order Hamiltonian (Legendre transform, O(eps)) ===")
for name, W in [("Gaussian", sp.exp(-u**2)), ("Lorentzian", 1/(1 + u**2))]:
    sv, P = sp.symbols('s P', positive=True)
    Lr = sv**2/2 + (GM/r)*(1 + eps*W.subs(u, sv/vs))
    p_of_s = sp.diff(Lr, sv)              # magnitude of canonical momentum (parallel to v)
    # invert to first order: s = P + eps*s1
    s1 = sp.symbols('s1')
    eq = sp.series(p_of_s.subs(sv, P + eps*s1) - P, eps, 0, 2).removeO()
    s1sol = sp.solve(sp.Eq(sp.expand(eq).coeff(eps, 1), 0), s1)[0]
    s_of_P = P + eps*s1sol
    H = (sv*p_of_s - Lr).subs(sv, s_of_P)
    H1 = sp.series(H, eps, 0, 2).removeO()
    target = P**2/2 - (GM/r)*(1 + eps*W.subs(u, P/vs))
    print(f"  {name}: H = P^2/2 - (GM/r)(1 + eps W(P/v*)) + O(eps^2): {sp.simplify(sp.expand(H1 - target)) == 0}")

print()
print("=== O7: Delaunay averaging -> apsidal advance per orbit ===")
# Kepler ellipse, eccentric anomaly E: r = a(1 - e cosE), dM = (1 - e cosE) dE, v^2 = (GM/a)(1+e cosE)/(1-e cosE)
# <W/r> over mean anomaly = (1/2pi) int W * (1/r) * (r/a) dE = Phi/a
# Delaunay: Lg = sqrt(GM a), G = Lg sqrt(1-e^2); omega-dot = d<H1>/dG at fixed Lg; H1 = -eps GM W/r
Lg, Gd = sp.symbols('L_g G_d', positive=True)
PhiF = sp.Function('Phi')
a_of = Lg**2/GM
e_of = sp.sqrt(1 - Gd**2/Lg**2)
H1avg = -eps*GM*PhiF(e_of)/a_of
omdot = sp.diff(H1avg, Gd)
T = 2*sp.pi*a_of**sp.Rational(3, 2)/sp.sqrt(GM)
dom = sp.simplify(omdot*T)
# express in e
dom_e = sp.simplify(dom.subs(Gd, Lg*sp.sqrt(1 - e**2)))
print("Delta omega per orbit =", dom_e)
target = 2*sp.pi*eps*sp.sqrt(1 - e**2)/e*sp.Symbol("dPhi/de")
print("  [expected 2 pi eps sqrt(1-e^2)/e * dPhi/de]")

# small-e: Phi(e) = <W(u_c * sqrt((1+e cosE)/(1-e cosE)))>_E
uc = sp.symbols('u_c', positive=True)
cE = sp.cos(E)
xfac = sp.sqrt((1 + e*cE)/(1 - e*cE))
for name, W in [("Gaussian", sp.exp(-u**2)), ("Lorentzian", 1/(1 + u**2)), ("W=u^2", u**2)]:
    integrand = W.subs(u, uc*xfac)
    ser = sp.series(integrand, e, 0, 3).removeO()
    Phi2 = sp.simplify(sp.integrate(sp.expand(ser), (E, 0, 2*sp.pi))/(2*sp.pi))
    dPhi = sp.diff(Phi2, e)
    small = sp.simplify(sp.limit(2*sp.pi*sp.sqrt(1 - e**2)/e*dPhi, e, 0))
    pred = sp.simplify(sp.pi*u*sp.diff(u*sp.diff(W, u), u)).subs(u, uc)
    print(f"  {name}: small-e Delta omega/eps = {sp.factor(small)};  pi u (u W')' = {sp.factor(pred)};  equal: {sp.simplify(small - pred) == 0}")

# Lorentzian at u_c = 1: W = 1/(1 + x^2), x^2 = (1+ec)/(1-ec)
cc = sp.symbols('cc')
WL1 = sp.simplify(1/(1 + (1 + e*cc)/(1 - e*cc)))
print("  Lorentzian at u_c=1: W = ", WL1, " -> average over E of (1 - e cosE)/2 = 1/2 for every e")

# W = u^2 exact in e
for ev in [0.3, 0.8]:
    num = mp.quad(lambda EE: (1 + ev*mp.cos(EE))/(1 - ev*mp.cos(EE)), [0, 2*mp.pi])/(2*mp.pi)
    print(f"  W=u^2: <(1+e cosE)/(1-e cosE)> at e={ev}: {num} vs 2/sqrt(1-e^2)-1 = {2/mp.sqrt(1-ev**2)-1}")
PhiU2 = uc**2*(2/sp.sqrt(1 - e**2) - 1)  # uses <1/(1-e cosE)> = 1/sqrt(1-e^2) (checked numerically below)
domU2 = sp.simplify(2*sp.pi*sp.sqrt(1 - e**2)/e*sp.diff(PhiU2, e))
print("  W=u^2 exact-in-e advance/eps =", domU2, " [claim 4 pi u_c^2/(1-e^2)]")
import mpmath as mp
for ev in [0.1, 0.5, 0.9]:
    val = mp.quad(lambda EE: 1/(1 - ev*mp.cos(EE)), [0, 2*mp.pi])/(2*mp.pi)
    print(f"    <1/(1 - e cosE)> at e={ev}: {val}  vs 1/sqrt(1-e^2) = {1/mp.sqrt(1-ev**2)}")

print()
print("=== GR anchor (textbook 6 pi GM/(c^2 a (1-e^2)) per orbit, from the 1PN test-particle Hamiltonian) ===")
# H1 = -p^4/(8c^2) - (3/2)(GM/r) p^2/c^2 + (GM)^2/(2 r^2 c^2); p^2 = GM(2/r - 1/a)
# orbit averages over mean anomaly via E: <f> = (1/2pi) int f (1 - e cosE) dE
rr = a*(1 - e*cE)
p2 = GM*(2/rr - 1/a)
def avg(f):
    return sp.simplify(sp.integrate(sp.simplify(f*(1 - e*cE)), (E, 0, 2*sp.pi))/(2*sp.pi))
# sympy struggles with these integrals for symbolic e; use the standard closed forms verified numerically
inv_r = 1/a
inv_r2 = 1/(a**2*sp.sqrt(1 - e**2))
for ev in [0.2, 0.7]:
    n1 = mp.quad(lambda EE: (1/(1 - ev*mp.cos(EE))**2)*(1 - ev*mp.cos(EE)), [0, 2*mp.pi])/(2*mp.pi)
    print(f"  check <a^2/r^2> at e={ev}: {n1} vs 1/sqrt(1-e^2) = {1/mp.sqrt(1-ev**2)}")
avg_p4 = GM**2*(4*inv_r2 - 4*inv_r/a + 1/a**2)
avg_p2_over_r = GM*(2*inv_r2 - inv_r/a)
H1avg = (-avg_p4/(8*c**2) - sp.Rational(3, 2)*GM*avg_p2_over_r/c**2 + GM**2*inv_r2/(2*c**2))
H1D = H1avg.subs({a: Lg**2/GM}).subs(e, sp.sqrt(1 - Gd**2/Lg**2))
domGR = sp.simplify(sp.diff(H1D, Gd)*T)
domGR_e = sp.simplify(domGR.subs(Gd, Lg*sp.sqrt(1 - e**2)).subs(Lg, sp.sqrt(GM*a)))
print("  averaged-GR advance per orbit =", domGR_e)
print("  equals 6 pi GM/(c^2 a (1-e^2)):", sp.simplify(domGR_e - 6*sp.pi*GM/(c**2*a*(1 - e**2))) == 0)
# separate contributions
for nm, term in [("p^4 term", -avg_p4/(8*c**2)), ("p^2/r term", -sp.Rational(3, 2)*GM*avg_p2_over_r/c**2), ("1/r^2 term", GM**2*inv_r2/(2*c**2))]:
    tD = term.subs({a: Lg**2/GM}).subs(e, sp.sqrt(1 - Gd**2/Lg**2))
    print(f"    {nm}: {sp.simplify(sp.simplify(sp.diff(tD, Gd)*T).subs(Gd, Lg*sp.sqrt(1-e**2)).subs(Lg, sp.sqrt(GM*a)))}")

print()
print("=== O9: u << 1 regime, ratio to GR ===")
# W ~ 1 - u^2: velocity part of L is -eps (GM/r) v^2/v*^2; by the W=u^2 result with eps -> -eps:
adv = -4*sp.pi*eps*(GM/(a*vs**2))/(1 - e**2)
grv = 6*sp.pi*GM/(c**2*a*(1 - e**2))
print("  ratio =", sp.simplify(adv/grv), " [claim -(2/3) eps (c/v*)^2]")
print("  both shapes have W = 1 - u^2 + O(u^4):",
      sp.series(sp.exp(-u**2), u, 0, 4), "|", sp.series(1/(1 + u**2), u, 0, 4))
