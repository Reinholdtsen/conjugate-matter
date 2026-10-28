"""Sensitivity of the velocity-structure diagnostics (round 3, label "corner"): inject artificial
velocity-selected structure into a real snapshot and measure the response.
  clumps: a fraction f of the particles is regrouped into compact co-moving groups of 10 (positions
          within 0.05 r50 of a seed particle, canonical velocities within 0.2 v* of the seed's);
  stream: a fraction f of the particles inside r50 get a common velocity direction (spread 0.1 rad),
          speeds kept.
Snapshot: run_H_eps10_rg1_N2000_s1 at t = 40 (and the eps = 0 run if present).
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import diagnostics as D   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)


def measure(x, w, vs):
    c = D.centre(x); x = x - c
    r = np.linalg.norm(x, axis=1); r50 = np.median(r)
    xi, _, _ = D.Xi(x, w, 0.25 * r50, [vs, 0.5 * vs])
    sl = D.S_l(x, w)
    return xi[0], xi[1], sl[0], sl[1], D.R_v(x, w, r50)


for name in ("run_H_eps10_rg1_N2000_s1.npz", "run_H_eps0_rg1_N2000_s1.npz"):
    fn = os.path.join(HERE, "runs", name)
    if not os.path.exists(fn):
        continue
    d = np.load(fn)
    meta = eval(str(d['meta'][0]), {'np': np})
    vs = float(meta['vstar'])
    x0 = d['x'][-1].astype(float); w0 = d['w'][-1].astype(float)
    r50 = np.median(np.linalg.norm(x0 - D.centre(x0), axis=1))
    print(f"{name}: t = 40, r50 = {r50:.3f}, v* = {vs:.4f}")
    print(f"   original:            Xi(v*) Xi(v*/2) S1 S2 Rv = " + " ".join(f"{v:+.4f}" for v in measure(x0, w0, vs)))
    for f in (0.02, 0.05, 0.10):
        x = x0.copy(); w = w0.copy()
        n = len(x); ng = int(f * n / 10)
        idx = rng.permutation(n)[:ng * 10].reshape(ng, 10)
        for g in idx:
            s = g[0]
            x[g[1:]] = x[s] + rng.normal(scale=0.05 * r50, size=(9, 3))
            w[g[1:]] = w[s] + rng.normal(scale=0.2 * vs / np.sqrt(3), size=(9, 3))
        print(f"   clumps f = {f:.2f}:     Xi(v*) Xi(v*/2) S1 S2 Rv = " + " ".join(f"{v:+.4f}" for v in measure(x, w, vs)))
    for f in (0.02, 0.05, 0.10):
        x = x0.copy(); w = w0.copy()
        c = D.centre(x); r = np.linalg.norm(x - c, axis=1)
        inner = np.nonzero(r < np.median(r))[0]
        pick = rng.permutation(inner)[:int(f * len(x))]
        u = rng.normal(size=3); u /= np.linalg.norm(u)
        for i in pick:
            dirn = u + rng.normal(scale=0.1, size=3); dirn /= np.linalg.norm(dirn)
            w[i] = np.linalg.norm(w[i]) * dirn
        print(f"   stream f = {f:.2f}:     Xi(v*) Xi(v*/2) S1 S2 Rv = " + " ".join(f"{v:+.4f}" for v in measure(x, w, vs)))
