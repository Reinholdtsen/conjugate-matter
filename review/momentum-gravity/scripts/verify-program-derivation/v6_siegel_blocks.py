"""Verifier check of P5: how X = Re Z enters the blocks of the Siegel generalized metric
H_Z = [[Y + X Y^-1 X, X Y^-1], [Y^-1 X, Y^-1]] (#11 sec. 6; #5 sec. C), d = 2 and d = 3,
expanded about the vacuum X = 0, Y = 1 + h.  Also: the quadratic part of the misalignment block
S = Y + X Y^-1 X - Y^-1 (#11 sec. 7.2) has no h-X mixing, and the Siegel target metric
Tr(Y^-1 dZ Y^-1 dZbar) has no dX-dY cross term."""
import sympy as sp

for d in (2, 3):
    t = sp.symbols('t')
    Xs = sp.Matrix(d, d, lambda i, j: sp.Symbol(f'x{min(i, j)}{max(i, j)}'))
    hs = sp.Matrix(d, d, lambda i, j: sp.Symbol(f'h{min(i, j)}{max(i, j)}'))
    X = t*Xs
    Y = sp.eye(d) + t*hs
    Yi = Y.inv()
    # series of Yi to O(t^2) is enough for the order counting
    Yi2 = (sp.eye(d) - t*hs + t**2*hs*hs)
    pos = Y + X*Yi2*X
    mix = X*Yi2
    mom = Yi2
    order = lambda Mtx, k: Mtx.applyfunc(lambda e: sp.expand(e).coeff(t, k))
    # linear-in-X part: differentiate w.r.t. the x's at X = 0
    def linX(Mtx):
        return Mtx.applyfunc(lambda e: sum(sp.diff(e, s).subs({q: 0 for q in Xs.free_symbols})*s for s in Xs.free_symbols))
    print(f"d = {d}: position block linear in X zero: {sp.simplify(linX(pos)) == sp.zeros(d, d)};"
          f" mixed block linear in X nonzero: {sp.simplify(linX(mix)) != sp.zeros(d, d)};"
          f" momentum block X-free: {all(sp.diff(e, s) == 0 for e in mom for s in Xs.free_symbols)}")
    S = Y + X*Yi2*X - Yi2
    S2 = order(S, 1)
    print(f"       misalignment block S at O(t): {S2.applyfunc(sp.expand) == (2*hs).applyfunc(sp.expand)} (= 2h, no X);"
          f" Tr(S^2) at O(t^2) contains an h*x cross term: {any(sp.expand((S*S).trace()).coeff(t, 2).coeff(a).coeff(b) != 0 for a in hs.free_symbols for b in Xs.free_symbols)}")
    # anchor: (omega^-1 H_Z)^2 = -1 exactly at a random numeric point
    import random
    random.seed(d)
    Xn = sp.Matrix(d, d, lambda i, j: 0); Yn = sp.Matrix(d, d, lambda i, j: 0)
    for i in range(d):
        for j in range(i, d):
            Xn[i, j] = Xn[j, i] = sp.Rational(random.randint(-9, 9), 7)
    B = sp.Matrix(d, d, lambda i, j: sp.Rational(random.randint(-5, 5), 3))
    Yn = B*B.T + sp.eye(d)
    Yni = Yn.inv()
    H = sp.BlockMatrix([[Yn + Xn*Yni*Xn, Xn*Yni], [Yni*Xn, Yni]]).as_explicit()
    om = sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [-sp.eye(d), sp.zeros(d)]]).as_explicit()
    I = om.inv()*H
    print(f"       anchor (omega^-1 H_Z)^2 = -1 at an exact random point: {sp.simplify(I*I + sp.eye(2*d)) == sp.zeros(2*d)}")
