"""Linear growth of the corner model at high k (round 3, label "corner").

Model: chi-only gated attraction U = -eps G m^2 W(|w-w'|/v*)/r, W = exp(-s^2/2), gate set by the
Hubble flow in the linear regime (dark-tests K2/K3), sub-horizon two-fluid linear theory.
Two readings of the velocity-dependent potential, both copied from round 2 and not re-derived here:
  'K4'  force = -grad_x U at fixed velocity (dark-tests K4; = the N-body 'F' reading):
        dc' = -th ; th' = -(2 + dlnH/dN - A) th - S
  'H'   Hamiltonian, gate on canonical momentum (critic c4b; = the N-body 'H' reading):
        dc' = -(1 + b) th - thd ; th' = -(2 + dlnH/dN + b - A) th - thd - S
  with A = (eps/2) Om_c Rv(y), b = (eps/2) Om_c Ra(y), thd = -(3/2) eps Om_c y J_W(y) dc,
  S = (3/2) Om_m [f_c (1 + eps R(y)) dc + f_b db], y = k v*/(aH)  (kernels R, Rv, Ra, J_W of c4b,
  recomputed here by the same quadratures; their anchors in c4b passed direct 3D quadrature).
  Baryons: db = 0 before z_drag, then gravity only, pressureless (reduction).
Background, EH98 no-wiggle P(k), sigma8 normalization: dark-tests cosmo.py (Planck 2018 [S]).
Both systems are linear in perturbations; the H system's derivation (critic c4b) is unreviewed.

Outputs (all linear theory; 'T2' = P_gated/P_LCDM of total matter):
  (1) T2 at the high-resolution Lyman-alpha scales k = 0.02-0.2 s/km, z = 3, 4.2, 5;
  (2) sigma(M, z) and 1-sigma collapse redshifts z_c (sigma = 1.686, a proxy) for M = 1e2..1e10 Msun;
  (3) the comoving gate radius and the matter-era growth exponents in the uniform limit (analytic anchor).
"""
import os
import sys
import numpy as np
import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dark-tests"))
import cosmo as C   # noqa: E402

# ---------------- kernels (c4b definitions) ----------------
def R_gauss(y):
    if y == 0:
        return 0.0
    x = y / np.sqrt(2)
    return float(np.sqrt(2) * y * mp.sqrt(mp.pi) / 2 * mp.exp(-x**2) * mp.erfi(x))


def _g0(x):
    return 2 * np.sinc(x / np.pi)


def _g2(x):
    x = np.asarray(x, float); out = np.empty_like(x); sm = np.abs(x) < 1e-2
    xs = x[sm]; out[sm] = 2/3 - xs**2/5 + xs**4/84
    xl = x[~sm]; out[~sm] = 2*(np.sin(xl)/xl + 2*np.cos(xl)/xl**2 - 2*np.sin(xl)/xl**3)
    return out


def _j1(x):
    x = np.asarray(x, float); out = np.empty_like(x); sm = np.abs(x) < 1e-3
    out[sm] = x[sm]/3 - x[sm]**3/30
    xl = x[~sm]; out[~sm] = np.sin(xl)/xl**2 - np.cos(xl)/xl
    return out


_tq = np.linspace(0, 14, 28001)
_Wp = -_tq * np.exp(-_tq**2 / 2); _Wpp = (_tq**2 - 1) * np.exp(-_tq**2 / 2)


def R_v(y): return 1 + 1.5 * np.trapezoid(_Wp * _g2(y * _tq), _tq)
def R_a(y): return 1 + 1.5 * np.trapezoid(_tq * _Wpp * _g2(y * _tq) + _Wp * (_g0(y * _tq) - _g2(y * _tq)), _tq)
def J_W(y): return np.trapezoid(_tq * _Wp * _j1(y * _tq), _tq)


YG = np.concatenate([np.linspace(0, 2, 401)[:-1], np.linspace(2, 60, 1161)])
TAB = dict(R=np.array([R_gauss(y) for y in YG]), Rv=np.array([R_v(y) for y in YG]),
           Ra=np.array([R_a(y) for y in YG]), yJ=np.array([y * J_W(y) for y in YG]))


def I(name, y):
    right = 0.0 if name == "yJ" else 1.0
    return np.interp(y, YG, TAB[name], right=right)


# ---------------- growth ----------------
fc, fb = C.f_c, C.f_b
a_drag = 1.0 / (1.0 + C.z_drag)


def grow(k, eps, vs, reading, z_out, a_i=1e-5, nstep=8000):
    """Return dict z -> total-matter delta (array over k), normalized arbitrarily (same IC for all)."""
    k = np.atleast_1d(np.asarray(k, float))
    N = np.linspace(np.log(a_i), 0.0, nstep)
    zs = sorted(z_out, reverse=True)
    Ns = [np.log(1 / (1 + z)) for z in zs]
    Y = np.zeros((4, k.size)); Y[0] = 1.0; Y[1] = 0.0   # dc, th (th = -dc' in K4), db, thb

    def rhs(Nv, Y):
        a = np.exp(Nv)
        y = k * vs / (a * C.H0 * C.E(a))
        Omm = C.Omega_m_a(a); Omc = fc * Omm
        dlnH = C.dlnH_dlna(a)
        dc, th, db, thb = Y
        R = I("R", y); A = 0.5 * eps * Omc * I("Rv", y)
        if reading == "H":
            b = 0.5 * eps * Omc * I("Ra", y)
            thd = -1.5 * eps * Omc * I("yJ", y) * dc
        else:
            b = 0.0; thd = 0.0
        src = 1.5 * Omm * (fc * (1 + eps * R) * dc + fb * db)
        d_dc = -(1 + b) * th - thd
        d_th = -(2 + dlnH + b - A) * th - thd - src
        if a < a_drag:
            return np.array([d_dc, d_th, 0 * db, 0 * thb])
        return np.array([d_dc, d_th, -thb, -(2 + dlnH) * thb - 1.5 * Omm * (fc * dc + fb * db)])

    out = {}
    h = N[1] - N[0]
    for i in range(nstep - 1):
        Nv = N[i]
        k1 = rhs(Nv, Y); k2 = rhs(Nv + h/2, Y + h/2*k1); k3 = rhs(Nv + h/2, Y + h/2*k2); k4 = rhs(Nv + h, Y + h*k3)
        Yn = Y + h/6*(k1 + 2*k2 + 2*k3 + k4)
        for z, Nz in zip(zs, Ns):
            if Nv < Nz <= Nv + h and z not in out:
                t = (Nz - Nv) / h
                Yz = (1 - t) * Y + t * Yn
                out[z] = fc * Yz[0] + fb * Yz[2]
        Y = Yn
    for z in zs:
        if z not in out:
            out[z] = fc * Y[0] + fb * Y[2]
    return out


_cache = {}


def T2(k, eps, vs, reading, zlist):
    key0 = (tuple(np.round(k, 10)), tuple(zlist))
    if key0 not in _cache:
        _cache[key0] = grow(k, 0.0, vs, "K4", zlist)
    g0 = _cache[key0]
    g = grow(k, eps, vs, reading, zlist)
    return {z: (g[z] / g0[z]) ** 2 for z in zlist}


def tophat(x):
    return np.where(x < 1e-3, 1 - x**2/10, 3*(np.sin(x) - x*np.cos(x))/np.maximum(x, 1e-300)**3)


rho_m0 = C.Om * 2.775e11 * C.h**2     # Msun/Mpc^3 [T]


def sigma_M(M, kk, Pk):
    R = (M / (4*np.pi/3 * rho_m0)) ** (1/3)
    return np.sqrt(np.trapezoid(kk**3 * Pk * tophat(kk * R)**2 / (2*np.pi**2), np.log(kk)))


if __name__ == "__main__":
    # anchor: uniform-limit matter-era exponents (single fluid, EdS): K4: p^2 + (1/2 - eps/2) p = (3/2)(1+eps);
    # H: p^2 + p/2 = (3/2)(1+eps)(1+eps/2).  Numerical check: solve the code's system with Om = Omc = 1, y -> inf.
    print("Uniform-limit EdS growth exponents (analytic):")
    for e in (1, 3, 7, 10):
        bK = 0.5 - e/2; pK = (-bK + np.sqrt(bK**2 + 6*(1+e))) / 2
        pH = (-0.5 + np.sqrt(0.25 + 6*(1+e)*(1+e/2))) / 2
        pG = (-0.5 + np.sqrt(0.25 + 6*(1+e))) / 2
        print(f"  eps = {e:2d}: K4 reading p = {pK:.3f}; H reading p = {pH:.3f}; plain G(1+eps) (no velocity terms) p = {pG:.3f}")
    # kernel spot values (compare c4b printout: y=1: R = 0.72478, R_v = 0.47699, R_a = -0.87168, J_W = -0.44956)
    print(f"kernels at y = 1: R = {I('R',1.0):.5f}, Rv = {I('Rv',1.0):.5f}, Ra = {I('Ra',1.0):.5f}, J_W = {I('yJ',1.0):.5f}"
          "  (c4b: 0.72478, 0.47699, -0.87168, -0.44956)")
    # gate radius
    for vs in (5, 10, 20, 30):
        s = [vs / ((1/(1+z)) * C.H0 * C.E(1/(1+z))) for z in (1089.92, 100, 30, 10, 5, 3, 0)]
        print(f"v* = {vs:2d} km/s: comoving gate radius s_c [kpc] at z = 1090, 100, 30, 10, 5, 3, 0: "
              + ", ".join(f"{1e3*x:.1f}" for x in s))
    # (1) T2 at high-resolution Lyman-alpha scales
    zl = [5.0, 4.2, 3.0]
    ks_skm = np.array([0.009, 0.02, 0.05, 0.1, 0.2])
    print("\n(1) T2 = P_gated/P_LCDM at Lyman-alpha scales (k in s/km), linear theory")
    for reading in ("H", "K4"):
        for vs in (5, 10, 20, 30):
            for e in (1, 3, 7, 10):
                rows = []
                for z in zl:
                    kmpc = ks_skm * C.Hz(z) / (1 + z)
                    t2 = T2(kmpc, e, vs, reading, [z])[z]
                    rows.append(f"z={z}: " + " ".join(f"{v:9.3g}" for v in t2))
                print(f"  {reading:2s} v*={vs:2d} eps={e:2d} | " + " | ".join(rows))
    print(f"  (k columns: {ks_skm} s/km)")
