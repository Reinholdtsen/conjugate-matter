#!/usr/bin/env python3
"""
Cross-check of flag12_audit.py section F by a different route.

The point (diag(y0, 1/y0), K_ref) is the image of (1, K_ref) under S = diag(s, 1/s), s^2 = y0.
Kinetic terms and V_lam are Sp(2,R)-invariant (checked in flag12_audit.py A), so the spectrum at
(diag(y0, 1/y0), K_ref) equals the spectrum at (1, K_ref) of V_lam(H, K) + V_b(S^-1 K S).
If the squeeze were a symmetry of V_b, this pulled-back potential would equal V_b and the
spectrum would not depend on y0.  Also varies f_H, f_K to show the y0-dependence is not tied to
one choice of couplings.  Uses the documents' coordinates (x, y, u, t) this time.
"""
import sympy as sp
import numpy as np

w = sp.Matrix([[0, 1], [-1, 0]]); Kref = sp.diag(1, -1)
def H_of(X, Y): return sp.Matrix([[Y + X**2/Y, X/Y], [X/Y, 1/Y]])
def V_lam(H, K, lam=1):
    I = w.inv()*H; C = K*I + I*K
    return lam*sp.Rational(1, 8)*(H.inv()*C.T*H*C).trace()
def V_b(K, mu=1): return -mu*((K*Kref).trace())**2/(2*(K.T*K).trace())

x, y, u, t = sp.symbols('x y u t', real=True)
cs = [x, y, u, t]
a = sp.sqrt(1 - u**2 + t**2)
H = H_of(x, 1 + y); K = sp.Matrix([[a, u + t], [u - t, -a]])
p0 = {x: 0, y: 0, u: 0, t: 0}

def metric(fH, fK):
    Hi = H.inv(); Hd = [sp.diff(H, v) for v in cs]; Kd = [sp.diff(K, v) for v in cs]
    G = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            G[i, j] = (fH**2*sp.Rational(1, 8)*(Hi*Hd[i]*Hi*Hd[j]).trace()
                       + fK**2*sp.Rational(1, 8)*((Hi*Kd[i].T*H*Kd[j]).trace() + (Hi*Kd[j].T*H*Kd[i]).trace()))
    return np.array(G.subs(p0).evalf(), dtype=float)

def spec_pulled_back(y0, fH=1, fK=1):
    sv = sp.sqrt(sp.nsimplify(y0))
    S = sp.diag(sv, 1/sv)
    V = V_lam(H, K) + V_b(S.inv()*K*S)
    grad = max(abs(float(sp.diff(V, v).subs(p0))) for v in cs)
    Hs = np.array(sp.Matrix(4, 4, lambda i, j: sp.diff(V, cs[i], cs[j]).subs(p0)).evalf(), dtype=float)
    ev = np.linalg.eigvals(np.linalg.solve(2*metric(fH, fK), Hs))
    return np.sort(ev.real), grad

for fH, fK in ((1, 1), (2, sp.Rational(1, 2)), (sp.Rational(1, 3), 3)):
    print(f"f_H = {fH}, f_K = {fK}:")
    for y0 in (1, 2, 4, 10):
        ev, g = spec_pulled_back(y0, fH, fK)
        print(f"   y0 = {y0:>2}: grad {g:.1e}, m^2 = {np.array2string(ev, precision=5, suppress_small=True)}")

print("\nPulled-back potential minus V_b near K_ref, to second order in (u, t), s^2 = y0 symbolic:")
s = sp.symbols('s', positive=True)
S = sp.diag(s, 1/s)
e = sp.symbols('e')
diff2 = sp.series((V_b(S.inv()*K*S) - V_b(K)).subs({u: e*u, t: e*t}), e, 0, 3).removeO()
print("   ", sp.factor(sp.simplify(diff2.subs(e, 1))))
