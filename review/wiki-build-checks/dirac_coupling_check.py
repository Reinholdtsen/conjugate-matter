"""Check #11 §11.2: 'Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34'.
Heaviside–Lorentz natural units, alpha = e^2/(4 pi)."""
from math import pi, sqrt
alpha = 1/137.035999
e = sqrt(4*pi*alpha)
for n_conv, label in [(2*pi, "eg = 2π (Dirac minimum)"), (4*pi, "eg = 4π")]:
    g = n_conv/e
    print(f"{label}: g = {g:.4f}, alpha_m = g^2/4π = {g**2/(4*pi):.3f}")
print(f"4π/e² = {4*pi/e**2:.3f}   (= 1/alpha)")
print(f"π/e²  = {pi/e**2:.3f}   (= 1/(4 alpha))")
