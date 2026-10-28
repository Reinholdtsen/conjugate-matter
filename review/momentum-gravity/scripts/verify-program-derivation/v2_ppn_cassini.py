"""Verifier check of P9: PPN gamma for massless graviton + unscreened Fierz-Pauli mode of
Yukawa strength alpha at r << lambda, three independent ways:
 (1) metric components from h_{mu nu} ~ T_{mu nu} - c eta_{mu nu} T for a static source;
 (2) light deflection from the ultra-relativistic limit of the normalised tensor factor;
 (3) the test-mass U v^2 coefficient of the two-body Lagrangian (v1 file) vs PPN (gamma + 1/2).
Then the Cassini bound (Bertotti, Iess, Tortora 2003: gamma - 1 = (2.1 +- 2.3)e-5)."""
import sympy as sp
al, c = sp.symbols('alpha c', positive=True)
# (1) static source, mostly-minus signature: h00 ~ (1-c) rho, hij ~ c rho delta_ij ; normalise h00 of each field to its Newtonian share
ratio = lambda cv: cv/(1 - cv)        # h_ij/h_00 per field
U_N = 1 + al                           # Newtonian strength (massless share 1, massive share alpha)
gam1 = (1*ratio(sp.Rational(1, 2)) + al*ratio(sp.Rational(1, 3)))/U_N
print("(1) metric:      gamma_PPN =", sp.simplify(gam1))
# (2) light bending: deflection ~ sum_i share_i * (UR normalised factor / gamma^2) ; GR: 2 ; FP: 3/2 ; PPN: (1+gamma) * (1+alpha)
g = sp.symbols('g', positive=True)
UR0 = sp.limit((2*g**2 - 1)/g**2, g, sp.oo)
UR1 = sp.limit((sp.Rational(3, 2)*g**2 - sp.Rational(1, 2))/g**2, g, sp.oo)
gam2 = (UR0 + al*UR1)/U_N - 1
print("(2) deflection:  gamma_PPN =", sp.simplify(gam2))
# (3) test-mass v^2 coefficient: GR 3/2 (EIH), FP 1 (v1 file); PPN coefficient = gamma + 1/2
gam3 = (sp.Rational(3, 2) + al*1)/U_N - sp.Rational(1, 2)
print("(3) U v^2 coeff: gamma_PPN =", sp.simplify(gam3))
print("all three equal:", sp.simplify(gam1 - gam2) == 0 and sp.simplify(gam1 - gam3) == 0)
g43 = gam1.subs(al, sp.Rational(4, 3))
print("alpha = 4/3:", g43, "=", float(g43), "; gamma - 1 =", float(g43 - 1))
# Cassini 2-sigma lower end
lo = 2.1e-5 - 2*2.3e-5
a_max = sp.nsolve(gam1 - 1 - lo, al, 1e-5)
print(f"Cassini 2-sigma lower end gamma-1 = {lo:.2e} -> alpha < {float(a_max):.4e} -> u < {float(sp.sqrt(3*a_max/4)):.4e}  (alpha = 4u^2/3)")
