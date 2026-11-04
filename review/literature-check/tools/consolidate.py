#!/usr/bin/env python3
"""consolidate.py — merge every finding of the three rounds into one table, with the verified label of each.

Sources, in work/literature-check/:
  g*/search.json, g*/verify.json            workflow 1 (searchers; verifiers' verdicts and new findings)
  round2/r*.out.json, round2/r*.verify.json  workflow 2 (screen readers; verifiers of strong matches)
  round3/*.json, round3/*.verify.json        workflow 3 (coverage sweeps; verifiers of strong matches)

Rules:
  1. A verifier's verified_relation replaces the finder's label ("reject" drops the finding).
  2. A finding no second agent judged keeps its finder's label and is marked single-agent.
  3. One paper, one conjecture: entries are merged by INSPIRE recid (or DOI, or id). Where verified labels
     disagree, the weaker one is kept and the disagreement is recorded.
  4. A restatement is labeled no closer than its source: HARMONIZE lists the decisions, each with its reason.
Writes results.json and prints, per conjecture, the strongest surviving relation and the papers that carry it.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lit  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RANK = {"anticipates": 4, "partial": 3, "related": 2, "evidence-against": 1, "collision": 0}
VERDICT = {4: "anticipated", 3: "partly anticipated", 2: "related only", 1: "related only", 0: "nothing relevant"}

# (conjecture, key) -> (label, reason). Keys are normalized ids as produced by key_of().
HARMONIZE = {
    ("C5", "2111.05659"): ("related", "restates Berglund-Hübsch-Minić 2019 (dual-space curvature as Λ), which two "
                                      "verifiers label related for C5: static, no contraction or collapse"),
    ("C5", "2610.19522"): ("related", "same restatement of Berglund-Hübsch-Minić 2019 for C5; see 2111.05659"),
}

# The verdict panel's label disputes (panel/*.out.json), applied after the verifiers' verdicts. Each judge read the
# passages again; where two judges' disputes bear on parallel papers, they are treated alike.
PANEL = {
    ("C1", "2202.05104"): ("partial", "panel c1-advocate: the Snowmass paper says 'dual SM' for the dual spacetime of "
                                      "string theory, with no Born, momentum or conjugate wording on its own pages"),
    ("C1", "2202.06890"): ("partial", "a hedged restatement ('could be associated') with no momentum identification on its "
                                      "own pages, treated like 2202.05104 (panel c1-content proposed anticipates)"),
    ("C6", "1804.05857"): ("partial", "panel c6: halo dark matter Bose-condenses at the centre through its own gravity, "
                                      "the same form as Riotto-Tkachev 2000"),
    ("C2", "2509.21924"): ("related", "panel c2-c3-c7: reaches only #14's model and the minimal sector #11 §12 excludes"),
    ("C4", "physics/0401083"): ("related", "panel c4: electric-magnetic duality as an axiom, the word 'reciprocity' aside"),
    ("C5", "1307.0159"): ("related", "panel c5: the dual coordinates are read as extra dimensions; shares C5's wording "
                                     "and inverse scale factor, not its claim"),
}


def key_of(ident):
    ident = re.sub(r"^arxiv:", "", (ident or "").strip(), flags=re.I)
    ident = re.sub(r"v\d+$", "", ident)
    return ident


def resolve_key(ident):
    """A merge key: INSPIRE recid when the identifier resolves there, else the normalized id."""
    k = key_of(ident)
    m = lit._resolve(k) if k else None
    return f"recid:{m['control_number']}" if m else k.lower()


def load(path):
    try:
        return json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def main():
    entries = {}   # (conj, mkey) -> entry

    def add(f, source, stage):
        conj = f.get("conjecture")
        mk = resolve_key(f.get("id", ""))
        e = entries.setdefault((conj, mk), {"conjecture": conj, "key": mk, "ids": set(), "citation": f["citation"],
                                            "labels": [], "verified": [], "quotes": [], "summary": f.get("summary", ""),
                                            "difference": f.get("difference", ""), "sources": []})
        e["ids"].add(key_of(f.get("id", "")))
        e["labels"].append((f.get("relation"), source))
        e["sources"].append(f"{source}:{stage}")
        for q in f.get("quotes", []) or []:
            e["quotes"].append({"text": q.get("text", ""), "where": q.get("where", ""), "check": q.get("check", ""),
                                "id": f.get("id", "")})
        if len(f.get("summary", "")) > len(e["summary"]):
            e["summary"], e["difference"] = f.get("summary", ""), f.get("difference", "")

    def verdicts(vs, source):
        for v in vs or []:
            mk = resolve_key(v.get("id", ""))
            e = entries.get((v.get("conjecture"), mk))
            if e is None:
                # a verifier sometimes names the conjecture differently; match on paper alone if unique
                cands = [x for (c, k), x in entries.items() if k == mk]
                e = cands[0] if len(cands) == 1 else None
            if e is not None:
                e["verified"].append((v["verified_relation"], source, v.get("reason", "")[:400]))

    for p in sorted(glob.glob(os.path.join(ROOT, "g*", "search.json"))):
        g = os.path.basename(os.path.dirname(p))
        for f in (load(p) or {}).get("findings", []):
            add(f, g, "search")
    for p in sorted(glob.glob(os.path.join(ROOT, "g*", "verify.json"))):
        g = os.path.basename(os.path.dirname(p))
        d = load(p) or {}
        for f in d.get("new_findings", []):
            add(f, g, "verifier-new")
        verdicts(d.get("verdicts"), f"{g}:verifier")
    for p in sorted(glob.glob(os.path.join(ROOT, "round2", "r*.out.json")) +
                    [x for x in glob.glob(os.path.join(ROOT, "round3", "*.json"))
                     if not x.endswith(("known.json", ".verify.json"))]):
        name = os.path.basename(p).replace(".out.json", "").replace(".json", "")
        for f in (load(p) or {}).get("findings", []):
            add(f, name, "round")
    for p in sorted(glob.glob(os.path.join(ROOT, "round2", "*.verify.json")) +
                    glob.glob(os.path.join(ROOT, "round3", "*.verify.json"))):
        name = os.path.basename(p).replace(".verify.json", "")
        verdicts((load(p) or {}).get("verdicts"), f"{name}:verifier")

    rows = []
    for (conj, mk), e in entries.items():
        if e["verified"]:
            vals = [v for v, _, _ in e["verified"]]
            if "reject" in vals and all(v == "reject" for v in vals):
                final, basis = "reject", "verifier"
            else:
                live = [v for v in vals if v != "reject"]
                final = min(live, key=lambda r: RANK[r])
                basis = "verified" + (f" (verifiers disagree: {sorted(set(vals))}; weaker kept)"
                                      if len(set(vals)) > 1 else "")
        else:
            labs = [l for l, _ in e["labels"]]
            final = min(labs, key=lambda r: RANK[r])
            basis = "single-agent label" + (f" (finders disagree: {sorted(set(labs))}; weaker kept)"
                                            if len(set(labs)) > 1 else "")
        for ident in e["ids"]:
            h = HARMONIZE.get((conj, ident))
            if h and RANK.get(final, -1) > RANK[h[0]]:
                final, basis = h[0], f"harmonized: {h[1]}"
            pnl = PANEL.get((conj, ident))
            if pnl:
                final, basis = pnl[0], f"panel: {pnl[1]}"
        if final == "reject":
            continue
        rows.append({"conjecture": conj, "key": mk, "ids": sorted(e["ids"]), "citation": e["citation"],
                     "relation": final, "basis": basis, "labels": e["labels"], "verified": e["verified"],
                     "summary": e["summary"], "difference": e["difference"], "quotes": e["quotes"],
                     "sources": e["sources"]})
    rows.sort(key=lambda r: (r["conjecture"], -RANK[r["relation"]], r["citation"]))
    with open(os.path.join(ROOT, "results.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1, ensure_ascii=False)
    print(f"{len(rows)} findings after merging (rejected ones dropped); written to results.json\n")
    for c in ["C1", "C2", "C3", "C4", "C5", "C6", "C7"]:
        rs = [r for r in rows if r["conjecture"] == c]
        top = max((RANK[r["relation"]] for r in rs), default=0)
        counts = {k: sum(1 for r in rs if r["relation"] == k) for k in RANK}
        print(f"== {c}: verdict {VERDICT[top]}   " + ", ".join(f"{k} {v}" for k, v in counts.items() if v))
        for r in rs:
            if RANK[r["relation"]] >= 3:
                print(f"   [{r['relation']}] {r['ids'][0]} — {r['citation'][:150]}  <{r['basis'][:90]}>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
