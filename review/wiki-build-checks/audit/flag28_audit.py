"""Flag 28 audit (steelman lens): #11 §11.2 says
   "Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34".
Search every unit system / reading of e / Dirac integer n for one under which
the whole sentence is right as written.

Anchors are textbook identities, independent of the paper:
  * Gauss's law fixes where 4π sits: HL (rationalized) point source has field
    q r̂/(4π r²), Gaussian q r̂/r². Checked here by integrating the flux.
  * Dirac: the string's Aharonov–Bohm phase q·Φ/ħ must be 2πn (ħ = c = 1).
  * Coulomb strength between two unit sources = coupling: HL q²/4π, Gaussian q².
  * Unit-free consequence: α·α_m = n²/4 (Dirac 1931; g_D = e/(2α) ≈ 68.5 e is
    the textbook Gaussian figure, quoted here from model memory, †).
alpha: CODATA 2018 value from model memory (†); the repo uses 137.035999.
"""
from math import pi, sqrt, log, isclose
import numpy as np
import sympy as sp

ALPHA = 1 / 137.035999084

# ---------------------------------------------------------------- A. anchors
print("== A. Anchors (independent of the paper) ==")
th = np.linspace(0, pi, 2001)
ph = np.linspace(0, 2 * pi, 2001)
TH, PH = np.meshgrid(th, ph, indexing="ij")
R = 3.7  # arbitrary radius: flux must not depend on it
for system, Br in [("HL", lambda g, r: g / (4 * pi * r**2)),
                   ("Gaussian", lambda g, r: g / r**2)]:
    integrand = Br(1.0, R) * R**2 * np.sin(TH)
    flux = np.trapezoid(np.trapezoid(integrand, ph, axis=1), th)
    print(f"{system:8s}: flux of a unit monopole through a sphere = {flux:.6f}"
          f"  ({'1' if system == 'HL' else '4π = %.6f' % (4 * pi)} expected)")

q0_HL = sqrt(4 * pi * ALPHA)  # HL elementary charge: q0²/4π = α
q0_G = sqrt(ALPHA)            # Gaussian elementary charge: q0² = α
for n in (1, 2):
    g_HL = 2 * pi * n / q0_HL           # q0·Φ = q0·g = 2πn
    g_G = 2 * pi * n / (q0_G * 4 * pi)  # q0·Φ = q0·4πg = 2πn  ->  q0·g = n/2
    am_HL, am_G = g_HL**2 / (4 * pi), g_G**2
    print(f"n={n}: HL α_m = g²/4π = {am_HL:.3f};  Gaussian α_m = g² = {am_G:.3f};"
          f"  α·α_m = {ALPHA * am_HL:.6f} (n²/4 = {n * n / 4})")
print(f"textbook Dirac charge g_D/e = 1/(2α) = {1 / (2 * ALPHA):.2f}  († '68.5 e')")

# ---------------------------------------------------------- B. the readings
print("\n== B. Readings of 'e·g ~ 2π ... magnetic coupling near 4π/e² ≈ 34' ==")
# Each reading: (label, unit system, value of the symbol e, minimal magnetic charge g)
readings = [
    ("R1 HL, e = our elementary charge, Dirac minimum (n=1)", "HL", q0_HL, 2 * pi / q0_HL),
    ("R2 HL, e = our charge, n=2 (Zwanziger 4πZ / S-dual g_D = 4π/e)", "HL", q0_HL, 4 * pi / q0_HL),
    ("R3 HL, e = 2 x our charge (#14 v3's g_d; our charge = e/2)", "HL", 2 * q0_HL, 2 * pi / q0_HL),
    ("R4 HL, e = our charge, minimum vs quark charge e/3, no color flux", "HL", q0_HL, 6 * pi / q0_HL),
    ("G1 Gaussian, e = our charge (e² = α), Dirac minimum (eg = 1/2)", "G", q0_G, 0.5 / q0_G),
    ("G2 Gaussian, e = our charge, n=2 (eg = 1)", "G", q0_G, 1.0 / q0_G),
]
near34 = lambda x: abs(x / 34 - 1) < 0.10
hdr = f"{'reading':66s} {'4π/e²':>9s} {'α_m':>9s} {'e·g/π':>7s}  C1 C2 C3 C4 C4'"
print(hdr)
print("C1: 4π/e² ≈ 34   C2: α_m ≈ 34   C3: 4π/e² = α_m   C4: e·g = 2π   C4': e·g ∈ 2πZ")
survivors_strict, survivors_lenient = [], []
for label, sysm, e, g in readings:
    lit = 4 * pi / e**2
    am = g**2 / (4 * pi) if sysm == "HL" else g**2
    eg = e * g
    c1, c2, c3 = near34(lit), near34(am), isclose(lit, am, rel_tol=1e-9)
    c4 = isclose(eg, 2 * pi, rel_tol=1e-9)
    k = eg / (2 * pi)
    c4l = isclose(k, round(k), rel_tol=1e-9) and round(k) >= 1
    f = lambda b: " Y" if b else " n"
    print(f"{label:66s} {lit:9.3f} {am:9.3f} {eg / pi:7.3f} {f(c1)} {f(c2)} {f(c3)} {f(c4)} {f(c4l)}")
    if c1 and c2 and c3 and c4:
        survivors_strict.append(label[:2])
    if c1 and c2 and c3 and c4l:
        survivors_lenient.append(label[:2])
print(f"R1 ratio (4π/e²)/α_m = {(4 * pi / q0_HL**2) / ((2 * pi / q0_HL)**2 / (4 * pi)):.6f}")
print(f"all claims hold, strict 'e·g = 2π': {survivors_strict or 'none'}")
print(f"all claims hold, lenient 'e·g ∈ 2πZ': {survivors_lenient or 'none'}")

# --------------------------------------------- C. symbolic: condition vs formula
print("\n== C. Is 'e·g = 2π' compatible with 'magnetic coupling = 4π/e²' for ANY e? ==")
e, g = sp.symbols("e g", positive=True)
print("HL      (α_m = g²/4π, e·g = 2π):",
      sp.solve([sp.Eq(g**2 / (4 * sp.pi), 4 * sp.pi / e**2), sp.Eq(e * g, 2 * sp.pi)], [e, g], dict=True))
print("Gaussian(α_m = g²,    e·g = 1/2):",
      sp.solve([sp.Eq(g**2, 4 * sp.pi / e**2), sp.Eq(e * g, sp.Rational(1, 2))], [e, g], dict=True))
print("Gaussian(α_m = g²,    e·g = 2π literal):",
      sp.solve([sp.Eq(g**2, 4 * sp.pi / e**2), sp.Eq(e * g, 2 * sp.pi)], [e, g], dict=True))
print("HL: g implied by α_m = 4π/e² :", sp.solve(sp.Eq(g**2 / (4 * sp.pi), 4 * sp.pi / e**2), g),
      "-> e·g =", sp.simplify(e * sp.solve(sp.Eq(g**2 / (4 * sp.pi), 4 * sp.pi / e**2), g)[0]))
a = sp.symbols("alpha", positive=True)
esol = sp.solve(sp.Eq(4 * sp.pi / e**2, 1 / (4 * a)), e)
print("HL: e that makes 4π/e² = 1/(4α):", esol, " = 2·sqrt(4πα)?",
      sp.simplify(esol[0] - 2 * sp.sqrt(4 * sp.pi * a)) == 0)

# ------------------------------------------------------ D. running of α_em
print("\n== D. Can running bring 4π/e² = 1/α_em(μ) down to 34? (one loop, SM) ==")
# inputs from model memory (†): 1/α(M_Z) MSbar, M_Z, b_Y = 41/6, b_2 = -19/6
MZ, ainvMZ, bsum = 91.1876, 127.95, 41 / 6 - 19 / 6
ainv = lambda mu: ainvMZ - bsum / (2 * pi) * log(mu / MZ)
print(f"cross-check vs referee step2a (127.930 at M_Z): 1/α(1e12) = {127.930 - bsum / (2 * pi) * log(1e12 / MZ):.2f}  (printed 114.44)")
for mu in (1e11, 1e16):
    print(f"cross-check vs v3-worklog R2: 1/(4α({mu:.0e})) = {ainv(mu) / 4:.2f}")
for mu in (1e3, 1e12, 1e16, 1.22e19):
    print(f"μ = {mu:9.2e} GeV: 4π/e² = 1/α = {ainv(mu):7.2f};  π/e² = 1/(4α) = {ainv(mu) / 4:6.2f}")
print(f"below M_Z 1/α rises to {1 / ALPHA:.3f}; minimum of 4π/e² up to M_Pl = {ainv(1.22e19):.2f} (never ≈ 34)")
