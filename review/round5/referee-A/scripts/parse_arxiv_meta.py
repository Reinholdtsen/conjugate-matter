import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
root = ET.parse(sys.argv[1]).getroot()
for e in root.findall('a:entry', ns):
    idd = e.find('a:id', ns).text.strip()
    title = ' '.join(e.find('a:title', ns).text.split())
    authors = ', '.join(a.find('a:name', ns).text for a in e.findall('a:author', ns))
    jr = e.find('arxiv:journal_ref', ns)
    doi = e.find('arxiv:doi', ns)
    pub = e.find('a:published', ns).text[:10]
    print(f"{idd}\n  title: {title}\n  authors: {authors[:200]}\n  journal_ref: {jr.text.strip() if jr is not None else '-'}\n  doi: {doi.text.strip() if doi is not None else '-'}\n  first version: {pub}")
