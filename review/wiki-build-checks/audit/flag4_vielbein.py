"""Flag 4, steelman (c): symmetric-vielbein parametrization Y = (1 + h/2)^2, d = 1.
Order-e^2 coefficient of S = Y + X^2/Y - 1/Y with h -> e h, x -> e x."""
import sympy as sp
e, h, x = sp.symbols('e h x')
for name, Y in [("Y = 1 + h        ", 1 + e*h),
                ("Y = (1 + h/2)^2  ", (1 + e*h/2)**2),
                ("Y = exp(h)       ", sp.exp(e*h))]:
    S = Y + (e*x)**2/Y - 1/Y
    c2 = sp.expand(sp.series(S, e, 0, 3).removeO().coeff(e, 2))
    print(name, "order-e^2 term of S:", c2)
