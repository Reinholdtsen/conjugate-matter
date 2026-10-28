#!/usr/bin/env python3
"""P1 (label: program). Where X = Re Z enters the Siegel generalized metric at linear order.

H_Z = [[Y + X Y^-1 X, X Y^-1], [Y^-1 X, Y^-1]] (#11 sec. 6; notes/debt1a-geometric-core.md sec. C).
Question: does a field that couples only to the position block (Y + X Y^-1 X, which is g = Y at X = 0) feel X
at linear order? Checked for d = 2 with general symmetric X and Y.
"""
import sympy as sp
d = 2
xs = sp.symbols('x11 x12 x22', real=True); ys = sp.symbols('y11 y12 y22', real=True)
X = sp.Matrix([[xs[0], xs[1]], [xs[1], xs[2]]])
Y = sp.Matrix([[ys[0], ys[1]], [ys[1], ys[2]]])
eps = sp.symbols('epsilon')
Yi = Y.inv()
Xe = eps*X
blocks = {'position block Y + X Y^-1 X': Y + Xe*Yi*Xe, 'mixed block X Y^-1': Xe*Yi, 'momentum block Y^-1': Yi}
for name, B in blocks.items():
    lin = sp.simplify(sp.diff(B, eps).subs(eps, 0))
    quad = sp.simplify(sp.diff(B, eps, 2).subs(eps, 0)/2)
    print(f"{name:30s}: linear in X -> zero: {lin == sp.zeros(d, d)} ; quadratic in X -> zero: {quad == sp.zeros(d, d)}")
# the Siegel matrix is symplectic-positive: check I[Z]^2 = -1 at a sample point (anchor, as battery T2)
om = sp.Matrix(sp.BlockMatrix([[sp.zeros(d), sp.eye(d)], [-sp.eye(d), sp.zeros(d)]]))
HZ = sp.Matrix(sp.BlockMatrix([[Y + X*Yi*X, X*Yi], [Yi*X, Yi]]))
vals = {xs[0]: sp.Rational(1, 3), xs[1]: sp.Rational(-1, 5), xs[2]: sp.Rational(2, 7),
        ys[0]: 2, ys[1]: sp.Rational(1, 2), ys[2]: 1}
IZ = om.inv()*HZ.subs(vals)
print("anchor: (omega^-1 H_Z)^2 = -1 at a sample point:", sp.simplify(IZ*IZ + sp.eye(2*d)) == sp.zeros(2*d, 2*d))
