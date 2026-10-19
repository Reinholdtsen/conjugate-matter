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

if ! "$py" verify/battery.py; then
  echo "verify/battery.py FAILED"
  status=1
fi

if [ "$status" -eq 0 ]; then
  echo "OK — all checks pass."
fi

exit "$status"
