"""Critic check c4c: robustness of c4b's consistent-reading transfer ratio at the
DESI pivot (eps = 0.1, v* = 120 km/s): step count, initial slope, start epoch,
plus the size of each O(eps) term at the pivot at z = 10 and z = 3.
Same equations as c4b (see its docstring)."""
import numpy as np
import mpmath as mp

def R_gauss(y):
    if y == 0: return 0.0
    x = y / np.sqrt(2)
    return float(np.sqrt(2) * y * mp.sqrt(mp.pi) / 2 * mp.exp(-x**2) * mp.erfi(x))
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
tq = np.linspace(0, 14, 28001)
Wp = -tq * np.exp(-tq**2 / 2); Wpp = (tq**2 - 1) * np.exp(-tq**2 / 2)
def R_v(y): return 1 + 1.5 * np.trapezoid(Wp * g2(y * tq), tq)
def R_a(y): return 1 + 1.5 * np.trapezoid(tq * Wpp * g2(y * tq) + Wp * (g0(y * tq) - g2(y * tq)), tq)
def J_W(y): return np.trapezoid(tq * Wp * j1(y * tq), tq)
h = 0.6736; H0 = 100 * h; Om = 0.3153; Ob = 0.02237 / h**2
Or = 2.473e-5 * (1 + 0.2271 * 3.046) / h**2; OL = 1 - Om - Or
fb = Ob / Om; fc = 1 - fb
def E(a): return np.sqrt(Or * a**-4 + Om * a**-3 + OL)
def Hf(a): return H0 * E(a)
def dlnH(a): return 0.5 * (-4 * Or * a**-4 - 3 * Om * a**-3) / E(a)**2
def Omega_m(a): return Om * a**-3 / E(a)**2
def s_c(a, vs): return vs / (a * Hf(a))
a_drag = 1 / 1061.0; ap = 0.25; kp = 0.009 * Hf(ap) / 4.0
ygrid = np.concatenate([np.linspace(0, 2, 401)[:-1], np.linspace(2, 60, 1161)])
Rt = np.array([R_gauss(y) for y in ygrid]); Rvt = np.array([R_v(y) for y in ygrid])
Rat = np.array([R_a(y) for y in ygrid]); yJt = np.array([y * J_W(y) for y in ygrid])
def I(tab, y, right): return np.interp(y, ygrid, tab, right=right)
def grow(k, eps, vs, nstep=6000, a0=1e-5, slope=0.0):
    N0, N1 = np.log(a0), np.log(ap)
    def rhs(N, Y):
        a = np.exp(N); y = k * s_c(a, vs)
        R = I(Rt, y, 1.0); Rv = I(Rvt, y, 1.0); Ra = I(Rat, y, 1.0); yJ = I(yJt, y, 0.0)
        Omm = Omega_m(a); Omc = fc * Omm
        A = 0.5 * eps * Omc * Rv; b = 0.5 * eps * Omc * Ra; thd = -1.5 * eps * Omc * yJ * Y[0]
        src = 1.5 * Omm * (fc * (1 + eps * R) * Y[0] + fb * Y[2])
        d = [-(1 + b) * Y[1] - thd, -(2 + dlnH(a) + b - A) * Y[1] - thd - src]
        if a < a_drag: return np.array(d + [0.0, 0.0])
        return np.array(d + [-Y[3], -(2 + dlnH(a)) * Y[3] - 1.5 * Omm * (fc * Y[0] + fb * Y[2])])
    Y = np.array([1.0, -slope, 0.0, 0.0]); hN = (N1 - N0) / nstep; N = N0
    for _ in range(nstep):
        k1 = rhs(N, Y); k2 = rhs(N + hN/2, Y + hN/2*k1); k3 = rhs(N + hN/2, Y + hN/2*k2); k4 = rhs(N + hN, Y + hN*k3)
        Y = Y + hN/6*(k1 + 2*k2 + 2*k3 + k4); N += hN
    return fc * Y[0] + fb * Y[2]
for label, kw in (("nstep 6000", {}), ("nstep 12000", {"nstep": 12000}), ("initial slope 0.5", {"slope": 0.5}),
                  ("start a = 1e-4", {"a0": 1e-4})):
    T2 = (grow(kp, 0.1, 120.0, **kw) / grow(kp, 0.0, 120.0, **kw))**2
    print(f"consistent reading, eps = 0.1, v* = 120, {label:18s}: T_m^2(k_*) = {T2:.6f}")
for z in (10.0, 3.0):
    a = 1 / (1 + z); y = kp * s_c(a, 120.0); Omc = fc * Omega_m(a)
    print(f"z = {z}: y = k_* s_c = {y:.3f}; per unit eps: gated source (3/2)Om_c R = {1.5*Omc*R_gauss(y):.3f}, "
          f"outflow (3/2)Om_c y|J_W| = {1.5*Omc*abs(y*J_W(y)):.3f}, inertia a_v R_a/eps = {0.5*Omc*R_a(y):+.3f}, "
          f"net anti-drag (A - a_v R_a)/eps = {0.5*Omc*(R_v(y)-R_a(y)):+.3f}")
