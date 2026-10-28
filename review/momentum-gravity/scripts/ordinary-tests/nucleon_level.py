"""Nucleon-level gate: best-case EP and light-vs-matter bounds, and a direct check of the Fermi-sphere estimate."""
import numpy as np

c = 299792.458
m_N = 938.9
VSTARS = [0.1, 1.0, 10.0, 120.0, 1000.0]
eta_micro_2s = 1.5e-15 + 2 * np.hypot(2.3e-15, 1.5e-15)
eta_ew_2s = 0.3e-13 + 2 * 1.8e-13
cass = (2.1e-5 + 2 * 2.3e-5) / 2

# Monte Carlo check of <exp(-|w_a - w_b|^2/v*^2)> for two uniform Fermi spheres (radius v_F), small v*/v_F
rng = np.random.default_rng(1)


def sphere(n, R):
    x = rng.normal(size=(n, 3))
    x /= np.linalg.norm(x, axis=1)[:, None]
    return x * R * rng.random(n)[:, None]**(1 / 3)


vF = 250.0 / np.sqrt(250.0**2 + m_N**2) * c
for frac in [0.05, 0.02]:
    vs = frac * vF
    est = []
    for rep in range(4):
        d = sphere(400000, vF) - sphere(400000, vF)
        est.append(np.mean(np.exp(-np.sum(d * d, axis=1) / vs**2)))
    print(f"MC <W> at v*/v_F = {frac}: {np.mean(est):.4e} +- {np.std(est)/np.sqrt(len(est)):.1e} (4 runs);"
          f" (3 sqrt(pi)/4)(v*/v_F)^3 = {3*np.sqrt(np.pi)/4*frac**3:.4e}")

print(f"\nk_F = 250 MeV/c (assumed), v_F = {vF:.0f} km/s")
for vs in VSTARS:
    W = 3 * np.sqrt(np.pi) / 4 * (vs / vF)**3
    print(f"  v* = {vs:7.1f}: <W> = {W:.2e};  best-case MICROSCOPE |eps| < {eta_micro_2s/W:.1e};"
          f" Eot-Wash {eta_ew_2s/W:.1e};  Cassini {cass/W:.1e}  (values > 1 mean no constraint)")
