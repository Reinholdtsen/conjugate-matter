# Minimal PDF text extractor (independent of the analysis agent's tools/pdftext.py).
# Inflates FlateDecode streams and pulls strings from Tj / TJ / ' / " operators.
# Usage: python -I pdf_text.py file.pdf > out.txt
import sys, re, zlib

data = open(sys.argv[1], 'rb').read()
out = []
for m in re.finditer(rb'stream\r?\n', data):
    start = m.end()
    end = data.find(b'endstream', start)
    if end < 0:
        continue
    raw = data[start:end]
    try:
        dec = zlib.decompress(raw)
    except Exception:
        try:
            dec = zlib.decompressobj().decompress(raw)
        except Exception:
            continue
    if b'Tj' not in dec and b'TJ' not in dec:
        continue
    # walk text objects
    line = []
    for tok in re.finditer(rb'\[(.*?)\]\s*TJ|\((.*?)(?<!\\)\)\s*Tj|(T\*|Td|TD|Tm|ET)', dec, re.S):
        if tok.group(1) is not None:
            parts = re.findall(rb'\((.*?)(?<!\\)\)|(-?\d+\.?\d*)', tok.group(1), re.S)
            s = b''
            for p, num in parts:
                if p:
                    s += p
                elif num:
                    try:
                        if float(num) < -200:
                            s += b' '
                    except ValueError:
                        pass
            line.append(s)
        elif tok.group(2) is not None:
            line.append(tok.group(2))
        else:
            if line:
                out.append(b''.join(line))
                line = []
    if line:
        out.append(b''.join(line))

txt = b'\n'.join(out)
txt = txt.replace(b'\\(', b'(').replace(b'\\)', b')').replace(b'\\\\', b'\\')
sys.stdout.write(txt.decode('latin-1'))
