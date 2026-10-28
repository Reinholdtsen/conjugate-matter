"""Remaining spot checks: O2 (EIH CM reduction), O14(a) Kepler Mars/Earth, O18 (static <W> vs the
orbit-force analog for MICROSCOPE), and order-of-magnitude size of a third-body anisotropic-inertia
term in the Earth-Moon problem (an unevaluated channel)."""
import numpy as np
import sympy as sp

print("=== O2: EIH two-body bracket in the CM frame ===")
m1, m2 = sp.symbols('m1 m2', positive=True)
vx, vy, nx, ny = sp.symbols('vx vy nx ny')
M = m1 + m2
v = sp.Matrix([vx, vy]); n = sp.Matrix([nx, ny])
v1 = m2/M*v; v2 = -m1/M*v
br = 3*(v1.dot(v1) + v2.dot(v2)) - 7*v1.dot(v2) - n.dot(v1)*n.dot(v2)
nu = m1*m2/M**2
print("  bracket - [(3+nu) v^2 + nu (n.v)^2] =", sp.simplify(br - ((3 + nu)*v.dot(v) + nu*n.dot(v)**2)))

print()
print("=== O14(a): Kepler-law test Mars vs Earth at v* = 10 km/s (Gaussian) ===")
GM_SUN = 132712440041.94
K = lambda u: (1 + 2*u**2)*np.exp(-u**2)
uE, uM = np.sqrt(GM_SUN/149.598e6)/10, np.sqrt(GM_SUN/227.956e6)/10
dK = K(uM) - K(uE)
print(f"  K(u_Mars) - K(u_Earth) = {dK:.5f}; |eta_p| < 6.5e-10 -> |eps| < 3*6.5e-10/dK = {3*6.5e-10/dK:.3g}")

print()
print("=== O18: atom-level gating, MICROSCOPE at v* = 10 km/s: static <W> vs orbit-force analog ===")
# smeared Gaussian gate <W>(V) = A exp(-V^2/b^2), A = (1+2 s^2/v*^2)^(-3/2), b^2 = v*^2 + 2 s^2
# circular-orbit force factor (K analog of W - uW'): <W> - V d<W>/dV = <W> (1 + 2 V^2/b^2)
def Wbar(V, s2, vs): return (1 + 2*s2/vs**2)**-1.5*np.exp(-V**2/(vs**2 + 2*s2))
def Kbar(V, s2, vs): return Wbar(V, s2, vs)*(1 + 2*V**2/(vs**2 + 2*s2))
sTi, sPt, sE = 0.228, 0.113, 1.0
for vs in (10.0, 30.0):
    V = 7.5
    dW = Wbar(V, sTi**2 + sE**2, vs) - Wbar(V, sPt**2 + sE**2, vs)
    dKb = Kbar(V, sTi**2 + sE**2, vs) - Kbar(V, sPt**2 + sE**2, vs)
    print(f"  v* = {vs}: Ti-Pt difference, static <W>: {dW:.3e}; orbit-force analog: {dKb:.3e}; ratio {dKb/dW:.2f}")

print()
print("=== third-body (Sun) anisotropic inertia in the Earth-Moon problem, order of magnitude ===")
# Moon's geocentric kinetic term gains eps (GM_sun/AU)/(2 v*^2) [W''(u_E) (e.v)^2 + (W'(u_E)/u_E)(v^2 - (e.v)^2)]
# anisotropic part: eps (GM_sun/(AU v*^2)) [W''(u) - W'(u)/u]; fractional lunar-orbit perturbation of that order
AU = 149.598e6
for vs in (10.0, 20.0, 30.0, 60.0, 120.0):
    u = 29.78/vs
    Wpp = (4*u**2 - 2)*np.exp(-u**2)
    Wpu = -2*np.exp(-u**2)
    an = (GM_SUN/(AU*vs**2))*(Wpp - Wpu)
    print(f"  v* = {vs:5.1f}: anisotropy / eps = {an:.3g};  |eps| at which it reaches 1 mm / 3.844e8 m = 2.6e-12: {2.6e-12/abs(an):.2g}")
