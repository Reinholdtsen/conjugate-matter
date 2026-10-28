"""Compressed Lyman-alpha bounds on eps (K6-K8, K10), recomputed with vgrowth.py.

Data [S]: DESI DR1 P1D (Chaves-Montero et al., arXiv:2601.21432): Delta^2_* = 0.379 +- 0.032,
  n_* = -2.309 +- 0.019, Pearson r = -0.1738, k_* = 0.009 s/km, z = 3.
  eBOSS (Chabanier+19 as tabulated by Rogers & Poulin, arXiv:2311.16377): 0.310 +- 0.020, -2.340 +- 0.006, r = 0.512.
Baseline [S]: Rogers & Poulin Table 2, Planck+BAO+SNe, Sum m_nu model: 0.3495 (+0.0095/-0.0071), -2.3052 +- 0.0032.
Model: Delta^2 = base * T^2(k_*), n = base_n + dlnT^2/dlnk at k_*.
Criterion: Delta chi^2 = 3.84 above the minimum over eps >= 0.
Variants: kernel B (agent's) or A (reading-A consistent), anti-drag on/off, matter or baryon ratio,
  Planck-prediction errors added in quadrature or not.
"""
import sys
import numpy as np
import vgrowth as G
import vcosmo as C

z = 3
conv = float(C.H(z))/(1+z)
kp = 0.009*conv
dl = 0.02
ks = kp*np.exp(np.array([-dl, 0.0, dl]))
eps_grid = np.concatenate([np.logspace(-3.5, np.log10(30), 90)])

DESI = dict(d=np.array([0.379, -2.309]), s=np.array([0.032, 0.019]), r=-0.1738)
EBOSS = dict(d=np.array([0.310, -2.340]), s=np.array([0.020, 0.006]), r=0.512)
BASE = np.array([0.3495, -2.3052]); BASE_S = np.array([0.5*(0.0095+0.0071), 0.0032])

def cov(dat, add_base=True, base_scale=1.0):
    s = dat["s"]; r = dat["r"]
    Cm = np.array([[s[0]**2, r*s[0]*s[1]], [r*s[0]*s[1], s[1]**2]])
    if add_base:
        Cm = Cm+np.diag((base_scale*BASE_S)**2)
    return Cm

def chi2_curve(T2, dat, add_base=True, base_scale=1.0, which="both"):
    """T2: (ne, 3) power ratio at ks. Returns chi2 for eps_grid with eps=0 prepended."""
    amp = T2[:, 1]
    dn = (np.log(T2[:, 2])-np.log(T2[:, 0]))/(2*dl)
    m = np.stack([BASE[0]*amp, BASE[1]+dn], axis=1)
    Ci = np.linalg.inv(cov(dat, add_base, base_scale))
    res = dat["d"][None, :]-m
    if which == "amp":
        var = cov(dat, add_base, base_scale)[0, 0]
        return res[:, 0]**2/var
    if which == "slope":
        var = cov(dat, add_base, base_scale)[1, 1]
        return res[:, 1]**2/var
    return np.einsum("ij,jk,ik->i", res, Ci, res)

def bound(ch, eps):
    """ch over [0]+eps; returns eps where chi2 - min = 3.84 (log-interp), nan if not reached."""
    e = np.concatenate([[0.0], eps])
    cmin = ch.min()
    target = cmin+3.84
    imin = int(np.argmin(ch))
    for i in range(max(imin, 0), len(e)-1):
        if ch[i] <= target < ch[i+1]:
            if e[i] == 0.0:
                lo, hi = 1e-6, e[i+1]
                # linear in eps from 0
                return e[i]+(target-ch[i])/(ch[i+1]-ch[i])*(e[i+1]-e[i])
            t = (target-ch[i])/(ch[i+1]-ch[i])
            return np.exp(np.log(e[i])+t*(np.log(e[i+1])-np.log(e[i])))
    return np.nan

def run(vstar, gate="gauss", dens="B", antidrag=True, ungated=False):
    Tm2, Tb2 = G.transfer(ks, eps_grid, vstar, gate=gate, dens=dens, antidrag=antidrag, ungated=ungated)
    one = np.ones((1, 3))
    return np.vstack([one, Tm2]), np.vstack([one, Tb2])

if __name__ == "__main__":
    vlist = [float(a) for a in sys.argv[1:]] or [10, 20, 30, 50, 80, 120, 200, 300, 500, 1000, 2000, 3000]
    print("DESI compressed bound on eps (Delta chi2 = 3.84 above min over eps>=0); Planck-prediction errors in quadrature")
    print(" v*   | B+AD matter  gas | B+AD noPlErr | B noAD matter | A+AD matter  gas | A noAD matter | rational B+AD m/g | rational A+AD m | eBOSS B+AD m")
    for vs in vlist:
        out = []
        TmB, TbB = run(vs, dens="B", antidrag=True)
        out += [bound(chi2_curve(TmB, DESI), eps_grid), bound(chi2_curve(TbB, DESI), eps_grid),
                bound(chi2_curve(TmB, DESI, add_base=False), eps_grid)]
        TmBn, _ = run(vs, dens="B", antidrag=False)
        out += [bound(chi2_curve(TmBn, DESI), eps_grid)]
        TmA, TbA = run(vs, dens="A", antidrag=True)
        out += [bound(chi2_curve(TmA, DESI), eps_grid), bound(chi2_curve(TbA, DESI), eps_grid)]
        TmAn, _ = run(vs, dens="A", antidrag=False)
        out += [bound(chi2_curve(TmAn, DESI), eps_grid)]
        TmR, TbR = run(vs, gate="rational", dens="B", antidrag=True)
        out += [bound(chi2_curve(TmR, DESI), eps_grid), bound(chi2_curve(TbR, DESI), eps_grid)]
        TmRA, _ = run(vs, gate="rational", dens="A", antidrag=True)
        out += [bound(chi2_curve(TmRA, DESI), eps_grid)]
        out += [bound(chi2_curve(TmB, EBOSS), eps_grid)]
        print("%5d | %.4f  %.4f | %.4f      | %.4f        | %.4f  %.4f | %.4f        | %.4f  %.4f     | %.4f          | %.5f" % ((vs,)+tuple(out)))
        if vs == 120:
            ch = chi2_curve(TmB, DESI)
            print("   v*=120 B+AD matter: chi2(eps=0) - min = %.3f ; slope-only bound %.4f ; amplitude-only bound %.4f ; base errors x2: %.4f"
                  % (ch[0]-ch.min(), bound(chi2_curve(TmB, DESI, which="slope"), eps_grid),
                     bound(chi2_curve(TmB, DESI, which="amp"), eps_grid),
                     bound(chi2_curve(TmB, DESI, base_scale=2.0), eps_grid)))
            chA = chi2_curve(TmA, DESI)
            print("   v*=120 A+AD matter: slope-only %.4f amplitude-only %.4f" %
                  (bound(chi2_curve(TmA, DESI, which="slope"), eps_grid), bound(chi2_curve(TmA, DESI, which="amp"), eps_grid)))
    # ungated reading (K10)
    TmU, TbU = run(120.0, ungated=True)
    print("ungated reading: DESI bound matter %.4f gas %.4f" % (bound(chi2_curve(TmU, DESI), eps_grid), bound(chi2_curve(TbU, DESI), eps_grid)))
