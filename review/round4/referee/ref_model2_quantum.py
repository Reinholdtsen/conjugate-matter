"""Referee check of Sec. 4 (model II restoration): structure of the one-loop tadpole with truncation N,
and exact phase decoupling."""
import sympy as sp
import numpy as np

# 1) one-loop mass shift of phi_00 from Tr((phi^+ phi)^2): second derivative wrt phi_00, conj(phi_00), Gaussian-averaged
Nn = 3
ph = sp.Matrix(Nn, Nn, lambda i, j: sp.Symbol(f'p{i}{j}'))
pc = sp.Matrix(Nn, Nn, lambda i, j: sp.Symbol(f'c{i}{j}'))   # independent conj variables
A = pc.T*ph   # phi^+ phi with phi^+_{ij} = conj(phi_ji)
quart = sp.expand((A*A).trace())
d2 = sp.expand(sp.diff(quart, sp.Symbol('p00'), sp.Symbol('c00')))
print("d^2 Tr((phi^+phi)^2)/d phi00 d conj(phi00) =", d2)
# Gaussian average: <p_ij c_kl> = delta_ik delta_jl G_ij ; set other fields' first moments to zero
G = {(i, j): sp.Symbol(f'G{i}{j}') for i in range(Nn) for j in range(Nn)}
avg = 0
for term in sp.Add.make_args(d2):
    coeff, rest = term.as_coeff_Mul()
    facs = sp.Mul.make_args(rest)
    ps = [f for f in facs if str(f).startswith('p')]
    cs = [f for f in facs if str(f).startswith('c')]
    if len(ps) == 1 and len(cs) == 1 and str(ps[0])[1:] == str(cs[0])[1:]:
        i, j = int(str(ps[0])[1]), int(str(ps[0])[2])
        avg += coeff*G[(i, j)]
    elif any(f.is_Pow for f in facs):
        for f in facs:
            if f.is_Pow:
                pass
        avg += 0
print("Gaussian average (N=3) =", sp.simplify(avg))

# 2) growth with truncation in the symmetric phase (K_ij = i+j+1+M^2, M^2 = 1)
print("\nT_0(N) = sum_k [G_0k + G_k0], G_ij = 1/(i+j+1+M^2), M^2=1:")
for N in (10, 100, 1000, 10000, 100000):
    k = np.arange(N)
    T = 2*np.sum(1.0/(k + 2.0))
    print(f"  N={N:6d}: T_0 = {T:.4f}   T_0 - 2 ln N = {T - 2*np.log(N):.4f}")

# 3) exact decoupling of every condensate phase: S invariant under independent diagonal U, V
rng = np.random.default_rng(5)
N = 10; m = np.arange(N); Kin = m[:, None] + m[None, :] + 1 - 4.0
def S(phi):
    A = phi.conj().T @ phi
    return np.sum(Kin*np.abs(phi)**2) + np.real(np.trace(A @ A))
phi = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
vals = [S(np.diag(np.exp(1j*rng.uniform(0, 6.3, N))) @ phi @ np.diag(np.exp(1j*rng.uniform(0, 6.3, N))).conj().T) for _ in range(5)]
print("\nS at 5 random independent diagonal U,V (N=10):", np.round(vals, 10))
