"""Observational limits on the corner (eps > 1, v* <~ 30 km/s) from small-scale structure
(round 3, label "corner").  Linear-theory proxies only; both readings of linear_corner.py.

A. High-resolution Lyman-alpha forest.  Tolerance proxy: the linear-power suppression of the
   warm-dark-matter models at the published 2-sigma bounds, m_WDM > 5.3 keV (XQ-100 + HIRES/MIKE,
   z = 3-5.4, smooth thermal history) and 3.5 keV (non-smooth thermal history) [S: Irsic et al.
   2017, PRD 96, 023522, arXiv:1702.01764, via search summary], with the Viel et al. 2005 fit
   T^2 = [1 + (alpha k)^(2 nu)]^(-10/nu), nu = 1.12,
   alpha = 0.049 (m/keV)^-1.11 (Omega_wdm/0.25)^0.11 (h/0.7)^1.22 Mpc/h  [S via search summaries;
   Omega_wdm = Omega_c and h from Planck 2018].  A gated model whose |T^2 - 1| at k = 0.1 s/km
   (z = 4.2) exceeds the WDM deviation there is marked 'beyond'.  This compares one number of the
   linear power, not a likelihood; an enhancement (K4 reading) is treated like a suppression of the
   same size, which ignores the IGM-temperature degeneracy.
B. sigma(M, z) and 1-sigma collapse redshifts (sigma = 1.686), the K11 proxy; density proxy
   (1+z_c)^3 relative to LCDM for 1e9 and 1e10 Msun, the pre-infall masses of the classical dSphs
   (Read, Walker & Steger 2019 Table 1: 0.8-22e9 Msun [S]), whose rho_DM(150 pc) = 0.79-2.36e8
   Msun/kpc^3 [S] they describe as consistent with CDM cusps for the early-quenched ones.
C. Reionization optical depth, toy model: Q(z) = min(1, zeta f_coll(>1e8 Msun, z)), Press-Schechter
   f_coll = erfc(1.686/(sqrt2 sigma)); zeta fixed (i) so that LCDM gives tau = 0.054 (Planck 2018
   [S]), then the same zeta in the gated model; (ii) per model so that Q(6) = 1 (reionization ends
   at z = 6 [T]).  He I ionized with H, He II at z < 3.5 [T]; Y_p = 0.245 [T, dagger].
D. Segue 1 heating by compact clumps (point masses): from Chandrasekhar's diffusion coefficients
   [T] for a massless star in a Maxwellian of clumps (derived in the docstring of heating_rate),
   d sigma_*^2/dt = (8 sqrt(2 pi)/3) G^2 f rho M_c lnL sigma_c^2/(sigma_c^2 + sigma_*^2)^(3/2).
   Inputs [S: Simon et al. 2011, arXiv:1007.4198, via search summary]: sigma_* = 3.7 km/s,
   M(<r_1/2) = 5.8e5 Msun, R_1/2 = 29 pc (3D r_1/2 = 4/3 R_1/2 [T]); age 12 Gyr [dagger];
   lnL = 5 [assumed]; criterion Delta sigma_*^2 < sigma_*^2 [assumed].  Clumps survive inside
   Segue 1 only if denser than its mean DM density: rho_s = (Delta/2.317) rho_crit Omega_m (1+z_c)^3
   with Delta = 200 (Graham & Ramani 2024, arXiv:2404.01378 [S]) gives the minimum z_c.
"""
import os
import sys
import numpy as np
from math import erfc, sqrt, pi

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import linear_corner as L   # noqa: E402
C = L.C

# ---------------- A. Lyman-alpha ----------------
def T2_wdm(k_mpc, m_keV):
    alpha = 0.049 * m_keV**-1.11 * (C.Oc / 0.25)**0.11 * (C.h / 0.7)**1.22   # Mpc/h
    nu = 1.12
    return (1 + (alpha * k_mpc / C.h)**(2 * nu))**(-10 / nu)


z_ly = 4.2
ks = np.array([0.05, 0.1, 0.2])
kmpc = ks * C.Hz(z_ly) / (1 + z_ly)
print(f"A. Lyman-alpha, z = {z_ly}: k = {ks} s/km = {np.round(kmpc, 3)} /Mpc")
tol = {}
for m in (5.3, 3.5):
    t = T2_wdm(kmpc, m)
    tol[m] = 1 - t
    print(f"   WDM {m} keV: T2 = {np.round(t, 4)}  -> allowed |T2-1| proxy {np.round(1-t, 4)}")
eps_grid = [0.3, 1, 2, 3, 5, 10]
vs_grid = [3, 5, 7, 10, 15, 20, 30]
res = {}
for reading in ("H", "K4"):
    print(f"   reading {reading}: T2 at k = 0.05 / 0.1 / 0.2 s/km; flag: B53 = beyond the 5.3-keV deviation at 0.1 s/km, "
          f"B35 = beyond 3.5 keV; (0.05) = also beyond at 0.05 s/km")
    for vs in vs_grid:
        line = []
        for e in eps_grid:
            t2 = L.T2(kmpc, e, vs, reading, [z_ly])[z_ly]
            dev = np.abs(t2 - 1)
            flag = "B35" if dev[1] > tol[3.5][1] else ("B53" if dev[1] > tol[5.3][1] else "ok ")
            if dev[0] > tol[5.3][0]:
                flag += "(0.05)"
            res[(reading, vs, e)] = (t2, flag)
            line.append(f"e{e:g}:{t2[0]:.3g}/{t2[1]:.3g}/{t2[2]:.3g} {flag}")
        print(f"     v*={vs:2d}: " + " | ".join(line))

# ---------------- B. collapse redshifts and density proxy ----------------
kk = np.logspace(-2, 3.3, 200)
zlist = [0.0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120, 150]
Pk0 = {z: C.P_lin(kk, z) for z in zlist}
masses = [1e2, 1e4, 1e6, 1e7, 1e8, 1e9, 1e10]


def sig_table(eps, vs, reading):
    if eps == 0:
        T = {z: np.ones_like(kk) for z in zlist}
    else:
        T = L.T2(kk, eps, vs, reading, zlist)
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


points = [(1, 5), (3, 5), (1, 10), (3, 10), (10, 10), (1, 20), (3, 20), (1, 30), (3, 30)]
S0 = sig_table(0, 10, "K4")
zc0 = {M: zc_of(S0[M]) for M in masses}
print("\nB. 1-sigma collapse redshift z_c (sigma(M, z_c) = 1.686), linear theory; LCDM: "
      + ", ".join(f"{M:.0e}: {zc0[M]:.2f}" for M in masses))
tables = {}
for reading in ("H", "K4"):
    for e, vs in points:
        S = sig_table(e, vs, reading)
        tables[(reading, e, vs)] = S
        zc = {M: zc_of(S[M]) for M in masses}
        dens = {M: ((1 + zc[M]) / (1 + zc0[M]))**3 for M in (1e9, 1e10)}
        print(f"   {reading:2s} eps={e:2d} v*={vs:2d}: z_c " + ", ".join(f"{M:.0e}:{zc[M]:.1f}" for M in masses)
              + f" | density proxy vs LCDM: 1e9: x{dens[1e9]:.3g}, 1e10: x{dens[1e10]:.3g}")

# ---------------- C. optical depth ----------------
sigT = 6.6524587e-29; mp_ = 1.67262192e-27; Yp = 0.245; cl = 2.99792458e8
rho_c0 = 1.87847e-26 * C.h**2      # kg/m^3 [T]
nH0 = (1 - Yp) * C.Ob * rho_c0 / mp_
fHe = Yp / (4 * (1 - Yp))
zz = np.linspace(0, 150, 3001)


def tau_of(Qz):
    ne = nH0 * (1 + zz)**3 * Qz * (1 + fHe + np.where(zz < 3.5, fHe, 0.0))
    Hs = C.Hz(zz) * 1e3 / 3.0856775814913673e22
    return np.trapezoid(sigT * cl * ne / ((1 + zz) * Hs), zz)


def fcoll(S, M=1e8):
    s = np.interp(zz, zlist, S[M])
    return np.array([erfc(1.686 / (sqrt(2) * x)) if x > 0 else 0.0 for x in s])


fc0 = fcoll(S0)
lo, hi = 1e-3, 1e5
for _ in range(80):
    mid = sqrt(lo * hi)
    if tau_of(np.minimum(1, mid * fc0)) < 0.054:
        lo = mid
    else:
        hi = mid
zeta0 = sqrt(lo * hi)
Q0 = np.minimum(1, zeta0 * fc0)
zend0 = zz[np.argmax(Q0 < 1)] if np.any(Q0 < 1) else np.nan
zeta_end0 = 1 / np.interp(6.0, zz, fc0)
print(f"\nC. tau toy model: LCDM zeta = {zeta0:.3g} gives tau = {tau_of(Q0):.4f}, reionization complete at z = {zend0:.2f}, "
      f"midpoint z = {zz[np.argmin(np.abs(Q0-0.5))]:.2f}; with Q(6) = 1 instead: tau = {tau_of(np.minimum(1, zeta_end0*fc0)):.4f}")
for key, S in tables.items():
    f = fcoll(S)
    t_i = tau_of(np.minimum(1, zeta0 * f))
    ze = 1 / np.interp(6.0, zz, f)
    t_ii = tau_of(np.minimum(1, ze * f))
    print(f"   {key[0]:2s} eps={key[1]:2d} v*={key[2]:2d}: f_coll(>1e8) at z = 6, 10, 20: "
          f"{np.interp(6, zz, f):.3g}, {np.interp(10, zz, f):.3g}, {np.interp(20, zz, f):.3g} | tau (i) same zeta: {t_i:.3f}; "
          f"(ii) Q(6) = 1: {t_ii:.3f}")

# ---------------- D. Segue 1 heating ----------------
G = 4.30091e-3     # pc (km/s)^2 / Msun [T]
sig_s = 3.7; M12 = 5.8e5; R12 = 29.0; r12 = 4 / 3 * R12
rho_seg = M12 / (4 * pi / 3 * r12**3)
age = 12.0          # Gyr [dagger]
lnL = 5.0
kms_pc_to_per_Gyr = 1.0227e3   # (km/s)/pc in 1/Gyr [T]
sig_c = sig_s       # clump dispersion taken equal to the stars' (assumption)
rate_per_fM = (8 * sqrt(2 * pi) / 3) * G**2 * rho_seg * lnL * sig_c**2 / (sig_c**2 + sig_s**2)**1.5 * kms_pc_to_per_Gyr
fM_max = sig_s**2 / (rate_per_fM * age)
print(f"\nD. Segue 1: mean DM density inside r_1/2 = {r12:.1f} pc: {rho_seg:.2f} Msun/pc^3; heating limit for compact clumps "
      f"(f M_c) < {fM_max:.3g} Msun (lnL = {lnL}, {age} Gyr, Delta sigma^2 < sigma^2)")
rho_m0_pc = C.Om * 2.775e11 * C.h**2 / 1e18     # Msun/pc^3
zmin = (rho_seg / (200 / 2.317 * rho_m0_pc))**(1 / 3) - 1
print(f"   clumps denser than that (rho_s = 86.3 rho_m(z_c)) need z_c > {zmin:.1f}")
for key, S in tables.items():
    out = []
    for M in (1e2, 1e4, 1e6):
        s = np.interp(zmin, zlist, S[M])
        out.append(f"M={M:.0e}: sigma(z_min)={s:.3g}, f_coll(>M, z_min)={erfc(1.686/(sqrt(2)*s)) if s > 0 else 0:.3g}")
    print(f"   {key[0]:2s} eps={key[1]:2d} v*={key[2]:2d}: " + "; ".join(out))
s0 = [np.interp(zmin, zlist, S0[M]) for M in (1e2, 1e4, 1e6)]
print(f"   LCDM: sigma(z_min) at 1e2, 1e4, 1e6 Msun = {', '.join(f'{x:.3g}' for x in s0)}")
