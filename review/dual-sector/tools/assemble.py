"""Assemble WF-A's readers and verifiers into the panel's evidence: digest.md (answers and record points, each with
its verifier's verdict), missed.md (passages the verifiers added) and statements.json (every quoted statement with
its verdict). Matching of a statement to its verdict is by paper id and the first 60 characters of the quotation."""
import json, re
from pathlib import Path
W = Path(__file__).resolve().parents[1] / "wfA"
OUT = Path(__file__).parent
labels = sorted(p.stem for p in W.glob("r?-*.json") if not p.stem.endswith("-verify"))
digest, missed, stmts = [], [], []
norm = lambda s: re.sub(r"\s+", " ", s or "").strip()[:60]
for r in labels:
    rd = json.loads((W / f"{r}.json").read_text()); vf = json.loads((W / f"{r}-verify.json").read_text())
    vmap = {(v["paper_id"], norm(v["quote_start"])[:40]): v for v in vf["statements"]}
    digest.append(f"\n\n# Reader {r}\n\nVerifier's overall assessment: {vf['overall']}\n")
    digest.append("\n## Papers read\n")
    for p in rd["papers"]:
        digest.append(f"- {p['id']} — {p['citation'][:220]} — first posted {p['first_posted'][:60]} — read: {p['read_how'][:120]}")
    digest.append("\n## Answers (reader), each with the verifier's verdict\n")
    va = {x["question"]: x for x in vf["answers"]}
    for a in rd["answers"]:
        v = va.get(a["question"]) or next((x for x in vf["answers"] if x["question"].split()[0] == a["question"].split()[0]), None)
        digest.append(f"### {a['question']} (reader confidence {a['confidence']})\n\n{a['answer']}\n\nEvidence: {'; '.join(a['evidence'])}\n")
        if v:
            digest.append(f"**Verifier: {v['verdict']}.** {v['correction']}" + (f"\n\nCounter-evidence: {' | '.join(v['counter_evidence'])}" if v['counter_evidence'] else "") + "\n")
        else:
            digest.append("**Verifier: no verdict matched to this answer.**\n")
    digest.append("\n## Where the reader found the record contradicted or qualified, with the verifier's verdict\n")
    for i, c in enumerate(rd["contradicts_record"]):
        v = vf["record_contradictions"][i] if i < len(vf["record_contradictions"]) else None
        digest.append(f"### {r} record point {i}\n\nRecord says: {c['record_says']}\n\nSource says: {c['source_says']}\n\nWhy: {c['why']}\n")
        digest.append(f"**Verifier: {v['verdict']}.** {v['note']}\n" if v else "**Verifier: no verdict.**\n")
    if rd["not_retrieved"]:
        digest.append("\n## Not retrieved\n\n" + "\n".join(f"- {x}" for x in rd["not_retrieved"]))
    if vf["retried"]:
        digest.append("\n## Verifier's second attempts\n\n" + "\n".join(f"- {x}" for x in vf["retried"]))
    for m in vf["missed"]:
        missed.append(f"- [{r}] {m['paper_id']} ({m['where']}; {', '.join(m['bears_on'])}): \"{m['quote']}\" — {m['why_it_matters']} [{m['quote_check'][:60]}]")
    for p in rd["papers"]:
        for s in p["statements"]:
            v = vmap.get((p["id"], norm(s["quote"])[:40]))
            stmts.append({"reader": r, "paper": p["id"], "first_posted": p["first_posted"][:40], "quote": s["quote"], "where": s["where"],
                          "bears_on": s["bears_on"], "reading": s["reading"], "quote_check": s["quote_check"],
                          "verdict": v["verdict"] if v else None, "correction": v["correction"] if v else None})
(OUT / "digest.md").write_text("# Evidence digest for the dual-sector panel\n\nBuilt by code from the nine readers and their verifiers (workflow A, 2026-11-06)." + "\n".join(digest), encoding="utf-8")
(OUT / "missed.md").write_text("# Passages the verifiers found that the readers missed\n\n" + "\n".join(missed), encoding="utf-8")
(OUT / "statements.json").write_text(json.dumps(stmts, indent=1, ensure_ascii=False), encoding="utf-8")
matched = sum(1 for s in stmts if s["verdict"])
print(f"digest {len(''.join(digest))} chars; missed {len(missed)}; statements {len(stmts)} ({matched} matched to a verdict)")
