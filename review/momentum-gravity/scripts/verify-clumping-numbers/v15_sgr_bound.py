"""Verifier v15: order-of-magnitude evaluation of the Kesden-Kamionkowski (PRL 97, 131303 [S]) Sgr-stream
bound (DM and baryons may not accelerate differently by more than ~10%) for a velocity-gated chi-chi force.
Differential acceleration of the satellite's chi toward the MW halo's chi: a_gate/a_grav ~ (G~/G) <W>,
<W> = average of W(|v_sat - v'|/v*) over halo velocities v' ~ N(0, sigma_h^2 I).  Bound: G~/G < 0.1/<W>
(taking the MW mass inside Sgr's orbit as chi-dominated; a chi fraction f_chi < 1 weakens it by 1/f_chi).
Sgr speed and halo dispersion at its radius are model-memory inputs (dagger), scanned over a range.
Gaussian closed form <W> = (v*^2/(v*^2+s^2))^1.5 exp(-v_sat^2/(2(v*^2+s^2))) checked by Monte Carlo."""
import numpy as np
rng = np.random.default_rng(7)

def W_gauss(s): return np.exp(-s**2 / 2)
def W_rat2(s): return (1 + s**2 / 2) ** -2

def avgW(W, vsat, sh, vstar, N=400000):
    v = rng.normal(0.0, sh, size=(N, 3))
    v[:, 0] -= vsat
    s = np.linalg.norm(v, axis=1) / vstar
    w = W(s)
    return w.mean(), w.std() / np.sqrt(N)

vstar = 120.0
print("v* = 120 km/s; bound G~/G < 0.1/<W>; instability thresholds to compare (agent C10, verified): MW 28.1-161, cluster 152-2929")
for vsat in [250.0, 300.0, 350.0]:
    for sh in [100.0, 120.0, 155.0]:
        closed = (vstar**2 / (vstar**2 + sh**2)) ** 1.5 * np.exp(-vsat**2 / (2 * (vstar**2 + sh**2)))
        mg, eg = avgW(W_gauss, vsat, sh, vstar)
        mr, er = avgW(W_rat2, vsat, sh, vstar)
        print(f"  v_sat={vsat:.0f} sigma_h={sh:.0f}: <W>_gauss={mg:.4f}+-{eg:.4f} (closed {closed:.4f}) -> G~/G < {0.1/mg:.2f};  "
              f"<W>_rat2={mr:.4f} -> G~/G < {0.1/mr:.2f}")
# narrow-gate scaling: ratio of local MW stream eigenvalue Lambda_g to <W>_Sgr, vs v*
print("\nRatio Lambda_g(sigma_loc=155/v*) / <W>_Sgr(gauss) vs v*  (instability needs gt*Lambda_g > Q >= 4.93; bound gt*<W> < 0.1,")
print("so the bound excludes the instability when Lambda_g/<W> < 10 Q ~ 49)")
for vstar in [10.0, 30.0, 60.0, 120.0, 240.0]:
    r = 155.0 / vstar
    Lg = (0.5 + r * r + np.sqrt(1 + 4 * r * r) / 2) ** -1.5
    for vsat, sh in [(300.0, 120.0), (350.0, 100.0)]:
        W = (vstar**2 / (vstar**2 + sh**2)) ** 1.5 * np.exp(-vsat**2 / (2 * (vstar**2 + sh**2)))
        print(f"  v*={vstar:5.0f}: v_sat={vsat:.0f}, sigma_h={sh:.0f}: Lambda_g={Lg:.3e}, <W>={W:.3e}, ratio={Lg/W:.1f}")
