"""Independent recomputation of the centre-of-mass-gating bounds (claims O9-O14, O23).

Written from scratch (the agent's scripts were not read first). Observational inputs are the
agent's sourced values, taken as given (this script checks the derivation and arithmetic, not
the citations). Orbital elements are standard values from memory (dagger), NASA fact-sheet style.
Bound rule (the agent's): |eps| < max(|x - 2 sig|, |x + 2 sig|) / |signal per unit eps|.
"""
import numpy as np

C = 299792.458              # km/s
GM_SUN = 132712440041.94    # km^3/s^2 (agent, DE430 [S])
GM_EM = 403503.2355         # km^3/s^2 (agent, DE430 [S])
MAS = 180/np.pi*3600e3      # mas per rad
DAY = 86400.0

# dagger: a [km], e, sidereal period [d]
PLANETS = {
    'Mercury': (57.909e6, 0.2056, 87.969),
    'Venus':   (108.210e6, 0.0068, 224.701),
    'Earth':   (149.598e6, 0.0167, 365.256),
    'Mars':    (227.956e6, 0.0935, 686.980),
    'Jupiter': (778.479e6, 0.0487, 4332.589),
    'Saturn':  (1432.041e6, 0.0520, 10759.22),
}
# agent's EPM2011 supplementary perihelion precessions [mas/cy], (value, sigma) [S via Iorio 2013]
EPM = {'Mercury': (-2.0, 3.0), 'Venus': (2.6, 1.6), 'Earth': (0.19, 0.19), 'Mars': (-0.020, 0.037),
       'Jupiter': (58.7, 28.3), 'Saturn': (-0.32, 0.47)}
MOON = (384400.0, 0.0549, 27.3217)      # dagger
LLR_PERIGEE_2SIG = 270.0                 # micro-arcsec/yr, agent [S] (Adelberger et al. 2003)
# double pulsar (agent [S], Kramer et al. 2021)
DP_PB = 0.10225156248     # d
DP_E = 0.0877775
DP_M = 1.338185 + 1.248868  # Msun (dagger: Kramer 2021 masses from memory)
DP_OMDOT = 16.899323        # deg/yr
DP_PBDOT_95 = 1.3e-4
LAGEOS_A = 12270.0          # km (agent [S])

N_E = 4096
Egrid = (np.arange(N_E) + 0.5)*2*np.pi/N_E


def Wfun(shape, x):
    return np.exp(-x**2) if shape == 'gauss' else 1/(1 + x**2)


def Wp(shape, x):
    return -2*x*np.exp(-x**2) if shape == 'gauss' else -2*x/(1 + x**2)**2


def K(shape, uu):
    return Wfun(shape, uu) - uu*Wp(shape, uu)


def adv_per_orbit(shape, uc, e):
    """first-order apsidal advance per orbit per unit eps, exact in e (midpoint rule, periodic)."""
    c = np.cos(Egrid)
    x = np.sqrt((1 + e*c)/(1 - e*c))
    dx = c/(x*(1 - e*c)**2)
    dPhi = np.mean(Wp(shape, uc*x)*uc*dx)
    return 2*np.pi*np.sqrt(1 - e**2)/e*dPhi


def two_sided(x, s):
    return max(abs(x - 2*s), abs(x + 2*s))


def bounds(shape, vstar):
    out = {}
    for name, (a, e, P) in PLANETS.items():
        uc = np.sqrt(GM_SUN/a)/vstar
        sig = adv_per_orbit(shape, uc, e)*(36525.0/P)*MAS    # mas/cy per eps
        x, s = EPM[name]
        out['prec ' + name] = two_sided(x, s)/abs(sig)
    a, e, P = MOON
    ucm = np.sqrt(GM_EM/a)/vstar
    sigm = adv_per_orbit(shape, ucm, e)*(365.25/P)*MAS*1e3  # micro-arcsec/yr per eps
    out['LLR perigee'] = LLR_PERIGEE_2SIG/abs(sigm)
    # GM_E: LLR vs SLR (Ries): relative diff -5.02e-10 +- 1.61e-9 (agent); eps (K_moon - K_lageos)
    rel, srel = -0.0002/398600.4354, np.hypot(0.0005, 0.0004)/398600.4354
    dK = K(shape, ucm) - K(shape, np.sqrt(398600.4418/LAGEOS_A)/vstar)
    out['GM_E LLR vs SLR'] = two_sided(rel, srel)/abs(dK)
    # double pulsar: d(omdot)/omdot < 1.3e-4/2.5
    GMdp = DP_M*GM_SUN
    Pb = DP_PB*DAY
    adp = (GMdp*Pb**2/(4*np.pi**2))**(1/3)
    ucd = np.sqrt(GMdp/adp)/vstar
    gr_per_orbit = np.radians(DP_OMDOT)*DP_PB/365.25
    out['double pulsar'] = (DP_PBDOT_95/2.5)/abs(adv_per_orbit(shape, ucd, DP_E)/gr_per_orbit)
    # Eros: flyby at 0.965 km/s (W) vs orbit at 3.6 m/s (K); ratio - 1 = +0.076 +- 0.269
    dKe = Wfun(shape, 0.965/vstar) - K(shape, 0.0036/vstar)
    out['Eros'] = two_sided(0.076, 0.269)/abs(dKe) if abs(dKe) > 0 else np.inf
    # Cassini: eps*K(u_E) in [-3.35e-5, 1.25e-5]
    kE = K(shape, np.sqrt(GM_SUN/PLANETS['Earth'][0])/vstar)
    out['Cassini'] = 3.35e-5/abs(kE) if kE != 0 else np.inf
    return out


for shape in ('gauss', 'lorentz'):
    print(f"--- {shape}: strongest test at the requested v* ---")
    for vstar in (0.1, 1.0, 10.0, 30.0, 120.0, 1000.0):
        b = bounds(shape, vstar)
        items = sorted(b.items(), key=lambda kv: kv[1])
        print(f"v* = {vstar:7.1f} km/s: " + "; ".join(f"{k} {v:.3g}" for k, v in items[:4]))
    print()

# Mars signal at 120 km/s (agent: -5.17e9 mas/cy per eps)
a, e, P = PLANETS['Mars']
print("Mars signal per eps at v*=120 (gauss) [mas/cy]:",
      f"{adv_per_orbit('gauss', np.sqrt(GM_SUN/a)/120, e)*(36525/P)*MAS:.4g}")
# u<<1 check: Mars and Mercury at 30000 km/s vs -(2/3)(c/v*)^2 of GR advance
for name in ('Mercury', 'Mars'):
    a, e, P = PLANETS[name]
    gr = 6*np.pi*GM_SUN/(C**2*a*(1 - e**2))
    for vstar in (3000.0, 30000.0):
        print(f"{name} v*={vstar}: adv/GR = {adv_per_orbit('gauss', np.sqrt(GM_SUN/a)/vstar, e)/gr:.6g};"
              f" -(2/3)(c/v*)^2 = {-(2/3)*(C/vstar)**2:.6g}")

print()
print("--- Gaussian envelope scan, 400 log points in [0.1, 3000] km/s ---")
vgrid = np.logspace(np.log10(0.1), np.log10(3000), 400)
env = []
for vstar in vgrid:
    b = bounds('gauss', vstar)
    k = min(b, key=b.get)
    env.append((vstar, b[k], k))
for lo, hi in ((0.3, 3000), (0.5, 3), (3, 300), (300, 3000)):
    sel = [t for t in env if lo <= t[0] <= hi]
    w = max(sel, key=lambda t: t[1])
    s = min(sel, key=lambda t: t[1])
    print(f"[{lo},{hi}] km/s: weakest {w[1]:.3g} at {w[0]:.3g} ({w[2]}); strongest {s[1]:.3g} at {s[0]:.3g} ({s[2]})")
print("Gaussian LLR bound at low v*:")
for vstar in (0.17, 0.18, 0.20, 0.25, 0.30):
    b = bounds('gauss', vstar)
    print(f"  v* = {vstar:.2f}: LLR {b['LLR perigee']:.3g}; Eros {b['Eros']:.3g}")
selL = []
for vstar in vgrid:
    b = bounds('lorentz', vstar)
    k = min(b, key=b.get)
    selL.append((vstar, b[k], k))
w = max(selL, key=lambda t: t[1])
print(f"Lorentzian over [0.1, 3000]: weakest {w[1]:.3g} at {w[0]:.3g} ({w[2]})")

print()
print("--- other inputs ---")
# Mercury beta cross-check (Will 2014: beta-1 = (-4.1 +- 7.8)e-5): advance fraction = -(beta-1)/3
lo, hi = -(-4.1e-5 + 2*7.8e-5)/3, -(-4.1e-5 - 2*7.8e-5)/3
print(f"Mercury beta: fractional advance shift in [{lo:.3e}, {hi:.3e}];"
      f" |eps| < {1.5*max(abs(lo), abs(hi))*(1000/C)**2:.3g} at v*=1000")
# double-pulsar factor 2.5: omdot ~ M^(2/3) => dM/M = 1.5 d omdot/omdot; Pbdot ~ m1 m2 M^(-1/3) ~ M^(5/3) at fixed ratio
print("Pbdot sensitivity to omdot bias at fixed mass ratio:", (5/3)*(3/2))
print("2PN/sigma ratio for omdot (agent: 4.39e-4 deg/yr vs 1.3e-5):", 4.39e-4/1.3e-5)

print()
print("--- grid endpoint: the scan's top point vs exactly 3000 km/s ---")
print("np.logspace top point =", repr(vgrid[-1]), "; included by a '<= 3000' filter:", vgrid[-1] <= 3000)
for shape in ('gauss', 'lorentz'):
    for vstar in (2920.0, 3000.0):
        b = bounds(shape, vstar)
        k = min(b, key=b.get)
        print(f"  {shape} v* = {vstar}: strongest {k} {b[k]:.3g}")
