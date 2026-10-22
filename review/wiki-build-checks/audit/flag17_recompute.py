"""Independent recomputation for flag 17 (gate conventions, a sqrt(2) in mu).

Sources (read in full):
  #1  notes/broken-born-theory.md  §3: M(k,q) = 4 pi alpha m/(q^2+m_phi^2) * exp(-k^2/mu^2), k = m v_rel/2
                                    §5.1: sigma_T = sigma_0 exp(-v^2/v*^2), v* = sqrt2 mu/m, mu = m v*/sqrt2 ~ 20 keV
  #6  notes/debt1a-ii-X-classification.md §4: "Wavepacket overlap of Gaussian profiles gives exactly
       exp(-(p1-p2)^2/2mu^2) -- the postulated gate, with mu = the chi quantum's own p-width"
  #13 papers/conjugate-special-relativity.md §4: "intrinsic momentum-space width mu ~ hbar/lambda_chi --
       precisely the gate scale ..., v* = sqrt2 mu/m_chi"
Anchors independent of the papers: two-body kinematics (reduced mass), the Gaussian product integral,
Born-approximation momentum-transfer cross-section.
"""
import sympy as sp
import numpy as np

print("=== 1. Kinematics: p1 - p2 versus k = m v_rel/2 (equal masses) ===")
m = sp.symbols('m', positive=True)
v1 = sp.Matrix(sp.symbols('v1x v1y v1z', real=True))
v2 = sp.Matrix(sp.symbols('v2x v2y v2z', real=True))
p1, p2 = m*v1, m*v2
vrel = v1 - v2
mred = m*m/(m+m)
k_vec = mred*vrel                       # textbook relative momentum = reduced mass x relative velocity
print("reduced mass m1 m2/(m1+m2) =", sp.simplify(mred), " -> k = m v_rel/2 as #1 states:",
      sp.simplify(k_vec - m*vrel/2) == sp.zeros(3, 1))
print("p1 - p2 - 2k =", sp.simplify(p1 - p2 - 2*k_vec).T, "(zero vector => |p1-p2| = 2k in every frame)")
# CM frame check: total momentum zero -> p1 = k, p2 = -k
P = p1 + p2
p1cm = p1 - P/2
print("CM-frame p1 equals k:", sp.simplify(p1cm - k_vec) == sp.zeros(3, 1))

print("\n=== 2. The two written gates as functions of k ===")
k, mu, mu1, mu6, v = sp.symbols('k mu mu1 mu6 v', positive=True)
G1 = sp.exp(-k**2/mu1**2)                 # #1 §3, amplitude-level
G6 = sp.exp(-(2*k)**2/(2*mu6**2))         # #6 §4 with p1 - p2 = 2k
print("#6 gate in terms of k:", sp.simplify(G6))
sol = sp.solve(sp.Eq(sp.log(G6), sp.log(G1)), mu6)
print("G6 == G1 for all k requires mu6 =", sol)
print("same mu: G6/G1 =", sp.simplify(G6.subs(mu6, mu)/G1.subs(mu1, mu)), "(not 1 => the formulas differ)")
print("same mu: G6 - G1^2 =", sp.simplify(G6.subs(mu6, mu) - G1.subs(mu1, mu)**2),
      "(zero => #6's displayed Gaussian is exactly the SQUARE of #1's gate)")

print("\n=== 3. Knee position: Born sigma_T with the full Yukawa propagator kept ===")
A, mphi, s = sp.symbols('A m_phi s', positive=True)
# q^2 = 2k^2(1 - cos th); with s = 1 - cos th in [0, 2], dOmega (1 - cos th) = 2 pi s ds
def sigmaT(gate_amp):
    M = A/(2*k**2*s + mphi**2)*gate_amp      # amplitude; the gate multiplies M as in #1 §3
    return sp.integrate(2*sp.pi*s*M**2, (s, 0, 2))
base = sp.simplify(sigmaT(1))
print("no-gate sigma_T(k) =", base)
print("  heavy-mediator limit k -> 0 of sigma_T*m_phi^4/A^2:", sp.limit(base*mphi**4/A**2, k, 0))
kb = 70e6*(120/299792.458)/2   # benchmark k = m v*/2 in eV, m_phi ~ m_chi = 70 MeV
ser = sp.series(sp.simplify(base*mphi**4/A**2), k, 0, 5).removeO()
print("  series of sigma_T*m_phi^4/A^2 in k:", sp.expand(ser))
rel = sp.simplify(1 - ser/(4*sp.pi))
print("  relative change of the no-gate sigma_T at the benchmark k = m v*/2 (m_phi = m_chi = 70 MeV):",
      sp.N(rel.subs({k: kb, mphi: 70e6})), "(negligible: the v-dependence of sigma_T is the gate's alone)")
# cross-check the series against the closed form at moderate k with 50-digit arithmetic
import mpmath as mp
mp.mp.dps = 50
f = sp.lambdify((k, mphi), base*mphi**4/A**2, 'mpmath')
for kk in (mp.mpf('0.1'), mp.mpf('1e-3')):
    print(f"    k/m_phi={float(kk):g}: closed form {mp.nstr(f(kk, mp.mpf(1)), 15)}  series {mp.nstr(sp.N(ser.subs({k: kk, mphi: 1}), 30), 15)}")
for label, g in [("#1 gate exp(-k^2/mu^2), amplitude level", sp.exp(-k**2/mu**2)),
                 ("#6 gate exp(-(p1-p2)^2/2mu^2), amplitude level", sp.exp(-(2*k)**2/(2*mu**2)))]:
    ratio = sp.simplify(sigmaT(g)/base)
    expo = sp.simplify(sp.log(ratio).subs(k, m*v/2))
    vstar = sp.simplify(sp.sqrt(-v**2/expo))
    print(f"{label}: sigma_T/sigma_T(no gate) = {ratio};  exponent in v = {sp.expand(expo)};  v* = {vstar}")
expo_rate = sp.expand(sp.simplify(sp.log(sp.exp(-(2*k)**2/(2*mu**2))).subs(k, m*v/2)))
print("#6 Gaussian read as the rate-level (sigma_T) factor: exponent =", expo_rate,
      "; v* =", sp.simplify(sp.sqrt(-v**2/expo_rate)))
print("#1's own sigma_T factor exp(-v^2/v*^2), v* = sqrt2 mu/m, equals exp(-(p1-p2)^2/2mu^2) with p1-p2 = m v:",
      sp.simplify(sp.exp(-v**2/(sp.sqrt(2)*mu/m)**2) - sp.exp(-(m*v)**2/(2*mu**2))) == 0)

print("\n=== 4. What Gaussian overlap gives, by width convention (symbolic; the 3D transverse integrals cancel in the ratio) ===")
pz = sp.symbols('p_z', real=True)
D = sp.symbols('Delta', positive=True)  # |p1 - p2|, along z; transverse Gaussian factors are D-independent and cancel
def overlap(c):
    """normalized overlap of profiles exp(-|p-p_i|^2/(c mu^2)) centred at 0 and Delta z-hat"""
    f1 = sp.exp(-pz**2/(c*mu**2))
    f2 = sp.exp(-(pz - D)**2/(c*mu**2))
    I = sp.integrate(f1*f2, (pz, -sp.oo, sp.oo), conds='none')
    return sp.simplify(I/I.subs(D, 0))
rows = [
    (1, "profile exp(-p^2/mu^2): mu = 1/e half-width of the overlapped profile"),
    (2, "profile exp(-p^2/2mu^2): mu = std of the overlapped profile (density), or 'oscillator width' of an amplitude"),
    (4, "amplitude exp(-p^2/4mu^2): mu = std of |psi|^2 (usual QM uncertainty), amplitude overlap <psi1|psi2>"),
]
for c, desc in rows:
    O = overlap(c)
    Ok = sp.simplify(O.subs(D, 2*k))
    print(f"c={c}: {desc}\n      overlap = {O} ;  in k: {Ok}"
          f" ;  equals #6's exp(-D^2/2mu^2)? {sp.simplify(O - sp.exp(-D**2/(2*mu**2))) == 0}"
          f" ;  equals #1's exp(-k^2/mu^2)? {sp.simplify(Ok - sp.exp(-k**2/mu**2)) == 0}")
# overlap probability |<psi1|psi2>|^2 for amplitude psi ~ exp(-p^2/2mu^2)
O2 = overlap(2)
print("|<psi1|psi2>|^2 with psi ~ exp(-p^2/2mu^2):", sp.simplify(O2**2),
      "; equals #6's displayed form?", sp.simplify(O2**2 - sp.exp(-D**2/(2*mu**2))) == 0)

print("\n=== 4b. Numerical cross-check of the Gaussian product identity (1D quadrature, anchor) ===")
x = np.linspace(-40, 40, 400001)
for c in (1, 2, 4):
    muv, Dv = 1.3, 2.1
    f1 = np.exp(-x**2/(c*muv**2)); f2 = np.exp(-(x - Dv)**2/(c*muv**2))
    num = np.trapezoid(f1*f2, x)/np.trapezoid(f1*f1, x)
    print(f"c={c}: quadrature {num:.12f}  vs exp(-D^2/(2 c mu^2)) = {np.exp(-Dv**2/(2*c*muv**2)):.12f}")

print("\n=== 5. Numbers that depend on the mu normalization ===")
c_kms = 299792.458
m_chi_eV, vstar_kms = 70e6, 120.0
beta = vstar_kms/c_kms
mu_1 = m_chi_eV*beta/np.sqrt(2)
mu_6 = m_chi_eV*beta
print(f"v*/c = {beta:.6e}")
print(f"#1 normalization (v* = sqrt2 mu/m): mu = m v*/sqrt2 = {mu_1/1e3:.2f} keV  (#1 §5.1 states ~20 keV)")
print(f"#6 normalization, amplitude reading (v* = mu/m): mu = m v* = {mu_6/1e3:.2f} keV  (stated nowhere)")
print(f"ratio = {mu_6/mu_1:.6f} (sqrt2 = {np.sqrt(2):.6f})")
for vv in (300.0, 1500.0):
    print(f"#1 sigma_T/m at {vv:.0f} km/s = 30*exp(-(v/v*)^2) = 30*exp(-{(vv/vstar_kms)**2:.2f}) = {30*np.exp(-(vv/vstar_kms)**2):.3e} cm^2/g"
          " (uses v* only; independent of the mu convention)")
