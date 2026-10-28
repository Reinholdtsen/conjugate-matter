"""Locate the small 280.7 discrepancy (agent 0.1597, mine 0.1590): agent uses r = 1.2917, I used 155/120."""
import numpy as np, sys
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-clumping-derivation')
from dynamic_eig2 import unstable_mapped
from dynamic_eig import fmt
for r in [155/120, 1.2917]:
    for npp in [10, 14]:
        ev, ns, dt = unstable_mapped(np.sqrt(19.7392), 280.7, r, v0=0.0, alpha=0.15, ds=0.04, npp=npp)
        print(f"r={r:.6f} npp={npp}: {fmt(ev)}")
