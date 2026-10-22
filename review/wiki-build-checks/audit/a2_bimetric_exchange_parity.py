"""Flag 39 audit, part 2: parity of the bimetric mass eigenstates under the frame exchange.

Euclidean d = 4 matrix model of the Hassan-Rosen potential density (the reading of
#8 sec 1's S_n(g,f)):   V(g, f) = sqrt(det g) * sum_n beta_n e_n(sqrt(g^-1 f)).
Anchors independent of the program's papers:
  * e_n(lam^-1) = e_{4-n}(lam)/e_4(lam)  (textbook identity of elementary symmetric
    polynomials), which gives the exchange identity S_n(g,f) = S_{4-n}(f,g);
  * an involution P that commutes with a symmetric matrix M lets M be diagonalised
    in P's +1 and -1 eigenspaces (linear algebra).
Checks:
  1. exchange identity for random SPD g, f;
  2. with a palindromic, T = 0 beta set: V(g,f) = V(f,g); a non-palindromic set fails;
  3. V(g, g) = 0 for every g (the diagonal direction g = f is exactly flat);
  4. the Hessian M of V at g = f = 1 on (h_g, h_f) commutes with the exchange P,
     annihilates every (h, h), and its non-null eigenvectors are all of the form (u, -u);
     on u = h_f - h_g it is c [Tr u^2 - (Tr u)^2] (Fierz-Pauli structure), c = (b1+b2)/4;
  5. with equal kinetic operators (equal Planck masses), the massless modes are the
     exchange-even (h, h) and the massive ones the exchange-odd (u, -u);
  6. contrast: the double inversion (g, f) -> (g^-1, f^-1) also inverts the eigenvalues of
     sqrt(g^-1 f), but it does not leave V invariant, and it acts as -1 on (h_g, h_f).
"""
import numpy as np
from math import comb
from itertools import combinations

rng = np.random.default_rng(3939)
d = 4


def spd():
    a = rng.standard_normal((d, d))
    return a @ a.T + d * np.eye(d) * 0.5


def symrand(s=1.0):
    m = rng.standard_normal((d, d)) * s
    return (m + m.T) / 2


def en(vals, n):
    return 1.0 if n == 0 else float(sum(np.prod(c) for c in combinations(vals, n)))


def sqrt_eigs(g, f):
    # eigenvalues of sqrt(g^-1 f) = sqrt of eigenvalues of g^-1/2 f g^-1/2 (SPD)
    w, U = np.linalg.eigh(g)
    gm12 = U @ np.diag(w ** -0.5) @ U.T
    lam = np.linalg.eigvalsh(gm12 @ f @ gm12)
    return np.sqrt(lam)


def V(g, f, beta):
    s = sqrt_eigs(g, f)
    return np.sqrt(np.linalg.det(g)) * sum(beta[n] * en(s, n) for n in range(5))


# 1. exchange identity
g, f = spd(), spd()
lhs = [np.sqrt(np.linalg.det(g)) * en(sqrt_eigs(g, f), n) for n in range(5)]
rhs = [np.sqrt(np.linalg.det(f)) * en(sqrt_eigs(f, g), 4 - n) for n in range(5)]
print("1. exchange identity sqrt(det g) e_n(sqrt(g^-1 f)) = sqrt(det f) e_{4-n}(sqrt(f^-1 g)):",
      np.allclose(lhs, rhs, rtol=1e-10), f"max rel dev {max(abs(a - b) / abs(a) for a, b in zip(lhs, rhs)):.1e}")

# 2. palindromic, T = 0 betas
b1, b2 = 0.7, -0.3
b0 = -4 * b1 - 3 * b2
beta = [b0, b1, b2, b1, b0]
T = sum(beta[n] * comb(3, n - 1) for n in range(1, 5))
V1 = sum(beta[n] * comb(4, n) for n in range(5))
print(f"2. beta = {[round(b, 4) for b in beta]}: T = {T:+.2e}, V(1) = {V1:+.2e}")
g, f = spd(), spd()
print(f"   V(g,f) = {V(g, f, beta):+.10f}, V(f,g) = {V(f, g, beta):+.10f}  (palindromic)")
beta_np = [0.3, 0.7, -0.3, 0.1, -0.2]
print(f"   V(g,f) = {V(g, f, beta_np):+.10f}, V(f,g) = {V(f, g, beta_np):+.10f}  (non-palindromic {beta_np})")

# 3. diagonal flatness
vals = [V(gg, gg, beta) for gg in (spd(), spd(), spd())]
print(f"3. V(g, g) for three random g: {[f'{v:+.1e}' for v in vals]}")

# 4. Hessian at g = f = 1 on 20 coordinates (10 for h_g, 10 for h_f)
basis = []
for i in range(d):
    for j in range(i, d):
        E = np.zeros((d, d)); E[i, j] = E[j, i] = 1.0
        basis.append(E)
n = len(basis)


def mat(v):
    return sum(c * E for c, E in zip(v, basis))


def F(v):
    return V(np.eye(d) + mat(v[:n]), np.eye(d) + mat(v[n:]), beta)


eps = 1e-4
M = np.zeros((2 * n, 2 * n))
for a in range(2 * n):
    for b in range(a, 2 * n):
        ea = np.zeros(2 * n); ea[a] = eps
        eb = np.zeros(2 * n); eb[b] = eps
        val = (F(ea + eb) - F(ea - eb) - F(-ea + eb) + F(-ea - eb)) / (4 * eps * eps)
        M[a, b] = M[b, a] = val
P = np.block([[np.zeros((n, n)), np.eye(n)], [np.eye(n), np.zeros((n, n))]])
print(f"4. Hessian: max|PMP - M| = {np.max(np.abs(P @ M @ P - M)):.1e}; scale max|M| = {np.max(np.abs(M)):.3f}")
diag_vecs = np.vstack([np.concatenate([e, e]) for e in np.eye(n)]).T
print(f"   max|M (h, h)| over the 10 basis directions h: {np.max(np.abs(M @ diag_vecs)):.1e}")
w, U = np.linalg.eigh(M)
nonnull = np.abs(w) > 1e-5 * np.max(np.abs(w))
odd_resid = max(np.linalg.norm(U[:n, k] + U[n:, k]) for k in np.where(nonnull)[0])
print(f"   non-null eigenvalues: {int(nonnull.sum())}; each eigenvector has form (u, -u): "
      f"max|u_g + u_f| = {odd_resid:.1e}")
# Fierz-Pauli structure on u = h_f - h_g, compared with c [Tr u^2 - (Tr u)^2]
c_pred = (b1 + b2) / 4
devs = []
for _ in range(5):
    hg, hf = symrand(), symrand()
    v = np.concatenate([coords := np.array([hg[i, j] for i in range(d) for j in range(i, d)]),
                        np.array([hf[i, j] for i in range(d) for j in range(i, d)])])
    quad = 0.5 * v @ M @ v
    u = hf - hg
    fp = c_pred * (np.trace(u @ u) - np.trace(u) ** 2)
    devs.append(abs(quad - fp) / abs(fp))
print(f"   quadratic part vs ((b1+b2)/4)[Tr u^2 - (Tr u)^2], u = h_f - h_g: max rel dev {max(devs):.1e} "
      f"(5 random pairs; c = {c_pred:.4f})")

# 5. equal kinetic operators: K(h_g) + K(h_f) = K(s) + K(a) for s, a = (h_g +- h_f)/sqrt2,
#    so the mass matrix is M itself up to a common factor; its null space is the even sector
even_dim = n - np.linalg.matrix_rank(np.hstack([M @ diag_vecs]), tol=1e-6)
print(f"5. massless (null) directions of M: {int((~nonnull).sum())}; all 10 even directions (h, h) are null "
      f"(rank of M on them = {np.linalg.matrix_rank(M @ diag_vecs, tol=1e-6)}); "
      f"massive directions: {int(nonnull.sum())}, all exchange-odd")

# 6. double inversion contrast
g, f = spd(), spd()
s = sqrt_eigs(g, f)
s_inv = sqrt_eigs(np.linalg.inv(g), np.linalg.inv(f))
print(f"6. double inversion: eigenvalues of sqrt(g^-1 f) inverted: "
      f"{np.allclose(np.sort(1 / s), np.sort(s_inv))}; "
      f"V(g,f) = {V(g, f, beta):+.6f}, V(g^-1,f^-1) = {V(np.linalg.inv(g), np.linalg.inv(f), beta):+.6f}, "
      f"V(g,f)/sqrt(det g det f) = {V(g, f, beta) / np.sqrt(np.linalg.det(g) * np.linalg.det(f)):+.6f}")
h = symrand(1e-6)
lin = (np.linalg.inv(np.eye(d) + h) - np.eye(d))
print(f"   linear action of g -> g^-1 at g = 1: max|d(g^-1) + h|/|h| = "
      f"{np.max(np.abs(lin + h)) / np.max(np.abs(h)):.1e}  (so dg -> -dg, df -> -df: both h_g + h_f and h_g - h_f odd)")
