"""(1) Gate-convention mapping: bound at the agent-convention v* that corresponds to the notebook's
amplitude-level v* = 120 km/s; (2) Weber-type law advance (plausibility of O1's 'Tisserand 3/8')."""
import sys, os, io, contextlib
import numpy as np
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import bounds_check as bc   # reuse my own bound function (runs its prints silently)

print("=== (1) convention: notebook amplitude gate exp(-v^2/(2 v*^2)) = agent's exp(-u^2) with v*_agent = sqrt(2) v*_nb ===")
for vnb in (120.0,):
    va = np.sqrt(2)*vnb
    for shape in ('gauss', 'lorentz'):
        b120 = bc.bounds(shape, vnb); bva = bc.bounds(shape, va)
        k1 = min(b120, key=b120.get); k2 = min(bva, key=bva.get)
        print(f"  {shape}: agent v* = {vnb}: {b120[k1]:.3g} ({k1});  agent v* = {va:.1f}: {bva[k2]:.3g} ({k2})")

print("=== (2) Weber-type term L1 = A (GM/r) rdot^2: advance per orbit by Delaunay averaging ===")
GM, a, e, A = sp.symbols('GM a e A', positive=True)
Lg, Gd = sp.symbols('L_g G_d', positive=True)
# <p_r^2/r> = <v^2/r> - h^2 <1/r^3>; <v^2/r> = GM(2<1/r^2> - <1/r>/a); <1/r^2> = 1/(a^2 sqrt(1-e^2)); <1/r^3> = 1/(a^3 (1-e^2)^(3/2)); h^2 = GM a (1-e^2)
avg = GM*(2/(a**2*sp.sqrt(1-e**2)) - 1/a**2) - GM*a*(1-e**2)/(a**3*(1-e**2)**sp.Rational(3,2))
H1 = -A*GM*avg
H1D = H1.subs(a, Lg**2/GM).subs(e, sp.sqrt(1 - Gd**2/Lg**2))
T = 2*sp.pi*(Lg**2/GM)**sp.Rational(3,2)/sp.sqrt(GM)
dom = sp.simplify(sp.simplify(sp.diff(H1D, Gd)*T).subs(Gd, Lg*sp.sqrt(1-e**2)).subs(Lg, sp.sqrt(GM*a)))
print("  advance per orbit =", dom, ";  ratio to GR 6 pi GM/(c^2 a(1-e^2)) with A = 1/c^2:",
      sp.simplify(dom.subs(A, 1/sp.Symbol('c')**2)/(6*sp.pi*GM/(sp.Symbol('c')**2*a*(1-e**2)))))
import mpmath as mp
for ev in (0.2, 0.6):
    n3 = mp.quad(lambda E: (1/(1-ev*mp.cos(E)))**3*(1-ev*mp.cos(E)), [0, 2*mp.pi])/(2*mp.pi)
    print(f"  check <a^3/r^3> at e={ev}: {n3} vs (1-e^2)^(-3/2) = {(1-ev**2)**-1.5}")
print(f"  1/3 of 42.98 arcsec/cy = {42.98/3:.2f};  3/8 of 38 arcsec/cy = {3*38/8:.2f}")
