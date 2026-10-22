"""Audit of flag 5, part B: from the action to the pole mass of the spin-2 mode.

Action (HR form; #8 section 1 writes the potential as V = 2 m^2 M^2 sum b_n e_n(X)):
    S = M^2 Int sqrt(-g) [ R(g) - 2 m^2 sum_n b_n e_n( sqrt(g^{-1} f) ) ]      (f = eta frozen)
Mostly-plus signature.  A helicity-2 plane wave along z:
    h_xy = h_yx = cos(w t - k z),   g = eta + eps h.
R is computed from scratch (own Christoffel/Riemann code, tested on a 2-sphere),
expanded to eps^2, and phase-averaged (total derivatives average to zero).
The potential is computed directly from the eigenvalues of g^{-1} eta.
The averaged Lagrangian is proportional to the dispersion function D(w, k); D = 0 gives
w^2 = k^2 + M_X^2, which identifies the pole mass M_X (Yukawa range 1/M_X).

Then the bimetric version with both metrics dynamical (Planck masses Mg, Mf):
the 2x2 helicity-2 mass matrix, its eigenvalues and eigenvectors.
"""
import sympy as sp

# ---------- curvature code (MTW conventions) ----------
def ricci_scalar(gm, coords):
    n = len(coords)
    gi = sp.simplify(gm.inv())
    Gam = [[[sp.simplify(sum(gi[a, s] * (sp.diff(gm[s, b_], coords[c]) + sp.diff(gm[s, c], coords[b_])
                                          - sp.diff(gm[b_, c], coords[s])) for s in range(n)) / 2)
             for c in range(n)] for b_ in range(n)] for a in range(n)]
    def riem(a, b_, c, d_):  # R^a_{b c d}
        r = sp.diff(Gam[a][d_][b_], coords[c]) - sp.diff(Gam[a][c][b_], coords[d_])
        r += sum(Gam[a][c][e] * Gam[e][d_][b_] - Gam[a][d_][e] * Gam[e][c][b_] for e in range(n))
        return r
    Ric = sp.Matrix(n, n, lambda b_, d_: sum(riem(a, b_, a, d_) for a in range(n)))
    return sp.simplify(sum(gi[b_, d_] * Ric[b_, d_] for b_ in range(n) for d_ in range(n)))

# unit test: 2-sphere of radius a has R = 2/a^2 (positive in MTW convention)
th, ph, a = sp.symbols('theta phi a', positive=True)
R_s2 = ricci_scalar(sp.diag(a**2, a**2 * sp.sin(th)**2), [th, ph])
print('test: 2-sphere R =', R_s2)

# ---------- helicity-2 wave in massive gravity ----------
t, x, y, z = sp.symbols('t x y z', real=True)
w, k, eps, m = sp.symbols('omega k epsilon m', positive=True)
b = sp.symbols('b0:5')
c = sp.cos(w * t - k * z)
eta = sp.diag(-1, 1, 1, 1)
h = sp.zeros(4)
h[1, 2] = h[2, 1] = c
g = eta + eps * h

R = ricci_scalar(g, [t, x, y, z])
sqrtmg = sp.sqrt(-g.det())
LR = sp.series(sqrtmg * R, eps, 0, 3).removeO()
LR1, LR2 = sp.expand(LR).coeff(eps, 1), sp.expand(LR).coeff(eps, 2)

def phase_avg(expr):
    # every term is a function of the phase w t - k z: average over one period in t at z = 0
    e = sp.expand(expr.subs(z, 0))
    return sp.simplify(sp.integrate(e, (t, 0, 2 * sp.pi / w)) * w / (2 * sp.pi))

print('order-eps part of sqrt(-g) R, averaged:', phase_avg(LR1))
avgR2 = phase_avg(LR2)
print('order-eps^2 part of sqrt(-g) R, averaged:', avgR2)

# potential: eigenvalues of g^{-1} eta for this h are 1, 1, 1/(1+eps c), 1/(1-eps c)
lam = sp.symbols('lam')
Minv = sp.simplify(g.inv() * eta)
evs = sp.roots(sp.Poly(sp.factor((lam * sp.eye(4) - Minv).det()), lam))
print('eigenvalues of g^{-1} eta (with multiplicity):', evs)
xs = []
for ev, mult in evs.items():
    xs += [sp.sqrt(ev)] * mult
def e_n(vals, n):
    from itertools import combinations
    return sum(sp.Mul(*cmb) for cmb in combinations(vals, n)) if n > 0 else sp.Integer(1)
Vsum = sum(b[n] * e_n(xs, n) for n in range(5))
LV = sp.series(sqrtmg * Vsum, eps, 0, 3).removeO()
LV1, LV2 = sp.expand(LV).coeff(eps, 1), sp.expand(LV).coeff(eps, 2)
print('order-eps part of sqrt(-g) V, averaged:', phase_avg(LV1))
avgV2 = sp.factor(phase_avg(LV2))
print('order-eps^2 part of sqrt(-g) V, averaged:', avgV2)

Leff = sp.expand(avgR2 - 2 * m**2 * avgV2)          # times M^2 eps^2
flat = {b[0]: -3 * b[1] - 3 * b[2] - b[3]}            # g-tadpole = 0 (flat background)
Leff_flat = sp.factor(Leff.subs(flat))
print('averaged quadratic Lagrangian / (M^2 eps^2), flat background:', Leff_flat)
w2 = sp.solve(sp.Eq(Leff_flat, 0), w**2) if Leff_flat.has(w) else None
W2 = sp.symbols('W2', positive=True)
sol = sp.solve(sp.Eq(Leff_flat.subs(w, sp.sqrt(W2)), 0), W2)
print('dispersion: omega^2 =', sol, ' -> pole mass^2 M_X^2 = omega^2 - k^2 =',
      [sp.factor(s_ - k**2) for s_ in sol])
print('   without imposing flatness, omega^2 - k^2 =',
      [sp.factor(s_ - k**2) for s_ in sp.solve(sp.Eq(Leff.subs(w, sp.sqrt(W2)), 0), W2)])

# ---------- bimetric: both metrics dynamical ----------
# helicity-2 amplitudes p (in g) and q (in f): h_xy = p c, l_xy = q c.  Kinetic terms
# from the computed avgR2 (scale by p^2 Mg^2 and q^2 Mf^2); potential prefactor 2 m^2 MV^2.
p, q, Mg, Mf, MV = sp.symbols('p q M_g M_f M_V', positive=True)
gb = eta + eps * p * h
fb = eta + eps * q * h
Mb = sp.simplify(gb.inv() * fb)
evb = sp.roots(sp.Poly(sp.factor((lam * sp.eye(4) - Mb).det()), lam))
xb = []
for ev, mult in evb.items():
    xb += [sp.sqrt(ev)] * mult
Vb = sum(b[n] * e_n(xb, n) for n in range(5))
LVb = sp.expand(sp.series(sp.sqrt(-gb.det()) * Vb, eps, 0, 3).removeO()).coeff(eps, 2)
avgVb = sp.factor(phase_avg(LVb).subs({b[0]: -3*b[1] - 3*b[2] - b[3], b[4]: -b[1] - 3*b[2] - 3*b[3]}))
print('bimetric: averaged potential at eps^2 (both tadpoles zero):', avgVb)
kin = sp.factor(avgR2 / ((w**2 - k**2)))           # kinetic weight per unit amplitude^2
# L = kin*(w^2-k^2)(Mg^2 p^2 + Mf^2 q^2) - 2 m^2 MV^2 avgVb  ->  K (w^2-k^2) - Mmat
K = sp.diag(Mg**2 * kin, Mf**2 * kin)
Vq = sp.expand(2 * m**2 * MV**2 * avgVb)
Mmat = sp.Matrix(2, 2, lambda i, j: sp.Rational(1, 2) * sp.diff(Vq, [p, q][i], [p, q][j]))
# generalized eigenproblem: det(K s - Mmat) = 0 for s = w^2 - k^2 = mass^2
s_ = sp.symbols('s')
masses = sp.solve(sp.Eq((K * s_ - Mmat).det(), 0), s_)
print('bimetric helicity-2 masses^2:', [sp.factor(mm) for mm in masses])
for mm in masses:
    ns = (K * mm - Mmat).nullspace()[0]
    print('   mass^2 =', sp.factor(mm), ' eigenvector (p, q) ~', list(sp.simplify(ns.T)))
print('   at equal Planck masses Mg = Mf = MV:',
      [sp.factor(mm.subs({Mf: Mg, MV: Mg})) for mm in masses])
