"""verify-critic-numbers: where the velocity-selection crossover 1/Lambda_g(r) equals 4/3 (eps of a
gravitational-strength massive spin-2) and 1 + 1/3; monotonicity of Lambda_g in r."""
import numpy as np
lam = lambda r: (0.5 + r**2 + np.sqrt(1 + 4 * r**2) / 2) ** -1.5
rr = np.linspace(1e-4, 20, 200001)
print("Lambda_g strictly decreasing on (0, 20]:", bool(np.all(np.diff(lam(rr)) < 0)))
lo, hi = 0.01, 1.0
for _ in range(100):
    mid = 0.5 * (lo + hi)
    if 1 / lam(mid) < 4 / 3:
        lo = mid
    else:
        hi = mid
print(f"1/Lambda_g = 4/3 at r = sigma/v* = {mid:.5f}; so eps = 4/3 exceeds the crossover only for sigma < {mid:.4f} v*")
for name, sig in (("UFD", 4.0), ("classical dSph", 10.0), ("dwarf core", 30.0)):
    print(f"  v* = 120: {name:14s} r = {sig/120:.4f}, crossover = {1/lam(sig/120):.4f}")
