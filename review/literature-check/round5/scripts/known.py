#!/usr/bin/env python3
"""known.py: build the set of identifiers the literature check already assessed (findings.json, round3/known.json)
and, for screening, tell whether an identifier or title occurs anywhere in the record (review/literature-check/),
round 5's raw outputs (out/) and query log (queries.tsv) excepted.
Usage: known.py build            -> writes ../known-ids.json
       known.py check ID|TITLE ... -> for each: in findings/known? mentioned anywhere in the record?"""
import json, os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
REC = os.path.join(ROOT, "review", "literature-check")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "known-ids.json")
RAW = (os.path.join(REC, "round5", "out") + os.sep, os.path.join(REC, "round5", "queries.tsv"))

def ids_in(text):
    out = set()
    for m in re.finditer(r"10\.\d{4,9}/[^\s\"'<>,;)\]]+", text):
        out.add("doi:" + m.group(0).rstrip(".").lower())
    for m in re.finditer(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d])", text):
        out.add("arxiv:" + m.group(1))
    for m in re.finditer(r"\b([a-z-]+(?:\.[A-Z]{2})?/\d{7})\b", text):
        out.add("arxiv:" + m.group(1))
    for m in re.finditer(r"recid:(\d+)", text):
        out.add("recid:" + m.group(1))
    for m in re.finditer(r"\bW\d{8,11}\b", text):
        out.add("openalex:" + m.group(0))
    return out

def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()

def build():
    known, titles = set(), []
    for f in json.load(open(os.path.join(REC, "findings.json"))):
        blob = json.dumps(f, ensure_ascii=False)
        known |= ids_in(f.get("key", "") + " " + " ".join(f.get("ids", [])) + " " + f.get("citation", ""))
        m = re.search(r"\"([^\"]{12,})\"", f.get("citation", ""))
        if m:
            titles.append(norm_title(m.group(1)))
    for p in json.load(open(os.path.join(REC, "round3", "known.json")))["papers"]:
        known |= ids_in(p.get("id", "") + " " + p.get("citation", ""))
        m = re.search(r"\"([^\"]{12,})", p.get("citation", ""))
        if m:
            titles.append(norm_title(m.group(1)))
    json.dump({"ids": sorted(known), "titles": sorted(set(titles))}, open(OUT, "w"), indent=0)
    print(f"{len(known)} identifiers, {len(set(titles))} titles -> {OUT}")

def record_text():
    parts = []
    for f in glob.glob(os.path.join(REC, "**", "*"), recursive=True):
        if os.path.isfile(f) and not f.endswith((".py", ".js")) and not f.startswith(RAW):
            try:
                parts.append(open(f, encoding="utf-8", errors="replace").read())
            except OSError:
                pass
    return "\n".join(parts).lower()

def check(args):
    k = json.load(open(OUT))
    ids, titles = set(k["ids"]), k["titles"]
    rec = record_text()
    for a in args:
        a_l = a.strip().lower()
        idset = ids_in(a) if re.search(r"10\.\d|\d{4}\.\d{4}|recid:|/\d{7}|\bW\d{8}", a) else set()
        in_known = bool(idset & ids) if idset else any(norm_title(a)[:60] in t or t[:60] in norm_title(a) for t in titles if len(t) > 15)
        if idset:
            bare = [i.split(":", 1)[1] for i in idset]
            anywhere = any(b.lower() in rec for b in bare)
        else:
            anywhere = norm_title(a)[:50] in re.sub(r"[^a-z0-9]+", " ", rec)
        print(f"{'KNOWN' if in_known else 'new  '} | {'in record' if anywhere else 'not in record'} | {a}")

if __name__ == "__main__":
    if sys.argv[1] == "build":
        build()
    else:
        check(sys.argv[2:])
