# Independent check of P7, P8 (and P9's gamma) by a different method from the agent's amplitude route:
# the classical field of a uniformly moving source in linearized spin-1 / massless spin-2 / Fierz-Pauli
# theory, expanded in the near zone (retardation via the d^2/dt^2 term), acting on a test particle.
# The one-sided Lagrangian is then reduced to the symmetric two-body form by an explicit total
# derivative, which is checked symbolically. Signature (-,+,+,+), units c = 1.
import sympy as sp

rx, ry, rz = sp.symbols('r_x r_y r_z', real=True)
v1 = sp.Matrix(sp.symbols('v1x v1y v1z', real=True))
v2 = sp.Matrix(sp.symbols('v2x v2y v2z', real=True))
M = sp.symbols('M', positive=True)
G, Gp, m1, m2, e1, e2, eps, alpha = sp.symbols('G Gp m1 m2 e1 e2 epsilon alpha', positive=True)
rvec = sp.Matrix([rx, ry, rz])          # r = x2 - x1 (field point minus source)
r = sp.sqrt(rx**2 + ry**2 + rz**2)
n = rvec / r
X = [rx, ry, rz]

def grad(f):
    return sp.Matrix([sp.diff(f, xi) for xi in X])
def dirder(f, a):                         # (a . grad) f
    return sum(a[i]*sp.diff(f, X[i]) for i in range(3))

K0 = sp.exp(-M*r)/(4*sp.pi*r)            # FT of 1/(q^2+M^2)
K1 = sp.exp(-M*r)/(8*sp.pi*M)            # FT of 1/(q^2+M^2)^2

# anchor: K1 is the convolution kernel: (lap - M^2) K1 = -K0
lapK1 = sum(sp.diff(K1, xi, 2) for xi in X)
print("anchor (lap - M^2) K1 + K0 = 0:", sp.simplify(lapK1 - M**2*K1 + K0) == 0)

def ret00(Kfun):
    # retardation correction  -d^2/dt^2 (S * K1) for a source at x1(t) moving with v1: d/dt -> -(v1.grad_r)
    return -dirder(dirder(Kfun, v1), v1)

# ---------------- total-derivative reduction -------------------------------------------
# (v1.grad)^2 K = d/dt[ -(v1.grad)K ] + (v1.grad)(v2.grad)K  for constant velocities, where
# d/dt acts on functions of r = x2 - x1 as (v2 - v1).grad
def ddt(f):
    return dirder(f, v2 - v1)
chk = sp.simplify(dirder(dirder(K1, v1), v1) - (ddt(-dirder(K1, v1)) + dirder(dirder(K1, v2), v1)))
print("identity (v1.d)^2 K1 = d/dt[-(v1.d)K1] + (v1.d)(v2.d)K1 :", chk == 0)

nv1 = (n.T*v1)[0]; nv2 = (n.T*v2)[0]; v1v2 = (v1.T*v2)[0]; v1s = (v1.T*v1)[0]; v2s = (v2.T*v2)[0]

def series_eps(expr, order=2):
    e = expr.subs({**{v1[i]: eps*v1[i] for i in range(3)}, **{v2[i]: eps*v2[i] for i in range(3)}}, simultaneous=True)
    return sp.series(e, eps, 0, order+1).removeO().subs(eps, 1)

# ---------------- spin 1: Darwin calibration (Lorenz gauge) ------------------------------
# box A_mu = -4 pi J_mu ; J^mu = e1 (1, v1) delta ; test particle L2 = e2 A_mu xdot^mu = e2(-phi + A.v2)
# massless limit of the kernels: K0 -> 1/(4 pi r); retardation kernel uses K1 with M -> 0 (constant part drops)
phi = 4*sp.pi*e1*(K0 + ret00(K1))
Avec = 4*sp.pi*e1*K0*v1
L1 = e2*(-phi + (Avec.T*v2)[0])
L1 = sp.limit(sp.simplify(L1), M, 0)
darwin = -e1*e2/r + e1*e2/(2*r)*(v1v2 + nv1*nv2)
# reduce: one-sided retardation piece -> symmetric piece + total derivative
tot1 = +4*sp.pi*e1*e2*ddt(-dirder(K1, v1))      # the total derivative that the reduction removes
# (first run had the sign of this total derivative flipped; the residual printed then was exactly 2x it)
diff1 = sp.simplify(sp.limit(sp.simplify(L1 - darwin - sp.limit(tot1, M, 0)), M, 0))
print("spin 1: L(one-sided) - Darwin - d/dt(...) =", diff1)

# ---------------- spin 2 --------------------------------------------------------------------
def spin2_L(cc, Gc, massive):
    g1 = 1/sp.sqrt(1 - v1s)
    eta = sp.diag(-1, 1, 1, 1)
    vup = sp.Matrix([1, v1[0], v1[1], v1[2]])
    Tup = m1*g1*vup*vup.T                      # T^{mu nu} (coefficient of delta^3)
    Tdn = eta*Tup*eta
    Ttr = sum(eta[i, i]*Tup[i, i] for i in range(4))
    S = Tdn - cc*eta*Ttr
    K0_ = K0 if massive else K0.subs(M, 0)
    h = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            h[a, b] = 16*sp.pi*Gc*S[a, b]*K0_
    h[0, 0] += 16*sp.pi*Gc*S[0, 0]*ret00(K1)
    xd = sp.Matrix([1, v2[0], v2[1], v2[2]])
    Hc = (xd.T*h*xd)[0]
    L2 = m2*Hc/(2*sp.sqrt(1 - v2s))
    tot = -16*sp.pi*Gc*m2/2*S[0, 0].subs({v1[i]: 0 for i in range(3)})*ddt(-dirder(K1, v1))
    return L2, tot

# massless: c = 1/2, coupling G
L2_0, tot0 = spin2_L(sp.Rational(1, 2), G, massive=False)
L2_0 = series_eps(L2_0)
tot0 = series_eps(tot0)
EIH = G*m1*m2/r*(1 + sp.Rational(3, 2)*(v1s + v2s) - sp.Rational(7, 2)*v1v2 - sp.Rational(1, 2)*nv1*nv2)
d0 = sp.simplify(sp.limit(sp.simplify(L2_0 - tot0), M, 0) - EIH)
print("massless spin 2: L(one-sided) - d/dt(...) - EIH(O(G) velocity terms, Will 2018 eq. 9 GR values) =", d0)

# massive: c = 1/3, coupling Gp fixed so the static potential is alpha G m1 m2 e^{-Mr}/r
L2_1, tot1_ = spin2_L(sp.Rational(1, 3), Gp, massive=True)
stat = sp.simplify(L2_1.subs({**{v1[i]: 0 for i in range(3)}, **{v2[i]: 0 for i in range(3)}}))
Gp_val = sp.solve(sp.Eq(stat, alpha*G*m1*m2*sp.exp(-M*r)/r), Gp)[0]
print("massive normalization: G' =", Gp_val, " (static h00 coefficient 4/3 G' -> alpha G)")
L2_1 = series_eps(L2_1.subs(Gp, Gp_val))
tot1_ = series_eps(tot1_.subs(Gp, Gp_val))
agent = alpha*G*m1*m2*sp.exp(-M*r)/r*(1 + (v1s + v2s) - sp.Rational(5, 2)*v1v2 - sp.Rational(1, 2)*nv1*nv2) \
        - alpha*G*m1*m2*M/2*nv1*nv2*sp.exp(-M*r)
d1 = sp.simplify(L2_1 - tot1_ - agent)
print("massive spin 2 (Fierz-Pauli, any M): L(one-sided) - d/dt(...) - agent's P8 form =", d1)
# symmetric under 1 <-> 2 (n -> -n)?
sym = agent.subs({**{v1[i]: v2[i] for i in range(3)}, **{v2[i]: v1[i] for i in range(3)}}, simultaneous=True).subs({rx: -rx, ry: -ry, rz: -rz})
print("agent's massive form symmetric under 1<->2:", sp.simplify(sym - agent) == 0)

# ---------------- P7 tensor factor ----------------------------------------------------------
gam, v = sp.symbols('gamma v', positive=True)
for cc, name in ((sp.Rational(1, 2), 'massless'), (sp.Rational(1, 3), 'Fierz-Pauli')):
    N = (gam**2 - cc)/(1 - cc)
    ser = sp.series(N.subs(gam, 1/sp.sqrt(1 - v**2)), v, 0, 7).removeO()
    print(f"{name}: normalized factor = {sp.factor(N)} ; series = {sp.expand(ser)}")
lim = sp.limit(((gam**2 - sp.Rational(1, 3))/(sp.Rational(2, 3)))/((gam**2 - sp.Rational(1, 2))/sp.Rational(1, 2)), gam, sp.oo)
print("gamma -> oo ratio massive/massless =", lim)
# general-frame relative Lorentz factor: -u1.u2 = g1 g2 (1 - v1.v2); square to O(v^2)
g1 = 1/sp.sqrt(1 - v1s); g2 = 1/sp.sqrt(1 - v2s)
grel2 = series_eps((g1*g2*(1 - v1v2))**2)
print("gamma_rel^2 - (1 + |v1 - v2|^2) to O(v^2):", sp.simplify(grel2 - (1 + ((v1 - v2).T*(v1 - v2))[0])))
# direct contraction in a general frame
eta = sp.diag(-1, 1, 1, 1)
u1 = g1*sp.Matrix([1, *v1]); u2 = g2*sp.Matrix([1, *v2])
T1 = m1*u1*u1.T; T2 = m2*u2*u2.T
contr = sum((eta*T1*eta)[a, b]*T2[a, b] for a in range(4) for b in range(4))
tr1 = sum(eta[a, a]*T1[a, a] for a in range(4)); tr2 = sum(eta[a, a]*T2[a, a] for a in range(4))
cs = sp.symbols('c_s')
print("T1.T2 - c T1 T2 - m1 m2((u1.u2)^2 - c) =", sp.simplify(contr - cs*tr1*tr2 - m1*m2*(((u1.T*eta*u2)[0])**2 - cs)))

# ---------------- P9: PPN gamma from the static fields --------------------------------------
# massless: h00 = 2U, hij = 2U delta ; massive, normalized to Newtonian strength alpha: h00 = 2 alpha U, hij = alpha U delta
U = sp.symbols('U')
h00 = 2*U + 2*alpha*U
hij = 2*U + alpha*U
gppn = sp.simplify((hij/2)/(h00/2))
print("gamma_PPN =", gppn, "; at alpha = 4/3:", gppn.subs(alpha, sp.Rational(4, 3)), "; light-bending ratio (1+gamma) massive/massless at equal Newtonian strength:",
      sp.Rational(1, 1)*(1 + sp.Rational(1, 2))/(1 + 1))
# test-mass U v^2 coefficient in a PPN metric g00 = -1 + 2U, gij = (1 + 2 gamma U) delta
gp, vv = sp.symbols('gamma_p vv', positive=True)
Lt = -sp.sqrt(1 - 2*U - (1 + 2*gp*U)*vv**2)
coef = sp.diff(sp.series(Lt, U, 0, 2).removeO(), U)
coef = sp.series(coef, vv, 0, 3).removeO().coeff(vv, 2)
print("test-mass U v^2 coefficient:", sp.simplify(coef), "-> GR:", coef.subs(gp, 1), "; gamma = 1/2:", coef.subs(gp, sp.Rational(1, 2)))
