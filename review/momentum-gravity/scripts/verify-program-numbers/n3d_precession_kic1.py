# Precession of fast gated orbits with initial conditions from the ungated Kepler problem (k_ic = 1),
# appropriate when the gate is mostly closed; complements n3b (k_ic = 1 + beta).
import sys
from math import atan2, sqrt, pi, exp
src = open(sys.argv[1]).read().split('print("== precession')[0]
exec(src)
def prec_long(beta, a, e, k_ic, n_orb=6):
    rp = a*(1-e); pp = sqrt(k_ic*(1+e)/(a*(1-e)))
    s0 = (rp, 0.0, 0.0, pp)
    T = 2*pi*a**1.5/sqrt(k_ic)
    s, roots, n = integrate(s0, beta, t_end=(n_orb+0.5)*T*1.6, event=radial)
    angs = [atan2(y[1], y[0]) for t, y in roots[:n_orb]]
    prev = 0.0; adv = []
    for g in angs:
        d = (g - prev) % (2*pi)
        if d > pi: d -= 2*pi
        adv.append(d); prev = g
    return sum(adv)/len(adv), len(adv)
print("GM/(a v*^2)  k_ic  precession/orbit (beta = 0.2, e = 0.3)   orbits used")
for x in (0.3, 1.0, 3.0, 10.0, 30.0):
    m, k = prec_long(0.2, 1/x, 0.3, 1.0)
    print(f"{x:8.2f}     1.0   {m: .4e}    {k}")
