#!/usr/bin/env python3
"""verify/dual_sector.py — the gate's check of notes/dual-sector.md against its record, review/dual-sector/.

The dual-sector investigation (2026-11-06) read the papers of Djordje Minic and coauthors on dark matter as the dual
of visible matter, and compared them with P.R.'s conjectures. This script checks, offline, that the note says what
the record holds:

  A. Quotations. Every passage of three or more words in double quotes in the note's body is found again, either in a
     repository document other than the note and its record, or among the quotations of quotes.json. Each of those
     occurs in the note and in its stored source: the excerpt stored when code found it in an abstract, a full text or
     a text extracted from a downloaded PDF. Passages read only from the handwritten slides of a talk are counted, and
     the note must say they were read from the images. --online fetches the arXiv full texts again.
  B. Citations. Every entry of the note's reference list with an identifier matches its metadata snapshot in
     sources.json (INSPIRE, arXiv or Crossref): the authors' surnames (the first author's and the count, past four),
     the title and a year; and the entry's link points at that identifier.
  C. Dates. Each first-public date the note gives matches the snapshot or, for the talk, the record's event file;
     the papers the note counts as prior art precede the program's lab notebook (September 2026) and its restatement
     follows it; the 173 days from the talk to the arXiv posting are recomputed.
  D. Counts. The statements, verdicts and missed passages of workflow A, the judges' verdicts of workflow B, the
     agents and tokens of each workflow and the pre-registration's score are recomputed from the record, and each is
     found in the note as the note states it.
  E. Dependent texts. Every quotation on the wiki page wiki/dark-matter/conjugate-matter/dual-standard-model.md and in
     the flags this note proposes (review/wiki-build-flags.md, flag 64's addendum and flags 70-73) is found in the
     note, in a repository document or among the quotations of quotes.json.
  F. Algebra. The zero-mode commutators the note relies on for "twice the dimension" ([x, x~] = 2 pi i lambda^2,
     [x, p] = [x~, p~] = i hbar, the rest zero; Minic 2020 eq. 27) form a non-degenerate 4 x 4 bracket per dimension,
     against 2 x 2 for (x, p) at hbar: a doubled phase space.

  python3 verify/dual_sector.py            # offline, as the gate runs it
  python3 verify/dual_sector.py --online   # also fetches the arXiv full texts again (network; slow)

A pass confirms that the note matches its record and the record its stored sources. It does not test the agents'
judgments of how close a paper comes to a conjecture; the verifiers and the panel tested those.
"""
import datetime
import glob
import hashlib
import html
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REC = os.path.join(ROOT, "review", "dual-sector")
NOTE = os.path.join(ROOT, "notes", "dual-sector.md")
PAGE = os.path.join(ROOT, "wiki", "dark-matter", "conjugate-matter", "dual-standard-model.md")
FLAGS = os.path.join(ROOT, "review", "wiki-build-flags.md")
NOTEBOOK = "2026-09"  # notes/broken-born-theory.md: "Version 0.1, September 2026"

fails = []


def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        fails.append(name)


def norm(s):
    """As tools/lit.py normalizes: tags dropped, NFKC, quotation marks and dashes unified, whitespace collapsed."""
    s = re.sub(r"</?(?:i|b|em|strong|sub|sup|span|p|br|math|jats:[a-z]+)\b[^>]*>", "", s)
    s = unicodedata.normalize("NFKC", html.unescape(s))
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"),
                 ("—", "-"), ("−", "-"), (" ", " "), ("``", '"'), ("''", '"')):
        s = s.replace(a, b)
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def loose(s):
    """Letters and digits only, diacritics removed: for titles, which metadata and the note may punctuate apart."""
    s = "".join(c for c in unicodedata.normalize("NFKD", norm(s)) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s)


def load(name):
    with open(os.path.join(REC, name), encoding="utf-8") as fh:
        return json.load(fh)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def note_parts():
    text = read(NOTE)
    cut = text.find("\n## References")
    end = text.find("\n## Sources")
    return text, text[:cut], text[cut:end]


def spans(text):
    return [re.sub(r"\s+", " ", s).strip() for s in re.findall(r'"([^"]+)"', text, flags=re.S) if len(s.split()) >= 3]


def repo_texts():
    paths = (glob.glob(os.path.join(ROOT, "wiki", "papers", "*.md")) + glob.glob(os.path.join(ROOT, "notes", "*.md"))
             + glob.glob(os.path.join(ROOT, "popsci", "*.md"))
             + glob.glob(os.path.join(ROOT, "review", "**", "*.md"), recursive=True)
             + [os.path.join(ROOT, "HANDOFF.md"), os.path.join(ROOT, "CLAUDE.md")])
    out = {}
    for p in paths:
        ap = os.path.abspath(p)
        if ap == NOTE or ap.startswith(REC + os.sep):
            continue
        out[os.path.relpath(p, ROOT)] = norm(re.sub(r"\*\*?", "", read(p)))
    return out


# ---------------------------------------------------------------------------------------------------------------

def section_a(body, quotes, docs):
    print("A. Quotations")
    nbody = norm(body)
    qtexts = [norm(e["text"]) for e in quotes]
    missing = [s for s in spans(body) if not any(norm(s) in d for d in docs.values()) and norm(s) not in qtexts]
    check("every quoted passage of the note is in a repository document or in quotes.json", not missing,
          f"{len(spans(body))} passages; not found: {[m[:60] for m in missing]}")
    # A passage that a verified statement of a paper holds is a quotation from the literature: it must be checked
    # against its source (quotes.json), even where a flag or CLAUDE.md repeats it.
    held = [norm(x["quote"]) for x in load(os.path.join("panel", "statements.json"))]
    unchecked = [s for s in spans(body) if any(norm(s) in h for h in held) and norm(s) not in qtexts]
    check("every quotation from the literature is checked against its source in quotes.json", not unchecked,
          f"{[u[:60] for u in unchecked]}")
    absent = [e["text"][:60] for e in quotes if norm(e["text"]) not in nbody]
    check("every quotation of quotes.json occurs in the note", not absent, f"{len(quotes)} quotations; {absent}")
    bad = []
    for e in quotes:
        if e["source"] == "image":
            continue
        if norm(e["text"]) not in norm(e.get("excerpt", "")) and not e.get("excerpt_note"):
            bad.append(e["text"][:60])
    check("each quotation is in the excerpt stored when code found it", not bad, f"{bad}")
    images = [e for e in quotes if e["source"] == "image"]
    check("quotations read only from slide images are declared in the note",
          not images or "read them from the images" in norm(body), f"{len(images)} from slide images")
    kinds = {}
    for e in quotes:
        kinds[e["source"]] = kinds.get(e["source"], 0) + 1
    print(f"      quotations by source: {kinds}")


def surname(name):
    name = name.strip()
    last = name.split(",", 1)[0] if "," in name else name.split()[-1]
    return "".join(c for c in unicodedata.normalize("NFKD", last) if not unicodedata.combining(c)).lower()


def ident_of_url(url):
    for rx, key in ((r"^https://arxiv\.org/abs/([^\s?#]+?)(?:v\d+)?$", lambda m: m.group(1)),
                    (r"^https://doi\.org/(10\.[^\s?#]+)$", lambda m: "doi:" + m.group(1).lower()),
                    (r"^https://inspirehep\.net/literature/(\d+)$", lambda m: "recid:" + m.group(1))):
        m = re.match(rx, url)
        if m:
            return key(m)
    return None


def section_b(refs, sources):
    print("B. Citations")
    entries = [ln for ln in refs.splitlines() if ln.startswith("- ")]
    lower = {k.lower(): k for k in sources}
    for k, s in sources.items():  # a DOI link may point at a snapshot keyed by its INSPIRE record
        for d in s.get("dois") or []:
            lower.setdefault("doi:" + d.lower(), k)
    checked, problems = 0, []
    for ln in entries:
        links = re.findall(r"\]\((https://[^)\s]+)\)", ln)
        idents = [ident_of_url(u) for u in links]
        idents = [i for i in idents if i]
        if not idents:
            continue
        key = idents[0]
        k = lower.get(key.lower()) or lower.get(re.sub(r"^arxiv:", "", key, flags=re.I).lower())
        if k is None:
            problems.append(f"{key}: no snapshot")
            continue
        s = sources[k]
        fold = "".join(c for c in unicodedata.normalize("NFKD", ln) if not unicodedata.combining(c)).lower()
        names = [surname(a) for a in s["authors"]]
        if len(names) <= 4:
            miss = [n for n in names if n not in fold]
        else:
            miss = [n for n in names[:1] if n not in fold]
            if f"({len(names)} authors)" not in ln:
                miss.append(f"count {len(names)}")
        if miss:
            problems.append(f"{k}: authors {miss}")
        if loose(s["title"].replace("$", "").rstrip(" †")) not in loose(ln):
            problems.append(f"{k}: title")
        years = {str(s.get("earliest_date") or "")[:4]} | set(re.findall(r"\((\d{4})\)", s.get("journal") or ""))
        if not any(y and y in ln for y in years):
            problems.append(f"{k}: year {sorted(years)}")
        checked += 1
    check("every reference with an identifier matches its snapshot and links to it", not problems and checked >= 30,
          f"{checked} references checked; {problems}")


def section_c(text, sources, events):
    print("C. Dates")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    def words(iso):
        d = datetime.date.fromisoformat(iso)
        return f"{d.day} {months[d.month - 1]} {d.year}"

    for key, iso in (("2003.00318", "2020-02-29"), ("2010.15610", "2020-10-29"), ("2104.00802", "2021-04-01"),
                     ("1709.04388", "2017-09-13"), ("1801.00160", "2017-12-30"), ("2610.19522", "2026-10-14")):
        check(f"first public date of {key}", str(sources[key].get("earliest_date"))[:10] == iso
              and words(iso) in re.sub(r"\s+", " ", text), f"{words(iso)}")
    talk = events["belgrade_talk"]
    check("the date of the Belgrade talk is in the record and the note",
          talk["date"] == "2019-09-09" and words(talk["date"]) in re.sub(r"\s+", " ", text)
          and norm(talk["evidence_quote"]) in norm(read(os.path.join(REC, talk["evidence_file"]))),
          f"{talk['date']}; {talk['evidence_file']}")
    days = (datetime.date(2020, 2, 29) - datetime.date(2019, 9, 9)).days
    check("days from the talk to the arXiv posting", days == 173 and "173 days" in text, f"{days}")
    prior = [k for k in ("2003.00318", "2010.15610", "2109.12763", "2212.06086", "2307.16712", "2407.06207",
                         "2604.19418", "2104.00802", "1606.01829", "1405.3949", "1307.7080", "1502.08005",
                         "1812.10821", "1905.08269", "1709.04388", "1605.04361", "2503.20854")]
    late = [k for k in prior if str(sources[k].get("earliest_date"))[:7] >= NOTEBOOK]
    check("papers counted as prior art precede the lab notebook (September 2026)", not late, f"{len(prior)}; {late}")
    check("the restatement of October 2026 follows the lab notebook",
          str(sources["2610.19522"].get("earliest_date"))[:7] > NOTEBOOK, sources["2610.19522"].get("earliest_date"))


def section_d(text):
    print("D. Counts")
    flat = re.sub(r"\s+", " ", text)
    readers = sorted(p for p in glob.glob(os.path.join(REC, "readers", "r?-*.json")) if not p.endswith("-verify.json"))
    stmts = sum(len(x["statements"]) for p in readers for x in json.load(open(p, encoding="utf-8"))["papers"])
    verdicts = {"confirmed": 0, "confirmed-in-part": 0, "refuted": 0}
    missed = 0
    for p in readers:
        v = json.load(open(p.replace(".json", "-verify.json"), encoding="utf-8"))
        for s in v["statements"]:
            verdicts[s["verdict"]] += 1
        missed += len(v["missed"])
    check("readers and verifiers", len(readers) == 9, f"{len(readers)}")
    check("quoted statements of workflow A", f"returned {stmts} quoted statements" in flat, f"{stmts}")
    check("verifier verdicts", f"confirmed {verdicts['confirmed']} readings, corrected {verdicts['confirmed-in-part']} "
          f"in part and refuted {verdicts['refuted']}" in flat, f"{verdicts}")
    check("passages the verifiers added", f"added {missed} passages" in flat, f"{missed}")
    sweep = json.load(open(os.path.join(REC, "readers", "r9-sweep.json"), encoding="utf-8"))
    check("full texts of the mechanical sweep", f"sweep of {len(sweep['papers'])} full texts" in flat
          and f"None of the {len(sweep['papers'])} full texts swept" in flat, f"{len(sweep['papers'])}")
    usage = load(os.path.join("workflows", "usage.json"))
    for key, label in (("workflow_A", "Workflow A"), ("workflow_B", "workflow B")):
        u = usage[key]
        check(f"agents and tokens of {label}", f"{u['agents']} agents" in flat and f"{u['subagent_tokens']:,}" in flat,
              f"{u['agents']}, {u['subagent_tokens']:,}")
    if "round_2" in usage:
        u = usage["round_2"]
        check("agents and tokens of round 2", f"round 2, {u['agents']} agents, {u['subagent_tokens']:,} tokens" in flat,
              f"{u['agents']}, {u['subagent_tokens']:,}")
    check("tokens of the linking agent", f"{usage['links_agent']['subagent_tokens']:,} tokens" in flat)
    if "workflow_D" in usage:
        u = usage["workflow_D"]
        check("agents and tokens of the propagation", f"{u['agents']}\n  agents, {u['subagent_tokens']:,} tokens"
              in text or f"{u['agents']} agents, {u['subagent_tokens']:,} tokens" in flat, f"{u['agents']}, {u['subagent_tokens']:,}")
    if "workflow_E" in usage:
        u = usage["workflow_E"]
        check("agents and tokens of the review", f"{u['agents']} agents, {u['subagent_tokens']:,}" in flat
              or f"{u['agents']} agents, {u['subagent_tokens']:,}\n" in text, f"{u['agents']}, {u['subagent_tokens']:,}")
        fin = json.load(open(os.path.join(REC, "finish", "results.json"), encoding="utf-8"))
        n = sum(len(fin[k]["findings"]) for k in ("v-note", "v-wiki", "v-sweep"))
        check("findings of the three reviewers", f"They raised {n} findings" in flat, f"{n}")
    conf = json.load(open(os.path.join(REC, "round2", "s-conf.json"), encoding="utf-8"))["overall"]
    for n in ("90 full-text queries", "113 contributions", "3,288 attachment files", "19,740 records"):
        check(f"conference sweep: {n}", n in conf and n in flat)
    ref = json.load(open(os.path.join(REC, "round2", "v-winn-refute.json"), encoding="utf-8"))["overall"]
    check("Winn's quotations found again by the refuter", "All 72 quotations are found again" in ref
          and "found all 72 quotations again" in flat)
    judges = ["j-identity", "j-difference", "j-content", "j-overlap"]
    props = {}
    for j in judges:
        for p in json.load(open(os.path.join(REC, "panel", f"{j}.json"), encoding="utf-8"))["propositions"]:
            props.setdefault(p["id"][:2], []).append((p["verdict"], p["confidence"]))
    p1 = props["P1"]
    check("P1: holds with qualification, four of four, high", all(v == ("holds-with-qualification", "high") for v in p1),
          f"{p1}")
    check("P2: holds with qualification, four of four, high",
          all(v == ("holds-with-qualification", "high") for v in props["P2"]), f"{props['P2']}")
    check("P3: holds, four of four, high", all(v == ("holds", "high") for v in props["P3"]), f"{props['P3']}")
    p4 = props["P4"]
    check("P4: holds, three high and one medium", all(v[0] == "holds" for v in p4)
          and sorted(c for _, c in p4) == ["high", "high", "high", "medium"] and "(three high, one medium)" in flat,
          f"{p4}")
    path = os.path.join(REC, "preregistration.md")
    if not os.path.exists(path):
        check("the pre-registration is in the record", False, path)
        return
    pre = read(path)
    probs = [float(x) for x in re.findall(r"^- [A-E]\d \((0\.\d\d)\)", pre.split("## Score")[0], flags=re.M)]
    hits = len(re.findall(r"^- [A-E]\d \(0\.\d\d\): hit\.", pre, flags=re.M))
    misses = len(re.findall(r"^- [A-E]\d \(0\.\d\d\): MISS\.", pre, flags=re.M))
    check("pre-registration: predictions and their score", len(probs) == hits + misses == 14
          and hits == 10 and "Ten of fourteen predictions held" in flat, f"{hits} of {len(probs)}")
    check("pre-registration: the expected number of hits", f"{sum(probs):.2f}" == "10.25"
          and "probabilities was 10.25" in flat, f"{sum(probs):.2f}")


def section_e(body, quotes, docs):
    print("E. Dependent texts")
    known = list(docs.values()) + [norm(body)] + [norm(e["text"]) for e in quotes]
    if os.path.exists(PAGE):
        page = read(PAGE)
        page_body = page.split("\n---", 2)[-1]
        miss = [s for s in spans(page_body) if not any(norm(s) in k for k in known)]
        check("every quotation on the wiki page is in the record", not miss, f"{len(spans(page_body))}; {miss}")
    else:
        check("the wiki page exists", False, PAGE)
    flags = read(FLAGS)
    start = flags.find("## Found by the dual-sector investigation")
    add64 = re.search(r"\*\*Addendum \(2026-11-06, the dual-sector investigation\)[\s\S]*?(?=\n\d+\. \*\*|\n## )", flags)
    texts = ([flags[start:]] if start >= 0 else []) + ([add64.group(0)] if add64 else [])
    check("the flags' section and flag 64's addendum exist", start >= 0 and add64)
    docs_wo_flags = [v for k, v in docs.items() if not k.endswith("wiki-build-flags.md")]
    known = docs_wo_flags + [norm(body)] + [norm(e["text"]) for e in quotes]
    miss = [s for t in texts for s in spans(t) if not any(norm(s) in k for k in known)]
    check("every quotation of the flags is in the record", not miss, f"{sum(len(spans(t)) for t in texts)}; {miss}")


def section_f():
    print("F. Algebra")
    from fractions import Fraction
    # Variables per dimension: (x, x~, p, p~). Brackets /i of the zero-mode algebra, in units hbar = 1, with the
    # string length entering as c = 2 pi lambda^2 / hbar, taken rational here; the determinant is c-independent.
    for c in (Fraction(0), Fraction(1, 3), Fraction(7)):
        M = [[0, c, 1, 0], [-c, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]]
        det = determinant(M)
        check(f"zero-mode bracket per dimension is non-degenerate (2 pi lambda^2 / hbar = {c})", det == 1, f"det {det}")
    check("one phase space (x, p) at hbar has a 2 x 2 bracket", determinant([[0, 1], [-1, 0]]) == 1)


def determinant(M):
    M = [row[:] for row in M]
    n, det = len(M), 1
    from fractions import Fraction
    M = [[Fraction(v) for v in row] for row in M]
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None:
            return 0
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            det = -det
        det *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            M[r] = [a - f * b for a, b in zip(M[r], M[i])]
    return det


def online(quotes):
    print("online: fetching the arXiv full texts again")
    sys.path.insert(0, os.path.join(REC, "tools"))
    import tempfile
    import lit  # noqa: E402  the record's copy of the search tool, with its cache moved out of the repository
    lit.CACHE = tempfile.mkdtemp(prefix="dualsector-")  # it would cache copyrighted full texts beside itself
    for e in quotes:
        if e["source"] != "full text":
            continue
        verdict, where, _ = lit.check_quote(e["id"], e["text"])
        check(f"online: {e['id']}: {e['text'][:40]}", verdict.startswith("FOUND"), f"{verdict} in {where}")


def main(argv):
    text, body, refs = note_parts()
    quotes, sources, events = load("quotes.json"), load("sources.json"), load("events.json")
    docs = repo_texts()
    section_a(body, quotes, docs)
    section_b(refs, sources)
    section_c(text, sources, events)
    section_d(text)
    section_e(body, quotes, docs)
    section_f()
    if "--online" in argv:
        online(quotes)
    if fails:
        print(f"\ndual_sector FAILED: {len(fails)} check(s): {fails}")
        return 1
    print("\ndual_sector OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
