"""Critic, tension (b): momentum-space C27 ('a doubly compact, exactly reciprocal phase space must be
torus-like') against observations C46 (Euclidean Snyder-de Sitter: Born-reciprocal, phase space Gr(3,5),
discrete x and p spectra).

Checks:
 (1) Kunneth: for X a rational homology 3-sphere (S^3 and every S^3/Gamma) and any closed orientable
     3-manifold M, H^2(X x M; R) = H^2(M), so every degree-2 class is pulled back from M and its cube
     vanishes: X x M is never symplectic. Betti numbers printed for a few M.
 (2) Gr~(2,5) = Gr~(3,5) = SO(5)/(SO(2)xSO(3)) is the complex quadric Q3 = {sum z_i^2 = 0} in CP^4:
     z = u + i v for an oriented orthonormal pair (u, v). Q3 is a smooth complex submanifold, so the
     Fubini-Study form restricts to a symplectic (Kahler) form; checked numerically (rank 6 at random
     points). It is compact, 6-dimensional, and not a product of two 3-manifolds.
 (3) Born reciprocity as an inner automorphism of so(5): the rotation by pi/2 in the (4,5) plane maps
     M_i4 -> M_i5, M_i5 -> -M_i4 (x -> p, p -> -x), fixes M_ij and M_45, and therefore maps the orbit of
     M_45 (= Gr~(2,5)) to itself.
 (4) Euler characteristic of Gr~(2,5) from the fixed points of a generic maximal-torus element: 4,
     so (even cohomology only) b2 = 1 and [omega]^3 != 0 is consistent.
"""
import numpy as np
import itertools

rng = np.random.default_rng(20261027)
print("=== (1) Kunneth: rational homology 3-sphere x closed 3-manifold ===")
def prod_betti(b1, b2):
    out = [0]*(len(b1)+len(b2)-1)
    for i, x in enumerate(b1):
        for j, y in enumerate(b2):
            out[i+j] += x*y
    return out
X = [1, 0, 0, 1]                      # S^3, RP^3, Poincare dodecahedral space, lens spaces (over R)
for name, M in [('S^3 (or any S^3/Gamma)', [1, 0, 0, 1]), ('T^3', [1, 3, 3, 1]), ('S^1 x S^2', [1, 1, 1, 1]),
                ('genus-2 surface x S^1', [1, 5, 5, 1])]:
    b = prod_betti(X, M)
    print(f"  X x {name}: Betti {b}; H^2 = H^0(X) (x) H^2(M) only (H^1(X) = H^2(X) = 0) ->"
          f" every [omega] = pi_M^* alpha, [omega]^3 = pi_M^*(alpha^3), alpha^3 in H^6(M) = 0 -> not symplectic")
print("  T^3 x T^3 Betti", prod_betti([1,3,3,1],[1,3,3,1]), "(symplectic, but needs a flat T^3 position space: not k = +1)")

print("\n=== (2) Gr~(2,5) as the quadric Q3 in CP^4; Fubini-Study form restricted is non-degenerate ===")
def random_pair():
    A = rng.normal(size=(5, 2))
    Q, _ = np.linalg.qr(A)
    return Q[:, 0], Q[:, 1]
maxq = 0.0
ranks = []
minsv = []
for trial in range(200):
    u, v = random_pair()
    z = u + 1j*v
    maxq = max(maxq, abs(np.sum(z*z)))
    # tangent space of Q3 at [z]: vectors w in C^5 with w . z = 0 (bilinear) and w orthogonal (hermitian) to z
    # basis of {w : z.w = 0, conj(z).w = 0}: complex dimension 3
    Mrows = np.vstack([z, np.conj(z)])             # conditions sum z_i w_i = 0, sum conj(z_i) w_i = 0
    _, s, Vh = np.linalg.svd(Mrows)
    W = Vh[2:].conj().T                              # 5 x 3 complex basis of the null space
    # real tangent basis (6 vectors) and Fubini-Study form omega(a,b) = Im <a,b>/|z|^2 on the horizontal space
    T = np.hstack([W, 1j*W])                         # 5 x 6
    Om = np.imag(T.conj().T @ T) / np.vdot(z, z).real
    ranks.append(np.linalg.matrix_rank(Om, tol=1e-9))
    minsv.append(np.min(np.abs(np.linalg.eigvals(Om))))
print(f"  max |sum z_i^2| over 200 oriented orthonormal pairs = {maxq:.2e}  (z = u + i v lies on Q3)")
print(f"  rank of restricted Fubini-Study form: min {min(ranks)}, max {max(ranks)} (6 = non-degenerate);"
      f" smallest |eigenvalue| {min(minsv):.3f}")
# injectivity up to SO(2) rotation of (u,v) = phase of z: check that rotating the pair changes z by a phase only
u, v = random_pair(); th = 0.7
u2, v2 = np.cos(th)*u - np.sin(th)*v, np.sin(th)*u + np.cos(th)*v
z1, z2 = u + 1j*v, u2 + 1j*v2
print(f"  rotating the oriented frame by 0.7 rad multiplies z by a phase: |z2 - e^(i th) z1| = "
      f"{min(np.linalg.norm(z2 - np.exp(1j*th)*z1), np.linalg.norm(z2 - np.exp(-1j*th)*z1)):.1e}")

print("\n=== (3) Born reciprocity in so(5): pi/2 rotation of the (4,5) plane ===")
def M(a, b, n=5):
    m = np.zeros((n, n)); m[a, b] = 1; m[b, a] = -1; return m
th = np.pi/2
O = np.eye(5); O[3, 3] = np.cos(th); O[3, 4] = -np.sin(th); O[4, 3] = np.sin(th); O[4, 4] = np.cos(th)
Ad = lambda m: O @ m @ O.T
errs = []
for i in range(3):
    errs.append(np.linalg.norm(Ad(M(i, 3)) - M(i, 4)))       # X_i ~ M_i4 -> M_i5 ~ P_i
    errs.append(np.linalg.norm(Ad(M(i, 4)) + M(i, 3)))       # P_i -> -X_i
    for j in range(i+1, 3):
        errs.append(np.linalg.norm(Ad(M(i, j)) - M(i, j)))   # rotations fixed
errs.append(np.linalg.norm(Ad(M(3, 4)) - M(3, 4)))           # M_45 fixed -> orbit of M_45 preserved
print(f"  max residual of  X -> P, P -> -X, M_ij fixed, M_45 fixed : {max(errs):.1e}")
print(f"  O^4 = 1: {np.linalg.norm(np.linalg.matrix_power(O,4) - np.eye(5)):.1e}; O^2 = (X,P) -> (-X,-P): "
      f"{np.linalg.norm((O@O) @ M(0,3) @ (O@O).T + M(0,3)):.1e}")

print("\n=== (4) Euler characteristic of Gr~(2,5) from torus fixed points ===")
# generic element of the maximal torus SO(2) x SO(2) x 1 of SO(5); fixed oriented 2-planes = invariant
# oriented planes; count among the planes spanned by pairs of eigenvectors that are real 2-planes
t = np.eye(5)
for k, ang in enumerate([0.37, 1.13]):
    c_, s_ = np.cos(ang), np.sin(ang)
    t[2*k:2*k+2, 2*k:2*k+2] = [[c_, -s_], [s_, c_]]
# an invariant 2-plane of a generic torus element is a sum of real invariant subspaces of total dim 2:
# the two rotation planes, or (line e5) + (line in a rotation plane) -- impossible (rotation planes have no
# invariant lines). So the fixed oriented planes are the two rotation planes x 2 orientations.
cands = []
for (i, j) in itertools.combinations(range(5), 2):
    P = np.zeros((5, 2)); P[i, 0] = 1; P[j, 1] = 1
    img = t @ P
    proj = P @ P.T
    if np.linalg.norm(proj @ img - img) < 1e-12:
        d = np.linalg.det(P.T @ img)        # orientation preserved iff det > 0
        cands.append(((i, j), d > 0))
print(f"  invariant coordinate planes: {cands}; each with 2 orientations -> chi = {2*len(cands)}")
print("  chi = 4 with only even cohomology (Kahler, cell decomposition) -> Betti (1,0,1,0,1,0,1), b2 = 1")

print("\n=== (5) the reciprocity length of a doubly compact SdS-type phase space ===")
# x -> (lambda^2/hbar) p must send the momentum sphere (radius kappa) onto the position sphere (radius R):
# lambda^2 kappa/hbar = R  ->  lambda = sqrt(R hbar/kappa)
import mpmath as mp
c = mp.mpf(299792458); hbar = mp.mpf('1.054571817e-34'); G = mp.mpf('6.67430e-11'); eV = mp.mpf('1.602176634e-19')
lP = mp.sqrt(hbar*G/c**3); Mpc = mp.mpf('3.0856775814913673e22'); cH0 = c/(67.4e3/Mpc)
for Ok in ['1e-2', '1e-5']:
    R0 = cH0/mp.sqrt(mp.mpf(Ok))
    lam_P = mp.sqrt(R0*lP)                                   # kappa = Planck momentum
    lam_b = mp.sqrt(R0*hbar*c/(mp.mpf('1.401e8')*eV))        # kappa = Born 1938's b (b c = 1.401e8 eV)
    print(f"  |Omega_k| = {Ok}: kappa = m_P c -> lambda = sqrt(R0 l_P) = {mp.nstr(lam_P,4)} m (= momentum-space C23);"
          f" kappa = Born's b -> lambda = {mp.nstr(lam_b,4)} m")
