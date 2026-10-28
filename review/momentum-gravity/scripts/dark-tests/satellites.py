"""Gate factors for galaxies and clusters, and the translation of published fifth-force limits.

<W> = E[ W(|V + w|/v*) ], w ~ isotropic Gaussian with 1D dispersion s: the mean gate between a
body moving at V through a Maxwellian population (or between two Maxwellian populations).
Gaussian gate: closed form (v*^2/(v*^2+s^2))^{3/2} exp(-V^2/(2(v*^2+s^2))); rational gate: numerical.
The extra acceleration of a satellite's DM toward the host's DM is eps*<W>*g_host,DM (host velocity
distribution taken position-independent: an estimate); its stars feel gravity only.  Published limits
on an ungated DM-only force (strength beta x gravity) are mapped as beta -> eps*<W>, a mapping that
ignores that the satellite's internal DM self-binding is enhanced by ~eps rather than eps*<W>.

Inputs [S]:
 Sgr: r = 18.11 kpc, V_r = 143.6, V_T = 276.0 km/s (del Pino et al. 2021, arXiv:2011.02627).
 Fornax: Galactocentric (X,Y,Z) = (-41.2,-50.9,-134) kpc, (vX,vY,vZ) = (40.4,-125,82.8) km/s;
   MW model: Dehnen gamma=1 (Hernquist) DM 1.2e12 Msun, a = 20 kpc; disk 1e11, bulge 3.4e10 Msun
   (Zamlung & Nusser 2025, arXiv:2509.01713). Disk+bulge treated here as a central point mass
   (reduction, adequate at r >= 18 kpc).
 Eilers et al. 2019 (arXiv:1810.09466): v_c(R0) = 229.0 km/s, slope -1.7 km/s/kpc (5-25 kpc),
   used only as an independent check of the host model at Sgr's radius (R0 = 8.122 kpc, dagger).
 Bullet Cluster: mass-centroid speed 2600 km/s (Springel & Farrar 2007, astro-ph/0703232);
   main-cluster galaxy dispersion ~1250 km/s (Barrena et al. 2002 via search summary),
   1163 km/s whole-cluster (DS+, arXiv:2212.00040); subcluster ~210 km/s (Barrena) or 472 km/s
   bias-corrected (DS+).
 Satellite internal dispersions ~12 km/s (dagger; changes <W> by <1%).
Limits [S]: Sgr streams: 'a dark-matter force greater than 10% the strength of gravity is
 already excluded' (Kesden & Kamionkowski 2006, astro-ph/0608095; Kesden 2009, arXiv:0903.4458;
 KK's beta^2 is the force ratio).  Fornax: beta >~ 0.4 excluded, beta <~ 0.2 mildly stripped
 (Zamlung & Nusser 2025; force (1+beta) G).  Bullet: a force 0.4-1.2 x gravity was proposed to
 explain the speed (Farrar & Rosen 2007, astro-ph/0610298), not needed per Springel & Farrar 2007.
"""
import numpy as np

Gk = 4.30091e-6  # kpc (km/s)^2 / Msun  [T]
M_DM, a_DM, M_c = 1.2e12, 20.0, 1e11 + 3.4e10


def Mtot(r):
    return M_DM * r**2 / (r + a_DM) ** 2 + M_c


def Phi(r):
    return -Gk * M_DM / (r + a_DM) - Gk * M_c / r


def rho_DM(r):
    return M_DM * a_DM / (2 * np.pi * r * (r + a_DM) ** 3)


def sigma_iso(r, rmax=1e5, n=200000):
    rr = np.geomspace(r, rmax, n)
    integ = rho_DM(rr) * Gk * Mtot(rr) / rr**2
    return np.sqrt(np.trapezoid(integ, rr) / rho_DM(r))


def turning_points(r0, vr, vt):
    E = 0.5 * (vr**2 + vt**2) + Phi(r0)
    L = r0 * vt
    f = lambda r: E - Phi(r) - L**2 / (2 * r**2)
    rr = np.geomspace(0.5, 2000, 200000)
    s = np.sign(f(rr))
    idx = np.where(np.diff(s) != 0)[0]
    roots = []
    for i in idx:
        lo, hi = rr[i], rr[i + 1]
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if np.sign(f(mid)) == np.sign(f(lo)):
                lo = mid
            else:
                hi = mid
        roots.append(0.5 * (lo + hi))
    rp, ra = roots[0], roots[-1]
    Vp, Va = L / rp, L / ra
    return rp, ra, Vp, Va


def W_gauss_avg(V, s, vstar):
    q = vstar**2 + s**2
    return (vstar**2 / q) ** 1.5 * np.exp(-V**2 / (2 * q))


def W_rat_avg(V, s, vstar):
    x = np.linspace(1e-6, V + 12 * s + 12 * vstar, 200001)
    if V > 1e-9:
        p = x / (V * s * np.sqrt(2 * np.pi)) * (np.exp(-(x - V) ** 2 / (2 * s**2)) - np.exp(-(x + V) ** 2 / (2 * s**2)))
    else:
        p = np.sqrt(2 / np.pi) * x**2 / s**3 * np.exp(-x**2 / (2 * s**2))
    W = 1.0 / (1.0 + (x / vstar) ** 2 / 2)
    return np.trapezoid(W * p, x)


if __name__ == "__main__":
    # host-model check against Eilers et al. at Sgr's radius
    r_sgr = 18.11
    vc_model = np.sqrt(Gk * Mtot(r_sgr) / r_sgr)
    vc_eilers = 229.0 - 1.7 * (r_sgr - 8.122)
    print("Host model check: v_c(18.11 kpc) model = %.1f km/s ; Eilers linear fit = %.1f km/s" % (vc_model, vc_eilers))
    sat_int = 12.0
    # Sgr
    vr, vt = 143.6, 276.0
    V_sgr = np.hypot(vr, vt)
    rp, ra, Vp, Va = turning_points(r_sgr, vr, vt)
    print("Sgr: |V| = %.1f km/s at r = %.2f kpc; model orbit: peri %.1f kpc (V=%.1f), apo %.1f kpc (V=%.1f)" % (V_sgr, r_sgr, rp, Vp, ra, Va))
    # Fornax
    X = np.array([-41.2, -50.9, -134.0]); Vv = np.array([40.4, -125.0, 82.8])
    r_for = np.linalg.norm(X); V_for = np.linalg.norm(Vv)
    vr_f = X @ Vv / r_for; vt_f = np.sqrt(V_for**2 - vr_f**2)
    rpf, raf, Vpf, Vaf = turning_points(r_for, vr_f, vt_f)
    print("Fornax: |V| = %.1f km/s at r = %.1f kpc (v_r = %.1f); model orbit: peri %.1f kpc (V=%.1f), apo %.1f kpc (V=%.1f)"
          % (V_for, r_for, vr_f, rpf, Vpf, raf, Vaf))
    cases = [
        ("Sgr now (~pericentre)", V_sgr, r_sgr),
        ("Sgr apocentre", Va, ra),
        ("Fornax now", V_for, r_for),
        ("Fornax pericentre", Vpf, rpf),
    ]
    vlist = [10, 20, 30, 50, 80, 120, 200, 300, 500, 1000, 2000, 3000]
    for lab, V, r in cases:
        sh = sigma_iso(r)
        s = np.hypot(sh, sat_int)
        print("%s: V=%.1f km/s, host DM sigma_1D (isotropic Jeans, model) = %.1f km/s, combined s = %.1f" % (lab, V, sh, s))
        print("   v*:     " + " ".join("%7d" % v for v in vlist))
        print("   <W>gs:  " + " ".join("%7.4f" % W_gauss_avg(V, s, v) for v in vlist))
        print("   <W>rat: " + " ".join("%7.4f" % W_rat_avg(V, s, v) for v in vlist))
    # Sgr with a host consistent with Eilers et al.: singular isothermal sphere, v_c = 212 km/s at 18 kpc,
    # sigma_1D = v_c/sqrt2 [T]; orbit in the logarithmic potential (a reduction: the real curve declines).
    vc = vc_eilers
    E = 0.5 * V_sgr**2 + vc**2 * np.log(r_sgr); L = r_sgr * vt
    f = lambda r: E - vc**2 * np.log(r) - L**2 / (2 * r**2)
    rr = np.geomspace(1, 500, 400000); fv = f(rr); idx = np.where(np.diff(np.sign(fv)) != 0)[0]
    rpi, rai = rr[idx[0]], rr[idx[-1]]
    print("Sgr in an isothermal host (v_c = %.1f km/s, sigma_1D = %.1f): peri %.1f kpc (V=%.1f), apo %.1f kpc (V=%.1f)"
          % (vc, vc / np.sqrt(2), rpi, L / rpi, rai, L / rai))
    s_iso = np.hypot(vc / np.sqrt(2), sat_int)
    print("   <W>gs  now:  " + " ".join("%7.4f" % W_gauss_avg(V_sgr, s_iso, v) for v in vlist))
    print("   <W>rat now:  " + " ".join("%7.4f" % W_rat_avg(V_sgr, s_iso, v) for v in vlist))
    print("   <W>gs  apo:  " + " ".join("%7.4f" % W_gauss_avg(L / rai, s_iso, v) for v in vlist))
    print()
    print("Translated limits (eps_max = beta_limit/<W>), Gaussian gate:")
    s_sgr = s_iso   # Eilers-consistent isothermal host (primary); Hernquist-model values printed above
    s_fp = np.hypot(sigma_iso(rpf), sat_int)
    s_fn = np.hypot(sigma_iso(r_for), sat_int)
    print("   v*   | Sgr (0.10, peri) | Fornax (0.4, peri) | Fornax (0.4, now) | rational: Sgr  Fornax-peri")
    for v in vlist:
        ws, wfp, wfn = W_gauss_avg(V_sgr, s_sgr, v), W_gauss_avg(Vpf, s_fp, v), W_gauss_avg(V_for, s_fn, v)
        wsr, wfpr = W_rat_avg(V_sgr, s_sgr, v), W_rat_avg(Vpf, s_fp, v)
        print("  %5d |   %10.4g     |   %10.4g      |   %10.4g     |   %8.4g  %8.4g"
              % (v, 0.1 / ws, 0.4 / wfp, 0.4 / wfn, 0.1 / wsr, 0.4 / wfpr))
    print()
    print("Bullet Cluster: gate factor between subcluster DM and main-cluster DM (V = 2600 km/s)")
    for sm, ss, lab in [(1250, 210, "Barrena"), (1163, 472, "DS+ 2022")]:
        s = np.hypot(sm, ss)
        print("  dispersions %s (%d, %d): s = %.0f" % (lab, sm, ss, s))
        for v in [120, 300, 1000, 3000]:
            print("    v*=%5d: <W> inter-cluster gauss %.3e  rational %.3e | within main (pairs, s=sqrt2*%d) gauss %.3e rational %.3e"
                  % (v, W_gauss_avg(2600, s, v), W_rat_avg(2600, s, v), sm,
                     W_gauss_avg(0, np.sqrt(2) * sm, v), W_rat_avg(0, np.sqrt(2) * sm, v)))
        for beta_need in [0.4, 1.2]:
            print("    Farrar-Rosen force %.1f x gravity would need eps = %.3g at v*=120 (gauss) " % (beta_need, beta_need / W_gauss_avg(2600, s, 120)))
    print()
    print("Internal gate factor for DM pairs in a system of 1D dispersion sigma (pair dispersion sqrt2*sigma), v*=120 and 30:")
    for sig, lab in [(3.7, "Segue-1-like (dagger)"), (10, "classical dSph (dagger)"), (30, "Debt-3a dwarf core"),
                     (155, "Debt-3a MW halo"), (1000, "cluster")]:
        print("  sigma=%6.1f %-24s  v*=120: gauss %.4f rational %.4f | v*=30: gauss %.4f rational %.4f"
              % (sig, lab, W_gauss_avg(0, np.sqrt(2) * sig, 120), W_rat_avg(0, np.sqrt(2) * sig, 120),
                 W_gauss_avg(0, np.sqrt(2) * sig, 30), W_rat_avg(0, np.sqrt(2) * sig, 30)))
