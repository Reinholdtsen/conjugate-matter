"""Is a normalised variant V' = -mu [Tr(K K_ref)]^2 / (2 Tr(K^T K)) bounded and rho-invariant? (candidate fix only)"""
import numpy as np, sympy as sp
rng = np.random.default_rng(9)
Kr = np.diag([1., -1.]); rho = np.array([[0., 1.], [-1., 0.]])
vals, inv = [], []
for _ in range(200000):
    b, c = rng.normal(scale=rng.choice([0.3, 3, 30]), size=2)
    if 1 - b*c < 0: continue
    a = rng.choice([-1, 1])*np.sqrt(1 - b*c)
    K = np.array([[a, b], [c, -a]])
    V = -np.trace(K@Kr)**2/(2*np.trace(K.T@K))
    Kp = np.linalg.inv(rho)@K@rho
    Vp = -np.trace(Kp@Kr)**2/(2*np.trace(Kp.T@Kp))
    vals.append(V); inv.append(abs(V - Vp))
print("samples:", len(vals), " min V'/mu =", min(vals), " max V'/mu =", max(vals), " max |V'(rho K) - V'(K)| =", max(inv))
t = sp.symbols('t', real=True)
Kt = sp.Matrix([[sp.cosh(2*t), sp.sinh(2*t)], [-sp.sinh(2*t), -sp.cosh(2*t)]])
Vt = -((Kt*sp.diag(1, -1)).trace())**2/(2*(Kt.T*Kt).trace())
print("on the runaway family: V'(t)/mu =", sp.simplify(Vt), "; t->oo limit:", sp.limit(Vt, t, sp.oo))
