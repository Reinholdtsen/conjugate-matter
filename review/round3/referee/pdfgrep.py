import sys, re, os
from pypdf import PdfReader
pdf, out = sys.argv[1], sys.argv[2]
if not os.path.exists(out):
    r = PdfReader(pdf)
    txt = []
    for i, p in enumerate(r.pages):
        try:
            txt.append(f"\n[[PAGE {i+1}]]\n" + (p.extract_text() or ""))
        except Exception as e:
            txt.append(f"\n[[PAGE {i+1} ERR {e}]]\n")
    open(out, "w").write("".join(txt))
t = open(out).read()
for pat in sys.argv[3:]:
    print(f"##### pattern: {pat}")
    for m in re.finditer(pat, t, flags=re.I):
        s = max(0, m.start()-350); e = min(len(t), m.end()+350)
        pg = t.rfind("[[PAGE", 0, m.start())
        print(t[pg:pg+12].strip(), "...", " ".join(t[s:e].split()))
        print("---")
