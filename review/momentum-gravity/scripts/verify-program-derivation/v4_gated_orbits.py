"""Verifier check of P13 (model b numerics), with an integrator written independently of the agent's.
Relative-coordinate Hamiltonian, units GM = mu = v* = 1, planar:
    H = p^2/2 - K(p)/r,  K(p) = 1 + beta exp(-p^2)
    xdot = p + 2 beta p exp(-p^2)/r,   pdot = -K(p) x / r^3
Integrator: Dormand-Prince 5(4), adaptive; pericentres located by bisection on the step.
Leading-order secular precession (derived here by orbit averaging, see analytic part):
    dw/orbit = -4 pi beta GM / (a v*^2 (1 - e^2)), a, e the measured orbit's.
Flybys: deflection between incoming and outgoing osculating-hyperbola asymptotes, each computed
with the local strength K(p) at the endpoint (the gated term is itself a 1/r tail).
"""
import numpy as np
import sympy as sp

# ---------------- analytic: orbit average of delta H = b p^2/r on a Kepler orbit with strength K ------------
L, Gd, Kc, b = sp.symbols('L G K b', positive=True)   # Delaunay L = sqrt(K a), G = L sqrt(1-e^2)
a = L**2/Kc
sq = Gd/L
avg_inv_r = 1/a
avg_inv_r2 = 1/(a**2*sq)
# p^2 = K (2/r - 1/a)  ->  <p^2/r> = K (2 <1/r^2> - <1/r>/a)
avgdH = b*Kc*(2*avg_inv_r2 - avg_inv_r/a)
wdot = sp.diff(avgdH, Gd)
T = 2*sp.pi*L**3/Kc**2
dw = sp.simplify(wdot*T)
e = sp.symbols('e', positive=True)
dw_ae = sp.simplify(dw.subs(Gd, L*sp.sqrt(1 - e**2)).subs(L, sp.sqrt(Kc*sp.Symbol('a', positive=True))))
print("secular precession per orbit from delta H = b p^2/r on a Kepler orbit of strength K:", dw_ae)
print("  (b = beta GM/v*^2 for the gated term; K cancels, so the bare GM/(a v*^2) enters)")
# GR cross-check of the method: test-mass 1PN H = p^2/2 - p^4/8 - K/r - (3/2) K p^2/r + K^2/(2 r^2) (c = 1)
avgp4 = Kc**2*(4*avg_inv_r2 - 4*avg_inv_r/a + 1/a**2)
dH_GR = -avgp4/8 - sp.Rational(3, 2)*Kc*(2*avg_inv_r2 - avg_inv_r/a)*Kc/Kc + Kc**2*avg_inv_r2/2
dwGR = sp.simplify((sp.diff(dH_GR, Gd)*T).subs(Gd, L*sp.sqrt(1 - e**2)).subs(L, sp.sqrt(Kc*sp.Symbol('a', positive=True))))
print("method check, GR test-mass 1PN Hamiltonian -> precession per orbit:", dwGR, " (expected 6 pi K/(a(1-e^2)))")

# ---------------- numerics ----------------
C = np.array([0, 1/5, 3/10, 4/5, 8/9, 1, 1])
A = [[], [1/5], [3/40, 9/40], [44/45, -56/15, 32/9], [19372/6561, -25360/2187, 64448/6561, -212/729],
     [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656], [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84]]
B5 = np.array([35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0])
B4 = np.array([5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40])


def make_rhs(beta):
    def f(y):
        x = y[:2]; p = y[2:]
        r = np.hypot(*x); p2 = p @ p
        gexp = np.exp(-p2)
        return np.concatenate([p + 2*beta*p*gexp/r, -(1 + beta*gexp)*x/r**3])
    return f


def ham(y, beta):
    x = y[:2]; p = y[2:]
    return 0.5*(p @ p) - (1 + beta*np.exp(-(p @ p)))/np.hypot(*x)


def step(f, y, h):
    k = []
    for i in range(7):
        yi = y + h*sum(A[i][j]*k[j] for j in range(i)) if i else y
        k.append(f(yi))
    k = np.array(k)
    y5 = y + h*(B5 @ k); y4 = y + h*(B4 @ k)
    return y5, np.max(np.abs(y5 - y4)/(1e-13 + 1e-13*np.abs(y)))


def adaptive(f, y, h, tol_fac=1.0):
    while True:
        yn, err = step(f, y, h)
        err /= tol_fac
        if err <= 1.0:
            hn = h*min(5.0, 0.9*err**(-0.2)) if err > 0 else 5*h
            return yn, h, hn
        h *= max(0.1, 0.9*err**(-0.25))


def radial(f, y):
    return y[:2] @ f(y)[:2]


def bound_orbit(beta, a0, e0, norb=8):
    f = make_rhs(beta)
    # start at pericentre of an approximate Kepler orbit with strength K0 = 1 + beta exp(-p^2) (iterated)
    rp = a0*(1 - e0); K0 = 1 + beta
    for _ in range(50):
        vp = np.sqrt(K0*(1 + e0)/rp)
        K0 = 1 + beta*np.exp(-vp**2)
    y = np.array([rp, 0.0, 0.0, vp])
    E0 = ham(y, beta); L0 = y[0]*y[3] - y[1]*y[2]
    Tk = 2*np.pi*a0**1.5/np.sqrt(K0)
    h = Tk/2000; t = 0.0
    peri = []; rmin = np.inf; rmax = 0.0
    prev = radial(f, y)
    while len(peri) < norb + 1:
        yn, hu, hn = adaptive(f, y, min(h, Tk/400))
        rn = np.hypot(*yn[:2]); rmin = min(rmin, rn); rmax = max(rmax, rn)
        cur = radial(f, yn)
        if prev < 0 <= cur:     # pericentre inside [y, yn]: bisect on step length
            lo, hi = 0.0, hu
            for _ in range(60):
                mid = 0.5*(lo + hi)
                ym, _ = step(f, y, mid)
                if radial(f, ym) < 0: lo = mid
                else: hi = mid
            ym, _ = step(f, y, 0.5*(lo + hi))
            peri.append(np.arctan2(ym[1], ym[0]))
            rmin = min(rmin, np.hypot(*ym[:2]))
        elif not peri and t == 0.0 and cur > 0:
            pass
        y, h, prev = yn, hn, cur
        t += hu
        if len(peri) == 0 and t > 0 and prev > 0 and np.hypot(*y[:2]) < rp*1.0000001:
            pass
    ang = np.unwrap(np.array(peri))
    dws = np.diff(ang)
    dw = np.mean(dws)          # pericentre-to-pericentre advance (no 2 pi: angle of the pericentre itself)
    am = 0.5*(rmin + rmax); em = (rmax - rmin)/(rmax + rmin)
    pred = -4*np.pi*beta/(am*(1 - em**2))
    dE = abs(ham(y, beta) - E0)/abs(E0); dL = abs((y[0]*y[3] - y[1]*y[2]) - L0)/abs(L0)
    return dw, pred, am, em, dE, dL, np.std(dws)


print()
print("bound orbits, beta = 0.2, e ~ 0.3: GM/(a v*^2), measured dw/orbit, leading-order formula, ratio, (a, e) measured, rel. energy and L errors")
for a0 in (300.0, 100.0, 10.0, 1.0):
    dw, pred, am, em, dE, dL, sd = bound_orbit(0.2, a0, 0.3)
    print(f"  {1/a0:7.4f}  {dw: .6e}  {pred: .6e}  {dw/pred:7.4f}   a = {am:9.4f}, e = {em:.4f}   dE = {dE:.1e}, dL = {dL:.1e}, scatter of dw = {sd:.1e}")
# step-size (tolerance) sensitivity for one case
print("GR-rate comparison per unit beta at v* = 120 km/s: (-4/6)(c/v*)^2 =", f"{-4/6*(299792.458/120)**2:.4e}")


def osc_dir(y, beta, sign):
    """outgoing (sign=+1) or incoming (sign=-1) asymptotic velocity direction of the osculating Kepler
    hyperbola with strength K = K(p) at state y, from the hodograph v = (K/L) z x (rhat + e_vec)."""
    x = y[:2]; p = y[2:]
    K = 1 + beta*np.exp(-(p @ p)); r = np.hypot(*x)
    Lz = x[0]*p[1] - x[1]*p[0]
    E = 0.5*(p @ p) - K/r
    vinf = np.sqrt(2*E)
    evec = np.array([p[1]*Lz, -p[0]*Lz])/K - x/r
    kap = sign*K/(Lz*vinf)
    cy = (kap*evec[0] - kap**2*evec[1])/(1 + kap**2)
    cx = -kap*(cy + evec[1])
    c_ = np.array([cx, cy])
    return c_/np.hypot(*c_) if sign > 0 else -c_/np.hypot(*c_)


def flyby(beta, vinf, bimp, R0=1e6, tol_fac=1.0):
    f = make_rhs(beta)
    # initial state at x = -X, y = y0, p = (px, 0): fix px by energy and y0 by L = -b vinf
    X = R0; y0 = bimp; px = vinf
    for _ in range(100):
        r = np.hypot(X, y0)
        # solve px^2/2 - (1 + beta exp(-px^2))/r = vinf^2/2 by Newton
        for _ in range(50):
            F = 0.5*px**2 - (1 + beta*np.exp(-px**2))/r - 0.5*vinf**2
            dF = px + 2*beta*px*np.exp(-px**2)/r
            px -= F/dF
        y0 = bimp*vinf/px
    y = np.array([-X, y0, px, 0.0])
    E0 = ham(y, beta)
    din = osc_dir(y, beta, -1)
    h = 1.0; t = 0.0
    while True:
        yn, hu, hn = adaptive(f, y, h, tol_fac)
        y, h = yn, hn
        if np.hypot(*y[:2]) > R0 and y[:2] @ y[2:] > 0:
            break
    dout = osc_dir(y, beta, +1)
    theta = np.arccos(np.clip(din @ dout, -1, 1))
    return theta, abs(ham(y, beta) - E0)/abs(E0)


print()
print("flybys, beta = 0.5, b = 20: v_inf, deflection, Rutherford(G), Rutherford(G (1 + beta e^{-v^2})), energy error")
th0, _ = flyby(0.0, 0.1, 20.0)
print(f"  validation beta = 0, v_inf = 0.1: theta = {th0:.6f}, Rutherford = {2*np.arctan(1/(20*0.01)):.6f}")
for vinf in (0.1, 0.3, 1.0, 3.0):
    th, dE = flyby(0.5, vinf, 20.0)
    th2, _ = flyby(0.5, vinf, 20.0, R0=1e7, tol_fac=0.1)
    Kinf = 1 + 0.5*np.exp(-vinf**2)
    print(f"  {vinf:4.1f}  {th:.6f} (R0=1e7, tighter tol: {th2:.6f})  R_G = {2*np.arctan(1/(20*vinf**2)):.6f}  R_Kinf = {2*np.arctan(Kinf/(20*vinf**2)):.6f}  dE = {dE:.1e}")
