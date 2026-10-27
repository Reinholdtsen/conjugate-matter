#!/bin/bash
# usage: fetch_crossref.sh outdir doi...
out="$1"; shift
for d in "$@"; do
  fn=$(echo "$d" | tr '/()' '___')
  curl -sS -m 40 -o "$out/$fn.json" "https://api.crossref.org/works/$d"
done
