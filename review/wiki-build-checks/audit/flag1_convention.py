#!/usr/bin/env python3
"""
Flag 1 audit, part G: convention check.
The documents fix eta = [[0,1],[1,0]] (#1 S2, verify/battery.py). Suppose instead someone reads
"eta standard" as the diagonal neutral metric eta' = diag(1_d, -1_d) with the same omega.
(1) Is (omega, eta') a para-Hermitian pair (K' = eta'^-1 omega, K'^2 = 1)?
(2) Do the omega-Lagrangian, eta'-null d-planes still form continuous families?
    Candidate family: graphs p = O x with O = Q diag(1^k, (-1)^(d-k)) Q^T, Q in O(d).
(3) Does the compatibility theorem's form H = diag(g, g^-1) survive under eta'? (If not, eta'
    is not the documents' convention; the off-diagonal eta is.)
Also (4): the joint stabilizer of (omega, eta) under eta' has dimension d^2 and its orbits
through the family have dimension k(d-k).
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(3)
for d in (2, 3, 4):
    Z = np.zeros((d, d)); I = np.eye(d)
    w = np.block([[Z, I], [-I, Z]]); ep = np.block([[I, Z], [Z, -I]])
    Kp = np.linalg.inv(ep) @ w
    ok1 = np.allclose(Kp @ Kp, np.eye(2 * d))
    worst = 0.0; dets = {}
    for k in range(d + 1):
        for t in range(100):
            Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
            O = Q @ np.diag([1.0] * k + [-1.0] * (d - k)) @ Q.T
            B = np.vstack([I, O]) / np.sqrt(2)
            worst = max(worst, np.abs(B.T @ w @ B).max(), np.abs(B.T @ ep @ B).max())
            U = B[:d] + 1j * B[d:]
            dets.setdefault(k, []).append(np.linalg.det(U) ** 2)
    # (3) H = diag(g, g^-1): does (eta'^-1 H)^2 = 1 hold?
    a = rng.standard_normal((d, d)); g = a @ a.T + d * I
    H = np.block([[g, Z], [Z, np.linalg.inv(g)]])
    J = np.linalg.inv(ep) @ H
    ok3 = np.allclose(J @ J, np.eye(2 * d))
    print(f"d={d}: K'^2 = 1: {ok1}; max |omega_L|,|eta'_L| over 100 random members of each family: {worst:.1e}")
    print("      det^2 ranges by k: " + ", ".join(
        f"k={k}: [{min(np.real(v)):+.6f},{max(np.real(v)):+.6f}]" for k, v in dets.items()))
    print(f"      (eta'^-1 diag(g,g^-1))^2 = 1 for random g: {ok3}  (False => eta' is not the papers' eta)")

# (4) sympy: joint stabilizer algebra of (omega, eta') and orbit dims through graph(O), O = diag(1^k,(-1)^(d-k))
for d in (2, 3, 4):
    Zs = sp.zeros(d); Is = sp.eye(d)
    w = sp.Matrix(sp.BlockMatrix([[Zs, Is], [-Is, Zs]])); ep = sp.Matrix(sp.BlockMatrix([[Is, Zs], [Zs, -Is]]))
    syms = sp.symbols(f'n0:{4*d*d}', real=True)
    m = sp.Matrix(2 * d, 2 * d, syms)
    cond = list(m.T * w + w * m) + list(m.T * ep + ep * m)
    A = sp.Matrix([[sp.diff(q, s) for s in syms] for q in cond])
    gens = [sp.Matrix(2 * d, 2 * d, list(v)) for v in A.nullspace()]
    dims = []
    for k in range(d + 1):
        O = sp.diag(*([1] * k + [-1] * (d - k)))
        B0 = sp.Matrix.vstack(Is, O)
        Pperp = sp.eye(2 * d) - B0 * (B0.T * B0).inv() * B0.T
        r = sp.Matrix([list(Pperp * gg * B0) for gg in gens]).rank()
        dims.append(r)
    print(f"d={d}: joint algebra of (omega, eta') has dim {len(gens)}; orbit dims through graph(diag(1^k,-1^(d-k))), k=0..d: {dims}")
