#!/usr/bin/env python3
"""Flag 33 audit: does verify/soliton_obituary.py check every number that
review/round3-adjudication.md and #11 §12 quote for the soliton candidate?

Read-only on the repository. Prints:
  1. the script's own check labels and a fresh run of it;
  2. every numeric token in the adjudication and in #11 §12, by line;
  3. a hand-built inventory of the numbers quoted for the candidate, each
     anchored to its source line by exact substring, with its voice and
     whether a check label in the script covers it;
  4. the derived quantities this audit cites (x1.6, alpha_m).
"""
import re, subprocess, sys
from math import pi

REPO = "/home/paul/git/reinholdtsen/conjugate-matter"
ADJ = open(f"{REPO}/review/round3-adjudication.md", encoding="utf-8").read().splitlines()
CP = open(f"{REPO}/papers/broken-born-checkpoint-v2.md", encoding="utf-8").read().splitlines()
SRC = open(f"{REPO}/verify/soliton_obituary.py", encoding="utf-8").read()

# §12 is the block from its heading to the next '## ' heading
s12_start = next(i for i, l in enumerate(CP) if l.startswith("## 12."))
s12_end = next(i for i in range(s12_start + 1, len(CP)) if CP[i].startswith("## "))
S12 = CP[s12_start:s12_end]
print(f"#11 §12 spans file lines {s12_start+1}-{s12_end}")

# ---- 1. the script's checks
labels = re.findall(r'check\(\s*"([^"]+)"', SRC)
print(f"\n== 1. check() calls in verify/soliton_obituary.py: {len(labels)}")
for i, l in enumerate(labels, 1):
    print(f"  {i:2d}. {l}")
run = subprocess.run([f"{REPO}/.venv/bin/python", f"{REPO}/verify/soliton_obituary.py"],
                     capture_output=True, text=True, cwd=REPO)
passes = [l for l in run.stdout.splitlines() if l.startswith("PASS")]
fails = [l for l in run.stdout.splitlines() if l.startswith("FAIL")]
print(f"  fresh run: exit {run.returncode}, {len(passes)} PASS, {len(fails)} FAIL")
print(f"  closing line: {run.stdout.strip().splitlines()[-1]!r}")
doc = SRC.split('"""')[1]
print("  docstring lines 1-3 and 'corrected record' line:")
for l in doc.splitlines():
    if l.strip() and ("every number" in l or "quote" in l or "corrected record" in l or "recomputed" in l):
        print("    |", l)

# ---- 2. raw numeric tokens, so nothing is missed
NUM = re.compile(r"(?<![\w.])(?:\d+(?:\.\d+)?(?:[eE][+-]?\d+)?(?:[–-]\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)?"
                 r"(?:\s*×\s*10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)?|10[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)")
def tokens(lines, offset):
    out = []
    for i, l in enumerate(lines):
        t = NUM.findall(l)
        if t:
            out.append((i + offset, t))
    return out
print("\n== 2a. numeric tokens in review/round3-adjudication.md (line: tokens)")
for ln, t in tokens(ADJ, 1):
    print(f"  {ln:3d}: {t}")
print("\n== 2b. numeric tokens in #11 §12 (line: tokens)")
for ln, t in tokens(S12, s12_start + 1):
    print(f"  {ln:3d}: {t}")

# ---- 3. inventory of numbers quoted for the soliton candidate
# (doc, exact substring, voice, label-substring in the script that covers it, or None)
A, S = "adj", "§12"
INV = [
  (A, "p = 104.31 with M_Pl", "adjudicator, 'My code' (r1)", "p = 104.31 with M_Pl"),
  (A, "0.828 with the reduced M_Pl", "adjudicator, 'My code' (r1)", "p = 0.828 with reduced M_Pl"),
  (A, "(1.66√g*)³ ≈ 4.6×10³", "adjudicator (r1)", "drops (1.66 sqrt(g*))^3 ~ 4.6e3"),
  (A, "M* = 2.9–4.4×10¹² GeV", "adjudicator (r2)", "M* at minimum production = 2.9-4.4e12 GeV"),
  (A, "overproduced 2.1×10³–1.2×10⁴ times", "adjudicator (r2)", "overproduced 2.1e3-1.2e4 times"),
  (A, "consistently normalized, the two conventions agree", "adjudicator (r2)", "conventions agree"),
  (A, "≳ 100 PeV unless diluted", "literature: LMW abstract (r3)", None),
  (A, "Kibble–Zurek integration (1e9–1e12 overproduction)", "REFEREE; 'I did not re-run' (r3)", None),
  (A, "(a factor of 4)", "adjudicator; model input (r4)", "both doublet members"),
  (A, "up to ×10", "v3's bracket, quoted as wrong (r4)", None),
  (A, "10% of the DM at 45–49 GeV", "adjudicator, 'My recount' (r4)", "10% of the dark matter at 45-49 GeV"),
  (A, "100% at 146–158 GeV", "adjudicator, 'My recount' (r4)", "100% at 146-158 GeV"),
  (A, "gives 28–46 / 96–153 GeV", "REFEREE's Boltzmann integration (r4)", None),
  (A, "We agree to within ×1.6", "ADJUDICATOR's own comparison (r4)", None),
  (A, "v3's 0.1–0.3 TeV was wrong", "v3, quoted as wrong (r4)", None),
  (A, "ξ bound 0.760, not 0.77", "referee finding, upheld (r5)", "xi < 0.760"),
  (A, "ΔN_eff < 0.286", "adjudicator (r5)", "Delta N_eff < 0.286"),
  (A, "3.2×10⁷ Hz", "adjudicator (r5)", "GW upper end 3.2e7 Hz"),
  (A, "lower mass bound should be ≳ 20–30 MeV", "accepted, 'not re-checked' (r6)", None),
  (A, "εθ/2π · e", "literature formula, 'not re-checked' (r9)", None),
  (A, "α_m ≈ 34", "referee finding column, upheld at abstract level (r10)", None),
  (A, "ε ~ 1e-7–1e-6", "referee's omitted-constraint list (v3's estimate)", None),
  (A, "n/s ≈ 100 (T_c/M_Pl)³", "lesson 2 anchor", "n/s ~ 100 (T_c/M_Pl)^3"),
  (A, "The replacement anchors\n   are the Friedmann coefficient 1.66", "lesson 2 anchor", "H = 1.66 sqrt(g*)"),
  (A, "ε ≲ 10⁻¹³ from gravity", "decision 1 (literature value; about P4)", None),
  (A, "at least 10³–10⁴ (ruling 2)", "decision 2, rounding of r2", "overproduced 2.1e3-1.2e4 times"),
  (A, "1e13–4e13 GeV, no dilution required", "v3's headline, quoted as wrong (verdict)", None),
  (S, "p ≈ 104 [V]", "[V]", "p = 104.31 with M_Pl"),
  (S, "p ≈ 0.023 (#14 v3)", "v3's value, diagnosed", "v3's 0.0228 drops"),
  (S, "M ≈ 2.9–4.4×10¹² GeV [V]", "[V]", "M* at minimum production = 2.9-4.4e12 GeV"),
  (S, "2.1×10³–1.2×10⁴ [V]", "[V]", "overproduced 2.1e3-1.2e4 times"),
  (S, "≲ 100 PeV", "[29S] literature", None),
  (S, "10¹⁶–10¹⁷ at the v3 benchmark [V]", "[V]", "overclose by 1e16-1e17"),
  (S, "a factor of a hundred to several thousand", "plain-language; p/1 and p/0.0228", "drops (1.66 sqrt(g*))^3 ~ 4.6e3"),
]
adj_text = "\n".join(ADJ); s12_text = "\n".join(S12)
def where(doc, sub):
    text, lines, off = (adj_text, ADJ, 1) if doc == A else (s12_text, S12, s12_start + 1)
    k = text.find(sub)
    if k < 0:
        return None
    return text[:k].count("\n") + off
print("\n== 3. inventory: numbers quoted for the soliton candidate")
print(f"  {'doc':4s} {'line':>4s}  {'covered':8s} voice  |  quoted text")
missing_src, uncovered = [], []
for doc, sub, voice, lab in INV:
    ln = where(doc, sub)
    if ln is None:
        missing_src.append(sub)
    cov = "-"
    if lab is not None:
        hits = [l for l in labels if lab in l]
        cov = "CHECKED" if hits else "LABEL?!"
    else:
        cov = "no"
        uncovered.append((doc, ln, sub, voice))
    print(f"  {doc:4s} {str(ln):>4s}  {cov:8s} {voice}  |  {sub!r}")
print(f"  inventory entries: {len(INV)}; not found in source text: {missing_src or 'none'}")
lab_bad = [lab for _, _, _, lab in INV if lab is not None and not any(lab in l for l in labels)]
print(f"  coverage labels not found in the script: {lab_bad or 'none'}")

print("\n  Uncovered, split by kind:")
inputs_or_wrong = ("literature", "v3's", "v3,", "decision 1")
computed = [u for u in uncovered if not any(u[3].startswith(p) or p in u[3][:12] for p in inputs_or_wrong)]
other = [u for u in uncovered if u not in computed]
print("   (a) computed figures for the candidate, quoted and NOT recomputed by the script:")
for d, ln, sub, v in computed:
    print(f"       {d} line {ln}: {sub!r}  <- {v}")
print("   (b) literature inputs, or v3 values quoted as wrong (no reading expects these to 'reproduce'):")
for d, ln, sub, v in other:
    print(f"       {d} line {ln}: {sub!r}  <- {v}")
print(f"   counts: (a) {len(computed)}, (b) {len(other)}")
uncovered_s12 = [u for u in uncovered if u[0] == S]
print(f"   §12 entries uncovered: {[(u[2], u[3]) for u in uncovered_s12]}")

# the flag's fourth item: does either document quote a NUMBER for flux, densities or sigma_T/M?
i0 = next(i for i, l in enumerate(ADJ) if l.startswith("## What survives v3"))
i1 = next(i for i in range(i0 + 1, len(ADJ)) if ADJ[i].startswith("## "))
surv = ADJ[i0:i1]
print(f"\n== 3b. 'What survives v3' (adj lines {i0+1}-{i1}): numeric tokens = {[t for _, t in tokens(surv, i0+1)]}")
for kw in ("flux", "densit", "σ_T", "sigma_T"):
    hits_adj = [i + 1 for i, l in enumerate(ADJ) if kw in l]
    hits_s12 = [i + s12_start + 1 for i, l in enumerate(S12) if kw in l]
    hits_src = [i + 1 for i, l in enumerate(SRC.splitlines()) if kw.lower() in l.lower()]
    print(f"  '{kw}': adjudication lines {hits_adj}; §12 lines {hits_s12}; script lines {hits_src}")
for kw in ("Zurek", "MeV", "alpha_m", "28", "Boltzmann", "eps", "1.6"):
    hits_src = [i + 1 for i, l in enumerate(SRC.splitlines()) if kw in l]
    print(f"  script lines containing '{kw}': {hits_src}")

print("\n== 3c. the adjudication's own coverage claims and its 'not re-checked' labels")
for i, l in enumerate(ADJ, 1):
    if ("every number" in l or "not re-checked" in l or "did not re-run" in l
            or "checks every" in l or (i > 1 and "every number" in ADJ[i-2] + l)):
        print(f"  {i:3d}: {l.strip()[:150]}")

# ---- 4. derived quantities cited by the audit
print("\n== 4. derived quantities")
lo10, hi10, lo100, hi100 = 45.2, 48.8, 146.4, 158.0          # the script's printed values
ref10, ref100 = (28, 46), (96, 153)                          # as quoted in ruling 4
ref10_notes = 28.3                                           # referee audit-notes line 116
print(f"  recount/referee, 10% lower ends : 45.2/28  = {lo10/ref10[0]:.3f};  45.2/28.3 = {lo10/ref10_notes:.3f}")
print(f"  recount/referee, 10% upper ends : 48.8/46  = {hi10/ref10[1]:.3f}")
print(f"  recount/referee, 100% lower ends: 146.4/96 = {lo100/ref100[0]:.3f}")
print(f"  recount/referee, 100% upper ends: 158.0/153 = {hi100/ref100[1]:.3f}")
ALPHA = 1/137.035999
print(f"  alpha_m = 1/(4 alpha) = {1/(4*ALPHA):.3f}  (ruling 10 quotes 'α_m ≈ 34'; not in the script)")
print(f"  p ratios behind §12's 'a hundred to several thousand': 104.3106/1 = {104.3106:.1f}; "
      f"104.3106/0.0228 = {104.3106/0.0228:.0f}")
