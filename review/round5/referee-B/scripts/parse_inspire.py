"""Parse saved INSPIRE JSON records (untrusted data; run with python -I) and print bibliographic fields."""
import json
import sys
import pathlib

d = pathlib.Path(sys.argv[1])
for f in sorted(d.glob('*.json')):
    try:
        js = json.loads(f.read_text())
    except Exception as ex:
        print(f.name, 'PARSE ERROR', ex)
        continue
    hits = js.get('hits', {}).get('hits', [])
    if not hits:
        print(f'{f.stem:<22s} NO HIT')
        continue
    md = hits[0]['metadata']
    title = md.get('titles', [{}])[0].get('title', '')
    auth = [a.get('full_name', '') for a in md.get('authors', [])[:6]]
    nauth = md.get('author_count', len(md.get('authors', [])))
    pubs = []
    for p in md.get('publication_info', []):
        pubs.append('%s %s, %s (%s)' % (p.get('journal_title', ''), p.get('journal_volume', ''),
                                         p.get('artid', p.get('page_start', '')), p.get('year', '')))
    dois = [x.get('value') for x in md.get('dois', [])]
    print(f'{f.stem:<22s} | {title}')
    print(f'{"":<22s} | authors({nauth}): {"; ".join(auth)}')
    print(f'{"":<22s} | pub: {" || ".join(pubs)} | doi: {", ".join(dois[:3])}')
