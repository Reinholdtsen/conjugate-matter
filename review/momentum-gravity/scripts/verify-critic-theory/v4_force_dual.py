"""
v4_force_dual.py  (verify-critic-theory, round 3) -- claim c2.

#13 s1: the dual cone bounds |dp/dt| <= c~ = c^4/G; s2: a dual boost of parameter F carries the
force-free frame to a uniformly forced one, gamma~ = (1 - F^2/c~^2)^(-1/2).
For a Newtonian gravitating pair, F/c~ = (G m1/(r c^2)) (G m2/(r c^2)).

Checks:
 1. F/c~ and gamma~ - 1 for Sun-Earth, the double pulsar (Kepler from P_b), 30+30 Msun at
    r = 2 G M_tot/c^2, and 1 kg on a 1.4 Msun, 12 km neutron star (#13's own example).
 2. The Siegel generalized metric: the part linear in X sits only in the mixed blocks (d = 2, sympy);
    H symplectic, det H = 1.
 3. Mixed-block size: with x~ = (G/c^3) p, dx~/dt = (G/c^3) F, so |dx X dx~| / (c^2 dt^2) ~ X v F G/c^5
    = X (v/c)(F/c~).
Constants: CODATA 2018 G; IAU nominal GM_sun, GM_earth, au.  Double-pulsar masses and P_b from
model memory (dagger): m_A = 1.338185, m_B = 1.248868 Msun, P_b = 0.10225156248 d.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 200   # gamma~-1 ~ 1e-65 needs > 65 digits
G = mp.mpf('6.67430e-11'); c = mp.mpf(299792458)
GMs = mp.mpf('1.32712440018e20'); GMe = mp.mpf('3.986004418e14'); au = mp.mpf('1.495978707e11')
ct = c ** 4 / G
print(f"c~ = c^4/G = {mp.nstr(ct, 6)} N;  c^5/G = {mp.nstr(c**5/G, 6)} W")

def report(name, Gm1, Gm2, r, v=None):
    F = Gm1 * Gm2 / (G * r ** 2)
    x = F / ct
    alt = (Gm1 / (r * c ** 2)) * (Gm2 / (r * c ** 2))
    gt = 1 / mp.sqrt(1 - x ** 2) - 1
    s = f"  {name}: F = {mp.nstr(F, 5)} N, F/c~ = {mp.nstr(x, 5)} (product form {mp.nstr(alt, 5)}), gamma~-1 = {mp.nstr(gt, 5)}"
    if v is not None:
        s += f", v = {mp.nstr(v/1e3, 5)} km/s, (v/c)(F/c~) = vF/(c^5/G) = {mp.nstr(v * F / (c**5 / G), 5)}"
    print(s)

print("1. pairs")
v_E = mp.sqrt((GMs + GMe) / au)
report("Sun-Earth", GMs, GMe, au, v_E)
mA, mB = mp.mpf('1.338185'), mp.mpf('1.248868')
Pb = mp.mpf('0.10225156248') * 86400
a = (GMs * (mA + mB) * Pb ** 2 / (4 * mp.pi ** 2)) ** (mp.mpf(1) / 3)
vrel = 2 * mp.pi * a / Pb
print(f"  double pulsar: a = {mp.nstr(a, 6)} m from Kepler")
report("double pulsar", GMs * mA, GMs * mB, a, vrel)
Mtot = 60 * GMs
report("30+30 Msun at r = 2GM_tot/c^2", 30 * GMs, 30 * GMs, 2 * Mtot / c ** 2)
print("  (30+30 case: F/c~ = (30/120)^2 = 1/16 for any mass scale)")
F_ns = 1.4 * GMs / mp.mpf(12e3) ** 2
print(f"  1 kg on 1.4 Msun, 12 km NS: F = {mp.nstr(F_ns, 4)} N, gamma~-1 = {mp.nstr(1/mp.sqrt(1-(F_ns/ct)**2)-1, 4)} (#13 s2: ~1e-65; reproduces #13, so arithmetic only)")
F_ns10 = 1.4 * GMs / mp.mpf(10e3) ** 2
print(f"  same with R = 10 km: F = {mp.nstr(F_ns10, 4)} N, gamma~-1 = {mp.nstr(1/mp.sqrt(1-(F_ns10/ct)**2)-1, 4)}")

print("\n2. Siegel generalized metric, d = 2")
x11, x12, x22, y11, y12, y22, eps = sp.symbols('x11 x12 x22 y11 y12 y22 epsilon', real=True)
X = sp.Matrix([[x11, x12], [x12, x22]])
Y = sp.Matrix([[y11, y12], [y12, y22]])
Yi = Y.inv()
def H_of(Xm):
    return sp.Matrix(sp.BlockMatrix([[Y + Xm * Yi * Xm, -Xm * Yi], [-Yi * Xm, Yi]]))
H = H_of(eps * X)
Om = sp.Matrix(sp.BlockMatrix([[sp.zeros(2), sp.eye(2)], [-sp.eye(2), sp.zeros(2)]]))
sympl = sp.simplify(H.T * Om * H - Om)
print("  H^T Omega H - Omega = 0 :", sympl == sp.zeros(4))
print("  det H =", sp.simplify(H.det()))
lin = H.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0))
print("  O(eps) part, diagonal blocks zero:", sp.simplify(lin[:2, :2]) == sp.zeros(2), sp.simplify(lin[2:, 2:]) == sp.zeros(2))
print("  O(eps) part, mixed block (position-dual):", sp.simplify(lin[:2, 2:]))
print("  -> linear coupling only through dx . (-X Y^-1) . dx~ (and its transpose)")

print("\n3. mixed-block / position-block ~ X v F G/c^5 = X (v/c)(F/c~): Sun-Earth value printed in 1.")
print("   note: (v/c)(F/c~) is a power ratio vF/(c^5/G); it vanishes for v = 0, so it depends on v and F, not F alone")
