"""Audit of flag 12, part 4 (steelman): could F2's 'bounded variant' be an H-covariant normalization,
V_c = -[Tr(K K_ref)]^2 / (2 Tr(H^-1 K^T H K)), under which the squeeze WOULD be exact?
F2 quotes for its variant: boost family rises from -1 to -0.5 (bounded). Test V_c on that family
H = S^T S, K = S^-1 K_ref S, S = [[cosh t, sinh t], [sinh t, cosh t]], and its squeeze invariance."""
import numpy as np
import sympy as sp

K0 = np.diag([1., -1.])
def Vfrob(H, K): return -np.trace(K @ K0)**2/(2*np.trace(K.T @ K))
def Vcov(H, K): return -np.trace(K @ K0)**2/(2*np.trace(np.linalg.inv(H) @ K.T @ H @ K))
print("boost family: t, V_frobenius (documents' V_b), V_covariant")
for t in (0.0, 1.0, 2.0, 4.0):
    S = np.array([[np.cosh(t), np.sinh(t)], [np.sinh(t), np.cosh(t)]])
    H = S.T @ S; K = np.linalg.inv(S) @ K0 @ S
    print(f"  t = {t}: {Vfrob(H, K):+.4f}  {Vcov(H, K):+.6e}")
a = sp.symbols('a', positive=True); A, b, c, p, q, r = sp.symbols('A b c p q r', real=True)
K = sp.Matrix([[A, b], [c, -A]]); H = sp.Matrix([[p, q], [q, r]]); S = sp.diag(a, 1/a); Kr = sp.diag(1, -1)
Vc = lambda H, K: -((K*Kr).trace())**2/(2*(H.inv()*K.T*H*K).trace())
print("V_cov squeeze-invariant (H -> S^T H S, K -> S^-1 K S):", sp.simplify(Vc(S.T*H*S, S.inv()*K*S) - Vc(H, K)) == 0)
