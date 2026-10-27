"""Extract embedded page images from an untrusted scanned PDF (run with python -I).
Usage: pdf_images.py in.pdf outdir first_page last_page"""
import sys, pathlib
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
a, b = int(sys.argv[3]), int(sys.argv[4])
for i in range(a - 1, min(b, len(r.pages))):
    for j, im in enumerate(r.pages[i].images):
        ext = pathlib.Path(im.name).suffix or '.png'
        fn = out / f'p{i+1:02d}_{j}{ext}'
        fn.write_bytes(im.data)
        print(fn, len(im.data))
