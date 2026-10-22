"""Lead check (pred-b verifier): how rho: Z -> -Z^{-1} acts on linear fluctuations
of the modular field Z = X + iY at the self-dual vacuum Z = i (#11 section 6),
compared with the frame-exchange parity of #8 section 3 / #11 section 7.5.

1. For symmetric d x d fluctuations x (of X) and h (of Y), linearize -Z^{-1} at
   Z = i*1 + eps*(x + i h).  Expect -Z^{-1} = i*1 - eps*(x + i h) + O(eps^2):
   both delta X and delta Y flip sign (no rho-even linear fluctuation of Z).
2. On the X = 0 slice H = diag(Y, Y^{-1}); exchanging the two blocks (Y <-> Y^{-1})
   gives the 'even' combination delta(Y) + delta(Y^{-1}) = O(eps^2): zero at
   linear order.
"""
import sympy as sp

eps = sp.symbols("eps")
for d in (1, 2, 3):
    xs = sp.symbols(f"x0:{d*(d+1)//2}", real=True)
    hs = sp.symbols(f"h0:{d*(d+1)//2}", real=True)
    def sym(vals):
        M = sp.zeros(d, d); k = 0
        for i in range(d):
            for j in range(i, d):
                M[i, j] = M[j, i] = vals[k]; k += 1
        return M
    x, h = sym(xs), sym(hs)
    Z = sp.I*sp.eye(d) + eps*(x + sp.I*h)
    W = -Z.inv()
    first = (W.diff(eps)).subs(eps, 0).applyfunc(sp.simplify)
    zeroth = W.subs(eps, 0).applyfunc(sp.simplify)
    ok0 = (zeroth - sp.I*sp.eye(d)).applyfunc(sp.simplify) == sp.zeros(d, d)
    ok1 = (first + (x + sp.I*h)).applyfunc(sp.simplify) == sp.zeros(d, d)
    print(f"d={d}: -Z^-1 at Z=i is i: {ok0}; first-order term is -(x + i h): {ok1}")
    Y = sp.eye(d) + eps*h
    even = (Y + Y.inv())
    lin = even.diff(eps).subs(eps, 0).applyfunc(sp.simplify)
    print(f"d={d}: linear part of delta(Y) + delta(Y^-1) vanishes: {lin == sp.zeros(d, d)}")
