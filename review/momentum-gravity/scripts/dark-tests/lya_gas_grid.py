"""DESI compressed-Lyman-alpha bound on eps(v*) using the total-matter ratio and the baryon (gas) ratio,
for the Gaussian and rational gates (Hubble-only gate, anti-drag on). Uses lya_bounds/robustness helpers."""
import numpy as np
import growth as G
import lya_bounds as L
from robustness import bound_from

zp, ks, dl, eps_grid = L.zp, L.ks, L.dl, L.eps_grid
print(" v*   | gauss: matter  gas | rational: matter  gas")
for v in [10, 20, 30, 50, 80, 120, 200, 300, 500, 1000, 2000, 3000]:
    row = []
    for gate in ["gauss", "rat"]:
        kk = np.tile(ks, eps_grid.size); ee = np.repeat(eps_grid, 3)
        o = G.run(kk, ee, v, gate=gate, z_out=(zp,), nstep=1500)[zp]
        for idx in (2, 1):
            d = o[idx].reshape(eps_grid.size, 3); T2 = (d / d[0]) ** 2
            D2 = L.base[0] * T2[:, 1]; n = L.base[1] + (np.log(T2[:, 2]) - np.log(T2[:, 0])) / (2 * dl)
            row.append(bound_from(D2, n))
    print("%5d | %8.4f %8.4f | %8.4f %8.4f" % (v, *row))
