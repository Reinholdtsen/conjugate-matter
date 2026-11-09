#!/usr/bin/env python3
r"""Verify the wiki in wiki/ against the rules in wiki/CLAUDE.md.

Checks, in order of severity:

  link         an internal link is not a path relative to its file, or names a
               file or folder that does not exist (a folder of the wiki is
               linked by its _index.md, any other folder with a trailing /)
  anchor       a link points at a heading that does not exist, or at a wiki
               heading whose ID GitHub spells differently from Hugo, so that the
               link would work on the site and not on GitHub
  heading      a heading holds a link, an image, a bare URL, emphasis or an
               attribute block, whose ID the gate does not compute (Hugo uses
               only part of the marked-up text, or the {#id})
  map          a page is not linked from its parent section's _index.md
  source       a frontmatter `sources` entry, or an inline-code repo path in the
               body, names a file that does not exist
  frontmatter  missing or invalid title, weight, status, description, sources
               (pages), or bookCollapseSection (sections)
  weight       two siblings share a weight
  section      a folder under wiki/ has no _index.md, a file is named claude.md,
               or two files serve at one URL (a.md and a/_index.md)
  gist         the body does not open with an italic plain-language passage
  statusline   a page that is not a section index has no **Status:** line
  status       a page's title pattern or status line disagrees with its status,
               or the page is missing from the register of that status
  voice        wording that tells how a claim's status came about instead of the
               claim (wiki/CLAUDE.md, Voice, "State the claim, not the discussion")
  summary      wiki/summary.md passes its length limit, links a dead or under-review
               page, or leaves out P.R.'s conjectures
  star         an unescaped starred symbol such as v* or M*, whose asterisk can
               close an emphasis span (an italic opening ends early); write v\*
  h1           the body contains an `# H1` (hugo-book renders the title as h1)
  fence        a fenced code block declares no language
  acronym      an acronym is unregistered, or a page uses it without spelling it
               out beside a use or linking it (registry: scripts/wiki-acronyms.txt)
  symbol       a page uses a symbol whose values the wiki states (w, w₀, wₐ, z)
               without defining it in words beside its first use (SYMBOLS)
  paper        a paper identifier (arXiv:…, doi:…, handle …) in prose is not a link to
               the paper; a paper link is not in canonical form, names an identifier
               scripts/wiki-papers.tsv lacks, or has a label that names another
               identifier, that names neither the identifier (an INSPIRE record as
               "INSPIRE N") nor the registered first author, or that gives a year
               the registry does not list for the paper (registry:
               scripts/wiki-papers.tsv, built online by scripts/wiki-papers.py; this
               check is offline)

Hugo does not validate internal links: it renders /wiki/does-not-exist without
complaint. This script catches a dead link in the Markdown, before any build. The
site in site/ adds two later layers: hugo-book's BookPortableLinks = 'error' fails
the build on a link to a missing page, and scripts/check-site.py checks every link
and #fragment in the built HTML (see site/CLAUDE.md).

Anchors are checked against heading IDs computed the way Hugo computes them (see
slugify), for every heading the `heading` check lets through. That is an
emulation; the built-site check is the authority on the IDs Hugo actually writes.

Links are relative file paths, so that one link works on the site, on GitHub and
in an editor (wiki/CLAUDE.md, Links). A link to a wiki page (a .md file under
wiki/ other than CLAUDE.md) is a page of the site; a link to any other file or
folder of the repository is served by GitHub, where the site's link hook sends it
(site/layouts/_markup/render-link.html). Anchors on GitHub are computed by
github_slug, whose rule was checked against GitHub's own anchors.

The documents in wiki/papers/ (RECORD_DIRS) are the program's papers, published
in full beside the wiki. They are the record the wiki is derived from, not wiki
pages, and keep their own wording and house style. The checks that keep the built
site sound apply to them as to any page: link, anchor, heading, map, source,
frontmatter (title, weight, description, and status `record`), weight, section,
star, h1 and fence. The rules for a wiki page's shape, status, wording and
citations do not: sources, gist, statusline, status, voice, summary, acronym,
symbol and paper. The section's _index.md is a wiki page and gets every check.

Exit status is 1 if any error is found, 0 otherwise.

Usage:
  scripts/check-wiki.py              # check everything
  scripts/check-wiki.py FILE...      # report only on these files (links still
                                     # resolve wiki-wide)
  scripts/check-wiki.py --stats      # also print status counts and link density
"""

import csv
import os
import re
import string
import sys
import unicodedata
import urllib.parse
from html.entities import html5
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ACRONYMS_FILE = ROOT / "scripts" / "wiki-acronyms.txt"
PAPERS_FILE = ROOT / "scripts" / "wiki-papers.tsv"

STATUSES = {
    "established", "alive", "conjecture", "open", "dead", "under-review",
    "superseded", "method", "record", "hub",
}

# A status shows in the title, opens the status line and has a register (wiki/CLAUDE.md, The tree).
TITLE_OF_STATUS = {
    "dead": r"^Obituary: ",
    "under-review": r"^Under review: ",
    "open": r"^(?:Open: |Row \d+: )",
    "superseded": r"\(superseded\)$",
    "conjecture": r"^Conjecture: |\((?:chat|popsci)-only\)$",
}
WORD_OF_STATUS = {
    "dead": "Dead", "under-review": "Under review", "open": "Open", "superseded": "Superseded",
    "conjecture": "Conjecture", "alive": "Alive", "established": "Established",
    "method": "Method", "record": "Record",
}
REGISTER_OF_STATUS = {
    "dead": "/wiki/status/graveyard",
    "under-review": "/wiki/status/under-review",
    "open": "/wiki/status/open-problems",
    "superseded": "/wiki/status/superseded",
    "conjecture": "/wiki/status/conjectures",
    "alive": "/wiki/status/alive",
}

# Wording that tells how a claim's status came about instead of the claim. Pages state what a
# claim is, what supports it, what weighs against it and where it stands now. These phrases
# have no place on a page, quoted or not.
DISCUSSION_RE = re.compile(
    r"\bconcur(?:s|red|ring|rence)?\b|Restore all pending|confusion on my part|prematurely|"
    r"[Rr]ecorded dead|\bnot dead\b|\bnot deaths?\b|Don't kill|\bkeep dead\b|"
    r"\buntil (?:he|Paul|P\.R\.) (?:reviews|rules|answers)|"
    r"(?:Paul|P\.R\.)'s (?:rule|direction|answers?|rulings?|review)\b|"
    r"\bhis (?:direction|rule|answers?|ruling|review)\b|"
    r"(?:awaits?|awaiting|pending|until|before) Paul\b|under (?:his|Paul's|P\.R\.'s) review|"
    r"review(?:s|ed)?(?: it| them| each)? with Claude|[Nn]arrowed by Paul|"
    r"Paul (?:narrowed|withdrew|directed|answered|accepted|ruled|deferred|chose|did not|does not)"
)
# A person is named P.R. Two pages introduce "Paul (P.R.)". Titles of source sections and of the
# checkpoint's page are cited as they stand.
PAUL_RE = re.compile(r"\bPaul\b(?! Dirac)")
PAUL_PAGES = {"_index.md", "method/collaboration.md"}
CITED_TITLES = ("Working with Paul", "Recommendations to Paul", "The checkpoint: #9 to #11 v2.5")
# The checkpoint's current versions as a tag on a citation; a citation is "#11 §9". Earlier
# versions may label a physics correction, and pages of document history may date things.
VERSION_RE = re.compile(r"#11,? \(?v2\.[345]\b|\(v2\.[345]\)|\b(?:[Ss]ince|[Uu]ntil) (?:#11 )?v2\.[345]\b")
HISTORY_PAGES = ("history/", "predictions/table-history.md", "method/review/", "status/superseded.md")
# Folders under wiki/ that publish the record itself, not wiki pages (see the docstring). Their files get
# the checks that keep the built site sound and none of the rules for a wiki page's shape, status or wording.
RECORD_DIRS = ("papers/",)

SUMMARY_MAX_WORDS = 800
SUMMARY_CONJECTURES = (
    "/wiki/dark-matter/conjugate-matter",
    "/wiki/dark-matter/candidates/momentum-space-monopoles",
    "/wiki/electric-magnetic-duality/monopole-explanation",
    "/wiki/electric-magnetic-duality/magnetic-identification",
    "/wiki/cosmology/scale-factor-duality/collapse-powered-expansion",
    "/wiki/dark-matter/momentum-clumping/founding-image",
)

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
# A link with its label and target, for the paper check.
LINK_FULL_RE = re.compile(r"(?<!!)\[(" + LINK_LABEL + r")\]\(\s*([^)\s]+?)\s*(?:\"[^\"]*\")?\)")
# A paper identifier as the wiki writes it in prose: arXiv:2003.00318, arXiv:hep-th/9211021 (a version
# suffix is allowed), an old-style arXiv identifier without the prefix (hep-th/9211021), doi:10.1103/
# PhysRevLett.45.1, handle 20.500.12415/6128. Every one is a link to the paper itself (wiki/CLAUDE.md,
# Links). A new-style number without the prefix (2003.00318) is not matched: it cannot be told from a
# decimal number, so such a mention is linked by hand. scripts/wiki-papers.py uses the same pattern.
PAPER_ID_RE = re.compile(
    r"\barXiv:((?:[a-z][a-z\-]*(?:\.[A-Z]{2})?/\d{7})|\d{4}\.\d{4,5})(?:v\d+)?"
    r"|\bdoi:(10\.\d{4,9}/[^\s,;)\]]*[^\s,;)\].])"
    r"|\bhandle (\d+(?:\.\d+)*/\d+)"
    r"|(?<![\w/.:\-])((?:astro-ph|hep-th|hep-ph|hep-lat|hep-ex|gr-qc|cond-mat|math-ph|quant-ph|nucl-th|nucl-ex"
    r"|physics|math)(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?\b",
    re.I,
)
# A link to a paper in canonical form, and the hosts whose links must take that form.
PAPER_URL_RES = (
    ("arXiv:", re.compile(r"^https://arxiv\.org/abs/([^\s?#]+?)(?:v\d+)?$")),
    ("doi:", re.compile(r"^https://doi\.org/(10\.[^\s?#]+)$")),
    ("recid:", re.compile(r"^https://inspirehep\.net/literature/(\d+)$")),
    ("hdl:", re.compile(r"^https://hdl\.handle\.net/([^\s?#]+)$")),
)
PAPER_HOST_RE = re.compile(r"^https?://(?:[\w-]+\.)*(?:arxiv\.org|doi\.org|inspirehep\.net|handle\.net)/", re.I)
# An INSPIRE record named in a link label, as the notes write it: [INSPIRE 1923123](https://inspirehep.net/...).
# Only labels are read for it; an INSPIRE number in prose is not an identifier the wiki must link.
INSPIRE_LABEL_RE = re.compile(r"\bINSPIRE (\d+)\b")
YEAR_RE = re.compile(r"\b(1[89]\d\d|20\d\d)\b")
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

# Symbols whose values the pages state ("w ≥ −1", "z ≈ 0.4"). Each is defined in words within
# BIND_WINDOW of its first use on every page (wiki/CLAUDE.md, Symbols): a reader arriving from a
# search engine has read no other page, and a link alone defines nothing. For each symbol: what it
# is; a pattern for a use in prose; patterns that must all match beside the first use; the pages
# on which the letter stands for another quantity; and forms that mean this symbol on any page,
# which fail on those pages, since two quantities there would share one letter. The glossary and
# the notation page define each symbol in its own entry and are not checked.
SYMBOL_REGISTERS = {"glossary.md", "notation.md"}
SYMBOLS = {
    "w": {
        "means": "the equation of state, pressure divided by energy density",
        # w alone and in w̃, w_eff, w(z), w₀, wₐ. The diameter note writes one wavelength as w,
        # so h/w and "wavelength w" are not uses.
        "use": re.compile(r"(?<![\w\\/])(?<!wavelength )w(?![A-Za-z0-9])"),
        "define": [re.compile(
            r"\bpressure\b(?:\W+\w+){0,2}?\W+(?:to|over|divided by|÷)\W+(?:\w+\W+){0,2}?energy density", re.I
        )],
        "elsewhere": {
            "dark-matter/conjugate-matter/gate-mechanism.md": "a fiber weight",
            "method/verification/gate-mechanism-script.md": "a fiber weight",
            "phase-space/born-geometry/double-field-theory.md": "a closed string's winding",
            "phase-space/modular-field/siegel-domain.md": "ω, as a script prints it",
            "phase-space/reciprocity/lagrangian-polarizations.md": "ω, as a script prints it",
            "phase-space/reciprocity/symplectic-form.md": "ω, as a script prints it",
            "symmetry-breaking/section-condition.md": "a variable in a script's output",
        },
        "always": re.compile(
            r"(?<![\w\\/])w(?:[₀ₐ]|̃|_eff|\([az]\)|\s*[=≥≤<>≈≃≡]\s*[−+-]\d+(?:\.\d+)?)|equation of state w\b"
        ),
    },
    "w₀": {
        "means": "the value of w today",
        "use": re.compile(r"(?<![\w\\])w₀"),
        "define": [re.compile(
            r"\b(?:value|equation of state)\b[^.]{0,30}?\btoday\b|\btoday's\b|\bpresent(?:-day)? value\b|\bw today\b", re.I
        )],
    },
    "wₐ": {
        "means": "how fast w changes as the universe expands",
        "use": re.compile(r"(?:(?<![\w\\])|(?<=w₀))wₐ"),
        "define": [re.compile(
            r"\brate of change\b|\bhow (?:fast |quickly )?(?:w|it) (?:has )?(?:chang|ris|fall|drift)\w*"
            r"|\bw (?:has been |is |was )?(?:rising|falling|changing|drifting|rises|falls|changes|drifts)\b", re.I
        )],
    },
    "z": {
        "means": "redshift, the stretching of light by the expansion since it was emitted: larger z is earlier",
        "use": re.compile(r"(?<![\w\\-])z(?![A-Za-z0-9])"),
        "define": [
            re.compile(r"\bredshift", re.I),
            re.compile(r"\bearlier\b|\bago\b|\bstretch|\bexpanded\b|\bemitted\b|1/\(1 \+ z\)|\bcosmic time\b", re.I),
        ],
        "elsewhere": {
            "electric-magnetic-duality/_index.md": "a point of the upper half-plane",
            "electric-magnetic-duality/modular-group.md": "a point of the upper half-plane",
            "phase-space/modular-field/modular-inversion.md": "a complex number",
            "phase-space/modular-field/siegel-domain.md": "a complex number",
            "phase-space/reciprocity/wigner-function.md": "a point of phase space",
            "gravity/spin-2-fields/equivalence-principle.md": "a height",
            "symmetry-breaking/inverse-higgs-constraints.md": "an axis in space",
            "dark-matter/conjugate-matter/gate-mechanism.md": "a scattering variable",
            "method/verification/gate-mechanism-script.md": "a variable of a check",
        },
        "always": re.compile(
            r"(?<![\w\\|−-])(?<!Im )(?<!Re )z(?:_\w+|\\\*)?\s*[≈≃=<>]\s*[−-]?\d+(?:\.\d+)?"
            r"|(?<=[wH]\()z′?\)|\b1 \+ z\b|\bredshifts? z\b"
        ),
    },
}

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


def load_papers():
    """Return {id: (surnames, years)} from the paper registry, scripts/wiki-papers.tsv."""
    reg = {}
    if not PAPERS_FILE.exists():
        return reg
    for raw in PAPERS_FILE.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        cells = raw.split("\t")
        if len(cells) >= 3:
            reg[cells[0]] = ([n for n in cells[1].split("|") if n], set(cells[2].split(",")) - {""})
    return reg


def paper_id(m):
    """The registry id of a PAPER_ID_RE match: arXiv:ID, doi:lowercased, hdl:H."""
    if m.group(1) or m.group(4):
        return "arXiv:" + (m.group(1) or m.group(4))
    if m.group(2):
        return "doi:" + m.group(2).lower()
    return "hdl:" + m.group(3)


def paper_of_url(url):
    """The registry id a canonical paper link points at, or None."""
    for prefix, rx in PAPER_URL_RES:
        m = rx.match(url)
        if m:
            value = urllib.parse.unquote(m.group(1))
            return prefix + (value.lower() if prefix == "doi:" else value)
    return None


def fold(text):
    """Lowercase, with diacritics removed: Minić and Minic, Hübsch and Hubsch, compare equal."""
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)).lower()


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
        # A block-list item is indented exactly two spaces, as every page writes it. Hugo's YAML parser rejects an item
        # indented deeper than its siblings, which this parser would otherwise accept (2026-11-06).
        m = re.match(r"^  -\s+(.*)$", raw)
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


def github_slug(text):
    """The ID GitHub gives a heading of a rendered Markdown file: the heading's text (a link or image by its
    label, a code span by its content, an escaped character as itself), lowercased, keeping letters, marks,
    decimal digits, connector punctuation, spaces and hyphens, each space a hyphen. Hugo drops marks (the
    tilde of c̃), so the two differ there. Checked against GitHub's anchors for all 4,555 headings of the
    repository's Markdown files on 2026-11-07."""
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = ESCAPED_PUNCT_RE.sub(lambda m: m.group(0)[1], t).lower()
    return "".join(c for c in t if c in " -" or unicodedata.category(c)[0] in "LM"
                   or unicodedata.category(c) in ("Nd", "Pc")).replace(" ", "-")


_GITHUB_IDS = {}


def github_ids(path):
    """GitHub's heading IDs for a Markdown file, in order; a repeated ID gets -1, -2, ..."""
    if path not in _GITHUB_IDS:
        _, body, offset = split_frontmatter(path.read_text(encoding="utf-8"))
        clean, _ = strip_code(body, offset)
        used, ids = {}, []
        for _, line in clean:
            m = HEADING_RE.match(line)
            if m and m.group(2).strip():
                base = github_slug(m.group(2))
                n = used.get(base, 0)
                ids.append(base if n == 0 else f"{base}-{n}")
                used[base] = n + 1
        _GITHUB_IDS[path] = ids
    return _GITHUB_IDS[path]


def resolve(f, target):
    """What a link in wiki file f points at, as (kind, path, anchor): ("external", None, "") for a URL;
    ("page", path, anchor) for a wiki page, f itself for '#anchor'; ("repo", path, anchor) for any other file
    or folder of the repository, which the site links on GitHub; ("bad", None, why) otherwise."""
    if re.match(r"^(?:https?:|mailto:)", target):
        return ("external", None, "")
    raw, _, anchor = target.partition("#")
    if not raw:
        return ("page", f, anchor)
    if raw.startswith("/") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", raw):
        return ("bad", None, "not a path relative to this file (wiki/CLAUDE.md, Links)")
    p = Path(os.path.normpath(f.parent / urllib.parse.unquote(raw)))
    if not p.is_relative_to(ROOT):
        return ("bad", None, "a path outside the repository")
    if not p.exists():
        return ("bad", None, "no such file or folder")
    if p.is_relative_to(WIKI) and p.is_dir():
        return ("bad", None, "a folder of the wiki; link its _index.md")
    if p.is_dir() != raw.endswith("/"):
        return ("bad", None, "a folder's path ends with /, and only a folder's")
    if p.is_relative_to(WIKI) and p.suffix == ".md" and p.name != "CLAUDE.md":
        return ("page", p, anchor)
    return ("repo", p, anchor)


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
    papers = load_papers()
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

    pages, parsed, by_url = {}, {}, {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm_lines, body, offset = split_frontmatter(text)
        fm, fm_errors = parse_frontmatter(fm_lines)
        clean, fences = strip_code(body, offset)
        anchors, on_github = set(), {}  # Hugo's heading IDs; Hugo's ID -> GitHub's for the same heading
        gh = iter(github_ids(f))
        for _, line in clean:
            m = HEADING_RE.match(line)
            if m and m.group(2).strip():
                slug, gh_id = slugify(m.group(2)), next(gh)
                if slug is not None:
                    on_github[heading_id(slug, anchors)] = gh_id
        url = page_url(f)
        # Hugo lowercases URLs, so a.md and a/_index.md, or A.md and a.md, collide.
        twin = by_url.setdefault(url.lower(), f)
        if twin != f:
            err("section", f, 1, f"serves at {url} like {twin.relative_to(ROOT)}; Hugo builds only one of them")
        pages[url] = {"anchors": anchors, "github": on_github, "path": f}
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
                kind, path, _ = resolve(f, target)
                if kind == "page" and path != f and path in parsed:
                    links.add(page_url(path))
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
        rel = f.relative_to(WIKI).as_posix()
        record = rel.startswith(RECORD_DIRS) and not is_index  # a published document, not a wiki page

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
        elif record:
            if status != "record":
                err("frontmatter", f, 1, f"a document in {', '.join('wiki/' + d for d in RECORD_DIRS)} "
                    f"has status `record`, got {status!r}")
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
        if not record and not re.match(r"^\s*(\*(?!\*)|_(?!_))", first):
            err("gist", f, 1, "body must open with an italic plain-language passage")
        if not is_index and not record and not any(line.lstrip().startswith("**Status:**") for _, line in clean):
            err("statusline", f, 1, "page has no `**Status:**` line")

        # --- status: title, status line, register -----------------------
        title = fm.get("title")
        pattern = TITLE_OF_STATUS.get(status)
        if pattern and isinstance(title, str) and not re.search(pattern, title):
            err("status", f, 1, f"status {status} needs a title matching {pattern!r}, got {title!r}")
        word = WORD_OF_STATUS.get(status)
        if word and not is_index and not record:
            line = next((s.lstrip() for _, s in clean if s.lstrip().startswith("**Status:**")), None)
            if line and not line.removeprefix("**Status:**").lstrip().startswith(word):
                err("status", f, 1, f"status {status}: the **Status:** line must open with {word!r}")
        register = REGISTER_OF_STATUS.get(status)
        if register and page_url(f) != register and register in pages:
            if page_url(f) not in outbound[pages[register]["path"]]:
                err("status", f, 1, f"status {status}: not linked from its register {register}")

        # --- voice --------------------------------------------------------
        desc = fm.get("description")
        for lineno, line in ([] if record else ([(1, desc)] if isinstance(desc, str) else []) + clean):
            seen = prose(line)
            for cited in CITED_TITLES:
                seen = seen.replace(cited, " ")
            m = DISCUSSION_RE.search(seen)
            if m:
                err("voice", f, lineno, f"{m.group(0)!r} tells how a status came about; state the claim and where it stands")
            if rel not in PAUL_PAGES and PAUL_RE.search(seen):
                err("voice", f, lineno, "a person is named P.R. outside _index and method/collaboration")
            if not rel.startswith(HISTORY_PAGES):
                m = VERSION_RE.search(seen)
                if m:
                    err("voice", f, lineno, f"{m.group(0)!r}: no version tag on a citation outside the history pages")

        # --- the executive summary ------------------------------------------
        if f == WIKI / "summary.md":
            lines = [line for _, line in clean]
            cut = next((i for i, line in enumerate(lines) if line.startswith("## Sources")), len(lines))
            words = sum(len(prose(line).split()) for line in lines[:cut])
            if words > SUMMARY_MAX_WORDS:
                err("summary", f, 1, f"{words} words before Sources; the limit is {SUMMARY_MAX_WORDS}")
            for url in sorted(outbound[f]):
                target = pages.get(url)
                if target and parsed[target["path"]][0].get("status") in ("dead", "under-review"):
                    err("summary", f, 1, f"links {url}: the summary lists no dead claims and no claims under review")
            for url in SUMMARY_CONJECTURES:
                if url not in outbound[f]:
                    err("summary", f, 1, f"does not link P.R.'s conjecture {url}")

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
                kind, path, anchor = resolve(f, target)
                if kind == "external":
                    continue
                if kind == "bad":
                    err("link", f, lineno, f"{target}: {anchor}")
                    continue
                if not anchor:
                    continue
                if kind == "page":
                    page = pages.get(page_url(path))
                    if page is None or anchor.lower() not in page["anchors"]:
                        err("anchor", f, lineno, f"no such heading on {path.relative_to(ROOT)}: #{anchor}")
                    elif page["github"][anchor.lower()] != anchor.lower():
                        err("anchor", f, lineno,
                            f"#{anchor}: GitHub gives this heading the ID #{page['github'][anchor.lower()]}, so the "
                            f"link would fail there; reword the heading so that the two agree (github_slug)")
                elif path.suffix == ".md":
                    if anchor not in github_ids(path):
                        err("anchor", f, lineno, f"no such heading on {path.relative_to(ROOT)} (on GitHub): #{anchor}")
                elif not re.fullmatch(r"L\d+(?:-L\d+)?", anchor):
                    err("anchor", f, lineno, f"#{anchor}: a file that is not Markdown takes only a line anchor (#L12, #L12-L20)")

            # --- paper links: every identifier links to its paper ---------------
            if record:
                continue
            text = INLINE_CODE_RE.sub(lambda c: " " * len(c.group(0)), line)  # code blanked, offsets kept
            spans = []
            for lm in LINK_FULL_RE.finditer(text):
                label, target = lm.group(1), lm.group(2)
                spans.append((lm.start(), lm.end()))
                pid = paper_of_url(target)
                if pid is None:
                    if PAPER_HOST_RE.match(target):
                        err("paper", f, lineno,
                            f"a paper link not in canonical form: {target} (https://arxiv.org/abs/ID, "
                            f"https://doi.org/DOI, https://inspirehep.net/literature/N or https://hdl.handle.net/H)")
                    continue
                if pid not in papers:
                    err("paper", f, lineno,
                        f"links {pid}, which scripts/wiki-papers.tsv lacks (run scripts/wiki-papers.py)")
                    continue
                named = [paper_id(im) for im in PAPER_ID_RE.finditer(label)]
                named += ["recid:" + n for n in INSPIRE_LABEL_RE.findall(label)]
                bare = re.fullmatch(r"(\d{4}\.\d{4,5})(?:v\d+)?", label.strip())  # a new-style number, linked by hand
                if bare and not named:
                    named = ["arXiv:" + bare.group(1)]
                surnames, years = papers[pid]
                if named:
                    if named != [pid]:
                        err("paper", f, lineno, f"the label names {', '.join(named)} but the link goes to {pid}")
                    continue
                if not any(fold(n) in fold(label) for n in surnames):
                    err("paper", f, lineno,
                        f"the label {label!r} names neither {pid} nor its first author ({' or '.join(surnames)})")
                wrong = [y for y in YEAR_RE.findall(label) if y not in years]
                if wrong:
                    err("paper", f, lineno,
                        f"the label {label!r} gives {wrong[0]}, which is not a year of {pid} "
                        f"({', '.join(sorted(years))})")
            for im in PAPER_ID_RE.finditer(text):
                if not any(a <= im.start() < b for a, b in spans):
                    err("paper", f, lineno,
                        f"{im.group(0)} is not a link to the paper (wiki/CLAUDE.md, Links): "
                        f"write [{im.group(0)}](URL)")

        # --- acronyms ---------------------------------------------------
        page_text = " ".join(prose(line) for _, line in clean)
        linked = set()
        for _, line in clean:
            for label in LINK_LABEL_RE.findall(INLINE_CODE_RE.sub(" ", line)):
                linked.update(ACRONYM_RE.findall(label))
        first_use = {}
        for lineno, line in ([] if record else clean):
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

        # --- symbols ------------------------------------------------------
        if rel not in SYMBOL_REGISTERS and not record:
            parts, starts, pos = [], [], 0  # starts: (offset in text, line number) per line
            for lineno, line in clean:
                parts.append(prose(line))
                starts.append((pos, lineno))
                pos += len(parts[-1]) + 1
            text = " ".join(parts)

            def line_at(offset):
                return max(start for start in starts if start[0] <= offset)[1]

            for sym, spec in SYMBOLS.items():
                other = spec.get("elsewhere", {}).get(rel)
                if other:
                    m = spec["always"].search(text)
                    if m:
                        err("symbol", f, line_at(m.start()),
                            f"{m.group(0)!r} uses {sym} as {spec['means']}, but {sym} is {other} on this page "
                            f"(SYMBOLS in scripts/check-wiki.py); give one of the two another symbol")
                    continue
                m = spec["use"].search(text)
                if m is None:
                    continue
                near = text[max(0, m.start() - BIND_WINDOW) : m.end() + BIND_WINDOW]
                if not all(d.search(near) for d in spec["define"]):
                    err("symbol", f, line_at(m.start()),
                        f"{sym} is first used here without a definition in words beside it ({spec['means']})")

    for sym, spec in SYMBOLS.items():
        for page in spec.get("elsewhere", {}):
            if not (WIKI / page).exists():
                err("symbol", WIKI / page, 1, f"SYMBOLS exempts this page from {sym}, but it does not exist")

    order = ["link", "anchor", "heading", "map", "source", "frontmatter", "weight", "section",
             "gist", "statusline", "status", "voice", "summary", "star", "h1", "fence", "acronym", "symbol", "paper"]
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
