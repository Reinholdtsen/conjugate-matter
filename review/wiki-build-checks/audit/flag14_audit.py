"""Flag 14 audit (independent of review/wiki-build-checks/sqrt_eig_check.py).

Source statement, notes/tuning-test.md (#7) §2 item 3:
  "The X = 0 slice gives Tr(S^2) = Tr(g^2) + Tr(g^-2) - 2d. The Hassan-Rosen
   ghost-free family is linear combinations sum beta_n e_n(sqrt(g^-1 f));
   Tr(g^2) = p4 of the square-root eigenvalues is a nonlinear polynomial in
   the e_n, hence outside the family."

Setting (from #7 §2, #5 §C): vacuum frame, reference metric f = 1, g = Y = Im Z.
Anchors are textbook identities (Newton's identities, e_n of reciprocals,
the Hassan-Rosen exchange identity), not numbers taken from the paper.
"""
import numpy as np
import sympy as sp
from itertools import combinations, combinations_with_replacement
from math import comb

rng = np.random.default_rng(20261021)

def en(vals, n):
    return 1.0 if n == 0 else float(sum(np.prod(c) for c in combinations(vals, n)))

def p(vals, k):
    return float(np.sum(np.asarray(vals) ** k))

def spd(d, lo=0.5, hi=2.0):
    """random SPD matrix whose square-root eigenvalues lie in [lo, hi] (T7's range)"""
    q, _ = np.linalg.qr(rng.standard_normal((d, d)))
    s = rng.uniform(lo, hi, size=d)
    return q @ np.diag(s ** 2) @ q.T

def msqrt(M):
    """principal square root of a diagonalizable matrix with positive eigenvalues"""
    w, V = np.linalg.eig(M)
    assert np.all(np.abs(w.imag) < 1e-10) and np.all(w.real > 0)
    return (V @ np.diag(np.sqrt(w.real)) @ np.linalg.inv(V)).real

def eigs(M):
    w = np.linalg.eigvals(M)
    return np.sort(w.real)

print("=== 1. Tr(S^2) on the X = 0 slice, from the full anticommutator {J0, I[Z]} ===")
for d in (3, 4, 5):
    Y = spd(d); Yi = np.linalg.inv(Y); X = np.zeros((d, d)); I_ = np.eye(d); O = np.zeros((d, d))
    HZ = np.block([[Y + X @ Yi @ X, X @ Yi], [Yi @ X, Yi]])
    omega = np.block([[O, I_], [-I_, O]]); J0 = np.block([[O, I_], [I_, O]])
    IZ = np.linalg.inv(omega) @ HZ
    M = J0 @ IZ + IZ @ J0
    S = M[:d, :d]
    lhs = np.trace(S @ S); rhs = np.trace(Y @ Y) + np.trace(Yi @ Yi) - 2 * d
    print(f"d={d}: Tr(S^2) = {lhs:.12f}   Tr(g^2)+Tr(g^-2)-2d = {rhs:.12f}   match={np.isclose(lhs, rhs)}")

print("\n=== 2. Which trace is p4 of which square-root eigenvalues (vacuum frame f = 1) ===")
for d in (3, 4, 5):
    g = spd(d); f = np.eye(d); gi = np.linalg.inv(g)
    mu = eigs(msqrt(gi @ f))   # eigenvalues of sqrt(g^-1 f)
    s = eigs(msqrt(np.linalg.inv(f) @ g))   # eigenvalues of sqrt(f^-1 g)
    sq_of_eig_g = np.sort(np.sqrt(np.linalg.eigvalsh(g)))   # square roots of g's eigenvalues
    print(f"d={d}: p4(eig sqrt(g^-1 f)) = {p(mu,4):.10f}  Tr(g^-2) = {np.trace(gi@gi):.10f}  Tr(g^2) = {np.trace(g@g):.10f}")
    print(f"      p4(eig sqrt(f^-1 g)) = {p(s,4):.10f}  (= Tr(g^2): {np.isclose(p(s,4), np.trace(g@g))});"
          f"  eig sqrt(f^-1 g) == sqrt(eig g): {np.allclose(s, sq_of_eig_g)}")

print("\n=== 3. Covariant form with a general reference f (not 1) ===")
d = 4; g = spd(d); f = spd(d); gi = np.linalg.inv(g); fi = np.linalg.inv(f)
mu = eigs(msqrt(gi @ f)); s = eigs(msqrt(fi @ g))
print(f"p4(eig sqrt(g^-1 f)) = {p(mu,4):.10f}   Tr[(g^-1 f)^2] = {np.trace(gi@f@gi@f):.10f}")
print(f"p4(eig sqrt(f^-1 g)) = {p(s,4):.10f}   Tr[(f^-1 g)^2] = {np.trace(fi@g@fi@g):.10f}")
print("exchange identity sqrt|g| e_n(sqrt(g^-1 f)) = sqrt|f| e_{4-n}(sqrt(f^-1 g)), n=0..4:")
lhs = [np.sqrt(np.linalg.det(g)) * en(mu, n) for n in range(5)]
rhs = [np.sqrt(np.linalg.det(f)) * en(s, 4 - n) for n in range(5)]
print("  lhs =", [round(v, 8) for v in lhs]); print("  rhs =", [round(v, 8) for v in rhs])
print("  all close:", np.allclose(lhs, rhs))

print("\n=== 4. Exact (sympy): Newton, reciprocal e_n, and Tr(g^2) as a function of e_n(mu) ===")
m = sp.symbols("m1:5", positive=True)
E = lambda vals, n: sp.Integer(1) if n == 0 else sum(sp.Mul(*c) for c in combinations(vals, n))
e1, e2, e3, e4 = (E(m, n) for n in range(1, 5))
newton = lambda a1, a2, a3, a4: a1**4 - 4*a1**2*a2 + 2*a2**2 + 4*a1*a3 - 4*a4
P4 = sum(v**4 for v in m)
print("Newton p4 = e1^4 - 4 e1^2 e2 + 2 e2^2 + 4 e1 e3 - 4 e4 (exact):", sp.expand(P4 - newton(e1, e2, e3, e4)) == 0)
inv = [1/v for v in m]
print("e_n(1/mu) = e_{4-n}(mu)/e_4(mu), n=0..4 (exact):",
      all(sp.simplify(E(inv, n) - E(m, 4 - n)/e4) == 0 for n in range(5)))
P4inv = sum(v**4 for v in inv)   # = Tr(g^2) when mu = eig sqrt(g^-1), since g's eigenvalues are 1/mu^2
rat = newton(e3/e4, e2/e4, e1/e4, 1/e4)
print("Tr(g^2) = p4(1/mu) = Newton(e3/e4, e2/e4, e1/e4, 1/e4) of mu (exact):", sp.simplify(P4inv - rat) == 0)
num, den = sp.fraction(sp.together(P4inv))
print("Tr(g^2) written over mu has denominator:", sp.factor(den), " -> not a polynomial in mu, hence not in the e_n(mu)")
print("density at f=1: sqrt(det g) e_n(mu) = e_{4-n}(s), s = 1/mu (exact):",
      all(sp.simplify(E(m, n)/e4 - E(inv, 4 - n)) == 0 for n in range(5)))

print("\n=== 5. Tr(g^2) is not a polynomial in e_n(mu): e_n(mu) stay bounded while Tr(g^2) diverges ===")
for eps in (1e-1, 1e-2, 1e-3):
    mu_ = np.array([eps, 1.0, 1.0, 1.0])
    print(f"mu=({eps:g},1,1,1): e_1..e_4(mu) = {[round(en(mu_, n), 6) for n in range(1, 5)]}, "
          f"Tr(g^2)=p4(1/mu) = {p(1/mu_, 4):.6g}, Tr(g^-2)=p4(mu) = {p(mu_, 4):.6g}")

print("\n=== 6. Least-squares membership tests over 400 random g (f = 1, sqrt-eigs in [0.5, 2]) ===")
N = 400; rows = []
for _ in range(N):
    g = spd(4); gi = np.linalg.inv(g)
    mu = eigs(msqrt(gi)); s = eigs(msqrt(g))
    rows.append(dict(mu=mu, s=s, trg2=np.trace(g@g), trgm2=np.trace(gi@gi),
                     trS2=np.trace((g-gi)@(g-gi)), detg=np.linalg.det(g)))
lin = lambda v: [en(v, n) for n in range(5)]
nl = lambda v: [en(v,1)**4, en(v,1)**2*en(v,2), en(v,2)**2, en(v,1)*en(v,3), en(v,4)]
def fit(basis_fn, key, target):
    A = np.array([basis_fn(r[key]) for r in rows]); b = np.array([target(r) for r in rows])
    c, *_ = np.linalg.lstsq(A, b, rcond=None)
    return np.sqrt(np.mean((A @ c - b) ** 2)), c
beta = rng.standard_normal(5)
targets = {
    "Tr(g^2)": lambda r: r["trg2"],
    "Tr(g^-2)": lambda r: r["trgm2"],
    "Tr(S^2) at X=0": lambda r: r["trS2"],
}
print("Convention A (bare potential function vs sum beta_n e_n(mu); same sqrt|g| on both sides):")
ctrlA = lambda r: sum(beta[n]*en(r["mu"], n) for n in range(5))
for name, t in list(targets.items()) + [("control: an HR member sum beta_n e_n(mu)", ctrlA)]:
    rl, _ = fit(lin, "mu", t); rn, cn = fit(nl, "mu", t)
    print(f"  {name:42s} rms vs span{{e_n(mu)}} = {rl:.3e}   rms vs Newton-degree-4 monomials in e_n(mu) = {rn:.3e}"
          + (f"  coeffs={np.round(cn, 6).tolist()}" if rn < 1e-8 else ""))
print("Convention B (fixed measure, e.g. sqrt|f| = 1 or sqrt|H| = 1; HR density sqrt|g| sum beta_n e_n(mu) = sum beta_n e_{4-n}(s)):")
ctrlB = lambda r: np.sqrt(r["detg"]) * sum(beta[n]*en(r["mu"], n) for n in range(5))
for name, t in list(targets.items()) + [("control: an HR density sqrt|g| sum beta_n e_n(mu)", ctrlB)]:
    rl, _ = fit(lin, "s", t); rn, cn = fit(nl, "s", t)
    print(f"  {name:42s} rms vs span{{e_n(s)}}  = {rl:.3e}   rms vs Newton-degree-4 monomials in e_n(s)  = {rn:.3e}"
          + (f"  coeffs={np.round(cn, 6).tolist()}" if rn < 1e-8 else ""))
