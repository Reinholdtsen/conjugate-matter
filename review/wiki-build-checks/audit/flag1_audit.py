"""Audit of wiki-build flag 1: are the omega-Lagrangian, eta-null polarizations of R^{2d} discrete
("the 2^d coordinate-type splittings, GL(d)-rigid", notes/debt1a-geometric-core.md SB)?

Conventions are the lab notebook's (#1 S2): (x, p) block basis, omega = [[0,1],[-1,0]], eta = [[0,1],[1,0]],
d = 4 for the physical case. Independent anchors (textbook, not the paper): dim Gr(k,d) = k(d-k);
dim Lambda(d) = d(d+1)/2; Arnold's det^2 : U(d)/O(d) -> U(1) generates pi_1(Lambda(d)) = Z.
"""
import itertools
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261021)


def forms(d):
    Z, I = np.zeros((d, d)), np.eye(d)
    return np.block([[Z, I], [-I, Z]]), np.block([[Z, I], [I, Z]])


def onb(M):
    q, _ = np.linalg.qr(M)
    return q


def complement(M):
    # orthonormal basis of the orthogonal complement of col(M) in R^{2d}
    u, s, vt = np.linalg.svd(M, full_matrices=True)
    r = int((s > 1e-10).sum())
    return u[:, r:]


def split_L(V, d):
    """L = V (+) V^perp with V (d x k, orthonormal) placed in x and V^perp in p."""
    k = V.shape[1]
    Vp = complement(V) if k < d else np.zeros((d, 0))
    top = np.hstack([V, np.zeros((d, d - k))])
    bot = np.hstack([np.zeros((d, k)), Vp])
    return np.vstack([top, bot])


def det2(M, d):
    M = onb(M)
    U = M[:d, :] + 1j * M[d:, :]
    return np.linalg.det(U) ** 2


print("=== A. The two conditions reduce to A^T B = 0 (symbolic, d = 3) ===")
d = 3
A = sp.Matrix(d, d, lambda i, j: sp.Symbol(f"a{i}{j}"))
B = sp.Matrix(d, d, lambda i, j: sp.Symbol(f"b{i}{j}"))
Ms = A.col_join(B)
om_s = sp.Matrix(sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [-sp.eye(d), sp.zeros(d)]]))
et_s = sp.Matrix(sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [sp.eye(d), sp.zeros(d)]]))
Fw, Fe = Ms.T * om_s * Ms, Ms.T * et_s * Ms
print("M^T omega M - (A^T B - B^T A) == 0:", sp.simplify(Fw - (A.T * B - B.T * A)) == sp.zeros(d))
print("M^T eta   M - (A^T B + B^T A) == 0:", sp.simplify(Fe - (A.T * B + B.T * A)) == sp.zeros(d))
print("(F_omega + F_eta)/2 - A^T B == 0:  ", sp.simplify((Fw + Fe) / 2 - A.T * B) == sp.zeros(d))

print("\n=== B. Exact classification in every affine chart of Gr(d, 2d), d = 1 and d = 2 (sympy) ===")
for d in (1, 2):
    names = [f"x{i+1}" for i in range(d)] + [f"p{i+1}" for i in range(d)]
    om_s = sp.Matrix(sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [-sp.eye(d), sp.zeros(d)]]))
    et_s = sp.Matrix(sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [sp.eye(d), sp.zeros(d)]]))
    for piv in itertools.combinations(range(2 * d), d):
        free = [r for r in range(2 * d) if r not in piv]
        syms = sp.symbols(f"s0:{d * d}")
        M = sp.zeros(2 * d, d)
        for c, r in enumerate(piv):
            M[r, c] = 1
        it = iter(syms)
        for r in free:
            for c in range(d):
                M[r, c] = next(it)
        eqs = [e for e in list(M.T * om_s * M) + list(M.T * et_s * M) if e != 0]
        sol = sp.solve(eqs, syms, dict=True)
        # dimension of each solution family = number of symbols left free
        dims = [len([s for s in syms if s not in so]) for so in sol]
        print(f"d={d} chart pivots {[names[r] for r in piv]}: solutions {sol}  -> family dimensions {dims}")

print("\n=== C. Tangent-space dimension of {omega-Lagrangian and eta-null} at each coordinate splitting ===")
print("    (chart L = col(M0 + N0 Phi); linearized conditions; anchors: Lagrangian-only = d(d+1)/2, Gr(k,d) = k(d-k))")
for d in (2, 3, 4):
    om, et = forms(d)
    out = []
    for k in range(d + 1):
        for S in itertools.combinations(range(d), k):
            V = np.eye(d)[:, list(S)]
            M0 = split_L(V, d)
            N0 = complement(M0)
            rows_w, rows_e = [], []
            for idx in range(d * d):
                Phi = np.zeros((d, d)); Phi.flat[idx] = 1.0
                dM = N0 @ Phi
                rows_w.append((M0.T @ om @ dM + dM.T @ om @ M0).ravel())
                rows_e.append((M0.T @ et @ dM + dM.T @ et @ M0).ravel())
            Jw = np.array(rows_w).T
            Je = np.array(rows_e).T
            tw = d * d - np.linalg.matrix_rank(Jw)
            tb = d * d - np.linalg.matrix_rank(np.vstack([Jw, Je]))
            out.append((k, S, tw, tb))
    by_k = {}
    for k, S, tw, tb in out:
        by_k.setdefault(k, set()).add((tw, tb))
    for k in range(d + 1):
        print(f"d={d} k={k}: {sum(1 for o in out if o[0]==k)} coordinate splittings; (tangent dim, Lagrangian only; with eta-null too) = {sorted(by_k[k])}; anchors d(d+1)/2={d*(d+1)//2}, k(d-k)={k*(d-k)}")
    print(f"d={d}: coordinate splittings in total = {len(out)} (2^d = {2**d}); number of k-values (GL(d)-orbits) = {d+1}")

print("\n=== D. Explicit continuous family through a mixed coordinate splitting is exact (sympy, d = 2) ===")
th = sp.Symbol("theta", real=True)
d = 2
L = sp.Matrix([[sp.cos(th), 0], [sp.sin(th), 0], [0, -sp.sin(th)], [0, sp.cos(th)]])
om_s = sp.Matrix(sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [-sp.eye(d), sp.zeros(d)]]))
et_s = sp.Matrix(sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [sp.eye(d), sp.zeros(d)]]))
print("L(theta)^T omega L(theta) =", sp.simplify(L.T * om_s * L).tolist(), "  L(theta)^T eta L(theta) =", sp.simplify(L.T * et_s * L).tolist())
print("L(0) = span{x1, p2};  L(pi/2) =", L.subs(th, sp.pi / 2).T.tolist(), "= span{x2, p1}")

print("\n=== E. det^2 on each family (random members), d = 2, 3, 4; and Maslov winding along the d = 2 circle ===")
for d in (2, 3, 4):
    om, et = forms(d)
    for k in range(d + 1):
        vals, worst = [], 0.0
        for _ in range(200):
            V = onb(rng.standard_normal((d, k))) if k > 0 else np.zeros((d, 0))
            M = split_L(V, d)
            worst = max(worst, np.abs(M.T @ om @ M).max(), np.abs(M.T @ et @ M).max())
            vals.append(det2(M, d))
        vals = np.array(vals)
        print(f"d={d} k={k}: max|omega|,|eta| on L = {worst:.1e}; det^2 over 200 random V: min {vals.real.min():+.12f} max {vals.real.max():+.12f} max|imag| {np.abs(vals.imag).max():.1e}; (-1)^(d-k) = {(-1)**(d-k):+d}")


def winding(path_vals):
    ph = np.unwrap(np.angle(path_vals))
    return (ph[-1] - ph[0]) / (2 * np.pi)


d = 2
om, et = forms(d)
ts = np.linspace(0, np.pi, 2001)
circ = [np.array([[np.cos(t), 0], [np.sin(t), 0], [0, -np.sin(t)], [0, np.cos(t)]]) for t in ts]
print("Gr(1,2) loop (theta: 0 -> pi closes as a subspace):", "closes:", np.allclose(onb(circ[0]) @ onb(circ[0]).T, onb(circ[-1]) @ onb(circ[-1]).T),
      " Maslov winding of det^2 =", round(winding([det2(M, d) for M in circ]), 6))
gen = []
eta_off = 0.0
for t in ts:
    U = np.diag([np.exp(1j * t), 1.0])
    M = np.vstack([U.real, U.imag])
    gen.append(det2(M, d))
    eta_off = max(eta_off, np.abs(M.T @ et @ M).max())
print("Maslov generator loop diag(e^{i t}, 1) R^2, t: 0 -> pi: winding of det^2 =", round(winding(gen), 6), "; max|eta on L| along it =", round(eta_off, 6), "(not eta-null)")

print("\n=== F. Symmetry group of the rigid pair (omega, eta), and its action on the splittings ===")
for d in (2, 3, 4):
    om, et = forms(d)
    rows = []
    for idx in range(4 * d * d):
        X = np.zeros((2 * d, 2 * d)); X.flat[idx] = 1.0
        rows.append(np.concatenate([(X.T @ om + om @ X).ravel(), (X.T @ et + et @ X).ravel()]))
    Jm = np.array(rows).T
    u, s, vt = np.linalg.svd(Jm)
    null = vt[(s > 1e-10).sum():]
    ok = all(np.allclose(n.reshape(2 * d, 2 * d)[:d, d:], 0) and np.allclose(n.reshape(2 * d, 2 * d)[d:, :d], 0)
             and np.allclose(n.reshape(2 * d, 2 * d)[d:, d:], -n.reshape(2 * d, 2 * d)[:d, :d].T) for n in null)
    print(f"d={d}: dim Lie algebra preserving omega and eta = {null.shape[0]} (d^2 = {d*d}); all of form diag(a, -a^T): {ok}")
    # orbit dimension of GL(d) and of O(d) at each coordinate splitting
    res = []
    for k in range(d + 1):
        S = tuple(range(k))
        V = np.eye(d)[:, list(S)]
        M0 = split_L(V, d); N0 = complement(M0)
        def orbit_dim(gens):
            vecs = []
            for a in gens:
                X = np.block([[a, np.zeros((d, d))], [np.zeros((d, d)), -a.T]])
                vecs.append((N0.T @ X @ M0).ravel())
            return np.linalg.matrix_rank(np.array(vecs)) if vecs else 0
        gl = [np.eye(d)[:, [i]] @ np.eye(d)[[j], :] for i in range(d) for j in range(d)]
        so = [g - g.T for g in gl if not np.allclose(g - g.T, 0)]
        res.append((k, orbit_dim(gl), orbit_dim(so), k * (d - k)))
    print(f"d={d}: (k, GL(d)-orbit dim, O(d)-orbit dim, k(d-k)) at the splitting span{{x_1..x_k, p_k+1..p_d}}: {res}")

om, et = forms(4)
K = np.linalg.inv(et) @ om
w, v = np.linalg.eig(K)
print("\nK = eta^-1 omega at d = 4: diag =", np.diag(K).astype(int).tolist(), "; off-diagonal zero:", np.allclose(K - np.diag(np.diag(K)), 0))
print("  K-eigenspaces (the para-Hermitian polarization): eigenvalue -1 -> x-space, +1 -> p-space; count = 2")
d = 4
inv_ok = True
for _ in range(100):
    k = int(rng.integers(0, d + 1))
    V = onb(rng.standard_normal((d, k))) if k > 0 else np.zeros((d, 0))
    M = split_L(V, d)
    P = M @ M.T
    inv_ok &= np.allclose(P @ K @ M, K @ M)  # K maps L into L
print("  every random V (+) V^perp (d = 4) is K-invariant:", inv_ok)

print("\n=== G. Completeness at d = 4 by numerical solve: minimize |A^T B|^2 on orthonormal frames (QR retraction) ===")
print("    (every zero found should be V (+) V^perp: rank A + rank B = d and col A orthogonal to col B)")
d = 4
counts, bad, worst_res = {}, 0, 0.0
for trial in range(200):
    M = onb(rng.standard_normal((2 * d, d)))
    for it in range(20000):
        A_, B_ = M[:d], M[d:]
        G = A_.T @ B_
        if np.abs(G).max() < 1e-14:
            break
        grad = np.vstack([2 * B_ @ G.T, 2 * A_ @ G])
        grad -= M @ (M.T @ grad + grad.T @ M) / 2      # project to the Stiefel tangent space
        M = onb(M - 0.2 * grad)
    A_, B_ = M[:d], M[d:]
    res = np.abs(A_.T @ B_).max()
    worst_res = max(worst_res, res)
    sA = np.linalg.svd(A_, compute_uv=False); sB = np.linalg.svd(B_, compute_uv=False)
    rA = int((sA > 1e-6).sum()); rB = int((sB > 1e-6).sum())
    if res > 1e-10 or rA + rB != d:
        bad += 1
    counts[rA] = counts.get(rA, 0) + 1
print(f"200 runs: worst residual |A^T B| = {worst_res:.1e}; runs failing (not converged, or rank A + rank B != d): {bad}; "
      f"k = rank A distribution: {dict(sorted(counts.items()))}")

print("\n=== H. Steelman not in the text: also demand L invariant under the matrix H = diag(g, g^-1) ===")
print("    (tangent dim of {omega-Lagrangian, eta-null, H L = L} at V(+)V^perp with V spanned by eigenvectors of g)")
d = 4
om, et = forms(d)
for label, g in (("generic g (random, distinct eigenvalues)", None), ("g = 1 (the notebook's flat vacuum, #1 S2)", np.eye(d))):
    if g is None:
        Q = onb(rng.standard_normal((d, d)))
        g = Q @ np.diag([0.5, 0.9, 1.7, 3.1]) @ Q.T
    lam, Q = np.linalg.eigh(g)
    H = np.block([[g, np.zeros((d, d))], [np.zeros((d, d)), np.linalg.inv(g)]])
    dims, n_pts = {}, 0
    for k in range(d + 1):
        for S in itertools.combinations(range(d), k):
            V = Q[:, list(S)]
            M0 = split_L(V, d); N0 = complement(M0)
            assert np.allclose(N0.T @ H @ M0, 0)  # L is H-invariant
            rows = []
            for idx in range(d * d):
                Phi = np.zeros((d, d)); Phi.flat[idx] = 1.0
                dM = N0 @ Phi
                rows.append(np.concatenate([(M0.T @ om @ dM + dM.T @ om @ M0).ravel(),
                                            (M0.T @ et @ dM + dM.T @ et @ M0).ravel(),
                                            (N0.T @ H @ N0 @ Phi - Phi @ M0.T @ H @ M0).ravel()]))
            t = d * d - np.linalg.matrix_rank(np.array(rows).T)
            dims.setdefault(k, set()).add(int(t)); n_pts += 1
    print(f"{label}: eigenvalue-adapted splittings = {n_pts}; tangent dims by k = {dict(sorted((k, sorted(v)) for k, v in dims.items()))}")
