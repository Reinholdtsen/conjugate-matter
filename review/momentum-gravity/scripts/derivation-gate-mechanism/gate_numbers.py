#!/usr/bin/env python3
"""Numbers for the gate-mechanism derivation.  Record inputs (#1 §5.1, #11 §8): m_chi c^2 = 70 MeV,
mu c = 20 keV, v* = sqrt2 mu/m ~ 120 km/s.  Convention (task statement): amplitude gate
exp(-k^2/mu^2), k = m v_rel/2, = exp(-v^2/v_a^2) with v_a = sqrt2 v* = 2 mu/m; cross-section exp(-v^2/v*^2).
Constants: hbar c = 197.3269804 MeV fm, c = 299792.458 km/s, 1 MeV/c^2 = 1.78266192e-27 g (CODATA)."""
import numpy as np

hbarc = 197.3269804          # MeV fm
c_kms = 299792.458
MeV_g = 1.78266192e-27
m, mu = 70.0, 0.020          # MeV
vstar = np.sqrt(2) * mu / m * c_kms
va = np.sqrt(2) * vstar
print("mu/m = %.4e ; v* = sqrt2 mu/m c = %.1f km/s ; v_a = sqrt2 v* = 2 mu/m c = %.1f km/s" % (mu / m, vstar, va))
print("hbar/(mu c) = %.0f fm = %.2f pm  (range of the nonlocality / of the R1 potential)" % (hbarc / mu, hbarc / mu / 1e3))
print("hbar/(M_X c) at M_X = 2 mu = 40 keV: %.2f pm" % (hbarc / (2 * mu) / 1e3))
print("(m/mu)^2 = %.3e  (cancellation needed for a k-scale mu in the degree-2 numerator)" % ((m / mu) ** 2))

print("\n-- t-channel X exchange (minimal coupling) vs the record's gate, forward amplitude --")
print("%10s %12s %16s %18s %18s" % ("v [km/s]", "k/m", "X: N(k)/N(0)-1", "gate exp(-k^2/mu^2)", "sigma gate e^-v2/v*2"))
for v in (50, 120, 171.3, 300, 1500):
    km = v / (2 * c_kms)
    kmu = (m * km) / mu
    print("%10.1f %12.4e %16.4e %18.4e %18.4e" % (v, km, 6 * km**2 + 6 * km**4, np.exp(-kmu**2), np.exp(-v**2 / vstar**2)))
v_O1 = 2 * c_kms / np.sqrt(6)
print("X-exchange k-dependence reaches O(1) (6k^2/m^2 = 1) at v_rel = %.0f km/s = %.3f c ; ratio to v_a: %.0f"
      % (v_O1, v_O1 / c_kms, v_O1 / va))

print("\n-- no polynomial of degree 2 in x = k^2/mu^2 with P(0) = 1 can gate --")
x_cl = (1500 / va) ** 2
a_, b_ = 1.0, x_cl
s0 = (b_ + a_) / (b_ - a_)
T2 = lambda y: 2 * y**2 - 1
bound = 1 / T2(s0)
xs = np.linspace(a_, b_, 200001)
Pstar = T2((2 * xs - (a_ + b_)) / (b_ - a_)) / T2((0 - (a_ + b_)) / (b_ - a_))
print("x range [1, %.1f] (v from v_a to 1500 km/s); Chebyshev minimax bound 1/T_2(%.5f) = %.5f ; "
      "max|P*| on grid = %.5f ; P*(0) = %.3f" % (x_cl, s0, bound, np.abs(Pstar).max(),
                                                 T2((0 - (a_ + b_)) / (b_ - a_)) / T2((0 - (a_ + b_)) / (b_ - a_))))
rng = np.random.default_rng(0)
best = np.inf
xg = np.linspace(a_, b_, 4001)
for _ in range(200000):
    b1, b2 = rng.uniform(-0.2, 0.05), rng.uniform(-0.002, 0.004)
    best = min(best, np.abs(1 + b1 * xg + b2 * xg**2).max())
print("random search over (b1, b2), 2e5 trials: best max|P| = %.5f (never below the bound)" % best)
print("Gaussian amplitude gate over the same range: from %.3e to %.3e" % (np.exp(-1.0), np.exp(-x_cl)))

print("\n-- record's benchmark arithmetic (contact Born, alpha~ = 1, m_phi = m_chi) --")
sig0 = 16 * np.pi * (hbarc / m) ** 2 * 1e-26            # fm^2 -> cm^2
print("sigma0 = 16 pi / m^2 = %.4e cm^2 ; sigma0/m = %.2f cm^2/g ; m for 30 cm^2/g: %.1f MeV"
      % (sig0, sig0 / (m * MeV_g), m * ((sig0 / (m * MeV_g)) / 30) ** (1 / 3)))

print("\n-- resonant route: zero-energy state with 1/a = mu --")
sig_res = 4 * np.pi * (hbarc / mu) ** 2 * 1e-26
print("sigma(k->0) = 4 pi a^2 = %.4e cm^2 ; sigma/m = %.3e cm^2/g ; ratio to 30 cm^2/g: %.2e"
      % (sig_res, sig_res / (m * MeV_g), sig_res / (m * MeV_g) / 30))

print("\n-- preferred-frame vertex: suppression exp(-m^2 V^2/mu^2) = exp(-2 V^2/v*^2) of a pair moving at V --")
for V in (100, 300, 600):
    print("  V = %4d km/s : %.3e" % (V, np.exp(-2 * V**2 / vstar**2)))
