# Check #7 §1 ("{J, I[Z]} ... zero exactly on the compatible locus") and §2 consequence 1
# ("The compatible locus is X = 0 and Y = Y^-1"), using verify/battery.py's conventions:
# omega=[[0,I],[-I,0]], eta=[[0,I],[I,0]] (J0 = eta), H_Z=[[Y+XY^-1X, XY^-1],[Y^-1X, Y^-1]], I[Z]=omega^-1 H_Z.
import numpy as np
d = 4
Id = np.eye(d); Zr = np.zeros((d, d))
omega = np.block([[Zr, Id], [-Id, Zr]]); eta = np.block([[Zr, Id], [Id, Zr]])
def anticomm(X, Y):
    Yi = np.linalg.inv(Y)
    HZ = np.block([[Y + X@Yi@X, X@Yi], [Yi@X, Yi]])
    IZ = np.linalg.inv(omega)@HZ
    return eta@IZ + IZ@eta, HZ
rng = np.random.default_rng(3)
# A configuration with X != 0: X and Y commuting, X^2 + Y^2 = 1, Y > 0 (rotate a diagonal pair by a random orthogonal Q).
theta = rng.uniform(-1.2, 1.2, size=d)
Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
X = Q@np.diag(np.sin(theta))@Q.T
Y = Q@np.diag(np.cos(theta))@Q.T
M, HZ = anticomm(X, Y)
print("|X| =", round(np.linalg.norm(X), 4), " min eig Y =", round(np.linalg.eigvalsh(Y).min(), 4))
print("|{J0, I[Z]}| at this X != 0 point:", np.linalg.norm(M))
print("eta-compatibility of H_Z there, |(eta^-1 H_Z)^2 - 1|:", round(np.linalg.norm((np.linalg.inv(eta)@HZ)@(np.linalg.inv(eta)@HZ) - np.eye(2*d)), 4))
# The point the note names: X = 0, Y = 1
M0, _ = anticomm(Zr, Id)
print("|{J0, I[Z]}| at X = 0, Y = 1:", np.linalg.norm(M0))
# A generic X = 0 point with Y != 1 (eta-compatible H = diag(g, g^-1), but Y != Y^-1)
a = rng.standard_normal((d, d)); Yg = a@a.T + d*Id
M1, H1 = anticomm(Zr, Yg)
print("|{J0, I[Z]}| at X = 0, generic Y:", round(np.linalg.norm(M1), 4),
      "; eta-compatible there:", np.allclose((np.linalg.inv(eta)@H1)@(np.linalg.inv(eta)@H1), np.eye(2*d)))
