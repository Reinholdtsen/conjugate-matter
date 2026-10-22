"""Debug the d=3 Jacobian rank at the X != 0 zero (expected kernel dim 6 = dim of the zero set)."""
import numpy as np
import sympy as sp

def anticomm_np(X, Y):
    d = X.shape[0]
    om = np.block([[np.zeros((d, d)), np.eye(d)], [-np.eye(d), np.zeros((d, d))]])
    J = np.block([[np.zeros((d, d)), np.eye(d)], [np.eye(d), np.zeros((d, d))]])
    Yi = np.linalg.inv(Y)
    H = np.block([[Y + X@Yi@X, X@Yi], [Yi@X, Yi]])
    I = np.linalg.inv(om)@H
    return J@I + I@J

def jac_fd(X0, Y0, h=1e-6):
    d = X0.shape[0]; cols = []
    for i in range(d):
        for j in range(i, d):
            E = np.zeros((d, d)); E[i, j] = E[j, i] = 1
            cols.append(((anticomm_np(X0 + h*E, Y0) - anticomm_np(X0 - h*E, Y0))/(2*h)).ravel())
            cols.append(((anticomm_np(X0, Y0 + h*E) - anticomm_np(X0, Y0 - h*E))/(2*h)).ravel())
    return np.array(cols).T

# exact analytic linearization at a zero: d{J,I} blocks dS, dA from S,A formulas (exact rationals)
def jac_exact(X0, Y0):
    d = X0.shape[0]; Yi = Y0.inv(); cols = []
    for i in range(d):
        for j in range(i, d):
            E = sp.zeros(d, d); E[i, j] = 1; E[j, i] = 1
            # vary X by E
            dS = E*Yi*X0 + X0*Yi*E; dA = E*Yi - Yi*E
            cols.append(list(dS) + list(dA))
            # vary Y by E: d(Y^-1) = -Yi E Yi
            dYi = -Yi*E*Yi
            dS = E + X0*dYi*X0 - dYi; dA = X0*dYi - dYi*X0
            cols.append(list(dS) + list(dA))
    return sp.Matrix(cols).T

K = sp.Matrix([[0, sp.Rational(1, 2), -1], [-sp.Rational(1, 2), 0, sp.Rational(1, 3)], [1, -sp.Rational(1, 3), 0]])
O3 = (sp.eye(3) - K)*(sp.eye(3) + K).inv()
X3 = O3*sp.diag(sp.Rational(3, 5), -sp.Rational(5, 13), sp.Rational(8, 17))*O3.T
Y3 = O3*sp.diag(sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17))*O3.T
print("O3 orthogonal:", (O3*O3.T - sp.eye(3)).is_zero_matrix, " O3 =", O3.tolist())
Je = jac_exact(X3, Y3)
print("exact analytic Jacobian (S,A blocks) rank:", Je.rank(), " kernel dim:", Je.shape[1] - Je.rank())
Xf = np.array(X3.evalf(), dtype=float); Yf = np.array(Y3.evalf(), dtype=float)
sv = np.linalg.svd(jac_fd(Xf, Yf), compute_uv=False)
print("finite-difference singular values:", np.array2string(sv, precision=3))
print("FD numerical rank (sv > 1e-6):", int(np.sum(sv > 1e-6)), " kernel dim:", 12 - int(np.sum(sv > 1e-6)))
# tangent vectors of the zero set at this point (exact): theta-derivatives and rotation derivatives
th = [sp.Symbol(f"th{k}") for k in range(3)]
s = sp.Symbol("s")
D = sp.diag(*[sp.Rational(3, 5), -sp.Rational(5, 13), sp.Rational(8, 17)])
Dy = sp.diag(*[sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17)])
tangents = []
for k in range(3):   # d/dtheta_k of (cos, sin) -> (-sin, cos)
    dX = sp.zeros(3, 3); dY = sp.zeros(3, 3)
    dX[k, k] = -Dy[k, k]; dY[k, k] = D[k, k]
    tangents.append((O3*dX*O3.T, O3*dY*O3.T))
for (p, q) in [(0, 1), (0, 2), (1, 2)]:  # rotation generators
    G = sp.zeros(3, 3); G[p, q] = 1; G[q, p] = -1
    Gr = O3*G*O3.T
    tangents.append((Gr*X3 - X3*Gr, Gr*Y3 - Y3*Gr))
def vec(dX, dY):
    v = []
    for i in range(3):
        for j in range(i, 3):
            v += [dX[i, j], dY[i, j]]
    return sp.Matrix(v)
T = sp.Matrix.hstack(*[vec(a, b) for a, b in tangents])
print("rank of the 6 exact tangent vectors:", T.rank(), "; Jacobian x tangents == 0:", (Je*T).is_zero_matrix)
