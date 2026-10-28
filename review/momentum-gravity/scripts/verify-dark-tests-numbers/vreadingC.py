"""Bracket for K6: DESI compressed bound under a third reading, 'C' = -grad_x U at fixed PECULIAR
velocities (the Hubble part of v - v' = H(x - x') + u - u' is differentiated).
Derived here [D]:
  density kernel  = R_B(y) (the agent's R);
  velocity kernel = R_vC(y) = -3 y Int_0^inf t W'(t) j1(y t) dt   (self term is a surface integral -> 0;
  only neighbours' velocities contribute; R_vC -> 2 y^2 at small y, -> 0 at large y).
The velocity term enters as +(eps/2) Om_c(a) R_vC(y) delta_c' exactly where the agent's anti-drag enters.
Also prints R_vC next to the agent's R_v for comparison.
"""
import numpy as np
import vgrowth as G
import vlya as L

def j1(x):
    x = np.asarray(x, float)
    xs = np.where(x < 1e-3, 1.0, x)
    return np.where(x < 1e-3, x/3, np.sin(xs)/xs**2-np.cos(xs)/xs)

def RvC_gauss(y):
    xg, wg = np.polynomial.legendre.leggauss(40)
    edges = np.linspace(0, 12, 241)
    a = edges[:-1][:, None]; b = edges[1:][:, None]
    t = 0.5*(b-a)*xg[None, :]+0.5*(b+a); w = 0.5*(b-a)*wg[None, :]
    Wp = -t*np.exp(-t*t/2)
    return float(-3*y*np.sum(w*t*Wp*j1(y*t)))

ytab = G.ytab
RvC = np.array([RvC_gauss(y) for y in ytab])
RB, RA, RV = G.kernels("gauss")

def transfer_C(kMpc, eps, vstar, N=6000, z_end=3.0):
    # reuse vgrowth.evolve by temporarily swapping the anti-drag table
    saved = G._cache["gauss"]
    G._cache["gauss"] = (RB, RA, RvC)
    try:
        Tm2, Tb2 = G.transfer(kMpc, eps, vstar, dens="B", antidrag=True, N=N, z_end=z_end)
    finally:
        G._cache["gauss"] = saved
    return Tm2, Tb2

if __name__ == "__main__":
    print(" y      R_B      R_A      R_v(A, agent)  R_vC(reading C)")
    for y in [0.3, 0.66, 1.0, 1.08, 2.0, 5.0, 20.0]:
        i = np.argmin(abs(ytab-y))
        print(" %.2f  %.4f  %.4f   %.4f        %.4f" % (ytab[i], RB[i], RA[i], RV[i], RvC[i]))
    print("small-y check R_vC/y^2 at y=0.01: %.4f (expect 2)" % (RvC_gauss(0.01)/1e-4))
    T, Tb = transfer_C(L.ks, [0.1, 1.0], 120.0)
    for j, e in enumerate([0.1, 1.0]):
        dn = (np.log(T[j, 2])-np.log(T[j, 0]))/(2*L.dl)
        print("reading C, eps=%.1f, v*=120: T_m^2(kp) = %.4f dn = %+.4f" % (e, T[j, 1], dn))
    print("DESI bound under reading C (Gaussian, Planck-prediction errors in quadrature):")
    print(" v*  | matter  gas")
    for vs in [10, 30, 50, 120, 300, 1000, 3000]:
        Tm2, Tb2 = transfer_C(L.ks, L.eps_grid, vs)
        one = np.ones((1, 3))
        Tm2 = np.vstack([one, Tm2]); Tb2 = np.vstack([one, Tb2])
        print("%5d | %.4f  %.4f" % (vs, L.bound(L.chi2_curve(Tm2, L.DESI), L.eps_grid), L.bound(L.chi2_curve(Tb2, L.DESI), L.eps_grid)))
