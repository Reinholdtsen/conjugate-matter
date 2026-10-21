# Is the squeeze S = diag(a, 1/a) a symmetry of lambda*V_lam + V_b (as ADJ4 F2 says) or not (as TN v2 says)?
import sympy as sp
a, A, b, c = sp.symbols('a A b c', positive=True)
w = sp.Matrix([[0, 1], [-1, 0]])
Kref = sp.diag(1, -1)
def Vb(K): return -((K*Kref).trace())**2/(2*(K.T*K).trace())
def Vlam(H, K):
    I = w.inv()*H; C = K*I + I*K
    return (H.inv()*C.T*H*C).trace()/8
K = sp.Matrix([[A, b], [c, -A]])
S = sp.diag(a, 1/a)
H = sp.eye(2)
tot = Vlam(H, K) + Vb(K)
tot_s = Vlam(S.T*H*S, S.inv()*K*S) + Vb(S.inv()*K*S)
print("lambda-term invariant under squeeze:", sp.simplify(Vlam(S.T*H*S, S.inv()*K*S) - Vlam(H, K)) == 0)
d = sp.simplify(Vb(S.inv()*K*S) - Vb(K))
print("V_b(S^-1 K S) - V_b(K) =", sp.factor(d))
vals = {a: 2, A: sp.Rational(1, 2), b: 1, c: sp.Rational(3, 4)}  # a^2 + bc = 1/4 + 3/4 = 1, on the hyperboloid
print("numeric example (a=2, K=[[1/2,1],[3/4,-1/2]]): V_b change =", sp.nsimplify(d.subs(vals)))
print("on the line K = K_ref:", sp.simplify(Vb(S.inv()*Kref*S) - Vb(Kref)))
