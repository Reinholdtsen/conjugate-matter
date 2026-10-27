import sys, json, glob, os
for fn in sorted(glob.glob(os.path.join(sys.argv[1], '*.json'))):
    try:
        m = json.load(open(fn))['message']
    except Exception as exc:
        print(os.path.basename(fn), 'PARSE FAIL', open(fn).read()[:120]); continue
    au = ', '.join((a.get('given','')+' '+a.get('family','')).strip() for a in m.get('author', [])[:6])
    date = m.get('published-print', m.get('published-online', m.get('issued', {}))).get('date-parts', [[None]])[0]
    print(f"{m.get('DOI')}\n  title: {m.get('title')}\n  authors: {au}\n  container: {m.get('container-title')} vol {m.get('volume')} issue {m.get('issue')} page {m.get('page')} article {m.get('article-number')}\n  date: {date}")
