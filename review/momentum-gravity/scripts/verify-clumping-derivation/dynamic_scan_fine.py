"""Fine-grid scan of the fastest unstable m=0 mode vs gate strength at fixed k (MW: r=155/120).
Uniform v_z grid (trapezoid), Gauss-Laguerre in v_perp, brute-force eigenvalues; operator as in
dynamic_eig.py. A mode is resolved when Im(omega)/kap exceeds ~2 grid spacings; resolution is
checked by repeating at two spacings."""
import numpy as np, sys, time
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-clumping-derivation')
from dynamic_eig import unstable, fmt
r = 155/120
k2 = float(sys.argv[1]); gts = [float(x) for x in sys.argv[2].split(',')]
hzs = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [0.045, 0.03]
for gt in gts:
    for hz in hzs:
        ev, dt = unstable(np.sqrt(k2), gt, r, thr=0.05, Lz=5.0, hz=hz, npp=10)
        print(f"kap^2={k2} gt={gt:g} hz={hz}: {fmt(ev)} [{dt:.0f}s]"); sys.stdout.flush()
