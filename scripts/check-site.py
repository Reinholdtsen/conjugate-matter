#!/usr/bin/env python3
"""Check the built site: every internal link resolves to a built page and every
#fragment to an id on that page.

scripts/check-wiki.py checks links and anchors in the Markdown, computing heading
IDs with its own emulation of Hugo's. This script checks the HTML Hugo actually
wrote, so a difference between the two (an anchor the emulation accepts but Hugo
spells differently) fails here, instead of a link on the site landing at the top
of the page rather than at its heading. It also covers what the Markdown check
cannot see: links the theme generates (menu, table of contents, brand).

Checked: the href of every <a> in every built .html file. An href with a scheme
or host (https:, mailto:, //host) is external and skipped; so is javascript:.
A relative href resolves against the page's own URL, as a browser resolves it.
A fragment is compared with the id attributes of the target page; a link to a
non-HTML file is checked for existence only.

Run it after a build. From site/, `npm run check` runs the root gate, the Hugo
build and then this script.

Usage: scripts/check-site.py [PUBLIC_DIR]     (default: site/public)

Exit status is 1 if any link or fragment fails to resolve, 0 otherwise.
"""

import posixpath
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site" / "public"


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.hrefs = set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])


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
        for href in c.hrefs:
            u = urlsplit(href)
            if u.scheme or u.netloc:
                continue
            target = f if not u.path else page_file(urljoin(here, u.path))
            if target is None:
                errors.add(f"{here}: link to missing page {href}")
                continue
            frag = unquote(u.fragment)
            if frag and target in pages and frag not in pages[target].ids:
                errors.add(f"{here}: no id '{frag}' on {page_url(target)} ({href})")
    for e in sorted(errors):
        print(e)
    n_links = sum(len(c.hrefs) for c in pages.values())
    if errors:
        print(f"\nsite check FAILED: {len(errors)} problem(s) in {len(pages)} pages", file=sys.stderr)
        return 1
    print(f"site OK — {len(pages)} pages, {n_links} links, every internal link and anchor resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
