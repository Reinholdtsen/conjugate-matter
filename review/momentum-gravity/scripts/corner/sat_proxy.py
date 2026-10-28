"""Milky Way satellite-count proxy for the corner (round 3, label "corner").

Tolerance proxy: linear-power suppression of thermal-relic WDM at the DES + Pan-STARRS1 satellite
bound m_WDM > 6.5 keV (95%) [S: Nadler et al. 2021, PRL 126, 091101, arXiv:2008.00022, via search
summary], Viel et al. 2005 fit (see obs_corner.py, [S] via search summaries).  Compared with the gated
linear T2 = P_gated/P_LCDM at k = 10, 20, 40 /Mpc (halo masses ~1e8-1e10 Msun) at z = 3 and 6, both
readings.  A suppression larger than the WDM one at the same k is marked 'S' (fewer satellite hosts than
the bound allows); an enhancement is marked 'E' (more early, dense hosts; the satellite count alone does
not bound an enhancement, so 'E' is not an exclusion).  One-number comparison, not a likelihood.
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import linear_corner as L   # noqa: E402
from obs_corner_wdm import T2_wdm   # noqa: E402

kk = np.array([10.0, 20.0, 40.0])
t_w = T2_wdm(kk, 6.5)
print(f"WDM 6.5 keV: T2 at k = {kk} /Mpc: {np.round(t_w, 4)}")
for reading in ("H", "K4"):
    print(f"reading {reading}:")
    for vs in (3, 5, 10, 20, 30):
        row = []
        for e in (1, 3, 10):
            T = L.T2(kk, e, vs, reading, [6.0, 3.0])
            t6, t3 = T[6.0], T[3.0]
            fl = "".join("S" if t < tw else ("E" if t > 1 / tw else "-") for t, tw in zip(t3, t_w))
            row.append(f"e{e}: z6 {'/'.join(f'{x:.3g}' for x in t6)} z3 {'/'.join(f'{x:.3g}' for x in t3)} [{fl}]")
        print(f"  v*={vs:2d}: " + " | ".join(row))
