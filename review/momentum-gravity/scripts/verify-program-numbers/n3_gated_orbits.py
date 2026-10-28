# Independent numerics for P13 (model b): H = p^2/2 - (1 + beta exp(-p^2))/r in units GM = mu = v* = 1,
# planar relative motion. Method differs from the agent's fixed-step RK4: adaptive Dormand-Prince 5(4)
# with step control, pericentre events located by bisection on sub-steps, and flybys started far out
# (no osculating-orbit correction), with a start-distance convergence test. Pure-Python floats.
from math import sqrt, exp, atan2, pi, atan, cos, sin

def rhs(s, beta):
    x, y, px, py = s
    r2 = x*x + y*y; r = sqrt(r2); p2 = px*px + py*py
    w = beta*exp(-p2)
    fac = 1.0 + 2.0*w/r                 # xdot = dH/dp = p (1 + 2 beta e^{-p^2}/r)
    k = (1.0 + w)/(r2*r)                # pdot = -dH/dx = -(1 + beta e^{-p^2}) x / r^3
    return (px*fac, py*fac, -k*x, -k*y)

def H(s, beta):
    x, y, px, py = s
    p2 = px*px + py*py
    return 0.5*p2 - (1.0 + beta*exp(-p2))/sqrt(x*x + y*y)

def Lz(s):
    x, y, px, py = s
    return x*py - y*px

A = [[], [1/5], [3/40, 9/40], [44/45, -56/15, 32/9],
     [19372/6561, -25360/2187, 64448/6561, -212/729],
     [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656],
     [35/384, 0.0, 500/1113, 125/192, -2187/6784, 11/84]]
B5 = [35/384, 0.0, 500/1113, 125/192, -2187/6784, 11/84, 0.0]
B4 = [5179/57600, 0.0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40]

def dp_step(s, h, beta):
    ks = []
    for i in range(7):
        if i == 0:
            si = s
        else:
            si = tuple(s[j] + h*sum(A[i][m]*ks[m][j] for m in range(i)) for j in range(4))
        ks.append(rhs(si, beta))
    y5 = tuple(s[j] + h*sum(B5[m]*ks[m][j] for m in range(7)) for j in range(4))
    err = tuple(h*sum((B5[m] - B4[m])*ks[m][j] for m in range(7)) for j in range(4))
    return y5, err

def integrate(s, beta, t_end=None, stop=None, event=None, rtol=1e-12, atol=1e-13, h=1e-3, max_steps=5_000_000):
    """Integrate until t_end or stop(s) is True. event(s) -> float; record roots where it crosses - to +."""
    t = 0.0; roots = []; n = 0
    ev_prev = event(s) if event else None
    while True:
        if t_end is not None and t + h > t_end:
            h = t_end - t
        y, e = dp_step(s, h, beta)
        sc = max(abs(e[j])/(atol + rtol*max(abs(s[j]), abs(y[j]))) for j in range(4))
        if sc <= 1.0:
            if event:
                ev = event(y)
                if ev_prev < 0.0 <= ev:
                    lo, hi = 0.0, h
                    for _ in range(60):
                        mid = 0.5*(lo + hi)
                        ym, _e = dp_step(s, mid, beta)
                        if event(ym) < 0.0: lo = mid
                        else: hi = mid
                    yr, _e = dp_step(s, 0.5*(lo + hi), beta)
                    roots.append((t + 0.5*(lo + hi), yr))
                ev_prev = ev
            t += h; s = y; n += 1
            if t_end is not None and t >= t_end: break
            if stop is not None and stop(s): break
            if n > max_steps: raise RuntimeError("too many steps")
        h *= min(5.0, max(0.2, 0.9*sc**(-0.2) if sc > 0 else 5.0))
    return s, roots, n

def radial(s):
    x, y, px, py = s
    return x*px + y*py                   # sign of r-dot (xdot is parallel to p in this model)

def precession(beta, a, e, k_ic, n_orb=8):
    rp = a*(1 - e)
    pp = sqrt(k_ic*(1 + e)/(a*(1 - e)))  # Kepler pericentre speed for strength k_ic, used as canonical p
    s0 = (rp, 0.0, 0.0, pp)
    T = 2*pi*a**1.5/sqrt(1 + beta)
    H0, L0 = H(s0, beta), Lz(s0)
    s, roots, n = integrate(s0, beta, t_end=(n_orb + 0.5)*T*1.3, event=radial)
    roots = roots[:n_orb]
    angs = [atan2(r[1][1], r[1][0]) for r in roots]
    prev = 0.0; adv = []
    for ang in angs:
        d = (ang - prev) % (2*pi)
        if d > pi: d -= 2*pi
        adv.append(d); prev = ang
    dH = max(abs(H(r[1], beta) - H0)/abs(H0) for r in roots)
    dL = max(abs(Lz(r[1]) - L0)/abs(L0) for r in roots)
    return sum(adv)/len(adv), adv, dH, dL, n

print("== precession, beta = 0.2, e = 0.3 (nominal); formula = -4 pi beta GM/(a v*^2 (1 - e^2))")
print("GM/(a v*^2)   k_ic    measured/orbit      formula        ratio     spread(max-min)   dH/H     dL/L")
for x in (1/300, 0.01, 0.1, 1.0):
    a = 1/x
    f = -4*pi*0.2*x/(1 - 0.3**2)
    for k_ic in (1.2, 1.0):
        m, adv, dH, dL, n = precession(0.2, a, 0.3, k_ic)
        print(f"{x:9.4f}   {k_ic:4.1f}   {m: .6e}   {f: .6e}   {m/f:7.4f}   {max(adv)-min(adv):.1e}   {dH:.1e}  {dL:.1e}")
# control: beta = 0 must give zero precession
m0, adv0, dH0, dL0, n0 = precession(0.0, 10.0, 0.3, 1.0)
print(f"control beta = 0, a = 10: precession per orbit = {m0:.2e}")

print("\n== flybys, beta = 0.5, b = 20 (units GM = v* = 1): deflection of the asymptotic direction")
def flyby(beta, vinf, b, X0):
    # start at (-X0, y0) moving in +x, with |p| fixed by energy; y0 = b (asymptote approx; error O(1/X0))
    r0 = sqrt(X0**2 + b**2)
    # solve p0^2/2 - (1 + beta e^{-p0^2})/r0 = vinf^2/2 for p0
    p = vinf
    for _ in range(100):
        f = 0.5*p*p - (1 + beta*exp(-p*p))/r0 - 0.5*vinf**2
        df = p + 2*p*beta*exp(-p*p)/r0
        p -= f/df
    s0 = (-X0, b, p, 0.0)
    H0, L0 = H(s0, beta), Lz(s0)
    s, _r, n = integrate(s0, beta, stop=lambda s: s[0]*s[2] + s[1]*s[3] > 0 and (s[0]**2 + s[1]**2) > r0**2, h=1.0)
    th = atan2(s[3], s[2])
    return abs(th), abs(H(s, beta) - H0)/abs(H0), abs(Lz(s) - L0)/abs(L0), n
print(" v_inf    X0        theta        Rutherford(G)  Rutherford(1+beta e^-v^2)   dH/H     dL/L   steps")
for vinf in (0.1, 0.3, 3.0):
    for X0 in (1e5, 1e6, 1e7):
        th, dH, dL, n = flyby(0.5, vinf, 20.0, X0)
        rg = 2*atan(1/(20*vinf**2))
        rk = 2*atan((1 + 0.5*exp(-vinf**2))/(20*vinf**2))
        print(f"{vinf:5.2f}  {X0:7.0e}   {th:.6f}   {rg:.6f}       {rk:.6f}                 {dH:.1e}  {dL:.1e}  {n}")
print("\n control beta = 0 (must reproduce Rutherford 2 atan(GM/(b v^2))):")
for vinf in (0.1, 0.3, 3.0):
    th, dH, dL, n = flyby(0.0, vinf, 20.0, 1e7)
    print(f"  v_inf = {vinf}: theta = {th:.7f}; Rutherford = {2*atan(1/(20*vinf**2)):.7f}")
