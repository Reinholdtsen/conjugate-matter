"""Critic check c1: how a single long-range exchange can depend on the relative
velocity of two bodies.

Claim checked (critic gap G4): tree-level exchange of a spin-J field between two
point sources T_i = m_i u_i^(x)J gives a residue proportional to a polynomial of
degree J in gamma = u1.u2 (Legendre P_J for a massive field, Chebyshev T_J for a
massless one; J = 2 reproduces P7 of the program analysis).  Relative-velocity
dependence therefore enters as J(J+1)/4 (v/c)^2 or J^2/2 (v/c)^2, never as a gate
at v* << c unless J ~ c/v*.

Part A  (algebra, d-dimensional Euclidean): the contraction of the traceless
        projection of a^(x)J with b^(x)J is proportional to the Gegenbauer
        polynomial C_J^{(d-2)/2}(cos theta): Chebyshev in d = 2, Legendre in d = 3.
        Checked by (i) explicit traceless tensors for J = 2, 3 and (ii) harmonicity
        of |x|^J C_J(a.x/|x|) for J = 1..6 (the zonal-harmonic characterization).
        The Lorentzian exchange numerators are the analytic continuation
        (massive: 3 dims orthogonal to q -> P_J; massless: 2 physical dims -> T_J)
        [T, dagger: standard spin-J projectors].
Part B  series of P_J(gamma), T_J(gamma) in beta = v/c with exact gamma(beta).
Part C  spin needed for an O(1) change at v = v* = 120 km/s.
Part D  the only polynomial way to get a velocity scale v* << c: near-cancellation
        of an attractive J=0 and a repulsive J=1 exchange.
"""
import sympy as sp

print("=== Part A: traceless contractions = Gegenbauer polynomials ===")
c = sp.symbols('c', real=True)  # cos(theta) between unit vectors a, b

# explicit traceless projections, unit vectors, contraction with b^(x)J
# J=2, dimension d: Pi_ij = a_i a_j - delta_ij/d ;  Pi.bb = c^2 - 1/d
for d in (2, 3):
    J2 = c**2 - sp.Rational(1, d)
    # J=3: Pi_ijk = a_i a_j a_k - (1/(d+2)) (delta_ij a_k + perms);  Pi.bbb = c^3 - 3c/(d+2)
    J3 = c**3 - sp.Rational(3, d + 2) * c
    if d == 2:
        ref2, ref3 = sp.chebyshevt(2, c), sp.chebyshevt(3, c)
    else:
        ref2, ref3 = sp.legendre(2, c), sp.legendre(3, c)
    r2 = sp.simplify(J2 / ref2)
    r3 = sp.simplify(J3 / ref3)
    print(f"d = {d}: J=2 contraction / {'T_2' if d==2 else 'P_2'} = {r2} (constant: {r2.is_constant()}); "
          f"J=3 contraction / {'T_3' if d==2 else 'P_3'} = {r3} (constant: {r3.is_constant()})")

# zonal harmonics: |x|^J * C_J(a.x/|x|) is harmonic iff C_J is the right Gegenbauer
x, y, z = sp.symbols('x y z', real=True)
ok2, ok3 = [], []
for J in range(1, 7):
    r = sp.sqrt(x**2 + y**2)
    h2 = sp.expand(sp.simplify(r**J * sp.chebyshevt(J, x / r)))
    lap2 = sp.simplify(sp.diff(h2, x, 2) + sp.diff(h2, y, 2))
    ok2.append(lap2 == 0)
    R = sp.sqrt(x**2 + y**2 + z**2)
    h3 = sp.expand(sp.simplify(R**J * sp.legendre(J, x / R)))
    lap3 = sp.simplify(sp.diff(h3, x, 2) + sp.diff(h3, y, 2) + sp.diff(h3, z, 2))
    ok3.append(lap3 == 0)
print("harmonic |x|^J T_J(a.x/|x|) in d=2, J=1..6:", ok2)
print("harmonic |x|^J P_J(a.x/|x|) in d=3, J=1..6:", ok3)

print("\n=== Part B: relative-velocity series, gamma = (1 - beta^2)^(-1/2) ===")
b = sp.symbols('beta', positive=True)
gam = 1 / sp.sqrt(1 - b**2)
print(" J | massive P_J(gamma)                      | massless T_J(gamma)")
for J in range(0, 5):
    sP = sp.series(sp.legendre(J, gam), b, 0, 5).removeO()
    sT = sp.series(sp.chebyshevt(J, gam), b, 0, 5).removeO()
    print(f" {J} | {str(sp.expand(sP)):40s} | {sp.expand(sT)}")
Jsym = sp.symbols('J', positive=True, integer=True)
# general first-order coefficients: P_J'(1) = J(J+1)/2, T_J'(1) = J^2; gamma - 1 = beta^2/2 + ...
for J in range(0, 7):
    cP = sp.diff(sp.legendre(J, c), c).subs(c, 1) / 2
    cT = sp.diff(sp.chebyshevt(J, c), c).subs(c, 1) / 2
    assert cP == sp.Rational(J * (J + 1), 4) and cT == sp.Rational(J * J, 2)
print("first-order coefficient of beta^2: massive J(J+1)/4, massless J^2/2 (checked J = 0..6): True")
print("anchors: J=2 massive 3/2, massless 2 (program P7); J=1 both 1/2 (Darwin-type gamma)")

print("\n=== Part C: spin needed for an O(1) velocity effect at v = v* ===")
cl = 299792.458
for vs in (30.0, 120.0, 300.0):
    beta2 = (vs / cl) ** 2
    Jm = float(sp.nsolve(Jsym * (Jsym + 1) / 4 * beta2 - 1, Jsym, 2 * cl / vs))
    Jl = float(sp.sqrt(2 / beta2))
    print(f"v* = {vs:6.1f} km/s: (v*/c)^2 = {beta2:.3e}; J(J+1)/4 (v*/c)^2 = 1 at J = {Jm:.0f} (massive), "
          f"J^2/2 (v*/c)^2 = 1 at J = {Jl:.0f} (massless)")

print("\n=== Part D: near-cancelling J=0 attraction + J=1 repulsion ===")
# residue f(gamma) = -a + b*gamma (units of the vector strength b), a = b(1 + delta)
# f = -b*delta + b(gamma - 1) ~ -b delta + b beta^2/2 : attractive below v* = c sqrt(2 delta)
for vs in (120.0,):
    delta = (vs / cl) ** 2 / 2
    print(f"v* = {vs} km/s needs delta = (v*/c)^2/2 = {delta:.3e}: each component is 1/delta = {1/delta:.3e} times the residual static force")
    for v in (0.0, 60.0, 120.0, 300.0, 1000.0, 2600.0):
        g = 1 / sp.sqrt(1 - (v / cl) ** 2)
        f = (-(1 + delta) + g) / delta   # in units of the static residual (-1 = attraction of unit strength)
        print(f"   relative speed {v:7.1f} km/s: force / |static residual| = {float(-f):+.4e}  (+ attractive, - repulsive)")
