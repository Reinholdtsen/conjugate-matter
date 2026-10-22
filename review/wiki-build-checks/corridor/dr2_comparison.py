"""The corridor against DESI DR2's own CPL numbers.

Inputs [S] (fetched 2026-10-22 from arXiv:2503.14738v*, HTML, Table 5 and the pivot text;
#11 cites this paper as [21S] but quotes none of these numbers):
  DESI+CMB            w0 = -0.42 +- 0.21,   wa = -1.75 +- 0.58;   z_p = 0.53, w_p = -1.024 +- 0.043
  DESI+CMB+Pantheon+  w0 = -0.838 +- 0.055, wa = -0.62 +0.22/-0.19
  DESI+CMB+Union3     w0 = -0.667 +- 0.088, wa = -1.09 +0.31/-0.27
  DESI+CMB+DESY5      w0 = -0.752 +- 0.057, wa = -0.86 +0.23/-0.20; z_p = 0.31, w_p = -0.954 +- 0.024
Abstract: preference over LambdaCDM 3.1 sigma (DESI+CMB), 2.8-4.2 sigma with SNe.

1. Each fit's slope k = -wa/(1+w0) and CPL crossing redshift z_c, against the corridor's
   k = 1.5, z_c = 2 (corridor_algebra.py).
2. ROUGH: is the corridor line inside DR2's favoured (confidence) region? Gaussian
   approximation in the pivot basis, where w_p and wa are uncorrelated by construction:
   chi2 = ((w_p - w_p^bf)/s_p)^2 + ((wa - wa^bf)/s_a)^2, s_a = mean of the asymmetric errors.
   Checked first against DR2's own LambdaCDM significance. Not a likelihood analysis.
"""
import math

FITS = {
    "DESI+CMB":           dict(w0=-0.42, wa=-1.75, sa=0.58, zp=0.53, wp=-1.024, sp=0.043),
    "DESI+CMB+Pantheon+": dict(w0=-0.838, wa=-0.62, sa=(0.22 + 0.19) / 2),
    "DESI+CMB+Union3":    dict(w0=-0.667, wa=-1.09, sa=(0.31 + 0.27) / 2),
    "DESI+CMB+DESY5":     dict(w0=-0.752, wa=-0.86, sa=(0.23 + 0.20) / 2, zp=0.31, wp=-0.954, sp=0.024),
}
K_CORR = 1.5


def sigma_2dof(chi2):
    """Two-sided Gaussian-equivalent significance of a 2-dof Delta chi^2 (p = exp(-chi2/2))."""
    p = math.exp(-chi2 / 2)
    lo, hi = 0.0, 40.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if math.erfc(mid / math.sqrt(2)) > p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


print("=== 1. Slope and CPL crossing of each DR2 fit ===")
print("%-20s %7s %7s %8s %6s %6s %6s" % ("combination", "w0", "wa", "w0+wa", "k", "a_c", "z_c"))
for name, d in FITS.items():
    w0, wa = d["w0"], d["wa"]
    k = -wa / (1 + w0)
    a_c = 1 + (1 + w0) / wa
    print("%-20s %7.3f %7.3f %8.3f %6.2f %6.3f %6.2f" % (name, w0, wa, w0 + wa, k, a_c, 1 / a_c - 1))
print("corridor             k = 1.50, a_c = 1/3, z_c = 2.00 for every w0")
print("corridor wa at each DR2 w0 (same w0, corridor slope):")
for name, d in FITS.items():
    print("   %-20s w0 = %7.3f -> corridor wa = %7.3f vs DR2 wa = %6.2f (%.1f sigma_a away in wa alone)"
          % (name, d["w0"], -K_CORR * (1 + d["w0"]), d["wa"], (-K_CORR * (1 + d["w0"]) - d["wa"]) / d["sa"]))

print()
print("=== 1b. Pivot consistency (Gaussian check: w_p = w0 + wa(1 - a_p)) ===")
for name, d in FITS.items():
    if "zp" not in d:
        continue
    ap = 1 / (1 + d["zp"])
    print("   %-20s w0 + wa(1-a_p) = %.4f ; DR2 w_p = %.3f" % (name, d["w0"] + d["wa"] * (1 - ap), d["wp"]))

print()
print("=== 2. ROUGH Gaussian test: does the corridor line enter DR2's favoured region? ===")
for name, d in FITS.items():
    if "zp" not in d:
        continue
    ap = 1 / (1 + d["zp"])

    def chi2(w0, wa):
        wp = w0 + wa * (1 - ap)
        return ((wp - d["wp"]) / d["sp"]) ** 2 + ((wa - d["wa"]) / d["sa"]) ** 2

    c_lcdm = chi2(-1.0, 0.0)
    # minimise along the corridor, t = 1 + w0 >= 0 (fine grid; the function is a parabola in t)
    best = min(((chi2(-1 + t, -K_CORR * t), t) for t in [i * 1e-5 for i in range(0, 100001)]))
    c_corr, t_best = best
    print("%-20s z_p = %.2f" % (name, d["zp"]))
    print("   LambdaCDM (-1, 0):        chi2 = %6.2f  -> %.1f sigma (2 dof); DR2 quotes %s"
          % (c_lcdm, sigma_2dof(c_lcdm), "3.1 sigma" if name == "DESI+CMB" else "4.2 sigma"))
    print("   best corridor point:      w0 = %.3f, wa = %.3f, chi2 = %6.2f -> %.1f sigma (2 dof) from the CPL best fit"
          % (-1 + t_best, -K_CORR * t_best, c_corr, sigma_2dof(c_corr)))
    print("   corridor gain over LCDM:  Delta chi2 = %.2f" % (c_lcdm - c_corr))
    print("   inside 2D 68%% (2.30)? %s ; inside 2D 95%% (6.18)? %s ; inside 2D 99.7%% (11.8)? %s"
          % (c_corr < 2.30, c_corr < 6.18, c_corr < 11.83))
