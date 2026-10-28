"""K9 number check: linear power excess of an ungated chi-only force at beta = 0.0048 at z = 0.57,
k = 0.1, 0.2 h/Mpc (sub-horizon two-fluid model of vgrowth.py, no background modification), and the
gated eps giving the same excess at k = 0.2 h/Mpc for several v* (agent's kernel 'B' + anti-drag, and
the reading-A kernel). This reproduces the agent's mapping arithmetic only; whether the mapping is a
bound is a separate question (Bottaro et al. 2024 [S]: the bound is driven by the background modification,
and BOSS full shape adds little beyond Planck+BAO because of the linear-bias degeneracy).
"""
import numpy as np
import vgrowth as G

h = G.h
kk = np.array([0.1, 0.2])*h
Tm2, Tb2 = G.transfer(kk, [0.0048], 120.0, z_end=0.57, ungated=True)
print("ungated beta=0.0048: power excess at z=0.57, k=0.1,0.2 h/Mpc: %.4f %.4f" % tuple(Tm2[0]-1))
Tm2b, _ = G.transfer(kk, [0.0048], 120.0, z_end=0.32, ungated=True)
print("ungated beta=0.0048: power excess at z=0.32: %.4f %.4f" % tuple(Tm2b[0]-1))
target = Tm2[0, 1]-1
eps = np.logspace(-3, 1, 81)
for dens in ["B", "A"]:
    for vs in [120, 300, 1000, 3000]:
        T, _ = G.transfer(kk[1:], eps, float(vs), z_end=0.57, dens=dens)
        ex = T[:, 0]-1
        if ex.max() < target:
            print("dens=%s v*=%5d: no solution for eps<=10" % (dens, vs)); continue
        i = np.where(ex >= target)[0][0]
        e = np.exp(np.interp(np.log(target), np.log(ex[i-1:i+1]), np.log(eps[i-1:i+1])))
        # excess at k = 0.1 h/Mpc for that eps
        T1, _ = G.transfer(kk[:1], [e], float(vs), z_end=0.57, dens=dens)
        print("dens=%s v*=%5d: eps_equiv(k=0.2 h/Mpc) = %.4f ; its excess at k=0.1 h/Mpc = %.4f (ungated %.4f)"
              % (dens, vs, e, T1[0, 0]-1, Tm2[0, 0]-1))
