"""
v3_k10_ungated.py -- K10: DESI compressed bound for the ungated force (W = 1: extra
chi-only gravity eps*G, no velocity terms), matter and gas ratios, with the
baseline-prediction errors of dark-tests.  (Peculiar-gate limit in the force-law reading.)
"""
import numpy as np
from v3_lya import transfer, cov, bound
C = cov((0.0083, 0.0032))
eps_grid = np.concatenate([[0.0], np.logspace(-3.5, np.log10(12.0), 200)])
tr = transfer('ungated', 120, eps_grid)
bm = bound(eps_grid[1:], tr['m'][0][1:], tr['m'][1][1:], C)[0]
bb = bound(eps_grid[1:], tr['b'][0][1:], tr['b'][1][1:], C)[0]
i = np.argmin(abs(eps_grid - 0.01))
print(f"ungated: T_m^2(k_p) at eps={eps_grid[i]:.4f}: {tr['m'][0][i]:.4f}, dn = {tr['m'][1][i]:+.5f}; DESI bound matter {bm:.4f}, gas {bb:.4f}")
