"""Critic, tension (c): the second frame f = E0[J].

gravity-sector C23: a second frame with fixed scale (Ydot = 0) admits no expanding FLRW in Hassan-Rosen
  dynamics (any k).
observations C52 (Comelli, Crisostomi, Nesti, Pilo): with a frozen flat second metric only open FRW exists.
Are these consistent, and what does each reading of 'no scale of its own' allow for k = +1?

(1) f = -X(t)^2 dt^2 + Y(t)^2 gamma_k. Flat (Riemann = 0) iff (Ydot/X)^2 + k = 0 and d/dt(Ydot/X) = 0:
    k = +1 impossible; k = 0 needs Ydot = 0; k = -1 is Milne (Ydot = X).
(2) HR Bianchi constraint (beta1 a^2 + 2 beta2 a Y + beta3 Y^2)(N Ydot - X adot) = 0:
    fixed Y -> adot = 0 (or a pinned at a root);  Milne f (X = 1, Y = t) -> N = adot: an ordinary
    lapse relation, so open FRW solutions exist.
(3) A frozen closed de Sitter reference (X = 1, Y = cosh t / H_f) gives N sinh(t) = adot: also only a
    lapse relation, so a frozen closed reference is not excluded by the constraint [D]; but every frozen f
    is the M_f -> infinity limit, which the record's M_f u = M_g forbids.
(4) On the program's beta1 > 0 dynamical branch y = Y/a lies in (0, 1] at every density, so a bounded
    ratio y is automatic and does not bound Y = y a.
"""
import sympy as sp

t, chi, th, ph = sp.symbols('t chi theta phi', real=True)
k = sp.symbols('k', real=True)
X = sp.Function('X')(t); Y = sp.Function('Y')(t)

def Sk(kval):
    return {1: sp.sin(chi), 0: chi, -1: sp.sinh(chi)}[kval]

def riemann_components(g, coords):
    n = len(coords)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, d]*(sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b])
                                          - sp.diff(g[b, c], coords[d])) for d in range(n))/2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    R = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(c+1, n):
                    expr = sp.diff(Gam[a][b][d], coords[c]) - sp.diff(Gam[a][b][c], coords[d])
                    expr += sum(Gam[a][c][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][c] for e in range(n))
                    expr = sp.simplify(expr)
                    if expr != 0:
                        R[(a, b, c, d)] = expr
    return R

print("=== (1) flatness of f = -X^2 dt^2 + Y^2 gamma_k ===")
coords = [t, chi, th, ph]
for kval in [1, 0, -1]:
    S = Sk(kval)
    g = sp.diag(-X**2, Y**2, Y**2*S**2, Y**2*S**2*sp.sin(th)**2)
    R = riemann_components(g, coords)
    # collect the independent conditions
    conds = set()
    for key, expr in R.items():
        num = sp.factor(sp.numer(sp.together(expr)))
        conds.add(sp.simplify(num))
    print(f"  k = {kval:+d}: nonzero Riemann numerators (up to factors):")
    for cnd in list(conds)[:4]:
        print("     ", sp.factor(cnd))
    # test candidate solutions
    if kval == -1:
        sub = {X: 1, Y: t}
    elif kval == 0:
        sub = {X: 1, Y: sp.Integer(1)}
    else:
        sub = None
    if sub is not None:
        import random
        random.seed(1)
        worst = 0.0
        for e_ in R.values():
            ex = e_.subs(sub).doit()
            for _ in range(5):
                val = complex(ex.subs({t: random.uniform(0.5, 2), chi: random.uniform(0.2, 1.3),
                                       th: random.uniform(0.2, 1.3), ph: 0.3}).evalf())
                worst = max(worst, abs(val))
        print(f"     candidate {sub}: max |Riemann component| at 5 random points each = {worst:.1e} (flat if ~0)")
print("  k = +1: the spatial-spatial component requires (Ydot/X)^2 + 1 = 0 -> no real flat closed slicing")
# direct check of the k=+1 condition
S = Sk(1)
g = sp.diag(-X**2, Y**2, Y**2*S**2, Y**2*S**2*sp.sin(th)**2)
R = riemann_components(g, coords)
e = sp.simplify(R[(1, 2, 1, 2)] if (1, 2, 1, 2) in R else list(R.values())[0])
print("  k=+1, R^chi_theta chi theta =", sp.factor(e))

print("\n=== (2)-(3) Bianchi constraint for frozen references ===")
a = sp.Function('a')(t); N = sp.Function('N')(t)
b1, b2, b3 = sp.symbols('beta1 beta2 beta3', positive=True)
poly = b1*a**2 + 2*b2*a*Y + b3*Y**2
bianchi = poly*(N*sp.diff(Y, t) - X*sp.diff(a, t))
for name, sub in [('fixed scale Y = Y0', {Y: sp.Symbol('Y0', positive=True), X: 1}),
                  ('Milne (flat, k = -1): X = 1, Y = t', {Y: t, X: 1}),
                  ('closed de Sitter reference: X = 1, Y = cosh(Hf t)/Hf',
                   {Y: sp.cosh(sp.Symbol('H_f', positive=True)*t)/sp.Symbol('H_f', positive=True), X: 1})]:
    expr = sp.simplify(bianchi.subs(sub).doit())
    print(f"  {name}: constraint = {sp.factor(expr)}")
print("  fixed scale: the factor (N*0 - adot) forces adot = 0 unless the polynomial vanishes (a pinned to a root)")
print("  Milne / closed dS: N Ydot = adot is solvable for the lapse N -> the constraint does not forbid expansion")

print("\n=== (4) program branch: y = Y/a in (0, 1] ===")
y, s = sp.symbols('y s', positive=True)
rho_hat = (1 - y**2)*(y**2 + (4 + 6*s)*y + 1)/(3*y)       # rho/(3 Mg^2 m^2 beta1), beta2 = s beta1
d = sp.factor(sp.diff(rho_hat, y))
print("  d rho_hat/dy =", d)
import numpy as np
f = sp.lambdify((y, s), rho_hat, 'numpy')
for sv in [-0.9, 0, 1, 10, 100]:
    ys = np.linspace(1e-4, 1, 20001)
    vals = f(ys, sv)
    print(f"  s = {sv:6}: rho_hat(1) = {f(1.0, sv):.1e}, min over (0,1] = {vals.min():.3e}, "
          f"monotone decreasing: {bool(np.all(np.diff(vals) < 0))}, rho_hat(1e-4) = {vals[0]:.3e}")
print("  -> every density rho >= 0 is reached once with y in (0, 1]; Y = y a grows with a; boundedness of y says"
      " nothing about the size of the universe")
