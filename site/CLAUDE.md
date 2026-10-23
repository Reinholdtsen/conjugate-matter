# site/ — the wiki as a static site

The Hugo site that publishes the program's wiki. Hugo with the hugo-book theme
builds `../wiki` into static HTML in `public/`, and a Cloudflare Workers
static-assets Worker, `conjugate-matter-wiki`, serves it. It is the same stack as
Paul's other Hugo sites (`~/git/bitsy-services/wiki`, and
`~/git/gargantis/gargantis/site` for the `site/` subfolder). Paul deploys it by
hand. No domain has been chosen yet.

## The content is not here

`hugo.toml` mounts `../wiki` (the repository's `wiki/` folder) as
`content/wiki`. Edit pages in `wiki/`, following `wiki/CLAUDE.md`; never copy
them into `site/content/`. `wiki/a/b.md` serves at `/wiki/a/b/`. The only page in
`site/content/` is the home page `/`, a short introduction that links to `/wiki`.
It sets no `title`: `layouts/home.html` renders the site title from `hugo.toml`
as its h1.

`ignoreFiles = ['CLAUDE\.md$']` keeps `wiki/CLAUDE.md`, and any CLAUDE.md added
under the content, from being built as a page. This file is outside the content
mounts.

## Files

- `hugo.toml` — site configuration: baseURL, title, theme, the `../wiki` mount,
  the hugo-book params (`BookSection = 'wiki'`, `BookPortableLinks = 'error'`).
- `content/_index.md` — the home page.
- `layouts/` — `single.html`, `list.html` and `home.html` render the page title
  as the h1, which hugo-book does not do. A file here shadows the theme's file of
  the same name.
- `themes/hugo-book` — the theme, a git submodule pinned to v13
  (`cec082b8dd9b31d0c52b2de95d86ced9909cc7ec`, the commit
  `bitsy-services/wiki` uses). Do not edit it.
- `package.json`, `package-lock.json` — the npm scripts below; `hugo-bin`
  0.166.0, which installs Hugo 0.168.0 extended, and `wrangler`.
- `wrangler.jsonc` — the Worker: `assets.directory` `./public`, Hugo's
  `404.html` for unknown paths, observability on, no routes.
- `public/`, `resources/`, `node_modules/`, `.hugo_build.lock`, `.wrangler/` —
  generated, git-ignored.

## Setup, once per clone

```sh
# from the repository root
git submodule update --init         # the theme
cd site && npm install              # Hugo (via hugo-bin) and wrangler
```

The root gate also needs the repository's `.venv` (root `CLAUDE.md`, "The gate").

## Commands (run from site/)

- `npm run dev` — `hugo server`, live reload at http://localhost:1313/.
- `npm run build` — `hugo --gc --minify --cleanDestinationDir` into `public/`.
  `--cleanDestinationDir` removes files a previous build left behind, so a
  renamed page's old HTML is neither checked against nor deployed.
- `npm run check` — the site's gate; see below.
- `npm run preview` — build, then `wrangler dev` serves `public/` locally the way
  the Worker will.
- `npm run deploy` — `npm run check`, then `wrangler deploy`.

## The gate

`npm run check` must pass before any deploy. It is not advisory, and
`npm run deploy` runs it first. It runs:

1. `../scripts/check.sh` — the repository's gate: every `verify/` script, then
   `scripts/check-wiki.py` on the Markdown;
2. the Hugo build;
3. `python3 ../scripts/check-site.py` on the HTML in `public/`.

Hugo itself validates no Markdown links, so links are checked in three layers:

1. **`scripts/check-wiki.py`, on the Markdown.** Every `/wiki/...` link must name
   a page and every `#fragment` a heading. It computes heading IDs the way Hugo
   does: subscript and superscript digits are dropped, so the heading
   "What w₀ and wₐ mean" has the ID `what-w-and-wₐ-mean`.
2. **`BookPortableLinks = 'error'`, in the build.** hugo-book's link render hook
   resolves every internal Markdown link through `.Page.GetPage` to the page's
   URL, so the `/wiki/...` links also work under a baseURL with a subpath, and a
   link to a page that does not exist fails the build. Its message reads
   "Image reference '…' not found" even for a page link. It does not check
   `#fragments`.
3. **`scripts/check-site.py`, on the HTML.** Every internal `<a href>` in the
   built site must resolve to a built file and every `#fragment` to an id on the
   target page. It also covers the links the theme generates (menu, table of
   contents), and it is the authority where layer 1's ID emulation and Hugo
   disagree.

Do not weaken any layer to make a build pass. Fix the link.

## Deploying (manual)

```sh
npx wrangler login     # once per machine
npm run deploy         # from site/: the gate, then wrangler deploy
```

Without routes, the Worker serves on its `workers.dev` subdomain. Nothing
deploys automatically.

## Adding a domain

1. In `wrangler.jsonc`, add after the `assets` block (the comment there shows
   it): `"routes": [{ "pattern": "<domain>", "custom_domain": true }]`. The
   domain's zone must be on the same Cloudflare account; the deploy creates the
   DNS record.
2. In `hugo.toml`, set `baseURL = 'https://<domain>/'`.
3. `npm run deploy`.

## Hugo and theme versions

`package-lock.json` pins `hugo-bin` 0.166.0, and that release installs Hugo
0.168.0 extended. hugo-book v13 builds with it, with four deprecation warnings
from the theme's templates: `.Site.Sites`, `.Site.LanguageCode`,
`.Language.LanguageDirection` and libsass. Hugo removes deprecated features in
later releases. Before upgrading `hugo-bin`, run `npm run check` on the new
version; if the build fails in the theme, update the submodule to a hugo-book
release that supports it, or keep the old version.
