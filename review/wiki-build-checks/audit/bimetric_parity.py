"""Audit of flag 39, bimetric side (#8 s1, s3; #11 s7.3, s7.5).

Hassan-Rosen potential, Euclidean skeleton, d = 4:
    V(g, f) = sqrt(det g) * sum_n beta_n e_n( sqrt(g^-1 f) )
#8 s1: palindrome beta_n = beta_{4-n}; #8 s2: flat aligned vacuum forces T = 0 = V(1).
Anchor independent of the program: at a proportional flat background with vanishing
tadpoles the HR quadratic potential must have Fierz-Pauli structure Tr(u^2) - (Tr u)^2
(the defining property of the dRGT/HR family) -- used to check this implementation.
High precision (mpmath, 40 digits) so finite differences are not the limiting error.
"""
import mpmath as mp
import sympy as sp
import random

mp.mp.dps = 40
D = 4
random.seed(39)

def rsym(scale=1.0):
    A = mp.matrix(D, D)
    for i in range(D):
        for j in range(i, D):
            v = mp.mpf(random.uniform(-1, 1))*scale
            A[i, j] = v; A[j, i] = v
    return A

def rpos():
    A = mp.matrix(D, D)
    for i in range(D):
        for j in range(D):
            A[i, j] = mp.mpf(random.uniform(-1, 1))
    return A*A.T + mp.eye(D)

def esym(A):
    """e_0..e_4 of the eigenvalues of A via Newton's identities on traces of powers."""
    p = [None] + [sum((A**k)[i, i] for i in range(D)) for k in range(1, D + 1)]
    e = [mp.mpf(1)]
    for n in range(1, D + 1):
        e.append(sum(((-1)**(k - 1))*e[n - k]*p[k] for k in range(1, n + 1))/n)
    return e

def V(g, f, beta):
    Xm = mp.sqrtm(mp.inverse(g)*f)
    e = esym(Xm)
    return mp.sqrt(mp.det(g))*sum(beta[n]*e[n] for n in range(D + 1))

def palin(b1, b2):
    b0 = -4*b1 - 3*b2              # T = b0 + 4 b1 + 3 b2 = 0 under the palindrome
    return [b0, b1, b2, b1, b0]

def tr(A):
    return sum(A[i, i] for i in range(D))

betaA = palin(mp.mpf("0.7"), mp.mpf("-0.3"))
betaB = palin(mp.mpf("-1.1"), mp.mpf("0.45"))
from math import comb
for name, beta in (("A", betaA), ("B", betaB)):
    V1 = sum(beta[n]*comb(4, n) for n in range(5))
    T = sum(beta[n]*comb(3, n - 1) for n in range(1, 5))
    print(f"beta set {name} = {[mp.nstr(b, 6) for b in beta]}: V(1) = {mp.nstr(V1, 5)}, T = {mp.nstr(T, 5)}")

print("\n== G1. Exchange (swap) symmetry of the potential density")
g, f = rpos(), rpos()
print("palindromic: |V(g,f) - V(f,g)| =", mp.nstr(abs(V(g, f, betaA) - V(f, g, betaA)), 5))
nonpal = [mp.mpf(x) for x in ("0.3", "0.7", "-0.3", "0.2", "-1.0")]
print("non-palindromic control: |V(g,f) - V(f,g)| =", mp.nstr(abs(V(g, f, nonpal) - V(f, g, nonpal)), 5))

print("\n== G2. The documents' aligned-frame map g -> g^-1 with f frozen at 1 (= #11 s6 at X = 0)")
g = rpos()
r = V(mp.inverse(g), mp.eye(D), betaA)/V(g, mp.eye(D), betaA)
print("V(g^-1, 1)/V(g, 1) =", mp.nstr(r, 12), "; det(g)^(-1/2) =", mp.nstr(1/mp.sqrt(mp.det(g)), 12),
      " -> not a symmetry of the potential density by itself")

print("\n== G3. Mass structure about g = f = 1:  g = 1 + a S + b U,  f = 1 + a S - b U")
print("   (a = even direction s = (dg+df)/2, b = odd direction t = (dg-df)/2)")
step = mp.mpf("1e-12")
def phi(a, b, S, U, beta):
    return V(mp.eye(D) + a*S + b*U, mp.eye(D) + a*S - b*U, beta)
for beta, name in ((betaA, "A"), (betaB, "B")):
    S, U = rsym(), rsym()
    p00 = phi(0, 0, S, U, beta)
    fa = (phi(step, 0, S, U, beta) - phi(-step, 0, S, U, beta))/(2*step)
    fb = (phi(0, step, S, U, beta) - phi(0, -step, S, U, beta))/(2*step)
    faa = (phi(step, 0, S, U, beta) - 2*p00 + phi(-step, 0, S, U, beta))/step**2
    fbb = (phi(0, step, S, U, beta) - 2*p00 + phi(0, -step, S, U, beta))/step**2
    fab = (phi(step, step, S, U, beta) - phi(step, -step, S, U, beta)
           - phi(-step, step, S, U, beta) + phi(-step, -step, S, U, beta))/(4*step**2)
    print(f"beta {name}: V0={mp.nstr(p00,3)}  dV/ds={mp.nstr(fa,3)}  dV/dt={mp.nstr(fb,3)}  "
          f"d2V/ds2={mp.nstr(faa,3)}  d2V/dsdt={mp.nstr(fab,3)}  d2V/dt2={mp.nstr(fbb,8)}")
    # exact statement along the even line: V(g, g) = sqrt(det g) V(1) = 0 for any g
    gg = rpos()
    print(f"          V(g, g) at a random g (exact even direction, all orders) = {mp.nstr(V(gg, gg, beta), 3)}")

print("\n== G4. Anchor: the odd-mode quadratic term has Fierz-Pauli structure, coefficient prop. to beta1+2beta2+beta3")
for beta, name in ((betaA, "A"), (betaB, "B")):
    ratios = []
    for _ in range(4):
        U = rsym()
        fbb = (phi(0, step, U, U, beta) - 2*phi(0, 0, U, U, beta) + phi(0, -step, U, U, beta))/step**2
        fbb = (V(mp.eye(D) + step*U, mp.eye(D) - step*U, beta) - 2*V(mp.eye(D), mp.eye(D), beta)
               + V(mp.eye(D) - step*U, mp.eye(D) + step*U, beta))/step**2
        FP = tr(U*U) - tr(U)**2
        ratios.append(fbb/FP)
    comb_ = beta[1] + 2*beta[2] + beta[3]
    print(f"beta {name}: (d2V/dt2)/[Tr(u^2)-(Tr u)^2] over 4 random u = {[mp.nstr(x, 12) for x in ratios]}; "
          f"divided by (beta1+2beta2+beta3) = {mp.nstr(ratios[0]/comb_, 12)}")

print("\n== G5. What the documents' bridge 'X -> X^-1' fixes: linear part of sqrt(g^-1 f)")
a_, b_ = rsym(), rsym()
eps = mp.mpf("1e-18")
Xm = mp.sqrtm(mp.inverse(mp.eye(D) + eps*a_)*(mp.eye(D) + eps*b_))
lin = (Xm - mp.eye(D))/eps
err = max(abs((lin - (b_ - a_)/2)[i, j]) for i in range(D) for j in range(D))
print("max |(sqrt(g^-1 f) - 1)/eps - (df - dg)/2| =", mp.nstr(err, 3),
      " (non-commuting dg, df) -> X's linear part sees only the odd mode; the even mode dg+df drops out")

print("\n== G6. Which linear involutions of (dg, df) give dg+df even and dg-df odd?")
p, q, r_, u = sp.symbols("p q r u")
L = sp.Matrix([[p, q], [r_, u]])            # (dg, df) -> L (dg, df), same map on every component
sol = sp.solve(list(L*sp.Matrix([1, 1]) - sp.Matrix([1, 1])) + list(L*sp.Matrix([1, -1]) + sp.Matrix([1, -1])),
               [p, q, r_, u], dict=True)
print("solutions:", sol, " (unique: the swap)")
sol2 = sp.solve(list(L*sp.Matrix([1, 1]) - sp.Matrix([1, 1])) + list(L*sp.Matrix([1, -1]) + sp.Matrix([1, -1]))
                + [p + 1, q], [p, q, r_, u], dict=True)
print("adding 'dg -> -dg' (scale-factor duality on the metric, #11 s6):", sol2, " (no solution)")

print("\n== G7. Equal Planck masses: kinetic cross terms cancel in the (s, t) basis (identity)")
Q = sp.Function("Q")
s_, t_, k = sp.symbols("s t k")
quad = lambda z: k*z**2                     # any quadratic form; scalar stand-in suffices for the identity
print("Q(s+t) + Q(s-t) - 2Q(s) - 2Q(t) =", sp.expand(quad(s_ + t_) + quad(s_ - t_) - 2*quad(s_) - 2*quad(t_)))
