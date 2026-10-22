#!/usr/bin/env python3
"""Part G addendum: det^2 (complex) on the eta' = diag(1,-1) families, k = 0..d; spread and value."""
import numpy as np
rng = np.random.default_rng(5)
for d in (2, 3, 4):
    I = np.eye(d)
    for k in range(d + 1):
        vals = []
        for t in range(100):
            Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
            O = Q @ np.diag([1.0] * k + [-1.0] * (d - k)) @ Q.T
            B = np.vstack([I, O]) / np.sqrt(2)
            U = B[:d] + 1j * B[d:]
            vals.append(np.linalg.det(U) ** 2)
        vals = np.array(vals)
        print(f"d={d} k={k}: det^2 mean {vals.mean():+.6f}, max spread |det^2 - mean| {np.abs(vals - vals.mean()).max():.1e}, "
              f"predicted i^(2k-d) = {complex(1j ** (2 * k - d)):+.3f}")
