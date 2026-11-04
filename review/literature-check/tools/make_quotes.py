#!/usr/bin/env python3
"""Build review/literature-check/quotes.json: every quotation from the literature that notes/literature-check.md
uses, found by code in its source (abstract or arXiv full text), with an excerpt and a hash of the full text.
Candidates: writeup/planned_quotes.tsv (id <TAB> quotation). Uses the gate's own normalization."""
import hashlib
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lit  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
spec = importlib.util.spec_from_file_location("gate", os.path.join(REPO, "verify", "literature_check.py"))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

_, body, _ = gate.note_parts()
nbody = gate.norm(body)
docs = gate.repo_texts()
cands = [line.rstrip("\n").split("\t", 1) for line in open(os.path.join(os.path.dirname(HERE), "writeup",
                                                                         "planned_quotes.tsv"), encoding="utf-8")
         if line.strip()]
out, unused = [], []
for ident, q in cands:
    nq = gate.norm(q)
    if nq not in nbody:
        unused.append((ident, q))
        continue
    verdict, where, _ = lit.check_quote(ident, q)
    assert verdict.startswith("FOUND"), (ident, q, verdict)
    entry = {"id": ident, "text": q, "source": "abstract" if where.startswith("abstract") else "full text",
             "found": f"{verdict} in {where}", "checked": "2026-11-03"}
    if entry["source"] == "full text":
        url, text, _ = lit.fulltext(ident if not ident.startswith(("recid:", "doi:")) else "")
        nt = gate.norm(text)
        k = nt.find(nq)
        if k < 0:
            lt, lq = gate.loose(text), gate.loose(q)
            assert lq in lt, (ident, q)
            entry["excerpt"] = q
            entry["excerpt_note"] = "found only after removing punctuation; the excerpt is the quotation itself"
        else:
            entry["excerpt"] = nt[max(0, k - 200):k + len(nq) + 200]
        entry["url"], entry["sha256"] = url, hashlib.sha256(nt.encode()).hexdigest()
    out.append(entry)
spans = [s for s in re.findall(r'"([^"]+)"', body, flags=re.S) if len(s.split()) >= 3]
orphans = [s for s in spans if not any(gate.norm(s) in d for d in docs.values())
           and not any(gate.norm(s) in gate.norm(e["text"]) for e in out)]
# Quotations entered by hand, for sources lit.py cannot reach (round 5: Khademi 2009's abstract), are kept.
qpath = os.path.join(REPO, "review", "literature-check", "quotes.json")
if os.path.exists(qpath):
    out += [e for e in json.load(open(qpath, encoding="utf-8")) if e["id"].startswith("openalex:")
            and gate.norm(e["text"]) in nbody]
with open(qpath, "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)
print(f"{len(out)} quotations written; {len(unused)} candidates unused:")
for i, q in unused:
    print("   unused:", i, q[:70])
print(f"{len(orphans)} quoted passages found neither in the repository nor among the quotations:")
for s in orphans:
    print("   orphan:", re.sub(r"\s+", " ", s)[:110])
