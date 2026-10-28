"""Critic check c4d: the three O(eps) velocity kernels of the consistent reading
(c4b) were derived independently: anti-drag R_v, inertia R_a, density-gradient
outflow J_W.  If the linear system is Hamiltonian, the momentum-dependence of the
force and the position(density)-dependence of the anomalous velocity are mixed
second derivatives of one U, which predicts R_v - R_a = -3 y J_W.  Checked here
on a y grid by direct quadrature of each kernel (Gaussian gate)."""
import numpy as np
def g0(x): return 2 * np.sinc(x / np.pi)
def g2(x):
    x = np.asarray(x, float); out = np.empty_like(x); sm = np.abs(x) < 1e-2
    xs = x[sm]; out[sm] = 2/3 - xs**2/5 + xs**4/84
    xl = x[~sm]; out[~sm] = 2*(np.sin(xl)/xl + 2*np.cos(xl)/xl**2 - 2*np.sin(xl)/xl**3)
    return out
def j1(x):
    x = np.asarray(x, float); out = np.empty_like(x); sm = np.abs(x) < 1e-3
    out[sm] = x[sm]/3 - x[sm]**3/30
    xl = x[~sm]; out[~sm] = np.sin(xl)/xl**2 - np.cos(xl)/xl
    return out
t = np.linspace(0, 14, 56001)
Wp = -t * np.exp(-t**2 / 2); Wpp = (t**2 - 1) * np.exp(-t**2 / 2)
for y in (0.1, 0.3, 0.7, 1.0, 1.5, 3.0, 6.0):
    Rv = 1 + 1.5 * np.trapezoid(Wp * g2(y * t), t)
    Ra = 1 + 1.5 * np.trapezoid(t * Wpp * g2(y * t) + Wp * (g0(y * t) - g2(y * t)), t)
    JW = np.trapezoid(t * Wp * j1(y * t), t)
    print(f"y = {y:4.1f}: R_v - R_a = {Rv - Ra:+.6f} ; -3 y J_W = {-3 * y * JW:+.6f} ; difference {Rv - Ra + 3*y*JW:+.1e}")
