#!/usr/bin/env python3
"""
Flag 1 audit -- independent recomputation (not using review/wiki-build-checks/).

Source claim (notes/debt1a-geometric-core.md SB line 27; echoed #11 S5, #9 S3, #1 v0.3):
  under strict P2 (omega AND eta rigid) the polarizations that are omega-Lagrangian AND
  eta-null are "discrete -- the 2^d coordinate-type splittings, GL(d)-rigid", hence no
  Lagrangian Grassmannian, no Maslov circle, no tau.

Conventions are the documents' own (#1 S2, verify/battery.py):
  omega = [[0,1],[-1,0]], eta = [[0,1],[1,0]] in the (x,p) block basis; I = omega^-1 H;
  tau = f * arg det^2 on U(d)/O(d) (#1 S2), z = x + i p the I-complex coordinate at H = 1.

Parts
  A  exact (sympy): full solution set at d = 2 on all six Plucker charts of Gr(2,4)
  B  exact (sympy): Zariski tangent dimension of the solution variety at each of the 2^d
     coordinate splittings, d = 2,3,4, vs k(d-k)
  C  exact (sympy): joint symmetry algebra {m : m^T w + w m = 0, m^T eta + eta m = 0}
     (dimension), and the orbit dimension of that group through each coordinate splitting
  D  numeric: explicit family V + V^perp for random V; omega, eta Gram matrices; det^2
     with H = 1 and with random H = diag(g, g^-1); Shilov variable W = U U^T real?
  E  numeric: the Maslov-generator loop leaves the compatible set (eta|_L != 0)
"""
import itertools
import numpy as np
import sympy as sp

np.set_printoptions(precision=4, suppress=True)

def forms(d, mod=sp):
    if mod is sp:
        Z = sp.zeros(d); I = sp.eye(d)
        w = sp.Matrix(sp.BlockMatrix([[Z, I], [-I, Z]]))
        e = sp.Matrix(sp.BlockMatrix([[Z, I], [I, Z]]))
    else:
        Z = np.zeros((d, d)); I = np.eye(d)
        w = np.block([[Z, I], [-I, Z]]); e = np.block([[Z, I], [I, Z]])
    return w, e

def coord_splitting(d, S, mod=sp):
    """basis (2d x d) of x_S + p_{S^c}: e_{x_i} for i in S, e_{p_j} for j not in S"""
    cols = [i for i in S] + [d + j for j in range(d) if j not in S]
    if mod is sp:
        E = sp.eye(2 * d)
        return sp.Matrix.hstack(*[E[:, c] for c in cols]), cols
    E = np.eye(2 * d)
    return E[:, cols], cols

# ---------------------------------------------------------------- Part A
print("=" * 78)
print("A. d = 2, exact: all 2-planes L in R^4 with omega|_L = 0 and eta|_L = 0")
print("   (six Plucker charts: pivots P, L = {v : v_P free, v_{P^c} = M v_P})")
d = 2
w, e = forms(d)
a, b, c, dd = sp.symbols('a b c dd', real=True)
names = ['x1', 'x2', 'p1', 'p2']
total_solutions = []
for P in itertools.combinations(range(4), 2):
    Q = [i for i in range(4) if i not in P]
    B = sp.zeros(4, 2)
    for col, piv in enumerate(P):
        B[piv, col] = 1
    M = sp.Matrix([[a, b], [c, dd]])
    for r, q in enumerate(Q):
        for col in range(2):
            B[q, col] = M[r, col]
    Gw = sp.simplify(B.T * w * B); Ge = sp.simplify(B.T * e * B)
    eqs = [Gw[0, 1], Ge[0, 0], Ge[0, 1], Ge[1, 1]]
    sols = sp.solve(eqs, [a, b, c, dd], dict=True)
    print(f"  chart pivots {[names[i] for i in P]}: equations {eqs}")
    for s in sols:
        free = [v for v in (a, b, c, dd) if v not in s]
        Bs = B.subs(s)
        print(f"     solution {s}  free parameters: {free}  -> dimension {len(free)}")
        total_solutions.append((P, s, free))
    if not sols:
        print("     no solution in this chart")
print("  => the solution set in Gr(2,4) has components of dimension",
      sorted(set(len(f) for _, _, f in total_solutions)))

# Identify the one-parameter family explicitly as V(theta) + V(theta)^perp
th = sp.symbols('theta', real=True)
v = sp.Matrix([sp.cos(th), sp.sin(th)]); vp = sp.Matrix([-sp.sin(th), sp.cos(th)])
Bfam = sp.Matrix.vstack(sp.Matrix.hstack(v, sp.zeros(2, 1)), sp.Matrix.hstack(sp.zeros(2, 1), vp))
print("  family L(theta) = span{(v,0),(0,v_perp)}, v = (cos t, sin t):")
print("     B^T omega B =", sp.simplify(Bfam.T * w * Bfam).tolist(),
      "  B^T eta B =", sp.simplify(Bfam.T * e * Bfam).tolist())
# L(0) = x1 + p2, L(pi/2) = x2 + p1: the two mixed coordinate splittings lie on one circle
print("     L(0) basis cols:", Bfam.subs(th, 0).T.tolist(), " L(pi/2):", Bfam.subs(th, sp.pi / 2).T.tolist())

# ---------------------------------------------------------------- Part B
print("=" * 78)
print("B. Zariski tangent dimension of {omega|_L = 0, eta|_L = 0} at each coordinate splitting")
print("   chart: L(M) = col(B0 + C0 M), C0 = basis of the opposite splitting; d^2 unknowns")
for d in (2, 3, 4):
    w, e = forms(d)
    syms = sp.symbols(f'm0:{d*d}', real=True)
    M = sp.Matrix(d, d, syms)
    by_k = {}
    for k in range(d + 1):
        for S in itertools.combinations(range(d), k):
            B0, _ = coord_splitting(d, S)
            C0, _ = coord_splitting(d, [j for j in range(d) if j not in S])
            B = B0 + C0 * M
            Gw = (B.T * w * B).expand(); Ge = (B.T * e * B).expand()
            eqs = [Gw[i, j] for i in range(d) for j in range(i + 1, d)] + \
                  [Ge[i, j] for i in range(d) for j in range(i, d)]
            # base point is a solution
            assert all(sp.simplify(q.subs({s: 0 for s in syms})) == 0 for q in eqs)
            Jac = sp.Matrix([[sp.diff(q, s) for s in syms] for q in eqs]).subs({s: 0 for s in syms})
            tdim = d * d - Jac.rank()
            by_k.setdefault(k, set()).add(tdim)
    line = ", ".join(f"k={k}: tangent dim {sorted(v)} (k(d-k) = {k*(d-k)}, #splittings {sp.binomial(d,k)})"
                     for k, v in by_k.items())
    print(f"  d = {d}: 2^d = {2**d} coordinate splittings; {line}")

# ---------------------------------------------------------------- Part C
print("=" * 78)
print("C. joint symmetry algebra of (omega, eta) and its orbits through the coordinate splittings")
for d in (2, 3, 4):
    w, e = forms(d)
    syms = sp.symbols(f'n0:{4*d*d}', real=True)
    m = sp.Matrix(2 * d, 2 * d, syms)
    cond = list((m.T * w + w * m)) + list((m.T * e + e * m))
    A = sp.Matrix([[sp.diff(q, s) for s in syms] for q in cond])
    ker = A.nullspace()
    gens = [sp.Matrix(2 * d, 2 * d, list(kv)) for kv in ker]
    # check block structure diag(a, -a^T)
    blockdiag = all(g[:d, d:] == sp.zeros(d) and g[d:, :d] == sp.zeros(d) and
                    g[d:, d:] == -g[:d, :d].T for g in gens)
    dims = {}
    for k in range(d + 1):
        for S in itertools.combinations(range(d), k):
            B0, cols = coord_splitting(d, S)
            # orbit dimension = rank of {g B0 mod span(B0)}: project out the B0 columns
            Pperp = sp.eye(2 * d) - B0 * (B0.T * B0).inv() * B0.T
            vecs = [list(Pperp * g * B0) for g in gens]
            r = sp.Matrix(vecs).rank() if vecs else 0
            dims.setdefault(k, set()).add(r)
    print(f"  d = {d}: dim of joint algebra = {len(gens)} (dim gl(d) = {d*d}); "
          f"all generators diag(a, -a^T): {blockdiag}")
    print("         orbit dimension through x_S + p_(S^c), by k = |S|: " +
          ", ".join(f"k={k}: {sorted(v)}" for k, v in dims.items()))

# ---------------------------------------------------------------- Part D
print("=" * 78)
print("D. numeric: L = V + V^perp for random V (dim k); Gram matrices, det^2, Shilov variable W")
rng = np.random.default_rng(20261021)

def orth(A):
    q, _ = np.linalg.qr(A)
    return q

def det2(B, g=None):
    """det(U)^2 for the Lagrangian col(B), complex structure I = omega^-1 H,
    H = diag(g, g^-1) (H = 1 if g is None). Map by symplectic S = diag(g^1/2, g^-1/2),
    which takes H to 1, then U = Bx + i Bp from an orthonormal basis."""
    d = B.shape[0] // 2
    if g is not None:
        ev, P = np.linalg.eigh(g)
        gh = P @ np.diag(np.sqrt(ev)) @ P.T; ghi = P @ np.diag(1 / np.sqrt(ev)) @ P.T
        S = np.block([[gh, np.zeros((d, d))], [np.zeros((d, d)), ghi]])
        B = S @ B
    Q = orth(B)
    U = Q[:d] + 1j * Q[d:]
    return np.linalg.det(U) ** 2, U

for d in (2, 3, 4):
    w, e = forms(d, np)
    for k in range(d + 1):
        worst_w = worst_e = worst_unit = 0.0
        d2s, d2g, imW = [], [], []
        for trial in range(200):
            Qd = orth(rng.standard_normal((d, d)))
            V, Vp = Qd[:, :k], Qd[:, k:]
            B = np.block([[V, np.zeros((d, d - k))], [np.zeros((d, k)), Vp]])
            worst_w = max(worst_w, np.abs(B.T @ w @ B).max())
            worst_e = max(worst_e, np.abs(B.T @ e @ B).max())
            val, U = det2(B)
            worst_unit = max(worst_unit, np.abs(U.conj().T @ U - np.eye(d)).max())
            d2s.append(val)
            Wsh = U @ U.T
            imW.append(np.abs(Wsh.imag).max())
            a_ = rng.standard_normal((d, d)); g = a_ @ a_.T + d * np.eye(d)
            d2g.append(det2(B, g)[0])
        d2s = np.array(d2s); d2g = np.array(d2g)
        print(f"  d={d} k={k}: max|omega_L|={worst_w:.1e} max|eta_L|={worst_e:.1e} "
              f"U unitary err={worst_unit:.1e} | det^2 (H=1): min {d2s.real.min():+.12f} "
              f"max {d2s.real.max():+.12f} max|Im| {np.abs(d2s.imag).max():.1e} "
              f"| det^2 (random g): spread {np.ptp(d2g.real):.1e}, mean {d2g.real.mean():+.6f} "
              f"| (-1)^(d-k) = {(-1)**(d-k):+d} | max|Im W| = {max(imW):.1e}")

# How far are random family members from every coordinate splitting? (non-coordinate points)
print("  distance (projector norm) from random family members to the nearest of the 2^d coordinate splittings:")
for d in (2, 3, 4):
    coordP = []
    for k in range(d + 1):
        for S in itertools.combinations(range(d), k):
            B0, _ = coord_splitting(d, S, np)
            coordP.append(B0 @ B0.T)
    for k in range(1, d):
        dmin = []
        for trial in range(200):
            Qd = orth(rng.standard_normal((d, d)))
            B = np.block([[Qd[:, :k], np.zeros((d, d - k))], [np.zeros((d, k)), Qd[:, k:]]])
            Pm = B @ B.T
            dmin.append(min(np.linalg.norm(Pm - Pc) for Pc in coordP))
        print(f"    d={d} k={k}: min over 200 samples of the nearest-coordinate distance = {min(dmin):.3f}, "
              f"median = {np.median(dmin):.3f}")

# ---------------------------------------------------------------- Part E
print("=" * 78)
print("E. the Maslov generator loop L(t) = span{cos t e_x1 + sin t e_p1, e_x2..e_xd}, t in [0, pi]")
for d in (1, 2, 4):
    w, e = forms(d, np)
    ts = np.linspace(0, np.pi, 9)
    out = []
    for t in ts:
        cols = [np.cos(t) * np.eye(2 * d)[:, 0] + np.sin(t) * np.eye(2 * d)[:, d]] + \
               [np.eye(2 * d)[:, i] for i in range(1, d)]
        B = np.array(cols).T
        val, _ = det2(B)
        out.append((t, np.angle(val), np.abs(B.T @ w @ B).max(), np.abs(B.T @ e @ B).max()))
    print(f"  d={d}: t/pi, arg det^2/pi, max|omega_L|, max|eta_L|:")
    for t, ph, ow, oe in out:
        print(f"     {t/np.pi:.3f}  {ph/np.pi:+.3f}  {ow:.1e}  {oe:.3f}")

# ---------------------------------------------------------------- summary numbers
print("=" * 78)
print("Counts: d, 2^d (coordinate splittings), d+1 (components Gr(k,d)), dims k(d-k), "
      "max dim, dim Lambda(d) = d(d+1)/2")
for d in range(1, 6):
    dims = [k * (d - k) for k in range(d + 1)]
    print(f"  d={d}: 2^d={2**d:2d}  components={d+1}  dims={dims}  max={max(dims)}  dim Lambda={d*(d+1)//2}")
