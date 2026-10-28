"""Context for Paul's reading of 'momentum gravity' between ordinary bodies (outside C1-C20):
one-particle exchange between point masses with relative Lorentz factor gamma; tensor factor of the
exchange amplitude T1.T2 - c T1 T2 with c = 1/3 (massive spin-2, Fierz-Pauli) or 1/2 (massless)
[T, dagger: vDVZ structure from memory]. For T^{mu nu} = m u^mu u^nu: T1.T2 = m1 m2 gamma^2, T1 T2 = m1 m2.
Ratio massive/massless at rest = (2/3)/(1/2) = 4/3 (the 4/3 in the diameter note's alpha).
Velocity dependence relative to rest: (gamma^2 - c)/(1 - c)."""
import sympy as sp
b = sp.symbols('beta', positive=True)
g2 = 1/(1 - b**2)
for name, c in [('massive (X)', sp.Rational(1, 3)), ('massless', sp.Rational(1, 2))]:
    f = (g2 - c)/(1 - c)
    print(name, ": factor =", sp.simplify(f), "; series:", sp.series(f, b, 0, 4))
print("rest-frame ratio massive/massless =", sp.Rational(2, 3)/sp.Rational(1, 2))
beta = 120/299792.458
print(f"at v = 120 km/s: massive factor - 1 = {float(((1/(1-beta**2)) - sp.Rational(1,3))/(sp.Rational(2,3)) - 1):.3e}")
