"""Composition of the negative Hessian mode at (1, K_ref), coordinates (x, y, u, t) as in verify/toy_coset.py."""
import numpy as np
w = np.array([[0., 1.], [-1., 0.]]); Kref = np.diag([1., -1.])
def V_lam(H, K):
    I = np.linalg.inv(w) @ H; C = K @ I + I @ K
    return np.trace(np.linalg.inv(H) @ C.T @ H @ C)/8
def fields(cc):
    x, y, u, t = cc; Y = 1 + y
    H = np.array([[Y + x*x/Y, x/Y], [x/Y, 1/Y]]); a = np.sqrt(1 - u*u + t*t)
    return H, np.array([[a, u + t], [u - t, -a]])
def hess4(f, h=1e-4):
    e = np.eye(4); Hm = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            Hm[i, j] = (f(h*e[i] + h*e[j]) - f(h*e[i] - h*e[j]) - f(-h*e[i] + h*e[j]) + f(-h*e[i] - h*e[j]))/(4*h*h)
    return Hm
for lam in (1.0, 4.0, 10.0, 100.0):
    Hm = hess4(lambda cc: lam*V_lam(*fields(cc)) - np.trace(fields(cc)[1] @ Kref)**2)
    ev, vec = np.linalg.eigh(Hm); v = vec[:, 0]
    print(f"lam = {lam:5.1f}: lowest eigenvalue {ev[0]:8.4f}; eigenvector (x, y, u, t) = {np.round(v, 4)}; "
          f"weight in K's t-direction {v[3]**2:.3f}, in H's x-direction {v[0]**2:.3f}")
