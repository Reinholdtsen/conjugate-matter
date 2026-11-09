#!/usr/bin/env bash
#
# Run before a deploy (site/: npm run deploy). The site links every repository
# file outside the wiki on GitHub at main (site/layouts/_markup/render-link.html),
# so GitHub's main must hold exactly this checkout: on main, nothing uncommitted
# in tracked files, and HEAD equal to origin/main. scripts/check-site.py has
# already checked that every linked file is tracked. Needs the network (git fetch).
set -uo pipefail

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)" || exit 1

fail() { echo "deploy FAILED: $1"; exit 1; }

branch=$(git rev-parse --abbrev-ref HEAD)
[ "$branch" = main ] || fail "on branch $branch; the site links files on GitHub's main"
[ -z "$(git status --porcelain --untracked-files=no)" ] || fail "uncommitted changes; commit and push first"
git fetch --quiet origin main || fail "git fetch origin main failed"
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] ||
  fail "HEAD $(git rev-parse --short HEAD) is not origin/main $(git rev-parse --short origin/main); push first"

echo "pushed OK — main is origin/main at $(git rev-parse --short HEAD)"
