"""Round-3 critic, check c2: do the corner agent's linear-theory exclusions survive the kernel corrections?

The corner agent's linear_corner.py integrates two systems (its docstring):
  'K4' : force law with the density kernel R (dark-tests K4 as implemented)  -> both round-3 dark-tests
         verifiers find the force law's density kernel is R1 = Int_0^1 R(y mu) dmu, not R;
  'H'  : critic c4b's Hamiltonian system                                     -> c4b counts -H*A_delta twice
         (check c1 here; round-3 dark-tests derivation verifier D5).
Corrected systems used here (derivation in c1_hamiltonian_system.py; corner sign convention th = -theta):
  'Fc' : d_dc = -th ; d_th = -(2 + dlnH - A) th - 1.5 Om_m [f_c (1 + eps R1) d_c + f_b d_b]
  'Hc' : d_dc = -(1 + b) th - thd ; d_th = -(2 + dlnH + b - A) th - 1.5 Om_m [f_c (1 + eps R) d_c + f_b d_b]
         (= the corner's 'H' with its second '- thd' removed from d_th), b = kappa B, A = kappa R_v,
         thd = -3 kappa yJ d_c, kappa = (eps/2) Om_c.
R1 = R + yJ (identity checked in c1).  All kernels and the cosmology are the corner's own (imported), so
differences from the corner's printed numbers come only from the two corrections.
Proxies, tolerances and data are the corner's (obs_corner.py, segue_heating.py), not re-derived:
WDM-template Lyman-alpha tolerances at z = 4.2 (5.3 / 3.5 keV), 1-sigma collapse redshift density proxy,
toy tau with Q(6) = 1, Segue 1 heating moment (limit 7.88 Msun at z_min = 87.7).
The Hamiltonian reading is singular for kappa B < -1, i.e. eps >~ 2.25 (c1, corner Q9); Hc at eps = 3 is not run.
"""
import os
import sys
import numpy as np
from math import erfc, sqrt

CORNER = "/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/corner"
sys.path.insert(0, CORNER)
import linear_corner as L   # noqa: E402
C = L.C
fc, fb = C.f_c, C.f_b
a_drag = 1.0 / (1.0 + C.z_drag)


def grow(k, eps, vs, reading, z_out, a_i=1e-5, nstep=8000):
    k = np.atleast_1d(np.asarray(k, float))
    N = np.linspace(np.log(a_i), 0.0, nstep)
    zs = sorted(z_out, reverse=True)
    Ns = [np.log(1 / (1 + z)) for z in zs]
    Y = np.zeros((4, k.size)); Y[0] = 1.0

    def rhs(Nv, Y):
        a = np.exp(Nv)
        y = k * vs / (a * C.H0 * C.E(a))
        Omm = C.Omega_m_a(a); Omc = fc * Omm
        dlnH = C.dlnH_dlna(a)
        dc, th, db, thb = Y
        R = L.I("R", y); yJ = L.I("yJ", y)
        A = 0.5 * eps * Omc * L.I("Rv", y)
        if reading in ("H", "Hc"):
            b = 0.5 * eps * Omc * L.I("Ra", y)
            thd = -1.5 * eps * Omc * yJ * dc
            src = 1.5 * Omm * (fc * (1 + eps * R) * dc + fb * db)
            d_dc = -(1 + b) * th - thd
            d_th = -(2 + dlnH + b - A) * th - (thd if reading == "H" else 0.0) - src
        elif reading in ("K4", "Fc"):
            Rd = R if reading == "K4" else R + yJ
            src = 1.5 * Omm * (fc * (1 + eps * Rd) * dc + fb * db)
            d_dc = -th
            d_th = -(2 + dlnH - A) * th - src
        else:
            raise ValueError(reading)
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
                tt = (Nz - Nv) / h
                out[z] = fc * ((1 - tt) * Y[0] + tt * Yn[0]) + fb * ((1 - tt) * Y[2] + tt * Yn[2])
        Y = Yn
    for z in zs:
        if z not in out:
            out[z] = fc * Y[0] + fb * Y[2]
    return out


L.grow = grow     # L.T2 now uses this integrator (it looks the name up at call time)
L._cache.clear()

# ---------------- A. Lyman-alpha, WDM-template tolerances (corner's printed values) ----------------
z_ly = 4.2
ks = np.array([0.05, 0.1, 0.2])
kmpc = ks * C.Hz(z_ly) / (1 + z_ly)
tol53 = np.array([0.0097, 0.0451, 0.1941]); tol35 = np.array([0.0271, 0.1209, 0.4472])


def flag(t2):
    dev = np.abs(t2 - 1)
    f = "B35" if dev[1] > tol35[1] else ("B53" if dev[1] > tol53[1] else "ok ")
    return f + ("(0.05)" if dev[0] > tol53[0] else "")


print(f"A. Lyman-alpha z = {z_ly}, k = {ks} s/km: T2 at 0.05/0.1/0.2 s/km; B53/B35 = beyond the 5.3/3.5-keV WDM deviation at 0.1 s/km")
for rd, vs, e, ref in (("H", 10, 1, "corner H: 0.927/0.754/0.932 B35"), ("K4", 10, 1, "corner K4: 1.2/1.92/6.91 B35"),
                       ("H", 3, 1, "corner H: 0.993/0.974/0.897 ok"), ("K4", 3, 1, "corner K4: 1.02/1.07/1.29 B53")):
    t2 = L.T2(kmpc, e, vs, rd, [z_ly])[z_ly]
    print(f"   anchor {rd} v*={vs} eps={e}: {t2[0]:.3g}/{t2[1]:.3g}/{t2[2]:.3g} {flag(t2)}   [{ref}]")
for rd in ("Hc", "Fc"):
    for vs in (3, 5, 7, 10, 20, 30):
        row = []
        for e in (0.3, 1, 2, 3):
            if rd == "Hc" and e > 2.2:
                row.append(f"e{e:g}: singular"); continue
            t2 = L.T2(kmpc, e, vs, rd, [z_ly])[z_ly]
            row.append(f"e{e:g}:{t2[0]:.3g}/{t2[1]:.3g}/{t2[2]:.3g} {flag(t2)}")
        print(f"   {rd} v*={vs:2d}: " + " | ".join(row))

# ---------------- B, C. collapse-redshift density proxy and toy tau ----------------
kk = np.logspace(-2, 3.3, 200)
zlist = [0.0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120, 150]
Pk0 = {z: C.P_lin(kk, z) for z in zlist}
masses = [1e8, 1e9, 1e10]


def sig_table(eps, vs, reading):
    T = {z: np.ones_like(kk) for z in zlist} if eps == 0 else L.T2(kk, eps, vs, reading, zlist)
    return {M: np.array([L.sigma_M(M, kk, Pk0[z] * T[z]) for z in zlist]) for M in masses}


def zc_of(s):
    lz = np.log(1 + np.array(zlist))
    if s[0] < 1.686:
        return np.nan
    if s[-1] > 1.686:
        return np.inf
    j = int(np.argmax(s < 1.686))
    l = lz[j-1] + (np.log(1.686) - np.log(s[j-1])) / (np.log(s[j]) - np.log(s[j-1])) * (lz[j] - lz[j-1])
    return np.exp(l) - 1


sigT = 6.6524587e-29; mp_ = 1.67262192e-27; Yp = 0.245; cl = 2.99792458e8
rho_c0 = 1.87847e-26 * C.h**2
nH0 = (1 - Yp) * C.Ob * rho_c0 / mp_
fHe = Yp / (4 * (1 - Yp))
zz = np.linspace(0, 150, 3001)


def tau_of(Qz):
    ne = nH0 * (1 + zz)**3 * Qz * (1 + fHe + np.where(zz < 3.5, fHe, 0.0))
    Hs = C.Hz(zz) * 1e3 / 3.0856775814913673e22
    return np.trapezoid(sigT * cl * ne / ((1 + zz) * Hs), zz)


def tau_ii(S):
    s = np.interp(zz, zlist, S[1e8])
    f = np.array([erfc(1.686 / (sqrt(2) * x)) if x > 0 else 0.0 for x in s])
    return tau_of(np.minimum(1, f / np.interp(6.0, zz, f)))


S0 = sig_table(0, 10, "K4")
zc0 = {M: zc_of(S0[M]) for M in masses}
print(f"\nB/C. LCDM z_c: " + ", ".join(f"{M:.0e}: {zc0[M]:.2f}" for M in masses) + f"; tau(ii) LCDM = {tau_ii(S0):.4f} [corner 0.0575]")
for rd, e, vs, ref in (("K4", 1, 10, "corner K4: 1e9 x2.17, tau(ii) 0.068"), ("H", 1, 20, "corner H: 1e9 x2.14, tau(ii) 0.071")):
    S = sig_table(e, vs, rd); zc = {M: zc_of(S[M]) for M in masses}
    print(f"   anchor {rd} eps={e} v*={vs}: 1e9 x{((1+zc[1e9])/(1+zc0[1e9]))**3:.3g}, tau(ii) {tau_ii(S):.3f}   [{ref}]")
for rd in ("Hc", "Fc"):
    for e, vs in ((1, 5), (1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (3, 5), (3, 10), (3, 20), (3, 30)):
        if rd == "Hc" and e > 2.2:
            continue
        S = sig_table(e, vs, rd); zc = {M: zc_of(S[M]) for M in masses}
        d9 = ((1 + zc[1e9]) / (1 + zc0[1e9]))**3; d10 = ((1 + zc[1e10]) / (1 + zc0[1e10]))**3
        print(f"   {rd} eps={e} v*={vs:2d}: z_c(1e8, 1e9, 1e10) = {zc[1e8]:.2f}, {zc[1e9]:.2f}, {zc[1e10]:.2f} | "
              f"density proxy 1e9: x{d9:.3g}, 1e10: x{d10:.3g} | tau(ii) = {tau_ii(S):.3f}  (Planck 0.054 +- 0.007)")

# ---------------- D. Segue 1 heating moment ----------------
z_min = 87.7
kD = np.logspace(-2, 3.6, 260)
PD = C.P_lin(kD, z_min)
Ms = np.logspace(0, 5, 26)


def H_moment(T):
    s = np.array([L.sigma_M(M, kD, PD * T) for M in Ms])
    F = np.array([erfc(1.686 / (sqrt(2) * x)) for x in s])
    Mmid = np.sqrt(Ms[1:] * Ms[:-1])
    return np.sum(Mmid * (F[:-1] - F[1:]))


print(f"\nD. Segue 1 heating moment at z_min = {z_min} (limit 7.88 Msun; LCDM {H_moment(np.ones_like(kD)):.3g})")
for rd, vs, e, ref in (("H", 10, 1.0, "corner H 1.05e3"), ("K4", 10, 1.0, "corner K4 742")):
    print(f"   anchor {rd} v*={vs} eps={e}: H = {H_moment(L.T2(kD, e, vs, rd, [z_min])[z_min]):.3g}   [{ref}]")
for rd in ("Hc", "Fc"):
    for vs in (3, 5, 10, 20):
        row = []
        for e in (0.3, 1.0, 2.0):
            Hm = H_moment(L.T2(kD, e, vs, rd, [z_min])[z_min])
            row.append(f"eps={e:g}: H={Hm:.3g}{' >limit' if Hm > 7.88 else ''}")
        print(f"   {rd} v*={vs:2d}: " + " | ".join(row))
