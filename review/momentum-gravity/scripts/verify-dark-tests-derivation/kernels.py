"""
Independent check of the linear-response kernels of a velocity-gated attraction
about the Hubble flow (dark-tests claim K4).

Model: pair potential U = -Gt m^2 W(|v - v'|/v*) / |x - x'|.
Reading (a), the one the agent states: force on particle i = -dU/dx_i at FIXED
velocities v_i, v_j.  Then the acceleration of a test particle at the origin is

    a = Gt * Int d^3r rho(r) W(|v(r) - v0| / v*) r_hat / r^2 ,

with v(r) = H r + u(r) for the medium and v0 = u0 for the test particle.

Units: H = 1, v* = 1 (so s = v*/H = 1), Gt*rhobar = 1.
Ungated (W = 1) response to delta = d0 sin(k z):  a_z = 4 pi d0 / k.

Three linear pieces, computed by brute-force 2D quadrature (r, mu) of the FULL
integrand (no expansion of W), with small amplitudes and central differences:
 (A) density mode delta = d0 sin(kz), no peculiar velocities  -> R_dens(y)
 (B)+(C) velocity mode u = U0 cos(kz) z_hat, test particle co-moving with it
     (u0 = u(0) = U0 z_hat)                                     -> R_v(y)
 (C) alone: uniform medium, test particle with u0 = U0 z_hat     -> anti-drag
Closed forms compared:
 R_agent(y) = y Int_0^inf sin(y t) W(t) dt   (Gaussian: sqrt2 y F(y/sqrt2))
 R_mine(y)  = Int_0^inf W(t/y) j1(t) dt = Int_0^1 R_agent(y mu) dmu
              (Gaussian: 1 - sqrt2 F(y/sqrt2)/y)
 R_v(y)     = 3 Int_0^1 mu^2 R_agent(y mu) dmu
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30


def dawson(x):
    x = mp.mpf(x)
    return mp.sqrt(mp.pi) / 2 * mp.exp(-x * x) * mp.erfi(x)


def R_agent_gauss(y):
    return float(mp.sqrt(2) * y * dawson(y / mp.sqrt(2)))


def R_mine_gauss(y):
    return float(1 - mp.sqrt(2) * dawson(y / mp.sqrt(2)) / y)


def R_v_from(Ra, y):
    return float(3 * mp.quad(lambda m: m**2 * Ra(y * m), [0, 1]))


def R_mine_from(Ra, y):
    return float(mp.quad(lambda m: Ra(y * m), [0, 1]))


Wg = lambda u: np.exp(-0.5 * u**2)

# quadrature grid
nr, nm = 3000, 600
rmax = 12.0
xr, wr = np.polynomial.legendre.leggauss(nr)
r = 0.5 * rmax * (xr + 1.0)
wr = 0.5 * rmax * wr
mu, wm = np.polynomial.legendre.leggauss(nm)
R, MU = np.meshgrid(r, mu, indexing="ij")
WW = np.outer(wr, wm)


def accel_z(rho_fac, dvz):
    """a_z = 2 pi Int dr dmu rho_fac * W(|r rhat + dvz zhat|) * mu  (r^2 cancels 1/r^2)."""
    mag = np.sqrt(R**2 + 2.0 * R * dvz * MU + dvz**2)
    return 2.0 * np.pi * np.sum(WW * rho_fac * Wg(mag) * MU)


print("Brute-force 2D quadrature, Gaussian gate W = exp(-u^2/2), reading (a): -grad_x U at fixed velocities")
print("Ungated normalization check (W=1 replaced by W(r) with huge v*):")
# check normalisation: W -> 1 cannot be integrated to infinity on this grid; use j1 identity instead
print("   Int_0^inf j1(t) dt =", float(mp.quad(lambda t: mp.sin(t) / t**2 - mp.cos(t) / t, [0, mp.inf])))

d0 = 1e-6
U0 = 1e-5
print()
print("   y   | R_dens brute | R_mine closed | R_agent closed || R_v brute | R_v closed | B-only brute | R_v-1 closed")
for y in [0.3, 0.6, 1.0, 1.08, 2.0, 3.0, 5.0]:
    k = y  # s = 1
    Z = R * MU
    # (A) density
    aA = accel_z(1.0 + d0 * np.sin(k * Z), 0.0) - accel_z(1.0 - d0 * np.sin(k * Z), 0.0)
    aA /= 2.0
    Rd = aA / (4.0 * np.pi * d0 / k)
    # (B)+(C): medium velocity U0 cos(kz) z, test particle u0 = U0 z ; dv = u(r) - u0
    dv_p = U0 * (np.cos(k * Z) - 1.0)
    aBC = (accel_z(1.0, dv_p) - accel_z(1.0, -dv_p)) / 2.0
    Rv = aBC / (4.0 * np.pi / 3.0 * U0)
    # (B) only: test particle at rest, medium velocity U0 cos(kz)
    dv_b = U0 * np.cos(k * Z)
    aB = (accel_z(1.0, dv_b) - accel_z(1.0, -dv_b)) / 2.0
    RB = aB / (4.0 * np.pi / 3.0 * U0)
    print(f" {y:5.2f} |  {Rd:10.6f}  |  {R_mine_gauss(y):10.6f}   |  {R_agent_gauss(y):10.6f}    || {Rv:9.6f} | {R_v_from(R_agent_gauss, y):9.6f}  |  {RB:10.6f}  | {R_v_from(R_agent_gauss, y) - 1:10.6f}")

# (C) anti-drag alone: uniform medium, test particle moving with U0 z_hat: dv = -U0
aC = (accel_z(1.0, -U0) - accel_z(1.0, U0)) / 2.0
print()
print(f"(C) anti-drag, uniform medium: a_z / U0 = {aC / U0:.6f} ; analytic (4 pi/3) Gt rho/H = {4 * np.pi / 3:.6f}")
print("    sign: positive = along the particle's own peculiar velocity (anti-drag)")

# identity check R_mine = Int_0^1 R_agent(y mu) dmu
print()
for y in [0.5, 1.0, 2.0]:
    print(f"identity check y={y}: Int_0^1 R_agent(y mu) dmu = {R_mine_from(R_agent_gauss, y):.8f} ; R_mine closed = {R_mine_gauss(y):.8f}")

# small-y limits
print()
for y in [1e-2, 3e-2]:
    print(f"small y={y}: R_mine/y^2 = {R_mine_gauss(y) / y**2:.6f} (expect 1/3 = Int t W dt / 3) ; R_agent/y^2 = {R_agent_gauss(y) / y**2:.6f}")

# overshoot of R_agent
ys = np.linspace(0.05, 12, 2000)
ra = np.array([R_agent_gauss(v) for v in ys])
rm = np.array([R_mine_gauss(v) for v in ys])
i = np.argmax(ra)
print()
print(f"R_agent max = {ra[i]:.4f} at y = {ys[i]:.3f}  (exceeds 1: effective-potential kernel)")
print(f"R_mine  max on grid = {rm.max():.4f} ; monotonic increasing: {bool(np.all(np.diff(rm) > 0))}")
