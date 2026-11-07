#!/usr/bin/env python3
"""Maintain scripts/wiki-papers.tsv, the registry of the papers the wiki links to.

The wiki links every paper it cites by an identifier to the paper itself (wiki/CLAUDE.md, Links): an arXiv
identifier to its abstract page, a DOI to doi.org, an INSPIRE record to inspirehep.net, a handle to
hdl.handle.net. scripts/check-wiki.py checks each such link offline, against this registry: the identifier must be
registered, and the link's label must name the identifier or else the registered first author's surname, with any
year in it a registered year, so that a link cannot point at another paper unnoticed. This script fills the registry from INSPIRE, arXiv and Crossref. It needs
the network; the gate does not.

  scripts/wiki-papers.py              add every identifier the wiki cites that the registry lacks
  scripts/wiki-papers.py ID ...       add these identifiers (arXiv:2003.00318, doi:10.x/y, recid:N, hdl:H)
  scripts/wiki-papers.py --recheck    look every registered identifier up again and report what differs

Columns of the registry, tab-separated: id, surname (the first author's, or a collaboration's name), years (the
first public year, then any later year of publication), title, source, retrieved (date). A row may be edited by
hand only to add an alias to the surname column, as "Aghanim|Planck", when the wiki cites a paper by another name;
the gate accepts any of the names.
"""

import datetime
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
REGISTRY = ROOT / "scripts" / "wiki-papers.tsv"
COLUMNS = ("id", "surname", "years", "title", "source", "retrieved")
UA = "conjugate-matter-wiki-papers/1.0 (research script; python urllib)"
GAP = {"inspirehep.net": 0.4, "export.arxiv.org": 3.1, "api.crossref.org": 0.6}
_last = {}

# An identifier as the wiki writes it in prose. Kept in step with PAPER_ID_RE in scripts/check-wiki.py.
ID_RE = re.compile(
    r"\barXiv:((?:[a-z][a-z\-]*(?:\.[A-Z]{2})?/\d{7})|\d{4}\.\d{4,5})(?:v\d+)?"
    r"|\bdoi:(10\.\d{4,9}/[^\s,;)\]]*[^\s,;)\].])"
    r"|\bhandle (\d+(?:\.\d+)*/\d+)"
    r"|(?<![\w/.:\-])((?:astro-ph|hep-th|hep-ph|hep-lat|hep-ex|gr-qc|cond-mat|math-ph|quant-ph|nucl-th|nucl-ex"
    r"|physics|math)(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?\b",
    re.I,
)


def norm_id(kind, value):
    if kind == "arxiv":
        return "arXiv:" + value
    if kind == "doi":
        return "doi:" + value.lower()
    if kind == "hdl":
        return "hdl:" + value
    return "recid:" + value


def parse_arg(arg):
    m = re.match(r"^(arxiv|doi|recid|hdl):(.+)$", arg, re.I)
    if not m:
        sys.exit(f"not an identifier: {arg} (write arXiv:…, doi:…, recid:… or hdl:…)")
    return norm_id(m.group(1).lower(), m.group(2))


def fetch(url):
    host = urllib.parse.urlparse(url).netloc
    wait = _last.get(host, 0) + GAP.get(host, 0.6) - time.time()
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, */*"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                _last[host] = time.time()
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            _last[host] = time.time()
            if e.code in (404, 400):
                return e.code, ""
            time.sleep(3 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(3 * (attempt + 1))
    return 0, ""


def surname_of(full):
    full = full.strip()
    if "," in full:
        return full.split(",", 1)[0].strip()
    return full.split()[-1] if full.split() else full


def from_inspire(meta, source):
    titles = meta.get("titles") or [{}]
    authors = meta.get("authors") or []
    collab = [c.get("value") for c in meta.get("collaborations") or [] if c.get("value")]
    surname = surname_of(authors[0]["full_name"]) if authors else (collab[0] if collab else "")
    years = []
    if meta.get("earliest_date"):
        years.append(meta["earliest_date"][:4])
    for p in meta.get("publication_info") or []:
        if p.get("year"):
            years.append(str(p["year"]))
    return {"surname": surname, "years": years, "title": titles[0].get("title", ""), "source": source}


def arxiv_year(value):
    """The year an arXiv identifier was assigned: 1502.08005 is 2015, hep-th/9211021 is 1992."""
    m = re.match(r"^(?:(\d{2})\d{2}\.|[a-zA-Z.\-]+/(\d{2}))", value)
    yy = int(m.group(1) or m.group(2)) if m else None
    return None if yy is None else str(1900 + yy if yy >= 91 else 2000 + yy)


def lookup(pid):
    got = _lookup(pid)
    kind, _, value = pid.partition(":")
    if got is not None and kind == "arXiv" and arxiv_year(value):
        got["years"] = [arxiv_year(value)] + [y for y in got["years"] if y != arxiv_year(value)]
    if got is not None and kind == "doi" and not got["years"]:
        st, text = fetch("https://api.crossref.org/works/" + urllib.parse.quote(value, safe="/"))
        if st == 200 and text:
            msg = json.loads(text)["message"]
            for key in ("published-online", "published-print", "issued"):
                parts = (msg.get(key) or {}).get("date-parts") or [[None]]
                if parts[0] and parts[0][0] and str(parts[0][0]) not in got["years"]:
                    got["years"].append(str(parts[0][0]))
    return got


def _lookup(pid):
    kind, _, value = pid.partition(":")
    if kind == "arXiv":
        st, text = fetch(f"https://inspirehep.net/api/arxiv/{value}")
        if st == 200 and text:
            return from_inspire(json.loads(text)["metadata"], "INSPIRE")
        st, text = fetch("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": value}))
        if st == 200 and text:
            ns = {"a": "http://www.w3.org/2005/Atom"}
            entry = ET.fromstring(text).find("a:entry", ns)
            if entry is not None and entry.findtext("a:title", "", ns).strip():
                names = [a.findtext("a:name", "", ns) for a in entry.findall("a:author", ns)]
                jref = entry.findtext("{http://arxiv.org/schemas/atom}journal_ref", "") or ""
                years = [entry.findtext("a:published", "", ns)[:4]] + re.findall(r"\((\d{4})\)", jref)
                return {"surname": surname_of(names[0]) if names else "",
                        "years": years,
                        "title": " ".join(entry.findtext("a:title", "", ns).split()), "source": "arXiv"}
        return None
    if kind == "recid":
        st, text = fetch(f"https://inspirehep.net/api/literature/{value}")
        return from_inspire(json.loads(text)["metadata"], "INSPIRE") if st == 200 and text else None
    if kind == "doi":
        st, text = fetch("https://inspirehep.net/api/doi/" + urllib.parse.quote(value, safe="/"))
        if st == 200 and text:
            return from_inspire(json.loads(text)["metadata"], "INSPIRE")
        st, text = fetch("https://api.crossref.org/works/" + urllib.parse.quote(value, safe="/"))
        if st == 200 and text:
            msg = json.loads(text)["message"]
            authors = msg.get("author") or []
            first = authors[0] if authors else {}
            years = []
            for key in ("published-print", "published-online", "issued"):
                parts = (msg.get(key) or {}).get("date-parts") or [[None]]
                if parts[0] and parts[0][0]:
                    years.append(str(parts[0][0]))
            return {"surname": first.get("family") or first.get("name", ""), "years": sorted(set(years)),
                    "title": " ".join((msg.get("title") or [""])[0].split()), "source": "Crossref"}
        return None
    return None  # handles are registered by hand: hdl.handle.net has no metadata API


def read_registry():
    rows = {}
    if REGISTRY.exists():
        for line in REGISTRY.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            cells = line.split("\t")
            rows[cells[0]] = dict(zip(COLUMNS, cells + [""] * (len(COLUMNS) - len(cells))))
    return rows


def write_registry(rows):
    head = ("# The papers the wiki links to. Built by scripts/wiki-papers.py from INSPIRE, arXiv and Crossref;\n"
            "# checked offline by scripts/check-wiki.py. Columns: " + ", ".join(COLUMNS) + ".\n")
    body = "".join("\t".join(r[c] for c in COLUMNS) + "\n" for _, r in sorted(rows.items(), key=lambda kv: kv[0].lower()))
    REGISTRY.write_text(head + body, encoding="utf-8")


def wiki_ids():
    found = set()
    link_re = re.compile(r"\]\((https?://[^)\s]+)\)")
    for f in WIKI.rglob("*.md"):
        if f.name == "CLAUDE.md":
            continue
        text = f.read_text(encoding="utf-8")
        for m in ID_RE.finditer(text):
            if m.group(1) or m.group(4):
                found.add(norm_id("arxiv", m.group(1) or m.group(4)))
            elif m.group(2):
                found.add(norm_id("doi", m.group(2)))
            elif m.group(3):
                found.add(norm_id("hdl", m.group(3)))
        for m in link_re.finditer(text):
            pid = id_of_url(m.group(1))
            if pid:
                found.add(pid)
    return found


def id_of_url(url):
    """The registry id a paper link points at, or None. Kept in step with scripts/check-wiki.py."""
    m = re.match(r"^https://arxiv\.org/abs/([^\s?#]+?)(?:v\d+)?$", url)
    if m:
        return "arXiv:" + m.group(1)
    m = re.match(r"^https://doi\.org/(10\.[^\s?#]+)$", url)
    if m:
        return "doi:" + urllib.parse.unquote(m.group(1)).lower()
    m = re.match(r"^https://inspirehep\.net/literature/(\d+)$", url)
    if m:
        return "recid:" + m.group(1)
    m = re.match(r"^https://hdl\.handle\.net/([^\s?#]+)$", url)
    if m:
        return "hdl:" + m.group(1)
    return None


def main(argv):
    rows = read_registry()
    today = datetime.date.today().isoformat()
    if argv and argv[0] == "--recheck":
        bad = 0
        for pid, row in sorted(rows.items()):
            if pid.startswith("hdl:"):
                continue
            got = lookup(pid)
            if got is None:
                print(f"{pid}: no longer resolves")
                bad += 1
            elif got["surname"] not in row["surname"].split("|") or got["title"] != row["title"]:
                print(f"{pid}: registry {row['surname']!r} {row['title']!r}; now {got['surname']!r} {got['title']!r}")
                bad += 1
        print(f"rechecked {len(rows)}; {bad} differ")
        return 1 if bad else 0
    wanted = {parse_arg(a) for a in argv} if argv else wiki_ids()
    missing = sorted(p for p in wanted if p not in rows)
    failed = []
    for pid in missing:
        if pid.startswith("hdl:"):
            failed.append(pid + " (a handle: add its row by hand from the repository page)")
            continue
        got = lookup(pid)
        if got is None:
            failed.append(pid)
            continue
        years = []
        for y in got["years"]:
            if y and y not in years:
                years.append(y)
        rows[pid] = {"id": pid, "surname": got["surname"], "years": ",".join(years), "title": got["title"],
                     "source": got["source"], "retrieved": today}
        print(f"added {pid}: {got['surname']} ({','.join(years)}) {got['title'][:70]}")
    write_registry(rows)
    for pid in failed:
        print(f"NOT FOUND {pid}")
    print(f"{len(missing) - len(failed)} added, {len(failed)} not found, {len(rows)} registered")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
