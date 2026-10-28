#!/usr/bin/env python3
"""Tree-level chi chi -> chi chi through ONE massive spin-2 field X_{mu nu}(x) on spacetime.

Question: can exchange of such a field, with arbitrary Lorentz-invariant chi-chi-X vertices,
give an amplitude whose dependence on the incoming relative momentum k (at fixed momentum
transfer q) has a scale mu << m?

Units hbar = c = 1, metric (+,-,-,-), equal masses m, scalar chi (fermions: gate_fermion.py).
CM frame: p1 = (E, k, 0, 0), p2 = (E, -k, 0, 0), p3, p4 rotated by theta; q^2 = 2k^2(1 - cos th).
The most general chi(p_in) -> chi(p_out) + X(l) vertex for on-shell chi, with P = p_in + p_out,
l = p_in - p_out, is
    V^{mu nu} = F1 P P + F2 (P l + l P) + F3 l l + F4 m^2 eta,
where F1..F4 are arbitrary functions of the vertex invariants.  With p_in^2 = p_out^2 = m^2 the
only invariant at the vertex is l^2 = t, so F_i = F_i(t): any number of derivatives and any form
factor reduce to this (checked in part 0).  At fixed t they are constants, so symbols suffice.
"""
import sympy as sp

m, M, k, q = sp.symbols('m M k q', positive=True)
c = sp.symbols('c', real=True)                      # cos(theta)
sn = sp.sqrt(1 - c**2)                               # sin(theta), theta in [0, pi]
E = sp.sqrt(m**2 + k**2)
eta = sp.diag(1, -1, -1, -1)
F1, F2, F3, F4 = sp.symbols('F1:5')
S = sp.symbols('S')                                  # S = s - u


def V4(*a):
    return sp.Matrix(a)


def dot(a, b):
    return sp.expand((a.T * eta * b)[0, 0])


def outer(a, b):
    return a * b.T


p1 = V4(E, k, 0, 0)
p2 = V4(E, -k, 0, 0)
p3 = V4(E, k * c, k * sn, 0)
p4 = V4(E, -k * c, -k * sn, 0)
cq = 1 - q**2 / (2 * k**2)                           # cos(theta) at fixed transfer q

s_ = dot(p1 + p2, p1 + p2)
t_ = dot(p1 - p3, p1 - p3)
u_ = dot(p1 - p4, p1 - p4)
print("== kinematics ==")
print("s =", sp.simplify(s_), "; t(q) =", sp.simplify(t_.subs(c, cq)),
      "; u(q) =", sp.simplify(u_.subs(c, cq)))
print("s - u at fixed q =", sp.expand((s_ - u_).subs(c, cq)))

print("\n== part 0: invariants available at one vertex ==")
# vertex 1 joins p1 and p3 only.  Its invariants: p1^2, p3^2, p1.p3.
print("p1^2 =", sp.simplify(dot(p1, p1)), "; p3^2 =", sp.simplify(dot(p3, p3)),
      "; p1.p3 in terms of t:", sp.simplify(dot(p1, p3) - (m**2 - t_ / 2)), "(= p1.p3 - (m^2 - t/2))")
print("P1.l1 =", sp.simplify(dot(p1 + p3, p1 - p3)), "(transverse on shell)")


def vertex(pin, pout, f=(F1, F2, F3, F4)):
    P, l = pin + pout, pin - pout
    a, b, cc, d = f
    return a * outer(P, P) + b * (outer(P, l) + outer(l, P)) + cc * outer(l, l) + d * m**2 * eta


def G_low(l):
    ll = eta * l
    return eta - outer(ll, ll) / M**2


def spin2(V1, V2, G):
    """V1^{mn} [ (G_mr G_ns + G_ms G_nr)/2 - G_mn G_rs/3 ] V2^{rs}  (massive spin-2 numerator)."""
    T1 = (V1.T * G * V2 * G).trace()
    T2 = (V1 * G * V2 * G).trace()
    return sp.expand(sp.Rational(1, 2) * (T1 + T2) - sp.Rational(1, 3) * (V1 * G).trace() * (V2 * G).trace())


print("\n== part 1: t-channel, most general vertex ==")
Nt = spin2(vertex(p1, p3), vertex(p2, p4), G_low(p1 - p3))
Nt_q = sp.expand(sp.simplify(Nt.subs(c, cq)))
Pk = sp.Poly(Nt_q, k)
print("numerator N_t(k, q) is a polynomial in k:", Nt_q.is_polynomial(k),
      "; degree in k =", Pk.degree(), "; lowest power of k:", min(mon[0] for mon in Pk.monoms()))
# rewrite in S = s - u: k^2 = (S - 4m^2 + q^2)/8
Nt_S = sp.expand(Nt_q.subs(k, sp.sqrt((S - 4 * m**2 + q**2) / 8)))
PS = sp.Poly(Nt_S, S)
print("N_t as a polynomial in S = s - u: degree =", PS.degree())
A_, B_, C_ = [sp.factor(PS.coeff_monomial(S**j)) for j in (0, 1, 2)]
print("  coefficient of S^2:", C_)
print("  coefficient of S^1:", B_)
print("  coefficient of S^0:", A_)

print("\n-- residue at the pole t = M^2 (q^2 = -M^2) --")
Res = sp.expand(Nt_q.subs(q, sp.I * M))
print("dRes/dF2, dRes/dF3, dRes/dF4 :", [sp.simplify(sp.diff(Res, F)) for F in (F2, F3, F4)])
z = sp.symbols('z')
Ssub = sp.expand((s_ - u_).subs(c, cq).subs(q, sp.I * M))          # s - u at t = M^2
P2 = (3 * z**2 - 1) / 2
target = sp.Rational(2, 3) * F1**2 * (4 * m**2 - M**2)**2 * P2.subs(z, Ssub / (4 * m**2 - M**2))
print("Res - (2/3) F1^2 (4m^2-M^2)^2 P_2(z_t), z_t = (s-u)/(4m^2-M^2):", sp.simplify(Res - target))

print("\n-- non-pole (contact) remainder --")
for label, fsub in (("F_i constants", {}),
                    ("F_i = a_i + b_i t", {F: sp.Symbol('a%d' % i) + sp.Symbol('b%d' % i) * (-q**2)
                                           for i, F in enumerate((F1, F2, F3, F4), start=1)})):
    Nf = sp.expand(Nt_q.subs(fsub, simultaneous=True))
    Rf = sp.expand(Nf.subs(q, sp.I * M))
    rem = sp.cancel((Nf - Rf) / (-q**2 - M**2))
    num, den = sp.fraction(sp.together(rem))
    print("  %-18s remainder denominator: %s ; numerator polynomial in (k, q): %s ; degree in k: %d"
          % (label, sp.factor(den), sp.expand(num).is_polynomial(k, q), sp.Poly(num, k).degree()))

print("\n== part 2: minimal coupling X_mn T^mn (conserved stress tensor) ==")
fmin = (sp.Rational(1, 2), 0, -sp.Rational(1, 2), t_ / (2 * m**2))
Vmin = vertex(p1, p3, fmin)
cons = sp.simplify(((eta * (p1 - p3)).T * Vmin))
print("l_mu V^{mu nu} =", list(cons))
Nmin = spin2(Vmin, vertex(p2, p4, fmin), G_low(p1 - p3))
st, ut, tt = s_, u_, t_
formula = (st - ut)**2 / 4 + tt**2 / 4 + 2 * m**2 * tt - sp.Rational(1, 3) * (2 * m**2 + tt)**2
print("N_min - [(s-u)^2/4 + t^2/4 + 2 m^2 t - (2m^2+t)^2/3] =", sp.simplify(Nmin - formula))
Nmin_q = sp.expand(sp.simplify(Nmin.subs(c, cq)))
N00 = Nmin_q.subs({k: 0, q: 0})
print("N_min(0,0) =", sp.simplify(N00), " (the 4/3-vs-1 massive/massless Newtonian factor: 8/3 vs 2)")
print("N_min(k, q=0)/N_min(0,0) =", sp.expand(sp.simplify(Nmin_q.subs(q, 0) / N00)))
print("N_min(k=0, q)/N_min(0,0) =", sp.expand(sp.simplify(Nmin_q.subs(k, 0) / N00)) if Nmin_q.subs(k, 0) != 0 else 'n/a')

print("\n== part 3: generic vertex, k-dependence at q = 0 ==")
N0 = sp.expand(Nt_q.subs(q, 0))
P0 = sp.Poly(N0, k)
n0, n1, n2 = [sp.factor(P0.coeff_monomial(k**j)) for j in (0, 2, 4)]
print("N_t(k, 0) = n0 + n1 k^2 + n2 k^4 with")
print("  n0 =", n0)
print("  n1 =", n1)
print("  n2 =", n2)
print("  k-scale^2 = n0/n1 =", sp.factor(n0 / n1))
print("  minimal coupling: n0/n1 =", sp.simplify((n0 / n1).subs({F1: fmin[0], F2: 0, F3: fmin[2], F4: 0})),
      "(F4 = t/2m^2 vanishes at q = 0)")

print("\n== part 4: u-channel (identical chi) at q -> 0 ==")
Nu = spin2(vertex(p1, p4, fmin), vertex(p2, p3, fmin), G_low(p1 - p4))
Nu_q0 = sp.simplify(Nu.subs(c, 1))
den_u = sp.simplify(u_.subs(c, 1) - M**2)
print("u - M^2 at q = 0:", den_u)
print("forward u-channel amplitude (minimal coupling) N_u/(u - M^2), series in k:")
print("  ", sp.series(sp.simplify(Nu_q0 / den_u), k, 0, 5))
# scalar exchange (spin 0, constant vertices g): forward t + u
g = sp.symbols('g', positive=True)
Afwd = g**2 * (1 / (0 - M**2) + 1 / (den_u))
print("spin-0 forward t+u: A(k)/A(0) =", sp.simplify(Afwd / Afwd.subs(k, 0)),
      "; limit k->oo of A(k)/A(0):", sp.limit(Afwd / Afwd.subs(k, 0), k, sp.oo))

print("\n== part 5: s-channel (chi chibar only; needs an X-chi-chibar vertex) ==")
G1, G2, G3, G4 = sp.symbols('G1:5')


def vertex_s(pa, pb, f=(G1, G2, G3, G4)):
    P, r = pa + pb, pa - pb
    a, b, cc, d = f
    return a * outer(r, r) + b * outer(P, P) + cc * (outer(P, r) + outer(r, P)) + d * m**2 * eta


Ptot = p1 + p2
Ns = spin2(vertex_s(p1, p2), vertex_s(p3, p4), G_low(Ptot))
Rs = sp.simplify(Ns.subs(M, sp.sqrt(s_)))                 # residue function: numerator at s = M^2
print("residue numerator at s = M^2:", sp.factor(Rs))
print("  equals (32/3) G1^2 k^4 P_2(cos th):", sp.simplify(Rs - sp.Rational(32, 3) * G1**2 * k**4 * P2.subs(z, c)) == 0)
delta = sp.symbols('delta', positive=True)                 # M^2 = 4(m^2 - delta): pole just below threshold
pole = Rs / (s_ - 4 * (m**2 - delta))
print("pole term near threshold:", sp.simplify(pole), "; limit k->0:", sp.limit(pole, k, 0))

print("\n== part 6: a residue F(s) that is not a polynomial needs every spin ==")
zz = sp.symbols('zz', real=True)
a = sp.Rational(-1)                                         # any nonzero a gives nonzero c_l
print("Legendre coefficients c_l = (2l+1)/2 * int_{-1}^{1} exp(a z) P_l(z) dz at a = -1:")
print("  ", [sp.N((2 * l + 1) / sp.Integer(2) * sp.integrate(sp.exp(a * zz) * sp.legendre(l, zz), (zz, -1, 1)), 6)
             for l in range(7)])
alpha = 2
print("Legendre coefficients of 1/(alpha - z), alpha = 2 (rational form):")
print("  ", [sp.N((2 * l + 1) / sp.Integer(2) * sp.integrate(sp.legendre(l, zz) / (alpha - zz), (zz, -1, 1)), 6)
             for l in range(7)])
