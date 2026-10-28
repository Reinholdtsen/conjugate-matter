"""Extra checks:
(1) v* at which the DESI compressed bound reaches eps = 1, for kernel B+AD (agent), A+AD (reading A),
    and reading C, matter and gas ratios (Gaussian gate).
(2) Shape of the gated transfer across the DESI P1D range (k = 0.001-0.03 s/km) at the bound, against the
    two-parameter (amplitude, slope) description at the pivot: how much curvature (running) the model has.
(3) Fornax gate factors in the Zamlung & Nusser host (Table 1 [S]): Hernquist halo 1.2e12 Msun a = 20 kpc,
    Miyamoto-Nagai disk 1e11 (6.5, 0.3), Hernquist bulge 3.4e10 (0.7), treated as spherical (disk mass
    enclosed approximated by its spherical-equivalent) ; isotropic Jeans dispersion of the halo tracer.
"""
import numpy as np
import vgrowth as G
import vlya as L
import vreadingC as RC

def bound_at(vs, variant, ratio):
    if variant == "C":
        Tm2, Tb2 = RC.transfer_C(L.ks, L.eps_grid, vs)
    else:
        Tm2, Tb2 = G.transfer(L.ks, L.eps_grid, vs, dens=variant, antidrag=True)
    one = np.ones((1, 3))
    T = np.vstack([one, Tm2 if ratio == "m" else Tb2])
    return L.bound(L.chi2_curve(T, L.DESI), L.eps_grid)

if __name__ == "__main__":
    vgrid = [10, 15, 20, 25, 30, 40, 50, 60]
    print("(1) eps_max(v*) near eps = 1:")
    for variant in ["B", "A", "C"]:
        for ratio in ["m", "g"]:
            vals = [bound_at(float(v), variant, ratio) for v in vgrid]
            lv = np.log(vgrid); le = np.log(vals)
            # eps_max decreasing in v*: find crossing of 1
            cross = np.nan
            for i in range(len(vgrid)-1):
                if vals[i] >= 1 > vals[i+1]:
                    t = (0-le[i])/(le[i+1]-le[i]); cross = np.exp(lv[i]+t*(lv[i+1]-lv[i]))
            print("  variant %s ratio %s: " % (variant, ratio)+" ".join("%d:%.3f" % (v, e) for v, e in zip(vgrid, vals))+"  -> eps=1 at v* = %.1f km/s" % cross)
    print("(2) transfer shape across the P1D range at the bound (v*=120, kernel B+AD, eps=0.0285; and A+AD eps=0.0584):")
    kp = L.kp; conv = kp/0.009
    kv = np.array([0.001, 0.003, 0.009, 0.02, 0.03])     # s/km
    for dens, eps in [("B", 0.0285), ("A", 0.0584)]:
        Tm2, _ = G.transfer(kv*conv, [eps], 120.0, dens=dens)
        T2 = Tm2[0]
        lT = np.log(T2); lk = np.log(kv)
        i0 = 2
        # two-parameter description from the pivot: ln T2(k) ~ lnT2(kp) + dn ln(k/kp), dn from +-2%
        Tl, _ = G.transfer(L.ks, [eps], 120.0, dens=dens)
        dn = (np.log(Tl[0, 2])-np.log(Tl[0, 0]))/(2*L.dl)
        pred = np.exp(lT[i0]+dn*(lk-lk[i0]))
        print("  dens=%s eps=%.4f: k[s/km] " % (dens, eps)+" ".join("%.3f" % k for k in kv))
        print("     T^2 model        "+" ".join("%.4f" % t for t in T2))
        print("     T^2 (amp+slope)  "+" ".join("%.4f" % t for t in pred))
        # local running at the pivot
        kr = kp*np.exp(np.array([-0.2, 0, 0.2]))
        Tr, _ = G.transfer(kr, [eps], 120.0, dens=dens)
        lr = np.log(Tr[0])
        print("     running d^2 lnT^2/dlnk^2 at k_p = %.4f ; slope dn = %.4f" % ((lr[2]-2*lr[1]+lr[0])/0.04, dn))
    # (3) Fornax host
    Gk = 4.300917e-6     # kpc (km/s)^2 / Msun  (dagger)
    Mh, ah = 1.2e12, 20.0; Md, ad, bd = 1e11, 6.5, 0.3; Mb, ab = 3.4e10, 0.7
    def Menc(r):
        mh = Mh*r*r/(r+ah)**2; mb = Mb*r*r/(r+ab)**2
        # disk: midplane circular-speed-equivalent mass
        md = Md*r**3/(r*r+(ad+bd)**2)**1.5
        return mh+mb+md
    def rho_h(r): return Mh*ah/(2*np.pi*r*(r+ah)**3)
    def sig2(r):
        rr = np.logspace(np.log10(r), np.log10(r*1e4), 20001)
        f = rho_h(rr)*Gk*Menc(rr)/rr**2
        return np.trapezoid(f, rr)/rho_h(r)
    for (lab, r, V) in [("now (149 kpc, 155.3 km/s)", 149.0, 155.3), ("pericentre (87.9 kpc, 253 km/s)", 87.9, 253.0)]:
        s = np.sqrt(sig2(r)+12.0**2)
        vc = np.sqrt(Gk*Menc(r)/r)
        out = []
        for vs in [120, 300, 3000]:
            q = vs**2+s**2
            out.append((vs**2/q)**1.5*np.exp(-V**2/(2*q)))
        print("(3) Fornax %s: v_c = %.1f, sigma_halo = %.1f km/s ; <W> gauss v*=120,300,3000: %.3f %.3f %.3f ; eps<0.4/<W> at 120: %.2f"
              % (lab, vc, np.sqrt(sig2(r)), out[0], out[1], out[2], 0.4/out[0]))
