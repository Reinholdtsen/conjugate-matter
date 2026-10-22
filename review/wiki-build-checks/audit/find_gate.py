import re, glob, sys
root = "/home/paul/git/reinholdtsen/conjugate-matter/"
files = sorted(glob.glob(root+"notes/*.md")+glob.glob(root+"papers/*.md")+glob.glob(root+"popsci/*.md")+[root+"HANDOFF.md"])
pats = [r"v_\*", r"v_\{\*\}", r"v\\\*", r"v\*", r"μ/m", r"\\mu/m", r"keV", r"k\^2/", r"k²/", r"μ²", r"\\mu\^2", r"fiber", r"p-width", r"width μ", r"width \$\\mu", r"√2", r"\\sqrt\{?2", r"sqrt 2", r"gate scale", r"relative momentum", r"p_1-p_2|p_1 - p_2|p₁ ?− ?p₂|p_1−p_2"]
rx = re.compile("|".join(pats))
for f in files:
    if "toy" in f: continue
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        for m in rx.finditer(line):
            s = max(0, m.start()-110); e = min(len(line), m.end()+110)
            print(f"{f.replace(root,'')}:{i}: ...{line[s:e].strip()}...")
            break
