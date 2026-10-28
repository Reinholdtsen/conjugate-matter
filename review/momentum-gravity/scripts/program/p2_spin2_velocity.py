#!/usr/bin/env python3
"""P2 (label: program). Velocity dependence of one-particle spin-2 exchange between point masses.

Checks, in order:
 1. T1^{mu nu} T2_{mu nu} - c T1 T2 for point masses (T_i = m_i u_i u_i) = m1 m2 (gamma^2 - c), gamma = u1.u2;
    normalized to its static value: (gamma^2 - c)/(1 - c).  Massless c = 1/2, Fierz-Pauli c = 1/3.
 2. Series in v: first relative-velocity dependence at O(v^2/c^2).
 3. Anchor independent of this script: vDVZ, light bending of a massive graviton is 3/4 of the massless value
    once the Newtonian potential is matched (Hinterbichler, Rev. Mod. Phys. 84, 671 (2012), sec. 3.3 [S]).
    Light is the gamma -> infinity limit of the same tensor factors.
 4. General frame: the factor depends only on u1.u2; to O(v^2) only on |v1 - v2|.
 5. The k k / M^2 terms of the Fierz-Pauli numerator drop on conserved point sources (k.u1 = k.u2 = 0).
 6. From amplitude to the O(1/c^2) two-body Lagrangian: V(q) = -(amplitude)/(4 E1 E2), retardation from
    1/(q^2 - w^2) with w^2 -> (q.v1)(q.v2), L_int = -V at first order.
    Calibration on spin 1 against the Darwin Lagrangian (textbook anchor), then spin 2 massless against the
    EIH Lagrangian as given by C. M. Will, CQG 35, 085001 (2018), arXiv:1801.08999, eq. (9) with GR values [S]
    (independent anchor), then the prediction for a massive spin-2 (Yukawa) term.
 7. CM-frame form; test-mass PPN check; sizes of (v/c)^2.
 8. Cross-check of the transcribed EIH Lagrangian: its Euler-Lagrange accelerations against the EIH equations
    of motion as printed on Wikipedia's 'Einstein-Infeld-Hoffmann equations' page [S] (two-body case).
"""
import sympy as sp
from fractions import Fraction
import random

print("== 1. Tensor factor for point masses")
v = sp.symbols('v', positive=True)
gam = 1/sp.sqrt(1 - v**2)
eta = sp.diag(1, -1, -1, -1)
u1 = sp.Matrix([1, 0, 0, 0])
u2 = sp.Matrix([gam, gam*v, 0, 0])
m1, m2, c = sp.symbols('m1 m2 c', positive=True)
T1 = m1*u1*u1.T            # upper indices
T2 = m2*u2*u2.T
T2low = eta*T2*eta          # lower both indices
contr = sum(T1[a, b]*T2low[a, b] for a in range(4) for b in range(4))
tr1 = sum(eta[a, b]*T1[a, b] for a in range(4) for b in range(4))
tr2 = sum(eta[a, b]*T2[a, b] for a in range(4) for b in range(4))
F = sp.simplify(contr - c*tr1*tr2)
g = sp.symbols('gamma', positive=True)
F_g = sp.simplify(F.subs(v, sp.sqrt(1 - 1/g**2)))
print("T1.T2 - c T1 T2 =", sp.factor(F_g), "  (expect m1 m2 (gamma^2 - c))")
assert sp.simplify(F_g - m1*m2*(g**2 - c)) == 0
N = lambda cc: sp.simplify((g**2 - cc)/(1 - cc))
N0, N1 = N(sp.Rational(1, 2)), N(sp.Rational(1, 3))
print("normalized, massless (c=1/2):", sp.expand(N0), "= Chebyshev T2(gamma):", sp.expand(sp.chebyshevt(2, g)))
print("normalized, Fierz-Pauli (c=1/3):", sp.expand(N1), "= Legendre P2(gamma):", sp.expand(sp.legendre(2, g)))
assert sp.expand(N0 - sp.chebyshevt(2, g)) == 0 and sp.expand(N1 - sp.legendre(2, g)) == 0

print("\n== 2. Series in v (v in units of c)")
s0 = sp.series(N0.subs(g, gam), v, 0, 6).removeO()
s1 = sp.series(N1.subs(g, gam), v, 0, 6).removeO()
print("massless   :", sp.expand(s0))
print("Fierz-Pauli:", sp.expand(s1))

print("\n== 3. Anchor: gamma -> infinity ratio massive/massless (light bending, Newtonian matched)")
ratio = sp.limit(N1/N0, g, sp.oo)
print("lim N1/N0 =", ratio, " (vDVZ: 3/4, Hinterbichler 2012 sec. 3.3 [S])")
assert ratio == sp.Rational(3, 4)

print("\n== 4. General frame")
a = sp.symbols('a1:4', real=True)
b = sp.symbols('b1:4', real=True)
eps = sp.symbols('epsilon', positive=True)
va = sp.Matrix(a)*eps
vb = sp.Matrix(b)*eps
g1 = 1/sp.sqrt(1 - va.dot(va))
g2 = 1/sp.sqrt(1 - vb.dot(vb))
U1 = sp.Matrix([g1, g1*va[0], g1*va[1], g1*va[2]])
U2 = sp.Matrix([g2, g2*vb[0], g2*vb[1], g2*vb[2]])
u12 = (U1.T*eta*U2)[0]
T1g = m1*U1*U1.T
T2g = m2*U2*U2.T
T2gl = eta*T2g*eta
contr_g = sum(T1g[i, j]*T2gl[i, j] for i in range(4) for j in range(4))
tr1g = sum(eta[i, j]*T1g[i, j] for i in range(4) for j in range(4))
tr2g = sum(eta[i, j]*T2g[i, j] for i in range(4) for j in range(4))
diff = sp.simplify(contr_g - c*tr1g*tr2g - m1*m2*(u12**2 - c))
print("T1.T2 - c T1 T2 - m1 m2((u1.u2)^2 - c) =", diff)
assert diff == 0
dv2 = sum((a[i] - b[i])**2 for i in range(3))
for cc, name in [(sp.Rational(1, 2), 'massless'), (sp.Rational(1, 3), 'Fierz-Pauli')]:
    Ng = (u12**2 - cc)/(1 - cc)
    ser = sp.series(Ng, eps, 0, 3).removeO()
    print(f"{name}: O(eps^2) term minus |v1-v2|^2/(1-c):",
          sp.simplify(sp.expand(ser - 1 - eps**2*dv2/(1 - cc))))

print("\n== 5. Fierz-Pauli numerator on conserved point sources")
k0, k1, k2, k3, M = sp.symbols('k0 k1 k2 k3 M', real=True)
# rest frame of body 1; body 2 moving along x; take k orthogonal to both u's (elastic, small q limit)
kvec = sp.Matrix([0, 0, k2, k3])
Gm = sp.Matrix(4, 4, lambda i, j: eta[i, j] - (eta*kvec)[i]*(eta*kvec)[j]/M**2)  # G_{mu nu}, lower
T1l = eta*T1*eta
num = 0
for mu in range(4):
    for nu in range(4):
        for al in range(4):
            for be in range(4):
                P = sp.Rational(1, 2)*(Gm[mu, al]*Gm[nu, be] + Gm[mu, be]*Gm[nu, al]) - sp.Rational(1, 3)*Gm[mu, nu]*Gm[al, be]
                num += T1[mu, nu]*P*T2[al, be]
num = sp.simplify(num)
print("T1 P_FP T2 =", sp.factor(sp.simplify(num.subs(v, sp.sqrt(1 - 1/g**2)))), " (expect m1 m2 (gamma^2 - 1/3))")
assert sp.simplify(num.subs(v, sp.sqrt(1 - 1/g**2)) - m1*m2*(g**2 - sp.Rational(1, 3))) == 0

print("\n== 6. Amplitude -> O(1/c^2) Lagrangian")
x, y, z, r, Mm = sp.symbols('x y z r M_X', positive=True)
R = sp.sqrt(x**2 + y**2 + z**2)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
# Fourier transforms (f(r) = int d^3q/(2pi)^3 e^{iqr} f(q)) checked through the differential identities they imply
print("massless: -lap(-r/2) - 1/r =", sp.simplify(-lap(-R/2) - 1/R), " => FT[4pi/q^4] = -r/2 (up to harmonic terms)")
print("massive : (-lap + M^2)(e^{-Mr}/2M) - e^{-Mr}/r =",
      sp.simplify(-lap(sp.exp(-Mm*R)/(2*Mm)) + Mm**2*sp.exp(-Mm*R)/(2*Mm) - sp.exp(-Mm*R)/R),
      " => FT[4pi/(q^2+M^2)^2] = e^{-Mr}/(2M)")
X = [x, y, z]
def retard(f):
    """FT of 4pi q_i q_j (...) = -d_i d_j f; returns the matrix."""
    return sp.Matrix(3, 3, lambda i, j: -sp.diff(f, X[i], X[j]))
Kret0 = retard(-R/2)                       # massless
Kret1 = retard(sp.exp(-Mm*R)/(2*Mm))       # massive
nn = sp.Matrix([x, y, z])/R
chk0 = sp.simplify(Kret0 - (sp.eye(3) - nn*nn.T)/(2*R))
print("massless retardation kernel minus (delta - n n)/(2r):", chk0 == sp.zeros(3, 3))
va1 = sp.Matrix(a); vb1 = sp.Matrix(b)
gg1 = 1/sp.sqrt(1 - eps**2*va1.dot(va1)); gg2 = 1/sp.sqrt(1 - eps**2*vb1.dot(vb1))
uu = gg1*gg2*(1 - eps**2*va1.dot(vb1))
def lag_terms(static_factor, Kret, prop_static, coupling):
    """L_int = -V, V(r) = -coupling*[static_factor/(g1 g2) * prop_static + v1_i K_ij v2_j], to O(eps^2)."""
    sf = sp.series(static_factor/(gg1*gg2), eps, 0, 3).removeO()
    Vr = -coupling*(sf*prop_static + eps**2*(va1.T*Kret*vb1)[0])
    return sp.expand(-Vr)
Gs, q1, q2 = sp.symbols('G q1 q2', positive=True)
nv1 = (nn.T*va1)[0]; nv2 = (nn.T*vb1)[0]
# spin 1 calibration (charges; like charges repel): V(q) = +4pi q1 q2 (u1.u2)/(g1 g2) /(q^2 - w^2)
L1 = lag_terms(uu, Kret0, 1/R, -q1*q2)   # coupling sign: V = +q1q2(...)/r
darwin = -q1*q2/R + q1*q2/(2*R)*eps**2*(va1.dot(vb1) + nv1*nv2)
print("spin 1: L_int - Darwin =", sp.simplify(L1 - sp.expand(darwin)))
assert sp.simplify(L1 - sp.expand(darwin)) == 0
# spin 2 massless: V(q) = -4pi G m1 m2 (2 (u1.u2)^2 - 1)/(g1 g2)/(q^2 - w^2)
L2 = lag_terms(2*uu**2 - 1, Kret0, 1/R, Gs*m1*m2)
eih = Gs*m1*m2/R*(1 + eps**2*(sp.Rational(3, 2)*(va1.dot(va1) + vb1.dot(vb1)) - sp.Rational(7, 2)*va1.dot(vb1)
                               - sp.Rational(1, 2)*nv1*nv2))
print("spin 2 massless: L_int - EIH(Will 2018 eq. 9, GR values) at O(G) =", sp.simplify(L2 - sp.expand(eih)))
assert sp.simplify(L2 - sp.expand(eih)) == 0
# spin 2 massive (Fierz-Pauli), strength alpha relative to Newton at r << lambda
al = sp.symbols('alpha', positive=True)
L3 = lag_terms((3*uu**2 - 1)/2, Kret1, sp.exp(-Mm*R)/R, al*Gs*m1*m2)
L3_short = sp.simplify(sp.expand(L3*R/(al*Gs*m1*m2)).subs(Mm, 0))
pred = 1 + eps**2*(va1.dot(va1) + vb1.dot(vb1) - sp.Rational(5, 2)*va1.dot(vb1) - sp.Rational(1, 2)*nv1*nv2)
print("massive spin 2, r << lambda_X: L_int*r/(alpha G m1 m2) - [1 + (v1^2+v2^2) - 5/2 v1.v2 - 1/2 (n.v1)(n.v2)] =",
      sp.simplify(L3_short - sp.expand(pred)))
assert sp.simplify(L3_short - sp.expand(pred)) == 0
# full M_X dependence of the retardation part
Kfull = sp.simplify(Kret1 - sp.exp(-Mm*R)*((sp.eye(3) - nn*nn.T)/(2*R) - Mm*nn*nn.T/2))
print("massive retardation kernel = e^{-Mr}[(delta - n n)/(2r) - (M/2) n n]:", Kfull == sp.zeros(3, 3))

print("\n== 7a. CM frame (v1 = m2 v/M, v2 = -m1 v/M, nu = m1 m2/M^2)")
vv = sp.Matrix(sp.symbols('w1:4', real=True))
Mt = m1 + m2
sub = {}
for i in range(3):
    sub[a[i]] = m2*vv[i]/Mt
    sub[b[i]] = -m1*vv[i]/Mt
nu = m1*m2/Mt**2
nvv = (nn.T*vv)[0]
cm0 = sp.simplify(sp.expand((L2*R/(Gs*m1*m2) - 1)/eps**2).subs(sub))
cm1 = sp.simplify(sp.expand((L3_short - 1)/eps**2).subs(sub))
print("massless:", sp.simplify(cm0 - (((3 + nu)*vv.dot(vv) + nu*nvv**2)/2)) == 0, " -> [(3 + nu) v^2 + nu (n.v)^2]/2")
print("massive :", sp.simplify(cm1 - ((1 + nu/2)*vv.dot(vv) + nu*nvv**2/2)) == 0, " -> (1 + nu/2) v^2 + nu (n.v)^2/2")

dvv = (va1 - vb1).dot(va1 - vb1)
print("EIH: 3/2 (v1^2+v2^2) - 7/2 v1.v2 - 3/2 |v1 - v2|^2 =",
      sp.simplify(sp.Rational(3, 2)*(va1.dot(va1) + vb1.dot(vb1)) - sp.Rational(7, 2)*va1.dot(vb1) - sp.Rational(3, 2)*dvv),
      " (so the EIH velocity terms are 3/2|v1-v2|^2 - 1/2 v1.v2 - 1/2 (n.v1)(n.v2): not a function of v1 - v2 alone)")

print("\n== 7b. Test-mass PPN check: L = -m sqrt(1 + 2 Phi - (1 - 2 gam Phi) v^2), Phi = -GM/r")
Phi, gp, V2 = sp.symbols('Phi gamma_PPN V2', real=True)
Lt = -sp.sqrt(1 + 2*Phi*eps**2 - (1 - 2*gp*Phi*eps**2)*V2*eps**2)
coef = sp.expand(sp.series(Lt, eps, 0, 5).removeO()).coeff(eps, 4).coeff(Phi, 1).coeff(V2, 1)
print("coefficient of -Phi v^2:", sp.simplify(-coef), "; at gamma_PPN = 1:", (-coef).subs(gp, 1), "; at 1/2:", (-coef).subs(gp, sp.Rational(1, 2)), " (GR gam=1 -> 3/2 = EIH test-mass value; gam=1/2 -> 1 = massive value)")
alpha_ = sp.symbols('alpha_', positive=True)
gam_bend = sp.simplify(2*(1 + sp.Rational(3, 4)*alpha_)/(1 + alpha_) - 1)
gam_vel = sp.simplify((sp.Rational(3, 2) + alpha_*1)/(1 + alpha_) - sp.Rational(1, 2))
print("graviton + massive mode of strength alpha (r << lambda, unscreened): gamma_PPN from light bending =",
      sp.factor(gam_bend), "; from the v^2 coefficient =", sp.factor(gam_vel), "; equal:", sp.simplify(gam_bend - gam_vel) == 0)
print("  gamma_PPN - 1 =", sp.factor(gam_bend - 1), "; at alpha = 4/3:", gam_bend.subs(alpha_, sp.Rational(4, 3)),
      "=", float(gam_bend.subs(alpha_, sp.Rational(4, 3))))

print("\n== 7c. Sizes")
cl = 299792.458
for vk in [10, 30, 100, 120, 300, 1000]:
    print(f"v = {vk:5d} km/s: (v/c)^2 = {(vk/cl)**2:.2e}")

print("\n== 8. EIH Lagrangian (Will 2018 form, 2 bodies) -> accelerations, vs EIH equations of motion (Wikipedia)")
e2 = sp.symbols('e2')   # 1/c^2
X1 = sp.Matrix(sp.symbols('X1_1:4', real=True)); X2 = sp.Matrix(sp.symbols('X2_1:4', real=True))
V1 = sp.Matrix(sp.symbols('V1_1:4', real=True)); V2v = sp.Matrix(sp.symbols('V2_1:4', real=True))
M1, M2 = sp.symbols('M1 M2', positive=True)
d = X1 - X2
rr = sp.sqrt(d.dot(d)); n12 = d/rr
Lfull = (M1*V1.dot(V1)/2 + M2*V2v.dot(V2v)/2 + e2*(M1*V1.dot(V1)**2 + M2*V2v.dot(V2v)**2)/8
         + M1*M2/rr*(1 + e2*(sp.Rational(3, 2)*(V1.dot(V1) + V2v.dot(V2v)) - sp.Rational(7, 2)*V1.dot(V2v)
                             - sp.Rational(1, 2)*n12.dot(V1)*n12.dot(V2v)))
         - e2*M1*M2*(M1 + M2)/(2*rr**2))
Q = list(X1) + list(X2); Qd = list(V1) + list(V2v)
Hs = sp.Matrix(6, 6, lambda i, j: sp.diff(Lfull, Qd[i], Qd[j]))
Bx = sp.Matrix(6, 6, lambda i, j: sp.diff(Lfull, Qd[i], Q[j]))
dLdq = sp.Matrix([sp.diff(Lfull, q) for q in Q])
random.seed(7)
def rnd():
    return sp.Rational(random.randint(-9, 9), random.randint(3, 7))
worst = 0
for trial in range(3):
    vals = {s: rnd() for s in list(X1) + list(X2) + list(V1) + list(V2v)}
    vals[M1] = sp.Rational(random.randint(2, 9), 3); vals[M2] = sp.Rational(random.randint(2, 9), 5)
    H0 = Hs.subs(vals).subs(e2, 0).evalf(40); H1 = sp.diff(Hs, e2).subs(vals).evalf(40)
    rhs = (dLdq - Bx*sp.Matrix(Qd)).subs(vals)
    f0 = rhs.subs(e2, 0).evalf(40); f1 = sp.diff(rhs, e2).subs(e2, 0).evalf(40)
    a0 = H0.LUsolve(f0); a1 = H0.LUsolve(f1 - H1*a0)
    # Wikipedia EIH, body A = 1, B = 2, G = 1; n_AB = (x_A - x_B)/r, n_BA = -n_AB; a_B Newtonian inside 1/c^2 terms
    xA, xB = X1.subs(vals), X2.subs(vals); vA, vB = V1.subs(vals), V2v.subs(vals)
    mA, mB = vals[M1], vals[M2]
    dAB = xA - xB; rAB = sp.sqrt(dAB.dot(dAB)); nAB = dAB/rAB; nBA = -nAB
    aB_N = mA*nAB/rAB**2
    br = (-4*mB/rAB - mA/rAB + vA.dot(vA) + 2*vB.dot(vB) - 4*vA.dot(vB) - sp.Rational(3, 2)*nAB.dot(vB)**2
          + sp.Rational(1, 2)*(xB - xA).dot(aB_N))
    a1_wiki = mB*nBA/rAB**2*br + mB/rAB**2*nAB.dot(4*vA - 3*vB)*(vA - vB) + sp.Rational(7, 2)*mB*aB_N/rAB
    a0_wiki = mB*nBA/rAB**2
    dev0 = max(abs(float((a0[i] - a0_wiki[i]).evalf(30))) for i in range(3))
    dev1 = max(abs(float((a1[i] - a1_wiki[i]).evalf(30))) for i in range(3))
    worst = max(worst, dev0, dev1)
    print(f"trial {trial}: |a_N - a_N(wiki)| = {dev0:.1e}, |a_1PN - a_1PN(wiki)| = {dev1:.1e}")
print("EIH Lagrangian reproduces the EIH equations of motion:", worst < 1e-20)
