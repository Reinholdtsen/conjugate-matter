import sys, json
for fn in sys.argv[1:]:
    print('###', fn)
    try:
        items = json.load(open(fn))['message']['items']
    except Exception as exc:
        print('PARSE FAIL'); continue
    for m in items:
        au = ', '.join((a.get('given','')+' '+a.get('family','')).strip() for a in m.get('author', [])[:5])
        date = m.get('published-print', m.get('published-online', m.get('issued', {}))).get('date-parts', [[None]])[0]
        print(f"  {m.get('DOI')} | {m.get('title')} | {au} | {m.get('container-title')} vol {m.get('volume')} issue {m.get('issue')} page {m.get('page')} art {m.get('article-number')} | {date}")
