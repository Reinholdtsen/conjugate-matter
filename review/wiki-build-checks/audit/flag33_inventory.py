#!/usr/bin/env python3
"""Flag 33, part 2: the inventory with explicit kinds, tested under each reading
of the coverage claim. Read-only on the repository.

Kinds:
  own      the record's own computed figure (adjudicator's code/recount, or [V])
  anchor   a textbook/published anchor the record names
  ref      a figure computed by the round-3 referee (or v3, restated) and quoted
  ownnc    a figure in the record's own voice that no script computed
  lit      a literature value or formula (an input)
  v3wrong  a v3 value quoted as wrong
  input    a model input (counting)
"""
import re, subprocess
HERE = "/tmp/claude-1000/-home-paul-git-reinholdtsen-conjugate-matter/f914ff8b-9e54-489b-92fe-c443048774ac/scratchpad/audit"
REPO = "/home/paul/git/reinholdtsen/conjugate-matter"
ADJ = open(f"{REPO}/review/round3-adjudication.md", encoding="utf-8").read()
CPL = open(f"{REPO}/papers/broken-born-checkpoint-v2.md", encoding="utf-8").read().splitlines()
SRC = open(f"{REPO}/verify/soliton_obituary.py", encoding="utf-8").read()
OLD = open(f"{HERE}/knot_numbers_96f58da.py", encoding="utf-8").read()
a = next(i for i, l in enumerate(CPL) if l.startswith("## 12."))
b = next(i for i in range(a + 1, len(CPL)) if CPL[i].startswith("## "))
S12 = "\n".join(CPL[a:b])
labels = re.findall(r'check\(\s*"([^"]+)"', SRC)
old_labels = re.findall(r'check\(\s*"([^"]+)"', OLD)
print(f"current script: {len(labels)} checks; predecessor knot_numbers.py @96f58da: {len(old_labels)} checks")

def line_of(text, sub, off=1):
    k = text.find(sub)
    return None if k < 0 else text[:k].count("\n") + off

# (doc, quoted substring, kind, cover: ('label', s) | ('code', s) | None, old-label substring or None)
INV = [
 ("adj", "p = 104.31 with M_Pl", "own", ("label", "p = 104.31 with M_Pl"), None),
 ("adj", "0.828 with the reduced M_Pl", "own", ("label", "p = 0.828 with reduced M_Pl"), None),
 ("adj", "(1.66√g*)³ ≈ 4.6×10³", "own", ("label", "~ 4.6e3"), None),
 ("adj", "M* = 2.9–4.4×10¹² GeV", "own", ("label", "2.9-4.4e12 GeV"), None),
 ("adj", "overproduced 2.1×10³–1.2×10⁴ times", "own", ("label", "2.1e3-1.2e4"), None),
 ("adj", "consistently normalized, the two conventions agree", "own", ("label", "conventions agree"), None),
 ("adj", "10% of the DM at 45–49 GeV", "own", ("label", "45-49 GeV"), None),
 ("adj", "100% at 146–158 GeV", "own", ("label", "146-158 GeV"), None),
 ("adj", "ξ bound 0.760, not 0.77", "own", ("label", "xi < 0.760"), None),
 ("adj", "ΔN_eff < 0.286", "own", ("label", "< 0.286"), None),
 ("adj", "3.2×10⁷ Hz", "own", ("label", "3.2e7 Hz"), None),
 ("adj", "at least 10³–10⁴ (ruling 2)", "own", ("label", "2.1e3-1.2e4"), None),
 ("adj", "(a factor of 4)", "input", ("code", "4*omega_h2("), None),
 ("adj", "n/s ≈ 100 (T_c/M_Pl)³", "anchor", ("label", "n/s ~ 100"), None),
 ("adj", "Friedmann coefficient 1.66", "anchor", ("label", "H = 1.66 sqrt(g*)"), None),
 ("adj", "Kibble–Zurek integration (1e9–1e12 overproduction)", "ref", None, None),
 ("adj", "gives 28–46 / 96–153 GeV", "ref", None, None),
 ("adj", "lower mass bound should be ≳ 20–30 MeV", "ref", None, None),
 ("adj", "α_m ≈ 34", "ref", None, "alpha_m = 1/(4 alpha) ~ 34"),
 ("adj", "ε ~ 1e-7–1e-6", "ref", None, "eps ~ v/M ~ 1e-7 to 1e-6"),
 ("adj", "We agree to within ×1.6", "ownnc", None, None),
 ("adj", "≳ 100 PeV unless diluted", "lit", None, None),
 ("adj", "εθ/2π · e", "lit", None, None),
 ("adj", "ε ≲ 10⁻¹³ from gravity", "lit", None, None),
 ("adj", "up to ×10", "v3wrong", None, None),
 ("adj", "v3's 0.1–0.3 TeV was wrong", "v3wrong", None, None),
 ("adj", "1e13–4e13 GeV, no dilution required", "v3wrong", None, None),
 ("§12", "p ≈ 104 [V]", "own", ("label", "p = 104.31 with M_Pl"), None),
 ("§12", "p ≈ 0.023 (#14 v3)", "own", ("label", "v3's 0.0228"), None),
 ("§12", "M ≈ 2.9–4.4×10¹² GeV [V]", "own", ("label", "2.9-4.4e12 GeV"), None),
 ("§12", "2.1×10³–1.2×10⁴ [V]", "own", ("label", "2.1e3-1.2e4"), None),
 ("§12", "10¹⁶–10¹⁷ at the v3 benchmark [V]", "own", ("label", "1e16-1e17"), None),
 ("§12", "a factor of a hundred to several thousand", "own", ("label", "~ 4.6e3"), None),
 ("§12", "≲ 100 PeV", "lit", None, None),
]
rows = []
for doc, sub, kind, cover, old in INV:
    text, off = (ADJ, 1) if doc == "adj" else (S12, a + 1)
    ln = line_of(text, sub, off)
    assert ln is not None, f"not in source: {sub}"
    if cover is None:
        cov = False
    elif cover[0] == "label":
        cov = any(cover[1] in l for l in labels)
        assert cov, f"label missing: {cover[1]}"
    else:
        cov = cover[1] in SRC
        assert cov, f"code missing: {cover[1]}"
    had_old = (old is not None) and any(old in l for l in old_labels)
    rows.append((doc, ln, sub, kind, cov, had_old))
print(f"inventory: {len(rows)} quoted numbers, every one located in its source text\n")
print(f"{'doc':4s} {'line':>4s} {'kind':7s} {'gated':5s} {'old':4s} quoted")
for doc, ln, sub, kind, cov, old in rows:
    print(f"{doc:4s} {ln:4d} {kind:7s} {'yes' if cov else 'NO':5s} {'yes' if old else '':4s} {sub}")

# Readings of 'every number that [adj] and [§12] quote ... recomputed and checked'
READINGS = {
  "R1 plain: every number quoted except v3 values quoted as wrong": {"own","anchor","input","ref","ownnc","lit"},
  "R2 knot_numbers convention: computed figures only (inputs/literature excluded)": {"own","anchor","input","ref","ownnc"},
  "R3 own voice: the record's own figures (referee figures excluded)": {"own","anchor","input","ownnc"},
  "R4 'corrected record' = adjudicator's recomputed figures + §12 [V]": {"own","anchor","input"},
}
print()
for name, kinds in READINGS.items():
    scope = [r for r in rows if r[3] in kinds]
    miss = [r for r in scope if not r[4]]
    print(f"{name}\n   in scope {len(scope)}, gated {len(scope)-len(miss)}, NOT gated {len(miss)}"
          + ("" if not miss else ":  " + "; ".join(f"{r[0]} l.{r[1]} '{r[2]}'" for r in miss)))

# §12's own claim, scoped to [V]
v_rows = [r for r in rows if r[0] == "§12" and "[V]" in r[2]]
print(f"\n§12's claim 'The [V] numbers here are gated': [V] numbers {len(v_rows)}, gated {sum(r[4] for r in v_rows)}")

# Closing line 'every number the round-3 record quotes reproduces': do the referee's ruling-4 figures reproduce?
out = subprocess.run([f"{REPO}/.venv/bin/python", f"{REPO}/verify/soliton_obituary.py"],
                     capture_output=True, text=True, cwd=REPO).stdout
m = re.search(r"10% of the dark matter at 45-49 GeV\s+\[([\d.]+)-([\d.]+)\]", out)
n = re.search(r"100% at 146-158 GeV\s+\[([\d.]+)-([\d.]+)\]", out)
r10 = (float(m.group(1)), float(m.group(2))); r100 = (float(n.group(1)), float(n.group(2)))
print(f"\nscript's psi window: 10% at {r10[0]}-{r10[1]} GeV, 100% at {r100[0]}-{r100[1]} GeV")
print(f"referee's quoted window 28-46 / 96-153 GeV reproduces? 10%: {r10 == (28.0, 46.0)}, 100%: {r100 == (96.0, 153.0)}")
print(f"largest endpoint ratio recount/referee: {max(r10[0]/28, r10[1]/46, r100[0]/96, r100[1]/153):.3f}")

# The adjudication's own coverage sentences, in full
print("\nadjudication sentences claiming coverage:")
for k in [m.start() for m in re.finditer("which checks", ADJ)]:
    s = ADJ.rfind("\n", 0, ADJ.rfind("\n", 0, k)) + 1
    e = ADJ.find(".", k) + 1
    print(f"  line {ADJ[:k].count(chr(10))+1}: " + " ".join(ADJ[s:e].split()))
for kw in ("did not re-run", "Accepted, not re-checked"):
    for mm in re.finditer(re.escape(kw), ADJ):
        print(f"  line {ADJ[:mm.start()].count(chr(10))+1}: contains '{kw}'")

# The flag's fourth item: benchmark arithmetic that survives
k0 = ADJ.find("## What survives v3"); k1 = ADJ.find("\n## ", k0 + 5)
surv = ADJ[k0:k1]
nums = re.findall(r"\d+(?:\.\d+)?(?:e[+-]?\d+)?|10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+", surv)
print(f"\n'What survives v3' numbers quoted: {nums}  (flux, densities, σ_T/M are named, with no value)")
for nm, pat in (("flux", "F = n v / 4 pi"), ("densities", "mean n ~ 4.2e-20"), ("sigma_T/M", "sigma_T/M ~ 1e-26")):
    print(f"  {nm:10s}: current script gates it: {any(pat in l for l in labels)}; predecessor @96f58da did: {any(pat in l for l in old_labels)}")
