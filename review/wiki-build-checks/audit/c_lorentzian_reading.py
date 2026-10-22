# Audit of flag 3: does an indefinite (Lorentzian) Y rescue "X = 0 and Y = Y^-1"?
# The identities S*Y - (X^2+Y^2-1) = X Y^-1 [X,Y] and A = Y^-1 [Y,X] Y^-1 are algebraic
# (checked symbolically in a_symbolic_zero_set.py without positivity), so the zero set is
# {[X,Y] = 0, X^2 + Y^2 = 1} for any invertible symmetric Y. Explicit Lorentzian example:
import numpy as np
d = 4
Id = np.eye(d); Zr = np.zeros((d, d))
omega = np.block([[Zr, Id], [-Id, Zr]]); J0 = np.block([[Zr, Id], [Id, Zr]])
def anti(X, Y):
    Yi = np.linalg.inv(Y)
    H = np.block([[Y + X@Yi@X, X@Yi], [Yi@X, Yi]])
    I = np.linalg.inv(omega)@H
    return J0@I + I@J0
th = np.array([0.4, 0.7, -0.3, 1.1])
rng = np.random.default_rng(7)
Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
sgn = np.array([-1.0, 1.0, 1.0, 1.0])               # signature (-,+,+,+)
X = Q@np.diag(np.sin(th))@Q.T
Y = Q@np.diag(sgn*np.cos(th))@Q.T
print("eigenvalues of Y (Lorentzian):", np.round(np.linalg.eigvalsh(Y), 4))
print("|X| =", round(np.linalg.norm(X), 4), "; |Y - Y^-1| =", round(np.linalg.norm(Y - np.linalg.inv(Y)), 4))
print("|{J0, I[Z]}| =", f"{np.linalg.norm(anti(X, Y)):.2e}")
