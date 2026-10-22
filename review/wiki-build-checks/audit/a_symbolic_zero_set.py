# Audit of flag 3: exact (sympy) zero set of {J0, I[Z]}.
# I[Z] is built here as omega^-1 H_Z from the standard Siegel generalized metric
# (#5 section C), not copied from #7, and compared with #7's printed I[Z].
import sympy as sp

def blocks(M, d):
    return M[:d, :d], M[:d, d:], M[d:, :d], M[d:, d:]

def setup(X, Y, d):
    Id = sp.eye(d); Z0 = sp.zeros(d)
    omega = sp.Matrix(sp.BlockMatrix([[Z0, Id], [-Id, Z0]]))
    J0 = sp.Matrix(sp.BlockMatrix([[Z0, Id], [Id, Z0]]))
    Yi = Y.inv()
    HZ = sp.Matrix(sp.BlockMatrix([[Y + X*Yi*X, X*Yi], [Yi*X, Yi]]))
    I = omega.inv()*HZ
    return omega, J0, HZ, I, Yi

print("=== d = 1 ===")
x, y = sp.symbols('x y', real=True)
X = sp.Matrix([[x]]); Y = sp.Matrix([[y]])
omega, J0, HZ, I, Yi = setup(X, Y, 1)
I7 = sp.Matrix(sp.BlockMatrix([[-Yi*X, -Yi], [Y + X*Yi*X, X*Yi]]))
print("omega^-1 H_Z equals #7's printed I[Z]:", sp.simplify(I - I7) == sp.zeros(2))
print("I^2 = -1:", sp.simplify(I*I + sp.eye(2)) == sp.zeros(2))
M = sp.simplify(J0*I + I*J0)
print("{J0, I[Z]} =", M.tolist())
sols = sp.solve([sp.numer(sp.together(e)) for e in M], [x, y], dict=True)
print("solutions of {J0,I}=0 over reals (y>0 to be imposed):", sols)
print("=> zero set at d=1 is x^2 + y^2 = 1, y > 0 (upper unit semicircle), e.g. Z = 3/5 + 4i/5:",
      sp.simplify(M.subs({x: sp.Rational(3, 5), y: sp.Rational(4, 5)})) == sp.zeros(2))

print("\n=== d = 2, general symmetric X, Y ===")
a, b, c, p, q, r = sp.symbols('a b c p q r', real=True)
X = sp.Matrix([[a, b], [b, c]]); Y = sp.Matrix([[p, q], [q, r]])
omega, J0, HZ, I, Yi = setup(X, Y, 2)
M = J0*I + I*J0
S = Y + X*Yi*X - Yi; A = X*Yi - Yi*X
M11, M12, M21, M22 = blocks(M, 2)
print("blocks = [[S,A],[A,S]] (T3, exact):",
      all(sp.simplify(B - T) == sp.zeros(2) for B, T in [(M11, S), (M12, A), (M21, A), (M22, S)]))
comm = X*Y - Y*X
print("identity A = Y^-1 [Y,X] Y^-1:", sp.simplify(A - Yi*(Y*X - X*Y)*Yi) == sp.zeros(2))
print("identity S*Y - (X^2 + Y^2 - 1) = X Y^-1 [X,Y]:",
      sp.simplify(S*Y - (X*X + Y*Y - sp.eye(2)) - X*Yi*comm) == sp.zeros(2))
print("=> {J0,I}=0  <=>  [X,Y]=0 and X^2+Y^2=1 (Y invertible)")

print("\n=== d = 2, explicit exact family with X != 0 ===")
# rational points on the unit circle: (s,c) = (3/5,4/5), (-5/13,12/13); rotation by (cos,sin) = (8/17,15/17)
s1, c1 = sp.Rational(3, 5), sp.Rational(4, 5)
s2, c2 = sp.Rational(-5, 13), sp.Rational(12, 13)
R = sp.Matrix([[sp.Rational(8, 17), -sp.Rational(15, 17)], [sp.Rational(15, 17), sp.Rational(8, 17)]])
Xf = R*sp.diag(s1, s2)*R.T; Yf = R*sp.diag(c1, c2)*R.T
omega, J0, HZ, I, Yi = setup(Xf, Yf, 2)
Mf = sp.simplify(J0*I + I*J0)
print("X =", Xf.tolist())
print("Y =", Yf.tolist(), " eigenvalues of Y:", list(Yf.eigenvals().keys()))
print("{J0, I[Z]} at this point (exact):", Mf.tolist())
print("is zero:", Mf == sp.zeros(4), "; X is nonzero:", Xf != sp.zeros(2), "; Y == Y^-1:", Yf == Yf.inv())
print("Z Zbar = 1 there (matrix |Z| = 1):", sp.simplify((Xf + sp.I*Yf)*(Xf - sp.I*Yf)) == sp.eye(2))
