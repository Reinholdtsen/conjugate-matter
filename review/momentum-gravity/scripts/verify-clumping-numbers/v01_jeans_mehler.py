"""Verifier v01: (a) stellar Jeans growth rate for a Maxwellian, two ways;
(b) the Gaussian-gate operator spectrum by brute-force 1D Nystrom, compared with
the Mehler closed form claimed by the clumping agent (C3).

Units: velocities in sigma, rates in sqrt(4 pi G rho) = 1/t_ff, k in k_J.
Independent anchors: (a) direct quadrature of Int p0(u) u^2/(u^2+g^2) du (no erfc
identity used) against the closed form; (b) numerical eigenvalues of a discretized
kernel, no Mehler formula used in the computation.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30

# ---------- (a) Jeans: kappa^2 = Int p0(u) u^2/(u^2 + (Gamma/kappa)^2) du ----------
def kappa2_quad(G, kap):
    g = mp.mpf(G) / kap          # Gamma/k in sigma units
    f = lambda u: mp.exp(-u**2 / 2) / mp.sqrt(2 * mp.pi) * u**2 / (u**2 + g**2)
    return mp.quad(f, [-mp.inf, 0, mp.inf])

def kappa2_closed(G, kap):
    xi = mp.mpf(G) / (mp.sqrt(2) * kap)
    return 1 - mp.sqrt(mp.pi) * xi * mp.exp(xi**2) * mp.erfc(xi)

for kap in [mp.mpf('0.5'), mp.mpf('0.01')]:
    G_q = mp.findroot(lambda G: kappa2_quad(G, kap) - kap**2, 0.7)
    G_c = mp.findroot(lambda G: kappa2_closed(G, kap) - kap**2, 0.7)
    print(f"Jeans kappa={float(kap)}: Gamma(quadrature)={mp.nstr(G_q, 12)}  Gamma(closed form)={mp.nstr(G_c, 12)}")

# ---------- (b) 1D Gaussian-gate kernel, brute force ----------
# K1(x,y) = p1(x)^1/2 exp(-r^2 (x-y)^2 / 2) p1(y)^1/2,  p1 = N(0,1)
def K1_eigs(r, n=1600, L=None):
    if L is None:
        L = 14.0
    x, h = np.linspace(-L, L, n, retstep=True)
    s = np.sqrt(h) * (2 * np.pi) ** -0.25 * np.exp(-x**2 / 4)
    K = s[:, None] * np.exp(-0.5 * r**2 * (x[:, None] - x[None, :]) ** 2) * s[None, :]
    ev = np.linalg.eigvalsh(K)[::-1]
    return ev

def closed(r):
    lam3 = (0.5 + r**2 + np.sqrt(1 + 4 * r**2) / 2) ** -1.5
    q = 2 * r**2 / (1 + 2 * r**2 + np.sqrt(1 + 4 * r**2))
    return lam3, q

print("\n r       | 1D Nystrom lam0^3   closed Lambda_g | q(Nystrom: lam1/lam0)  q(closed) | l=1: lam0^3 q, l=2: lam0^3 q^2 (Nystrom)")
for r in [0.25, 1.2917, 4.0, 8.333, 16.0, 32.0]:
    n = 1600 if r < 10 else 3000
    ev = K1_eigs(r, n=n)
    lam0, lam1 = ev[0], ev[1]
    qn = lam1 / lam0
    lam3, qc = closed(r)
    print(f" {r:7.4f} | {lam0**3:.7e}  {lam3:.7e} | {qn:.7f}  {qc:.7f} | {lam0**3*qn:.6e} {lam0**3*qn**2:.6e}")
    # check geometric progression of the 1D spectrum
    if r in (1.2917, 8.333):
        print("          1D ratios lam_{j+1}/lam_j, j=0..4:", np.round(ev[1:6] / ev[0:5], 7))
