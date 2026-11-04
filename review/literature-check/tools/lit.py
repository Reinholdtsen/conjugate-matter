#!/usr/bin/env python3
"""lit.py — literature tools for the conjecture literature check.

Every command caches what it fetches under work/literature-check/cache/, so agents share one another's fetches.
Standard library only. Run with any python3 (the repo's .venv works).

  lit.py search 'INSPIRE QUERY' [--size N] [--page P] [--sort mostrecent|mostcited] [--abstracts] [--full]
        INSPIRE-HEP search, one line per hit. INSPIRE syntax: t (title), a (author), abstracts.value:"...",
        fulltext "..." (full text of arXiv papers), refersto:recid:N, "and", "or", "not", quotes for phrases.
  lit.py show ID [ID ...]      full metadata and abstract; ID is an arXiv id (1506.02187, hep-th/9211021),
                               recid:NNN or doi:10.xxx. Saves a snapshot under cache/records/.
  lit.py cites ID [--size N] [--sort mostcited|mostrecent] [--abstracts]
                               papers that cite ID (INSPIRE citation graph, forward)
  lit.py refs ID               the references of ID (INSPIRE citation graph, backward)
  lit.py arxiv 'QUERY' [--size N] [--abstracts]
                               arXiv API search (covers cond-mat, math-ph, physics, which INSPIRE lacks).
                               arXiv syntax: all:, ti:, abs:, au:, AND, OR, ANDNOT, quoted phrases.
  lit.py crossref 'QUERY' [--size N]
                               Crossref search, for journal papers and books not on arXiv
  lit.py doi DOI [DOI ...]     Crossref metadata (and abstract, when Crossref has one) for a DOI
  lit.py openalex 'QUERY' [--size N] [--field default|title_and_abstract|title|fulltext] [--abstracts]
                               OpenAlex (250M works: journals, books, theses, proceedings beyond arXiv and
                               INSPIRE). Phrase search: --field title_and_abstract '"born reciprocity"'
  lit.py text ID [--grep REGEX ...] [--context N] [--max M]
                               full text of an arXiv paper (arxiv.org/html, then ar5iv), with each match in
                               context; without --grep, prints the length and the section headings
  lit.py quote ID 'VERBATIM QUOTE'
                               checks that the quote occurs in ID's abstract or full text, after normalizing
                               whitespace, case, quotation marks and dashes. Prints FOUND (where) or NOT FOUND;
                               "FOUND (loose)" means it matched only with punctuation and math stripped.
"""
import fcntl
import hashlib
import html
import html.parser
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(os.path.dirname(HERE), "cache")
UA = "conjugate-matter-literature-check/1.0 (research script; python urllib)"
INSPIRE = "https://inspirehep.net/api"
FIELDS = ("control_number,titles,authors.full_name,arxiv_eprints,publication_info,citation_count,"
          "abstracts,dois,earliest_date,document_type")
SPACING = {"api.openalex.org": 0.25, "arxiv.org": 3.0, "export.arxiv.org": 3.0, "ar5iv.labs.arxiv.org": 1.0, "inspirehep.net": 0.35,
           "api.crossref.org": 0.5}


# ---------------------------------------------------------------- fetching ---------------------------------------

def _throttle(host):
    """Space requests to one host across concurrent processes, with a lock file per host."""
    gap = SPACING.get(host, 0.5)
    os.makedirs(os.path.join(CACHE, "locks"), exist_ok=True)
    path = os.path.join(CACHE, "locks", host)
    with open(path, "a+") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        fh.seek(0)
        try:
            last = float(fh.read().strip() or 0)
        except ValueError:
            last = 0.0
        wait = last + gap - time.time()
        if wait > 0:
            time.sleep(wait)
        fh.seek(0)
        fh.truncate()
        fh.write(str(time.time()))
        fh.flush()
        fcntl.flock(fh, fcntl.LOCK_UN)


def _write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = f"{path}.tmp.{os.getpid()}"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(data)
    os.replace(tmp, path)


def fetch(url, kind, retries=6):
    """GET url as text, cached under cache/<kind>/<sha1>.  Returns (status, text)."""
    key = hashlib.sha1(url.encode()).hexdigest()
    path = os.path.join(CACHE, kind, key)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            blob = json.load(fh)
        return blob["status"], blob["text"]
    host = urllib.parse.urlparse(url).netloc
    delay = 2.0
    for attempt in range(retries):
        _throttle(host)
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                charset = resp.headers.get_content_charset() or "utf-8"
                text = raw.decode(charset, errors="replace")
                status = resp.status
        except urllib.error.HTTPError as e:
            status, text = e.code, ""
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            return 0, f"network error: {e}"
        break
    if status == 200 or status == 404:
        _write(path, json.dumps({"url": url, "status": status, "text": text}))
    return status, text


def inspire_json(path_and_query):
    status, text = fetch(f"{INSPIRE}/{path_and_query}", "inspire")
    if status != 200:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


# ---------------------------------------------------------------- formatting -------------------------------------

def _authors(meta, n=3):
    names = [a.get("full_name", "?") for a in meta.get("authors", [])]
    if not names:
        return "?"
    short = "; ".join(names[:n])
    return short + (f" et al. ({len(names)})" if len(names) > n else "")


def _year(meta):
    for key in ("earliest_date", "preprint_date"):
        if meta.get(key):
            return meta[key][:4]
    for pub in meta.get("publication_info", []) or []:
        if pub.get("year"):
            return str(pub["year"])
    return "?"


def _arxiv(meta):
    eps = meta.get("arxiv_eprints") or []
    return eps[0]["value"] if eps else ""


def _journal(meta):
    out = []
    for pub in meta.get("publication_info", []) or []:
        bits = [pub.get("journal_title", ""), pub.get("journal_volume", ""),
                pub.get("artid", "") or pub.get("page_start", ""), f"({pub['year']})" if pub.get("year") else ""]
        s = " ".join(b for b in bits if b)
        if s:
            out.append(s)
    return "; ".join(out)


def _abstract(meta):
    abs_ = meta.get("abstracts") or []
    for a in abs_:
        if a.get("source") == "arXiv":
            return a.get("value", "")
    return abs_[0].get("value", "") if abs_ else ""


def _line(meta):
    t = (meta.get("titles") or [{}])[0].get("title", "?")
    ax = _arxiv(meta)
    return (f"[{_year(meta)}] {_authors(meta)} — {t}"
            f"  | arXiv:{ax or '—'} recid:{meta.get('control_number')} cites:{meta.get('citation_count', '?')}")


def _print_hits(hits, abstracts, full):
    for i, h in enumerate(hits, 1):
        m = h["metadata"]
        print(f"{i:2d}. {_line(m)}")
        if abstracts or full:
            a = re.sub(r"\s+", " ", _abstract(m))
            print("    " + (a if full else a[:420] + ("…" if len(a) > 420 else "")))


# ---------------------------------------------------------------- commands ---------------------------------------

def _opts(args, spec):
    """Tiny option parser: spec maps --name to default (bool flags default False)."""
    vals = dict(spec)
    rest, i = [], 0
    while i < len(args):
        a = args[i]
        if a in spec:
            if isinstance(spec[a], bool):
                vals[a] = True
            else:
                vals[a] = type(spec[a])(args[i + 1]) if spec[a] is not None else args[i + 1]
                i += 1
        elif a == "--grep":
            vals.setdefault("--grep-list", []).append(args[i + 1])
            i += 1
        else:
            rest.append(a)
        i += 1
    return vals, rest


def cmd_search(args):
    o, rest = _opts(args, {"--size": 25, "--page": 1, "--sort": "mostrecent", "--abstracts": False, "--full": False})
    q = " ".join(rest)
    qs = urllib.parse.urlencode({"q": q, "size": o["--size"], "page": o["--page"], "sort": o["--sort"],
                                 "fields": FIELDS})
    d = inspire_json(f"literature?{qs}")
    if d is None:
        print("INSPIRE error (query syntax or network); query was:", q)
        return 1
    total = d["hits"]["total"]
    print(f"INSPIRE: {total} hits for: {q}  (showing page {o['--page']}, {len(d['hits']['hits'])} hits, "
          f"sort={o['--sort']})")
    _print_hits(d["hits"]["hits"], o["--abstracts"], o["--full"])
    return 0


def _resolve(ident):
    """Return INSPIRE metadata for an arXiv id, recid:N or doi:..., or None."""
    ident = ident.strip()
    if ident.startswith("recid:"):
        d = inspire_json(f"literature/{ident[6:]}")
    elif ident.startswith("doi:"):
        d = inspire_json(f"doi/{urllib.parse.quote(ident[4:], safe='/')}")
    else:
        ident = re.sub(r"^arxiv:", "", ident, flags=re.I)
        ident = re.sub(r"v\d+$", "", ident)
        d = inspire_json(f"arxiv/{ident}")
    return d["metadata"] if d and "metadata" in d else None


def _snapshot(ident, meta):
    keep = {k: meta.get(k) for k in ("control_number", "titles", "arxiv_eprints", "publication_info", "dois",
                                     "earliest_date", "citation_count", "document_type")}
    keep["authors"] = [a.get("full_name") for a in meta.get("authors", [])]
    keep["abstract"] = _abstract(meta)
    keep["queried_as"] = ident
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", ident)
    _write(os.path.join(CACHE, "records", safe + ".json"), json.dumps(keep, indent=1, ensure_ascii=False))
    return keep


def _arxiv_meta(ident):
    """Fallback for arXiv papers outside INSPIRE (cond-mat etc.): the arXiv API entry."""
    ident = re.sub(r"v\d+$", "", re.sub(r"^arxiv:", "", ident, flags=re.I))
    status, text = fetch("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ident}),
                         "arxivapi")
    if status != 200:
        return None
    entries = _parse_arxiv_feed(text)
    return entries[0] if entries and entries[0]["title"] else None


def cmd_show(args):
    rc = 0
    for ident in args:
        meta = _resolve(ident)
        if meta is None:
            am = _arxiv_meta(ident) if not ident.startswith(("recid:", "doi:")) else None
            if am is None:
                print(f"== {ident}: not found in INSPIRE (or arXiv)")
                rc = 1
                continue
            print(f"== {ident} (arXiv only, not in INSPIRE)")
            print(f"title:    {am['title']}\nauthors:  {'; '.join(am['authors'])}\nyear:     {am['year']}\n"
                  f"arXiv:    {am['id']}  categories: {am['cats']}\nabstract: {am['abstract']}\n")
            _write(os.path.join(CACHE, "records", re.sub(r"[^A-Za-z0-9._-]", "_", ident) + ".json"),
                   json.dumps({"queried_as": ident, "source": "arXiv API", **am}, indent=1, ensure_ascii=False))
            continue
        snap = _snapshot(ident, meta)
        t = (meta.get("titles") or [{}])[0].get("title", "?")
        print(f"== {ident}")
        print(f"title:    {t}")
        print(f"authors:  {'; '.join(snap['authors'][:12])}{' …' if len(snap['authors']) > 12 else ''}")
        print(f"year:     {_year(meta)}   type: {', '.join(meta.get('document_type') or [])}")
        print(f"journal:  {_journal(meta) or '—'}")
        print(f"doi:      {', '.join(d['value'] for d in (meta.get('dois') or [])) or '—'}")
        print(f"arXiv:    {_arxiv(meta) or '—'}   recid: {meta.get('control_number')}   "
              f"cites: {meta.get('citation_count')}")
        print(f"abstract: {re.sub(chr(10), ' ', snap['abstract'])}\n")
    return rc


def _recid(ident):
    meta = _resolve(ident)
    return meta.get("control_number") if meta else None


def cmd_cites(args):
    o, rest = _opts(args, {"--size": 25, "--page": 1, "--sort": "mostcited", "--abstracts": False, "--full": False})
    rid = _recid(rest[0])
    if rid is None:
        print("not found:", rest[0])
        return 1
    return cmd_search([f"refersto:recid:{rid}", "--size", str(o["--size"]), "--page", str(o["--page"]),
                       "--sort", o["--sort"]] + (["--abstracts"] if o["--abstracts"] else [])
                      + (["--full"] if o["--full"] else []))


def cmd_refs(args):
    d = inspire_json(f"literature?{urllib.parse.urlencode({'q': f'citedby:recid:{_recid(args[0])}', 'size': 250, 'fields': FIELDS})}")
    if d is None:
        print("not found:", args[0])
        return 1
    print(f"{d['hits']['total']} references of {args[0]} found in INSPIRE")
    _print_hits(d["hits"]["hits"], False, False)
    return 0


def _parse_arxiv_feed(text):
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    out = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return out
    for e in root.findall("a:entry", ns):
        get = lambda tag: (e.findtext(tag, default="", namespaces=ns) or "").strip()
        out.append({"id": get("a:id").rsplit("/abs/", 1)[-1], "title": re.sub(r"\s+", " ", get("a:title")),
                    "authors": [re.sub(r"\s+", " ", a.findtext("a:name", default="", namespaces=ns))
                                for a in e.findall("a:author", ns)],
                    "year": get("a:published")[:4], "abstract": re.sub(r"\s+", " ", get("a:summary")),
                    "cats": " ".join(c.get("term", "") for c in e.findall("a:category", ns)),
                    "journal": get("x:journal_ref"), "doi": get("x:doi")})
    return out


def cmd_arxiv(args):
    o, rest = _opts(args, {"--size": 25, "--abstracts": False, "--full": False})
    q = " ".join(rest)
    status, text = fetch("https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "start": 0, "max_results": o["--size"], "sortBy": "relevance"}), "arxivapi")
    if status != 200:
        print("arXiv API error", status)
        return 1
    m = re.search(r"<opensearch:totalResults[^>]*>(\d+)<", text)
    entries = _parse_arxiv_feed(text)
    print(f"arXiv: {m.group(1) if m else '?'} hits for: {q}  (showing {len(entries)})")
    for i, e in enumerate(entries, 1):
        au = "; ".join(e["authors"][:3]) + (f" et al. ({len(e['authors'])})" if len(e["authors"]) > 3 else "")
        print(f"{i:2d}. [{e['year']}] {au} — {e['title']}  | arXiv:{re.sub(r'v[0-9]+$', '', e['id'])} "
              f"[{e['cats'].split(' ')[0]}]" + (f" | {e['journal']}" if e["journal"] else ""))
        if o["--abstracts"] or o["--full"]:
            a = e["abstract"]
            print("    " + (a if o["--full"] else a[:420] + ("…" if len(a) > 420 else "")))
    return 0


def cmd_crossref(args):
    o, rest = _opts(args, {"--size": 20})
    q = " ".join(rest)
    status, text = fetch("https://api.crossref.org/works?" + urllib.parse.urlencode(
        {"query": q, "rows": o["--size"], "select": "DOI,title,author,issued,container-title,type"}), "crossref")
    if status != 200:
        print("Crossref error", status)
        return 1
    items = json.loads(text)["message"]["items"]
    print(f"Crossref: {len(items)} items for: {q}")
    for i, it in enumerate(items, 1):
        au = "; ".join(f"{a.get('given', '')} {a.get('family', '')}".strip() for a in (it.get("author") or [])[:3])
        yr = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        print(f"{i:2d}. [{yr}] {au or '?'} — {(it.get('title') or ['?'])[0]}  | "
              f"{(it.get('container-title') or [''])[0]} | doi:{it.get('DOI')} | {it.get('type')}")
    return 0


def _openalex_abstract(inv):
    if not inv:
        return ""
    pos = sorted((i, w) for w, idx in inv.items() for i in idx)
    return " ".join(w for _, w in pos)


def cmd_openalex(args):
    """OpenAlex: journals, books, theses and proceedings beyond arXiv and INSPIRE.
    --field default|title_and_abstract|title|fulltext  (default: relevance search over all fields)."""
    o, rest = _opts(args, {"--size": 25, "--field": "default", "--abstracts": False, "--full": False,
                           "--sort": "relevance"})
    q = " ".join(rest)
    params = {"per-page": o["--size"], "select": "id,doi,title,publication_year,authorships,primary_location,"
              "cited_by_count,type,abstract_inverted_index,ids"}
    if o["--field"] == "default":
        params["search"] = q
    else:
        params["filter"] = f"{o['--field']}.search:{q}"
    if o["--sort"] == "mostcited":
        params["sort"] = "cited_by_count:desc"
    status, text = fetch("https://api.openalex.org/works?" + urllib.parse.urlencode(params), "openalex")
    if status != 200:
        print("OpenAlex error", status)
        return 1
    d = json.loads(text)
    print(f"OpenAlex: {d['meta']['count']} works for: {q}  (field={o['--field']}, showing {len(d['results'])})")
    for i, w in enumerate(d["results"], 1):
        au = "; ".join(a["author"]["display_name"] for a in (w.get("authorships") or [])[:3])
        n = len(w.get("authorships") or [])
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "—"
        ax = (w.get("ids") or {}).get("arxiv") or ""
        print(f"{i:2d}. [{w.get('publication_year')}] {au}{f' et al. ({n})' if n > 3 else ''} — {w.get('title')}  | "
              f"{src} | {w.get('type')} | doi:{(w.get('doi') or '—').replace('https://doi.org/', '')}"
              f"{' | ' + ax if ax else ''} | cites:{w.get('cited_by_count')}")
        if o["--abstracts"] or o["--full"]:
            a = _openalex_abstract(w.get("abstract_inverted_index"))
            print("    " + (a if o["--full"] else a[:420] + ("…" if len(a) > 420 else "")) if a else "    (no abstract)")
    return 0


def crossref_work(doi):
    """Crossref metadata for a DOI: dict with title, authors, year, container, type, abstract; or None."""
    doi = re.sub(r"^doi:", "", doi.strip(), flags=re.I)
    status, text = fetch(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/')}", "crossref")
    if status != 200:
        return None
    it = json.loads(text)["message"]
    abstract = re.sub(r"<[^>]+>", " ", it.get("abstract") or "")
    return {"doi": doi, "title": (it.get("title") or ["?"])[0],
            "authors": [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in (it.get("author") or [])],
            "year": ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0],
            "container": (it.get("container-title") or [""])[0], "type": it.get("type"),
            "abstract": re.sub(r"\s+", " ", html.unescape(abstract)).strip()}


def cmd_doi(args):
    rc = 0
    for d in args:
        w = crossref_work(d)
        if w is None:
            print(f"== {d}: not found in Crossref")
            rc = 1
            continue
        _write(os.path.join(CACHE, "records", re.sub(r"[^A-Za-z0-9._-]", "_", "doi:" + w["doi"]) + ".json"),
               json.dumps({"queried_as": d, "source": "Crossref", **w}, indent=1, ensure_ascii=False))
        print(f"== doi:{w['doi']} (Crossref)\ntitle:    {w['title']}\nauthors:  {'; '.join(w['authors'])}\n"
              f"year:     {w['year']}   type: {w['type']}\njournal:  {w['container']}\n"
              f"abstract: {w['abstract'] or '— (Crossref has none; read the publisher page with WebFetch)'}\n")
    return rc


class _Text(html.parser.HTMLParser):
    SKIP = {"script", "style", "nav", "header", "footer", "button"}
    BLOCK = {"p", "div", "section", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "br", "table", "figcaption",
             "blockquote", "dd", "dt"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip, self.heads, self._h = [], 0, [], None

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        if tag == "math":
            alt = dict(attrs).get("alttext")
            if alt:
                self.parts.append(f" {alt} ")
            self.skip += 1
        if tag in self.BLOCK:
            self.parts.append("\n")
        if tag in ("h1", "h2", "h3", "h4"):
            self._h = []

    def handle_endtag(self, tag):
        if tag in self.SKIP or tag == "math":
            self.skip = max(0, self.skip - 1)
        if tag in ("h1", "h2", "h3", "h4") and self._h is not None:
            self.heads.append(re.sub(r"\s+", " ", "".join(self._h)).strip())
            self._h = None
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.skip:
            return
        self.parts.append(data)
        if self._h is not None:
            self._h.append(data)


def fulltext(ident):
    """Return (source_url, text, headings) for an arXiv paper, or (None, reason, [])."""
    ident = re.sub(r"v\d+$", "", re.sub(r"^arxiv:", "", ident, flags=re.I))
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", ident)
    tpath = os.path.join(CACHE, "text", safe + ".json")
    if os.path.exists(tpath):
        with open(tpath, encoding="utf-8") as fh:
            blob = json.load(fh)
        return blob["url"], blob["text"], blob["heads"]
    for url in (f"https://arxiv.org/html/{ident}", f"https://ar5iv.labs.arxiv.org/html/{ident}"):
        status, page = fetch(url, "html")
        if status != 200 or len(page) < 5000 or "ltx_document" not in page and "ltx_page_main" not in page:
            continue
        p = _Text()
        p.feed(page)
        text = re.sub(r"[ \t\r\f\v]+", " ", "".join(p.parts))
        text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
        if len(text) < 2000:
            continue
        _write(tpath, json.dumps({"url": url, "text": text, "heads": p.heads}, ensure_ascii=False))
        return url, text, p.heads
    return None, ("no HTML full text (arxiv.org/html and ar5iv both failed); read the PDF with WebFetch "
                  f"https://arxiv.org/pdf/{ident} and mark the quote 'checked by WebFetch only'"), []


def cmd_text(args):
    o, rest = _opts(args, {"--context": 300, "--max": 12})
    url, text, heads = fulltext(rest[0])
    if url is None:
        print(text)
        return 1
    print(f"full text of {rest[0]} from {url}: {len(text)} characters")
    pats = o.get("--grep-list", [])
    if not pats:
        print("headings:", " | ".join(h for h in heads if h)[:3000])
        return 0
    flat = re.sub(r"\s+", " ", text)
    for pat in pats:
        ms = list(re.finditer(pat, flat, flags=re.I))
        print(f"\n--- /{pat}/: {len(ms)} matches" + (f" (showing {o['--max']})" if len(ms) > o["--max"] else ""))
        for m in ms[:o["--max"]]:
            a, b = max(0, m.start() - o["--context"]), min(len(flat), m.end() + o["--context"])
            print(f"  …{flat[a:b]}…\n")
    return 0


def norm(s):
    s = re.sub(r"</?(?:i|b|em|strong|sub|sup|span|p|br|math|jats:[a-z]+)\b[^>]*>", "", s)
    s = unicodedata.normalize("NFKC", html.unescape(s))
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"),
                 ("—", "-"), ("−", "-"), (" ", " "), ("``", '"'), ("''", '"')):
        s = s.replace(a, b)
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def loose(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", norm(s)) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.replace("ł", "l").replace("ø", "o").replace("đ", "d"))


def check_quote(ident, quote):
    """Return (verdict, where, context) for a verbatim quote from ident's abstract or full text."""
    nq, lq = norm(quote), loose(quote)
    texts = []
    meta = _resolve(ident)
    if meta:
        texts.append(("abstract", _abstract(meta)))
        _snapshot(ident, meta)
    else:
        am = _arxiv_meta(ident) if not ident.startswith(("recid:", "doi:")) else None
        if am:
            texts.append(("abstract (arXiv API)", am["abstract"]))
        if ident.startswith("doi:"):
            w = crossref_work(ident)
            if w and w["abstract"]:
                texts.append(("abstract (Crossref)", w["abstract"]))
    ax = _arxiv(meta) if meta else (None if ident.startswith(("recid:", "doi:")) else ident)
    if ax:
        url, text, _ = fulltext(ax)
        if url:
            texts.append((f"full text ({url})", text))
    for where, t in texts:
        nt = norm(t)
        k = nt.find(nq)
        if k >= 0:
            return "FOUND", where, nt[max(0, k - 120):k + len(nq) + 120]
    for where, t in texts:
        if lq and lq in loose(t):
            return "FOUND (loose)", where, ""
    return "NOT FOUND", ", ".join(w for w, _ in texts) or "no text available", ""


def cmd_quote(args):
    ident, quote = args[0], " ".join(args[1:])
    verdict, where, ctx = check_quote(ident, quote)
    print(f"{verdict}: {ident} — searched {where}")
    if ctx:
        print(f"  context: …{ctx}…")
    return 0 if verdict.startswith("FOUND") else 2


COMMANDS = {"search": cmd_search, "show": cmd_show, "cites": cmd_cites, "refs": cmd_refs, "arxiv": cmd_arxiv,
            "crossref": cmd_crossref, "doi": cmd_doi, "openalex": cmd_openalex, "text": cmd_text,
            "quote": cmd_quote}

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        sys.exit(1)
    sys.exit(COMMANDS[sys.argv[1]](sys.argv[2:]))
