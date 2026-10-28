# Debug of n3b: list the pericentre events for fast orbits (GM/(a v*^2) = 3, 10).
import sys
from math import atan2, sqrt, pi, exp
src = open(sys.argv[1]).read().split('print("== precession')[0]
exec(src)
for x in (3.0, 10.0):
    a = 1/x; e = 0.3; beta = 0.2
    rp = a*(1-e); pp = sqrt(1.2*(1+e)/(a*(1-e)))
    s0 = (rp, 0.0, 0.0, pp)
    T = 2*pi*a**1.5/sqrt(1+beta)
    s, roots, n = integrate(s0, beta, t_end=12*T, event=radial)
    print(f"x = {x}: r_p = {rp:.4f}, p_p^2 = {pp**2:.3f}, beta e^-p^2 at pericentre = {beta*exp(-pp**2):.2e}")
    for t, y in roots[:6]:
        r = sqrt(y[0]**2 + y[1]**2)
        print(f"   t/T = {t/T:8.4f}  r = {r:.6f}  angle = {atan2(y[1], y[0]): .6f}")
    # apocentre speed and gate there
    E = H(s0, beta); L = Lz(s0)
