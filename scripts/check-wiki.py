#!/usr/bin/env python3
r"""Verify the wiki in wiki/ against the rules in wiki/CLAUDE.md.

Checks, in order of severity:

  link         an internal link points at a wiki page that does not exist, or
               is not an absolute /wiki/ link
  anchor       a link points at a heading that does not exist
  heading      a heading holds a link, an image, a bare URL, emphasis or an
               attribute block, whose ID the gate does not compute (Hugo uses
               only part of the marked-up text, or the {#id})
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
slugify), for every heading the `heading` check lets through. That is an
emulation; the built-site check is the authority on the IDs Hugo actually writes.

Exit status is 1 if any error is found, 0 otherwise.

Usage:
  scripts/check-wiki.py              # check everything
  scripts/check-wiki.py FILE...      # report only on these files (links still
                                     # resolve wiki-wide)
  scripts/check-wiki.py --stats      # also print status counts and link density
"""

import csv
import re
import string
import sys
import unicodedata
from html.entities import html5
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ACRONYMS_FILE = ROOT / "scripts" / "wiki-acronyms.txt"

STATUSES = {
    "established", "alive", "conjecture", "open", "dead",
    "superseded", "method", "record", "hub",
}

FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
# An ATX heading, as CommonMark reads it: up to three spaces, one to six #, then a
# space or tab or the end of the line. Group 2 is the text; a closing run of #
# counts only after a space or tab, so "C#" keeps its #.
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+|$)(.*?)[ \t]*(?:(?<=[ \t])#+[ \t]*)?$")
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

# Heading markup, as slugify strips it (code spans: code_spans()). A backslash
# before markup makes it plain text. Raw HTML as goldmark recognizes it (an open
# or closing tag, a comment, a processing instruction, a declaration, CDATA) and
# the typographer's << and >> are matched in one left-to-right pass: whichever
# starts first wins, as in goldmark, so <b>>> is a tag and then ».
HTML_OR_GUILLEMET_RE = re.compile(
    r"(?<!\\)(?:<[A-Za-z][A-Za-z0-9-]*(?:[ \t]+[A-Za-z_:][A-Za-z0-9:._-]*"
    r"(?:[ \t]*=[ \t]*(?:[^\"'=<>`\x00-\x20]+|'[^']*'|\"[^\"]*\"))?)*[ \t]*/?>"
    r"|</[A-Za-z][A-Za-z0-9-]*[ \t]*>|<!-->|<!--->|<!--.*?-->|<\?.*?\?>|<![A-Z].*?>"
    r"|<!\[CDATA\[.*?\]\]>|<<|>>)"
)
NAMED_ENTITY_RE = re.compile(r"&[A-Za-z][A-Za-z0-9]*;")
LINK_OR_IMAGE_RE = re.compile(r"(?<!\\)!?\[(" + LINK_LABEL + r")(?<!\\)\]\([^)]*\)")
# An emphasis pair of underscores, _text_ or __text__. CommonMark opens one only
# where the underscore does not follow a letter or digit and closes it only where
# it is not followed by one, so G_eff, and an unpaired U(1)_d, stay text.
UNDERSCORE_PAIR_RE = re.compile(r"(?<![^\W_])(_+)(?=\S)(.+?)(?<=\S)\1(?![^\W_])")
# Stand-ins while markup is removed; the slug drops all four.
ESCAPED_UNDERSCORE = "\x00"  # \_, which no emphasis pair takes
ESCAPED_HYPHEN = "\x01"  # \-, which no typographer dash takes
RAW_HTML = "\x02"  # a tag, which slugs to nothing but keeps -<b>-- from reading as ---
ESCAPED_BACKSLASH = "\x03"  # \\, so that its second backslash escapes nothing
# Markup that heading_markup keeps out of headings: an inline link or image, a
# footnote reference, an autolink, and a URL or email address that the linkify
# extension turns into a link.
HEADING_LINK_RE = re.compile(
    r"\]\(|\[\^|<[A-Za-z][A-Za-z0-9+.-]{1,31}:|<[^\s<>]*@|://|www\.|\w@\w"
)
# A trailing attribute block, {#id}, {.class} or {name=value}, which goldmark
# takes as the heading's attributes, not its text.
HEADING_ATTRS_RE = re.compile(r"\{[ \t]*(?:\}|(?:[#.]|[A-Za-z_:][\w.:-]*[ \t]*=).*\})[ \t]*$")
ESCAPED_PUNCT_RE = re.compile(r"\\[!-/:-@\[-`{-~]")


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


def code_spans(text):
    """The code spans in a line of Markdown as [(start, end, code)].

    A backtick run opens a code span unless a backslash escapes its first
    backtick, and the next run of the same length closes it (backslashes inside
    escape nothing); a run with no such closer is plain text."""
    spans, i = [], 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text) and text[i + 1] in string.punctuation:
            i += 2
            continue
        if text[i] != "`":
            i += 1
            continue
        j = i
        while j < len(text) and text[j] == "`":
            j += 1
        k = j
        while k < len(text):
            if text[k] != "`":
                k += 1
                continue
            e = k
            while e < len(text) and text[e] == "`":
                e += 1
            if e - k == j - i:
                spans.append((i, e, text[j:k]))
                break
            k = e
        i = spans[-1][1] if spans and spans[-1][0] == i else j
    return spans


def _heading_text(text):
    """Markdown outside code spans, reduced to the text Hugo slugs."""
    text = text.replace("\\\\", ESCAPED_BACKSLASH)
    text = text.replace("\\_", ESCAPED_UNDERSCORE).replace("\\-", ESCAPED_HYPHEN)
    # Raw HTML is stripped; the typographer turns << and >> into guillemets.
    text = HTML_OR_GUILLEMET_RE.sub(
        lambda m: {"<<": "«", ">>": "»"}.get(m.group(0), RAW_HTML), text)
    text = LINK_OR_IMAGE_RE.sub(r"\1", text)
    text = UNDERSCORE_PAIR_RE.sub(r"\2", text)
    # The typographer turns --- into an em dash and -- into an en dash, which the
    # slug then drops; a single - stays. A heading of only a dash is not empty.
    text = text.replace("---", "—").replace("--", "–")
    return text.replace(ESCAPED_UNDERSCORE, "_").replace(ESCAPED_HYPHEN, "-")


def slugify(text):
    """Hugo's default heading ID (autoHeadingIDType "github") for a heading's
    Markdown, or None where Hugo gives the heading no ID.

    Hugo slugs the heading's plain text (its render.TextPlain): markup is gone,
    code-span content stays, raw HTML is stripped, and named entities are resolved
    last, inside code spans too (&amp; is '&'; numeric references stay as typed).
    A heading whose plain text is empty, such as one of raw HTML only, gets no ID.
    Each character is then kept if it is a letter of any script (str.isalpha(): ₐ,
    ℤ and Greek stay), a decimal digit (category Nd only, so subscript and
    superscript digits such as ₀ ² ⁴ and the superscript minus are dropped), '-'
    or '_', and lowercased one character at a time by Go's simple case mapping
    (İ gives i); each space (U+0020 only, not a tab or a no-break space) becomes
    '-', runs not collapsed; everything else is dropped. Underscores are dropped
    only where they pair up as emphasis (_text_); U(1)_d gives u1_d. '*' and '~'
    markup falls to the filter.

    Of a link, an image or an emphasis span, Hugo slugs only the first inline node
    of the content, so its ID depends on where goldmark splits that text; the
    `heading` check (heading_markup) keeps such markup out of headings, and this
    function does not emulate it.

    Checked against the IDs Hugo 0.168 wrote (2026-10-22) for every wiki heading,
    149 edge cases (entities in and out of code spans, escapes, raw HTML with a
    quoted '>', padded code, typographer dashes and quotes, duplicates, empty and
    symbol-only headings) and about 100,000 random headings built from markup
    fragments: every heading heading_markup lets through got Hugo's ID.
    """
    parts, pos = [], 0
    for start, end, code in code_spans(text):
        parts.append(_heading_text(text[pos:start]))
        # CommonMark strips one space from each end of padded code: `` `a` ``.
        if code.startswith(" ") and code.endswith(" ") and code.strip(" "):
            code = code[1:-1]
        parts.append(code)
        pos = end
    parts.append(_heading_text(text[pos:]))
    plain = "".join(parts).replace(RAW_HTML, "")
    plain = NAMED_ENTITY_RE.sub(lambda m: html5.get(m.group(0)[1:], m.group(0)), plain)
    if not plain:
        return None
    slug = []
    for ch in plain.strip():
        if ch in " -":
            slug.append("-")
        elif ch == "_" or ch.isalpha() or unicodedata.category(ch) == "Nd":
            # str.lower() maps U+0130 (I with a dot) to i and a combining dot; Go's
            # unicode.ToLower, which Hugo uses, maps it to i.
            slug.append("i" if ch == "\u0130" else ch.lower())
    return "".join(slug)


def _flanking(text, start, end):
    """(can open, can close) for the delimiter run text[start:end], by CommonMark's
    flanking rules as goldmark applies them."""
    before = text[start - 1] if start else " "
    after = text[end] if end < len(text) else " "
    b_space, a_space = before.isspace(), after.isspace()
    b_punct = unicodedata.category(before)[0] in "PS"
    a_punct = unicodedata.category(after)[0] in "PS"
    left = not a_space and (not a_punct or b_space or b_punct)
    right = not b_space and (not b_punct or a_space or a_punct)
    if text[start] == "_":
        return left and (not right or b_punct), right and (not left or a_punct)
    return left, right


def heading_markup(text):
    """'link', 'emphasis' or 'attributes' if a heading's Markdown holds markup
    whose ID the gate does not compute, else None.

    Hugo slugs a link, an image or an emphasis or strikethrough span by the first
    inline node of its content only, and goldmark splits that content at an
    apostrophe, a quote, '--', '_', a code span and other markup: a heading
    [Born's question](...) gets the ID 'born'. An autolink, and a URL or email
    address that the linkify extension turns into a link, add nothing. A trailing
    attribute block ({#id}) sets or changes the ID. A link is any '](', footnote
    reference, autolink, URL or email address; emphasis is a run of *, _ or ~
    that can open followed by one that can close. The tests err toward reporting.
    """
    for start, end, _ in reversed(code_spans(text)):
        text = text[:start] + "`" + text[end:]  # a code span slugs whole
    text = ESCAPED_PUNCT_RE.sub("!", text)  # an escaped character is plain text
    if HEADING_LINK_RE.search(text):
        return "link"
    if HEADING_ATTRS_RE.search(text):
        return "attributes"
    for ch in "*_~":
        opened = False
        for m in re.finditer(re.escape(ch) + "+", text):
            if ch == "~" and len(m.group()) > 2:
                continue  # a longer run of tildes is text, not strikethrough
            can_open, can_close = _flanking(text, m.start(), m.end())
            if opened and can_close:
                return "emphasis"
            opened = opened or can_open
    return "emphasis" if UNDERSCORE_PAIR_RE.search(text) else None


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
                slug = slugify(m.group(2))
                if slug is not None:
                    heading_id(slug, anchors)
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
            markup = heading_markup(m.group(2)) if m else None
            if markup:
                why = {
                    "link": "a link in a heading: Hugo's ID for it keeps only part of the link text",
                    "emphasis": "emphasis in a heading: Hugo's ID for it keeps only part of the emphasized text",
                    "attributes": "an attribute block in a heading: {#id} or {.class} sets or changes the ID",
                }[markup]
                err("heading", f, lineno,
                    f"{why}, which the gate does not compute; make the heading plain text "
                    f"(code spans are fine; escape a literal *, _, ~ or {{)")

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

    order = ["link", "anchor", "heading", "map", "source", "frontmatter", "weight", "section",
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
