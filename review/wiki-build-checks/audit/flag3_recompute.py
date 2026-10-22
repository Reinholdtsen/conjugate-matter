"""
Independent recomputation for flag 3 (zero set of {J0, I[Z]}, notes/debt1a-iii-tuning-test.md S2 item 1).

Definitions taken from the sources (not from review/wiki-build-checks/zero_locus.py):
  #5 (debt1a-geometric-core.md SC): Z = X + iY, Y > 0, H_Z = [[Y + X Y^-1 X, X Y^-1], [Y^-1 X, Y^-1]]
  #5 SB: I = omega^-1 H ; J = involution anticommuting with I ("H-compatible real structure")
  #7 S2: I[Z] = [[-Y^-1 X, -Y^-1], [Y + X Y^-1 X, X Y^-1]],  J0 = [[0,1],[1,0]]
  HANDOFF App. A / verify/battery.py: omega = [[0,1],[-1,0]], eta = J0 = [[0,1],[1,0]]
Claim under test (#7 S2 item 1): {J0, I[Z]} = 0  <=>  X = 0 and Y = Y^-1.
"""
import itertools
import numpy as np
import sympy as sp

def symsym(name, d):
    """generic symbolic symmetric d x d matrix"""
    M = sp.zeros(d, d)
    for i in range(d):
        for j in range(i, d):
            s = sp.Symbol(f"{name}{i}{j}", real=True)
            M[i, j] = s; M[j, i] = s
    return M

def blocks(d):
    Id = sp.eye(d); Z0 = sp.zeros(d, d)
    omega = sp.BlockMatrix([[Z0, Id], [-Id, Z0]]).as_explicit()
    J0 = sp.BlockMatrix([[Z0, Id], [Id, Z0]]).as_explicit()
    return omega, J0

def HZ(X, Y):
    Yi = Y.inv()
    return sp.BlockMatrix([[Y + X*Yi*X, X*Yi], [Yi*X, Yi]]).as_explicit()

def IZ_note(X, Y):
    Yi = Y.inv()
    return sp.BlockMatrix([[-Yi*X, -Yi], [Y + X*Yi*X, X*Yi]]).as_explicit()

def anticomm(X, Y, J=None):
    d = X.shape[0]
    omega, J0 = blocks(d)
    if J is None: J = J0
    I = omega.inv() * HZ(X, Y)
    return J*I + I*J

def zeroQ(M):
    return all(sp.simplify(e) == 0 for e in M)

print("=== Part 1: block algebra, symbolic (d = 1, 2) and exact random rational (d = 3) ===")
for d in (1, 2):
    X = symsym("x", d); Y = symsym("y", d)
    omega, J0 = blocks(d)
    I = omega.inv() * HZ(X, Y)
    print(f"d={d}: omega^-1 H_Z equals #7's printed I[Z]:", zeroQ(I - IZ_note(X, Y)))
    print(f"d={d}: I[Z]^2 = -1:", zeroQ(I*I + sp.eye(2*d)))
    Mt = J0*I + I*J0
    Yi = Y.inv()
    S = Y + X*Yi*X - Yi; A = X*Yi - Yi*X
    print(f"d={d}: blocks [[S,A],[A,S]]:",
          zeroQ(Mt[:d, :d] - S), zeroQ(Mt[:d, d:] - A), zeroQ(Mt[d:, :d] - A), zeroQ(Mt[d:, d:] - S))
    # the two identities that characterize the zero set
    print(f"d={d}: identity S == (X^2 + Y^2 - 1) Y^-1 - X A :", zeroQ(S - ((X*X + Y*Y - sp.eye(d))*Yi - X*A)))
    print(f"d={d}: identity A == Y^-1 (Y X - X Y) Y^-1      :", zeroQ(A - Yi*(Y*X - X*Y)*Yi))

# d = 3 with random exact rationals
rng = np.random.default_rng(7)
def randrat_sym(d, posdef=False):
    a = sp.Matrix(d, d, lambda i, j: sp.Rational(int(rng.integers(-9, 10)), int(rng.integers(1, 6))))
    m = (a + a.T) / 2
    if posdef: m = a*a.T + d*sp.eye(d)
    return m
X3 = randrat_sym(3); Y3 = randrat_sym(3, posdef=True)
omega3, J03 = blocks(3)
I3 = omega3.inv()*HZ(X3, Y3); M3 = J03*I3 + I3*J03
Y3i = Y3.inv(); S3 = Y3 + X3*Y3i*X3 - Y3i; A3 = X3*Y3i - Y3i*X3
print("d=3 exact random: blocks match:", (M3[:3, :3] - S3).is_zero_matrix, (M3[:3, 3:] - A3).is_zero_matrix,
      "| S identity:", (S3 - ((X3*X3 + Y3*Y3 - sp.eye(3))*Y3i - X3*A3)).is_zero_matrix,
      "| A identity:", (A3 - Y3i*(Y3*X3 - X3*Y3)*Y3i).is_zero_matrix)

print("\n  -> by the two identities (valid for any symmetric X and invertible Y):")
print("     A = 0 <=> [X,Y] = 0 ; and given A = 0, S = 0 <=> X^2 + Y^2 = 1.")
print("     So zero set = {[X,Y]=0, X^2+Y^2=1, Y>0}, not {X=0, Y=1}.")

# noncommutative (dimension-free) check of the same identities with matrix symbols
n = sp.Symbol("n", integer=True, positive=True)
Xm = sp.MatrixSymbol("X", n, n); Ym = sp.MatrixSymbol("Y", n, n); Idn = sp.Identity(n)
Yim = Ym.I
Sm = Ym + Xm*Yim*Xm - Yim; Am = Xm*Yim - Yim*Xm
r1 = sp.expand((Sm - ((Xm*Xm + Ym*Ym - Idn)*Yim - Xm*Am)).doit())
r2 = sp.expand((Am - Yim*(Ym*Xm - Xm*Ym)*Yim).doit())
print("dimension-free MatrixSymbol check, residuals:", sp.simplify(r1), "|", sp.simplify(r2))

print("\n=== Part 2: exact zeros with X != 0 ===")
x, y = sp.symbols("x y", real=True)
S1 = sp.simplify((y + x**2/y - 1/y))
print("d=1: S =", sp.factor(S1), "; solve S=0 for y>0:", [s for s in sp.solve(sp.Eq(S1, 0), y)])
for (a, b) in [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(-5, 13), sp.Rational(12, 13)),
               (sp.Rational(8, 17), sp.Rational(15, 17))]:
    Mx = anticomm(sp.Matrix([[a]]), sp.Matrix([[b]]))
    print(f"d=1: Z = {a} + {b} i, |Z|^2 = {a**2 + b**2}: {{J0, I[Z]}} =", Mx.tolist())
# d = 2: rotate by a rational rotation; eigenpairs from Pythagorean triples
O2 = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])
X2 = O2*sp.diag(sp.Rational(3, 5), -sp.Rational(5, 13))*O2.T
Y2 = O2*sp.diag(sp.Rational(4, 5), sp.Rational(12, 13))*O2.T
print("d=2: X =", X2.tolist(), " Y =", Y2.tolist())
print("     Y pos.def:", all(ev > 0 for ev in Y2.eigenvals()), " [X,Y]=0:", (X2*Y2 - Y2*X2).is_zero_matrix,
      " X^2+Y^2=1:", (X2*X2 + Y2*Y2 - sp.eye(2)).is_zero_matrix)
print("     {J0, I[Z]} exactly zero:", anticomm(X2, Y2).is_zero_matrix, "  X != 0:", not X2.is_zero_matrix,
      "  Y != 1:", Y2 != sp.eye(2))
# d = 3: rational orthogonal via Cayley transform of a rational skew matrix
K = sp.Matrix([[0, sp.Rational(1, 2), -1], [-sp.Rational(1, 2), 0, sp.Rational(1, 3)], [1, -sp.Rational(1, 3), 0]])
O3 = (sp.eye(3) - K)*(sp.eye(3) + K).inv()
print("d=3: Cayley O orthogonal:", (O3*O3.T - sp.eye(3)).is_zero_matrix)
X3z = O3*sp.diag(sp.Rational(3, 5), -sp.Rational(5, 13), sp.Rational(8, 17))*O3.T
Y3z = O3*sp.diag(sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17))*O3.T
print("     {J0, I[Z]} exactly zero:", anticomm(X3z, Y3z).is_zero_matrix, "  X != 0:", not X3z.is_zero_matrix,
      "  Y eigenvalues:", sorted(Y3z.eigenvals().keys()))
# the claim's point Z = i, and the X = 0 slice
print("check Z = i (X=0,Y=1) is a zero, d=2:", anticomm(sp.zeros(2, 2), sp.eye(2)).is_zero_matrix)
yv = sp.Symbol("yv", positive=True)
print("X = 0 slice, d=1: S =", sp.simplify(yv - 1/yv), "-> zero only at yv =", sp.solve(yv - 1/yv, yv))
# a non-zero point off the set for contrast
print("contrast: Z = 3/5 + (1/2) i (|Z| != 1) gives nonzero:", anticomm(sp.Matrix([[sp.Rational(3, 5)]]), sp.Matrix([[sp.Rational(1, 2)]])).tolist())

print("\n=== Part 3: local dimension of the zero set (kernel of the linearized map) ===")
def jacobian_kernel_dim(X0, Y0):
    d = X0.shape[0]
    params = []
    dX = sp.zeros(d, d); dY = sp.zeros(d, d)
    for i in range(d):
        for j in range(i, d):
            a = sp.Symbol(f"a{i}{j}"); b = sp.Symbol(f"b{i}{j}")
            params += [a, b]
            dX[i, j] += a; dY[i, j] += b
            if i != j: dX[j, i] += a; dY[j, i] += b
    t = sp.Symbol("t")
    M = anticomm(X0 + t*dX, Y0 + t*dY)
    lin = [sp.diff(e, t).subs(t, 0) for e in M]
    Jm = sp.Matrix([[sp.diff(l, p) for p in params] for l in lin])
    # entries are exact Rationals; do NOT nsimplify (it replaced exact rationals by approximations in a first run)
    assert all(e.is_Rational for e in Jm)
    rank = Jm.rank()
    return len(params), rank, len(params) - rank
for d in (1, 2, 3):
    nP, rk, kd = jacobian_kernel_dim(sp.zeros(d, d), sp.eye(d))
    print(f"d={d} at Z=i: params={nP}, rank={rk}, kernel dim={kd}, d(d+1)/2={d*(d+1)//2}")
nP, rk, kd = jacobian_kernel_dim(X2, Y2)
print(f"d=2 at the X!=0 zero above: params={nP}, rank={rk}, kernel dim={kd}")
nP, rk, kd = jacobian_kernel_dim(X3z, Y3z)
print(f"d=3 at the X!=0 zero above: params={nP}, rank={rk}, kernel dim={kd}")

print("\n=== Part 4: group-theory anchor (independent of the block formulas) ===")
# The map Z -> {J0, I[Z]} is equivariant: for g in Sp(2d), H -> g^T H g sends I = omega^-1 H to g^-1 I g.
# If g also commutes with J0, {J0, g^-1 I g} = g^-1 {J0, I} g, so the zero set is invariant under the
# centralizer C of J0 in Sp(2d).  Its orbit through Z = i has dim = dim C - dim(C cap U(d)).
def nullspace_dim_of_conditions(d, extra_antisym=False):
    n2 = 2*d
    om = np.block([[np.zeros((d, d)), np.eye(d)], [-np.eye(d), np.zeros((d, d))]])
    J = np.block([[np.zeros((d, d)), np.eye(d)], [np.eye(d), np.zeros((d, d))]])
    rows = []
    for k in range(n2*n2):
        E = np.zeros(n2*n2); E[k] = 1; M = E.reshape(n2, n2)
        c = [(M.T@om + om@M).ravel(), (M@J - J@M).ravel()]
        if extra_antisym: c.append((M + M.T).ravel())
        rows.append(np.concatenate(c))
    L = np.array(rows).T
    s = np.linalg.svd(L, compute_uv=False)
    return n2*n2 - int(np.sum(s > 1e-10))
for d in (1, 2, 3, 4):
    c = nullspace_dim_of_conditions(d); st = nullspace_dim_of_conditions(d, True)
    print(f"d={d}: dim centralizer(J0) in sp(2d) = {c} (d^2={d*d}); stabilizer of Z=i inside it = {st}; orbit dim = {c-st} (d(d+1)/2={d*(d+1)//2})")

def expm(M, terms=40):
    nrm = np.linalg.norm(M, 1); s = max(0, int(np.ceil(np.log2(nrm))) + 1) if nrm > 0 else 0
    A = M / (2**s); E = np.eye(M.shape[0]); T = np.eye(M.shape[0])
    for k in range(1, terms):
        T = T@A/k; E = E + T
    for _ in range(s): E = E@E
    return E

def Z_from_H(H, d):
    Y = np.linalg.inv(H[d:, d:]); X = Y@H[d:, :d]
    return X, Y

rng2 = np.random.default_rng(3)
for d in (1, 2, 3, 4):
    om = np.block([[np.zeros((d, d)), np.eye(d)], [-np.eye(d), np.zeros((d, d))]])
    J = np.block([[np.zeros((d, d)), np.eye(d)], [np.eye(d), np.zeros((d, d))]])
    a = rng2.normal(size=(d, d)); a = (a - a.T)/2
    b = rng2.normal(size=(d, d)); b = (b + b.T)/2 * 0.7
    M = np.block([[a, b], [b, a]])
    g = expm(M)
    H1 = g.T@np.eye(2*d)@g
    X, Y = Z_from_H(H1, d)
    I1 = np.linalg.inv(om)@H1
    ac = J@I1 + I1@J
    sympl = np.max(np.abs(g.T@om@g - om)); comm = np.max(np.abs(g@J - J@g))
    print(f"d={d}: g symplectic err {sympl:.1e}, [g,J0] err {comm:.1e}; |{{J0,I[g.i]}}|max = {np.max(np.abs(ac)):.1e};"
          f" |X|max = {np.max(np.abs(X)):.3f}; [X,Y] err {np.max(np.abs(X@Y-Y@X)):.1e}; X^2+Y^2-1 err {np.max(np.abs(X@X+Y@Y-np.eye(d))):.1e}")
    # closed form for the pure-b generators: Z = tanh(2b) + i sech(2b)
    gb = expm(np.block([[np.zeros((d, d)), b], [b, np.zeros((d, d))]]))
    Xb, Yb = Z_from_H(gb.T@gb, d)
    w, V = np.linalg.eigh(b)
    th = V@np.diag(np.tanh(2*w))@V.T; se = V@np.diag(1/np.cosh(2*w))@V.T
    print(f"      pure-b orbit: X = tanh(2b) err {np.max(np.abs(Xb-th)):.1e}, Y = sech(2b) err {np.max(np.abs(Yb-se)):.1e}")
# d = 1 textbook picture: the centralizer is the hyperbolic one-parameter group [[cosh t, sinh t],[sinh t, cosh t]];
# its orbit through i is the geodesic with endpoints -1, +1, i.e. the unit semicircle.
for t in (-1.3, -0.4, 0.25, 0.9, 2.0):
    g = np.array([[np.cosh(t), np.sinh(t)], [np.sinh(t), np.cosh(t)]])
    X, Y = Z_from_H(g.T@g, 1)
    print(f"d=1, t={t:+.2f}: Z = {X[0,0]:+.4f} + {Y[0,0]:.4f} i, |Z| = {np.hypot(X[0,0], Y[0,0]):.12f}")

print("\n=== Part 5: the potential along and across the zero set; quadratic order ===")
phi = sp.Symbol("phi", real=True)
Mphi = anticomm(sp.Matrix([[sp.cos(phi)]]), sp.Matrix([[sp.sin(phi)]]))
V_phi = sp.simplify(sum(e**2 for e in Mphi))
print("d=1, Z = cos(phi) + i sin(phi): ||{J0,I}||_F^2 =", V_phi)
eps = sp.Symbol("eps")
for d in (1, 2):
    h = symsym("h", d); xx = symsym("u", d)
    Ye = sp.eye(d) + eps*h; Xe = eps*xx
    Mt = anticomm(Xe, Ye)
    Vn = sum(e**2 for e in Mt)                 # positive norm: 2Tr(S^2) + 2Tr(A^T A)
    ser = sp.series(Vn, eps, 0, 5).removeO()
    c2 = sp.expand(ser.coeff(eps, 2)); c4 = sp.expand(ser.coeff(eps, 4))
    print(f"d={d}: eps^2 coeff - 8Tr(h^2) =", sp.simplify(c2 - 8*(h*h).trace()),
          "| eps^2 coeff depends on x:", any(s.name.startswith('u') for s in c2.free_symbols),
          "| eps^4 coeff depends on x:", any(s.name.startswith('u') for s in c4.free_symbols))
    Yi = Ye.inv(); Se = Ye + Xe*Yi*Xe - Yi
    t4 = sp.simplify(sp.series((Se*Se).trace(), eps, 0, 3).removeO().coeff(eps, 2) - 4*(h*h).trace())
    print(f"      T4 analogue: [Tr(S^2)]_eps^2 - 4Tr(h^2) =", t4)
# along h = 0 the potential is quartic in x; along the curved valley y = sqrt(1-x^2) it vanishes
xs = sp.Symbol("xs", real=True)
print("d=1 straight line y=1: ||{J0,I}||^2 =", sp.series(sum(e**2 for e in anticomm(sp.Matrix([[xs]]), sp.Matrix([[1]]))), xs, 0, 7))
print("d=1 curved valley y=sqrt(1-x^2): ||{J0,I}||^2 =", sp.simplify(sum(e**2 for e in anticomm(sp.Matrix([[xs]]), sp.Matrix([[sp.sqrt(1 - xs**2)]])))))

print("\n=== Part 6: conventions ===")
d = 1
X1 = sp.Matrix([[sp.Rational(3, 5)]]); Y1 = sp.Matrix([[sp.Rational(4, 5)]])
omega, J0 = blocks(1)
H1 = HZ(X1, Y1)
for lbl, I in [("I = omega^-1 H", omega.inv()*H1), ("I = -omega^-1 H (flipped omega)", -omega.inv()*H1),
               ("I = H^-1 omega", H1.inv()*omega), ("I = H omega", H1*omega)]:
    print(f"Z = 3/5 + 4/5 i, {lbl}: I^2 = -1: {(I*I + sp.eye(2)).is_zero_matrix}; {{J0,I}} =", (J0*I + I*J0).tolist())
K0 = sp.diag(1, -1)
xg, yg = sp.symbols("xg yg", positive=True)
IK = omega.inv()*HZ(sp.Matrix([[xg]]), sp.Matrix([[yg]]))
print("other natural polarization K0 = diag(1,-1): {K0, I[Z]} =", sp.simplify(K0*IK + IK*K0).tolist(), "-> zero set X = 0, any Y")
# a generic H0-compatible J (J = U J0 U^-1, U in Sp(2d) cap O(2d) = U(d)): zero set dimension at Z = i
for d in (2, 3):
    rngu = np.random.default_rng(11 + d)
    a = rngu.normal(size=(d, d)); a = (a - a.T)/2; s = rngu.normal(size=(d, d)); s = (s + s.T)/2
    U = expm(np.block([[a, s], [-s, a]]))   # generator of u(d) inside sp(2d)
    om = np.block([[np.zeros((d, d)), np.eye(d)], [-np.eye(d), np.zeros((d, d))]])
    J = U@np.block([[np.zeros((d, d)), np.eye(d)], [np.eye(d), np.zeros((d, d))]])@np.linalg.inv(U)
    I0 = np.linalg.inv(om)@np.eye(2*d)
    cols = []
    for (i, j) in [(i, j) for i in range(d) for j in range(i, d)]:
        for which in ("X", "Y"):
            E = np.zeros((d, d)); E[i, j] = E[j, i] = 1
            h = 1e-6
            def ac(Xp, Yp):
                Yi = np.linalg.inv(Yp)
                Hp = np.block([[Yp + Xp@Yi@Xp, Xp@Yi], [Yi@Xp, Yi]])
                Ip = np.linalg.inv(om)@Hp
                return (J@Ip + Ip@J).ravel()
            Xp = h*E if which == "X" else np.zeros((d, d)); Yp = np.eye(d) + (h*E if which == "Y" else 0)
            Xm = -h*E if which == "X" else np.zeros((d, d)); Ym = np.eye(d) - (h*E if which == "Y" else 0)
            cols.append((ac(Xp, Yp) - ac(Xm, Ym))/(2*h))
    Jac = np.array(cols).T
    sv = np.linalg.svd(Jac, compute_uv=False)
    print(f"d={d}: generic U(d)-rotated polarization J: {{J,I0}} = 0: {np.allclose(J@I0 + I0@J, 0)}, J^2 = 1: {np.allclose(J@J, np.eye(2*d))};"
          f" kernel dim of linearized map at Z = i = {Jac.shape[1] - int(np.sum(sv > 1e-6))}")
