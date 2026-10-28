"""Independent check of the first-order apsidal-advance formula (claims O7, O8).

Method (different from the agent's RK4 integration): the exact (all-orders-in-eps) model
    L = s^2/2 + (1/r)(1 + eps W(s/v*))      (GM = 1, per unit reduced mass)
conserves E = p.v - L and J = r x p, with p = v [1 + eps W'(s/v*)/(r v* s)].
E depends on (r, s) only, so s(r) follows from E; the tangential speed from J; then
    apsidal angle = 2 * int_{r1}^{r2} (w/r)/sqrt(s^2 - w^2) dr.
With r = A - B cos(psi) the integrand is an even, periodic, analytic function of psi, so the
midpoint rule converges exponentially. The first-order coefficient is extracted by a symmetric
difference in eps (cancels O(eps^2)), and compared with
    Delta omega / eps = 2 pi sqrt(1-e^2)/e dPhi/de,  Phi(e) = <W(u_c sqrt((1+e cosE)/(1-e cosE)))>_E.
"""
import mpmath as mp

mp.mp.dps = 40

SHAPES = {
    'gauss':   (lambda x: mp.exp(-x**2),      lambda x: -2*x*mp.exp(-x**2)),
    'lorentz': (lambda x: 1/(1 + x**2),       lambda x: -2*x/(1 + x**2)**2),
}


def advance_exact(shape, uc, e, eps, N):
    W, Wp = SHAPES[shape]
    vs = 1/uc              # a = 1, GM = 1 -> circular speed 1, u_c = 1/v*
    r1, r2 = 1 - e, 1 + e

    def f(r, s):
        return 1 + eps*Wp(s/vs)/(r*vs*s)

    def Efun(r, s):
        return s**2/2 + eps*s*Wp(s/vs)/(r*vs) - (1 + eps*W(s/vs))/r

    def Jfun(r, s):
        return r*s*f(r, s)   # at a turning point w = s

    s1g = mp.sqrt((1 + e)/(1 - e))
    s2g = mp.sqrt((1 - e)/(1 + e))
    sol = mp.findroot(lambda a1, a2: [Jfun(r1, a1) - Jfun(r2, a2), Efun(r1, a1) - Efun(r2, a2)],
                      (s1g, s2g), tol=mp.mpf(10)**(-36))
    s1, s2 = sol[0], sol[1]
    E0 = Efun(r1, s1)
    J0 = Jfun(r1, s1)
    A, B = (r1 + r2)/2, (r2 - r1)/2
    total = mp.mpf(0)
    for k in range(N):
        psi = (k + mp.mpf(1)/2)*mp.pi/N
        r = A - B*mp.cos(psi)
        sg = mp.sqrt(2*(E0 + 1/r))
        s = mp.findroot(lambda ss: Efun(r, ss) - E0, sg, tol=mp.mpf(10)**(-36))
        w = J0/(r*f(r, s))
        rd2 = s**2 - w**2
        total += (w/r)/mp.sqrt(rd2)*B*mp.sin(psi)
    dtheta = total*mp.pi/N
    return 2*dtheta - 2*mp.pi


def advance_formula(shape, uc, e):
    W, Wp = SHAPES[shape]

    def dPhi_integrand(E):
        c = mp.cos(E)
        x = mp.sqrt((1 + e*c)/(1 - e*c))
        dx = c/(x*(1 - e*c)**2)
        return Wp(uc*x)*uc*dx
    dPhi = mp.quad(dPhi_integrand, [0, mp.pi, 2*mp.pi])/(2*mp.pi)
    return 2*mp.pi*mp.sqrt(1 - e**2)/e*dPhi


def small_e(shape, uc):
    if shape == 'gauss':
        return 4*mp.pi*uc**2*(uc**2 - 1)*mp.exp(-uc**2)
    return 4*mp.pi*uc**2*(uc**2 - 1)/(1 + uc**2)**3


print("Kepler sanity (eps = 0): advance =", mp.nstr(advance_exact('gauss', 1.3, mp.mpf('0.3'), 0, 200), 5))
delta = mp.mpf('1e-12')
cases = [('gauss', '0.5', '0.1'), ('gauss', '1.0', '0.1'), ('gauss', '1.6', '0.1'), ('gauss', '3.0', '0.3'),
         ('gauss', '1.0', '0.6'), ('gauss', '3.0', '0.6'), ('lorentz', '1.0', '0.3'), ('lorentz', '1.0', '0.6'),
         ('lorentz', '3.0', '0.3'), ('lorentz', '0.5', '0.2')]
print(f"{'shape':8s} {'u_c':>5s} {'e':>5s} {'quadrature dω/dε (N=300)':>28s} {'N=600':>28s} {'formula':>28s} {'small-e':>12s} {'rel.diff':>10s}")
for shape, ucs, es in cases:
    uc, e = mp.mpf(ucs), mp.mpf(es)
    vals = []
    for N in (300, 600):
        ap = advance_exact(shape, uc, e, delta, N)
        am = advance_exact(shape, uc, e, -delta, N)
        vals.append((ap - am)/(2*delta))
    form = advance_formula(shape, uc, e)
    rel = (vals[1] - form)/form if form != 0 else vals[1]
    print(f"{shape:8s} {ucs:>5s} {es:>5s} {mp.nstr(vals[0], 15):>28s} {mp.nstr(vals[1], 15):>28s} {mp.nstr(form, 15):>28s} {mp.nstr(small_e(shape, uc), 7):>12s} {mp.nstr(rel, 3):>10s}")

print()
print("Second-order size at the Gaussian zero crossing (u_c = 1, e = 0.1): advance/eps for finite eps")
for epsv in ['1e-3', '5e-4']:
    epsm = mp.mpf(epsv)
    ap = advance_exact('gauss', mp.mpf(1), mp.mpf('0.1'), epsm, 300)
    print(f"  eps = {epsv}: advance/eps = {mp.nstr(ap/epsm, 8)}   (agent's RK4: 3.115669e-02 at 1e-3, 2.709865e-02 at 5e-4; formula 2.303546e-02)")
