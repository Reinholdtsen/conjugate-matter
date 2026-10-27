import sys, json
for fn in sys.argv[1:]:
    print('###', fn)
    d = json.load(open(fn))
    for h in d['hits']['hits']:
        m = h['metadata']
        print('  title:', [t['title'] for t in m.get('titles', [])][:1])
        print('  pubinfo:', m.get('publication_info'))
        print('  dois:', m.get('dois'))
        if 'abstracts' in m:
            for a in m['abstracts']:
                print('  abstract:', a['value'])
