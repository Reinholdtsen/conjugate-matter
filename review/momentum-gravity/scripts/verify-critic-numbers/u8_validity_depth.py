"""verify-critic-numbers, c5-validity sensitivity: the validity limit gt < (1+r^2)^(5/2)/(X r^2) uses
X = G Psi_chi/sigma^2 = 9/2 (centre of a uniform core of radius 3/k_J).  Here: X for an isolated NFW halo
(isotropic Jeans, DM only) at several radii, and for the toy MW models of u7 at the Sun (chi-only potential
over the Jeans DM dispersion there).  Models only (dagger parameters)."""
import numpy as np

# NFW, units r_s = 1, 4 pi G rho_s r_s^2 = 1:  Phi(x) = -ln(1+x)/x ; rho = 1/(x(1+x)^2) ; g = M(x)/x^2
def sig2(x):
    xx = np.logspace(np.log10(x), np.log10(x) + 6, 20000)
    rho = 1 / (xx * (1 + xx) ** 2)
    M = np.log1p(xx) - xx / (1 + xx)
    return np.trapezoid(rho * M / xx**2, xx) * x * (1 + x) ** 2

print("isolated NFW (isotropic): X = |Phi(x)|/sigma^2(x)")
for x in (0.05, 0.1, 0.3, 1.0, 2.0):
    print(f"  x = r/r_s = {x:5.2f}: |Phi| = {np.log1p(x)/x:.4f}, sigma^2 = {sig2(x):.5f}, X = {np.log1p(x)/x/sig2(x):.2f}")

src = open("/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-critic-numbers/u7_sgr_bound.py").read()
ns = {}
exec(src[:src.index("x0 = np.array([17.5, 2.5, -6.5])")], ns)
Gk = ns['Gk']
for M in ns['models']:
    R0 = 8.2
    phi_nfw = Gk * 4 * np.pi * M.rho_s * M.rs**3 * np.log1p(R0 / M.rs) / R0
    s = M.sigma_dm(R0)
    print(f"MW toy model '{M.name}': G Psi_chi(R0) = {phi_nfw:.4g} (km/s)^2, sigma_DM(R0) = {s:.1f} km/s, X = {phi_nfw/s**2:.2f};"
          f" with sigma = 155: X = {phi_nfw/155**2:.2f}")
r = 155 / 120
for X in (4.5,):
    pass
print(f"validity limit at MW r = 155/120 for X = 4.5 / 5.0 / 6.0: " +
      ", ".join(f"{(1+r**2)**2.5/(X*r**2):.3f}" for X in (4.5, 5.0, 6.0)))
rc = 1000 / 120
print(f"validity limit at cluster r = 1000/120 for X = 4.5 / 8 / 12: " +
      ", ".join(f"{(1+rc**2)**2.5/(X*rc**2):.1f}" for X in (4.5, 8.0, 12.0)))
