# Anchors for the corridor numerics: each checks the code against something independent of the
# documents (a textbook identity, an exact solution, or a separately coded integration).
import math
import sys
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import cosmo as C

ok_all = True


def check(name, cond, detail):
    global ok_all
    ok_all &= bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}: {detail}")


# ---- A1: Lambda-CDM limit (tau_i = 0 sits on the maximum forever: w = -1 exactly) ----
OL = 1 - C.OM - C.OR
r = C.solve(1.0, 0.0)
check("A1a V0 shoot at tau_i = 0", abs(r["V0"] - 1.5 * OL) < 1e-11,
      f"V0 = {r['V0']:.15f}, expected 3 Omega_L / 2 = {1.5 * OL:.15f}")
Hl = np.sqrt(C.OM * r["a"]**-3 + C.OR * r["a"]**-4 + OL)
check("A1b H(z) vs analytic LCDM, 0 < z < 1e4", np.max(np.abs(r["H"] / Hl - 1)) < 1e-12,
      f"max |H/H_LCDM - 1| = {np.max(np.abs(r['H'] / Hl - 1)):.2e}")
chi = C.comoving_distance(r["N"], r["H"])
xg, wg = np.polynomial.legendre.leggauss(200)
for zz in [0.5, 1.0, 2.5, C.ZSTAR]:
    # independent quadrature: Gauss-Legendre in ln(1+z) of (1+z)/H(z)
    u = 0.5 * math.log1p(zz) * (xg + 1)
    zq = np.expm1(u)
    Hq = np.sqrt(C.OM * (1 + zq)**3 + C.OR * (1 + zq)**4 + OL)
    ref = 0.5 * math.log1p(zz) * np.sum(wg * (1 + zq) / Hq)
    num = np.interp(-math.log1p(zz), r["N"], chi)
    check(f"A1c D_M(z = {zz:g})", abs(num / ref - 1) < 1e-6, f"trapezoid {num:.10f} vs Gauss {ref:.10f}"
          f" (rel {num / ref - 1:.1e})")

# ---- A2: CPL closed-form density vs numerical continuity equation (textbook identity) ----
w0t, wat = -0.8, -0.5
errs = []
for npts in [10001, 20001, 40001]:
    Ng = np.linspace(math.log(1e-3), 0, npts)
    ag = np.exp(Ng)
    dlnrho = -3 * (1 + C.cpl_w(ag, w0t, wat))       # d ln rho / dN
    lnrho = -C.cumtrap_from_end(Ng, dlnrho)          # ln rho(N) - ln rho(0)
    errs.append(np.max(np.abs(np.exp(lnrho) / C.cpl_X(ag, w0t, wat) - 1)))
# trapezoid is second order: the error must fall ~4x per halving and be small
check("A2 CPL rho closed form (trapezoid convergence)",
      errs[-1] < 1e-7 and 3.5 < errs[0] / errs[1] < 4.5 and 3.5 < errs[1] / errs[2] < 4.5,
      "max rel diff at 10001/20001/40001 points = " + ", ".join(f"{e:.2e}" for e in errs) +
      f"; ratios {errs[0] / errs[1]:.2f}, {errs[1] / errs[2]:.2f}")

# ---- A3: the fits recover an exact CPL input ----
ZMAX = 2.5
aa = np.linspace(1 / (1 + ZMAX), 1, 4001)
c = C.wls_line(1 - aa, C.cpl_w(aa, w0t, wat), np.ones_like(aa))
check("A3a w(a) line fit on exact CPL", abs(c[0] - w0t) < 1e-12 and abs(c[1] - wat) < 1e-12,
      f"(w0, wa) = ({c[0]:.14f}, {c[1]:.14f})")

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from c3_fits import distance_fits      # same fitting code as the main run
fake = dict(N=r["N"], a=r["a"], om=C.OM, orr=C.OR)
fake["H"] = np.sqrt(C.OM * r["a"]**-3 + C.OR * r["a"]**-4 + OL * C.cpl_X(r["a"], w0t, wat))
fake["w"] = C.cpl_w(r["a"], w0t, wat)
res = distance_fits(fake, ZMAX)
for k, v in res.items():
    check(f"A3b distance fit {k} on exact CPL", abs(v[0] - w0t) < 1e-6 and abs(v[1] - wat) < 1e-6,
          f"(w0, wa) = ({v[0]:.9f}, {v[1]:.9f})" + (f", extra = {v[2]:.9f}" if len(v) > 2 else ""))

# ---- A4: step-size convergence on a thawing case ----
from c3_fits import w_fits as _wf
for f, ti in [(0.3, 0.3 * 0.03), (1.0, 1.0 * 0.5), (2.0, 2.0 * 1.5)]:
    rA = C.solve(f, ti, dN=2e-3)
    rB = C.solve(f, ti, dN=1e-3)
    pA = _wf(rA, 2.5)["F1 w(a) LSQ, uniform in a"]
    pB = _wf(rB, 2.5)["F1 w(a) LSQ, uniform in a"]
    check(f"A4 step convergence (f = {f}, tau_i/f = {ti / f:g})",
          abs(rA["w"][-1] - rB["w"][-1]) < 1e-7 and abs(rA["V0"] - rB["V0"]) < 1e-8 and np.max(np.abs(pA - pB)) < 1e-6,
          f"w(1): {rA['w'][-1]:.10f} vs {rB['w'][-1]:.10f}; V0: {rA['V0']:.10f} vs {rB['V0']:.10f};"
          f" F1 (w0, wa) diff {np.max(np.abs(pA - pB)):.1e}")

# ---- A5: linear hilltop regime: nonlinear code vs an independent linear integration in cosmic time,
#          and vs the Dutta-Scherrer closed form (dagger: model memory, Phys. Rev. D 78, 123525 (2008)) ----
om5, orr5 = 0.30, 0.0
OL5 = 1 - om5
for f in [0.5, 1.0, 2.0]:
    # small displacement so 1 + w0 ~ 1e-3: the linear regime
    ti = {0.5: 2e-3, 1.0: 2e-2, 2.0: 0.1}[f]
    rn = C.solve(f, ti, om=om5, orr=orr5)
    one_w0 = 1 + rn["w"][-1]
    # (i) linear ODE u'' + 3 H u' - m^2 u = 0 in exact LCDM, cosmic time, m^2 = V0/f^2, V0 = 3 OL/2
    V0 = 1.5 * OL5
    m2 = V0 / f**2
    HL = math.sqrt(OL5)
    t0 = math.asinh(math.sqrt(OL5 / om5)) / (1.5 * HL)
    a_of_t = lambda t: (om5 / OL5) ** (1 / 3) * math.sinh(1.5 * HL * t) ** (2 / 3)
    H_of_t = lambda t: HL / math.tanh(1.5 * HL * t)
    s1, s2, ns = math.log(1e-7 * t0), math.log(t0), 60000
    hs = (s2 - s1) / ns
    t = math.exp(s1)
    u, ud = 1 + m2 * t * t / 6, m2 * t / 3            # regular matter-era solution sinh(mt)/(mt)

    def dd(s, u, ud):
        t = math.exp(s)
        return t * ud, t * (-3 * H_of_t(t) * ud + m2 * u)
    S, A, UD = [], [], []
    s = s1
    for i in range(ns):
        k1 = dd(s, u, ud); k2 = dd(s + hs / 2, u + hs / 2 * k1[0], ud + hs / 2 * k1[1])
        k3 = dd(s + hs / 2, u + hs / 2 * k2[0], ud + hs / 2 * k2[1]); k4 = dd(s + hs, u + hs * k3[0], ud + hs * k3[1])
        u += hs / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); ud += hs / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        s = s1 + (i + 1) * hs
        A.append(a_of_t(math.exp(s))); UD.append(ud)
    A, UD = np.array(A), np.array(UD)
    shape_lin = lambda aq: np.interp(aq, A, UD**2) / UD[-1]**2
    # (ii) Dutta-Scherrer (dagger)
    K = math.sqrt(1 + 2 / (3 * f**2))                 # sqrt(1 - (4/3) V''/V) at the maximum
    F = lambda aq: np.sqrt(1 + (1 / OL5 - 1) * aq**-3)
    B = lambda Fv: (K - Fv) * (Fv + 1)**K + (K + Fv) * (Fv - 1)**K
    shape_ds = lambda aq: aq**(3 * (K - 1)) * (B(F(aq)) / B(F(1.0)))**2
    shape_nl = lambda aq: np.interp(aq, rn["a"], 1 + rn["w"]) / one_w0
    aq = np.array([0.2, 0.35, 0.5, 0.7, 0.85])
    sl, sd, sn = shape_lin(aq), shape_ds(aq), shape_nl(aq)
    check(f"A5i  f = {f}: linear(cosmic time) vs Dutta-Scherrer shape", np.max(np.abs(sl / sd - 1)) < 1e-4,
          "(1+w)/(1+w0) at a = " + ", ".join(f"{x:g}" for x in aq) + ": lin " +
          " ".join(f"{x:.5f}" for x in sl) + " | DS " + " ".join(f"{x:.5f}" for x in sd))
    check(f"A5ii f = {f}: nonlinear code vs linear, 1 + w0 = {one_w0:.2e}", np.max(np.abs(sn / sl - 1)) < 20 * one_w0 + 1e-3,
          "nonlinear " + " ".join(f"{x:.5f}" for x in sn) + f" (max rel diff {np.max(np.abs(sn / sl - 1)):.1e})")

print("\nALL ANCHORS PASS" if ok_all else "\nSOME ANCHOR FAILED")
