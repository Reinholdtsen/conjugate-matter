#!/usr/bin/env python3
"""
Independent recomputation for flag 40 (review/wiki-build-flags.md).

Source statement (root CLAUDE.md, round-4 lesson):
  "Round 4 found a potential that was bounded only at frozen H."

Model, from papers/reciprocity-toy-models.md (v2) §2 and §4, built from the raw
definitions (no formula from the flag or its check script is used):
  w = [[0,1],[-1,0]];  H(Z) = [[Y + X^2/Y, X/Y],[X/Y, 1/Y]];  I = w^-1 H
  K real 2x2, traceless, det K = -1 (target: hyperboloid a^2 + bc = 1)
  V_lam = (lam/8) Tr(H^-1 C^T H C),  C = K I + I K        (§2)
  V_mu  = -mu [Tr(K K_ref)]^2   (the naive potential, §4)
  K_ref identified from §4's "At H = 1, V_b = -(mu/2)(1 + cos 2 phi)".

Coordinates on K's target: my own global chart of dS_2,
  a = cosh s cos f,  (b + c)/2 = cosh s sin f,  (b - c)/2 = sinh s,
not the (u, t) chart of verify/toy_coset.py; that chart is evaluated only at
the end, to compare with the numbers the flag quotes.
"""
import sympy as sp
import numpy as np

w = sp.Matrix([[0, 1], [-1, 0]])
def H_of(X, Y):
    return sp.Matrix([[Y + X**2/Y, X/Y], [X/Y, 1/Y]])
lam, mu, fK = sp.symbols("lambda mu f_K", positive=True)
s, f = sp.symbols("s f", real=True)

def V_lam(H, K):
    I = w.inv()*H
    C = K*I + I*K
    return lam/8*(H.inv()*C.T*H*C).trace()
def V_mu(K, Kref):
    return -mu*((K*Kref).trace())**2

print("== 0. Anchors (textbook identities, independent of the paper)")
A = sp.Matrix(2, 2, sp.symbols("m0:4"))
print("  2x2 identity M^T w M = det(M) w:", sp.simplify(A.T*w*A - A.det()*w) == sp.zeros(2))
a_, b_, c_ = sp.symbols("a b c", real=True)
Kg = sp.Matrix([[a_, b_], [c_, -a_]])
print("  Cayley-Hamilton: traceless K has K^2 = -det(K) * 1:",
      sp.simplify(Kg**2 + Kg.det()*sp.eye(2)) == sp.zeros(2),
      "-> det K = -1 gives K^2 = 1 and K^T w K = -w")
Kc = sp.Matrix([[sp.cosh(s)*sp.cos(f), sp.cosh(s)*sp.sin(f) + sp.sinh(s)],
                [sp.cosh(s)*sp.sin(f) - sp.sinh(s), -sp.cosh(s)*sp.cos(f)]])
print("  chart: trace", sp.simplify(Kc.trace()), "| det", sp.simplify(Kc.det()),
      "| K^2 - 1 =", sp.simplify(Kc**2 - sp.eye(2)).tolist(),
      "| K^T w K + w =", sp.simplify(Kc.T*w*Kc + w).tolist())
# surjectivity: invert random hyperboloid points
rng = np.random.default_rng(11)
worst = 0.0
for _ in range(2000):
    av, bv = rng.normal(scale=4), rng.normal(scale=4)
    cv = (1 - av**2)/bv
    q, p = (bv - cv)/2, (bv + cv)/2
    sv = np.arcsinh(q); fv = np.arctan2(p, av)
    Kn = np.array([[np.cosh(sv)*np.cos(fv), np.cosh(sv)*np.sin(fv) + np.sinh(sv)],
                   [np.cosh(sv)*np.sin(fv) - np.sinh(sv), -np.cosh(sv)*np.cos(fv)]])
    worst = max(worst, np.abs(Kn - np.array([[av, bv], [cv, -av]])).max())
print(f"  chart covers the hyperboloid: max reconstruction error over 2000 random points = {worst:.2e}")

print("\n== 1. Identify K_ref from §4: V_b(H=1, K(phi)) = -(mu/2)(1 + cos 2 phi)")
phi = sp.symbols("phi", real=True)
Kphi = sp.Matrix([[sp.cos(phi), sp.sin(phi)], [sp.sin(phi), -sp.cos(phi)]])
for name, Kr in (("diag(1,-1)", sp.diag(1, -1)), ("diag(-1,1)", sp.diag(-1, 1)), ("[[0,1],[1,0]]", sp.Matrix([[0, 1], [1, 0]]))):
    Vb = -mu*((Kphi*Kr).trace())**2/(2*(Kphi.T*Kphi).trace())
    print(f"  K_ref = {name:14s}: V_b - [-(mu/2)(1+cos2phi)] = {sp.simplify(Vb + mu/2*(1 + sp.cos(2*phi)))}")
Kref = sp.diag(1, -1)

print("\n== 2. Frozen H = 1 (Z = i), K free on its whole target (the model as defined in §2)")
H1 = H_of(0, 1)
print("  H(Z=i) =", H1.tolist())
V1 = sp.simplify(sp.expand(V_lam(H1, Kc) + V_mu(Kc, Kref)).rewrite(sp.exp))
V1 = sp.simplify(V1.rewrite(sp.cosh))
target = lam*sp.sinh(s)**2 - 4*mu*sp.cosh(s)**2*sp.cos(f)**2
print("  V(s, f) - [lam sinh^2 s - 4 mu cosh^2 s cos^2 f] =", sp.simplify((V1 - target).rewrite(sp.exp)))
Vf0 = sp.simplify((V1.subs(f, 0)).rewrite(sp.exp))
print("  along f = 0:  V + 4 mu - (lam - 4 mu) sinh^2 s =",
      sp.simplify((Vf0 + 4*mu - (lam - 4*mu)*sp.sinh(s)**2).rewrite(sp.exp)))
Vnum = sp.lambdify((s, f, lam, mu), target, "numpy")
print("  lam = mu = 1, f = 0 (K stays off the circle along s):")
for sv in (0.0, 1.0, 2.0, 5.0, float(np.arcsinh(100.0))):
    print(f"    s = {sv:8.5f}  (sinh s = {np.sinh(sv):9.4f}):  V = {Vnum(sv, 0.0, 1.0, 1.0):.6f}")
print("  restricted to the circle (s = 0): V(0, f) + 2mu(1 + cos 2f) =",
      sp.simplify(sp.expand_trig(sp.simplify(V1.subs(s, 0).rewrite(sp.cos)) + 2*mu*(1 + sp.cos(2*f)))))
fs = np.linspace(0, 2*np.pi, 2001)
vc = Vnum(0.0, fs, 1.0, 1.0)
print(f"    numeric range on the circle at lam = mu = 1: [{vc.min():.6f}, {vc.max():.6f}]")

print("\n== 3. Frozen H = 1: boundedness against lam/mu (mu = 1)")
S, F = np.meshgrid(np.linspace(-12, 12, 2401), np.linspace(-np.pi, np.pi, 721))
for lv in (0.5, 1.0, 2.0, 3.0, 3.9, 4.0, 4.1, 5.0, 10.0, 100.0):
    Vg = Vnum(S, F, lv, 1.0)
    i = np.unravel_index(np.argmin(Vg), Vg.shape)
    print(f"  lam = {lv:6.1f}: min V on |s| <= 12 grid = {Vg.min(): .6e} at s = {S[i]: .3f}, f = {F[i]: .3f};"
          f"  V(s=12, f=0) = {Vnum(12.0, 0.0, lv, 1.0): .4e}")
# lower bound for lam >= 4 mu: V >= lam sinh^2 - 4 mu cosh^2 = -4 mu + (lam - 4 mu) sinh^2 s >= -4 mu
lb = sp.simplify((lam*sp.sinh(s)**2 - 4*mu*sp.cosh(s)**2 - (-4*mu + (lam - 4*mu)*sp.sinh(s)**2)).rewrite(sp.exp))
print("  bound: lam sinh^2 s - 4mu cosh^2 s - [-4mu + (lam-4mu) sinh^2 s] =", lb,
      "-> V >= -4 mu for every K iff lam >= 4 mu (equality line at lam = 4 mu)")

print("\n== 4. Frozen-H Hessian and mass^2 at K_ref = (s, f) = (0, 0)")
Hs = sp.hessian(target, (s, f)).subs({s: 0, f: 0})
print("  Hessian in (s, f):", sp.simplify(Hs).tolist())
grad = [sp.simplify(sp.diff(target, v).subs({s: 0, f: 0})) for v in (s, f)]
print("  gradient at K_ref:", grad, "(critical point)")
# kinetic metric at H = 1: L_kin = (f_K^2/4) Tr(dK^T dK) = (1/2) G_ij dq^i dq^j
J = [sp.diff(Kc, v) for v in (s, f)]
g = sp.Matrix(2, 2, lambda i, j: sp.simplify(((J[i].T*J[j]).trace() + (J[j].T*J[i]).trace())/2)).subs({s: 0, f: 0})
G = fK**2/2*g
print("  kinetic metric G at K_ref:", G.tolist())
M2 = sp.simplify(G.inv()*Hs)
print("  mass^2 matrix G^-1 Hess:", M2.tolist())
print("  at lam = mu = 1, f_K = 1: mass^2 =", [sp.nsimplify(e) for e in M2.subs({lam: 1, mu: 1, fK: 1}).eigenvals(multiple=True)])

print("\n== 5. The same frozen-H potential in verify/toy_coset.py's chart (u, t), to compare with the flag")
u, t = sp.symbols("u t", real=True)
Kut = sp.Matrix([[sp.sqrt(1 - u**2 + t**2), u + t], [u - t, -sp.sqrt(1 - u**2 + t**2)]])
Vut = sp.simplify(sp.expand(V_lam(H1, Kut) + V_mu(Kut, Kref)))
print("  V(u, t) =", sp.expand(Vut), "| minus flag's form:", sp.simplify(Vut - (-4*mu + 4*mu*u**2 + (lam - 4*mu)*t**2)))
Hut = sp.hessian(Vut, (u, t)).subs({u: 0, t: 0, lam: 1, mu: 1})
print("  Hessian at (0,0), lam = mu = 1:", Hut.tolist(), "eigenvalues", Hut.eigenvals())
print("  V(u=0, t=100), lam = mu = 1:", Vut.subs({u: 0, t: 100, lam: 1, mu: 1}))

print("\n== 6. H dynamical: the boost family of §4 (H = S^T S, K = S^-1 K0 S)")
tb = sp.symbols("tb", real=True)
Sb = sp.Matrix([[sp.cosh(tb), sp.sinh(tb)], [sp.sinh(tb), sp.cosh(tb)]])
Hb, Kb = Sb.T*Sb, Sb.inv()*Kref*Sb
print("  S symplectic:", sp.simplify(Sb.T*w*Sb - w) == sp.zeros(2))
print("  V_lam on family =", sp.simplify(V_lam(Hb, Kb)), "| V_mu on family =", sp.simplify(V_mu(Kb, Kref)))
Vmu_b = sp.lambdify(tb, sp.simplify(V_mu(Kb, Kref)).subs(mu, 1))
print("  V_mu (mu = 1) at tb = 0, 1, 2, 4:", [f"{Vmu_b(x):.6g}" for x in (0.0, 1.0, 2.0, 4.0)],
      "-> unbounded for every lam (V_lam = 0 on the family)")

print("\n== 7. Full 4x4 Hessian at (1, K_ref), toy_coset chart (x, y, u, t), H = H(x, 1 + y)")
x, y = sp.symbols("x y", real=True)
Vfull = V_lam(H_of(x, 1 + y), Kut) + V_mu(Kut, Kref)
coords = (x, y, u, t)
Hfull = sp.hessian(Vfull, coords).subs({x: 0, y: 0, u: 0, t: 0})
Hfull = sp.simplify(Hfull)
print("  symbolic Hessian:", Hfull.tolist())
for lv in (1, 4, 10, 100):
    Hn = np.array(Hfull.subs({lam: lv, mu: 1}).evalf(), dtype=float)
    ev, vec = np.linalg.eigh(Hn)
    neg = vec[:, 0]
    print(f"  lam = {lv:3d}, mu = 1: eigenvalues {np.round(ev, 4)};"
          f" lowest mode weights (x, y, u, t)^2 = {np.round(neg**2, 3)};"
          f" frozen-H (u,t) block eigenvalues {np.round(np.linalg.eigvalsh(Hn[2:, 2:]), 4)}")
# kinetic metric at (1, K0): H part (f_H^2/8) Tr(H^-1 dH H^-1 dH) -> G_H; K part as above
JH = [sp.diff(H_of(x, 1 + y), v).subs({x: 0, y: 0}) for v in (x, y)]
gH = sp.Matrix(2, 2, lambda i, j: (JH[i]*JH[j]).trace())
JK = [sp.diff(Kut, v).subs({u: 0, t: 0}) for v in (u, t)]
gK = sp.Matrix(2, 2, lambda i, j: ((JK[i].T*JK[j]).trace() + (JK[j].T*JK[i]).trace())/2)
print("  Tr(dH dH) metric in (x, y):", gH.tolist(), "| Tr(dK^T dK) metric in (u, t):", gK.tolist())
Gfull = sp.diag(*(sp.Rational(1, 4)*gH).diagonal(), *(sp.Rational(1, 2)*gK).diagonal())  # f_H = f_K = 1
for lv in (1, 10):
    Mn = np.array((Gfull.inv()*Hfull.subs({lam: lv, mu: 1})).evalf(), dtype=float)
    print(f"  lam = {lv:3d}: mass^2 (f_H = f_K = 1) = {np.round(np.sort(np.linalg.eigvals(Mn).real), 4)}")

print("\n== 8. Round-4 referee's chart (X, Y, b, c) with a = sqrt(1 - bc), H = H(X, Y) at Y = 1")
Xr, Yr, br, cr = sp.symbols("X Y b c", real=True)
Kbc = sp.Matrix([[sp.sqrt(1 - br*cr), br], [cr, -sp.sqrt(1 - br*cr)]])
Vr = V_lam(H_of(Xr, Yr), Kbc) + V_mu(Kbc, Kref)
Hr = sp.hessian(Vr, (Xr, Yr, br, cr)).subs({Xr: 0, Yr: 1, br: 0, cr: 0, lam: 1, mu: 1})
evr = np.linalg.eigvalsh(np.array(Hr.evalf(), dtype=float))
print("  full Hessian eigenvalues, lam = mu = 1:", np.round(evr, 4),
      "| frozen-H (b, c) block:", np.round(np.linalg.eigvalsh(np.array(Hr[2:, 2:].evalf(), dtype=float)), 4))
