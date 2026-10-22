"""Flag 40 audit: is the naive potential -mu[Tr(K K_ref)]^2 'bounded at frozen H'?

Independent of review/wiki-build-checks/frozen_h_naive.py: other coordinates
((b, c) with a^2 = 1 - bc; hyperbolic (s, th) on the hyperboloid), and the potential
is built numerically from the toy note's own definitions:
  V_lam = (1/8) Tr(H^-1 C^T H C), C = K I + I K, I = w^-1 H   (toy note §2)
  V_mu  = -mu [Tr(K K_ref)]^2                                 (toy note §4, naive form)
Three readings of 'frozen H' are tested:
  R1  the documents' frozen-H reduction: H = 1 and K on its compatible circle K(phi)
  R2  H = 1 fixed, K free on its whole target, lam >= 4 mu
  R3  H = 1 fixed, K free on its whole target, at the quoted lam = mu = 1
"""
import numpy as np
import sympy as sp

np.set_printoptions(precision=4, suppress=True)
w = np.array([[0., 1.], [-1., 0.]])
Kref = np.diag([1., -1.])
MU = 1.0


def V_lam(H, K):
    I = np.linalg.inv(w) @ H
    C = K @ I + I @ K
    return np.trace(np.linalg.inv(H) @ C.T @ H @ C) / 8


def V_mu(K):
    return -MU * np.trace(K @ Kref) ** 2


def on_target(K):
    return (abs(np.trace(K)) < 1e-9 and np.allclose(K @ K, np.eye(2), atol=1e-6 * max(1, np.abs(K).max() ** 2))
            and np.allclose(K.T @ w @ K, -w, atol=1e-6 * max(1, np.abs(K).max() ** 2)))


def K_hyp(s, th):
    """hyperboloid a^2 + bc = 1 in hyperbolic coordinates: a = cosh s cos th, (b+c)/2 = cosh s sin th, (b-c)/2 = sinh s"""
    a, u, t = np.cosh(s) * np.cos(th), np.cosh(s) * np.sin(th), np.sinh(s)
    return np.array([[a, u + t], [u - t, -a]])


print("== A. Anchors (textbook identities, independent of the paper)")
a, b, c = sp.symbols("a b c", real=True)
Ks = sp.Matrix([[a, b], [c, -a]]); ws = sp.Matrix([[0, 1], [-1, 0]])
print("  Cayley-Hamilton, traceless 2x2: K^2 + det(K) 1 =", list(sp.expand(Ks * Ks + Ks.det() * sp.eye(2))))
print("  K^T w K - det(K) w =", list(sp.expand(Ks.T * ws * Ks - Ks.det() * ws)))
rng = np.random.default_rng(40)
pts = [(rng.uniform(0, 6), rng.uniform(0, 2 * np.pi)) for _ in range(200)]
print("  K_hyp(s, th) on the target (K^2 = 1, K^T w K = -w, traceless) at 200 random points:",
      all(on_target(K_hyp(s, th)) for s, th in pts))

print("\n== B. Reading R3: H = 1 fixed, K free, lam = mu = 1 (the couplings of the gated -6.47)")
lam = 1.0
for T in (0.0, 10.0, 100.0):
    s = np.arcsinh(T)
    K = K_hyp(s, 0.0)
    print(f"  (b-c)/2 = {T:6.1f}: on target {on_target(K)}, lam*V_lam = {lam * V_lam(np.eye(2), K):10.2f}, "
          f"V_mu = {V_mu(K):10.2f}, total = {lam * V_lam(np.eye(2), K) + V_mu(K):10.2f}")

print("\n== C. Closed form at H = 1 in (b, c), a^2 = 1 - bc (sympy, from the matrix definitions)")
lam_s, mu_s = sp.symbols("lam mu", positive=True)
Is = ws.inv() * sp.eye(2)
Cs = Ks * Is + Is * Ks
Vtot = sp.expand(lam_s * sp.Rational(1, 8) * (Cs.T * Cs).trace() - mu_s * ((Ks * sp.diag(1, -1)).trace()) ** 2)
Vtot = sp.expand(Vtot.subs(a ** 2, 1 - b * c))
print("  V(H = 1) =", Vtot)
tau = sp.symbols("tau", real=True)
print("  along b = -c = tau (the incompatible, non-compact direction):", sp.factor(sp.expand(Vtot.subs({b: tau, c: -tau}))))
print("  on the compatible circle b = c (K symmetric):", sp.factor(sp.expand(Vtot.subs(c, b))))

print("\n== D. Boundedness at H = 1 with K free, by grid search over the hyperboloid (mu = 1)")
S = np.linspace(0, 8, 401); TH = np.linspace(0, 2 * np.pi, 361)
for lam in (1.0, 3.9, 4.0, 4.1, 10.0, 100.0):
    vals = np.array([[lam * V_lam(np.eye(2), K_hyp(s, th)) + V_mu(K_hyp(s, th)) for th in TH] for s in S])
    i, j = np.unravel_index(vals.argmin(), vals.shape)
    print(f"  lam = {lam:5.1f}: min V over s <= 8 = {vals.min():12.4e} at s = {S[i]:.2f}, th = {TH[j]:.3f}; "
          f"min over s <= 4 = {vals[S <= 4].min():10.4e}")

print("\n== E. Frozen-H Hessian at (1, K_ref), two coordinate systems (finite differences on the numeric V)")
def Kbc(bv, cv):
    av = np.sqrt(1 - bv * cv); return np.array([[av, bv], [cv, -av]])
def Kut(uv, tv):
    av = np.sqrt(1 - uv ** 2 + tv ** 2); return np.array([[av, uv + tv], [uv - tv, -av]])
def hess2(f, h=1e-4):
    e = np.eye(2); Hm = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            Hm[i, j] = (f(*(h * e[i] + h * e[j])) - f(*(h * e[i] - h * e[j])) - f(*(-h * e[i] + h * e[j]))
                        + f(*(-h * e[i] - h * e[j]))) / (4 * h * h)
    return Hm
for lam in (1.0, 10.0, 100.0):
    ebc = np.linalg.eigvalsh(hess2(lambda x, y: lam * V_lam(np.eye(2), Kbc(x, y)) + V_mu(Kbc(x, y))))
    eut = np.linalg.eigvalsh(hess2(lambda x, y: lam * V_lam(np.eye(2), Kut(x, y)) + V_mu(Kut(x, y))))
    print(f"  lam = {lam:5.1f}: (b, c) eigenvalues {ebc}; (u, t) eigenvalues {eut}; "
          f"negative count {int((ebc < -1e-6).sum())} / {int((eut < -1e-6).sum())}")

print("\n== F. Reading R1: the documents' frozen-H reduction, H = 1 and K = K(phi)")
PH = np.linspace(0, 2 * np.pi, 2001)
Kphi = lambda p: np.array([[np.cos(p), np.sin(p)], [np.sin(p), -np.cos(p)]])
vcirc = np.array([V_mu(Kphi(p)) for p in PH])
print("  max |V_mu(K(phi)) + 2 mu (1 + cos 2 phi)| =", f"{np.abs(vcirc + 2 * MU * (1 + np.cos(2 * PH))).max():.2e}")
print("  max V_lam on the circle =", f"{max(V_lam(np.eye(2), Kphi(p)) for p in PH):.2e}")
print(f"  range of V on the circle: [{vcirc.min():.4f}, {vcirc.max():.4f}]  (bounded, for every lam)")

print("\n== G. The 'only' half: H dynamical, along the compatible boost family H = S^T S, K = S^-1 K_ref S")
for lam in (1.0, 100.0):
    out = []
    for t in (0.0, 2.0, 4.0):
        St = np.array([[np.cosh(t), np.sinh(t)], [np.sinh(t), np.cosh(t)]])
        H, K = St.T @ St, np.linalg.inv(St) @ Kref @ St
        out.append((t, lam * V_lam(H, K), lam * V_lam(H, K) + V_mu(K)))
    print(f"  lam = {lam:5.1f}: " + "; ".join(f"t = {t}: lam*V_lam = {vl:.1e}, total = {vt:.4e}" for t, vl, vt in out))

print("\n== H. The naive term by itself does not involve H: on the whole K-target it is unbounded at ANY H")
for s in (0.0, 3.0, 6.0):
    print(f"  s = {s}: V_mu(K_hyp(s, 0)) = {V_mu(K_hyp(s, 0.0)):.4e}  (= -4 cosh^2 s = {-4 * np.cosh(s) ** 2:.4e})")

print("\n== I. Full 4x4 Hessian (H dynamical) vs the frozen-H K-block, toy_coset coordinates (x, y, u, t)")
def fields(cc):
    x, y, u, t = cc
    Y = 1 + y; H = np.array([[Y + x * x / Y, x / Y], [x / Y, 1 / Y]])
    return H, Kut(u, t)
def hess4(f, h=1e-4):
    e = np.eye(4); Hm = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            Hm[i, j] = (f(h * e[i] + h * e[j]) - f(h * e[i] - h * e[j]) - f(-h * e[i] + h * e[j])
                        + f(-h * e[i] - h * e[j])) / (4 * h * h)
    return Hm
for lam in (1.0, 10.0, 100.0):
    Hm = hess4(lambda cc: lam * V_lam(*fields(cc)) + V_mu(fields(cc)[1]))
    print(f"  lam = {lam:5.1f}: full min eigenvalue {np.linalg.eigvalsh(Hm).min():8.4f}; "
          f"K-block (u, t) eigenvalues {np.linalg.eigvalsh(Hm[2:, 2:])}")
