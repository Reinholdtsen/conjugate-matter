# Flag 17 audit (steelman lens): is the sqrt(2) between #6's and #1's gate a convention, and
# under which conventions are #6 §4 and #13 §4 right as written?
# Anchors are textbook Gaussian integrals and two-body kinematics, not the papers' own numbers.
import numpy as np
import sympy as sp

m, v, mu, x, D, c0 = sp.symbols('m v mu x Delta c0', positive=True)
v1, v2 = sp.symbols('v1 v2', real=True)

print("== 1. Kinematics (equal masses): p1 - p2 vs #1's k = m v_rel/2")
k_def = m * sp.Abs(v1 - v2) / 2
dp = m * (v1 - v2)
print("  (p1-p2)^2 - 4 k^2 =", sp.simplify(dp**2 - 4 * k_def**2))

print("== 2. The flag's literal comparison (both read as the amplitude-level gate, same mu)")
k = sp.Symbol('k', positive=True)
g6 = sp.exp(-(2 * k)**2 / (2 * mu**2))         # #6 §4 with p1-p2 = 2k
g1 = sp.exp(-k**2 / mu**2)                     # #1 §3
print("  #6 in k:", g6, "  #1:", g1)
print("  log(#6)/log(#1) =", sp.simplify(sp.log(g6) / sp.log(g1)))
mu6 = sp.Symbol('mu6', positive=True)
print("  #6 with mu6 = sqrt2*mu, divided by #1:",
      sp.simplify(g6.subs(mu, mu6).subs(mu6, sp.sqrt(2) * mu) / g1))

print("== 3. Rate-level identity: #1 §5.1's sigma_T factor, written in p1-p2, with #1's own mu")
vstar1 = sp.sqrt(2) * mu / m                   # #1 §5.1 definition
rate1 = sp.exp(-v**2 / vstar1**2)              # sigma_T/sigma_0 in #1 §5.1
sq_amp1 = (g1.subs(k, m * v / 2))**2           # |#1 gate|^2 at k = m v/2
form6 = sp.exp(-(m * v)**2 / (2 * mu**2))      # #6's expression at |p1-p2| = m v
print("  |#1 gate|^2 / #1 rate factor =", sp.simplify(sq_amp1 / rate1))
print("  #6 expression / #1 rate factor =", sp.simplify(form6 / rate1))

print("== 4. Overlap of two Gaussian fiber profiles, centres a separation Delta apart")
print("     result written exp(-c Delta^2/mu^2); #6 form is c = 1/2; #1 amplitude gate is c = 1/4 (k = Delta/2)")
conv = {
    "W1 amplitude exp(-x^2/2mu^2)  [mu = Gaussian std-parameter of psi; density std mu/sqrt2]": 2 * mu**2,
    "W2 amplitude exp(-x^2/4mu^2)  [density std = mu, i.e. Delta p = mu]                  ": 4 * mu**2,
    "W3 amplitude exp(-x^2/mu^2)   [mu = 1/e half-width of psi; density std mu/2]         ": mu**2,
}
def coeff(expr):
    # expr is exp(-c*Delta^2/mu^2) up to normalization; return c
    e = sp.simplify(sp.log(expr))
    return sp.simplify(-sp.diff(e, D, 2) * mu**2 / 2)
for name, a in conv.items():
    psi1 = sp.exp(-x**2 / a)
    psi2 = sp.exp(-(x - D)**2 / a)
    n_amp = sp.integrate(psi1 * psi1, (x, -sp.oo, sp.oo))
    O1 = sp.integrate(psi1 * psi2, (x, -sp.oo, sp.oo)) / n_amp
    O2 = O1**2
    n_den = sp.integrate(psi1**2 * psi1**2, (x, -sp.oo, sp.oo))
    O3 = sp.integrate(psi1**2 * psi2**2, (x, -sp.oo, sp.oo)) / n_den
    out = []
    for lab, O in (("O1 <psi1|psi2>", O1), ("O2 |<psi1|psi2>|^2", O2), ("O3 density overlap", O3)):
        c = coeff(O)
        tag = "= #6 form" if c == sp.Rational(1, 2) else ("= #1 gate" if c == sp.Rational(1, 4) else "")
        out.append(f"{lab}: c={c} {tag}")
    print("  " + name)
    for o in out:
        print("      " + o)

print("== 5. 3-D numerical check (W1, O1): exponent uses |Delta|^2 with c = 1/4")
muv = 1.3
Dvec = np.array([0.7, -0.4, 1.1])
g = np.linspace(-12, 12, 241)
X, Y, Z = np.meshgrid(g, g, g, indexing='ij')
dx = g[1] - g[0]
psi_a = np.exp(-(X**2 + Y**2 + Z**2) / (2 * muv**2))
psi_b = np.exp(-((X - Dvec[0])**2 + (Y - Dvec[1])**2 + (Z - Dvec[2])**2) / (2 * muv**2))
num = (psi_a * psi_b).sum() * dx**3 / ((psi_a * psi_a).sum() * dx**3)
print(f"  numeric overlap = {num:.10f}; exp(-|D|^2/(4 mu^2)) = {np.exp(-Dvec @ Dvec / (4 * muv**2)):.10f}")

print("== 6. v* implied by each reading (sigma_T ~ amplitude^2; v* = 1/e point of sigma_T)")
def vstar_from_rate(rate):
    e = sp.simplify(sp.log(rate))          # = -v^2/v*^2
    return sp.sqrt(sp.simplify(-v**2 / e))
print("  #6 form as AMPLITUDE gate: v* =", vstar_from_rate(form6**2))
print("  #6 form as RATE factor:    v* =", vstar_from_rate(form6))
print("  #1 gate as amplitude:      v* =", vstar_from_rate(sq_amp1))

print("== 7. #11 §8 notation: M ~ F(k^2/mu^2) and sigma_T = sigma0 F(v^2/v*^2), same F, Gaussian F(x)=exp(-a x)")
a, vs = sp.symbols('a v_s', positive=True)
F = lambda t: sp.exp(-a * t)
eq = sp.Eq(sp.log(F((m * v / 2)**2 / mu**2)**2), sp.log(F(v**2 / vs**2)))
print("  solve |F(k^2/mu^2)|^2 = F(v^2/v*^2) for v*:", sp.solve(eq, vs), " (independent of a)")

print("== 8. Same physical profile, two names for its width")
vst = sp.Symbol('v_star', positive=True)
pW1 = sp.exp(-x**2 / (2 * (m * vst / sp.sqrt(2))**2))   # #1 naming: mu1 = m v*/sqrt2, W1 profile
pW3 = sp.exp(-x**2 / (m * vst)**2)                      # #6 amplitude naming: mu6 = m v*, W3 profile
print("  W1(mu1 = m v*/sqrt2) / W3(mu6 = m v*) =", sp.simplify(pW1 / pW3))

print("== 9. Benchmark (#1 §5.1): m_chi = 70 MeV, v* = 120 km/s")
c_kms = 299792.458
m_keV = 70e3
b = 120 / c_kms
print(f"  #1 convention mu = m v*/sqrt2 = {m_keV * b / np.sqrt(2):.2f} keV (source states ~20 keV)")
print(f"  #6-amplitude convention mu = m v* = {m_keV * b:.2f} keV (stated nowhere)")
