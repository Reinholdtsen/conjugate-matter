"""Flag 39 audit, part 4: of the three involutions of a pair of metrics that invert the
eigenvalues of sqrt(g^-1 f) (#8 sec 1's "X -> X^-1"), which leave the palindromic
Hassan-Rosen potential density invariant?
  exchange            (g, f) -> (f, g)
  double inversion    (g, f) -> (g^-1, f^-1)      [linear action -1 on (dg, df)]
  exchange+inversion  (g, f) -> (f^-1, g^-1)      [linear action (dg, df) -> (-df, -dg)]
Only an invariant one can be the symmetry that #8 sec 1 uses to derive the palindrome.
"""
import numpy as np
from itertools import combinations

rng = np.random.default_rng(394)
d = 4


def spd():
    a = rng.standard_normal((d, d))
    return a @ a.T + d * np.eye(d) * 0.5


def en(vals, n):
    return 1.0 if n == 0 else float(sum(np.prod(c) for c in combinations(vals, n)))


def sqrt_eigs(g, f):
    w, U = np.linalg.eigh(g)
    gm12 = U @ np.diag(w ** -0.5) @ U.T
    return np.sqrt(np.linalg.eigvalsh(gm12 @ f @ gm12))


def V(g, f, beta):
    s = sqrt_eigs(g, f)
    return np.sqrt(np.linalg.det(g)) * sum(beta[n] * en(s, n) for n in range(5))


b1, b2 = 0.7, -0.3
b0 = -4 * b1 - 3 * b2
beta = [b0, b1, b2, b1, b0]
inv = np.linalg.inv
for trial in range(3):
    g, f = spd(), spd()
    s = np.sort(sqrt_eigs(g, f))
    maps = {"exchange": (f, g), "double inversion": (inv(g), inv(f)), "exchange+inversion": (inv(f), inv(g))}
    out = []
    for name, (g2, f2) in maps.items():
        s2 = np.sort(sqrt_eigs(g2, f2))
        inverted = np.allclose(np.sort(1 / s), s2)
        out.append(f"{name}: eigs inverted {inverted}, V ratio {V(g2, f2, beta) / V(g, f, beta):.6f}")
    print(f"trial {trial}: " + "; ".join(out))
