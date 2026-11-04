#!/usr/bin/env python3
"""recheck.py — re-check, by code, every identifier and quote the literature-check agents reported.

For each finding (searchers' findings and verifiers' new_findings) in work/literature-check/g*/search.json and
verify.json, or in a workflow result file given as the first argument:
  - resolve the identifier (INSPIRE, then arXiv, then Crossref) and compare its title, first author and year with
    the citation the agent wrote;
  - run the quote check of lit.py on every quote.
Writes work/literature-check/recheck.json and prints one line per finding plus a summary. Exit 1 if any check fails.

    python3 work/literature-check/tools/recheck.py [workflow-result.json]
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lit  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def findings_from(obj, group):
    out = []
    for f in obj.get("findings", []) or []:
        out.append(dict(f, group=group, source="search"))
    for f in obj.get("new_findings", []) or []:
        out.append(dict(f, group=group, source="verify"))
    return out


def load(argv):
    items = []
    if len(argv) > 1:
        data = json.load(open(argv[1], encoding="utf-8"))
        data = data.get("result", data)
        for g in data.get("groups", []):
            items += findings_from(g.get("search") or {}, g["key"]) + findings_from(g.get("verify") or {}, g["key"])
        return items
    for path in sorted(glob.glob(os.path.join(ROOT, "*", "search.json")) +
                       glob.glob(os.path.join(ROOT, "*", "verify.json"))):
        group = os.path.basename(os.path.dirname(path))
        try:
            items += findings_from(json.load(open(path, encoding="utf-8")), group)
        except (json.JSONDecodeError, OSError) as e:
            print(f"cannot read {path}: {e}")
    return items


def metadata(ident):
    """(title, authors, years, source) for an identifier, or None. years: every year the record carries
    (preprint, earliest, publication), since a citation may give either the preprint's or the journal's."""
    ident = ident.strip()
    m = lit._resolve(ident)
    if m:
        t = (m.get("titles") or [{}])[0].get("title", "")
        years = {lit._year(m)} | {str(p["year"]) for p in (m.get("publication_info") or []) if p.get("year")}
        years |= {m[k][:4] for k in ("earliest_date", "preprint_date") if m.get(k)}
        return t, [a.get("full_name", "") for a in m.get("authors", [])], years - {"?"}, "INSPIRE"
    if ident.startswith("doi:"):
        w = lit.crossref_work(ident)
        if w:
            return w["title"], w["authors"], {str(w["year"])}, "Crossref"
        return None
    if not ident.startswith("recid:"):
        a = lit._arxiv_meta(ident)
        if a:
            years = {a["year"]} | set(re.findall(r"\b(?:19|20)\d\d\b", a.get("journal", "")))
            return a["title"], a["authors"], years, "arXiv"
    return None


def surname(full):
    full = full.strip()
    if "," in full:
        return full.split(",")[0].strip()
    return full.split()[-1] if full.split() else full


def words(s):
    return set(re.findall(r"[a-z0-9]{3,}", lit.norm(re.sub(r"\$[^$]*\$", " ", s))))


def main(argv):
    items = load(argv)
    seen, rows, bad = set(), [], 0
    for f in items:
        ident = (f.get("id") or "").strip()
        key = (ident, f.get("conjecture"), f.get("source"))
        if key in seen:
            continue
        seen.add(key)
        row = {"group": f["group"], "source": f["source"], "conjecture": f.get("conjecture"), "id": ident,
               "relation": f.get("relation"), "citation": f.get("citation", "")}
        meta = metadata(ident) if ident else None
        if meta is None:
            row.update(resolved=False, problems=["identifier does not resolve"])
        else:
            title, authors, years, src = meta
            cit = f.get("citation", "")
            tw, cw = words(title), words(cit)
            overlap = len(tw & cw) / max(1, len(tw))
            first = surname(authors[0]) if authors else ""
            probs = []
            if overlap < 0.7:
                probs.append(f"title mismatch ({overlap:.0%} of title words in citation): {title!r}")
            if first and lit.norm(first) not in lit.norm(cit) and lit.loose(first) not in lit.loose(cit):
                probs.append(f"first author {first!r} not in citation")
            cited_years = set(re.findall(r"\b(?:18|19|20)\d\d\b", cit))
            if years and not (years & cited_years):
                probs.append(f"year: record has {sorted(years)}, citation has {sorted(cited_years) or 'none'}")
            row.update(resolved=True, meta_source=src, meta_title=title, meta_first_author=first,
                       meta_years=sorted(years), problems=probs)
        qres = []
        for q in f.get("quotes", []) or []:
            text = q.get("text", "")
            if not text.strip():
                continue
            verdict, where, _ = lit.check_quote(ident, text) if ident else ("NOT FOUND", "no id", "")
            qres.append({"text": text[:160], "verdict": verdict, "where": where, "agent_check": q.get("check", "")})
        row["quotes"] = qres
        nq = len(qres)
        nf = sum(1 for q in qres if q["verdict"].startswith("FOUND"))
        webfetch_only = sum(1 for q in qres if not q["verdict"].startswith("FOUND")
                            and "webfetch" in q["agent_check"].lower())
        row["quotes_found"] = f"{nf}/{nq}"
        row["quotes_webfetch_only"] = webfetch_only
        failed_quotes = nq - nf - webfetch_only
        ok = row.get("resolved") and not row["problems"] and failed_quotes == 0
        row["ok"] = bool(ok)
        bad += 0 if ok else 1
        rows.append(row)
        flag = "ok  " if ok else "FAIL"
        print(f"{flag} {row['group'][:22]:22s} {row['conjecture'] or '?':3s} {row['relation'] or '?':16s} "
              f"{ident[:28]:28s} quotes {row['quotes_found']}"
              + (f" (+{webfetch_only} WebFetch-only)" if webfetch_only else "")
              + ("" if ok else "  | " + "; ".join(row.get("problems", []))
                 + ("; " + ", ".join(q["text"][:60] + "… " + q["verdict"] for q in qres
                                     if not q["verdict"].startswith("FOUND")
                                     and "webfetch" not in q["agent_check"].lower()) if failed_quotes else "")))
    out = os.path.join(ROOT, "recheck.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1, ensure_ascii=False)
    print(f"\n{len(rows)} findings re-checked, {len(rows) - bad} clean, {bad} with problems; written to {out}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
