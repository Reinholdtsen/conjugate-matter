"""Small-scale consequence: earlier collapse of small halos under the gated force (linear theory proxy).

sigma(M, z) from P_lin(k, z) * T_m(k, z)^2 (growth.py ratio applied to the EH98 LCDM spectrum);
collapse redshift z_c(M): sigma(M, z_c) = 1.686 (spherical-collapse threshold [T]); a 1-sigma
peak, used only as a formation-epoch proxy. Characteristic density proxy: (1+z_c)^3 [T, scaling].
Points examined: the DESI compressed-Lyman-alpha boundary of lya_bounds.out (baseline variant),
plus eps = 1 at v* = 120 km/s for illustration.
"""
import numpy as np
import cosmo as C
import growth as G

k = np.logspace(-2, 3, 160)
zlist = [0.0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80]
rho_m0 = C.Om * 2.775e11 * C.h**2   # Msun / Mpc^3  [T]
masses = [1e7, 1e8, 1e9, 1e10, 1e11]
Rs = [(M / (4 * np.pi / 3 * rho_m0)) ** (1 / 3) for M in masses]
print("M[Msun] -> top-hat R[Mpc comoving]:", ", ".join("%.0e:%.4f" % (M, R) for M, R in zip(masses, Rs)))

Pk0 = {z: C.P_lin(k, z) for z in zlist}


def sigmaR(Pk, R):
    x = k * R
    W = np.where(x < 1e-3, 1 - x**2 / 10, 3 * (np.sin(x) - x * np.cos(x)) / np.maximum(x, 1e-300) ** 3)
    return np.sqrt(np.trapezoid(k**3 * Pk * W**2 / (2 * np.pi**2), np.log(k)))


std = G.run(k, 0.0, 120.0, z_out=tuple(zlist), nstep=1500)


def zc_table(eps, vstar, gate="gauss"):
    g = G.run(k, eps, vstar, gate=gate, z_out=tuple(zlist), nstep=1500)
    rows = []
    for M, R in zip(masses, Rs):
        s_g, s_s = [], []
        for z in zlist:
            T2 = (g[z][2] / std[z][2]) ** 2
            s_g.append(sigmaR(Pk0[z] * T2, R)); s_s.append(sigmaR(Pk0[z], R))
        s_g = np.array(s_g); s_s = np.array(s_s)
        lz = np.log(1 + np.array(zlist))

        def zc(s):
            # sigma decreasing with z; find crossing of 1.686
            if s[0] < 1.686:
                return np.nan
            if s[-1] > 1.686:
                return np.inf
            j = np.argmax(s < 1.686)
            l = lz[j - 1] + (np.log(1.686) - np.log(s[j - 1])) / (np.log(s[j]) - np.log(s[j - 1])) * (lz[j] - lz[j - 1])
            return np.exp(l) - 1
        zg, zs = zc(s_g), zc(s_s)
        rows.append((M, s_s[0], s_g[0], zs, zg, ((1 + zg) / (1 + zs)) ** 3))
    return rows


points = [(3.08, 10), (0.775, 20), (0.348, 30), (0.129, 50), (0.055, 80), (0.0285, 120), (0.016, 200),
          (0.014, 300), (0.017, 1000), (1.0, 120), (0.3, 120)]
import sys
if len(sys.argv) > 1:   # optional: pairs eps v on the command line
    a = [float(x) for x in sys.argv[1:]]
    points = list(zip(a[0::2], [int(x) for x in a[1::2]]))
for eps, v in points:
    print("eps=%.4f v*=%d km/s:" % (eps, v))
    for M, ss, sg, zs, zg, dens in zc_table(eps, v):
        print("   M=%.0e  sigma(z=0): LCDM %.3f gated %.3f | z_c(1-sigma): LCDM %.2f gated %.2f | (1+z_c)^3 ratio %.3f"
              % (M, ss, sg, zs, zg, dens))
