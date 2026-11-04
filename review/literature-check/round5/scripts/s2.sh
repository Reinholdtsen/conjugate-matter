#!/usr/bin/env bash
# s2.sh ID 'QUERY' -> one request to Semantic Scholar's public search API (no key), saves out/ID.json and
# out/ID.headers, logs to queries.tsv. No retry: a 429 is recorded as such.
D="$(cd "$(dirname "$0")/.." && pwd)"
id=$1; q=$2
url="https://api.semanticscholar.org/graph/v1/paper/search?$(python3 -I -c 'import sys,urllib.parse;print(urllib.parse.urlencode({"query":sys.argv[1],"limit":100,"fields":"title,year,authors,venue,journal,externalIds,abstract,publicationTypes"}))' "$q")"
code=$(curl -s -A "conjugate-matter-literature-check/1.0 (research script)" -D "$D/out/$id.headers" -o "$D/out/$id.json" -w "%{http_code}" "$url")
if [ "$code" = "200" ]; then
  first=$(python3 -I -c 'import json,sys;d=json.load(open(sys.argv[1]));print(f"S2: {d.get(\"total\")} hits (showing {len(d.get(\"data\",[]))})")' "$D/out/$id.json")
else
  first="S2 HTTP $code: $(head -c 300 "$D/out/$id.json")"
fi
printf '%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$id" "s2 search: $q" "$first" >> "$D/queries.tsv"
echo "$first"
