"""Two-body problem with a relative-velocity-gated correction to Newtonian gravity.

Model (per pair):  L = m1 v1^2/2 + m2 v2^2/2 + (G m1 m2 / r) [1 + eps W(|v1 - v2|/v*)]
i.e. V = -(G m1 m2/r)[1 + eps W], entering the Lagrangian as L = T - V.
Galilean invariant, so the relative motion is a reduced-mass problem:
  L_rel = mu v^2/2 + (k/r)[1 + eps W(v/v*)],  k = G m1 m2,  k/mu = G M.

Part A (sympy): circular-orbit Kepler constant, first-order Hamiltonian, small-e precession,
                 and an independent anchor (textbook GR 1PN test-particle precession 6 pi GM/(c^2 a(1-e^2))
                 reproduced by the same averaging machinery, including its velocity-dependent term).
Part B (numpy): direct integration of the Euler-Lagrange equations (velocity-dependent, so the
                 acceleration solves a 2x2 linear system), compared with the formulas.
"""
import numpy as np
import sympy as sp

print("=" * 78)
print("PART A: symbolic derivation")
print("=" * 78)

mu, k, eps, vs, r, rd, thd = sp.symbols('mu k epsilon v_s r rdot thetadot', positive=True)
u = sp.symbols('u', positive=True)
Wf = sp.Function('W')

v = sp.sqrt(rd**2 + r**2 * thd**2)
L = mu / 2 * (rd**2 + r**2 * thd**2) + k / r * (1 + eps * Wf(v / vs))

# Radial Euler-Lagrange equation on a circular orbit: rdot = 0 and rddot = 0, so
# d/dt(dL/drdot) = 0 there (dL/drdot is proportional to rdot, its time derivative vanishes when
# rdot = rddot = 0 identically). Condition: dL/dr = 0.
dLdr = sp.diff(L, r)
circ = sp.simplify(dLdr.subs(rd, 0))
# write v = r*thetadot = u*v_s
vv = sp.symbols('v', positive=True)
circ_v = sp.simplify(circ.subs(thd, vv / r))
print("dL/dr on circular orbit:", circ_v)
# Solve for v^2 r * mu / k
sol = sp.solve(sp.Eq(circ_v, 0), k)[0]
# GM_eff = v^2 r = (k/mu)*X  ->  X = k/(mu v^2 r)
X = sp.simplify((mu * vv**2 * r) / sol)
print("(mu v^2 r)/k on a circular orbit =", sp.simplify(X))
# Expected: 1 + eps (W(u) - u W'(u)), i.e. v^2 r = (k/mu) [1 + eps(W - u W')], exact for circular orbits
for name, Wexpr in [("Gaussian", sp.exp(-u**2)), ("Lorentzian", 1 / (1 + u**2))]:
    Xc = X.subs(Wf(vv / vs), Wexpr.subs(u, vv / vs))
    Xc = Xc.replace(lambda ex: isinstance(ex, sp.Subs), lambda ex: sp.diff(Wexpr, u).subs(u, ex.point[0]))
    Kexp = 1 + eps * (Wexpr - u * sp.diff(Wexpr, u)).subs(u, vv / vs)
    print(f"  check (mu v^2 r)/k = 1 + eps (W - u W') exactly, {name}:", sp.simplify(Xc - Kexp) == 0)

# Concrete shapes: K(u) = W - u W'
for name, Wexpr in [("Gaussian exp(-u^2)", sp.exp(-u**2)), ("Lorentzian 1/(1+u^2)", 1 / (1 + u**2))]:
    K = sp.simplify(Wexpr - u * sp.diff(Wexpr, u))
    dK = sp.diff(K, u)
    crit = [c for c in sp.solve(sp.Eq(dK, 0), u) if c.is_positive]
    print(f"{name}: K(u) = W - uW' = {sp.factor(K)};  max at u = {crit}, K_max = {[sp.nsimplify(K.subs(u, c)) for c in crit]} = {[float(K.subs(u, c)) for c in crit]}")

# First-order Hamiltonian: H = p.v - L  with p = dL/dv.  Check H = p^2/(2mu) - (k/r)(1+eps W(p/(mu v*))) + O(eps^2)
# 1D radial-free check (pure speed variable is enough because L depends on |v| only)
p = sp.symbols('p', positive=True)
Wg = sp.exp(-u**2)  # concrete W for the series check (the statement is general; checked for two shapes)
for name, Wexpr in [("Gaussian", sp.exp(-u**2)), ("Lorentzian", 1 / (1 + u**2))]:
    Lspeed = mu * vv**2 / 2 + k / r * (1 + eps * Wexpr.subs(u, vv / vs))
    pexpr = sp.diff(Lspeed, vv)
    # invert p(v) to first order in eps: v = p/mu + eps*v1
    v1 = sp.symbols('v1')
    vtrial = p / mu + eps * v1
    eq = sp.series(pexpr.subs(vv, vtrial) - p, eps, 0, 2).removeO()
    v1sol = sp.solve(sp.Eq(sp.expand(eq).coeff(eps, 1), 0), v1)[0]
    vsol = p / mu + eps * v1sol
    H = sp.series((p * vv - Lspeed).subs(vv, vsol), eps, 0, 2).removeO()
    Hexp = p**2 / (2 * mu) - k / r * (1 + eps * Wexpr.subs(u, p / (mu * vs)))
    print(f"first-order Hamiltonian H = p^2/2mu - (k/r)(1+eps W(p/mu v*)) for {name}:",
          sp.simplify(sp.expand(H - Hexp)) == 0)

# Small-e precession from the averaged perturbation  <h1> = -eps (GM/a) Phi(e),
# Phi = (1/2pi) int_0^{2pi} W(u_c sqrt((1+e cosE)/(1-e cosE))) dE;  Delta omega/orbit = 2 pi eps sqrt(1-e^2)/e dPhi/de
e, E, uc = sp.symbols('e E u_c', positive=True)
s = sp.sqrt((1 + e * sp.cos(E)) / (1 - e * sp.cos(E)))
for name, Wexpr in [("Gaussian", sp.exp(-u**2)), ("Lorentzian", 1 / (1 + u**2)), ("W=u^2 (anchor form)", u**2)]:
    integrand = Wexpr.subs(u, uc * s)
    ser = sp.series(integrand, e, 0, 3).removeO()
    Phi2 = sp.integrate(sp.expand(ser), (E, 0, 2 * sp.pi)) / (2 * sp.pi)
    Phi2 = sp.simplify(Phi2)
    dom = sp.simplify(sp.limit(2 * sp.pi * sp.sqrt(1 - e**2) / e * sp.diff(Phi2, e), e, 0))
    formula = sp.simplify(sp.pi * uc * sp.diff(uc * sp.diff(Wexpr.subs(u, uc), uc), uc))
    print(f"{name}: small-e Delta omega/eps = {sp.factor(dom)} ; pi*u*(u W')' = {sp.factor(formula)} ; equal: {sp.simplify(dom - formula) == 0}")

# Exact-in-e result for W = u^2: (1+x)/(1-x) = -1 + 2/(1-x); <1/(1 - e cosE)>_E = 1/sqrt(1-e^2) (standard;
# sympy's antiderivative mishandles the branch, so the average is checked numerically here)
import mpmath as mp
for ev in [0.1, 0.5, 0.9]:
    num = mp.quad(lambda EE: 1 / (1 - ev * mp.cos(EE)), [0, 2 * mp.pi]) / (2 * mp.pi)
    print(f"  <1/(1-e cosE)> at e={ev}: quad = {mp.nstr(num, 15)}, 1/sqrt(1-e^2) = {mp.nstr(1 / mp.sqrt(1 - ev**2), 15)}")
Phi_exact = -1 + 2 / sp.sqrt(1 - e**2)
dom_u2 = sp.simplify(2 * sp.pi * sp.sqrt(1 - e**2) / e * sp.diff(uc**2 * Phi_exact, e))
print("W = u^2: Delta omega/eps exact in e =", dom_u2)

# Independent anchor (textbook GR): test-particle 1PN Hamiltonian per unit mass (isotropic gauge)
#   h1 = -p^4/(8c^2) - (3/2)(GM/r) p^2/c^2 + (GM)^2/(2 r^2 c^2)
# total perihelion advance per orbit must be 6 pi GM / (c^2 a (1-e^2)).
GM, a, c = sp.symbols('GM a c', positive=True)
Lam, Gd = sp.symbols('L G', positive=True)  # Delaunay L = sqrt(GM a), G = L sqrt(1-e^2)
inv_r = 1 / a
inv_r2 = 1 / (a**2 * sp.sqrt(1 - e**2))
v2_over_r = GM * (2 * inv_r2 - inv_r / a)       # <v^2/r>, v^2 = GM(2/r - 1/a)
v4 = GM**2 * (4 * inv_r2 - 4 * inv_r / a + 1 / a**2)  # <v^4>
h1 = -v4 / (8 * c**2) - sp.Rational(3, 2) * v2_over_r / c**2 * GM / GM * 1 + GM**2 / (2 * c**2) * inv_r2
# note: the middle term is -(3/2) GM <p^2/r>/c^2 = -(3/2) <v^2 * GM / r>/c^2 ; v2_over_r already carries GM
h1 = -v4 / (8 * c**2) - sp.Rational(3, 2) * GM * (2 * inv_r2 - inv_r / a) * GM / c**2 + GM**2 / (2 * c**2) * inv_r2
h1_del = h1.subs({a: Lam**2 / GM}).subs({e: sp.sqrt(1 - Gd**2 / Lam**2)})
domdt = sp.diff(h1_del, Gd)
dom_orbit = sp.simplify((domdt * 2 * sp.pi * a**sp.Rational(3, 2) / sp.sqrt(GM)).subs({Gd: Lam * sp.sqrt(1 - e**2)}).subs({Lam: sp.sqrt(GM * a)}))
print("anchor: GR 1PN test-particle advance per orbit from averaged h1 =", sp.simplify(dom_orbit),
      "; textbook 6 pi GM/(c^2 a (1-e^2)) reproduced:", sp.simplify(dom_orbit - 6 * sp.pi * GM / (c**2 * a * (1 - e**2))) == 0)
# the velocity-dependent interaction term alone, -(3/2)(GM/r)(p^2/c^2), is W = u^2 with eps/v*^2 = (3/2)/c^2:
print("  velocity-dependent GR term alone (W=u^2, eps/v*^2 = 3/(2c^2)):",
      sp.simplify(dom_u2.subs(uc, sp.sqrt(GM / a) / vs) * sp.Rational(3, 2) * vs**2 / c**2))

print()
print("=" * 78)
print("PART B: numerical integration of the Euler-Lagrange equations")
print("=" * 78)
# Units: GM = 1, reduced mass 1. L = v^2/2 + (1/r)(1 + eps W(|v|/vs)).


def make_W(shape):
    if shape == 'gauss':
        W = lambda x: np.exp(-x * x)
        W1 = lambda x: -2 * x * np.exp(-x * x)
        W2 = lambda x: (4 * x * x - 2) * np.exp(-x * x)
    else:
        W = lambda x: 1.0 / (1 + x * x)
        W1 = lambda x: -2 * x / (1 + x * x)**2
        W2 = lambda x: (6 * x * x - 2) / (1 + x * x)**3
    return W, W1, W2


def accel(state, eps, vs, Wt):
    """Euler-Lagrange: (d2L/dv dv) a = dL/dr - (d2L/dv dr) v, with L = v^2/2 + f(r) g(|v|)."""
    W, W1, W2 = Wt
    x, y, vx, vy = state
    rr = (x * x + y * y) ** 0.5
    sp_ = (vx * vx + vy * vy) ** 0.5
    rhx, rhy = x / rr, y / rr
    vhx, vhy = vx / sp_, vy / sp_
    f = 1.0 / rr
    fp = -1.0 / (rr * rr)
    xs = sp_ / vs
    g = 1 + eps * W(xs)
    g1 = eps * W1(xs) / vs
    g2 = eps * W2(xs) / (vs * vs)
    # A = alpha I + beta vh vh^T ; A^{-1} = (1/alpha)[I - beta/(alpha+beta) vh vh^T]
    alpha = 1 + f * g1 / sp_
    beta = f * (g2 - g1 / sp_)
    rdotv = rhx * vx + rhy * vy
    bx = fp * g * rhx - fp * g1 * vhx * rdotv
    by = fp * g * rhy - fp * g1 * vhy * rdotv
    proj = vhx * bx + vhy * by
    cfac = beta / (alpha + beta)
    ax = (bx - cfac * proj * vhx) / alpha
    ay = (by - cfac * proj * vhy) / alpha
    return np.array([vx, vy, ax, ay])


def rk4(state, h, eps, vs, Wt):
    k1 = accel(state, eps, vs, Wt)
    k2 = accel(state + 0.5 * h * k1, eps, vs, Wt)
    k3 = accel(state + 0.5 * h * k2, eps, vs, Wt)
    k4 = accel(state + h * k3, eps, vs, Wt)
    return state + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def precession_numeric(eps, vs, ecc, shape, norbits=12, nsteps=6000):
    Wt = make_W(shape)
    # start at periapsis of the zeroth-order Kepler ellipse with a=1
    rp = 1 - ecc
    vp = np.sqrt((1 + ecc) / (1 - ecc))
    st = np.array([rp, 0.0, 0.0, vp])
    h = 2 * np.pi / nsteps
    peri_angles = []
    prev_rv = None
    prev = st.copy()
    unwrapped = 0.0
    lastang = 0.0
    for i in range(int(norbits * nsteps * 1.05)):
        new = rk4(st, h, eps, vs, Wt)
        rv_old = st[0] * st[2] + st[1] * st[3]
        rv_new = new[0] * new[2] + new[1] * new[3]
        ang = np.arctan2(new[1], new[0])
        d = ang - lastang
        if d < -np.pi:
            d += 2 * np.pi
        if d > np.pi:
            d -= 2 * np.pi
        unwrapped_new = unwrapped + d
        if rv_old < 0 <= rv_new:
            frac = -rv_old / (rv_new - rv_old)
            peri_angles.append(unwrapped + frac * (unwrapped_new - unwrapped))
        unwrapped = unwrapped_new
        lastang = ang
        st = new
        if len(peri_angles) >= norbits:
            break
    pa = np.array(peri_angles)
    n = np.arange(len(pa))
    slope = np.polyfit(n, pa, 1)[0]
    return slope - 2 * np.pi


def Phi_e(uc, ecc, shape, n=4096):
    W, W1, _ = make_W(shape)
    Eg = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = ecc * np.cos(Eg)
    s_ = np.sqrt((1 + x) / (1 - x))
    ds_de = np.cos(Eg) / (s_ * (1 - x)**2)
    return np.mean(W1(uc * s_) * uc * ds_de)


def dom_formula(uc, ecc, shape):
    """precession per orbit per unit eps, exact in e (first order in eps)."""
    return 2 * np.pi * np.sqrt(1 - ecc**2) / ecc * Phi_e(uc, ecc, shape)


def dom_small_e(uc, shape):
    W, W1, W2 = make_W(shape)
    return np.pi * uc * (W1(uc) + uc * W2(uc))


print("Precession per orbit: numerical (exact EL equations) vs first-order formula")
print(f"{'shape':>6} {'u_c':>5} {'e':>5} {'eps':>7} {'numeric/eps':>13} {'formula':>13} {'small-e':>13} {'rel.diff':>9}")
base = {}
for shape in ['gauss', 'lorentz']:
    for ecc in [0.1, 0.3]:
        # Newtonian numerical drift (eps = 0) to subtract
        base[(shape, ecc)] = precession_numeric(0.0, 1.0, ecc, shape)
for shape in ['gauss', 'lorentz']:
    for uc_ in [0.5, 1.0, 1.6, 3.0]:
        vs_ = 1.0 / uc_
        for ecc in [0.1, 0.3]:
            for epsv in [1e-3, 5e-4]:
                num = (precession_numeric(epsv, vs_, ecc, shape) - base[(shape, ecc)]) / epsv
                frm = dom_formula(uc_, ecc, shape)
                se = dom_small_e(uc_, shape)
                rd_ = (num - frm) / abs(frm) if abs(frm) > 1e-12 else float('nan')
                print(f"{shape:>6} {uc_:5.2f} {ecc:5.2f} {epsv:7.0e} {num:13.6e} {frm:13.6e} {se:13.6e} {rd_:9.2e}")
print("Newtonian RK4 drift per orbit (subtracted):", {kk: f"{vv_:.1e}" for kk, vv_ in base.items()})
# Lorentzian at u_c = 1: 1/(1+s^2) = (1 - e cosE)/2, so Phi = 1/2 for every e and the first-order precession vanishes
for ecc in [0.05, 0.2, 0.6]:
    Eg = np.linspace(0, 2 * np.pi, 4096, endpoint=False)
    x = ecc * np.cos(Eg)
    print(f"  Lorentzian, u_c = 1: Phi(e={ecc}) = {np.mean(1 / (1 + (1 + x) / (1 - x))):.15f}")

print()
print("Circular orbits: Kepler constant  omega^2 r^3 = GM [1 + eps K(u)],  K = W - u W'")
print(f"{'shape':>6} {'u':>5} {'eps':>7} {'K_formula':>10} {'K_numeric':>10} {'r osc (formula IC)':>19} {'r osc (naive IC)':>17}")


def circ_test(eps, vs, shape, nsteps=4000, norb=3):
    W, W1, W2 = make_W(shape)
    Kf = lambda x: W(x) - x * W1(x)
    # solve v^2 * 1 = 1 + eps K(v/vs) at r = 1
    vv_ = 1.0
    for _ in range(50):
        vv_ = np.sqrt(1 + eps * Kf(vv_ / vs))
    Wt = make_W(shape)
    out = []
    for v0 in [vv_, 1.0]:
        st = np.array([1.0, 0.0, 0.0, v0])
        h = 2 * np.pi / nsteps
        rs = []
        angs = []
        t = 0.0
        unwr = 0.0
        last = 0.0
        for i in range(nsteps * norb):
            st = rk4(st, h, eps, vs, Wt)
            t += h
            rs.append(np.hypot(st[0], st[1]))
            ang = np.arctan2(st[1], st[0])
            d = ang - last
            if d < -np.pi:
                d += 2 * np.pi
            unwr += d
            last = ang
        omega = unwr / t
        rs = np.array(rs)
        out.append((omega, rs.max() - rs.min(), rs.mean()))
    (om, osc, rmean), (_, osc_naive, _) = out
    Knum = (om**2 * rmean**3 - 1) / eps
    return Kf(vv_ / vs), Knum, osc, osc_naive


for shape in ['gauss', 'lorentz']:
    for uc_ in [0.5, 0.7071, 1.0, 2.0]:
        epsv = 1e-3
        Kf_, Kn, osc, oscn = circ_test(epsv, 1.0 / uc_, shape)
        print(f"{shape:>6} {uc_:5.2f} {epsv:7.0e} {Kf_:10.6f} {Kn:10.6f} {osc:19.2e} {oscn:17.2e}")
