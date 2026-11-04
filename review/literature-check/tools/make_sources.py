#!/usr/bin/env python3
"""Build review/literature-check/sources.json: metadata snapshots of every work the note cites, from INSPIRE
(CC0), the arXiv API (CC0 metadata) or Crossref (bibliographic fields only; Crossref abstracts are not stored).
Prints one reference line per work, built from the metadata alone, for the note's reference list.
Usage: make_sources.py KEY...   (arXiv id, recid:N or doi:...)
"""
import datetime
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lit  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(REPO, "review", "literature-check", "sources.json")


def cached_date(url, kind):
    p = os.path.join(lit.CACHE, kind, hashlib.sha1(url.encode()).hexdigest())
    return datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat() if os.path.exists(p) else None


def initials(name):
    if "," in name:
        last, first = [s.strip() for s in name.split(",", 1)]
    else:
        parts = name.split()
        last, first = parts[-1], " ".join(parts[:-1])
    ini = " ".join(re.sub(r"^(\w)\w*", r"\1.", w) if not w.endswith(".") else w for w in re.split(r"\s+", first) if w)
    ini = re.sub(r"(\w)\w*-(\w)\w*\.?", r"\1.-\2.", ini) if "-" in first else ini
    return f"{ini} {last}".strip()


def journal_line(meta):
    out = []
    for pub in meta.get("publication_info", []) or []:
        jt = re.sub(r"\.(?=[A-Z])", ". ", pub.get("journal_title", "") or "")
        vol, page, yr = pub.get("journal_volume", ""), pub.get("artid", "") or pub.get("page_start", ""), pub.get("year")
        if jt:
            out.append(" ".join(b for b in (jt, vol, page) if b) + (f" ({yr})" if yr else ""))
        elif pub.get("pubinfo_freetext"):
            out.append(pub["pubinfo_freetext"])
    return "; ".join(out)


def snapshot(key):
    meta = lit._resolve(key)
    if meta:
        path = (f"literature/{key[6:]}" if key.startswith("recid:") else
                f"doi/{key[4:]}" if key.startswith("doi:") else f"arxiv/{re.sub(r'v[0-9]+$', '', key)}")
        url = f"{lit.INSPIRE}/{path}" if not key.startswith("doi:") else None
        return {"key": key, "source": "INSPIRE", "recid": meta.get("control_number"),
                "api_url": f"https://inspirehep.net/api/literature/{meta.get('control_number')}",
                "retrieved": (cached_date(url, "inspire") if url else None) or "2026-11-02",
                "title": (meta.get("titles") or [{}])[0].get("title", ""),
                "authors": [a.get("full_name", "") for a in meta.get("authors", [])],
                "earliest_date": meta.get("earliest_date") or meta.get("preprint_date"),
                "journal": journal_line(meta), "dois": [d["value"] for d in meta.get("dois") or []],
                "arxiv": lit._arxiv(meta), "abstract": lit._abstract(meta)}
    if key.startswith("doi:"):
        w = lit.crossref_work(key)
        if w:
            raw = json.loads(lit.fetch(f"https://api.crossref.org/works/{key[4:]}", "crossref")[1])["message"]
            vp = " ".join(x for x in (raw.get("volume", ""), raw.get("article-number") or raw.get("page", "")) if x)
            w["container"] = f"{w['container']} {vp} ({w['year']})" if vp else w["container"]
            return {"key": key, "source": "Crossref", "api_url": f"https://api.crossref.org/works/{key[4:]}",
                    "retrieved": cached_date(f"https://api.crossref.org/works/{key[4:]}", "crossref") or "2026-11-02",
                    "title": w["title"], "authors": w["authors"], "earliest_date": str(w["year"]),
                    "journal": w["container"], "dois": [key[4:]], "arxiv": "", "abstract": ""}
        return None
    am = lit._arxiv_meta(key)
    if am:
        return {"key": key, "source": "arXiv API", "api_url": f"https://export.arxiv.org/api/query?id_list={key}",
                "retrieved": "2026-11-02", "title": am["title"], "authors": am["authors"], "earliest_date": am["year"],
                "journal": am["journal"], "dois": [am["doi"]] if am["doi"] else [], "arxiv": am["id"].split("v")[0],
                "abstract": am["abstract"]}
    return None


def ref_line(s):
    names = [initials(a) for a in s["authors"]]
    who = ", ".join(names) if len(names) <= 4 else f"{names[0]} et al. ({len(names)} authors)"
    bits = [who, f"\"{s['title']}\""]
    if s["journal"]:
        bits.append(s["journal"])
    bits.append(f"({(s['earliest_date'] or '')[:4]})" if not s["journal"] else "")
    tail = f"arXiv:{s['arxiv']}" if s["arxiv"] else (f"doi:{s['dois'][0]}" if s["dois"] else "")
    return ", ".join(b for b in bits if b) + (f", {tail}" if tail else "")


def main(keys):
    data = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    rc = 0
    for k in keys:
        s = snapshot(k)
        if s is None:
            print(f"!! {k}: no metadata")
            rc = 1
            continue
        data[k] = s
        print(f"{k}\t{s['earliest_date']}\t{ref_line(s)}")
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(data.items())), fh, indent=1, ensure_ascii=False)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
