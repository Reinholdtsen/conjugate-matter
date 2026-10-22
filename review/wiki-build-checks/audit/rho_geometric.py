"""Audit of flag 39 (independent of review/wiki-build-checks/rho_parity.py).

Geometric action of Born reciprocity rho: (x,p) -> (p,-x) on the program's fields,
derived from the symplectic matrix rather than from the Moebius formula.

Conventions taken from the sources:
  omega = [[0,1],[-1,0]] (blocks)            HANDOFF App. A; toy note s1
  H_Z = [[Y+XY^-1X, XY^-1],[Y^-1X, Y^-1]]    #5 sC, #11 s6
  J0  = [[0,1],[1,0]] (blocks)               #7 s2 (polarization at the vacuum)
  eta = [[0,1],[1,0]], K = eta^-1 omega      HANDOFF App. A; #11 s5
  Sp acts by H -> S^T H S, J -> S^-1 J S     toy note s2
  rho as a matrix: v=(x,p) -> (p,-x), i.e. R = [[0,1],[-1,0]] (blocks)
"""
import itertools
import numpy as np
import sympy as sp

def blocks(A, B, C, D):
    return sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]))

def setup(d):
    I_d, Z_d = sp.eye(d), sp.zeros(d)
    w = blocks(Z_d, I_d, -I_d, Z_d)
    R = blocks(Z_d, I_d, -I_d, Z_d)
    return w, R

def H_of(X, Y):
    Yi = Y.inv()
    return blocks(Y + X*Yi*X, X*Yi, Yi*X, Yi)

def Z_from_H(H, d):
    H22 = H[d:, d:]; H21 = H[d:, :d]
    Yp = H22.inv()
    Xp = Yp*H21
    return Xp, Yp

def sym_basis(d):
    out = []
    for i in range(d):
        for j in range(i, d):
            E = sp.zeros(d); E[i, j] = 1; E[j, i] = 1
            out.append(E)
    return out

print("== A. rho acting on H by congruence induces Z -> -Z^-1 (no Moebius formula assumed)")
rng = np.random.default_rng(39)
for d in (1, 2, 3, 4):
    w, R = setup(d)
    worst = 0.0
    for _ in range(5):
        # random rational symmetric X and positive-definite Y, exact arithmetic
        A = sp.Matrix(d, d, lambda i, j: sp.Rational(int(rng.integers(-9, 10)), 7))
        X = (A + A.T)/2
        B = sp.Matrix(d, d, lambda i, j: sp.Rational(int(rng.integers(-9, 10)), 5))
        Y = B*B.T + sp.eye(d)
        H = H_of(X, Y)
        assert (H.T*w*H - w).applyfunc(sp.simplify) == sp.zeros(2*d)   # H symplectic
        Hp = R.T*H*R
        Hp2 = R*H*R.T                     # the other (passive) convention
        Xp, Yp = Z_from_H(Hp, d)
        Zp = Xp + sp.I*Yp
        target = -(X + sp.I*Y).inv()
        diff = (Zp - target).applyfunc(sp.nsimplify)
        same_conv = (Hp - Hp2) == sp.zeros(2*d)
        reconstr = (H_of(Xp, Yp) - Hp) == sp.zeros(2*d)
        worst = max(worst, max(abs(complex(e)) for e in diff))
    print(f"d={d}: max|Z' - (-Z^-1)| over 5 exact random Z = {worst}; "
          f"R^T H R == R H R^T: {same_conv}; H' is again of Siegel form H_Z': {reconstr}")

print("\n== B. Exact Jacobian of the induced map at the fixed point Z = i*1 (real coords: entries of x, h)")
eps = sp.symbols("eps")
for d in (1, 2, 3, 4):
    w, R = setup(d)
    basis = sym_basis(d)
    n = len(basis)
    cols = []
    for kind in ("x", "h"):
        for E in basis:
            X = eps*E if kind == "x" else sp.zeros(d)
            Y = sp.eye(d) + (eps*E if kind == "h" else sp.zeros(d))
            Hp = R.T*H_of(X, Y)*R
            Xp, Yp = Z_from_H(Hp, d)
            dX = Xp.diff(eps).subs(eps, 0)
            dY = Yp.diff(eps).subs(eps, 0)
            col = [sp.simplify(dX[i, j]) for i in range(d) for j in range(i, d)] + \
                  [sp.simplify(dY[i, j]) for i in range(d) for j in range(i, d)]
            cols.append(col)
    Jac = sp.Matrix(cols).T
    ev = Jac.eigenvals()
    print(f"d={d}: tangent dim {2*n}; Jacobian == -identity: {Jac == -sp.eye(2*n)}; eigenvalues {dict(ev)}")

print("\n== C. On the slice X = 0 the induced map is Y -> Y^-1 (scale-factor duality); linear part")
for d in (1, 2, 3):
    w, R = setup(d)
    hs = sp.symbols(f"h0:{d*(d+1)//2}", real=True)
    h = sp.zeros(d); k = 0
    for i in range(d):
        for j in range(i, d):
            h[i, j] = h[j, i] = hs[k]; k += 1
    Y = sp.eye(d) + eps*h
    Xp, Yp = Z_from_H(R.T*H_of(sp.zeros(d), Y)*R, d)
    is_inv = (Yp - Y.inv()).applyfunc(sp.simplify) == sp.zeros(d)
    lin = Yp.diff(eps).subs(eps, 0).applyfunc(sp.simplify)
    print(f"d={d}: X' = 0: {Xp.applyfunc(sp.simplify) == sp.zeros(d)}; Y' = Y^-1: {is_inv}; "
          f"linear part of Y' is -h: {lin == -h}")

print("\n== D. rho does not fix the vacuum polarization: J0 -> -J0, K0 -> -K0")
for d in (1, 2, 3, 4):
    w, R = setup(d)
    I_d, Z_d = sp.eye(d), sp.zeros(d)
    J0 = blocks(Z_d, I_d, I_d, Z_d)
    eta = blocks(Z_d, I_d, I_d, Z_d)
    K0 = eta.inv()*w
    I0 = w.inv()*sp.eye(2*d)          # I = w^-1 H at H = 1 (Z = i)
    print(f"d={d}: J0^2=1 {J0**2 == sp.eye(2*d)}; J0 antisymplectic {J0.T*w*J0 == -w}; "
          f"{{J0,I0}}=0 {J0*I0 + I0*J0 == sp.zeros(2*d)}; R^-1 J0 R = -J0: {R.inv()*J0*R == -J0}; "
          f"R^-1 K0 R = -K0: {R.inv()*K0*R == -K0}; R fixes I0: {R.inv()*I0*R == I0}")

print("\n== E. Twisted element rho~ = (J -> -J) o rho fixes (Z=i, J0). Its action on the J tangent space")
for d in (1, 2, 3, 4):
    w, R = setup(d)
    I_d, Z_d = sp.eye(d), sp.zeros(d)
    J0 = blocks(Z_d, I_d, I_d, Z_d)
    I0 = w.inv()
    N = 2*d
    syms = sp.symbols(f"q0:{N*N}")
    dJ = sp.Matrix(N, N, syms)
    invol = list(J0*dJ + dJ*J0)                    # tangent to J^2 = 1
    antis = list(dJ.T*w*J0 + J0.T*w*dJ)            # tangent to J^T w J = -w
    compat = list(I0*dJ + dJ*I0)                   # stays anticommuting with I at Z = i
    def tangent(eqs):
        M = sp.Matrix([[sp.diff(e, s) for s in syms] for e in eqs])
        return M.nullspace()
    full = tangent(invol + antis)
    comp = tangent(invol + antis + compat)
    def action_eigs(basis):
        Bm = sp.Matrix.hstack(*basis)
        imgs = []
        for v in basis:
            M = sp.Matrix(N, N, list(v))
            Mp = -(R.inv()*M*R)
            imgs.append(sp.Matrix(list(Mp)))
        Im = sp.Matrix.hstack(*imgs)
        coeff = (Bm.T*Bm).inv()*Bm.T*Im          # express images in the basis
        closed = (Bm*coeff - Im) == sp.zeros(*Im.shape)
        return closed, dict(coeff.eigenvals())
    cf, ef = action_eigs(full)
    cc, ec = action_eigs(comp)
    print(f"d={d}: anti-symplectic involutions: tangent dim {len(full)} (expect d(d+1)={d*(d+1)}), "
          f"twisted-rho eigenvalues {ef} (subspace closed: {cf})")
    print(f"      compatible with I (Lambda(d) moduli): dim {len(comp)} (expect d(d+1)/2={d*(d+1)//2}), "
          f"twisted-rho eigenvalues {ec} (closed: {cc})")
