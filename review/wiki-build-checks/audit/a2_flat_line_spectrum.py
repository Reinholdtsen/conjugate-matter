"""Audit of flag 12, part 2: is the flat line H = diag(y, 1/y), K = K_ref the orbit of ANY symmetry?

If some exact symmetry of the full action (kinetic + potential) carried the vacuum (1, K_ref) to the
point (diag(y, 1/y), K_ref), the small-fluctuation spectrum there -- the eigenvalues of G^-1 V'' with G
the kinetic (target-space) metric -- would be the same for every y. (Each point of the line is a global
minimum, V = -mu, so V'' is the covariant Hessian there.) A y-dependent spectrum rules out every such
symmetry, not only the conjugation squeeze, and means the one-loop effective potential, a function of
these masses, generically depends on y: the classical degeneracy is not protected.

Positive control: the naive potential V_mu = -mu[Tr(K K_ref)]^2 IS exactly squeeze-invariant (part 1),
so its spectrum along the same line must come out y-independent (it has a negative mode: a saddle).

Lagrangian as in toy note v2 Sec. 2 and verify/toy_coset.py:
  L = (f_H^2/8) Tr(H^-1 dH H^-1 dH) + (f_K^2/4) Tr(H^-1 dK^T H dK) + (lam/8) Tr(H^-1 C^T H C) + mu V_x
Coordinates: Z = X + iY for H(Z) = [[Y + X^2/Y, X/Y], [X/Y, 1/Y]]; K = [[sqrt(1 - bc), b], [c, -sqrt(1 - bc)]].
"""
import numpy as np
import sympy as sp

X, Y, b, c, y = sp.symbols('X Y b c y', real=True)
dX, dY, db, dc = sp.symbols('dX dY db dc', real=True)
fH, fK, lam, mu = sp.symbols('f_H f_K lambda mu', positive=True)
w = sp.Matrix([[0, 1], [-1, 0]])
Kref = sp.diag(1, -1)
H = sp.Matrix([[Y + X**2/Y, X/Y], [X/Y, 1/Y]])
Aq = sp.sqrt(1 - b*c)
K = sp.Matrix([[Aq, b], [c, -Aq]])
coords = [X, Y, b, c]; vel = [dX, dY, db, dc]
dH = sum((sp.diff(H, v)*dv for v, dv in zip(coords, vel)), sp.zeros(2))
dK = sum((sp.diff(K, v)*dv for v, dv in zip(coords, vel)), sp.zeros(2))
Hi = H.inv()
Lkin = fH**2/8*(Hi*dH*Hi*dH).trace() + fK**2/4*(Hi*dK.T*H*dK).trace()
I = w.inv()*H
C = K*I + I*K
Vlam = (Hi*C.T*H*C).trace()/8
Vb = -((K*Kref).trace())**2/(2*(K.T*K).trace())
Vmu = -((K*Kref).trace())**2
pt = {X: 0, Y: y, b: 0, c: 0}

G = sp.Matrix(4, 4, lambda i, j: sp.diff(Lkin, vel[i], vel[j])).subs(pt)
G = sp.simplify(G)
print("kinetic metric G at (diag(y,1/y), K_ref), coordinates (X, Y, b, c):")
sp.pprint(G)

def analyse(name, Vx):
    V = lam*Vlam + mu*Vx
    grad = [sp.simplify(sp.diff(V, v).subs(pt)) for v in coords]
    Hs = sp.simplify(sp.Matrix(4, 4, lambda i, j: sp.diff(V, coords[i], coords[j]).subs(pt)))
    M2 = sp.simplify(G.inv()*Hs)
    print(f"\n== {name}")
    print("   V on the line:", sp.simplify(V.subs(pt)), "; gradient on the line:", grad)
    print("   mass matrix G^-1 V'' (symbolic in y):")
    sp.pprint(M2)
    print("   trace G^-1 V'' =", sp.simplify(M2.trace()))
    fM = sp.lambdify((y, fH, fK, lam, mu), M2, 'numpy')
    for (fh, fk, la, m) in ((1, 1, 1, 1), (1, 2, 3, 0.5)):
        print(f"   f_H={fh}, f_K={fk}, lambda={la}, mu={m}:")
        for yv in (0.25, 0.5, 1.0, 2.0, 4.0):
            ev = np.sort(np.linalg.eigvals(np.array(fM(yv, fh, fk, la, m), dtype=float)).real)
            nz = ev[np.abs(ev) > 1e-12]
            pos = nz[nz > 0]
            print(f"     y = {yv:<5}: masses^2 {np.array2string(ev, precision=5)}"
                  f"  Tr M^2 = {ev.sum():.5f}  sum ln m^2 (nonzero, positive) = {np.log(pos).sum():.5f}")
    return M2

M2b = analyse("bounded variant V_b (Frobenius norm, as in the documents)", Vb)
M2m = analyse("positive control: naive V_mu = -mu [Tr(K K_ref)]^2 (exactly squeeze-invariant)", Vmu)

# the referee's/adjudicator's coordinate Hessian at y = 1 (lambda = mu = 1), to tie this to the quoted [0, 0.764, 2, 5.236]
Hs1 = sp.Matrix(4, 4, lambda i, j: sp.diff(Vlam + Vb, coords[i], coords[j]).subs({X: 0, Y: 1, b: 0, c: 0}))
print("\nplain coordinate Hessian of V_lam + V_b at (1, K_ref) in (X, Y, b, c):", [sp.nsimplify(e) for e in Hs1.eigenvals(multiple=True)],
      "=", np.round(np.sort(np.array([float(e) for e in Hs1.eigenvals(multiple=True)])), 4))
ev1 = Hs1.eigenvects()
for val, mult, vecs in ev1:
    if val == 0:
        print("   zero-mode eigenvector (X, Y, b, c):", list(vecs[0]), "-> pure dY: the squeeze direction along the flat line")
