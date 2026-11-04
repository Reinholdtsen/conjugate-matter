#!/usr/bin/env python3
"""run_openalex.py: send the OpenAlex queries of ../not-run-queries.json once each, with the check's own lit.py,
after OpenAlex's free daily budget has reset (00:00 UTC). Round 5 of the literature check.

  python3 run_openalex.py            check the budget, then run every query not yet answered, stop at the first 429
  python3 run_openalex.py --dry-run  print the lit.py commands only; send nothing
  python3 run_openalex.py --screen   (no network) screen the answered queries against ../known-ids.json

Before sending anything it reads the budget from the headers of a free single-work lookup (OpenAlex charges $0 for
/works/W...): if x-ratelimit-remaining-usd is 0 it prints the reset time and exits. A query counts as answered when
out/<ID>.txt starts with "OpenAlex: "; one that got 429 is not, and is sent once more after a reset. Each answered
query's results are read back from lit.py's cache (same URL, no second request) into out/<ID>.screen.tsv: one line
per work with KNOWN/new against findings.json and round3/known.json (by DOI, arXiv id or title)."""
import hashlib, json, os, re, subprocess, sys, urllib.parse, urllib.request

R5 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIT = os.path.join(os.path.dirname(R5), "tools", "lit.py")
CACHE = os.path.join(os.path.dirname(R5), "cache", "openalex")
SIZE_DEFAULT = 200
SIZES = {"Q21": 25}      # recorded size of the relevance (default-field) query; the others read up to 200 at once
SELECT = ("id,doi,title,publication_year,authorships,primary_location,cited_by_count,type,abstract_inverted_index,"
          "ids")


def field_of(q):
    f = q["field"].split(" ")[0]
    return {"default": "default", "fulltext": "fulltext", "title_and_abstract": "title_and_abstract"}[f]


def lit_args(q):
    size = SIZES.get(q["id"], SIZE_DEFAULT)
    return ["openalex", q["string"], "--field", field_of(q), "--size", str(size), "--abstracts"]


def lit_url(q):
    """The URL lit.py builds for this query (so its cached answer can be read back without a request)."""
    size = SIZES.get(q["id"], SIZE_DEFAULT)
    params = {"per-page": size, "select": SELECT}
    if field_of(q) == "default":
        params["search"] = q["string"]
    else:
        params["filter"] = f"{field_of(q)}.search:{q['string']}"
    return "https://api.openalex.org/works?" + urllib.parse.urlencode(params)


def budget():
    req = urllib.request.Request("https://api.openalex.org/works/W3153563614",
                                 headers={"User-Agent": "conjugate-matter-literature-check/1.0 (research script)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        h = {k.lower(): v for k, v in r.headers.items()}
    return float(h.get("x-ratelimit-remaining-usd", "0")), h.get("x-ratelimit-limit-usd"), int(h.get("x-ratelimit-reset", "0"))


def answered(qid):
    p = os.path.join(R5, "out", f"{qid}.txt")
    return os.path.exists(p) and open(p, encoding="utf-8").read().startswith("OpenAlex: ")


def screen(q):
    path = os.path.join(CACHE, hashlib.sha1(lit_url(q).encode()).hexdigest())
    if not os.path.exists(path):
        return None
    d = json.loads(json.load(open(path, encoding="utf-8"))["text"])
    known = json.load(open(os.path.join(R5, "known-ids.json")))
    ids, titles = set(known["ids"]), set(known["titles"])
    rows = []
    for w in d.get("results", []):
        doi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
        ax = ((w.get("ids") or {}).get("arxiv") or "").rsplit("/", 1)[-1]
        t = re.sub(r"[^a-z0-9]+", " ", (w.get("title") or "").lower()).strip()
        hit = ("doi:" + doi in ids) or (ax and "arxiv:" + re.sub(r"v\d+$", "", ax) in ids) or (t in titles)
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "-"
        rows.append(["KNOWN" if hit else "new", str(w.get("publication_year")), w.get("id", "").rsplit("/", 1)[-1],
                     doi or "-", ax or "-", w.get("type") or "-", src, (w.get("title") or "").replace("\t", " ")])
    out = os.path.join(R5, "out", f"{q['id']}.screen.tsv")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(f"# {q['id']} ({q['conjecture']}): {d['meta']['count']} works, {len(rows)} read\n")
        fh.write("\n".join("\t".join(r) for r in rows) + "\n")
    return d["meta"]["count"], len(rows), sum(r[0] == "new" for r in rows)


def main():
    qs = json.load(open(os.path.join(R5, "not-run-queries.json")))["openalex"]
    if "--dry-run" in sys.argv:
        for q in qs:
            print(q["id"], "python3", LIT, " ".join(repr(a) for a in lit_args(q)))
        return 0
    if "--screen" not in sys.argv:
        left, limit, reset = budget()
        print(f"OpenAlex free budget: {left} of {limit} USD left; resets in {reset} s")
        if left <= 0:
            print("Budget is used up: nothing sent.")
            return 1
        for q in qs:
            if answered(q["id"]):
                continue
            first = subprocess.run([os.path.join(R5, "scripts", "q.sh"), q["id"], *lit_args(q)],
                                   capture_output=True, text=True).stdout.strip()
            print(q["id"], first[:160])
            if "429" in first:
                print("OpenAlex answered 429: stopped. The remaining queries were not sent.")
                break
    for q in qs:
        if answered(q["id"]):
            print(q["id"], "screen:", screen(q))
    return 0


if __name__ == "__main__":
    sys.exit(main())
