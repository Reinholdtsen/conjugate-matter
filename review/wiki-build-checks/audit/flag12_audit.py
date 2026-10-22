#!/usr/bin/env python3
"""
Independent audit of review/wiki-build-flags.md item 12.

Question: with the bounded potential V_b = -mu [Tr(K K_ref)]^2 / (2 Tr K^T K) of the toy note
v2 section 4, is the diagonal squeeze S = diag(s, 1/s) (acting H -> S^T H S, K -> S^-1 K S, the
toy note section 2 action) an exact symmetry of model I (round-4 adjudication F2 and revision 1),
or is the zero mode an unprotected flat line (toy note v2 section 4)?

Definitions are taken from papers/reciprocity-toy-models.md sections 2 and 4 only.
My own coordinates: H = H(X, Y), K = [[alpha, b], [c, -alpha]], alpha = sqrt(1 - b c) near K_ref.
"""
import sympy as sp
import numpy as np

w = sp.Matrix([[0, 1], [-1, 0]])
Kref = sp.diag(1, -1)
mu, lam, s = sp.symbols('mu lam s', positive=True)

def H_of(X, Y):
    return sp.Matrix([[Y + X**2/Y, X/Y], [X/Y, 1/Y]])

def V_lam(H, K):                      # (lam/8) Tr(H^-1 C^T H C), C = K I + I K, I = w^-1 H
    I = w.inv()*H
    C = K*I + I*K
    return lam*sp.Rational(1, 8)*(H.inv()*C.T*H*C).trace()

def V_b(K):                           # toy note v2 section 4
    return -mu*((K*Kref).trace())**2/(2*(K.T*K).trace())

def V_naive(K):                       # the round-4 F1 potential
    return -mu*((K*Kref).trace())**2

def zero(M):
    return all(sp.simplify(e) == 0 for e in sp.Matrix(M))

print("== A. Anchors (textbook facts about the definitions, independent of the paper's claims)")
X, Y = sp.symbols('X Y', real=True)
HZ = H_of(X, Y)
print("H(Z) symplectic:", zero(HZ.T*w*HZ - w), "| det H = 1:", sp.simplify(HZ.det()) == 1,
      "| I^2 = -1:", zero((w.inv()*HZ)**2 + sp.eye(2)))
S = sp.diag(s, 1/s)
print("squeeze diag(s, 1/s) symplectic:", zero(S.T*w*S - w))
print("squeeze maps (1, K_ref) to (diag(s^2, s^-2), K_ref):", S.T*S, (S.inv()*Kref*S) == Kref)
# kinetic terms and V_lam are invariant under the squeeze (they are Sp(2,R)-invariant)
h11, h12, d11, d12, d22 = sp.symbols('h11 h12 d11 d12 d22', real=True)
h22 = (1 + h12**2)/h11
Hg = sp.Matrix([[h11, h12], [h12, h22]]); dH = sp.Matrix([[d11, d12], [d12, d22]])
k = sp.symbols('k0:4', real=True); q = sp.symbols('q0:4', real=True)
Kg = sp.Matrix(2, 2, k); dK = sp.Matrix(2, 2, q)
def kin(H, dH, K, dK):
    Hi = H.inv()
    return (sp.Rational(1, 8)*(Hi*dH*Hi*dH).trace(), sp.Rational(1, 4)*(Hi*dK.T*H*dK).trace())
k0 = kin(Hg, dH, Kg, dK); k1 = kin(S.T*Hg*S, S.T*dH*S, S.inv()*Kg*S, S.inv()*dK*S)
print("H-kinetic invariant under squeeze:", sp.simplify(k0[0] - k1[0]) == 0,
      "| K-kinetic invariant:", sp.simplify(k0[1] - k1[1]) == 0,
      "| V_lam invariant:", sp.simplify(V_lam(Hg, Kg) - V_lam(S.T*Hg*S, S.inv()*Kg*S)) == 0)

print("\n== B. Is V_b invariant under the squeeze K -> S^-1 K S?  (finite transformation, sympy)")
al, b, c = sp.symbols('alpha b c', real=True)
K = sp.Matrix([[al, b], [c, -al]])
Ks = S.inv()*K*S
print("S^-1 K S =", Ks.tolist())
dVb = sp.factor(sp.simplify(V_b(Ks) - V_b(K)))
print("V_b(S^-1 K S) - V_b(K) =", dVb)
dVn = sp.simplify(V_naive(Ks) - V_naive(K))
print("V_naive(S^-1 K S) - V_naive(K) =", dVn, " (the naive potential IS squeeze-invariant)")
# numeric instance on the hyperboloid and on the compatible circle at H = 1
for name, Kn in (("K(phi=0.3) at H = 1 (compatible, V_lam = 0)",
                  sp.Matrix([[sp.cos(0.3), sp.sin(0.3)], [sp.sin(0.3), -sp.cos(0.3)]])),
                 ("generic hyperboloid point alpha=0.8, b=0.5, c=0.72",
                  sp.Matrix([[0.8, 0.5], [0.72, -0.8]]))):
    sv = 2
    Sn = sp.diag(sv, sp.Rational(1, sv))
    before = (V_lam(sp.eye(2), Kn) if 'phi' in name else 0) + V_b(Kn)
    Hn = sp.eye(2)
    after_lam = V_lam(Sn.T*Hn*Sn, Sn.inv()*Kn*Sn); before_lam = V_lam(Hn, Kn)
    print(f"  {name}: det K = {sp.N(Kn.det(), 6)}; s = 2:"
          f" V_lam {sp.N(before_lam.subs(lam, 1), 6)} -> {sp.N(after_lam.subs(lam, 1), 6)},"
          f" V_b/mu {sp.N(V_b(Kn).subs(mu, 1), 6)} -> {sp.N(V_b(Sn.inv()*Kn*Sn).subs(mu, 1), 6)}")
print("  invariance set of the whole squeeze group: from the factored difference, alpha = 0 (where V_b = 0)"
      " or b = c = 0 (then alpha^2 = 1, K = +-K_ref)")

print("\n== C. Continuous symmetries of V_b and of V_naive inside sp(2): solve dV(K + e[K, Xg]) = 0 for all K")
p_, q_, r_ = sp.symbols('p q r', real=True)
Xg = sp.Matrix([[p_, q_], [r_, -p_]])
eps = sp.symbols('eps')
def generators_preserving(Vfun):
    Ku = sp.Matrix([[al, b], [(1 - al**2)/b, -al]])        # hyperboloid alpha^2 + b c = 1, b != 0
    dV = sp.diff(Vfun(Ku + eps*(Ku*Xg - Xg*Ku)), eps).subs(eps, 0)
    num = sp.numer(sp.together(sp.simplify(dV)))
    eqs = sp.Poly(sp.expand(num), al, b).coeffs()
    return sp.solve(eqs, [p_, q_, r_], dict=True)
print("V_naive: generators X = [[p, q], [r, -p]] with dV = 0 identically:", generators_preserving(V_naive))
print("V_b    : generators X = [[p, q], [r, -p]] with dV = 0 identically:", generators_preserving(V_b))

print("\n== D. The flat line: V_lam + V_b along (H = diag(y, 1/y), K = K_ref), and off it")
y = sp.symbols('y', positive=True)
print("V_lam(H(X, Y), K_ref) =", sp.factor(sp.simplify(V_lam(H_of(X, Y), Kref))))
print("V_total on (diag(y, 1/y), K_ref) =", sp.simplify(V_lam(H_of(0, y), Kref) + V_b(Kref)))
print("Cauchy-Schwarz anchor: Tr(K_ref^T K_ref) =", (Kref.T*Kref).trace(), "so V_b >= -mu, equality iff K parallel to K_ref")

print("\n== E. Hessian at (1, K_ref) with lam = mu = 1")
bb, cc = sp.symbols('bb cc', real=True)
def fields_mine(Xv, Yv, bv, cv):
    a = sp.sqrt(1 - bv*cv)
    return H_of(Xv, Yv), sp.Matrix([[a, bv], [cv, -a]])
coords = [X, Y, bb, cc]
Hm, Km = fields_mine(X, Y, bb, cc)
Vtot = (V_lam(Hm, Km) + V_b(Km)).subs({lam: 1, mu: 1})
pt = {X: 0, Y: 1, bb: 0, cc: 0}
Hess = sp.Matrix(4, 4, lambda i, j: sp.simplify(sp.diff(Vtot, coords[i], coords[j]).subs(pt)))
print("Hessian in my coords (X, Y, b, c):", Hess.tolist())
print("  gradient at the point:", [sp.simplify(sp.diff(Vtot, v).subs(pt)) for v in coords])
print("  null space:", [list(v) for v in Hess.nullspace()], "(the Y direction = the squeeze line)")
# anchor to the documents' coordinates (x, y, u, t): H(x, 1 + y), K = [[a, u + t], [u - t, -a]]
x_, y_, u_, t_ = sp.symbols('x y u t', real=True)
a_ = sp.sqrt(1 - u_**2 + t_**2)
Vdoc = (V_lam(H_of(x_, 1 + y_), sp.Matrix([[a_, u_ + t_], [u_ - t_, -a_]]))
        + V_b(sp.Matrix([[a_, u_ + t_], [u_ - t_, -a_]]))).subs({lam: 1, mu: 1})
cd = [x_, y_, u_, t_]
Hd = sp.Matrix(4, 4, lambda i, j: sp.simplify(sp.diff(Vdoc, cd[i], cd[j]).subs({x_: 0, y_: 0, u_: 0, t_: 0})))
print("  in the documents' coords (x, y, u, t) the eigenvalues are", Hd.eigenvals(),
      "=", sorted(float(e) for e in Hd.eigenvals(multiple=True)), "(note v2 quotes 0, 0.764, 2, 5.236)")

print("\n== F. Physical spectrum m^2 = eig((2G)^-1 Hess) along the flat line (f_H = f_K = 1, lam = mu = 1)")
# kinetic metric from L_kin = (1/8) Tr(H^-1 dH H^-1 dH) + (1/4) Tr(H^-1 dK^T H dK)
def metric(Hm, Km):
    Hi = Hm.inv()
    Hd_ = [sp.diff(Hm, v) for v in coords]; Kd_ = [sp.diff(Km, v) for v in coords]
    G = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            G[i, j] = (sp.Rational(1, 8)*(Hi*Hd_[i]*Hi*Hd_[j]).trace()
                       + sp.Rational(1, 8)*((Hi*Kd_[i].T*Hm*Kd_[j]).trace() + (Hi*Kd_[j].T*Hm*Kd_[i]).trace()))
    return G
Gsym = metric(Hm, Km)
Vnaive_tot = (V_lam(Hm, Km) + V_naive(Km)).subs({lam: 1, mu: 1})
def spectrum(Vexpr, y0):
    p = {X: 0, Y: y0, bb: 0, cc: 0}
    grad = [float(sp.diff(Vexpr, v).subs(p)) for v in coords]
    Hn = np.array(sp.Matrix(4, 4, lambda i, j: sp.diff(Vexpr, coords[i], coords[j]).subs(p)).evalf(), dtype=float)
    Gn = np.array(Gsym.subs(p).evalf(), dtype=float)
    ev = np.linalg.eigvals(np.linalg.solve(2*Gn, Hn))
    return np.sort(ev.real), max(abs(g) for g in grad), np.max(np.abs(ev.imag))
print("y0      | grad max | m^2 with V_b (sorted)                         | sum m^2")
for y0 in (sp.Rational(1, 4), sp.Rational(1, 2), 1, 2, 4, 10):
    ev, gm, im = spectrum(Vtot, y0)
    print(f"{float(y0):7.3f} | {gm:.1e}  | {np.array2string(ev, precision=5, suppress_small=True):45s} | {ev.sum():.5f}"
          + (f"  (imag {im:.1e})" if im > 1e-9 else ""))
print("control: the naive potential, whose residual symmetry IS the squeeze (critical points, saddles):")
for y0 in (sp.Rational(1, 4), 1, 4, 10):
    ev, gm, im = spectrum(Vnaive_tot, y0)
    print(f"{float(y0):7.3f} | {gm:.1e}  | {np.array2string(ev, precision=5, suppress_small=True):45s} | {ev.sum():.5f}")

print("\n== G. One-loop consequence in 1+1 (illustration): V_1 = (1/8pi) sum_i m_i^2 [1 + ln(L^2/m_i^2)] + const")
print("The coefficient of ln(L^2) is (1/8pi) sum m^2; if it varies along the line, the classical flat")
print("direction is lifted at one loop (no symmetry keeps it flat).")
for y0 in (1, 2, 4):
    ev, _, _ = spectrum(Vtot, y0)
    nz = ev[ev > 1e-12]
    print(f"  y0 = {y0}: sum m^2 = {nz.sum():.5f};  sum m^2 (1 - ln m^2) = {np.sum(nz*(1 - np.log(nz))):.5f}")
