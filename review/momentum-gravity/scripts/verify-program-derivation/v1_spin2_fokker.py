"""Independent check (verifier, derivation lens) of the program agent's P7 and P8.

Route deliberately different from an amplitude/1/(4E1E2) calculation: the classical
Fokker (Wheeler-Feynman) action for two point sources of a linear field, with the
time-symmetric Green's function expanded to second order in d/dt.

  G(r, tau) = int dw/2pi e^{-i w tau} int d^3q/(2pi)^3 e^{iq.r} / (q^2 + M^2 - w^2)
            = delta(tau) Y(r) - delta''(tau) Z(r) + ...,
  Y = FT[1/(q^2+M^2)]   = e^{-Mr}/(4 pi r),
  Z = FT[1/(q^2+M^2)^2] = e^{-Mr}/(8 pi M)   (massless: -r/(8 pi) + const).

Cross term of the Fokker action for sources J1(t1), J2(t2):
  int dt1 dt2 J1 J2 G(x1(t1)-x2(t2), t1-t2)
  = int dt [ J1 J2 Y(r) - J1 J2 v1_i v2_j d_i d_j Z(r) ] + O(v^4)   (static J at leading order)
(two integrations by parts of delta''(t1-t2) = -d_t1 d_t2 delta(t1-t2), and
 d/dt2 acting on x2 gives -v2.grad_r).

Tensor structure of the exchanged field (conserved sources):
  spin 0 : J1 J2 with J = q/gamma (scalar density per dt)
  spin 1 : J1.J2 with J^mu = e (1, v)
  spin 2 : T1.T2 - c T1 T2, T^{mu nu} = m gamma v^mu v^nu, v^mu = (1, v); c = 1/2 massless, 1/3 Fierz-Pauli
Overall normalisation fixed so the static limit is the Newton/Coulomb/Yukawa potential.
Anchors (independent of the agent): Darwin Lagrangian (spin 1) and the EIH Lagrangian's O(G) terms
(spin 2, massless), both textbook forms; the vDVZ ratio 3/4.
"""
import sympy as sp

print("=== Part 1: tensor factor T1.T2 - c T1 T2 for point masses, any frame ===")
g1, g2 = sp.symbols('gamma1 gamma2', positive=True)
v1 = sp.Matrix(sp.symbols('a1:4', real=True))
v2 = sp.Matrix(sp.symbols('b1:4', real=True))
m1, m2, c = sp.symbols('m1 m2 c', positive=True)
eta = sp.diag(1, -1, -1, -1)
gam1 = 1/sp.sqrt(1 - (v1.T*v1)[0])
gam2 = 1/sp.sqrt(1 - (v2.T*v2)[0])
u1 = gam1*sp.Matrix([1, *v1])
u2 = gam2*sp.Matrix([1, *v2])
T1 = m1*u1*u1.T          # upper indices
T2 = m2*u2*u2.T
T1low = eta*T1*eta
contr = sum(T1low[i, j]*T2[i, j] for i in range(4) for j in range(4))
tr1 = sum(eta[i, i]*T1[i, i] for i in range(4))
tr2 = sum(eta[i, i]*T2[i, i] for i in range(4))
gam_rel = (u1.T*eta*u2)[0]
expr = contr - c*tr1*tr2 - m1*m2*(gam_rel**2 - c)
# numerical spot checks at random velocities (exact rationals)
import random
random.seed(7)
ok = True
for trial in range(5):
    sub = {s: sp.Rational(random.randint(-30, 30), 100) for s in list(v1) + list(v2)}
    sub.update({c: sp.Rational(1, 3), m1: 2, m2: 3})
    val = sp.nsimplify(sp.simplify(expr.subs(sub)))
    ok &= (val == 0)
print("T1.T2 - c T1 T2 == m1 m2 ((u1.u2)^2 - c) at 5 random exact velocity pairs:", ok)

gam, v = sp.symbols('gamma v', positive=True)
N0 = (gam**2 - sp.Rational(1, 2))/(1 - sp.Rational(1, 2))
N1 = (gam**2 - sp.Rational(1, 3))/(1 - sp.Rational(1, 3))
print("normalised massless   :", sp.expand(N0), "  Chebyshev T2(gamma) =", sp.chebyshevt(2, gam), " equal:", sp.simplify(N0 - sp.chebyshevt(2, gam)) == 0)
print("normalised Fierz-Pauli:", sp.expand(N1), "  Legendre P2(gamma)  =", sp.expand(sp.legendre(2, gam)), " equal:", sp.simplify(N1 - sp.legendre(2, gam)) == 0)
gv = 1/sp.sqrt(1 - v**2)
print("series massless   :", sp.series(N0.subs(gam, gv), v, 0, 7))
print("series Fierz-Pauli:", sp.series(N1.subs(gam, gv), v, 0, 7))
print("gamma->oo ratio N1/N0 =", sp.limit(N1/N0, gam, sp.oo))
# relative gamma to O(v^2) depends only on |v1-v2|
eps = sp.symbols('epsilon', positive=True)
gr = sp.series(gam_rel.subs({s: eps*s for s in list(v1)+list(v2)}), eps, 0, 3).removeO()
dv = v1 - v2
print("u1.u2 - [1 + |v1-v2|^2/2] at O(eps^2):", sp.simplify(gr - (1 + eps**2*(dv.T*dv)[0]/2)))

print()
print("=== Part 2: O(v^2) two-body Lagrangians from the Fokker action ===")
x, y, z = sp.symbols('x y z', real=True)
rv = sp.Matrix([x, y, z])
r = sp.sqrt(x**2 + y**2 + z**2)
n = rv/r
M = sp.symbols('M', positive=True)
G, e1, e2, al = sp.symbols('G e1 e2 alpha', positive=True)

def hess_contract(Zf):
    H = sp.Matrix(3, 3, lambda i, j: sp.diff(Zf, rv[i], rv[j]))
    return (v1.T*H*v2)[0]

Y0 = 1/(4*sp.pi*r)
Z0 = -r/(8*sp.pi)
YM = sp.exp(-M*r)/(4*sp.pi*r)
ZM = sp.exp(-M*r)/(8*sp.pi*M)
# check Y, Z are the claimed Fourier transforms via (-lap + M^2) Y = 0 off origin, (-lap + M^2) Z = Y
lap = lambda f: sum(sp.diff(f, s, 2) for s in (x, y, z))
print("(-lap+M^2) Y_M = 0 off origin:", sp.simplify(-lap(YM) + M**2*YM) == 0)
print("(-lap+M^2) Z_M = Y_M         :", sp.simplify(-lap(ZM) + M**2*ZM - YM) == 0)
print("-lap Z_0 = Y_0 (massless)     :", sp.simplify(-lap(Z0) - Y0) == 0)

def series2(f):
    return sp.series(f.subs({s: eps*s for s in list(v1)+list(v2)}), eps, 0, 3).removeO().subs(eps, 1)

vv = (v1.T*v2)[0]
nv1 = (n.T*v1)[0]
nv2 = (n.T*v2)[0]
v1s = (v1.T*v1)[0]
v2s = (v2.T*v2)[0]

# spin 1: L_int = - e1 e2 * 4 pi * [ (J1.J2) Y - v1 v2 : dd Z ], J^mu = (1, v)
J1J2 = 1 - vv
L1 = -e1*e2*4*sp.pi*(J1J2*Y0 - hess_contract(Z0))
Darwin = -e1*e2/r + e1*e2/(2*r)*(vv + nv1*nv2)        # Landau-Lifshitz sec. 65 / Jackson 12.6 (anchor)
print("spin 1: L_int - Darwin =", sp.simplify(sp.expand(L1 - Darwin)))

# spin 2: tensor factor with T^{mu nu} = m gamma v^mu v^nu, normalised to its static value (1-c)
def F_tensor(cval):
    vmu1 = sp.Matrix([1, *v1]); vmu2 = sp.Matrix([1, *v2])
    dot4 = (vmu1.T*eta*vmu2)[0]
    t1 = gam1*(1 - v1s)      # trace of T1/m1 = 1/gamma1
    t2 = gam2*(1 - v2s)
    full = gam1*gam2*dot4**2 - cval*t1*t2
    return series2(full)/(1 - cval)

F0 = F_tensor(sp.Rational(1, 2))
F1 = F_tensor(sp.Rational(1, 3))
print("massless tensor factor to O(v^2):", sp.expand(F0))
print("FP tensor factor to O(v^2)      :", sp.expand(F1))
# L_int = + G m1 m2 * 4 pi [ F Y - v1 v2 : dd Z ]   (attractive; static limit +G m1 m2/r)
L2 = G*m1*m2*4*sp.pi*(F0*Y0 - hess_contract(Z0))
EIH_G = G*m1*m2/r*(1 + sp.Rational(3, 2)*(v1s + v2s) - sp.Rational(7, 2)*vv - sp.Rational(1, 2)*nv1*nv2)  # LL sec. 106, O(G) part (anchor)
print("spin 2 massless: L_int - EIH O(G) terms =", sp.simplify(sp.expand(L2 - EIH_G)))

L2M = al*G*m1*m2*4*sp.pi*(F1*YM - hess_contract(ZM))
claimed = al*G*m1*m2*sp.exp(-M*r)/r*(1 + (v1s + v2s) - sp.Rational(5, 2)*vv - sp.Rational(1, 2)*nv1*nv2) \
          - al*G*m1*m2*M/2*sp.exp(-M*r)*nv1*nv2
print("massive spin 2: L_int - [agent's form incl. -(alpha G m1 m2 M/2) e^{-Mr}(n.v1)(n.v2)] =",
      sp.simplify(sp.expand(L2M - claimed)))

# CM-frame forms
mu_, Mt, nu = sp.symbols('mu M_t nu', positive=True)
vr = sp.Matrix(sp.symbols('w1:4', real=True))
sub_cm = {}
m1v, m2v = sp.symbols('m1v m2v', positive=True)
# v1 = (m2/(m1+m2)) w, v2 = -(m1/(m1+m2)) w
def cm(expr_v):
    e = expr_v
    rep = {v1[i]: m2/(m1+m2)*vr[i] for i in range(3)}
    rep.update({v2[i]: -m1/(m1+m2)*vr[i] for i in range(3)})
    return sp.simplify(e.subs(rep, simultaneous=True))
nuv = m1*m2/(m1+m2)**2
w2 = (vr.T*vr)[0]; nw = (n.T*vr)[0]
gr_vel = 1 + sp.Rational(3, 2)*(v1s + v2s) - sp.Rational(7, 2)*vv - sp.Rational(1, 2)*nv1*nv2 - 1
fp_vel = (v1s + v2s) - sp.Rational(5, 2)*vv - sp.Rational(1, 2)*nv1*nv2
print("CM: GR velocity terms - [(3+nu) w^2 + nu (n.w)^2]/2 =",
      sp.simplify(cm(gr_vel) - ((3 + nuv)*w2 + nuv*nw**2)/2))
print("CM: FP velocity terms - [(1+nu/2) w^2 + nu (n.w)^2/2] =",
      sp.simplify(cm(fp_vel) - ((1 + nuv/2)*w2 + nuv*nw**2/2)))
dvs = ((v1 - v2).T*(v1 - v2))[0]
print("general frame: GR velocity terms - [3/2|v1-v2|^2 - 1/2 v1.v2 - 1/2 (n.v1)(n.v2)] =",
      sp.simplify(sp.expand(gr_vel - (sp.Rational(3, 2)*dvs - sp.Rational(1, 2)*vv - sp.Rational(1, 2)*nv1*nv2))))
# Galilean boost of the GR O(G) velocity terms: v_i -> v_i + U, is the change zero?
U = sp.Matrix(sp.symbols('U1:4', real=True))
boost = gr_vel.subs({**{v1[i]: v1[i] + U[i] for i in range(3)}, **{v2[i]: v2[i] + U[i] for i in range(3)}}, simultaneous=True)
print("GR O(G) velocity terms change under Galilean boost (nonzero expected):", sp.simplify(sp.expand(boost - gr_vel)) != 0)

print()
print("=== Part 3: sizes (v/c)^2 ===")
cl = 299792.458
for vk in (100, 120, 300):
    print(f"v = {vk} km/s: (v/c)^2 = {(vk/cl)**2:.3e}")
