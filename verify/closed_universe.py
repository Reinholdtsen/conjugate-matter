#!/usr/bin/env python3
"""
closed_universe.py — every number of the closed-universe investigation (notes/closed-universe.md), recomputed
and checked. The work was done outside the repository in executed scripts; this file ports them (it imports
none of them) and is self-contained. The ported sources are named at each section. Paths such as
closed/dynamics/cc.py name scripts in the investigation's work folder, which is not in the repository; its
record (the analyses, the verdicts, the critic's scripts and grid.csv) is in review/closed-universe/.

    .venv/bin/python verify/closed_universe.py

Exit code 1 if any check fails. Anchors come first and are independent of the investigation: CODATA 2018's
published Planck units and the PDG photon density; the exact closed dust and dust + radiation solutions, which
the integrator must reproduce; the pendulum average that the oscillating field's averaged description uses,
against mpmath's elliptic integrals and a direct integration; the textbook spectrum of the S^3 Laplacian; the
Poincare dodecahedral space's first scalar mode (Aurich et al. 2005) from binary-icosahedral characters; the
published curvature values of DESI DR2 and of Akrami, Alestas and Nesseris; Lee et al. 2020's published
torsion-balance ranges, which the interpolation for X's range must reproduce; and the calibration of the
background fit against two published DESI DR2 results. Two literature anchors sit inside section D, where the
derivation they test is made: von Strauss et al. 2012's quartic for the bimetric ratio and Konnig 2015's
gradient-instability frequency. Section F has two of its own: the winding numbers of SU(2)'s fundamental (|W| = 1) and
of SO(3) in SO(4) acting on R^4 (|W| = 4), with Bott periodicity's stable values for U/O as the table its homotopy
groups must match. Everything else after the anchors is a regression check: it reproduces the
investigation's own numbers and derivations, and is not independent of them.

Inputs: CODATA 2018 constants; H0 = 67.4 km/s/Mpc, Omega_m = 0.315, T_CMB = 2.7255 K, three massless neutrinos
at (4/11)^(1/3) T; closed means Omega_k < 0, curvature radius today R0 = c/(H0 sqrt|Omega_k|). Dark energy is
the field tau with V = V0 [1 + cos(tau/f)], f in units of the reduced Planck mass, thawing from rest at
theta_i (measured from the hilltop), V0 shot so that H(a = 1) = H0 and theta_i shot to a target w0 = w(a = 1).
Bimetric sector: Hassan-Rosen, palindromic beta_n = beta_(4-n), beta0 = -4 beta1 - 3 beta2, M_f = M_g.
Other inputs are typed in with their sources where they are used.

Runtime is about 16 s: the closed histories run only the representative case, the two grid extremes
and the over-constraint pair; the background fit uses a Levenberg-Marquardt minimizer in place of the original
Nelder-Mead and reproduces its printed profile to every digit.
"""
import sys
import time
from math import pi, sqrt, log, log10, exp, sin, cos, atan, asinh, erf, isfinite
from itertools import combinations
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
def r3(x):
    """x to three significant figures"""
    return float(f"{x:.3g}")
def r4(x):
    return float(f"{x:.4g}")

# CODATA 2018 (h, c, k_B, e exact; G measured)
HBAR = 6.62607015e-34/(2*pi); H_PL = 2*pi*HBAR; C = 299792458.0; G = 6.67430e-11
KB = 1.380649e-23; EV = 1.602176634e-19; GEV = 1e9*EV
A_BOHR = 5.29177210903e-11; ALPHA = 7.2973525693e-3
L_P = sqrt(HBAR*G/C**3); M_P = sqrt(HBAR*C/G); E_P = M_P*C**2; T_P = E_P/KB; T_PL = L_P/C
HBARC_EVM = HBAR*C/EV                                  # 1.973269804e-7 eV m
MPC = 3.0856775814913673e22; GPC = 1e3*MPC
H0 = 67.4e3/MPC; OM = 0.315; T0 = 2.7255
ZETA3 = 1.2020569031595942
RHO_CRIT = 3*H0**2/(8*pi*G)
RHO_GAMMA = (pi**2/15)*(KB*T0)**4/(HBAR*C)**3/C**2
NU1 = (7/8)*(4/11)**(4/3)                              # one massless neutrino species relative to photons
OR = RHO_GAMMA*(1 + 3*NU1)/RHO_CRIT
OGAM = RHO_GAMMA/RHO_CRIT
N_GAMMA0 = 2*ZETA3/pi**2*(KB*T0/(HBAR*C))**3
YR = 3.15576e7; GYR = 1e9*YR                           # Julian year
T_H0_GYR = 1/H0/GYR
L_H = C/H0
def R0_of(ok):
    """curvature radius today, c/(H0 sqrt|Omega_k|)"""
    return C/(H0*sqrt(ok))
def ODE0(ok):
    """Omega_DE,0 = 1 - Omega_m - Omega_r + |Omega_k|"""
    return 1 - OM - OR + ok


# ======================================================================================================
# Closed FLRW with the field tau (port of closed/dynamics/cc.py, solve.py; trimmed to the quantities checked
# here, with the same step control). Units: reduced Planck mass 1, c = 1, H0 = 1, a0 = 1; densities in
# Mbar_P^2 H0^2 (critical density today = 3); Kc = |Omega_k|; H^2 = rho/3 - Kc/a^2. chi = sqrt(Kc) int dt/a is
# the conformal time in radians of the 3-sphere. The field is stored as delta = tau - pi f, so
# V = 2 V0 sin^2(delta/2f) >= 0. Dormand-Prince 5(4) with event location. Three forms: N-form (independent
# ln a) while H^2 is not small; t-form (H by its second-order equation) through H = 0; and, once the
# oscillation is adiabatic (omega/sqrt(S) > R), the exact pendulum average of the field (<w> from complete
# elliptic integrals), validated in the original's validate.py. The crunch is integrated with the full field.
# ======================================================================================================
C2_, C3_, C4_, C5_ = 1/5, 3/10, 4/5, 8/9
A21 = 1/5
A31, A32 = 3/40, 9/40
A41, A42, A43 = 44/45, -56/15, 32/9
A51, A52, A53, A54 = 19372/6561, -25360/2187, 64448/6561, -212/729
A61, A62, A63, A64, A65 = 9017/3168, -355/33, 46732/5247, 49/176, -5103/18656
B1, B3, B4, B5, B6 = 35/384, 500/1113, 125/192, -2187/6784, 11/84
E1, E3, E4, E5, E6, E7 = 71/57600, -71/16695, 71/1920, -17253/339200, 22/525, -1/40

def _stages(fun, x, y, k1, h):
    y2 = [yi + h*A21*a for yi, a in zip(y, k1)]
    k2 = fun(x + C2_*h, y2)
    y3 = [yi + h*(A31*a + A32*b) for yi, a, b in zip(y, k1, k2)]
    k3 = fun(x + C3_*h, y3)
    y4 = [yi + h*(A41*a + A42*b + A43*c) for yi, a, b, c in zip(y, k1, k2, k3)]
    k4 = fun(x + C4_*h, y4)
    y5 = [yi + h*(A51*a + A52*b + A53*c + A54*d) for yi, a, b, c, d in zip(y, k1, k2, k3, k4)]
    k5 = fun(x + C5_*h, y5)
    y6 = [yi + h*(A61*a + A62*b + A63*c + A64*d + A65*e) for yi, a, b, c, d, e in zip(y, k1, k2, k3, k4, k5)]
    k6 = fun(x + h, y6)
    yn = [yi + h*(B1*a + B3*c + B4*d + B5*e + B6*g) for yi, a, c, d, e, g in zip(y, k1, k3, k4, k5, k6)]
    return yn, k3, k4, k5, k6

class Event:
    """g(x, y) crossing zero; direction +1 upward only, -1 downward only; callback(x, y) at the crossing"""
    def __init__(self, name, g, direction=0, terminal=False, callback=None, xtol=1e-14):
        self.name, self.g, self.direction, self.terminal = name, g, direction, terminal
        self.callback, self.xtol = callback, xtol

def _locate(fun, x, y, k1, h, g, g0, g1, xtol=1e-14):
    lo, hi, glo, ghi = 0.0, h, g0, g1
    side = 0
    hh = h
    for _ in range(80):
        hh = (lo*ghi - hi*glo)/(ghi - glo)
        gm = g(x + hh, _stages(fun, x, y, k1, hh)[0])
        if gm == 0 or abs(hi - lo) <= 1e-15*(abs(x) + abs(h)):
            return hh
        if (gm < 0) == (glo < 0):
            lo, glo = hh, gm
            if side == -1:
                ghi *= 0.5
            side = -1
        else:
            hi, ghi = hh, gm
            if side == +1:
                glo *= 0.5
            side = +1
        if abs(hi - lo) <= xtol*abs(h):
            break
    return hh

def dp5(fun, x, y, xend, h, scale, events=(), maxsteps=50_000_000):
    """integrate y' = fun(x, y) towards xend; scale(y, yn) gives per-component absolute tolerances (None =
    excluded). Returns (x, y, reason, nsteps)."""
    n = len(y)
    sgn = 1.0 if xend >= x else -1.0
    h = sgn*abs(h)
    k1 = fun(x, y)
    gold = [ev.g(x, y) for ev in events]
    nsteps = 0
    while True:
        if nsteps >= maxsteps:
            return x, y, 'maxsteps', nsteps
        last = False
        if sgn*(x + h - xend) >= 0:
            h = xend - x
            last = True
        try:
            yn, k3, k4, k5, k6 = _stages(fun, x, y, k1, h)
            k7 = fun(x + h, yn)
            sc = scale(y, yn)
            s2, m = 0.0, 0
            for i in range(n):
                if sc[i] is None:
                    continue
                e = h*(E1*k1[i] + E3*k3[i] + E4*k4[i] + E5*k5[i] + E6*k6[i] + E7*k7[i])/sc[i]
                s2 += e*e
                m += 1
            err = sqrt(s2/m)
            if not isfinite(err):
                raise ValueError
        except (ValueError, OverflowError, ZeroDivisionError):
            h *= 0.25
            if abs(h) < 1e-14*max(abs(x), 1e-300) or abs(h) < 1e-300:
                return x, y, 'stepsize', nsteps
            continue
        if err <= 1.0:
            stop = None
            if events:
                gnew = [ev.g(x + h, yn) for ev in events]
                hits = []
                for j, ev in enumerate(events):
                    g0, g1 = gold[j], gnew[j]
                    if (g0 < 0 <= g1 and ev.direction >= 0) or (g0 > 0 >= g1 and ev.direction <= 0):
                        if g0 == 0:
                            continue
                        hh = _locate(fun, x, y, k1, h, ev.g, g0, g1, ev.xtol)
                        yy = _stages(fun, x, y, k1, hh)[0] if hh != 0 else list(y)
                        hits.append((abs(hh), ev, x + hh, yy))
                hits.sort(key=lambda r: r[0])
                for _, ev, xe, ye in hits:
                    if ev.callback is not None:
                        ev.callback(xe, ye)
                    if ev.terminal:
                        stop = (ev.name, xe, ye)
                        break
                gold = gnew
            if stop is not None:
                return stop[1], stop[2], stop[0], nsteps + 1
            x, y, k1 = x + h, yn, k7
            nsteps += 1
            if last:
                return x, y, 'end', nsteps
            fac = 5.0 if err == 0 else min(5.0, max(0.2, 0.9*err**-0.2))
        else:
            fac = max(0.2, 0.9*err**-0.2)
        h = sgn*abs(h*fac)
        if abs(h) < 1e-14*max(abs(x), 1e-300) or abs(h) < 1e-300:
            return x, y, 'stepsize', nsteps

def ellipKE(m):
    """complete elliptic integrals K(m), E(m), parameter m = k^2 in [0, 1), by the arithmetic-geometric mean"""
    a, b = 1.0, sqrt(1.0 - m)
    csum, p2 = 0.5*m, 0.5
    for _ in range(40):
        cn = 0.5*(a - b)
        if cn <= 1e-17*a:
            break
        a, b = 0.5*(a + b), sqrt(a*b)
        p2 *= 2.0
        csum += p2*cn*cn
    K = pi/(2.0*a)
    return K, K*(1.0 - csum)

def wbar(m):
    """oscillation-averaged w of a canonical field in V0(1 - cos x) at energy 2 V0 m: 2(E/K - 1 + m)/m - 1"""
    if m < 1e-3:
        return -m*(1/8 + m*(1/16 + m*(41/1024 + m*59/2048)))
    K, E = ellipKE(m)
    return 2.0*(E/K - 1.0 + m)/m - 1.0

def omega_osc(m, mass):
    if m >= 1.0:
        return 0.0
    if m < 1e-6:
        return mass*(1 - m/4 - 5*m*m/64)
    return pi*mass/(2.0*ellipKE(m)[0])

def t_rm(a, om, orr):
    """cosmic time since the bang for H^2 = orr/a^4 + om/a^3 (exact)"""
    x = om*a
    if x < 1e-6*orr:
        return a*a/(2*sqrt(orr))*(1 - 2*x/(3*orr))
    return 2.0/(3.0*om*om)*((x - 2*orr)*sqrt(orr + x) + 2*orr**1.5)

def chi_rm(a, om, orr, sqK):
    return sqK*2.0/om*(sqrt(orr + om*a) - sqrt(orr))

class Model:
    def __init__(self, Kc, f, V0, theta_i, om=OM, orr=OR):
        self.Kc, self.f, self.V0, self.theta_i = Kc, f, V0, theta_i
        self.om, self.orr = om, orr
        self.sqK = sqrt(abs(Kc))
        self.mass = sqrt(V0)/f if V0 > 0 else 0.0
        self.delta_i = theta_i*f - pi*f

    def V(self, d):
        s = sin(0.5*d/self.f)
        return 2.0*self.V0*s*s

    def dV(self, d):
        return self.V0/self.f*sin(d/self.f)

    def Eosc(self, d, p):
        s = sin(0.5*d/self.f)
        return 0.5*p*p + 2.0*self.V0*s*s

    def rhs_NF(self, sgn):                       # y = [delta, pi, t, chi], x = ln a
        om3, or3, Kc, sqK, V0, f = 3*self.om, 3*self.orr, self.Kc, self.sqK, self.V0, self.f
        V0f = V0/f
        def fun(N, y):
            d, p = y[0], y[1]
            e1 = exp(-N); e2 = e1*e1; e3 = e2*e1
            s = sin(0.5*d/f)
            rho = om3*e3 + or3*e3*e1 + 0.5*p*p + 2.0*V0*s*s
            iH = 1.0/(sgn*sqrt(rho/3.0 - Kc*e2))
            return [p*iH, -3.0*p - V0f*sin(d/f)*iH, iH, sqK*e1*iH]
        return fun

    def rhs_TF(self):                            # y = [ln a, H, delta, pi, chi], x = t
        om3, or3, Kc, sqK, V0, f = 3*self.om, 3*self.orr, self.Kc, self.sqK, self.V0, self.f
        V0f = V0/f
        def fun(t, y):
            N, H, d, p = y[0], y[1], y[2], y[3]
            e1 = exp(-N); e2 = e1*e1; e3 = e2*e1
            rpp = om3*e3 + 4.0/3.0*or3*e3*e1 + p*p
            return [H, -0.5*rpp + Kc*e2, p, -3.0*H*p - V0f*sin(d/f), sqK*e1]
        return fun

    def rhs_NA(self, sgn):                       # y = [u = ln(rho_tau a^3), t, chi], x = ln a
        om3, or3, Kc, sqK, V0 = 3*self.om, 3*self.orr, self.Kc, self.sqK, self.V0
        def fun(N, y):
            e1 = exp(-N); e2 = e1*e1; e3 = e2*e1
            rt = exp(y[0])*e3
            iH = 1.0/(sgn*sqrt((om3*e3 + or3*e3*e1 + rt)/3.0 - Kc*e2))
            return [-3.0*wbar(rt/(2.0*V0)), iH, sqK*e1*iH]
        return fun

    def rhs_TA(self):                            # y = [ln a, H, u, chi], x = t
        om3, or3, Kc, sqK, V0 = 3*self.om, 3*self.orr, self.Kc, self.sqK, self.V0
        def fun(t, y):
            N, H, u = y[0], y[1], y[2]
            e1 = exp(-N); e2 = e1*e1; e3 = e2*e1
            rt = exp(u)*e3
            wb = wbar(rt/(2.0*V0))
            rpp = om3*e3 + 4.0/3.0*or3*e3*e1 + (1.0 + wb)*rt
            return [H, -0.5*rpp + Kc*e2, -3.0*wb*H, sqK*e1]
        return fun

    def parts(self, N, d, p):
        e1 = exp(-N); e3 = e1**3
        return 3*self.om*e3, 3*self.orr*e3*e1, 0.5*p*p, self.V(d)

    def S_full(self, N, d, p):
        rm, rr, kin, V = self.parts(N, d, p)
        return (rm + rr + kin + abs(V))/3.0 + abs(self.Kc)*exp(-2*N)

    def S_avg(self, N, u):
        e1 = exp(-N); e3 = e1**3
        return (3*self.om*e3 + 3*self.orr*e3*e1 + exp(u)*e3)/3.0 + abs(self.Kc)*exp(-2*N)

    def H2_full(self, N, d, p):
        rm, rr, kin, V = self.parts(N, d, p)
        return (rm + rr + kin + V)/3.0 - self.Kc*exp(-2*N)

    def H2_avg(self, N, u):
        e1 = exp(-N); e3 = e1**3
        return (3*self.om*e3 + 3*self.orr*e3*e1 + exp(u)*e3)/3.0 - self.Kc*exp(-2*N)

    def adiab_full(self, N, d, p):
        if self.V0 <= 0:
            return 0.0
        m = self.Eosc(d, p)/(2*self.V0)
        return omega_osc(m, self.mass)/sqrt(self.S_full(N, d, p)) if m < 1 else 0.0

    def adiab_avg(self, N, u):
        m = exp(u - 3*N)/(2*self.V0)
        return omega_osc(m, self.mass)/sqrt(self.S_avg(N, u))

    def sc_field(self, d, p, rtol):
        E = self.Eosc(d, p)
        ampd = self.f*sqrt(2*E/self.V0) if self.V0 > 0 else 1.0
        return rtol*(abs(d) + ampd) + 1e-300, rtol*(abs(p) + sqrt(2*E)) + 1e-300

    def sc_NF(self, rtol):
        def sc(y, yn):
            sd, sp_ = self.sc_field(y[0], y[1], rtol)
            return [sd, sp_, rtol*max(abs(y[2]), abs(yn[2])) + 1e-300, rtol*max(abs(y[3]), abs(yn[3])) + 1e-300]
        return sc

    def sc_TF(self, rtol):
        def sc(y, yn):
            sd, sp_ = self.sc_field(y[2], y[3], rtol)
            return [rtol*(abs(y[0]) + 1.0), rtol*sqrt(self.S_full(y[0], y[2], y[3])), sd, sp_,
                    rtol*max(abs(y[4]), abs(yn[4])) + 1e-300]
        return sc

    def sc_NA(self, rtol):
        return lambda y, yn: [rtol, rtol*max(abs(y[1]), abs(yn[1])) + 1e-300, rtol*max(abs(y[2]), abs(yn[2])) + 1e-300]

    def sc_TA(self, rtol):
        return lambda y, yn: [rtol*(abs(y[0]) + 1.0), rtol*sqrt(self.S_avg(y[0], y[2])), rtol,
                              rtol*max(abs(y[3]), abs(yn[3])) + 1e-300]

    def to_today(self, rtol=1e-10, a_i=1e-6, events=()):
        """N-form from a_i (field at rest, radiation + matter era) to a = 1"""
        y = [self.delta_i, 0.0, t_rm(a_i, self.om, self.orr), chi_rm(a_i, self.om, self.orr, self.sqK)]
        x, y, why, ns = dp5(self.rhs_NF(+1.0), log(a_i), y, 0.0, 0.05, self.sc_NF(rtol), events)
        if why != 'end':
            raise RuntimeError('to_today: ' + why)
        return y

    def w_today(self, d, p):
        """w(a = 1) and the Taylor w_a = -dw/da(1) (H(1) = 1)"""
        kin, V = 0.5*p*p, self.V(d)
        rho = kin + V
        if rho == 0:
            return float('nan'), float('nan')
        dwdt = (-6.0*p*p*V - 2.0*self.dV(d)*p*rho)/rho**2
        return (kin - V)/rho, -dwdt

def shoot_V0(Kc, f, theta_i, rtol=1e-10):
    """V0 with H(a = 1) = 1: smallest root on a geometric scan up from just below the frozen-field value"""
    Otau = 1.0 - OM - OR + Kc
    def g(V0):
        m = Model(Kc, f, V0, theta_i)
        y = m.to_today(rtol)
        return (0.5*y[1]**2 + m.V(y[0]))/3.0 - Otau
    Vtop = 1 + cos(theta_i)
    Vguess = 3*Otau/Vtop
    lo = 0.98*Vguess
    glo = g(lo)
    if glo > 0:
        lo = 0.5*Vguess
        glo = g(lo)
        if glo > 0:
            return None
    for _ in range(80):
        hi = lo*1.04
        ghi = g(hi)
        if ghi > 0:
            break
        lo, glo = hi, ghi
    else:
        return None
    side = 0
    for _ in range(100):
        x = (lo*ghi - hi*glo)/(ghi - glo)
        gx = g(x)
        if abs(gx) < 1e-13 or abs(hi - lo) < 1e-15*x:
            return x
        if gx < 0:
            lo, glo = x, gx
            if side == -1:
                ghi *= 0.5
            side = -1
        else:
            hi, ghi = x, gx
            if side == +1:
                glo *= 0.5
            side = +1
    return x

def illinois(g, lo, hi, glo, ghi, xtol=1e-12, gtol=1e-12, itmax=100):
    side = 0
    x = lo
    for _ in range(itmax):
        x = (lo*ghi - hi*glo)/(ghi - glo)
        gx = g(x)
        if abs(gx) < gtol or abs(hi - lo) < xtol*max(1.0, abs(x)):
            return x
        if (gx < 0) == (glo < 0):
            lo, glo = x, gx
            if side == -1:
                ghi *= 0.5
            side = -1
        else:
            hi, ghi = x, gx
            if side == +1:
                glo *= 0.5
            side = +1
    return x

def w0_of(Kc, f, th):
    V0 = shoot_V0(Kc, f, th)
    if V0 is None:
        return None, None
    m = Model(Kc, f, V0, th)
    y = m.to_today()
    return m.w_today(y[0], y[1])[0], V0

def solve_theta(Kc, f, w0t, th_max=3.1):
    """smallest theta_i with w(1) = w0t (thawing branch): geometric scan upward from 1e-3, then Illinois"""
    th, prev = 1e-3, None
    g = lambda t_: w0_of(Kc, f, t_)[0] - w0t
    while th < th_max:
        w, V0 = w0_of(Kc, f, th)
        if w is None:
            return None
        if w >= w0t:
            return None if prev is None else illinois(g, prev[0], th, prev[1] - w0t, w - w0t, xtol=1e-13, gtol=1e-11)
        prev = (th, w)
        th = th*1.15 if th < 0.1 else th + 0.05
    return None

def _crunch_end(m, N, st):
    """remaining time and conformal time from a_end to a = 0 for the local power law"""
    d, p = st[0], st[1]
    rm, rr, kin, V = m.parts(N, d, p)
    rho = rm + rr + kin + V
    H = -sqrt(m.H2_full(N, d, p))
    weff = (rr/3 + kin - V)/rho
    q = 2.0/(3.0*(1.0 + weff))
    trem = q/abs(H)
    chirem = m.sqK*trem/(exp(N)*(1 - q)) if q < 1 else float('nan')
    return dict(t=st[2] + trem, chi=st[3] + chirem, weff_end=weff, kin_frac=kin/rho, a_end=exp(N))

def _field_from_Q(m, Q, H, phase):
    """field state with first-order averaged energy Q at expansion rate H and oscillation phase 'phase'"""
    mm = Q/(2*m.V0)
    om_ = omega_osc(mm, m.mass)
    def F(A):
        d, p = A*cos(phase), -om_*A*sin(phase)
        return m.Eosc(d, p) + 1.5*H*d*p - Q
    A0 = sqrt(2*Q)/m.mass
    lo, hi = 0.5*A0, 2.0*A0
    flo, fhi = F(lo), F(hi)
    A = illinois(F, lo, hi, flo, fhi, xtol=1e-15, gtol=1e-16*Q) if flo*fhi < 0 else A0
    return A*cos(phase), -om_*A*sin(phase)

def _contract_from_avg(m, avg_state, phase, rtol, a_end, s_sw):
    """from the averaged contracting state to the crunch with the full field, at oscillation phase 'phase'"""
    kind, X, st = avg_state
    if kind == 'T':
        N, H, u, chi = st
        Q = exp(u - 3*N)
        d, p = _field_from_Q(m, Q, H, phase)
        H = -sqrt(max(m.H2_full(N, d, p), 0.0))
        evs = [Event('S2', lambda x, yy: (yy[1]*yy[1]/m.S_full(yy[0], yy[2], yy[3]) - s_sw) if yy[1] < 0 else -1.0,
                     +1, True)]
        x, yy, why, ns = dp5(m.rhs_TF(), X, [N, H, d, p, chi], 1e300, 1e-3, m.sc_TF(rtol), evs)
        if why != 'S2':
            raise RuntimeError('contraction (t-form) ended: ' + why)
        N = yy[0]
        y = [yy[2], yy[3], x, yy[4]]
    else:
        N = X
        u, t, chi = st
        H = -sqrt(m.H2_avg(N, u))
        d, p = _field_from_Q(m, exp(u - 3*N), H, phase)
        y = [d, p, t, chi]
    x, yy, why, ns = dp5(m.rhs_NF(-1.0), N, y, log(a_end), -0.01, m.sc_NF(rtol))
    if why != 'end':
        raise RuntimeError('contraction ended: ' + why)
    return _crunch_end(m, x, yy)

def history(m, rtol=1e-10, R=1000.0, s_sw=0.2, full=False, a_end=1e-10):
    """big bang -> today -> turnaround -> crunch (port of cc.history, one oscillation phase at the crunch)"""
    res = dict(first_min=None)
    y = m.to_today(rtol)
    res['w0'], res['waT'] = m.w_today(y[0], y[1])
    res['t0'], res['chi0'] = y[2], y[3]
    turned = [False]
    def dz_cb(x, yy):
        if res['first_min'] is None:
            res['first_min'] = dict(t=yy[2], a=exp(x))
    def turn_full(xe, ye):
        if turned[0]:
            return
        turned[0] = True
        N_, H_, d_, p_ = ye[0], ye[1], ye[2], ye[3]
        rm, rr, kin, V = m.parts(N_, d_, p_)
        mm = m.Eosc(d_, p_)/(2*m.V0) if m.V0 > 0 else float('nan')
        res['turn'] = dict(t=xe, a=exp(N_), chi=ye[4], rho_tau=kin + V, Od=(kin + V)*exp(3*N_)/3.0, m=mm,
                           wbar=wbar(mm) if m.V0 > 0 and mm < 1 else float('nan'),
                           constraint=(H_*H_ + m.Kc*exp(-2*N_))/((rm + rr + kin + V)/3) - 1)
    def turn_avg(xe, ye):
        if turned[0]:
            return
        turned[0] = True
        N_, H_, u_ = ye[0], ye[1], ye[2]
        rt = exp(u_ - 3*N_)
        mm = rt/(2*m.V0)
        e1 = exp(-N_)
        rm, rr = 3*m.om*e1**3, 3*m.orr*e1**4
        res['turn'] = dict(t=xe, a=exp(N_), chi=ye[3], rho_tau=rt, Od=exp(u_)/3.0, m=mm, wbar=wbar(mm),
                           constraint=(H_*H_ + m.Kc*e1**2)/((rm + rr + rt)/3) - 1)
    seg, N, state, tcur = 'NF+', 0.0, list(y), None
    while True:
        if seg == 'NF+':
            if m.H2_full(N, state[0], state[1])/m.S_full(N, state[0], state[1]) < s_sw:
                tcur = state[2]
                state = [N, sqrt(max(m.H2_full(N, state[0], state[1]), 0.0)), state[0], state[1], state[3]]
                seg = 'TF'
                continue
            evs = [Event('S', lambda x, yy: m.H2_full(x, yy[0], yy[1])/m.S_full(x, yy[0], yy[1]) - s_sw, -1, True)]
            if not full:
                evs.append(Event('A', lambda x, yy: m.adiab_full(x, yy[0], yy[1]) - R, +1, True))
            evs.append(Event('dz', lambda x, yy: yy[0], +1, callback=dz_cb, xtol=1e-9))
            N, st, why, ns = dp5(m.rhs_NF(+1.0), N, state, 230.0, 0.01, m.sc_NF(rtol), evs)
            if why == 'S':
                tcur = st[2]
                state = [N, sqrt(max(m.H2_full(N, st[0], st[1]), 0.0)), st[0], st[1], st[3]]
                seg = 'TF'
            elif why == 'A':
                d, p = st[0], st[1]
                Q = m.Eosc(d, p) + 1.5*sqrt(m.H2_full(N, d, p))*d*p
                state = [log(Q) + 3*N, st[2], st[3]]
                seg = 'NA+'
            else:
                raise RuntimeError('NF+ ended: ' + why)
        elif seg == 'NF-':
            N, st, why, ns = dp5(m.rhs_NF(-1.0), N, state, log(a_end), -0.01, m.sc_NF(rtol))
            if why != 'end':
                raise RuntimeError('NF- ended: ' + why)
            res['crunch'] = _crunch_end(m, N, st)
            break
        elif seg == 'NA+':
            evs = [Event('S', lambda x, yy: m.H2_avg(x, yy[0])/m.S_avg(x, yy[0]) - s_sw, -1, True)]
            N, st, why, ns = dp5(m.rhs_NA(+1.0), N, state, 230.0, 0.01, m.sc_NA(rtol), evs)
            if why != 'S':
                raise RuntimeError('NA+ ended: ' + why)
            tcur = st[1]
            state = [N, sqrt(max(m.H2_avg(N, st[0]), 0.0)), st[0], st[2]]
            seg = 'TA'
        elif seg == 'NA-':
            evs = [Event('A-', lambda x, yy: m.adiab_avg(x, yy[0]) - R, -1, True)]
            N, st, why, ns = dp5(m.rhs_NA(-1.0), N, state, log(a_end), -0.01, m.sc_NA(rtol), evs)
            if why != 'A-':
                raise RuntimeError('NA- ended: ' + why)
            res['avg_state'] = ('N', N, list(st))
            break
        elif seg == 'TF':
            evs = [Event('turn', lambda x, yy: yy[1], -1, callback=turn_full),
                   Event('S2', lambda x, yy: (yy[1]*yy[1]/m.S_full(yy[0], yy[2], yy[3]) - s_sw) if yy[1] < 0 else -1.0,
                         +1, True)]
            if not full:
                evs.append(Event('A', lambda x, yy: (m.adiab_full(yy[0], yy[2], yy[3]) - R) if yy[1] > 0 else -1.0,
                                 +1, True))
            x, yy, why, ns = dp5(m.rhs_TF(), tcur, state, 1e300, 1e-3*(1 + tcur), m.sc_TF(rtol), evs)
            if why == 'S2':
                N = yy[0]
                state = [yy[2], yy[3], x, yy[4]]
                seg = 'NF-'
            elif why == 'A':
                N, H, d, p = yy[0], yy[1], yy[2], yy[3]
                Q = m.Eosc(d, p) + 1.5*H*d*p
                H = sqrt(max(m.H2_avg(N, log(Q) + 3*N), 0.0))
                state = [N, H, log(Q) + 3*N, yy[4]]
                tcur = x
                seg = 'TA'
            else:
                raise RuntimeError('TF ended: ' + why)
        elif seg == 'TA':
            evs = [Event('turn', lambda x, yy: yy[1], -1, callback=turn_avg),
                   Event('S2', lambda x, yy: (yy[1]*yy[1]/m.S_avg(yy[0], yy[2]) - s_sw) if yy[1] < 0 else -1.0,
                         +1, True),
                   Event('A-', lambda x, yy: (m.adiab_avg(yy[0], yy[2]) - R) if yy[1] < 0 else 1.0, -1, True)]
            x, yy, why, ns = dp5(m.rhs_TA(), tcur, state, 1e300, 1e-3*(1 + tcur), m.sc_TA(rtol), evs)
            if why == 'S2':
                N = yy[0]
                state = [yy[2], x, yy[3]]
                seg = 'NA-'
            elif why == 'A-':
                res['avg_state'] = ('T', x, list(yy))
                break
            else:
                raise RuntimeError('TA ended: ' + why)
    if 'crunch' not in res:
        res['crunch'] = _contract_from_avg(m, res['avg_state'], 0.0, rtol, a_end, s_sw)
    return res


# ======================================================================================================
# Background fit (port of closed/critic/f_corridor_curvature_fit.py): DESI DR2 BAO (arXiv:2503.14738,
# Table 'tab:alphas', typed in by the critic) plus DESI's compressed CMB prior on (theta_*, omega_b, omega_bc);
# r_d from DESI's fitting formula; theta_* = r_*/D_M(z_*) with z_* from Hu-Sugiyama, calibrated so that DESI's
# CMB-only LCDM point (Omega_m = 0.3169, H0 = 67.14) gives 100 theta_* = 1.04110. No supernovae: a background
# reduction. Profiles in Omega_K, minimized over (omega_b, omega_bc, h, dark-energy parameters). The original's
# Nelder-Mead is replaced by Levenberg-Marquardt on the 16 whitened residuals (box bounds by an active set).
# ======================================================================================================
FIT_CKMS = 299792.458
FIT_OMG = 2.4728e-5                     # omega_gamma for T0 = 2.7255 K
FIT_NEFF = 3.044
FIT_OMR = FIT_OMG*(1 + 0.22711*FIT_NEFF)
FIT_OMNU = 0.06/93.14                   # one 0.06 eV neutrino, matter at late times
BAO_2D = [(0.510, 13.588, 0.167, 21.863, 0.425, -0.459), (0.706, 17.351, 0.177, 19.455, 0.330, -0.404),
          (0.934, 21.576, 0.152, 17.641, 0.193, -0.416), (1.321, 27.601, 0.318, 14.176, 0.221, -0.434),
          (1.484, 30.512, 0.760, 12.817, 0.516, -0.500), (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]
BAO_DV = (0.295, 7.942, 0.075)
MU_CMB = np.array([1.04110e-2, 0.02223, 0.14208])
C_CMB = 1e-9*np.array([[0.006621, 0.12444, -1.1929], [0.12444, 21.344, -94.001], [-1.1929, -94.001, 1488.4]])
W_CMB = np.linalg.cholesky(np.linalg.inv(C_CMB)).T
W_BAO = [np.linalg.cholesky(np.linalg.inv(np.array([[s1**2, r*s1*s2], [r*s1*s2, s2**2]]))).T
         for (_, _, s1, _, s2, r) in BAO_2D]
ZQ = np.array([b[0] for b in BAO_2D] + [BAO_DV[0]])
LNZ = np.linspace(0, np.log(1 + 1200.0), 6000)
ZG = np.expm1(LNZ)
DLNZ = np.diff(LNZ)

def fit_E2(z, h, om_m, Ok, de):
    a = 1/(1 + z)
    Om, Or = om_m/h**2, FIT_OMR/h**2
    fde = 1.0 if de is None else a**(-3*(1 + de[0] + de[1]))*np.exp(-3*de[1]*(1 - a))
    return Or*(1 + z)**4 + Om*(1 + z)**3 + Ok*(1 + z)**2 + (1 - Om - Or - Ok)*fde

def fit_zstar(ob, om):
    g1 = 0.0783*ob**-0.238/(1 + 39.5*ob**0.763)
    g2 = 0.560/(1 + 21.1*ob**1.81)
    return 1048*(1 + 0.00124*ob**-0.738)*(1 + g1*om**g2)

def fit_rstar(ob, om, zs):
    lz = np.linspace(np.log(1 + zs), np.log(1 + 1e8), 4000)
    z = np.expm1(lz)
    cs = FIT_CKMS/np.sqrt(3*(1 + 3*ob/(4*FIT_OMG)/(1 + z)))
    return np.trapezoid(cs/(100*np.sqrt(FIT_OMR*(1 + z)**4 + om*(1 + z)**3))*(1 + z), lz)

def fit_rd(ob, obc):
    return 147.05*(ob/0.02236)**-0.13*(obc/0.1432)**-0.23*(FIT_NEFF/3.04)**-0.1

def fit_comoving(h, om_m, Ok, de, zq):
    integ = (1 + ZG)/np.sqrt(fit_E2(ZG, h, om_m, Ok, de))
    chi = np.concatenate([[0], np.cumsum(0.5*(integ[1:] + integ[:-1])*DLNZ)])
    chiq = np.interp(np.log1p(zq), LNZ, chi)
    DH0 = FIT_CKMS/(100*h)
    if Ok > 0:
        DM = DH0/np.sqrt(Ok)*np.sinh(np.sqrt(Ok)*chiq)
    elif Ok < 0:
        DM = DH0/np.sqrt(-Ok)*np.sin(np.sqrt(-Ok)*chiq)
    else:
        DM = DH0*chiq
    return DM, DH0/np.sqrt(fit_E2(zq, h, om_m, Ok, de))

FIT_CAL = [1.0]
def fit_theta(ob, obc, h, Ok, de):
    om = obc + FIT_OMNU
    zs = fit_zstar(ob, om)
    return FIT_CAL[0]*fit_rstar(ob, om, zs)/fit_comoving(h, om, Ok, de, np.array([zs]))[0][0]
FIT_CAL[0] = 1.04110e-2/fit_theta(0.02223, 0.3169*0.6714**2 - FIT_OMNU, 0.6714, 0.0, None)

def fit_de(x, model):
    if model == 'LCDM':
        return None
    if model == 'w0wa':
        return (x[3], x[4])
    return (x[3], -{'corr1.5': 1.5, 'corr2.0': 2.0}[model]*(1 + x[3]))     # the corridor w_a = -s(1 + w0)

def fit_resid(x, Ok, model):
    ob, obc, h = x[:3]
    de = fit_de(x, model)
    out = [W_CMB @ (np.array([fit_theta(ob, obc, h, Ok, de), ob, obc]) - MU_CMB)]
    r_d = fit_rd(ob, obc)
    DM, DH = fit_comoving(h, obc + FIT_OMNU, Ok, de, ZQ)
    for i, (z, dm, s1, dh, s2, r) in enumerate(BAO_2D):
        out.append(W_BAO[i] @ np.array([DM[i]/r_d - dm, DH[i]/r_d - dh]))
    DV = (ZQ[-1]*DM[-1]**2*DH[-1])**(1/3)
    out.append([(DV/r_d - BAO_DV[1])/BAO_DV[2]])
    return np.concatenate(out)

def fit_bounds(model):
    lo, hi = [0.015, 0.10, 0.5], [0.03, 0.18, 0.9]          # the original's box
    if model.startswith('corr'):
        lo, hi = lo + [-1.0], hi + [-0.3]                  # thawing, never phantom: w0 in [-1, -0.3]
    if model == 'w0wa':
        lo, hi = lo + [-1e9, -1e9], hi + [1e9, 1e9]
    return np.array(lo), np.array(hi)

def fit_lm(x0, Ok, model, iters=200):
    """minimize chi^2 = |residuals|^2; returns (x, chi2)"""
    lo, hi = fit_bounds(model)
    x = np.array(x0, float)
    n = len(x)
    r = fit_resid(x, Ok, model)
    f = r @ r
    lam = 1e-3
    for _ in range(iters):
        J = np.empty((len(r), n))
        for j in range(n):
            dx = 1e-7*max(1.0, abs(x[j]))
            xp = x.copy(); xp[j] += dx
            if xp[j] > hi[j]:
                xp[j] = x[j] - dx; dx = -dx
            J[:, j] = (fit_resid(xp, Ok, model) - r)/dx
        g = J.T @ r
        free = np.array([not ((x[j] <= lo[j] and g[j] > 0) or (x[j] >= hi[j] and g[j] < 0)) for j in range(n)])
        A = J[:, free].T @ J[:, free]
        while True:
            step = np.zeros(n)
            step[free] = -np.linalg.solve(A + lam*np.diag(np.diag(A)), g[free])
            xn = np.clip(x + step, lo, hi)
            rn = fit_resid(xn, Ok, model)
            fn = rn @ rn
            if fn < f:
                lam = max(lam/10, 1e-12)
                break
            lam *= 10
            if lam > 1e12:
                return x, f
        done = f - fn < 1e-12*max(f, 1.0)
        x, r, f = xn, rn, fn
        if done:
            break
    return x, f

FIT_BASE = [0.02223, 0.14208, 0.68]
FIT_START = {'LCDM': FIT_BASE, 'w0wa': FIT_BASE + [-0.45, -1.6], 'corr1.5': FIT_BASE + [-0.95],
             'corr2.0': FIT_BASE + [-0.95]}

def Phi(x):
    return 0.5*(1 + erf(x/sqrt(2)))

def gauss_closed(mean, sig):
    """a Gaussian posterior in Omega_K truncated to Omega_K < 0: (95% bound on |Omega_K|, P(closed))"""
    pc = Phi(-mean/sig)
    lo, hi = 0.0, 0.1
    for _ in range(100):
        mid = 0.5*(lo + hi)
        if (pc - Phi((-mid - mean)/sig))/pc < 0.95:
            lo = mid
        else:
            hi = mid
    return hi, pc

def fit_profile(model, oks):
    """chi^2 profile on the Omega_K grid of the original (step 0.001), warm-started outward from +0.002;
    Gaussian reading: parabola through the points with dchi2 < 6, as the original"""
    oks = [round(o, 4) for o in oks]
    i0 = oks.index(0.002)
    prof = {}
    x, v = fit_lm(FIT_START[model], 0.002, model)
    prof[0.002] = (v, x)
    for direction in (+1, -1):
        xc = prof[0.002][1]
        k = i0 + direction
        while 0 <= k < len(oks):
            xc, v = fit_lm(xc, oks[k], model)
            prof[oks[k]] = (v, xc)
            k += direction
    O = np.array(sorted(prof))
    V = np.array([prof[o][0] for o in O])
    sel = V - V.min() < 6
    A = np.polyfit(O[sel], V[sel], 2)
    mean, sig = -A[1]/(2*A[0]), 1/np.sqrt(A[0])
    bound, pc = gauss_closed(mean, sig)
    return dict(O=O, V=V, sel=sel, mean=mean, sig=sig, pc=pc, bound=bound, x={o: prof[o][1] for o in O})


# ======================================================================================================
print("== Anchors (independent of the investigation)")
# ======================================================================================================
check("CODATA 2018 Planck length 1.616255e-35 m", close(L_P, 1.616255e-35, 2e-6), f"{L_P:.6e}")
check("CODATA 2018 Planck mass 2.176434e-8 kg", close(M_P, 2.176434e-8, 2e-6), f"{M_P:.6e}")
check("CODATA 2018 Planck temperature 1.416784e32 K", close(T_P, 1.416784e32, 2e-6), f"{T_P:.6e}")
check("CODATA 2018 Planck time 5.391247e-44 s", close(T_PL, 5.391247e-44, 2e-6), f"{T_PL:.6e}")
check("CODATA 2018 hbar c = 197.3269804 MeV fm", close(HBARC_EVM, 1.973269804e-7, 1e-9), f"{HBARC_EVM:.10e} eV m")
check("PDG: photon number density 410.73 cm^-3 at 2.7255 K", close(N_GAMMA0/1e6, 410.73, 1e-4), f"{N_GAMMA0/1e6:.2f}")
MRED_GEV = sqrt(HBAR*C**5/(8*pi*G))/GEV
check("PDG: reduced Planck energy 2.435e18 GeV", close(MRED_GEV, 2.435e18, 1e-3), f"{MRED_GEV:.4e} GeV")

# exact closed solutions the integrator must reproduce (textbook: Weinberg 1972 s15.3, MTW s27.10)
for K in (1e-2, 1e-3):
    om = 1 + K
    r = history(Model(K, 1.0, 0.0, 0.5, om=om, orr=0.0), full=True)
    A_, B_ = om/(2*K), om/(2*K**1.5)                    # a = A(1 - cos eta), t = B(eta - sin eta)
    errs = (r['turn']['a']/(2*A_) - 1, r['turn']['t']/(pi*B_) - 1, r['crunch']['t']/(2*pi*B_) - 1,
            r['turn']['chi'] - pi)
    check(f"closed dust + curvature, |Omega_k| = {K:g}, Omega_m = 1 + |Omega_k|: integrator reproduces the cycloid's "
          "a_max = Omega_m/(Omega_m - 1), t_turn = (pi/2) Omega_m/(H0 (Omega_m - 1)^1.5), t_crunch = 2 t_turn and "
          "chi_turn = pi to 1e-8", max(abs(e) for e in errs) < 1e-8, ", ".join(f"{e:.1e}" for e in errs))
K = 1e-3
om = 1 + K - OR
r = history(Model(K, 1.0, 0.0, 0.5, om=om, orr=OR), full=True)
A_, B_ = om/(2*K), sqrt(OR/K)                           # a(eta) = A(1 - cos eta) + B sin eta
et = pi - atan(B_/A_)
errs = (r['turn']['a']/(A_*(1 - cos(et)) + B_*sin(et)) - 1,
        r['turn']['t']/((A_*(et - sin(et)) + B_*(1 - cos(et)))/sqrt(K)) - 1, r['turn']['chi'] - et)
check("closed dust + radiation + curvature (|Omega_k| = 1e-3): a_max, t_turn and chi_turn of the exact solution "
      "a = A(1 - cos eta) + sqrt(Omega_r/|Omega_k|) sin eta, to 1e-8", max(abs(e) for e in errs) < 1e-8,
      ", ".join(f"{e:.1e}" for e in errs))
eta_, Om_, Or_, K_ = sp.symbols('eta Omega_m Omega_r K', positive=True)
a_ex = Om_/(2*K_)*(1 - sp.cos(eta_)) + sp.sqrt(Or_/K_)*sp.sin(eta_)
check("sympy: that a(eta) solves (da/deta)^2 = (Omega_r + Omega_m a - |Omega_k| a^2)/|Omega_k|",
      sp.simplify(sp.diff(a_ex, eta_)**2 - (Or_ + Om_*a_ex - K_*a_ex**2)/K_) == 0)
mflat = Model(0.0, 1.0, 1.5*(1 - OM), 0.0, om=OM, orr=0.0)       # tau frozen at the hilltop: V = 2 V0 = Lambda
t_flat = mflat.to_today()[2]
check("flat LCDM without radiation: age H0 t0 = 2/(3 sqrt(Omega_L)) asinh(sqrt(Omega_L/Omega_m)) (textbook)",
      close(t_flat, 2/(3*sqrt(1 - OM))*asinh(sqrt((1 - OM)/OM)), 1e-9), f"{t_flat:.12f}")
mp.mp.dps = 30                                          # the reference cancels badly near m = 1e-6 at 20 digits
worst = max(max(abs(ellipKE(x_)[0]/float(mp.ellipk(x_)) - 1), abs(ellipKE(x_)[1]/float(mp.ellipe(x_)) - 1))
            for x_ in (1e-8, 1e-3, 0.1, 0.5, 0.9, 0.999999))
worst_w = max(abs(wbar(x_) - float(2*(mp.ellipe(x_)/mp.ellipk(x_) - 1 + x_)/x_ - 1))/
              abs(float(2*(mp.ellipe(x_)/mp.ellipk(x_) - 1 + x_)/x_ - 1)) for x_ in (1e-6, 9.9e-4, 1.01e-3, 0.05, 0.9))
check("averaged field: AGM K(m), E(m) and <w>(m) = 2(E/K - 1 + m)/m - 1 against mpmath's elliptic integrals",
      worst < 1e-14 and worst_w < 1e-9, f"{worst:.1e}, {worst_w:.1e}")
V0p, fp = 1.3, 0.7
xA = 1.5
mm_ = sin(xA/2)**2
hits = []
dp5(lambda t, y: [y[1], -V0p/fp*sin(y[0]/fp), 0.5*y[1]**2 - 2*V0p*sin(y[0]/(2*fp))**2,
                  0.5*y[1]**2 + 2*V0p*sin(y[0]/(2*fp))**2], 0.0, [xA*fp, 0.0, 0.0, 0.0],
    2.5*4*ellipKE(mm_)[0]*fp/sqrt(V0p), 0.01, lambda y, yn: [1e-13, 1e-13, None, None],
    [Event('z', lambda t, y: y[0], +1, callback=lambda t, y: hits.append((t, y[2], y[3])))])
Tnum, wnum = hits[1][0] - hits[0][0], (hits[1][1] - hits[0][1])/(hits[1][2] - hits[0][2])
check("pendulum V0(1 - cos(x/f)) integrated directly: period 4K(m)/mass and period-averaged w equal the formulas",
      close(Tnum, 4*float(mp.ellipk(mm_))*fp/sqrt(V0p), 1e-9) and abs(wnum - wbar(mm_)) < 1e-9,
      f"T = {Tnum:.10f}, <w> = {wnum:.10f}")

# the S^3 scalar spectrum (textbook): -Laplacian eigenvalues (nu^2 - 1)/R^2, degeneracy nu^2
chi_, nu_ = sp.symbols('chi nu', positive=True)
fnu = sp.sin(nu_*chi_)/sp.sin(chi_)
lap_f = sp.diff(sp.sin(chi_)**2*sp.diff(fnu, chi_), chi_)/sp.sin(chi_)**2
check("S^3: the zonal harmonic sin(nu chi)/sin(chi) has -Laplacian eigenvalue nu^2 - 1 (unit radius), any nu",
      sp.simplify(lap_f + (nu_**2 - 1)*fnu) == 0)
check("S^3: harmonic polynomials of degree l on R^4 number C(l+3,3) - C(l+1,3) = (l+1)^2 = nu^2 (l = 0..20)",
      all(sp.binomial(l + 3, 3) - sp.binomial(l + 1, 3) == (l + 1)**2 for l in range(21)))
def spin_mats(j):
    d = int(round(2*j + 1)); ms = [j - n for n in range(d)]
    Jp = np.zeros((d, d), complex)
    for n in range(1, d):
        Jp[n - 1, n] = sqrt(j*(j + 1) - ms[n]*(ms[n] + 1))
    return [(Jp + Jp.conj().T)/2, (Jp - Jp.conj().T)/2j, np.diag(ms).astype(complex)]
ok_su2 = True
for l2 in range(0, 7):                                  # SU(2) = S^3: left action, spin l = (nu - 1)/2
    L = spin_mats(l2/2)
    ev = np.linalg.eigvalsh(sum((2*La) @ (2*La) for La in L))
    nu = l2 + 1
    ok_su2 &= np.allclose(ev, nu**2 - 1) and len(ev)*(l2 + 1) == nu**2
check("S^3 = SU(2): -Laplacian = sum (2 J_a)^2 on spin l = (nu - 1)/2 gives nu^2 - 1, (2l+1) x (2l+1) = nu^2 states",
      ok_su2)
def ricci_scalar(gmat, X):
    dim = len(X)
    gi = gmat.inv()
    Gam = [[[sum(gi[l, s]*(sp.diff(gmat[s, m], X[n]) + sp.diff(gmat[s, n], X[m]) - sp.diff(gmat[m, n], X[s]))
                 for s in range(dim))/2 for n in range(dim)] for m in range(dim)] for l in range(dim)]
    Rs = 0
    for m in range(dim):
        for n in range(dim):
            Ric = 0
            for l in range(dim):
                Ric += sp.diff(Gam[l][m][n], X[l]) - sp.diff(Gam[l][m][l], X[n])
                for s in range(dim):
                    Ric += Gam[l][l][s]*Gam[s][m][n] - Gam[l][n][s]*Gam[s][m][l]
            Rs += gi[m, n]*Ric
    return sp.simplify(Rs)
th_, ph_ = sp.symbols('theta phi', positive=True)
G_S3 = sp.diag(1, sp.sin(chi_)**2, sp.sin(chi_)**2*sp.sin(th_)**2)
check("unit S^3 in hyperspherical coordinates has Ricci scalar 6 (textbook)", ricci_scalar(G_S3, [chi_, th_, ph_]) == 6)

# the Poincare dodecahedral space S^3/I*: invariants of the binary icosahedral group I* (order 120) in the spin-j
# representation, from its characters (classes by half-angle and size); a scalar mode nu = 2j + 1 survives iff
# V_j has an I*-invariant. Aurich, Lustig and Steiner 2005 (astro-ph/0412569): first eigenvalue k(k+2) at k = 12.
CLASSES = [(0, 1), (pi, 1), (pi/2, 30), (pi/3, 20), (2*pi/3, 20), (pi/5, 12), (3*pi/5, 12), (2*pi/5, 12), (4*pi/5, 12)]
def n_invariant(j2):
    tot = 0.0
    for al, n in CLASSES:
        tot += n*((j2 + 1)*cos(al)**j2 if abs(sin(al)) < 1e-12 else sin((j2 + 1)*al)/sin(al))
    return round(tot/120)
first = next(j2 for j2 in range(1, 200) if n_invariant(j2) > 0)
check("Poincare dodecahedral space: the class sizes sum to 120; the lowest nontrivial scalar mode is nu = 13, i.e. "
      "k = 12 with eigenvalue k(k + 2) = 168 (Aurich et al. 2005)", sum(n for _, n in CLASSES) == 120 and
      first + 1 == 13 and 12*14 == 13**2 - 1, f"first invariant at j = {first/2:g}, nu = {first + 1}")

# published curvature (Gaussian summaries)
OK_DESI = (0.0023, 0.0011)        # DESI DR2 BAO + CMB, LCDM + Omega_K: arXiv:2503.14738, Table 5
OK_AAN = (0.003, 0.001)           # exponential quintessence + Omega_K: Akrami, Alestas, Nesseris, arXiv:2504.04226, abstract
W0WA_DESI = ((-0.43, 0.22), (-1.72, 0.64))   # DR2 flat w0wa, DESI + (theta_*, omega_b, omega_bc)_CMB (the critic's source)
print(f"      typed in: DESI DR2 + CMB LCDM + Omega_K = {OK_DESI[0]} +- {OK_DESI[1]}; Akrami-Alestas-Nesseris "
      f"Omega_K = {OK_AAN[0]} +- {OK_AAN[1]}")

# X's range: Lee et al. 2020 (thesis Table 11.4; lambda in mm; +alpha95, |alpha95|), as typed in
# verify/phase_space_diameter.py; the bound is the one-sided crossing at alpha = 4/3 (the aligned vacuum, u = 1)
TAB = [(0.025, 7.9, 6.4), (0.028, 4.51, 3.73), (0.032, 2.56, 2.08), (0.035, 1.77, 1.45), (0.040, 1.06, 0.877),
       (0.045, 0.699, 0.585), (0.050, 0.494, 0.419), (0.056, 0.35, 0.3), (0.063, 0.251, 0.218),
       (0.071, 0.183, 0.162), (0.079, 0.14, 0.126), (0.089, 0.106, 0.097), (0.100, 0.0813, 0.0766)]
def crossing(col, target):
    for (l1_, *a1), (l2_, *a2) in zip(TAB, TAB[1:]):
        y1, y2 = a1[col], a2[col]
        if (y1 - target)*(y2 - target) <= 0:
            tt = log(y1/target)/log(y1/y2)
            return exp(log(l1_) + tt*log(l2_/l1_))*1e-3
LAM_X = crossing(0, 4/3)
MX_EV = HBARC_EVM/LAM_X
check("the range interpolation reproduces Lee et al.'s published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3); at "
      "alpha = 4/3 it gives lambda_X < 37.7 um, M_X c^2 > 5.24 meV", round(crossing(1, 1.0)*1e6, 1) == 38.6 and
      round(crossing(1, 8/3)*1e6) == 30 and round(LAM_X*1e6, 1) == 37.7 and round(MX_EV*1e3, 2) == 5.24,
      f"{LAM_X*1e6:.3f} um, {MX_EV*1e3:.4f} meV")

# fit calibration against two published DR2 results
xw, vw = fit_lm(FIT_START['w0wa'], 0.0, 'w0wa')
xl, vl = fit_lm(FIT_START['LCDM'], 0.0, 'LCDM')
print(f"      flat LCDM: chi2 = {vl:.2f}, Omega_m = {(xl[1] + FIT_OMNU)/xl[2]**2:.4f}, H0 = {100*xl[2]:.2f} "
      f"(DR2 DESI+CMB: 0.3027, 68.17); flat w0wa: chi2 = {vw:.2f}, w0 = {xw[3]:.3f}, wa = {xw[4]:.3f}")
check("fit calibration: flat w0wa best fit within 1 sigma of DR2's DESI + (theta_*, omega_b, omega_bc) result "
      "w0 = -0.43 +- 0.22, wa = -1.72 +- 0.64", abs(xw[3] - W0WA_DESI[0][0]) < W0WA_DESI[0][1] and
      abs(xw[4] - W0WA_DESI[1][0]) < W0WA_DESI[1][1], f"w0 = {xw[3]:.3f}, wa = {xw[4]:.3f}")
OK_GRID = [round(-0.002 + 0.001*i, 4) for i in range(10)]          # -0.002 .. +0.007
PROF_L = fit_profile('LCDM', OK_GRID)
check("fit calibration: LCDM + Omega_K gives 0.00242 +- 0.00114, within 0.2 sigma and 5% in width of DR2's "
      "DESI + CMB 0.0023 +- 0.0011", abs(PROF_L['mean'] - OK_DESI[0]) < 0.2*OK_DESI[1] and
      close(PROF_L['sig'], OK_DESI[1], 0.05) and round(PROF_L['mean'], 5) == 0.00242 and round(PROF_L['sig'], 5) == 0.00114,
      f"{PROF_L['mean']:+.5f} +- {PROF_L['sig']:.5f}")


# ======================================================================================================
print("\n== B. Closed tau histories (regression: closed/dynamics/grid.csv, overconstraint.out, contrasts.out, "
      "critic/d_light_travel.out)")
# ======================================================================================================
TG = T_H0_GYR
def run_history(K, f, w0t):
    th = solve_theta(K, f, w0t)
    V0 = shoot_V0(K, f, th)
    r = history(Model(K, f, V0, th))
    r.update(K=K, f=f, w0t=w0t, theta_i=th, V0=V0)
    return r
def derived(r):
    K, tr = r['K'], r['turn']
    R0 = R0_of(K)
    r.update(a_max=tr['a'], t_turn=tr['t']*TG, t_crunch=r['crunch']['t']*TG, R0_Gpc=R0/GPC, Rmax_m=tr['a']*R0,
             Rmax_Gpc=tr['a']*R0/GPC, T_turn=T0/tr['a'], c_light=(tr['chi'] - r['chi0'] - pi)/sqrt(K))
    return r
REP = derived(run_history(1e-3, 1.0, -0.8))
print(f"      representative: |Omega_k| = 1e-3, f = 1, w0 = -0.8: theta_i = {REP['theta_i']:.10f}, V0 = {REP['V0']:.10f}, "
      f"w0 = {REP['w0']:.10f}, waT = {REP['waT']:.9f}; a_max = {REP['a_max']:.7f}, t_turn = {REP['t_turn']:.7e} Gyr, "
      f"t_crunch = {REP['t_crunch']:.7e} Gyr")
check("representative history reproduces grid.csv: theta_i = 1.4993693881, V0 = 2.4773014872, a_max = 1726.12670, "
      "t_turn = 1.24388683e6 Gyr", abs(REP['theta_i'] - 1.4993693881418884) < 1e-9 and abs(REP['V0'] - 2.477301487223793) < 1e-9
      and close(REP['a_max'], 1726.1267002053414, 1e-7) and close(REP['t_turn'], 1243886.8328322116, 1e-7))
check("B1: a_max = 1726, t_turn = 1.24e6 Gyr, R0 = 140.7 Gpc", round(REP['a_max']) == 1726 and
      r3(REP['t_turn']) == 1.24e6 and round(REP['R0_Gpc'], 1) == 140.7, f"R0 = {REP['R0_Gpc']:.3f} Gpc")
check("B1: R_max = 2.43e5 Gpc = 7.49e30 m", r3(REP['Rmax_Gpc']) == 2.43e5 and r3(REP['Rmax_m']) == 7.49e30,
      f"{REP['Rmax_Gpc']:.4e} Gpc, {REP['Rmax_m']:.4e} m")
check("B1: T_CMB at the turnaround = T0/a_max = 1.58 mK; atilde_min = 1/a_max = 5.8e-4",
      round(REP['T_turn']*1e3, 2) == 1.58 and float(f"{1/REP['a_max']:.2g}") == 5.8e-4,
      f"{REP['T_turn']*1e3:.4f} mK, {1/REP['a_max']:.4e}")

# the grid extremes: smallest R_max and t_turn (|Omega_k| = 1e-2, f = 0.2, w0 = -0.7) and largest (1e-5, 2, -0.95)
LO = derived(run_history(1e-2, 0.2, -0.7))
HI = derived(run_history(1e-5, 2.0, -0.95))
check("grid extremes reproduce grid.csv: a_max = 102.052198 (1e-2, 0.2, -0.7) and 1.35935492e7 (1e-5, 2, -0.95)",
      close(LO['a_max'], 102.05219806617711, 1e-7) and close(HI['a_max'], 13593549.170707047, 1e-7),
      f"{LO['a_max']:.6f}, {HI['a_max']:.8e}")
check("B3: R_max runs from 4.54e3 to 1.91e10 Gpc and t_turn from about 2.3e4 to 9.8e10 Gyr over the grid",
      r3(LO['Rmax_Gpc']) == 4.54e3 and r3(HI['Rmax_Gpc']) == 1.91e10 and float(f"{LO['t_turn']:.2g}") == 2.3e4
      and float(f"{HI['t_turn']:.2g}") == 9.8e10,
      f"R_max {LO['Rmax_Gpc']:.4e} .. {HI['Rmax_Gpc']:.4e} Gpc, t_turn {LO['t_turn']:.4e} .. {HI['t_turn']:.4e} Gyr")

# over-constraint: fixed (w0, w_a) = the representative's (Taylor convention), solve (f, theta_i) at |Omega_k| = 1e-4
def w0wa_of(K, f, th):
    V0 = shoot_V0(K, f, th)
    y = Model(K, f, V0, th).to_today()
    return np.array(Model(K, f, V0, th).w_today(y[0], y[1])), V0
def solve_f_theta(K, w0t, wat, f, th):
    """Newton in (f, theta_i), V0 shot inside, for w(1) = w0t and w_a = wat"""
    target = np.array([w0t, wat])
    for _ in range(30):
        F, V0 = w0wa_of(K, f, th)
        res = F - target
        if np.max(np.abs(res)) < 1e-11:
            break
        J = np.empty((2, 2))
        for j, (df, dth) in enumerate(((1e-6, 0.0), (0.0, 1e-6))):
            J[:, j] = (w0wa_of(K, f + df, th + dth)[0] - F)/1e-6
        step = np.linalg.solve(J, -res)
        f, th = f + step[0], th + step[1]
    V0 = shoot_V0(K, f, th)
    return f, th, V0
f4, th4, V04 = solve_f_theta(1e-4, -0.8, REP['waT'], 1.0, REP['theta_i'])
OC = history(Model(1e-4, f4, V04, th4))
OC.update(K=1e-4, f=f4, theta_i=th4, V0=V04)
OC = derived(OC)
slope = log(OC['t_turn']/REP['t_turn'])/log(1e-4/1e-3)
print(f"      |Omega_k| = 1e-4 at the representative's (w0, wa) = (-0.8, {REP['waT']:.9f}): f = {f4:.9f}, "
      f"theta_i = {th4:.9f}, w0 = {OC['w0']:.10f}, wa = {OC['waT']:.9f}; a_max = {OC['a_max']:.6e}, t_turn = {OC['t_turn']:.9e} Gyr")
check("over-constraint pair reproduces overconstraint.out: f = 1.000731895, theta_i = 1.501224780, t_turn = 3.9292086e7 Gyr",
      abs(f4 - 1.000731895) < 2e-9 and abs(th4 - 1.501224780) < 2e-9 and close(OC['t_turn'], 3.929208553e7, 1e-7))
check("B5: at fixed (w0, wa), d ln t_turn/d ln|Omega_k| = -1.5 (two-point, |Omega_k| = 1e-3 and 1e-4)",
      abs(slope + 1.5) < 2e-3, f"{slope:.5f}")

HIST = [('representative', REP), ('smallest R_max', LO), ('largest R_max', HI), ('over-constraint 1e-4', OC)]
for name, r in HIST:
    tr = r['turn']
    print(f"      {name}: |Omega_k| = {r['K']:g}, f = {r['f']:.4g}: Omega_d = {tr['Od']:.7f}, first minimum at a = "
          f"{r['first_min']['a']:.4f}, <w>(turn) = {tr['wbar']:.3e}, t_crunch/t_turn = {r['t_crunch']/r['t_turn']:.8f}, "
          f"w_eff(crunch) = {r['crunch']['weff_end']:.6f}, c = {r['c_light']:+.4f}")
check("B2: every history has V0 > 0 (so V = 2 V0 sin^2(delta/2f) >= 0 throughout) and turns around",
      all(r['V0'] > 0 and 'turn' in r for _, r in HIST))
check("B2: a_max = (Omega_m + Omega_d)/|Omega_k| to <= 1e-5, Omega_d = rho_tau a^3/3 at the turnaround "
      "(Friedmann constraint there < 1e-8)", all(abs((OM + r['turn']['Od'])/r['K']/r['a_max'] - 1) <= 1e-5 and
      abs(r['turn']['constraint']) < 1e-8 for _, r in HIST),
      ", ".join(f"{(OM + r['turn']['Od'])/r['K']/r['a_max'] - 1:.1e}" for _, r in HIST))
check("B2: t_turn = (pi/2)(Omega_m + Omega_d)|Omega_k|^-1.5/H0 to 1e-3", all(abs(r['turn']['t']/(0.5*pi*(OM + r['turn']['Od'])
      /r['K']**1.5) - 1) < 1e-3 for _, r in HIST),
      ", ".join(f"{r['turn']['t']/(0.5*pi*(OM + r['turn']['Od'])/r['K']**1.5) - 1:.1e}" for _, r in HIST))
check("B2: t_crunch = 2 t_turn to 1e-3", all(abs(r['t_crunch']/r['t_turn']/2 - 1) < 1e-3 for _, r in HIST))
check("B2: the crunch is kinetic: w_eff -> 1 and the kinetic fraction -> 1 at a = 1e-10",
      all(r['crunch']['weff_end'] > 0.9999 and r['crunch']['kin_frac'] > 0.9999 for _, r in HIST))
check("B2: tau's first minimum lies in a = 1.34-18.9 (grid range 1.3367-18.939)",
      all(1.335 <= r['first_min']['a'] <= 18.95 for _, r in HIST) and round(LO['first_min']['a'], 4) == 1.3367)
check("B2: |<w>| <= 1.1e-7 at the turnaround", all(abs(r['turn']['wbar']) <= 1.1e-7 for _, r in HIST),
      f"largest {max(abs(r['turn']['wbar']) for _, r in HIST):.3e}")
check("B2: Omega_d/Omega_DE,0 >= 1.0149, Omega_DE,0 = 1 - Omega_m - Omega_r + |Omega_k|",
      all(r['turn']['Od']/ODE0(r['K']) >= 1.0149 for _, r in HIST),
      ", ".join(f"{r['turn']['Od']/ODE0(r['K']):.5f}" for _, r in HIST))

# controls
Kh = 1e-2
V0h = shoot_V0(Kh, 1.0, 0.0)
mh = Model(Kh, 1.0, V0h, 0.0)
yh = mh.to_today()
xh, yh, whyh, _ = dp5(mh.rhs_NF(+1.0), 0.0, yh, log(1e8), 0.01, mh.sc_NF(1e-10))
Hh = sqrt(mh.H2_full(xh, yh[0], yh[1]))
check("B4: tau frozen at the hilltop (theta_i = 0, V = 2 V0 = Lambda), |Omega_k| = 1e-2: H > 0 all the way to a = 1e8, "
      "H/H0 -> sqrt(Omega_Lambda) (contrasts.out: 0.833611704)", whyh == 'end' and abs(Hh - sqrt(2*V0h/3)) < 1e-9 and
      round(Hh, 9) == 0.833611704, f"H/H0 = {Hh:.9f}")
rts = np.roots([2*V0h/3, 0.0, -Kh, OM, OR])            # H^2 a^4 = Omega_L a^4 - |Omega_k| a^2 + Omega_m a + Omega_r
check("B4: and H^2 = 0 has no positive root for that history (quartic in a)",
      not any(abs(z.imag) < 1e-12 and z.real > 0 for z in rts))
rm_, rr_, kin_, V_, a_, kap = sp.symbols('rho_m rho_r K_tau V a kappa', positive=True)
H2_flat_open = (rm_ + rr_ + kin_ + V_)/3 + kap/a_**2      # k = -kappa <= 0 (kappa > 0 open; flat as kappa -> 0)
check("B4 (sympy): with V >= 0, H^2 = rho/3 - k/a^2 > 0 whenever k <= 0, so flat and open universes never turn around",
      H2_flat_open.is_positive and ((rm_ + rr_ + kin_ + V_)/3).is_positive)

# light
check("B6: conformal time from today to the turnaround = pi + c sqrt|Omega_k|, with c = -1.98 to +0.62 in the four "
      "histories (grid-wide, critic/d_light_travel.out: -1.991 to +0.628)",
      round(min(r['c_light'] for _, r in HIST), 2) == -1.98 and round(max(r['c_light'] for _, r in HIST), 2) == 0.62,
      ", ".join(f"{r['c_light']:+.6f}" for _, r in HIST))
Hs_, ts_ = sp.symbols('H t', positive=True)
eta_dS = 2*sp.atan(sp.tanh(Hs_*ts_/2))
check("B6 (sympy): closed de Sitter R = cosh(Ht)/H from its throat: eta = 2 arctan(tanh(Ht/2)) solves d eta/dt = 1/R and "
      "tends to pi/2", sp.simplify(sp.diff(eta_dS, ts_) - Hs_/sp.cosh(Hs_*ts_)) == 0 and sp.limit(eta_dS, ts_, sp.oo) == sp.pi/2)


# ======================================================================================================
print("\n== C. Data bounds given closure (port of critic/g_answer_numbers.py and f_corridor_curvature_fit.py)")
# ======================================================================================================
def answer(ok):
    """smallest a_max = (Omega_m + Omega_DE,0)/|Omega_k| (Omega_d >= Omega_DE,0 on the thawing grid) at a bound"""
    R0 = R0_of(ok)
    amax = (OM + ODE0(ok))/ok
    Rmax = amax*R0
    return dict(R0=R0/GPC, amax=amax, Rmax=Rmax/GPC, Rmax_lP=Rmax/L_P, tturn=(pi/2)*(OM + ODE0(ok))/ok**1.5/H0/GYR,
                inv=1/amax, grain=HBARC_EVM/Rmax, T=T0/amax*1e3, Rmax_m=Rmax, R0_m=R0)
def show(label, ok, A):
    print(f"      {label}: |Omega_k| < {ok:.6f}: R0 > {A['R0']:.2f} Gpc, a_max > {A['amax']:.1f}, R_max > {A['Rmax']:.4e} Gpc "
          f"= {A['Rmax_lP']:.4e} l_P, t_turn > {A['tturn']:.4e} Gyr, 1/a_max < {A['inv']:.4e}, hbar c/R_max < "
          f"{A['grain']:.4e} eV, T_CMB(turn) < {A['T']:.4f} mK")
B_DESI, PC_DESI = gauss_closed(*OK_DESI)
AD = answer(B_DESI)
show("DESI DR2 + CMB", B_DESI, AD)
check("C1: DESI DR2 + CMB truncated to Omega_K < 0: P(closed) = 0.018, |Omega_k| < 0.00113", round(PC_DESI, 3) == 0.018
      and round(B_DESI, 5) == 0.00113)
check("C1: R0 > 132.4 Gpc, a_max > 887, R_max > 1.174e5 Gpc = 2.242e65 l_P, t_turn > 6.015e5 Gyr",
      round(AD['R0'], 1) == 132.4 and round(AD['amax']) == 887 and r4(AD['Rmax']) == 1.174e5 and
      r4(AD['Rmax_lP']) == 2.242e65 and r4(AD['tturn']) == 6.015e5)
check("C1: 1/a_max < 1.128e-3, hbar c/R_max < 5.446e-38 eV, T_CMB(turnaround) < 3.073 mK",
      r4(AD['inv']) == 1.128e-3 and r4(AD['grain']) == 5.446e-38 and round(AD['T'], 3) == 3.073)

PROF = {m_: fit_profile(m_, OK_GRID) for m_ in ('corr1.5', 'corr2.0')}
PROF['w0wa'] = fit_profile('w0wa', [round(-0.005 + 0.001*i, 4) for i in range(12)])
for m_, P in [('LCDM', PROF_L)] + list(PROF.items()):
    print(f"      {m_:7s}: chi2 min {P['V'].min():.2f}; dchi2 " + " ".join(f"{o:+.3f}:{v - P['V'].min():.3f}"
          for o, v in zip(P['O'], P['V'])) + f"  -> Omega_K = {P['mean']:+.5f} +- {P['sig']:.5f}, P(closed) = "
          f"{P['pc']:.4f}, |Omega_k| < {P['bound']:.6f}")
P15, P20, PW = PROF['corr1.5'], PROF['corr2.0'], PROF['w0wa']
check("C2: corridor (w_a = -s(1 + w0), w0 >= -1) + Omega_K: s = 1.5 gives 0.00252 +- 0.00119 (= 0.0025 +- 0.0012), "
      "s = 2.0 gives 0.00245 +- 0.00119", round(P15['mean'], 5) == 0.00252 and round(P15['sig'], 5) == 0.00119 and
      round(P15['mean'], 4) == 0.0025 and round(P15['sig'], 4) == 0.0012 and round(P20['mean'], 5) == 0.00245 and
      round(P20['sig'], 5) == 0.00119)
check("C2: P(closed) = 0.017-0.020 (s = 1.5, 2.0); 95% bound given closure |Omega_k| < 0.001207 (s = 1.5)",
      round(P15['pc'], 3) == 0.017 and round(P20['pc'], 3) == 0.020 and round(P15['bound'], 6) == 0.001207,
      f"{P15['pc']:.4f}, {P20['pc']:.4f}; s = 2.0 bound {P20['bound']:.5f}")
check("C2: the corridor result lies within 1 sigma of both published values (DESI DR2 0.0023 +- 0.0011; Akrami et al. "
      "0.003 +- 0.001)", abs(P15['mean'] - OK_DESI[0]) < OK_DESI[1] and abs(P15['mean'] - OK_AAN[0]) < OK_AAN[1])
AC = answer(P15['bound'])         # the unrounded bound (the critic's g_answer_numbers.py rounded it to 0.00121 first)
show("corridor + Omega_K (s = 1.5)", P15['bound'], AC)
check("C2: at the corridor bound: R0 > 128.0 Gpc, a_max > 829.5, R_max > 1.062e5 Gpc, t_turn > 5.441e5 Gyr",
      round(AC['R0'], 1) == 128.0 and round(AC['amax'], 1) == 829.5 and r4(AC['Rmax']) == 1.062e5 and
      r4(AC['tturn']) == 5.441e5)
check("C2: 1/a_max < 1.206e-3, grain < 6.022e-38 eV, T < 3.286 mK",
      r4(AC['inv']) == 1.206e-3 and r4(AC['grain']) == 6.022e-38 and round(AC['T'], 3) == 3.286)
check("C2: in the same fit w0wa + Omega_K gives +0.00071 +- 0.00151, P(closed) = 0.32",
      round(PW['mean'], 5) == 0.00071 and round(PW['sig'], 5) == 0.00151 and round(PW['pc'], 2) == 0.32,
      f"dchi2 at -0.003: {PW['V'][list(PW['O']).index(-0.003)] - PW['V'].min():.3f} (selection edge 6)")
AF = answer(1e-4)
show("cosmic-variance floor", 1e-4, AF)
check("C3: floor |Omega_k| = 1e-4: R0 > 444.8 Gpc, a_max > 1e4, R_max > 4.448e6 Gpc, t_turn > 2.279e7 Gyr",
      round(AF['R0'], 1) == 444.8 and round(AF['amax']) == 10000 and r4(AF['Rmax']) == 4.448e6 and r4(AF['tturn']) == 2.279e7)
check("C3: grain < 1.438e-39 eV, T < 0.273 mK", r4(AF['grain']) == 1.438e-39 and round(AF['T'], 3) == 0.273)
print(f"      [{time.time() - T_START:.1f} s]")


# ======================================================================================================
print("\n== D. Bimetric sector (ports of gravity-sector/bimetric_flrw.py, proportional_closed.py, y_epochs.py, "
      "higuchi_gradient.py, s3_harmonics.py, turnaround_toy.py and critic/c_second_frame.py)")
# ======================================================================================================
print(f"      minimal M_X (anchors): lambda_X < {LAM_X*1e6:.3f} um, M_X c^2 > {MX_EV*1e3:.4f} meV")

t = sp.Symbol('t'); k = sp.Symbol('k', real=True)
Nt, at, Xt, Yt = [sp.Function(n_)(t) for n_ in ('N', 'a', 'X', 'Y')]
bb = sp.symbols('beta0:5', real=True)
Mg, Mf, mg = sp.symbols('M_g M_f m', positive=True)
lam = sp.Symbol('lam')
poly = sp.expand(sp.prod([1 + lam*e_ for e_ in (Xt/Nt, Yt/at, Yt/at, Yt/at)]))
UN = bb[0]*at**3 + 3*bb[1]*at**2*Yt + 3*bb[2]*at*Yt**2 + bb[3]*Yt**3
UX = bb[1]*at**3 + 3*bb[2]*at**2*Yt + 3*bb[3]*at*Yt**2 + bb[4]*Yt**3
check("potential of the bidiagonal ansatz: N a^3 sum beta_n e_n(sqrt(g^-1 f)) = N U_N + X U_X",
      sp.simplify(sp.expand(Nt*at**3*sum(bb[n]*poly.coeff(lam, n) for n in range(5))) - (Nt*UN + Xt*UX)) == 0)
rho_f = sp.Function('rho')
Lgr = 3*Mg**2*(-at*at.diff(t)**2/Nt + k*Nt*at) - Nt*at**3*rho_f(at)      # sqrt(-g) R(g) reduced, curvature k
Lfr = 3*Mf**2*(-Yt*Yt.diff(t)**2/Xt + k*Xt*Yt)                            # f with the same gamma_k
LAG = Lgr + Lfr - mg**2*Mg**2*(Nt*UN + Xt*UX)
def EL(Lx, q):
    return sp.diff(Lx, q) - sp.diff(sp.diff(Lx, q.diff(t)), t)
EN, EX = sp.diff(LAG, Nt), sp.diff(LAG, Xt)
bian = sp.simplify(at.diff(t)*EL(LAG, at) - Nt*sp.diff(EN, t))
BIAN_T = 3*mg**2*Mg**2*(bb[1]*at**2 + 2*bb[2]*at*Yt + bb[3]*Yt**2)*(Nt*Yt.diff(t) - Xt*at.diff(t))
check("Bianchi constraint: adot EL_a - N dE_N/dt = 3 m^2 M_g^2 (beta1 a^2 + 2 beta2 a Y + beta3 Y^2)(N Ydot - X adot) "
      "(up to sign), with no k", (sp.simplify(bian - BIAN_T) == 0 or sp.simplify(bian + BIAN_T) == 0) and not bian.has(k))

# D1: the algebraic y-equation
ad, a0s, Xs = sp.Symbol('adot'), sp.Symbol('a', positive=True), sp.Symbol('X', positive=True)
y, rs, Ms = sp.symbols('y rho_s M_s', positive=True)
Hk = sp.Symbol('Hk')                                        # H^2 + k/a^2
rep = lambda e_: e_.subs({Yt.diff(t): Xt*at.diff(t)}).subs({Yt: y*at}).subs({at.diff(t): ad, Xt: Xs}).subs({at: a0s})
EN2 = sp.expand(rep(EN.subs(Nt, 1)).subs(rho_f(a0s), 3*Mg**2*mg**2*rs))      # rho_* = rho/(3 M_g^2 m^2)
EX2 = sp.expand(rep(EX.subs(Nt, 1)))
EN3 = sp.expand(sp.simplify(EN2/(3*Mg**2*a0s**3)).subs(ad**2, Hk*a0s**2 - k))
EX3 = sp.expand(sp.simplify(EX2/(3*Mf**2*y**3*a0s**3)).subs(ad**2, Hk*a0s**2 - k))
HK_SOL = sp.solve(EN3, Hk)[0]
QUART = sp.factor(sp.simplify(EX3.subs(Hk, HK_SOL)*y))
check("D1: on the dynamical branch (Ydot = X adot, y = Y/a) both Friedmann equations depend on k only through "
      "H^2 + k/a^2, so the algebraic y-equation (a quartic) does not depend on k",
      not sp.simplify(EN3).has(k) and not sp.simplify(EX3).has(k) and not QUART.has(k))
VS = (bb[3]/3*y**4 + (bb[2] - bb[4]/(3*Ms**2))*y**3 + (bb[1] - bb[3]/Ms**2)*y**2
      + (rs + bb[0]/3 - bb[2]/Ms**2)*y - bb[1]/(3*Ms**2))
check("anchor: that quartic is von Strauss et al. 2012's (arXiv:1111.1655) with M_* = M_f/M_g, times m^2/y^2",
      sp.simplify(QUART.subs(Mf, Ms*Mg)/VS - mg**2/y**2) == 0)

# D2: program couplings
b1, b2, s_ = sp.symbols('beta1 beta2 s', real=True)
PROG = {bb[0]: -4*b1 - 3*b2, bb[1]: b1, bb[2]: b2, bb[3]: b1, bb[4]: -4*b1 - 3*b2}
RHO_Y = sp.factor(sp.solve(sp.expand(QUART.subs(PROG).subs(Mf, Mg)), rs)[0])
PG = (bb[0] + 3*bb[1]*y + 3*bb[2]*y**2 + bb[3]*y**3).subs(PROG)
check("program branch: rho_*(y) = (1 - y^2)(beta1 y^2 + (4 beta1 + 6 beta2) y + beta1)/(3y); H^2 + k/a^2 = "
      "m^2 (P_g(y)/3 + rho_*), P_g(1) = 0", sp.simplify(RHO_Y - (1 - y**2)*(b1*y**2 + (4*b1 + 6*b2)*y + b1)/(3*y)) == 0
      and sp.simplify(HK_SOL.subs(PROG) - mg**2*(PG/3 + rs)) == 0 and sp.simplify(PG.subs(y, 1)) == 0)
MBAR2, MX2 = 2*Mg**2, 4*mg**2*(b1 + b2)
lhs_ = 3*MBAR2*mg**2*(PG/3 + RHO_Y)
rhs_ = 3*Mg**2*mg**2*RHO_Y + (MBAR2*MX2/8)*(b1/(b1 + b2))*(1 - y)**4/y
check("D2: exact, all y: 2 P_g + 3 rho_* = beta1 (1 - y)^4/y, i.e. 3 Mbar^2 (H^2 + k/a^2) = rho + "
      "(Mbar^2 M_X^2/8)(beta1/(beta1 + beta2))(1 - y)^4/y with Mbar^2 = 2 M_g^2",
      sp.simplify(2*PG + 3*RHO_Y - b1*(y - 1)**4/y) == 0 and sp.simplify(lhs_ - rhs_) == 0)

# D3: leading order
c1 = sp.symbols('c1:4')
yser = 1 + c1[0]*rs + c1[1]*rs**2 + c1[2]*rs**3
eqs = sp.series(RHO_Y.subs(y, yser) - rs, rs, 0, 4).removeO()
solc = sp.solve([eqs.coeff(rs, n) for n in (1, 2, 3)], c1, dict=True)[0]
Hk_ser = sp.series((PG/3 + rs).subs(y, sp.expand(yser.subs(solc))), rs, 0, 3).removeO()
check("D3: y = 1 - rho_*/(4(beta1 + beta2)) + O(rho_*^2) and (H^2 + k/a^2)/m^2 = rho_*/2 + 0 rho_*^2, so "
      "1 - y = 2(H^2 + k/a^2)/M_X^2 at leading order (and 3(2 M_g^2)(H^2 + k/a^2) = rho)",
      sp.simplify(solc[c1[0]] + 1/(4*(b1 + b2))) == 0 and sp.simplify(Hk_ser.coeff(rs, 1) - sp.Rational(1, 2)) == 0 and
      sp.simplify(Hk_ser.coeff(rs, 2)) == 0 and sp.simplify(-solc[c1[0]]*rs - 2*(mg**2*rs/2)/MX2) == 0)
mp.mp.dps = 90
MBARP = mp.sqrt(mp.mpf(HBAR)*mp.mpf(C)**5/(8*mp.pi*mp.mpf(G)))/mp.mpf(EV)       # reduced Planck energy, eV
H0EV = mp.mpf(HBAR)*mp.mpf(H0)/mp.mpf(EV)
MXm = mp.mpf(MX_EV)
def one_minus_y(rho, s):
    """exact branch, beta1 = 1, s = beta2/beta1: rho_* = 8(1 + s) rho/(3 Mbar^2 M_X^2)"""
    rstar = 8*(1 + s)*rho/(3*MBARP**2*MXm**2)
    f_ = lambda yy: (1 - yy**2)*(yy**2 + (4 + 6*s)*yy + 1)/(3*yy) - rstar
    return 1 - mp.findroot(f_, 1 - rstar/(4*(1 + s)))
omy = one_minus_y(3*MBARP**2*H0EV**2, 1)                    # today, flat-limit density (H^2 + k/a^2 = H0^2)
omy_c = one_minus_y(3*MBARP**2*H0EV**2*(1 + mp.mpf('0.01')), 1)
check("D3: today, at the minimal M_X: 1 - y = 1.5e-61 (1.507e-61 flat limit; 1.522e-61 at Omega_k = -0.01; exact branch "
      "= leading order 2 H0^2/M_X^2)", float(mp.nstr(omy, 2)) == 1.5e-61 and close(float(omy), float(2*H0EV**2/MXm**2), 1e-12),
      f"{mp.nstr(omy, 4)}, {mp.nstr(omy_c, 4)}")

# D4: the Fierz-Pauli mass from homogeneous shear about f = c^2 g
cc_, d1, d2, ee = sp.symbols('c d1 d2 e', real=True)
dvec = [d1, d2, -d1 - d2]
poly2 = sp.expand(sp.prod([1 + lam*e_ for e_ in [cc_] + [cc_*sp.exp(ee*di) for di in dvec]]))
V2 = sp.simplify(sp.series(sum(bb[n]*poly2.coeff(lam, n) for n in range(5)), ee, 0, 3).removeO().coeff(ee, 2))
Kq = cc_*bb[1] + 2*cc_**2*bb[2] + cc_**3*bb[3]
Mmat = sp.Matrix([[mg**2*Mg**2*Kq, -mg**2*Mg**2*Kq], [-mg**2*Mg**2*Kq, mg**2*Mg**2*Kq]])
Kmat = sp.diag(Mg**2, Mf**2*cc_**2)        # shear kinetic terms (M^2 a^3/2) b'^2 and M_f^2 (Y^3/2X) c'^2, Y = c a, X = c
mfp2 = [z for z in (Kmat.inv()*Mmat).eigenvals() if sp.simplify(z) != 0][0]
check("D4: potential at O(shear^2) = (1/2)(c beta1 + 2c^2 beta2 + c^3 beta3) sum d_i^2; the massive shear mode has "
      "m_FP^2 = m^2 K (1 + M_g^2/(M_f^2 c^2)), which at c = 1, M_f = M_g, beta3 = beta1 is M_X^2 = 4 m^2 (beta1 + beta2)",
      sp.simplify(V2 - sp.Rational(1, 2)*Kq*sum(di**2 for di in dvec)) == 0 and
      sp.simplify(mfp2.subs({cc_: 1, Mf: Mg, bb[1]: b1, bb[2]: b2, bb[3]: b1}) - 4*mg**2*(b1 + b2)) == 0)

# D5: the broken vacua
u = sp.Symbol('u', positive=True)
PF = bb[4] + 3*bb[3]/u + 3*bb[2]/u**2 + bb[1]/u**3
PGu = bb[0] + 3*bb[1]*u + 3*bb[2]*u**2 + bb[3]*u**3
check("proportional backgrounds f = u^2 g (palindrome): P_g(u) = u^2 P_f(u) iff u(u - 1)(u + 1)(beta1 u^2 + "
      "(3 beta2 - beta0) u + beta1) = 0, for any k",
      sp.simplify(sp.expand((PGu - u**2*PF)*u) - (u - 1)*(u + 1)*(bb[1]*u**2 + (3*bb[2] - bb[0])*u + bb[1])).subs(
          {bb[3]: bb[1], bb[4]: bb[0]}) == 0)
b2_on = sp.solve(b1*u**2 + (4*b1 + 6*b2)*u + b1, b2)[0]   # flat branch: 3 beta2 - beta0 = 4 beta1 + 6 beta2
PGp = PG.subs(y, u)
check("D5: every broken vacuum (u != 1) has Lambda_g = m^2 P_g(u) = -3 m^2 (beta1 + beta2)(u - 1)^2 = "
      "18 m^2 u (beta1 + beta2)^2/beta1", sp.simplify((PGp + 3*(b1 + b2)*(u - 1)**2).subs(b2, b2_on)) == 0 and
      sp.simplify((PGp - 18*u*(b1 + b2)**2/b1).subs(b2, b2_on)) == 0)
ex_roots = sorted(float(z) for z in sp.solve(-u**2 + (-4 + 12)*u - 1, u))
print(f"      e.g. beta1 = -1, beta2 = 2: u = {ex_roots[0]:.5f}, {ex_roots[1]:.5f}, Lambda_g/m^2 = "
      f"{[round(float(PGp.subs({b1: -1, b2: 2, u: z})), 4) for z in ex_roots]} (bimetric_flrw.out: -2.2863, -141.7137)")

# D6: G_eff, the halfway point and the gradient instability
check("D6: as y -> 0 (rho_* ~ beta1/(3y)), (H^2 + k/a^2)/(m^2 rho_*) -> 1, i.e. H^2 + k/a^2 -> rho/(3 M_g^2): "
      "G_eff -> 2 G_N", sp.limit(((PG/3 + rs)/rs).subs(y, b1/(3*rs)), rs, sp.oo) == 1 and
      sp.limit(RHO_Y*y, y, 0) == b1/3)
mp.mp.dps = 30
MBARP, MXm = +MBARP, +MXm
def bim_state(yv, s):
    """(rho, H^2 + k/a^2) on the exact branch at y, beta1 = 1, in eV units"""
    rho = (1 - yv**2)*(yv**2 + (4 + 6*s)*yv + 1)/(3*yv)*3*MBARP**2*MXm**2/(8*(1 + s))
    Pg_ = (-4 - 3*s) + 3*yv + 3*s*yv**2 + yv**3
    return rho, rho/(3*MBARP**2/2) + MXm**2/(4*(1 + s))*Pg_/3
def T_of_rho(rho):
    return (30*rho/(mp.pi**2*mp.mpf('106.75')))**mp.mpf('0.25')
half = {}
for sv in (0, 1):
    lo_, hi_ = mp.mpf('0.01'), mp.mpf('0.99')
    for _ in range(100):
        mid = (lo_ + hi_)/2
        rho_, hk2 = bim_state(mid, sv)
        if rho_/(3*hk2) < mp.mpf('0.75')*MBARP**2:
            lo_ = mid
        else:
            hi_ = mid
    rho_, hk2 = bim_state(lo_, sv)
    half[sv] = (float(T_of_rho(rho_))/1e12, float(mp.sqrt(hk2)/MXm), float(lo_))
print("      G_eff halfway (M_eff^2 = 1.5 M_g^2) at the minimal M_X, g* = 106.75: " + "; ".join(
      f"s = {sv}: y = {v[2]:.4f}, H/M_X = {v[1]:.4f}, T = {v[0]:.4f} TeV" for sv, v in half.items()))
check("D6: G_eff is halfway between G_N and 2 G_N at T = 1.55-1.58 TeV (s = 1, 0; quoted as ~1.5 TeV)",
      round(half[1][0], 2) == 1.55 and round(half[0][0], 2) == 1.58)
r_, w_, rp_ = sp.symbols('r w rp', real=True)
rhoK = bb[1]/r_ - bb[0] + 3*bb[2] + 3*(bb[3] - bb[1])*r_ + (bb[4] - 3*bb[2])*r_**2 - bb[3]*r_**3   # Konnig 2015
B2r = bb[1] + 2*bb[2]*r_ + bb[3]*r_**2
B3r = bb[1] + 4*bb[2]*r_ + 3*bb[3]*r_**2
line1 = rp_*((r_**2 + 1)*(bb[1] - bb[3]*r_**2)*rp_/(rhoK*(w_ + 1)) - r_**2*B3r/B2r)/(3*r_**3) - 1   # eq. (eigenfreq)
L1 = line1.subs(rp_, -3*(1 + w_)*rhoK/sp.diff(rhoK, r_)).subs(PROG).subs(b2, s_*b1).subs(b1, 1)
fL = sp.lambdify((r_, w_, s_), L1, 'numpy')
check("D6: Konnig 2015 eq. (eigenfreq) on the program branch: omega^2/(k/calH)^2 -> 2w + 1 at high density (r -> 0), "
      "so the scalar gradient instability needs w > -1/2", all(abs(fL(1e-9, wv, sv) - (2*wv + 1)) < 1e-6
      for wv in (-0.999, -0.6, -0.499, 0.0, 1/3) for sv in (-0.5, 1.0, 10.0)))
rgrid = np.linspace(1e-6, 1 - 1e-9, 100001)
crit = []
for wv in (1/3, 0.0):
    for sv in (-0.5, 0.0, 1.0, 10.0):
        vals = fL(rgrid, wv, sv)
        j = np.where(np.diff(np.sign(vals)) != 0)[0][-1]
        lo_, hi_ = rgrid[j], rgrid[j + 1]
        for _ in range(60):
            mid = 0.5*(lo_ + hi_)
            if np.sign(fL(mid, wv, sv)) == np.sign(vals[j]):
                lo_ = mid
            else:
                hi_ = mid
        rc = mp.mpf(lo_)
        m2 = MXm**2/(4*(1 + sv))
        rho_ = MBARP**2/2*m2*(1 - rc**2)*(rc**2 + (4 + 6*sv)*rc + 1)/rc
        hk = mp.sqrt(m2*(1 + 3*sv*rc + 3*rc**2 + (-4 - 3*sv)*rc**3)/(3*rc))
        crit.append((float(T_of_rho(rho_))/1e9, float(hk/MXm), wv, sv, float(rc)))
print("      gradient-instability crossover (unstable above): " + "; ".join(
      f"w = {c_[2]:.2g}, s = {c_[3]:g}: r_c = {c_[4]:.4f}, T = {c_[0]:.0f} GeV, H/M_X = {c_[1]:.3f}" for c_ in crit))
check("D6: the gradient instability (radiation or dust) operates above T = 1.31-1.38 TeV, i.e. H/M_X = 0.47-0.52 "
      "(~1.3 TeV, H ~ 0.5 M_X)", all(1305 < c_[0] < 1380 and 0.46 < c_[1] < 0.53 for c_ in crit) and
      round(min(c_[0] for c_ in crit)) == 1309 and round(max(c_[0] for c_ in crit)) == 1377)

# D7: SO(4)-invariant tensors on S^3 = invariants of the isotropy SO(3) at a point
eps3 = np.zeros((3, 3, 3))
for i_, j_, k_ in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    eps3[i_, j_, k_], eps3[i_, k_, j_] = 1, -1
Tso3 = [-eps3[i_] for i_ in range(3)]
Amat = np.vstack([np.kron(Ta, np.eye(3)) + np.kron(np.eye(3), Ta) for Ta in Tso3])
SYM = np.array([(np.eye(9)[3*i_ + j_] + np.eye(9)[3*j_ + i_])/2 for (i_, j_) in
                [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]]).T
n_sym = 6 - np.linalg.matrix_rank(Amat @ SYM)
n_vec = 3 - np.linalg.matrix_rank(np.vstack(Tso3))
check("D7: SO(3)-invariant symmetric 2-tensors at a point of S^3 (the isotropy of SO(4)) form a space of dimension 1 "
      "(the round metric), with no invariant vectors: an SO(4)-invariant f is -X^2 dt^2 + Y^2 gamma_(k=+1)",
      n_sym == 1 and n_vec == 0, f"dim {n_sym}, vectors {n_vec}")

# D8: a frozen flat reference and a fixed scale
chi_, th_ = sp.symbols('chi theta', real=True)
coords = [t, chi_, th_, sp.Symbol('phi', real=True)]
gF = sp.diag(-Xt**2, Yt**2, Yt**2*sp.sin(chi_)**2, Yt**2*sp.sin(chi_)**2*sp.sin(th_)**2)
gFi = gF.inv()
def Gam(a_, b_, c_):
    return sum(gFi[a_, d_]*(sp.diff(gF[d_, b_], coords[c_]) + sp.diff(gF[d_, c_], coords[b_]) -
                            sp.diff(gF[b_, c_], coords[d_])) for d_ in range(4))/2
R1212 = sp.simplify(sp.diff(Gam(1, 2, 2), coords[1]) - sp.diff(Gam(1, 2, 1), coords[2]) +
                    sum(Gam(1, 1, e_)*Gam(e_, 2, 2) - Gam(1, 2, e_)*Gam(e_, 2, 1) for e_ in range(4)))
check("D8: f = -X^2 dt^2 + Y^2 gamma_(k=+1) has R^chi_(theta chi theta) = (X^2 + Ydot^2) sin^2(chi)/X^2, never zero: "
      "a flat reference cannot be put in k = +1 form", sp.simplify(R1212 - (Xt**2 + Yt.diff(t)**2)*sp.sin(chi_)**2/Xt**2) == 0)
Y0 = sp.Symbol('Y0', positive=True)
fixed = sp.factor(BIAN_T.subs({Yt: Y0, Xt: 1}).doit())
check("D8: with a fixed scale (Ydot = 0) the Bianchi constraint is -3 m^2 M_g^2 (beta1 a^2 + 2 beta2 a Y0 + beta3 Y0^2) adot: "
      "proportional to adot", sp.simplify(fixed + 3*mg**2*Mg**2*(bb[1]*at**2 + 2*bb[2]*at*Y0 + bb[3]*Y0**2)*at.diff(t)) == 0)

# D9: the turnaround toy (M_g = M_f = m = 1, beta1 = beta2 = 1, k = 1, dust 9.5/a^3 + radiation 0.05/a^4): the f lapse
# X = y - 3(rho + p) dy/drho is a function of a alone and never divides by adot
TB = [-7.0, 1.0, 1.0, 1.0, -7.0]
aS, adS, addS, YS, YdS, XS = sp.symbols('a ad add Y Yd X')
af_, Yf_, Xf_ = [sp.Function(n_)(t) for n_ in ('af', 'Yf', 'Xf')]
UNt = TB[0]*af_**3 + 3*TB[1]*af_**2*Yf_ + 3*TB[2]*af_*Yf_**2 + TB[3]*Yf_**3
UXt = TB[1]*af_**3 + 3*TB[2]*af_**2*Yf_ + 3*TB[3]*af_*Yf_**2 + TB[4]*Yf_**3
Lt = (3*(-af_*af_.diff(t)**2 + af_) + 3*(-Yf_*Yf_.diff(t)**2/Xf_ + Xf_*Yf_) - (UNt + Xf_*UXt)
      - af_**3*(9.5/af_**3 + 0.05/af_**4))
def clean(e_):
    e_ = e_.subs({af_.diff(t, 2): addS}).subs({Xf_.diff(t): 0, af_.diff(t): adS, Yf_.diff(t): YdS})
    return sp.expand(e_.subs({af_: aS, Yf_: YS, Xf_: XS}))
f_add = sp.lambdify((aS, adS, YS, XS), sp.solve(clean(EL(Lt, af_)), addS)[0])
f_EN = sp.lambdify((aS, adS, YS), clean(3*(af_*af_.diff(t)**2 + af_) - UNt - af_**3*(9.5/af_**3 + 0.05/af_**4)))
f_EX = sp.lambdify((aS, adS, YS, YdS, XS), clean(sp.diff(Lt, Xf_)))
def toy_state(A):
    r_ = 9.5/A**3 + 0.05/A**4
    lo_, hi_ = 1e-12, 1.0
    for _ in range(60):
        mid = 0.5*(lo_ + hi_)
        if (1 - mid**2)*(mid**2 + 10*mid + 1)/(3*mid) > r_/3:
            lo_ = mid
        else:
            hi_ = mid
    yv = 0.5*(lo_ + hi_)
    drs = (-3*yv**2 - 8*yv - 1/yv**2 - 12*yv)/3
    return r_, yv, yv - 3*(r_ + 0.05/(3*A**4))/(3*drs)
def toy_F(A):
    r_, yv, _ = toy_state(A)
    return A**2*((TB[0] + 3*yv + 3*yv**2 + yv**3)/3 + r_/3) - 1
lo_, hi_ = 1e-3, 50.0
for _ in range(80):
    mid = 0.5*(lo_ + hi_)
    if toy_F(mid) > 0:
        lo_ = mid
    else:
        hi_ = mid
AMAX_T = 0.5*(lo_ + hi_)
_, YT, XT = toy_state(AMAX_T)
def toy_rhs(A, V):
    _, yv, Xv = toy_state(A)
    return V, f_add(A, V, yv*A, Xv)
A_, V_ = 0.95*AMAX_T, sqrt(toy_F(0.95*AMAX_T))
hstep, path = 1e-3, []
while True:                                             # RK4 through the turnaround
    k1_ = toy_rhs(A_, V_); k2_ = toy_rhs(A_ + hstep/2*k1_[0], V_ + hstep/2*k1_[1])
    k3_ = toy_rhs(A_ + hstep/2*k2_[0], V_ + hstep/2*k2_[1]); k4_ = toy_rhs(A_ + hstep*k3_[0], V_ + hstep*k3_[1])
    A_ += hstep/6*(k1_[0] + 2*k2_[0] + 2*k3_[0] + k4_[0]); V_ += hstep/6*(k1_[1] + 2*k2_[1] + 2*k3_[1] + k4_[1])
    path.append((A_, V_))
    if V_ < 0 and A_ < 0.95*AMAX_T:
        break
resN = resX = 0.0
Xmin = float('inf')
for A_, V_ in path[::10]:
    r_, yv, Xv = toy_state(A_)
    scale_ = 3*A_**3*(toy_F(A_) + 1)/A_**2
    resN = max(resN, abs(f_EN(A_, V_, yv*A_))/scale_)
    resX = max(resX, abs(f_EX(A_, V_, yv*A_, Xv*V_, Xv))/scale_)
    Xmin = min(Xmin, Xv)
dA = 1e-5*AMAX_T
dYda = (toy_state(AMAX_T + dA)[1]*(AMAX_T + dA) - toy_state(AMAX_T - dA)[1]*(AMAX_T - dA))/(2*dA)
amax_num = max(p_[0] for p_ in path)
print(f"      toy: a_max = {AMAX_T:.6f} (integrated {amax_num:.6f}), y = {YT:.6f}, X = {XT:.6f}, dY/da = {dYda:.6f}; "
      f"max relative residuals of the g and f Friedmann equations {resN:.1e}, {resX:.1e}; min X on the path {Xmin:.5f}")
check("D9: through adot = 0 the f lapse is regular: a_max = 1.588667, X = dY/da = 1.226664 at the turnaround, X > 0 "
      "on the path, both Friedmann constraints hold along the integrated path",
      round(AMAX_T, 6) == 1.588667 and round(XT, 6) == 1.226664 and abs(dYda - XT) < 1e-7 and abs(amax_num - AMAX_T) < 1e-6
      and Xmin > 1 and resN < 1e-9 and resX < 1e-9 and path[0][1] > 0 > path[-1][1])
print(f"      [{time.time() - T_START:.1f} s]")


# ======================================================================================================
print("\n== E. Momentum space and reciprocity (ports of verify-minisuperspace-derivation/d5_fibre_and_measure.py, "
      "momentum-space/compact_reciprocity.py, critic/e_polarization_integrability.py, b_compact_phase_space.py, "
      "a_dualcurv_conventions.py, h_misc.py, minisuperspace/closure_epochs.py, radius_mass_pairing.py, dynamics/context.py)")
# ======================================================================================================
# E1: the fibre metric
x11, x12, x22, y11, y12, y22 = sp.symbols('x11 x12 x22 y11 y12 y22', real=True)
Xm = sp.Matrix([[x11, x12], [x12, x22]]); Ym = sp.Matrix([[y11, y12], [y12, y22]])
Yi = Ym.inv()
HZ = sp.BlockMatrix([[Ym + Xm*Yi*Xm, Xm*Yi], [Yi*Xm, Yi]]).as_explicit()
p1, p2, p3 = sp.symbols('p1 p2 p3', real=True)
fibre = G_S3.inv().subs({chi_: sp.Rational(7, 10), th_: sp.Rational(11, 10)})
check("E1: the generalized metric H_Z = [[Y + X Y^-1 X, X Y^-1], [Y^-1 X, Y^-1]] has p-p block Y^-1 = g^-1 for any X "
      "(d = 2, det H_Z = 1): the fibre metric over a point does not depend on p, so the fibre is flat (k~ = 0; "
      "Ricci scalar of the S^3 fibre metric at a point = 0)", sp.simplify(HZ[2:, 2:] - Yi) == sp.zeros(2, 2) and
      sp.simplify(HZ.det() - 1) == 0 and ricci_scalar(fibre, [p1, p2, p3]) == 0)

# E2: grain and spectrum
nu_big = 10**6
check("E2: S^3 momentum spectrum p = hbar sqrt(nu^2 - 1)/R (from the anchor's eigenvalues): lowest sqrt(3) hbar/R, "
      "spacing -> hbar/R (the grain; hbar c/R as an energy)", abs((sqrt(nu_big**2 - 1) - sqrt((nu_big - 1)**2 - 1)) - 1)
      < 1e-6 and abs(sqrt(2**2 - 1) - sqrt(3)) < 1e-15)

# E3: a localized state on S^3_R
mp.mp.dps = 30
def kin_ratio(s):
    """<-Laplacian> R^2 of exp(-chi^2/(4 s^2)) on the unit S^3 (s = sigma/R), over the flat 3/(4 s^2)"""
    num = mp.quad(lambda c_: (c_/(2*s**2))**2*mp.exp(-c_**2/(2*s**2))*mp.sin(c_)**2, [0, min(40*s, mp.pi)])
    den = mp.quad(lambda c_: mp.exp(-c_**2/(2*s**2))*mp.sin(c_)**2, [0, min(40*s, mp.pi)])
    return num/den/(3/(4*s**2))
coef = [float((kin_ratio(mp.mpf(sv)) - 1)/mp.mpf(sv)**2) for sv in (0.01, 0.003)]
cs_, sg_ = sp.symbols('c sigma', positive=True)
I_ = lambda n_: sp.integrate(cs_**n_*sp.exp(-cs_**2/(2*sg_**2)), (cs_, 0, sp.oo))
ratio_ser = sp.series((I_(4) - I_(6)/3)/(4*sg_**4)/(I_(2) - I_(4)/3)/(3/(4*sg_**2)), sg_, 0, 3).removeO()
E3_VAL = 2/3*(1.0/R0_of(1e-2))**2
check("E3: <p^2> of a Gaussian of geodesic width sigma on S^3_R = (3 hbar^2/4 sigma^2)(1 - (2/3)(sigma/R)^2 + ...): "
      "coefficient -2/3 by quadrature and from the Gaussian moments; (2/3)(sigma/R0)^2 = 3.5e-55 at sigma = 1 m, "
      "|Omega_k| = 1e-2", abs(coef[1] + 2/3) < 1e-5 and sp.simplify(ratio_ser - (1 - sp.Rational(2, 3)*sg_**2)) == 0 and
      float(f"{E3_VAL:.2g}") == 3.5e-55, f"c = {coef[0]:.6f} (sigma/R = 0.01), {coef[1]:.6f} (0.003); {E3_VAL:.3e}")

# E4: integrability of the Born-rotated polarizations on T*S^3 (left trivialization, frame [e_a, e_b] = (2/R) eps_abc e_c)
Rr, ell, thp = sp.symbols('R ell theta', positive=True)
pv = sp.symbols('p1:4', real=True)
eps = sp.LeviCivita
def bracket(V, W, Rinv):
    A, B = V; Cc, D = W
    der = lambda Bvec, f_: sum(Bvec[i]*sp.diff(f_, pv[i]) for i in range(3))
    base = [sum(A[a_]*Cc[b_]*2*Rinv*eps(a_, b_, c_) for a_ in range(3) for b_ in range(3))
            + der(B, Cc[c_]) - der(D, A[c_]) for c_ in range(3)]
    fib = [der(B, D[c_]) - der(D, B[c_]) for c_ in range(3)]
    return [sp.simplify(x_) for x_ in base], [sp.simplify(x_) for x_ in fib]
def omega_(V, W, Rinv):
    A, B = V; Cc, D = W
    val = sum(B[a_]*Cc[a_] - D[a_]*A[a_] for a_ in range(3))
    val += -2*Rinv*sum(pv[d_]*eps(b_, c_, d_)*A[b_]*Cc[c_] for b_ in range(3) for c_ in range(3) for d_ in range(3))
    return sp.simplify(val)
def horizontal(a_, Rinv):
    return [1 if i == a_ else 0 for i in range(3)], [Rinv*sum(eps(a_, c_, b_)*pv[b_] for b_ in range(3)) for c_ in range(3)]
def vertical(a_):
    return [0, 0, 0], [1 if i == a_ else 0 for i in range(3)]
def comb(cv, V, ch, Hh):
    return [cv*V[0][i] + ch*Hh[0][i] for i in range(3)], [cv*V[1][i] + ch*Hh[1][i] for i in range(3)]
integ = {}
for label, Rinv in [('S3', 1/Rr), ('T3', 0)]:
    Hs = [horizontal(a_, Rinv) for a_ in range(3)]
    Vs = [vertical(a_) for a_ in range(3)]
    Ls = [comb(sp.cos(thp), Vs[a_], sp.sin(thp)*ell, Hs[a_]) for a_ in range(3)]
    Ps = [comb(-sp.sin(thp), Vs[a_], sp.cos(thp)*ell, Hs[a_]) for a_ in range(3)]
    lag = all(sp.simplify(omega_(Ls[i], Ls[j], Rinv)) == 0 for i in range(3) for j in range(3))
    br = bracket(Ls[0], Ls[1], Rinv)
    cL, cP = sp.symbols('cL1:4'), sp.symbols('cP1:4')
    eqs = []
    for i in range(3):
        eqs.append(sp.Eq(br[0][i], sum(cL[a_]*Ls[a_][0][i] + cP[a_]*Ps[a_][0][i] for a_ in range(3))))
        eqs.append(sp.Eq(br[1][i], sum(cL[a_]*Ls[a_][1][i] + cP[a_]*Ps[a_][1][i] for a_ in range(3))))
    sol = sp.solve(eqs, list(cL) + list(cP), dict=True)[0]
    off = [sp.simplify(sol[c_]) for c_ in cP]
    integ[label] = (lag, off, {nm: all(sp.simplify(x_.subs(thp, v_)) == 0 for x_ in off)
                               for nm, v_ in (('0', 0), ('pi/4', sp.pi/4), ('pi/2', sp.pi/2))})
lagS, offS, atS = integ['S3']
lagT, offT, atT = integ['T3']
print(f"      [L_1, L_2] outside L_theta on T*S^3: {[sp.factor(x_) for x_ in offS]}")
check("E4: on T*S^3 every L_theta = span{cos(theta) d/dp_a + sin(theta) ell H_a} is Lagrangian; the Frobenius "
      "obstruction is ell^2 p sin^3(theta)/R^2", lagS and sp.simplify(offS[0] - ell**2*pv[1]*sp.sin(thp)**3/Rr**2) == 0
      and sp.simplify(offS[1] + ell**2*pv[0]*sp.sin(thp)**3/Rr**2) == 0 and offS[2] == 0)
check("E4: L_theta is integrable at theta = 0 and not at pi/4 or pi/2 (the mirror) on T*S^3; on T^3 every theta is",
      atS == {'0': True, 'pi/4': False, 'pi/2': False} and lagT and all(atT.values()))
check("E4: the curvature measure (L/R0)^2 at L = 1 m, |Omega_k| = 1e-2 is 5.309e-55", r4((1.0/R0_of(1e-2))**2) == 5.309e-55,
      f"{(1.0/R0_of(1e-2))**2:.4e}")

# E5: compact phase spaces
def prod_betti(b1_, b2_):
    out = [0]*(len(b1_) + len(b2_) - 1)
    for i, x_ in enumerate(b1_):
        for j, y_ in enumerate(b2_):
            out[i + j] += x_*y_
    return out
XB = [1, 0, 0, 1]                                       # S^3 or any rational homology 3-sphere (S^3/Gamma)
Ms_ = {'S^3': [1, 0, 0, 1], 'T^3': [1, 3, 3, 1], 'S^1 x S^2': [1, 1, 1, 1], 'genus-2 x S^1': [1, 5, 5, 1]}
check("E5: Kunneth: for X a rational homology 3-sphere, H^2(X x M) = H^2(M) for every closed 3-manifold M, so every "
      "class [omega] is pulled back from M and [omega]^3 = 0: X x M is not symplectic (S^3 x S^3 has b2 = 0)",
      all(prod_betti(XB, M_)[2] == M_[2] for M_ in Ms_.values()) and prod_betti(XB, XB) == [1, 0, 0, 2, 0, 0, 1])
rng = np.random.default_rng(20261027)
qmax, ranks = 0.0, []
for _ in range(50):
    Qm, _r = np.linalg.qr(rng.normal(size=(5, 2)))
    z = Qm[:, 0] + 1j*Qm[:, 1]
    qmax = max(qmax, abs(np.sum(z*z)))
    W = np.linalg.svd(np.vstack([z, np.conj(z)]))[2][2:].conj().T
    Tm = np.hstack([W, 1j*W])
    ranks.append(np.linalg.matrix_rank(np.imag(Tm.conj().T @ Tm)/np.vdot(z, z).real, tol=1e-9))
def Mgen(a_, b_):
    m_ = np.zeros((5, 5)); m_[a_, b_] = 1; m_[b_, a_] = -1
    return m_
O5 = np.eye(5)                                          # rotation by pi/2 in the (4,5) plane
O5[3, 3] = O5[4, 4] = np.cos(np.pi/2); O5[3, 4], O5[4, 3] = -np.sin(np.pi/2), np.sin(np.pi/2)
Ad = lambda m_: O5 @ m_ @ O5.T
res5 = max([np.linalg.norm(Ad(Mgen(i, 3)) - Mgen(i, 4)) for i in range(3)] + [np.linalg.norm(Ad(Mgen(i, 4)) + Mgen(i, 3))
           for i in range(3)] + [np.linalg.norm(Ad(Mgen(i, j)) - Mgen(i, j)) for i, j in combinations(range(3), 2)]
           + [np.linalg.norm(Ad(Mgen(3, 4)) - Mgen(3, 4))])
check("E5: Gr~(2,5) = SO(5)/(SO(2) x SO(3)) is the quadric Q3 in CP^4 (z = u + i v), where the Fubini-Study form is "
      "non-degenerate (Kahler); the SO(5) reciprocity automorphism (pi/2 in the (4,5) plane: X -> P, P -> -X, M_45 "
      "fixed) has residual ~1e-16", qmax < 1e-14 and min(ranks) == 6 and res5 < 1e-15, f"{qmax:.1e}, residual {res5:.1e}")
LAM_SD = sqrt(R0_of(1e-2)*L_P)
check("E5: its Born length sqrt(R0 l_P) = 1.489e-4 m at |Omega_k| = 1e-2", r4(LAM_SD) == 1.489e-4, f"{LAM_SD:.4e} m")
F_H = ALPHA*HBAR*C/A_BOHR**2                            # hydrogen Coulomb force at the Bohr radius (#13's criterion)
LAM13, LAMX_Q = sqrt(HBAR*C/F_H), 37.7e-6               # X's range as quoted, 37.7 um
kap = lambda R_, lam_: HBAR*C*R_/lam_**2/E_P            # kappa c from lambda = sqrt(R hbar/kappa), in E_P
# The quoted numbers were computed (critic/h_misc.py) from rounded inputs: today's R0 at |Omega_k| = 1.13e-3, the
# turnaround floor R_max = 1.174e5 Gpc, lambda_X = 37.7 um. They are checked with those inputs; the third digit of the
# first moves with the rounding (printed below), the others do not.
R_TODAY_Q, R_FLOOR_Q = R0_of(1.13e-3), 1.174e5*GPC
kt = (kap(R_TODAY_Q, LAMX_Q), kap(R_TODAY_Q, LAM13), kap(R_FLOOR_Q, LAMX_Q), kap(R_FLOOR_Q, LAM13))
check("E5: kappa c >= 46.4 E_P (X range 37.7 um) and >= 1.72e11 E_P (#13's maximum force, lambda <= 6.195e-10 m) today "
      "(|Omega_k| = 1.13e-3); 4.1e4 and 1.5e14 E_P at the turnaround floor R_max = 1.174e5 Gpc",
      round(kt[0], 1) == 46.4 and r3(kt[1]) == 1.72e11 and float(f"{kt[2]:.2g}") == 4.1e4 and float(f"{kt[3]:.2g}") == 1.5e14
      and r4(LAM13) == 6.195e-10, ", ".join(f"{x_:.4e}" for x_ in kt))
ku = (kap(AD['R0_m'], LAMX_Q), kap(AD['R0_m'], LAM_X), kap(AD['R0_m'], LAM13), kap(AD['Rmax_m'], LAMX_Q),
      kap(AD['Rmax_m'], LAM13))
print(f"      with unrounded inputs (|Omega_k| < {B_DESI:.7f}, R_max = {AD['Rmax']:.5e} Gpc): {ku[0]:.2f} E_P (37.7 um), "
      f"{ku[1]:.2f} E_P (lambda_X = {LAM_X*1e6:.2f} um), {ku[2]:.4e}; floor {ku[3]:.4e}, {ku[4]:.4e} E_P")
check("E5: with unrounded inputs the X-range figure is 46.5 E_P, the others unchanged at their quoted digits",
      round(ku[0], 1) == 46.5 and round(ku[1], 1) == 46.5 and r3(ku[2]) == 1.72e11 and
      float(f"{ku[3]:.2g}") == 4.1e4 and float(f"{ku[4]:.2g}") == 1.5e14)

# E6: photons in the 3-sphere
NG = [N_GAMMA0*2*pi**2*R0_of(ok)**3 for ok in (1e-2, 1e-5)]
check("E6: photons in the whole S^3, n_gamma 2 pi^2 R0^3 = 2.1e91 (|Omega_k| = 1e-2) to 6.6e95 (1e-5) "
      "(context.out: 2.0961e91, 6.6285e95)", float(f"{NG[0]:.2g}") == 2.1e91 and float(f"{NG[1]:.2g}") == 6.6e95 and
      r4(NG[0]) == 2.096e91 and r4(NG[1]) == 6.629e95, f"{NG[0]:.4e}, {NG[1]:.4e}")

# E7: the symmetric dual-curvature reading (k~ = k, v M~^2 = M_P^2), |Omega_k| = 1e-2
Rq, lamq, R0q, Cq, ellq = sp.symbols('R lambda R0 C ell', positive=True)
aq = Rq/ellq
check("E7 (sympy): with a atilde = C, the a^-6 term over M_P^2 is (R_sd/R)^6 and dual over our curvature is (R_sd/R)^2, "
      "R_sd = sqrt(C) ell, in either normalization (ell = lambda or R0)",
      sp.simplify(Cq**3/aq**6 - (sp.sqrt(Cq)*ellq/Rq)**6) == 0 and sp.simplify(Cq/aq**2 - (sp.sqrt(Cq)*ellq/Rq)**2) == 0)
T0EV = KB*T0/EV
G_S0 = 2 + (7/8)*6*(4/11)
E_INF_EV = 1.39e25          # E_inf < 1.39e16 GeV: Soman et al. 2025 from r < 0.036, the record's bound
T_RH_EV = E_INF_EV*(30/(pi**2*106.75))**0.25
A_BBN = (T0EV/1e6)*(G_S0/10.75)**(1/3)                  # T = 1 MeV, g*s = 10.75
A_END = (T0EV/T_RH_EV)*(G_S0/106.75)**(1/3)             # instantaneous reheating, Standard Model g*s = 106.75
OMEGA_NU1 = NU1*OGAM
OKT_MAX = 0.394*OMEGA_NU1   # Delta N_eff > -0.394: Planck 2018 + BAO N_eff = 2.99 +- 0.17 at 2 sigma, SM 3.044 (dual_closure.py)
R0e = R0_of(1e-2)
up_bbn = 0.1**(1/6)*A_BBN*R0e                           # a^-6 term <= 10% of M_P^2 at T = 1 MeV
up_neff = R0e*sqrt(OKT_MAX/1e-2)
n_lhc = 6.8e12*R0e/HBARC_EVM                            # LHC 6.8 TeV beam protons: mode index p R0/hbar
lam_late = up_bbn*sqrt(pi/n_lhc)                        # momentum cap n <= pi R_sd^2/lambda^2
lam_inf = A_END*R0e*exp(-55)*sqrt(pi/n_lhc)             # standard inflation: R_sd below R at pivot exit, N* = 55
lam2 = sqrt(L_P*L_H)
print(f"      |Omega_k| = 1e-2: Omega_nu1 = {OMEGA_NU1:.5e}, a_BBN = {A_BBN:.4e}, a_end = {A_END:.4e}; R_sd <= {up_bbn:.4e} m "
      f"(BBN), {up_neff:.4e} m (N_eff); lambda <= {lam_late:.4e} m (LHC cap + N_eff + BBN), {lam_inf:.4e} m (+ inflation)")
check("E7: at |Omega_k| = 1e-2: BBN bound R_sd <= 1.568e17 m, N_eff bound 3.029e25 m; the LHC 6.8 TeV cap plus N_eff "
      "plus BBN needs lambda <= 1.278e-6 m, adding standard inflation (N* = 55) lambda <= 1.986e-49 m",
      r4(up_bbn) == 1.568e17 and r4(up_neff) == 3.029e25 and r4(lam_late) == 1.278e-6 and r4(lam_inf) == 1.986e-49)
check("E7: for lambda = sqrt(l_P c/H0) the window is empty: the LHC cap needs R_sd >= 5.779e18 m > 1.568e17 m",
      lam2*sqrt(n_lhc/pi) > up_bbn and r4(lam2*sqrt(n_lhc/pi)) == 5.779e18, f"{lam2*sqrt(n_lhc/pi):.4e} m")

# E8: the inflationary throat of closed de Sitter space, R_min = c/H_inf
H_INF = sqrt(8*pi*G*(E_INF_EV*EV)**4/(HBAR*C)**3/(3*C**2))   # flat-limit Friedmann at energy density E_inf^4
R_MIN = C/H_INF
check("E8: with E_inf < 1.39e16 GeV (Soman et al. 2025, r < 0.036) and H_inf^2 = 8 pi G E_inf^4/(3 (hbar c)^3 c^2): "
      "c/H_inf = sqrt(3/8pi)(E_P/E_inf)^2 l_P = 2.67e5 l_P, and atilde = l_P H_inf/c <= 3.75e-6 there (lambda = l_P)",
      close(R_MIN/L_P, sqrt(3/(8*pi))*(E_P/(E_INF_EV*EV))**2, 1e-9) and r3(R_MIN/L_P) == 2.67e5 and
      r3(L_P/R_MIN) == 3.75e-6, f"c/H_inf = {R_MIN:.4e} m = {R_MIN/L_P:.4e} l_P; atilde = {L_P/R_MIN:.4e}")

# E9: the dual terms after inflation (closure units C = 1, v M~^2 = M_P^2, lambda = l_P)
eps6 = [(L_P/(A_END*R0_of(ok)))**6 for ok in (1e-5, 1e-4, 1e-3, 1e-2)]
check("E9: the a^-6 term after inflation is largest at its end and below 1e-198 for |Omega_k| <= 1e-2 (log10 = -198.39 "
      "at 1e-2; later epochs smaller as (l_P/R)^6)", max(eps6) < 1e-198 and round(log10(eps6[-1]), 2) == -198.39,
      f"log10 = {[round(log10(e_), 2) for e_ in eps6]}")
print(f"      (the bound is on the a^-6 term, the only dual term at k~ = 0; under the symmetric reading k~ = k the dual "
      f"curvature over ours is (l_P/R)^2 = 10^{2*log10(L_P/(A_END*R0_of(1e-2))):.2f} at the end of inflation)")

# E10: the R - Mc pairing
hq, cq, Gq, Hq, fq, xq = sp.symbols('hbar c G H f x', positive=True)
Mq = 2*sp.pi**2*Rq**3*3*(Hq**2 + cq**2/Rq**2)/(8*sp.pi*Gq)  # M = rho 2 pi^2 R^3, rho from the closed Friedmann equation
Aq = sp.simplify(fq*(Rq/sp.sqrt(hq*Gq/cq**3))/(Mq*cq/(sp.sqrt(hq*cq/Gq)*cq)))
check("E10: (D_x/l_P)/(D_p/(m_P c)) = f R c^2/(G M) = f (4/3pi)/(1 + (HR/c)^2), hbar-free; at H = 0, G M/c^2 = (3 pi/4) R "
      "(the cycloid's R_max = 4 G M/(3 pi c^2))", sp.simplify(Aq - fq*sp.Rational(4, 3)/sp.pi/(1 + (Hq*Rq/cq)**2)) == 0 and
      sp.diff(Aq, hq) == 0 and sp.simplify(Gq*Mq.subs(Hq, 0)/cq**2 - 3*sp.pi/4*Rq) == 0)
asp = [4*fv/(3*pi) for fv in (1, 2, pi, 2*pi)]
check("E10: the aspect ratio at a turnaround spans 4/(3 pi) = 0.4244 (D_x = R) to 8/3 (D_x = 2 pi R) across conventions",
      abs(asp[0] - 0.4244) < 1e-4 and abs(asp[-1] - 8/3) < 1e-12 and asp == sorted(asp), f"{[round(x_, 4) for x_ in asp]}")

# ======================================================================================================
print("\n== F. Topology of the polarization manifold (port of gravity-sector/grassmannian_homotopy.py; gravity-sector "
      "C35-C38; flag 61)")
# ======================================================================================================
# Lambda(4) = U(4)/O(4), the Lagrangian Grassmannian of R^8, is the space of polarizations. Its homotopy follows from the
# fibration O(4) -> U(4) -> U(4)/O(4) and standard inputs [T]: pi_0(O(4)) = Z2, pi_1(O(4)) = Z2, pi_2(O(4)) = 0,
# pi_3(O(4)) = Z + Z (left and right multiplication by unit quaternions), pi_1(U(4)) = Z (the winding of det),
# pi_2(U(4)) = 0, pi_3(U(4)) = Z (the winding number W[g] = (1/24 pi^2) Int_{S^3} Tr (g^-1 dg)^3). The maps computed are
# pi_1(O(4)) -> pi_1(U(4)) and pi_3(SO(4)) -> pi_3(U(4)). Two literature anchors come first: |W| = 1 for SU(2)'s
# fundamental and |W| = 4 for SO(3) in SO(4) acting on R^4 (spin 1 plus spin 0, Dynkin index 4). The groups derived
# must match Bott periodicity's stable values for U/O. On the light Maslov circle alone pi_2(S^1) = pi_3(S^1) = 0, so
# the point defects and textures belong to the regime in which the order parameter ranges over all of Lambda(4).
def _section_f():
    def quat_left(q):                     # x -> q x as a 4x4 real matrix, q = (q0, q1, q2, q3)
        q0, q1, q2, q3 = np.moveaxis(q, -1, 0)
        return np.stack([np.stack([q0, -q1, -q2, -q3], -1), np.stack([q1, q0, -q3, q2], -1),
                         np.stack([q2, q3, q0, -q1], -1), np.stack([q3, -q2, q1, q0], -1)], -2)
    def quat_right(q):                    # x -> x q
        q0, q1, q2, q3 = np.moveaxis(q, -1, 0)
        return np.stack([np.stack([q0, -q1, -q2, -q3], -1), np.stack([q1, q0, q3, -q2], -1),
                         np.stack([q2, -q3, q0, q1], -1), np.stack([q3, q2, -q1, q0], -1)], -2)
    def su2(q):                           # the fundamental representation
        q0, q1, q2, q3 = np.moveaxis(q, -1, 0)
        return np.stack([np.stack([q0 + 1j*q1, q2 + 1j*q3], -1), np.stack([-q2 + 1j*q3, q0 - 1j*q1], -1)], -2)
    def embed4(U):
        out = np.zeros(U.shape[:-2] + (4, 4), complex)
        out[..., :2, :2] = U
        out[..., 2, 2] = out[..., 3, 3] = 1
        return out
    def adjoint(q):                       # x -> q x qbar
        return quat_left(q) @ quat_right(q*np.array([1, -1, -1, -1]))
    def qmul(a, b):
        a0, a1, a2, a3 = a
        b0, b1, b2, b3 = b
        return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                         a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
    rng = np.random.default_rng(0)
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    x = rng.normal(size=4)
    L, R = quat_left(q), quat_right(q)
    check("F anchor: x -> q x and x -> x q are quaternion multiplication by a unit quaternion, orthogonal with det 1",
          np.allclose(L @ x, qmul(q, x)) and np.allclose(R @ x, qmul(x, q)) and np.allclose(L.T @ L, np.eye(4))
          and np.allclose(R.T @ R, np.eye(4)) and abs(np.linalg.det(L) - 1) < 1e-12 and abs(np.linalg.det(R) - 1) < 1e-12)

    def winding(gfun, n=48):
        """W over S^3 = (chi, theta, phi), A_i = g^-1 d_i g: midpoint grid, central differences"""
        chi = (np.arange(n) + 0.5)*np.pi/n
        ph = (np.arange(2*n) + 0.5)*np.pi/n
        C, TH, PH = np.meshgrid(chi, chi, ph, indexing='ij')
        def qof(c, t, f):
            return np.stack([np.cos(c), np.sin(c)*np.cos(t), np.sin(c)*np.sin(t)*np.cos(f),
                             np.sin(c)*np.sin(t)*np.sin(f)], -1)
        h = 1e-5
        tot = 0.0
        Cf, Tf, Pf = C.ravel(), TH.ravel(), PH.ravel()
        for s in range(0, Cf.size, 8192):
            c, t, f = Cf[s:s + 8192], Tf[s:s + 8192], Pf[s:s + 8192]
            gi = np.linalg.inv(gfun(qof(c, t, f)))
            A = [gi @ (gfun(qof(c + h*(i == 0), t + h*(i == 1), f + h*(i == 2)))
                       - gfun(qof(c - h*(i == 0), t - h*(i == 1), f - h*(i == 2))))/(2*h) for i in range(3)]
            tot += (3*np.trace(A[0] @ (A[1] @ A[2] - A[2] @ A[1]), axis1=-2, axis2=-1)).sum()
        return (tot*(np.pi/n)**3/(24*np.pi**2)).real

    W_f = winding(su2)
    check("F anchor: SU(2)'s fundamental representation has |W| = 1 [T]", abs(abs(W_f) - 1) < 1e-3, f"W = {W_f:+.6f}")
    W_e = winding(lambda q: embed4(su2(q)))
    check("F anchor: embedding SU(2) in U(4) leaves W unchanged", abs(W_e - W_f) < 1e-9, f"W = {W_e:+.6f}")
    W_a = winding(lambda q: adjoint(q).astype(complex))
    check("F anchor: SO(3) in SO(4) acting on R^4 (spin 1 plus spin 0) has |W| = 4, its Dynkin index [T]",
          abs(abs(W_a) - 4) < 4e-3, f"W = {W_a:+.6f}")
    W_l = winding(lambda q: quat_left(q).astype(complex))
    W_r = winding(lambda q: quat_right(q).astype(complex))
    pi3_is_Z2 = abs(abs(W_l) - 2) < 2e-3 and abs(W_l + W_r) < 1e-9
    check("F1: the generators x -> q x and x -> x q of pi_3(SO(4)) = Z + Z have W = -2 and +2 in pi_3(U(4)) = Z; the image "
          "is 2Z and pi_2(O(4)) = 0, so pi_3(Lambda(4)) = Z2 (C37)", pi3_is_Z2, f"W = {W_l:+.6f}, {W_r:+.6f}")

    ts = np.linspace(0, 1, 2001)
    def det_winding(Ut, power):
        ang = np.unwrap(np.angle(np.array([np.linalg.det(U)**power for U in Ut])))
        return (ang[-1] - ang[0])/(2*np.pi)
    w_uo = det_winding([np.diag([np.exp(1j*np.pi*t), 1, 1, 1]) for t in ts], 2)
    w_u = det_winding([np.diag([np.exp(2j*np.pi*t), 1, 1, 1]) for t in ts], 2)
    pi1_is_Z = abs(w_uo - 1) < 1e-9 and abs(w_u - 2) < 1e-9
    check("F2: det^2 winds once on the loop t -> diag(e^(i pi t), 1, 1, 1), which closes in Lambda(4) because "
          "diag(-1, 1, 1, 1) is in O(4), and twice on the generator of pi_1(U(4)): pi_1(Lambda(4)) = Z, the Maslov class "
          "(C35)", pi1_is_Z, f"{w_uo:+.6f}, {w_u:+.6f}")
    rot = [np.block([[np.array([[np.cos(2*np.pi*t), -np.sin(2*np.pi*t)], [np.sin(2*np.pi*t), np.cos(2*np.pi*t)]]),
                      np.zeros((2, 2))], [np.zeros((2, 2)), np.eye(2)]]).astype(complex) for t in ts]
    w_so = det_winding(rot, 1)
    pi2_is_Z2 = abs(w_so) < 1e-9
    check("F3: the generator of pi_1(SO(4)) = Z2 has det winding 0 in U(4) (det = 1 on SO(4), so this confirms an input "
          "rather than testing one); pi_1(O(4)) -> pi_1(U(4)) is therefore zero and, with pi_2(U(4)) = 0, pi_2(Lambda(4)) = Z2 "
          "follows by exactness (C36): the polarization manifold admits point defects", pi2_is_Z2, f"{w_so:+.6f}")
    derived = ("Z" if pi1_is_Z else "?", "Z2" if pi2_is_Z2 else "?", "Z2" if pi3_is_Z2 else "?")
    check("F4: pi_1, pi_2, pi_3 of Lambda(4) as derived in F1-F3 match Bott periodicity's stable values for U/O, Z, Z2, Z2 "
          "[T]; free classes of maps S^3 -> Lambda(4) are pi_3 modulo the pi_1 action, trivial on Z2 since Aut(Z2) is "
          "trivial, so [S^3, Lambda(4)] = Z2, two texture classes on a closed universe (C38; argued, not computed)",
          derived == ("Z", "Z2", "Z2"), f"{derived}")

_section_f()

# ======================================================================================================
print(f"\nwall time {time.time() - T_START:.1f} s")
if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — every number of the closed-universe investigation reproduces.")
