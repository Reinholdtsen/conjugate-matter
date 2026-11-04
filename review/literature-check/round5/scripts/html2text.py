#!/usr/bin/env python3
"""html2text.py FILE: print the visible text of an HTML file, plus every <meta name=...> and every link href."""
import html.parser, re, sys
class P(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.out=[]; self.skip=0; self.meta=[]; self.links=[]
    def handle_starttag(self, t, a):
        a=dict(a)
        if t in ("script","style"): self.skip+=1
        if t=="meta" and (a.get("name") or a.get("property")): self.meta.append((a.get("name") or a.get("property"), a.get("content")))
        if t=="a" and a.get("href"): self.links.append(a["href"])
        if t in ("p","div","br","li","tr","h1","h2","h3","td","dd","dt"): self.out.append("\n")
    def handle_endtag(self, t):
        if t in ("script","style"): self.skip=max(0,self.skip-1)
    def handle_data(self, d):
        if not self.skip: self.out.append(d)
p=P(); p.feed(open(sys.argv[1],encoding="utf-8",errors="replace").read())
print("=== META"); [print(f"  {k}: {v}") for k,v in p.meta]
print("=== TEXT"); print(re.sub(r"\n\s*\n+","\n",re.sub(r"[ \t]+"," ","".join(p.out))).strip())
print("=== LINKS"); [print("  "+l) for l in p.links if "bitstream" in l or "handle" in l or ".pdf" in l.lower()]
