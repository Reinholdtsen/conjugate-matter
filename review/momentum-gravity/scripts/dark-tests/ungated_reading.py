"""If the gate used peculiar velocities only (velocity relative to the local comoving frame), linear-regime pairs
have |du| << v* and the force is ungated in linear cosmology (range > horizon, no anti-drag since W = 1 for all
linear pairs).  Compute the linear power excess and the DESI compressed bound for that ungated model."""
import numpy as np
import growth as G
import lya_bounds as L
from robustness import bound_from
import cosmo as C

zp, ks, dl, eps_grid = L.zp, L.ks, L.dl, L.eps_grid
kk = np.tile(ks, eps_grid.size); ee = np.repeat(eps_grid, 3)
o = G.run(kk, ee, 120.0, ungated=True, z_out=(zp,), nstep=1500)[zp]
for idx, lab in [(2, "matter"), (1, "gas")]:
    d = o[idx].reshape(eps_grid.size, 3); T2 = (d / d[0]) ** 2
    D2 = L.base[0] * T2[:, 1]; n = L.base[1] + (np.log(T2[:, 2]) - np.log(T2[:, 0])) / (2 * dl)
    i = np.argmin(np.abs(eps_grid - 0.01))
    print("ungated (%s): T^2(k_p, z=3) at eps=0.01: %.4f, dn = %+.5f ; DESI compressed bound eps < %.4f"
          % (lab, T2[i, 1], n[i] - L.base[1], bound_from(D2, n)))
