"""Verifier v12: near-threshold slope of the purely growing rate, first-order perturbation theory.
K T(i g) phi = mu phi with T = v_z/(v_z - i g), g = Gamma/kappa.  For g -> 0+:
T - 1 -> i g P(1/v_z) - pi g delta(v_z); the odd part drops out for the even top mode, so
mu = Lambda_0 (1 - pi g F0),  F0 = int phi0(v_z=0, v_perp)^2 d^2 v_perp  (phi0 normalized).
Setting mu = kappa^2:  Gamma = sqrt(Lambda_0) (1 - kappa^2/Lambda_0) / (pi F0)  (kappa ~ sqrt(Lambda_0)).
Anchor: gt = 0 gives slope sqrt(2/pi) = 0.79788 (Jeans relation expanded near kappa = 1).
phi0 from the 3D Cartesian product of numerically diagonalized 1D gate kernels (as in v02)."""
import numpy as np

def slope(r, gt, L=12.0):
    n = int(max(401, 2 * L * r * 14)) | 1          # odd: grid point at 0
    x, h = np.linspace(-L, L, n, retstep=True)
    u1 = np.sqrt(h) * (2 * np.pi) ** -0.25 * np.exp(-x**2 / 4)
    K = u1[:, None] / np.sqrt(h) * np.exp(-0.5 * r**2 * (x[:, None] - x[None, :]) ** 2) * u1[None, :] / np.sqrt(h) * h
    lam, psi = np.linalg.eigh(K)
    idx = np.argsort(lam)[::-1]
    lam, psi = lam[idx], psi[:, idx]
    J = int(np.searchsorted(-lam / lam[0], -1e-9))
    ev = np.arange(0, J, 2)
    lam, psi = lam[ev], psi[:, ev]
    c = psi.T @ u1
    i0 = n // 2
    psi0 = psi[i0, :] / np.sqrt(h)                 # continuum value at x = 0
    L3 = lam[:, None, None] * lam[None, :, None] * lam[None, None, :]
    a3 = c[:, None, None] * c[None, :, None] * c[None, None, :]
    # top eigenvalue (Newton from the right)
    Lam = 1.0 + gt * L3.max()
    for _ in range(100):
        d = Lam - gt * L3
        f = np.sum(a3**2 / d) - 1
        fp = -np.sum(a3**2 / d**2)
        new = Lam - f / fp
        if new <= gt * L3.max():
            new = 0.5 * (Lam + gt * L3.max())
        if abs(new - Lam) < 1e-14 * Lam:
            Lam = new; break
        Lam = new
    phi = a3 / (Lam - gt * L3)                      # coefficients phi[n1,n2,n3]
    phi /= np.sqrt(np.sum(phi**2))
    # F0 = sum_{n1,n2} ( sum_{n3} phi[n1,n2,n3] psi_{n3}(0) )^2   (z = third index)
    proj = np.tensordot(phi, psi0, axes=([2], [0]))
    F0 = np.sum(proj**2)
    return Lam, F0, np.sqrt(Lam) / (np.pi * F0)

print(f"anchor gt=0: slope = {slope(1.0, 0.0)[2]:.5f} (sqrt(2/pi) = {np.sqrt(2/np.pi):.5f})")
for r, gt, label in [(1.2917, 10.0, "C2 MW gt=10 (agent: Gamma/(1-frac)=0.8779)"),
                     (155 / 120, 56.14, "MW gt=56.14"),
                     (1000 / 120, 1598.0, "C11 cluster gt=1598 (agent: 0.447)"),
                     (1000 / 120, 304.4, "cluster gt=304.4")]:
    Lam, F0, s = slope(r, gt)
    print(f"{label}: Lambda_0={Lam:.5f}, F0={F0:.5f}, slope sqrt(L0)/(pi F0) = {s:.4f}; "
          f"Gamma at kappa^2=0.999 L0: {s*0.001:.4e}, at 0.99 L0: {s*0.01:.4e}")
