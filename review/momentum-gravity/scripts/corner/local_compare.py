"""Local (homogeneous, Jeans-swindle) model numbers at the gate ratios realized in the N-body runs
(round 3, label "corner").  Formulas copied from round 2 (clumping C3, C10; critic c5), not re-derived:
  Lambda_g(r) = [1/2 + r^2 + sqrt(1+4r^2)/2]^(-3/2)   (top eigenvalue of the Gaussian-gate operator)
  q(r) = 2r^2/(1 + 2r^2 + sqrt(1+4r^2))               (sector ratio; l-th sector Lambda_g q^l)
  <W>(r) = (1 + 2r^2)^(-3/2)                          (pair-averaged gate, Maxwellian)
  crossover eps = 1/Lambda_g (velocity-selected mode overtakes gravity's density mode)
  re-virialized condition: Lambda_0(eps, r) = Q (1 + eps <W>); as eps -> inf it needs Q < Lambda_g/<W>
  local-model validity (critic c5, from the clumping derivation verifier): eps < 1/(4.5 r^2 (1+r^2)^-2.5)
Lambda_0 is computed with the radial Nystrom operator of critic c5 (re-implemented here) to find the
re-virialized threshold at the core margin Q = 1.0966 (clumping C10).
Anchors: Lambda_0(1.2917, 10) = 2.30503422 (clumping C3), Lambda_g closed form vs Nystrom.
"""
import numpy as np

x, wq = np.polynomial.legendre.leggauss(500)
V = 4.5 * (x + 1); WV = 4.5 * wq
p0 = (2 * np.pi) ** -1.5 * np.exp(-V**2 / 2)
sq = np.sqrt(p0 * 4 * np.pi * V**2 * WV)


def W0(r):
    a = np.outer(V, V) * r**2
    e = np.exp(a - (V[:, None]**2 + V[None, :]**2) * r**2 / 2)
    s = np.where(a > 1e-8, (1 - np.exp(-2 * a)) / (2 * np.where(a > 1e-8, a, 1)), 1.0)
    return e * s


def Lam0(g, r, Wm=None):
    Wm = W0(r) if Wm is None else Wm
    return np.linalg.eigvalsh(sq[:, None] * (1 + g * Wm) * sq[None, :])[-1]


def Lg(r): return (0.5 + r**2 + np.sqrt(1 + 4 * r**2) / 2) ** -1.5
def q(r): return 2 * r**2 / (1 + 2 * r**2 + np.sqrt(1 + 4 * r**2))
def Wav(r): return (1 + 2 * r**2) ** -1.5
def valid(r): return 1 / (4.5 * r**2 * (1 + r**2) ** -2.5)


print(f"anchor: Lambda_0(1.2917, 10) = {Lam0(10, 1.2917):.8f} (clumping C3: 2.30503422); "
      f"Lambda_g(1) closed {Lg(1.0):.6f}")
Q = 1.0966
for r in (0.4, 0.55, 0.66, 1.0, 1.5, 2.0):
    Wm = W0(r)
    cap = Lg(r) / Wav(r)
    # re-virialized threshold: smallest eps with Lam0 >= Q (1 + eps <W>)
    thr = np.inf
    if cap > Q:
        lo, hi = 0.0, 1.0
        while Lam0(hi, r, Wm) < Q * (1 + hi * Wav(r)) and hi < 1e7:
            hi *= 2
        if hi < 1e7:
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if Lam0(mid, r, Wm) < Q * (1 + mid * Wav(r)):
                    lo = mid
                else:
                    hi = mid
            thr = 0.5 * (lo + hi)
    l1cap = Lg(r) * q(r) / Wav(r)
    print(f"r = {r:4.2f}: Lambda_g = {Lg(r):.4f}, q = {q(r):.4f}, <W> = {Wav(r):.4f}, crossover 1/Lambda_g = {1/Lg(r):.3f}, "
          f"re-virialized cap Lambda_g/<W> = {cap:.4f} (core margin Q = {Q}) -> re-virialized l=0 threshold eps = {thr:.4g}; "
          f"l=1 cap Lambda_g q/<W> = {l1cap:.4f}; local validity eps < {valid(r):.3f}")
