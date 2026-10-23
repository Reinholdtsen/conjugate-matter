#!/usr/bin/env python3
r"""Verify the wiki in wiki/ against the rules in wiki/CLAUDE.md.

Checks, in order of severity:

  link         an internal link points at a wiki page that does not exist, or
               is not an absolute /wiki/ link
  anchor       a link points at a heading that does not exist
  map          a page is not linked from its parent section's _index.md
  source       a frontmatter `sources` entry, or an inline-code repo path in the
               body, names a file that does not exist
  frontmatter  missing or invalid title, weight, status, description, sources
               (pages), or bookCollapseSection (sections)
  weight       two siblings share a weight
  section      a folder under wiki/ has no _index.md, or a file is named claude.md
  gist         the body does not open with an italic plain-language passage
  statusline   a page that is not a section index has no **Status:** line
  star         an unescaped starred symbol such as v* or M*, whose asterisk can
               close an emphasis span (an italic opening ends early); write v\*
  h1           the body contains an `# H1` (hugo-book renders the title as h1)
  fence        a fenced code block declares no language
  acronym      an acronym is unregistered, or a page uses it without spelling it
               out beside a use or linking it (registry: scripts/wiki-acronyms.txt)

Hugo does not validate internal links: it renders /wiki/does-not-exist without
complaint. This script catches a dead link in the Markdown, before any build. The
site in site/ adds two later layers: hugo-book's BookPortableLinks = 'error' fails
the build on a link to a missing page, and scripts/check-site.py checks every link
and #fragment in the built HTML (see site/CLAUDE.md).

Anchors are checked against heading IDs computed the way Hugo computes them (see
slugify). That is an emulation; the built-site check is the authority on the IDs
Hugo actually writes.

Exit status is 1 if any error is found, 0 otherwise.

Usage:
  scripts/check-wiki.py              # check everything
  scripts/check-wiki.py FILE...      # report only on these files (links still
                                     # resolve wiki-wide)
  scripts/check-wiki.py --stats      # also print status counts and link density
"""

import csv
import html
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ACRONYMS_FILE = ROOT / "scripts" / "wiki-acronyms.txt"

STATUSES = {
    "established", "alive", "conjecture", "open", "dead",
    "superseded", "method", "record", "hub",
}

FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
# Markdown inline links: [text](target). Image links (![...]) are skipped. The
# text may hold one level of brackets, as in [The polarization frame E₀[J]](...);
# a pattern that stopped at the first ']' would never see such a link.
LINK_LABEL = r"(?:[^\[\]]|\[[^\[\]]*\])*"
LINK_RE = re.compile(r"(?<!!)\[" + LINK_LABEL + r"\]\(\s*([^)\s]+?)\s*(?:\"[^\"]*\")?\)")
LINK_LABEL_RE = re.compile(r"(?<!!)\[(" + LINK_LABEL + r")\]\([^)]*\)")
INLINE_CODE_RE = re.compile(r"`([^`]*)`")
# A candidate acronym: an all-caps run of 2-6 characters with at least two
# letters, optionally pluralized ("UFDs" -> UFD). Version tags and the
# provenance tags ([D], [T], ...) have one letter and are skipped.
ACRONYM_RE = re.compile(r"\b([A-Z][A-Z0-9]{1,5})(?:es|s)?\b")
# A one-letter symbol followed by an unescaped asterisk (v*, M*, g*). In
# Markdown that asterisk can close an emphasis span, so inside an italic
# passage it ends the italics early.
STARRED_RE = re.compile(r"(?<![\\*\w])([A-Za-zα-ωΑ-Ω])\*(?!\*)")
# Inline code that names a file in this repository.
REPO_PATH_RE = re.compile(
    r"^(?:(?:papers|notes|popsci|review|verify|scripts|wiki)/[^\s*?]+"
    r"|HANDOFF\.md|CLAUDE\.md|README\.md|requirements\.txt)$"
)
# How far apart an acronym and its spelled-out form may sit and still read as
# a definition: wide enough for "Foo Bar (FB)" and a parenthetical aside, too
# narrow for the expansion to be in another paragraph.
BIND_WINDOW = 180

# Heading markup, as slugify strips it. A code span is `code` or ``co`de``.
CODE_SPAN_RE = re.compile(r"(`+)(.+?)(?<!`)\1(?!`)")
HTML_TAG_RE = re.compile(r"<!--.*?-->|</?[A-Za-z][A-Za-z0-9-]*(?:\s[^<>]*)?/?>")
NAMED_ENTITY_RE = re.compile(r"&[A-Za-z][A-Za-z0-9]*;")
LINK_OR_IMAGE_RE = re.compile(r"!?\[(" + LINK_LABEL + r")\]\([^)]*\)")
# An emphasis pair of underscores, _text_ or __text__. CommonMark opens one only
# where the underscore does not follow a letter or digit and closes it only where
# it is not followed by one, so G_eff, and an unpaired U(1)_d, stay text.
UNDERSCORE_PAIR_RE = re.compile(r"(?<![^\W_])(_+)(?=\S)(.+?)(?<=\S)\1(?![^\W_])")
ESCAPED_UNDERSCORE = "\x00"  # stands in for \_ while emphasis pairs are removed


def load_acronyms():
    """Return {ACRONYM: expansion or None}. None means no expansion needed."""
    reg = {}
    if not ACRONYMS_FILE.exists():
        return reg
    for raw in ACRONYMS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        acro, _, exp = line.partition("\t")
        exp = exp.strip()
        reg[acro.strip()] = None if exp in ("", "-") else exp
    return reg


def normalize(text):
    """Lowercase, fold -ise/-ize, flatten non-alphanumerics to single spaces."""
    text = text.lower().replace("isation", "ization").replace("ise", "ize")
    return re.sub(r"[\W_]+", " ", text)


def binds(page_text, acro, expansion):
    """True if some use of `acro` sits within BIND_WINDOW of its expansion."""
    want = normalize(expansion)
    for m in re.finditer(r"\b" + re.escape(acro) + r"(?:es|s)?\b", page_text):
        lo = max(0, m.start() - BIND_WINDOW)
        if want in normalize(page_text[lo : m.end() + BIND_WINDOW]):
            return True
    return False


def unquote(val):
    val = val.strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
        return val[1:-1]
    return val


def parse_frontmatter(lines):
    """Parse the YAML subset the wiki uses: scalars, inline and block lists."""
    data, errors, key = {}, [], None
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m and not raw[0].isspace():
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                data[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                data[key] = (
                    [unquote(x) for x in next(csv.reader([inner], skipinitialspace=True))]
                    if inner else []
                )
            else:
                data[key] = unquote(val)
            continue
        m = re.match(r"^\s+-\s+(.*)$", raw)
        if m and key is not None and isinstance(data.get(key), list):
            data[key].append(unquote(m.group(1)))
            continue
        errors.append(raw.strip())
    return data, errors


def split_frontmatter(text):
    """Return (frontmatter_lines, body_lines, body_offset) or ([], lines, 1)."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[1:i], lines[i + 1 :], i + 2
    return [], lines, 1


def strip_code(body_lines, offset):
    """Return ([(lineno, line)] outside fences, [(lineno, info)] fence opens)."""
    out, fences, fence = [], [], None
    for idx, line in enumerate(body_lines):
        lineno = offset + idx
        m = FENCE_RE.match(line)
        if m:
            marker, info = m.group(2), m.group(3).strip()
            if fence is None:
                fence = marker[0], len(marker)
                fences.append((lineno, info))
                continue
            if marker[0] == fence[0] and len(marker) >= fence[1] and not info:
                fence = None
                continue
        if fence is None:
            out.append((lineno, line))
    return out, fences


def _heading_text(text):
    """Markdown outside code spans, reduced to the text Hugo slugs."""
    text = text.replace("\\_", ESCAPED_UNDERSCORE)
    # Goldmark's typographer turns << >> into guillemets before raw HTML is parsed.
    text = text.replace("<<", "«").replace(">>", "»")
    text = HTML_TAG_RE.sub("", text)
    # Named entities are resolved (&amp; is '&'); numeric ones stay as typed.
    text = NAMED_ENTITY_RE.sub(lambda m: html.unescape(m.group(0)), text)
    text = LINK_OR_IMAGE_RE.sub(r"\1", text)
    text = UNDERSCORE_PAIR_RE.sub(r"\2", text)
    # The typographer turns --- into an em dash and -- into an en dash, which are
    # then dropped; a single - stays.
    text = re.sub(r"---|--", "", text)
    return text.replace(ESCAPED_UNDERSCORE, "_")


def slugify(text):
    """Hugo's default heading ID (autoHeadingIDType "github") for a heading's Markdown.

    Hugo slugs the heading's rendered text: markup is gone, code-span content and
    link text stay. Each character is then kept if it is a letter of any script
    (str.isalpha(): ₐ, ℤ and Greek stay), a decimal digit (category Nd only, so
    subscript and superscript digits such as ₀ ² ⁴ and the superscript minus are
    dropped), '-' or '_', and lowercased one character at a time; each space
    (U+0020 only, not a tab or a no-break space) becomes '-', runs not collapsed;
    everything else is dropped. Underscores are dropped only where they pair up as
    emphasis (_text_); U(1)_d gives u1_d. '*' and '~' markup falls to the filter.

    Checked against Hugo 0.159 and 0.168 (2026-10-22): every wiki heading's ID,
    and a set of edge cases (entities, raw HTML, padded code, duplicates). One
    known divergence: inside emphasis or link text, Hugo loses the text after a
    typographer dash or a literal underscore ([a--b](...) gives 'a'). No wiki
    heading has emphasis or a link; scripts/check-site.py would catch one.
    """
    parts, pos = [], 0
    for m in CODE_SPAN_RE.finditer(text):
        parts.append(_heading_text(text[pos : m.start()]))
        code = m.group(2)
        # CommonMark strips one space from each end of padded code: `` `a` ``.
        if code.startswith(" ") and code.endswith(" ") and code.strip(" "):
            code = code[1:-1]
        parts.append(code)
        pos = m.end()
    parts.append(_heading_text(text[pos:]))
    slug = []
    for ch in "".join(parts).strip():
        if ch in " -":
            slug.append("-")
        elif ch == "_" or ch.isalpha() or unicodedata.category(ch) == "Nd":
            slug.append(ch.lower())
    return "".join(slug)


def heading_id(slug, used):
    """Hugo's de-duplication: a heading whose slug is empty is 'heading', and a
    taken ID gets the first free suffix -1, -2, ... Records the result in `used`."""
    slug = slug or "heading"
    if slug in used:
        n = 1
        while f"{slug}-{n}" in used:
            n += 1
        slug = f"{slug}-{n}"
    used.add(slug)
    return slug


def page_url(path):
    """Map a wiki file to the URL it serves at (no trailing slash)."""
    rel = path.relative_to(WIKI).with_suffix("")
    parts = ["wiki"] + list(rel.parts)
    if parts[-1] == "_index":
        parts.pop()
    return "/" + "/".join(parts)


def parent_index(path):
    """The _index.md whose map must link to this file (None for the home page)."""
    if path == WIKI / "_index.md":
        return None
    folder = path.parent.parent if path.name == "_index.md" else path.parent
    return folder / "_index.md"


def prose(line):
    """A line as a reader sees it: inline code and link targets removed."""
    line = INLINE_CODE_RE.sub(" ", line)
    return LINK_LABEL_RE.sub(lambda m: m.group(1), line)


def main(argv):
    stats = "--stats" in argv
    argv = [a for a in argv if a != "--stats"]
    if not WIKI.is_dir():
        print("wiki OK — no wiki/ directory")
        return 0

    registry = load_acronyms()
    errors = []

    def err(kind, path, lineno, msg):
        errors.append((kind, path.relative_to(ROOT), lineno, msg))

    files = sorted(p for p in WIKI.rglob("*.md") if p.name != "CLAUDE.md")
    for p in WIKI.rglob("*"):
        if p.is_file() and p.name.lower() == "claude.md" and p.name != "CLAUDE.md":
            err("section", p, 1, "a page named claude.md collides with CLAUDE.md under Hugo's case folding")
        if p.is_dir() and not (p / "_index.md").exists():
            err("section", p, 1, "folder has no _index.md")
    if not (WIKI / "_index.md").exists():
        err("section", WIKI, 1, "wiki/_index.md (the home page) is missing")

    pages, parsed = {}, {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm_lines, body, offset = split_frontmatter(text)
        fm, fm_errors = parse_frontmatter(fm_lines)
        clean, fences = strip_code(body, offset)
        anchors = set()
        for _, line in clean:
            m = HEADING_RE.match(line)
            if m and m.group(2).strip():
                heading_id(slugify(m.group(2)), anchors)
        url = page_url(f)
        pages[url] = {"anchors": anchors, "path": f}
        parsed[f] = (fm, fm_lines, fm_errors, clean, fences)

    targets = set(parsed)
    if argv:
        wanted = {Path(a).resolve() for a in argv}
        targets = {f for f in parsed if f in wanted}

    outbound = {}  # page path -> set of target urls (other pages)
    for f in parsed:
        _, _, _, clean, _ = parsed[f]
        links = set()
        for _, line in clean:
            for target in LINK_RE.findall(INLINE_CODE_RE.sub(" ", line)):
                if target.startswith("/wiki"):
                    base = "/" + target.partition("#")[0].strip("/")
                    if base != page_url(f):
                        links.add(base)
        outbound[f] = links

    siblings = {}  # folder -> [(weight, path)]
    for f, (fm, *_rest) in parsed.items():
        w = fm.get("weight")
        if isinstance(w, str) and re.fullmatch(r"-?\d+", w):
            folder = f.parent.parent if f.name == "_index.md" else f.parent
            if f == WIKI / "_index.md":
                continue
            siblings.setdefault(folder, []).append((int(w), f))
    dup_weight = set()
    for folder, items in siblings.items():
        by_w = {}
        for w, f in items:
            by_w.setdefault(w, []).append(f)
        for w, fs in by_w.items():
            if len(fs) > 1:
                dup_weight.update((f, w, tuple(sorted(x.name for x in fs))) for f in fs)

    for f in sorted(targets):
        fm, fm_lines, fm_errors, clean, fences = parsed[f]
        is_index = f.name == "_index.md"

        # --- frontmatter -------------------------------------------------
        if not fm_lines:
            err("frontmatter", f, 1, "no frontmatter block")
        for bad in fm_errors:
            err("frontmatter", f, 1, f"unparseable frontmatter line: {bad!r}")
        if not isinstance(fm.get("title"), str) or not fm.get("title"):
            err("frontmatter", f, 1, "missing `title`")
        w = fm.get("weight")
        if not (isinstance(w, str) and re.fullmatch(r"-?\d+", w)):
            err("frontmatter", f, 1, f"`weight` missing or not an integer: {w!r}")
        status = fm.get("status")
        if status not in STATUSES:
            err("frontmatter", f, 1, f"`status` must be one of {sorted(STATUSES)}, got {status!r}")
        if not isinstance(fm.get("description"), str) or not fm.get("description"):
            err("frontmatter", f, 1, "missing `description`")
        if is_index:
            if fm.get("bookCollapseSection") != "true":
                err("frontmatter", f, 1, "section index needs `bookCollapseSection: true`")
        else:
            src = fm.get("sources")
            if not isinstance(src, list) or not src:
                err("frontmatter", f, 1, "page needs a non-empty `sources` list")
        for entry in fm.get("sources", []) if isinstance(fm.get("sources"), list) else []:
            path = entry.split()[0] if entry.split() else ""
            if not (ROOT / path).exists():
                err("source", f, 1, f"sources entry names a missing file: {entry!r}")

        for f2, w2, names in sorted(x for x in dup_weight if x[0] == f):
            err("weight", f, 1, f"weight {w2} shared by siblings {', '.join(names)}")

        # --- parent map -------------------------------------------------
        parent = parent_index(f)
        if parent is not None and parent in parsed:
            if page_url(f) not in outbound[parent]:
                err("map", f, 1, f"not linked from its parent section {parent.relative_to(ROOT)}")

        # --- body shape -------------------------------------------------
        first = next((line for _, line in clean if line.strip()), "")
        if not re.match(r"^\s*(\*(?!\*)|_(?!_))", first):
            err("gist", f, 1, "body must open with an italic plain-language passage")
        if not is_index and not any(line.lstrip().startswith("**Status:**") for _, line in clean):
            err("statusline", f, 1, "page has no `**Status:**` line")

        for lineno, info in fences:
            if not info:
                err("fence", f, lineno, "fenced code block has no language (use `text` for formulas)")

        for lineno, line in clean:
            m = HEADING_RE.match(line)
            if m and len(m.group(1)) == 1:
                err("h1", f, lineno, "body H1 — hugo-book renders the frontmatter title as h1; start at ##")

            for sm in STARRED_RE.finditer(INLINE_CODE_RE.sub(" ", line)):
                err("star", f, lineno,
                    f"unescaped starred symbol {sm.group(0)!r} can close an emphasis span; write {sm.group(1)}\\*")

            for code in INLINE_CODE_RE.findall(line):
                code = code.strip()
                if REPO_PATH_RE.match(code) and not (ROOT / code).exists():
                    err("source", f, lineno, f"inline path names a missing file: {code}")

            for target in LINK_RE.findall(INLINE_CODE_RE.sub(" ", line)):
                if re.match(r"^(https?:|mailto:)", target):
                    continue
                if target.startswith("#"):
                    anchor = target[1:].lower()
                    if anchor and anchor not in pages[page_url(f)]["anchors"]:
                        err("anchor", f, lineno, f"no such heading on this page: {target}")
                    continue
                if not target.startswith("/wiki"):
                    err("link", f, lineno,
                        f"not an absolute /wiki/ link: {target} (cite repo files as inline code paths)")
                    continue
                base, _, anchor = target.partition("#")
                base = "/" + base.strip("/")
                if base not in pages:
                    err("link", f, lineno, f"no such page: {target}")
                elif anchor and anchor.lower() not in pages[base]["anchors"]:
                    err("anchor", f, lineno, f"no such heading on {base}: #{anchor}")

        # --- acronyms ---------------------------------------------------
        page_text = " ".join(prose(line) for _, line in clean)
        linked = set()
        for _, line in clean:
            for label in LINK_LABEL_RE.findall(INLINE_CODE_RE.sub(" ", line)):
                linked.update(ACRONYM_RE.findall(label))
        first_use = {}
        for lineno, line in clean:
            for acro in ACRONYM_RE.findall(prose(line)):
                if sum(c.isalpha() for c in acro) < 2:
                    continue
                first_use.setdefault(acro, lineno)
        for acro, lineno in sorted(first_use.items(), key=lambda kv: kv[1]):
            if acro not in registry:
                err("acronym", f, lineno,
                    f"unregistered acronym {acro!r} — spell it out, or add it to scripts/wiki-acronyms.txt")
                continue
            expansion = registry[acro]
            if expansion is None or acro in linked or binds(page_text, acro, expansion):
                continue
            err("acronym", f, lineno,
                f"{acro!r} is never spelled out beside a use on this page (expected {expansion!r}) or linked")

    order = ["link", "anchor", "map", "source", "frontmatter", "weight", "section",
             "gist", "statusline", "star", "h1", "fence", "acronym"]
    errors.sort(key=lambda e: (order.index(e[0]), str(e[1]), e[2]))
    for kind, path, lineno, msg in errors:
        print(f"{path}:{lineno}: {kind}: {msg}")

    if stats:
        inbound = {url: set() for url in pages}
        for f, links in outbound.items():
            for url in links:
                if url in inbound:
                    inbound[url].add(page_url(f))
        counts = {}
        for f, (fm, *_rest) in parsed.items():
            counts[fm.get("status")] = counts.get(fm.get("status"), 0) + 1
        print("\nstatus counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items(), key=str)))
        n_links = sum(len(v) for v in outbound.values())
        print(f"pages: {len(pages)}; internal links (distinct page pairs): {n_links}")
        weak = []
        for url, srcs in sorted(inbound.items()):
            path = pages[url]["path"]
            parent = parent_index(path)
            others = {s for s in srcs if parent is None or s != page_url(parent)}
            if len(others) < 3 and url != "/wiki":
                weak.append((len(others), url))
        print(f"pages with fewer than 3 inbound links from outside their parent map: {len(weak)}")
        for n, url in sorted(weak):
            print(f"  {n}  {url}")

    if errors:
        tally = {}
        for kind, *_rest in errors:
            tally[kind] = tally.get(kind, 0) + 1
        summary = ", ".join(f"{v} {k}" for k, v in sorted(tally.items()))
        print(f"\nwiki check FAILED: {len(errors)} problem(s): {summary}", file=sys.stderr)
        return 1

    print(f"wiki OK — {len(pages)} pages, no problems")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
