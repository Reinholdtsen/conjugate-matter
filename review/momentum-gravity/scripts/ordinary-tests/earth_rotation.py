"""Earth-rotation speeds relevant to body-level vs element-level gating (omega_E, R_E: standard values, from memory)."""
import numpy as np
omega_E = 7.2921150e-5   # rad/s (sidereal), dagger
R_E = 6378.137           # km equatorial, dagger
v_eq = omega_E * R_E
print(f"equatorial surface speed omega_E R_E = {v_eq:.4f} km/s; max relative speed between two Earth elements = {2*v_eq:.3f} km/s")
for lat in [35.7, 48.8]:
    print(f"  lab at latitude {lat}: speed relative to Earth's CM = {v_eq*np.cos(np.radians(lat)):.3f} km/s")
v_moon = 1.0251
print(f"Moon vs surface elements: {v_moon - v_eq:.3f} - {v_moon + v_eq:.3f} km/s (extreme, coplanar)")
print(f"v*/omega_E for v* = 0.1 km/s: {0.1/omega_E:.0f} km (cylinder radius within which rigid-rotation relative speeds < v*)")
