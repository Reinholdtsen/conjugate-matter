# Why every fit lands in the crossing region: if 1 + w(a) is strictly convex on the fit range, the
# least-squares line crosses it at two points a1 < a2 inside the range (residuals have zero mean and
# zero first moment), so the line lies below the curve for a < a1, in particular at a = 0, where the
# true curve is at -1 (frozen field).  Hence w0 + wa (the line at a = 0) < -1.
# Check: sign of d2w/da2 on 0 < z < 2.5 for the thawing cases; and the toy power laws a^p.
import math
import sys
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import cosmo as C
from c3_fits import w_fits, describe

ZMAX = 2.5
amin = 1 / (1 + ZMAX)
print("== toy shapes 1 + w = eps a^p, LSQ uniform in a: s = -wa/(1 + w0) ==")
aa = np.linspace(amin, 1, 4001)
a0 = np.linspace(0, 1, 4001)
for p in [1.0, 1.5, 2.0, 3.0, 4.0]:
    c = C.wls_line(1 - aa, -1 + 0.1 * aa**p, np.ones_like(aa))
    c0 = C.wls_line(1 - a0, -1 + 0.1 * a0**p, np.ones_like(a0))
    print(f"p = {p}: fit on [{amin:.3f}, 1]: s = {describe(*c)[0]:.4f}   fit on [0, 1]: s = {describe(*c0)[0]:.4f}")

print("\n== convexity of the true w(a) on the fit range, and the two crossings of the F1 line ==")
for f, x in [(0.1, 6.0e-4), (0.3, 0.2012), (0.5, 0.6484), (1.0, 1.164), (2.0, 2.090), (5.0, 2.584)]:
    r = C.solve(f, x * f)
    w_on = np.interp(np.log(aa), r["N"], r["w"])
    # second derivative on the smooth RK4 grid (uniform in N), by the chain rule:
    # dw/da = w_N / a,  d2w/da2 = (w_NN - w_N) / a^2
    onew = 2 * r["K"] / r["rho"]              # 1 + w without the cancellation in (K - V)/(K + V)
    wN = np.gradient(onew, r["N"])
    wNN = np.gradient(wN, r["N"])
    d2 = ((wNN - wN) / r["a"]**2)[5:-5]
    ag = r["a"][5:-5]
    c = w_fits(r, ZMAX)["F1 w(a) LSQ, uniform in a"]
    resid = w_on - C.cpl_w(aa, c[0], c[1])
    cross = aa[1:][np.sign(resid[1:]) != np.sign(resid[:-1])]
    a2 = cross[-1]
    conv_low = np.all(d2[(ag > 1e-3) & (ag <= a2)] > 0)
    infl = ag[1:][(np.sign(d2[1:]) != np.sign(d2[:-1])) & (ag[1:] > 1e-3)]
    print(f"f = {f}, tau_i/f = {x}: true w(1) = {r['w'][-1]:+.4f}; F1 line meets w(a) at a = "
          f"{', '.join(f'{v:.3f}' for v in cross)}; w convex on [0.001, a2 = {a2:.3f}]: {bool(conv_low)};"
          f" inflection(s) of w(a) at a = {', '.join(f'{v:.3f}' for v in infl) or 'none below 1'};"
          f" line at a = 0: {c[0] + c[1]:+.4f} (true w there: -1)")
