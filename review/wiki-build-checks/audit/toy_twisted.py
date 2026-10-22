"""Audit of flag 39 in the program's one explicit rho-symmetric action: toy note s2, model I (d = 1).

Fields H(Z), Z = X + iY, and K = [[a, b], [c, -a]] on the hyperboloid a^2 + bc = 1.
Potential (toy note s2, s4): U = (lam/8) Tr(H^-1 C^T H C) + V_b,  C = K I + I K,  I = w^-1 H,
V_b = -mu [Tr(K K_ref)]^2 / (2 Tr K^T K),  K_ref = diag(1, -1);  lam = mu = 1.
Symmetry action (toy note s2): H -> S^T H S, K -> S^-1 K S; rho = [[0,1],[-1,0]]; flip K -> -K.
Vacuum (Z = i, K = K_ref). Coordinates here: Z = x + i(1 + h), b, c (a = sqrt(1 - bc)).
"""
import sympy as sp

x, h, b, c = sp.symbols("x h b c", real=True)
coords = (x, h, b, c)
w = sp.Matrix([[0, 1], [-1, 0]])
rho = sp.Matrix([[0, 1], [-1, 0]])
Kref = sp.diag(1, -1)

def H_of(X, Y):
    return sp.Matrix([[Y + X**2/Y, X/Y], [X/Y, 1/Y]])

Y = 1 + h
H = H_of(x, Y)
a = sp.sqrt(1 - b*c)
K = sp.Matrix([[a, b], [c, -a]])
I = w.inv()*H
C = K*I + I*K
U = sp.Rational(1, 8)*(H.inv()*C.T*H*C).trace() - ((K*Kref).trace())**2/(2*(K.T*K).trace())

at0 = {x: 0, h: 0, b: 0, c: 0}
grad = [sp.simplify(sp.diff(U, v).subs(at0)) for v in coords]
Hess = sp.Matrix(4, 4, lambda i, j: sp.simplify(sp.diff(U, coords[i], coords[j]).subs(at0)))
print("gradient at the vacuum:", grad)
print("Hessian at the vacuum (coords x, h, b, c):"); sp.pprint(Hess)
print("Hessian eigenvalues:", [sp.nsimplify(e) for e in Hess.eigenvals(multiple=True)],
      "numeric:", sorted(float(e) for e in Hess.eigenvals(multiple=True)))
ker = Hess.nullspace()
print("kernel (zero modes):", [list(v) for v in ker])

# twisted element: rho on (H, K), then K -> -K
Zc = x + sp.I*Y
Zp = -1/Zc
Kp = -(rho.inv()*K*rho)
img = [sp.re(sp.expand_complex(Zp)), sp.im(sp.expand_complex(Zp)) - 1, Kp[0, 1], Kp[1, 0]]
check_a = sp.simplify(Kp[0, 0] - sp.sqrt(1 - Kp[0, 1]*Kp[1, 0]))
L = sp.Matrix(4, 4, lambda i, j: sp.simplify(sp.diff(img[i], coords[j]).subs(at0)))
print("\ntwisted rho fixes the vacuum:", [sp.simplify(e.subs(at0)) for e in img] == [0, 0, 0, 0],
      "; image stays on the hyperboloid branch a > 0:", check_a == 0)
print("Jacobian L of the twisted element at the vacuum (coords x, h, b, c):"); sp.pprint(L)
print("L^2 = 1:", L*L == sp.eye(4), "; L^T Hess L == Hess (symmetry of the potential):",
      sp.simplify(L.T*Hess*L - Hess) == sp.zeros(4))
print("eigenvalues of L:", L.eigenvals())
for v in ker:
    Lv = L*v
    lam = [sp.simplify(Lv[i]/v[i]) for i in range(4) if v[i] != 0]
    print("zero mode", list(v), "-> L v =", list(Lv), "; parity", lam)

# the exact flat line of the toy note: H = diag(y, 1/y), K = K_ref, and its image
yv = sp.symbols("y", positive=True)
Hy = H_of(0, yv)
Hy_img = rho.T*Hy*rho
print("\nflat line H = diag(y, 1/y) maps to", list(Hy_img), "= diag(1/y, y): y -> 1/y, so dy -> -dy at y = 1")
print("U along the flat line:", sp.simplify(U.subs({x: 0, b: 0, c: 0, h: yv - 1})))
