import numpy as np
from math import pi
np.set_printoptions(precision=4, suppress=True)
w = np.array([[0., 1.], [-1., 0.]]); K0 = np.diag([1., -1.]); rho = w.copy()
def V_lam(H, K):
    I = np.linalg.inv(w) @ H; C = K @ I + I @ K
    return np.trace(np.linalg.inv(H) @ C.T @ H @ C)/8
def V_mu(K, Kref=K0):
    return -np.trace(K @ Kref)**2
def V_bounded(K, Kref=K0):
    return -np.trace(K @ Kref)**2/(2*np.trace(K.T @ K))
print("== F1: runaway along the boost family H = S^T S, K = S^-1 K0 S")
for t in (0.0, 1.0, 2.0, 4.0):
    S = np.array([[np.cosh(t), np.sinh(t)], [np.sinh(t), np.cosh(t)]])
    H = S.T @ S; K = np.linalg.inv(S) @ K0 @ S
    print(f"t={t}: V_lam = {V_lam(H, K):.2e}, V_mu = {V_mu(K):.4e}, V_bounded = {V_bounded(K):.4f}")
print("\n== F2: Hessian of V_lam + V_mu at (1, K0) in coords (x, y, u, t_) as in toy_coset")
def fields(c):
    x, y, u, tt = c
    Y = 1 + y; H = np.array([[Y + x**2/Y, x/Y], [x/Y, 1/Y]])
    a = np.sqrt(1 - u**2 + tt**2); K = np.array([[a, u + tt], [u - tt, -a]])
    return H, K
def hess(f, h=1e-4):
    n = 4; Hm = np.zeros((n, n)); e = np.eye(n)
    for i in range(n):
        for j in range(n):
            Hm[i, j] = (f(h*e[i] + h*e[j]) - f(h*e[i] - h*e[j]) - f(-h*e[i] + h*e[j]) + f(-h*e[i] - h*e[j]))/(4*h*h)
    return Hm
for lam in (1.0, 10.0, 100.0):
    f = lambda c: lam*V_lam(*fields(c)) + V_mu(fields(c)[1])
    print(f"lam={lam}: eigs of V_lam*lam + V_mu: {np.linalg.eigvalsh(hess(f))}")
fb = lambda c: V_lam(*fields(c)) + V_bounded(fields(c)[1])
print(f"bounded variant (lam=1): eigs {np.linalg.eigvalsh(hess(fb))}")
print("\n== F3: the twisted rho = rho o (K -> -K) fixes the vacuum (1, K0)?")
H1 = rho.T @ np.eye(2) @ rho; K1 = -(np.linalg.inv(rho) @ K0 @ rho)
print("H ->", H1.ravel(), " K ->", K1.ravel(), " fixed:", np.allclose(H1, np.eye(2)) and np.allclose(K1, K0))
print("\n== F5: I_K depends on the scale along the eigenlines (needs H)")
# W of a Gaussian state; I = int du (int dv W)^2 with xi = u e+ + v e-; rescale e+ -> s e+, e- -> e-/s
x = np.linspace(-9, 9, 721); dx = x[1] - x[0]
psi = np.exp(-(x - 1.3)**2/0.7) + 0.6*np.exp(-(x + 1.3)**2/0.7); psi /= np.sqrt(np.sum(psi**2)*dx)
rho_x = psi**2
for s in (1.0, 2.0):
    # density along L+ in the rescaled coordinate u' = u/s is s*rho(s u'), so I scales by s
    up = x; dens = s*np.interp(s*up, x, rho_x, left=0, right=0)
    print(f"scale s={s}: I = {np.sum(dens**2)*dx:.6f}")
print("\n== F4: real GW model, Hessians at diag(a0, +a1) vs diag(a0, -a1), N = 8, mu2 = 4, lam = 1")
N, MU2, LAM = 8, 4.0, 1.0
idx = np.add.outer(np.arange(N), np.arange(N)) + 1.0
def S_real(p):
    M = np.zeros((N, N), dtype=complex); iu = np.triu_indices(N, 1)
    M[np.diag_indices(N)] = p[:N]
    k = N; nn = len(iu[0])
    M[iu] = p[k:k+nn] + 1j*p[k+nn:k+2*nn]; M = M + np.triu(M, 1).conj().T
    return float(np.sum((idx - MU2)*np.abs(M)**2) + LAM*np.trace(np.linalg.matrix_power(M, 4)).real)
q = np.array([max(0, -(2*m + 1 - MU2)/(2*LAM)) for m in range(N)])
def full_hess(p0, h=1e-4):
    n = len(p0); Hm = np.zeros((n, n)); e = np.eye(n); f0 = S_real(p0)
    for i in range(n):
        for j in range(i, n):
            Hm[i, j] = Hm[j, i] = (S_real(p0 + h*e[i] + h*e[j]) - S_real(p0 + h*e[i] - h*e[j])
                                   - S_real(p0 - h*e[i] + h*e[j]) + S_real(p0 - h*e[i] - h*e[j]))/(4*h*h)
    return Hm
nparam = N + N*(N - 1)
res = {}
for sgn in (+1, -1):
    p0 = np.zeros(nparam); p0[0] = np.sqrt(q[0]); p0[1] = sgn*np.sqrt(q[1])
    ev = np.linalg.eigvalsh(full_hess(p0))
    res[sgn] = ev
    print(f"sign {sgn:+d}: S = {S_real(p0):.4f}, lowest eigs {ev[:4]}, min {ev.min():.4f}")
dF = 0.5*np.sum(np.log(res[+1])) - 0.5*np.sum(np.log(res[-1]))
print(f"one-loop free-energy difference F(+) - F(-) = {dF:.3f}  (eigenvalue-normalization dependent constants cancel)")
