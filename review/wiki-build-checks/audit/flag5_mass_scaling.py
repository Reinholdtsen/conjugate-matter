"""Flag 5 audit: does the beta-combination 2(b1+b2) fix M_X or M_X^2?

Part A  (sympy)  palindrome: b1 + 2 b2 + b3 = 2(b1 + b2); T = 0 gives b0 = -4 b1 - 3 b2.
Part B  (mpmath, 60 digits) second-order expansion of the Hassan-Rosen potential
        U(g,f) = sqrt(det g) * sum_n b_n e_n(sqrt(g^-1 f))   (#8 section 1's V, without 2 m^2 M^2)
        about the aligned point g = f = 1 (d = 4, Euclidean skeleton), g = 1 + eps h, f = 1 + eps l,
        on the program's family (palindrome + T = 0, so V(1) = 0).
        Fits U_2 = a Tr(D^2) + b (Tr D)^2 with D = h - l, checks b = -a (Fierz-Pauli form),
        checks that a depends on (b1, b2) only through b1 + b2, and that a is linear in the b's.
Part C  mass from the quadratic action. With the standard linearized Einstein-Hilbert normalization
        (model memory, see note), M_g = M_f (alpha = 1) gives m_FP^2 = 16 m^2 a; compared with the
        literature formula m_FP^2 = 2 m^2 (b1 + 2 b2 + b3) at c = alpha = 1 (dagger, model memory).
        Whatever the kinetic normalization, it does not contain the b's, so m_FP^2 is linear in them.
Part D  independent textbook anchor: the static Green's function of (-Laplacian + k) in 3D decays as
        exp(-sqrt(k) r)/(4 pi r).  The Yukawa range is 1/sqrt(k): the mass is the square root of the
        quadratic coefficient. Computed by numerical Fourier integral, not by the closed form.
"""
import random
import mpmath as mp
import sympy as sp
from itertools import combinations

mp.mp.dps = 60
d = 4

# ---------------- Part A ----------------
b0, b1, b2, b3, b4 = sp.symbols('b0:5')
pal = {b3: b1, b4: b0}
T = b1 + 3*b2 + 3*b3 + b4                       # #8 section 2
V1 = sum(sp.binomial(4, n)*s for n, s in enumerate([b0, b1, b2, b3, b4]))
print("A1  (b1+2b2+b3) - 2(b1+b2) under palindrome:", sp.simplify((b1 + 2*b2 + b3).subs(pal) - 2*(b1 + b2)))
sol_b0 = sp.solve(sp.Eq(T.subs(pal), 0), b0)[0]
print("A2  T = 0 under palindrome gives b0 =", sol_b0)
print("A3  V(1) - 2T under palindrome:", sp.simplify((V1 - 2*T).subs(pal)))

# ---------------- Part B ----------------
def esym(vals, n):
    if n == 0:
        return mp.mpf(1)
    return mp.fsum(mp.fprod(c) for c in combinations(vals, n))

def U(g, f, beta):
    E, Q = mp.eigsy(g)
    gm12 = Q * mp.diag([1/mp.sqrt(e) for e in E]) * Q.T
    S = gm12 * f * gm12
    S = (S + S.T) / 2
    lam, _ = mp.eigsy(S)
    s = [mp.sqrt(x) for x in lam]
    sqrtdet = mp.sqrt(mp.fprod(E))
    return sqrtdet * mp.fsum(beta[n] * esym(s, n) for n in range(5))

def family(B1, B2):
    """palindrome + T = 0"""
    B1, B2 = mp.mpf(B1), mp.mpf(B2)
    B0 = -4*B1 - 3*B2
    return [B0, B1, B2, B1, B0]

rng = random.Random(5)
def randsym():
    m = mp.matrix(d, d)
    for i in range(d):
        for j in range(i, d):
            v = mp.mpf(rng.uniform(-1, 1))
            m[i, j] = v
            m[j, i] = v
    return m

I4 = mp.eye(d)
eps = mp.mpf('1e-20')

def second_order(h, l, beta):
    up = U(I4 + eps*h, I4 + eps*l, beta)
    dn = U(I4 - eps*h, I4 - eps*l, beta)
    c0 = U(I4, I4, beta)
    return (up + dn - 2*c0) / (2*eps**2), c0, (up - dn) / (2*eps)

def tr(m):
    return mp.fsum(m[i, i] for i in range(d))

def fit_ab(beta):
    Ds = [randsym(), randsym()]
    rows, rhs = [], []
    for D in Ds:
        F2, _, _ = second_order(D/2, -D/2, beta)
        rows.append([tr(D*D), tr(D)**2]); rhs.append(F2)
    a, b = mp.lu_solve(mp.matrix(rows), mp.matrix(rhs))
    return a, b

print()
print("B   aligned-point expansion of U on the family (palindrome + T = 0)")
checks = [(1, 0), (0, 1), (0.25, 0.75), (2, -1), (2, 0), (0.6, 1.4)]
results = {}
for B1, B2 in checks:
    beta = family(B1, B2)
    a, b = fit_ab(beta)
    # cross-check on a generic (h, l), not just h = -l
    h, l = randsym(), randsym()
    F2, c0, F1 = second_order(h, l, beta)
    D = h - l
    resid = F2 - (a*tr(D*D) + b*tr(D)**2)
    results[(B1, B2)] = a
    print(f"    b1={B1:<5} b2={B2:<5} b1+b2={B1+B2:<5}  a={mp.nstr(a, 12):<16} b+a={mp.nstr(b + a, 3):<10}"
          f" a/((b1+2b2+b3)/8)={mp.nstr(a / ((2*(mp.mpf(B1)+mp.mpf(B2)))/8), 12):<14}"
          f" U(1,1)={mp.nstr(c0, 3):<8} |1st order|={mp.nstr(abs(F1), 3):<8} generic-(h,l) residual={mp.nstr(resid, 3)}")

print()
print("B'  linearity: a(2,0)/a(1,0) =", mp.nstr(results[(2, 0)] / results[(1, 0)], 15),
      "; a(0.6,1.4)/a(0.25,0.75) =", mp.nstr(results[(0.6, 1.4)] / results[(0.25, 0.75)], 15),
      "  (b1+b2 doubled in both)")
print("    same b1+b2, different split: a(1,0), a(0,1), a(0.25,0.75), a(2,-1) =",
      [mp.nstr(results[k], 12) for k in [(1, 0), (0, 1), (0.25, 0.75), (2, -1)]])

# ---------------- Part C ----------------
print()
print("C   m_FP^2 / m^2 = 16 a  (alpha = 1, standard EH normalization)  vs  2(b1 + 2b2 + b3) [dagger]:")
for k in [(1, 0), (2, 0), (0.6, 1.4)]:
    B1, B2 = k
    lit = 2 * (2*(mp.mpf(B1) + mp.mpf(B2)))
    print(f"    b1={B1}, b2={B2}:  16a = {mp.nstr(16*results[k], 12)},  2(b1+2b2+b3) = {mp.nstr(lit, 12)}")
r2 = results[(2, 0)] / results[(1, 0)]
print("    doubling b1+b2 multiplies M_X^2 by", mp.nstr(r2, 12), "and M_X by", mp.nstr(mp.sqrt(r2), 12),
      "(a literal M_X ∝ 2(b1+b2) would need 2)")

# ---------------- Part D ----------------
print()
print("D   textbook anchor: G_k(r) = 1/(2 pi^2 r) * Int_0^inf q sin(q r)/(q^2 + k) dq, decay rate of r*G")
def G(k, r):
    k = mp.mpf(k); r = mp.mpf(r)
    integral = mp.quadosc(lambda q: q*mp.sin(q*r)/(q**2 + k), [0, mp.inf], omega=r)
    return integral / (2*mp.pi**2*r)
mp.mp.dps = 30
for k in [1, 4, 16]:
    r1, r2_ = mp.mpf(2), mp.mpf(5)
    rate = -(mp.log(r2_*G(k, r2_)) - mp.log(r1*G(k, r1))) / (r2_ - r1)
    print(f"    k={k:<3} fitted decay rate = {mp.nstr(rate, 10):<14} sqrt(k) = {mp.nstr(mp.sqrt(k), 10):<6}"
          f" range = {mp.nstr(1/rate, 10)}")
print("    quadrupling the quadratic coefficient k halves the Yukawa range: the mass is sqrt(k).")
