import sympy as sp
a, b, c = sp.symbols("a b c")
Yp = sp.Matrix([[a, b], [b, c]])
sol = sp.solve(list(Yp*Yp - sp.eye(2)), [a, b, c], dict=True)
print("solutions of Y^2 = 1 (2x2 symmetric):", sol)
pd = []
for s in sol:
    M = Yp.subs(s)
    free = M.free_symbols
    # positive definite requires trace > 0 and det > 0; det(Y) for Y^2=1 is +-1
    print("  family", M.tolist(), " det =", sp.simplify(M.det()), " trace =", sp.simplify(M.trace()))
