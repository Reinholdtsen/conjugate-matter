#!/usr/bin/env python3
"""Copy the literature check's record from work/literature-check/ into review/literature-check/.

Only structured outputs, query logs, briefs, scripts and tools are copied. The agents' download folders and the
full-text cache stay in work/ (copyrighted texts, ~400 MB). Fails if any copied file holds an e-mail address.
"""
import glob
import os
import re
import shutil
import sys

WORK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(WORK))
DEST = os.path.join(REPO, "review", "literature-check")
SCRIPTS = os.path.expanduser("~/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/"
                             "ffa896d4-bb41-4d95-8eb7-c38982df6f8d/workflows/scripts")
PREREG = os.path.expanduser("~/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/prereg/literature-check.md")

plan = [("BRIEF.md", "brief.md"), ("results.json", "findings.json"), ("recheck.json", "recheck.json"),
        ("recheck-all.out", "recheck.out")]
plan += [(f"screen{s}", f"screen/screen{s}") for s in (".json", ".out", "-fulltext.json", "-gap.json")]
for g in sorted(glob.glob(os.path.join(WORK, "g?-*"))):
    name = os.path.basename(g)
    plan += [(f"{name}/search.json", f"round1/{name}.search.json"), (f"{name}/verify.json", f"round1/{name}.verify.json")]
    for q in ("queries.jsonl", "queries.log", "queries.tsv", "web_queries.json"):
        if os.path.exists(os.path.join(g, q)):
            plan.append((f"{name}/{q}", f"round1/{name}.{q}"))
    for v in ("verify", "verifier"):
        for q in ("queries.jsonl", "queries.log"):
            if os.path.exists(os.path.join(g, v, q)):
                plan.append((f"{name}/{v}/{q}", f"round1/{name}.verifier-{q}"))
for p in sorted(glob.glob(os.path.join(WORK, "round2", "r*.json"))):
    b = os.path.basename(p)
    out = b if b.endswith((".out.json", ".verify.json")) else b.replace(".json", ".input.json")
    plan.append((f"round2/{b}", f"round2/{out}"))
plan.append(("round2/r4-triage/queries.tsv", "round2/r4-triage.queries.tsv"))
for p in sorted(glob.glob(os.path.join(WORK, "round3", "*.json"))):
    b = os.path.basename(p)
    plan.append((f"round3/{b}", f"round3/{b}"))
for d in ("lineages", "oa-c1-c6-c7", "oa-c2-c3-c4", "oa-c5"):
    for q in ("queries.log", "queries.tsv", "web_queries.tsv"):
        if os.path.exists(os.path.join(WORK, "round3", d, q)):
            plan.append((f"round3/{d}/{q}", f"round3/{d}.{q}"))
for p in sorted(glob.glob(os.path.join(WORK, "panel", "*.json"))):
    b = os.path.basename(p)
    plan.append((f"panel/{b}", f"panel/{b.replace('.json', '.evidence.json') if re.match(r'C\d', b) else b}"))
for n in range(1, 5):
    plan.append((f"workflow{n}-result.json", f"workflows/workflow{n}-result.json"))
for t in ("lit.py", "consolidate.py", "recheck.py", "screen.py", "assemble_record.py"):
    plan.append((f"tools/{t}", f"tools/{t}"))

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@(?:gmail|googlemail)\.com|paul\.reinholdtsen", re.I)
bad = 0
for src, dst in plan:
    s = os.path.join(WORK, src)
    d = os.path.join(DEST, dst)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copyfile(s, d)
for js in sorted(glob.glob(os.path.join(SCRIPTS, "literature-check-*.js"))):
    shutil.copyfile(js, os.path.join(DEST, "workflows", os.path.basename(js)))
shutil.copyfile(PREREG, os.path.join(DEST, "preregistration.md"))
for root, _, files in os.walk(DEST):
    for f in files:
        p = os.path.join(root, f)
        if EMAIL.search(open(p, encoding="utf-8", errors="replace").read()):
            print("E-MAIL FOUND:", p)
            bad = 1
total = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(DEST) for f in fs)
print(f"{len(plan) + 5} files copied to {DEST}, {total / 1e6:.2f} MB")
sys.exit(bad)
