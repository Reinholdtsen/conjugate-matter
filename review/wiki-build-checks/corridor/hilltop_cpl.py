"""Where does a never-phantom hilltop field land in the CPL plane?

Steelman test for the corridor observation: integrate the program's own potential
V = V0 [1 + cos(tau/f)] (#11 sec. 10) as a canonical scalar in flat FRW with matter and
radiation, starting frozen near the hilltop. Its exact w(a) obeys 1 + w = tau_dot^2/rho >= 0
at every a (rho > 0 because V >= 0). Then summarize w(a) by CPL three ways:

  T  Taylor at a = 1:   w0 = w(1), wa = -dw/da(1)   (the expansion the wiki CPL page uses)
  L  least squares in a over 0 <= z <= 2.33  (a in [1/3.33, 1]), uniform in a
  D  distance-calibrated: fit (w0, wa) so CPL reproduces the field's D_M(z) and D_H(z) at
     seven BAO-like redshifts (1% each) and D_M(1090) (0.1%), Omega_m and H0 held at truth.

and report k = -wa/(1 + w0), w0 + wa, and the CPL crossing redshift z_c = 1/(k - 1),
against the exact field's minimum of 1 + w.

Units: reduced Planck mass 1, H0 = 1 (V0 found by shooting so that H(a=1) = 1).
The BAO-like redshifts are DESI's tracer redshifts from model memory (dagger); the
argument does not depend on their exact values.
No scipy in the repo venv: RK4 (vectorized over cases) and Gauss-Newton are written out.
Usage: hilltop_cpl.py [nsteps]   (default 6000; rerun with 24000 to check convergence)
"""
import sys
import numpy as np

OM, OR = 0.31, 9.0e-5
OPHI = 1.0 - OM - OR
RHO_M0, RHO_R0 = 3.0 * OM, 3.0 * OR
N_I = np.log(1e-5)
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
NGRID = np.concatenate([np.linspace(N_I, 0.0, NS + 1), np.linspace(0.0, 0.02, 11)[1:]])
I0 = NS                                             # index of N = 0 (a = 1)

CASES = [(f, th) for f in [0.15, 0.2, 0.3, 0.5, 0.7, 1.0, 2.0]
         for th in [0.01, 0.03, 0.05, 0.15, 0.3, 0.6, 1.0]]
F = np.array([c[0] for c in CASES])
TH = np.array([c[1] for c in CASES])


def rhs(N, phi, u, V0):
    V = V0 * (1.0 + np.cos(phi / F))
    dV = -(V0 / F) * np.sin(phi / F)
    rm, rr = RHO_M0 * np.exp(-3 * N), RHO_R0 * np.exp(-4 * N)
    H2 = (rm + rr + V) / (3.0 - 0.5 * u * u)
    epsH = (rm + 4.0 * rr / 3.0 + H2 * u * u) / (2.0 * H2)
    return u, -(3.0 - epsH) * u - dV / H2


def integrate(V0, keep=False):
    phi, u = TH * F, np.zeros_like(F)
    hist = [(phi, u)] if keep else None
    for i in range(NGRID.size - 1):
        N, h = NGRID[i], NGRID[i + 1] - NGRID[i]
        a1, b1 = rhs(N, phi, u, V0)
        a2, b2 = rhs(N + h / 2, phi + h / 2 * a1, u + h / 2 * b1, V0)
        a3, b3 = rhs(N + h / 2, phi + h / 2 * a2, u + h / 2 * b2, V0)
        a4, b4 = rhs(N + h, phi + h * a3, u + h * b3, V0)
        phi = phi + h / 6 * (a1 + 2 * a2 + 2 * a3 + a4)
        u = u + h / 6 * (b1 + 2 * b2 + 2 * b3 + b4)
        if keep:
            hist.append((phi, u))
        elif i + 1 == I0:
            break
    if not keep:
        return phi, u
    P = np.array([p for p, _ in hist])              # shape (nN, ncases)
    U = np.array([q for _, q in hist])
    V = V0 * (1.0 + np.cos(P / F))
    rm = (RHO_M0 * np.exp(-3 * NGRID))[:, None]
    rr = (RHO_R0 * np.exp(-4 * NGRID))[:, None]
    H2 = (rm + rr + V) / (3.0 - 0.5 * U * U)
    rho_phi = 0.5 * H2 * U * U + V
    return H2, rho_phi, H2 * U * U / rho_phi


def rho_phi_today(V0):
    phi, u = integrate(V0)
    V = V0 * (1.0 + np.cos(phi / F))
    H2 = (RHO_M0 + RHO_R0 + V) / (3.0 - 0.5 * u * u)
    return 0.5 * H2 * u * u + V


# rho_phi is non-increasing in a (w >= -1), so V0 (1 + cos th_i) >= 3 Omega_phi: lower bracket
lo = 3.0 * OPHI / (1.0 + np.cos(TH))
hi = 4.0 * lo
for _ in range(60):
    mid = 0.5 * (lo + hi)
    high = rho_phi_today(mid) > 3.0 * OPHI
    hi = np.where(high, mid, hi)
    lo = np.where(high, lo, mid)
V0 = 0.5 * (lo + hi)
H2, RHO, OPW = integrate(V0, keep=True)
OK = np.abs(H2[I0] - 1) < 1e-8
print("nsteps =", NS, "; shooting converged (|H(a=1)^2 - 1| < 1e-8) for", int(OK.sum()), "of", F.size, "cases")

# ---------- distances ----------
# Both models are put through the same pipeline on the same nodes x = ln(1+z) = -N, so the
# discretization error is common to both and cancels in their ratio.
ZBAO = np.array([0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330])   # dagger: DESI tracer z_eff
ZSTAR = 1090.0
XN = -NGRID[:I0 + 1][::-1]                                           # 0 .. 11.5, uniform


def observables(Ex):
    integrand = np.exp(XN) / Ex
    DM = np.concatenate([[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(XN))])
    xb = np.log1p(ZBAO)
    return np.concatenate([np.interp(xb, XN, DM), 1.0 / np.interp(xb, XN, Ex),
                           [np.interp(np.log1p(ZSTAR), XN, DM)]])


def E_cpl(w0, wa):
    a = np.exp(-XN)
    de = OPHI * a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
    return np.sqrt(OM * a ** -3 + OR * a ** -4 + de)


SIG = np.concatenate([np.full(7, 0.01), np.full(7, 0.01), [0.001]])


def fit_distances(target, start):
    """Levenberg-Marquardt on the 15 relative residuals."""
    resid = lambda q: (observables(E_cpl(*q)) / target - 1) / SIG
    p = np.array(start, dtype=float)
    r = resid(p)
    lam = 1e-3
    for _ in range(200):
        J = np.empty((r.size, 2))
        for j in range(2):
            dp = np.zeros(2)
            dp[j] = 1e-7
            J[:, j] = (resid(p + dp) - r) / 1e-7
        A = J.T @ J
        step = np.linalg.solve(A + lam * np.diag(np.diag(A)), -J.T @ r)
        rn = resid(p + step)
        if np.all(np.isfinite(rn)) and rn @ rn < r @ r:
            p, r, lam = p + step, rn, lam / 3
            if np.max(np.abs(step)) < 1e-12:
                break
        else:
            lam *= 10
    chi2 = float(np.sum(((observables(E_cpl(*p)) / target - 1) / SIG) ** 2))
    return p, chi2


def summarize(w0, wa):
    k = -wa / (1 + w0)
    zc = 1.0 / (k - 1.0) if k > 1 else float('inf')
    return k, w0 + wa, zc


print("Exact field: 1 + w = H^2 u^2 / rho_phi >= 0 at every a (canonical, rho_phi > 0).")
print("Per method: w0, wa, k = -wa/(1+w0), w0+wa, z_c (where the CPL line crosses -1).")
print()
print("  f    th_i |  w(1)    min(1+w)   w(z=0.4)  w(z=2)   w(z=1090)  || "
      "T: w0     wa      k    w0+wa    z_c || L: w0     wa      k    w0+wa    z_c || "
      "D: w0     wa      k    w0+wa    z_c   chi2")
a = np.exp(NGRID)
rows = []
for c in range(F.size):
    w = OPW[:, c] - 1.0
    if not OK[c]:
        print("%5.2f %5.2f | shooting did not reach H(a=1) = 1 (field rolls off): skipped" % (F[c], TH[c]))
        continue
    if not (-1.0 < w[I0] < -0.3):
        print("%5.2f %5.2f | w(1) = %.3f outside (-1, -0.3): skipped" % (F[c], TH[c], w[I0]))
        continue
    dwdN = (w[I0 + 1] - w[I0 - 1]) / (NGRID[I0 + 1] - NGRID[I0 - 1])
    T = (w[I0], -dwdN)
    au = np.linspace(1 / 3.33, 1.0, 2001)
    wu = np.interp(au, a[:I0 + 1], w[:I0 + 1])
    L, *_ = np.linalg.lstsq(np.vstack([np.ones(au.size), 1 - au]).T, wu, rcond=None)
    Ex_true = np.sqrt(H2[:I0 + 1, c][::-1])
    D, chi2 = fit_distances(observables(Ex_true), tuple(L))
    wz = lambda zz: np.interp(-np.log1p(zz), NGRID, w)
    out = [F[c], TH[c], w[I0], OPW[:I0 + 1, c].min(), wz(0.4), wz(2.0), wz(1090.0)]
    for (w0, wa) in [T, tuple(L), tuple(D)]:
        out += [w0, wa, *summarize(w0, wa)]
    out.append(chi2)
    rows.append(out)
    print(("%5.2f %5.2f | %7.4f  %9.2e  %8.4f  %8.4f  %10.7f || "
           "%7.4f %7.4f %5.2f %7.4f %5.2f || %7.4f %7.4f %5.2f %7.4f %5.2f || "
           "%7.4f %7.4f %5.2f %7.4f %5.2f %7.4f") % tuple(out))

rows = np.array(rows)
print()
print("cases kept:", len(rows))
print("min over cases of the exact min(1+w): %.3e (>= 0: never phantom)" % rows[:, 3].min())
print("max over cases of |w(z=1090) + 1|: %.2e (the field is frozen at early times)" % np.max(np.abs(rows[:, 6] + 1)))
for name, j in [("T (Taylor at a=1)", 7), ("L (LSQ in a, z<=2.33)", 12), ("D (distances)", 17)]:
    kk = rows[:, j + 2]
    s = rows[:, j + 3] + 1
    inq = bool(np.all((rows[:, j] > -1) & (s < 0)))
    print("%-22s k in [%.3f, %.3f]; w0+wa+1 in [%+.4f, %+.4f]; all in crossing quadrant: %s; z_c in [%.2f, %.2f]"
          % (name, kk.min(), kk.max(), s.min(), s.max(), inq, rows[:, j + 4].min(), rows[:, j + 4].max()))
res = rows[rows[:, 2] > -0.999]
print("resolved cases (1 + w(1) > 1e-3): %d" % len(res))
for name, j in [("T (Taylor at a=1)", 7), ("L (LSQ in a, z<=2.33)", 12), ("D (distances)", 17)]:
    kk = res[:, j + 2]
    s = res[:, j + 3] + 1
    inq = bool(np.all((res[:, j] > -1) & (s < 0)))
    print("  %-22s k in [%.3f, %.3f]; all in crossing quadrant: %s; z_c in [%.2f, %.2f]"
          % (name, kk.min(), kk.max(), inq, res[:, j + 4].min(), res[:, j + 4].max()))
near = res[res[:, 2] < -0.9]
print("resolved and near Lambda (-0.999 > w(1) > ... , w(1) < -0.9): %d cases; D k in [%.3f, %.3f]; L k in [%.3f, %.3f]"
      % (len(near), near[:, 19].min(), near[:, 19].max(), near[:, 14].min(), near[:, 14].max()))
print("For comparison: corridor k = 1.5 (z_c = 2); a CPL crossing at z = 0.4 needs k = 3.5.")

# ---------- independent anchor: matter-era thawing from rest gives 1 + w ~ a^3 ----------
# (phi_dot = -V' t/3 with H = 2/(3t), so kinetic energy ~ t^2 ~ a^3; corridor_algebra.py sec. 5)
print()
print("anchor: d ln(1+w)/d ln a in the matter era (expect -> 3 while H >> |m|):")
for c in range(F.size):
    if not OK[c] or (F[c], TH[c]) not in [(1.0, 0.3), (0.5, 0.3), (0.3, 0.05), (2.0, 1.0)]:
        continue
    lw = np.log(OPW[:, c])
    vals = []
    for aa in [1e-3, 1e-2, 0.05, 0.1, 0.3, 1.0]:
        i = int(np.argmin(np.abs(NGRID - np.log(aa))))
        vals.append((lw[i + 1] - lw[i - 1]) / (NGRID[i + 1] - NGRID[i - 1]))
    print("  f = %.1f th_i = %.2f: a = 1e-3, 1e-2, 0.05, 0.1, 0.3, 1 ->" % (F[c], TH[c]),
          " ".join("%.3f" % v for v in vals))
