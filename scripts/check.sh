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

for script in verify/battery.py verify/soliton_obituary.py verify/toy_coset.py; do
  if ! "$py" "$script"; then
    echo "$script FAILED"
    status=1
  fi
  echo
done

if [ "$status" -eq 0 ]; then
  echo "OK — all checks pass."
fi

exit "$status"
