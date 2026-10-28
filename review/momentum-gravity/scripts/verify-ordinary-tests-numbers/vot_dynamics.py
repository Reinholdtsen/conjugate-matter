# Independent check of the round-2 ordinary-tests claims O5-O9 (two-body dynamics of
# L = mu v^2/2 + (k/r)[1 + eps W(v/v*)]).  Methods differ from the agent's two_body.py:
#  (A) Kepler constant from the first-order Hamiltonian's circular-orbit conditions
#      (dH/dr = 0, Omega = dH/dl), not from the Lagrangian radial equation.
#  (B) First-order Hamiltonian checked by a NUMERICAL Legendre transform (root solve for v(p)).
#  (C) Small-e apsidal advance from the epicyclic frequency of the Hamiltonian,
#      Delta omega = 2 pi (Omega/omega_r - 1), not from Delaunay averaging.
#  (D) Exact apsidal angle of the full Lagrangian model by quadrature with the conserved
#      energy function h = v.dL/dv - L and canonical angular momentum l (no ODE integration),
#      compared with the agent's Delaunay formula 2 pi eps sqrt(1-e^2)/e dPhi/de.
#  (E) Anchor for the quadrature machinery: exact Schwarzschild geodesic apsidal angle
#      (textbook metric, independent of everything here) against 6 pi GM/(c^2 p).
import sympy as sp
import mpmath as mp

print("=== (A) Kepler constant from the first-order Hamiltonian ===")
r, l, eps, vs = sp.symbols('r ell epsilon v_s', positive=True)
Wf = sp.Function('W')
# mu = 1, k = 1 (so GM = 1 for the relative orbit).  Circular orbit: p_r = 0, |p| = l/r.
H = l**2/(2*r**2) - (1/r)*(1 + eps*Wf(l/(r*vs)))
dHdr = sp.diff(H, r)
Om = sp.diff(H, l)
# solve dH/dr = 0 for l^2 perturbatively: l^2 = r (1 + eps c1)
c1 = sp.symbols('c1')
u = sp.symbols('u', positive=True)
l0 = sp.sqrt(r)
lsol = sp.sqrt(r*(1 + eps*c1))
eq = sp.series(dHdr.subs(l, lsol).doit(), eps, 0, 2).removeO()
c1sol = sp.solve(sp.expand(eq).coeff(eps, 1), c1)[0]
lfin = sp.sqrt(r*(1 + eps*c1sol))
Omfin = Om.subs(l, lfin).doit()
kepler = sp.series(Omfin**2*r**3, eps, 0, 2).removeO()
# express with u = l0/(r v_s) = 1/(sqrt(r) v_s)
kep_u = sp.simplify(kepler.subs(vs, 1/(sp.sqrt(r)*u)))
print("Omega^2 r^3 (GM = 1) to O(eps):", sp.simplify(kep_u))
x = sp.symbols('x')
for name, W in [("Gaussian", sp.exp(-x**2)), ("Lorentzian", 1/(1 + x**2))]:
    K_agent = W - x*sp.diff(W, x)
    expr = kep_u.replace(Wf, sp.Lambda(x, W)).doit()
    Kmine = sp.simplify((expr - 1)/eps)
    Kmine = sp.simplify(Kmine.subs(u, x))
    print(f"  {name}: K(u) from Hamiltonian route = {sp.simplify(Kmine)} ; "
          f"equals W - uW': {sp.simplify(Kmine - K_agent) == 0}")
    crit = sp.solve(sp.diff(K_agent, x), x)
    crit = [c for c in crit if c.is_positive]
    print(f"     max of K at u = {crit}, K_max = {[sp.nsimplify(K_agent.subs(x, c)) for c in crit]}"
          f" = {[float(K_agent.subs(x, c)) for c in crit]}")

print()
print("=== (B) First-order Hamiltonian vs numerical exact Legendre transform ===")
mp.mp.dps = 40
def check_H(Wfun, dW, name, epsv=mp.mpf('1e-6'), vstar=mp.mpf('0.8'), rr=mp.mpf('1.3')):
    # L(v) = v^2/2 + (1/r)(1 + eps W(v/v*)), p = dL/dv = v + (eps/r) W'(v/v*)/v*
    worst = 0
    for pval in [mp.mpf('0.3'), mp.mpf('0.8'), mp.mpf('1.1'), mp.mpf('2.0')]:
        v = mp.findroot(lambda v: v + (epsv/rr)*dW(v/vstar)/vstar - pval, pval)
        Hexact = pval*v - (v**2/2 + (1/rr)*(1 + epsv*Wfun(v/vstar)))
        Hfirst = pval**2/2 - (1/rr)*(1 + epsv*Wfun(pval/vstar))
        rel = abs(Hexact - Hfirst)/epsv**2   # should be O(1): difference is O(eps^2)
        worst = max(worst, rel)
    print(f"  {name}: max |H_exact - H_first|/eps^2 over 4 momenta = {mp.nstr(worst, 6)}  (eps = {epsv})")
check_H(lambda y: mp.e**(-y**2), lambda y: -2*y*mp.e**(-y**2), "Gaussian")
check_H(lambda y: 1/(1 + y**2), lambda y: -2*y/(1 + y**2)**2, "Lorentzian")

print()
print("=== (C) Small-e advance from the epicyclic frequency of the first-order Hamiltonian ===")
pr = sp.symbols('p_r', real=True)
Hfull = (pr**2 + l**2/r**2)/2 - (1/r)*(1 + eps*Wf(sp.sqrt(pr**2 + l**2/r**2)/vs))
Hrr = sp.diff(Hfull, r, 2).subs(pr, 0)
Hpp = sp.diff(Hfull, pr, 2).subs(pr, 0)
Omg = sp.diff(Hfull, l).subs(pr, 0)
# circular orbit radius at fixed l: dH/dr = 0 at p_r = 0 -> r = l^2 (1 + eps d1)
d1 = sp.symbols('d1')
rsol = l**2*(1 + eps*d1)
eqr = sp.series(sp.diff(Hfull, r).subs(pr, 0).subs(r, rsol).doit(), eps, 0, 2).removeO()
d1sol = sp.solve(sp.expand(eqr).coeff(eps, 1), d1)[0]
rfin = l**2*(1 + eps*d1sol)
wr2 = (Hrr*Hpp).subs(r, rfin).doit()
Omc = Omg.subs(r, rfin).doit()
ratio = sp.series(Omc/sp.sqrt(wr2), eps, 0, 2).removeO()
adv = sp.simplify(2*sp.pi*(ratio - 1))
# u = |p|/v* at the circular orbit = (l/r)/v* = 1/(l v*) at zeroth order
adv_u = sp.simplify(adv.subs(vs, 1/(l*u)))
for name, W in [("Gaussian", sp.exp(-x**2)), ("Lorentzian", 1/(1 + x**2)), ("W = u^2", x**2)]:
    a_ = sp.simplify(adv_u.replace(Wf, sp.Lambda(x, W)).doit().subs(u, x)/eps)
    agent = sp.pi*x*sp.diff(x*sp.diff(W, x), x)
    print(f"  {name}: epicyclic Delta omega/eps = {sp.factor(a_)} ; equals pi u (u W')': "
          f"{sp.simplify(a_ - agent) == 0}")

print()
print("=== (D) Exact apsidal angle by quadrature, full Lagrangian model ===")
mp.mp.dps = 30
def apsidal(Wfun, dWfun, epsv, uc, e):
    # units GM = 1 (mu = 1, k = 1), a = 1 -> circular speed 1, v* = 1/uc
    vstar = 1/mp.mpf(uc)
    # conserved quantities taken at Newtonian values for (a, e); they differ from the
    # perturbed orbit's (a, e) by O(eps), which shifts Delta omega only at O(eps^2)
    E = mp.mpf(-1)/2
    ell = mp.sqrt(1 - mp.mpf(e)**2)
    K = lambda y: Wfun(y) - y*dWfun(y)
    def speed(rr):
        # h = v^2/2 - (1/r)(1 + eps K(v/v*)) = E
        v0 = mp.sqrt(2*(E + 1/rr))
        return mp.findroot(lambda v: v**2/2 - (1/rr)*(1 + epsv*K(v/vstar)) - E, v0)
    def vtheta(rr, v):
        # l = r v_th [1 + (eps/r) W'(u)/(v* v)]
        return ell/(rr*(1 + (epsv/rr)*dWfun(v/vstar)/(vstar*v)))
    def vr2(rr):
        v = speed(rr)
        return v**2 - vtheta(rr, v)**2
    rmin = mp.findroot(vr2, 1 - mp.mpf(e))
    rmax = mp.findroot(vr2, 1 + mp.mpf(e))
    A = (rmax + rmin)/2; B = (rmax - rmin)/2
    def integrand(psi):
        rr = A - B*mp.cos(psi)
        v = speed(rr)
        vt = vtheta(rr, v)
        vr = mp.sqrt(max(v**2 - vt**2, mp.mpf(0)))
        if vr == 0:
            return mp.mpf(0)
        return vt/(rr*vr)*B*mp.sin(psi)
    dtheta = 2*mp.quad(integrand, [0, mp.pi/2, mp.pi])
    return dtheta - 2*mp.pi

def delaunay(Wfun, uc, e):
    Phi = lambda ee: mp.quad(lambda E: Wfun(mp.mpf(uc)*mp.sqrt((1 + ee*mp.cos(E))/(1 - ee*mp.cos(E)))),
                             [0, mp.pi])/mp.pi
    return 2*mp.pi*mp.sqrt(1 - mp.mpf(e)**2)/e*mp.diff(Phi, mp.mpf(e))

G = (lambda y: mp.e**(-y**2), lambda y: -2*y*mp.e**(-y**2))
Lz = (lambda y: 1/(1 + y**2), lambda y: -2*y/(1 + y**2)**2)
U2 = (lambda y: y**2, lambda y: 2*y)
cases = [("Gaussian", G, 1.6, 0.1), ("Gaussian", G, 1.0, 0.1), ("Gaussian", G, 0.5, 0.3),
         ("Lorentzian", Lz, 3.0, 0.3), ("Lorentzian", Lz, 1.0, 0.6), ("W=u^2", U2, 0.7, 0.5)]
print(f"  {'shape':10s} {'u_c':>5s} {'e':>5s} | quadrature dw/eps at eps=1e-7, 1e-3, 5e-4 | Delaunay formula | small-e pi u(uW')'")
for name, (Wfun, dW), uc, e in cases:
    q7 = apsidal(Wfun, dW, mp.mpf('1e-7'), uc, e)/mp.mpf('1e-7')
    q3 = apsidal(Wfun, dW, mp.mpf('1e-3'), uc, e)/mp.mpf('1e-3')
    q4 = apsidal(Wfun, dW, mp.mpf('5e-4'), uc, e)/mp.mpf('5e-4')
    dl = delaunay(Wfun, uc, e)
    y = mp.mpf(uc)
    small = mp.pi*y*mp.diff(lambda t: t*dW(t), y)
    print(f"  {name:10s} {uc:5.2f} {e:5.2f} | {mp.nstr(q7, 10):>14s} {mp.nstr(q3, 8):>12s} {mp.nstr(q4, 8):>12s} |"
          f" {mp.nstr(dl, 10):>14s} | {mp.nstr(small, 8)}")
print("  W = u^2 exact-in-e claim 4 pi u_c^2/(1-e^2) at u_c=0.7, e=0.5:", mp.nstr(4*mp.pi*0.49/(1 - 0.25), 10))
PhiL = mp.quad(lambda E: 1/(1 + (1 + 0.6*mp.cos(E))/(1 - 0.6*mp.cos(E))), [0, mp.pi])/mp.pi
print("  Lorentzian Phi(u_c = 1, e = 0.6) =", mp.nstr(PhiL, 15))

print()
print("=== (E) Anchor for the quadrature: exact Schwarzschild apsidal angle ===")
# Geodesic orbit equation (G = M = c = 1), U = 1/r: (dU/dphi)^2 = 2U^3 - U^2 + 2U/L^2 + (E^2-1)/L^2
# For semi-latus rectum p and eccentricity e, the turning points are U1 = (1-e)/p, U2 = (1+e)/p,
# and the cubic's third root is U3 = 1/2 - U1 - U2.  Exact: dphi = 2 int dU / sqrt(2 (U-U1)(U2-U)(U3-U)).
for p in [1e3, 1e5]:
    for e in [0.2, 0.6]:
        p_ = mp.mpf(p); U1 = (1 - e)/p_; U2 = (1 + e)/p_; U3 = mp.mpf(1)/2 - U1 - U2
        f = lambda chi: 2/mp.sqrt(2*(U3 - ((U1 + U2)/2 - (U2 - U1)/2*mp.cos(chi))))
        dphi = mp.quad(f, [0, mp.pi])
        print(f"  p = {p:.0e} GM/c^2, e = {e}: exact advance = {mp.nstr(dphi - 2*mp.pi, 10)} ;"
              f" 6 pi/p = {mp.nstr(6*mp.pi/p_, 10)} ; ratio = {mp.nstr((dphi - 2*mp.pi)/(6*mp.pi/p_), 8)}")
