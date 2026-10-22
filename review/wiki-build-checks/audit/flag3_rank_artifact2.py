"""Compare the symbolic-path Jacobian with the analytic one at the d=3 zero, entry by entry."""
import sympy as sp, numpy as np
src = open("flag3_recompute.py").read().split('print("=== Part 1')[0]
ns = {}; exec(src, ns); anticomm = ns["anticomm"]; HZ = ns["HZ"]; blocks = ns["blocks"]
K = sp.Matrix([[0, sp.Rational(1, 2), -1], [-sp.Rational(1, 2), 0, sp.Rational(1, 3)], [1, -sp.Rational(1, 3), 0]])
O3 = (sp.eye(3) - K)*(sp.eye(3) + K).inv()
X0 = O3*sp.diag(sp.Rational(3, 5), -sp.Rational(5, 13), sp.Rational(8, 17))*O3.T
Y0 = O3*sp.diag(sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17))*O3.T
d = 3; t = sp.Symbol("t")
Yi0 = Y0.inv()
bad = 0
for i in range(d):
    for j in range(i, d):
        E = sp.zeros(d, d); E[i, j] = 1; E[j, i] = 1
        for which in ("X", "Y"):
            Xt = X0 + (t*E if which == "X" else sp.zeros(d, d)); Yt = Y0 + (t*E if which == "Y" else sp.zeros(d, d))
            M = anticomm(Xt, Yt)
            dM = M.applyfunc(lambda e: sp.diff(e, t).subs(t, 0))
            if which == "X":
                dS = E*Yi0*X0 + X0*Yi0*E; dA = E*Yi0 - Yi0*E
            else:
                dYi = -Yi0*E*Yi0; dS = E + X0*dYi*X0 - dYi; dA = X0*dYi - dYi*X0
            ok = (dM[:d, :d] - dS).applyfunc(sp.simplify).is_zero_matrix and (dM[:d, d:] - dA).applyfunc(sp.simplify).is_zero_matrix
            if not ok:
                bad += 1
                print(f"mismatch at ({i},{j}) {which}: max |diff| =",
                      max(abs(float(v)) for v in list(dM[:d, :d] - dS) + list(dM[:d, d:] - dA)))
print("single-direction (one parameter at a time) symbolic derivatives disagreeing with analytic:", bad)
# Now the original multi-parameter path, but with a single symbolic t and numeric directions -> should be fine;
# the original used many symbols a_ij,b_ij inside one inverse. Re-do it and evaluate Y^-1 by adjugate/det instead.
params = []; dX = sp.zeros(d, d); dY = sp.zeros(d, d)
for i in range(d):
    for j in range(i, d):
        a = sp.Symbol(f"a{i}{j}"); b = sp.Symbol(f"b{i}{j}"); params += [a, b]
        dX[i, j] += a; dY[i, j] += b
        if i != j: dX[j, i] += a; dY[j, i] += b
Yt = Y0 + t*dY; Xt = X0 + t*dX
Yinv_adj = Yt.adjugate() / Yt.det()
omega, J0 = blocks(3)
H = sp.BlockMatrix([[Yt + Xt*Yinv_adj*Xt, Xt*Yinv_adj], [Yinv_adj*Xt, Yinv_adj]]).as_explicit()
I = omega.inv()*H; M = J0*I + I*J0
lin = [sp.diff(e, t).subs(t, 0) for e in M]
Jm = sp.Matrix([[sp.expand(sp.diff(l, p)) for p in params] for l in lin])
print("multi-parameter path with adjugate inverse: rank", Jm.rank(), "kernel", 12 - Jm.rank())
Yt_inv_default = Yt.inv()
diffinv = (Yt_inv_default - Yinv_adj).subs(t, sp.Rational(1, 7)).subs({p: sp.Rational(k + 1, 11) for k, p in enumerate(params)})
print("default .inv() vs adjugate inverse at a random rational point: max |diff| =", max(abs(float(sp.nsimplify(v))) for v in diffinv))
