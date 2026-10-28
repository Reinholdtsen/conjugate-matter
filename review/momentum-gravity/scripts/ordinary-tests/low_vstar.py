"""Gaussian body-level gate at low v*: where does LLR take over from the O(1) Eros bound?"""
import io, contextlib
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import bounds as B
for vs in [0.10, 0.12, 0.15, 0.18, 0.20, 0.22, 0.25, 0.30, 0.35, 0.40, 0.50]:
    b = B.all_bounds(vs, 'gauss')
    k = min(b, key=b.get)
    print(f"v* = {vs:5.2f} km/s: LLR perigee |eps| < {b['LLR perigee']:.2e}; strongest: {k} {b[k]:.2e}")
