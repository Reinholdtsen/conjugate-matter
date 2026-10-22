"""Robustness of the rough Gaussian test in dr2_comparison.py: use the asymmetric wa error
on the side facing the corridor (+0.23 for DESY5; DESI+CMB is symmetric), and report the
1-dof significance too (the corridor is a one-parameter line nested in CPL)."""
import math

def sig(chi2, dof):
    p = math.exp(-chi2 / 2) if dof == 2 else math.erfc(math.sqrt(chi2 / 2))
    lo, hi = 0.0, 40.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if math.erfc(mid / math.sqrt(2)) > p else (lo, mid)
    return (lo + hi) / 2

for name, wa_bf, sa, zp, wp_bf, sp in [("DESI+CMB+DESY5", -0.86, 0.23, 0.31, -0.954, 0.024),
                                       ("DESI+CMB", -1.75, 0.58, 0.53, -1.024, 0.043)]:
    ap = 1 / (1 + zp)
    f = lambda t: ((-1 + t - 1.5 * t * (1 - ap) - wp_bf) / sp) ** 2 + ((-1.5 * t - wa_bf) / sa) ** 2
    c, t = min((f(i * 1e-5), i * 1e-5) for i in range(100001))
    print("%-15s sigma_a=%.3f: best corridor w0=%.3f wa=%.3f chi2=%.2f -> %.1f sigma (2 dof), %.1f sigma (1 dof); LCDM chi2=%.2f"
          % (name, sa, -1 + t, -1.5 * t, c, sig(c, 2), sig(c, 1), f(0.0)))
