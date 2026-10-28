"""Exact-trajectory check of the rotor weight formula used in lab_forces.py (claim O21).

A rotor element moves on r(t) = R_lab(t) + rho0 [cos(w_r t) e_E(t) + sin(w_r t) e_N(t)] on the rotating
Earth. The generalized force Q = dL/dr - d/dt(dL/dv) of L_int = (GMm/|r|)(1 + eps exp(-|v|^2/v*^2)) is
computed symbolically on that trajectory, projected on the lab vertical, averaged over one rotor turn,
and compared with
    correct:  W(u_el) - u_lab W'(u_el) (w_E/|w|)        agent:  K(u_el) = W(u_el) - u_el W'(u_el).
Units: R = 1, GMm = 1. rho0 -> small at fixed rim speed.
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
t, Om, phi, eps, vs, rho0, wr = sp.symbols('t Omega phi epsilon v_s rho0 w_r', positive=True)
c, s_ = sp.cos(Om*t), sp.sin(Om*t)
Rlab = sp.Matrix([sp.cos(phi)*c, sp.cos(phi)*s_, sp.sin(phi)])
eE = sp.Matrix([-s_, c, 0])
eN = sp.Matrix([-sp.sin(phi)*c, -sp.sin(phi)*s_, sp.cos(phi)])
r = Rlab + rho0*(sp.cos(wr*t)*eE + sp.sin(wr*t)*eN)
v = r.diff(t)
X = sp.Matrix(sp.symbols('x y z'))
V = sp.Matrix(sp.symbols('vx vy vz'))
L = 1/sp.sqrt(X.dot(X))*(1 + eps*sp.exp(-V.dot(V)/vs**2))
dLdr = sp.Matrix([sp.diff(L, q) for q in X])
dLdv = sp.Matrix([sp.diff(L, q) for q in V])
sub = {**{X[i]: r[i] for i in range(3)}, **{V[i]: v[i] for i in range(3)}}
Q = dLdr.subs(sub) - dLdv.subs(sub).diff(t)
Qup = (Q.T*Rlab)[0]                       # lab vertical (unit vector since R = 1)
# first-order-in-eps part
Q1 = sp.diff(Qup, eps)
f = sp.lambdify((t, Om, phi, vs, rho0, wr), Q1, 'mpmath')

def W(x): return mp.exp(-x**2)
def Wp(x): return -2*x*mp.exp(-x**2)

for (ulab, urim, latdeg) in [(3.064, 0.6, 48.8), (0.306, 0.06, 48.8), (1.0, 0.2, 40.0)]:
    vsv = mp.mpf(1)/100            # v* in units of sqrt(GM/R); only ratios matter here
    lat = mp.radians(latdeg)
    Omv = ulab*vsv/mp.cos(lat)     # so that Omega R cos(phi) = u_lab v*
    rho = mp.mpf('1e-12')
    wrv = urim*vsv/rho
    N = 64
    Tr = 2*mp.pi/wrv
    avg_exact = mp.fsum(f(k*Tr/N, Omv, lat, vsv, rho, wrv) for k in range(N))/N
    # formulas, averaged over the same rotor phases (element at the rim)
    corr, agent = [], []
    for k in range(N):
        th = 2*mp.pi*k/N
        wE = ulab + urim*(-mp.sin(th))
        wN = urim*mp.cos(th)
        uel = mp.sqrt(wE**2 + wN**2)
        corr.append(W(uel) - ulab*Wp(uel)*wE/uel)
        agent.append(W(uel) - uel*Wp(uel))
    print(f"u_lab={ulab}, u_rim={urim}, lat={latdeg}: exact-trajectory <dQ_up/deps> = {mp.nstr(-avg_exact, 12)};"
          f" correct formula {mp.nstr(mp.fsum(corr)/N, 12)}; agent's <K(u_el)> {mp.nstr(mp.fsum(agent)/N, 12)}")
