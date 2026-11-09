"""Find author-year citations in wiki prose and propose links to the cited papers (Paul, 2026-11-06:
"whenever referenced include a link to the paper itself if possible").

Verified papers: scripts/wiki-papers.tsv (the registry) and review/literature-check/sources.json. Nothing is
linked from memory. A citation is linked only when its first surname is the paper's first author (diacritics
folded), its year is one of the paper's years, and, where an author list is known, every other surname it names
is a coauthor. Author lists come from sources.json, else from INSPIRE (fetched once, cached in
inspire-authors.json), else, for the one handle, from the repository page's citation metadata (hdl.html). Two
verified papers that share first author and year make a citation ambiguous unless the surrounding text identifies
one; the script reports the evidence it finds, and decisions.tsv records the reviewer's reading of every proposal.

  author_year.py            survey: write candidates.json, proposals.json and review.txt; change nothing
  author_year.py --apply    apply the proposals decisions.tsv accepts; write author-year-links.tsv and
                            author-year-skipped.tsv
  author_year.py --report   rerun on the pre-task snapshot, check the proposals equal author-year-links.tsv,
                            and rewrite author-year-skipped.tsv

Pages never touched: CLAUDE.md, summary.md, method/literature-check.md, program/founding-suppositions.md,
dark-matter/conjugate-matter/_index.md. Never linked: headings, frontmatter, fenced and inline code, text inside a
link, double-quoted text and blockquotes, citations marked with a dagger or said to come from model memory (unless
the line gives a matching title or journal), and any mention on a line that already links the same paper. Only the
first qualifying mention of a paper on a page is linked; an existing link to the paper earlier on the page means
the paper is linked already.
"""

import importlib.util
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WIKI = ROOT / "wiki"
spec = importlib.util.spec_from_file_location("cw", ROOT / "scripts" / "check-wiki.py")
cw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cw)

EXCLUDED = {
    "summary.md",
    "method/literature-check.md",
    "program/founding-suppositions.md",
    "dark-matter/conjugate-matter/_index.md",
}
CACHE = HERE / "inspire-authors.json"
DECISIONS = HERE / "decisions.tsv"
LINKS_OUT = HERE / "author-year-links.tsv"
SKIPPED_OUT = HERE / "author-year-skipped.tsv"


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()


def fold2(s):
    """fold, with German umlauts written out first (Könnig = Koennig)."""
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("Ä", "Ae"), ("Ö", "Oe"), ("Ü", "Ue")):
        s = s.replace(a, b)
    return fold(s)


def keys_of(name):
    return {fold(name), fold2(name)}


def surname_of(full):
    full = full.strip()
    if "," in full:
        return full.split(",", 1)[0].strip()
    return full.split()[-1] if full.split() else full


# ------------------------------------------------------------------------------------------- verified papers
def load_registry():
    rows = {}
    for line in (ROOT / "scripts" / "wiki-papers.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        c = line.split("\t")
        rows[c[0]] = {"id": c[0], "surnames": [n for n in c[1].split("|") if n],
                      "years": [y for y in c[2].split(",") if y], "title": c[3], "source": c[4]}
    return rows


def sources_entries():
    d = json.loads((ROOT / "review" / "literature-check" / "sources.json").read_text(encoding="utf-8"))
    out = []
    for key, v in d.items():
        ids = []
        arx = v.get("arxiv") or ""
        if not arx and re.match(r"^(\d{4}\.\d{4,5}|[a-z\-]+(\.[A-Z]{2})?/\d{7})$", key):
            arx = key
        if arx:
            ids.append("arXiv:" + arx)
        for doi in v.get("dois") or []:
            ids.append("doi:" + doi.lower())
        if key.startswith("doi:"):
            ids.append("doi:" + key[4:].lower())
        if v.get("recid"):
            ids.append("recid:" + str(v["recid"]))
        m = re.search(r"/handle/(\d+(?:\.\d+)*/\d+)", v.get("landing_page") or "")
        if m:
            ids.append("hdl:" + m.group(1))
        years = set()
        if v.get("earliest_date"):
            years.add(str(v["earliest_date"])[:4])
        years |= set(re.findall(r"\((\d{4})\)", v.get("journal") or ""))
        out.append({"key": key, "ids": list(dict.fromkeys(ids)), "years": years,
                    "authors": [surname_of(a) for a in v.get("authors") or []],
                    "title": v.get("title") or "", "journal": v.get("journal") or v.get("venue") or ""})
    return out


def handle_page_authors():
    """Author list of the registered handle, from the repository page's citation metadata (fetched earlier)."""
    page = HERE / "hdl.html"
    if not page.exists():
        return {}
    text = page.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'name="citation_abstract_html_url" content="https?://hdl\.handle\.net/([^"]+)"', text)
    authors = re.findall(r'name="citation_author" content="([^"]+)"', text)
    return {"hdl:" + m.group(1): [surname_of(a) for a in authors]} if m and authors else {}


def build_works():
    reg = load_registry()
    works, by_id = [], {}

    def new_work():
        w = {"ids": [], "surnames": [], "years": set(), "titles": [], "journal": "",
             "authors": None, "authors_from": None, "skey": None}
        works.append(w)
        return w

    for s in sources_entries():
        w = next((by_id[i] for i in s["ids"] if i in by_id), None) or new_work()
        w["skey"] = s["key"]
        for i in s["ids"]:
            if i not in w["ids"]:
                w["ids"].append(i)
            by_id[i] = w
        w["years"] |= s["years"]
        if s["authors"]:
            w["authors"], w["authors_from"] = s["authors"], "sources.json"
            if s["authors"][0] not in w["surnames"]:
                w["surnames"].append(s["authors"][0])
        w["titles"].append(s["title"])
        w["journal"] = s["journal"]
    for pid, row in reg.items():
        w = by_id.get(pid)
        if w is None:  # the same paper under another identifier (the arXiv and DOI rows of one paper)
            w = next((o for o in works if any(fold(t) == fold(row["title"]) for t in o["titles"])
                      and any(fold(a) == fold(b) for a in row["surnames"] for b in o["surnames"])), None)
        w = w or new_work()
        if pid not in w["ids"]:
            w["ids"].append(pid)
        by_id[pid] = w
        for n in row["surnames"]:
            if n not in w["surnames"]:
                w["surnames"].append(n)
        w["years"] |= set(row["years"])
        w["titles"].append(row["title"])
    for pid, authors in handle_page_authors().items():
        if pid in by_id and by_id[pid]["authors"] is None:
            by_id[pid]["authors"], by_id[pid]["authors_from"] = authors, "repository page (hdl.html)"
    order = {"arXiv": 0, "doi": 1, "recid": 2, "hdl": 3}
    for n, w in enumerate(works):
        w["n"] = n
        w["reg_ids"] = [i for i in w["ids"] if i in reg]
        w["link_id"] = sorted(w["ids"], key=lambda i: order[i.split(":")[0]])[0] if w["ids"] else None
        w["name"] = f"{w['surnames'][0]} {'/'.join(sorted(w['years']))}: {w['titles'][0][:80]}"
    return works, by_id, reg


def doi_case():
    """DOIs in the publisher's case, from sources.json (the registry lowercases them; doi.org ignores case)."""
    d = json.loads((ROOT / "review" / "literature-check" / "sources.json").read_text(encoding="utf-8"))
    out = {}
    for v in d.values():
        for doi in v.get("dois") or []:
            out[doi.lower()] = doi
    return out


DOI_CASE = doi_case()


def url_of(pid):
    kind, _, value = pid.partition(":")
    if kind == "arXiv":
        return "https://arxiv.org/abs/" + value
    if kind == "doi":
        return "https://doi.org/" + urllib.parse.quote(DOI_CASE.get(value.lower(), value), safe="/:;.-_")
    if kind == "recid":
        return "https://inspirehep.net/literature/" + value
    return "https://hdl.handle.net/" + value


# --------------------------------------------------- author lists of registry-only papers, from INSPIRE
def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "conjugate-matter-author-year/1.0 (research script)",
                                               "Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):
                return None
            time.sleep(3 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(3 * (attempt + 1))
    return None


def inspire_record(pid, cache):
    if pid in cache:
        return cache[pid]
    kind, _, value = pid.partition(":")
    url = {"arXiv": f"https://inspirehep.net/api/arxiv/{value}",
           "doi": "https://inspirehep.net/api/doi/" + urllib.parse.quote(value, safe="/"),
           "recid": f"https://inspirehep.net/api/literature/{value}"}.get(kind)
    got = None
    if url:
        time.sleep(0.5)
        data = fetch_json(url)
        if data and "metadata" in data:
            md = data["metadata"]
            got = {"authors": [surname_of(a.get("full_name", "")) for a in md.get("authors") or []],
                   "collaborations": [c.get("value") for c in md.get("collaborations") or []],
                   "title": (md.get("titles") or [{}])[0].get("title", ""),
                   "journal": "; ".join(
                       f"{p.get('journal_title', '')} {p.get('journal_volume', '')} "
                       f"{p.get('artid') or p.get('page_start') or ''} ({p.get('year', '')})"
                       for p in md.get("publication_info") or [] if p.get("journal_title"))}
    cache[pid] = got
    CACHE.write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf-8")
    return got


def ensure_authors(w, cache):
    if w["authors"] is None and w["link_id"] and not w["link_id"].startswith("hdl:"):
        got = inspire_record(w["link_id"], cache)
        if got and got["authors"]:
            w["authors"], w["authors_from"] = got["authors"], "INSPIRE, fetched for this check"
            if not w["journal"]:
                w["journal"] = got["journal"]
    return w["authors"]


# ------------------------------------------------------------------------------------- citations in prose
UP = "".join(chr(c) for c in range(0x41, 0x250) if chr(c).isupper() and chr(c).isalpha())
WORD = rf"[{UP}][^\W\d_]*(?:['’][^\W\d_]+)*(?:-[{UP}][^\W\d_]*(?:['’][^\W\d_]+)*)*"
PARTICLE = r"(?:(?:[dD]e|[vV]on|[vV]an|[dD]er|[dD]en|[dD]a|[dD]i|[dD]u|[dD]el|[dD]ella|[dD]os|[lL]e|[lL]a|'t|’t|ten|ter)\s+)"
INITIALS = rf"(?:[{UP}]\.(?:\s?-?[{UP}]\.)*\s+)"
INITIALS_RE = re.compile(rf"^{INITIALS}")
NAME = rf"(?:{INITIALS}?{PARTICLE}*{WORD})"
SEP = r"(?:,\s+and\s+|\s+and\s+|\s*&\s*|,\s+|\s*[–—]\s*)"
CIT_RE = re.compile(
    rf"(?<![\w/#.@-])(?P<names>{NAME}(?:{SEP}{NAME})*)"
    r"(?P<tail>\s+et\s+al\.?,?|\s+and\s+(?:coauthors|co-authors|collaborators|colleagues),?)?"
    r"(?:\s+\((?P<pyear>(?:1[89]|20)\d\d)(?P<psuf>[a-z])?\)|,?\s+(?P<year>(?:1[89]|20)\d\d)(?P<suf>[a-z])?)"
    r"(?!\d)(?!\.\d)(?![–-]\d)"
)
PLANCK_PART_RE = re.compile(r"^ (?:I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII)\b(?![.\w])")
SEP_RE = re.compile(SEP)
STOP = {fold(w) for w in """In On At By For From Since Until Before After During Of To As And Or But The A An This That
These Those Its It January February March April May June July August September October November December Jan Feb Mar
Apr Jun Jul Aug Sep Sept Oct Nov Dec Withdrawn Version Round Step Table Figure Fig Section Item Items Flag Flags Row Rows
Note Notes Paper Papers Chapter Appendix Rev Phys Lett Nucl Proc Ann Annals Class Quant Grav Astrophys Astron Mon Not Roy
Soc Eur Int Mod Commun Math Found Gen Rel Physics Science Nature Review Reviews Summer Winter Spring Autumn Fall Revised
Updated Draft Published Posted Read Retrieved Accessed Archived Edition Vol Volume No Nos Issue Part Erratum Corrigendum
Report Reports Proceedings Conference Workshop Symposium School Lectures Lecture Thesis Since Through
A B C D E T II III IV TeV Machine Nature Press Group Group's Japan Mathematics Applications Astronomy Astrophysics
Wissenschaften Scholarpedia Supernova Washington Hutchinson Addison-Wesley Cambridge Oxford University Princeton Springer
Wiley Dover Pergamon Benjamin Freeman Clarendon""".split()}
ACRONYM_RE = re.compile(r"^[A-Z][A-Z0-9]{1,6}$")
# Phrases that use the dagger for the literature battery or for the marks themselves, not as a mark on a citation.
DAGGER_PROSE_RE = re.compile(r"†\s+(?:literature\s+)?battery|the\s+†\s+(?:or|and)\s+\[S\]|†\s+(?:mark|marks|references|"
                             r"entries|entry|citations?|reference)\b|marked\s+†|(?:a|the|its|their|keep|keeps)\s+†(?:\s|,|\.|$)")
MEMORY_RE = re.compile(r"model memory|from memory|†")
# A sentence ends at '. ' before a capital, except after an abbreviation or an initial.
SENT_END_RE = re.compile(r"(?<!\bal)(?<!\beq)(?<!\beqs)(?<!\bcf)(?<!\bvs)(?<!\be\.g)(?<!\bi\.e)(?<!\bRev)(?<!\bPhys)"
                         r"(?<!\bLett)(?<!\bRef)(?<!\bRefs)(?<!\bNo)(?<!\bp)(?<!\bpp)(?<!\bSec)(?<!\bFig)(?<!\bVol)"
                         rf"(?<!\b[{UP}])\.\s+(?=[{UP}*\[(#\"])")


def blank(text, spans):
    chars = list(text)
    for a, b in spans:
        for i in range(max(0, a), min(len(chars), b)):
            chars[i] = " "
    return "".join(chars)


def sentence_of(line, start, end):
    a, b = 0, len(line)
    for m in SENT_END_RE.finditer(line):
        if m.end() <= start:
            a = m.end()
        elif m.start() >= end:
            b = m.start() + 1
            break
    return line[a:b]


def page_lines(f):
    raw = f.read_text(encoding="utf-8")
    lines = raw.split("\n")
    fm, body, off = cw.split_frontmatter(raw)
    clean, _ = cw.strip_code(body, off)
    for lineno, line in clean:
        assert lines[lineno - 1] == line, (f, lineno)
    return raw, lines, clean


def name_parts(text, m):
    """The names of a CIT_RE match as [(start of the name with its initials, start of the surname, surname)]."""
    out, pos = [], m.start("names")
    for part in (p for p in SEP_RE.split(m.group("names")) if p and p.strip()):
        part = part.strip()
        k = text.find(part, pos)
        ini = INITIALS_RE.match(part)
        skip = ini.end() if ini else 0
        out.append((k, k + skip, part[skip:]))
        pos = k + len(part)
    return out


def scan(works, by_id, cache):
    index = {}
    for w in works:
        for n in w["surnames"]:
            for k in keys_of(n):
                index.setdefault(k, [])
                if w not in index[k]:
                    index[k].append(w)
    multiword = sorted({n for w in works for n in w["surnames"] if " " in n}, key=len, reverse=True)
    candidates, pages = [], {}
    for f in sorted(WIKI.rglob("*.md")):
        rel = f.relative_to(WIKI).as_posix()
        if f.name == "CLAUDE.md" or rel in EXCLUDED:
            continue
        raw, lines, clean = page_lines(f)
        events, in_quote = [], False
        for lineno, line in clean:
            if not line.strip():
                in_quote = False
                continue
            code = [(a, b) for a, b, _ in cw.code_spans(line)] + [(m.start(), m.end()) for m in cw.INLINE_CODE_RE.finditer(line)]
            text = blank(line, code)
            links = [(lm.start(), lm.end(), lm.group(1), lm.group(2)) for lm in cw.LINK_FULL_RE.finditer(text)]
            # double-quoted spans, with link targets blanked; an unclosed quote carries to the next line
            qtext = blank(text, [(a + len(label) + 2, b) for a, b, label, _ in links])
            quotes, qs = [], (0 if in_quote else None)
            for i, ch in enumerate(qtext):
                if ch == '"':
                    if qs is None:
                        qs = i
                    else:
                        quotes.append((qs, i + 1))
                        qs = None
            in_quote = qs is not None
            if in_quote:
                quotes.append((qs, len(qtext)))
            heading = bool(cw.HEADING_RE.match(line))
            blockquote = bool(re.match(r"^\s*>", line))
            line_works = set()
            for a, b, label, target in links:
                pid = cw.paper_of_url(target)
                if pid and pid in by_id:
                    line_works.add(by_id[pid]["n"])
                    events.append((lineno, a, 0, "link", by_id[pid]))
            for m in CIT_RE.finditer(text):
                parts = name_parts(text, m)
                year = m.group("year") or m.group("pyear")
                chosen = None
                for k0 in range(len(parts)):  # the full name list, then without leading names ("Monopoles, Kibble 1976")
                    lstart, sstart, first = parts[k0]
                    first = re.sub(r"['’]s$", "", first)
                    for mw in multiword:  # a registered multi-word surname ("Lopes Cardoso", "Camara da Silva")
                        if fold(mw) != fold(first) and fold(mw).endswith(" " + fold(first)):
                            pre = mw[: len(mw) - len(first)]
                            if fold(text[max(0, sstart - len(pre)):sstart]) == fold(pre):
                                first, sstart = mw, sstart - len(pre)
                                lstart = min(lstart, sstart)
                                break
                    split = None
                    if not (keys_of(first) & index.keys()) and "-" in first:  # "Murayama-Shu 2009": two surnames
                        bits = first.split("-")
                        if keys_of(bits[0]) & index.keys():
                            split = bits
                    lead = split[0] if split else first
                    if (keys_of(first) & index.keys() or split) and (k0 == 0 or any(
                            year in w["years"] for k in keys_of(lead) for w in index.get(k, []))):
                        chosen = (k0, lstart, first, split)
                        break
                if chosen is None:
                    k0 = 0
                    while k0 < len(parts) and fold(parts[k0][2].split()[-1]) in STOP:
                        k0 += 1
                    if k0 == len(parts):
                        continue
                    chosen = (k0, parts[k0][0], re.sub(r"['’]s$", "", parts[k0][2]), None)
                k0, lstart, first, split = chosen
                others = [p[2] for p in parts[k0 + 1:]]
                if split:
                    first, others = split[0], split[1:] + others
                end = m.end()
                if fold(first) in ("planck", "aghanim"):
                    pm = PLANCK_PART_RE.match(text[end:])
                    if pm:
                        end += pm.end()
                sent = sentence_of(blank(line, [(mm.start(), mm.end()) for mm in DAGGER_PROSE_RE.finditer(line)]), lstart, end)
                c = {"file": rel, "line": lineno, "col": lstart, "end": end, "label": line[lstart:end], "first": first,
                     "others": others, "etal": bool(m.group("tail")), "year": year,
                     "possessive": any(p[2].endswith(("'s", "’s")) for p in parts[k0:]), "heading": heading,
                     "blockquote": blockquote,
                     "in_link": any(a <= lstart < b for a, b, *_ in links),
                     "quoted": any(a <= lstart < b for a, b in quotes),
                     "memory": bool(MEMORY_RE.search(sent)) or "†" in line[end:end + 3],
                     "sentence": sent.strip(), "line_text": line, "line_works": line_works,
                     "context": line[max(0, lstart - 240):end + 240]}
                by_name = []
                for k in keys_of(first):
                    for w in index.get(k, []):
                        if w not in by_name:
                            by_name.append(w)
                matched, fails = [], []
                for w in (w for w in by_name if year in w["years"]):
                    authors = ensure_authors(w, cache) if others else w["authors"]
                    if authors is not None and others:
                        known = set()
                        for a in authors:
                            known |= keys_of(a) | {fold(a).split()[-1]} | {fold(p) for p in a.split("-")}
                        bare = [re.sub(r"['’]s$", "", o) for o in others]
                        missing = [o for o in bare if not ((keys_of(o) | {fold(o).split()[-1]}) & known)]
                        if missing:
                            fails.append((w, missing))
                            continue
                    matched.append(w)
                c["by_name"], c["matched"], c["fails"] = by_name, matched, fails
                candidates.append(c)
                events.append((lineno, lstart, 1, "cite", c))
        pages[rel] = {"path": f, "raw": raw, "events": sorted(events, key=lambda e: (e[0], e[1], e[2]))}
    return candidates, pages


def identify(c, matched, page_raw, cache):
    """Evidence on the page or line that picks one of several verified papers, as [(work, evidence)]."""
    found = []
    low = page_raw.lower()
    for w in matched:
        ev = []
        for i in w["ids"]:
            if i.split(":", 1)[1].lower() in low:
                ev.append("page cites " + i)
        for t in w["titles"]:
            words = [x for x in re.findall(r"[a-z]{6,}", fold(t)) if x not in ("theory", "string", "physics")]
            hit = sorted({x for x in words if x in fold(c["line_text"])})
            if len(hit) >= 3:
                ev.append("line shares title words " + ",".join(hit))
        if c["etal"]:
            others = [x for x in matched if x is not w]
            mine = ensure_authors(w, cache) or []
            if len(mine) > 1 and all(len(ensure_authors(x, cache) or []) == 1 for x in others):
                ev.append("et al.: every other candidate has one author (" +
                          "; ".join(f"{x['link_id']}: {', '.join(x['authors'])}, {x['authors_from']}" for x in others) + ")")
        if ev:
            found.append((w, ev))
    return found


# Reviewed by hand: the sentence carries a dagger or "from memory", but it marks another citation, and this one is
# marked [S] (live-searched) or identified by the journal it gives. (file, line, label) -> why it is not a dagger.
NOT_DAGGER = {
    ("cosmology/scale-factor-duality/cosmological-constraint.md", 107, "Veneziano 1991"):
        "marked [S]; the dagger is Tseytlin 1991's",
    ("dark-matter/momentum-clumping/founding-image.md", 153, "Riotto and Tkachev 2000"):
        "the list is marked [S]; the dagger is #11's [13]†",
    ("dark-matter/momentum-clumping/founding-image.md", 153, "Sikivie and Yang 2009"):
        "the list is marked [S]; the dagger is #11's [13]†",
    ("dark-matter/momentum-clumping/founding-image.md", 153, "Berezhiani and Khoury 2015"):
        "the list is marked [S]; the dagger is #11's [13]†",
    ("dark-matter/momentum-clumping/founding-image.md", 153, "Levkov, Panin and Tkachev 2018"):
        "marked [S] here; the dagger is #11's own citation of it, [13]†",
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Lozano 1995"):
        "the list is marked [S]; the dagger is #11's [3]†",
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Harvey, Moore and Strominger 1995"):
        "the list is marked [S]; the dagger is #11's [3]†",
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Kapustin and Witten 2007"):
        "the list is marked [S]; the dagger is #11's [3]†",
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Galakhov, Mironov and Morozov 2014"):
        "the list is marked [S]; the dagger is #11's [3]†",
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Freidel, Leigh and Minic 2014"):
        "the line gives the journal, Phys. Lett. B, which matches arXiv:1307.7080 (Phys. Lett. B 730 302 (2014))",
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Berglund, Hübsch and Minic 2021"):
        "the dagger is #11's [3]†, Freidel, Leigh and Minic's, later in the sentence; the sentence ends [S]",
}


# Reviewed by hand: two verified papers share first author and year, and the text identifies one of them.
# (file, line, label) -> (identifier, the identifying text).
IDENTIFIED = {
    ("cosmology/scale-factor-duality/self-dual-length-obituary.md", 82, "Lee et al. 2020"):
        ("arXiv:2002.11761", "et al.; the other Lee 2020 paper, the thesis hdl:1773/45542, has one author (its repository "
                             "page's citation metadata), and the same line cites it separately as 'Lee 2020 thesis'"),
    ("cosmology/scale-factor-duality/self-dual-length-obituary.md", 82, "Lee 2020"):
        ("hdl:1773/45542", "the text reads 'Lee 2020 thesis, Table 11.4'; hdl:1773/45542 is the dissertation"),
    ("cosmology/scale-factor-duality/square-at-the-bounce.md", 71, "Gasperini–Veneziano 1993"):
        ("arXiv:hep-th/9211021", "the line quotes the diameter note §6, whose sentence this is; the note's only "
                                 "Gasperini–Veneziano 1993 is hep-th/9211021 (wiki/papers/phase-space-diameter.md, References)"),
    ("cosmology/scale-factor-duality/collapse-powered-expansion.md", 91, "Gasperini and Veneziano 1993"):
        ("arXiv:hep-th/9309023", "the page's source for 'collapse in another frame' is notes/literature-check.md §6 (its "
                                 "Sources), whose only Gasperini and Veneziano 1993 is hep-th/9309023, quoted there"),
    ("dark-matter/candidates/soliton-candidate/kinetic-mixing.md", 104, "Brümmer–Jaeckel 2009"):
        ("arXiv:0902.3615", "the page's reference list gives F. Brümmer, J. Jaeckel as arXiv:0902.3615 and the "
                            "three-author paper as arXiv:0905.0633; the audit notes quote 'BJ p.5'"),
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Berglund, Hübsch and Minic 2021"):
        ("arXiv:2111.14205", "the sentence restates notes/literature-check.md §5, the page's source, which gives this "
                             "reading for 'a 2021 conference paper (arXiv:2111.14205)'"),
    ("electric-magnetic-duality/unified-modular-structure.md", 114, "Freidel, Leigh and Minic 2014"):
        ("arXiv:1307.7080", "the line gives the journal, Phys. Lett. B; arXiv:1307.7080 is Phys. Lett. B 730, 302 (2014), "
                            "arXiv:1405.3949 is Int. J. Mod. Phys. D 23 (2014)"),
    ("dark-matter/candidates/momentum-space-monopoles.md", 108, "Brümmer, Ferrante, Fischer and Frigerio 2026"):
        ("arXiv:2509.21924", "the quotation beside it, 'dark monopoles cannot constitute a sizeable fraction of dark "
                             "matter', is from arXiv:2509.21924's abstract (sources.json); the later paper is named apart"),
    ("dark-matter/candidates/soliton-candidate/hidden-sector.md", 99, "Brümmer, Ferrante, Fischer and Frigerio 2026"):
        ("arXiv:2509.21924", "the quotation beside it is from arXiv:2509.21924's abstract (sources.json); 'posted before "
                             "#14 v3' and flag 68, which gives arXiv:2509.21924"),
    ("status/alive.md", 222, "Brümmer, Ferrante, Fischer and Frigerio 2026"):
        ("arXiv:2509.21924", "flag 68, cited beside it, gives arXiv:2509.21924 for the exclusion of the minimal model"),
}


def decide(pages, cache, reg, rejected):
    """Walk each page in order. An existing link settles its paper; a candidate is proposed for its paper's first
    qualifying mention; every other first mention is recorded with the reason it was not linked."""
    props, skips = [], []
    for rel, page in pages.items():
        settled, reported = set(), set()
        for lineno, col, _, kind, obj in page["events"]:
            if kind == "link":
                settled.add(obj["n"])
                continue
            c = obj
            M = c["matched"]
            key = (fold(c["first"]), c["year"])
            if not M:
                if key not in reported:
                    reported.add(key)
                    if c["fails"]:
                        why = "; ".join(f"{w['link_id']} lacks {', '.join(miss)}" for w, miss in c["fails"])
                        skips.append((c, None, "unverified", f"coauthors differ from every verified {c['first']} {c['year']} paper ({why})"))
                    elif c["by_name"]:
                        yrs = sorted({y for w in c["by_name"] for y in w["years"]})
                        skips.append((c, None, "unverified", f"no verified {c['first']} paper of {c['year']} (verified years: {', '.join(yrs)})"))
                    elif ACRONYM_RE.match(c["first"]):
                        skips.append((c, None, "acronym", f"{c['first']} is initials or an abbreviation, not a surname; "
                                                          "a link label must name the paper's first author"))
                    else:
                        skips.append((c, None, "unverified", f"no verified paper by {c['first']}"))
                continue
            if all(w["n"] in settled for w in M):
                continue  # a later mention
            if any(w["n"] in c["line_works"] for w in M):
                for w in M:
                    if w["n"] in c["line_works"]:
                        settled.add(w["n"])
                skips.append((c, [w for w in M if w["n"] in c["line_works"]][0], "linked", "the line already links the paper"))
                continue
            evidence = None
            manual = IDENTIFIED.get((c["file"], c["line"], c["label"]))
            if manual:
                w = next(x for x in M if x["link_id"] == manual[0])
                evidence = ["by hand: " + manual[1]]
            elif len(M) > 1:
                found = identify(c, M, page["raw"], cache)
                if len(found) == 1:
                    w, evidence = found[0]
                else:
                    if ("amb",) + key not in reported:
                        reported.add(("amb",) + key)
                        alts = " or ".join(f"{w['link_id']} ({w['titles'][0][:60]})" for w in M)
                        extra = (" [evidence for several: " + "; ".join(f"{w['link_id']}: {', '.join(e)}" for w, e in found) + "]") if found else ""
                        skips.append((c, None, "ambiguous", f"{alts}{extra}"))
                    continue
            elif not manual:
                w = M[0]
            if w["n"] in settled:
                continue
            reason = None
            if c["heading"]:
                reason = ("heading", "a link in a heading fails the gate")
            elif c["in_link"]:
                reason = ("inside a link", "the mention is the label of another link")
            elif c["blockquote"]:
                reason = ("quoted", "in a blockquote (quoted record text)")
            elif c["quoted"]:
                reason = ("quoted", "inside double quotation marks")
            elif c["possessive"]:
                reason = ("possessive", "a possessive, not an author-year citation")
            elif c["memory"] and (c["file"], c["line"], c["label"]) not in NOT_DAGGER:
                reason = ("†", "the sentence marks the citation † or says it is from model memory")
            elif w["link_id"] not in reg and w["link_id"].startswith("hdl:"):
                reason = ("unverified", f"{w['link_id']} is a handle the registry lacks, and scripts/wiki-papers.py "
                                        "registers handles only by hand")
            elif (c["file"], c["line"], c["label"]) in rejected:
                reason = rejected[(c["file"], c["line"], c["label"])]
            elif w["link_id"] in reg and not all(y in reg[w["link_id"]]["years"] for y in cw.YEAR_RE.findall(c["label"])):
                reason = ("registry year", f"the label gives {', '.join(cw.YEAR_RE.findall(c['label']))}; the registry row of "
                          f"{w['link_id']} has only {', '.join(reg[w['link_id']]['years'])} ({reg[w['link_id']]['source']}), "
                          f"so the gate's paper check would fail it, and the registry is not edited by hand")
            if reason:
                skips.append((c, w, reason[0], reason[1]))
                continue
            props.append((c, w, evidence))
            settled.add(w["n"])
    return props, skips


def prop_key(c, w):
    return f"{c['file']}\t{c['line']}\t{c['label']}\t{w['link_id']}"


def write_review(props, skips, cache):
    with open(HERE / "review.txt", "w", encoding="utf-8") as fh:
        for i, (c, w, ev) in enumerate(props):
            ensure_authors(w, cache)
            fh.write(f"#{i} {c['file']}:{c['line']} [{c['label']}] -> {w['link_id']} (registered: {w['link_id'] in w['reg_ids']})\n")
            fh.write(f"    paper: {w['name']}\n    authors ({w['authors_from']}): {', '.join((w['authors'] or [])[:8])}\n")
            if ev:
                fh.write(f"    IDENTIFIED among {len(c['matched'])}: {'; '.join(ev)}\n")
            named = 1 + len(c["others"])
            if w["authors"] and not c["etal"] and named < len(w["authors"]) and len(w["authors"]) < 30:
                fh.write(f"    WARNING: names {named} of the paper's {len(w['authors'])} authors, without et al.\n")
            if c["memory"]:
                fh.write(f"    NOTE: dagger or memory in the sentence; not a dagger here: {NOT_DAGGER.get((c['file'], c['line'], c['label']))}\n")
            fh.write(f"    ...{c['context']}...\n\n")
        fh.write("\n\n############ SKIPPED (first mentions not linked)\n\n")
        for c, w, why, note in skips:
            if why in ("unverified",):
                continue
            fh.write(f"- {why}: {c['file']}:{c['line']} [{c['label']}] {('-> ' + w['link_id']) if w else ''} | {note}\n")
            fh.write(f"    ...{c['context']}...\n\n")
    json.dump([{"key": prop_key(c, w), "evidence": ev} for c, w, ev in props],
              open(HERE / "proposals.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def write_candidates(candidates):
    out = []
    for c in candidates:
        d = {k: v for k, v in c.items() if k not in ("by_name", "matched", "fails", "line_works", "line_text")}
        d["by_name"] = [w["name"] for w in c["by_name"]]
        d["matched"] = [w["link_id"] for w in c["matched"]]
        d["fails"] = [(w["link_id"], miss) for w, miss in c["fails"]]
        out.append(d)
    (HERE / "candidates.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")


def load_decisions():
    """decisions.tsv: file, line, label, identifier, decision (accept or a skip reason), note."""
    out = {}
    if DECISIONS.exists():
        for line in DECISIONS.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            cells = line.split("\t")
            out["\t".join(cells[:4])] = (cells[4], cells[5] if len(cells) > 5 else "")
    return out


def rejections(decisions):
    out = {}
    for key, (decision, note) in decisions.items():
        if decision != "accept":
            f, ln, label, _ = key.split("\t")
            out[(f, int(ln), label)] = (decision, note)
    return out


def apply(props, skips, pages, reg):
    decisions = load_decisions()
    missing = [prop_key(c, w) for c, w, _ in props if prop_key(c, w) not in decisions]
    if missing:
        print("no decision for", len(missing), "proposals, e.g.", missing[:3])
        return 1
    accepted = [(c, w) for c, w, _ in props]
    unregistered = sorted({w["link_id"] for c, w in accepted if w["link_id"] not in reg})
    if unregistered:
        print("register first: .venv/bin/python scripts/wiki-papers.py " + " ".join(
            i if not i.startswith("doi:") else i for i in unregistered))
        return 1
    # gate rule: the label names the registered first author and only registered years
    for c, w in accepted:
        names, years = reg[w["link_id"]]["surnames"], set(reg[w["link_id"]]["years"])
        assert any(cw.fold(n) in cw.fold(c["label"]) for n in names), (c["label"], names)
        assert all(y in years for y in cw.YEAR_RE.findall(c["label"])), (c["label"], years)
    by_file = {}
    for c, w in accepted:
        by_file.setdefault(c["file"], []).append((c, w))
    rows = []
    for rel, items in sorted(by_file.items()):
        path = WIKI / rel
        lines = path.read_text(encoding="utf-8").split("\n")
        for c, w in sorted(items, key=lambda cw_: (cw_[0]["line"], -cw_[0]["col"])):
            line = lines[c["line"] - 1]
            assert line[c["col"]:c["end"]] == c["label"], (rel, c["line"], c["label"])
            url = url_of(w["link_id"])
            lines[c["line"] - 1] = line[:c["col"]] + f"[{c['label']}]({url})" + line[c["end"]:]
            rows.append((rel, c["line"], c["label"], w["link_id"], url))
        path.write_text("\n".join(lines), encoding="utf-8")
    with open(LINKS_OUT, "w", encoding="utf-8") as fh:
        fh.write("file\tline\tlabel\tidentifier\turl\n")
        for r in sorted(rows):
            fh.write("\t".join(["wiki/" + r[0], str(r[1]), r[2], r[3], r[4]]) + "\n")
    with open(SKIPPED_OUT, "w", encoding="utf-8") as fh:
        fh.write("file\tline\tlabel\treason\tidentifier\tdetail\n")
        for c, w, why, note in sorted(skips, key=lambda s: (s[0]["file"], s[0]["line"], s[0]["col"])):
            if why == "linked":
                continue
            fh.write("\t".join(["wiki/" + c["file"], str(c["line"]), c["label"], why.strip(), w["link_id"] if w else "",
                                note.strip()]) + "\n")
    print(f"applied {len(rows)} links on {len(by_file)} pages")
    return 0


REASONS = {"linked": "line links the paper"}


def report(props, skips):
    """Write author-year-skipped.tsv; check that the proposals are the links in author-year-links.tsv."""
    import csv
    applied = {(r["file"], r["line"], r["label"], r["identifier"])
               for r in csv.DictReader(open(LINKS_OUT, encoding="utf-8"), delimiter="\t")}
    now = {("wiki/" + c["file"], str(c["line"]), c["label"], w["link_id"]) for c, w, _ in props}
    if now != applied:
        print("proposals differ from the applied links:", sorted(now ^ applied)[:10])
        return 1
    with open(SKIPPED_OUT, "w", encoding="utf-8") as fh:
        fh.write("file\tline\tlabel\treason\tidentifier\tdetail\n")
        for c, w, why, note in sorted(skips, key=lambda s: (s[0]["file"], s[0]["line"], s[0]["col"])):
            ident = w["link_id"] if w else " or ".join(x["link_id"] for x in c["matched"])
            fh.write("\t".join(["wiki/" + c["file"], str(c["line"]), c["label"], REASONS.get(why, why), ident,
                                note.strip()]) + "\n")
    print(f"wrote {SKIPPED_OUT.name}: {len(skips)} rows; the {len(applied)} links match the proposals")
    return 0


def main(argv):
    global WIKI
    if "--report" in argv:  # the state the decisions were made on; the links added no lines
        WIKI = HERE / "snapshot" / "wiki-before-authoryear"
    works, by_id, reg = build_works()
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    candidates, pages = scan(works, by_id, cache)
    decisions = load_decisions()
    props, skips = decide(pages, cache, reg, rejections(decisions))
    write_candidates(candidates)
    write_review(props, skips, cache)
    print(len(candidates), "candidates;", sum(1 for c in candidates if c["matched"]), "match a verified paper")
    print("proposed:", len(props), "| skipped first mentions:", Counter(s[2] for s in skips))
    if "--apply" in argv:
        return apply(props, skips, pages, reg)
    if "--report" in argv:
        return report(props, skips)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
