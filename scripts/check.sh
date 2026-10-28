#!/usr/bin/env bash
#
# The definition of done for this repo. Exits non-zero if any verification
# script fails. New arbitration and audit scripts in verify/ get added here.
#
# Run it with:  scripts/check.sh
# First time:   python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
set -uo pipefail

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)" || exit 1

py=.venv/bin/python
if [ ! -x "$py" ]; then
  echo "check FAILED: no .venv. Create it with:"
  echo "  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
  exit 1
fi

status=0

for script in verify/battery.py verify/soliton_obituary.py verify/toy_coset.py verify/toy_gw.py verify/toy_s4.py verify/toy_s5.py verify/phase_space_diameter.py verify/closed_universe.py; do
  if ! "$py" "$script"; then
    echo "$script FAILED"
    status=1
  fi
  echo
done

# The wiki: internal links, anchors, section maps, source paths, frontmatter,
# page shape and acronyms. Hugo would render a dead link without complaint.
if ! "$py" scripts/check-wiki.py; then
  echo "scripts/check-wiki.py FAILED"
  status=1
fi
echo

if [ "$status" -eq 0 ]; then
  echo "OK — all checks pass."
fi

exit "$status"
