"""Where the Hubble flow closes the gate: r_gate(z) = v*/H(z) (proper), (1+z) v*/H(z) (comoving),
from recombination to today, compared with linear peculiar velocities and the nonlinear scale.
Background: Planck 2018 (cosmo.py). Linear power: EH98 no-wiggle, sigma8-normalized (cosmo.py)."""
import numpy as np
import cosmo as C

vstar = 120.0  # km/s, benchmark (calc note #2)
zs = [0.0, 0.3, 0.6, 1.0, 2.0, 3.0, 4.0, 6.0, 10.0, 20.0, 50.0, 100.0, 300.0, 1089.92, 3402.0]

print("Gate radius for v* = %.0f km/s (scales linearly with v*)" % vstar)
print("   z        H(z)[km/s/Mpc]   r_gate proper [kpc]   r_gate comoving [Mpc]   k_gate=1/s_c [1/Mpc]")
for z in zs:
    H = C.Hz(z)
    rp = vstar / H * 1e3
    rc = (1 + z) * vstar / H
    print("  %8.2f   %12.2f      %12.3f          %10.4f            %8.3f" % (z, H, rp, rc, 1 / rc))

# maximum of comoving gate radius = minimum of aH
zz = np.linspace(0.0, 3.0, 30001)
aH = C.Hz(zz) / (1 + zz)
i = np.argmin(aH)
print("Comoving gate radius peaks at z = %.3f (minimum of aH = %.2f km/s/Mpc): s_c,max = %.4f Mpc for v*=120"
      % (zz[i], aH[i], vstar / aH[i]))
print("  ratio s_c(z=0)/s_c,max = %.4f" % ((vstar / C.H0) / (vstar / aH[i])))
# deceleration-acceleration transition for comparison: q=0 <=> Om(1+z)^3 = 2 OL (no radiation)
print("  check: deceleration->acceleration at z_t = (2 OL/Om)^(1/3) - 1 = %.3f" % ((2 * C.OL / C.Om) ** (1 / 3) - 1))

# Velocity-space form: H r_proper = v*  <=>  k_v = 1/v* in s/km, at every z
print("In velocity units (as the Lyman-alpha forest measures): gate width = v* exactly; 1/v* = %.5f s/km for v*=120" % (1 / vstar))

# Linear pairwise velocity dispersion of the matter field
k = np.logspace(-4, 2.5, 4000)


def pairwise_s1(r_c, z):
    a = 1 / (1 + z)
    f = C.growth_rate_f(a)
    aH = C.Hz(z) * a
    P = C.P_lin(k, z)
    x = k * r_c
    j0 = np.where(x < 1e-4, 1 - x**2 / 6, np.sin(x) / np.maximum(x, 1e-300))
    du2 = (aH * f) ** 2 / np.pi**2 * np.trapezoid(P * (1 - j0) * k, np.log(k))   # <|du|^2>, 3D
    return np.sqrt(du2 / 3.0), f


def kNL(z):
    D2 = k**3 * C.P_lin(k, z) / (2 * np.pi**2)
    j = np.argmax(D2 >= 1.0)
    return k[j] if D2[j] >= 1.0 else np.nan


print()
print("Linear peculiar velocities vs the gate (v* = 120 km/s): s1 = 1D rms of the pair velocity difference")
print("   z     f(z)    s_c[Mpc]   s1(s_c/2)  s1(s_c)  s1(2 s_c) [km/s]   k_NL[1/Mpc]  1/k_NL[Mpc]  Hubble dv across 1/k_NL [km/s]")
for z in [0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 10.0, 30.0, 100.0, 1089.92]:
    a = 1 / (1 + z)
    sc = vstar / (C.Hz(z) * a)
    s_half, f = pairwise_s1(sc / 2, z)
    s_one, _ = pairwise_s1(sc, z)
    s_two, _ = pairwise_s1(2 * sc, z)
    kn = kNL(z)
    dvH = C.Hz(z) * a / kn if np.isfinite(kn) else np.nan
    print("  %7.2f  %.3f   %7.4f    %7.2f    %7.2f   %7.2f            %8.3f    %8.4f      %8.2f"
          % (z, f, sc, s_half, s_one, s_two, kn, 1 / kn if np.isfinite(kn) else np.nan, dvH))

# chi thermal velocity, ILLUSTRATION under an explicit assumption (dark bath at the photon
# temperature until kinetic decoupling at T_kd = m/20; no entropy injection afterwards).
m_eV = 70e6
T0_eV = 8.617333262e-5 * C.T_cmb
T_kd = m_eV / 20
for z in [1089.92, 3.0, 0.0]:
    T = T0_eV * (1 + z)
    v = np.sqrt(3 * T_kd / m_eV) * (T / T_kd) * C.C_KMS
    print("chi thermal v_rms at z=%.1f (assumption: T_kd = m/20, dark bath = photon temperature): %.3e km/s" % (z, v))
