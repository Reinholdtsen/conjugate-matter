"""Referee's independent check of Model I (Sec. 2) and the Sec. 4 rho-preserving potential.
Own conventions: omega = [[0,1],[-1,0]], rho = [[0,1],[-1,0]], H -> S^T H S, K -> S^{-1} K S.
"""
import sympy as sp
import numpy as np

om = sp.Matrix([[0, 1], [-1, 0]])
rho = sp.Matrix([[0, 1], [-1, 0]])
I2 = sp.eye(2)
print("== basics")
print("rho^T om rho == om:", sp.simplify(rho.T*om*rho - om) == sp.zeros(2))
print("rho^2:", list(rho*rho))

X, Y = sp.symbols('X Y', real=True)
Yp = sp.symbols('Y', positive=True)
HZ = sp.Matrix([[Yp + X**2/Yp, X/Yp], [X/Yp, 1/Yp]])
print("H(Z) det:", sp.simplify(HZ.det()), " symmetric:", HZ == HZ.T)
Iop = om.inv()*HZ
print("I^2 == -1:", sp.simplify(Iop*Iop + I2) == sp.zeros(2))

# K target: traceless, det -1  <=> K^2=1 and K^T om K = -om (non-scalar)
a, b, c = sp.symbols('a b c', real=True)
K = sp.Matrix([[a, b], [c, -a]])
print("K^2 - (a^2+bc) 1:", list(sp.expand(K*K - (a**2+b*c)*I2)))
print("K^T om K + det(K)... :", list(sp.expand(K.T*om*K - K.det()*om)), " det K =", K.det())

print("\n== Sp(2,R) invariance of the three terms (generic S, H, dH, K, dK; algebraic identity)")
s1, s2, s3 = sp.symbols('s1 s2 s3', real=True)
S = sp.Matrix([[s1, s2], [s3, (1+s2*s3)/s1]])  # det S = 1 -> symplectic in 2D
print("S symplectic:", sp.simplify(S.T*om*S - om) == sp.zeros(2))
h1, h2, h3, d1, d2, d3 = sp.symbols('h1 h2 h3 d1 d2 d3', real=True)
Hg = sp.Matrix([[h1, h2], [h2, h3]])
dHg = sp.Matrix([[d1, d2], [d2, d3]])
k1, k2, k3, e1, e2, e3 = sp.symbols('k1 k2 k3 e1 e2 e3', real=True)
Kg = sp.Matrix([[k1, k2], [k3, -k1]])
dKg = sp.Matrix([[e1, e2], [e3, -e1]])

def LH(H, dH):
    return (H.inv()*dH*H.inv()*dH).trace()

def LK(H, dK):
    return (H.inv()*dK.T*H*dK).trace()

def LV(H, K):
    I = om.inv()*H
    C = K*I + I*K
    return (H.inv()*C.T*H*C).trace()

Si = S.inv()
for name, f, args, targs in [
    ("H kinetic", LH, (Hg, dHg), (S.T*Hg*S, S.T*dHg*S)),
    ("K kinetic", LK, (Hg, dKg), (S.T*Hg*S, Si*dKg*S)),
    ("potential", LV, (Hg, Kg), (S.T*Hg*S, Si*Kg*S)),
]:
    diff = sp.simplify(sp.together(f(*targs) - f(*args)))
    print(f"  {name}: transformed - original = {diff}")
print("  potential under K->-K:", sp.simplify(LV(Hg, -Kg) - LV(Hg, Kg)))
print("  K kinetic under K->-K:", sp.simplify(LK(Hg, -dKg) - LK(Hg, dKg)))

print("\n== positivity of K kinetic vs naive Tr(dK dK)")
db, dc = sp.symbols('db dc', real=True)
# tangent to a^2+bc=1 at K0=diag(1,-1): da = -(b dc + c db)/(2a) = 0
dK0 = sp.Matrix([[0, db], [dc, 0]])
print("  naive Tr(dK dK) at K0:", sp.expand((dK0*dK0).trace()))
print("  H-contracted at H=1:", sp.expand(LK(I2, dK0)))
rng = np.random.default_rng(1)
mins = []
for _ in range(2000):
    A = rng.normal(size=(2, 2)); Hn = A@A.T + 0.1*np.eye(2); Hn /= np.sqrt(np.linalg.det(Hn))
    dK = rng.normal(size=(2, 2)); dK[1, 1] = -dK[0, 0]
    mins.append(np.trace(np.linalg.inv(Hn)@dK.T@Hn@dK)/np.sum(dK**2))
print("  random (H,dK): min of Tr(H^-1 dK^T H dK)/|dK|^2 =", min(mins))

print("\n== vacua at H=1")
C1 = K*om.inv() + om.inv()*K
print("  C at H=1:", list(C1), " -> zero iff b=c")
phi = sp.symbols('phi', real=True)
Kphi = sp.Matrix([[sp.cos(phi), sp.sin(phi)], [sp.sin(phi), -sp.cos(phi)]])
print("  V(1,K(phi)) =", sp.simplify(LV(I2, Kphi)))
print("  V(1,K) general =", sp.factor(sp.expand(LV(I2, K))))

print("\n== rho action")
HZr = sp.simplify(rho.T*HZ*rho)
Zc = X + sp.I*Yp
Zp = sp.simplify(-1/Zc)
Xp, Ypp = sp.simplify(sp.re(Zp)), sp.simplify(sp.im(Zp))
HZp = HZ.subs({X: Xp, Yp: Ypp}, simultaneous=True)
print("  rho^T H(Z) rho - H(-1/Z):", sp.simplify(HZr - HZp))
print("  fixed point: H(i) =", list(HZ.subs({X: 0, Yp: 1})))
print("  rho^-1 K(phi) rho - K(phi+pi):", sp.simplify(rho.inv()*Kphi*rho - Kphi.subs(phi, phi+sp.pi)))
print("  K(phi+pi) + K(phi):", sp.simplify(Kphi.subs(phi, phi+sp.pi) + Kphi))

print("\n== stabilizer of (1,K0) in Sp(2,R)")
t = sp.symbols('t', real=True)
R = sp.Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])  # S^T S = 1 & det 1 -> rotation
K0 = sp.diag(1, -1)
eqs = sp.simplify(R.inv()*K0*R - K0)
print("  R(t)^-1 K0 R(t) - K0 =", list(eqs))
print("  solutions t in [0,2pi):", sp.solveset(sp.sin(t)**2, t, sp.Interval.Ropen(0, 2*sp.pi)))
# twisted rho: (rho, K->-K)
print("  twisted rho on (1,K0): H ->", list(rho.T*I2*rho), " K -> -(rho^-1 K0 rho) =", list(-(rho.inv()*K0*rho)))
print("  O=K11: vacuum", K0[0, 0], " rho-image", (rho.inv()*K0*rho)[0, 0])

print("\n== Hessian of V at (H=1, K0) on the 4 field directions (X, Y, b, c), a = sqrt(1-bc)")
bb, cc = sp.symbols('bb cc', real=True)
Kloc = sp.Matrix([[sp.sqrt(1 - bb*cc), bb], [cc, -sp.sqrt(1 - bb*cc)]])
Vloc = LV(HZ, Kloc)/8
vars4 = [X, Yp, bb, cc]
pt = {X: 0, Yp: 1, bb: 0, cc: 0}
Hess = sp.Matrix(4, 4, lambda i, j: sp.diff(Vloc, vars4[i], vars4[j]).subs(pt))
Hess = sp.simplify(Hess)
print("  Hessian (lambda=1):", Hess.tolist())
print("  rank:", Hess.rank(), " eigenvalues:", Hess.eigenvals())
print("  V at vacuum:", sp.simplify(Vloc.subs(pt)), " gradient:", [sp.simplify(sp.diff(Vloc, v).subs(pt)) for v in vars4])

print("\n== stiffness of phi at H=1: (f_K^2/4) Tr(dK^T dK) along K(phi)")
dKphi = sp.diff(Kphi, phi)
print("  (1/4) Tr(H^-1 dK^T H dK) at H=1 =", sp.simplify(LK(I2, dKphi)/4), "* (d phi)^2 * f_K^2")

print("\n== Sec. 4 rho-preserving potential  V_mu = -mu [Tr(K K_ref)]^2")
Kref = K0
mu = sp.symbols('mu', positive=True)
Vmu = lambda KK: -mu*((KK*Kref).trace())**2
print("  at H=1, K(phi):", sp.simplify(Vmu(Kphi) + 2*mu*(1+sp.cos(2*phi))), "(=0 means -2mu(1+cos2phi))")
print("  rho-invariance (full model, any K):", sp.simplify(Vmu(rho.inv()*K*rho) - Vmu(K)))
# along a compatible (lambda-term-zero) family: H = S^T S, K = S^-1 K0 S with S a hyperbolic 'boost' not commuting with K0
St = sp.Matrix([[sp.cosh(t), sp.sinh(t)], [sp.sinh(t), sp.cosh(t)]])
Ht, Kt = St.T*St, St.inv()*K0*St
print("  S(t) symplectic:", sp.simplify(St.T*om*St - om) == sp.zeros(2))
print("  K(t) =", sp.simplify(Kt).tolist(), " K(t)^2 = 1:", sp.simplify(Kt*Kt - I2) == sp.zeros(2))
print("  lambda-term on family:", sp.simplify(LV(Ht, Kt)))
print("  V_mu on family:", sp.simplify(Vmu(Kt)))
for tv in [0, 0.5, 1, 2, 4]:
    print(f"    t={tv}: V_total/mu = {float(sp.N((Vmu(Kt)/mu).subs(t, tv))):.4f}")
# Hessian of V_lambda/8 + V_mu at (1,K0) in the 4 coordinates, lambda=1, mu=1
Vtot = Vloc - ((Kloc*Kref).trace())**2
Ht2 = sp.Matrix(4, 4, lambda i, j: sp.diff(Vtot, vars4[i], vars4[j]).subs(pt))
Ht2 = sp.simplify(Ht2)
print("  Hessian of V_lambda/8 + V_mu (lambda=mu=1) at (1,K0):", Ht2.tolist())
ev = Ht2.eigenvals()
print("  eigenvalues:", {sp.nsimplify(k): v for k, v in ev.items()}, "->", [float(k) for k in ev])
for lam in [1, 10, 100]:
    Vt = lam*Vloc - ((Kloc*Kref).trace())**2
    Hl = sp.Matrix(4, 4, lambda i, j: sp.diff(Vt, vars4[i], vars4[j]).subs(pt))
    print(f"  lambda={lam}, mu=1: Hessian eigenvalues", sorted([round(float(k), 4) for k in Hl.eigenvals()]))
