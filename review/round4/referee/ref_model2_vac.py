"""Referee check of Model II (Sec. 3): real vs complex symmetry, vacua, flat phase, Delta(beta)."""
import numpy as np
from scipy.optimize import minimize
from scipy.special import eval_genlaguerre
import math

rng = np.random.default_rng(20261019)
N = 8
mu2, lam = 4.0, 1.0
m_idx = np.arange(N)
Kin = (m_idx[:, None] + m_idx[None, :] + 1 - mu2)
Pi = np.diag((-1.0)**m_idx)

def S_c(phi):
    A = phi.conj().T @ phi
    return float(np.sum(Kin*np.abs(phi)**2) + lam*np.real(np.trace(A @ A)))

def S_r(phi):  # real (Hermitian) model, same normalisation, quartic Tr phi^4
    return float(np.sum(Kin*np.abs(phi)**2) + lam*np.real(np.trace(np.linalg.matrix_power(phi, 4))))

print("== real vs complex")
Hm = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)); Hm = (Hm + Hm.conj().T)/2
psi = Pi @ Hm
print("  Pi phi Hermitian?", np.allclose(psi, psi.conj().T), " |Pi phi - (Pi phi)^+| =", np.linalg.norm(psi - psi.conj().T))
print("  Tr phi^4 =", np.trace(np.linalg.matrix_power(Hm, 4)).real, "  Tr (Pi phi)^4 =", np.trace(np.linalg.matrix_power(psi, 4)))
print("  Tr (psi psi^+)^2 =", np.trace((psi @ psi.conj().T) @ (psi @ psi.conj().T)).real)
Cm = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
U = np.diag(np.exp(1j*rng.uniform(0, 2*np.pi, N))); V = np.diag(np.exp(1j*rng.uniform(0, 2*np.pi, N)))
print("  complex: S[phi] =", S_c(Cm), " S[Pi phi] =", S_c(Pi @ Cm), " S[U phi V^+] =", S_c(U @ Cm @ V.conj().T))
Wn = np.linalg.qr(rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)))[0]
print("  complex, NON-diagonal unitary U: S[U phi] =", S_c(Wn @ Cm), "(not invariant, as expected)")

print("\n== real model: is phi -> Pi phi a symmetry on its own vacua?  Hessians at diag(a0, +a1) vs diag(a0, -a1)")
q = np.maximum(0, -(2*m_idx + 1 - mu2)/(2*lam))
def herm_basis(N):
    B = []
    for i in range(N):
        E = np.zeros((N, N), complex); E[i, i] = 1; B.append(E)
    for i in range(N):
        for j in range(i+1, N):
            E = np.zeros((N, N), complex); E[i, j] = E[j, i] = 1/np.sqrt(2); B.append(E)
            E = np.zeros((N, N), complex); E[i, j] = 1j/np.sqrt(2); E[j, i] = -1j/np.sqrt(2); B.append(E)
    return B
B = herm_basis(N)
def hessian(S, phi0, basis, h=1e-4):
    n = len(basis); Hs = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            f = lambda a, b: S(phi0 + a*basis[i] + b*basis[j])
            Hs[i, j] = Hs[j, i] = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h))/(4*h*h)
    return Hs
vplus = np.diag(np.sqrt(q)).astype(complex)
vminus = np.diag(np.sqrt(q)*np.array([1, -1] + [1]*(N-2))).astype(complex)
print("  S_r(v+) =", S_r(vplus), " S_r(v-) =", S_r(vminus))
ep = np.sort(np.linalg.eigvalsh(hessian(S_r, vplus, B)))
em = np.sort(np.linalg.eigvalsh(hessian(S_r, vminus, B)))
print("  lowest 6 Hessian eigenvalues at v+:", np.round(ep[:6], 4))
print("  lowest 6 Hessian eigenvalues at v-:", np.round(em[:6], 4))
pos = lambda e: e[e > 1e-6]
print("  sum log(positive eigenvalues): v+ %.6f  v- %.6f  -> one-loop free energies differ by %.6f"
      % (np.sum(np.log(pos(ep))), np.sum(np.log(pos(em))), 0.5*(np.sum(np.log(pos(ep))) - np.sum(np.log(pos(em))))))
print("  number of zero modes: v+ %d  v- %d" % (np.sum(np.abs(ep) < 1e-6), np.sum(np.abs(em) < 1e-6)))
# same test for the complex model: should be identical by symmetry
Bc = []
for i in range(N):
    for j in range(N):
        E = np.zeros((N, N), complex); E[i, j] = 1; Bc.append(E)
        E = np.zeros((N, N), complex); E[i, j] = 1j; Bc.append(E)
ecp = np.sort(np.linalg.eigvalsh(hessian(S_c, vplus, Bc)))
ecm = np.sort(np.linalg.eigvalsh(hessian(S_c, vminus, Bc)))
print("  complex model: max |eig(v+) - eig(v-)| =", np.max(np.abs(ecp - ecm)))

print("\n== complex vacua by gradient descent, N=%d, mu^2=4, lambda=1" % N)
def pack(z): return np.concatenate([z.real.ravel(), z.imag.ravel()])
def unpack(v): return (v[:N*N] + 1j*v[N*N:]).reshape(N, N)
def grad(v):
    phi = unpack(v)
    G = 2*Kin*phi + 4*lam*phi @ (phi.conj().T @ phi)
    return pack(G)
results = []
for s in range(6):
    z0 = (rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)))*0.7
    r = minimize(lambda v: S_c(unpack(v)), pack(z0), jac=grad, method='L-BFGS-B', options={'maxiter': 20000, 'gtol': 1e-12, 'ftol': 1e-15})
    phi = unpack(r.x)
    off = np.linalg.norm(phi - np.diag(np.diag(phi)))
    results.append((r.fun, off, np.round(np.abs(np.diag(phi))**2, 6)[:4], np.angle(phi[1, 1]) - np.angle(phi[0, 0])))
for k, (f, off, d, beta) in enumerate(results):
    print(f"  start {k}: S_min={f:.10f}  |offdiag|={off:.2e}  |phi_mm|^2={d}  beta={np.mod(beta, 2*np.pi):.4f}")
print("  q_m formula:", q[:4], "  S_min formula:", -np.sum(np.minimum(0, 2*m_idx+1-mu2)**2)/(4*lam))
# global-minimum check with many random restarts at smaller N
best = np.inf
for s in range(200):
    z0 = (rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)))*rng.uniform(0.1, 1.5)
    r = minimize(lambda v: S_c(unpack(v)), pack(z0), jac=grad, method='L-BFGS-B', options={'maxiter': 5000})
    best = min(best, r.fun)
print("  200 random restarts: lowest S found =", best)

print("\n== flat relative phase and duality action on beta")
for beta in np.linspace(0, 2*np.pi, 7):
    v = np.diag(np.sqrt(q)*np.exp(1j*np.array([0, beta] + [0]*(N-2))))
    vd = Pi @ v
    bd = np.angle(vd[1, 1]) - np.angle(vd[0, 0])
    print(f"  beta={beta:.4f}: S={S_c(v):.12f}   duality -> beta'={np.mod(bd, 2*np.pi):.4f} (beta+pi mod 2pi = {np.mod(beta+np.pi, 2*np.pi):.4f})")

print("\n== Delta(beta) = <x^2>_vac - <x^2>_dual on a grid; dual computed by direct 2D Fourier quadrature (theta=1)")
L, M = 7.0, 141
xs = np.linspace(-L, L, M); dx = xs[1]-xs[0]
X1, X2 = np.meshgrid(xs, xs, indexing='ij'); R2 = X1**2 + X2**2
f00 = 2*np.exp(-R2)
f11 = 2*(-1)*eval_genlaguerre(1, 0, 2*R2)*np.exp(-R2)
# D f(x) = (pi)^-1 int d2y exp(-i x~.y) f(y), x~ = 2 theta^-1 x, theta^-1 = [[0,-1],[1,0]] -> x~ = (-2 x2, 2 x1)
Y1, Y2 = X1.ravel(), X2.ravel()
def Dop(F):
    Fv = F.ravel()
    out = np.empty(M*M, complex)
    xt1, xt2 = -2*X2.ravel(), 2*X1.ravel()
    for chunk in range(0, M*M, 400):
        ph = np.exp(-1j*(np.outer(xt1[chunk:chunk+400], Y1) + np.outer(xt2[chunk:chunk+400], Y2)))
        out[chunk:chunk+400] = ph @ Fv * dx*dx/np.pi
    return out.reshape(M, M)
D00, D11 = Dop(f00), Dop(f11)
print("  max|D f00 - f00| =", np.max(np.abs(D00 - f00)), "  max|D f11 + f11| =", np.max(np.abs(D11 + f11)))
def moment(F): return np.sum(R2*np.abs(F)**2)/np.sum(np.abs(F)**2)
Ds = []
for beta in np.linspace(0, 2*np.pi, 9):
    F = np.sqrt(1.5)*f00 + np.sqrt(0.5)*np.exp(1j*beta)*f11
    DF = np.sqrt(1.5)*D00 + np.sqrt(0.5)*np.exp(1j*beta)*D11
    Ds.append((beta, moment(F) - moment(DF), moment(F), moment(DF)))
D0 = Ds[0][1]
for beta, d, mv, md in Ds:
    print(f"  beta={beta:.4f}: <x^2>_vac={mv:.6f} <x^2>_dual={md:.6f} Delta={d:+.6f}  Delta/Delta(0)={d/D0:+.6f}  cos(beta)={np.cos(beta):+.6f}")
# odd under duality: Delta[Pi phi] = -Delta[phi]
F = np.sqrt(1.5)*f00 + np.sqrt(0.5)*np.exp(0.7j)*f11
DF = Dop(F); DDF = Dop(DF)
print("  Delta[phi] =", moment(F) - moment(DF), "  Delta[D phi] =", moment(DF) - moment(DDF))
# exact Delta(0): (|phi|^2 - |Pi phi|^2) = 4 sqrt(1.5*0.5) cos(beta) f00 f11 ; normalised by int|phi|^2 = 2 pi (1.5+0.5)
num = np.sum(R2*4*np.sqrt(0.75)*f00*f11)*dx*dx; den = np.sum(np.abs(np.sqrt(1.5)*f00 + np.sqrt(0.5)*f11)**2)*dx*dx
print("  grid Delta(0) from cross term:", num/den, "  analytic 4 sqrt(0.75) pi / (4 pi) =", 4*np.sqrt(0.75)*np.pi/(4*np.pi))
