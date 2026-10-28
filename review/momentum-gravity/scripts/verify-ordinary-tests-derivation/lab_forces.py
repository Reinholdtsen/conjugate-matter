"""Lab-scale consequences of the velocity-dependent Lagrangian (checks O21; missed effects).

Model: body of mass m in the Earth's field, Earth's centre of mass at rest (Sun ignored here),
    L = m|v|^2/2 + (GM m/|r|)(1 + eps W(|v|/v*)),   v relative to the Earth's centre of mass.
Euler-Lagrange: M(v) a + (d2L/dv dr) v = dL/dr, with the velocity Hessian
    M_ij = m d_ij + (GM m/r) eps [W''(u)/v*^2 w_i w_j + W'(u)/(v* |v|) (d_ij - w_i w_j)],  w = v/|v|.
(1) static weight of a body held on the rotating Earth (sympy, exact trajectory);
(2) free-fall acceleration of a body released co-moving with the surface (exact 3x3 solve);
(3) the weight of a spinning horizontal rotor: correct vertical force vs the agent's <K(u_el)>.
"""
import numpy as np
import sympy as sp

print("=== (1) held body on the rotating Earth: generalized force on the exact trajectory ===")
t, R, Om, phi, eps, vs, GMm = sp.symbols('t R Omega phi epsilon v_s GMm', positive=True)
Wf = sp.Function('W')
rvec = sp.Matrix([R*sp.cos(phi)*sp.cos(Om*t), R*sp.cos(phi)*sp.sin(Om*t), R*sp.sin(phi)])
vvec = rvec.diff(t)
X = sp.Matrix(sp.symbols('x y z'))
Vv = sp.Matrix(sp.symbols('vx vy vz'))
Lint = GMm/sp.sqrt(X.dot(X))*(1 + eps*Wf(sp.sqrt(Vv.dot(Vv))/vs))
dLdr = sp.Matrix([sp.diff(Lint, xi) for xi in X])
dLdv = sp.Matrix([sp.diff(Lint, vi) for vi in Vv])
subsd = {**{X[i]: rvec[i] for i in range(3)}, **{Vv[i]: vvec[i] for i in range(3)}}
Q = dLdr.subs(subsd) - dLdv.subs(subsd).diff(t)
rhat = rvec/R
Qr = sp.simplify((Q.T*rhat)[0].doit())
u = sp.symbols('u', positive=True)
w_surf = R*Om*sp.cos(phi)
Qr_u = sp.simplify(Qr.subs(Om, u*vs/(R*sp.cos(phi))))
print("  Q.rhat * R^2/GMm =", sp.simplify(Qr_u*R**2/GMm))
print("  [expected -(1 + eps (W(u) - u W'(u))) with u = Omega R cos(phi)/v*]")
# north component
north = sp.Matrix([-sp.sin(phi)*sp.cos(Om*t), -sp.sin(phi)*sp.sin(Om*t), sp.cos(phi)])
Qn = sp.simplify((Q.T*north)[0].doit().subs(Om, u*vs/(R*sp.cos(phi))))
print("  Q.north * R^2/GMm =", sp.simplify(Qn*R**2/GMm), "  [plumb-line tilt term]")

print()
print("=== (2) free fall from co-moving with the surface: a = M^-1 dL/dr ===")
GM_E, R_E = 398600.4418, 6378.137        # km^3/s^2, km (dagger)
OM_E = 7.2921150e-5                      # rad/s (dagger)
vc2 = GM_E/R_E
print(f"  v_c^2 = GM/R = {vc2:.2f} km^2/s^2 (v_c = {np.sqrt(vc2):.3f} km/s)")

def shapes(name):
    if name == 'gauss':
        return (lambda x: np.exp(-x**2), lambda x: -2*x*np.exp(-x**2), lambda x: (4*x**2 - 2)*np.exp(-x**2))
    return (lambda x: 1/(1 + x**2), lambda x: -2*x/(1 + x**2)**2, lambda x: (6*x**2 - 2)/(1 + x**2)**3)

def freefall_factor(name, vstar, lat_deg, epsv):
    W, Wp, Wpp = shapes(name)
    lat = np.radians(lat_deg)
    r = R_E*np.array([np.cos(lat), 0.0, np.sin(lat)])
    v = np.array([0.0, OM_E*R_E*np.cos(lat), 0.0])
    s = np.linalg.norm(v)
    rr = np.linalg.norm(r)
    if s == 0:
        Mh = np.eye(3)*(1 + epsv*(GM_E/rr)*Wpp(0.0)/vstar**2)   # W'(u)/u -> W''(0)
        Wv = W(0.0)
    else:
        uu = s/vstar
        wh = v/s
        Mh = np.eye(3) + epsv*(GM_E/rr)*(Wpp(uu)/vstar**2*np.outer(wh, wh) + Wp(uu)/(vstar*s)*(np.eye(3) - np.outer(wh, wh)))
        Wv = W(uu)
    F = -(GM_E/rr**2)*(1 + epsv*Wv)*r/rr       # per unit m; (d2L/dv dr) v = 0 since r.v = 0
    a = np.linalg.solve(Mh, F)
    return np.dot(a, -r/rr)/(GM_E/rr**2), Mh

for name in ('gauss', 'lorentz'):
    for vstar in (0.1, 0.3, 1.0):
        epsv = 1e-12
        row = []
        for lat in (90.0, 80.0, 60.0, 45.0, 0.0):
            fac, _ = freefall_factor(name, vstar, lat, epsv)
            row.append(f"lat {lat:4.0f}: {(fac - 1)/epsv:10.4g}")
        print(f"  {name:7s} v*={vstar:4.1f} km/s, (g_ff/g_N - 1)/eps: " + "; ".join(row))
print("  pole, analytic: (g_ff/g_N - 1)/eps -> 1 + 2 v_c^2/v*^2 =",
      "; ".join(f"v*={vs_}: {1 + 2*vc2/vs_**2:.4g}" for vs_ in (0.1, 0.3, 1.0)))
print("  inertia at the pole: m_eff/m = 1 - 2 eps v_c^2/v*^2 -> zero at eps =",
      "; ".join(f"v*={vs_}: {vs_**2/(2*vc2):.3g}" for vs_ in (0.1, 0.17, 0.3, 1.0)))
# compare: satellites (u = 7.6 km/s / v*) see K(u_sat)
for vstar in (0.1, 0.3, 1.0):
    W, Wp, Wpp = shapes('gauss')
    us = 7.6/vstar
    print(f"  Gaussian, satellite at 7.6 km/s, v*={vstar}: K(u_sat) = {W(us) - us*Wp(us):.3g}")

print()
print("=== (3) spinning horizontal rotor at latitude phi: vertical (lab-up) force factor ===")
# element velocity relative to Earth CM: w = V_lab e_E + v_rot (horizontal); dw/dt = Omega x w + spin part (horizontal)
# vertical generalized force: -(GMm/R^2)[1 + eps (W(u_el) - u_lab W'(u_el) (w_E/|w|))]
def rotor_factors(name, vstar, lat_deg, vrim):
    W, Wp, _ = shapes(name)
    Vl = OM_E*R_E*np.cos(np.radians(lat_deg))
    ul = Vl/vstar
    nr, nth = 400, 720
    rho = (np.arange(nr) + 0.5)/nr                   # radius fraction
    th = (np.arange(nth) + 0.5)*2*np.pi/nth
    RHO, TH = np.meshgrid(rho, th, indexing='ij')
    wt = RHO*2*np.pi/nr*np.ones_like(TH)               # area weight ~ rho drho dtheta
    vE = Vl + vrim*RHO*(-np.sin(TH))
    vN = vrim*RHO*np.cos(TH)
    sp_ = np.hypot(vE, vN)
    uel = sp_/vstar
    correct = W(uel) - ul*Wp(uel)*(vE/sp_)
    agent = W(uel) - uel*Wp(uel)
    K0 = W(ul) - ul*Wp(ul)
    avg = lambda f: np.sum(f*wt)/np.sum(wt)
    return avg(correct) - K0, avg(agent) - K0

for (vrim, vstar, lat) in [(60, 0.1, 48.8), (30, 0.1, 35.7), (60, 0.3, 48.8), (60, 1.0, 48.8)]:
    dc, da = rotor_factors('gauss', vstar, lat, vrim/1000.0)
    print(f"  Gaussian v_rim={vrim} m/s v*={vstar} lat={lat}: Delta(factor) correct {dc:+.3e}; agent's <K(u_el)> {da:+.3e}")
