# Independent checks of round-2 ordinary-tests claims O2 (EIH CM reduction), O14 (derived inputs),
# O15 (Cassini, Collett intervals), O16 (LLR synodic coefficient), O20 (momentum variant numbers).
import numpy as np
import sympy as sp

print("=== O2: EIH two-body interaction in the CM frame ===")
m1, m2, c, G, r = sp.symbols('m1 m2 c G r', positive=True)
vx, vy, nx, ny = sp.symbols('v_x v_y n_x n_y', real=True)
M = m1 + m2; nu = m1*m2/M**2
v = sp.Matrix([vx, vy]); n = sp.Matrix([nx, ny])
v1 = m2/M*v; v2 = -m1/M*v
# EIH 1PN Lagrangian interaction term (Landau-Lifshitz sec. 106 form, dagger):
#   (G m1 m2 / 2 r c^2) [3 (v1^2 + v2^2) - 7 v1.v2 - (n.v1)(n.v2)]
bracket = 3*(v1.dot(v1) + v2.dot(v2)) - 7*v1.dot(v2) - n.dot(v1)*n.dot(v2)
target = (3 + nu)*v.dot(v) + nu*n.dot(v)**2
print("  bracket in CM frame - [(3+nu) v^2 + nu (n.v)^2] =", sp.simplify(bracket - target))

print()
print("=== O14 derived inputs ===")
gLLR, sLLR = 398600.4354, 0.0005
for lab, g, s in [('Ries 1992', 398600.4356, 0.0004), ('Dunn 1999', 398600.4360, 0.0002)]:
    print(f"  GM_E(LLR) - GM_E({lab}) = {gLLR - g:+.4f} km3/s2 -> relative {(gLLR - g)/g:+.3e} +- {np.hypot(sLLR, s)/g:.3e}")
xE = 7.2/6.687 - 1; sE = 1.8/6.687
print(f"  Eros: M_fly/M_orb - 1 = {xE:+.4f} +- {sE:.4f}; 2 sigma |max| = {max(abs(xE - 2*sE), abs(xE + 2*sE)):.4f}")
GMeros = 6.674e-20*6.687e15
print(f"  Eros GM = {GMeros:.4e} km3/s2 ; circular speed at 35 km = {np.sqrt(GMeros/35.)*1e3:.2f} m/s")

print()
print("=== O15: light vs dynamical mass ===")
g, sg = 2.1e-5, 2.3e-5
lo, hi = g - 2*sg, g + 2*sg
print(f"  Cassini: gamma_fit - 1 = -2 eps K -> eps K in [{-hi/2:.3e}, {-lo/2:.3e}]")
gC, sC = 0.97, 0.09
print(f"  Collett: eps <K> = (1 - gamma)/2 in [{(1 - (gC + 2*sC))/2:.3f}, {(1 - (gC - 2*sC))/2:.3f}]")
# exact form (1+gamma_fit) GM_dyn = 2 GM_bare with GM_dyn = GM (1 + eps K): gamma_fit = 2/(1+eps K) - 1
for gam in [gC - 2*sC, gC + 2*sC]:
    print(f"    exact inversion at gamma = {gam:.2f}: eps K = {2/(1 + gam) - 1:+.4f}")

print()
print("=== O16: Sun-Moon gated term vs EIH cross term, coefficient ratio |W'(u_E)| c^2/(3 v_E v*) ===")
cl = 299792.458; vE = np.sqrt(132712440041.94/149.6e6)
print(f"  v_E (circular, a = 149.6e6 km) = {vE:.3f} km/s")
for vs in [30., 120., 1000.]:
    u = vE/vs; dW = 2*u*np.exp(-u**2)
    coef = dW*cl**2/(3*vE*vs)
    print(f"  Gaussian v* = {vs:6.0f}: ratio = {coef:.3e} eps -> |eps| < {1e-3/coef:.2e} if LLR fits the EIH cross term to 1e-3")

print()
print("=== O20: momentum-difference variant ===")
V1, V2, Vc, vrel = sp.symbols('V1 V2 V v', real=True)
Mt = m1 + m2; mu = m1*m2/Mt
vv1 = Vc + m2/Mt*vrel; vv2 = Vc - m1/Mt*vrel
print("  m1 v1 - m2 v2 - [(m1-m2) V + 2 mu v] =", sp.simplify(m1*vv1 - m2*vv2 - ((m1 - m2)*Vc + 2*mu*vrel)))
VCMB = 370.
GMs = 132712440041.94; GME = 398600.4354; EMRAT = 81.3005691
qE = GME/GMs                 # m_E/M_sun from DE430 GMs
qMa = 42828.37/GMs           # Mars GM (dagger)
def ratio(q, v):             # q = m2/m1 (light/heavy)
    mu_over_m1 = q/(1 + q)
    return 2*mu_over_m1*v/((1 - q)*VCMB)
print(f"  Sun-Earth : 2 mu v/((m1-m2) V) = {ratio(qE, 29.78):.3e}")
print(f"  Sun-Mars  : {ratio(qMa, 24.13):.3e}")
print(f"  Earth-Moon: {ratio(1/EMRAT, 1.0245):.3e}")
# v*_pair = p*/mu for p* = 20 keV/c
keV = 1.602176634e-16; cms = 299792458.
pstar = 20*keV/cms           # kg m/s
mN = 938.919e3*keV/cms**2; me = 510.99895*keV/cms**2
for lab, mu_ in [('nucleon pair (m_N/2)', mN/2), ('electron pair (m_e/2)', me/2), ('1 kg - 1 kg (0.5 kg)', 0.5),
                 ('Earth-Moon', 5.972e24/EMRAT/(1 + 1/EMRAT))]:
    print(f"  {lab:24s}: v*_pair = p*/mu = {pstar/mu_:.3e} m/s")
# notebook convention check: mu_fiber = m_chi v*/sqrt2 with m_chi = 70 MeV, v* = 120 km/s
print(f"  notebook: m_chi v*/sqrt2 = {70e3*120/299792.458/np.sqrt(2):.2f} keV ; chi-pair width p*/(m_chi/2) = "
      f"{20/35e3*299792.458:.1f} km/s = sqrt2 x {20/35e3*299792.458/np.sqrt(2):.1f} km/s")
