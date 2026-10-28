"""verify-critic-numbers, claim c3: the gate exp(-s^2/2), s = |v1 - v2|/v*, applied to chi-chi gravity.

Independent of the critic's script (written before opening it).
Model: both velocities drawn from an isotropic Maxwellian with 1D dispersion sigma (homogeneous,
uncorrelated with position).  r = sigma/v*.

Three methods for the pair average <W>:
  (a) closed form: v1 - v2 is Gaussian with 1D dispersion sqrt(2) sigma, so
      <W> = (1 + 2 r^2)^(-3/2)                                   [D, Gaussian integral]
  (b) 1D quadrature over the relative speed with mpmath (Maxwell speed distribution)
  (c) Monte Carlo: 20 independent seeds x 4e5 pairs, error bar = std of run means / sqrt(20)
Also: test-particle gate <W>(v) for a chi particle of speed v (Maxwellian shift), its average over
the test particle's Maxwellian (must equal (a)), the binding factor f_b + (1 - f_b)<W>, and a crude
self-consistency iteration (isothermal scaling sigma_chi^2 = b * sigma_tracer^2) - a REDUCED model,
not a computed equilibrium.
"""
import numpy as np
import mpmath as mp

VSTAR = 120.0  # km/s, the record's knee (amplitude-gate convention exp(-v^2/(2 v*^2)))


def W_closed(sig, vs=VSTAR):
    r = sig / vs
    return (1 + 2 * r**2) ** -1.5


def W_quad(sig, vs=VSTAR):
    s2 = 2 * sig**2   # 1D variance of the relative velocity
    f = lambda u: 4 * mp.pi * u**2 * (2 * mp.pi * s2) ** -1.5 * mp.e**(-u**2 / (2 * s2)) * mp.e**(-u**2 / (2 * vs**2))
    return float(mp.quad(f, [0, 3 * sig, 10 * sig, mp.inf]))


def W_mc(sig, vs=VSTAR, nrun=20, n=400_000):
    means = []
    for seed in range(nrun):
        rng = np.random.default_rng(1000 + seed)
        v1 = rng.normal(0.0, sig, size=(n, 3))
        v2 = rng.normal(0.0, sig, size=(n, 3))
        s2 = np.sum((v1 - v2) ** 2, axis=1) / vs**2
        means.append(np.mean(np.exp(-0.5 * s2)))
        del v1, v2, s2
    means = np.array(means)
    return means.mean(), means.std(ddof=1) / np.sqrt(nrun)


def W_test(v, sig, vs=VSTAR):
    """gate averaged over source velocities, for a test particle of speed v (Maxwellian shift)"""
    return (vs**2 / (vs**2 + sig**2)) ** 1.5 * np.exp(-v**2 / (2 * (vs**2 + sig**2)))


def W_test_avg(sig, vs=VSTAR):
    f = lambda v: 4 * mp.pi * v**2 * (2 * mp.pi * sig**2) ** -1.5 * mp.e**(-v**2 / (2 * sig**2)) * W_test(float(v), sig, vs)
    return float(mp.quad(f, [0, 3 * sig, 10 * sig, mp.inf]))


print("== pair-averaged gate <W>, v* = 120 km/s")
print(f"{'case':28s} {'sigma':>7s} {'r':>7s} {'closed':>11s} {'quad':>11s} {'MC (20 runs)':>22s} {'test-avg':>11s}")
cases = [("MW, critic's sigma", 155.0), ("MW, sigma = 170 (240/sqrt2)", 170.0), ("MW, sigma = 165 (233/sqrt2)", 164.8),
         ("cluster, critic's sigma", 1000.0), ("Coma 1015 - 59", 956.0), ("Coma 1015", 1015.0), ("Coma 1015 + 59", 1074.0),
         ("dwarf core (3a) sigma = 30", 30.0)]
res = {}
for name, sig in cases:
    wc, wq = W_closed(sig), W_quad(sig)
    m, e = W_mc(sig)
    wt = W_test_avg(sig)
    res[name] = wc
    print(f"{name:28s} {sig:7.1f} {sig/VSTAR:7.4f} {wc:11.4e} {wq:11.4e} {m:11.4e} +- {e:8.1e} {wt:11.4e}")

print("\n== test-particle gate (source-averaged) at the halo's own speeds, MW sigma = 155 and cluster 1000")
for sig in (155.0, 1000.0):
    print(f"  sigma = {sig:6.1f}: v = 0: {W_test(0, sig):.4e}; v = sigma: {W_test(sig, sig):.4e}; "
          f"v = sqrt(3) sigma: {W_test(np.sqrt(3)*sig, sig):.4e}")

print("\n== binding factor b = f_b + (1 - f_b) <W>  (force on a chi particle from all matter, relative to ungated)")
fb_planck = 0.0224 / (0.0224 + 0.120)     # Planck 2018 abstract: Omega_b h^2 = 0.0224, Omega_c h^2 = 0.120 [S]
print(f"  cosmic f_b (Planck 2018 abstract, Omega_b h^2/(Omega_b h^2 + Omega_c h^2)) = {fb_planck:.4f}")
for name, sig, fbs in (("MW sigma=155", 155.0, (0.046, 0.10, fb_planck)), ("cluster sigma=1000", 1000.0, (0.13, fb_planck))):
    w = W_closed(sig)
    print("  " + name + ": " + "; ".join(f"f_b = {fb:.3f} -> b = {fb + (1-fb)*w:.4f}" for fb in fbs))
print("  (MW f_b = 0.046: stars 5e10 Msun [S: Bland-Hawthorn & Gerhard 2016] + ~1e10 cold gas (dagger) over Mvir 1.3e12 [S, via citing paper])")

print("\n== crude self-consistency (REDUCED model): chi dispersion set by the force it feels,")
print("   sigma_chi^2 = b(sigma_chi) * sigma_tr^2 (isothermal scaling at fixed density profile), iterate")
for name, sig_tr, fb in (("MW", 155.0, 0.046), ("MW", 155.0, fb_planck), ("cluster", 1000.0, 0.13), ("cluster", 1000.0, fb_planck)):
    s = sig_tr
    for _ in range(200):
        b = fb + (1 - fb) * W_closed(s)
        s_new = np.sqrt(b) * sig_tr
        if abs(s_new - s) < 1e-10:
            break
        s = 0.5 * (s + s_new)
    print(f"  {name:8s} f_b = {fb:.3f}: sigma_chi = {s:7.2f} km/s (r = {s/VSTAR:.3f}), <W> = {W_closed(s):.4f}, b = {b:.4f}")

print("\n== MC re-run with fresh seeds (the runs above reuse one seed set for every case, so their")
print("   fluctuations are common to all cases): cluster sigma = 1000, 40 runs x 1e6 pairs, seeds 5000-5039")
means = []
for seed in range(40):
    rng = np.random.default_rng(5000 + seed)
    d = rng.normal(0.0, 1000.0, size=(1_000_000, 3)) - rng.normal(0.0, 1000.0, size=(1_000_000, 3))
    means.append(np.mean(np.exp(-0.5 * np.sum(d**2, axis=1) / VSTAR**2)))
    del d
means = np.array(means)
print(f"  MC = {means.mean():.4e} +- {means.std(ddof=1)/np.sqrt(40):.1e}; closed = {W_closed(1000.0):.4e}; "
      f"pull = {(means.mean()-W_closed(1000.0))/(means.std(ddof=1)/np.sqrt(40)):+.2f} sigma")
