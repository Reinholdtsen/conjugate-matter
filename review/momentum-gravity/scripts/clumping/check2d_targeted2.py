"""2D (v_perp, v_z) m=0 check of the factorized purely growing roots at kappa^2 = 19.7392 (MW, r = 1.2917):
gt = 255 (factorized 0.68660) and gt = 1275 (factorized 0.18851; probe also found 0.1151).
Signs of the real determinant det(kappa^2 - M(i Gamma)) on a Gamma grid; a change marks an m=0 eigenvalue crossing."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from check2d import detsign
r = 1.2917
kw = dict(nperp=10, h=0.6)
k = math.sqrt(19.7392)
for gt, Gf in [(255.0, 0.68660), (1275.0, 0.18851)]:
    t1 = time.time()
    Gs = sorted(set([round(x, 4) for x in [0.1, 0.13, 0.17, 0.2, 0.25, 0.35, 0.5, 0.62, 0.66, 0.71, 0.75, 0.9, 1.2, 1.6, 2.2, 3.0, 4.5]]))
    out = []
    for G in Gs:
        s, im, n = detsign(r, gt, k, G, **kw)
        out.append((G, int(round(s))))
    ch = [(out[i][0], out[i+1][0]) for i in range(len(out)-1) if out[i][1] != out[i+1][1]]
    print(f"gt={gt} (factorized top {Gf}): signs {out}; sign changes in {ch} (n={n}, {time.time()-t1:.0f}s)")
    sys.stdout.flush()
