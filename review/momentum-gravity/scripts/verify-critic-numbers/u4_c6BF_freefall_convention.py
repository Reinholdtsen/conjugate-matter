"""verify-critic-numbers, claims c6B (polar free fall) and c6F (gate-convention factor sqrt2).

c6B. Test body of mass m << M (Earth) released from rest at the pole, so its velocity relative to the
Earth's centre of mass starts at zero.  Lagrangian per unit mass (the ordinary-tests reading, O5):
    L = v^2/2 + (GM/r) [1 + eps W(v)],
for two gate conventions: W = exp(-v^2/v_a^2) (ordinary tests / program) and W = exp(-v^2/(2 v*^2)) (record's
amplitude gate).  Derive rddot at v = 0 with sympy (1D radial motion suffices at release from rest).
Inputs: GM_Earth = 3.986004418e14 m^3/s^2 and WGS84 polar radius 6356752.3 m (dagger, standard values from memory).

c6F. Record (notebook sec. 3, 5.1): amplitude gate exp(-k^2/mu^2), k = m v_rel/2, v* = sqrt(2) mu/m;
cross-section gate sigma_T ~ |M|^2 ~ exp(-v^2/v*^2).
"""
import sympy as sp

t = sp.symbols('t')
GM, eps, vs = sp.symbols('GM epsilon v_s', positive=True)
r = sp.Function('r')(t)
rd = sp.diff(r, t)
for name, W in (("exp(-v^2/v_a^2)", sp.exp(-rd**2 / vs**2)), ("exp(-v^2/(2 v*^2))", sp.exp(-rd**2 / (2 * vs**2)))):
    L = rd**2 / 2 + GM / r * (1 + eps * W)
    EL = sp.diff(sp.diff(L, rd), t) - sp.diff(L, r)
    rdd = sp.solve(sp.Eq(EL, 0), sp.diff(r, t, 2))[0]
    at_rest = sp.simplify(rdd.subs(rd, 0))
    ratio = sp.simplify(at_rest / (-GM / r**2))
    first = sp.series(ratio, eps, 0, 2).removeO()
    m_eff = sp.simplify(sp.diff(sp.diff(L, rd), rd).subs(rd, 0))
    print(f"W = {name}:")
    print(f"   rddot(v=0)/(-GM/r^2) = {ratio}")
    print(f"   first order in eps   = {sp.expand(first)}")
    print(f"   effective inertia (d^2L/dv^2 at v=0) = {m_eff}; vanishes at eps = {sp.solve(sp.Eq(m_eff, 0), eps)}")

GM_E = 3.986004418e14
R_pol = 6356752.3
R_mean = 6371.0e3
print("\nnumbers at the pole, v gate scale = 0.10 km/s:")
for conv, k in (("exp(-v^2/v_a^2), v_a = 0.1 km/s", 2.0), ("exp(-v^2/(2v*^2)), v* = 0.1 km/s", 1.0)):
    x = GM_E / (R_pol * 100.0**2)
    print(f"  {conv}: (g_ff/g_N - 1)/eps = 1 + {k:.0f} GM/(R v^2) = {1 + k*x:.5e};  inertia vanishes at eps = {1/(k*x):.4e}")
print(f"  (mean radius 6371 km instead of polar: {1 + 2*GM_E/(R_mean*1e4):.5e}, {R_mean*1e4/(2*GM_E):.4e})")
print(f"  equatorial rotation speed 2 pi R_eq/sidereal day = {2*3.141592653589793*6378137.0/86164.0905:.1f} m/s:"
      f" gate exp(-v^2/v_a^2) there = {__import__('math').exp(-(2*3.141592653589793*6378137.0/86164.0905/100.0)**2):.2e}")

print("\nc6F:")
m, v, mu, vstar = sp.symbols('m v mu v_star', positive=True)
k = m * v / 2
amp = sp.exp(-k**2 / mu**2).subs(mu, m * vstar / sp.sqrt(2))
print("  amplitude gate with k = m v/2, mu = m v*/sqrt2:", sp.simplify(amp))
print("  cross-section gate |amp|^2:", sp.simplify(amp**2))
va = sp.symbols('v_a', positive=True)
sol = sp.solve(sp.Eq(-v**2 / va**2, sp.log(amp)), va)
print("  exp(-v^2/v_a^2) equals the amplitude gate for v_a =", sol, f"-> v_a = {float(sp.sqrt(2))*120:.2f} km/s at v* = 120;"
      f" ordinary-tests 120 km/s = record v* {120/float(sp.sqrt(2)):.2f} km/s")
