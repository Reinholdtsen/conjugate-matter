"""Lyman-alpha and BOSS-scale bounds on a velocity-gated chi-only attraction (linear theory).

Compressed Lyman-alpha parameters at z_p = 3, k_p = 0.009 s/km:
  Delta^2 = k^3 P_lin(k_p)/(2 pi^2), n = dlnP_lin/dlnk at k_p.
Data [S]:
  DESI DR1 P1D (Chaves-Montero et al., arXiv:2601.21432): Delta^2 = 0.379 +- 0.032,
      n = -2.309 +- 0.019, Pearson r = -0.1738; 'fully consistent with ... Planck 2018'.
  eBOSS (Rogers & Poulin, arXiv:2311.16377): 0.310 +- 0.020, -2.340 +- 0.006, r = 0.512;
      4.9 sigma tension with Planck under LCDM.
  Planck (CMB+BAO+SNe, sum m_nu extension; Rogers & Poulin): Delta^2 = 0.3495 (+0.0095/-0.0071),
      n = -2.3052 +- 0.0032  -> used as the eps = 0 baseline (symmetrized 0.0083).
Model: growth.py (Hubble-flow gate; see its docstring for reductions).
Bound: Delta chi^2 = chi^2(eps) - min_{eps>=0} chi^2 = 3.84 (one parameter, eps >= 0).
The compression assumes a LCDM-like shape around k_p; the gated force adds a scale-dependent
feature, so the compressed bound is an estimate, not a likelihood analysis.
"""
import numpy as np
import cosmo as C
import growth as G

zp = 3.0
kp = 0.009 * C.Hz(zp) / (1 + zp)   # 1/Mpc
dl = 0.05
ks = kp * np.exp(np.array([-dl, 0.0, dl]))

# ---- anchor: LCDM prediction from EH98 vs the published Planck prediction
P = C.P_lin(ks, zp)
D2_EH = ks[1] ** 3 * P[1] / (2 * np.pi**2)
n_EH = (np.log(P[2]) - np.log(P[0])) / (2 * dl)
print("k_p = 0.009 s/km at z=3 -> %.4f 1/Mpc (%.4f h/Mpc)" % (kp, kp / C.h))
print("Anchor: EH98 no-wiggle LCDM (Planck 2018 params): Delta^2 = %.4f, n = %.4f" % (D2_EH, n_EH))
print("        published Planck-based prediction (Rogers & Poulin): Delta^2 = 0.3495, n = -2.3052")

base = np.array([0.3495, -2.3052]); base_sig = np.array([0.0083, 0.0032])
data = {
    "DESI": (np.array([0.379, -2.309]), np.array([0.032, 0.019]), -0.1738),
    "eBOSS": (np.array([0.310, -2.340]), np.array([0.020, 0.006]), 0.512),
}


def chi2(D2, n, name):
    mu, sig, r = data[name]
    cov = np.array([[sig[0] ** 2, r * sig[0] * sig[1]], [r * sig[0] * sig[1], sig[1] ** 2]])
    cov = cov + np.diag(base_sig**2)
    ic = np.linalg.inv(cov)
    d = np.stack([D2 - mu[0], n - mu[1]], axis=-1)
    return np.einsum("...i,ij,...j->...", d, ic, d)


eps_grid = np.concatenate([[0.0], np.logspace(-3.5, 1.0, 91)])
vgrid = [10, 20, 30, 50, 80, 120, 200, 300, 500, 1000, 2000, 3000]


def compressed(vstar, gate="gauss", antidrag=True, pec=False):
    kk = np.tile(ks, eps_grid.size)
    ee = np.repeat(eps_grid, 3)
    pt = G.make_s1_table(vstar) if pec else None
    o = G.run(kk, ee, vstar, gate=gate, antidrag=antidrag, pec=pt, z_out=(zp,), nstep=1500)[zp]
    dm = o[2].reshape(eps_grid.size, 3)
    T2 = (dm / dm[0]) ** 2
    D2 = base[0] * T2[:, 1]
    n = base[1] + (np.log(T2[:, 2]) - np.log(T2[:, 0])) / (2 * dl)
    return T2[:, 1], n - base[1], D2, n


def bound(D2, n, name):
    c = chi2(D2, n, name)
    i0 = np.argmin(c)
    target = c[i0] + 3.84
    j = np.where((np.arange(c.size) > i0) & (c > target))[0]
    if j.size == 0:
        return np.nan, eps_grid[i0], c[0] - c[i0]
    j = j[0]
    # log-interpolate between j-1 and j
    e1, e2 = max(eps_grid[j - 1], 1e-6), eps_grid[j]
    c1, c2 = c[j - 1], c[j]
    lb = np.log(e1) + (target - c1) / (c2 - c1) * (np.log(e2) - np.log(e1))
    return np.exp(lb), eps_grid[i0], c[0] - c[i0]


variants = [
    ("gauss, anti-drag, Hubble-only gate (baseline)", dict(gate="gauss", antidrag=True, pec=False)),
    ("gauss, anti-drag, linear pair-velocity smoothing", dict(gate="gauss", antidrag=True, pec=True)),
    ("gauss, NO anti-drag term, Hubble-only", dict(gate="gauss", antidrag=False, pec=False)),
    ("rational gate, anti-drag, Hubble-only", dict(gate="rat", antidrag=True, pec=False)),
]

if __name__ == "__main__":
    results = {}
    for lab, kw in variants:
        print()
        print("Variant:", lab)
        print("  v*[km/s]  eps_max(DESI)  [best eps, chi2(0)-chi2min]   eps_max(eBOSS)   T^2(k_p) and dn at eps=0.1   at eps=1")
        res = []
        for v in vgrid:
            T2p, dn, D2, n = compressed(v, **kw)
            bD, eD, cD = bound(D2, n, "DESI")
            bE, eE, cE = bound(D2, n, "eBOSS")
            i01 = np.argmin(np.abs(eps_grid - 0.1)); i1 = np.argmin(np.abs(eps_grid - 1.0))
            print("  %6d     %9.4f      [%.4f, %.2f]          %9.5f        %.4f %+.4f        %.4f %+.4f"
                  % (v, bD, eD, cD, bE, T2p[i01], dn[i01], T2p[i1], dn[i1]))
            res.append((v, bD, bE))
        results[lab] = res

    # ---- small-scale enhancement at the DESI bound (baseline variant), z = 3
    print()
    print("Linear matter power ratio T_m^2 at z=3 for eps at the DESI compressed bound (baseline variant)")
    kv_list = np.array([0.0045, 0.009, 0.018, 0.03, 0.05])
    kc_list = kv_list * C.Hz(zp) / (1 + zp)
    print("  k_v [s/km]:", "  ".join("%.4f" % x for x in kv_list), "  | k=10/Mpc")
    for v, bD, bE in results[variants[0][0]]:
        if not np.isfinite(bD):
            continue
        o = G.run(np.append(kc_list, 10.0), bD, v, z_out=(zp,), nstep=1500)[zp]
        s = G.run(np.append(kc_list, 10.0), 0.0, v, z_out=(zp,), nstep=1500)[zp]
        T2 = (o[2] / s[2]) ** 2
        print("  v*=%5d eps=%.3f:" % (v, bD), "  ".join("%.3f" % x for x in T2[:-1]), "  | %.3f" % T2[-1])

    # ---- BOSS-scale mapping: gated eps giving the same linear power excess at k = 0.2 h/Mpc, z = 0.57
    # as the ungated (range > horizon) bound beta < 0.0048 (Bottaro et al. 2023, Planck + BOSS FS + BAO, 95%) [S]
    print()
    kB = np.array([0.1, 0.2]) * C.h
    for zB in [0.57, 0.32]:
        o = G.run(kB, 0.0048, 120.0, ungated=True, z_out=(zB,), nstep=1500)[zB]
        s = G.run(kB, 0.0, 120.0, z_out=(zB,), nstep=1500)[zB]
        ex_u = (o[2] / s[2]) ** 2 - 1
        print("Ungated beta=0.0048: linear power excess at z=%.2f, k=0.1,0.2 h/Mpc: %.4f %.4f" % (zB, ex_u[0], ex_u[1]))
        print("  BOSS-equivalent gated bound (same excess at k=0.2 h/Mpc, z=%.2f):" % zB)
        for v in vgrid:
            kk = np.tile(kB, eps_grid.size); ee = np.repeat(eps_grid, 2)
            og = G.run(kk, ee, v, z_out=(zB,), nstep=1500)[zB]
            dm = og[2].reshape(eps_grid.size, 2)
            ex = (dm / dm[0]) ** 2 - 1
            j = np.argmax(ex[:, 1] > ex_u[1])
            eq = np.interp(ex_u[1], ex[:, 1][: j + 1], eps_grid[: j + 1]) if ex[j, 1] > ex_u[1] else np.nan
            print("    v*=%5d km/s: eps_equiv = %.4f" % (v, eq))
