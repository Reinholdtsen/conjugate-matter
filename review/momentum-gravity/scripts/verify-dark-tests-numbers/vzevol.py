"""Redshift evolution of the gated enhancement at the DESI pivot (k_* = 0.009 s/km converted at each z)
over the DESI P1D redshift range z = 2.2-4.2, at the v*=120 DESI boundary (kernel B eps = 0.0285; kernel A eps = 0.0584).
The compressed parameters assume LambdaCDM growth between redshifts; this measures the departure."""
import numpy as np
import vgrowth as G
import vcosmo as C
for dens, eps in [("B", 0.0285), ("A", 0.0584)]:
    row = []
    for z in [4.2, 3.6, 3.0, 2.6, 2.2]:
        conv = float(C.H(z))/(1+z)
        kp = 0.009*conv
        ks = kp*np.exp(np.array([-0.02, 0.0, 0.02]))
        Tm2, _ = G.transfer(ks, [eps], 120.0, z_end=z, dens=dens)
        dn = (np.log(Tm2[0, 2])-np.log(Tm2[0, 0]))/0.04
        row.append("z=%.1f: T^2=%.4f dn=%+.4f" % (z, Tm2[0, 1], dn))
    print("kernel %s eps=%.4f | " % (dens, eps)+" | ".join(row))
