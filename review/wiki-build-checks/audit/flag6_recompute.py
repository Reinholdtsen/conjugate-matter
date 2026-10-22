"""Flag 6 audit: is the wedge-sector vacuum energy zero "by symmetry rather than tuning"?

Independent recomputation from the Hassan-Rosen potential as #8 section 1 states it:
    U(g, f) = sqrt|det g| * sum_n beta_n e_n( sqrt(g^-1 f) ),  d = 4,
    action  S = M_g^2 sqrt(g) R(g) + M_f^2 sqrt(f) R(f) - 2 m^4 U(g, f).
Field equations (textbook variation, delta(sqrt g R) = -sqrt g G^{mu nu} delta g_{mu nu}):
    g-eq:  M_g^2 sqrt(g) G^{mu nu}(g) = -2 m^4 dU/dg_{mu nu}
    f-eq:  M_f^2 sqrt(f) G^{mu nu}(f) = -2 m^4 dU/df_{mu nu}
On flat metrics G = 0, so a flat background needs dU/dg = 0 and dU/df = 0 there.
Nothing below uses #8's own T or V(1) as input; they are compared at the end.
"""
import numpy as np
import sympy as sp
from itertools import combinations
from math import comb

print("=" * 72)
print("A. Potential's contribution to both field equations at f = c^2 g (sympy, exact)")
print("=" * 72)
b = sp.symbols("beta0:5", real=True)
c = sp.symbols("c", positive=True)
gs = sp.symbols("g1:5", positive=True)
fs = sp.symbols("f1:5", positive=True)


def e(vals, n):
    if n == 0:
        return sp.Integer(1)
    return sp.Add(*[sp.Mul(*cm) for cm in combinations(vals, n)])


lam = [sp.sqrt(fs[i] / gs[i]) for i in range(4)]  # eigenvalues of sqrt(g^-1 f), diagonal metrics
U = sp.sqrt(sp.Mul(*gs)) * sp.Add(*[b[n] * e(lam, n) for n in range(5)])
bg = {**{gs[i]: 1 for i in range(4)}, **{fs[i]: c**2 for i in range(4)}}
dUdg = [sp.simplify(sp.diff(U, gs[i]).subs(bg)) for i in range(4)]
dUdf = [sp.simplify(sp.diff(U, fs[i]).subs(bg)) for i in range(4)]
print("isotropic (all four components equal):",
      all(sp.simplify(x - dUdg[0]) == 0 for x in dUdg),
      all(sp.simplify(x - dUdf[0]) == 0 for x in dUdf))
Pg = sp.expand(2 * dUdg[0])
Qf = sp.expand(2 * dUdf[0])
print("2 dU/dg_ii at (1, c^2) =", Pg)
print("2 dU/df_ii at (1, c^2) =", Qf)
# Textbook HR proportional-background combinations (Hassan-Schmidt-May-von Strauss form, dagger):
Pg_txt = b[0] + 3 * b[1] * c + 3 * b[2] * c**2 + b[3] * c**3
Qf_txt = (c * b[1] + 3 * c**2 * b[2] + 3 * c**3 * b[3] + c**4 * b[4]) / c**2
print("matches beta0+3c beta1+3c^2 beta2+c^3 beta3 :", sp.simplify(Pg - Pg_txt) == 0)
print("matches (c b1+3c^2 b2+3c^3 b3+c^4 b4)/c^2   :", sp.simplify(Qf - Qf_txt) == 0)
# In units of m^4: Lambda_g = Pg/M_g^2 (g-eq), Lambda_f = Qf/M_f^2 (f-eq, sqrt f * f^{..}f^{..} = c^4 c^-4)

print()
print("At the aligned point c = 1:")
Lg1 = sp.expand(Pg.subs(c, 1))
Lf1 = sp.expand(Qf.subs(c, 1))
V1 = sp.expand(sum(b[n] * comb(4, n) for n in range(5)))  # U at g = f = 1
T8 = b[1] + 3 * b[2] + 3 * b[3] + b[4]                    # #8's T, for comparison only
print("  g-eq flatness form  L_g =", Lg1)
print("  f-eq flatness form  L_f =", Lf1)
print("  U(1,1) = V(1)           =", V1)
print("  L_g == V(1) - T(#8) :", sp.expand(Lg1 - (V1 - T8)) == 0, "  (#8 sec.2: 'V(1) = T' is the g-eq)")
print("  L_f == T(#8)        :", sp.expand(Lf1 - T8) == 0)
print("  V(1) == L_g + L_f   :", sp.expand(V1 - Lg1 - Lf1) == 0, "  (Pascal: C(4,n) = C(3,n) + C(3,n-1))")

print()
print("Even/odd tadpoles under the exchange g <-> f (massless = even, X = odd, #8 sec.3):")
even = sp.expand(Lg1 + Lf1)
odd = sp.expand(Lg1 - Lf1)
print("  even (sources the massless graviton's Lambda):", even)
print("  odd  (relative mode):                          ", odd)
pal = {b[3]: b[1], b[4]: b[0]}
print("  palindrome beta_n = beta_{4-n}:  odd ->", sp.expand(odd.subs(pal)),
      "   even ->", sp.expand(even.subs(pal)))
print("  palindrome: L_g ->", sp.expand(Lg1.subs(pal)), "  L_f ->", sp.expand(Lf1.subs(pal)),
      "  V(1) ->", sp.expand(V1.subs(pal)))

print()
print("=" * 72)
print("B. Counting conditions on (beta0..beta4) (exact linear algebra)")
print("=" * 72)
row = lambda expr: [sp.expand(expr).coeff(b[n]) for n in range(5)]
Mflat = sp.Matrix([row(Lg1), row(Lf1)])
Mpal = sp.Matrix([[1, 0, 0, 0, -1], [0, 1, 0, -1, 0]])  # beta0-beta4 = 0, beta1-beta3 = 0
print("generic bimetric, flat aligned vacuum: rank", Mflat.rank(), "-> free betas", 5 - Mflat.rank())
print("palindrome alone:                       rank", Mpal.rank(), "-> free betas", 5 - Mpal.rank())
Mboth = Mpal.col_join(Mflat)
print("palindrome + flat aligned vacuum:       rank", Mboth.rank(), "-> free betas", 5 - Mboth.rank())
print("  conditions added by flatness beyond the palindrome:", Mboth.rank() - Mpal.rank())
Ppar = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]])  # beta = P (p0,p1,p2)
print("flatness forms restricted to the palindromic subspace:", list(Mflat * Ppar),
      " rank", (Mflat * Ppar).rank())
print("is V(1) zero on the generic flat-aligned locus (no palindrome)?",
      sp.Matrix([row(V1)]).rank() == 1 and sp.Matrix([row(V1)]).col_join(Mflat).rank() == Mflat.rank())

print()
print("=" * 72)
print("C. A palindromic theory whose aligned vacuum is not flat: the PM point (#11 sec.7.4)")
print("=" * 72)
al, b2, Mg = sp.symbols("alpha beta_2 M_g", positive=True)
pm = {b[0]: 3 * b2 / al**2, b[1]: 0, b[2]: b2, b[3]: 0, b[4]: 3 * al**2 * b2}
Mf = al * Mg
lam_g = sp.simplify((Pg / Mg**2).subs(pm))
lam_f = sp.simplify((Qf / Mf**2).subs(pm))
print("Lambda_g(c) - Lambda_f(c) at the PM point:", sp.simplify(lam_g - lam_f),
      " (zero for every c = 'undetermined ratio', the published PM hallmark)")
print("Lambda(c) [units m^4] =", sp.factor(lam_g))
pm1 = {k: sp.sympify(v).subs(al, 1) for k, v in pm.items()}
print("alpha = 1 betas:", [pm1[b[n]] for n in range(5)], "palindromic:",
      pm1[b[0]] == pm1[b[4]] and pm1[b[1]] == pm1[b[3]])
print("  aligned (c=1) Lambda =", sp.simplify(lam_g.subs({al: 1, c: 1})),
      "  T_pal = beta0+4beta1+3beta2 =", sp.simplify((b[0] + 4 * b[1] + 3 * b[2]).subs(pm1)))
print("  real zeros of Lambda(c) at alpha=1:", sp.solve(sp.Eq(lam_g.subs(al, 1), 0), c))

print()
print("=" * 72)
print("D. Numerical cross-check with full symmetric perturbations (numpy, no diagonal shortcut)")
print("=" * 72)
rng = np.random.default_rng(20261021)


def U_num(beta, g, f):
    ev = np.linalg.eigvals(np.linalg.solve(g, f)).astype(complex)
    en = np.poly(-np.sqrt(ev))          # coefficients of prod(x + s_i) = e_0..e_4
    val = np.sqrt(abs(np.linalg.det(g))) * np.dot(beta, en)
    return val


def check(beta, base, label):
    d = rng.standard_normal((4, 4)); d = (d + d.T) / 2
    eps = 1e-6
    dg = (U_num(beta, base + eps * d, base) - U_num(beta, base - eps * d, base)) / (2 * eps)
    df = (U_num(beta, base, base + eps * d) - U_num(beta, base, base - eps * d)) / (2 * eps)
    tr = np.trace(np.linalg.solve(base, d))
    V1n = sum(beta[n] * comb(4, n) for n in range(5))
    T8n = beta[1] + 3 * beta[2] + 3 * beta[3] + beta[4]
    print(f"  {label}: dU/dg.d = {dg.real:+.8f}  vs (V1-T)/2 Tr = {0.5*(V1n-T8n)*tr:+.8f}; "
          f"dU/df.d = {df.real:+.8f} vs T/2 Tr = {0.5*T8n*tr:+.8f}; |Im| < {max(abs(dg.imag), abs(df.imag)):.0e}")


beta_gen = rng.standard_normal(5)
p = rng.standard_normal(3)
beta_pal = np.array([p[0], p[1], p[2], p[1], p[0]])
for base, nm in [(np.eye(4), "Euclidean"), (np.diag([-1.0, 1, 1, 1]), "Lorentzian")]:
    check(beta_gen, base, f"generic beta, {nm}")
    check(beta_pal, base, f"palindromic beta, {nm}")
# exchange symmetry U(g,f) = U(f,g) iff palindrome (HR identity sqrt g e_n = sqrt f e_{4-n})
A = rng.standard_normal((4, 4)); G = A @ A.T + 4 * np.eye(4)
B = rng.standard_normal((4, 4)); F = B @ B.T + 4 * np.eye(4)
print("  U(g,f) - U(f,g): palindromic", f"{abs(U_num(beta_pal, G, F) - U_num(beta_pal, F, G)):.1e}",
      "| generic", f"{abs(U_num(beta_gen, G, F) - U_num(beta_gen, F, G)):.1e}")
print("  palindromic sample: T_pal =", f"{beta_pal[0] + 4*beta_pal[1] + 3*beta_pal[2]:+.6f}",
      "-> aligned Lambda = m^4 T/M^2, not zero unless tuned")

print()
print("=" * 72)
print("E. Generic bimetric with the ratio c free: how many tunings for a flat proportional vacuum?")
print("=" * 72)
Pf_poly = sp.expand(Qf * c)  # b1 + 3 b2 c + 3 b3 c^2 + b4 c^3, same zeros as Qf for c > 0
res = sp.resultant(sp.Poly(Pg, c), sp.Poly(Pf_poly, c))
print("resultant(P_g, P_f; c) is a single polynomial condition on the betas; nonzero:", sp.expand(res) != 0,
      "| total degree", sp.Poly(res, *b).total_degree())
for trial in range(50):
    bb = rng.standard_normal(4)  # beta1..beta4
    roots = np.roots([bb[3], 3 * bb[2], 3 * bb[1], bb[0]])  # beta4 c^3 + 3beta3 c^2 + 3beta2 c + beta1
    pos = [r.real for r in roots if abs(r.imag) < 1e-12 and r.real > 0]
    if pos:
        cs = pos[0]
        break
b0 = -(3 * bb[0] * cs + 3 * bb[1] * cs**2 + bb[2] * cs**3)  # the single tuning
beta = np.array([b0, *bb])
Pg_n = sum(beta[n] * comb(3, n) * cs**n for n in range(4))
Pf_n = sum(beta[n] * comb(3, n - 1) * cs**(n - 1) for n in range(1, 5))
Vc_n = sum(beta[n] * comb(4, n) * cs**n for n in range(5))
print(f"random beta1..4 = {np.round(bb, 4)}, positive root c* = {cs:.6f}, tuned beta0 = {b0:.6f}")
print(f"  P_g(c*) = {Pg_n:.1e}, P_f(c*) = {Pf_n:.1e}, V(c*) = {Vc_n:.1e}")
bp = np.array([beta[n] * cs**n for n in range(5)])  # f -> f / c*^2 maps e_n -> c*^n e_n
Lg_p = sum(bp[n] * comb(3, n) for n in range(4)); Lf_p = sum(bp[n] * comb(3, n - 1) for n in range(1, 5))
print(f"  after rescaling f by 1/c*^2: beta' = {np.round(bp, 4)}; L_g = {Lg_p:.1e}, L_f = {Lf_p:.1e}"
      f" (flat, aligned); palindromic? {np.allclose(bp, bp[::-1])}")
# Einstein-Hilbert term under f -> s^2 f in d = 4 (textbook: sqrt f -> s^4, R -> s^-2), so M_f -> s M_f
t, x, y, z, s = sp.symbols("t x y z s", positive=True)
a = sp.Function("a")(t); N = sp.Function("N")(t)
X = [t, x, y, z]


def ricci_scalar(gm):
    gi = gm.inv()
    Gam = [[[sum(gi[r, l] * (sp.diff(gm[l, m], X[n]) + sp.diff(gm[l, n], X[m]) - sp.diff(gm[m, n], X[l]))
                 for l in range(4)) / 2 for n in range(4)] for m in range(4)] for r in range(4)]
    Ric = sp.zeros(4)
    for m in range(4):
        for n in range(4):
            Ric[m, n] = sum(sp.diff(Gam[r][m][n], X[r]) - sp.diff(Gam[r][m][r], X[n])
                            + sum(Gam[r][r][l] * Gam[l][m][n] - Gam[r][n][l] * Gam[l][m][r] for l in range(4))
                            for r in range(4))
    return sp.simplify(sum(gi[m, n] * Ric[m, n] for m in range(4) for n in range(4)))


fm = sp.diag(-N**2, a**2, a**2, a**2)
R1 = ricci_scalar(fm); R2 = ricci_scalar(s**2 * fm)
print("  R(s^2 f)/R(f) =", sp.simplify(R2 / R1), "; sqrt|det(s^2 f)|/sqrt|det f| =",
      sp.simplify(sp.sqrt(-(s**2 * fm).det()) / sp.sqrt(-fm.det())))
