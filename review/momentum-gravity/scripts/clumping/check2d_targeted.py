"""Targeted independent check of the factorized growth-rate solver with the 2D (v_perp, v_z) m = 0 Nystrom
(check2d.py functions).  For each case: static limit at the same resolution vs radial Nystrom; then
sign of det(kappa^2 - M(i Gamma)) at Gamma = 0.9, 0.97, 1.03, 1.1 x (factorized root) and at a coarse set
above the root (a sign change in the bracket confirms the root; no change above it means no larger
purely growing m = 0 root)."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from check2d import detsign, static2d
from static_threshold import top_eigs

r = 1.2917
kw = dict(nperp=10, h=0.6)
if __name__ == '__main__':
    for gt in [56.14, 280.7]:
        e2, n = static2d(r, gt, nperp=10, h=0.6)
        print(f"static, nperp=10 h=0.6: gt={gt}: 2D {e2:.5f} vs radial {top_eigs(r, gt, 0, nev=1)[0][0]:.5f} (n={n})")
    sys.stdout.flush()
    for k2, gt, Gf in [(4.9348, 56.14, 0.44210), (4.9348, 280.7, 0.56618)]:
        k = math.sqrt(k2)
        t1 = time.time()
        out = []
        for f in [0.9, 0.97, 1.03, 1.1]:
            s, im, n = detsign(r, gt, k, f*Gf, **kw)
            out.append((round(f*Gf, 4), int(round(s)), float("%.1e" % im)))
        above = []
        for G in [0.8, 1.2, 2.0, 3.5]:
            s, im, n = detsign(r, gt, k, G, **kw)
            above.append((G, int(round(s)), float("%.1e" % im)))
        print(f"kappa^2={k2}, gt={gt}, factorized root {Gf}: det signs near root {out}; above {above} (n={n}, {time.time()-t1:.0f}s)")
        sys.stdout.flush()
