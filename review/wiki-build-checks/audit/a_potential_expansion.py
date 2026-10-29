"""Audit of flag 5, part A: independent expansion of the Hassan-Rosen potential.

Source definition (#8 = notes/beta-coefficients.md, section 1):
    V = 2 m^2 M^2 sum_{n=0}^{4} beta_n e_n(X),  X = sqrt(g^{-1} f),  d = 4.
The potential density in the action is sqrt(det g) * V (standard HR form).

Expand around the aligned point g = f = 1 (Euclidean skeleton, as the notes use):
    g = 1 + eps*h,  f = 1 + eps*l,   h, l random symmetric integer 4x4 matrices
    (h and l generally do NOT commute, so this tests the full matrix structure).
Exact rational arithmetic throughout (sympy).

Printed checks:
  1. order eps: the two tadpoles (g-side and f-side) and their beta combinations.
  2. order eps^2 with both tadpoles set to zero (flat aligned vacuum):
     the quadratic term is  c * (b1 + 2 b2 + b3) * [Tr((h-l)^2) - (Tr(h-l))^2]
     with one universal rational constant c -> the Fierz-Pauli structure, and its
     weight is LINEAR in (b1 + 2 b2 + b3).  This weight multiplies m^2: it is the
     coefficient of a mass-SQUARED term (part B turns it into a pole mass).
  3. palindrome b_n = b_{4-n}: b1 + 2b2 + b3 -> 2(b1 + b2); tadpoles coincide.
"""
import random
import sympy as sp

d = 4
eps, t = sp.symbols('epsilon t')
b = sp.symbols('b0:5')
I = sp.eye(d)


def rand_sym(seed):
    rng = random.Random(seed)
    M = sp.zeros(d)
    for i in range(d):
        for j in range(i, d):
            v = sp.Integer(rng.randint(-4, 4))
            M[i, j] = v
            M[j, i] = v
    return M


def coeffs(expr, order):
    expr = sp.expand(expr)
    return [expr.coeff(eps, k) for k in range(order + 1)]


def expand_potential(h, l):
    # g^{-1} f through O(eps^2)
    ginv = I - eps * h + eps**2 * (h * h)
    M = (ginv * (I + eps * l)).applyfunc(sp.expand)
    M1 = M.applyfunc(lambda e: e.coeff(eps, 1))
    M2 = M.applyfunc(lambda e: e.coeff(eps, 2))
    # principal square root X = 1 + eps A + eps^2 B:  X^2 = 1 + 2 eps A + eps^2 (A^2 + 2B)
    A = M1 / 2
    B = (M2 - A * A) / 2
    X = I + eps * A + eps**2 * B
    # verify X^2 == g^{-1} f through O(eps^2), and g^{-1} really inverts g through O(eps^2)
    R = (X * X - M).applyfunc(sp.expand)
    assert all(e.coeff(eps, k) == 0 for e in R for k in range(3))
    G = ((I + eps * h) * ginv).applyfunc(sp.expand)
    assert all((G[i, j]).coeff(eps, k) == (1 if (i == j and k == 0) else 0)
               for i in range(d) for j in range(d) for k in range(3))
    # elementary symmetric polynomials from det(t + X) = sum_n e_n t^{d-n}
    cp = sp.Poly(sp.expand((t * I + X).det(method='berkowitz')), t)
    e = [sp.expand(cp.coeff_monomial(t**(d - n))) for n in range(d + 1)]
    sqrtg = sp.series(sp.sqrt(sp.expand((I + eps * h).det())), eps, 0, 3).removeO()
    L = sp.expand(sqrtg * sum(b[n] * e[n] for n in range(d + 1)))
    return coeffs(L, 2)


tadpole_g = b[0] + 3 * b[1] + 3 * b[2] + b[3]          # expected g-side combination
tadpole_f = b[1] + 3 * b[2] + 3 * b[3] + b[4]          # expected f-side combination
flat = sp.solve([tadpole_g, tadpole_f], [b[0], b[4]], dict=True)[0]
B_FP = b[1] + 2 * b[2] + b[3]

consts = []
for seed in range(6):
    if seed == 0:
        h, l = rand_sym(100), sp.zeros(d)      # massive-gravity case: f frozen
        label = 'massive gravity (l = 0)'
    else:
        h, l = rand_sym(100 + seed), rand_sym(200 + seed)
        label = f'bimetric, draw {seed}'
    c0, c1, c2 = expand_potential(h, l)
    # 1. order eps
    pred1 = sp.Rational(1, 2) * h.trace() * tadpole_g + sp.Rational(1, 2) * l.trace() * tadpole_f
    ok1 = sp.expand(c1 - pred1) == 0
    # 2. order eps^2 at the flat aligned vacuum
    D = h - l
    FP = (D * D).trace() - D.trace()**2
    q = sp.expand(c2.subs(flat))
    ratio = sp.simplify(q / (B_FP * FP)) if FP != 0 else None
    consts.append(ratio)
    print(f'[{label}] V(1) = {sp.expand(c0)} ; order-eps matches tadpoles: {ok1} ;'
          f' Tr(D^2)-(TrD)^2 = {FP} ; eps^2 term / [(b1+2b2+b3)(Tr D^2-(Tr D)^2)] = {ratio}')

print('universal constant c (same on every draw):', set(consts))

# also: without the flatness condition the eps^2 term is NOT pure FP (tadpole pollution)
h, l = rand_sym(7), sp.zeros(d)
c0, c1, c2 = expand_potential(h, l)
P1, P2 = h.trace(), (h * h).trace()
x, y = sp.symbols('x y')
sol = sp.solve(sp.Poly(sp.expand(c2 - (x * P1**2 + y * P2)), *b).coeffs(), [x, y], dict=True)
print('massive gravity, general betas, eps^2 term = x (Tr h)^2 + y Tr h^2 with')
h2 = rand_sym(8)
c0b, c1b, c2b = expand_potential(h2, sp.zeros(d))
# solve x, y as beta-polynomials from two draws
X_, Y_ = sp.symbols('X_ Y_')
eqs = [sp.expand(c2 - (X_ * P1**2 + Y_ * P2)), sp.expand(c2b - (X_ * h2.trace()**2 + Y_ * (h2 * h2).trace()))]
s = sp.solve(eqs, [X_, Y_], dict=True)[0]
print('   x =', sp.factor(s[X_]), ' ;  y =', sp.factor(s[Y_]))
print('   x + y =', sp.factor(sp.expand(s[X_] + s[Y_])),
      '  (FP structure needs x = -y; the defect is proportional to the g-tadpole)')

# 3. palindrome
pal = {b[3]: b[1], b[4]: b[0]}
print('palindrome: b1 + 2b2 + b3 ->', sp.factor(B_FP.subs(pal)))
print('palindrome: g-tadpole ->', sp.expand(tadpole_g.subs(pal)), ' ; f-tadpole ->', sp.expand(tadpole_f.subs(pal)))
