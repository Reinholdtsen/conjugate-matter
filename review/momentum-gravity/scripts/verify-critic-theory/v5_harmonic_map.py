"""
v5_harmonic_map.py  (verify-critic-theory, round 3) -- claim c6D.

H = sum_a [p_a^2/2m + Phi(x_a)] + U(p_1 - p_2)   (1D per component; two particles; m, Omega equal)

1. sympy: for Phi = m Omega^2 x^2/2 the map X_a = p_a/(m Omega), P_a = -m Omega x_a is canonical
   and gives H' = sum [P_a^2/2m + m Omega^2 X_a^2/2] + U(m Omega (X_1 - X_2)).
   Hamilton's equations: pdot_a = -dPhi/dx_a for ANY Phi -- the momentum-only term never enters pdot.
2. numerics (m = Omega = mu = 1, U = -g exp(-(p1-p2)^2/2), g = 0.3, RK4):
   a. harmonic trap: integrate the original system and the mapped system; check X(t) = p(t)/(m Omega).
   b. relative momentum p1 - p2 with and without U in: free space, uniform field, harmonic trap,
      quartic trap.  In free space and in a uniform field d(p1-p2)/dt = 0 identically, so U cannot
      change relative momenta; in a curved potential it changes them indirectly (through x).
"""
import numpy as np
import sympy as sp

print("1. symbolic canonical map")
m, W = sp.symbols('m Omega', positive=True)
x1, x2, p1, p2 = sp.symbols('x1 x2 p1 p2', real=True)
U = sp.Function('U')
X1, X2 = p1 / (m * W), p2 / (m * W)
P1, P2 = -m * W * x1, -m * W * x2
def pb(f, g):
    return sp.simplify(sum(sp.diff(f, q) * sp.diff(g, pp) - sp.diff(f, pp) * sp.diff(g, q)
                           for q, pp in [(x1, p1), (x2, p2)]))
print("  {X1,P1} =", pb(X1, P1), " {X2,P2} =", pb(X2, P2), " {X1,X2} =", pb(X1, X2),
      " {P1,P2} =", pb(P1, P2), " {X1,P2} =", pb(X1, P2))
H = (p1 ** 2 + p2 ** 2) / (2 * m) + m * W ** 2 * (x1 ** 2 + x2 ** 2) / 2 + U(p1 - p2)
Xs1, Xs2, Ps1, Ps2 = sp.symbols('X1 X2 P1 P2', real=True)
Hn = H.subs({p1: m * W * Xs1, p2: m * W * Xs2, x1: -Ps1 / (m * W), x2: -Ps2 / (m * W)})
print("  H in (X,P):", sp.simplify(Hn))
Phi = sp.Function('Phi')
Hg = (p1 ** 2 + p2 ** 2) / (2 * m) + Phi(x1) + Phi(x2) + U(p1 - p2)
print("  general Phi: pdot1 = -dH/dx1 =", -sp.diff(Hg, x1), ";  xdot1 = dH/dp1 =", sp.diff(Hg, p1))

print("\n2. numerics")
g, mu = 0.3, 1.0
def Uprime(d):            # dU/d(d), U = -g exp(-d^2/(2 mu^2))
    return g * d / mu ** 2 * np.exp(-d ** 2 / (2 * mu ** 2))

def rhs(y, dPhi, withU=True):
    xa, xb, pa, pb_ = y
    d = pa - pb_
    up = Uprime(d) if withU else 0.0
    return np.array([pa + up, pb_ - up, -dPhi(xa), -dPhi(xb)])

def rk4(y, dPhi, withU, dt, n):
    out = [y.copy()]
    for _ in range(n):
        k1 = rhs(y, dPhi, withU); k2 = rhs(y + dt / 2 * k1, dPhi, withU)
        k3 = rhs(y + dt / 2 * k2, dPhi, withU); k4 = rhs(y + dt * k3, dPhi, withU)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        out.append(y.copy())
    return np.array(out)

dt, n = 1e-3, 20000
y0 = np.array([0.7, -0.4, 0.3, -0.5])   # x1, x2, p1, p2

# a. harmonic: mapped system H' = sum P^2/2 + X^2/2 + U(X1 - X2) (m = Omega = 1): Xdot = P, Pdot = -X - U'(X1-X2)
def rhs_mapped(z):
    Xa, Xb, Pa, Pb = z
    up = Uprime(Xa - Xb)
    return np.array([Pa, Pb, -Xa - up, -Xb + up])
z = np.array([y0[2], y0[3], -y0[0], -y0[1]])   # X = p, P = -x
traj = rk4(y0, lambda x: x, True, dt, n)
zs = [z.copy()]
for _ in range(n):
    k1 = rhs_mapped(z); k2 = rhs_mapped(z + dt / 2 * k1); k3 = rhs_mapped(z + dt / 2 * k2); k4 = rhs_mapped(z + dt * k3)
    z = z + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); zs.append(z.copy())
zs = np.array(zs)
err = max(np.max(np.abs(zs[:, 0] - traj[:, 2])), np.max(np.abs(zs[:, 1] - traj[:, 3])),
          np.max(np.abs(zs[:, 2] + traj[:, 0])), np.max(np.abs(zs[:, 3] + traj[:, 1])))
print(f"  a. harmonic trap, t = {n*dt:.0f}: max |mapped - original| over the run = {err:.2e}")

# b. relative momentum with and without U
cases = {"free space": lambda x: 0.0 * x,
         "uniform field (Phi = 0.8 x)": lambda x: 0.8 + 0.0 * x,
         "harmonic (Phi = x^2/2)": lambda x: x,
         "quartic (Phi = x^4/4)": lambda x: x ** 3}
for name, dPhi in cases.items():
    tw = rk4(y0, dPhi, True, dt, n); tn = rk4(y0, dPhi, False, dt, n)
    dpw = tw[:, 2] - tw[:, 3]; dpn = tn[:, 2] - tn[:, 3]
    print(f"  b. {name:28s}: max over t<={n*dt:.0f} of |(p1-p2)_withU - (p1-p2)_noU| = {np.max(np.abs(dpw - dpn)):.3e};"
          f"  (p1-p2) drift with U: {np.max(np.abs(dpw - dpw[0])):.3e}")
