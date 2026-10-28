"""verify-critic-numbers, sgr: DM share of the host's radial acceleration along Sgr's radii in the u7 toy
models (spherical approximation).  KK's PRD states its limit as a DM force > 10% of gravity (beta^2 > 0.1);
the PRL phrases it as DM and baryons accelerating differently by > 10%, which would weaken the eps bound
by 1/f_DM if read as the difference relative to the total acceleration."""
import numpy as np
src = open("/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-critic-numbers/u7_sgr_bound.py").read()
ns = {}
exec(src[:src.index("x0 = np.array([17.5, 2.5, -6.5])")], ns)
for M in ns['models']:
    out = []
    for r in (15.0, 19.0, 30.0, 45.0, 60.0):
        Mh = 4 * np.pi * M.rho_s * M.rs**3 * (np.log(1 + r / M.rs) - r / (r + M.rs))
        out.append(f"r={r:.0f}: {Mh/M.Menc_sph(r):.3f}")
    print(f"{M.name:24s} f_DM = M_halo/M_total: " + ", ".join(out))
