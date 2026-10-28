"""Context for the compression check: LambdaCDM curvature d^2 lnP/dlnk^2 of the EH98 no-wiggle linear power
at the DESI pivot (z = 3, k_* = 0.009 s/km), to compare with the gated model's added running (vextra.out)."""
import numpy as np
import vpk as P
import vcosmo as C
z = 3
kp = 0.009*float(C.H(z))/(1+z)
lk = np.log(P.kgrid); lP = np.log(P.P_EH)
d = 0.2
v = np.interp(np.log(kp)+np.array([-d, 0, d]), lk, lP)
print("EH98 LCDM at pivot: slope %.4f, curvature d2lnP/dlnk2 = %.4f" % ((v[2]-v[0])/(2*d), (v[2]-2*v[1]+v[0])/d**2))
