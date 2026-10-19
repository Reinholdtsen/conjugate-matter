"""lambda->inf monopole (H=1): f = min int [K'^2 + (K^2-1)^2/(2xi^2) + K^2], with analytic tail 1/(2L) beyond xi=L."""
import numpy as np
from scipy.integrate import solve_bvp
def f(x, y):
    K, Kp = y
    return np.vstack([Kp, K*(K**2-1)/x**2 + K])
def bc(ya, yb):
    return np.array([ya[0]-1, yb[0]])
for L in [30.0, 40.0, 60.0]:
    for x0 in [1e-3]:
        xi = np.concatenate([np.geomspace(x0, 1, 400)[:-1], np.linspace(1, L, 3000)])
        # guess: regular small-xi behaviour K~1-a xi^2, decaying as exp(-xi) at large xi
        Kg = (1 + xi) * np.exp(-xi)
        y0 = np.vstack([Kg, -xi*np.exp(-xi)])
        s = solve_bvp(f, bc, xi, y0, tol=1e-7, max_nodes=300000)
        K, Kp = s.sol(xi)
        E = np.trapezoid(Kp**2 + (K**2-1)**2/(2*xi**2) + K**2, xi)
        # small-xi piece [0,x0]: K~1 -> integrand ~ K'^2+... ~ O(x0) negligible
        print(f"L={L:5.1f} x0={x0:.0e} status={s.status} msg='{s.message[:40]}' E(0..L)={E:.5f}  +tail 1/(2L)={1/(2*L):.5f} -> f_inf={E+1/(2*L):.4f}")
