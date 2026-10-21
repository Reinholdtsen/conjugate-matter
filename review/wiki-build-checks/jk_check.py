# Is the J/K naming conflict (master-topics C27) only nominal?
# #11 §5: with omega, eta standard, I = w^-1 H, J = eta^-1 H, K = eta^-1 w; I^2=-1, J^2=K^2=+1, IJ=K.
# P2' writes eta = HJ; the toy note writes eta = wK. Check both equal the standard eta on the
# compatible family H = diag(g, g^-1) (d = 2, generic symmetric positive g), and that the toy's
# reference vacuum K0 = diag(1,-1) is #11's K up to sign (d = 1).
import sympy as sp
a, b, c = sp.symbols('a b c', positive=True)
g = sp.Matrix([[a, b], [b, c]])
Z, One = sp.zeros(2), sp.eye(2)
w = sp.Matrix(sp.BlockMatrix([[Z, One], [-One, Z]]))
eta = sp.Matrix(sp.BlockMatrix([[Z, One], [One, Z]]))
H = sp.Matrix(sp.BlockMatrix([[g, Z], [Z, g.inv()]]))
I = w.inv()*H; J = eta.inv()*H; K = eta.inv()*w
s = lambda M: sp.simplify(M)
print("I^2 = -1:", s(I*I + sp.eye(4)) == sp.zeros(4))
print("J^2 = +1:", s(J*J - sp.eye(4)) == sp.zeros(4))
print("K^2 = +1:", s(K*K - sp.eye(4)) == sp.zeros(4))
print("IJ = K:  ", s(I*J - K) == sp.zeros(4))
print("HJ = eta:", s(H*J - eta) == sp.zeros(4))
print("wK = eta:", s(w*K - eta) == sp.zeros(4))
print("HJ = wK: ", s(H*J - w*K) == sp.zeros(4))
# d = 1, H = 1: #11's K versus the toy's K0
w1 = sp.Matrix([[0, 1], [-1, 0]]); eta1 = sp.Matrix([[0, 1], [1, 0]])
K11 = eta1.inv()*w1; J11 = eta1.inv()*sp.eye(2); K0 = sp.diag(1, -1)
print("d=1: #11 K =", K11.tolist(), "; toy K0 =", K0.tolist(), "; K0 == -K11:", K0 == -K11)
print("d=1: #11 J =", J11.tolist(), "(= toy K(phi) at phi = pi/2)")
