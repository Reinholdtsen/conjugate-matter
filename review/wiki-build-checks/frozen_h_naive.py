"""Is the naive potential lam*V_lam - mu[Tr(K Kref)]^2 bounded at frozen H = 1?
Same fields, coordinates and V_lam as verify/toy_coset.py (K = [[a, u+t],[u-t, -a]], a^2 = 1 - u^2 + t^2)."""
import sympy as sp, numpy as np
u, t, lam, mu = sp.symbols("u t lam mu", real=True)
w = sp.Matrix([[0, 1], [-1, 0]]); Kref = sp.diag(1, -1)
a = sp.sqrt(1 - u**2 + t**2)
K = sp.Matrix([[a, u + t], [u - t, -a]])
H = sp.eye(2); I = w.inv()*H; C = K*I + I*K
V_lam = sp.Rational(1, 8)*(H.inv()*C.T*H*C).trace()
V = sp.simplify(lam*V_lam - mu*((K*Kref).trace())**2)
print("V at H = 1:", sp.expand(V))
hess = sp.hessian(V, (u, t)).subs({u: 0, t: 0})
print("frozen-H Hessian in (u, t) at K_ref:", hess)
for L in (1, 10, 100):
    print(f"lam={L}, mu=1: frozen-H eigenvalues {[float(e) for e in hess.subs({lam: L, mu: 1}).eigenvals(multiple=True)]}")
f = sp.lambdify(t, V.subs({lam: 1, mu: 1, u: 0}))
print("lam = mu = 1, H = 1, u = 0: V(t) at t = 0, 10, 100:", [float(f(x)) for x in (0, 10, 100)])
# on the compatible circle (t = 0 means b = c, K symmetric): V = -4 mu (1 - u^2), bounded
print("on the circle (t = 0):", sp.simplify(V.subs(t, 0)))
