"""Why did the first script's symbolic Jacobian report rank 7 at the d=3 zero? Re-run its path, then simplify entries."""
import sympy as sp
import importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location("r", "flag3_recompute.py")
# only borrow helper definitions: exec the top part of the file up to Part 1
src = open("flag3_recompute.py").read().split('print("=== Part 1')[0]
ns = {}; exec(src, ns)
anticomm = ns["anticomm"]
K = sp.Matrix([[0, sp.Rational(1, 2), -1], [-sp.Rational(1, 2), 0, sp.Rational(1, 3)], [1, -sp.Rational(1, 3), 0]])
O3 = (sp.eye(3) - K)*(sp.eye(3) + K).inv()
X0 = O3*sp.diag(sp.Rational(3, 5), -sp.Rational(5, 13), sp.Rational(8, 17))*O3.T
Y0 = O3*sp.diag(sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17))*O3.T
d = 3; params = []; dX = sp.zeros(d, d); dY = sp.zeros(d, d)
for i in range(d):
    for j in range(i, d):
        a = sp.Symbol(f"a{i}{j}"); b = sp.Symbol(f"b{i}{j}"); params += [a, b]
        dX[i, j] += a; dY[i, j] += b
        if i != j: dX[j, i] += a; dY[j, i] += b
t = sp.Symbol("t")
M = anticomm(X0 + t*dX, Y0 + t*dY)
lin = [sp.diff(e, t).subs(t, 0) for e in M]
Jm = sp.Matrix([[sp.diff(l, p) for p in params] for l in lin])
nonrational = sum(1 for e in Jm if not e.is_Rational)
print("entries that are not plain Rationals before simplify:", nonrational)
Js = Jm.applyfunc(lambda e: sp.nsimplify(sp.simplify(e)))
print("after simplify: non-Rational entries:", sum(1 for e in Js if not e.is_Rational), "; rank:", Js.rank(), "; kernel:", 12 - Js.rank())
