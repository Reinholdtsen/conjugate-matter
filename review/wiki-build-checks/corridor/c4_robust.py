# Robustness of c3: steeper and flatter hills, other Omega_m, a finer tau_i scan.
# Same integrator and fits (cosmo.py, c3_fits.py). Prints one line per thawing case and a summary.
import math
import sys
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import cosmo as C
from c3_fits import w_fits, distance_fits, tangent, describe

ZMAX = 2.5
configs = [(0.1, 0.30), (0.2, 0.30), (0.3, 0.30), (0.5, 0.30), (1.0, 0.30), (2.0, 0.30), (5.0, 0.30),
           (0.5, 0.25), (0.5, 0.35), (1.0, 0.25), (1.0, 0.35)]
xs = np.geomspace(1e-4, 3.0, 70)       # tau_i / f
keys = None
allrows = []
print("one line per case: f, Omega_m, tau_i/f, true w(1); s = -wa/(1+w0) for T (tangent), F1, F2, F3, F4, F5;"
      " part-3 diagnostics: min(1+w), min(1+w_eff) with w_eff = -1 - (1/3) dln(rho_tau)/dN,"
      " max relative step growth of rho_tau\n")
for f, om in configs:
    for x in xs:
        try:
            r = C.solve(f, x * f, om=om)
        except RuntimeError:
            continue
        w0t = r["w"][-1]
        if not (-0.985 <= w0t <= -0.5):
            continue
        fits = {"T": tangent(r)}
        fits.update(w_fits(r, ZMAX))
        fits.update(distance_fits(r, ZMAX))
        if keys is None:
            keys = list(fits.keys())
        dl = np.gradient(np.log(r["rho"]), r["N"])
        row = dict(f=f, om=om, x=x, w0t=w0t, fits=fits,
                   one_w_min=np.min(1 + r["w"]),
                   one_weff_min=np.min(-dl / 3),
                   rel_growth=np.max(np.diff(r["rho"]) / r["rho"][:-1]))
        allrows.append(row)
        ss = [describe(fits[k][0], fits[k][1])[0] for k in keys]
        gg = [describe(fits[k][0], fits[k][1])[1] for k in keys]
        print(f"f={f:<4} Om={om:.2f} tau_i/f={x:.3e} w(1)={w0t:+.4f} | s: " +
              " ".join(f"{v:5.2f}" for v in ss) + " | max(w0+wa+1) = " + f"{max(gg):+.4f}" +
              f" | 1+w>={row['one_w_min']:.1e} 1+w_eff>={row['one_weff_min']:+.1e} drho/rho<={row['rel_growth']:.1e}")

print(f"\n== Summary over {len(allrows)} thawing cases (true w(1) in [-0.985, -0.5]), 0 < z < {ZMAX} ==")
for k in keys:
    ss = np.array([describe(R["fits"][k][0], R["fits"][k][1])[0] for R in allrows])
    gg = np.array([describe(R["fits"][k][0], R["fits"][k][1])[1] for R in allrows])
    w0f = np.array([R["fits"][k][0] for R in allrows])
    zc = np.array([describe(R["fits"][k][0], R["fits"][k][1])[2] for R in allrows])
    print(f"{k:<44s} w0>-1: {np.sum(w0f > -1)}/{len(allrows)}  w0+wa<-1: {np.sum(gg < 0)}/{len(allrows)}"
          f"  s in [{ss.min():.3f}, {ss.max():.3f}] median {np.median(ss):.3f}"
          f"  z_c in [{zc.min():.2f}, {zc.max():.2f}]")
print("part 3 over all cases: min(1+w) = %.2e; min(1 + w_eff) = %+.2e; max relative step growth of rho_tau = %.2e"
      % (min(R["one_w_min"] for R in allrows), min(R["one_weff_min"] for R in allrows),
         max(R["rel_growth"] for R in allrows)))
print("by f (F1 / F3 / F5 median s):")
for f in sorted(set(R["f"] for R in allrows)):
    sub = [R for R in allrows if R["f"] == f and R["om"] == 0.30]
    if not sub:
        continue
    med = lambda k: np.median([describe(R["fits"][k][0], R["fits"][k][1])[0] for R in sub])
    print(f"  f = {f:<4}: n = {len(sub):2d}, w(1) from {min(R['w0t'] for R in sub):+.3f} to {max(R['w0t'] for R in sub):+.3f};"
          f" median s: F1 {med(keys[1]):.3f}, F3 {med(keys[3]):.3f}, F5 {med(keys[5]):.3f};"
          f" K = sqrt(1 + 2/(3 f^2)) = {math.sqrt(1 + 2 / (3 * f * f)):.3f}")
