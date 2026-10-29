"""Arithmetic rechecks for the draft-answer number audit (answer-check-numbers).

Every input below is copied from a printed output named in the comment; this script
only redoes ratios, unit conversions and simple closed forms.
"""
import math
import os
import re
from collections import Counter

import numpy as np

C_KMS = 299792.458
G = 6.67430e-11
C = 299792458.0
PC = 3.0856775814913673e16

print("== margins (critic3/c4_numbers.out inputs: 28.07, 692.8; c1 0.1063; VCN u7 2.46)")
print(f"  28.07/0.1063 = {28.07/0.1063:.1f}   (draft: 264x)")
print(f"  692.8/0.1063 = {692.8/0.1063:.0f}   (draft: 6500x)")
print(f"  28.07/2.46   = {28.07/2.46:.2f}   (draft: at least 11x)")
print(f"  with the draft's rounded bound 0.11: 28.07/0.11 = {28.07/0.11:.0f}; 692.8/0.11 = {692.8/0.11:.0f}")

print("== second gate scale (draft: 4x at 30 km/s to 40x at 3 km/s)")
print(f"  120/30 = {120/30:.1f}; 120/3 = {120/3:.1f}")

print("== spin-2 velocity factors at 120 km/s (draft: 2.4e-7 X, 3.2e-7 graviton)")
b2 = (120.0 / C_KMS) ** 2
g2 = 1.0 / (1.0 - b2)
print(f"  (3g^2-1)/2 - 1 = {(3*g2-1)/2-1:.4e}; 2g^2-1 - 1 = {2*g2-2:.4e}")

print("== spin needed for O(1) at 120 km/s (draft: 3500-5000)")
Jm = (-1 + math.sqrt(1 + 16 / b2)) / 2
Jl = math.sqrt(2 / b2)
print(f"  J(J+1)/4 b^2 = 1 -> J = {Jm:.1f}; J^2/2 b^2 = 1 -> J = {Jl:.1f}")

print("== VON scan endpoint (draft: earlier scan stopped at 2923 km/s)")
grid = np.logspace(-1, math.log10(3000), 400)
kept = grid[grid <= 3000]
print(f"  last grid point {grid[-1]!r}; last kept {kept[-1]:.1f} km/s")

print("== gate conventions (task: v_a = sqrt2 v*)")
print(f"  sqrt2 * 120 = {math.sqrt(2)*120:.2f} km/s; 120/sqrt2 = {120/math.sqrt(2):.2f} km/s")
print(f"  VON scan 0.3-3000 km/s in v_a is v* = {0.3/math.sqrt(2):.3f}-{3000/math.sqrt(2):.0f} km/s in the record's convention")
print(f"  Mars 1.82e-11 at v_a=120 scaled by (170/120)^2 (leading order): {1.82e-11*(170/120)**2:.2e}  (VON at 170: 3.5e-11)")
print(f"  Mercury INPOP15a 1.7e-11..2.5e-11 at v_a=120 scaled the same way: "
      f"{1.7e-11*(170/120)**2:.1e}..{2.5e-11*(170/120)**2:.1e}  (not computed by any agent)")

print("== Vainshtein radius, 1 kg, lambda = 50 um, r_V^3 = K r_S lambda^2 (VCN u6: K = 2, 1, 15)")
rS = 2 * G * 1.0 / C**2
for K, label in ((2, "eq.43 m1=0 (repo line 383)"), (1, "eq.40 palindromic"), (15, "eq.41 palindromic")):
    rV = (K * rS * (50e-6) ** 2) ** (1 / 3)
    print(f"  K = {K:2d} {label:28s}: r_V = {rV:.3e} m; round(log10) = {round(math.log10(rV))}")

print("== screened windows (VCN u6: Saturn 1.024/0.264 pc, Pluto 8.560/2.210 pc; draft 0.3-9 pc)")
print(f"  span {min(1.024,0.264,8.560,2.210):.3f}-{max(1.024,0.264,8.560,2.210):.2f} pc")

print("== eBOSS compressed fit, H reading, v* = 120 (critic3/c1: chi2 26.31 -> 1.90)")
d = 26.31 - 1.90
print(f"  Delta chi2 = {d:.2f}; sqrt = {math.sqrt(d):.2f} (one-parameter Gaussian equivalent)")

print("== N-body window (corner/phys_scales.out)")
print(f"  25/0.5774 = {25/0.5774:.1f} t_ff; 43 x 14.96 Myr = {43*14.96/1e3:.3f} Gyr; "
      f"43 x 8.66 = {43*8.66/1e3:.3f} Gyr; 43 x 2.71 = {43*2.71/1e3:.3f} Gyr")

print("== N-body run count and seeds (corner/runs/log_*.txt)")
runs = sorted(os.listdir("/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/"
                         "7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/corner/runs"))
logs = [r for r in runs if r.startswith("log_")]
cases = Counter()
for r in logs:
    m = re.match(r"log_eps_([\d.]+)_rg_([\d.]+)_N_(\d+)_seed_(\d+)_.*?(_reading_F)?\.txt$", r)
    cases[(m.group(1), m.group(2), m.group(3), "F" if m.group(5) else "H")] += 1
print(f"  {len(logs)} run logs")
for k in sorted(cases):
    print(f"   eps={k[0]:>2} r_g={k[1]:>3} N={k[2]} reading {k[3]}: {cases[k]} seeds")

print("== injection test (corner/injection_test.out): smallest injected fraction and stream response")
print("  smallest injected fraction = 0.02; 2% stream: Xi(v*/2) 0.0852 -> 0.0396, S1 -0.0485 -> -0.0535, "
      "S2 0.1982 -> 0.2858 (dS2 = +0.088); control dS2 errors 0.04-0.11 (summary_numbers.out)")

print("== calc note #2 narrow-gate overstatement (critic3 c3 2.9e-31; linearized 8.7e-31)")
print(f"  8.7e-31/2.9e-31 = {8.7e-31/2.9e-31:.2f}")

print("== cores (VDD/VDN sigma_T/m = 2.369e-62 cm^2/g at G~ = G; need 30 cm^2/g; sigma ~ G~^2)")
print(f"  sqrt(30/2.369e-62) = {math.sqrt(30/2.369e-62):.3e}")

print("== record-convention top end of the ordinary-matter scan (VON vot_topend: gauss 8.65e-9, lorentz 9.42e-9 at v_a = 3000)")
va = math.sqrt(2) * 3000
print(f"  record v* = 3000 km/s is v_a = {va:.0f} km/s; leading-order v_a^2 scaling of the double-pulsar bound: "
      f"gauss {8.65e-9*(va/3000)**2:.2e}, lorentz {9.42e-9*(va/3000)**2:.2e}  (not computed by any agent)")

print("== crossover 1/Lambda_g(r), closed form Lambda_g = [(sqrt(1+4r^2)-1)/(2r^2)]^3, anchored on VCN u2")
lam = lambda r: ((math.sqrt(1 + 4 * r * r) - 1) / (2 * r * r)) ** 3
for r in (1.0, 1.2917, 1.5, 1.6, 8.3333):
    print(f"  r = {r:7.4f}: 1/Lambda_g = {1/lam(r):.3f}")
