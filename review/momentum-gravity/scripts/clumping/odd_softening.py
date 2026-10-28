"""Test: does the purely growing coupled rate at fixed kappa^2 = 19.7392 (MW, r = 1.2917) collapse as the parity-odd
sector reaches its static threshold gt_odd = kappa^2/(Lam_g q)?  (Lam_g q = top static eigenvalue of the l=1 sector.)"""
import sys, math
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from env_growth import root
from static_threshold import Lam_g_closed, q_closed
r, k2 = 1.2917, 19.7392
godd = k2/(Lam_g_closed(r)*q_closed(r))
print(f"odd-sector static threshold gt_odd = kappa^2/(Lam_g q) = {godd:.2f}")
for gt in [200.0, 240.0, 255.0, 265.0, 272.0, 277.0, 280.7, 283.0, 290.0, 320.0]:
    G, res = root(Gated(r, gt), math.sqrt(k2))
    print(f"gt={gt:6.1f} (gt/gt_odd={gt/godd:.4f}): purely growing Gamma = {G:.4f}")
    sys.stdout.flush()
