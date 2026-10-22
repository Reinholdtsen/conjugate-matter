#!/usr/bin/env python3
"""
Audit of flag 6 (review/wiki-build-flags.md): is the wedge sector's zero vacuum
energy "by symmetry rather than tuning" (#1 v0.6, #10), or does it need a condition
on the beta_n that the palindrome does not supply?

Setting (#8 sec. 1-3, #11 sec. 7.3): Hassan-Rosen potential
    P(g, f) = sqrt(det g) * sum_n beta_n e_n( sqrt(g^-1 f) ),  d = 4,
aligned point g = f (X = 1), palindrome beta_n = beta_{4-n}, equal Planck masses.

Anchors independent of the paper:
  A. textbook identity: Einstein tensor G_{mu nu} is invariant under g -> c^2 g (sympy);
  B. exchange identity sqrt(det f) e_n(sqrt(f^-1 g)) = sqrt(det g) e_{4-n}(sqrt(g^-1 f));
  C. field-equation coefficients of P at g = f = 1 by finite differences on random
     4x4 symmetric perturbations (no use of #8's formulas);
then exact algebra (sympy) for the counts and the proportional-background condition.
"""
import itertools
from math import comb
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261021)
d = 4

def esym(vals, n):
    if n == 0:
        return 1.0
    return sum(np.prod(c) for c in itertools.combinations(vals, n))

def sqrt_eigs(g, f):
    # eigenvalues of sqrt(g^-1 f): g^-1 f is similar to g^-1/2 f g^-1/2 (sym. pos. def.)
    w, U = np.linalg.eigh(g)
    gmh = U @ np.diag(w ** -0.5) @ U.T
    lam = np.linalg.eigvalsh(gmh @ f @ gmh)
    return np.sqrt(lam)

def P(g, f, beta):
    s = sqrt_eigs(g, f)
    return np.sqrt(np.linalg.det(g)) * sum(beta[n] * esym(s, n) for n in range(5))

def randsym():
    m = rng.standard_normal((d, d))
    return (m + m.T) / 2

def V1_T(beta):
    V1 = sum(beta[n] * comb(4, n) for n in range(5))
    T = sum(beta[n] * comb(3, n - 1) for n in range(1, 5))
    return V1, T

print("== A. Textbook anchor: G_{mu nu}(c^2 g) = G_{mu nu}(g) (Bianchi-I metric, sympy)")
t, x, y, z, c = sp.symbols('t x y z c', positive=True)
N, a, b, e = [sp.Function(s)(t) for s in ('N', 'a', 'b', 'e')]
coords = [t, x, y, z]

def einstein_lower(gm):
    gi = gm.inv()
    n = 4
    Gam = [[[sum(gi[i, l] * (sp.diff(gm[l, j], coords[k]) + sp.diff(gm[l, k], coords[j])
                             - sp.diff(gm[j, k], coords[l])) for l in range(n)) / 2
             for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n)
    for j in range(n):
        for k in range(n):
            Ric[j, k] = sp.simplify(sum(sp.diff(Gam[i][j][k], coords[i]) for i in range(n))
                                    - sum(sp.diff(Gam[i][j][i], coords[k]) for i in range(n))
                                    + sum(Gam[i][i][l] * Gam[l][j][k] for i in range(n) for l in range(n))
                                    - sum(Gam[i][k][l] * Gam[l][j][i] for i in range(n) for l in range(n)))
    R = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return sp.simplify(Ric - gm * R / 2)

gmet = sp.diag(-N**2, a**2, b**2, e**2)
diffG = sp.simplify(einstein_lower(c**2 * gmet) - einstein_lower(gmet))
print("   G(c^2 g) - G(g) is the zero matrix:", diffG == sp.zeros(4))

print("\n== B. Exchange anchor: sqrt(det f) e_n(sqrt(f^-1 g)) = sqrt(det g) e_{4-n}(sqrt(g^-1 f))")
def posdef():
    m = rng.standard_normal((d, d))
    return m @ m.T + d * np.eye(d)
gR, fR = posdef(), posdef()
errs = []
for n in range(5):
    lhs = np.sqrt(np.linalg.det(fR)) * esym(sqrt_eigs(fR, gR), n)
    rhs = np.sqrt(np.linalg.det(gR)) * esym(sqrt_eigs(gR, fR), 4 - n)
    errs.append(abs(lhs - rhs) / abs(rhs))
print("   max relative error over n = 0..4:", f"{max(errs):.2e}",
      "-> exchange g<->f acts as beta_n -> beta_{4-n}; invariance = palindrome")

print("\n== C. Field-equation coefficients of P at g = f = 1 (finite differences, random beta, dg, df)")
I4 = np.eye(d)
eps = 1e-5
worst = 0.0
for trial in range(5):
    beta = rng.standard_normal(5)
    dg, df = randsym(), randsym()
    num = (P(I4 + eps * dg, I4 + eps * df, beta) - P(I4 - eps * dg, I4 - eps * df, beta)) / (2 * eps)
    V1, T = V1_T(beta)
    pred = 0.5 * (V1 - T) * np.trace(dg) + 0.5 * T * np.trace(df)
    worst = max(worst, abs(num - pred) / max(1.0, abs(pred)))
print(f"   dP = 1/2 (V(1) - T) Tr dg + 1/2 T Tr df ; worst relative mismatch over 5 trials: {worst:.2e}")
print("   -> g-equation's potential term vanishes iff V(1) = T (#8 sec. 2's flatness condition);")
print("      f-equation's potential term vanishes iff T = 0.")

print("\n   Z2 decomposition at the aligned point (palindromic beta with T != 0):")
bp = np.array([1.0, 0.7, -0.4, 0.7, 1.0])          # beta_0=beta_4, beta_1=beta_3
V1p, Tp = V1_T(bp)
dl = randsym()
even = (P(I4 + eps * dl, I4 + eps * dl, bp) - P(I4 - eps * dl, I4 - eps * dl, bp)) / (2 * eps)
odd = (P(I4 + eps * dl, I4 - eps * dl, bp) - P(I4 - eps * dl, I4 + eps * dl, bp)) / (2 * eps)
print(f"   beta = {bp.tolist()}: V(1) = {V1p:.4f}, T = {Tp:.4f}, V(1) - 2T = {V1p - 2*Tp:.2e}")
pe, po = 0.5 * V1p * np.trace(dl), 0.5 * (V1p - 2 * Tp) * np.trace(dl)
print(f"   even mode (dg = df):  dP/eps = {even:.6f}  vs  1/2 V(1) Tr d = {pe:.6f}  (rel. diff {abs(even-pe)/abs(pe):.1e})")
print(f"   odd  mode (dg = -df): dP/eps = {odd:.2e}  vs  1/2 (V(1) - 2T) Tr d = {po:.2e}")
print("   -> the palindrome kills the odd (massive-mode) tadpole; the even-mode term V(1) = 2T is left free.")

print("\n== D. Exact algebra (sympy)")
b0, b1, b2, b3, b4 = B = sp.symbols('beta0:5')
V1s = sum(B[n] * comb(4, n) for n in range(5))
Ts = sum(B[n] * comb(3, n - 1) for n in range(1, 5))
lam_g1, lam_f1 = sp.expand(V1s - Ts), sp.expand(Ts)
print("   generic: lambda_g(1) =", lam_g1, "; lambda_f(1) =", lam_f1)
Mgen = sp.Matrix([[sp.diff(q, bb) for bb in B] for q in (lam_g1, lam_f1)])
print("   generic flat aligned vacuum: rank of conditions =", Mgen.rank(), "-> free betas:", 5 - Mgen.rank())
pal = {b4: b0, b3: b1}
print("   palindrome: V(1) - 2T =", sp.expand((V1s - 2 * Ts).subs(pal)),
      "; lambda_g(1) =", sp.expand(lam_g1.subs(pal)), "; lambda_f(1) =", sp.expand(lam_f1.subs(pal)))
Mpal = sp.Matrix([[sp.diff(q.subs(pal), bb) for bb in (b0, b1, b2)] for q in (lam_g1, lam_f1)])
print("   palindromic flat aligned vacuum: rank of conditions on (beta0,beta1,beta2) =", Mpal.rank(),
      "-> free betas:", 3 - Mpal.rank(), "(total conditions on the 5 betas:", 2 + Mpal.rank(), ")")
print("   T = 0 under the palindrome  <=>  beta0 =", sp.solve(sp.Eq(Ts.subs(pal), 0), b0)[0])
Tfun = sp.lambdify((b0, b1, b2), Ts.subs(pal))
print("   T is not identically zero on the palindromic family: T(1,0,0) =", Tfun(1, 0, 0),
      "; T(0,1,0) =", Tfun(0, 1, 0), "; T(0,0,1) =", Tfun(0, 0, 1))

print("\n== E. Proportional backgrounds f = c^2 g (scaling of P + anchor A), alpha = M_f/M_g")
A_, Bs, cc, al = sp.symbols('A B c alpha', positive=True)
p = A_**2 * sum(B[n] * comb(4, n) * (Bs / A_)**sp.Rational(n, 2) for n in range(5))
# delta g = eps g  =>  dP = (dp/dA) A eps = 2 eps sqrt(g) lambda_g ; sqrt(g) = A^2
lam_g = sp.simplify((A_ * sp.diff(p, A_) / (2 * A_**2)).subs({A_: 1, Bs: cc**2}))
lam_f = sp.simplify((Bs * sp.diff(p, Bs) / (2 * Bs**2)).subs({A_: 1, Bs: cc**2}))
print("   lambda_g(c) =", sp.expand(lam_g))
print("   lambda_f(c) =", sp.expand(lam_f))
# g-eq: G(g) + Lambda_g g = 0, Lambda_g = lambda_g/M_g^2 ; f-eq: G(f) + Lambda_f f = 0, Lambda_f = lambda_f/M_f^2
# G(f) = G(g) (anchor A) and f = c^2 g  =>  Lambda_g = c^2 Lambda_f  <=>  alpha^2 lambda_g - c^2 lambda_f = 0
cond = sp.expand(sp.simplify(cc * (al**2 * lam_g - cc**2 * lam_f)))
print("   proportional-background condition (times c):", sp.collect(cond, cc))
r1 = sp.expand(cond.subs({al: 1, cc: 1}))
print("   generic, alpha = 1, at c = 1:", r1, " (a condition: c = 1 is not automatic)")
print("   palindrome, alpha = 1, at c = 1:", sp.expand(r1.subs(pal)), " (c = 1 is always a solution)")
print("   palindrome, alpha = 1: Lambda of the aligned vacuum (units m^4/M^2) =",
      sp.expand(lam_g.subs(cc, 1).subs(pal)), "= T")
ex = {b0: 1, b1: 0, b2: 0, b3: 0, b4: 1}
print("   example palindromic beta = (1,0,0,0,1): condition at c=1 ->", cond.subs({al: 1, cc: 1}).subs(ex),
      "; Lambda_g(1) =", lam_g.subs(cc, 1).subs(ex), "; T =", Ts.subs(ex), "; V(1) =", V1s.subs(ex))
pm = {b0: 3 * b2, b1: 0, b3: 0, b4: 3 * b2}   # #11 sec. 7.4's PM point at alpha = 1
print("   #11 sec. 7.4 PM point at alpha = 1: condition ->", sp.simplify(cond.subs(al, 1).subs(pm)),
      "(any c); Lambda_g(c) =", sp.factor(lam_g.subs(pm)), "; T =", sp.expand(Ts.subs(pm)))

print("\n== F. Generic HR (no palindrome): is the second condition at c = 1 a tuning or a normalization?")
# f -> f/k^2 with beta_n -> beta_n k^n is the same theory (P depends on f only via sqrt(g^-1 f)).
lamg_num = sp.lambdify((cc, *B), lam_g)
lamf_num = sp.lambdify((cc, *B), lam_f)
for attempt in range(50):
    b14 = rng.standard_normal(4)                  # beta1..beta4, random
    roots = np.roots([b14[3], 3 * b14[2], 3 * b14[1], b14[0]])   # beta4 c^3 + 3beta3 c^2 + 3beta2 c + beta1
    pos = [r.real for r in roots if abs(r.imag) < 1e-12 and r.real > 0]
    if pos:
        break
k = pos[0]
b0v = -(3 * b14[0] * k + 3 * b14[1] * k**2 + b14[2] * k**3)   # ONE condition: lambda_g(k) = 0
bet = [b0v, *b14]
print(f"   random beta1..4 = {np.round(b14, 4).tolist()}, positive root c* = {k:.6f}, beta0 fixed to {b0v:.6f}")
print(f"   at c*: lambda_g = {lamg_num(k, *bet):.2e}, lambda_f = {lamf_num(k, *bet):.2e}  (flat proportional vacuum, one condition)")
betp = [bet[n] * k**n for n in range(5)]
lg1 = sum(betp[n] * comb(3, n) for n in range(5)); lf1 = sum(betp[n] * comb(3, n - 1) for n in range(1, 5))
print(f"   after f -> f/c*^2, beta_n -> beta_n c*^n: lambda_g(1) = {lg1:.2e}, lambda_f(1) = {lf1:.2e}")
s1 = P(gR, fR, bet); s2 = P(gR, fR / k**2, betp)
print(f"   same potential: P(g, f; beta) - P(g, f/c*^2; beta') = {s1 - s2:.2e}")
print("   -> in generic HR both c = 1 conditions hold after a change of units for f: one physical tuning.")
# discrimination test for the rescaling identity: random k, random beta; and a wrong rescaling
kr = 1.0 + 3.0 * rng.random(); br = rng.standard_normal(5)
ok = P(gR, fR, br); good = P(gR, fR / kr**2, [br[n] * kr**n for n in range(5)])
bad = P(gR, fR / kr**2, [br[n] * kr**(n + 1) for n in range(5)])
print(f"   discrimination (k = {kr:.4f}): right rescaling rel. diff {abs(ok-good)/abs(ok):.1e}; "
      f"wrong rescaling rel. diff {abs(ok-bad)/abs(ok):.2f}")
