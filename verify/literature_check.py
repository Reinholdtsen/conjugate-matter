#!/usr/bin/env python3
"""verify/literature_check.py — the gate's check of notes/literature-check.md against its record.

The literature check of P.R.'s conjectures (2026-11-02) left a record in review/literature-check/. This script
checks that the note says what that record holds, offline:

  A. Verdicts. Each conjecture's verdict is recomputed from findings.json by the pre-registered rule (the
     strongest relation that survives verification), with the count of findings by relation, and compared with
     the note's two tables. Each verdict must rest on at least one finding a second agent confirmed.
  B. Counts. The findings, the records citing the screen's ten anchors, the records read in round 2, the panel's
     label changes, the code check's unresolved identifiers, flagged findings and quotations read only by web
     fetch, the agents and tokens the workflow tool reported, and the verdicts of the two reviews of the write-up
     and of the check of the merges and the last sweep:
     each recomputed from the record, and each found in the note's prose as the note states it.
  C. Quotations. Every passage of three or more words in double quotes in the note's body is found again, either
     in a repository document or among the quotations of quotes.json. Each of those is in the note and in its
     source: the stored abstract (sources.json; INSPIRE and arXiv metadata are CC0) or, for a full text, the
     excerpt stored when the quotation was found by code. Full texts are not stored; --online re-fetches them.
  D. Citations. Every reference with an identifier matches its metadata snapshot: each author's surname and the
     number of authors, the title, the year, and the volume and page.
  E. The pre-registration. Its predicted verdicts against the recomputed ones.
  F. Flags 64–69 in review/wiki-build-flags.md: each quotation is found in a repository document or in quotes.json.
  G. The algebra behind flag 66 (note §6), after the C5 panel judge's script (review/literature-check/checks/). The
     program's rule (#1 §6: the conjugate energy E = ρ̃ã³ enters our constraint as E/a³, ã = 1/a) gives
     w_eff = −w̃ through our own continuity equation. Gasperini and Veneziano's scale-factor duality with sources
     (Phys. Rept. 373, 1 (2003), §2.2, eqs. 2.27–2.32; d = 3) gives the same density and pressure; within it no
     de Sitter universe has a source with p = −ρ, the partner of a stiff source, and the power law with a stiff
     source, a ∝ t^(1/2), goes to a ∝ t^(−1/2), both with ρ̄ < 0 by eq. 2.27 (ρ̄ > 0 needs 3γ² < 1). In Einstein
     gravity the map takes no flat Friedmann solution to another; inverting a between single-fluid solutions at
     shared cosmic time gives w → −2 − w (the phantom duality, the program's superseded heuristic), at shared
     conformal time w → −2/3 − w. In Mukherjee, Jassal and Lochan's Brans–Dicke pairing (2024, §6, eqs. 46–47)
     d ln ã/d ln a = −1/2, not −1, with stiff contracting contents. Under the three maps the conjugate content that
     acts on ours as Λ is stiff, Λ itself and radiation. The anchors are the published equations, not the program's
     results.

  python3 verify/literature_check.py            # offline, as the gate runs it
  python3 verify/literature_check.py --online   # also re-fetches every source (network; slow)

A pass confirms that the note matches its record and the record its stored sources, and in section G the algebra
behind flag 66. It does not test the agents' judgments of how close a paper comes to a conjecture; the verifiers
and the panel tested those. Section G confirms arithmetic, not the program's use of the map in Einstein gravity.
"""
import glob
import hashlib
import html
import json
import os
import re
import sys
import tempfile
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REC = os.path.join(ROOT, "review", "literature-check")
NOTE = os.path.join(ROOT, "notes", "literature-check.md")

CONJ = ["C1", "C2", "C3", "C4", "C5", "C6", "C7"]
RELATIONS = ["anticipates", "partial", "related", "evidence-against", "collision"]
RANK = {"anticipates": 4, "partial": 3, "related": 2, "evidence-against": 1, "collision": 0}
VERDICT = {4: "anticipated", 3: "partly anticipated", 2: "related only", 1: "related only", 0: "nothing relevant"}

# The numbers the note states, each recomputed below.
EXPECT = {"findings": 287, "screened": 498, "round2": 143, "panel_changes": 5, "agents": 31, "tokens_M": 11.2,
          "prereg_hits": 4, "unresolved": 8, "webfetch_only": 6, "recheck_problems": 23,
          # the two reviews of the write-up (note §11): verdicts, confirmed, confirmed in part, refuted
          "review1": (56, 41, 15, 0), "review2": (71, 64, 7, 0), "review2_findings": (23, 25, 23),
          "review3": (47, 43, 4, 0),  # the check of the merges
          "review4": (14, 13, 1, 0)}  # the last sweep
# Findings that carry a verdict and were judged by their finder alone, as the note lists them.
SINGLE_AGENT = {("C1", "2305.12593"), ("C3", "doi:10.1063/PT.3.3571"), ("C5", "hep-th/9309023"),
                ("C6", "astro-ph/0003388")}

fails = []


def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        fails.append(name)


def norm(s):
    """Lower case, Unicode-normalized, without quotation marks, apostrophes or Markdown emphasis."""
    s = re.sub(r"</?(?:i|b|em|strong|sub|sup|span|p|br|math|jats:[a-z]+)\b[^>]*>", "", s)
    s = unicodedata.normalize("NFKC", html.unescape(s))
    for a, b in (("–", "-"), ("—", "-"), ("−", "-"), (" ", " ")):
        s = s.replace(a, b)
    s = re.sub(r"[\"'“”‘’`*_]", "", s)
    s = re.sub(r"-\s+", "-", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def loose(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", norm(s)) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.replace("ł", "l").replace("ø", "o").replace("đ", "d"))


def load(name):
    with open(os.path.join(REC, name), encoding="utf-8") as fh:
        return json.load(fh)


def note_parts():
    text = open(NOTE, encoding="utf-8").read()
    body, _, rest = text.partition("\n## References")
    refs = rest.partition("\n## Sources")[0]
    return text, body, refs


def table_rows(body, header_start):
    """Rows of the Markdown table whose header line starts with header_start, as lists of cells."""
    lines = body.splitlines()
    i = next(k for k, line in enumerate(lines) if line.startswith(header_start))
    rows = []
    for line in lines[i + 2:]:
        if not line.startswith("|"):
            break
        rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def recompute(findings):
    out = {}
    for c in CONJ:
        rs = [f for f in findings if f["conjecture"] == c]
        top = max(RANK[f["relation"]] for f in rs)
        out[c] = {"verdict": VERDICT[top], "n": len(rs),
                  "counts": [sum(1 for f in rs if f["relation"] == r) for r in RELATIONS],
                  "top": [f for f in rs if RANK[f["relation"]] == top]}
    return out


def section_a(findings, body):
    print("A. Verdicts recomputed from findings.json")
    v = recompute(findings)
    verdicts = {r[0]: r[2] for r in table_rows(body, "| | Conjecture | Verdict")}
    counts = {r[0]: [int(x) for x in r[1:]] for r in table_rows(body, "| | Findings |")}
    for c in CONJ:
        print(f"     {c}: {v[c]['verdict']:19s} {v[c]['n']:3d} findings; " +
              ", ".join(f"{r} {n}" for r, n in zip(RELATIONS, v[c]["counts"]) if n))
        check(f"{c} verdict in the note", verdicts.get(c) == v[c]["verdict"], f"note: {verdicts.get(c)}")
        check(f"{c} counts in the note", counts.get(c) == [v[c]["n"]] + v[c]["counts"], f"note: {counts.get(c)}")
        confirmed = [f for f in v[c]["top"] if f["basis"].startswith(("verified", "panel"))]
        check(f"{c} verdict rests on a confirmed finding", bool(confirmed), f"{len(confirmed)} of {len(v[c]['top'])}")
    single = {(f["conjecture"], f["ids"][0]) for f in findings
              if f["relation"] in ("anticipates", "partial", "evidence-against") and f["basis"].startswith("single-agent")}
    check("single-agent findings that carry a verdict", single == SINGLE_AGENT, f"{sorted(single)}")
    return v


def section_b(findings, body):
    print("B. Counts")
    check("findings after merging", len(findings) == EXPECT["findings"], f"{len(findings)}")
    screen = load("screen/screen.json")
    check("records citing the ten anchors", screen["distinct_citing"] == EXPECT["screened"],
          f"{screen['distinct_citing']} from {len(screen['anchors'])} anchors")
    check("anchors of the citation screen", len(screen["anchors"]) == 10, f"{len(screen['anchors'])}")
    read = set()
    for p in glob.glob(os.path.join(REC, "round2", "r*.input.json")):
        read |= {x["recid"] for x in json.load(open(p, encoding="utf-8"))["items"]}
    check("distinct records read in round 2", len(read) == EXPECT["round2"], f"{len(read)}")
    def before_panel(f):
        live = [v[0] for v in f["verified"] if v[0] != "reject"]
        return min(live or [label for label, _ in f["labels"]], key=lambda r: RANK[r])
    changed = sum(1 for f in findings if f["basis"].startswith("panel:") and before_panel(f) != f["relation"])
    check("labels the panel changed", changed == EXPECT["panel_changes"], f"{changed}")
    recheck = load("recheck.json")
    carries = {(f["conjecture"], i.lower()) for f in findings
               if f["relation"] in ("anticipates", "partial", "evidence-against") for i in f["ids"]}

    def carries_verdict(r):
        return (r["conjecture"], re.sub(r"^arxiv:", "", r["id"], flags=re.I).lower()) in carries
    missed = [(r["id"], q) for r in recheck if carries_verdict(r) for q in r["quotes"]
              if not q["verdict"].startswith("FOUND")]
    web = [i for i, q in missed if "webfetch" in q["agent_check"].lower()]
    check("quotations in findings that carry a verdict, read only by web fetch",
          len(missed) == len(web) == EXPECT["webfetch_only"], f"{len(web)} from {sorted(set(web))}")
    unresolved = [r for r in recheck if not r.get("resolved")]
    check("identifiers that did not resolve, none in a finding that carries a verdict",
          len(unresolved) == EXPECT["unresolved"] and not any(carries_verdict(r) for r in unresolved),
          f"{len(unresolved)}")
    flagged = sum(1 for r in recheck if not r["ok"])
    check("findings the code check flagged", flagged == EXPECT["recheck_problems"], f"{flagged} of {len(recheck)}")
    agents = tokens = 0
    for n in range(1, 5):
        w = load(f"workflows/workflow{n}-result.json")
        agents += w["agentCount"]
        tokens += w["totalTokens"]
        print(f"     workflow {n}: {w['agentCount']} agents, {w['totalTokens']:,} tokens")
    check("agents in the four workflows", agents == EXPECT["agents"], f"{agents}")
    check("tokens, in millions", round(tokens / 1e6, 1) == EXPECT["tokens_M"], f"{tokens:,} = {tokens / 1e6:.2f}M")

    def tally(results):
        v = [r["verdict"] for r in results]
        return (len(v), v.count("confirmed"), v.count("partly"), len(v) - v.count("confirmed") - v.count("partly"))
    first = tally([r for g in load("workflows/workflow5-result.json")["verifications"] for r in g["results"]])
    check("the first review's verdicts: all, confirmed, in part, other", first == EXPECT["review1"], f"{first}")
    rounds = load("workflows/workflow7-result.json")["rounds"]
    second = tally([r for x in rounds for r in x["verdicts"]["results"]])
    found = tuple(len(x["review"]["findings"]) for x in rounds)
    check("the second review's verdicts: all, confirmed, in part, other", second == EXPECT["review2"], f"{second}")
    check("the second review's findings by reviewer", found == EXPECT["review2_findings"],
          ", ".join(f"{x['lens']} {n}" for x, n in zip(rounds, found)))
    merges = load("workflows/workflow8-result.json")["rounds"]
    third = tally([r for x in merges for r in x["verdicts"]["results"]])
    check("the check of the merges: verdicts all, confirmed, in part, other", third == EXPECT["review3"], f"{third}")
    fourth = tally(load("workflows/workflow9-result.json")["verdicts"]["results"])
    check("the last sweep: verdicts all, confirmed, in part, other", fourth == EXPECT["review4"], f"{fourth}")
    # The same counts as the note's prose states them, so that a count changed in the note fails too.
    say = dict(enumerate("zero one two three four five six seven eight nine ten eleven twelve".split()))
    r1, r2, f2, r3, r4 = (EXPECT["review1"], EXPECT["review2"], EXPECT["review2_findings"], EXPECT["review3"],
                          EXPECT["review4"])
    stated = [f"The result is {EXPECT['findings']} findings", f"{EXPECT['screened']} distinct records",
              f"one of {say[len(screen['anchors'])]} anchors", f"the {EXPECT['round2']} flagged records",
              f"{say[EXPECT['unresolved']]} of the {EXPECT['findings']} did not resolve",
              f"flagged {EXPECT['recheck_problems']} of the {EXPECT['findings']} findings",
              f"except {say[EXPECT['webfetch_only']]} from two sources", f"{say[EXPECT['panel_changes']]} were applied",
              f"{EXPECT['agents']} agents in four workflows", f"{EXPECT['tokens_M']} million tokens",
              f"{say[EXPECT['prereg_hits']]} of seven predicted verdicts were right",
              f"of the {r1[0]} verdicts", f"{r1[1]} confirmed and {r1[2]} confirmed in part",
              f"{r2[1]} were confirmed and {r2[2]} confirmed in part",
              f"({f2[0]} findings), one the wiki ({f2[1]}), and one what was missing or unverified ({f2[2]})",
              f"{r3[0]} findings, none refuted, {r3[1]} confirmed and {r3[2]} confirmed in part",
              f"{r4[0]} findings, none refuted, {r4[1]} confirmed and {r4[2]} confirmed in part"]
    nbody = norm(body)
    for phrase in stated:
        check(f"the note states: {phrase}", norm(phrase) in nbody)


def repo_texts():
    paths = (glob.glob(os.path.join(ROOT, "papers", "*.md")) + glob.glob(os.path.join(ROOT, "notes", "*.md")) +
             glob.glob(os.path.join(ROOT, "popsci", "*.md")) + glob.glob(os.path.join(ROOT, "review", "**", "*.md"),
                                                                    recursive=True) +
             [os.path.join(ROOT, "HANDOFF.md"), os.path.join(ROOT, "CLAUDE.md")])
    out = {}
    for p in paths:
        if os.path.abspath(p) == NOTE or os.path.abspath(p).startswith(REC + os.sep):
            continue
        out[os.path.relpath(p, ROOT)] = norm(open(p, encoding="utf-8").read())
    return out


def section_c(body, quotes, sources):
    print("C. Quotations")
    # The flags file copies the note's quotations from the literature, so it is no source for them.
    docs = {k: v for k, v in repo_texts().items() if k != os.path.join("review", "wiki-build-flags.md")}
    lit = [(q, norm(q["text"]), loose(q["text"])) for q in quotes]
    titles = [norm(s["title"]) for s in sources.values()]
    spans = [s for s in re.findall(r'"([^"]+)"', body, flags=re.S) if len(s.split()) >= 3]
    nbody = norm(body)
    n_repo = n_lit = 0
    for s in spans:
        ns = norm(s)
        if any(ns in nq for _, nq, _ in lit) or any(ns == t for t in titles):
            n_lit += 1
        elif any(ns in d for d in docs.values()):
            n_repo += 1
        else:
            check(f"quotation found nowhere: \"{' '.join(s.split())[:70]}\"", False)
    print(f"     {len(spans)} quoted passages: {n_lit} from the literature, {n_repo} from repository documents")
    found = loose_found = 0
    for q, nq, lq in lit:
        src = sources.get(q["id"])
        check(f"quotation's source in sources.json: {q['id']}", src is not None)
        check(f"quotation in the note: {q['id']} \"{q['text'][:50]}\"", nq in nbody)
        text = src["abstract"] if (src and q["source"] == "abstract") else q.get("excerpt", "")
        if nq in norm(text):
            found += 1
        elif lq and lq in loose(text):
            loose_found += 1
        else:
            check(f"quotation in its stored {q['source']}: {q['id']} \"{q['text'][:50]}\"", False)
    n_abs = sum(1 for q in quotes if q["source"] == "abstract")
    check("quotations found in their stored sources", found + loose_found == len(quotes),
          f"{found} exact, {loose_found} loose; {n_abs} in abstracts, {len(quotes) - n_abs} in full-text excerpts")


def words(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", norm(s)) if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+", s)


SURNAME_RE = re.compile(r"(?:[A-Z]\.(?:-[A-Z]\.)?\s+)+(.+)")


def surname(name):
    name = name.strip()
    if "," in name:
        return name.split(",")[0]
    m = SURNAME_RE.match(name)
    return m.group(1) if m else name.split()[-1]


def section_d(refs, sources):
    print("D. Citations against their metadata snapshots")
    by_doi = {d.lower(): k for k, s in sources.items() for d in s.get("dois", [])}
    n = 0
    for line in [x[2:] for x in refs.splitlines() if x.startswith("- ")]:
        m = re.search(r"arXiv:(\S+?)(?:,|$)", line) or re.search(r"doi:(\S+?)(?:,|$)", line)
        oa = re.search(r"OpenAlex (W\d+)", line)
        if oa:
            key = f"openalex:{oa.group(1)}"
        elif m and line[m.start():].startswith("arXiv"):
            key = m.group(1)
        elif m:
            key = by_doi.get(m.group(1).lower()) or f"doi:{m.group(1)}"
        else:
            check(f"reference without an identifier: {line[:60]}", False)
            continue
        s = sources.get(key)
        if s is None:
            check(f"reference has no metadata snapshot: {key}", False)
            continue
        n += 1
        who, title = line.split(', "', 1)[0], line.split('"')[1]
        meta = [loose(surname(a)) for a in s["authors"]]
        m_n = re.search(r"et al\. \((\d+) authors\)", who)
        if m_n:
            ok = loose(surname(who.split(" et al.")[0])) == meta[0] and int(m_n.group(1)) == len(meta)
        else:
            names = [loose(surname(x)) for x in who.split(", ")]
            ok = names == meta
        check(f"{key}: authors", ok, "" if ok else f"note {who[:60]!r}; metadata {s['authors'][:6]}")
        tw, mw = set(words(title)), set(words(s["title"]))
        jac = len(tw & mw) / max(1, len(tw | mw))
        check(f"{key}: title", jac >= 0.7, f"word overlap {jac:.2f}" if jac < 0.7 else "")
        year = re.findall(r"\((\d{4})\)", line)
        years = set(re.findall(r"\((\d{4})\)", s["journal"])) | {str(s["earliest_date"] or "")[:4]}
        check(f"{key}: year", bool(year) and year[-1] in years, f"note {year}; metadata {sorted(years)}")
        jn = re.search(r'",\s*([^,]*?\d[^,]*?),\s*([A-Za-z]?\d+)\s*\((\d{4})\)', line)
        if jn and re.search(r"\d", s["journal"]):
            vol = re.findall(r"\d+", jn.group(1))[-1]
            check(f"{key}: volume and page", vol in s["journal"] and jn.group(2) in s["journal"],
                  f"note {vol} {jn.group(2)}; metadata {s['journal']}")
    print(f"     {n} references checked against INSPIRE, arXiv, Crossref or OpenAlex snapshots")


def section_e(v):
    print("E. The pre-registration, scored")
    text = open(os.path.join(REC, "preregistration.md"), encoding="utf-8").read()
    hits = 0
    for c in CONJ:
        row = next(line for line in text.splitlines() if line.startswith(f"| {c} |"))
        pred = re.split(r"\s*[;(]", row.split("|")[3].strip())[0]
        options = {o.strip().replace("nothing", "nothing relevant").replace("relevant relevant", "relevant")
                   for o in pred.split(" or ")}
        if "related only or nothing" in pred:
            options = {"related only", "nothing relevant"}
        hit = v[c]["verdict"] in options
        hits += hit
        print(f"     {c}: predicted {pred!r}, found {v[c]['verdict']!r}: {'hit' if hit else 'miss'}")
    check("predicted verdicts that held", hits == EXPECT["prereg_hits"], f"{hits} of {len(CONJ)}")


def online(quotes, sources):
    """Re-fetch every source and find each quotation again (network)."""
    sys.path.insert(0, os.path.join(REC, "tools"))
    import lit  # noqa: E402  the check's own tool, with its cache moved out of the repository
    lit.CACHE = tempfile.mkdtemp(prefix="litcheck-")
    print("Online: re-fetching sources")
    for q in quotes:
        page = re.search(r"https://web\.archive\.org/[^\s;,]+", sources.get(q["id"], {}).get("abstract_source", ""))
        if q["id"].startswith("openalex:") and page:
            # Khademi 2009 (round 5): lit.py has no route to this abstract; fetch the archived page sources.json names.
            status, text = lit.fetch(page.group(0), "wayback")
            ok = status == 200 and norm(q["text"]) in norm(html.unescape(re.sub(r"<[^>]+>", " ", text)))
            check(f"online {q['id']}: \"{q['text'][:50]}\"", ok, f"{'FOUND' if ok else 'NOT FOUND'} in {page.group(0)}")
            continue
        verdict, where, _ = lit.check_quote(q["id"], q["text"])
        check(f"online {q['id']}: \"{q['text'][:50]}\"", verdict.startswith("FOUND"), f"{verdict} in {where}")
        if q["source"] == "full text" and verdict.startswith("FOUND"):
            url, text, _ = lit.fulltext(sources[q["id"]].get("arxiv") or q["id"])
            if url and hashlib.sha256(norm(text).encode()).hexdigest() != q.get("sha256"):
                print(f"     note: the full text of {q['id']} has changed since the check")


def section_f(quotes):
    print("F. Quotations in flags 64–69 (review/wiki-build-flags.md)")
    path = os.path.join(ROOT, "review", "wiki-build-flags.md")
    text = open(path, encoding="utf-8").read()
    part = text.split("## Found by the literature check")[1].split("The executed checks referred to above")[0]
    docs = {k: v for k, v in repo_texts().items() if k != os.path.relpath(path, ROOT)}
    lit = [norm(q["text"]) for q in quotes]
    spans = [s for s in re.findall(r'"([^"]+)"', part, flags=re.S) if len(s.split()) >= 3]
    for s in spans:
        ns = norm(s)
        check(f"flag quotation: \"{' '.join(s.split())[:60]}\"", any(ns in d for d in docs.values()) or any(ns in q for q in lit))
    print(f"     {len(spans)} quoted passages")


def section_g():
    """The algebra behind flag 66, after the C5 panel judge's script (review/literature-check/checks/)."""
    print("G. The algebra behind flag 66: the duality dictionary as scale-factor duality with sources")
    import sympy as sp

    t = sp.symbols("t", positive=True)
    wt, w, C = sp.symbols("wt w C", real=True)

    # The program's rule (#1 §6): E = ρ̃ã³ enters our constraint as E/a³, with ã = 1/a; our pressure comes from OUR
    # continuity equation, so no reflection of the pressure is assumed.
    at = sp.Function("at", positive=True)(t)
    a = 1 / at
    rho_t = C * at ** (-3 * (1 + wt))
    rho_eff = sp.simplify(rho_t * at**3 / a**3)
    H = sp.diff(a, t) / a
    p_eff = sp.simplify(-rho_eff - sp.diff(rho_eff, t) / (3 * H))
    w_eff = sp.simplify(p_eff / rho_eff)
    check("the program's rule gives w_eff = -w~ through our continuity equation", sp.simplify(w_eff + wt) == 0,
          f"w_eff = {w_eff}")

    # Gasperini and Veneziano 2003, §2.2, eqs. 2.30-2.32, d = 3: rhobar = rho a^3, pbar = p a^3; a -> 1/a,
    # rhobar fixed, pbar -> -pbar. It never uses our continuity equation.
    rhobar, pbar = rho_t * at**3, wt * rho_t * at**3
    H_t = sp.diff(at, t) / at
    check("eq. 2.31 holds on the conjugate side", sp.simplify(sp.diff(rhobar, t) + 3 * H_t * pbar) == 0)
    check("eq. 2.31 holds after the duality map", sp.simplify(sp.diff(rhobar, t) + 3 * H * (-pbar)) == 0)
    d_rho, d_p = sp.simplify(rhobar / a**3 - rho_eff), sp.simplify(-pbar / a**3 - p_eff)
    check("the duality map gives the program's density and pressure", d_rho == 0 and d_p == 0,
          f"differences {d_rho}, {d_p}")

    # Their string-frame power laws (eqs. 2.33-2.38): a = t^alpha, phibar = -beta ln t, rhobar = rho0 a^(-d gamma).
    d = 3
    gam, al, be, rho0 = sp.symbols("gamma alpha beta rho0", real=True)
    sols = sp.solve([sp.Eq(d * gam * al + be, 2), sp.Eq(2 * be - be**2 - d * al**2, 0)], [al, be], dict=True)
    s = [x for x in sols if sp.simplify(x[al]) != 0][0]
    alpha, beta = sp.simplify(s[al]), sp.simplify(s[be])
    aa, phib = t**alpha, -beta * sp.log(t)
    Hs = sp.diff(aa, t) / aa
    rhob = rho0 * aa ** (-d * gam)
    r0 = sp.simplify((sp.diff(phib, t) ** 2 - d * Hs**2) / (sp.exp(phib) * rhob) * rho0)   # eq. 2.27 fixes rho0
    eq28 = sp.simplify(sp.diff(Hs, t) - Hs * sp.diff(phib, t) - sp.Rational(1, 2) * sp.exp(phib) * gam * rhob.subs(rho0, r0))
    eq29 = sp.simplify(2 * sp.diff(phib, t, 2) - sp.diff(phib, t) ** 2 - d * Hs**2)
    eq37 = sp.simplify(alpha - 2 * gam / (1 + d * gam**2)) == 0 and sp.simplify(beta - 2 / (1 + d * gam**2)) == 0
    check("the power laws match their eq. 2.37 and solve eqs. 2.28 and 2.29, with rho0 from eq. 2.27",
          eq37 and eq28 == 0 and eq29 == 0, f"alpha = {alpha}")
    flip = sp.simplify(alpha.subs(gam, -gam) + alpha), sp.simplify(beta.subs(gam, -gam) - beta)
    check("duality: alpha(-gamma) = -alpha(gamma), beta unchanged", flip == (0, 0))
    stiff, partner = alpha.subs(gam, 1), alpha.subs(gam, -1)
    # The duality turns a stiff source into one with p = -rho. No de Sitter universe solves eqs. 2.27-2.29 with such a
    # source, whatever the sign of rhobar: with H constant, eq. 2.28 with eq. 2.27 makes phibar' a root of a quadratic
    # with constant coefficients, so phibar'' = 0, and eq. 2.29 then needs phibar'^2 + d H^2 = 0. The power laws give
    # only exponents, and eq. 2.27 gives them rho0 < 0 where d gamma^2 > 1: the stiff one and its partner among them.
    Hc, x = sp.symbols("H_c", real=True, nonzero=True), sp.symbols("x", real=True)
    roots = sp.solve(sp.Eq(-Hc * x, -sp.Rational(1, 2) * (x**2 - d * Hc**2)), x)
    no_ds = len(roots) == 2 and all(sp.simplify(-(r**2) - d * Hc**2).is_negative for r in roots)
    check("the partner of a stiff source is not de Sitter; the stiff power law a ~ t^(1/2) goes to a ~ t^(-1/2)",
          no_ds and (stiff, partner) == (sp.Rational(1, 2), -sp.Rational(1, 2)),
          f"de Sitter: phibar' = {roots}, eq. 2.29 fails; partner dilaton beta = {beta.subs(gam, -1)}; the power laws "
          f"need rho0 = {sp.factor(r0)} by eq. 2.27: {r0.subs(gam, 1)} at gamma = 1 and {r0.subs(gam, -1)} at -1")

    # Einstein gravity, no dilaton (8 pi G = 1): a single fluid w, a = t^q.
    q = 2 / (3 * (1 + w))
    aE = t**q
    HE = sp.diff(aE, t) / aE
    rhoE = 3 * HE**2
    atE = 1 / aE
    resid = sp.simplify(sp.diff(atE, t) ** 2 / atE**2 - rhoE * aE**3 / atE**3 / 3)
    # Any flat solution a(t), rho = 3 H^2: the image a~ = 1/a, rho~ = rho a^3 / a~^3 misses the Friedmann equation by
    # H^2 (1 - a^6), which vanishes only where a = 1 or H = 0.
    af = sp.Function("af", positive=True)(t)
    Hf = sp.diff(af, t) / af
    image = (sp.diff(1 / af, t) * af) ** 2 - 3 * Hf**2 * af**3 * af**3 / 3
    check("in Einstein gravity the map takes no flat Friedmann solution to another",
          sp.simplify(image - Hf**2 * (1 - af**6)) == 0 and sp.simplify(resid.subs({w: 0, t: 2})) != 0,
          "the image misses the Friedmann equation by H^2 (1 - a^6); dust at t = 2: "
          + str(sp.nsimplify(resid.subs({w: 0, t: 2}))))
    wbar = sp.symbols("wbar", real=True)
    cosmic = sp.simplify(sp.solve(sp.Eq(2 / (3 * (1 + wbar)), -q), wbar)[0])
    conformal = sp.simplify(sp.solve(sp.Eq(2 / (1 + 3 * wbar), -2 / (1 + 3 * w)), wbar)[0])
    check("inversion at shared cosmic time: w -> -2 - w (phantom duality)", sp.simplify(cosmic + 2 + w) == 0, f"{cosmic}")
    check("inversion at shared conformal time: w -> -2/3 - w", sp.simplify(conformal + sp.Rational(2, 3) + w) == 0,
          f"{conformal}")

    # Mukherjee, Jassal and Lochan 2024, §6: Brans-Dicke w_BD = -4/3, U = 0; eqs. 46a, 46b, 47.
    H0, lam0, a0 = sp.symbols("H0 lambda0 a0", positive=True)
    aJ, lamJ = a0 * sp.exp(H0 * t), lam0 * sp.exp(-3 * H0 * t)
    k = sp.simplify(sp.log(sp.sqrt(lamJ) * aJ / (sp.sqrt(lam0) * a0)) / sp.log(aJ / a0))
    check("their pairing has d ln a~ / d ln a = -1/2, not -1", k == -sp.Rational(1, 2), f"{k}")
    tt, tc = sp.symbols("ttilde t_c", positive=True)
    aS = (tc - tt) ** sp.Rational(1, 3)
    stiff_const = sp.simplify(3 * (sp.diff(aS, tt) / aS) ** 2 * aS**6)
    check("their contracting description (eq. 47) is stiff: rho~ a~^6 constant", sp.diff(stiff_const, tt) == 0,
          f"rho~ a~^6 = {stiff_const}")

    # Which conjugate content acts on ours as a cosmological constant (w = -1) under each map.
    rules = [("program (scale-factor duality with sources)", lambda x: w_eff.subs(wt, x), 1),
             ("phantom duality (shared cosmic time)", lambda x: -2 - x, -1),
             ("shared conformal time", lambda x: sp.Rational(-2, 3) - x, sp.Rational(1, 3))]
    for name, rule, want in rules:
        need = sp.solve(sp.Eq(rule(wt), -1), wt)[0]
        check(f"Lambda from conjugate w~ = {want}: {name}", need == want, f"needs w~ = {need}")
    rows = [w_eff.subs(wt, x) for x in (0, -1, 1)]
    check("the program's rule: dual dust -> dust, dual Lambda -> stiff, dual stiff -> Lambda", rows == [0, 1, -1],
          f"w_eff = {rows}")


def main(argv):
    findings, quotes, sources = load("findings.json"), load("quotes.json"), load("sources.json")
    _, body, refs = note_parts()
    v = section_a(findings, body)
    section_b(findings, body)
    section_c(body, quotes, sources)
    section_d(refs, sources)
    section_e(v)
    section_f(quotes)
    section_g()
    if "--online" in argv:
        online(quotes, sources)
    if fails:
        print(f"\nFAILED: {len(fails)} checks: " + "; ".join(fails))
        return 1
    print("\nOK — the literature-check note matches its record: verdicts, counts, quotations and citations; "
          "the algebra behind flag 66 holds.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
