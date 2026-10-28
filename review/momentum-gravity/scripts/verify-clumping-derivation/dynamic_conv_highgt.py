"""Resolution check of the strong-gating growth rates (MW, r=155/120): repeat two points at
finer v_z spacing and more Gauss-Laguerre nodes in v_perp."""
import numpy as np, sys
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-clumping-derivation')
from dynamic_eig import unstable, fmt
r = 155/120
for k2, gt in [(19.7392, 19000.0), (24.77, 1200.0)]:
    for hz, npp in [(0.045, 10), (0.035, 14), (0.045, 16)]:
        ev, dt = unstable(np.sqrt(k2), gt, r, thr=0.05, Lz=5.0, hz=hz, npp=npp)
        print(f"kap^2={k2} gt={gt:g} hz={hz} npp={npp}: {fmt(ev)} [{dt:.0f}s]"); sys.stdout.flush()
for k2, gt in [(24.77, 4500.0), (24.77, 5500.0), (24.77, 22000.0), (24.77, 26000.0)]:
    ev, dt = unstable(np.sqrt(k2), gt, r, thr=0.05, Lz=5.0, hz=0.045, npp=10)
    print(f"kap^2={k2} gt={gt:g} hz=0.045 npp=10: {fmt(ev)} [{dt:.0f}s]"); sys.stdout.flush()
