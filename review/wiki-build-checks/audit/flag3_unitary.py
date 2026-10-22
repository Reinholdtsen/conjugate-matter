"""Z Z-bar = 1  <=>  [X,Y] = 0 and X^2 + Y^2 = 1 (symbolic, d = 2); and the zero set meets X = 0 only at Y = 1."""
import sympy as sp
def symsym(name, d):
    M = sp.zeros(d, d)
    for i in range(d):
        for j in range(i, d):
            s = sp.Symbol(f"{name}{i}{j}", real=True); M[i, j] = s; M[j, i] = s
    return M
X = symsym("x", 2); Y = symsym("y", 2)
Z = X + sp.I*Y; Zb = X - sp.I*Y
P = sp.expand(Z*Zb - sp.eye(2))
re = P.applyfunc(lambda e: sp.re(e)); im = P.applyfunc(lambda e: sp.im(e))
print("Re(Z Zbar - 1) == X^2 + Y^2 - 1:", (re - (X*X + Y*Y - sp.eye(2))).applyfunc(sp.expand).is_zero_matrix)
print("Im(Z Zbar - 1) == Y X - X Y   :", (im - (Y*X - X*Y)).applyfunc(sp.expand).is_zero_matrix)
print("Z symmetric => Z^dagger = Zbar, so Z Zbar = 1 is unitarity:", (Z.T - Z).is_zero_matrix)
# intersection with Theorem A's eta-compatible slice X = 0: Y^2 = 1 with Y > 0
Yp = symsym("y", 2)
sol = sp.solve(list(Yp*Yp - sp.eye(2)), list(Yp.free_symbols), dict=True)
print("solutions of Y^2 = 1 (2x2 symmetric):", sol)
print("positive-definite ones:", [s for s in sol if all(ev > 0 for ev in Yp.subs(s).eigenvals())])
