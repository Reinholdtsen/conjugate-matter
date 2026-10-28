"""Critic check c3: the most literal reading of 'regular gravity that depends on
relative velocity' for chi bodies -- the fiber-overlap gate acting on chi-chi
graviton exchange itself (the record asserts chi gravity is ungated, #11 sec. 8,
but derives no reason; program-analysis open question 3).

If chi-chi gravity carried the gate W(s) = exp(-s^2/2), s = |v1 - v2|/v* (the
amplitude-level convention of the notebook, v* = sqrt2 mu/m), a virialized chi halo
with 1D dispersion sigma would have its chi self-gravity multiplied by the
pair average <W> = (1 + 2 sigma^2/v*^2)^(-3/2)  (relative velocity of two
Maxwellian particles has per-component variance 2 sigma^2).
Checked by Monte Carlo (independent runs give the error bar).
Also printed: the rate-level convention W = exp(-s^2) for comparison.
Consequence estimate: a cluster's chi would then be bound mainly by baryons; the
ratio of the available potential to the virial requirement is ~ f_b + (1-f_b)<W>.
"""
import numpy as np

def W_avg_closed(sigma, vs, rate=False):
    k = 2.0 if rate else 1.0    # exp(-k s^2/2): k=1 amplitude, k=2 rate convention
    return (1 + 2 * k * sigma**2 / vs**2) ** -1.5

rng_seeds = [11, 22, 33, 44]
envs = [("UFD (sigma = 4 km/s)", 4.0), ("classical dSph (10)", 10.0), ("dwarf core (30)", 30.0),
        ("MW halo (155)", 155.0), ("cluster (1000)", 1000.0)]
vs = 120.0
print(f"v* = {vs} km/s, gate on chi-chi graviton exchange (hypothetical)")
for name, s in envs:
    mc = []
    for sd in rng_seeds:
        rng = np.random.default_rng(sd)
        w = rng.normal(0, np.sqrt(2) * s, size=(400000, 3))
        mc.append(np.mean(np.exp(-np.sum(w**2, axis=1) / (2 * vs**2))))
    mc = np.array(mc)
    print(f"  {name:22s} <W> closed = {W_avg_closed(s, vs):.4e}  MC = {mc.mean():.4e} +- {mc.std(ddof=1)/2:.1e}"
          f"   (rate convention exp(-s^2): {W_avg_closed(s, vs, rate=True):.4e})")

fb = 0.156   # Omega_b/Omega_m (Planck 2018: 0.0493/0.3153)  [dagger inputs]
for name, s in envs[-2:]:
    Wv = W_avg_closed(s, vs)
    print(f"{name}: effective binding of chi relative to ungated ~ f_b + (1 - f_b)<W> = {fb + (1-fb)*Wv:.3f}")
