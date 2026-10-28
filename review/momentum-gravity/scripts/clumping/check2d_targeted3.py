"""2D (v_perp, v_z) m=0 determinant-sign scan at r = 1.2917, Gt/G = 56.14 for kappa^2 = 2 and 3, where the factorized
solver gave purely growing roots 0.025 and none: tests whether faster purely growing m=0 roots exist there."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from check2d import detsign
r, gt = 1.2917, 56.14
kw = dict(nperp=10, h=0.6)
for k2 in [2.0, 3.0]:
    t1 = time.time(); k = math.sqrt(k2)
    Gs = [0.03, 0.06, 0.1, 0.15, 0.22, 0.3, 0.4, 0.5, 0.65, 0.8, 1.0, 1.3, 1.7, 2.3, 3.2]
    out = [(G, int(round(detsign(r, gt, k, G, **kw)[0]))) for G in Gs]
    ch = [(out[i][0], out[i+1][0]) for i in range(len(out)-1) if out[i][1] != out[i+1][1]]
    print(f"kappa^2={k2}: signs {out}; sign changes in {ch} ({time.time()-t1:.0f}s)")
    sys.stdout.flush()
