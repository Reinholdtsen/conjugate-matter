"""Upper bounds on eps(v*) for V = -(G m1 m2/r)[1 + eps W(|v1-v2|/v*)], body-level (CM) velocities.

Formulas (derived and checked in two_body.py):
  Kepler constant, circular orbit:  omega^2 r^3 = GM [1 + eps K(u)],  K = W - u W',  u = v/v*
  apsidal advance per orbit (first order in eps, exact in e):
      d_omega = 2 pi eps sqrt(1-e^2)/e dPhi/de,
      Phi = (1/2pi) int_0^2pi W(u_c sqrt((1+e cosE)/(1-e cosE))) dE,  u_c = sqrt(GM/a)/v*

Inputs (all live-searched this session; see the claims list for sources):
  GM_sun, GM_EM, GM_E (LLR-derived), GM_E (SLR, Ries 1992; Dunn 1999)  -- DE430 lunar memo, Table 3 and text
  planetary a, P, e, masses                                            -- NASA Planetary Fact Sheet (2025)
  supplementary perihelion precessions (EPM2011)                       -- Pitjev & Pitjeva 2013 via Iorio 2013 Table 1
  Kepler third-law eta_p (one-sided 2 sigma)                           -- Talmadge et al. 1988 via Will 1998 Table 4
  Cassini gamma-1 = (2.1 +- 2.3)e-5                                    -- Bertotti, Iess, Tortora 2003
  LLR anomalous perigee precession, 2 sigma < 270 muas/yr              -- Adelberger, Heckel, Nelson 2003 sec. 4.5
  LAGEOS a = 12270 km                                                   -- ILRS / literature
  double pulsar Pb, e, omega-dot, M, Pb-dot test                       -- Kramer et al. 2021
  Eros flyby mass (7.2 +- 1.8)e15 kg at 965 m/s; orbit mass 6.69e15 kg -- NEAR results (see claims)
"""
import numpy as np

RAD2MAS = 180 / np.pi * 3600e3
RAD2MUAS = RAD2MAS * 1e3


def W_of(shape):
    if shape == 'gauss':
        return (lambda x: np.exp(-x * x), lambda x: -2 * x * np.exp(-x * x))
    return (lambda x: 1 / (1 + x * x), lambda x: -2 * x / (1 + x * x)**2)


def K_of(u, shape):
    W, W1 = W_of(shape)
    return W(u) - u * W1(u)


def dom(uc, ecc, shape, n=8192):
    """precession per orbit per unit eps (rad), exact in e."""
    W, W1 = W_of(shape)
    Eg = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = ecc * np.cos(Eg)
    s = np.sqrt((1 + x) / (1 - x))
    ds = np.cos(Eg) / (s * (1 - x)**2)
    with np.errstate(over='ignore', under='ignore'):
        dPhi = np.mean(W1(uc * s) * uc * ds)
    return 2 * np.pi * np.sqrt(1 - ecc**2) / ecc * dPhi


def two_sided(x, sig, nsig=2.0):
    return max(abs(x - nsig * sig), abs(x + nsig * sig))


# ---------------------------------------------------------------- inputs
GM_SUN = 132712440041.94          # km^3/s^2 (DE430)
planets = {  # a [1e6 km], P [d], e, mass [1e24 kg] (NASA fact sheet)
    'Mercury': (57.9, 88.0, 0.206, 0.330),
    'Venus': (108.2, 224.7, 0.007, 4.87),
    'Earth': (149.6, 365.2, 0.017, 5.97),
    'Mars': (228.0, 687.0, 0.094, 0.642),
    'Jupiter': (778.5, 4331, 0.049, 1898),
    'Saturn': (1432.0, 10747, 0.052, 568),
}
# supplementary perihelion precessions, mas/cy (EPM2011)
dvarpi = {'Mercury': (-2.0, 3.0), 'Venus': (2.6, 1.6), 'Earth': (0.19, 0.19),
          'Mars': (-0.020, 0.037), 'Jupiter': (58.7, 28.3), 'Saturn': (-0.32, 0.47)}
# Talmadge et al. 1988 eta_p one-sided 2-sigma bounds, 1+eta_p = (mu_p/mu_earth)^(1/3)
eta_p = {'Mercury': 1.4e-8, 'Venus': 1.5e-9, 'Mars': -6.5e-10, 'Jupiter': -6e-8}
GAMMA, SGAMMA = 2.1e-5, 2.3e-5
LLR_PERIGEE_2SIG_MUAS = 270.0
GM_EM = 403503.2355               # km^3/s^2 (DE430, LLR fit)
A_MOON, P_MOON, E_MOON = 0.384e6, 27.3, 0.055
GM_E_LLR, S_LLR = 398600.4354, 0.0005
GM_E_RIES, S_RIES = 398600.4356, 0.0004
GM_E_DUNN, S_DUNN = 398600.4360, 0.0002
A_LAGEOS = 12270.0
# double pulsar
PB_DAYS, E_DP, OMDOT_DEGYR, M_DP = 0.1022515592973, 0.087777023, 16.899323, 2.587052
PBDOT_TEST_95 = 1.3e-4          # Pb-dot(GW) obs/GR agreement at 95%
# Eros
M_EROS_FLY, S_EROS_FLY, V_EROS_FLY = 7.2e15, 1.8e15, 0.965   # kg, kg, km/s
M_EROS_ORB = 6.69e15
R_EROS_ORB = 35.0  # km circular orbit radius used for the gravity field

# ---------------------------------------------------------------- derived system speeds
vc = {p: np.sqrt(GM_SUN / (a * 1e6)) for p, (a, P, e, m) in planets.items()}
v_moon = np.sqrt(GM_EM / A_MOON)
v_lageos = np.sqrt(GM_E_LLR / A_LAGEOS)
G_KM = 6.6743e-20  # km^3 kg^-1 s^-2 (CODATA 2018, only to convert Eros mass to an orbital speed)
v_eros_orb = np.sqrt(G_KM * M_EROS_ORB / R_EROS_ORB)
GM_DP = M_DP * GM_SUN
PB_S = PB_DAYS * 86400
v_dp = (2 * np.pi * GM_DP / PB_S)**(1 / 3)
om_orbit_dp = np.radians(OMDOT_DEGYR) * PB_DAYS / 365.25   # GR periastron advance per orbit (observed), rad

print("Relative orbital speeds used (km/s):")
for p in planets:
    print(f"  Sun-{p:8s} v_c = {vc[p]:8.3f}")
print(f"  Earth-Moon       v_c = {v_moon:8.4f}   (e = {E_MOON})")
print(f"  Earth-LAGEOS     v_c = {v_lageos:8.4f}")
print(f"  double pulsar    v_c = {v_dp:8.2f}   (e = {E_DP}); observed advance per orbit = {om_orbit_dp:.4e} rad")
print(f"  Eros orbit (35 km) v = {v_eros_orb*1e3:.2f} m/s ; NEAR flyby v = {V_EROS_FLY} km/s")
print(f"  orbits per century: " + ", ".join(f"{p} {36525/planets[p][1]:.2f}" for p in planets) +
      f"; lunar orbits per year {365.25/P_MOON:.3f}")

# ---------------------------------------------------------------- individual bounds


def bound_planet_prec(vstar, shape, planet):
    a, P, e, m = planets[planet]
    rate = dom(vc[planet] / vstar, e, shape) * 36525 / P * RAD2MAS   # mas/cy per unit eps
    x, s = dvarpi[planet]
    return two_sided(x, s) / abs(rate) if rate != 0 else np.inf, rate


def bound_kepler(vstar, shape, planet):
    dK = K_of(vc[planet] / vstar, shape) - K_of(vc['Earth'] / vstar, shape)
    return 3 * abs(eta_p[planet]) / abs(dK) if dK != 0 else np.inf


def bound_cassini(vstar, shape):
    # photons outside the gate (W(c/v*) ~ 0): 1+gamma_eff = 2/(1+eps K_earth)  ->  eps K = -(gamma-1)/2
    lo, hi = -(GAMMA + 2 * SGAMMA) / 2, -(GAMMA - 2 * SGAMMA) / 2
    K = K_of(vc['Earth'] / vstar, shape)
    return max(abs(lo), abs(hi)) / K if K > 0 else np.inf


def bound_llr_prec(vstar, shape):
    rate = dom(v_moon / vstar, E_MOON, shape) * 365.25 / P_MOON * RAD2MUAS   # muas/yr per unit eps
    return LLR_PERIGEE_2SIG_MUAS / abs(rate) if rate != 0 else np.inf, rate


def bound_llr_slr(vstar, shape, which='ries'):
    gm_s, s_s = (GM_E_RIES, S_RIES) if which == 'ries' else (GM_E_DUNN, S_DUNN)
    d = (GM_E_LLR - gm_s) / GM_E_LLR
    s = np.hypot(S_LLR, s_s) / GM_E_LLR
    dK = K_of(v_moon / vstar, shape) - K_of(v_lageos / vstar, shape)
    return two_sided(d, s) / abs(dK) if dK != 0 else np.inf


def bound_double_pulsar(vstar, shape):
    # eps-advance would bias the masses inferred from omega-dot: dM/M = 1.5 d(omdot)/omdot,
    # and the GR prediction of Pb-dot (prop. to M^(5/3) at fixed mass ratio) by 2.5 d(omdot)/omdot.
    frac = dom(v_dp / vstar, E_DP, shape) / om_orbit_dp
    return (PBDOT_TEST_95 / 2.5) / abs(frac) if frac != 0 else np.inf


def bound_eros(vstar, shape):
    W, _ = W_of(shape)
    # flyby: v ~ const = 0.965 km/s along the hyperbola -> GM_fly = GM (1 + eps W(v/v*)); orbit: GM (1 + eps K)
    r = M_EROS_FLY / M_EROS_ORB
    sr = S_EROS_FLY / M_EROS_ORB
    dW = W(V_EROS_FLY / vstar) - K_of(v_eros_orb / vstar, shape)
    return two_sided(r - 1, sr) / abs(dW) if dW != 0 else np.inf


def all_bounds(vstar, shape):
    b = {}
    for p in planets:
        b[f'prec {p}'] = bound_planet_prec(vstar, shape, p)[0]
    for p in eta_p:
        b[f'Kepler {p}/Earth'] = bound_kepler(vstar, shape, p)
    b['Cassini (light vs planets)'] = bound_cassini(vstar, shape)
    b['LLR perigee'] = bound_llr_prec(vstar, shape)[0]
    b['GM_E: LLR vs SLR(Ries)'] = bound_llr_slr(vstar, shape, 'ries')
    b['GM_E: LLR vs SLR(Dunn)'] = bound_llr_slr(vstar, shape, 'dunn')
    b['double pulsar'] = bound_double_pulsar(vstar, shape)
    b['Eros flyby vs orbit'] = bound_eros(vstar, shape)
    return b


VSTARS = [0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 120.0, 300.0, 1000.0, 3000.0]
for shape in ['gauss', 'lorentz']:
    print()
    print("=" * 100)
    print(f"Body-level gate, W = {'exp(-u^2)' if shape == 'gauss' else '1/(1+u^2)'}: upper bounds on |eps| (2 sigma)")
    print("=" * 100)
    for vstar in VSTARS:
        b = all_bounds(vstar, shape)
        best = min(b, key=b.get)
        top = sorted(b.items(), key=lambda kv: kv[1])[:4]
        print(f"v* = {vstar:7.1f} km/s : strongest = {best:28s} |eps| < {b[best]:.2e} ; next: " +
              "; ".join(f"{k} {v:.1e}" for k, v in top[1:]))

# ---------------------------------------------------------------- rate tables at the requested v*
print()
print("Per-unit-eps signals at the requested v* (for transparency)")
for shape in ['gauss', 'lorentz']:
    for vstar in [0.1, 1.0, 10.0, 120.0, 1000.0]:
        rates = {p: bound_planet_prec(vstar, shape, p)[1] for p in planets}
        llr = bound_llr_prec(vstar, shape)[1]
        print(f"  {shape:7s} v*={vstar:7.1f}: planet advance [mas/cy per eps]: " +
              ", ".join(f"{p} {r:.2e}" for p, r in rates.items()) + f" ; Moon [muas/yr per eps] {llr:.2e}")

# ---------------------------------------------------------------- fine scan: weakest point of the envelope
print()
print("Envelope scan (strongest bound at each v*), 400 log-spaced points 0.1-3000 km/s")
for shape in ['gauss', 'lorentz']:
    grid = np.logspace(-1, np.log10(3000), 400)
    env = []
    who = []
    for vs_ in grid:
        b = all_bounds(vs_, shape)
        k_ = min(b, key=b.get)
        env.append(b[k_])
        who.append(k_)
    env = np.array(env)
    for lo, hi in [(0.1, 0.5), (0.5, 3), (3, 300), (300, 3000)]:
        m = (grid >= lo) & (grid <= hi)
        i = np.argmax(np.where(m, env, -np.inf))
        j = np.argmin(np.where(m, env, np.inf))
        print(f"  {shape:7s} v* in [{lo},{hi}] km/s: weakest |eps| < {env[i]:.2e} at v* = {grid[i]:.3g} ({who[i]}); "
              f"strongest {env[j]:.2e} at v* = {grid[j]:.3g} ({who[j]})")

# ---------------------------------------------------------------- u<<1 regime: equivalence with a 1PN-like term
print()
print("u << 1 limit: eps-advance / GR advance = -(2/3) eps (c/v*)^2 for every system (both ~ v^2):")
c = 299792.458
for p in ['Mercury', 'Earth', 'Mars']:
    a, P, e, m = planets[p]
    gr = 6 * np.pi * GM_SUN / (c**2 * a * 1e6 * (1 - e**2))
    for vstar in [3000.0, 30000.0]:
        ratio = dom(vc[p] / vstar, e, 'gauss') / gr
        print(f"  {p:8s} v*={vstar:8.0f}: d_omega(eps=1)/GR = {ratio:.4e} ; -(2/3)(c/v*)^2 = {-(2/3)*(c/vstar)**2:.4e}")
