# Remaining per-test numbers (claims O14a, O15) and a candidate test in the Gaussian low-v* window:
# Dawn's orbital GM of Ceres against the pre-Dawn perturbation (ephemeris) GM.
#   Dawn: GM = 62.62736 +- 0.00040 km^3/s^2 (Konopliv et al. 2018, Icarus 299; via search snippet [S])
#   pre-Dawn: 62.36 +- 0.37 km^3/s^2 (Konopliv et al. 2006, as tabulated in the 2011 Dawn gravity overview,
#   NTRS 20140010847; via search snippet [S]); encounter speeds of km/s, so W ~ 0 there for v* <= 0.3 km/s
#   Dawn orbit radii at Ceres (dagger, from memory): RC3 ~13,600+470 km, Survey ~4,400+470,
#   HAMO ~1,470+470, LAMO ~385+470 km; Ceres mean radius ~470 km (dagger)
import importlib.util, numpy as np
spec = importlib.util.spec_from_file_location("vb", "/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-ordinary-tests-numbers/vot_bounds_lib.py")
vb = importlib.util.module_from_spec(spec); spec.loader.exec_module(vb)
vb.dp_limit = 1.3e-4/2.5
for shape in ['gauss', 'lorentz']:
    for vs in [1., 10., 120., 1000.]:
        b = vb.bounds(vs, shape)
        keys = [k for k in b if k.startswith('Kepler')] + ['Cassini']
        print(f"{shape:8s} v* = {vs:6.0f}: " + "; ".join(f"{k} {b[k]:.3g}" for k in keys))
print()
x = 62.62736/62.36 - 1; s = np.hypot(0.00040/62.36, 0.37*62.62736/62.36**2)
lim = max(abs(x - 2*s), abs(x + 2*s))
print(f"Ceres: GM_Dawn/GM_preDawn - 1 = {x:+.4f} +- {s:.4f}; 2 sigma |max| = {lim:.4f}")
GM = 62.62736
phases = {'RC3': 13600 + 470, 'Survey': 4400 + 470, 'HAMO': 1470 + 470, 'LAMO': 385 + 470}
K = lambda u: (1 + 2*u**2)*np.exp(-u**2)
for vs in [0.07, 0.1, 0.15, 0.2, 0.3]:
    parts = []
    Ks = []
    for nm, rr in phases.items():
        v = np.sqrt(GM/rr); Ks.append(K(v/vs))
        parts.append(f"{nm} v={v:.3f} K={K(v/vs):.3g}")
    print(f"v* = {vs:4.2f}: " + "; ".join(parts) +
          f" -> |eps| < {lim/max(Ks):.3g} (most favourable phase) ... {lim/min(Ks):.3g} (least favourable)")
