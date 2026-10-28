"""Critic check c6: re-runs for the analyst/verifier disagreements that touch the answer.

(A) P13 (program) vs its verifiers: does the gated precession saturate, or peak and
    turn prograde?  Uses the ordinary-tests analysis' independent first-order formula
    (O7): dw = 2 pi beta sqrt(1-e^2)/e dPhi/de,
    Phi(e) = (1/2pi) Int W(u_c sqrt((1+e cosE)/(1-e cosE))) dE, u_c^2 = GM/(a v*^2),
    with P13's gate W = exp(-u^2), beta = 0.2, e = 0.3.  Compared with the derivation
    verifier's first-order values (v4c: -0.39248 at 0.3, +0.040047 at 1, +0.61760 at 2)
    and P13's leading formula -4 pi beta u_c^2/(1-e^2).
(B) Ordinary tests O13/O23 vs their derivation verifier: free fall from rest at the pole
    in L = v^2/2 + (GM/r)(1 + eps W(|v|/v*)), body-level gate (sympy, exact at v = 0).
(C) P19 / C14 / K16: Born versus classical regime for the long-range core-making force.
(D) C7 vs the clumping derivation verifier: harmonic core canonical map (sympy).
(E) Range of X (P17 / P9 vs verifiers): Vainshtein radii, u = 1, r_V = (r_S (1+u^2) lambda^2)^(1/3)
    (the convention of verify/phase_space_diameter.py as quoted by P18).
(F) Gate-width conventions across the analyses.
"""
import numpy as np
import mpmath as mp
import sympy as sp

print("=== (A) gated precession, first order in beta, exact in e (O7 formula) ===")
mp.mp.dps = 25
beta, e0 = 0.2, 0.3
def Phi(e, uc):
    f = lambda E: mp.exp(-(uc**2) * (1 + e * mp.cos(E)) / (1 - e * mp.cos(E)))
    return mp.quad(f, [0, mp.pi, 2 * mp.pi]) / (2 * mp.pi)
for uc2 in (0.0033, 0.01, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 3.0, 30.0):
    uc = mp.sqrt(uc2)
    dPhi = mp.diff(lambda e: Phi(e, uc), e0)
    dw = 2 * mp.pi * beta * mp.sqrt(1 - e0**2) / e0 * dPhi
    lead = -4 * mp.pi * beta * uc2 / (1 - e0**2)
    print(f"  GM/(a v*^2) = {uc2:7.4f}: first-order dw = {float(dw):+.5e} rad/orbit ; leading-order formula {float(lead):+.5e} ; ratio {float(dw/lead):+.4f}")
print("  verifier v4c (first order, e = 0.3): 0.30 -> -3.9248e-01 ; 1.00 -> +4.0047e-02 ; 2.00 -> +6.1760e-01")

print("\n=== (B) free fall from rest, body-level velocity gate ===")
r, GM, eps, vs = sp.symbols('r GM epsilon v_s', positive=True)
vr = sp.symbols('v_r')
W = lambda u: sp.exp(-u**2)
L = vr**2 / 2 + GM / r * (1 + eps * W(vr / vs))     # radial motion only
# Euler-Lagrange: d/dt(dL/dvr) = dL/dr ; at vr = 0: M_eff * rddot = dL/dr, M_eff = d2L/dvr2
Meff = sp.diff(L, vr, 2).subs(vr, 0)
Fr = sp.diff(L, r).subs(vr, 0)
acc = sp.simplify(Fr / Meff)
print("  rddot at rest =", acc)
ser = sp.series(acc / (-GM / r**2), eps, 0, 2).removeO()
print("  rddot/(-GM/r^2) to first order in eps =", sp.simplify(ser))
vc2 = 3.986004418e14 / 6.3568e6          # polar radius, GM_E (dagger inputs)
print(f"  Earth pole: v_c^2 = GM_E/R_pole = {vc2/1e6:.2f} km^2/s^2")
for v_s in (0.1, 0.17, 0.3, 1.0):
    k = 1 + 2 * vc2 / (v_s * 1e3)**2
    print(f"   v* = {v_s:5.2f} km/s: (g_ff/g_N - 1)/eps = {k:.4g} ; inertia m(1 - 2 eps v_c^2/v*^2) vanishes at eps = {(v_s*1e3)**2/(2*vc2):.3g}")

print("\n=== (C) Born vs classical for the core-making long-range force ===")
G = 6.67430e-11; hbar = 1.054571817e-34; c = 2.99792458e8
mchi = 70e6 * 1.602176634e-19 / c**2
alphaG = G * mchi**2 / (hbar * c)
for ratio in (2.37e31, 3.56e31):
    for v in (30e3,):
        eta = ratio * alphaG * c / v
        print(f"  Gt/G = {ratio:.2e}: G m^2/(hbar c) = {alphaG:.3e}; Coulomb (Sommerfeld) parameter Gt m^2/(hbar v) at 30 km/s = {eta:.2e} (Born regime if << 1)")

print("\n=== (D) harmonic core: momentum-only attraction = position attraction (canonical map) ===")
m, Om = sp.symbols('m Omega', positive=True)
xa, xb, pa, pb = sp.symbols('x_a x_b p_a p_b', real=True)
U = sp.Function('U')
Hsys = (pa**2 + pb**2) / (2 * m) + m * Om**2 * (xa**2 + xb**2) / 2 + U(pa - pb)
Xa, Xb, Pa, Pb = pa / (m * Om), pb / (m * Om), -m * Om * xa, -m * Om * xb
def PB(f, g):
    return sp.simplify(sum(sp.diff(f, q) * sp.diff(g, p) - sp.diff(f, p) * sp.diff(g, q) for q, p in ((xa, pa), (xb, pb))))
print("  {X_a,P_a} =", PB(Xa, Pa), " {X_a,P_b} =", PB(Xa, Pb), " {X_a,X_b} =", PB(Xa, Xb), " {P_a,P_b} =", PB(Pa, Pb))
XA, XB, PA, PB_ = sp.symbols('X_a X_b P_a P_b', real=True)
Hnew = Hsys.subs({pa: m * Om * XA, pb: m * Om * XB, xa: -PA / (m * Om), xb: -PB_ / (m * Om)})
print("  H in (X, P):", sp.simplify(Hnew))

print("\n=== (E) Vainshtein radii for the range of X (u = 1) ===")
rS_sun = 2 * 1.32712440018e20 / c**2; rS_earth = 2 * 3.986004418e14 / c**2
AU = 1.495978707e11; pc = 3.0856775814913673e16
def rV(rS, lam, u=1.0): return (rS * (1 + u**2) * lam**2) ** (1 / 3)
def lam_for(rS, rv, u=1.0): return np.sqrt(rv**3 / (rS * (1 + u**2)))
print(f"  lambda_X = 1 kpc: r_V(Sun) = {rV(rS_sun, 1e3*pc)/AU:.4g} AU (P18: 1.19e3 AU)")
print(f"  Earth screens its own surface (r_V = R_E) for lambda_X > {lam_for(rS_earth, 6.371e6):.3g} m")
for name, R in (("1 AU", AU), ("Saturn 9.58 AU", 9.58 * AU), ("Pluto 39.5 AU", 39.5 * AU)):
    lam = lam_for(rS_sun, R)
    print(f"  Sun's r_V encloses {name:15s} for lambda_X > {lam:.3g} m = {lam/pc:.3g} pc")
rS_bin = 2 * 2 * 1.32712440018e20 / c**2
print(f"  two solar-mass stars, lambda_X = 1 kpc: r_V = {rV(rS_bin, 1e3*pc)/AU:.3g} AU (wide binaries beyond this would see G(1 + 4/3) unscreened)")

print("\n=== (F) gate-width conventions ===")
print("  amplitude gate (notebook, clumping, dark-tests): W = exp(-v^2/(2 v*^2)), v* = sqrt2 mu/m")
print("  rate-form gate used as a potential (program P12-P13, ordinary tests): W = exp(-v^2/v_a^2)")
for vb in (120.0,):
    print(f"  same width: v_a = sqrt2 v* = {np.sqrt(2)*vb:.1f} km/s for v* = {vb} km/s")
