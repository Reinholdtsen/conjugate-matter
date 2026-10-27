"""Parse saved Crossref JSON (untrusted data; run with python -I)."""
import json, sys, pathlib
for f in sorted(pathlib.Path(sys.argv[1]).glob('*.json')):
    try:
        m = json.loads(f.read_text())['message']
    except Exception as ex:
        print(f.name, 'PARSE ERROR', ex); continue
    au = '; '.join((a.get('given','') + ' ' + a.get('family','')).strip() for a in m.get('author', [])[:5])
    yr = (m.get('issued', {}).get('date-parts') or [[None]])[0][0]
    print(f"{f.stem:<36s} | {m.get('title',[''])[0]}")
    print(f"{'':<36s} | {au} | {m.get('container-title',[''])[0] if m.get('container-title') else ''} {m.get('volume','')}({m.get('issue','')}) {m.get('page','')} [{yr}]")
