"""
v3_lya.py -- verifier's own re-run of the compressed DESI DR1 Lyman-alpha bound (K6)
in each reading of the gated force, Hubble-flow gate, Gaussian (and rational) W.

Data as quoted by dark-tests K6 (not yet re-checked here): Delta^2_* = 0.379 +- 0.032,
n_* = -2.309 +- 0.019, r = -0.1738 at k_* = 0.009 s/km, z = 3; LCDM baseline
(published Planck-based prediction) 0.3495, -2.3052.  Model: Delta^2 = 0.3495 T^2(k_p),
n = -2.3052 + d ln T^2/d ln k.  Criterion: Delta chi^2 = 3.84 above the minimum over
eps >= 0.  Covariance: DESI errors only (variant 'desi'); a second variant adds a
baseline-prediction uncertainty passed on the command line, if any.
Matter ratio: T_m = delta_cb(gated)/delta_cb(LCDM); gas ratio: T_b (baryons).
"""
import sys
import numpy as np
from v3_cosmo import grow, kpivot

D_OBS = np.array([0.379, -2.309]); SIG = np.array([0.032, 0.019]); RHO = -0.1738
BASE = np.array([0.3495, -2.3052])
def cov(extra=(0.0, 0.0)):
    s = np.sqrt(SIG**2 + np.array(extra)**2)
    c = np.array([[SIG[0]**2, RHO*SIG[0]*SIG[1]], [RHO*SIG[0]*SIG[1], SIG[1]**2]])
    c[0, 0] += extra[0]**2; c[1, 1] += extra[1]**2
    return c

def transfer(reading, vstar, eps, gate='gauss', z=3.0, hlog=0.05, nstep=6000):
    kp = kpivot(z=z)
    ks = kp*np.exp(np.array([-hlog, 0.0, hlog]))[:, None]
    eps = np.atleast_1d(eps)[None, :]
    dc, db, dm = grow(ks, eps, vstar, reading, gate=gate, a_end=1/(1+z), nstep=nstep)
    dc0, db0, dm0 = grow(ks[:, :1], 0.0, vstar, 'lcdm', a_end=1/(1+z), nstep=nstep)
    out = {}
    for name, d, d0 in (('m', dm, dm0), ('b', db, db0)):
        T2 = (d/d0)**2
        out[name] = (T2[1], (np.log(T2[2]) - np.log(T2[0]))/(2*hlog))
    return out

def chi2(T2, dn, C):
    Ci = np.linalg.inv(C)
    d = np.stack([BASE[0]*T2 - D_OBS[0], BASE[1] + dn - D_OBS[1]], axis=-1)
    return np.einsum('...i,ij,...j->...', d, Ci, d)

def bound(eps_grid, T2, dn, C):
    c2 = chi2(T2, dn, C)
    i0 = np.argmin(c2); dc2 = c2 - c2[i0]
    for i in range(i0, len(eps_grid)-1):
        if dc2[i] < 3.84 <= dc2[i+1]:
            f = (3.84 - dc2[i])/(dc2[i+1] - dc2[i])
            return np.exp(np.log(eps_grid[i]) + f*(np.log(eps_grid[i+1]) - np.log(eps_grid[i]))), c2[0]-c2[i0]
    return np.nan, c2[0]-c2[i0]

if __name__ == '__main__':
    extra = (float(sys.argv[1]), float(sys.argv[2])) if len(sys.argv) > 2 else (0.0, 0.0)
    C = cov(extra)
    print(f"covariance extra (baseline-prediction) errors: {extra}")
    eps_grid = np.concatenate([[0.0], np.logspace(-3.5, np.log10(12.0), 160)])
    eg = eps_grid[1:]
    readings = ('agent', 'iii', 'i', 'ii')
    for gate in ('gauss', 'rational'):
        vlist = (30, 120, 300) if gate == 'gauss' else (30, 120)
        for vs in vlist:
            row = []
            for rd in readings:
                tr = transfer(rd, vs, eps_grid, gate=gate)
                bm, pm = bound(eg, tr['m'][0][1:], tr['m'][1][1:], C)
                bb, pb = bound(eg, tr['b'][0][1:], tr['b'][1][1:], C)
                row.append((rd, bm, bb))
                if vs == 120 and gate == 'gauss':
                    for etest in (0.1, 1.0):
                        tt = transfer(rd, vs, np.array([etest]), gate=gate)
                        print(f"   [{rd:5s}] v*=120 eps={etest}: T_m^2={tt['m'][0][0]:.4f} dn_m={tt['m'][1][0]:+.4f} | "
                              f"T_b^2={tt['b'][0][0]:.4f} dn_b={tt['b'][1][0]:+.4f}")
            print(f"{gate:8s} v*={vs:4d} km/s  eps_max (matter / gas): " +
                  "  ".join(f"{rd}: {bm:.4f} / {bb:.4f}" for rd, bm, bb in row))
