"""Critic check c4: independent reduced re-derivation of the dark-tests analysis
(its two verifiers returned no result), for the long-range chi-only attraction
U = -Gt m^2 W(|v - v'|/v*)/r, eps = Gt/G, Gaussian gate W = exp(-s^2/2).

Part 1  background (flat LCDM + radiation, Planck 2018 inputs, dagger) and the
        comoving gate radius s_c = v*(1+z)/H(z)  (dark-tests K2).
Part 2  density kernel R(y) = y Int_0^oo sin(yt) W(t) dt = sqrt2 y D(y/sqrt2) and the
        longitudinal velocity kernel R_v(y) = 1 + (3/2) Int W'(t) g2(yt) dt, which I
        derived independently and which equals K4's 3 Int_0^1 mu^2 R(y mu) dmu.
Part 3  quadrature of the anti-drag (force at fixed velocity) and of the
        anomalous velocity dU/dp of the Hamiltonian reading, for a particle moving
        with small u through a uniform Hubble-flow medium.  Expected:
        anti-drag      a = (4 pi/3)(Gt rho/H) u   -> rate (eps/2) Omega_c H
        anomalous vel. dx = (4 pi/3)(Gt rho/H^2) u -> (eps/2) Omega_c u   (critic gap G7)
Part 4  two-fluid sub-horizon growth from a = 1e-5 (smooth radiation; baryons
        held at zero before z_drag = 1060), transfer ratio T at the DESI pivot
        k_* = 0.009 s/km, z = 3, slope change dn, and the compressed-likelihood
        bound on eps (DESI DR1: Delta^2 = 0.379 +- 0.032, n = -2.309 +- 0.019,
        r = -0.1738; baseline 0.3495, -2.3052, as quoted by dark-tests K6 [S there]).
        Two readings: (a) dark-tests K4 (force at fixed velocity, anti-drag on);
        (b) Hamiltonian reading: (a) plus the anomalous-velocity factor (1 + a_v)
        in the continuity equation, a_v = (eps/2) Omega_c R_a(k s_c).
Part 5  Sgr gate average <W> (K13 inputs) in closed form.
"""
import numpy as np
import mpmath as mp

# ---------------- Part 1: background ----------------
h = 0.6736; H0 = 100 * h
Om = 0.3153; Ob = 0.02237 / h**2
Or = 2.473e-5 * (1 + 0.2271 * 3.046) / h**2      # photons + 3.046 massless neutrinos
OL = 1 - Om - Or
fb = Ob / Om; fc = 1 - fb
def E(a): return np.sqrt(Or * a**-4 + Om * a**-3 + OL)
def H(a): return H0 * E(a)
def dlnH(a):  # dlnH/dlna
    return 0.5 * (-4 * Or * a**-4 - 3 * Om * a**-3) / E(a)**2
def Omega_m(a): return Om * a**-3 / E(a)**2
print(f"background: Omega_r = {Or:.3e}, z_eq = {Om/Or - 1:.0f} (Planck 3402 +- 26), f_b = {fb:.4f}")
cl = 299792.458
def s_c(a, vs): return vs / (a * H(a))      # comoving Mpc
for z in (1089.92, 100, 10, 3, 0):
    a = 1 / (1 + z)
    print(f"  z = {z:8.2f}: H = {H(a):11.2f} km/s/Mpc, comoving s_c(v*=120) = {s_c(a,120):.4f} Mpc")
zz = np.linspace(0, 3, 30001); aa = 1 / (1 + zz)
i = np.argmax(s_c(aa, 120)); print(f"  peak of comoving s_c: {s_c(aa[i],120):.4f} Mpc at z = {zz[i]:.3f}  (K2: 2.0277 at 0.631)")

# ---------------- Part 2: kernels ----------------
mp.mp.dps = 30
def R_gauss(y):
    y = float(y)
    if y == 0: return 0.0
    x = y / np.sqrt(2)
    D = float(mp.sqrt(mp.pi) / 2 * mp.exp(-x**2) * mp.erfi(x))
    return np.sqrt(2) * y * D
# numeric check of R(1) by direct oscillatory quadrature
R1num = float(mp.quadosc(lambda t: mp.sin(t) * mp.exp(-t**2 / 2), [0, mp.inf], omega=1))
print(f"R(1): closed {R_gauss(1.0):.6f}, quadrature {R1num:.6f}  (K4: 0.724778)")
def g0(x): return 2 * np.sinc(x / np.pi)
def g2(x):
    x = np.asarray(x, float); out = np.empty_like(x)
    sm = np.abs(x) < 1e-2
    xs = x[sm]; out[sm] = 2/3 - xs**2/5 + xs**4/84
    xl = x[~sm]; out[~sm] = 2*(np.sin(xl)/xl + 2*np.cos(xl)/xl**2 - 2*np.sin(xl)/xl**3)
    return out
tq = np.linspace(0, 14, 28001)
Wp = -tq * np.exp(-tq**2 / 2); Wpp = (tq**2 - 1) * np.exp(-tq**2 / 2)
def R_v_mine(y): return 1 + 1.5 * np.trapezoid(Wp * g2(y * tq), tq)
def R_v_K4(y):
    mu = np.linspace(0, 1, 2001); return 3 * np.trapezoid(mu**2 * np.array([R_gauss(y*m) for m in mu]), mu)
def R_a(y): return 1 + 1.5 * np.trapezoid(tq * Wpp * g2(y * tq) + Wp * (g0(y * tq) - g2(y * tq)), tq)
for y in (0.3, 1.0, 3.0, 10.0):
    print(f"  y = {y:5.1f}: R = {R_gauss(y):.5f}, R_v(mine) = {R_v_mine(y):.5f}, R_v(K4 formula) = {R_v_K4(y):.5f}, R_a = {R_a(y):.5f}")

# ---------------- Part 3: anti-drag and anomalous velocity by quadrature ----------------
# units H = v* = Gt*rho = 1; medium in Hubble flow, particle at origin with velocity u along z
def quad_force(u, W, Wd):
    r = np.linspace(1e-6, 12, 6001); mu = np.polynomial.legendre.leggauss(400)
    m, wm = mu
    Rg, Mg = np.meshgrid(r, m, indexing='ij')
    s = np.sqrt(Rg**2 - 2 * Rg * u * Mg + u**2)
    Fz = 2 * np.pi * np.trapezoid(np.sum(W(s) * Mg * wm, axis=1), r)            # Int d^3x W x_hat_z / r^2
    Az = -2 * np.pi * np.trapezoid(np.sum(Rg * Wd(s) * (u - Rg * Mg) / s * wm, axis=1), r)  # -Int d^3x (1/r) W'(s) (u - x)_z/s
    return Fz, Az
gW = lambda s: np.exp(-s**2 / 2); gWd = lambda s: -s * np.exp(-s**2 / 2)
rW = lambda s: 1 / (1 + s**2 / 2); rWd = lambda s: -s / (1 + s**2 / 2)**2
for u in (0.003, 0.01):
    for nm, W, Wd in (("Gaussian", gW, gWd), ("rational", rW, rWd)):
        Fz, Az = quad_force(u, W, Wd)
        print(f"  u/v* = {u}: {nm:8s} anti-drag F/((4pi/3)u) = {Fz/(4*np.pi/3*u):.5f} ; anomalous velocity / ((4pi/3)u) = {Az/(4*np.pi/3*u):.5f}")

# ---------------- Part 4: growth and the Lyman-alpha bound ----------------
a_drag = 1 / 1061.0
zp = 3.0; ap = 1 / (1 + zp)
kp = 0.009 * H(ap) / (1 + zp)          # comoving 1/Mpc
print(f"pivot: k_* = 0.009 s/km at z = 3 -> {kp:.4f} /Mpc ; k_* s_c(z=3, v*=120) = {kp*s_c(ap,120):.4f} (K5: 0.6927, 1.080)")

ygrid = np.concatenate([np.linspace(0, 2, 401)[:-1], np.linspace(2, 60, 1161)])
Rtab = np.array([R_gauss(y) for y in ygrid])
Rvtab = np.array([R_v_mine(y) for y in ygrid])
Ratab = np.array([R_a(y) for y in ygrid])
def interp(tab, y): return np.interp(y, ygrid, tab, right=1.0)

def grow(k, eps, vs, hamiltonian=False, N0=np.log(1e-5), N1=np.log(ap), nstep=12000):
    # y = [dc, thc, db, thb]
    def rhs(N, Y):
        a = np.exp(N); y = k * s_c(a, vs)
        R = interp(Rtab, y); Rv = interp(Rvtab, y); Ra = interp(Ratab, y)
        Omm = Omega_m(a); Omc = fc * Omm
        A = 0.5 * eps * Omc * Rv
        av = 0.5 * eps * Omc * Ra if hamiltonian else 0.0
        dc, thc, db, thb = Y
        src_c = 1.5 * Omm * (fc * (1 + eps * R) * dc + fb * db)
        d_dc = -(1 + av) * thc
        d_thc = -(2 + dlnH(a) - A) * thc - src_c
        if a < a_drag:
            return np.array([d_dc, d_thc, 0.0, 0.0])
        src_b = 1.5 * Omm * (fc * dc + fb * db)
        return np.array([d_dc, d_thc, -thb, -(2 + dlnH(a)) * thb - src_b])
    Y = np.array([1.0, 0.0, 0.0, 0.0]); hN = (N1 - N0) / nstep; N = N0
    for _ in range(nstep):
        k1 = rhs(N, Y); k2 = rhs(N + hN/2, Y + hN/2*k1); k3 = rhs(N + hN/2, Y + hN/2*k2); k4 = rhs(N + hN, Y + hN*k3)
        Y = Y + hN/6*(k1 + 2*k2 + 2*k3 + k4); N += hN
    return fc * Y[0] + fb * Y[2], Y[2]

_base = {}
def grow0(kk, nstep):
    key = (round(kk, 12), nstep)
    if key not in _base:
        _base[key] = grow(kk, 0.0, 120.0, False, nstep=nstep)   # eps = 0: independent of v* and reading
    return _base[key]

def transfer(eps, vs, ham=False, dl=0.05, nstep=12000):
    out = {}
    for tag, kk in (("m", kp * np.exp(-dl)), ("0", kp), ("p", kp * np.exp(dl))):
        m1, b1 = grow(kk, eps, vs, ham, nstep=nstep); m0, b0 = grow0(kk, nstep)
        out[tag] = (m1 / m0, b1 / b0)
    Tm2 = out["0"][0]**2; Tb2 = out["0"][1]**2
    dn_m = (np.log(out["p"][0]**2) - np.log(out["m"][0]**2)) / (2 * dl)
    dn_b = (np.log(out["p"][1]**2) - np.log(out["m"][1]**2)) / (2 * dl)
    return Tm2, dn_m, Tb2, dn_b

# step-count convergence at one point
for ns in (6000, 12000):
    print(f"  convergence nstep={ns}: T^2, dn (matter) at eps=0.1, v*=120:", tuple(round(x, 5) for x in transfer(0.1, 120.0, nstep=ns)[:2]))
Tm2, dnm, Tb2, dnb = transfer(0.1, 120.0)
print(f"eps = 0.1, v* = 120 (reading a): T_m^2 = {Tm2:.4f}, dn_m = {dnm:+.4f} ; gas T_b^2 = {Tb2:.4f}, dn_b = {dnb:+.4f}   (K5: 1.0783, +0.1308)")
Tm2h, dnmh, _, _ = transfer(0.1, 120.0, ham=True)
print(f"eps = 0.1, v* = 120 (reading b, Hamiltonian): T_m^2 = {Tm2h:.4f}, dn_m = {dnmh:+.4f}")

D0, n0 = 0.3495, -2.3052
d = np.array([0.379, -2.309]); sD, sn, rho = 0.032, 0.019, -0.1738
C = np.array([[sD**2, rho*sD*sn], [rho*sD*sn, sn**2]]); Ci = np.linalg.inv(C)
def chi2(T2, dn):
    v = np.array([D0 * T2 - d[0], n0 + dn - d[1]]); return v @ Ci @ v
def bound(vs, which="m", ham=False):
    # T^2 and dn are ~linear in eps for small eps; tabulate and interpolate
    eg = np.array([0.0, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.56, 5.12, 10.24])
    vals = []
    for e in eg:
        if e == 0: vals.append((1.0, 0.0)); continue
        Tm2, dnm, Tb2, dnb = transfer(e, vs, ham, nstep=6000)
        vals.append((Tm2, dnm) if which == "m" else (Tb2, dnb))
    vals = np.array(vals)
    ef = np.linspace(0, eg[-1], 20001)
    T2f = np.interp(ef, eg, vals[:, 0]); dnf = np.interp(ef, eg, vals[:, 1])
    c2 = np.array([chi2(a, b) for a, b in zip(T2f, dnf)])
    cmin = c2.min(); above = np.where((c2 > cmin + 3.84) & (ef > ef[np.argmin(c2)]))[0]
    return (ef[above[0]] if len(above) else np.nan), chi2(1.0, 0.0) - cmin
for vs in (120.0, 30.0, 10.0):
    bm, dchi = bound(vs, "m"); bb, _ = bound(vs, "b"); bh, _ = bound(vs, "m", ham=True)
    print(f"v* = {vs:6.1f} km/s: eps_max (matter) = {bm:.4f}, (gas) = {bb:.4f}, (matter, Hamiltonian reading) = {bh:.4f}; "
          f"chi2(eps=0) - min = {dchi:.2f}")
print("dark-tests K6 for comparison: v*=120: 0.0285 / 0.0812 ; v*=30: 0.3484 / 1.1424 ; v*=10: 3.0825 / >10")

# ---------------- Part 5: Sgr gate average ----------------
V, s1, vs = 311.1, 149.9, 120.0
Wsgr = (vs**2 / (vs**2 + s1**2))**1.5 * np.exp(-V**2 / (2 * (vs**2 + s1**2)))
print(f"Sgr: <W> = {Wsgr:.4f} -> eps < 0.10/<W> = {0.10/Wsgr:.2f}  (K13: 0.066, 1.524)")
