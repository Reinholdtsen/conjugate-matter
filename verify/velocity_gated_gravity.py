#!/usr/bin/env python3
"""
velocity_gated_gravity.py — every load-bearing number of the momentum-gravity investigation (notes/
velocity-gated-gravity.md), recomputed and checked. Paul's question (2026-10-26): "I think the obituary is
premature. Would momentum gravity look like a perturbation to regular gravity that depends on the relative
velocity of two massive bodies?" The investigation ran outside the repository in executed scripts; its record
(analyses, verdicts, the critics' rulings, every script beside its printed output) is review/momentum-gravity/.
This file ports the scripts it needs (it imports none of them) and is self-contained. The ported source is
named at each section as scripts/<agent>/<file>, relative to review/momentum-gravity/. The numbers checked are
those of review/momentum-gravity/answer.md and of the final critic's load-bearing list (run3/critic.json);
where the two differ, the critic's ruling and run 4's corrections (applied in answer.md) are used.

    .venv/bin/python verify/velocity_gated_gravity.py

Exit code 1 if any check fails. Anchors come first and are independent of the investigation: CODATA 2018
constants; the Einstein-Infeld-Hoffmann O(G) two-body Lagrangian and the Darwin Lagrangian (Landau-Lifshitz
sec. 106 and 65), which the Fokker action of massless spin-2 and spin-1 exchange must reproduce; the textbook
Fierz-Pauli and de Donder numerators; Planck 2018's published age and matter-radiation equality, which the
LCDM backgrounds must reproduce; the exact Einstein-de Sitter and Meszaros growing modes, which the growth
integrators must reproduce; the closed form of the gate's Fourier kernel (an erfi integral); Lee et al. 2020's
published torsion-balance ranges, which the interpolation for X's range must reproduce; Mercury's general-
relativistic perihelion advance, which the precession code's units must reproduce; the Plummer sphere's
central free-fall time. Everything after the anchors is a regression check: it reproduces the investigation's
own numbers and is not independent of them. Checks marked "record" read the record's printed output and
recompute nothing: they cover the 29 N-body runs of the low-v* corner, whose runs took hours of CPU and whose
snapshots (about 90 MB) were not kept, so they cannot be rerun here.

Inputs: CODATA 2018. The record's hypothetical long-range attraction U = -eps G m^2 W(|v - v'|/v*)/r with the
amplitude gate W = exp(-s^2/2) (the record's convention; the ordinary-matter analyses use exp(-v^2/v_a^2), and
v_a = sqrt2 v*); v* = 120 km/s; m_chi = 70 MeV and sigma_T/m = 30 cm^2/g at 30 km/s (Debt 3a). Each data input
(Planck 2018, DESI DR1 and eBOSS Lyman-alpha compressions, planetary ephemerides, the double pulsar, Lee et al.
2020, Vasiliev-Belokurov 2020's Sagittarius, Enander-Mortsell 2013) is typed in with its source where it is
used; the record marks them [S] (live-searched by its agents) unless a dagger is shown.

Two ports are reduced, without changing any printed digit: the critic's kernel table (critic3/c1) is built only
on its nodes up to y = 3 (the v* = 120 km/s runs never leave y < 1.2; the code refuses y in (3, 300]), and the
corner's kernels (corner/linear_corner.py) evaluate sin and cos once per node. Not recomputed: the N-body
runs (see above); the satellite-count proxy corner/sat_proxy.py (the critic did not rerun it either); the
superseded round-2 analyses except where a superseded number is quoted.

Runtime is about 35 s on the development machine (8 GB); peak resident memory about 175 MB.
"""
import itertools
import os
import re
import sys
import time
from math import pi, sqrt, log, log10, exp, erfc, floor
import mpmath as mp
import numpy as np
import sympy as sp

T_START = time.time()
failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def close(x, y, rel):
    return abs(x/y - 1) < rel
def rs(x, n):
    """x to n significant figures"""
    return float(f"{x:.{n}g}")
def r2(x): return rs(x, 2)
def r3(x): return rs(x, 3)
def r4(x): return rs(x, 4)
def stamp():
    print(f"      [{time.time() - T_START:.1f} s]")

HERE = os.path.dirname(os.path.abspath(__file__))
RECORD = os.path.join(HERE, "..", "review", "momentum-gravity", "scripts")

# CODATA 2018 (h, c, e exact; G measured)
HBAR = 1.054571817e-34; C = 299792458.0; G = 6.67430e-11; EV = 1.602176634e-19
HBARC_EVM = HBAR*C/EV                                   # 1.973269804e-7 eV m
C_KMS = 299792.458
KPC = 3.0856775814913673e19; PC = 3.0856775814913673e16; AU = 1.495978707e11
GEV_KG = 1.78266192e-27
PHI = (1 + sqrt(5))/2


# ======================================================================================================
# Backgrounds. Three LCDM backgrounds are used, each as its record script used it.
#  BG_DT: the dark-tests agent's cosmo.py (Planck 2018 TT,TE,EE+lowE+lensing [S], 0.06 eV neutrino treated as
#         massless) with its EH98 no-wiggle P(k) and sigma8 normalization: the corner (corner/linear_corner.py)
#         and the gate radius (dark-tests/r_gate.py) run on it.
#  BG_VDD: the round-3 dark-tests derivation verifier's v3_cosmo.py (same column, one massive neutrino in
#         Omega_m): only its Omega_c(z = 10) enters a quoted number (the singular eps).
#  BG_C1: the final critic's c1_hamiltonian_system.py (TT,TE,EE+lowE+lensing+BAO column, dagger: h = 0.6766,
#         omega_c = 0.11933, omega_b = 0.02242, massless neutrinos): the Lyman-alpha bounds run on it.
# ======================================================================================================
MPC_KM = 3.0856775814913673e19; GYR_S = 3.15576e16

class BG:
    """flat background: Om, Orad, OL; f_c, f_b of the clustering matter; H0 in km/s/Mpc; a_drag"""
    def __init__(self, H0, Om, Orad, OL, f_c, f_b, a_drag, Oc=None):
        self.H0, self.Om, self.Orad, self.OL, self.f_c, self.f_b, self.a_drag = H0, Om, Orad, OL, f_c, f_b, a_drag
        self.Oc = Oc
    def E(self, a):
        a = np.asarray(a, float)
        return np.sqrt(self.Orad/a**4 + self.Om/a**3 + self.OL)
    def Hz(self, z):
        return self.H0*self.E(1.0/(1.0 + np.asarray(z, float)))
    def dlnH_dlna(self, a):
        a = np.asarray(a, float)
        return 0.5*(-4*self.Orad/a**4 - 3*self.Om/a**3)/self.E(a)**2
    def Omega_m_a(self, a):
        return self.Om/a**3/self.E(a)**2
    def age_gyr(self, n=200000):
        lna = np.linspace(log(1e-9), 0.0, n)
        return np.trapezoid(1.0/(self.H0*self.E(np.exp(lna))), lna)*MPC_KM/GYR_S

# dark-tests/cosmo.py
DT_h = 0.6736; DT_omb, DT_omc = 0.02237, 0.1200; DT_Om = 0.3153
DT_Ob, DT_Oc = DT_omb/DT_h**2, DT_omc/DT_h**2
DT_sigma8, DT_ns, DT_zdrag, DT_Tcmb, DT_Neff = 0.8111, 0.9649, 1059.94, 2.7255, 3.046
DT_Orad = 2.4728e-5*(DT_Tcmb/2.7255)**4*(1.0 + 0.2271*DT_Neff)/DT_h**2
BG_DT = BG(100*DT_h, DT_Om, DT_Orad, 1.0 - DT_Om - DT_Orad, DT_Oc/(DT_Oc + DT_Ob), DT_Ob/(DT_Oc + DT_Ob),
           1.0/(1.0 + DT_zdrag), Oc=DT_Oc)

# verify-dark-tests-derivation/v3_cosmo.py
VDD_h = 0.6736
VDD_Oc, VDD_Ob, VDD_Onu = 0.1200/VDD_h**2, 0.02237/VDD_h**2, 0.06/93.14/VDD_h**2
VDD_Or = 2.4728e-5*(1 + 3.046*(7/8)*(4/11)**(4/3))/VDD_h**2
VDD_Om = VDD_Oc + VDD_Ob + VDD_Onu
VDD_OL = 1 - VDD_Om - VDD_Or
def vdd_E2(a): return VDD_Or/a**4 + VDD_Om/a**3 + VDD_OL
def vdd_Omc(a): return VDD_Oc/a**3/vdd_E2(a)

# critic3/c1_hamiltonian_system.py
C1_h = 0.6766; C1_omc, C1_omb = 0.11933, 0.02242
C1_Oc, C1_Ob = C1_omc/C1_h**2, C1_omb/C1_h**2
C1_Om = C1_Oc + C1_Ob
C1_Orad = 2.4728e-5*(1 + 0.2271*3.046)/C1_h**2
BG_C1 = BG(100*C1_h, C1_Om, C1_Orad, 1 - C1_Om - C1_Orad, C1_Oc/C1_Om, C1_Ob/C1_Om, 1/1061.0, Oc=C1_Oc)
BG_EDS = BG(70.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, Oc=1.0)       # Einstein-de Sitter, all chi (anchors)

# dark-tests/cosmo.py: linear growth (Meszaros growing mode with smooth radiation and Lambda), EH98, sigma8
def solve_growth(bg, a_i=1e-6, a_f=1.5, n=30000):
    """sub-horizon matter growth, started on the Meszaros growing mode D = 1 + 3y/2, y = a/a_eq (RK4 in ln a)"""
    a_eq = bg.Orad/bg.Om
    lna = np.linspace(log(a_i), log(a_f), n)
    dN = lna[1] - lna[0]
    Nh = lna[:-1] + dN/2
    f1 = -(2 + bg.dlnH_dlna(np.exp(lna))); g1 = 1.5*bg.Omega_m_a(np.exp(lna))
    fh = -(2 + bg.dlnH_dlna(np.exp(Nh))); gh = 1.5*bg.Omega_m_a(np.exp(Nh))
    y0 = a_i/a_eq
    D = np.empty(n); Dp = np.empty(n)
    d, dp = 1 + 1.5*y0, 1.5*y0
    D[0], Dp[0] = d, dp
    for i in range(n - 1):
        k1d, k1p = dp, f1[i]*dp + g1[i]*d
        d2, p2 = d + dN/2*k1d, dp + dN/2*k1p
        k2d, k2p = p2, fh[i]*p2 + gh[i]*d2
        d3, p3 = d + dN/2*k2d, dp + dN/2*k2p
        k3d, k3p = p3, fh[i]*p3 + gh[i]*d3
        d4, p4 = d + dN*k3d, dp + dN*k3p
        k4d, k4p = p4, f1[i + 1]*p4 + g1[i + 1]*d4
        d += dN/6*(k1d + 2*k2d + 2*k3d + k4d)
        dp += dN/6*(k1p + 2*k2p + 2*k3p + k4p)
        D[i + 1], Dp[i + 1] = d, dp
    return lna, D, Dp

DT_lna, DT_D, DT_Dp = solve_growth(BG_DT)
DT_D1 = np.interp(0.0, DT_lna, DT_D)
def growth_LCDM(a):
    return np.interp(np.log(a), DT_lna, DT_D)/DT_D1
def growth_rate_f(a):
    return np.interp(np.log(a), DT_lna, DT_Dp/DT_D)
def T_EH_nowiggle(k):
    """Eisenstein & Hu 1998 no-wiggle transfer function (eqs. 26, 28-31), k in 1/Mpc"""
    k = np.asarray(k, float)
    omh2 = DT_Om*DT_h**2; fb = DT_Ob/DT_Om; th = DT_Tcmb/2.7
    s = 44.5*np.log(9.83/omh2)/np.sqrt(1.0 + 10.0*DT_omb**0.75)
    alpha = 1.0 - 0.328*np.log(431.0*omh2)*fb + 0.38*np.log(22.3*omh2)*fb**2
    Gam = DT_Om*DT_h*(alpha + (1.0 - alpha)/(1.0 + (0.43*k*s)**4))
    q = k/DT_h*th**2/Gam
    L0 = np.log(2*np.e + 1.8*q); C0 = 14.2 + 731.0/(1.0 + 62.5*q)
    return L0/(L0 + C0*q**2)
def tophat(x):
    x = np.asarray(x, float)
    return np.where(x < 1e-3, 1.0 - x**2/10.0, 3.0*(np.sin(x) - x*np.cos(x))/np.maximum(x, 1e-300)**3)
_KGRID = np.logspace(-5, 3, 6000)
DT_AS = DT_sigma8**2/np.trapezoid(_KGRID**3*_KGRID**DT_ns*T_EH_nowiggle(_KGRID)**2*tophat(_KGRID*8.0/DT_h)**2/
                                  (2*np.pi**2), np.log(_KGRID))
def P_lin(k, z=0.0):
    D = growth_LCDM(1.0/(1.0 + z)) if z != 0 else 1.0
    k = np.asarray(k, float)
    return DT_AS*k**DT_ns*T_EH_nowiggle(k)**2*D**2
def sigma_R(R):
    return sqrt(np.trapezoid(_KGRID**3*P_lin(_KGRID)*tophat(_KGRID*R)**2/(2*np.pi**2), np.log(_KGRID)))


# ======================================================================================================
# The critic's kernels and linear system (port of critic3/c1_hamiltonian_system.py). Gaussian gate W(t) =
# exp(-t^2/2); y = k v*/(aH) with k comoving. Kernels by direct quadrature of their definitions:
#   R  = y Int sin(yt) W dt (kernel of grad[W(s/s_c)/s]); R1 = y Int W j1(yt) dt (force law, fixed velocity);
#   J  = Int t W' j1(yt) dt; R_v = 1 + 3 Int W' g(yt) dt, g = j0 - 2 j1/x; B = 1 + 3 Int [t W'' g + 2 W' j1/x] dt.
# Systems (theta = -i k w/H, ' = d/dlna, kappa = (eps/2) Omega_c(a)):
#   F (force law):  delta' = theta; theta' = -(2 + Hdot/H^2) theta + grav + 3 kappa R1 delta + kappa R_v theta
#   H (record's Hamiltonian reading, = VDD's D2):
#                   delta' = (1 + kappa B) theta + 3 kappa yJ delta;
#                   theta' = ... + 3 kappa (R1 - yJ) delta + kappa (R_v - B) theta
#   agent (round-2 dark-tests hybrid): F with R in place of R1; c4b (round-2 critic): H with R - yJ in place
#   of R1 - yJ (the -H A_delta term counted twice).
# ======================================================================================================
C1_T = np.linspace(0.0, 12.0, 120001)
C1_W = np.exp(-C1_T**2/2); C1_Wp = -C1_T*C1_W; C1_Wpp = (C1_T**2 - 1)*C1_W
C1_TWp, C1_TWpp = C1_T*C1_Wp, C1_T*C1_Wpp
def c1_kernels(y):
    x = y*C1_T
    s = np.sin(x); c = np.cos(x)
    n = int(np.count_nonzero(x < 1e-2))                   # series below x = 1e-2, as in c1's sph()
    j0 = np.empty_like(x); j1 = np.empty_like(x); j1x = np.empty_like(x)
    xs = x[:n]
    j0[:n] = 1 - xs**2/6 + xs**4/120
    j1[:n] = xs/3 - xs**3/30
    j1x[:n] = 1/3 - xs**2/30 + xs**4/840
    inv = 1/x[n:]
    j0[n:] = s[n:]*inv
    j1[n:] = s[n:]*inv**2 - c[n:]*inv
    j1x[n:] = j1[n:]*inv
    g = j0 - 2*j1x
    R = y*np.trapezoid(s*C1_W, C1_T)
    R1 = y*np.trapezoid(C1_W*j1, C1_T)
    J = np.trapezoid(C1_TWp*j1, C1_T)
    Rv = 1 + 3*np.trapezoid(C1_Wp*g, C1_T)
    B = 1 + 3*np.trapezoid(C1_TWpp*g + 2*C1_Wp*j1x, C1_T)
    return R, R1, J, Rv, B

C1_LY = np.linspace(log(1e-3), log(300.0), 700)
C1_NUSE = int(np.searchsorted(C1_LY, log(3.0))) + 1      # nodes up to y = 3 (reduction; see docstring)
C1_YMAX = float(np.exp(C1_LY[C1_NUSE - 1]))
C1_TAB = None
C1_ASYM = np.array([1.0, 1.0, 0.0, 1.0, 1.0])
def c1_K(y):
    l = np.log(np.maximum(y, 1e-30))
    if np.any((l > C1_LY[C1_NUSE - 1]) & (l <= C1_LY[-1])):
        raise ValueError("y outside the ported part of the kernel table")
    out = []
    for c in range(5):
        v = np.interp(l, C1_LY[:C1_NUSE], C1_TAB[:, c])
        v = np.where(l > C1_LY[-1], C1_ASYM[c], v)
        if c in (0, 1, 3):                                 # R, R1, R_v ~ y^2 at small y
            v = np.where(l < C1_LY[0], C1_TAB[0, c]*(np.exp(l)/exp(C1_LY[0]))**2, v)
        out.append(v)
    return out

C1_SYS = ("lcdm", "agent", "F", "H", "c4b")
def c1_grow(k, vs, cases, bg=BG_C1, a_end=0.25, a_i=1e-6, nstep=16000):
    """RK4 in ln a for every (system, eps) column at once; cases = [(system, eps array), ...].
    Returns, per case, (total matter delta, baryon delta), each of shape (len(k), len(eps))."""
    k = np.asarray(k, float)[:, None]
    sid, eps, sl, i0 = [], [], [], 0
    for s_, e_ in cases:
        e_ = np.atleast_1d(np.asarray(e_, float))
        sid += [C1_SYS.index(s_)]*len(e_); eps.append(e_); sl.append(slice(i0, i0 + len(e_))); i0 += len(e_)
    eps = np.concatenate(eps)[None, :]; sid = np.array(sid)[None, :]
    isH = (sid == 3) | (sid == 4); gated = sid != 0
    useR1 = (sid == 2) | (sid == 3)
    N0, N1 = log(a_i), log(a_end); dN = (N1 - N0)/nstep
    def rhs(N, Y):
        dc, th, db, tb = Y
        a = exp(N)
        om = float(bg.Omega_m_a(a)); oc, ob = bg.f_c*om, bg.f_b*om
        fr = -(2 + float(bg.dlnH_dlna(a)))
        grav = 1.5*(oc*dc + ob*db)
        y = k*vs/(a*bg.H0*float(bg.E(a)))
        R, R1, J, Rv, B = c1_K(y)
        kap = 0.5*eps*oc
        yJ = y*J
        Dk = np.where(useR1, R1, R) - np.where(isH, yJ, 0.0)
        Vk = np.where(isH, Rv - B, Rv)
        ddc = np.where(isH, (1 + kap*B)*th + 3*kap*yJ*dc, th)
        dth = fr*th + grav + np.where(gated, 3*kap*Dk*dc + kap*Vk*th, 0.0)
        if a >= bg.a_drag:
            ddb, dtb = tb, fr*tb + grav
        else:
            ddb, dtb = 0*db, 0*tb
        return np.array([ddc, dth, ddb, dtb])
    Y = np.zeros((4, k.shape[0], eps.shape[1])); Y[0] = 1.0
    N = N0
    for _ in range(nstep):
        k1 = rhs(N, Y); k2 = rhs(N + dN/2, Y + dN/2*k1); k3 = rhs(N + dN/2, Y + dN/2*k2); k4 = rhs(N + dN, Y + dN*k3)
        Y = Y + dN/6*(k1 + 2*k2 + 2*k3 + k4); N += dN
    m = bg.f_c*Y[0] + bg.f_b*Y[2]
    return [(m[:, s_], Y[2][:, s_]) for s_ in sl]


# ======================================================================================================
# The corner's kernels and linear systems (port of corner/linear_corner.py and critic3/c2_corner_recheck.py),
# on BG_DT. Corner sign convention th = -theta. With b = kappa R_a, A = kappa R_v, thd = -3 kappa yJ delta_c:
#   K4 (round-2 force law, density kernel R):   dc' = -th; th' = -(2 + dlnH - A) th - S(R)
#   H  (round-2 critic c4b):                    dc' = -(1 + b) th - thd; th' = -(2 + dlnH + b - A) th - thd - S(R)
#   Fc (corrected force law, R1 = R + yJ):      dc' = -th; th' = -(2 + dlnH - A) th - S(R + yJ)
#   Hc (corrected Hamiltonian, = D2):           H without the second -thd
# S(K) = 1.5 Om_m [f_c (1 + eps K) dc + f_b db]; baryons held at zero before z_drag, then gravity only.
# ======================================================================================================
def _R_gauss(y):
    if y == 0:
        return 0.0
    x = y/np.sqrt(2)
    return float(np.sqrt(2)*y*mp.sqrt(mp.pi)/2*mp.exp(-x**2)*mp.erfi(x))
CN_TQ = np.linspace(0, 14, 28001)
CN_Wp = -CN_TQ*np.exp(-CN_TQ**2/2); CN_Wpp = (CN_TQ**2 - 1)*np.exp(-CN_TQ**2/2)
def cn_kernels(y):
    """R_v, R_a, J_W of linear_corner.py (its _g0, _g2, _j1 with sin and cos evaluated once)"""
    x = y*CN_TQ
    s, c = np.sin(x), np.cos(x)
    xs = np.where(x == 0, 1.0, x)
    g0 = np.where(x == 0, 2.0, 2*s/xs)
    g2 = np.where(np.abs(x) < 1e-2, 2/3 - x**2/5 + x**4/84, 2*(s/xs + 2*c/xs**2 - 2*s/xs**3))
    j1 = np.where(np.abs(x) < 1e-3, x/3 - x**3/30, s/xs**2 - c/xs)
    Rv = 1 + 1.5*np.trapezoid(CN_Wp*g2, CN_TQ)
    Ra = 1 + 1.5*np.trapezoid(CN_TQ*CN_Wpp*g2 + CN_Wp*(g0 - g2), CN_TQ)
    JW = np.trapezoid(CN_TQ*CN_Wp*j1, CN_TQ)
    return Rv, Ra, JW
CN_YG = np.concatenate([np.linspace(0, 2, 401)[:-1], np.linspace(2, 60, 1161)])
CN_TAB = None
def cn_I(name, y):
    return np.interp(y, CN_YG, CN_TAB[name], right=(0.0 if name == "yJ" else 1.0))

CN_RD = {"K4": 0, "H": 1, "Fc": 2, "Hc": 3}
def cn_grow(k, cases, z_out, bg=BG_DT, a_i=1e-5, nstep=8000):
    """the corner's RK4 on its fixed ln a grid, every case at once; cases = [(eps, v*, reading), ...].
    Returns z -> total-matter delta, shape (len(cases), len(k)). Stops once every z_out is recorded (the
    grid and the interpolation at each z are those of the original)."""
    k = np.atleast_1d(np.asarray(k, float))[None, :]
    eps = np.array([c_[0] for c_ in cases], float)[:, None]
    vs = np.array([c_[1] for c_ in cases], float)[:, None]
    rd = np.array([CN_RD[c_[2]] for c_ in cases])[:, None]
    isH = (rd == 1) | (rd == 3); dbl = rd == 1; isFc = rd == 2
    N = np.linspace(log(a_i), 0.0, nstep)
    zs = sorted(z_out, reverse=True); Ns = [log(1/(1 + z)) for z in zs]
    Y = np.zeros((4, eps.shape[0], k.shape[1])); Y[0] = 1.0
    def rhs(Nv, Y):
        a = exp(Nv)
        y = k*vs/(a*bg.H0*float(bg.E(a)))
        Omm = float(bg.Omega_m_a(a)); Omc = bg.f_c*Omm; dlnH = float(bg.dlnH_dlna(a))
        dc, th, db, thb = Y
        R = cn_I("R", y); yJ = cn_I("yJ", y)
        A = 0.5*eps*Omc*cn_I("Rv", y)
        b = np.where(isH, 0.5*eps*Omc*cn_I("Ra", y), 0.0)
        thd = np.where(isH, -1.5*eps*Omc*yJ*dc, 0.0)
        src = 1.5*Omm*(bg.f_c*(1 + eps*np.where(isFc, R + yJ, R))*dc + bg.f_b*db)
        d_dc = -(1 + b)*th - thd
        d_th = -(2 + dlnH + b - A)*th - np.where(dbl, thd, 0.0) - src
        if a < bg.a_drag:
            return np.array([d_dc, d_th, 0*db, 0*thb])
        return np.array([d_dc, d_th, -thb, -(2 + dlnH)*thb - 1.5*Omm*(bg.f_c*dc + bg.f_b*db)])
    out = {}
    hh = N[1] - N[0]
    for i in range(nstep - 1):
        Nv = N[i]
        k1 = rhs(Nv, Y); k2 = rhs(Nv + hh/2, Y + hh/2*k1); k3 = rhs(Nv + hh/2, Y + hh/2*k2); k4 = rhs(Nv + hh, Y + hh*k3)
        Yn = Y + hh/6*(k1 + 2*k2 + 2*k3 + k4)
        for z, Nz in zip(zs, Ns):
            if Nv < Nz <= Nv + hh and z not in out:
                tt = (Nz - Nv)/hh
                out[z] = bg.f_c*((1 - tt)*Y[0] + tt*Yn[0]) + bg.f_b*((1 - tt)*Y[2] + tt*Yn[2])
        Y = Yn
        if len(out) == len(zs):
            break
    for z in zs:
        if z not in out:
            out[z] = bg.f_c*Y[0] + bg.f_b*Y[2]
    return out
def cn_T2(k, cases, zlist):
    """P_gated/P_LCDM of total matter for every case (baseline: eps = 0, as the corner's T2)"""
    g = cn_grow(k, [(0.0, 10.0, "K4")] + list(cases), zlist)
    return {z: (g[z][1:]/g[z][0:1])**2 for z in zlist}


# ======================================================================================================
print("== Anchors (independent of the investigation)")
# ======================================================================================================
check("A1: CODATA 2018 hbar c = 197.3269804 MeV fm", close(HBARC_EVM, 1.973269804e-7, 1e-9), f"{HBARC_EVM:.10e} eV m")
check("A1: CODATA 2018 Planck mass 2.176434e-8 kg", close(sqrt(HBAR*C/G), 2.176434e-8, 2e-6), f"{sqrt(HBAR*C/G):.6e}")

# --- Fokker action of linear-field exchange at O(v^2) (port of scripts/verify-program-derivation/v1_spin2_fokker.py)
# time-symmetric Green's function G(r, tau) = delta(tau) Y(r) - delta''(tau) Z(r) + ...; cross term
# J1 J2 Y - J1 J2 v1_i v2_j d_i d_j Z; spin-2 tensor factor T1.T2 - c T1 T2 (c = 1/2 massless, 1/3 Fierz-Pauli)
va = sp.Matrix(sp.symbols('a1:4', real=True)); vb = sp.Matrix(sp.symbols('b1:4', real=True))
xx, yy_, zz_ = sp.symbols('x y z', real=True)
rvec = sp.Matrix([xx, yy_, zz_]); rr = sp.sqrt(xx**2 + yy_**2 + zz_**2); nvec = rvec/rr
Gs, m1s, m2s, Ms, als, e1s, e2s, epss = sp.symbols('G m1 m2 M alpha e1 e2 epsilon', positive=True)
ETA = sp.diag(1, -1, -1, -1)
v1s = (va.T*va)[0]; v2s = (vb.T*vb)[0]; v12 = (va.T*vb)[0]; nv1 = (nvec.T*va)[0]; nv2 = (nvec.T*vb)[0]
gam1 = 1/sp.sqrt(1 - v1s); gam2 = 1/sp.sqrt(1 - v2s)
def hess_contract(Zf):
    H = sp.Matrix(3, 3, lambda i, j: sp.diff(Zf, rvec[i], rvec[j]))
    return (va.T*H*vb)[0]
def series2(f):
    return sp.series(f.subs({s_: epss*s_ for s_ in list(va) + list(vb)}, simultaneous=True), epss, 0, 3).removeO().subs(epss, 1)
def F_tensor(cval):
    vmu1 = sp.Matrix([1, *va]); vmu2 = sp.Matrix([1, *vb])
    dot4 = (vmu1.T*ETA*vmu2)[0]
    full = gam1*gam2*dot4**2 - cval*gam1*(1 - v1s)*gam2*(1 - v2s)
    return series2(full)/(1 - cval)
Y0 = 1/(4*sp.pi*rr); Z0 = -rr/(8*sp.pi)
YM = sp.exp(-Ms*rr)/(4*sp.pi*rr); ZM = sp.exp(-Ms*rr)/(8*sp.pi*Ms)
lap = lambda f: sum(sp.diff(f, s_, 2) for s_ in (xx, yy_, zz_))
green_ok = (sp.simplify(-lap(Z0) - Y0) == 0 and sp.simplify(-lap(ZM) + Ms**2*ZM - YM) == 0 and
            sp.simplify(-lap(YM) + Ms**2*YM) == 0)
F0 = F_tensor(sp.Rational(1, 2)); F1 = F_tensor(sp.Rational(1, 3))
L_spin2 = Gs*m1s*m2s*4*sp.pi*(F0*Y0 - hess_contract(Z0))
EIH_G = Gs*m1s*m2s/rr*(1 + sp.Rational(3, 2)*(v1s + v2s) - sp.Rational(7, 2)*v12 - sp.Rational(1, 2)*nv1*nv2)
L_spin1 = -e1s*e2s*4*sp.pi*((1 - v12)*Y0 - hess_contract(Z0))
DARWIN = -e1s*e2s/rr + e1s*e2s/(2*rr)*(v12 + nv1*nv2)
check("A2: Fokker action: massless spin-2 exchange at O(v^2) reproduces the O(G) terms of the Einstein-Infeld-Hoffmann "
      "Lagrangian (G m1 m2/r)[1 + 3/2(v1^2 + v2^2) - 7/2 v1.v2 - 1/2 (n.v1)(n.v2)] (Landau-Lifshitz sec. 106) exactly; "
      "spin 1 reproduces the Darwin Lagrangian (LL sec. 65); Y = e^(-Mr)/4pi r, Z = e^(-Mr)/8pi M solve their equations",
      green_ok and sp.simplify(sp.expand(L_spin2 - EIH_G)) == 0 and sp.simplify(sp.expand(L_spin1 - DARWIN)) == 0)
gq = sp.symbols('gamma', positive=True)
N_dd = (gq**2 - sp.Rational(1, 2))/(1 - sp.Rational(1, 2)); N_fp = (gq**2 - sp.Rational(1, 3))/(1 - sp.Rational(1, 3))
check("A3: textbook numerators normalized to their static value: de Donder (massless) (gamma^2 - 1/2)/(1/2) = 2 gamma^2 - 1 = "
      "T_2(gamma); Fierz-Pauli (gamma^2 - 1/3)/(2/3) = (3 gamma^2 - 1)/2 = P_2(gamma); static ratio massive/massless 4/3 "
      "(vDVZ), 3/4 as gamma -> infinity",
      sp.simplify(N_dd - sp.chebyshevt(2, gq)) == 0 and sp.simplify(N_fp - sp.legendre(2, gq)) == 0 and
      sp.Rational(2, 3)/sp.Rational(1, 2) == sp.Rational(4, 3) and sp.limit(N_fp/N_dd, gq, sp.oo) == sp.Rational(3, 4))
mp.mp.dps = 40
ok_tf = True
rng_tf = np.random.default_rng(7)
for _ in range(5):
    w1 = [mp.mpf(int(x_))/100 for x_ in rng_tf.integers(-30, 31, 3)]; w2 = [mp.mpf(int(x_))/100 for x_ in rng_tf.integers(-30, 31, 3)]
    g1_ = 1/mp.sqrt(1 - sum(x_**2 for x_ in w1)); g2_ = 1/mp.sqrt(1 - sum(x_**2 for x_ in w2))
    u1 = [g1_] + [g1_*x_ for x_ in w1]; u2 = [g2_] + [g2_*x_ for x_ in w2]
    dot = lambda p_, q_: p_[0]*q_[0] - sum(p_[i]*q_[i] for i in (1, 2, 3))
    TT = sum((1 if i == 0 else -1)*(1 if j == 0 else -1)*u1[i]*u1[j]*u2[i]*u2[j] for i in range(4) for j in range(4))
    ok_tf &= abs(TT - mp.mpf(1)/3*dot(u1, u1)*dot(u2, u2) - (dot(u1, u2)**2 - mp.mpf(1)/3)) < mp.mpf(10)**-30
check("A3: point-mass stress tensors: T1.T2 - c T1 T2 = m1 m2 ((u1.u2)^2 - c) at five random velocity pairs (40 digits)", ok_tf)

# --- Planck 2018 backgrounds (ports of dark-tests/cosmo.py, verify-dark-tests-derivation/v3_cosmo.py, critic3/c1)
PL_AGE, PL_AGE_S, PL_ZEQ, PL_ZEQ_S = 13.797, 0.023, 3402.0, 26.0   # Planck 2018 Table 2, TT,TE,EE+lowE+lensing [S]
age_dt = BG_DT.age_gyr(); zeq_dt = DT_Om/DT_Orad - 1
aa_ = np.logspace(-9, 0, 200001)
age_vdd = np.trapezoid(1/(aa_*100*VDD_h*np.sqrt(vdd_E2(aa_))), aa_)*(3.0857e19/3.15576e16)
check("A4: Planck 2018 LCDM (TT,TE,EE+lowE+lensing): the dark-tests background (massless neutrinos) gives age 13.795 Gyr "
      "(published 13.797 +- 0.023) and z_eq = 3419 (3402 +- 26, within 1 sigma); the derivation verifier's (one massive "
      "neutrino) gives 13.797 Gyr", abs(age_dt - PL_AGE) < 0.1*PL_AGE_S and round(age_dt, 3) == 13.795 and
      abs(zeq_dt - PL_ZEQ) < PL_ZEQ_S and round(age_vdd, 3) == 13.797, f"{age_dt:.4f}, {zeq_dt:.1f}; {age_vdd:.4f}")
age_c1 = BG_C1.age_gyr()
check("A4: Planck 2018 + BAO column (the Lyman-alpha background, h = 0.6766, omega_c = 0.11933, omega_b = 0.02242, "
      "massless neutrinos): age 13.80 Gyr, within 1 sigma of the published 13.787 +- 0.020 (dagger)",
      abs(age_c1 - 13.787) < 0.020, f"{age_c1:.4f} Gyr")
check("A4: sigma8 normalization of the EH98 no-wiggle P(k) returns 0.8111 (regression: normalization, not an anchor)",
      round(sigma_R(8.0/DT_h), 4) == 0.8111, f"{sigma_R(8.0/DT_h):.5f}")

# --- exact growing modes the integrators must reproduce
BG_MR = BG(70.0, 0.3, 0.3/3000.0, 0.0, 1.0, 0.0, 0.0)          # matter + radiation, no Lambda, a_eq = 1/3000
lna_m, D_m, _ = solve_growth(BG_MR, a_i=1e-6, a_f=1.0, n=30000)
mesz = np.max(np.abs(D_m/(1 + 1.5*np.exp(lna_m)*3000.0) - 1))
check("A5: Meszaros (matter + smooth radiation): D = 1 + 3a/(2 a_eq) is exact; the cosmo.py integrator holds it to 1e-9 "
      "from a = 1e-6 to 1", mesz < 1e-9, f"max deviation {mesz:.1e}")
# --- the gate's Fourier kernel in closed form (independent of the quadratures)
C1_TAB = np.array([c1_kernels(exp(l)) for l in C1_LY[:C1_NUSE]])
dR = [abs(c1_kernels(y_)[0] - _R_gauss(y_)) for y_ in (0.3, 1.0, 1.08, 3.0)]
check("A6: gate kernel R(y) = y Int_0^inf sin(yt) e^(-t^2/2) dt = sqrt(pi/2) y e^(-y^2/2) erfi(y/sqrt2) (closed form): the "
      "critic's quadrature matches it at y = 0.3, 1, 1.08, 3 to 1e-8, inside the 6 decimals its kernels are quoted to",
      max(dR) < 1e-8, ", ".join(f"{d_:.1e}" for d_ in dR))
CN_TAB = {"R": np.array([_R_gauss(y_) for y_ in CN_YG])}       # the corner's kernel tables (linear_corner.py)
_kn = np.array([cn_kernels(y_) for y_ in CN_YG])
CN_TAB.update(Rv=_kn[:, 0], Ra=_kn[:, 1], yJ=CN_YG*_kn[:, 2])
stamp()
eds_c1 = c1_grow([1.0], 120.0, [("lcdm", [0.0])], bg=BG_EDS, a_end=1.0, a_i=1e-6, nstep=4000)[0][0][0, 0]
eds_exact = 0.6*(1/1e-6) + 0.4*(1/1e-6)**-1.5              # delta = 1, theta = 0 at a_i: (3/5) a/a_i + (2/5)(a/a_i)^-3/2
eds_cn = cn_grow([1.0], [(0.0, 10.0, "K4")], [0.0], bg=BG_EDS)[0.0][0, 0]
check("A5: Einstein-de Sitter: from delta = 1, delta' = 0 at a_i the exact solution is (3/5)(a/a_i) + (2/5)(a/a_i)^(-3/2); "
      "both growth integrators (critic's and corner's) reproduce it at a = 1 to 1e-8",
      close(eds_c1, eds_exact, 1e-8) and close(eds_cn, 0.6/1e-5 + 0.4*(1e5)**-1.5, 1e-8),
      f"{eds_c1/eds_exact - 1:.1e}, {eds_cn/(0.6e5) - 1:.1e}")


# --- Lee et al. 2020 (thesis Table 11.4; lambda in mm; +alpha95, |alpha95|), as typed in verify/phase_space_diameter.py
TAB_LEE = [(0.025, 7.9, 6.4), (0.028, 4.51, 3.73), (0.032, 2.56, 2.08), (0.035, 1.77, 1.45), (0.040, 1.06, 0.877),
           (0.045, 0.699, 0.585), (0.050, 0.494, 0.419), (0.056, 0.35, 0.3), (0.063, 0.251, 0.218),
           (0.071, 0.183, 0.162), (0.079, 0.14, 0.126), (0.089, 0.106, 0.097), (0.100, 0.0813, 0.0766)]
def crossing(col, target):
    for (l1_, *a1), (l2_, *a2) in zip(TAB_LEE, TAB_LEE[1:]):
        y1, y2 = a1[col], a2[col]
        if (y1 - target)*(y2 - target) <= 0:
            tt = log(y1/target)/log(y1/y2)
            return exp(log(l1_) + tt*log(l2_/l1_))*1e-3
check("A7: the range interpolation reproduces Lee et al. 2020's published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3)",
      round(crossing(1, 1.0)*1e6, 1) == 38.6 and round(crossing(1, 8/3)*1e6) == 30,
      f"{crossing(1, 1.0)*1e6:.2f}, {crossing(1, 8/3)*1e6:.2f} um")

# --- Mercury's GR perihelion advance from the typed-in orbit (NASA Planetary Fact Sheet, as in vot_bounds_lib.py)
GMSUN_KM = 132712440041.94                                 # km^3/s^2 (DE430)
RAD2MAS = 180/pi*3600e3
merc_gr = 6*pi*GMSUN_KM/(C_KMS**2*57.9e6*(1 - 0.206**2))*36525/88.0*RAD2MAS/1e3
check("A8: GR perihelion advance of Mercury 6 pi G M/(c^2 a (1 - e^2)) per orbit from the fact-sheet a, e, P: 43.0 "
      "arcsec/cy (textbook 42.98)", abs(merc_gr - 42.98) < 0.1, f"{merc_gr:.3f} arcsec/cy")

# --- Plummer sphere (G = M = a = 1): rho0 = 3/(4 pi), central free-fall time 1/sqrt(4 pi G rho0) = 1/sqrt3
check("A9: Plummer sphere in N-body units: central free-fall time 1/sqrt(4 pi G rho0) = 1/sqrt3 = 0.5774",
      abs(1/sqrt(4*pi*3/(4*pi)) - 1/sqrt(3)) < 1e-15 and round(1/sqrt(3), 4) == 0.5774)
stamp()


# ======================================================================================================
print("\n== B. X between ordinary bodies (ports of verify/phase_space_diameter.py's range, "
      "verify-program-derivation/v1_spin2_fokker.py, critic3/c4_numbers.py (d), verify-critic-theory/v4_force_dual.py)")
# ======================================================================================================
L_X = Gs*m1s*m2s*4*sp.pi*als*(F1*YM - hess_contract(ZM))
L_X_form = (als*Gs*m1s*m2s*sp.exp(-Ms*rr)/rr*(1 + (v1s + v2s) - sp.Rational(5, 2)*v12 - sp.Rational(1, 2)*nv1*nv2)
            - als*Gs*m1s*m2s*Ms/2*sp.exp(-Ms*rr)*nv1*nv2)
check("B0: X (massive spin 2, Fierz-Pauli) at O(v^2): alpha G m1 m2 e^(-Mr)/r [1 + v1^2 + v2^2 - 5/2 v1.v2 - 1/2 (n.v1)(n.v2)] "
      "- (alpha G m1 m2 M/2) e^(-Mr)(n.v1)(n.v2): a Yukawa with relativistic O(v^2/c^2) terms, no gate",
      sp.simplify(sp.expand(L_X - L_X_form)) == 0)
uq = sp.symbols('u', positive=True)
LAM_X = crossing(0, 4/3)
lam_u = {u_: crossing(0, 4/3*u_**2) for u_ in (0.5, 1.5)}
check("B0: V = -(G m1 m2/r)(1 + alpha e^(-r/lambda_X)), alpha = 4u^2/3 = 4/3 at the aligned vacuum u = 1: unscreened "
      "lambda_X < 37.7 um, M_X c^2 > 5.2 meV (recomputed here; also gated in verify/phase_space_diameter.py); 57.0 um at "
      "u = 0.5, 30.8 um at u = 1.5", round(LAM_X*1e6, 1) == 37.7 and round(HBARC_EVM/LAM_X*1e3, 1) == 5.2 and
      round(lam_u[0.5]*1e6, 1) == 57.0 and round(lam_u[1.5]*1e6, 1) == 30.8,
      f"{LAM_X*1e6:.2f} um, {HBARC_EVM/LAM_X*1e3:.3f} meV; {lam_u[0.5]*1e6:.2f}, {lam_u[1.5]*1e6:.2f} um")
b2_120 = (120.0/C_KMS)**2; g2_120 = 1/(1 - b2_120)
fX, fgr = (3*g2_120 - 1)/2 - 1, 2*g2_120 - 1 - 1
check("B1: X's velocity factor (3 gamma^2 - 1)/2 - 1 = 2.40e-7 at 120 km/s; graviton 2 gamma^2 - 1 - 1 = 3.20e-7 "
      "(critic: 2.403e-07, 3.204e-07)", r4(fX) == 2.403e-7 and r4(fgr) == 3.204e-7 and r2(fX) == 2.4e-7 and
      r2(fgr) == 3.2e-7, f"{fX:.4e}, {fgr:.4e}")
gv1, gv2 = sp.symbols('g1 g2', positive=True)
check("B1: both factors grow monotonically with relative velocity (d/dgamma > 0 for gamma > 1): no velocity gate at "
      "any range", all(sp.diff(f_, gq).subs(gq, 1 + sp.Symbol('d', positive=True)).is_positive
                       for f_ in (N_fp, N_dd)))
dv = va - vb
urel = series2(gam1*gam2*(1 - v12)) - (1 + (dv.T*dv)[0]/2)
check("B1: u1.u2 = gamma_rel = 1 + |v1 - v2|^2/2 + O(v^4): the factor depends on the relative velocity",
      sp.simplify(urel) == 0)

# #13's dual kinematics (verify-critic-theory/v4_force_dual.py): F/c~, c~ = c^4/G
mp.mp.dps = 200
Gm = mp.mpf('6.67430e-11'); cm_ = mp.mpf(299792458)
GMs_, GMe_, au_ = mp.mpf('1.32712440018e20'), mp.mpf('3.986004418e14'), mp.mpf('1.495978707e11')
ct = cm_**4/Gm
F_se = GMs_*GMe_/(Gm*au_**2); xF = F_se/ct
gt1 = 1/mp.sqrt(1 - xF**2) - 1
v_E = mp.sqrt((GMs_ + GMe_)/au_)
siegel = v_E*F_se/(cm_**5/Gm)
check("B2: #13's dual kinematics, Sun-Earth: F/c~ = 2.93e-22, gamma~ - 1 = 4.28e-44 (the answer's '(F/c~)^2 ~ 4e-44'; "
      "(F/c~)^2 itself is 8.56e-44 = 2(gamma~ - 1)), or zero if free fall is dual rest (#13 sec. 5)",
      r3(float(xF)) == 2.93e-22 and r3(float(gt1)) == 4.28e-44 and r3(float(xF**2)) == 8.56e-44,
      f"F/c~ = {mp.nstr(xF, 5)}, gamma~-1 = {mp.nstr(gt1, 5)}")
check("B2: Siegel reading (flag 39): the X-linear term sits in the mixed blocks with size X (v/c)(F/c~) = vF/(c^5/G) "
      "= 2.91e-26 ~ 3e-26 for Sun-Earth", r3(float(siegel)) == 2.91e-26,
      f"{mp.nstr(siegel, 5)}")
xs_ = sp.symbols('x11 x12 x22 y11 y12 y22', real=True)
Xm = sp.Matrix([[xs_[0], xs_[1]], [xs_[1], xs_[2]]]); Ym = sp.Matrix([[xs_[3], xs_[4]], [xs_[4], xs_[5]]])
Yi = Ym.inv()
Hs = sp.Matrix(sp.BlockMatrix([[Ym + epss**2*Xm*Yi*Xm, -epss*Xm*Yi], [-epss*Yi*Xm, Yi]]))
Om4 = sp.Matrix(sp.BlockMatrix([[sp.zeros(2), sp.eye(2)], [-sp.eye(2), sp.zeros(2)]]))
lin = Hs.applyfunc(lambda e_: sp.diff(e_, epss).subs(epss, 0))
check("B2: Siegel generalized metric (d = 2): symplectic, det 1, and its part linear in X lies only in the mixed blocks",
      sp.simplify(Hs.T*Om4*Hs - Om4) == sp.zeros(4) and sp.simplify(Hs.det()) == 1 and
      sp.simplify(lin[:2, :2]) == sp.zeros(2) and sp.simplify(lin[2:, 2:]) == sp.zeros(2))
mp.mp.dps = 15
stamp()


# ======================================================================================================
print("\n== C. A universal relative-velocity gate between ordinary bodies (ports of verify-ordinary-tests-numbers/"
      "vot_bounds_lib.py, vot_bounds.py, vot_topend.py; critic3/c4_numbers.py (e, g); verify-critic-numbers/u4)")
# ======================================================================================================
# V = -(G m1 m2/r)[1 + eps W(|v1 - v2|/v_a)], W = exp(-u^2) or 1/(1 + u^2) in the ordinary-tests convention.
# Inputs as typed in by the ordinary-tests numbers verifier [S]: DE430 GM_sun, GM_EM, GM_E (LLR), SLR GM_E (Ries
# 1992, Dunn 1999); planets: NASA Planetary Fact Sheet (2025); supplementary perihelion precessions: Pitjev &
# Pitjeva 2013 Table 5; LLR perigee 270 muas/yr (Adelberger, Heckel, Nelson 2003); double pulsar: Kramer et al.
# 2021; Cassini gamma - 1 = (2.1 +- 2.3)e-5; Eros (Yeomans et al. 1999); Talmadge et al. 1988 via Will 1998.
vstar_s, va_s, vv_s = sp.symbols('v_star v_a v', positive=True)
sol_va = sp.solve(sp.Eq(-vv_s**2/va_s**2, -vv_s**2/(2*vstar_s**2)), va_s)
check("C0: exp(-v^2/v_a^2) equals the record's amplitude gate exp(-v^2/(2 v*^2)) iff v_a = sqrt2 v*: v_a = 169.7 km/s at "
      "v* = 120; the scan v_a = 0.3-3000 km/s is v* = 0.21-2121 km/s ('0.2-2100' in the record's convention)",
      sol_va == [sp.sqrt(2)*vstar_s] and round(sqrt(2)*120, 1) == 169.7 and round(0.3/sqrt(2), 2) == 0.21 and
      round(3000/sqrt(2)) == 2121)
GMEM = 403503.2355
PLANETS = {'Mercury': (57.9, 0.206, 88.0, -2.0, 3.0), 'Venus': (108.2, 0.007, 224.7, 2.6, 1.6),
           'Earth': (149.6, 0.017, 365.2, 0.19, 0.19), 'Mars': (228.0, 0.094, 687.0, -0.020, 0.037),
           'Jupiter': (778.5, 0.049, 4331., 58.7, 28.3), 'Saturn': (1432.0, 0.052, 10747., -0.32, 0.47)}
MOON_A, MOON_E = 384400., 0.0549
V_LAG = sqrt(398600.4356/12270.)
def gate_shapes(name):
    if name == 'gauss':
        W = lambda u: np.exp(-u**2); dW = lambda u: -2*u*np.exp(-u**2)
    else:
        W = lambda u: 1/(1 + u**2); dW = lambda u: -2*u/(1 + u**2)**2
    return W, dW, (lambda u: W(u) - u*dW(u))
EGRID = np.arange(4096)*2*np.pi/4096
_cE = np.cos(EGRID)
def adv_per_orbit(dW, uc, e):
    """first-order apsidal advance per orbit per unit eps: 2 pi sqrt(1 - e^2)/e dPhi/de, Phi(e) = <W(uc s)>_E"""
    s = np.sqrt((1 + e*_cE)/(1 - e*_cE))
    dsde = _cE/(s*(1 - e*_cE)**2)
    return 2*np.pi*np.sqrt(1 - e**2)/e*np.mean(dW(uc*s)*uc*dsde)
def two_sided(x, sig):
    return max(abs(x - 2*sig), abs(x + 2*sig))
PB_DP = 0.1022515592973*86400.; E_DP = 0.087777023; GM_DP = 2.587052*GMSUN_KM
A_DP = (GM_DP*PB_DP**2/(4*np.pi**2))**(1/3); V_DP = sqrt(GM_DP/A_DP)
OMDOT_DP = 16.899323
DGR_DP = np.radians(OMDOT_DP)*PB_DP/(365.25*86400)
mA_, mB_ = 1.338185, 1.248868; M_ = mA_ + mB_
dlnM = 1.5; dlnmB = 2/3*dlnM; dlnmA = (M_*dlnM - mB_*dlnmB)/mA_
FAC_S = dlnmA + dlnmB - dlnM/3
DP_LIMIT = 1.3e-4/FAC_S
def bounds(vstar, shape, dp_limit=None):
    dp_limit = DP_LIMIT if dp_limit is None else dp_limit
    W, dW, K = gate_shapes(shape)
    out = {}
    with np.errstate(divide='ignore', over='ignore'):
        for nm, (a6, e, P, x, sg) in PLANETS.items():
            uc = sqrt(GMSUN_KM/(a6*1e6))/vstar
            sig = adv_per_orbit(dW, uc, e)*36525/P*RAD2MAS
            out['prec ' + nm] = two_sided(x, sg)/abs(sig) if sig != 0 else np.inf
        vM = sqrt(GMEM/MOON_A); PM = 2*np.pi*sqrt(MOON_A**3/GMEM)/86400
        sigM = adv_per_orbit(dW, vM/vstar, MOON_E)*365.25/PM*RAD2MAS*1e3
        out['LLR perigee'] = 270./abs(sigM)
        dK = K(vM/vstar) - K(V_LAG/vstar)
        for lab, gslr, sslr in [('Ries', 398600.4356, 0.0004), ('Dunn', 398600.4360, 0.0002)]:
            out['GM_E LLR-SLR ' + lab] = two_sided((398600.4354 - gslr)/gslr, np.hypot(0.0005, sslr)/gslr)/abs(dK) \
                if dK != 0 else np.inf
        sdp = adv_per_orbit(dW, V_DP/vstar, E_DP)/DGR_DP
        out['double pulsar'] = dp_limit/abs(sdp)
        uE = sqrt(GMSUN_KM/149.6e6)/vstar
        out['Cassini'] = (2.1 + 4.6)/2*1e-5/K(uE)
        vorb = sqrt(6.674e-20*6.687e15/35.)
        out['Eros'] = two_sided(7.2/6.687 - 1, 1.8/6.687)/abs(W(0.965/vstar) - K(vorb/vstar))
        for nm, b_ in [('Mercury', 1.4e-8), ('Venus', 1.5e-9), ('Mars', 6.5e-10), ('Jupiter', 6e-8)]:
            up = sqrt(GMSUN_KM/(PLANETS[nm][0]*1e6))/vstar
            d_ = (K(up) - K(uE))/3
            out['Kepler ' + nm + '/Earth'] = b_/abs(d_) if d_ != 0 else np.inf
    return out
check("C1: double-pulsar mass-bias factor (masses from omega-dot and Shapiro s, Kramer et al. 2021 sec. VI.2.1) 2.4666, "
      "so |d omega-dot/omega-dot| < 5.27e-5 from their 1.3e-4", round(FAC_S, 4) == 2.4666 and r3(DP_LIMIT) == 5.27e-5,
      f"{FAC_S:.4f}, {DP_LIMIT:.3e}")
b120 = bounds(120., 'gauss'); b170 = bounds(170., 'gauss'); b170L = bounds(170., 'lorentz')
best = lambda b_: min(b_, key=b_.get)
check("C2: at v_a = 120 km/s Mars's perihelion binds: 1.82e-11 (Earth 4.04e-11, Mercury 6.37e-11)",
      best(b120) == 'prec Mars' and r3(b120['prec Mars']) == 1.82e-11 and r3(b120['prec Earth']) == 4.04e-11 and
      r3(b120['prec Mercury']) == 6.37e-11, f"{b120['prec Mars']:.3e}")
MAS = pi/(180*3600*1000)
sig_merc = abs(adv_per_orbit(gate_shapes('gauss')[1], sqrt(GMSUN_KM/57.9e6)/120., 0.206))
inpop = [lim_*MAS/(36525/88.0)/sig_merc for lim_ in (3.1, 2.075)]   # INPOP15a, 1 sigma, as typed in by n6 (record)
check("C2: the interim's '2e-11 from Mercury' is INPOP15a's 1-sigma anomalous advance (3.1 mas/cy, criterion 1; "
      "2.075 mas/cy, mean) at v_a = 120 km/s: eps < 2.5e-11 and 1.7e-11, in the ordinary-tests convention "
      "(verify-program-numbers/n6_mercury_bound.py)", [r2(x_) for x_ in inpop] == [2.5e-11, 1.7e-11],
      ", ".join(f"{x_:.3e}" for x_ in inpop))
check("C2: at the record's v* = 120 km/s (v_a = 170): |eps| < 3.5e-11 from Mars's perihelion (Gaussian; Lorentzian "
      "3.64e-11)", best(b170) == 'prec Mars' and r2(b170['prec Mars']) == 3.5e-11 and r3(b170L['prec Mars']) == 3.64e-11,
      f"{b170['prec Mars']:.3e}, {b170L['prec Mars']:.3e}")
vgrid = np.logspace(np.log10(0.1), np.log10(3000.), 1201)
env = {}
for shape in ('gauss', 'lorentz'):
    bs = []; who = []
    for vs_ in vgrid:
        b_ = bounds(vs_, shape); k_ = best(b_); bs.append(b_[k_]); who.append(k_)
    env[shape] = (np.array(bs), who)
eg_, wg_ = env['gauss']; el_, wl_ = env['lorentz']
mg03 = vgrid >= 0.3
ig = int(np.argmax(np.where(mg03, eg_, -np.inf))); il = int(np.argmax(el_))
check("C3: Gaussian gate, envelope over v_a = 0.3-3000 km/s: |eps| < 8.65e-9 ('8.7e-9'), weakest at the 3000 km/s end, "
      "set by the double pulsar", r3(eg_[mg03].max()) == 8.65e-9 and r2(eg_[mg03].max()) == 8.7e-9 and
      wg_[ig] == 'double pulsar' and vgrid[ig] > 2999, f"{eg_[mg03].max():.3e} at {vgrid[ig]:.0f} km/s ({wg_[ig]})")
check("C3: Lorentzian gate, envelope over v_a = 0.1-3000 km/s: |eps| < 9.42e-9 ('9.4e-9'), double pulsar at 3000 km/s",
      r3(el_.max()) == 9.42e-9 and wl_[il] == 'double pulsar' and vgrid[il] > 2999, f"{el_.max():.3e} ({wl_[il]})")
W_, dW_, _ = gate_shapes('gauss')
a6, e6, P6 = PLANETS['Mercury'][:3]
lead = adv_per_orbit(dW_, sqrt(GMSUN_KM/(a6*1e6))/30000., e6)/(6*np.pi*GMSUN_KM/(C_KMS**2*a6*1e6*(1 - e6**2)))
check("C3: leading order u -> 0: d omega-dot/omega-dot_GR = -(2/3)(c/v_a)^2 eps (Mercury at v_a = 30000 km/s: -66.574), "
      "so the double-pulsar limit gives 5.27e-5 (3/2)(v_a/c)^2 = 7.92e-9 at 3000 km/s (critic c4 (e))",
      round(lead, 3) == -66.574 and round(-2/3*(C_KMS/30000)**2, 3) == -66.574 and
      r3(5.27e-5*1.5*(3000/C_KMS)**2) == 7.92e-9, f"{lead:.4f}")
lowg = eg_[(vgrid >= 0.1) & (vgrid <= 0.3)]
i_lo = int(np.argmax(np.where((vgrid >= 0.1) & (vgrid <= 0.3), eg_, -np.inf)))
check("C4: below v_a ~ 0.3 km/s there is no numerical bound: the Gaussian envelope's weakest point on 0.1-0.3 km/s is "
      "eps < 0.615 (Eros)", r3(lowg.max()) == 0.615 and wg_[i_lo] == 'Eros', f"{lowg.max():.3f} at {vgrid[i_lo]:.3f} km/s")
GM_EARTH, R_POLE = 3.986004418e14, 6356752.3               # dagger, standard values (u4)
check("C4: qualitative exclusion there: a body at rest at the pole has inertia m(1 - 2 G M eps/(R v_a^2)), which "
      "vanishes at eps = 7.97e-5 for v_a = 0.1 km/s", r3(R_POLE*100.0**2/(2*GM_EARTH)) == 7.97e-5,
      f"{R_POLE*100.0**2/(2*GM_EARTH):.4e}")
stamp()


# ======================================================================================================
print("\n== D. The obituary's scope: Debt 3a's shortfall (ports of review/wiki-build-checks/debt3a_check.py and "
      "verify-clumping-numbers/v09_units.py)")
# ======================================================================================================
# debt3a_check.py, inputs exactly as Debt 3a states them (natural units, GeV)
cm_g = 5.0677e13; g_gev = 5.6096e23; c3a = 2.99792458e5
m3a = 0.070; vst3a = 120/c3a
S3a = 30*cm_g**2/g_gev
g3a = sqrt(pi*S3a/m3a)
ratio3a = {}
for name, rho_, sig_ in (("dwarf core", 1.0, 30), ("MW local", 0.4, 155)):
    rho = rho_/cm_g**3; sg = sig_/c3a; n_ = rho/m3a
    neff, s2 = (n_, sg**2) if sg < vst3a else (n_*(vst3a/sg)**3/(2*pi)**1.5, vst3a**2)
    ratio3a[name] = g3a*neff/(m3a*s2)
check("D1: Debt 3a's record logic (debt3a_check.py, the critic's run c3): g = 2.48e3 GeV^-2; the contact gate's "
      "collective pull over m min(sigma, v*)^2 is 3.9e-28 (dwarf core) and 2.9e-31 (MW)",
      r3(g3a) == 2.48e3 and r2(ratio3a["dwarf core"]) == 3.9e-28 and r2(ratio3a["MW local"]) == 2.9e-31,
      f"{g3a:.4g}; {ratio3a['dwarf core']:.4e}, {ratio3a['MW local']:.4e}")
check("D1: so the pull is 10^-27.4 (dwarf core) to 10^-30.5 (MW) of threshold ('falls short by 10^28-10^31' quotes the "
      "ratios' printed exponents e-28 and e-31; the shortfall factors are 2.6e27 and 3.5e30)",
      floor(log10(ratio3a["dwarf core"])) == -28 and floor(log10(ratio3a["MW local"])) == -31 and
      r2(1/ratio3a["dwarf core"]) == 2.6e27 and r2(1/ratio3a["MW local"]) == 3.5e30,
      f"log10 = {log10(ratio3a['dwarf core']):.2f}, {log10(ratio3a['MW local']):.2f}")
# v09_units.py (CODATA), linearized criterion g n Lambda_g(r) >= m sigma^2, r = sigma/v*
def lam_g(r):
    """top eigenvalue of the Gaussian-gate operator on a Maxwellian (clumping C3; Mehler algebra)"""
    return (0.5 + r*r + np.sqrt(1 + 4*r*r)/2)**-1.5
hbarc_gevm = 1.973269804e-16
m_g09 = 0.07*GEV_KG*1e3
g09 = sqrt(pi*(30.0*m_g09/(hbarc_gevm*100)**2)/0.07**2)
cm3 = (hbarc_gevm*100)**3
lin = {}; r3a = {}
for name, rho_, sig_ in (("dwarf", 1.0, 30.0), ("MW", 0.4, 155.0)):
    n_ = rho_/0.07
    lin[name] = g09*n_*cm3*lam_g(sig_/120.0)/(0.07*(sig_*1e3/C)**2)
    ngate = n_*min(1.0, (120.0/sig_)**3/(2*pi)**1.5) if sig_ > 120.0 else n_
    r3a[name] = g09*ngate*cm3/(0.07*min(sig_*1e3/C, 120e3/C)**2)
check("D2: linearized (clumping C6, CODATA): g n Lambda_g(sigma/v*)/(m sigma^2) = 3.27e-28 (dwarf core), 8.7e-31 (MW)",
      r3(lin["dwarf"]) == 3.27e-28 and r2(lin["MW"]) == 8.7e-31, f"{lin['dwarf']:.4e}, {lin['MW']:.4e}")
over = lin["MW"]/r3a["MW"]
check("D3 (flag 58): for a gate narrower than the dispersion the linearized criterion is g n Lambda_g >= m sigma^2; "
      "3a's form g n (v*/sigma)^3 (2 pi)^(-3/2) >= m v*^2 overstates the MW shortfall by (2 pi)^(3/2) r Lambda_g(r) "
      "= 3.04 ('about 3x') at r = 155/120; the verdict is unchanged",
      round(over, 2) == 3.04 and round((2*pi)**1.5*(155/120)*lam_g(155/120), 2) == 3.04 and lin["MW"] < 1e-29,
      f"{over:.4f}")
stamp()


# ======================================================================================================
print("\n== E. The long-range chi-only gated attraction U = -eps G m^2 W(|v - v'|/v*)/r (ports of critic3/"
      "c1_hamiltonian_system.py, critic3/c4_numbers.py (c), dark-tests/r_gate.py, verify-dark-tests-derivation/"
      "v3_misc.py, verify-critic-numbers/u7_sgr_bound.py)")
# ======================================================================================================
kk108 = c1_kernels(1.08)
R_, R1_, J_, Rv_, B_ = kk108
mu_, wmu_ = np.polynomial.legendre.leggauss(64); mu_ = 0.5*(mu_ + 1); wmu_ = 0.5*wmu_
Rmu = np.array([c1_kernels(1.08*m_)[0] for m_ in mu_])
ids = (abs(R1_ - 1.08*J_ - R_), abs(Rv_ - B_ + 3*1.08*J_), abs(R1_ - np.sum(wmu_*Rmu)), abs(Rv_ - 3*np.sum(wmu_*mu_**2*Rmu)))
check("E1: kernels at the DESI pivot y = 1.08, by quadrature of their definitions: R = 0.803130 (the round-2 agent's "
      "density kernel), R1 = 0.311446 (the force law's), 2.58x smaller; R_v = 0.536423, B = -0.938630",
      round(R_, 6) == 0.803130 and round(R1_, 6) == 0.311446 and round(R_/R1_, 2) == 2.58 and round(Rv_, 6) == 0.536423
      and round(B_, 6) == -0.938630, f"R {R_:.6f}, R1 {R1_:.6f}, J {J_:+.6f}, R_v {Rv_:.6f}, B {B_:+.6f}")
check("E1: kernel identities R1 - yJ = R, R_v - B = -3yJ, R1 = Int_0^1 R(y mu) dmu, R_v = 3 Int mu^2 R(y mu) dmu, to 1e-8",
      max(ids) < 1e-8, ", ".join(f"{x_:.1e}" for x_ in ids))
ap_ = 0.25
kp = 0.009*BG_C1.H0*float(BG_C1.E(ap_))*ap_
yp = kp*120/(ap_*BG_C1.H0*float(BG_C1.E(ap_)))
check("E1: pivot k = 0.009 s/km at z = 3 is 0.6898/Mpc; y_p = k_p v*/(aH) = 1.0800 at v* = 120 (the gate in velocity "
      "units is v* at every epoch)", round(kp, 4) == 0.6898 and round(yp, 4) == 1.0800, f"{kp:.5f}, {yp:.6f}")
i_minB = int(np.argmin(C1_TAB[:, 4]))
minB, y_minB = C1_TAB[i_minB, 4], exp(C1_LY[i_minB])

dl = 0.05
kk3 = kp*np.exp(np.array([-dl, 0.0, dl]))
EG1 = np.concatenate([[0.0], np.geomspace(1e-3, 1.0, 41)])
EG03 = np.concatenate([[0.0], np.geomspace(0.3e-3, 0.3, 41)])
c1_cases = [("lcdm", [0.0]), ("H", [0.1, 1.0]), ("F", [0.1, 1.0]), ("c4b", [0.1, 1.0]), ("agent", [0.1, 1.0]),
            ("H", EG1), ("F", EG1), ("c4b", EG1), ("agent", EG1), ("H", EG03)]
c1_res = c1_grow(kk3, 120.0, c1_cases)
m0_, b0_ = c1_res[0][0][:, 0], c1_res[0][1][:, 0]
def c1_resp(res):
    m_, b_ = res
    Tm2 = (m_/m0_[:, None])**2; Tb2 = (b_/b0_[:, None])**2
    return (Tm2[1], (np.log(Tm2[2]) - np.log(Tm2[0]))/(2*dl), Tb2[1], (np.log(Tb2[2]) - np.log(Tb2[0]))/(2*dl))
RESP = {s_: c1_resp(c1_res[i]) for i, s_ in ((1, "H"), (2, "F"), (3, "c4b"), (4, "agent"))}
for s_ in ("agent", "F", "H", "c4b"):
    r_ = RESP[s_]
    print(f"      {s_:5s}: eps = 0.1: T_m^2 = {r_[0][0]:.4f}, dn_m = {r_[1][0]:+.4f} | T_b^2 = {r_[2][0]:.4f}, "
          f"dn_b = {r_[3][0]:+.4f};  eps = 1: T_m^2 = {r_[0][1]:.4f}, dn_m = {r_[1][1]:+.4f}")
check("E2: DESI pivot, v* = 120 km/s, z = 3, eps = 0.1: record's reading (H) T_m^2 = 0.9478, dn = -0.0603 (a suppression); "
      "force law 1.0356, +0.0637; c4b's transcription 0.9862, +0.0048; round-2 agent's hybrid 1.0784, +0.1310",
      [round(RESP["H"][0][0], 4), round(RESP["H"][1][0], 4)] == [0.9478, -0.0603] and
      [round(RESP["F"][0][0], 4), round(RESP["F"][1][0], 4)] == [1.0356, 0.0637] and
      [round(RESP["c4b"][0][0], 4), round(RESP["c4b"][1][0], 4)] == [0.9862, 0.0048] and
      [round(RESP["agent"][0][0], 4), round(RESP["agent"][1][0], 4)] == [1.0784, 0.1310],
      f"H {RESP['H'][0][0]:.6f}")

# compressed Lyman-alpha likelihoods: DESI DR1 (Delta^2 = 0.379 +- 0.032, n = -2.309 +- 0.019, r = -0.1738) and
# eBOSS (0.310 +- 0.020, -2.340 +- 0.006, r = 0.512), around the Planck prediction 0.3495, -2.3052 (errors 0.0083,
# 0.0032) [S by the round-3 dark-tests verifiers]
D0_PL, N0_PL = 0.3495, -2.3052
def make_chi2(d, sD, sn, rho, base_err):
    Cm = np.array([[sD**2 + base_err[0]**2, rho*sD*sn], [rho*sD*sn, sn**2 + base_err[1]**2]])
    Ci = np.linalg.inv(Cm)
    def chi2(T2, dn):
        v_ = np.array([D0_PL*T2 - d[0], N0_PL + dn - d[1]])
        return np.einsum("i...,ij,j...->...", v_, Ci, v_)
    return chi2
DESI_B = make_chi2((0.379, -2.309), 0.032, 0.019, -0.1738, (0.0083, 0.0032))
DESI_0 = make_chi2((0.379, -2.309), 0.032, 0.019, -0.1738, (0.0, 0.0))
EBOSS = make_chi2((0.310, -2.340), 0.020, 0.006, 0.512, (0.0083, 0.0032))
def c1_bound(resp, eg, chi2, emax):
    out = []
    for T2, dn in ((resp[0], resp[1]), (resp[2], resp[3])):
        ef = np.linspace(0, emax, 40001)
        c2_ = chi2(np.interp(ef, eg, T2), np.interp(ef, eg, dn))
        i0 = int(np.argmin(c2_)); ab = np.where((c2_ > c2_[i0] + 3.84) & (ef > ef[i0]))[0]
        out.append((ef[ab[0]] if len(ab) else np.inf, ef[i0], c2_[0], c2_[i0]))
    return out
BND = {s_: c1_bound(c1_resp(c1_res[5 + i]), EG1, DESI_B, 1.0) for i, s_ in enumerate(("H", "F", "c4b", "agent"))}
BND0_c4b = c1_bound(c1_resp(c1_res[7]), EG1, DESI_0, 1.0)
LYA_H_M, LYA_H_G = BND["H"][0][0], BND["H"][1][0]
LYA_F_M, LYA_F_G = BND["F"][0][0], BND["F"][1][0]
check("E3: compressed DESI DR1, v* = 120 km/s, delta chi^2 = 3.84 with baseline errors: record's reading eps < 0.0570 "
      "(matter ratio) / 0.1063 (gas ratio) -> 'eps < 0.06 to 0.11'", f"{LYA_H_M:.4f}" == "0.0570" and
      f"{LYA_H_G:.4f}" == "0.1063", f"{LYA_H_M:.5f} / {LYA_H_G:.5f}")
check("E3: force-law reading eps < 0.0585 / 0.1755 -> the bracket '0.06-0.18' (critic: 0.0585/0.176)",
      f"{LYA_F_M:.4f}" == "0.0585" and f"{LYA_F_G:.4f}" == "0.1755" and round(LYA_F_G, 3) == 0.176,
      f"{LYA_F_M:.5f} / {LYA_F_G:.5f}")
check("E3: the superseded numbers come from the flawed systems: the round-2 agent's hybrid gives 0.028 (matter; the "
      "interim's '0.03'); c4b's system gives 0.358/0.305 with baseline errors, 0.354/0.299 with DESI errors only "
      "(c4b printed 0.3405/0.2959: the '0.34' that counted -H A_delta twice)",
      round(BND["agent"][0][0], 3) == 0.028 and round(BND["c4b"][0][0], 3) == 0.358 and round(BND["c4b"][1][0], 3) == 0.305
      and round(BND0_c4b[0][0], 3) == 0.354 and round(BND0_c4b[1][0], 3) == 0.299 and close(BND0_c4b[0][0], 0.3405, 0.05),
      f"agent {BND['agent'][0][0]:.4f}; c4b {BND['c4b'][0][0]:.4f}/{BND['c4b'][1][0]:.4f}, "
      f"DESI-only {BND0_c4b[0][0]:.4f}/{BND0_c4b[1][0]:.4f}")
dmax = max(abs(LYA_H_M/0.0572 - 1), abs(LYA_H_G/0.1069 - 1), abs(LYA_F_M/0.0585 - 1), abs(LYA_F_G/0.1760 - 1))
check("E3 (record): the second, independent derivation (VDD v3_lya_withbase.out: H 0.0572/0.1069, force law "
      "0.0585/0.1760) and this port round alike to the quoted 0.06/0.11 (H) and 0.06/0.18 (force law)",
      [round(x_, 2) for x_ in (LYA_H_M, LYA_H_G, 0.0572, 0.1069)] == [0.06, 0.11, 0.06, 0.11] and
      [round(x_, 2) for x_ in (LYA_F_M, LYA_F_G, 0.0585, 0.1760)] == [0.06, 0.18, 0.06, 0.18],
      f"largest difference {dmax:.2%}")
EB = c1_bound(c1_resp(c1_res[9]), EG03, EBOSS, 0.3)[0]
check("E4: eBOSS compression in the record's reading: chi^2 falls from 26.31 (eps = 0) to 1.90 at eps = 0.0535 (upper "
      "bound 0.0741); delta chi^2 = 24.4, 4.94 'sigma' for one parameter (not evidence: the data sit 4.90 sigma from "
      "Planck [S, arXiv:2311.16377])", f"{EB[2]:.2f}" == "26.31" and f"{EB[3]:.2f}" == "1.90" and
      f"{EB[1]:.4f}" == "0.0535" and f"{EB[0]:.4f}" == "0.0741" and round(sqrt(EB[2] - EB[3]), 2) == 4.94,
      f"{EB[2]:.3f} -> {EB[3]:.3f} at {EB[1]:.5f}; bound {EB[0]:.5f}")
mm8 = c1_grow([kp], 120.0, [("lcdm", [0.0]), ("H", [0.1])], nstep=8000)
t8 = (mm8[1][0][0, 0]/mm8[0][0][0, 0])**2
t16 = (c1_res[1][0][1, 0]/m0_[1])**2
check("E4: step test: T_m^2(eps = 0.1, H) is 0.947755 with 8000 and 16000 RK4 steps", round(t8, 6) == round(t16, 6) == 0.947755,
      f"{t8:.7f}, {t16:.7f}")
OC50, OC3 = BG_DT.f_c*float(BG_DT.Omega_m_a(1/51)), BG_DT.f_c*float(BG_DT.Omega_m_a(1/4))
OC10_VDD, OC10_DT = float(vdd_Omc(1/11)), BG_DT.f_c*float(BG_DT.Omega_m_a(1/11))
eps_sing = [2/(-minB)/oc for oc in (round(OC50, 4), round(OC10_VDD, 3), round(OC3, 4))]
check("E5: the record's reading becomes singular where 1 + kappa B = 0: min B = -1.0712 at y = 1.41, so eps = "
      "2/(1.0712 Omega_c) = 2.248 (z = 50, Omega_c = 0.8305), 2.236 (z = 10, 0.835), 2.293 (z = 3, 0.8143): linear theory "
      "fails above eps ~ 2.2", round(minB, 4) == -1.0712 and round(y_minB, 2) == 1.41 and
      [round(e_, 3) for e_ in eps_sing] == [2.248, 2.236, 2.293] and
      [round(OC50, 4), round(OC10_VDD, 3), round(OC3, 4)] == [0.8305, 0.835, 0.8143],
      f"{minB:.5f} at y = {y_minB:.3f}; Omega_c(10) on the dark-tests background {OC10_DT:.4f} gives {2/(-minB)/OC10_DT:.3f}")
# dark-tests/r_gate.py on BG_DT
rg0 = 120.0/BG_DT.H0
zz_ = np.linspace(0.0, 3.0, 30001); aH_ = BG_DT.Hz(zz_)/(1 + zz_); i_ = int(np.argmin(aH_))
check("E6: Hubble gate radius r_gate = v*/H0 = 1.781 Mpc for v* = 120 km/s (proper, today); the comoving gate radius "
      "peaks at 2.028 Mpc at z = 0.631, where the expansion turns from deceleration to acceleration "
      "((2 Omega_L/Omega_m)^(1/3) - 1 = 0.631)", round(rg0, 3) == 1.781 and round(120/aH_[i_], 3) == 2.028 and
      round(zz_[i_], 3) == 0.631 and round((2*BG_DT.OL/BG_DT.Om)**(1/3) - 1, 3) == 0.631,
      f"{rg0*1e3:.3f} kpc; {120/aH_[i_]:.4f} Mpc at z = {zz_[i_]:.3f}")

# Sagittarius: the gate averaged over a Maxwellian host, <W> = (v*^2/S^2)^(3/2) exp(-V^2/(2 S^2)), S^2 = v*^2 + s^2
def gate_avg(V, s_, vs_=120.0):
    S2 = vs_**2 + s_**2
    return (vs_**2/S2)**1.5*np.exp(-V**2/(2*S2))
xq = np.linspace(317.6 - 12*120, 317.6 + 12*120, 200001); yq = np.linspace(-12*120, 12*120, 200001)
px_ = np.exp(-(xq - 317.6)**2/(2*120**2))/sqrt(2*pi)/120; py_ = np.exp(-yq**2/(2*120**2))/sqrt(2*pi)/120
quad_gate = np.trapezoid(px_*np.exp(-xq**2/(2*120**2)), xq)*np.trapezoid(py_*np.exp(-yq**2/(2*120**2)), yq)**2
mc_ = []
for k_ in range(20):
    rng_ = np.random.default_rng(1000 + k_)
    u_ = rng_.normal(0.0, 120.0, size=(200000, 3)); u_[:, 0] += 317.6
    mc_.append(np.mean(np.exp(-np.sum(u_**2, axis=1)/(2*120.0**2))))
mc_ = np.array(mc_); mc_err = mc_.std(ddof=1)/sqrt(len(mc_))
# exact variance of W over the pair distribution: E[W^2] is the same Gaussian average with v*^2 -> v*^2/2
var_W = gate_avg(317.6, 120.0, 120.0/sqrt(2)) - gate_avg(317.6, 120.0)**2
pull_u7 = (0.0614977 - gate_avg(317.6, 120.0))/sqrt(var_W/(10*400000))
check("E7: gate average closed form (0.06136 at V = 317.6, sigma_rel = 120) against quadrature (1e-9) and a Monte "
      "Carlo of 20 independent runs of 2e5 pairs (pull < 3 sigma)", abs(quad_gate/gate_avg(317.6, 120.0) - 1) < 1e-9 and
      abs(mc_.mean() - gate_avg(317.6, 120.0)) < 3*mc_err and round(gate_avg(317.6, 120.0), 5) == 0.06136,
      f"MC {mc_.mean():.5f} +- {mc_err:.5f}")
check("E7 (record): u7's MC '0.06150 +- 0.00004' is 3.3 sigma from the closed form on its own 10-run error bar, but "
      "2.2 sigma on the exact variance (sigma of a 4e6-pair mean = 6.1e-5): its error bar came out low, the closed form "
      "stands", round(pull_u7, 1) == 2.2 and r2(sqrt(var_W/4e6)) == 6.1e-5, f"pull {pull_u7:.2f}")
del u_
# VDD v3_misc.py K13: inverse-mass shifts of the satellite's chi in the host's gated potential (Hamiltonian reading)
wS = gate_avg(311.1, np.hypot(149.9, 12.0)); S2_ = 120.0**2 + 149.9**2 + 12.0**2
etas = []
for rt in (200.0, 300.0):
    PhiN = 212.0**2*(1 + np.log(rt/18.11))                # truncated singular isothermal host (assumption)
    etas.append((PhiN*wS/S2_, -PhiN*wS*(311.1**2/S2_ - 1)/S2_))
check("E7: Sgr, force-law mapping: <W> = 0.0656 at V = 311.1 km/s, so KK's 10% gives eps < 1.52 (round 2's '1.5')",
      round(wS, 4) == 0.0656 and round(0.1/wS, 2) == 1.52, f"{wS:.5f}")
check("E7: Sgr, record's reading (VDD D14, order of magnitude): the satellite chi's inverse mass shifts by eta_perp = "
      "+0.27..+0.30 eps and eta_par = -0.44..-0.49 eps (host truncated at 200-300 kpc), so eps < 0.1/|eta| = 0.20-0.37",
      [round(e_[0], 3) for e_ in etas] == [0.271, 0.303] and [round(e_[1], 3) for e_ in etas] == [-0.438, -0.490] and
      round(0.1/abs(etas[1][1]), 2) == 0.20 and round(0.1/etas[0][0], 2) == 0.37,
      f"{etas[0][0]:+.4f} {etas[1][0]:+.4f}; {etas[0][1]:+.4f} {etas[1][1]:+.4f}")
# VCN u7_sgr_bound.py: three toy Milky-Way potentials (dagger), Sgr now (Vasiliev & Belokurov 2020 [S])
GK = 4.30091e-6; KMS_KPC_GYR = 1.0227
class MWModel:
    def __init__(self, Mb, ab, Md, ad, bd, rho_s, rs_, name):
        self.Mb, self.ab, self.Md, self.ad, self.bd, self.rho_s, self.rs, self.name = Mb, ab, Md, ad, bd, rho_s, rs_, name
    def acc(self, x):
        R2 = x[0]**2 + x[1]**2; r = sqrt(R2 + x[2]**2)
        a_ = -GK*self.Mb/(r*(r + self.ab)**2)*x
        zb = sqrt(x[2]**2 + self.bd**2)
        den = (R2 + (self.ad + zb)**2)**1.5
        ad_ = -GK*self.Md/den*np.array([x[0], x[1], x[2]*(self.ad + zb)/zb])
        Mh = 4*pi*self.rho_s*self.rs**3*(log(1 + r/self.rs) - r/(r + self.rs))
        return a_ + ad_ - GK*Mh/r**3*x
    def Menc_sph(self, r):
        Mh = 4*pi*self.rho_s*self.rs**3*(np.log(1 + r/self.rs) - r/(r + self.rs))
        return self.Mb*r**2/(r + self.ab)**2 + self.Md*r**3/(r**2 + (self.ad + self.bd)**2)**1.5 + Mh
    def vc(self, R):
        return sqrt(-self.acc(np.array([R, 0.0, 0.0]))[0]*R)
    def rho_h(self, r):
        y_ = r/self.rs
        return self.rho_s/(y_*(1 + y_)**2)
    def sigma_dm(self, r):
        rr_ = np.logspace(np.log10(r), np.log10(r) + 4, 4000)
        return sqrt(np.trapezoid(self.rho_h(rr_)*GK*self.Menc_sph(rr_)/rr_**2, rr_)/self.rho_h(r))
def nfw_for_vc(base, vc_target, R0=8.2):
    lo, hi = 1e5, 1e9
    for _ in range(100):
        mid = sqrt(lo*hi); base.rho_s = mid
        if base.vc(R0) < vc_target:
            lo = mid
        else:
            hi = mid
    return base
MODELS = [nfw_for_vc(MWModel(0.5e10, 0.6, 6.8e10, 3.0, 0.28, 1e7, 16.0, "light halo"), 220.0),
          nfw_for_vc(MWModel(1.19e10, 0.6, 3.52e10, 3.0, 0.3, 1e7, 8.8, "KK-like"), 230.0),
          nfw_for_vc(MWModel(0.9e10, 0.6, 5.0e10, 3.0, 0.28, 1e7, 20.0, "heavier halo"), 240.0)]
X0_SGR = np.array([17.5, 2.5, -6.5]); V0_SGR = np.array([237.9, -24.3, 209.0])
allW = []
for Mm in MODELS:
    sig_r = np.linspace(8, 120, 113); sig_t = np.array([Mm.sigma_dm(r_) for r_ in sig_r])
    dt_ = -1e-4; x_ = X0_SGR.copy(); v_ = V0_SGR*KMS_KPC_GYR
    nst = int(3.0/abs(dt_)); rs_o = np.empty(nst); Vs_o = np.empty(nst)
    acc = Mm.acc(x_)*KMS_KPC_GYR**2
    for i in range(nst):
        v_ = v_ + 0.5*dt_*acc; x_ = x_ + dt_*v_; acc = Mm.acc(x_)*KMS_KPC_GYR**2; v_ = v_ + 0.5*dt_*acc
        rs_o[i] = sqrt(x_ @ x_); Vs_o[i] = sqrt(v_ @ v_)/KMS_KPC_GYR
    sig_h = np.interp(rs_o, sig_r, sig_t)
    for sh_over in (None, 100.0, 150.0):
        sh = sig_h if sh_over is None else np.full_like(rs_o, sh_over)
        Wt = gate_avg(Vs_o, np.sqrt(sh**2 + 12.0**2))
        gDM = GK*(4*pi*Mm.rho_s*Mm.rs**3*(np.log(1 + rs_o/Mm.rs) - rs_o/(rs_o + Mm.rs)))/rs_o**2
        W_now = gate_avg(np.linalg.norm(V0_SGR), sqrt((sh_over if sh_over else Mm.sigma_dm(np.linalg.norm(X0_SGR)))**2 + 144))
        allW.append([W_now, Wt.mean(), np.sum(Wt*gDM)/np.sum(gDM), Wt[rs_o < np.percentile(rs_o, 20)].mean()])
allW = np.array(allW)
SGR_LO, SGR_HI = 0.1/allW.max(), 0.1/allW.min()
check("E7: Sgr, three toy Milky-Way potentials x three host dispersions x four orbit weightings (VCN u7, 3-Gyr "
      "orbits): eps < 0.36-2.46; with VDD's 0.20 the quoted range is 'of order 1 (0.2-2.5)'",
      round(SGR_LO, 2) == 0.36 and round(SGR_HI, 2) == 2.46 and round(0.1/abs(etas[1][1]), 1) == 0.2 and round(SGR_HI, 1) == 2.5,
      f"<W> in [{allW.min():.4f}, {allW.max():.4f}]")
check("E8: clumping needs eps > 1 at every gate width (F2), so the allowed strength is at least 1/0.1755 = 5.7x ('6x') "
      "too small, 1/0.1063 = 9.4x ('9x') in the record's reading; eps = 4/3 exceeds the record-reading gas bound 12.5x",
      round(1/LYA_F_G, 1) == 5.7 and round(1/LYA_H_G, 1) == 9.4 and round((4/3)/LYA_H_G, 1) == 12.5,
      f"{1/LYA_F_G:.2f}, {1/LYA_H_G:.2f}, {(4/3)/LYA_H_G:.2f}")
stamp()


# ======================================================================================================
print("\n== F. Clumping thresholds (ports of verify-critic-numbers/u2_c5_static_thresholds.py, u10_crossover_43.py, "
      "critic3/c4_numbers.py (a, b), corner/local_compare.py)")
# ======================================================================================================
# Local homogeneous (Jeans-swindle) model, static limit: unstable at (k/k_J)^2 = Q iff the top eigenvalue Lambda_0
# of K = p0^(1/2)[1 + gt W]p0^(1/2) on velocity space reaches Q (no re-virialization) or Q(1 + gt <W>) (re-
# virialized); W = exp(-|v - v'|^2/(2 v*^2)), units sigma = 1, r = sigma/v*. u2's radial l = 0 Nystrom operator;
# its top eigenvalue is found here from the rank-one secular equation (same matrix, checked against eigvalsh).
def gl_composite(a, b, npanel, nper=16):
    x0, w0 = np.polynomial.legendre.leggauss(nper)
    edges = np.linspace(a, b, npanel + 1)
    return (np.concatenate([0.5*(hi - lo)*x0 + 0.5*(hi + lo) for lo, hi in zip(edges[:-1], edges[1:])]),
            np.concatenate([0.5*(hi - lo)*w0 for lo, hi in zip(edges[:-1], edges[1:])]))
class Radial:
    def __init__(self, r, vmax=9.0):
        panel = min(0.25, 1.2/max(r, 1e-9))
        v, w = gl_composite(0.0, vmax, int(np.ceil(vmax/panel)))
        p0 = (2*np.pi)**-1.5*np.exp(-v**2/2)
        self.a = np.sqrt(4*np.pi*w)*v*np.sqrt(p0)
        x = r**2*np.outer(v, v)
        with np.errstate(invalid='ignore', divide='ignore'):
            ang = np.where(x > 1e-12, -np.expm1(-2*x)/(2*x), 1.0 - x)
        self.Kg = self.a[:, None]*np.exp(-r**2*(v[:, None] - v[None, :])**2/2)*ang*self.a[None, :]
        self.mu, vec = np.linalg.eigh(self.Kg)
        self.c2 = (vec.T @ self.a)**2
    def lam_gate(self):
        return self.mu[-1]
    def lam0_dense(self, gt):
        return np.linalg.eigvalsh(np.outer(self.a, self.a) + gt*self.Kg)[-1]
    def lam0(self, gt):
        if gt == 0:
            return float(np.sum(self.c2))
        F_ = lambda L: np.sum(self.c2/(L - gt*self.mu)) - 1.0
        lo = gt*self.mu[-1]*(1 + 1e-15) + 1e-300; hi = gt*self.mu[-1] + np.sum(self.c2) + 1.0
        if F_(lo) < 0:
            return lo
        for _ in range(200):
            mid = 0.5*(lo + hi)
            if F_(mid) > 0:
                lo = mid
            else:
                hi = mid
        return 0.5*(lo + hi)
def crit(solver, Q, revir_W=None, gmax=1e5):
    f = (lambda g: solver.lam0(g) - Q) if revir_W is None else (lambda g: solver.lam0(g) - Q*(1 + g*revir_W))
    if f(0.0) >= 0:
        return 0.0
    prev = 0.0
    for g in np.logspace(-3, np.log10(gmax), 49):
        if f(g) >= 0:
            lo, hi = np.log(max(prev, 1e-6)), np.log(g)
            for _ in range(40):
                mid = 0.5*(lo + hi)
                if f(np.exp(mid)) < 0:
                    lo = mid
                else:
                    hi = mid
            return float(np.exp(0.5*(lo + hi)))
        prev = g
    return np.inf
def W_pair(r):
    return (1 + 2*r**2)**-1.5
def valid_limit(r, X=4.5):
    """local model valid for gt < (1 + r^2)^(5/2)/(X r^2), X = |Phi|/sigma^2 = 9/2 (VCD's sizing)"""
    return (1 + r**2)**2.5/(X*r**2)
S_MW, S_CL, S_1 = Radial(155/120), Radial(1000/120), Radial(1.0)
check("F1 anchors: gt = 0 gives Lambda_0 = 1 (Jeans criterion); r -> 0 gives 1 + gt (gate = 1): 3.9991 at r = 0.01, "
      "gt = 3; the secular root equals the dense eigenvalue to 1e-12", abs(S_MW.lam0(0.0) - 1) < 1e-12 and
      round(Radial(0.01).lam0(3.0), 4) == 3.9991 and max(abs(S_MW.lam0(g) - S_MW.lam0_dense(g)) for g in (10.0, 100.0)) < 1e-12)
check("F1: the gate-only top eigenvalue Lambda_g = [1/2 + r^2 + sqrt(1 + 4r^2)/2]^(-3/2) matches the Nystrom operator: "
      "1.4928686e-01 (MW, r = 155/120), 1.4435026e-03 (cluster, r = 1000/120); Lambda_0(1.2917, 10) = 2.30511",
      close(S_MW.lam_gate(), lam_g(155/120), 1e-9) and close(S_CL.lam_gate(), lam_g(1000/120), 1e-9) and
      f"{lam_g(1000/120):.7e}" == "1.4435026e-03" and round(S_MW.lam0(10.0), 5) == 2.30511,
      f"{S_MW.lam_gate():.7e}, {S_CL.lam_gate():.7e}")
rr_g = np.geomspace(1e-3, 10, 2001); inv_g = 1/lam_g(rr_g)
lo_, hi_ = 0.01, 1.0
for _ in range(100):
    mid = 0.5*(lo_ + hi_)
    lo_, hi_ = (mid, hi_) if 1/lam_g(mid) < 4/3 else (lo_, mid)
check("F2: velocity-selected clumping needs eps > 1/Lambda_g(sigma/v*): increasing in r, min over r in [1e-3, 10] = "
      "1.000003 (so eps > 1 everywhere); 1/Lambda_g(1) = phi^3 = 4.236 (so eps >= 4.24 wherever sigma >= v*); "
      "1/Lambda_g = 4/3 at r = 0.33282", round(inv_g.min(), 6) == 1.000003 and bool(np.all(np.diff(inv_g) > 0)) and
      abs(1/lam_g(1.0) - PHI**3) < 1e-12 and round(1/lam_g(1.0), 2) == 4.24 and round(0.5*(lo_ + hi_), 5) == 0.33282,
      f"min {inv_g.min():.7f}; {1/lam_g(1.0):.6f}")
kJ_ = np.sqrt(4*np.pi*G*0.4*GEV_KG/1e-6)/155e3
Q_SUN = (2*np.pi/kJ_/3.085677581e19/8.2)**2
thr_mw = {Q_: (crit(S_MW, Q_), crit(S_MW, Q_, revir_W=W_pair(155/120))) for Q_ in (np.pi**2/2, 2*np.pi**2, Q_SUN)}
THR_MW = thr_mw[np.pi**2/2][0]
check("F3: Milky Way (sigma = 155, v* = 120, r = 1.2917, <W> = 0.1107): threshold 28.07 at the core margin Q = pi^2/2, "
      "127.5 at 2 pi^2, 161.2 at the solar-circle (lambda_J/R0)^2 = 24.771 ('28-161'); none (inf) once the halo "
      "re-virializes ('at least 28, or none')", round(THR_MW, 2) == 28.07 and round(thr_mw[2*np.pi**2][0], 1) == 127.5
      and round(thr_mw[Q_SUN][0], 1) == 161.2 and round(Q_SUN, 3) == 24.771 and round(W_pair(155/120), 4) == 0.1107 and
      all(np.isinf(v_[1]) for v_ in thr_mw.values()), f"{THR_MW:.4f}, {thr_mw[2*np.pi**2][0]:.2f}, {thr_mw[Q_SUN][0]:.2f}")
THR_CL = 1/lam_g(1000/120)
cl_jeans = (crit(S_CL, (np.pi/3)**2), crit(S_CL, (np.pi/3)**2, revir_W=W_pair(1000/120)))
check("F3: clusters (sigma = 1000, r = 8.333): velocity-selection crossover 692.8 ('at least 690'); the instability "
      "threshold at Q = (pi/3)^2 is 152.2 (the interim's 'at least 152'), 798.8 re-virialized",
      round(THR_CL, 1) == 692.8 and round(cl_jeans[0], 1) == 152.2 and round(cl_jeans[1], 1) == 798.8,
      f"{THR_CL:.4f}; {cl_jeans[0]:.3f} / {cl_jeans[1]:.3f}")
check("F4: margins at v* = 120 over the allowed eps: 28.07/0.1063 = 264 (MW), 692.8/0.1063 = 6.52e3 (clusters), "
      "28.07/2.46 = 11.4 (loosest Sgr mapping)", round(THR_MW/LYA_H_G) == 264 and r3(THR_CL/LYA_H_G) == 6.52e3 and
      round(THR_MW/SGR_HI, 1) == 11.4, f"{THR_MW/LYA_H_G:.1f}, {THR_CL/LYA_H_G:.4g}, {THR_MW/SGR_HI:.2f}")
check("F5: the local model holds only for eps < (1 + r^2)^(5/2)/(4.5 r^2): 1.549 (MW), 133.3 (clusters), so the "
      "thresholds 28 and 690 lie beyond it; 1.257 at r = 1, 3.106 at r = 2",
      round(valid_limit(155/120), 3) == 1.549 and round(valid_limit(1000/120), 1) == 133.3 and
      round(valid_limit(1.0), 3) == 1.257 and round(valid_limit(2.0), 3) == 3.106 and THR_MW > valid_limit(155/120)
      and THR_CL > valid_limit(1000/120))
thr_r1 = crit(S_1, (np.pi/3)**2, revir_W=W_pair(1.0))
check("F6: gates as wide as the dispersion (r = 1): crossover 4.24, re-virialized threshold 9.785 at Q = (pi/3)^2 "
      "('clumping would need eps of about 4 to 10' below 3 km/s), both beyond the model's validity (1.257)",
      round(thr_r1, 3) == 9.785 and thr_r1 > valid_limit(1.0), f"{thr_r1:.4f}")
stamp()


# ======================================================================================================
print("\n== G. The low-v* corner (record: corner/runs/log_*.txt, diagnostics_final.out, injection_test.out, "
      "summary_numbers.out; recomputed: ports of corner/phys_scales.py and critic3/c2_corner_recheck.py)")
# ======================================================================================================
cdir = os.path.join(RECORD, "corner")
logs = sorted(f_ for f_ in os.listdir(os.path.join(cdir, "runs")) if f_.startswith("log_"))
cases_ = {}; dE = {}
for f_ in logs:
    m_ = re.match(r"log_eps_([\d.]+)_rg_([\d.]+)_N_(\d+)_seed_(\d+)_.*?(_reading_F)?\.txt$", f_)
    key = (float(m_.group(1)), float(m_.group(2)), int(m_.group(3)), "F" if m_.group(5) else "H")
    cases_[key] = cases_.get(key, 0) + 1
    txt = open(os.path.join(cdir, "runs", f_)).read()
    dE[f_] = (key[3], float(re.search(r"max\|dE/E\| = ([0-9.e+-]+)", txt).group(1)))
eps_set = sorted({k_[0] for k_ in cases_}); rg_set = sorted({k_[1] for k_ in cases_ if k_[0] > 0})
check("G1 (record): 29 run logs: eps = 0 (control), 1, 3, 10 in the record's (Hamiltonian) reading plus eps = 3 in the "
      "force law; gate as wide as (r_g = 1) or 2.5x wider than (r_g = 0.4) the dispersion; three seeds per case, two for "
      "the N = 1000 control", len(logs) == 29 and eps_set == [0.0, 1.0, 3.0, 10.0] and rg_set == [0.4, 1.0] and
      sorted(cases_.values()) == [2] + [3]*9 and cases_.get((0.0, 1.0, 1000, "H")) == 2,
      f"{len(cases_)} cases")
dEH = sorted(v_[1] for v_ in dE.values() if v_[0] == "H"); dEF = sorted(v_[1] for v_ in dE.values() if v_[0] == "F")
check("G1 (record): after the ramp the Hamiltonian runs conserve energy to max|dE/E| = 5.4e-5 (23 of the 26 within "
      "the corner's stated 1.8e-5; the three eps = 10 exceptions are 1.86e-5, 2.94e-5, 5.37e-5); the force-law runs "
      "drift 2.0-3.8%, as a non-conservative force should",
      len(dEH) == 26 and r2(dEH[-1]) == 5.4e-5 and sum(x_ <= 1.8e-5 for x_ in dEH) == 23 and
      [r3(x_) for x_ in dEF] == [1.98e-2, 2.21e-2, 3.76e-2], f"H max {dEH[-1]:.2e}; F {dEF}")
diag = open(os.path.join(cdir, "diagnostics_final.out")).read()
blk = diag.split("=== reading H, eps = 10, r_g = 1, N = 2000")[1].split("=== reading")[0]
xi = re.search(r"xi_u05 = ([+-][0-9.]+) \+- ([0-9.]+)", blk.split("post-ramp average")[1])
check("G2 (record): eps = 10, gate = dispersion, N = 2000: post-ramp xi_u05 = -0.0069 +- 0.0063 (no velocity-selected "
      "clumping)", xi and xi.group(1) == "-0.0069" and xi.group(2) == "0.0063")
inj = open(os.path.join(cdir, "injection_test.out")).read()
def inj_row(label):
    return [float(x_) for x_ in re.search(re.escape(label) + r":\s+Xi\(v\*\) Xi\(v\*/2\) S1 S2 Rv = (.*)", inj).group(1).split()]
o_, c2p, s2p, s5p = inj_row("original"), inj_row("clumps f = 0.02"), inj_row("stream f = 0.02"), inj_row("stream f = 0.05")
check("G3 (record): sensitivity: injected clumps holding 2% of the mass raise Xi(v*/2) from +0.0852 to +0.2339; a 2% "
      "stream does not register (Xi(v*/2) +0.0396, S2 +0.088 within the control errors); a 5% stream does (S1 +0.8181)",
      o_[1] == 0.0852 and c2p[1] == 0.2339 and s2p[1] == 0.0396 and round(s2p[3] - o_[3], 3) == 0.088 and s5p[2] == 0.8181)
summ = open(os.path.join(cdir, "summary_numbers.out")).read()
ratios = [float(x_) for x_ in re.findall(r"sig_k/sig_c = ([0-9.]+)", summ)]
check("G3 (record): the record's reading separates kinematic from canonical dispersion by up to 11.5x "
      "(eps = 10, r_g = 1)", max(ratios) == 11.50)
# Not adjudicated by the record: the close-pair statistic xi_u1 sits slightly above the control in every gated
# N = 2000 case. The corner agent and the final critic read the N-body as a null; nothing separates this offset
# from the halo's reorganization (r50 changes by 0.685-1.647). Printed so the note can state it.
dxi = [(float(a_), float(b_)) for a_, b_ in re.findall(r"dxi_u1 = ([+-][0-9.]+) \+- ([0-9.]+)", summ)]
r50s = [float(x_) for x_ in re.findall(r"r50/r50\(t=0\) = ([0-9.]+)", summ)]
pulls = [a_/b_ for a_, b_ in dxi]
check("G3 (record, not adjudicated): in all 7 gated N = 2000 cases xi_u1 exceeds the control by +0.0073 to +0.0231, "
      "1.7-3.5 sigma on three seeds, while the halo's r50 changes by a factor 0.685-1.647",
      len(dxi) == 7 and all(a_ > 0 for a_, _ in dxi) and min(a_ for a_, _ in dxi) == 0.0073
      and max(a_ for a_, _ in dxi) == 0.0231 and round(min(pulls), 1) == 1.7 and round(max(pulls), 1) == 3.5
      and min(r50s) == 0.685 and max(r50s) == 1.647,
      f"pulls {', '.join(f'{p_:.2f}' for p_ in pulls)}")
check("G3 (record, not adjudicated): injected 2% clumps raise xi_u1 = Xi(v*) from +0.0146 to +0.0409 in one "
      "snapshot, a change comparable to that offset; the null rests on Xi(v*/2), which they raise from +0.0852 to "
      "+0.2339",
      o_[0] == 0.0146 and c2p[0] == 0.0409 and o_[1] == 0.0852 and c2p[1] == 0.2339)
tff_pl = 1/np.sqrt(4*np.pi*3/(4*np.pi))
tff_my = [1/np.sqrt(4*np.pi*4.30091e-3*rho_)*0.977792 for rho_ in (0.79e8/1e9, 2.36e8/1e9, 2.40)]
check("G4: the runs' post-ramp window of 25 units is 25/0.5774 = 43.3 central free-fall times; dwarf t_ff = 14.96, "
      "8.66 Myr (classical dSph, Read-Walker-Steger 2019) and 2.71 Myr (Segue 1, Simon et al. 2011), so 43 t_ff = "
      "0.117-0.643 Gyr ('0.1-0.6 Gyr')", round(25/tff_pl, 1) == 43.3 and [round(t_, 2) for t_ in tff_my] == [14.96, 8.66, 2.71]
      and round(43*tff_my[2]/1e3, 3) == 0.117 and round(43*tff_my[0]/1e3, 3) == 0.643)
check("G4: the corner needs a second gate scale 120/30 = 4 to 120/3 = 40 times below the record's 120 km/s",
      120/30 == 4 and 120/3 == 40)
stamp()

# critic3/c2_corner_recheck.py on the corner's kernels (built in the anchors) and background
check("G5: corner kernels at y = 1 (c4b's printout): R = 0.72478, R_v = 0.47699, R_a = -0.87168, J_W = -0.44956",
      [round(float(cn_I(n_, 1.0)), 5) for n_ in ("R", "Rv", "Ra", "yJ")] == [0.72478, 0.47699, -0.87168, -0.44956])
z_ly = 4.2
kmpc_ly = np.array([0.05, 0.1, 0.2])*float(BG_DT.Hz(z_ly))/(1 + z_ly)
TOL53 = np.array([0.0097, 0.0451, 0.1941]); TOL35 = np.array([0.0271, 0.1209, 0.4472])  # corner's WDM-template levels
def flag(t2):
    d_ = np.abs(t2 - 1)
    return "B35" if d_[1] > TOL35[1] else ("B53" if d_[1] > TOL53[1] else "ok")
ly_cases = [(1, 10, "H"), (1, 10, "K4"), (1, 3, "Hc"), (1, 5, "Fc"), (1, 3, "Fc")]
TLY = cn_T2(kmpc_ly, ly_cases, [z_ly])[z_ly]
check("G5 anchors: the corner's printed Lyman-alpha responses reproduce (z = 4.2, k = 0.05/0.1/0.2 s/km, v* = 10, "
      "eps = 1): H 0.927/0.754/0.932, K4 1.2/1.92/6.91", [r3(x_) for x_ in TLY[0]] == [0.927, 0.754, 0.932] and
      [r3(x_) for x_ in TLY[1]] == [1.2, 1.92, 6.91])
check("G6: eps = 1, Lyman-alpha against the 5.3-keV WDM template at 0.1 s/km: beyond it from v* = 3 km/s (record's "
      "reading, T^2 = 0.939) and 5 km/s (force law, 1.08); the force law passes at 3 km/s (1.03)",
      flag(TLY[2]) == "B53" and flag(TLY[3]) == "B53" and flag(TLY[4]) == "ok" and r3(TLY[2][1]) == 0.939 and
      r3(TLY[3][1]) == 1.08 and r3(TLY[4][1]) == 1.03)
KK_ = np.logspace(-2, 3.3, 200)
ZLIST = [0.0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120, 150]
PK0 = {z: P_lin(KK_, z) for z in ZLIST}
MASSES = [1e8, 1e9, 1e10]
RHO_M0 = DT_Om*2.775e11*DT_h**2
def sigma_M(M, kk, Pk):
    R = (M/(4*np.pi/3*RHO_M0))**(1/3)
    return np.sqrt(np.trapezoid(kk**3*Pk*tophat(kk*R)**2/(2*np.pi**2), np.log(kk)))
def zc_of(s_):
    lz = np.log(1 + np.array(ZLIST))
    if s_[0] < 1.686:
        return np.nan
    if s_[-1] > 1.686:
        return np.inf
    j = int(np.argmax(s_ < 1.686))
    l_ = lz[j - 1] + (np.log(1.686) - np.log(s_[j - 1]))/(np.log(s_[j]) - np.log(s_[j - 1]))*(lz[j] - lz[j - 1])
    return np.exp(l_) - 1
SIG_T, MP_, YP, RHO_C0 = 6.6524587e-29, 1.67262192e-27, 0.245, 1.87847e-26*DT_h**2
NH0 = (1 - YP)*DT_Ob*RHO_C0/MP_; FHE = YP/(4*(1 - YP))
ZZ_T = np.linspace(0, 150, 3001)
def tau_ii(S):
    """toy reionization: ionized fraction tracks the collapsed fraction above 1e8 Msun, normalized to Q(6) = 1"""
    s_ = np.interp(ZZ_T, ZLIST, S[1e8])
    f_ = np.array([erfc(1.686/(sqrt(2)*x_)) if x_ > 0 else 0.0 for x_ in s_])
    Qz = np.minimum(1, f_/np.interp(6.0, ZZ_T, f_))
    ne = NH0*(1 + ZZ_T)**3*Qz*(1 + FHE + np.where(ZZ_T < 3.5, FHE, 0.0))
    return np.trapezoid(SIG_T*C*ne/((1 + ZZ_T)*BG_DT.Hz(ZZ_T)*1e3/3.0856775814913673e22), ZZ_T)
def sig_table(Tz):
    return {M: np.array([sigma_M(M, KK_, PK0[z]*Tz[z]) for z in ZLIST]) for M in MASSES}
S0_ = sig_table({z: np.ones_like(KK_) for z in ZLIST}); zc0 = {M: zc_of(S0_[M]) for M in MASSES}
TAU_L = tau_ii(S0_)
d_cases = [(1, 10, "K4"), (1, 20, "H"), (3, 5, "Fc"), (3, 30, "Fc"), (2, 10, "Hc"), (2, 10, "Fc"), (1, 30, "Hc"),
           (1, 20, "Fc")]
TD = cn_T2(KK_, d_cases, ZLIST)
dens = {}
for i, c_ in enumerate(d_cases):
    S_ = sig_table({z: TD[z][i] for z in ZLIST}); zc = {M: zc_of(S_[M]) for M in MASSES}
    dens[c_] = (((1 + zc[1e9])/(1 + zc0[1e9]))**3, tau_ii(S_))
for c_, (d9, ta) in dens.items():
    print(f"      eps = {c_[0]}, v* = {c_[1]:2d}, {c_[2]:2s}: density proxy 1e9 Msun x{d9:.3g}, tau(ii) = {ta:.3f}")
check("G7 anchors: LCDM tau(ii) = 0.0575; the corner's K4 (eps = 1, v* = 10: x2.17, tau 0.068) and H (eps = 1, v* = 20: "
      "x2.14, tau 0.071) reproduce", round(TAU_L, 4) == 0.0575 and r3(dens[(1, 10, "K4")][0]) == 2.17 and
      round(dens[(1, 10, "K4")][1], 3) == 0.068 and r3(dens[(1, 20, "H")][0]) == 2.14 and round(dens[(1, 20, "H")][1], 3) == 0.071)
TAU_PL, TAU_PL_S = 0.054, 0.007                            # Planck 2018 reionization optical depth
check("G7: eps = 3, force law (fixed-velocity reading): at v* = 5 km/s the 1e9-Msun density proxy is x9.54 and tau(ii) "
      "= 0.099 (6.4 sigma above Planck's 0.054 +- 0.007); at 30 km/s x366, tau 0.582: excluded at 5-30 km/s (the record's "
      "reading is singular there, E5)", r3(dens[(3, 5, "Fc")][0]) == 9.54 and round(dens[(3, 5, "Fc")][1], 3) == 0.099 and
      round((dens[(3, 5, "Fc")][1] - TAU_PL)/TAU_PL_S, 1) == 6.4 and r3(dens[(3, 30, "Fc")][0]) == 366 and
      round(dens[(3, 30, "Fc")][1], 3) == 0.582, f"{dens[(3, 5, 'Fc')][0]:.4f}, {dens[(3, 5, 'Fc')][1]:.4f}")
check("G7: eps = 2 at v* = 10 km/s: tau(ii) = 0.078 (3.4 sigma) in both readings, density x4.39 (record's) and x3.59 "
      "(force law): excluded from 10 km/s up", round(dens[(2, 10, "Hc")][1], 3) == 0.078 and
      round(dens[(2, 10, "Fc")][1], 3) == 0.078 and r3(dens[(2, 10, "Hc")][0]) == 4.39 and r3(dens[(2, 10, "Fc")][0]) == 3.59
      and round((0.078 - TAU_PL)/TAU_PL_S, 1) == 3.4)
check("G7: eps = 1: tau(ii) = 0.073, 2.7 sigma high, at v* = 30 (record's reading) and 20 km/s (force law); dwarf "
      "densities x2.27 and x2.82 ('x2.3-2.8')", round(dens[(1, 30, "Hc")][1], 3) == 0.073 and
      round(dens[(1, 20, "Fc")][1], 3) == 0.073 and round((0.073 - TAU_PL)/TAU_PL_S, 1) == 2.7 and
      r3(dens[(1, 30, "Hc")][0]) == 2.27 and r3(dens[(1, 20, "Fc")][0]) == 2.82)
Z_MIN = 87.7
KD_ = np.logspace(-2, 3.6, 260); PD_ = P_lin(KD_, Z_MIN); MS_ = np.logspace(0, 5, 26)
def H_moment(T):
    s_ = np.array([sigma_M(M, KD_, PD_*T) for M in MS_])
    F_ = np.array([erfc(1.686/(sqrt(2)*x_)) for x_ in s_])
    return np.sum(np.sqrt(MS_[1:]*MS_[:-1])*(F_[:-1] - F_[1:]))
s_cases = [(1.0, 10, "H"), (1.0, 10, "K4"), (1.0, 5, "Hc"), (1.0, 5, "Fc"), (1.0, 3, "Hc"), (1.0, 3, "Fc")]
TSg = cn_T2(KD_, s_cases, [Z_MIN])[Z_MIN]
HM = [H_moment(t_) for t_ in TSg]
check("G8: Segue 1 heating moment at z_min = 87.7 (limit 7.88 Msun): the corner's anchors 1.05e3 (H) and 742 (K4) at "
      "v* = 10 reproduce; eps = 1 at v* = 5 gives 39 (record's reading) and 12.5 (force law), above the limit; at v* = 3, "
      "7.6 and 2.49, below it", r3(HM[0]) == 1.05e3 and r3(HM[1]) == 742 and r3(HM[2]) == 39.0 and r3(HM[3]) == 12.5 and
      r3(HM[4]) == 7.6 and r3(HM[5]) == 2.49 and HM[2] > 7.88 and HM[3] > 7.88 and HM[4] < 7.88,
      ", ".join(f"{x_:.3g}" for x_ in HM))
# the integrators' gated systems in the Einstein-de Sitter uniform limit (y -> infinity: R, R_v, R_a -> 1, yJ -> 0):
# K4/Fc: p^2 + (1/2 - eps/2) p = (3/2)(1 + eps); H/Hc: p^2 + p/2 = (3/2)(1 + eps)(1 + eps/2) (implementation check)
gE = cn_grow([1.0], [(e_, 1e12, rd_) for rd_ in ("Fc", "Hc") for e_ in (1.0, 3.0)], [np.e - 1, 0.0], bg=BG_EDS)
pnum = np.log(gE[0.0][:, 0]/gE[np.e - 1][:, 0])
pan = [(-(0.5 - e_/2) + sqrt((0.5 - e_/2)**2 + 6*(1 + e_)))/2 for e_ in (1.0, 3.0)] + \
      [(-0.5 + sqrt(0.25 + 6*(1 + e_)*(1 + e_/2)))/2 for e_ in (1.0, 3.0)]
check("G9: the corner's integrator in the Einstein-de Sitter uniform limit reproduces its systems' analytic growth "
      "exponents (force law 1.73205, 3.00000; record's reading 1.88600, 3.63104 at eps = 1, 3) to 1e-4 (implementation "
      "check, not independent of the model)", max(abs(pnum - np.array(pan))) < 1e-4,
      ", ".join(f"{x_:.5f}" for x_ in pnum))
stamp()


# ======================================================================================================
print("\n== H. Cores (ports of verify-dark-tests-derivation/v3_misc.py K16, verify-dark-tests-numbers/vscatter.py, "
      "verify-critic-numbers/u5_c6C_born.py)")
# ======================================================================================================
m_chi = 70e6*EV/C**2; mu_r = m_chi/2; kap_ = G*m_chi**2
v30 = 30e3
lnB = log(2*mu_r*v30*KPC/HBAR) - 0.5
sT = 4*pi*(kap_/(mu_r*v30**2))**2*lnB
sTm = sT*1e4/(m_chi*1e3)
check("H1: a gravitational-strength 1/r chi-chi force scatters at sigma_T/m = 2.37e-62 cm^2/g at 30 km/s (Born, "
      "ln Lambda = 68.67 at b = 1 kpc; eta = 3.29e-37); dwarf cores (30 cm^2/g) need G~/G = 3.56e31 ('3.6e31')",
      r4(sTm) == 2.369e-62 and round(lnB, 2) == 68.67 and r3(kap_/(HBAR*v30)) == 3.29e-37 and r4(sqrt(30/sTm)) == 3.559e31
      and r2(sqrt(30/sTm)) == 3.6e31, f"{sTm:.4e}, {sqrt(30/sTm):.4e}")
def sigmaT_born(Gt, b, v=v30):
    al = Gt*m_chi**2; k_ = mu_r*v/HBAR; x_ = 4*k_**2*b**2
    return 2*pi*al**2/(mu_r**2*v**4)*(np.log1p(x_) - x_/(1 + x_))
def sigmaT_born_numeric(Gt, b, v=v30):
    al = Gt*m_chi**2; k_ = mu_r*v/HBAR; kap0 = 1/b
    pref = (2*mu_r*al/HBAR**2)**2*mp.pi/k_**4
    return float(pref*mp.quad(lambda y_: (kap0*mp.e**y_)**4/((kap0*mp.e**y_)**2 + kap0**2)**2, [-60, 0, mp.log(2*k_/kap0)]))
def sigmaT_classical(Gt, b, v=v30):
    b90 = Gt*m_chi**2/(mu_r*v**2)
    return 4*pi*b90**2*log(b/b90)
def solve_gt(fun, b):
    lo, hi = 1e20, 1e45
    for _ in range(300):
        mid = sqrt(lo*hi)
        if fun(mid*G, b)/m_chi < 30e-4/1e-3:
            lo = mid
        else:
            hi = mid
    return sqrt(lo*hi)
gB1 = solve_gt(sigmaT_born, KPC); gC1 = solve_gt(sigmaT_classical, KPC)
gt_lnN = sqrt(30e-4/1e-3*m_chi*mu_r**2*v30**4/(4*pi*(G*m_chi**2)**2*155.1))
num_ok = close(sigmaT_born(3.5e31*G, 2.385*KPC), sigmaT_born_numeric(3.5e31*G, 2.385*KPC), 1e-6)
check("H2: the exact Born transfer cross-section of a screened 1/r potential, (2 pi al^2/mu^2 v^4)[ln(1 + 4k^2b^2) - "
      "4k^2b^2/(1 + 4k^2b^2)], equals its numerical q-integral; it needs G~/G = 3.5588e31 (b = 1 kpc); the classical "
      "routes give 3.30e31 (self-consistent log) and 2.37e31 (ln N = 155.1), so '3.6e31' is the Born value",
      num_ok and round(gB1/1e31, 4) == 3.5588 and r3(gC1) == 3.30e31 and r3(gt_lnN) == 2.37e31,
      f"{gB1:.5e}, {gC1:.4e}, {gt_lnN:.4e}")
check("H2: Born is the right regime: the Sommerfeld parameter G~ m^2/(hbar v) at G~/G = 3.56e31, 30 km/s is 1.17e-5",
      r3(3.56e31*G*m_chi**2/(HBAR*v30)) == 1.17e-5)
stamp()


# ======================================================================================================
print("\n== I. Carriers (ports of verify-critic-theory/v1_spinJ_residues.py, v2_tower_gate.py, v3_gate_range.py, "
      "v7_misc_numbers.py; critic3/c4_numbers.py (f))")
# ======================================================================================================
def sym_all(T):
    J = T.ndim
    if J <= 1:
        return T.copy()
    perms = list(itertools.permutations(range(J)))
    return sum(np.transpose(T, p_) for p_ in perms)/len(perms)
def outer_power(x, J):
    T = np.array(1.0 + 0j)
    for _ in range(J):
        T = np.multiply.outer(T, x)
    return T
def trace2(T, ginv):
    return np.tensordot(ginv, T, axes=([0, 1], [0, 1]))
def traceless_part(xup, J, g):
    """traceless part (metric g) of x_a x_b ..., by least squares over symmetric rank-(J - 2) corrections"""
    n_ = len(xup); ginv = np.linalg.inv(g)
    A = outer_power(g @ xup, J)
    if J < 2:
        return A
    cols = []
    for kk in range(n_**(J - 2)):
        S_ = np.zeros(n_**(J - 2), dtype=complex); S_[kk] = 1.0
        S_ = S_.reshape((n_,)*(J - 2)) if J > 2 else S_.reshape(())
        cols.append(trace2(sym_all(np.multiply.outer(g.astype(complex), S_)), ginv).ravel())
    Ssol = np.linalg.lstsq(np.array(cols).T, trace2(A, ginv).ravel(), rcond=None)[0]
    Ssol = Ssol.reshape((n_,)*(J - 2)) if J > 2 else Ssol.reshape(())
    return A - sym_all(np.multiply.outer(g.astype(complex), Ssol))
def contract(Tlow, yup):
    out = Tlow
    for _ in range(Tlow.ndim):
        out = np.tensordot(out, yup, axes=([0], [0]))
    return complex(out)
dev = 0.0
for n_, poly in ((3, lambda J, x_: float(sp.legendre(J, x_))), (2, lambda J, x_: float(sp.chebyshevt(J, x_)))):
    g_ = np.diag([1.0] + [-1.0]*(n_ - 1))
    for J in range(0, 5):
        for gam_ in (1.0001, 1.5, 3.0):
            u1 = np.zeros(n_); u1[0] = 1.0
            u2 = np.zeros(n_); u2[0] = gam_; u2[1] = sqrt(gam_**2 - 1)
            T_ = traceless_part(u1.astype(complex), J, g_)
            r_ = contract(T_, u2.astype(complex))/contract(T_, u1.astype(complex))
            dev = max(dev, abs(r_.real - poly(J, gam_))/max(1, abs(poly(J, gam_))), abs(r_.imag))
check("I1: spin-J exchange between point sources: the residue is the traceless projection, a degree-J polynomial in "
      "gamma = u1.u2: Legendre P_J (massive, 3 states orthogonal to q) and Chebyshev T_J (massless, 2 helicities), J = 0-4",
      dev < 1e-12, f"max deviation {dev:.1e}")
bq = sp.symbols('beta', positive=True); gb = 1/sp.sqrt(1 - bq**2)
coef_ok = all(sp.series(sp.legendre(J, gb), bq, 0, 3).removeO().coeff(bq, 2) == sp.Rational(J*(J + 1), 4) and
              sp.series(sp.chebyshevt(J, gb), bq, 0, 3).removeO().coeff(bq, 2) == sp.Rational(J*J, 2) for J in range(9))
grow_ok = all(all(abs(complex(r_).imag) < 1e-12 and abs(complex(r_).real) <= 1 + 1e-12 for r_ in sp.Poly(p_, gq).nroots())
              for J in range(1, 9) for p_ in (sp.legendre(J, gq), sp.chebyshevt(J, gq)))
check("I1: (v/c)^2 coefficients J(J + 1)/4 (massive) and J^2/2 (massless), J = 0-8; all roots lie in [-1, 1], so every "
      "residue grows with gamma > 1: for any finite spin, exchange makes the force grow with relative velocity",
      coef_ok and grow_ok)
Jm = (-1 + sqrt(1 + 16/b2_120))/2; Jl = sqrt(2/b2_120)
mp.mp.dps = 40
gstar = 1/mp.sqrt(1 - mp.mpf(b2_120))
PJ = mp.hyp2f1(-4996, 4997, 1, (1 - gstar)/2) - 1; TJ = mp.cosh(3533*mp.acosh(gstar)) - 1
check("I2: an O(1) effect at 120 km/s needs J = 4996.0 (massive, J(J + 1)/4 (v/c)^2 = 1) or 3533.1 (massless): "
      "'spin 3500-5000'; there P_4996(gamma*) - 1 = 1.28, T_3533(gamma*) - 1 = 1.18",
      round(Jm, 1) == 4996.0 and round(Jl, 1) == 3533.1 and round(float(PJ), 2) == 1.28 and round(float(TJ), 2) == 1.18,
      f"{Jm:.2f}, {Jl:.2f}")
mp.mp.dps = 60
xt = mp.mpf(5)
coeffs = [mp.e**xt*(2*J + 1)*(-1)**J*mp.sqrt(mp.pi/(2*xt))*mp.besseli(J + mp.mpf(1)/2, xt) for J in range(int(6*mp.e*5*3 + 80) + 1)]
tower_ok = all(abs(mp.fsum(c_*mp.legendre(J, g_) for J, c_ in enumerate(coeffs))/mp.e**(-xt*(g_ - 1)) - 1) < mp.mpf(10)**-12
               for g_ in (mp.mpf(1), mp.mpf('1.05'), mp.mpf('1.5'), mp.mpf(3)))
asym_dev = []
for x_ in (320, 1000, 3000):
    x_ = mp.mpf(x_); J = int(mp.sqrt(x_))
    exact = mp.e**x_*(2*J + 1)*mp.sqrt(mp.pi/(2*x_))*mp.besseli(J + mp.mpf(1)/2, x_)
    asym = (2*J + 1)*mp.e**(2*x_)/(2*x_)*mp.e**(-J*(J + 1)/(2*x_))
    asym_dev.append(float(abs(mp.log10(exact) - mp.log10(asym))))
xg = (mp.mpf('299792.458')/120)**2; Jg = mp.sqrt(xg)
log10max = mp.log10(2*Jg + 1) + 2*xg*mp.log10(mp.e) - mp.log10(2*xg) - Jg*(Jg + 1)/(2*xg)*mp.log10(mp.e)
check("I3: an infinite spin tower: exp(-x(gamma - 1)) = e^x Sum (2J + 1)(-1)^J i_J(x) P_J(gamma) (checked at x = 5); its "
      "largest term (2J + 1) e^(2x)/(2x) e^(-J(J+1)/2x) (exact to 3e-4 in log10 at x = 320-3000) is 10^5421169 times the "
      "net force at v* = 120 km/s (x = c^2/v*^2 = 6.24e6)", tower_ok and max(asym_dev) < 3e-4 and
      int(mp.nint(log10max)) == 5421169, f"log10 = {mp.nstr(log10max, 10)}; {', '.join(f'{d_:.1e}' for d_ in asym_dev)}")
mp.mp.dps = 15
rho_cs = 1.97327e-7/(KPC*120.0/C_KMS)
check("I4: continuous-spin exchange (Schuster-Toro-Zhou 2023, eq. 129 [S]): the correction matters when rho v r/(hbar c) "
      "~ 1: rho = 1.598e-23 eV for 120 km/s at 1 kpc, ten times smaller at 10 kpc (the switch-on velocity falls with "
      "distance)", r4(rho_cs) == 1.598e-23 and r4(1.97327e-7/(10*KPC*120.0/C_KMS)) == 1.598e-24)
vi_, vj_, rh_ = sp.Matrix(sp.symbols('p1:4', real=True)), sp.Matrix(sp.symbols('q1:4', real=True)), sp.Matrix([0, 0, 1])
dvij = vi_ - vj_
corr = (sp.sqrt((dvij.T*dvij)[0]) - (dvij.T*rh_)[0])**2
check("I4: eq. 129's correction (|v_i - v_j| - (v_i - v_j).r^)^2 depends only on the relative velocity, vanishes for "
      "bodies moving together and for relative motion along r^", sp.simplify(corr.subs(dict(zip(vi_, vj_)))) == 0 and
      sp.simplify(corr.subs({vi_[0]: vj_[0], vi_[1]: vj_[1], vi_[2]: vj_[2] + 5})) == 0)
# the contact range of the record's gate comes from X's mass (v3_gate_range.py (b), (d)): quantum expectation of
# A = F^(1/2)(p) V(x) F^(1/2)(p) against the classical gated value, hbar = mu = 1, Gaussian gate, V = 1/sqrt(x^2 + 1)
NG = 24000; dxg = 0.25
xg_ = (np.arange(NG) - NG//2)*dxg; kg_ = 2*np.pi*np.fft.fftfreq(NG, d=dxg)
Fh = np.sqrt(np.exp(-kg_**2)); Vg = 1.0/np.sqrt(xg_**2 + 1.0)
psi = np.exp(-(xg_ - 100.0)**2/(4*36.0)); psi /= np.sqrt(np.sum(np.abs(psi)**2)*dxg)
phi_ = np.fft.ifft(Fh*np.fft.fft(Vg*np.fft.ifft(Fh*np.fft.fft(psi))))
qexp = (np.vdot(psi, phi_)*dxg).real
gx_ = np.exp(-(xg_ - 100.0)**2/(2*36.0)); gx_ /= gx_.sum()
pv = np.linspace(-8/12, 8/12, 4001); gp = np.exp(-pv**2*2*36.0); gp /= gp.sum()
ratio_q = qexp/(np.sum(gx_*Vg)*np.sum(gp*np.exp(-pv**2)))
mu_c = 70.0*(120e3/C)/sqrt(2)
check("I5: the record's gate on the incoming relative momentum survives at long range non-relativistically: at "
      "100 hbar/mu the quantum expectation matches the classical gated value to 5e-5 (1.000051); hbar/mu = 1.0e-11 m "
      "(mu c = 19.8 keV): the gate is contact-range because X is massive",
      round(ratio_q, 6) == 1.000051 and r2(197.3269804/mu_c*1e-15) == 1.0e-11 and round(mu_c*1e3, 1) == 19.8,
      f"{ratio_q:.7f}")
stamp()


# ======================================================================================================
print("\n== J. Flag 57: the Vainshtein radius (port of verify-critic-numbers/u6_c6E_vainshtein.py)")
# ======================================================================================================
# Enander & Mortsell, JHEP 2013, arXiv:1306.1086, sec. 5, eqs. 38-43 [S, read by the critic-numbers verifier]:
#   m1^2 = m^2 (beta1 + beta2 c), m2^2 = m^2 (beta2 c + beta3 c^2), m_g^2 = (1/c + c)(m1^2 + m2^2) = 1/lambda^2
#   eq. 40 (all fields except F): r_V^3 = G M (1 + c^2)^3 m2^2/(c^3 m_g^4)
#   eq. 41 (field F):             r_V^3 = G M (1 + c^2)^3 (7 m1^2 + 8 m2^2)/(c^3 m_g^4)
#   eq. 43 (m1 = 0):              r_V^3 = G M c^2 (1 + c^-2)^2/m_g^2
# Every parameter and what fixes it: c, the background ratio (u in the diameter note) = 1 in the program's aligned
# vacuum; beta1, beta2, beta3: the program's palindromic vacuum has beta3 = beta1, so m1 = m2 at c = 1 for any
# beta1, beta2; m^2: fixed by lambda through m_g^2 = 1/lambda^2; lambda = 50 um (the value used at
# verify/phase_space_diameter.py:383); M: the source mass (1 kg; the Sun for the windows); G M -> G M/c^2.
cq_, b1_, b2_, b3_, msq, Mq, lamq = sp.symbols('c beta1 beta2 beta3 m2 M lambda', positive=True)
m1sq_ = msq*(b1_ + b2_*cq_); m2sq_ = msq*(b2_*cq_ + b3_*cq_**2)
mgsq_ = (1/cq_ + cq_)*(m1sq_ + m2sq_)
rV3 = {"40": Mq*(1 + cq_**2)**3*m2sq_/(cq_**3*mgsq_**2), "41": Mq*(1 + cq_**2)**3*(7*m1sq_ + 8*m2sq_)/(cq_**3*mgsq_**2),
       "43": Mq*cq_**2*(1 + cq_**-2)**2/mgsq_}
Kcoef = {}
for eq_, ex_ in rV3.items():
    if eq_ == "43":                                        # m1 = 0: beta1 + beta2 c = 0
        ex_ = ex_.subs(b1_, -b2_*cq_)
        sub = {msq: sp.solve(sp.Eq(mgsq_.subs(b1_, -b2_*cq_), 1/lamq**2), msq)[0]}
    else:
        ex_ = ex_.subs(b3_, b1_); sub = {msq: sp.solve(sp.Eq(mgsq_.subs(b3_, b1_), 1/lamq**2), msq)[0]}
    Kcoef[eq_] = sp.simplify((ex_.subs(sub)/(Mq*lamq**2)).subs(cq_, 1))/2      # in units of r_S lambda^2
m12_same = sp.simplify((m1sq_ - m2sq_).subs(b3_, b1_).subs(cq_, 1)) == 0
check("J1: in r_V^3 = K r_S lambda^2 at c = 1: the palindromic vacuum (beta3 = beta1, so m1 = m2 for any beta1, beta2) "
      "gives K = 1 (eq. 40) and 15 (eq. 41); the m1 = 0 form (eq. 43, used at verify/phase_space_diameter.py:383) gives "
      "K = 2, and m1 = 0 = m2 there would make X massless", Kcoef == {"40": 1, "41": 15, "43": 2} and m12_same,
      f"{Kcoef}")
rS1 = 2*G*1.0/C**2
rv1 = {K_: (K_*rS1*(50e-6)**2)**(1/3) for K_ in (1, 2, 15)}
check("J2: a 1 kg mass with lambda_X = 50 um: r_V = 1.55e-12 m (eq. 40), 3.82e-12 m (eq. 41) ('1.5-3.8e-12 m'), "
      "1.95e-12 m (eq. 43); under eq. 41 round(log10 r_V) = -11, so the rounding check at "
      "verify/phase_space_diameter.py:384 would fail; lab masses stay unscreened",
      r3(rv1[1]) == 1.55e-12 and r3(rv1[15]) == 3.82e-12 and r3(rv1[2]) == 1.95e-12 and round(log10(rv1[15])) == -11 and
      round(log10(rv1[2])) == -12 and rv1[15] < 1e-9, f"{rv1[1]:.3e}, {rv1[15]:.3e}, {rv1[2]:.3e}")
GMc2_sun = G*1.98847e30/C**2
win = {(K_, nm_): sqrt((a_*AU)**3/(2*K_*GMc2_sun))/PC for K_ in (1, 15) for nm_, a_ in (("Saturn", 9.5826), ("Pluto", 39.482))}
check("J3: if this branch screens at all (open), the Sun's Vainshtein radius covers Saturn for lambda > 1.024 pc "
      "(eq. 40) or 0.264 pc (eq. 41), Pluto for 8.560 or 2.210 pc: the windows open at ~0.3-9 pc and close at "
      "Enander-Mortsell's 4.4 kpc (their published linear-theory lensing window, 4.4 kpc-4.4 Mpc at u ~ 1 [T][S])",
      [round(win[(1, "Saturn")], 3), round(win[(15, "Saturn")], 3), round(win[(1, "Pluto")], 3),
       round(win[(15, "Pluto")], 3)] == [1.024, 0.264, 8.560, 2.210] and round(win[(15, "Saturn")], 1) == 0.3 and
      round(win[(1, "Pluto")]) == 9)

# ======================================================================================================
print(f"\nwall time {time.time() - T_START:.1f} s")
if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — every number of the velocity-gated-gravity investigation reproduces.")
