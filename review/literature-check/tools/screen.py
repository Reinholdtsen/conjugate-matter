#!/usr/bin/env python3
"""screen.py — a systematic screen of the Born-reciprocity literature for the conjectures' subjects.

Collects every INSPIRE record that cites one of the anchor papers below (the lineage of Born reciprocity,
reciprocal relativity, metastring theory and Born geometry), then flags each record whose title or abstract
matches a conjecture's subject terms, and counts, per anchor and subject, the citing papers whose full text
matches (INSPIRE full-text search). Writes work/literature-check/screen.json and prints the flagged records.

    python3 work/literature-check/tools/screen.py
"""
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lit  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Anchors: (label, INSPIRE query that finds the anchor itself).
ANCHORS = [
    ("Born 1938", 't "suggestion for unifying quantum theory and relativity" and a Born'),
    ("Born 1949", 't "reciprocity theory of elementary particles" and a Born'),
    ("FLM 2013 Born reciprocity in string theory", 'arxiv:1307.7080'),
    ("FLM 2014 dynamical phase space", 'arxiv:1405.3949'),
    ("FLM 2015 metastring", 'arxiv:1502.08005'),
    ("FLM 2016 quantum spaces are modular", 'arxiv:1606.01829'),
    ("FRS 2017 generalised kinematics / Born geometry", 'arxiv:1706.07089'),
    ("FKGLM theory of metaparticles", 't metaparticles and a Freidel'),
    ("Low reciprocal relativity", 'a Low, Stephen G. and t reciprocal'),
    ("Bolognesi trans-Planckian 2012", 'arxiv:1207.5514'),
]

SUBJECTS = {
    "C1 dark matter": r"dark matter|dark sector|hidden sector|mirror matter",
    "C2/C3 monopoles": r"monopole|magnetic charge|dyon",
    "C4 magnetic duality": r"electric.magnetic|magnetic dual|s.duality|montonen",
    "C5 acceleration / dark energy": r"dark energy|cosmological constant|accelerat|vacuum energy",
    "C6/C7 clumping / velocity": r"clump|condensat|velocity.space|momentum.space (?:cluster|condens|clump|structure)|gated",
}
FULLTEXT = {
    "C1 dark matter": '"dark matter"',
    "C2/C3 monopoles": '"magnetic monopole"',
    "C5 acceleration / dark energy": '"dark energy"',
}


def anchor_recid(query):
    d = lit.inspire_json("literature?" + urllib.parse.urlencode({"q": query, "size": 5, "sort": "mostcited",
                                                               "fields": lit.FIELDS}))
    if not d or not d["hits"]["hits"]:
        return None, None
    m = d["hits"]["hits"][0]["metadata"]
    return m["control_number"], lit._line(m)


def citing(recid):
    out, page = [], 1
    while True:
        d = lit.inspire_json("literature?" + urllib.parse.urlencode(
            {"q": f"refersto:recid:{recid}", "size": 250, "page": page, "sort": "mostrecent", "fields": lit.FIELDS}))
        if not d:
            break
        hits = d["hits"]["hits"]
        out += [h["metadata"] for h in hits]
        if len(out) >= d["hits"]["total"] or not hits:
            break
        page += 1
    return out


def main():
    records, per_anchor, ft_counts = {}, {}, {}
    for label, q in ANCHORS:
        rid, line = anchor_recid(q)
        if rid is None:
            print(f"anchor not found: {label} ({q})")
            continue
        cits = citing(rid)
        per_anchor[label] = {"recid": rid, "anchor": line, "citing": len(cits)}
        print(f"{label}: recid {rid}, {len(cits)} citing — {line}")
        for m in cits:
            r = records.setdefault(m["control_number"], {"meta": m, "anchors": []})
            r["anchors"].append(label)
        for subj, phrase in FULLTEXT.items():
            d = lit.inspire_json("literature?" + urllib.parse.urlencode(
                {"q": f"refersto:recid:{rid} and fulltext {phrase}", "size": 1, "fields": "control_number"}))
            ft_counts.setdefault(label, {})[subj] = d["hits"]["total"] if d else None
    flagged = {s: [] for s in SUBJECTS}
    for rid, r in records.items():
        m = r["meta"]
        text = ((m.get("titles") or [{}])[0].get("title", "") + " " + lit._abstract(m)).lower()
        for s, pat in SUBJECTS.items():
            if re.search(pat, text):
                flagged[s].append({"recid": rid, "line": lit._line(m), "anchors": r["anchors"]})
    print(f"\n{len(records)} distinct citing records")
    for s, rows in flagged.items():
        print(f"\n== {s}: {len(rows)} flagged by title or abstract")
        for row in sorted(rows, key=lambda x: x["line"]):
            print("  " + row["line"][:230] + f"  <- {', '.join(row['anchors'])}")
    print("\nfull-text matches among citing papers, per anchor:")
    for a, c in ft_counts.items():
        print(f"  {a}: " + ", ".join(f"{k} {v}" for k, v in c.items()))
    with open(os.path.join(ROOT, "screen.json"), "w", encoding="utf-8") as fh:
        json.dump({"anchors": per_anchor, "distinct_citing": len(records), "fulltext_counts": ft_counts,
                   "flagged": flagged}, fh, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
