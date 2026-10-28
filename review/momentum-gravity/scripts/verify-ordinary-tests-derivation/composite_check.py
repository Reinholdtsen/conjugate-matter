"""Independent checks of the composite-body claims O17, O18 (dispersions), O19 (Fermi gas), O20.

All derived from scratch.
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 25

print("=== O17: Gaussian gate averaged over Maxwellian internal velocities ===")
# <exp(-|V + w|^2/v*^2)>, w ~ N(0, s^2 I_3).  Reduce by isotropy: w = (rho, cos t) about V.
def avg_gauss_quad(V, s, vs):
    def inner(wm):
        # angular average of exp(-(V^2 + wm^2 + 2 V wm mu)/vs^2) over mu in [-1,1], done analytically:
        # (1/2) int exp(-2 V wm mu/vs^2) dmu = sinh(2 V wm/vs^2)/(2 V wm/vs^2)
        z = 2*V*wm/vs**2
        ang = mp.sinh(z)/z if z != 0 else mp.mpf(1)
        return mp.exp(-(V**2 + wm**2)/vs**2)*ang*4*mp.pi*wm**2*mp.exp(-wm**2/(2*s**2))/(2*mp.pi*s**2)**1.5
    return mp.quad(inner, [0, s, 3*s, 10*s, mp.inf])
def avg_gauss_formula(V, s, vs):
    return (1 + 2*s**2/vs**2)**(-1.5)*mp.exp(-V**2/(vs**2 + 2*s**2))
for V, s, vs in [(0, 1.0, 0.1), (0.5, 1.0, 1.0), (2.0, 0.3, 1.0), (30.0, 200.0, 120.0)]:
    q = avg_gauss_quad(mp.mpf(V), mp.mpf(s), mp.mpf(vs))
    f = avg_gauss_formula(mp.mpf(V), mp.mpf(s), mp.mpf(vs))
    print(f"  V={V:6.2f} s={s:6.1f} v*={vs:6.1f}: quadrature {mp.nstr(q, 12)}  formula {mp.nstr(f, 12)}")

print("  Lorentzian, V = 0, s >> v*: <1/(1 + w^2/v*^2)> vs (v*/s)^2 and vs (v*/s)^2 (1 - sqrt(pi/2) v*/s)")
for ratio in [10, 100, 1000]:
    s, vs = mp.mpf(ratio), mp.mpf(1)
    q = mp.quad(lambda wm: 4*mp.pi*wm**2*mp.exp(-wm**2/(2*s**2))/(2*mp.pi*s**2)**1.5/(1 + wm**2/vs**2),
                [0, vs, 10*vs, s, 5*s, mp.inf])
    print(f"    s/v* = {ratio}: <W> = {mp.nstr(q, 8)};  (v*/s)^2 = {mp.nstr((vs/s)**2, 8)};"
          f"  with first correction {mp.nstr((vs/s)**2*(1 - mp.sqrt(mp.pi/2)*vs/s), 8)}")

print()
print("=== O17: Earth-rotation relative speeds ===")
omega_E = 7.2921150e-5   # rad/s (dagger)
R_E = 6378.137           # km (dagger)
veq = omega_E*R_E
print(f"  equatorial surface speed {veq:.4f} km/s; max element-element relative speed {2*veq:.3f} km/s;"
      f" Moon (1.025 km/s) vs elements, coplanar extremes {1.025 - veq:.3f} - {1.025 + veq:.3f} km/s")
for lat in (35.7, 48.8):
    print(f"  lab at latitude {lat}: {veq*np.cos(np.radians(lat)):.3f} km/s relative to Earth's centre of mass")

print()
print("=== O18: classical 1D thermal dispersions sqrt(kT/m) at 300 K ===")
kB, amu = 1.380649e-23, 1.66053906660e-27
for el, A in [('Be', 9.0122), ('Al', 26.9815), ('Ti', 47.867), ('Pt', 195.084)]:
    print(f"  {el}: {np.sqrt(kB*300/(A*amu))/1e3:.3f} km/s")

print()
print("=== O19: Fermi-gas nucleon gate ===")
mN = 938.92  # MeV (dagger, mean nucleon mass)
for kF in (200.0, 250.0, 270.0):
    vrel = kF/np.sqrt(kF**2 + mN**2)*299792.458
    vnr = kF/mN*299792.458
    print(f"  k_F = {kF:.0f} MeV/c: v_F = {vrel:.0f} km/s (relativistic p/E); p/m = {vnr:.0f} km/s")
# exact pair average of a Gaussian gate exp(-w^2/v*^2) for v1, v2 uniform in a sphere of radius R:
# density of w = v1 - v2 is V_overlap(|w|)/V^2, V_overlap(d) = (pi/12)(4R + d)(2R - d)^2 for d < 2R
def pair_avg(x):   # x = v*/R
    R = mp.mpf(1)
    Vs = 4*mp.pi*R**3/3
    f = lambda d: mp.exp(-d**2/x**2)*4*mp.pi*d**2*(mp.pi/12)*(4*R + d)*(2*R - d)**2/Vs**2
    return mp.quad(f, [0, x, 5*x, 2*R])
for x in ['0.02', '0.05', '0.1']:
    xm = mp.mpf(x)
    lead = 3*mp.sqrt(mp.pi)/4*xm**3
    nxt = lead*(1 - 3/(2*mp.sqrt(mp.pi))*xm)
    print(f"  v*/v_F = {x}: exact {mp.nstr(pair_avg(xm), 8)};  leading (3 sqrt(pi)/4)x^3 = {mp.nstr(lead, 8)};"
          f"  with -(3/(2 sqrt(pi)))x correction {mp.nstr(nxt, 8)}")
print("  agent's MC: 1.6335e-4 +- 2.3e-6 (x = 0.05, 4 runs); 1.48e-5 +- 1.9e-6 (x = 0.02)")
vF = 250/np.sqrt(250**2 + mN**2)*299792.458
for vs in (0.1, 1.0, 10.0, 120.0, 1000.0):
    print(f"  v* = {vs:7.1f}: (3 sqrt(pi)/4)(v*/v_F)^3 = {3*np.sqrt(np.pi)/4*(vs/vF)**3:.3g}")
# MICROSCOPE 2-sigma |eta| with stat and syst in quadrature
eta2 = 1.5e-15 + 2*np.hypot(2.3e-15, 1.5e-15)
print(f"  MICROSCOPE |eta| 2-sigma (|central| + 2 sqrt(stat^2+syst^2)) = {eta2:.3g}")
for vs in (10.0, 120.0, 1000.0):
    Wv = 3*np.sqrt(np.pi)/4*(vs/vF)**3
    print(f"    v* = {vs}: best-case |eps| < {eta2/Wv:.2g}")
# residual dependence on the bodies' relative velocity V (sharp Fermi sphere): overlap is linear in |V|
print("  residual CM-velocity dependence for a sharp Fermi sphere: <W>(V)/<W>(0) - 1 ~ -(3/4)|V|/v_F:"
      f" Mars (24.1 km/s) {-(3/4)*24.1/vF:.2e}; double pulsar (625 km/s) {-(3/4)*625/vF:.2e}")

print()
print("=== O20: momentum-difference variant ===")
import sympy as sp
m1, m2, V, v = sp.symbols('m1 m2 V v')
M = m1 + m2
mu = m1*m2/M
v1 = V + m2/M*v
v2 = V - m1/M*v
print("  m1 v1 - m2 v2 - [(m1-m2)V + 2 mu v] =", sp.simplify(m1*v1 - m2*v2 - ((m1 - m2)*V + 2*mu*v)))
print("  in the CM frame (V = 0) the literal variant is 2 mu v, i.e. twice k = mu v")
keV = 1.602176634e-16   # J
pstar = 20*keV/299792458.0
for name, muv in [('nucleon pair', 938.92/2*1.78266192e-30), ('electron pair', 0.51099895/2*1.78266192e-30),
                  ('1 kg pair', 0.5), ('chi pair (m=70 MeV)', 35*1.78266192e-30)]:
    print(f"  {name}: p*/mu = {pstar/muv:.4g} m/s;  literal-variant width p*/(2 mu) = {pstar/(2*muv):.4g} m/s")
