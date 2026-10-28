"""Linear growth of structure with a velocity-gated chi-only attraction (Hubble-flow gate).

Two fluids, sub-horizon, radiation smooth (Meszaros approximation) [T]:
  dc'' + (2 + dlnH/dN - (eps/2) f_c Om_cl(a) A Rv(k s')) dc'
        = 1.5 Om_cl(a) [f_b db + f_c (1 + eps A R(k s')) dc]
  db'' + (2 + dlnH/dN) db' = 1.5 Om_cl(a) [f_b db + f_c dc]        (a > a_drag; db = 0 before)
N = ln a; s' = comoving gate width; R, Rv from gate_kernels.py (derived and brute-force checked there).
Hubble-only gate: A = 1, s' = v*/(aH).  With linear pairwise smoothing ('pec'): the Gaussian gate
averaged over an isotropic Gaussian pair-velocity spread s1 (1D) gives A = (v*^2/(v*^2+s1^2))^{3/2}
and s' = sqrt(v*^2 + s1^2)/(aH), with s1 = linear LCDM pair-velocity rms at r = v*/(aH) (an estimate:
formally second order in perturbations; it weakens the force, so it brackets the Hubble-only case).
Ungated comparison model (range > horizon): R = 1, Rv = 0, A = 1.
Reductions: baryon pressure after decoupling neglected; baryons do not cluster before z_drag;
massive neutrino treated as smooth; linear theory only.
"""
import numpy as np
import cosmo as C
import gate_kernels as GK

Ocl = C.Oc + C.Ob
a_drag = 1.0 / (1.0 + C.z_drag)


def Om_cl(a):
    return Ocl / a**3 / C.E(a) ** 2


def aH(a):
    return C.H0 * C.E(a) * a  # km/s/Mpc


_k_s1 = np.logspace(-4, 2.5, 3000)


def s1_pair(r_c, z):
    a = 1 / (1 + z)
    f = C.growth_rate_f(a)
    P = C.P_lin(_k_s1, z)
    x = _k_s1 * r_c
    j0 = np.where(x < 1e-4, 1 - x**2 / 6, np.sin(x) / np.maximum(x, 1e-300))
    du2 = (aH(a) * f) ** 2 / np.pi**2 * np.trapezoid(P * (1 - j0) * _k_s1, np.log(_k_s1))
    return np.sqrt(du2 / 3.0)


def make_s1_table(vstar):
    zz = np.concatenate([np.linspace(0, 10, 41), np.logspace(np.log10(11), np.log10(2e4), 40)])
    s1 = np.array([s1_pair(vstar / aH(1 / (1 + z)), z) for z in zz])
    return np.log(1 / (1 + zz))[::-1], s1[::-1]


def run(kvec, eps, vstar, gate="gauss", antidrag=True, pec=None, ungated=False,
        z_out=(0.0,), a_i=1e-5, dc_p0=0.3, nstep=3000):
    """Return dict z -> (dc, db, dm) arrays over kvec."""
    k = np.atleast_1d(np.asarray(kvec, dtype=float))
    eps = np.broadcast_to(np.asarray(eps, dtype=float), k.shape).copy()
    N = np.linspace(np.log(a_i), 0.0, nstep)
    zout = sorted(z_out, reverse=True)
    Nout = [np.log(1 / (1 + z)) for z in zout]
    nk = k.size
    y = np.zeros((4, nk))
    y[0] = 1.0; y[1] = dc_p0

    def coeffs(Nv):
        a = np.exp(Nv)
        om = Om_cl(a)
        fr = 2 + C.dlnH_dlna(a)
        if ungated:
            return om, fr, np.ones(nk), np.zeros(nk), 1.0
        if pec is not None:
            s1 = np.interp(Nv, pec[0], pec[1])
            A = (vstar**2 / (vstar**2 + s1**2)) ** 1.5
            sp = np.sqrt(vstar**2 + s1**2) / aH(a)
        else:
            A = 1.0
            sp = vstar / aH(a)
        yy = k * sp
        Rk = GK.R(yy, gate)
        Rvk = GK.Rv(yy, gate) if antidrag else np.zeros(nk)
        return om, fr, Rk, Rvk, A

    def rhs(Nv, y):
        om, fr, Rk, Rvk, A = coeffs(Nv)
        dc, dcp, db, dbp = y
        dcpp = -(fr - 0.5 * eps * C.f_c * om * A * Rvk) * dcp + 1.5 * om * (C.f_b * db + C.f_c * (1 + eps * A * Rk) * dc)
        if np.exp(Nv) > a_drag:
            dbpp = -fr * dbp + 1.5 * om * (C.f_b * db + C.f_c * dc)
        else:
            dbpp = np.zeros(nk); dbp = np.zeros(nk)
        return np.array([dcp, dcpp, dbp, dbpp])

    out = {}
    j = 0
    for i in range(nstep - 1):
        Nv, dN = N[i], N[i + 1] - N[i]
        # land exactly on output times
        while j < len(Nout) and Nout[j] <= Nv + 1e-12:
            j += 1
        k1 = rhs(Nv, y); k2 = rhs(Nv + dN / 2, y + dN / 2 * k1)
        k3 = rhs(Nv + dN / 2, y + dN / 2 * k2); k4 = rhs(Nv + dN, y + dN * k3)
        ynew = y + dN / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        for jj, (zo, No) in enumerate(zip(zout, Nout)):
            if Nv < No <= Nv + dN and zo not in out:
                w = (No - Nv) / dN
                yo = (1 - w) * y + w * ynew
                out[zo] = (yo[0].copy(), yo[2].copy(), C.f_c * yo[0] + C.f_b * yo[2])
        y = ynew
    for zo in zout:
        if zo not in out:
            out[zo] = (y[0].copy(), y[2].copy(), C.f_c * y[0] + C.f_b * y[2])
    return out


def ratio(kvec, eps, vstar, z, **kw):
    """T_m, T_c, T_b = growth with force / growth without, at redshift z."""
    g = run(kvec, eps, vstar, z_out=(z,), **kw)[z]
    s = run(kvec, 0.0, vstar, z_out=(z,), **{kk: v for kk, v in kw.items() if kk in ('a_i', 'dc_p0', 'nstep')})[z]
    return g[2] / s[2], g[0] / s[0], g[1] / s[1]


if __name__ == "__main__":
    # sanity: matter-dominated small-scale growth exponent with/without anti-drag (single fluid, f_c->1)
    for ad, lab in [(False, "no anti-drag"), (True, "with anti-drag")]:
        for e in [0.01, 0.1, 1.0]:
            # p^2 + (1/2 - ad*e/2) p - 1.5(1+e) = 0
            b = 0.5 - (e / 2 if ad else 0.0)
            p = (-b + np.sqrt(b * b + 6 * (1 + e))) / 2
            print("EdS single-fluid growth exponent, %s, eps=%.2f: p = %.4f  (p-1)/eps = %.3f" % (lab, e, p, (p - 1) / e))
    # IC insensitivity
    kp = 0.009 * C.Hz(3.0) / 4.0
    for c0 in [0.1, 0.3, 1.0]:
        Tm, Tc, Tb = ratio([kp, 3.0, 10.0], 0.3, 120.0, 3.0, dc_p0=c0)
        print("IC test dc'(a_i)=%.1f: T_m(k_p,z=3)=%.6f  T_m(3/Mpc)=%.6f  T_m(10/Mpc)=%.6f" % (c0, Tm[0], Tm[1], Tm[2]))
    for ns_ in [1500, 3000, 6000]:
        Tm, Tc, Tb = ratio([kp, 10.0], 0.3, 120.0, 3.0, nstep=ns_)
        print("step test nstep=%d: T_m(k_p)=%.7f T_m(10)=%.7f" % (ns_, Tm[0], Tm[1]))
    # ungated limit check: deep-MD scale-independent enhancement vs analytic two-fluid estimate
    Tm, Tc, Tb = ratio([1.0, 10.0], 0.01, 120.0, 0.0, ungated=True)
    print("ungated eps=0.01: T_m(z=0) at k=1,10 /Mpc = %.5f %.5f ; T_c = %.5f, T_b = %.5f" % (Tm[0], Tm[1], Tc[0], Tb[0]))
