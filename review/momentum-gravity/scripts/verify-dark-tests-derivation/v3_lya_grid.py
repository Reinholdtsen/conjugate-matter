"""
v3_lya_grid.py -- DESI compressed bound over the full v* grid of K6/K17 in readings
i (Hamiltonian, record's), ii (Lagrangian), iii (force law, correct kernel) and agent
(as implemented), Gaussian gate, covariance with the baseline-prediction errors
(0.0083, 0.0032) as in dark-tests.  Also: (T^2, dn) at each boundary, amplitude-only
and slope-only bounds, and the best-fit eps with chi2(0) - chi2_min.
"""
import numpy as np
from v3_lya import transfer, cov, chi2, BASE, D_OBS

C = cov((0.0083, 0.0032))
eps_grid = np.concatenate([[0.0], np.logspace(-3.5, np.log10(12.0), 200)])
eg = eps_grid[1:]

def bound_generic(c2):
    i0 = np.argmin(c2); d = c2 - c2[i0]
    for i in range(i0, len(c2)-1):
        if d[i] < 3.84 <= d[i+1]:
            f = (3.84 - d[i])/(d[i+1] - d[i])
            lo = max(eps_grid[i], 1e-5)
            return np.exp(np.log(lo) + f*(np.log(eps_grid[i+1]) - np.log(lo))), eps_grid[i0], c2[0]-c2[i0]
    return np.nan, eps_grid[i0], c2[0]-c2[i0]

def one(rd, vs, which='m'):
    tr = transfer(rd, vs, eps_grid)
    T2, dn = tr[which]
    c_both = chi2(T2, dn, C)
    D2 = BASE[0]*T2; n = BASE[1] + dn
    c_amp = (D2 - D_OBS[0])**2/C[0, 0]
    c_slope = (n - D_OBS[1])**2/C[1, 1]
    b, ebest, dchi0 = bound_generic(c_both)
    ba = bound_generic(c_amp)[0]; bs = bound_generic(c_slope)[0]
    if np.isfinite(b):
        T2b = np.interp(np.log(b), np.log(eg), T2[1:]); dnb = np.interp(np.log(b), np.log(eg), dn[1:])
    else:
        T2b = dnb = np.nan
    return b, ebest, dchi0, ba, bs, T2b, dnb

print("reading | v* | eps_max(matter) [best eps, chi2(0)-min] amp-only slope-only | T^2, dn at bound || eps_max(gas)")
for rd in ('i', 'ii', 'iii', 'agent'):
    for vs in (10, 20, 30, 50, 80, 120, 200, 300, 500, 1000, 2000, 3000):
        bm, eb, d0, ba, bs, T2b, dnb = one(rd, vs, 'm')
        bg = one(rd, vs, 'b')[0]
        print(f"{rd:5s} | {vs:5d} | {bm:8.4f} [{eb:.4f}, {d0:.2f}] {ba:8.4f} {bs:8.4f} | {T2b:.4f} {dnb:+.4f} || {bg:8.4f}")
