# Flag 27 audit, part A: exact algebra, independent of review/wiki-build-checks/v_sign_check.py.
# Sources: #1 s3 (V = V0[1 + cos(tau/f)]), #1 s6 (dictionary, minisuperspace), #1 s7 item 3,
# #9 s8 + row 5, #11 s10 + row 5.
import sympy as sp

x = sp.symbols('x', real=True)            # x = tau/f
P = sp.Interval.Ropen(0, 2*sp.pi)         # one period

print("== 1. Sign of the potential as written, V/V0 = 1 + cos x ==")
neg_doc = sp.solveset(1 + sp.cos(x) < 0, x, P)
zero_doc = sp.solveset(sp.Eq(1 + sp.cos(x), 0), x, P)
print("  set where 1 + cos x < 0 in one period:", neg_doc)
print("  set where 1 + cos x = 0 in one period:", zero_doc, "(isolated point: the minimum)")
print("  minimum of 1 + cos x over the period:", sp.minimum(1 + sp.cos(x), x, sp.Interval(0, 2*sp.pi)))
print("  identity 1 + cos x = 2 cos^2(x/2) >= 0:", sp.simplify(1 + sp.cos(x) - 2*sp.cos(x/2)**2) == 0)

print("== 2. '#1 s7: a cosine potential is negative over half its range' ==")
neg_cos = sp.solveset(sp.cos(x) < 0, x, P)
print("  set where cos x < 0 in one period:", neg_cos, " fraction of period:", sp.simplify(neg_cos.measure/(2*sp.pi)))
print("  fraction where 1 + cos x < 0:", neg_doc.measure/(2*sp.pi) if neg_doc != sp.S.EmptySet else 0)

print("== 3. Can either sign of V0 give a positive hilltop AND a negative region? ==")
for label, V0 in (("V0 > 0", sp.Symbol('V0', positive=True)), ("V0 < 0", -sp.Symbol('W', positive=True))):
    V = V0*(1 + sp.cos(x))
    Vmax = sp.maximum(V, x, sp.Interval(0, 2*sp.pi))
    Vmin = sp.minimum(V, x, sp.Interval(0, 2*sp.pi))
    print(f"  {label}: hilltop value max V = {Vmax}, min V = {Vmin};"
          f" (max>0 and min<0) = {sp.And(sp.Gt(Vmax, 0), sp.Lt(Vmin, 0))}")
print("  -> V0 > 0: positive hilltop (dark energy today) but never negative;"
      " V0 < 0: hilltop at V = 0 (no dark energy today).")

print("== 4. Flat FRW: what a turnaround (H = 0) requires ==")
rho_m, rho_r, td, M, Mt, a = sp.symbols('rho_m rho_r taudot M_P Mtilde a', positive=True)
Vs = sp.Symbol('V', real=True)
rho = rho_m + rho_r + td**2/2 + Vs
for label, pref in (("GR: 3 M_P^2 H^2 = rho", 3*M**2),
                    ("#1 s6 minisuperspace: 3 H^2 (M_P^2 + Mt^2 a^-6) = rho", 3*(M**2 + Mt**2*a**-6))):
    H2 = rho/pref
    Vturn = sp.solve(sp.Eq(H2, 0), Vs)[0]
    print(f"  {label}: H = 0  <=>  V = {Vturn};  V < 0 forced: {sp.ask(sp.Q.negative(Vturn))}")
print("  (rho_m > 0 makes the turnaround value of V strictly negative; with V >= 0, H^2 > 0 for all time)")

print("== 5. #1 s6 dictionary: can dual-frame content supply late-time negative energy? ==")
rt, wt = sp.symbols('rho_tilde w_tilde', real=True)
at = 1/a                                         # constraint a * a_tilde = 1
rho_eff = rt*at**3/a**3                          # rho_eff = E / a^3 with E = rho_tilde * a_tilde^3
print("  rho_eff =", sp.simplify(rho_eff), "-> sign(rho_eff) = sign(rho_tilde)")
scal = sp.simplify((at**(-3*(1 + wt)))*at**3/a**3)
print("  rho_eff scaling for dual w_tilde:", scal, "= a^(-3(1 - w_tilde)):",
      sp.simplify(scal - a**(-3*(1 - wt))) == 0)
for name, w in (("dual dust", 0), ("dual curvature (negative if dual space closed)", sp.Rational(-1, 3)),
                ("dual Lambda (negative if dual Lambda < 0)", -1), ("dual stiff (kinetic, >= 0)", 1)):
    p = sp.simplify(-3*(1 - w))
    print(f"  {name:48s} w_tilde = {str(w):5s} -> rho_eff ~ a^{p};  ratio to our dust a^-3: a^{p + 3}")
print("  -> the only components that can be negative decay faster than dust (a^-1, a^-3 relative):"
      " none can stop a late-time expansion.")

print("== 6. 'Turnaround = conjugate bounce by constraint identity' (kinematics only) ==")
t = sp.symbols('t', real=True)
af = sp.Function('a', positive=True)(t)
atf = 1/af
d1 = sp.diff(atf, t)
d2 = sp.diff(atf, t, 2)
ad, add = sp.symbols('adot addot', real=True)
d2s = d2.subs(sp.Derivative(af, (t, 2)), add).subs(sp.Derivative(af, t), ad)
print("  d(a_tilde)/dt =", sp.simplify(d1))
print("  d2(a_tilde)/dt2 =", sp.simplify(d2s), "; at adot = 0:", sp.simplify(d2s.subs(ad, 0)),
      "(> 0 when addot < 0: our maximum is their minimum)")
print("  -> holds IF a turnaround (adot = 0, addot < 0) exists; it does not supply one.")

print("== 7. Side consequence of a fix that lets rho_tau < 0: what 'w >= -1 always' (#1 s7 item 1) becomes ==")
K = sp.Symbol('K', positive=True)        # kinetic energy taudot^2/2 > 0
Vn = sp.Symbol('Vn', negative=True)
w = (K - Vn) / (K + Vn)
print("  rho + p = 2K =", sp.simplify((K + Vn) + (K - Vn)), "(>= 0 for any V: the NEC holds)")
# with rho = K + V < 0:  w < -1  <=>  (K - V) > -(K + V)  (multiplying by rho < 0 flips)  <=>  K > 0
cond = sp.simplify((K - Vn) + (K + Vn))
print("  for rho_tau = K + V < 0: w < -1  <=>  (K - V) + (K + V) > 0  <=>", cond, "> 0  -> always, when taudot != 0")
print("  example K = 1, V = -3:", w.subs({K: 1, Vn: -3}), "; K = 1, V = -1.01:", sp.nsimplify(w.subs({K: 1, Vn: sp.Rational(-101, 100)})))
