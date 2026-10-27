"""Safely extract text sources from downloaded arXiv e-prints (untrusted data; run with python -I).

For each downloads/arxiv/<id>/eprint.bin: gunzip; if the result is a tar archive, extract only
.tex/.bbl/.txt members with tarfile's 'data' filter (no absolute paths, no links, no devices)
into downloads/arxiv/<id>/src/; otherwise write the gunzipped bytes to src/main.tex.
Nothing extracted is executed.
"""
import gzip
import io
import pathlib
import sys
import tarfile

root = pathlib.Path(sys.argv[1])
for d in sorted(root.iterdir()):
    f = d / 'eprint.bin'
    if not f.exists():
        continue
    out = d / 'src'
    out.mkdir(exist_ok=True)
    raw = f.read_bytes()
    try:
        data = gzip.decompress(raw)
    except Exception:
        data = raw
    bio = io.BytesIO(data)
    n = 0
    if tarfile.is_tarfile(bio):
        bio.seek(0)
        with tarfile.open(fileobj=bio) as tf:
            members = [m for m in tf.getmembers() if m.isfile() and m.name.lower().endswith(('.tex', '.bbl', '.txt'))]
            for m in members:
                tf.extract(m, path=out, filter='data')
                n += 1
    else:
        (out / 'main.tex').write_bytes(data)
        n = 1
    print(d.name, 'extracted', n, 'files')
