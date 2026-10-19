import json, urllib.request, urllib.parse, sys, os, time
OUT = sys.argv[1]
queries = {
 "1a": 'j "Proc.Roy.Soc.Lond.A,165,291"',
 "1b": 'j "Rev.Mod.Phys.,21,463"',
 "2": 'arxiv:hep-th/0007220',
 "3a": 'arxiv:1106.3344',
 "3b": 'arxiv:1109.3515',
 "4a": 'arxiv:1202.1986',
 "4b": 'arxiv:1407.4331',
 "4c": 'arxiv:1410.0207',
 "5": 'arxiv:1503.07521',
 "6": 'j "Nucl.Phys.B,282,397"',
 "7a": 'j "Proc.Roy.Soc.Lond.A,133,60"',
 "7b": 'j "Phys.Rev.,176,1489"',
 "8a": 'j "Phys.Lett.B,72,117"',
 "8b": 'j "Phys.Lett.B,83,321"',
 "8c": 'arxiv:hep-th/9603086',
 "9": 'arxiv:1909.00696',
 "10a": 'arxiv:0901.0283',
 "10b": 'arxiv:0907.4746',
 "10c": 'arxiv:0902.3615',
 "11a": 'arxiv:1011.5120',
 "11b": 'arxiv:1810.05338',
 "12": 'arxiv:2109.12771',
 "13": 'arxiv:1808.09459',
 "14": 'arxiv:0905.0633',
 "15a": 'j "Nucl.Phys.B,79,276"',
 "15b": 'j "JETP Lett.,20,194"',
 "16a": 'j "Phys.Rev.Lett.,35,760"',
 "16b": 'j "Sov.J.Nucl.Phys.,24,449"',
 "17": 't "The Early Universe" and a Kolb',
 "18": 'j "J.Phys.A,9,1387"',
 "19": 'j "Phys.Rev.Lett.,43,1365"',
 "20b": 'j "Phys.Rev.D,26,1296"',
 "20c": 'j "Astrophys.J.,160,383"',
 "21": 'arxiv:hep-ex/0207020',
 "22": 'j "Phys.Rev.Lett.,70,2511"',
 "23": 'arxiv:1807.06209',
}
fields = "titles,authors.full_name,publication_info,arxiv_eprints,dois,author_count"
res = {}
for k, q in queries.items():
    url = "https://inspirehep.net/api/literature?" + urllib.parse.urlencode({"q": q, "fields": fields, "size": 3})
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.load(r)
    except Exception as e:
        print(k, "ERROR", e); continue
    res[k] = {"url": url, "data": d}
    hits = d["hits"]["hits"]
    print(f"=== [{k}] q={q}  total={d['hits']['total']}")
    for h in hits:
        m = h["metadata"]
        t = m.get("titles", [{}])[0].get("title")
        au = [a["full_name"] for a in m.get("authors", [])][:8]
        pi = [(p.get("journal_title"), p.get("journal_volume"), p.get("page_start") or p.get("artid"), p.get("year")) for p in m.get("publication_info", []) if p.get("journal_title")]
        ax = [a["value"] for a in m.get("arxiv_eprints", [])]
        print(f"   recid={h['id']} title={t!r}\n   authors={au} (n={m.get('author_count')})\n   pub={pi} arxiv={ax}")
    time.sleep(0.4)
json.dump(res, open(OUT, "w"), indent=1)
