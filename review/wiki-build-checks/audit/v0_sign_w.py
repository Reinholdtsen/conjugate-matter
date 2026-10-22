# If V0 < 0 then V = V0[1+cos] <= 0 everywhere. Can tau then be dark energy (w near -1) with rho_tau > 0?
# Canonical scalar: rho = K + V, p = K - V, K = taudot^2/2 >= 0. Write V = -U with U >= 0.
import sympy as sp
K, U = sp.symbols('K U', nonnegative=True)
rho = K - U; p = K + U
w_minus_1 = sp.simplify(p/rho - 1)
print("V = -U <= 0: w - 1 =", w_minus_1, "-> with rho = K - U > 0 this is >= 0, so w >= +1 (stiff side), never near -1")
for k_, u_ in ((1, 0.5), (2, 0.1), (1, 0.9)):
    print(f"  K={k_}, U={u_}: rho={k_-u_}, w={(k_+u_)/(k_-u_):.4f}")
# Consequence of the alternative fix (negative minimum): once rho_tau < 0, p/rho can fall below -1 although rho + p >= 0
td, V = sp.symbols('td V', real=True)
print("rho + p =", sp.simplify((td**2/2 + V) + (td**2/2 - V)),
      "; example td=1, V=-1: rho =", sp.Rational(1, 2) - 1, ", w =", (sp.Rational(1, 2) + 1)/(sp.Rational(1, 2) - 1))
