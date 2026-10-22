import sympy as sp
src = open("flag3_recompute.py").read().split('print("=== Part 1')[0]
ns = {}; exec(src, ns); blocks = ns["blocks"]
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
Yt = Y0 + t*dY
Ydef = Yt.inv(); Yadj = Yt.adjugate()/Yt.det()
# derivative of the inverse at t = 0 should be -Y0^-1 dY Y0^-1 (linear in b's)
exact = -Y0.inv()*dY*Y0.inv()
for lbl, Yinv in [("default .inv()", Ydef), ("adjugate/det", Yadj)]:
    der = Yinv.applyfunc(lambda e: sp.diff(e, t).subs(t, 0))
    dif = (der - exact).applyfunc(sp.expand)
    print(f"{lbl}: d(Y^-1)/dt at t=0 minus exact -Y0^-1 dY Y0^-1 -> zero matrix: {dif.is_zero_matrix}")
    if not dif.is_zero_matrix:
        print("   nonzero entries:", [(k, sp.nsimplify(v)) for k, v in enumerate(dif) if v != 0][:4])
    val0 = Yinv.applyfunc(lambda e: e.subs(t, 0))
    print(f"   value at t=0 equals Y0^-1: {(val0 - Y0.inv()).applyfunc(sp.simplify).is_zero_matrix}")
