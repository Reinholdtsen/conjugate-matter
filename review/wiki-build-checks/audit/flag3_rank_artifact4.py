import sympy as sp
src = open("flag3_recompute.py").read().split('print("=== Part 1')[0]
ns = {}; exec(src, ns); anticomm = ns["anticomm"]
K = sp.Matrix([[0, sp.Rational(1, 2), -1], [-sp.Rational(1, 2), 0, sp.Rational(1, 3)], [1, -sp.Rational(1, 3), 0]])
O3 = (sp.eye(3) - K)*(sp.eye(3) + K).inv()
X0 = O3*sp.diag(sp.Rational(3, 5), -sp.Rational(5, 13), sp.Rational(8, 17))*O3.T
Y0 = O3*sp.diag(sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17))*O3.T
d = 3; t = sp.Symbol("t"); params = []; dX = sp.zeros(d, d); dY = sp.zeros(d, d)
for i in range(d):
    for j in range(i, d):
        a = sp.Symbol(f"a{i}{j}"); b = sp.Symbol(f"b{i}{j}"); params += [a, b]
        dX[i, j] += a; dY[i, j] += b
        if i != j: dX[j, i] += a; dY[j, i] += b
M = anticomm(X0 + t*dX, Y0 + t*dY)
lin = [sp.diff(e, t).subs(t, 0) for e in M]
Jm = sp.Matrix([[sp.diff(l, p) for p in params] for l in lin])
print("same path, NO nsimplify: rank", Jm.rank(), "kernel", 12 - Jm.rank())
Jn = Jm.applyfunc(sp.nsimplify)
changed = [(e, n) for e, n in zip(Jm, Jn) if e != n]
print("entries altered by nsimplify:", len(changed), "; e.g.", changed[:2])
print("after nsimplify: rank", Jn.rank())
