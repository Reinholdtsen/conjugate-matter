"""Flag 39 audit, part 1: the two actions of reciprocity on linear fluctuations.

(a) Moebius rho: Z -> -Z^{-1} (#11 sec 6), linearized at the fixed point Z = i*1.
    Build its real matrix on the 2n real coordinates (x, h), n = d(d+1)/2,
    by numerical differentiation (independent of the flag's sympy script),
    and print its eigenvalues and trace.
(b) Frame exchange (#8 sec 1, #11 sec 7.3): (dg, df) -> (df, dg) on Sym + Sym.
    Print its eigenvalues and trace.
A linear change of field variables preserves the trace of an involution, so if
the traces differ, no relabelling of (x, h) as (dg, df) turns one into the other.
"""
import numpy as np

rng = np.random.default_rng(39)


def sym_basis(d):
    B = []
    for i in range(d):
        for j in range(i, d):
            E = np.zeros((d, d))
            E[i, j] = E[j, i] = 1.0
            B.append(E)
    return B


def coords(M, d):
    return np.array([M[i, j] for i in range(d) for j in range(i, d)])


def mobius(Z):
    return -np.linalg.inv(Z)


for d in (1, 2, 3, 4):
    B = sym_basis(d)
    n = len(B)
    I = np.eye(d)
    Z0 = 1j * I
    W0 = mobius(Z0)
    eps = 1e-6
    cols = []
    # tangent directions: first n are x (real part), next n are h (imaginary part)
    for k in range(2 * n):
        dZ = B[k] if k < n else 1j * B[k - n]
        dW = (mobius(Z0 + eps * dZ) - mobius(Z0 - eps * dZ)) / (2 * eps)
        cols.append(np.concatenate([coords(dW.real, d), coords(dW.imag, d)]))
    L = np.array(cols).T
    ev = np.linalg.eigvals(L)
    print(f"d={d}: n={n}; -Z^-1 at Z=i equals i: {np.allclose(W0, Z0)}; "
          f"max|L + 1| = {np.max(np.abs(L + np.eye(2 * n))):.1e}; "
          f"trace(Moebius) = {np.trace(L):+.6f}; eigenvalues in {sorted(set(np.round(ev.real, 6)))}")
    P = np.block([[np.zeros((n, n)), np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    evP = np.linalg.eigvalsh(P)
    print(f"      exchange on (dg, df): trace = {np.trace(P):+.1f}; "
          f"#(+1) = {int(np.sum(evP > 0))}, #(-1) = {int(np.sum(evP < 0))}")
    # Check a random fluctuation the flag's way: first-order term is -(x + i h)
    x = rng.standard_normal((d, d)); x = (x + x.T) / 2
    h = rng.standard_normal((d, d)); h = (h + h.T) / 2
    e2 = 1e-5
    first = (mobius(Z0 + e2 * (x + 1j * h)) - mobius(Z0 - e2 * (x + 1j * h))) / (2 * e2)
    print(f"      random (x, h): max|first-order term + (x + i h)| = {np.max(np.abs(first + x + 1j * h)):.1e}")
