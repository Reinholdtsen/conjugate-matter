"""
v7_misc_numbers.py  (verify-critic-theory, round 3) -- numbers quoted in the loophole entries.

T2: constituent speeds inside ordinary bodies (a gate acting on constituent pairs would be closed
    by internal motion): electron in hydrogen alpha c; nucleon Fermi momentum 250-270 MeV/c
    (dagger, textbook nuclear-matter value).
T3: velocity scale of gravitational Sommerfeld/ladder effects between chi quanta, alpha_G c with
    alpha_G = G m^2/(hbar c), m = 70 MeV.
T8: hbar H0 (H0 = 67.4 and 73 km/s/Mpc, dagger), the mass scale of a thawing scalar.
c1 tuned spin-0 + spin-1 pair: Eotvos parameter if the scalar couples to mass and the vector to
    baryon number, each 1.248e7 times the residual (v1 part E). Atomic masses (dagger, AME):
    Be-9 9.0121831 u, Ti-48 47.9479463 u, Pt-195 194.9647917 u.
"""
import math
c = 299792458.0
alpha = 7.2973525693e-3
hbar = 1.054571817e-34
G = 6.67430e-11
eV = 1.602176634e-19
MeV = 1e6 * eV

print(f"T2: alpha c = {alpha*c/1e3:.1f} km/s")
mN = 938.92  # MeV, mean nucleon mass
for pF in [250.0, 270.0]:
    vF = pF / math.sqrt(pF ** 2 + mN ** 2)
    print(f"    nucleon Fermi momentum {pF:.0f} MeV/c -> v_F = {vF:.3f} c = {vF*c/1e3:.3e} km/s")
v_star = 120.0
print(f"    ratios to v* = 120 km/s: alpha c / v* = {alpha*c/1e3/v_star:.1f}")

m_chi = 70.0 * MeV / c ** 2
aG = G * m_chi ** 2 / (hbar * c)
print(f"T3: alpha_G(chi, 70 MeV) = {aG:.3e};  alpha_G c = {aG*c:.3e} m/s")

Mpc = 3.0856775814913673e22
for H0 in [67.4, 73.0]:
    H = H0 * 1e3 / Mpc
    print(f"T8: H0 = {H0} km/s/Mpc -> hbar H0 = {hbar*H/eV:.3e} eV, c/H0 = {c/H/Mpc/1e3:.2f} Gpc")

ratio = 1.2483e7            # each component / residual (v1 part E)
u = {"Be-9": (9.0121831, 9), "Ti-48": (47.9479463, 48), "Pt-195": (194.9647917, 195)}
bpm = {k: A / M for k, (M, A) in u.items()}   # baryons per unit mass, in units of 1/u
for k, v in bpm.items():
    print(f"c1: {k}: baryon number per unit mass = {v:.6f} /u")
for a_, b_ in [("Be-9", "Ti-48"), ("Ti-48", "Pt-195")]:
    eta = ratio * (bpm[a_] - bpm[b_])
    print(f"c1: tuned pair, vector on baryon number: Eotvos eta({a_},{b_}) ~ {ratio:.3e} x {bpm[a_]-bpm[b_]:+.3e} = {eta:+.2e}")

# T4 (massive tower): mass of a carrier whose range is 1 kpc or 1 au (AKT 2018 [S]: an infinite
# fine-tuned higher-spin tower affects graviton dynamics at energies comparable to its lightest mass)
pc = 3.0856775814913673e16
hbarc_eVm = 197.3269804e6 * 1e-15
for name, L in [("1 kpc", 1e3 * pc), ("1 au", 1.495978707e11)]:
    print(f"T4: range {name}: carrier mass hbar c / L = {hbarc_eVm / L:.3e} eV")

# T9 (continuous-spin carrier, Schuster-Toro-Zhou JHEP 04 (2023) 010 eq. (129) [S]):
# L_int ~ (g^2/4 pi r)[1 - (rho r)^2 (|v_ij| - v_ij.rhat)^2/32 + ...]  (natural units; scalar spatial current)
# correction O(1) at rho v r ~ 1 -> rho = hbar c (c/v)/r ; also the static-deviation length hbar c/rho
for vk, name, L in [(120.0, "1 kpc", 1e3 * pc), (120.0, "10 kpc", 1e4 * pc), (29.78, "1 au (Earth orbit)", 1.495978707e11)]:
    rho = hbarc_eVm * (c / (vk * 1e3)) / L
    print(f"T9: v_rel = {vk} km/s at r = {name}: rho v r/(hbar c) = 1 for rho = {rho:.3e} eV; hbar c/rho = {hbarc_eVm/rho:.3e} m = {hbarc_eVm/rho/pc:.3e} pc")
    # size of the leading correction for transverse motion, |v| - v.rhat = v: (rho r)^2 v^2 / 32 at that rho
    print(f"    leading correction at that rho for transverse motion: (rho r v)^2/32 = {1/32:.4f} (expansion parameter = 1)")
