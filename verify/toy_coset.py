#!/usr/bin/env python3
"""
toy_coset.py — baseline toy for spontaneously broken reciprocity
(notes/toy-lagrangian.md, criteria S1-S3), d = 1.

    .venv/bin/python verify/toy_coset.py

Exit code 1 if any check fails.

Fields on a 1+1 (or any) dimensional base, valued in phase-space structures
on R^2 with the rigid symplectic form w = [[0,1],[-1,0]]:
  H  positive symmetric with H^T w^-1 ... i.e. H in Sp(2)/U(1) (the upper
     half-plane, H = H(Z), Z = X + iY), and I = w^-1 H, I^2 = -1;
  K  a real structure with K^2 = 1 and K^T w K = -w (for 2x2: traceless,
     det K = -1); eta = w K is the neutral metric.
Lagrangian (Euclidean signs):
  L = (f_H^2/8) Tr(H^-1 dH H^-1 dH) + (f_K^2/4) Tr(H^-1 dK^T H dK) + V,
  V = (lam/8) Tr(H^-1 C^T H C),  C = K I + I K.
Symmetry: S in Sp(2,R) acting by H -> S^T H S, K -> S^-1 K S.
rho = [[0,1],[-1,0]] (the Born rotation (x,p) -> (p,-x)) is an element.
"""
import sys
import sympy as sp

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def zero(M):
    return all(sp.simplify(e) == 0 for e in sp.Matrix(M))

w = sp.Matrix([[0, 1], [-1, 0]])
rho = sp.Matrix([[0, 1], [-1, 0]])
def H_of(X, Y):
    return sp.Matrix([[Y + X**2/Y, X/Y], [X/Y, 1/Y]])
def terms(H, dH, K, dK):
    Hi = H.inv()
    I = w.inv()*H
    C = K*I + I*K
    return (sp.Rational(1, 8)*(Hi*dH*Hi*dH).trace(),
            sp.Rational(1, 4)*(Hi*dK.T*H*dK).trace(),
            sp.Rational(1, 8)*(Hi*C.T*H*C).trace())

print("== Anchors")
X, Y = sp.symbols("X Y", real=True)
HZ = H_of(X, Y)
check("H(Z) is symplectic and I = w^-1 H squares to -1",
      zero(HZ.T*w*HZ - w) and zero((w.inv()*HZ)**2 + sp.eye(2)))
check("rho is symplectic and is the quarter turn: rho^2 = -1", zero(rho.T*w*rho - w) and zero(rho**2 + sp.eye(2)))

print("\n== S1: the action is invariant under Sp(2,R), hence under rho")
h11, h12, h22, d11, d12, d22 = sp.symbols("h11 h12 h22 d11 d12 d22")
k = sp.symbols("k0:4"); q = sp.symbols("q0:4")
H = sp.Matrix([[h11, h12], [h12, h22]]); dH = sp.Matrix([[d11, d12], [d12, d22]])
K = sp.Matrix(2, 2, k); dK = sp.Matrix(2, 2, q)
s1, s2, s3 = sp.symbols("s1 s2 s3", nonzero=True)
S = sp.Matrix([[s1, s2], [s3, (1 + s2*s3)/s1]])
check("generic S is symplectic", zero(S.T*w*S - w))
base = terms(H, dH, K, dK)
moved = terms(S.T*H*S, S.T*dH*S, S.inv()*K*S, S.inv()*dK*S)
for name, a, b_ in zip(("H kinetic", "K kinetic", "potential"), base, moved):
    check(f"{name} term invariant under generic symplectic S", sp.simplify(a - b_) == 0)
moved_rho = terms(rho.T*H*rho, rho.T*dH*rho, rho.inv()*K*rho, rho.inv()*dK*rho)
check("all three terms invariant under rho", all(sp.simplify(a - b_) == 0 for a, b_ in zip(base, moved_rho)))
flipped = terms(H, dH, -K, -dK)
check("all three terms invariant under K -> -K", all(sp.simplify(a - b_) == 0 for a, b_ in zip(base, flipped)))

import numpy as np
rng = np.random.default_rng(3)
def num_H(Xv, Yv):
    return np.array([[Yv + Xv**2/Yv, Xv/Yv], [Xv/Yv, 1/Yv]])
pos = []
for _ in range(200):
    Hn = num_H(rng.normal(), np.exp(rng.normal())); dKn = rng.normal(size=(2, 2))
    pos.append(np.trace(np.linalg.inv(Hn) @ dKn.T @ Hn @ dKn))
check("the K kinetic term Tr(H^-1 dK^T H dK) is positive for random H and dK (no ghost)", min(pos) > 0)
db, dc = sp.symbols("db dc", real=True)
dK0 = sp.Matrix([[0, db], [dc, 0]])           # tangent to {a^2 + bc = 1} at K0 = diag(1, -1)
check("the naive Tr(dK dK) is indefinite on K's target space (de Sitter): 2 db dc",
      sp.expand((dK0*dK0).trace()) == 2*db*dc)

print("\n== S2: vacua")
a, b, c = sp.symbols("a b c", real=True)
Kg = sp.Matrix([[a, b], [c, -a]])
I0 = w.inv()*sp.eye(2)
C0 = Kg*I0 + I0*Kg
normC = sp.factor(sum(e**2 for e in C0))
check("at H = 1, |C|^2 = 2 (b - c)^2: V = 0 exactly when K is symmetric", sp.simplify(normC - 2*(b - c)**2) == 0,
      str(normC))
phi = sp.symbols("phi", real=True)
Kphi = sp.Matrix([[sp.cos(phi), sp.sin(phi)], [sp.sin(phi), -sp.cos(phi)]])
check("K(phi) is a compatible real structure for every phi",
      zero(Kphi**2 - sp.eye(2)) and zero(Kphi.T*w*Kphi + w) and zero(Kphi*I0 + I0*Kphi))
check("V vanishes on the circle K(phi) at H = 1",
      sp.simplify(terms(sp.eye(2), sp.zeros(2), Kphi, sp.zeros(2))[2]) == 0)
check("V >= 0: V = (lam/8)|C|^2_H is a sum of squares at H = 1",
      sp.simplify(terms(sp.eye(2), sp.zeros(2), Kg, sp.zeros(2))[2] - sum(e**2 for e in C0)/8) == 0)
check("rho maps the vacuum (1, K(phi)) to (1, -K(phi)) = (1, K(phi + pi))",
      zero(rho.T*rho - sp.eye(2)) and zero(rho.inv()*Kphi*rho + Kphi) and
      zero(rho.inv()*Kphi*rho - Kphi.subs(phi, phi + sp.pi)))
# A rho-fixed vacuum needs rho^T H rho = H (only Z = i, i.e. H = 1) and rho^-1 K rho = K.
check("no vacuum is rho-invariant: at H = 1 a compatible K with rho^-1 K rho = K must vanish",
      sp.solve(list(rho.inv()*Kphi*rho - Kphi), phi) == [])
Zs = sp.symbols("Zs")
check("rho acts on Z as Z -> -1/Z with fixed point Z = i",
      zero(rho.T*H_of(X, Y)*rho - H_of(-X/(X**2 + Y**2), Y/(X**2 + Y**2))))
s = sp.symbols("t0:4")
Sg = sp.Matrix(2, 2, s)
K0 = sp.Matrix([[1, 0], [0, -1]])
stab = sp.solve(list(Sg.T*Sg - sp.eye(2)) + list(K0*Sg - Sg*K0) + [Sg.det() - 1], s, dict=True)
check("the stabilizer of the vacuum (1, K0) in Sp(2,R) is {+1, -1} (so the orbit is 3-dimensional)",
      sorted([tuple(sp.Matrix(2, 2, [d[x] for x in s])) for d in stab]) == [(-1, 0, 0, -1), (1, 0, 0, 1)])

print("\n== S3: order parameter")
check("O = K_11 takes +1 in (1, K0) and -1 in its rho-image (1, -K0)",
      K0[0, 0] == 1 and (rho.inv()*K0*rho)[0, 0] == -1)

print("\n== Spectrum at the vacuum (1, K0): 4 fields, 3-dim vacuum manifold")
x, y, u, t = sp.symbols("x y u t", real=True)
Hf = H_of(x, 1 + y)
af = sp.sqrt(1 - u**2 + t**2)
Kf = sp.Matrix([[af, u + t], [u - t, -af]])
coords = [x, y, u, t]
Vf = terms(Hf, sp.zeros(2), Kf, sp.zeros(2))[2]
hess = sp.Matrix(4, 4, lambda i, j: sp.diff(Vf, coords[i], coords[j])).subs({x: 0, y: 0, u: 0, t: 0})
hess = sp.simplify(hess)
ev = [sp.nsimplify(e) for e in hess.eigenvals(multiple=True)]
check("potential Hessian has rank 1: three flat directions (Goldstones), one massive", hess.rank() == 1, str(ev))

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — the coset baseline meets S1-S3 classically.")
