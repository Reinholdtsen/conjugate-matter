"""Minimal PDF text extractor (FlateDecode content streams, literal and hex strings).
Usage: python -I pdftext.py file.pdf > out.txt
Reads untrusted data; only decompresses and prints text tokens."""
import re
import sys
import zlib


def unescape(s: bytes) -> str:
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == 0x5C and i + 1 < len(s):  # backslash
            n = s[i + 1]
            m = {ord('n'): '\n', ord('r'): '\r', ord('t'): '\t', ord('b'): '\b', ord('f'): '\f',
                 ord('('): '(', ord(')'): ')', ord('\\'): '\\'}
            if n in m:
                out.append(m[n]); i += 2; continue
            if 0x30 <= n <= 0x37:
                j = i + 1; oct_ = b''
                while j < len(s) and len(oct_) < 3 and 0x30 <= s[j] <= 0x37:
                    oct_ += bytes([s[j]]); j += 1
                out.append(chr(int(oct_, 8))); i = j; continue
            i += 2; continue
        out.append(chr(c)); i += 1
    return ''.join(out)


def text_from_stream(data: bytes) -> str:
    res = []
    # tokens: literal strings (balanced parens, simplified), hex strings, operators
    i = 0
    n = len(data)
    line = []
    while i < n:
        c = data[i]
        if c == 0x28:  # (
            depth = 1; j = i + 1; buf = bytearray()
            while j < n and depth > 0:
                ch = data[j]
                if ch == 0x5C:
                    buf += data[j:j + 2]; j += 2; continue
                if ch == 0x28:
                    depth += 1
                elif ch == 0x29:
                    depth -= 1
                    if depth == 0:
                        break
                buf.append(ch); j += 1
            line.append(unescape(bytes(buf)))
            i = j + 1
            continue
        if c == 0x3C and i + 1 < n and data[i + 1] != 0x3C:  # hex string
            j = data.find(b'>', i)
            hx = re.sub(rb'\s', b'', data[i + 1:j])
            try:
                b = bytes.fromhex(hx.decode('ascii') + ('0' if len(hx) % 2 else ''))
                line.append(b.decode('latin-1'))
            except Exception:
                pass
            i = j + 1
            continue
        # operators that end a line
        if data[i:i + 2] in (b'Td', b'TD', b'T*') or data[i:i + 2] == b'ET':
            if line:
                res.append(''.join(line)); line = []
            i += 2
            continue
        if data[i:i + 2] == b'TJ':
            i += 2
            continue
        i += 1
    if line:
        res.append(''.join(line))
    return '\n'.join(res)


def main(path):
    raw = open(path, 'rb').read()
    for m in re.finditer(rb'stream\r?\n', raw):
        start = m.end()
        end = raw.find(b'endstream', start)
        chunk = raw[start:end]
        try:
            dec = zlib.decompress(chunk)
        except Exception:
            try:
                dec = zlib.decompressobj().decompress(chunk)
            except Exception:
                continue
        if b'BT' in dec and (b'Tj' in dec or b'TJ' in dec):
            t = text_from_stream(dec)
            if t.strip():
                print(t)
                print('=' * 20)


if __name__ == '__main__':
    main(sys.argv[1])
