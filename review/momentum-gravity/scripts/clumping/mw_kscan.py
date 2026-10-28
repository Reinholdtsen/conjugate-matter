"""MW (r = 1.2917): purely growing coupled growth rate Gamma(kappa^2) at Gt/G = 56.14 and 280.7 (2x and 10x the
no-revir threshold for Q = 4.93), to find the fastest mode with kappa^2 >= Q. Gamma in 1/t_ff (t_ff = 40.98 Myr)."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from env_growth import root
for gt in [56.14, 280.7]:
    m = Gated(1.2917, gt)
    row = []
    for k2 in [1.0, 2.0, 3.0, 4.9348, 8.0, 12.0, 19.7392, 30.0]:
        G, res = root(m, math.sqrt(k2))
        row.append((k2, round(G, 4)))
    print(f"gt={gt}: (kappa^2, Gamma) = {row}  ; t_ff=40.98 Myr, t_orb(sun)=219 Myr")
    sys.stdout.flush()
