#!/usr/bin/env python3
"""Check the built site: every internal link resolves, every page of wiki/ is
built, and Hugo wrote the heading IDs that scripts/check-wiki.py computes.

scripts/check-wiki.py checks links and anchors in the Markdown, computing heading
IDs with its own emulation of Hugo's. This script checks the HTML Hugo actually
wrote, so a difference between the two (an anchor the emulation accepts but Hugo
spells differently) fails here, instead of a link on the site landing at the top
of the page rather than at its heading. It also covers what the Markdown check
cannot see: links the theme generates (menu, table of contents, brand), the
theme's assets, and what the build left out.

Checked, in every built .html file:

  link     every href and src. One with a scheme or host (https:, mailto:,
           //host) is external and skipped; any other resolves against the
           page's own URL, as a browser resolves it, and must name a built file.
           A #fragment must be an id on the target page (a link to a non-HTML
           file is checked for existence only).
  h1       the page has exactly one h1.

and, for wiki/:

  page     every page is built, and no CLAUDE.md is. Hugo skips a draft, a
           future-dated or an expired page without an error.
  heading  a page's heading IDs, in order, are the ones scripts/check-wiki.py
           computes (slugify and heading_id).

A run that finds no pages or no links fails: then the checker is broken, not the
site.

Run it after a build. From site/, `npm run check` runs the root gate, the Hugo
build and then this script.

Usage: scripts/check-site.py [PUBLIC_DIR]     (default: site/public)

Exit status is 1 if any check fails, 0 otherwise.
"""

import importlib.util
import posixpath
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PUBLIC = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "site" / "public"
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


def load_check_wiki():
    """scripts/check-wiki.py as a module (its file name cannot be imported)."""
    spec = importlib.util.spec_from_file_location("check_wiki", ROOT / "scripts" / "check-wiki.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Collector(HTMLParser):
    """A page's ids, its references (href and src), its number of h1 elements,
    and the headings inside its <article> in order, as (tag, id)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.headings = set(), [], []
        self.h1s = self.article = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        self.refs.extend(a[name] for name in ("href", "src") if a.get(name))
        if tag == "h1":
            self.h1s += 1
        if tag == "article":
            self.article += 1
        if self.article and tag in HEADINGS:
            self.headings.append((tag, a.get("id") or ""))

    def handle_endtag(self, tag):
        if tag == "article" and self.article:
            self.article -= 1


def page_url(f):
    """The URL path a built file serves at: public/a/b/index.html is /a/b/."""
    rel = f.relative_to(PUBLIC).as_posix()
    if rel == "index.html" or rel.endswith("/index.html"):
        rel = rel[: -len("index.html")]
    return "/" + rel


def page_file(path):
    """Map a URL path to the built file that serves it, or None."""
    path = posixpath.normpath("/" + unquote(path).lstrip("/"))
    p = PUBLIC / path.lstrip("/")
    if p.is_dir():
        p = p / "index.html"
    return p if p.is_file() else None


def wiki_heading_ids(cw, src):
    """The IDs scripts/check-wiki.py gives a wiki page's headings, in order ('' for
    a heading that Hugo gives none)."""
    _, body, offset = cw.split_frontmatter(src.read_text(encoding="utf-8"))
    clean, _ = cw.strip_code(body, offset)
    used, ids = set(), []
    for _, line in clean:
        m = cw.HEADING_RE.match(line)
        if m:
            slug = cw.slugify(m.group(2))
            ids.append("" if slug is None else cw.heading_id(slug, used))
    return ids


def main():
    if not PUBLIC.is_dir():
        print(f"site check FAILED: {PUBLIC} does not exist; build the site first")
        return 1
    pages = {}
    for f in PUBLIC.rglob("*.html"):
        c = Collector()
        c.feed(f.read_text(encoding="utf-8", errors="replace"))
        pages[f] = c
    errors = set()
    for f, c in pages.items():
        here = page_url(f)
        if c.h1s != 1:
            errors.add(f"{here}: {c.h1s} h1 elements, not 1")
        for ref in c.refs:
            u = urlsplit(ref)
            if u.scheme or u.netloc:
                continue
            target = f if not u.path else page_file(urljoin(here, u.path))
            if target is None:
                errors.add(f"{here}: link to missing file {ref}")
                continue
            frag = unquote(u.fragment)
            if frag and target in pages and frag not in pages[target].ids:
                errors.add(f"{here}: no id '{frag}' on {page_url(target)} ({ref})")

    cw = load_check_wiki()
    n_wiki = n_headings = 0
    for src in sorted(WIKI.rglob("*.md")):
        # Hugo lowercases URLs, so wiki/CLAUDE.md would build at /wiki/claude/.
        built = PUBLIC / cw.page_url(src).lower().lstrip("/") / "index.html"
        name = src.relative_to(ROOT)
        if src.name == "CLAUDE.md":
            if built.exists():
                errors.add(f"{page_url(built)}: {name} is built as a page")
            continue
        if built not in pages:
            errors.add(f"{name}: not built (a draft, future-dated or expired page?)")
            continue
        n_wiki += 1
        hugo = [hid for _, hid in pages[built].headings]
        if pages[built].headings[:1] == [("h1", "")]:
            hugo = hugo[1:]  # the page title, which the layout renders without an ID
        mine = wiki_heading_ids(cw, src)
        n_headings += len(mine)
        if hugo != mine:
            n = next((i for i, (h, m) in enumerate(zip(hugo, mine)) if h != m), min(len(hugo), len(mine)))
            on_site = repr(hugo[n]) if n < len(hugo) else "no heading"
            computed = repr(mine[n]) if n < len(mine) else "no heading"
            errors.add(f"{name}: heading {n + 1} has the ID {on_site} on the site but {computed} "
                       f"in scripts/check-wiki.py; fix its slugify")

    n_refs = sum(len(c.refs) for c in pages.values())
    if not pages or not n_refs:
        errors.add(f"{len(pages)} pages and {n_refs} links found: the build or this check is broken")
    for e in sorted(errors):
        print(e)
    if errors:
        print(f"\nsite check FAILED: {len(errors)} problem(s) in {len(pages)} pages", file=sys.stderr)
        return 1
    print(f"site OK — {len(pages)} pages, {n_refs} links, every internal link and anchor resolves; "
          f"{n_wiki} wiki pages built, {n_headings} heading IDs as scripts/check-wiki.py computes them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
