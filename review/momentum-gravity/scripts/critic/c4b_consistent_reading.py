"""Critic check c4b: the dark-tests Lyman-alpha bound under a self-consistent
(Hamiltonian = Lagrangian at first order in eps) reading of the velocity-gated
potential U = -Gt m^2 W(|w|/v*)/r, w the relative canonical momentum per mass
(Hubble flow + peculiar).  Dark-tests K4 used 'force = -grad_x U at fixed
velocity' with xdot = v, which follows from no Lagrangian.

Derivation (proper coordinates, sub-horizon, linear in eps and in perturbations;
q = peculiar canonical momentum per mass, u = peculiar velocity):
  xdot = p/m + dU/dp  ->  u = q + xa,   xa = a_v R_a(y) q + x_delta   (Fourier, longitudinal)
  qdot = -H q - H xa + F/m          (the -H xa term: Hubble-frame subtraction uses xdot)
  F/m  = gravity(all matter) + gated density force (kernel R, chi only) + anti-drag A q
  a_v = (eps/2) Omega_c,  A = (eps/2) Omega_c R_v(y),  y = k s_c,  s_c = v*/(aH) comoving
  div x_delta/(aH) = theta_delta = -(3/2) eps Omega_c y J_W(y) delta_c,
  J_W(y) = Int_0^oo t W'(t) j1(y t) dt  (< 0: outflow from overdensities).
In theta variables (theta = div/(aH)):
  delta_c' = -(1 + a_v R_a) theta_q - theta_delta
  theta_q' = -(2 + dlnH/dN + a_v R_a - A) theta_q - theta_delta - (3/2) Omega_m [f_c (1+eps R) delta_c + f_b delta_b]
Uniform limit (y >> 1): R = R_v = R_a = 1, J_W -> 0: the anti-drag A and the extra
drag a_v cancel exactly (a lone particle's peculiar velocity decays as 1/a), and
growth gets delta'' + ... = (3/2)(1+eps)(1+eps Omega_c/2) delta: EdS exponent shift 0.9 eps.

Checks in this script:
  (1) EdS growth-exponent shift of the consistent system in the uniform limit (expect 0.9).
  (2) R_a(y) by direct 3D quadrature of the exact anomalous velocity for a plane-wave
      peculiar-momentum field (independent of the g0/g2 angular formulas of c4).
  (3) J_W(y) by direct quadrature of the anomalous velocity from a sinusoidal density.
  (4) T^2, dn at the DESI pivot and the compressed-likelihood eps bound vs v*,
      readings: (a) dark-tests K4; (c) consistent.
"""
import numpy as np
import mpmath as mp
import sympy as sp

# ---------- (1) EdS uniform-limit exponent ----------
p, e = sp.symbols('p epsilon')
# delta ~ a^p ; uniform limit, EdS: Omega_m = Omega_c = 1, dlnH/dN = -3/2, a_v = A = eps/2
# delta' = -(1+eps/2) th ; th' = -(1/2 + eps/2 - eps/2) th - (3/2)(1+eps) delta
# -> delta'' + (1/2) delta' = (3/2)(1+eps)(1+eps/2) delta
sol = sp.solve(sp.Eq(p**2 + p/2, sp.Rational(3, 2) * (1 + e) * (1 + e/2)), p)
pp = [s for s in sol if sp.limit(s, e, 0) == 1][0]
print("(1) consistent reading, uniform limit, EdS: dp/deps at eps=0 =", sp.nsimplify(sp.diff(pp, e).subs(e, 0)),
      " (dark-tests K4: 0.8 with anti-drag, 0.6 without)")

# ---------- kernels ----------
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

# ---------- (2),(3) direct quadrature (units H = v* = Gt rho = 1, s = 1) ----------
def quad_Ra(y, amp=1e-3):
    r = np.linspace(1e-6, 12, 4001); m, wm = np.polynomial.legendre.leggauss(300)
    phi = np.linspace(0, 2*np.pi, 1, endpoint=False)  # axisymmetric: field along z, k along z
    Rg, Mg = np.meshgrid(r, m, indexing='ij'); zg = Rg * Mg
    # relative canonical momentum w = q0 - H r - q(r), q0 = amp z_hat, q(r) = amp cos(k z) z_hat
    wx_perp = -Rg * np.sqrt(1 - Mg**2)          # transverse magnitude (in the r-z plane)
    wz = -zg + amp * (1 - np.cos(y * zg))
    s = np.sqrt(wx_perp**2 + wz**2)
    Wd = -s * np.exp(-s**2 / 2)
    integrand = Rg * Wd * wz / s                 # (1/r) W'(s) w_z/s times r^2 -> r W' w_z/s
    xa_z = -2 * np.pi * np.trapezoid(np.sum(integrand * wm, axis=1), r)
    return xa_z / (4 * np.pi / 3 * amp)
def quad_JW(y):
    r = np.linspace(1e-6, 12, 4001); m, wm = np.polynomial.legendre.leggauss(300)
    Rg, Mg = np.meshgrid(r, m, indexing='ij')
    # xa = + Int d^3r delta(r) (1/r) W'(r) r_hat ; delta = sin(k z); z-component
    integrand = Rg * np.sin(y * Rg * Mg) * (-Rg * np.exp(-Rg**2 / 2)) * Mg
    xz = 2 * np.pi * np.trapezoid(np.sum(integrand * wm, axis=1), r)
    return xz / (4 * np.pi)
for y in (0.3, 1.0, 3.0):
    print(f"(2,3) y = {y}: R_a formula = {R_a(y):+.5f}, R_a quadrature = {quad_Ra(y):+.5f} ; "
          f"J_W formula = {J_W(y):+.5f}, J_W quadrature = {quad_JW(y):+.5f} ; R = {R_gauss(y):.5f}, R_v = {R_v(y):.5f}")

# ---------- (4) growth and bounds ----------
h = 0.6736; H0 = 100 * h; Om = 0.3153; Ob = 0.02237 / h**2
Or = 2.473e-5 * (1 + 0.2271 * 3.046) / h**2; OL = 1 - Om - Or
fb = Ob / Om; fc = 1 - fb
def E(a): return np.sqrt(Or * a**-4 + Om * a**-3 + OL)
def Hf(a): return H0 * E(a)
def dlnH(a): return 0.5 * (-4 * Or * a**-4 - 3 * Om * a**-3) / E(a)**2
def Omega_m(a): return Om * a**-3 / E(a)**2
def s_c(a, vs): return vs / (a * Hf(a))
a_drag = 1 / 1061.0; ap = 0.25
kp = 0.009 * Hf(ap) / 4.0
ygrid = np.concatenate([np.linspace(0, 2, 401)[:-1], np.linspace(2, 60, 1161)])
Rt = np.array([R_gauss(y) for y in ygrid]); Rvt = np.array([R_v(y) for y in ygrid])
Rat = np.array([R_a(y) for y in ygrid]); yJt = np.array([y * J_W(y) for y in ygrid])
def I(tab, y, right): return np.interp(y, ygrid, tab, right=right)

def grow(k, eps, vs, reading, nstep=6000):
    N0, N1 = np.log(1e-5), np.log(ap)
    def rhs(N, Y):
        a = np.exp(N); y = k * s_c(a, vs)
        R = I(Rt, y, 1.0); Rv = I(Rvt, y, 1.0); Ra = I(Rat, y, 1.0); yJ = I(yJt, y, 0.0)
        Omm = Omega_m(a); Omc = fc * Omm
        A = 0.5 * eps * Omc * Rv
        if reading == "a":       # dark-tests K4
            b = 0.0; thd_coef = 0.0; extra_drag = 0.0
        else:                    # consistent
            b = 0.5 * eps * Omc * Ra; thd_coef = -1.5 * eps * Omc * yJ; extra_drag = b
        dc, thq, db, thb = Y
        thd = thd_coef * dc
        src = 1.5 * Omm * (fc * (1 + eps * R) * dc + fb * db)
        d_dc = -(1 + b) * thq - thd
        d_thq = -(2 + dlnH(a) + extra_drag - A) * thq - thd - src
        if a < a_drag: return np.array([d_dc, d_thq, 0.0, 0.0])
        return np.array([d_dc, d_thq, -thb, -(2 + dlnH(a)) * thb - 1.5 * Omm * (fc * dc + fb * db)])
    Y = np.array([1.0, 0.0, 0.0, 0.0]); hN = (N1 - N0) / nstep; N = N0
    for _ in range(nstep):
        k1 = rhs(N, Y); k2 = rhs(N + hN/2, Y + hN/2*k1); k3 = rhs(N + hN/2, Y + hN/2*k2); k4 = rhs(N + hN, Y + hN*k3)
        Y = Y + hN/6*(k1 + 2*k2 + 2*k3 + k4); N += hN
    return fc * Y[0] + fb * Y[2], Y[2]
_b = {}
def g0run(kk):
    key = round(kk, 12)
    if key not in _b: _b[key] = grow(kk, 0.0, 120.0, "a")
    return _b[key]
def transfer(eps, vs, reading, dl=0.05):
    o = {}
    for t, kk in (("m", kp*np.exp(-dl)), ("0", kp), ("p", kp*np.exp(dl))):
        m1, b1 = grow(kk, eps, vs, reading); m0, b0 = g0run(kk); o[t] = (m1/m0, b1/b0)
    return (o["0"][0]**2, (np.log(o["p"][0]**2) - np.log(o["m"][0]**2)) / (2*dl),
            o["0"][1]**2, (np.log(o["p"][1]**2) - np.log(o["m"][1]**2)) / (2*dl))
for rd in ("a", "c"):
    Tm2, dnm, Tb2, dnb = transfer(0.1, 120.0, rd)
    print(f"(4) eps=0.1, v*=120, reading {rd}: T_m^2 = {Tm2:.4f}, dn_m = {dnm:+.4f}; T_b^2 = {Tb2:.4f}, dn_b = {dnb:+.4f}")

D0, n0 = 0.3495, -2.3052
d = np.array([0.379, -2.309]); sD, sn, rho = 0.032, 0.019, -0.1738
Ci = np.linalg.inv(np.array([[sD**2, rho*sD*sn], [rho*sD*sn, sn**2]]))
def chi2(T2, dn):
    v = np.array([D0*T2 - d[0], n0 + dn - d[1]]); return v @ Ci @ v
eg = np.array([0.0, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.56, 5.12, 10.24])
def bound(vs, reading):
    vm, vb = [(1.0, 0.0)], [(1.0, 0.0)]
    for e_ in eg[1:]:
        Tm2, dnm, Tb2, dnb = transfer(e_, vs, reading); vm.append((Tm2, dnm)); vb.append((Tb2, dnb))
    res = []
    for vals in (np.array(vm), np.array(vb)):
        ef = np.linspace(0, eg[-1], 20001)
        c2 = np.array([chi2(a_, b_) for a_, b_ in zip(np.interp(ef, eg, vals[:, 0]), np.interp(ef, eg, vals[:, 1]))])
        i0 = np.argmin(c2); ab = np.where((c2 > c2[i0] + 3.84) & (ef > ef[i0]))[0]
        res.append(ef[ab[0]] if len(ab) else np.inf)
    return res, np.array(vm)
for vs in (10.0, 30.0, 50.0, 120.0, 300.0, 1000.0):
    (bm_a, bb_a), _ = bound(vs, "a")
    (bm_c, bb_c), vmc = bound(vs, "c")
    i1 = list(eg).index(0.16)
    print(f"v* = {vs:7.1f}: reading a (K4): eps_max matter {bm_a:.4f} gas {bb_a:.4f} | consistent: matter {bm_c:.4f} gas {bb_c:.4f}"
          f"  [consistent T_m^2, dn at eps=0.16: {vmc[i1,0]:.4f}, {vmc[i1,1]:+.4f}]")
print("dark-tests K6 (reading a): 10: 3.08/>10; 30: 0.348/1.14; 50: 0.13/0.42; 120: 0.0285/0.081; 300: 0.014/0.023; 1000: 0.017/0.017")
