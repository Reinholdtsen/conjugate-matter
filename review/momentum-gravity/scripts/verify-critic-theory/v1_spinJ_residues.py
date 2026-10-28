"""
v1_spinJ_residues.py  (verify-critic-theory, round 3)

Independent check of claim c1: the residue of tree-level spin-J exchange between two
spinless point sources (currents u^{mu1}...u^{muJ}) is a degree-J polynomial in
gamma = u1.u2; massive -> Legendre P_J, massless -> Chebyshev T_J; (v/c)^2 coefficients
J(J+1)/4 and J^2/2.

Method (written before reading the critic's c1 script):
 A. Build the traceless part of x^{(x)J} by explicit linear algebra (no closed formula
    assumed) in an n-dimensional space with metric g, then contract with y^{(x)J}.
    - massive spin J in D=4: physical states = symmetric traceless tensors of the 3-dim
      space orthogonal to the on-shell (complex) momentum q; with u1,u2 orthogonal to q
      (classical limit) that space is Lorentzian (t,y,z) -> n=3, metric diag(1,-1,-1).
    - massless spin J in D=4: physical states = 2 helicities; for complex null q
      orthogonal to u1,u2 the transverse plane modulo q is the (t,z) plane -> n=2,
      metric diag(1,-1).
    u1 = (1,0,..), u2 = (gamma, sqrt(gamma^2-1), ..) so u.u = 1, u1.u2 = gamma.
 B. Independent textbook anchors at J=2: Fierz-Pauli numerator (1/2)(th th + th th) - (1/3) th th
    and the D=4 de Donder numerator (1/2)(eta eta + eta eta) - (1/2) eta eta, contracted in 4D
    with an explicit complex on-shell q orthogonal to u1, u2.
    Massless helicity sum for general J, done directly with null polarization vectors.
 C. (v/c)^2 coefficients (sympy).
 D. Spin needed for an O(1) effect at v = 120 km/s; exact polynomial values there.
 E. The tuned J=0 (attractive) + J=1 (repulsive) residual.
"""
import itertools, math
import numpy as np
import sympy as sp
import mpmath as mp

np.set_printoptions(precision=6, suppress=True)

# ---------------------------------------------------------------- A
def sym(T):
    """Full symmetrization of a numpy tensor over all indices."""
    J = T.ndim
    if J <= 1:
        return T.copy()
    acc = np.zeros_like(T)
    perms = list(itertools.permutations(range(J)))
    for p in perms:
        acc = acc + np.transpose(T, p)
    return acc / len(perms)

def outer_power(x, J):
    T = np.array(1.0 + 0j)
    for _ in range(J):
        T = np.multiply.outer(T, x)
    return T

def lower(T, g):
    """Lower all indices with metric g (g diagonal or full)."""
    for ax in range(T.ndim):
        T = np.moveaxis(np.tensordot(g, T, axes=([1], [ax])), 0, ax)
    return T

def trace(T, ginv):
    """Contract first two (upper) indices with ginv (applied to lowered tensor): T_ab... ginv^{ab}"""
    return np.tensordot(ginv, T, axes=([0, 1], [0, 1]))

def traceless_part(xup, J, g):
    """Traceless part (w.r.t. metric g) of the symmetric tensor with LOWER indices x_a x_b ...
    Solve T = A - sym(g (x) S), trace(T) = 0, for symmetric S of rank J-2, by least squares."""
    n = len(xup)
    ginv = np.linalg.inv(g)
    xlow = g @ xup
    A = outer_power(xlow, J)              # lower indices
    if J < 2:
        return A
    # basis for rank-(J-2) tensors (full index basis; redundancy is harmless)
    m = n ** (J - 2)
    cols = []
    for k in range(m):
        S = np.zeros(m, dtype=complex); S[k] = 1.0
        S = S.reshape((n,) * (J - 2)) if J > 2 else S.reshape(())
        GS = sym(np.multiply.outer(g.astype(complex), S))
        cols.append(trace(GS, ginv).ravel())
    M = np.array(cols).T                  # maps S -> trace(sym(g S))
    rhs = trace(A, ginv).ravel()
    Ssol, *_ = np.linalg.lstsq(M, rhs, rcond=None)
    Ssol = Ssol.reshape((n,) * (J - 2)) if J > 2 else Ssol.reshape(())
    T = A - sym(np.multiply.outer(g.astype(complex), Ssol))
    # check tracelessness
    assert np.max(np.abs(trace(T, ginv))) < 1e-9, "not traceless"
    return T

def contract(Tlow, yup):
    out = Tlow
    for _ in range(Tlow.ndim):
        out = np.tensordot(out, yup, axes=([0], [0]))
    return complex(out)

print("A. traceless-projection residues vs Legendre (n=3) and Chebyshev (n=2), Lorentzian metric")
gammas = [1.0, 1.0001, 1.1, 1.5, 3.0]
maxdev = {2: 0.0, 3: 0.0}
for n, poly, name in [(3, lambda J, x: float(sp.legendre(J, x)), "P_J"),
                      (2, lambda J, x: float(sp.chebyshevt(J, x)), "T_J")]:
    g = np.diag([1.0] + [-1.0] * (n - 1))
    for J in range(0, 7):
        row = []
        for gam in gammas:
            u1 = np.zeros(n); u1[0] = 1.0
            u2 = np.zeros(n); u2[0] = gam; u2[1] = math.sqrt(gam * gam - 1.0)
            T = traceless_part(u1.astype(complex), J, g)
            r = contract(T, u2.astype(complex)) / contract(T, u1.astype(complex))
            dev = abs(r.real - poly(J, gam)) / max(1.0, abs(poly(J, gam)))
            maxdev[n] = max(maxdev[n], dev, abs(r.imag))
            row.append(r.real)
        print(f"  n={n} J={J}: residue/static at gamma={gammas}: " +
              ", ".join(f"{v:.6f}" for v in row) +
              f"   [{name}: " + ", ".join(f"{poly(J, x):.6f}" for x in gammas) + "]")
print(f"  max relative deviation n=3 vs P_J: {maxdev[3]:.2e};  n=2 vs T_J: {maxdev[2]:.2e}")

# Euclidean sanity (|cos| <= 1): same projection with Euclidean metric gives the zonal harmonic
print("  Euclidean n=3, J=4, cos=0.3: ", end="")
g = np.eye(3)
x = np.array([1.0, 0, 0]); c = 0.3; y = np.array([c, math.sqrt(1 - c * c), 0])
T = traceless_part(x.astype(complex), 4, g)
print(f"{(contract(T, y.astype(complex)) / contract(T, x.astype(complex))).real:.6f}  vs P_4(0.3) = {float(sp.legendre(4, 0.3)):.6f}")

# ---------------------------------------------------------------- B
print("\nB. textbook J=2 numerators contracted in D=4 with complex on-shell q orthogonal to u1,u2")
eta = np.diag([1.0, -1.0, -1.0, -1.0]).astype(complex)
gam = 1.37
u1 = np.array([1, 0, 0, 0], dtype=complex)
u2 = np.array([gam, 0, 0, math.sqrt(gam ** 2 - 1)], dtype=complex)
M = 1.0
q_up = np.array([0, 1j * M, 0, 0])            # q.q = -(iM)^2 = M^2 > 0 : on the massive pole
q_lo = eta @ q_up
print(f"  q.q = {complex(q_up @ eta @ q_up):.3f} (= M^2), q.u1 = {complex(q_lo @ u1):.1e}, q.u2 = {complex(q_lo @ u2):.1e}")
th = eta - np.outer(q_lo, q_lo) / M ** 2       # lower-index theta
u1l, u2l = eta @ u1, eta @ u2
# project with upper-index vectors: contraction th_{mu nu} u1^mu u2^nu
def TH(a, b, t): return complex(a @ t @ b)
fp = 0.5 * (TH(u1, u2, th) * TH(u1, u2, th) * 2) - (1 / 3) * TH(u1, u1, th) * TH(u2, u2, th)
fp_static = 0.5 * 2 - 1 / 3
print(f"  Fierz-Pauli: numerator = {fp.real:.6f}; /static = {(fp / fp_static).real:.6f};  (3g^2-1)/2 = {(3 * gam ** 2 - 1) / 2:.6f}")
dd = 0.5 * (TH(u1, u2, eta) ** 2 * 2) - 0.5 * TH(u1, u1, eta) * TH(u2, u2, eta)
dd_static = 1 - 0.5
print(f"  de Donder D=4: numerator = {dd.real:.6f}; /static = {(dd / dd_static).real:.6f};  2g^2-1 = {2 * gam ** 2 - 1:.6f}")
print(f"  static ratio massive/massless = {(fp_static / dd_static):.6f}  (the bimetric alpha = 4/3 at u=1)")

print("  massless helicity sum, complex null q=(0,1,i,0): polarizations eps+- = (e_t +- e_z)/sqrt2 (mod q)")
qn = np.array([0, 1, 1j, 0])
e_t = np.array([1, 0, 0, 0], dtype=complex); e_z = np.array([0, 0, 0, 1], dtype=complex)
epp = (e_t + e_z) / math.sqrt(2); epm = (e_t - e_z) / math.sqrt(2)
dot = lambda a, b: complex(a @ eta @ b)
print(f"    checks: q.q={dot(qn,qn):.1e}, eps+.q={dot(epp,qn):.1e}, eps-.q={dot(epm,qn):.1e}, eps+.eps+={dot(epp,epp):.1e}, eps+.eps-={dot(epp,epm):.3f}")
for gam in [1.0001, 1.37, 3.0]:
    u2 = np.array([gam, 0, 0, math.sqrt(gam ** 2 - 1)], dtype=complex)
    vals = []
    for J in range(0, 7):
        s = dot(u1, epp) ** J * dot(u2, epm) ** J + dot(u1, epm) ** J * dot(u2, epp) ** J
        s0 = dot(u1, epp) ** J * dot(u1, epm) ** J * 2
        vals.append((s / s0).real)
    print(f"    gamma={gam}: helicity sum/static J=0..6: " + ", ".join(f"{v:.6f}" for v in vals))
    print(f"                 T_J(gamma)        J=0..6: " + ", ".join(f"{float(sp.chebyshevt(J, gam)):.6f}" for J in range(7)))

# ---------------------------------------------------------------- C
print("\nC. first-order (v/c)^2 coefficients")
beta = sp.symbols('beta', positive=True)
gm = 1 / sp.sqrt(1 - beta ** 2)
for J in range(0, 9):
    cP = sp.series(sp.legendre(J, gm), beta, 0, 3).removeO().coeff(beta, 2)
    cT = sp.series(sp.chebyshevt(J, gm), beta, 0, 3).removeO().coeff(beta, 2)
    print(f"  J={J}: massive coeff = {cP} (J(J+1)/4 = {sp.Rational(J*(J+1),4)}),  massless coeff = {cT} (J^2/2 = {sp.Rational(J*J,2)})")
Js = sp.symbols('J', positive=True, integer=True)
x = sp.symbols('x')
# general J: P_J'(1) from the Legendre ODE (1-x^2)y'' - 2xy' + J(J+1)y = 0 at x=1: -2y'(1) + J(J+1) = 0
print("  from the ODEs at x=1: P_J'(1) = J(J+1)/2 (Legendre: -2y' + J(J+1)y = 0), T_J'(1) = J^2 (Chebyshev: -y' + J^2 y = 0)")

# ---------------------------------------------------------------- D
print("\nD. spin needed for an O(1) change at v = 120 km/s")
c_kms = 299792.458
v = 120.0
b2 = (v / c_kms) ** 2
Jm = (-1 + math.sqrt(1 + 16 / b2)) / 2
Jl = math.sqrt(2 / b2)
print(f"  (v/c)^2 = {b2:.6e};  J(J+1)/4 (v/c)^2 = 1 -> J = {Jm:.1f};  J^2/2 (v/c)^2 = 1 -> J = {Jl:.1f}")
mp.mp.dps = 40
gstar = 1 / mp.sqrt(1 - mp.mpf(b2))
for J in [2, 10, 100, int(round(Jl)), int(round(Jm))]:
    PJ = mp.hyp2f1(-J, J + 1, 1, (1 - gstar) / 2)
    TJ = mp.cosh(J * mp.acosh(gstar))
    print(f"  J={J:5d}: P_J(gamma*)-1 = {mp.nstr(PJ - 1, 6)},  T_J(gamma*)-1 = {mp.nstr(TJ - 1, 6)}")
print("  (single-spin residues increase with v; none decreases -> no single exchange is a gate)")

# ---------------------------------------------------------------- E
print("\nE. tuned J=0 attraction + J=1 repulsion, residual zero-crossing placed at v0 = 120 km/s")
# covariant numerators: scalar 1 (attractive between like sources), vector gamma (repulsive)
# attraction A(gamma) = g0^2 - g1^2 gamma, static residual delta = g0^2 - g1^2 > 0
def gam_of(vk): return 1 / math.sqrt(1 - (vk / c_kms) ** 2)
g0m1 = gam_of(120.0) - 1
g1sq = 1 / g0m1          # in units of delta
g0sq = g1sq + 1
print(f"  gamma(120)-1 = {g0m1:.6e};  g1^2/delta = {g1sq:.4e},  g0^2/delta = {g0sq:.4e}")
for vk in [0, 60, 100, 120, 150, 200, 300, 1000, 2600]:
    A = g0sq - g1sq * gam_of(vk)
    print(f"  v_rel = {vk:6.0f} km/s: attraction/static residual = {A:+.5e}")
