"""Re-sort the evidence by question: by-question.md (answers to Q1..Q11 and other findings from every reader, each with
its verifier's verdict; then every record point with its verdict) and papers.md (each reader's papers and how read)."""
import json, re, collections
from pathlib import Path
W = Path(__file__).resolve().parents[1] / "wfA"; OUT = Path(__file__).parent
labels = sorted(p.stem for p in W.glob("r?-*.json") if not p.stem.endswith("-verify"))
byq = collections.defaultdict(list); rec, papers = [], []
def qkey(q):
    m = re.match(r"\s*(Q\d+)", q); return m.group(1) if m else "Other"
for r in labels:
    rd = json.loads((W / f"{r}.json").read_text()); vf = json.loads((W / f"{r}-verify.json").read_text())
    vlist = list(vf["answers"])
    for a in rd["answers"]:
        v = next((x for x in vlist if x["question"] == a["question"]), None) or \
            next((x for x in vlist if qkey(x["question"]) == qkey(a["question"]) and qkey(a["question"]) != "Other"), None)
        if v: vlist.remove(v)
        txt = f"#### {r}: {a['question']} (reader confidence {a['confidence']})\n\n{a['answer']}\n\nEvidence: {'; '.join(a['evidence'])}\n\n"
        txt += (f"**Verifier ({r}-verify): {v['verdict']}.** {v['correction']}" + (f"\n\nCounter-evidence: {' | '.join(v['counter_evidence'])}" if v["counter_evidence"] else "")) if v else "**Verifier: no verdict matched.**"
        byq[qkey(a["question"])].append(txt + "\n")
    for v in vlist:  # verifier answers with no reader answer
        byq[qkey(v["question"])].append(f"#### {r}-verify only: {v['question']}\n\n**{v['verdict']}.** {v['correction']}\n")
    for i, c in enumerate(rd["contradicts_record"]):
        v = vf["record_contradictions"][i] if i < len(vf["record_contradictions"]) else None
        rec.append(f"#### {r} record point {i}\n\nRecord says: {c['record_says']}\n\nSource says: {c['source_says']}\n\nWhy (reader): {c['why']}\n\n" + (f"**Verifier: {v['verdict']}.** {v['note']}\n" if v else "**Verifier: none.**\n"))
    for j in range(len(rd["contradicts_record"]), len(vf["record_contradictions"])):  # raised by the verifier alone
        v = vf["record_contradictions"][j]
        rec.append(f"#### {r}-verify record point {j} (raised by the verifier, not the reader)\n\nRecord says: {v['record_says']}\n\n**Verifier: {v['verdict']}.** {v['note']}\n")
    papers.append(f"\n## {r}\n\nVerifier's overall: {vf['overall']}\n")
    papers += [f"- {p['id']} — {p['citation']} — first posted {p['first_posted']} — read: {p['read_how']}" for p in rd["papers"]]
    if rd["not_retrieved"]: papers.append("\nNot retrieved: " + " | ".join(rd["not_retrieved"]))
    if vf["retried"]: papers.append("\nVerifier's second attempts: " + " | ".join(vf["retried"]))
    if rd["leads"]: papers.append("\nLeads: " + " | ".join(rd["leads"]))
TITLES = {"Q1": "Identification", "Q2": "What dual is", "Q3": "Field content", "Q4": "Coupling", "Q5": "Detection", "Q6": "Gravity",
          "Q7": "Dynamics", "Q8": "Monopoles", "Q9": "Polarization and vacuum", "Q10": "Dark energy", "Q11": "Priority", "Other": "Other findings"}
order = [f"Q{i}" for i in range(1, 12)] + ["Other"]
body = ["# The evidence by question\n\nBuilt by code from the nine readers and their verifiers (workflow A, 2026-11-06). Each answer is followed by its verifier's verdict; the verifier's correction governs where they differ. The record points, where a reader found the record contradicted or qualified, follow at the end."]
for q in order:
    if byq[q]: body.append(f"\n## {q}: {TITLES[q]}\n\n" + "\n".join(byq[q]))
body.append("\n## Record points: where the primary sources contradict or qualify the record\n\n" + "\n".join(rec))
(OUT / "by-question.md").write_text("\n".join(body), encoding="utf-8")
(OUT / "papers.md").write_text("# The papers each reader read\n" + "\n".join(papers), encoding="utf-8")
print({q: len(byq[q]) for q in order}, "record points", len(rec))
