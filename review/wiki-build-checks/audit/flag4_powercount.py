"""Flag 4, steelman (b): non-uniform power counting h ~ e^2, x ~ e.
Under it, does "S = 2h + x^2 + O(3), A = [h, x] + O(3)" hold literally?
Also: is #7 §2 item 3 (X = 0 slice, Tr(S^2) = Tr(g^2) + Tr(g^-2) - 2d) exact,
i.e. independent of the item-2 expansion?
"""
import sympy as sp
import numpy as np

e = sp.symbols('e')
h11, h12, h22, x11, x12, x22 = sp.symbols('h11 h12 h22 x11 x12 x22')
hm = sp.Matrix([[h11, h12], [h12, h22]])
xm = sp.Matrix([[x11, x12], [x12, x22]])
I2 = sp.eye(2)

def lowest_order(M, nmax=7):
    """Lowest power of e with a nonzero coefficient in any entry of M."""
    T = M.applyfunc(lambda f: sp.expand(sp.series(f, e, 0, nmax).removeO()))
    for k in range(nmax):
        if any(sp.simplify(t.coeff(e, k)) != 0 for t in T):
            return k
    return None

# h ~ e^2, x ~ e
Y = I2 + e**2*hm; X = e*xm; Yi = Y.inv()
S = Y + X*Yi*X - Yi
A = X*Yi - Yi*X
print("power counting h ~ e^2, x ~ e:")
print("  lowest order of S - (2h + x^2):", lowest_order(S - (2*e**2*hm + e**2*xm*xm)))
print("  lowest order of A - [h, x]    :", lowest_order(A - e**3*(hm*xm - xm*hm)))
print("  lowest order of [h, x] itself :", lowest_order(e**3*(hm*xm - xm*hm)))
print("  lowest order of Tr(S^2)       :", lowest_order(sp.Matrix([[sp.expand((S*S).trace())]])))
# uniform counting for contrast (what #7's 'quadratic order' and battery T4 use)
Y = I2 + e*hm; X = e*xm; Yi = Y.inv()
S = Y + X*Yi*X - Yi
print("uniform counting h ~ x ~ e:")
print("  lowest order of S - (2h + x^2):", lowest_order(S - (2*e*hm + e**2*xm*xm)))
print("  lowest order of Tr(S^2)       :", lowest_order(sp.Matrix([[sp.expand((S*S).trace())]])))

# item 3: X = 0 slice identity, exact, random positive Y at d = 4
rng = np.random.default_rng(11)
d = 4
a = rng.standard_normal((d, d)); g = a @ a.T + d*np.eye(d)
gi = np.linalg.inv(g)
S0 = g - gi
lhs = np.trace(S0 @ S0); rhs = np.trace(g @ g) + np.trace(gi @ gi) - 2*d
print(f"item 3 at X = 0: Tr(S^2) = {lhs:.10f}, Tr(g^2)+Tr(g^-2)-2d = {rhs:.10f}, diff = {lhs-rhs:.2e}")
