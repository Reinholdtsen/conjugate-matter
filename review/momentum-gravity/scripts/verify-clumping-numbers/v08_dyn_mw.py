"""Verifier v08: MW (r = sigma/v* = 155/120) dynamic checks of C2, C11, C12 with the generator
eigenvalue method (v07), azimuthal sectors m = 0, 1, 2 about k. Two z-panel resolutions."""
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from v07_dynamic_basis import DynB, MW_PANELS

FINE = [(0, 1.2, 170), (1.2, 2.5, 50), (2.5, 4.5, 26), (4.5, 8.0, 12)]
r = 155 / 120

def show(g, k=3):
    return "[" + ", ".join(f"{c.real:+.5f}{c.imag:+.5f}i" for c in g[:k]) + "]" if len(g) else "[]"

cache = {}
def get(m, fine):
    key = (m, fine)
    if key not in cache:
        cache[key] = DynB(r, m=m, panels=FINE if fine else MW_PANELS, Nperp=10)
    return cache[key]

cases = [
    ("C2  gt=10 kap2=0.999*L0", 0.999 * 2.30503422, 10.0),
    ("C2  gt=10 kap2=1.001*L0", 1.001 * 2.30503422, 10.0),
    ("C2  gt=10 kap2=2.2", 2.2, 10.0),
    ("C2  gt=10 kap2=2.4", 2.4, 10.0),
    ("C11 gt=56.14 kap2=pi^2/2", np.pi**2 / 2, 56.14),
    ("C11 gt=280.7 kap2=pi^2/2", np.pi**2 / 2, 280.7),
    ("C11 gt=280.7 kap2=30", 30.0, 280.7),
    ("C11 gt=255 kap2=2pi^2", 2 * np.pi**2, 255.0),
    ("C12 gt=240 kap2=2pi^2", 2 * np.pi**2, 240.0),
    ("C12 gt=272", 2 * np.pi**2, 272.0),
    ("C12 gt=277", 2 * np.pi**2, 277.0),
    ("C12 gt=280.7", 2 * np.pi**2, 280.7),
    ("C12 gt=283", 2 * np.pi**2, 283.0),
    ("C12 gt=290", 2 * np.pi**2, 290.0),
    ("C12 gt=320", 2 * np.pi**2, 320.0),
    ("C12 gt=100 kap2=2", 2.0, 100.0),
    ("C12 gt=56.14 kap2=3", 3.0, 56.14),
]
t0 = time.time()
for fine in [False, True]:
    print(f"==== z panels: {'FINE' if fine else 'MW_PANELS'} ====")
    for name, kap2, gt in cases:
        out = []
        for m in [0, 1, 2]:
            D = get(m, fine)
            g = D.growing(kap2, gt)
            pg = [c for c in g if abs(c.real) < 1e-6]
            tr = [c for c in g if c.real > 1e-6]
            out.append(f"m={m}: n_grow={len(g)} pure={show(pg,2)} trav={show(tr,2)}")
        print(f"{name:28s} | " + " | ".join(out), flush=True)
    print(f"time {time.time()-t0:.0f}s")
