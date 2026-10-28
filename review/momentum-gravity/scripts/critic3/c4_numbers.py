"""Round-3 critic, check c4: small numbers used in the rulings and the final claims.

(a) Velocity-selection crossover 1/Lambda_g(r), r = sigma/v*, for the Gaussian gate.  Closed form used here:
    Lambda_g(r) = [2/(1 + 2 r^2 + sqrt(1 + 4 r^2))]^(3/2)   (inferred by the critic; anchored on values printed by
    the round-3 critic-numbers verifier, which did not state the formula: 1/Lambda_g(1) = phi^3 = 4.236068,
    Lambda_g(8.3333) = 1.4435026e-03).
(b) Margins: velocity-selected thresholds (verifier u2 / round-2 c5 printed values) over the allowed eps at
    v* = 120 km/s: Lyman-alpha in the record's Hamiltonian reading (critic check c1: 0.0570 matter / 0.1063 gas);
    Sgr in the Hamiltonian reading (dark-tests derivation verifier D14, order of magnitude: 0.20-0.37) and the
    loosest Sgr mapping (critic-numbers verifier U3: up to 2.46).
(c) Singular threshold of the Hamiltonian linear system: 1 + kappa B = 0, kappa = (eps/2) Omega_c(z), min B from c1.
(d) Velocity dependence of single X (massive spin 2, Fierz-Pauli) and graviton exchange between slow bodies:
    (3 gamma^2 - 1)/2 and 2 gamma^2 - 1 [T: textbook numerators; verified explicitly by the critic-theory verifier v1].
(e) Universal gated term on ordinary bodies, leading order u = v/v* -> 0: d(omega-dot)/omega-dot_GR = -(2/3)(c/v*)^2 eps
    (ordinary-tests O9, confirmed by the ordinary-tests numbers verifier); double-pulsar limit |d omega-dot/omega-dot|
    < 5.27e-5 (that verifier, from Kramer et al. 2021 [S there]).  Sanity check of the 3000 km/s end only.
(f) Continuous-spin threshold rho v r/(hbar c) = 1 (Schuster-Toro-Zhou 2023, eq. 129 [S, this session]).
(g) Gate-width conventions: exp(-v^2/v_a^2) equals the amplitude gate exp(-v^2/(2 v*^2)) for v_a = sqrt2 v*.
"""
import numpy as np

lam = lambda r: (2.0 / (1 + 2 * r**2 + np.sqrt(1 + 4 * r**2)))**1.5
phi = (1 + 5**0.5) / 2
print(f"(a) 1/Lambda_g(1) = {1/lam(1.0):.6f} (phi^3 = {phi**3:.6f}); Lambda_g(8.3333) = {lam(8.3333):.7e}; "
      f"1/Lambda_g(1.2917) = {1/lam(1.2917):.3f}; 1/Lambda_g(8.3333) = {1/lam(8.3333):.1f}")
rs = np.geomspace(1e-3, 10, 2001)
print(f"    min over r in [1e-3, 10] of 1/Lambda_g = {np.min(1/lam(rs)):.6f} (at r = {rs[np.argmin(1/lam(rs))]:.3g}); "
      f"monotone increasing: {bool(np.all(np.diff(1/lam(rs)) > 0))}")
lo, hi = 0.01, 1.0
for _ in range(100):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if 1 / lam(mid) < 4 / 3 else (lo, mid)
print(f"    1/Lambda_g = 4/3 at r = {0.5*(lo+hi):.5f}")

thr = {"MW, WKB no re-virialization, Q = pi^2/2 (u2: 28.07)": 28.07,
       "MW crossover 1/Lambda_g(1.2917)": 1 / lam(1.2917),
       "cluster crossover 1/Lambda_g(8.3333) (u2: 692.8)": 1 / lam(8.3333)}
bounds = {"Lya H-reading matter (c1)": 0.0570, "Lya H-reading gas (c1)": 0.1063,
          "Sgr H-reading, upper end (VDD D14)": 0.37, "Sgr loosest mapping (VCN U3)": 2.46}
print("(b) threshold / allowed eps at v* = 120 km/s")
for tn, tv in thr.items():
    print(f"    {tn}: " + "; ".join(f"{bn} {bv}: {tv/bv:.3g}" for bn, bv in bounds.items()))

minB = -1.0712
for z, oc in ((50, 0.8305), (10, 0.835), (3, 0.8143)):
    print(f"(c) z = {z}: Omega_c = {oc}: 1 + kappa B = 0 at eps = {2/(-minB)/oc:.3f}")

c = 299792.458
for v in (30.0, 100.0, 120.0, 600.0):
    b = v / c; g = 1 / np.sqrt(1 - b**2)
    print(f"(d) v = {v:6.1f} km/s: X (3g^2-1)/2 - 1 = {(3*g**2 - 1)/2 - 1:.3e} ; graviton 2g^2-1 - 1 = {2*g**2 - 1 - 1:.3e}")

for vs in (3000.0, 1000.0):
    print(f"(e) v* = {vs:.0f} km/s: leading-order (u -> 0) bound |eps| < 5.27e-5 * (3/2)(v*/c)^2 = {5.27e-5*1.5*(vs/c)**2:.3g}"
          "   [exact, ordinary-tests numbers verifier: 8.5-8.7e-9 Gaussian, 9.3-9.4e-9 Lorentzian at 3000; 2.15e-9 Gaussian at 1000]")

hbarc = 1.97327e-7   # eV m
kpc, au = 3.0856776e19, 1.495978707e11
for v, r, lab in ((120.0, kpc, "120 km/s at 1 kpc"), (120.0, 10 * kpc, "120 km/s at 10 kpc"), (29.78, au, "29.78 km/s at 1 au")):
    print(f"(f) rho v r/(hbar c) = 1 for {lab}: rho = {hbarc/(r*v/c):.3e} eV")
print(f"(g) v_a = sqrt2 v* = {2**0.5*120:.1f} km/s for v* = 120; ordinary-tests v_a = 120 km/s is v* = {120/2**0.5:.2f} km/s")
