"""Extract text from an untrusted PDF with pypdf (run with python -I). Usage: pdf2txt.py in.pdf out.txt"""
import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
with open(sys.argv[2], 'w') as f:
    for i, p in enumerate(r.pages):
        try:
            t = p.extract_text() or ''
        except Exception as ex:
            t = f'[extract error {ex}]'
        f.write(f'\n=== PAGE {i+1} ===\n{t}')
print('pages', len(r.pages))
