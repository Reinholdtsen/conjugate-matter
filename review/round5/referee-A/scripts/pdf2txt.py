"""Extract text from an untrusted PDF (read-only, no execution). Usage: python -I pdf2txt.py in.pdf out.txt"""
import sys
from pypdf import PdfReader

src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src)
parts = []
for i, p in enumerate(r.pages):
    try:
        t = p.extract_text() or ""
    except Exception as exc:  # noqa
        t = f"[page {i+1}: extract error {exc}]"
    parts.append(f"\n===== page {i+1} =====\n" + t)
with open(dst, "w", encoding="utf-8") as fh:
    fh.write("".join(parts))
print(f"{src}: {len(r.pages)} pages -> {dst}")
