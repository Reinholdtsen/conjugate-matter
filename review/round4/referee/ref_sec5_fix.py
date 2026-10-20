"""Combined map (psi -> F psi, K -> -K) check with a direct (non-FFT) unitary Fourier transform; finer rotation check."""
import numpy as np
x = np.linspace(-15, 15, 3001); dx = x[1]-x[0]
psi = np.exp(-(x-1.3)**2/0.7) + 0.6*np.exp(-(x+1.3)**2/0.7)
psi = psi/np.sqrt(np.sum(np.abs(psi)**2)*dx)
Fm = np.exp(-1j*np.outer(x, x))*dx/np.sqrt(2*np.pi)   # same grid for p
F1 = Fm @ psi; F2 = Fm @ F1
print("norm F psi:", np.sum(np.abs(F1)**2)*dx, "  max|F^2 psi(x) - psi(-x)| =", np.max(np.abs(F2 - psi[::-1])))
Ip = lambda f: np.sum(np.abs(f)**4)*dx
print(f"I_+K[psi] = {Ip(psi):.6f}   I_-K[psi] = {Ip(F1):.6f}")
print(f"combined map: I_-K[F psi] = int |F(F psi)|^4 = {Ip(F2):.6f}   I_+K[F psi] = {Ip(F1):.6f}")
print(f"K->-K alone: I_-K[psi] - I_+K[psi] = {Ip(F1)-Ip(psi):+.6f}  (nonzero: K->-K alone is not a symmetry of I)")
