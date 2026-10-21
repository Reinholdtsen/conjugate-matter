"""Which trace does p4 of the 'square-root eigenvalues' give, in #7's vacuum
frame (reference metric f = 1, dynamical g = Y)?  Also check the identities the
elementary-symmetric-polynomials page states as [T]."""
import numpy as np
from itertools import combinations
from math import comb
rng = np.random.default_rng(7)
d = 4
a = rng.standard_normal((d, d)); g = a @ a.T + d * np.eye(d)   # positive definite
f = np.eye(d)                                                   # vacuum-frame reference

def psqrt(M):  # principal square root of a matrix with positive eigenvalues
    w, V = np.linalg.eig(M); return (V @ np.diag(np.sqrt(w)) @ np.linalg.inv(V)).real

def en(vals, n): return sum(np.prod(c) for c in combinations(vals, n)) if n > 0 else 1.0

X = psqrt(np.linalg.inv(g) @ f)             # sqrt(g^-1 f)
mu = np.linalg.eigvals(X).real
print("p4(eig sqrt(g^-1 f)) =", np.sum(mu**4))
print("Tr(g^-2)             =", np.trace(np.linalg.matrix_power(np.linalg.inv(g), 2)))
print("Tr(g^2)              =", np.trace(g @ g))
Xi = psqrt(np.linalg.inv(f) @ g)            # sqrt(f^-1 g)
nu = np.linalg.eigvals(Xi).real
print("p4(eig sqrt(f^-1 g)) =", np.sum(nu**4))
# page identities
print("X^2 == g^-1 f:", np.allclose(X @ X, np.linalg.inv(g) @ f))
print("e_n(X^-1) == e_{4-n}(X)/e_4(X):", all(np.isclose(en(1/mu, n), en(mu, 4-n)/en(mu, 4)) for n in range(5)))
f2 = (lambda b: b @ b.T + d*np.eye(d))(rng.standard_normal((d, d)))
Y = psqrt(np.linalg.inv(g) @ f2); Yi = psqrt(np.linalg.inv(f2) @ g)
my = np.linalg.eigvals(Y).real; myi = np.linalg.eigvals(Yi).real
lhs = [np.sqrt(np.linalg.det(g)) * en(my, n) for n in range(5)]
rhs = [np.sqrt(np.linalg.det(f2)) * en(myi, 4 - n) for n in range(5)]
print("sqrt|g| e_n(sqrt(g^-1 f)) == sqrt|f| e_{4-n}(sqrt(f^-1 g)):", np.allclose(lhs, rhs))
# Newton: p4 = e1^4 - 4 e1^2 e2 + 2 e2^2 + 4 e1 e3 - 4 e4
e = [en(mu, n) for n in range(5)]
print("Newton p4 identity:", np.isclose(np.sum(mu**4), e[1]**4 - 4*e[1]**2*e[2] + 2*e[2]**2 + 4*e[1]*e[3] - 4*e[4]))
# linear coefficient C(3,n-1) at identity
dl = rng.standard_normal((d, d)) * 1e-7; dl = (dl + dl.T) / 2
lam = np.linalg.eigvalsh(np.eye(d) + dl)
print("e_n(1+delta) linear coeffs:", [round((en(lam, n) - comb(4, n)) / np.trace(dl), 4) for n in range(5)])
