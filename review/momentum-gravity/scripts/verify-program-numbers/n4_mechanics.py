# Independent sympy checks of the mechanics claims P5 (Siegel blocks), P10, P12, P15.
import sympy as sp

# ---------------- P5: linear-in-X content of H_Z blocks (d = 2) --------------------------
a, b, cc, d1, d2, d3, t = sp.symbols('a b c d1 d2 d3 t', real=True)
Y = sp.Matrix([[a, b], [b, cc]])
Xm = sp.Matrix([[d1, d2], [d2, d3]])
Yi = Y.inv()
HZ = sp.BlockMatrix([[Y + Xm*Yi*Xm, Xm*Yi], [Yi*Xm, Yi]]).as_explicit()
# scale X -> t X and look at the t^1 coefficient of each block
HZt = HZ.subs({d1: t*d1, d2: t*d2, d3: t*d3}, simultaneous=True)
lin = HZt.applyfunc(lambda e: sp.simplify(sp.diff(e, t).subs(t, 0)))
print("P5: t^1 coefficient, position (x-x) block zero:", lin[:2, :2] == sp.zeros(2, 2),
      "; mixed block zero:", lin[:2, 2:] == sp.zeros(2, 2), "; momentum block zero:", lin[2:, 2:] == sp.zeros(2, 2))
om = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]])
samp = {a: 2, b: sp.Rational(1, 3), cc: 1, d1: sp.Rational(1, 2), d2: -1, d3: sp.Rational(3, 7)}
I = om.inv()*HZ.subs(samp)
print("anchor (omega^-1 H_Z)^2 = -1 at a sample point:", sp.simplify(I*I + sp.eye(4)) == sp.zeros(4, 4))

# ---------------- P10: model (a), U depends on momenta only -----------------------------
m1, m2, u = sp.symbols('m1 m2 u', positive=True)
x1, x2, p1, p2 = sp.symbols('x1 x2 p1 p2', real=True)   # 1D suffices for these statements
Uf = sp.Function('U')
for name, arg in (("p1 - p2", p1 - p2), ("k = (m2 p1 - m1 p2)/M", (m2*p1 - m1*p2)/(m1 + m2))):
    Hm = p1**2/(2*m1) + p2**2/(2*m2) + Uf(arg)
    pdot1 = -sp.diff(Hm, x1)
    xdot1 = sp.diff(Hm, p1); xdot2 = sp.diff(Hm, p2)
    cm = sp.simplify(m1*xdot1 + m2*xdot2 - (p1 + p2))
    shift = sp.simplify(arg.subs({p1: p1 + m1*u, p2: p2 + m2*u}, simultaneous=True) - arg)
    print(f"P10 arg {name}: pdot1 = {pdot1}; d(m1x1+m2x2)/dt - P = {cm}; boost shift of argument = {shift}")

# ---------------- P12: model (b) --------------------------------------------------------
Gt, vs, r = sp.symbols('Gtilde v_star r', positive=True)
v1 = sp.Matrix(sp.symbols('v1x v1y v1z', real=True)); v2 = sp.Matrix(sp.symbols('v2x v2y v2z', real=True))
W = sp.Function('W')
w = sp.sqrt(((v1 - v2).T*(v1 - v2))[0])/vs
L = m1*(v1.T*v1)[0]/2 + m2*(v2.T*v2)[0]/2 + Gt*m1*m2*W(w)/r
pv = [sp.diff(L, q) for q in list(v1) + list(v2)]
Efun = sum(q*pq for q, pq in zip(list(v1) + list(v2), pv)) - L
ws = sp.symbols('w_s', positive=True)
target = m1*(v1.T*v1)[0]/2 + m2*(v2.T*v2)[0]/2 - Gt*m1*m2/r*(W(w) - w*sp.Subs(sp.Derivative(W(ws), ws), ws, w).doit())
print("P12 energy function - [sum m v^2/2 - Gt m1 m2 (W - w W')/r] =", sp.simplify(sp.expand(Efun - target)))
uvec = sp.Matrix(sp.symbols('ux uy uz', real=True))
Lb = L.subs({**{v1[i]: v1[i] + uvec[i] for i in range(3)}, **{v2[i]: v2[i] + uvec[i] for i in range(3)}}, simultaneous=True)
print("P12 boost: L(v+u) - L(v) - [u.(m1 v1 + m2 v2) + M u^2/2] =",
      sp.simplify(sp.expand(Lb - L - ((uvec.T*(m1*v1 + m2*v2))[0] + (m1 + m2)*(uvec.T*uvec)[0]/2))))
# Gaussian gate, relative coordinate, 1D: L_rel = mu v^2/2 + Gt m1 m2 exp(-v^2/vs^2)/r
mu, M, v, p = sp.symbols('mu M v p', positive=True)
Lrel = mu*v**2/2 + Gt*m1*m2*sp.exp(-v**2/vs**2)/r
hess = sp.diff(Lrel, v, 2).subs(v, 0)
print("P12 Lagrangian Hessian at v_rel = 0:", sp.simplify(hess.subs(m1*m2, mu*M)), "; zero at r =",
      sp.solve(sp.Eq(hess.subs(m1, mu*M/m2), 0), r))
Hrel = p**2/(2*mu) - Gt*m1*m2*sp.exp(-p**2/(mu**2*vs**2))/r
inv = sp.diff(Hrel, p, 2).subs(p, 0)
print("P12 Hamiltonian inverse inertia at p = 0:", sp.simplify(inv.subs(m1, mu*M/m2)), " = (1/mu)(1 + 2 Gt M/(r v*^2))?",
      sp.simplify(inv.subs(m1, mu*M/m2) - (1/mu)*(1 + 2*Gt*M/(r*vs**2))) == 0)
# CM drift for the two gate arguments (1D)
for name, arg in (("|p1/m1 - p2/m2|/v*", (p1/m1 - p2/m2)/vs), ("|p1 - p2|/(m1 v*)", (p1 - p2)/(m1*vs))):
    Hb = p1**2/(2*m1) + p2**2/(2*m2) - Gt*m1*m2*sp.exp(-arg**2)/sp.Abs(x1 - x2)
    cm = sp.simplify(m1*sp.diff(Hb, p1) + m2*sp.diff(Hb, p2) - (p1 + p2))
    print(f"P12 CM drift, gate argument {name}: {cm}")
