#!/usr/bin/env python3
"""P3 (label: program). Mechanics of momentum-dependent two-body interactions.

Models:
 (a) H = p1^2/2m1 + p2^2/2m2 + U(argument), U depending only on momenta (the literal Born image of a
     position potential, and the chat-only 'Yukawa in momentum' read as a potential);
 (b) L = sum m v^2/2 + Gt m1 m2 W(|v1 - v2|/v*)/r, W(0) = 1: a long-range force gated in relative velocity;
     first-order Hamiltonian H = sum p^2/2m - Gt m1 m2 W(|p1/m1 - p2/m2|/v*)/r;
 (c) the gated contact interaction of notes/stream-stability.md, smoothed: U = -g delta_eps(r) G((p1-p2)/mu).
For each: Hamilton's equations, the Lagrangian to first order, Galilean invariance of the argument,
the momentum-velocity relation, and numerical two-body examples for (b) and (c).
Reductions stated where made (planar motion; relative coordinate; units GM = mu = v* = 1 in the numerics).
"""
import sympy as sp
import numpy as np
import mpmath as mp

# ---------------------------------------------------------------- (a)
print("== (a) U depends on momenta only")
m1, m2, t = sp.symbols('m1 m2 t', positive=True)
x1 = sp.Matrix(sp.symbols('x1_1:4', real=True)); x2 = sp.Matrix(sp.symbols('x2_1:4', real=True))
p1 = sp.Matrix(sp.symbols('p1_1:4', real=True)); p2 = sp.Matrix(sp.symbols('p2_1:4', real=True))
U = sp.Function('U')
Mt = m1 + m2
args = {
    'p1 - p2': p1 - p2,
    'k = (m2 p1 - m1 p2)/M': (m2*p1 - m1*p2)/Mt,
    'p1/m1 - p2/m2': p1/m1 - p2/m2,
}
for name, s in args.items():
    H = p1.dot(p1)/(2*m1) + p2.dot(p2)/(2*m2) + U(*s)
    pdot1 = [-sp.diff(H, q) for q in x1]
    xdot1 = [sp.diff(H, q) for q in p1]
    xdot2 = [sp.diff(H, q) for q in p2]
    # Galilean generator K = m1 x1 + m2 x2 - t P:  dK/dt = sum m_i xdot_i - P
    dK = sp.simplify(sp.Matrix([m1*xdot1[i] + m2*xdot2[i] - (p1[i] + p2[i]) for i in range(3)]))
    # canonical boost p_i -> p_i + m_i u
    u = sp.Matrix(sp.symbols('u1:4', real=True))
    s_boost = s.subs({**{p1[i]: p1[i] + m1*u[i] for i in range(3)}, **{p2[i]: p2[i] + m2*u[i] for i in range(3)}},
                     simultaneous=True)
    shift = sp.simplify(s_boost - s)
    print(f"argument {name}: pdot_1 = {pdot1}; xdot_1 - p1/m1 = {[sp.simplify(xdot1[i] - p1[i]/m1) for i in range(1)]}...;")
    print(f"   d(m1 x1 + m2 x2)/dt - P = {list(dK)}; argument shift under boost = {list(shift)}")
# Lagrangian to first order (1D suffices for the structure)
P1, P2, V1, V2, ep = sp.symbols('P1 P2 V1 V2 epsilon', real=True)
u1f = sp.Function('u')
H1 = P1**2/(2*m1) + P2**2/(2*m2) + ep*u1f(P1 - P2)
# invert v = dH/dp to O(eps): p = m v - eps m U'(m1 v1 - m2 v2)
P1s = m1*V1 - ep*m1*sp.diff(u1f(P1 - P2), P1).subs({P1: m1*V1, P2: m2*V2})
P2s = m2*V2 - ep*m2*sp.diff(u1f(P1 - P2), P2).subs({P1: m1*V1, P2: m2*V2})
chk1 = sp.series((sp.diff(H1, P1).subs({P1: P1s, P2: P2s}) - V1), ep, 0, 2).removeO()
Lag = P1s*V1 + P2s*V2 - H1.subs({P1: P1s, P2: P2s})
Lag1 = sp.series(Lag, ep, 0, 2).removeO()
print("Legendre check with generic U (sympy Subs expansion):", sp.simplify(chk1) == 0)
# the same check with a concrete U, where sympy expands the shifted argument reliably
uc = lambda z: z**3/3 + sp.sin(z) + sp.exp(-z**2)
H1c = P1**2/(2*m1) + P2**2/(2*m2) + ep*uc(P1 - P2)
P1c = m1*V1 - ep*m1*sp.diff(uc(P1 - P2), P1).subs({P1: m1*V1, P2: m2*V2})
P2c = m2*V2 - ep*m2*sp.diff(uc(P1 - P2), P2).subs({P1: m1*V1, P2: m2*V2})
chk1c = [sp.simplify(sp.series(sp.diff(H1c, Pk).subs({P1: P1c, P2: P2c}) - Vk, ep, 0, 2).removeO()) for Pk, Vk in [(P1, V1), (P2, V2)]]
Lagc = sp.series(P1c*V1 + P2c*V2 - H1c.subs({P1: P1c, P2: P2c}), ep, 0, 2).removeO()
print("Legendre check with concrete U = s^3/3 + sin s + exp(-s^2): v recovered to O(eps):", chk1c,
      "; L - [sum m v^2/2 - eps U(m1 v1 - m2 v2)] =", sp.simplify(Lagc - (m1*V1**2/2 + m2*V2**2/2 - ep*uc(m1*V1 - m2*V2))))
print("L to O(eps) - [m1 v1^2/2 + m2 v2^2/2 - eps U(m1 v1 - m2 v2)] =",
      sp.simplify(Lag1 - (m1*V1**2/2 + m2*V2**2/2 - ep*u1f(m1*V1 - m2*V2))))
# inertia: d xdot1/d p1
print("d xdot1/d p1 (1D) =", sp.diff(sp.diff(H1, P1), P1), " (inverse mass shifted by U'')")
# literal Born image of a position potential: rho: (x, p) -> (p, -x)
xs, ps = sp.symbols('x_s p_s', real=True)
Vf = sp.Function('V')
H_orig = ps**2/(2*m1) + Vf(xs)
H_img = H_orig.subs({xs: ps, ps: -xs}, simultaneous=True)
print("Born image of p^2/2m + V(x):", H_img, "-> xdot =", sp.diff(H_img, ps), ", pdot =", -sp.diff(H_img, xs))

# ---------------------------------------------------------------- (b)
print("\n== (b) Newtonian potential gated in relative velocity")
Gt, vs = sp.symbols('Gtilde v_star', positive=True)
X1 = sp.Matrix(sp.symbols('X1_1:4', real=True)); X2 = sp.Matrix(sp.symbols('X2_1:4', real=True))
W1 = sp.Matrix(sp.symbols('W1_1:4', real=True)); W2 = sp.Matrix(sp.symbols('W2_1:4', real=True))
W = sp.Function('W')
d = X1 - X2; r = sp.sqrt(d.dot(d))
wrel = sp.sqrt((W1 - W2).dot(W1 - W2))/vs
L = m1*W1.dot(W1)/2 + m2*W2.dot(W2)/2 + Gt*m1*m2*W(wrel)/r
pc1 = sp.Matrix([sp.diff(L, q) for q in W1]); pc2 = sp.Matrix([sp.diff(L, q) for q in W2])
Efun = sp.simplify(pc1.dot(W1) + pc2.dot(W2) - L)
wsym = sp.symbols('w', positive=True)
Wexpr = W(wsym) - wsym*sp.diff(W(wsym), wsym)
target = m1*W1.dot(W1)/2 + m2*W2.dot(W2)/2 - Gt*m1*m2/r*Wexpr.subs(wsym, wrel)
print("energy function - [sum m v^2/2 - Gt m1 m2 (W - w W')/r] =", sp.simplify(sp.expand(Efun - target.doit())))
print("canonical p1 - m1 v1 (first component):", sp.simplify(pc1[0] - m1*W1[0]))
# Galilean boost of the Lagrangian
uu = sp.Matrix(sp.symbols('u1:4', real=True))
Lb = L.subs({**{X1[i]: X1[i] + uu[i]*t for i in range(3)}, **{X2[i]: X2[i] + uu[i]*t for i in range(3)},
             **{W1[i]: W1[i] + uu[i] for i in range(3)}, **{W2[i]: W2[i] + uu[i] for i in range(3)}}, simultaneous=True)
dL = sp.simplify(sp.expand(Lb - L))
total = sp.simplify(dL - (uu.dot(m1*W1 + m2*W2) + Mt*uu.dot(uu)/2))
print("L(boosted) - L - [u.(m1 v1 + m2 v2) + M u^2/2] =", total, " (remainder is d/dt[u.(m1x1+m2x2) + M u^2 t/2])")
# relative-motion Hessian at v_rel = 0 for W = exp(-w^2)
mu_r, Mtot, rr = sp.symbols('mu M r', positive=True)
q = sp.Matrix(sp.symbols('q1:4', real=True))
Lrel = mu_r*q.dot(q)/2 + Gt*Mtot*mu_r*sp.exp(-q.dot(q)/vs**2)/rr
Hes = sp.Matrix(3, 3, lambda i, j: sp.diff(Lrel, q[i], q[j])).subs({q[0]: 0, q[1]: 0, q[2]: 0})
print("Lagrangian Hessian at v_rel = 0 (Gaussian W):", sp.simplify(Hes[0, 0]), "* identity -> zero at r_* = 2 Gt M/v*^2:",
      sp.solve(sp.Eq(Hes[0, 0], 0), rr))
# first-order Hamiltonian and its Legendre check (1D)
Pr, Vr, eg = sp.symbols('P_r V_r eta', real=True)
Wg = lambda z: sp.exp(-z**2)
Hrel = Pr**2/(2*mu_r) - eg*Gt*Mtot*mu_r*Wg(Pr/(mu_r*vs))/rr
Prs = mu_r*Vr + eg*Gt*Mtot*mu_r*sp.diff(Wg(Pr/(mu_r*vs)), Pr).subs(Pr, mu_r*Vr)/rr*mu_r
chk = sp.series(sp.diff(Hrel, Pr).subs(Pr, Prs) - Vr, eg, 0, 2).removeO()
Lr = sp.series(Prs*Vr - Hrel.subs(Pr, Prs), eg, 0, 2).removeO()
print("first-order Legendre check:", sp.simplify(chk) == 0, "; L - [mu v^2/2 + eta Gt M mu W(v/v*)/r] =",
      sp.simplify(Lr - (mu_r*Vr**2/2 + eg*Gt*Mtot*mu_r*Wg(Vr/vs)/rr)))
print("Hamiltonian inverse inertia d2H/dp2 at p = 0:", sp.simplify(sp.diff(Hrel, Pr, 2).subs({Pr: 0, eg: 1})),
      " = (1/mu)(1 + 2 Gt M/(r v*^2))")
# Hamilton's equations, 3D, and Galilean check of argument choices
for name, warg in [('|p1/m1 - p2/m2|/v*', sp.sqrt((p1/m1 - p2/m2).dot(p1/m1 - p2/m2))/vs),
                   ('|p1 - p2|/(m1 v*)  [non-invariant]', sp.sqrt((p1 - p2).dot(p1 - p2))/(m1*vs))]:
    dx = x1 - x2; rx = sp.sqrt(dx.dot(dx))
    Hb = p1.dot(p1)/(2*m1) + p2.dot(p2)/(2*m2) - Gt*m1*m2*sp.exp(-warg**2)/rx
    pd1 = sp.Matrix([-sp.diff(Hb, qq) for qq in x1])
    newton = -Gt*m1*m2*sp.exp(-warg**2)*dx/rx**3
    xd1 = sp.Matrix([sp.diff(Hb, qq) for qq in p1]); xd2 = sp.Matrix([sp.diff(Hb, qq) for qq in p2])
    cm = sp.simplify(m1*xd1 + m2*xd2 - (p1 + p2))
    print(f"argument {name}: pdot_1 - (gated Newton force) = {list(sp.simplify(pd1 - newton))};"
          f" d(m1x1+m2x2)/dt - P zero: {cm == sp.zeros(3, 1)}")

# ---------------------------------------------------------------- (c)
print("\n== (c) gated contact interaction (calc note #2), smoothed with width eps")
g, mug, es = sp.symbols('g mu_g eps_s', positive=True)
dx = x1 - x2; rx2 = dx.dot(dx)
delta = sp.exp(-rx2/(2*es**2))/(2*sp.pi*es**2)**sp.Rational(3, 2)
Gg = sp.exp(-(p1 - p2).dot(p1 - p2)/(2*mug**2))
Hc = p1.dot(p1)/(2*m1) + p2.dot(p2)/(2*m2) - g*delta*Gg
pd1 = sp.Matrix([-sp.diff(Hc, qq) for qq in x1])
print("pdot_1 = g * G * grad delta_eps:", sp.simplify(pd1 - g*Gg*sp.Matrix([sp.diff(delta, qq) for qq in x1])) == sp.zeros(3, 1))
rval = sp.symbols('R', positive=True)
mag = sp.simplify(sp.diff(sp.exp(-rval**2/(2*es**2))/(2*sp.pi*es**2)**sp.Rational(3, 2), rval))
print("|d delta/dr| at r = 10 eps relative to its maximum:",
      float(abs(mag.subs({rval: 10*es, es: 1})) / max(abs(float(mag.subs({rval: z, es: 1}))) for z in np.linspace(0.01, 3, 300))))

# ---------------------------------------------------------------- numerics
print("\n== Numerics, model (b): H = p^2/2 - (1 + beta exp(-p^2))/r  (relative coordinate, GM = mu = v* = 1)")
def make_rhs(beta):
    def rhs(y):
        x, yy, px, py = y
        r = np.hypot(x, yy); p2 = px*px + py*py
        gate = np.exp(-p2)
        fac = 1.0 + 2.0*beta*gate/r                     # xdot = p (1 + 2 beta e^{-p^2}/r)
        k = (1.0 + beta*gate)/r**3                       # pdot = -(1 + beta W) r_vec/r^3
        return np.array([px*fac, py*fac, -k*x, -k*yy])
    return rhs
def energy(y, beta):
    r = np.hypot(y[0], y[1]); p2 = y[2]**2 + y[3]**2
    return 0.5*p2 - (1.0 + beta*np.exp(-p2))/r
def rk4(rhs, y, dt):
    k1 = rhs(y); k2 = rhs(y + 0.5*dt*k1); k3 = rhs(y + 0.5*dt*k2); k4 = rhs(y + dt*k3)
    return y + dt*(k1 + 2*k2 + 2*k3 + k4)/6

# orbit average for the perturbative precession: <1/r> = 1/a, <1/r^2> = 1/(a^2 sqrt(1-e^2))
for e_ in [0.1, 0.3, 0.6]:
    I1 = mp.quad(lambda E: 1/(1 - e_*mp.cos(E)), [0, 2*mp.pi])/(2*mp.pi)
    print(f"  check <1/r^2> a^2 = {float(I1):.10f} vs 1/sqrt(1-e^2) = {1/np.sqrt(1-e_**2):.10f}")
a_s, e_s, beta_s, k_s, mu_s, G_s, L_s = sp.symbols('a e beta k mu G L', positive=True)
# delta H = beta p^2/r (leading order in p^2), Kepler constant k = 1 + beta; Delaunay: Lam = sqrt(k a), Gd = Lam sqrt(1-e^2)
Lam, Gd = sp.symbols('Lambda G_d', positive=True)
aL = Lam**2/k_s
avg = beta_s*k_s*(2/(aL**2*(Gd/Lam)) - 1/aL**2)        # beta <p^2/r> with p^2 = k(2/r - 1/a)
omegadot = sp.diff(avg, Gd)
T = 2*sp.pi*sp.sqrt(aL**3/k_s)
dw = sp.simplify((T*omegadot).subs(Gd, Lam*sp.sqrt(1 - e_s**2)).subs(Lam, sp.sqrt(k_s*a_s)))
print("  perturbative precession per orbit (GM = v* = 1):", dw, " -> general units: -4 pi beta GM/(a v*^2 (1-e^2))")

def precession(beta, a, e, norb=8, nstep=6000):
    k = 1.0 + beta
    rp = a*(1 - e); pp = np.sqrt(k*(1 + e)/(a*(1 - e)))
    y = np.array([rp, 0.0, 0.0, pp])
    T = 2*np.pi*np.sqrt(a**3/k); dt = T/nstep
    E0 = energy(y, beta); L0 = y[0]*y[3] - y[1]*y[2]
    rhs = make_rhs(beta)
    angles = []; prev = y[0]*y[2] + y[1]*y[3]; rmin, rmax = 1e300, 0
    for i in range(int(norb*nstep*1.05)):
        ynew = rk4(rhs, y, dt)
        rad = ynew[0]*ynew[2] + ynew[1]*ynew[3]
        r = np.hypot(ynew[0], ynew[1]); rmin = min(rmin, r); rmax = max(rmax, r)
        if prev < 0 <= rad:                               # pericentre passage between y and ynew
            f = -prev/(rad - prev)
            ym = y + f*(ynew - y)
            angles.append(np.arctan2(ym[1], ym[0]))
        prev = rad; y = ynew
    ang = np.unwrap(np.array(angles))
    dws = np.diff(ang)                                   # pericentre advance per orbit (angles unwrapped)
    dE = abs(energy(y, beta) - E0)/abs(E0); dL = abs(y[0]*y[3] - y[1]*y[2] - L0)/abs(L0)
    a_n = (rmin + rmax)/2; e_n = (rmax - rmin)/(rmax + rmin)
    return dws.mean() if len(dws) else np.nan, dE, dL, a_n, e_n
beta = 0.2; e = 0.3
print(f"  beta = {beta}, e = {e}; columns: GM/(a v*^2), measured dw/orbit [rad], formula -4 pi beta/(a(1-e^2)), ratio, |dE/E|, |dL/L|")
for a in [300.0, 100.0, 30.0, 10.0, 3.0, 1.0]:
    dwm, dE, dL, a_n, e_n = precession(beta, a, e)
    form = -4*np.pi*beta/(a_n*(1 - e_n**2))
    print(f"  {1/a:8.4f}  {dwm: .6e}  {form: .6e}  {dwm/form:7.4f}  {dE:.1e}  {dL:.1e}")
# comparison with the GR precession at the same orbit: 6 pi GM/(a c^2 (1-e^2))
cl = 299792.458
for vstar in [120.0]:
    print(f"  ratio gated/GR precession at equal orbit = (-4 beta/6)(c/v*)^2 = {(-4*1.0/6)*(cl/vstar)**2:.3e} * beta  (v* = {vstar} km/s)")

print("\n  Flybys, beta = 0.5, impact parameter b = 20 GM/v*^2: deflection vs v_inf")
def kepler_dir(y, k, outgoing):
    """asymptotic position angle of an osculating Kepler hyperbola (potential -k/r) through state y."""
    x, yy, px, py = y
    r = np.hypot(x, yy); L = x*py - yy*px
    A = np.array([py*L, -px*L]) - k*np.array([x, yy])/r
    e = np.hypot(*A)/k; phiA = np.arctan2(A[1], A[0])
    psi = np.arccos(-1.0/e)
    s = 1 if L > 0 else -1
    return phiA + s*psi if outgoing else phiA - s*psi
def flyby(beta, vinf, b=20.0, R0=2.0e4):
    rhs = make_rhs(beta)
    y = np.array([-R0, b, vinf, 0.0])
    k_in = 1.0 + beta*np.exp(-vinf**2)
    phi_in = kepler_dir(y, k_in, outgoing=False)
    E0 = energy(y, beta)
    while True:
        r = np.hypot(y[0], y[1]); sp_ = np.hypot(y[2], y[3])
        dt = 2e-3*r/max(sp_, 1e-3)
        y = rk4(rhs, y, dt)
        if np.hypot(y[0], y[1]) > R0 and y[0]*y[2] + y[1]*y[3] > 0:
            break
    k_out = 1.0 + beta*np.exp(-(y[2]**2 + y[3]**2))
    phi_out = kepler_dir(y, k_out, outgoing=True)
    theta = (phi_out - (phi_in + np.pi) + np.pi) % (2*np.pi) - np.pi
    return abs(theta), abs(energy(y, beta) - E0)/abs(E0)
print("  v_inf/v*   theta_num   theta_R(G(1+beta))   theta_R(G)   |dE/E|")
for vinf in [0.1, 0.3, 0.6, 1.0, 1.5, 2.0, 3.0]:
    th, dE = flyby(0.5, vinf)
    thR1 = 2*np.arctan(1.5/(20*vinf**2)); thR0 = 2*np.arctan(1.0/(20*vinf**2))
    print(f"  {vinf:7.2f}   {th:.6f}    {thR1:.6f}            {thR0:.6f}    {dE:.1e}")

print("\n== Numerics, model (c): H = p^2/2 - g exp(-r^2/2) exp(-p^2)  (contact width 1, gate v* = 1, g = 0.05)")
def make_rhs_c(gc):
    def rhs(y):
        x, yy, px, py = y
        r2 = x*x + yy*yy; p2 = px*px + py*py
        s = np.exp(-r2/2); gate = np.exp(-p2)
        fac = 1.0 + 2.0*gc*s*gate                         # xdot = p + g s (2 p) e^{-p^2}
        return np.array([px*fac, py*fac, -gc*s*gate*x, -gc*s*gate*yy])
    return rhs
print("  b    v_inf   deflection [rad]")
for b in [0.5, 3.0, 10.0]:
    for vinf in [0.3, 1.0, 3.0]:
        rhs = make_rhs_c(0.05); y = np.array([-30.0, b, vinf, 0.0]); dt = 0.01/vinf
        while not (y[0] > 30.0):
            y = rk4(rhs, y, dt)
        print(f"  {b:4.1f}  {vinf:4.1f}   {abs(np.arctan2(y[3], y[2])):.3e}")
