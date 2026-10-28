"""Combine the executed outputs into the allowed region in (eps = Gt/G, v*): parses lya_gas_grid.out,
lya_bounds.out (BOSS-scale mapping) and satellites.out, prints the bound of each probe and the strongest."""
import re
import numpy as np

D = "/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/dark-tests/"

lya = {}
for ln in open(D + "lya_gas_grid.out"):
    m = re.match(r"\s*(\d+)\s*\|\s*([\d.na]+)\s+([\d.na]+)\s*\|\s*([\d.na]+)\s+([\d.na]+)", ln)
    if m:
        v = int(m.group(1)); lya[v] = [float(x) for x in m.groups()[1:]]

boss = {}
txt = open(D + "lya_bounds.out").read()
blk = txt.split("BOSS-equivalent gated bound (same excess at k=0.2 h/Mpc, z=0.57):")[1].split("Ungated")[0]
for m in re.finditer(r"v\*=\s*(\d+) km/s: eps_equiv = ([\d.na]+)", blk):
    boss[int(m.group(1))] = float(m.group(2))

sat = {}
blk = open(D + "satellites.out").read().split("Translated limits")[1].split("Bullet")[0]
for ln in blk.splitlines():
    m = re.match(r"\s*(\d+)\s*\|\s*([\d.e+]+)\s*\|\s*([\d.e+]+)\s*\|\s*([\d.e+]+)\s*\|\s*([\d.e+]+)\s+([\d.e+]+)", ln)
    if m:
        sat[int(m.group(1))] = [float(x) for x in m.groups()[1:]]

print("eps_max(v*) by probe (95%-level estimates; see each script for model and data)")
print("  v*   | Lya DESI gauss matter/gas | Lya DESI rational matter/gas | BOSS-mapped | Sgr g/r | Fornax-peri g/r | strongest (gauss, matter..gas)")
for v in sorted(lya):
    gm, gg, rm, rg = lya[v]
    b = boss.get(v, np.nan)
    s = sat.get(v, [np.nan] * 5)
    cands = {"Lya": gm, "BOSS-mapped": b, "Sgr": s[0], "Fornax": s[1]}
    best = min((x, k) for k, x in cands.items() if np.isfinite(x))
    cands2 = {"Lya": gg if np.isfinite(gg) else np.inf, "BOSS-mapped": b, "Sgr": s[0], "Fornax": s[1]}
    best2 = min((x, k) for k, x in cands2.items() if np.isfinite(x))
    print("  %5d |   %7.4f / %7.4f       |    %7.4f / %7.4f         |  %7.4f    | %6.3g/%6.3g | %6.3g/%6.3g | %s %.4f .. %s %.4f"
          % (v, gm, gg, rm, rg, b, s[0], s[3], s[1], s[4], best[1], best[0], best2[1], best2[0]))
