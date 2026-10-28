"""Verifier v14: analytic first-order anchor for the gate-only m = +-1 purely growing mode.
Within the m=1 sector (no gravity), the top static state is l=1, m=1 (P_z-even), eigenvalue
mu1 = gt Lambda_g q. Its normalized symmetric eigenfunction is psi0(z) [psi1(x) psi0(y) + i psi0(x) psi1(y)]/sqrt2
with Mehler 1D functions of Gaussian parameter c = sqrt(1+4r^2)/4, so F0 = int |phi(z=0)|^2 d^2v_perp = psi0(0)^2
= sqrt(2c/pi). First order (as in v12): Gamma = kappa (1 - kappa^2/mu1)/(pi F0).
Compared with the generator-eigenvalue results of v08 (m=1): gt=283 -> 0.01041, gt=290 -> 0.06187,
gt=320 -> 0.25937 at kappa^2=2 pi^2; gt=56.14, kappa^2=3 -> 0.19882."""
import numpy as np
r = 155 / 120
Lg = (0.5 + r * r + np.sqrt(1 + 4 * r * r) / 2) ** -1.5
q = 2 * r * r / (1 + 2 * r * r + np.sqrt(1 + 4 * r * r))
c = np.sqrt(1 + 4 * r * r) / 4
F0 = np.sqrt(2 * c / np.pi)
# numerical check of psi0(0)^2 via a grid eigenvector of the 1D kernel
x, h = np.linspace(-12, 12, 1201, retstep=True)
u1 = np.sqrt(h) * (2 * np.pi) ** -0.25 * np.exp(-x**2 / 4)
K = u1[:, None] / np.sqrt(h) * np.exp(-0.5 * r**2 * (x[:, None] - x[None, :]) ** 2) * u1[None, :] / np.sqrt(h) * h
lam, psi = np.linalg.eigh(K)
p0 = psi[:, -1] / np.sqrt(h)
print(f"Lambda_g q = {Lg*q:.6f}; F0 analytic sqrt(2c/pi) = {F0:.5f}; numerical psi0(0)^2 = {p0[600]**2:.5f}")
for kap2, gt, lm in [(2 * np.pi**2, 283.0, 0.01041), (2 * np.pi**2, 290.0, 0.06187), (2 * np.pi**2, 320.0, 0.25937), (3.0, 56.14, 0.19882)]:
    mu1 = gt * Lg * q
    G1 = np.sqrt(kap2) * (1 - kap2 / mu1) / (np.pi * F0)
    print(f"kappa^2={kap2:.4f} gt={gt}: mu1={mu1:.4f}, first-order Gamma={G1:.5f}, L-matrix (v08) = {lm}")
