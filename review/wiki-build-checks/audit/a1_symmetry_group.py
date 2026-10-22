"""Audit of flag 12, part 1: which continuous Sp(2,R) symmetries does each potential keep?

Conventions taken from the documents (toy note v2 Sec. 2, Sec. 4; verify/toy_coset.py):
  Sp(2,R) acts by H -> S^T H S, K -> S^-1 K S.
  K on the hyperboloid: K = [[A, b], [c, -A]], A^2 + b c = 1.
  naive potential  V_mu = -[Tr(K K_ref)]^2               (mu = 1)
  bounded variant  V_b  = -[Tr(K K_ref)]^2 / (2 Tr K^T K) (Frobenius norm, as written in all documents)
  lambda-term      V_lam = (1/8) Tr(H^-1 C^T H C), C = K I + I K, I = w^-1 H

Anchor (independent of the paper): trace cyclicity, Tr(S^-1 K S M) = Tr(K S M S^-1); if S commutes
with M = K_ref the trace is unchanged. So V_mu MUST come out exactly squeeze-invariant: a positive control.
"""
import numpy as np
import sympy as sp

w = sp.Matrix([[0, 1], [-1, 0]])
Kref = sp.diag(1, -1)

def V_mu(K):
    return -((K*Kref).trace())**2

def V_b(K):
    return -((K*Kref).trace())**2/(2*(K.T*K).trace())

def V_lam(H, K):
    I = w.inv()*H
    C = K*I + I*K
    return (H.inv()*C.T*H*C).trace()/8

a = sp.symbols('a', positive=True)
A, b, c = sp.symbols('A b c', real=True)
K = sp.Matrix([[A, b], [c, -A]])
S = sp.diag(a, 1/a)
Sc = S.inv()*K*S

print("== 1. Positive control: the naive potential under the squeeze S = diag(a, 1/a)")
print("   V_mu(S^-1 K S) - V_mu(K) =", sp.simplify(V_mu(Sc) - V_mu(K)))

print("\n== 2. The lambda-term under the squeeze, generic positive H (not only on the flat line)")
p, q, r = sp.symbols('p q r', real=True)
Hg = sp.Matrix([[p, q], [q, r]])
print("   V_lam(S^T H S, S^-1 K S) - V_lam(H, K) =", sp.simplify(V_lam(S.T*Hg*S, Sc) - V_lam(Hg, K)))

print("\n== 3. The bounded variant V_b under the squeeze")
d = sp.factor(sp.simplify(V_b(Sc) - V_b(K)))
print("   V_b(S^-1 K S) - V_b(K) =", d)
# a point on the hyperboloid: A = 1/2, b = 1, c = 3/4 (A^2 + bc = 1)
pt = {A: sp.Rational(1, 2), b: 1, c: sp.Rational(3, 4)}
print("   hyperboloid check A^2 + bc =", (A**2 + b*c).subs(pt))
for av in (sp.Rational(1, 2), 2, 3):
    print(f"   a = {av}: V_b before = {sp.nsimplify(V_b(K).subs(pt))}, after = {sp.nsimplify(V_b(Sc).subs(pt).subs(a, av))}")
# where is V_b invariant for every a? need the a-dependent factor to vanish identically in a
num = sp.numer(sp.together(d))
coeffs = sp.Poly(sp.expand(num), a).coeffs()
sols = sp.solve([sp.expand(co) for co in coeffs], [A, b, c], dict=True)
print("   K with V_b invariant for every a (all coefficients in a vanish):", sols)

print("\n== 4. Lie-algebra test: does V_b (or V_mu) keep ANY one-parameter subgroup of Sp(2,R)?")
# generators of sl(2,R): squeeze h, rotation r (contains rho), symmetric boost s
gens = {"squeeze diag(1,-1)": np.array([[1., 0.], [0., -1.]]),
        "rotation [[0,1],[-1,0]]": np.array([[0., 1.], [-1., 0.]]),
        "sym. boost [[0,1],[1,0]]": np.array([[0., 1.], [1., 0.]])}
K0 = np.diag([1., -1.])
def Vb_n(Kn):
    return -np.trace(Kn @ K0)**2/(2*np.trace(Kn.T @ Kn))
def Vmu_n(Kn):
    return -np.trace(Kn @ K0)**2
def expm2(X, e):
    # exact exponential of a traceless 2x2: X^2 = -det(X) * 1
    dlt = -np.linalg.det(X)
    if dlt > 0:
        s = np.sqrt(dlt); return np.cosh(e*s)*np.eye(2) + np.sinh(e*s)/s*X
    if dlt < 0:
        s = np.sqrt(-dlt); return np.cos(e*s)*np.eye(2) + np.sin(e*s)/s*X
    return np.eye(2) + e*X
rng = np.random.default_rng(12)
Ks = []
while len(Ks) < 40:
    bb, cc = rng.normal(scale=1.5, size=2)
    if 1 - bb*cc <= 0: continue
    Ks.append(np.array([[np.sqrt(1 - bb*cc)*rng.choice([-1, 1]), bb], [cc, 0.]]))
    Ks[-1][1, 1] = -Ks[-1][0, 0]
eps = 1e-6
for name, V in (("V_mu (naive)", Vmu_n), ("V_b (bounded)", Vb_n)):
    D = np.zeros((len(Ks), 3))
    for i, Kn in enumerate(Ks):
        for j, X in enumerate(gens.values()):
            Sp_, Sm_ = expm2(X, eps), expm2(X, -eps)
            D[i, j] = (V(np.linalg.inv(Sp_) @ Kn @ Sp_) - V(np.linalg.inv(Sm_) @ Kn @ Sm_))/(2*eps)
    sv = np.linalg.svd(D, compute_uv=False)
    _, _, vt = np.linalg.svd(D)
    print(f"   {name}: singular values of the 40x3 derivative matrix {np.array2string(sv, precision=3)}")
    if sv[-1] < 1e-6*sv[0]:
        print(f"      null direction (an exact continuous symmetry) = {np.round(vt[-1], 6)} in (squeeze, rotation, boost)")
    else:
        print("      no null direction: no one-parameter subgroup of Sp(2,R) leaves this potential invariant")
for name, X in gens.items():
    Sp_ = expm2(X, eps); Sm_ = expm2(X, -eps)
    der = [(Vb_n(np.linalg.inv(Sp_) @ Kn @ Sp_) - Vb_n(np.linalg.inv(Sm_) @ Kn @ Sm_))/(2*eps) for Kn in Ks]
    print(f"   V_b, generator {name}: max |dV_b/d eps| over the 40 K = {max(abs(x) for x in der):.4f}")
