# Part 2 and 3: integrate the hilltop field V = V0[1 + cos(tau/f)] for a scan of (f, tau_i) that
# thaw from w = -1, fit CPL (w0, wa) over 0 < z < 2.5 by several conventions, and place the fits
# relative to the crossing boundary w0 + wa = -1 and to the corridor wa = -1.5(1 + w0).
# Part 3: check that the true w(a) never goes below -1 (and that rho_tau never grows).
import math
import sys
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import cosmo as C


def w_fits(r, zmax):
    """direct fits of the CPL line to the true w(a)"""
    out = {}
    aa = np.linspace(1 / (1 + zmax), 1, 4001)
    out["F1 w(a) LSQ, uniform in a"] = C.wls_line(1 - aa, np.interp(np.log(aa), r["N"], r["w"]), np.ones_like(aa))
    zz = np.linspace(0, zmax, 4001)
    out["F2 w(a) LSQ, uniform in z"] = C.wls_line(1 - 1 / (1 + zz), np.interp(-np.log1p(zz), r["N"], r["w"]),
                                                  np.ones_like(zz))
    return out


def tangent(r):
    """Taylor CPL at a = 1: w0 = w(1), wa = -dw/da(1) = -dw/dN(0)"""
    h = r["N"][-1] - r["N"][-2]
    dwdN = (3 * r["w"][-1] - 4 * r["w"][-2] + r["w"][-3]) / (2 * h)
    return np.array([r["w"][-1], -dwdN])


def distance_fits(r, zmax, nz=50, want_resid=False):
    """fits of CPL to the true expansion history through H(z) and D_M(z) on a uniform z grid in (0, zmax]
    F3: Omega_m, H0 fixed at truth;  F4: Omega_m free, H0 fixed;
    F5: physical matter density fixed, h free, D_M(z* = 1090) matched exactly (CMB-like anchor)"""
    N, H = r["N"], r["H"]
    a = np.exp(N)
    om, orr = r["om"], r["orr"]
    zg = np.linspace(zmax / nz, zmax, nz)
    Ng = -np.log1p(zg)
    Nst = -math.log1p(C.ZSTAR)
    chi_t = C.comoving_distance(N, H)
    D_t, H_t = np.interp(Ng, N, chi_t), np.interp(Ng, N, H)
    Dst_t = np.interp(Nst, N, chi_t)

    def resid(Hc):
        chi = C.comoving_distance(N, Hc)
        return np.concatenate([np.interp(Ng, N, Hc) / H_t - 1, np.interp(Ng, N, chi) / D_t - 1])

    def H3(p):
        return np.sqrt(om * a**-3 + orr * a**-4 + (1 - om - orr) * C.cpl_X(a, p[0], p[1]))

    def H4(p):
        return np.sqrt(p[2] * a**-3 + orr * a**-4 + (1 - p[2] - orr) * C.cpl_X(a, p[0], p[1]))

    def eta_for(w0, wa):
        X = C.cpl_X(a, w0, wa)
        g = lambda eta: Dst_t - np.interp(Nst, N, C.comoving_distance(
            N, np.sqrt(om * a**-3 + orr * a**-4 + (eta**2 - om - orr) * X)))   # increasing in eta
        lo, hi = 0.75, 1.35
        return C.illinois(g, lo, hi, g(lo), g(hi), tol=1e-14)

    def H5(p):
        eta = eta_for(p[0], p[1])
        return np.sqrt(om * a**-3 + orr * a**-4 + (eta**2 - om - orr) * C.cpl_X(a, p[0], p[1]))

    out, res = {}, {}
    starts = [np.array([-0.9, -0.3]), np.array([-1.0, 0.0]), np.array([-0.7, -1.0])]
    for key, Hf, extra in [("F3 H(z), D_M(z); Om, H0 fixed", H3, None),
                           ("F4 H(z), D_M(z); Om free", H4, om),
                           ("F5 H(z), D_M(z) + D_M(z*); om h^2 fixed", H5, None)]:
        best = None
        for p0 in starts:
            p0 = p0 if extra is None else np.append(p0, extra)
            p, cost = C.lm(lambda p: resid(Hf(p)), p0)
            if best is None or cost < best[1]:
                best = (p, cost)
        p = best[0]
        if key.startswith("F5"):
            p = np.append(p, eta_for(p[0], p[1]))
        out[key] = p
        res[key] = np.max(np.abs(resid(Hf(best[0]))))
    return (out, res) if want_resid else out


def describe(w0, wa):
    s = -wa / (1 + w0) if w0 > -1 else float("nan")
    zc = 1 / (s - 1) if s > 1 else float("inf")
    return s, w0 + wa + 1, zc


if __name__ == "__main__":
    ZMAX = 2.5
    fs = [0.3, 0.5, 1.0, 2.0]
    xs = np.geomspace(1e-4, 2.8, 36)          # tau_i / f
    rows = []
    print("Model: flat; Omega_m = %.2f, Omega_r = %.0e; V = V0[1 + cos(tau/f)], V0 shot to Omega_DE = %.5f;"
          % (C.OM, C.OR, 1 - C.OM - C.OR))
    print("tau frozen (dtau/dt = 0) at a = %.0e; units 8 pi G = 1, H0 = 1. CPL fit range 0 < z < %.1f."
          % (C.A_I, ZMAX))
    print("s = -wa/(1 + w0): the fit is in the crossing region (w0 + wa < -1) iff s > 1; corridor s = 1.5;"
          " z_c = 1/(s - 1) is where the CPL line crosses -1.\n")
    for f in fs:
        for x in xs:
            ti = x * f
            try:
                r = C.solve(f, ti)
            except RuntimeError:
                continue
            w0t = r["w"][-1]
            if not (-0.985 <= w0t <= -0.5):
                continue
            # Part 3 diagnostics on the full history a = 1e-4 .. 1
            one_w_min = np.min(1 + r["w"])
            drho_max = np.max(np.diff(r["rho"]))                      # must be <= 0 (no growth)
            dlnrho = np.gradient(np.log(r["rho"]), r["N"])
            weff_min = np.min(-1 - dlnrho / 3)
            Om_de_z2 = np.interp(-math.log(3.0), r["N"], r["rho"] / (3 * r["H"]**2))
            fits = {"T  tangent at a = 1": tangent(r)}
            fits.update(w_fits(r, ZMAX))
            dfit, dres = distance_fits(r, ZMAX, want_resid=True)
            fits.update(dfit)
            rows.append(dict(f=f, x=x, r=r, w0t=w0t, one_w_min=one_w_min, drho_max=drho_max,
                             weff_min=weff_min, Om_de_z2=Om_de_z2, fits=fits, dres=dres,
                             w_z25=np.interp(-math.log(3.5), r["N"], r["w"]),
                             tau0_f=r["tau"][-1] / f, Vmin=np.min(r["V"])))

    keys = list(rows[0]["fits"].keys())
    print("== Per case: true history, then each CPL fit as (w0, wa | s, w0+wa+1) ==")
    for R in rows:
        print(f"\nf = {R['f']:.1f}, tau_i/f = {R['x']:.3e}, V0 = {R['r']['V0']:.5f}: true w(1) = {R['w0t']:+.4f},"
              f" true w(z=2.5) = {R['w_z25']:+.5f}, tau0/f = {R['tau0_f']:.3f}, Omega_DE(z=2) = {R['Om_de_z2']:.3f}")
        print(f"   part 3: min(1+w) = {R['one_w_min']:.3e}, max step change of rho_tau = {R['drho_max']:.2e},"
              f" min w_eff from d ln rho/dN = {R['weff_min']:+.6f}, min V = {R['Vmin']:.3e}")
        for k in keys:
            p = R["fits"][k]
            s, g, zc = describe(p[0], p[1])
            extra = ""
            if k.startswith("F4"):
                extra = f"  Om_fit = {p[2]:.4f}"
            if k.startswith("F5"):
                extra = f"  h_fit/h = {p[2]:.5f}"
            if k in R["dres"]:
                extra += f"  max|resid| = {R['dres'][k]:.1e}"
            print(f"   {k:<44s} w0 = {p[0]:+.4f}  wa = {p[1]:+.4f} | s = {s:5.3f}  w0+wa+1 = {g:+.4f}"
                  f"  z_c = {zc:5.2f}{extra}")

    print("\n== Summary over all %d thawing cases (true w(1) in [-0.985, -0.5]) ==" % len(rows))
    for k in keys:
        ss = np.array([describe(R["fits"][k][0], R["fits"][k][1])[0] for R in rows])
        gg = np.array([describe(R["fits"][k][0], R["fits"][k][1])[1] for R in rows])
        w0f = np.array([R["fits"][k][0] for R in rows])
        print(f"{k:<44s} fitted w0 > -1 in {np.sum(w0f > -1)}/{len(rows)};"
              f" w0+wa < -1 in {np.sum(gg < 0)}/{len(rows)}; s in [{np.nanmin(ss):.3f}, {np.nanmax(ss):.3f}],"
              f" median {np.nanmedian(ss):.3f}")
    print(f"part 3: min over all cases of min(1+w) = {min(R['one_w_min'] for R in rows):.3e};"
          f" max step change of rho_tau = {max(R['drho_max'] for R in rows):.2e};"
          f" min w_eff = {min(R['weff_min'] for R in rows):+.6f}; min V = {min(R['Vmin'] for R in rows):.3e}")

    print("\n== Fit-range sensitivity (F1 and F3), s = -wa/(1+w0) by z_max ==")
    for zmax in [1.0, 1.5, 2.5, 4.0]:
        s1, s3 = [], []
        for R in rows:
            p1 = w_fits(R["r"], zmax)["F1 w(a) LSQ, uniform in a"]
            p3 = distance_fits(R["r"], zmax)["F3 H(z), D_M(z); Om, H0 fixed"]
            s1.append(describe(p1[0], p1[1])[0]); s3.append(describe(p3[0], p3[1])[0])
        s1, s3 = np.array(s1), np.array(s3)
        print(f"z_max = {zmax:3.1f}: F1 s in [{s1.min():.3f}, {s1.max():.3f}] (all > 1: {bool(np.all(s1 > 1))});"
              f"  F3 s in [{s3.min():.3f}, {s3.max():.3f}] (all > 1: {bool(np.all(s3 > 1))})")
