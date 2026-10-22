#!/usr/bin/env python3
"""
Flag 1 audit, part F: an unbiased search that does not presuppose the form V + V^perp.

Minimise f(L) = |B^T omega B|^2 + |B^T eta B|^2 over d-planes L = col(B), B orthonormal
(Grassmannian; QR retraction), from random starts, d = 2, 3, 4. For every converged zero:
  - k = dim(L cap x-space), j = dim(L cap p-space); is k + j = d (L = V + W)?
  - is W = V^perp?
  - distance to the nearest of the 2^d coordinate splittings
  - det^2 with H = 1, vs (-1)^(d-k)
  - the Shilov variable W_sh = U U^T: real?
Conventions as in flag1_recompute.py (#1 S2, verify/battery.py).
"""
import itertools
import numpy as np

rng = np.random.default_rng(7)

def forms(d):
    Z = np.zeros((d, d)); I = np.eye(d)
    return np.block([[Z, I], [-I, Z]]), np.block([[Z, I], [I, Z]])

def orth(A):
    q, _ = np.linalg.qr(A)
    return q

def f_and_grad(B, w, e):
    Gw = B.T @ w @ B; Ge = B.T @ e @ B
    f = np.sum(Gw ** 2) + np.sum(Ge ** 2)
    grad = 2 * (w @ B @ Gw.T + w.T @ B @ Gw) + 2 * (e @ B @ Ge.T + e.T @ B @ Ge)
    return f, grad

def dim_intersection(B, sub):
    """dim(col(B) cap col(sub)) for orthonormal B (2d x d) and coordinate basis sub"""
    M = np.hstack([B, sub])
    s = np.linalg.svd(M, compute_uv=False)
    rank = np.sum(s > 1e-8)
    return B.shape[1] + sub.shape[1] - rank

for d in (2, 3, 4):
    w, e = forms(d)
    E = np.eye(2 * d)
    Xsp, Psp = E[:, :d], E[:, d:]
    coordP = []
    for k in range(d + 1):
        for S in itertools.combinations(range(d), k):
            cols = list(S) + [d + j for j in range(d) if j not in S]
            coordP.append(E[:, cols] @ E[:, cols].T)
    stats = {}
    n_conv = n_fail = 0
    bad_structure = 0
    for start in range(300):
        B = orth(rng.standard_normal((2 * d, d)))
        step = 0.05
        f, g = f_and_grad(B, w, e)
        for it in range(20000):
            Bn = orth(B - step * g)
            fn, gn = f_and_grad(Bn, w, e)
            if fn < f:
                B, f, g = Bn, fn, gn
                step = min(step * 1.2, 0.5)
            else:
                step *= 0.5
            if f < 1e-28 or step < 1e-14:
                break
        if f > 1e-20:
            n_fail += 1
            continue
        n_conv += 1
        k = dim_intersection(B, Xsp); j = dim_intersection(B, Psp)
        if k + j != d:
            bad_structure += 1
            continue
        # V = L cap x-space, W = L cap p-space; check W = V^perp (as subspaces of R^d)
        Pl = B @ B.T
        Vx = Pl[:d, :d]            # projector of L restricted to x-block = projector onto V
        Wp = Pl[d:, d:]            # = projector onto W
        perp_err = np.abs(Vx @ Wp).max() + np.abs(Vx + Wp - np.eye(d)).max()
        dist = min(np.linalg.norm(Pl - Pc) for Pc in coordP)
        U = B[:d] + 1j * B[d:]
        det2 = np.linalg.det(U) ** 2
        imW = np.abs((U @ U.T).imag).max()
        s = stats.setdefault(k, dict(n=0, perp=0.0, dists=[], det2=[], imW=0.0))
        s['n'] += 1; s['perp'] = max(s['perp'], perp_err); s['dists'].append(dist)
        s['det2'].append(det2); s['imW'] = max(s['imW'], imW)
    print(f"d = {d}: 300 random starts, {n_conv} converged to f < 1e-20, {n_fail} did not; "
          f"converged zeros violating L = (L cap x) + (L cap p): {bad_structure}")
    for k in sorted(stats):
        s = stats[k]; dd = np.array(s['dists']); d2 = np.array(s['det2'])
        print(f"   k = dim(L cap x) = {k}: {s['n']:3d} zeros | max err of W = V^perp: {s['perp']:.1e} | "
              f"distance to nearest coordinate splitting: min {dd.min():.3f} median {np.median(dd):.3f} "
              f"max {dd.max():.3f} | det^2 in [{d2.real.min():+.9f}, {d2.real.max():+.9f}], "
              f"max|Im det^2| {np.abs(d2.imag).max():.1e}, (-1)^(d-k) = {(-1)**(d-k):+d} | max|Im W_sh| {s['imW']:.1e}")

# Contrast: a generic Lagrangian (random U in U(d)) is not eta-null and has complex W_sh
print("contrast: random Lagrangians L = U R^d, U Haar-random unitary")
for d in (2, 3, 4):
    w, e = forms(d)
    mins = []; imWs = []
    for t in range(200):
        A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
        U, _ = np.linalg.qr(A)
        B = np.vstack([U.real, U.imag])
        assert np.abs(B.T @ w @ B).max() < 1e-12
        mins.append(np.abs(B.T @ e @ B).max())
        imWs.append(np.abs((U @ U.T).imag).max())
    print(f"   d = {d}: max|omega_L| < 1e-12 for all; max|eta_L| over samples: min {min(mins):.3f}; "
          f"max|Im W_sh|: min {min(imWs):.3f}")
