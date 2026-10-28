"""K11 under the reading-A kernel at the reading-A DESI boundary (vlya.out, columns A+AD matter/gas)."""
import numpy as np
import vhalo as V
import vgrowth as G
import vpk as P
cases = [(0.0584, 120), (0.1761, 120), (0.7810, 30), (2.5838, 30), (6.9504, 10)]
zouts = np.concatenate([np.linspace(0, 10, 101), np.linspace(10.25, 60, 200)])
PEH0 = np.interp(np.log(V.kk), np.log(P.kgrid), P.P_EH)
for (eps, vs) in cases:
    snaps = V.evolve_snap(V.kk, [0.0, eps], vs, zouts, dens="A")
    M = 1e8
    sL = []; sG = []
    for iz, zz in enumerate(zouts):
        dc, db = snaps[iz]
        dm = (G.Oc*dc+G.Ob*db)/(G.Oc+G.Ob)
        T2 = (dm[1]/dm[0])**2
        Pz = PEH0*P.Dz(zz)**2
        sL.append(V.sigma_M(M, Pz)); sG.append(V.sigma_M(M, Pz*T2))
    sL = np.array(sL); sG = np.array(sG)
    def zc(s):
        idx = np.where(s < 1.686)[0]
        if len(idx) == 0: return np.nan
        i = idx[0]
        return np.interp(1.686, [s[i], s[i-1]], [zouts[i], zouts[i-1]])
    zl, zg = zc(sL), zc(sG)
    print("reading A: eps=%.4f v*=%4d M=1e8: z_c LCDM %.2f gated %.2f | (1+z_c)^3 ratio %.3f" % (eps, vs, zl, zg, ((1+zg)/(1+zl))**3))
