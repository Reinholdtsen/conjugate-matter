#!/usr/bin/env python3
"""Side check for flag 40: the v2 repair V_b = -mu [Tr(K K_ref)]^2 / (2 Tr K^T K) at frozen H = 1,
K free on its hyperboloid, same definitions as flag40_recompute.py (global chart s, f)."""
import sympy as sp, numpy as np
w = sp.Matrix([[0, 1], [-1, 0]])
lam, mu = sp.symbols("lambda mu", positive=True)
s, f = sp.symbols("s f", real=True)
Kc = sp.Matrix([[sp.cosh(s)*sp.cos(f), sp.cosh(s)*sp.sin(f) + sp.sinh(s)],
                [sp.cosh(s)*sp.sin(f) - sp.sinh(s), -sp.cosh(s)*sp.cos(f)]])
Kref = sp.diag(1, -1)
I = w.inv()  # H = 1
C = Kc*I + I*Kc
V = lam/8*(C.T*C).trace() - mu*((Kc*Kref).trace())**2/(2*(Kc.T*Kc).trace())
Hs = sp.simplify(sp.hessian(V, (s, f)).subs({s: 0, f: 0}))
print("V_lam + V_b, frozen H = 1: Hessian at K_ref in (s, f):", Hs.tolist())
print("  at lam = mu = 1:", Hs.subs({lam: 1, mu: 1}).tolist())
Vn = sp.lambdify((s, f), V.subs({lam: 1, mu: 1}), "numpy")
S, F = np.meshgrid(np.linspace(-12, 12, 2401), np.linspace(-np.pi, np.pi, 721))
Vg = Vn(S, F)
print(f"  lam = mu = 1: min over |s| <= 12 grid = {Vg.min():.6f}; V(s=12, f=0) = {Vn(12.0, 0.0):.4e}")
