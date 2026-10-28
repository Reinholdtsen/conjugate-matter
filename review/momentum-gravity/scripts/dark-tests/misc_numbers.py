"""Small numbers quoted in the report: background potential of the gated force, pivot-gate identity, kernel values."""
import numpy as np
import mpmath as mp
import cosmo as C
import gate_kernels as GK

# (1) uniform-background potential per particle: Phi_bg = -Gt rho_c int d^3r W(Hr/v*)/r = -4 pi Gt rho_c (v*/H)^2 int t W(t) dt
I_g = mp.quad(lambda t: t * mp.exp(-t**2 / 2), [0, mp.inf])
print("Gaussian gate: int_0^inf t W(t) dt = %s  ->  Phi_bg/(m v*^2) = -(3/2) eps Omega_c(a)" % mp.nstr(I_g, 12))
for v in [30, 120, 1000]:
    print("  v* = %5d km/s: (v*/c)^2 = %.3e  (fractional size of the background binding energy per unit eps, times 1.5*Omega_c<=1.3)" % (v, (v / C.C_KMS) ** 2))
# rational gate: log divergence, cut at the Hubble radius r = c/H  (t_max = c/v*)
for v in [120]:
    tmax = C.C_KMS / v
    I_r = mp.quad(lambda t: t / (1 + t**2 / 2), [0, tmax])
    print("Rational gate, cut at c/H: int t W dt = %.3f for v*=%d (still a uniform potential, no force)" % (float(I_r), v))
# (2) pivot-gate identity at z = 3
kp = 0.009 * C.Hz(3.0) / 4.0
sc = 120.0 * 4.0 / C.Hz(3.0)
print("k_p s_c(z=3) = %.4f ; k_v v* = 0.009*120 = %.4f ; R_gauss = %.4f, Rv_gauss = %.4f" % (kp * sc, 0.009 * 120, GK.R(kp * sc), GK.Rv(kp * sc)))
# (3) kernel at the pivot at earlier epochs for v* = 120
for z in [4, 6, 10, 20, 50, 100, 300, 1089.92]:
    s = 120.0 * (1 + z) / C.Hz(z)
    print("  z=%7.2f: k_p s_c = %.4f  R = %.4f  Rv = %.4f" % (z, kp * s, GK.R(kp * s), GK.Rv(kp * s)))
# (4) anti-drag growth-exponent shift in matter domination (single fluid): coefficient of eps in p-1
print("EdS, f_c=1: (p-1)/eps -> 0.6 (density term only), 0.8 (with anti-drag) as eps -> 0 [from p^2+(1/2-eps/2)p-3/2(1+eps)=0]")
for e in [1e-4]:
    for b, lab in [(0.5, "no anti-drag"), (0.5 - e / 2, "anti-drag")]:
        p = (-b + np.sqrt(b * b + 6 * (1 + e))) / 2
        print("   %s: (p-1)/eps = %.5f" % (lab, (p - 1) / e))
