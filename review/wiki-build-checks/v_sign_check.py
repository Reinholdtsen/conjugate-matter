# Sign of tau's potential as the documents write it: V = V0[1 + cos(tau/f)] (#1 s3, #9 s8, #11 s10)
# versus #1 s7 item 3 "A cosine potential is negative over half its range".
import numpy as np, sympy as sp
x = np.linspace(0, 2*np.pi, 200001)          # x = tau/f over one period
V_doc  = 1 + np.cos(x)                        # V/V0 as written
V_bare = np.cos(x)                            # a bare cosine, V/V0
print("V0[1+cos]: min V/V0 =", V_doc.min(), "at tau/f =", x[V_doc.argmin()])
print("V0[1+cos]: fraction of period with V < 0 =", (V_doc < 0).mean())
print("V0 cos   : fraction of period with V < 0 =", (V_bare < 0).mean())
t = sp.symbols('t', real=True)
print("sympy minimum of 1+cos t over reals:", sp.minimum(1 + sp.cos(t), t, sp.Interval(0, 2*sp.pi)))
# NEC subtlety used on the pages: rho + p = taudot^2 >= 0 for any V, but w = p/rho >= -1 needs rho > 0.
td, V = sp.symbols('td V', real=True)
rho = td**2/2 + V; p = td**2/2 - V
print("rho + p =", sp.simplify(rho + p))
print("example rho<0 (td=1, V=-1): w =", (p/rho).subs({td:1, V:-1}))
