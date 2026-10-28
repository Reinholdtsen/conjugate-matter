"""Verifier check of P10-P12, P14, P15 (mechanics of momentum-dependent interactions), written
without reference to the agent's scripts.  3D, two bodies, sympy.  Zero tests on transcendental
expressions are numeric at random points (iszero); polynomial ones are exact."""
import random
import sympy as sp
random.seed(11)


def iszero(expr, n=4, tol=1e-10):
    exprs = list(expr) if isinstance(expr, sp.MatrixBase) else [expr]
    exprs = [sp.sympify(e).doit() for e in exprs]
    syms = set().union(*[e.free_symbols for e in exprs])
    for _ in range(n):
        sub = {s: sp.Float(random.uniform(0.3, 1.7)) * (1 if s.is_positive else random.choice([-1, 1])) for s in syms}
        for e in exprs:
            if abs(complex(sp.N(e.subs(sub), 30))) > tol:
                return False
    return True


m1, m2, eps, vs, Gt, g, mu_w = sp.symbols('m1 m2 epsilon v_star Gtilde g mu_w', positive=True)
M = m1 + m2
x1 = sp.Matrix(sp.symbols('x1_1:4', real=True)); x2 = sp.Matrix(sp.symbols('x2_1:4', real=True))
p1 = sp.Matrix(sp.symbols('p1_1:4', real=True)); p2 = sp.Matrix(sp.symbols('p2_1:4', real=True))
v1 = sp.Matrix(sp.symbols('v1_1:4', real=True)); v2 = sp.Matrix(sp.symbols('v2_1:4', real=True))
u = sp.Matrix(sp.symbols('u1:4', real=True))
grad = lambda f, X: sp.Matrix([sp.diff(f, s) for s in X])
dot = lambda a, b: (a.T*b)[0]
boost_p = {**{p1[i]: p1[i] + m1*u[i] for i in range(3)}, **{p2[i]: p2[i] + m2*u[i] for i in range(3)}}

print("=== Model (a): H = sum p^2/2m + eps U(arg), U depends on momenta only ===", flush=True)
Uc = lambda A: (A[0]**3/3 + sp.sin(A[1]) + sp.exp(-A[2]**2) + A[0]*A[1]*A[2])   # concrete, generic U
args = {'p1 - p2': p1 - p2, 'k = (m2 p1 - m1 p2)/M': (m2*p1 - m1*p2)/M, 'p1/m1 - p2/m2': p1/m1 - p2/m2}
for name, A in args.items():
    H = dot(p1, p1)/(2*m1) + dot(p2, p2)/(2*m2) + eps*Uc(A)
    pdot1 = -grad(H, x1)
    shift = (A.subs(boost_p, simultaneous=True) - A).applyfunc(sp.simplify)
    cm = m1*grad(H, p1) + m2*grad(H, p2) - (p1 + p2)
    print(f"arg {name:22s}: pdot1 = {list(pdot1)}; boost shift = {list(shift)}; CM drift d(m1x1+m2x2)/dt - P zero: {iszero(cm)}", flush=True)
# the CM drift for p1 - p2 equals (m1 - m2) grad U
A = p1 - p2
H = dot(p1, p1)/(2*m1) + dot(p2, p2)/(2*m2) + eps*Uc(A)
s = sp.Matrix(sp.symbols('s1:4', real=True))
gU = grad(Uc(s), s).subs({s[i]: A[i] for i in range(3)}, simultaneous=True)
print("  p1 - p2: CM drift - eps (m1 - m2) grad U == 0:", iszero(m1*grad(H, p1) + m2*grad(H, p2) - (p1 + p2) - eps*(m1 - m2)*gU), flush=True)
# first-order Lagrangian for arg p1 - p2: p = m v - eps m dU/dp|_{p = m v}
at_mv = {**{p1[i]: m1*v1[i] for i in range(3)}, **{p2[i]: m2*v2[i] for i in range(3)}}
P1 = m1*v1 - eps*m1*grad(Uc(A), p1).subs(at_mv, simultaneous=True)
P2 = m2*v2 - eps*m2*grad(Uc(A), p2).subs(at_mv, simultaneous=True)
rep = {**{p1[i]: P1[i] for i in range(3)}, **{p2[i]: P2[i] for i in range(3)}}
vres = grad(H, p1).subs(rep, simultaneous=True) - v1
L = dot(P1, v1) + dot(P2, v2) - H.subs(rep, simultaneous=True)
Lclaim = m1*dot(v1, v1)/2 + m2*dot(v2, v2)/2 - eps*Uc(m1*v1 - m2*v2)
d_eps1 = lambda f: sp.diff(f, eps).subs(eps, 0)
print("Legendre: velocity residual O(eps) zero:", iszero(vres.applyfunc(d_eps1)) and iszero(vres.subs(eps, 0)),
      "; L - [sum m v^2/2 - eps U(m1 v1 - m2 v2)] zero at O(eps^0, eps^1):",
      iszero((L - Lclaim).subs(eps, 0)) and iszero(d_eps1(L - Lclaim)), flush=True)
X, P, m = sp.symbols('X P m', real=True)
V = sp.Function('V')
Hb = X**2/(2*m) + V(P)
print("Born image H = x^2/2m + V(p): xdot =", sp.diff(Hb, P), "; pdot =", -sp.diff(Hb, X), flush=True)

print()
print("=== Model (b): L = sum m v^2/2 + Gt m1 m2 W(|v1 - v2|/v*)/r, Gaussian W(w) = exp(-w^2) ===", flush=True)
rvec = x1 - x2; r = sp.sqrt(dot(rvec, rvec))
w = sp.sqrt(dot(v1 - v2, v1 - v2))/vs
W = lambda q: sp.exp(-q**2)
dW = lambda q: -2*q*sp.exp(-q**2)
Lb = m1*dot(v1, v1)/2 + m2*dot(v2, v2)/2 + Gt*m1*m2*W(w)/r
Efun = dot(v1, grad(Lb, v1)) + dot(v2, grad(Lb, v2)) - Lb
Eclaim = m1*dot(v1, v1)/2 + m2*dot(v2, v2)/2 - Gt*m1*m2/r*(W(w) - w*dW(w))
print("energy function - [sum m v^2/2 - Gt m1 m2 (W - w W')/r] zero:", iszero(Efun - Eclaim), flush=True)
boost_v = {**{v1[i]: v1[i] + u[i] for i in range(3)}, **{v2[i]: v2[i] + u[i] for i in range(3)}}
print("L(boosted) - L - [u.(m1 v1 + m2 v2) + M u^2/2] zero:",
      iszero(Lb.subs(boost_v, simultaneous=True) - Lb - (dot(u, m1*v1 + m2*v2) + M*dot(u, u)/2)), flush=True)
vr = sp.Matrix(sp.symbols('vr1:4', real=True)); rr = sp.symbols('r', positive=True)
mu = m1*m2/M
Lrel = mu*dot(vr, vr)/2 + Gt*m1*m2*sp.exp(-dot(vr, vr)/vs**2)/rr
Hess = sp.Matrix(3, 3, lambda i, j: sp.diff(Lrel, vr[i], vr[j])).subs({q: 0 for q in vr})
h00 = sp.simplify(Hess[0, 0])
print("Lagrangian Hessian at v_rel = 0:", sp.factor(h00), "* I ; off-diagonal zero:", Hess[0, 1] == 0,
      "; zero at r =", sp.solve(h00, rr), flush=True)
pr = sp.Matrix(sp.symbols('pr1:4', real=True))
Hrel = dot(pr, pr)/(2*mu) - Gt*m1*m2*sp.exp(-dot(pr, pr)/(mu*vs)**2)/rr
iH = sp.Matrix(3, 3, lambda i, j: sp.diff(Hrel, pr[i], pr[j])).subs({q: 0 for q in pr})
print("Hamiltonian inverse inertia at p = 0 equals (1/mu)(1 + 2 Gt M/(r v*^2)):",
      sp.simplify(iH[0, 0] - (1 + 2*Gt*M/(rr*vs**2))/mu) == 0, flush=True)
for name, A in [('|p1/m1 - p2/m2|/v*', sp.sqrt(dot(p1/m1 - p2/m2, p1/m1 - p2/m2))/vs),
                ('|p1 - p2|/(m1 v*)', sp.sqrt(dot(p1 - p2, p1 - p2))/(m1*vs))]:
    Hb1 = dot(p1, p1)/(2*m1) + dot(p2, p2)/(2*m2) - Gt*m1*m2*sp.exp(-A**2)/r
    pd1 = -grad(Hb1, x1)
    newton_gate = -Gt*m1*m2*sp.exp(-A**2)*rvec/r**3
    cmv = m1*grad(Hb1, p1) + m2*grad(Hb1, p2) - (p1 + p2)
    print(f"gate arg {name:20s}: pdot1 = Newton x gate: {iszero(pd1 - newton_gate)}; CM drift zero: {iszero(cmv)}", flush=True)
Gs = sp.symbols('G_s', positive=True)
Lb2 = m1*dot(v1, v1)/2 + m2*dot(v2, v2)/2 + Gs*m1*m2*sp.exp(-dot(v1 - v2, v1 - v2)/vs**2)/r
pp1 = grad(Lb2, v1); pp2 = grad(Lb2, v2)
Hfrom = dot(pp1, v1) + dot(pp2, v2) - Lb2
Hclaim = dot(pp1, pp1)/(2*m1) + dot(pp2, pp2)/(2*m2) - Gs*m1*m2*sp.exp(-dot(pp1/m1 - pp2/m2, pp1/m1 - pp2/m2)/vs**2)/r
dG = lambda f: sp.diff(f, Gs).subs(Gs, 0)
print("model b: H(v(p)) - [p^2/2m - Gt m1 m2 W(|p1/m1-p2/m2|/v*)/r] vanishes at O(Gt^0) and O(Gt^1):",
      iszero((Hfrom - Hclaim).subs(Gs, 0)) and iszero(dG(Hfrom - Hclaim)),
      "; nonzero at O(Gt^2):", not iszero(sp.diff(Hfrom - Hclaim, Gs, 2).subs(Gs, 0)), flush=True)

print()
print("=== Model (c): U = -g delta_e(x1 - x2) G((p1 - p2)/mu) ===", flush=True)
e_ = sp.symbols('e_', positive=True)
dl = sp.exp(-dot(rvec, rvec)/(2*e_**2))/(2*sp.pi*e_**2)**sp.Rational(3, 2)
Gg = sp.exp(-dot(p1 - p2, p1 - p2)/(2*mu_w**2))
Hc = dot(p1, p1)/(2*m1) + dot(p2, p2)/(2*m2) - g*dl*Gg
print("pdot1 = g G grad_x1 delta:", iszero(-grad(Hc, x1) - g*Gg*grad(dl, x1)),
      "; xdot1 = p1/m1 - g delta dG/dp1:", iszero(grad(Hc, p1) - (p1/m1 - g*dl*grad(Gg, p1))), flush=True)
rs = sp.symbols('rs', positive=True)
d_r = sp.diff(sp.exp(-rs**2/(2*e_**2)), rs)
rmax = sp.solve(sp.diff(d_r, rs), rs)
ratio = sp.simplify(d_r.subs(rs, 10*e_)/d_r.subs(rs, rmax[0]))
print("Gaussian smoothing: |d delta/dr| max at r =", rmax, "; value at 10 eps / max =", ratio, "=", float(ratio), flush=True)
print("p1 - p2 boost shift:", list((p1 - p2).subs(boost_p, simultaneous=True) - (p1 - p2)), "(zero only for m1 = m2)", flush=True)
