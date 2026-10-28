"""Reduced cluster run (r = 8.333): purely growing coupled root at kappa^2 = Q = 1.0966 for gt = 1598 (2x the
re-virialized threshold 798.8) and gt = 304.4 (2x the no-revir threshold 152.2). Coarse scan (24 pts) + 22 bisections."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from static_threshold import top_eigs
from env_growth import Dtilde
r = 8.3333; tff = 149.62; tcross = 3*tff; Q = 1.0966
for gt in [1598.0, 304.4]:
    t1 = time.time()
    m = Gated(r, gt, L=6.0); k = math.sqrt(Q)
    L0 = top_eigs(r, gt, 0, nev=1)[0][0]
    Gs = np.geomspace(3.0, 3e-3, 24)
    vals = [Dtilde(m, k, G)[0] for G in Gs]
    G = 0.0
    for i in range(len(Gs) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            a, b, fa = Gs[i], Gs[i + 1], vals[i]
            for _ in range(22):
                mm = math.sqrt(a*b); fm = Dtilde(m, k, mm)[0]
                if np.sign(fm) == np.sign(fa): a, fa = mm, fm
                else: b = mm
            G = math.sqrt(a*b); break
    res = abs(m.D(k, 1j*G)) if G > 0 else None
    te = tff/G if G > 0 else float('inf')
    print(f"cluster Q={Q} gt={gt}: Lambda_0={L0:.4f}, Gamma={G:.5f}/t_ff, e-fold={te:.0f} Myr, t_e/t_cross={te/tcross:.3f} |D|={res} ({time.time()-t1:.0f}s)")
    sys.stdout.flush()
