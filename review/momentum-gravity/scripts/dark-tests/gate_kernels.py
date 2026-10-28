"""Linear-response kernels of a velocity-gated long-range attraction in a Hubble flow.

Model (task statement): U = -Gt m^2 W(|v - v'|/v*)/|x - x'|, W(0) = 1, acting among chi only.
Reading used here (a reduction, stated): the force on a particle is -grad_x U at fixed
velocities, i.e. the gate modulates the coupling; the Lagrangian reading, which adds
d/dt(dU/dv) terms, is not treated.

In an unperturbed Hubble flow the relative velocity of two comoving particles at proper
separation r is H r (to first order in H r/c; parallel transport of comoving 4-velocities
along the constant-time slice, whose extrinsic curvature is H h_ij). Linearizing the
force about the Hubble flow gives two terms [D, this script]:

 (i) density term:  4 pi Gt rho_c R(k s) delta_c,
     R(y) = y * int_0^inf sin(y t) W(t) dt,        s = v*/(aH) the comoving gate width;
 (ii) velocity term (anti-drag): +(4 pi/3) Gt rho_c / H * R_v(k s) * u,
     R_v(y) = 3 int_0^1 mu^2 R(y mu) dmu   (identity derived for any W with W(0)=1, W(inf)=0).
     Origin: neighbours ahead of a particle moving with peculiar velocity u recede from it
     more slowly than neighbours behind, so the gate is more open ahead.

Gates: Gaussian W(u) = exp(-u^2/2) (the lab notebook's exp(-k^2/mu^2) with k = m v/2,
v* = sqrt(2) mu/m gives exactly this); rational W(u) = 1/(1 + u^2/2) (same curvature at 0).
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30


def R_gauss_exact(y):
    # y * int_0^inf sin(y t) exp(-t^2/2) dt = sqrt(2) y F(y/sqrt2), F = Dawson
    x = mp.mpf(y) / mp.sqrt(2)
    F = mp.sqrt(mp.pi) / 2 * mp.exp(-x * x) * mp.erfi(x)
    return float(mp.sqrt(2) * y * F)


def R_rational_exact(y):
    # y * int_0^inf sin(y t)/(1 + t^2/2) dt = 2y int sin(yt)/(2 + t^2) dt
    # int_0^inf sin(y t)/(a^2 + t^2) dt = [e^{-ay} Ei(ay) - e^{ay} Ei(-ay)]/(2a)
    a = mp.sqrt(2)
    y = mp.mpf(y)
    val = (mp.exp(-a * y) * mp.ei(a * y) - mp.exp(a * y) * mp.ei(-a * y)) / (2 * a)
    return float(2 * y * val)


def R_numeric(y, W, tmax=60.0, n=600001):
    # brute-force sine transform with a smooth taper (check only)
    t = np.linspace(0.0, tmax, n)
    f = np.sin(y * t) * W(t)
    return y * np.trapezoid(f, t)


# tabulate on a log grid for fast vectorized use
_y = np.logspace(-4, 4, 1601)
_Rg = np.array([R_gauss_exact(v) for v in _y])
_Rr = np.array([R_rational_exact(v) for v in _y])


def _Rv_from_R(Rtab):
    mu = np.linspace(0.0, 1.0, 2001)
    out = np.empty_like(_y)
    for i, yy in enumerate(_y):
        z = np.maximum(yy * mu, _y[0])
        Rz = np.interp(np.log(z), np.log(_y), Rtab)
        Rz = np.where(yy * mu < _y[0], (yy * mu) ** 2 * Rtab[0] / _y[0] ** 2, Rz)
        out[i] = 3.0 * np.trapezoid(mu**2 * Rz, mu)
    return out


_Rvg = _Rv_from_R(_Rg)
_Rvr = _Rv_from_R(_Rr)


def _interp(y, tab, small_coef, large_val=1.0):
    y = np.asarray(y, dtype=float)
    ly = np.log(np.clip(y, _y[0], _y[-1]))
    out = np.interp(ly, np.log(_y), tab)
    out = np.where(y < _y[0], small_coef * y**2, out)
    out = np.where(y > _y[-1], large_val, out)
    return out


def R(y, gate="gauss"):
    tab = _Rg if gate == "gauss" else _Rr
    return _interp(y, tab, tab[0] / _y[0] ** 2)


def Rv(y, gate="gauss"):
    tab = _Rvg if gate == "gauss" else _Rvr
    return _interp(y, tab, tab[0] / _y[0] ** 2)


def antidrag_bruteforce(u, W, H=1.0, vstar=1.0, rmax=100.0, nr=40001, nmu=1601):
    """z-force per (Gt rho) on a particle with peculiar velocity u zhat in a uniform medium
    in Hubble flow v' = H r: F_z = 2 pi int dr int dmu mu W(|H r rhat - u zhat|/v*).
    (d^3r/r^2 * rhat_z = dr dOmega mu.)  Analytic linear result: (4 pi/3) u/H [W(0) - W(inf)].
    Quadratic r-grid (fine near r ~ u/H), evaluated in chunks to bound memory."""
    s = np.linspace(0.0, 1.0, nr)
    r = rmax * s**2
    mu = np.linspace(-1.0, 1.0, nmu)
    inner = np.empty_like(r)
    for i0 in range(0, nr, 2000):
        rr = r[i0:i0 + 2000][:, None]
        rel = np.sqrt(np.maximum((H * rr) ** 2 - 2 * H * rr * u * mu[None, :] + u**2, 0.0)) / vstar
        inner[i0:i0 + 2000] = np.trapezoid(mu[None, :] * W(rel), mu, axis=1)
    return 2 * np.pi * np.trapezoid(inner, r)


if __name__ == "__main__":
    Wg = lambda t: np.exp(-t**2 / 2)
    Wr = lambda t: 1.0 / (1.0 + t**2 / 2)
    print("Check 1: density kernel R(y), closed form vs brute-force sine transform")
    for yy in [0.1, 0.5, 1.0, 2.0, 5.0]:
        print("  y=%4.1f  gauss: exact %.6f  numeric %.6f | rational: exact %.6f  numeric %.6f"
              % (yy, R_gauss_exact(yy), R_numeric(yy, Wg), R_rational_exact(yy),
                 R_numeric(yy, Wr, tmax=4000.0, n=4000001)))
    print("  limits: R(1e-3)/y^2 gauss = %.4f (expect 1)  R(1e3) gauss = %.6f (expect ~1)"
          % (R(1e-3) / 1e-6, R(1e3)))
    print("Check 2: anti-drag, brute-force force on a moving particle vs (4pi/3) u/H")
    for u in [0.003, 0.01, 0.03]:
        Fg = antidrag_bruteforce(u, Wg, rmax=20.0)
        Fr = antidrag_bruteforce(u, Wr, rmax=400.0, nr=80001)
        print("  u/v*=%.3f  gauss: F=%.6e  analytic=%.6e  ratio=%.5f | rational: F=%.6e ratio=%.5f"
              % (u, Fg, 4 * np.pi / 3 * u, Fg / (4 * np.pi / 3 * u), Fr, Fr / (4 * np.pi / 3 * u)))
    print("Check 3: R_v limits: R_v(1e-3)/y^2 = %.4f (expect 3/5)   R_v(1e3) = %.5f (expect ~1)"
          % (Rv(1e-3) / 1e-6, Rv(1e3)))
    print("Table: y = k s  |  R_gauss  Rv_gauss  |  R_rational  Rv_rational")
    for yy in [0.1, 0.3, 1.0, 3.0, 10.0, 30.0]:
        print("  %6.2f  |  %.4f  %.4f  |  %.4f  %.4f" % (yy, R(yy), Rv(yy), R(yy, 'rat'), Rv(yy, 'rat')))
