"""verify-critic-numbers, claims c5-thresholds, c5-validity, c5-margins.

Written before opening the critic's c5 script.  Model (the clumping analysis's C1/C3, local homogeneous
Jeans-swindle model, static limit): unstable at (k/k_J)^2 = Q iff the top eigenvalue Lambda_0 of
    K = p0^(1/2) [1 + gt W] p0^(1/2),   W = exp(-|v - v'|^2/(2 v*^2)),  gt = G~/G,
on velocity space reaches Q.  Units sigma = 1, r = sigma/v*.

Two discretizations of my own:
  (A) radial l = 0 Nystrom (composite Gauss-Legendre), angle-averaged gate
      Wbar = exp(-r^2 (v - v')^2/2) (1 - exp(-2 r^2 v v'))/(2 r^2 v v');
  (B) Cartesian: the gate factorizes, K_gate = K1 x K1 x K1; I compute the 1D spectrum of K1 numerically
      (Nystrom), then solve the rank-one secular equation 1 = sum c_n1^2 c_n2^2 c_n3^2/(Lambda - gt l_n1 l_n2 l_n3).
Anchors independent of the claim: gt = 0 gives Lambda_0 = 1 (Jeans criterion, textbook); r -> 0 gives
Lambda_0 -> 1 + gt (gate = 1, gravity rescaled).  My own derivation of the gate-only top eigenvalue
(Gaussian-kernel / Mehler algebra): Lambda_g = (1/2 + r^2 + sqrt(1 + 4 r^2)/2)^(-3/2).
Validity of the local model: my reconstruction of the clumping derivation verifier's sizing is the ratio of
the dropped background anomalous velocity to v at v -> 0,
    delta(0) = gt (|Phi|/sigma^2) r^2 (1 + r^2)^(-5/2)        [D, Hamiltonian xdot = v + grad_v phi_g0],
with |Phi|/sigma^2 = 9/2 (centre of a uniform core of radius 3/k_J); valid if delta(0) < 1.
"""
import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def lam_g_closed(r):
    return (0.5 + r**2 + np.sqrt(1 + 4 * r**2) / 2) ** -1.5


def gl_composite(a, b, npanel, nper=16):
    x0, w0 = np.polynomial.legendre.leggauss(nper)
    edges = np.linspace(a, b, npanel + 1)
    xs, ws = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        xs.append(0.5 * (hi - lo) * x0 + 0.5 * (hi + lo))
        ws.append(0.5 * (hi - lo) * w0)
    return np.concatenate(xs), np.concatenate(ws)


class Radial:
    def __init__(self, r, vmax=9.0, panel=None):
        if panel is None:
            panel = min(0.25, 1.2 / max(r, 1e-9))
        npan = int(np.ceil(vmax / panel))
        v, w = gl_composite(0.0, vmax, npan)
        self.v = v
        p0 = (2 * np.pi) ** -1.5 * np.exp(-v**2 / 2)
        self.a = np.sqrt(4 * np.pi * w) * v * np.sqrt(p0)
        x = r**2 * np.outer(v, v)
        with np.errstate(invalid='ignore', divide='ignore'):
            ang = np.where(x > 1e-12, -np.expm1(-2 * x) / (2 * x), 1.0 - x)
        self.Wbar = np.exp(-r**2 * (v[:, None] - v[None, :]) ** 2 / 2) * ang
        self.Kg = self.a[:, None] * self.Wbar * self.a[None, :]
        self.Kgrav = np.outer(self.a, self.a)

    def lam0(self, gt):
        return np.linalg.eigvalsh(self.Kgrav + gt * self.Kg)[-1]

    def lam_gate(self):
        return np.linalg.eigvalsh(self.Kg)[-1]


class Cartesian:
    def __init__(self, r, xmax=9.0, panel=None, keep=1e-15):
        if panel is None:
            panel = min(0.25, 1.2 / max(r, 1e-9))
        npan = int(np.ceil(2 * xmax / panel))
        x, w = gl_composite(-xmax, xmax, npan)
        psi = (2 * np.pi) ** -0.25 * np.exp(-x**2 / 4)
        sw = np.sqrt(w)
        K1 = (sw * psi)[:, None] * np.exp(-r**2 * (x[:, None] - x[None, :]) ** 2 / 2) * (sw * psi)[None, :]
        lam, vec = np.linalg.eigh(K1)
        c = vec.T @ (sw * psi)            # overlaps <psi1|phi_n>
        idx = np.argsort(lam)[::-1]
        lam, c = lam[idx], c[idx]
        m = (c**2 > keep) & (lam > 0)
        self.l1, self.c2 = lam[m], c[m] ** 2
        L = self.l1
        self.prod = (L[:, None, None] * L[None, :, None] * L[None, None, :]).ravel()
        C = self.c2
        self.wt = (C[:, None, None] * C[None, :, None] * C[None, None, :]).ravel()
        self.l1max = lam[0]

    def lam0(self, gt):
        lo = gt * self.l1max**3 * (1 + 1e-14) + 1e-300
        F = lambda L: np.sum(self.wt / (L - gt * self.prod)) - 1.0
        hi = max(1.0, lo) * 2 + gt + 1
        while F(hi) > 0:
            hi *= 2
        lo_ = lo
        if F(lo_) < 0:          # root sits essentially on the pole (gate-dominated)
            return lo_
        for _ in range(200):
            mid = 0.5 * (lo_ + hi)
            if F(mid) > 0:
                lo_ = mid
            else:
                hi = mid
        return 0.5 * (lo_ + hi)


def crit(solver, Q, revir_W=None, gmax=1e5):
    """smallest gt with Lambda_0(gt) = Q (no revir) or = Q (1 + gt <W>) (revir); inf if none below gmax.
    log-grid scan for the first sign change, then 40 bisections in log gt."""
    f = (lambda g: solver.lam0(g) - Q) if revir_W is None else (lambda g: solver.lam0(g) - Q * (1 + g * revir_W))
    if f(0.0) >= 0:
        return 0.0
    grid = np.logspace(-3, np.log10(gmax), 49)
    prev = 0.0
    for g in grid:
        if f(g) >= 0:
            lo, hi = np.log(max(prev, 1e-6)), np.log(g)
            for _ in range(40):
                mid = 0.5 * (lo + hi)
                if f(np.exp(mid)) < 0:
                    lo = mid
                else:
                    hi = mid
            return float(np.exp(0.5 * (lo + hi)))
        prev = g
    return np.inf


def W_pair(r):
    return (1 + 2 * r**2) ** -1.5


def valid_limit(r, X=4.5):
    return (1 + r**2) ** 2.5 / (X * r**2)


print("== anchors")
R = Radial(1.0)
print(f"  gt = 0: Lambda_0 radial = {R.lam0(0.0):.10f} (Jeans: 1)")
Rs = Radial(0.01)
print(f"  r = 0.01, gt = 3: Lambda_0 = {Rs.lam0(3.0):.6f} (broad-gate limit 1 + gt = 4; first correction ~ -3 r^2 gt)")

print("\n== gate-only top eigenvalue: closed form vs radial Nystrom vs Cartesian 1D spectrum cubed")
for r in (0.25, 1 / 3, 0.4, 1.0, 155 / 120, 4.0, 1000 / 120):
    Rr, Cr = Radial(r), Cartesian(r)
    print(f"  r = {r:7.4f}: closed {lam_g_closed(r):.7e}  radial {Rr.lam_gate():.7e}  cartesian {Cr.l1max**3:.7e}"
          f"   crossover 1/Lambda_g = {1/lam_g_closed(r):.4f}")
print(f"  r = 1: 1/Lambda_g = {1/lam_g_closed(1.0):.6f};  golden ratio cubed = {PHI**3:.6f}")

print("\n== Lambda_0 at (r, gt): radial vs Cartesian secular (two discretizations)")
for r, gt in ((155 / 120, 10.0), (155 / 120, 100.0), (1000 / 120, 1000.0), (0.25, 1.0), (1.0, 4.0)):
    print(f"  r = {r:7.4f}, gt = {gt:7.1f}: radial {Radial(r).lam0(gt):.8f}  cartesian {Cartesian(r).lam0(gt):.8f}")

Qcore = ((np.pi / 3) ** 2, (2 * np.pi / 3) ** 2)
QMW = (np.pi**2 / 2, 2 * np.pi**2)
# solar-circle margin (lambda_J/R0)^2 from rho = 0.4 GeV/cm^3, sigma = 155 km/s, R0 = 8.2 kpc (C10 inputs, recomputed)
G = 6.67430e-11; GeVkg = 1.78266192e-27; kpc = 3.085677581e19
kJ = np.sqrt(4 * np.pi * G * 0.4 * GeVkg / 1e-6) / 155e3
lamJ = 2 * np.pi / kJ / kpc
Qsun = (lamJ / 8.2) ** 2
print(f"\n  MW local Jeans length {lamJ:.3f} kpc, (lambda_J/R0)^2 = {Qsun:.3f} at R0 = 8.2 kpc; at R0 = 8.0: {(lamJ/8.0)**2:.3f}; 8.3: {(lamJ/8.3)**2:.3f}")

envs = [("UFD", 4.0, Qcore), ("classical dSph", 10.0, Qcore), ("dwarf core (3a)", 30.0, Qcore),
        ("MW local", 155.0, QMW + (Qsun,)), ("cluster core", 1000.0, Qcore)]

print("\n== environments x v*: r, crossover 1/Lambda_g, validity limit (closed forms)")
for vs in (10.0, 30.0, 120.0, 300.0, 1000.0):
    for name, sig, Qs in envs:
        r = sig / vs
        print(f"  v* = {vs:6.0f}  {name:16s} sigma = {sig:6.0f}  r = {r:8.4f}  1/Lam_g = {1/lam_g_closed(r):10.4g}  valid < {valid_limit(r):9.4g}")

print("\n== critical gt, no revir / revir (Lambda_0 = Q(1 + gt <W>)), radial Nystrom, selected cases")
rows = {}
sel = [(120.0, e) for e in envs] + [(10.0, envs[0]), (10.0, envs[1]), (30.0, envs[0]), (30.0, envs[1])]
for vs, (name, sig, Qs) in sel:
    r = sig / vs
    S = Radial(r)
    line = f"  v* = {vs:5.0f} {name:16s} r = {r:7.4f} <W> = {W_pair(r):.4g}"
    for Q in Qs:
        g0 = crit(S, Q)
        g1 = crit(S, Q, revir_W=W_pair(r))
        rows[(vs, name, round(Q, 4))] = (g0, g1)
        line += f" | Q={Q:6.3f}: {g0:9.4g} / {g1:9.4g}"
    print(line, flush=True)

print("\n== validity limit: sensitivity to |Phi|/sigma^2 (9/2 assumed; MW at the Sun: v_esc^2/(2 sigma^2) with")
print("   v_esc = 528 km/s [S: Deason et al. 2019], sigma = 155 km/s)")
X_sun = 528.0**2 / 2 / 155.0**2
for name, r in (("MW v*=120", 155 / 120), ("dwarf v*=120", 30 / 120), ("cluster v*=120", 1000 / 120), ("dSph v*=10", 1.0)):
    print(f"  {name:15s}: X = 4.5 -> {valid_limit(r):8.4g};  X = {X_sun:.2f} -> {valid_limit(r, X_sun):8.4g};  X = 9 -> {valid_limit(r, 9.0):8.4g}")

print("\n== margins at v* = 120: threshold / allowed eps")
allowed = {"K4 matter 0.0282": 0.0282, "K4 gas 0.0804": 0.0804, "K4 gas 0.0812": 0.0812,
           "consistent gas 0.2959": 0.2959, "consistent matter 0.3405": 0.3405, "Sgr 1.52": 1.52, "Sgr upper 2.7": 2.7}
thr = {"MW crossover 1/Lam_g": 1 / lam_g_closed(155 / 120),
       "MW no-revir Q=pi^2/2": rows[(120.0, "MW local", round(np.pi**2 / 2, 4))][0],
       "MW no-revir Q=sun": rows[(120.0, "MW local", round(Qsun, 4))][0],
       "cluster crossover 1/Lam_g": 1 / lam_g_closed(1000 / 120),
       "cluster no-revir Q=(pi/3)^2": rows[(120.0, "cluster core", round(Qcore[0], 4))][0],
       "cluster revir Q=(pi/3)^2": rows[(120.0, "cluster core", round(Qcore[0], 4))][1]}
for tn, tv in thr.items():
    print(f"  {tn:30s} = {tv:9.4g}: " + "; ".join(f"{an}: {tv/av:8.3g}" for an, av in allowed.items()))
