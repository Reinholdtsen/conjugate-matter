#!/usr/bin/env bash
# q.sh ID SUBCOMMAND ARGS...  -> runs the check's own lit.py, saves the full output to out/ID.txt,
# logs time, id, command and first output line to queries.tsv (round 5 of the literature check).
D="$(cd "$(dirname "$0")/.." && pwd)"
LIT="$D/../tools/lit.py"
id=$1; shift
out=$(python3 "$LIT" "$@" 2>&1)
printf '%s\n' "$out" > "$D/out/$id.txt"
first=$(printf '%s\n' "$out" | head -1)
printf '%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$id" "$*" "$first" >> "$D/queries.tsv"
printf '%s\n' "$first"
