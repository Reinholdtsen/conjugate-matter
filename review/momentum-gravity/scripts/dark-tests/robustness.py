"""Robustness of the DESI compressed-Lyman-alpha bound (baseline variant of lya_bounds.py):
(a) baryon (gas) growth ratio instead of total matter; (b) EH98 LCDM baseline instead of the published
Planck prediction; (c) Planck-prediction uncertainty doubled; (d) amplitude only / slope only."""
import numpy as np
import cosmo as C
import growth as G
import lya_bounds as L   # reuses its grids, data and chi2 (re-running its module-level prints is avoided below)

zp, ks, dl, eps_grid = L.zp, L.ks, L.dl, L.eps_grid


def run_ratios(vstar):
    kk = np.tile(ks, eps_grid.size); ee = np.repeat(eps_grid, 3)
    o = G.run(kk, ee, vstar, z_out=(zp,), nstep=1500)[zp]
    dm = o[2].reshape(eps_grid.size, 3); db = o[1].reshape(eps_grid.size, 3)
    return (dm / dm[0]) ** 2, (db / db[0]) ** 2


def bound_from(D2, n, base_sig_scale=1.0, which="both"):
    mu, sig, r = L.data["DESI"]
    cov = np.array([[sig[0] ** 2, r * sig[0] * sig[1]], [r * sig[0] * sig[1], sig[1] ** 2]]) + np.diag((L.base_sig * base_sig_scale) ** 2)
    if which == "amp":
        c = (D2 - mu[0]) ** 2 / cov[0, 0]
    elif which == "slope":
        c = (n - mu[1]) ** 2 / cov[1, 1]
    else:
        ic = np.linalg.inv(cov)
        d = np.stack([D2 - mu[0], n - mu[1]], axis=-1)
        c = np.einsum("...i,ij,...j->...", d, ic, d)
    i0 = np.argmin(c); target = c[i0] + 3.84
    j = np.where((np.arange(c.size) > i0) & (c > target))[0]
    if j.size == 0:
        return np.nan
    j = j[0]; e1, e2 = max(eps_grid[j - 1], 1e-6), eps_grid[j]
    return np.exp(np.log(e1) + (target - c[j - 1]) / (c[j] - c[j - 1]) * (np.log(e2) - np.log(e1)))


if __name__ == "__main__":
    print("v*  | baseline | gas(delta_b) | EH98 baseline | Planck err x2 | amplitude only | slope only | T_b^2/T_m^2 at k_p, eps=0.03")
    for v in [30, 50, 120, 300, 1000]:
        T2m, T2b = run_ratios(v)
        out = []
        for T2, base in [(T2m, L.base), (T2b, L.base), (T2m, np.array([0.3368, -2.3072]))]:
            D2 = base[0] * T2[:, 1]; n = base[1] + (np.log(T2[:, 2]) - np.log(T2[:, 0])) / (2 * dl)
            out.append(bound_from(D2, n))
        D2 = L.base[0] * T2m[:, 1]; n = L.base[1] + (np.log(T2m[:, 2]) - np.log(T2m[:, 0])) / (2 * dl)
        out.append(bound_from(D2, n, base_sig_scale=2.0))
        out.append(bound_from(D2, n, which="amp"))
        out.append(bound_from(D2, n, which="slope"))
        i = np.argmin(np.abs(eps_grid - 0.03))
        print("%5d | %.4f | %.4f | %.4f | %.4f | %.4f | %.4f | %.5f" % (v, *out, T2b[i, 1] / T2m[i, 1]))
