"""Decode dvips Type-3 glyph-name text of the form /XY (base-36 pairs, offset 360). Usage: python -I decode_t3.py in.txt out.txt"""
import sys, re
D = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def dec(m):
    a, b = m.group(1), m.group(2)
    v = D.index(a) * 36 + D.index(b) - 360
    if 32 <= v < 127:
        return chr(v)
    return {12: 'fi', 13: 'fl', 11: 'ff', 14: 'ffi'}.get(v, '?')
t = open(sys.argv[1], encoding='utf-8', errors='replace').read()
t = re.sub(r'/([0-9A-Z])([0-9A-Z])', dec, t)
open(sys.argv[2], 'w').write(t)
