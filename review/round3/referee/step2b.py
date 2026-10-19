"""Step 2b: own numerical solution of the 't Hooft-Polyakov monopole to check f (M = 4 pi f v/g).
Energy (units 4 pi v/g), xi = g v r, Phi^a = v H rhat^a, A^a_i = eps_aij rhat_j (1-K)/(g r):
  E = int_0^inf dxi [ K'^2 + (K^2-1)^2/(2 xi^2) + xi^2 H'^2/2 + K^2 H^2 + mu xi^2 (H^2-1)^2 ]
mu is proportional to lambda/g^2. BPS (mu=0): K = xi/sinh xi, H = coth xi - 1/xi, E = 1.
"""
import numpy as np
from scipy.integrate import solve_bvp, quad

def energy(K, Kp, H, Hp, xi, mu):
    return Kp**2 + (K**2 - 1)**2 / (2 * xi**2) + xi**2 * Hp**2 / 2 + K**2 * H**2 + mu * xi**2 * (H**2 - 1)**2

# 1) normalisation check with the analytic BPS solution
def bps(xi):
    K = xi / np.sinh(xi)
    Kp = (np.sinh(xi) - xi * np.cosh(xi)) / np.sinh(xi)**2
    H = 1 / np.tanh(xi) - 1 / xi
    Hp = -1 / np.sinh(xi)**2 + 1 / xi**2
    return K, Kp, H, Hp
E_bps = quad(lambda x: energy(*bps(x), x, 0.0), 1e-6, 60, limit=400)[0]
print(f"BPS analytic solution energy (units 4 pi v/g): {E_bps:.6f}  (expect 1)")

# 2) lambda -> infinity: H == 1, minimise over K
L = 40.0
xi = np.linspace(1e-4, L, 4000)
def f_inf(x, y):
    K, Kp = y
    return np.vstack([Kp, K * (K**2 - 1) / x**2 + K])
def bc_inf(ya, yb):
    return np.array([ya[0] - 1, yb[0]])
y0 = np.vstack([np.exp(-xi), -np.exp(-xi)])
sol = solve_bvp(f_inf, bc_inf, xi, y0, tol=1e-9, max_nodes=200000)
K, Kp = sol.sol(xi)
Einf = np.trapezoid(Kp**2 + (K**2 - 1)**2 / (2 * xi**2) + K**2, xi)
print(f"lambda->inf (H=1): solve_bvp status={sol.status}, f_inf = E = {Einf:.4f}")

# 3) finite mu: coupled system, continuation in mu
def make(mu):
    def f(x, y):
        K, Kp, H, Hp = y
        Kpp = K * (K**2 - 1) / x**2 + K * H**2
        # (x^2 H')' = 2 K^2 H + 4 mu x^2 H (H^2-1)  ->  H'' = [2K^2H + 4mu x^2 H(H^2-1) - 2x H']/x^2
        Hpp = (2 * K**2 * H + 4 * mu * x**2 * H * (H**2 - 1) - 2 * x * Hp) / x**2
        return np.vstack([Kp, Kpp, Hp, Hpp])
    return f
def bc(ya, yb):
    return np.array([ya[0] - 1, ya[2], yb[0], yb[2] - 1])
xg = np.linspace(1e-3, L, 3000)
Kb, Kbp, Hb, Hbp = bps(xg)
guess = np.vstack([Kb, Kbp, Hb, Hbp])
res = []
for mu in [1e-4, 0.01, 0.1, 0.5, 1, 3, 10, 30, 100, 300, 1000, 3000]:
    s = solve_bvp(make(mu), bc, xg, guess, tol=1e-6, max_nodes=500000)
    K, Kp, H, Hp = s.sol(xg)
    E = np.trapezoid(energy(K, Kp, H, Hp, xg, mu), xg)
    res.append((mu, s.status, E))
    if s.status == 0:
        guess = s.sol(xg)
    print(f"mu={mu:<7} status={s.status} f = E = {E:.4f}")
