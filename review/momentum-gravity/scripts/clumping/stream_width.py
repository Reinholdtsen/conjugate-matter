"""Velocity width of the pure gated (stream) eigenmode, Gaussian gate, exact (Mehler):
top eigenfunction of p0^1/2 W p0^1/2 is exp(-gam v^2), gam = sqrt(1+4r^2)/4 (sigma=1); delta f ∝ p0^1/2 * eigenfunction
∝ exp(-(1/4+gam) v^2): per-component dispersion s = [2(1/4+gam)]^-1/2, 3D rms = sqrt(3) s.  Compare sqrt(v*/sigma) = r^-1/2."""
import math
for r in [0.25, 1.2917, 4.0, 8.3333, 16.0, 64.0]:
    gam = math.sqrt(1 + 4*r*r)/4
    s = (2*(0.25 + gam))**-0.5
    print(f"r={r:8.4f}: per-component width s={s:.4f} sigma, 3D rms={math.sqrt(3)*s:.4f} sigma, sqrt(v*/sigma)={r**-0.5:.4f}, s/sqrt(v*/sigma)={s*r**0.5:.4f}")
