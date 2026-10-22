import sympy as sp
a, b, c = sp.symbols("a b c", real=True)
Yp = sp.Matrix([[a, b], [b, c]])
E = (Yp*Yp - sp.eye(2)).applyfunc(sp.expand)
print("Y^2 - 1 entries:", E.tolist())
# case b = 0
s0 = sp.solve([E[0, 0].subs(b, 0), E[1, 1].subs(b, 0)], [a, c], dict=True)
print("b = 0 solutions:", s0, "-> positive definite:", [s for s in s0 if s[a] > 0 and s[c] > 0])
# case b != 0: off-diagonal b(a + c) = 0 forces c = -a, so trace(Y) = 0 and Y cannot be positive definite
print("off-diagonal entry factored:", sp.factor(E[0, 1]), "; with c = -a, trace =", (Yp.subs(c, -a)).trace())
