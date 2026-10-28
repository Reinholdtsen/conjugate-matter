# (1) O22: amplitude factor of a velocity-gated Yukawa between two 300 K bodies at rest (atom-level
#     gating, Gaussian W): <W> = (1 + 2 s^2/v*^2)^(-3/2), s^2 = s_A^2 + s_B^2; and nucleon-level (3 sqrt(pi)/4)(v*/v_F)^3.
# (2) O13: sensitivity of the Gaussian LLR window edge to the lunar eccentricity (the Gaussian tail is
#     dominated by the slowest, apogee, part of the orbit).  e = 0.026-0.077 is the range of the
#     osculating lunar eccentricity (dagger, from memory); a single Kepler orbit at each e is a reduction,
#     not a model of the solar-perturbed orbit.
import importlib.util, numpy as np
kB = 1.380649e-23; amu = 1.66053907e-27
s = lambda A: np.sqrt(kB*300/(A*amu))/1e3
pairs = {'Ti-W (47.87, 183.84)': (47.867, 183.84), 'Be-Cu (9.01, 63.55)': (9.012182, 63.546)}
for lab, (a, b) in pairs.items():
    s2 = s(a)**2 + s(b)**2
    print(f"{lab}: s = {np.sqrt(s2):.3f} km/s; <W>(V=0) at v* = 0.01, 0.1, 1, 10 km/s: " +
          ", ".join(f"{(1 + 2*s2/vs**2)**-1.5:.3g}" for vs in [0.01, 0.1, 1., 10.]))
vF = 77136.
print("nucleon-level factor at v* = 1, 10, 120 km/s: " + ", ".join(f"{3*np.sqrt(np.pi)/4*(vs/vF)**3:.2g}" for vs in [1., 10., 120.]))
spec = importlib.util.spec_from_file_location("vb", "/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-ordinary-tests-numbers/vot_bounds_lib.py")
vb = importlib.util.module_from_spec(spec); spec.loader.exec_module(vb)
for e in [0.026, 0.0549, 0.077]:
    vb.moon['e'] = e
    row = []
    for vs in [0.16, 0.17, 0.18, 0.20]:
        row.append(f"v*={vs:.2f}: {vb.bounds(vs, 'gauss')['LLR perigee']:.3g}")
    # v* where LLR bound = Eros bound 0.615
    lo, hi = 0.15, 0.25
    for _ in range(60):
        mid = 0.5*(lo + hi)
        if vb.bounds(mid, 'gauss')['LLR perigee'] > 0.615: lo = mid
        else: hi = mid
    print(f"lunar e = {e}: LLR bound " + "; ".join(row) + f" ; LLR = Eros (0.615) at v* = {hi:.4f} km/s")
