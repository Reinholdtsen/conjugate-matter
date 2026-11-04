"""Verifier check of exponents read from Henry-Couannier's Dark Gravity review (arXiv:gr-qc/0610079, sec. 13).

The review's equation (24): for a << 1 in a cold era, (1/a)'' = c in conformal time t < 0 (c > 0 needed for
a > 0; the review writes the constant as -n pi G rho0 / 6). Its equation (20) source term on the dark side is
(1/A^2)(rho~ - 3 p~) with A = a^2, and its cold-era law rho~ ~ 1/A~^(3/2) with A~ = 1/A.

Checks:
 1. conjugate scale factor at~ = 1/a solves at~'' = c: at~ = (c/2) t^2, contracting as t -> 0-.
 2. the conjugate side's own cosmic time T, dT = at~ dt, gives at~ ~ |T|^(2/3): a contracting dust (EdS) law.
 3. our cosmic time t', dt' = a dt with a = 2/(c t^2), gives a ~ t'^2 (accelerating).
 4. the dark-side source term (1/A^2) rho~ scales as a^(-1) = at~: it shrinks as the dark side contracts.
 5. the program's route for contrast (wiki 'duality dictionary'): stiff rho~ ~ at~^-6, E = rho~ at~^3,
    rho_eff = E / a^3 with at~ = 1/a: constant.
"""
import sympy as sp

t = sp.symbols("t", negative=True)
c, T0 = sp.symbols("c T0", positive=True)

# 1
at = c * t**2 / 2
assert sp.simplify(sp.diff(at, t, 2) - c) == 0
a = 1 / at
print("1. at~ =", at, "; at~'' =", sp.diff(at, t, 2), "; d(at~)/dt at t<0:", sp.diff(at, t), "(< 0: contracting)")

# 2  conjugate cosmic time T(t) = integral of at~ dt, chosen to vanish at t = 0
T = sp.integrate(at, t)  # c t^3 / 6, negative for t < 0
print("2. T(t) =", T)
S = sp.symbols("S", positive=True)  # S = |T| = -T, the conjugate cosmic time left before the crunch
t_of_S = -(6 * S / c) ** sp.Rational(1, 3)  # real root of c t^3 / 6 = -S with t < 0
assert sp.simplify(T.subs(t, t_of_S) + S) == 0
expr = sp.simplify(at.subs(t, t_of_S))
print("   at~(|T|) =", expr)
exp_T = sp.simplify(sp.diff(sp.log(expr), S) * S)
print("   d ln at~ / d ln|T| =", exp_T, "(2/3 = dust law; at~ -> 0 as |T| -> 0: a crunch)")

# 3  our cosmic time t'(t) = integral of a dt
tp = sp.integrate(a, t)  # -2/(c t), positive for t < 0
print("3. t'(t) =", tp)
tps = sp.symbols("tp", positive=True)
t_of_tp = sp.solve(sp.Eq(tp, tps), t)[0]
a_tp = sp.simplify(a.subs(t, t_of_tp))
print("   a(t') =", a_tp, "; d ln a / d ln t' =", sp.simplify(sp.diff(sp.log(a_tp), tps) * tps))
print("   a''(t') sign:", sp.sign(sp.diff(a_tp, tps, 2)))

# 4  dark-side source term (1/A^2) rho~ with rho~ ~ A~^(-3/2), A~ = 1/A, A = a^2
av = sp.symbols("a", positive=True)
A = av**2
At = 1 / A
src = (1 / A**2) * At**sp.Rational(-3, 2)
print("4. dark-side source ~", sp.simplify(src), "= at~^1 with at~ = 1/a: falls as the dark side contracts")

# 5  the program's route for contrast
rho_t = (1 / av) ** -6  # stiff in the dual frame, at~ = 1/a
E = rho_t * (1 / av) ** 3
print("5. program: stiff rho~ =", sp.simplify(rho_t), "; E =", sp.simplify(E), "; rho_eff = E/a^3 =", sp.simplify(E / av**3))

# 6  the same image with a shared cosmic time: invert a collapsing dust universe at~ ~ (tc - t)^(2/3).
#    A power law a ~ (tc - t)^q or t^q has w with q = 2 / (3 (1 + w)).
w = sp.symbols("w")
q_shared_cosmic = -sp.Rational(2, 3)  # a = 1/at~
w_shared_cosmic = sp.solve(sp.Eq(sp.Rational(2, 3) / (1 + w), q_shared_cosmic), w)[0]
q_dg = 2  # a ~ t'^2 from step 3 (shared conformal time)
w_dg = sp.solve(sp.Eq(sp.Rational(2, 3) / (1 + w), q_dg), w)[0]
print("6. inverse of a collapsing dust universe, shared cosmic time: a ~ (tc-t)^-2/3, w =", w_shared_cosmic)
print("   (the program's heuristic dictionary for dual dust: w_eff = -2 - 0 =", -2 - 0, ")")
print("   Dark Gravity, shared conformal time: a ~ t'^2, w_eff =", w_dg)
# and the heuristic's self-consistency: rho_eff = rho~ (densities identified), H~ = -H, so both Friedmann
# equations coincide; check rho~ ~ at~^-3 equals a^3 and H^2 ~ rho_eff gives q = -2/3
tc, tt = sp.symbols("t_c tt", positive=True)
a_h = (tc - tt) ** q_shared_cosmic
H_h = sp.diff(a_h, tt) / a_h
ratio = sp.simplify(H_h**2 / a_h**3)  # rho_eff ~ a^3 for dual dust under the heuristic
print("   heuristic check: H^2 / a^3 =", ratio, "(constant up to the factor: H^2 proportional to rho_eff ~ a^3)")

# 7  the program's corrected dictionary vs Gasperini-Veneziano 2003 eq. (2.32) (Veneziano 1991), d = 3:
#    GV: a -> 1/a with rhobar = rho a^3 and pbar = p a^3 -> -pbar. Program: E = rho~ at~^3 enters as E / a^3.
rt, pt, at_, a_ = sp.symbols("rho_t p_t at a", positive=True)
rho_dual_GV = rt * at_**3 / a_**3          # rhobar preserved: rho a^3 = rho~ at~^3
p_dual_GV = -pt * at_**3 / a_**3           # pbar reversed
rho_eff_prog = (rt * at_**3) / a_**3       # E / a^3
print("7. GV rho' - program rho_eff =", sp.simplify(rho_dual_GV - rho_eff_prog),
      "; GV w' =", sp.simplify((p_dual_GV / rho_dual_GV).subs(pt, sp.Symbol('wt') * rt)), "(= -w~)")

# 8  Dark Gravity hot regime (review eq. 22: (1/a)'' = 0 for a << 1, t < 0) and the general shared-conformal-time rule
k = sp.symbols("k", positive=True)
at_hot = -k * t                           # at~ linear in conformal time, positive for t < 0
a_hot = 1 / at_hot
H_hot = sp.simplify(sp.diff(a_hot, t) / a_hot**2)   # H = (1/a) da/dt' with dt' = a dt
print("8. hot regime: our H = (da/dt)/a^2 =", H_hot, "(constant: de Sitter, a ~ exp(k t'))")
T_hot = sp.integrate(at_hot, t)           # conjugate cosmic time: -k t^2 / 2 (negative, -> 0 at t -> 0-)
S2 = sp.symbols("S2", positive=True)
at_of_S = sp.simplify(at_hot.subs(t, -sp.sqrt(2 * S2 / k)))
print("   conjugate: T(t) =", T_hot, "; at~(|T|) =", at_of_S, "; exponent", sp.simplify(sp.diff(sp.log(at_of_S), S2) * S2),
      "(1/2: radiation-like contraction to a crunch)")
wt, eta = sp.symbols("wt eta")
q_t = 2 / (1 + 3 * wt)                    # at~ ~ eta^q_t in conformal time for a w~ fluid
w_ours = sp.solve(sp.Eq(2 / (1 + 3 * w), -q_t), w)[0]   # a = 1/at~ ~ eta^(-q_t)
print("   shared conformal time, a = 1/at~: w =", sp.simplify(w_ours), "; w + w~ =", sp.simplify(w_ours + wt),
      "; w~ = 1/3 ->", w_ours.subs(wt, sp.Rational(1, 3)), "; w~ = 0 ->", w_ours.subs(wt, 0),
      "; w~ = 1 ->", w_ours.subs(wt, 1))
