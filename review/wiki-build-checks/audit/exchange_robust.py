"""Robustness of the exchange check: U(g,f) - U(f,g) for palindromic vs generic beta, several draws."""
import numpy as np
from math import comb
rng = np.random.default_rng(7)
def U_num(beta, g, f):
    ev = np.linalg.eigvals(np.linalg.solve(g, f)).astype(complex)
    en = np.poly(-np.sqrt(ev))
    return np.sqrt(abs(np.linalg.det(g))) * np.dot(beta, en)
for k in range(5):
    A = rng.standard_normal((4, 4)); G = A @ A.T + 0.5 * np.eye(4)
    B = rng.standard_normal((4, 4)); F = B @ B.T + 0.5 * np.eye(4)
    p = rng.standard_normal(3); bp = np.array([p[0], p[1], p[2], p[1], p[0]])
    bg = rng.standard_normal(5)
    u1, u2 = U_num(bp, G, F), U_num(bp, F, G)
    print(f"draw {k}: pal U(g,f)={u1.real:+.12f} U(f,g)={u2.real:+.12f} rel.diff={abs(u1-u2)/abs(u1):.1e} | "
          f"generic rel.diff={abs(U_num(bg,G,F)-U_num(bg,F,G))/abs(U_num(bg,G,F)):.1e}")
