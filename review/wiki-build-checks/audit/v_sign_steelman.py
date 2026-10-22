"""Flag 27 steelman audit: can V = V0[1 + cos(tau/f)] (#1 s3, #9 s8, #11 s10) produce
the turnaround the same documents claim ("eventually goes negative", "turnaround after
V(tau) < 0", #1 s7 item 3 "a cosine potential is negative over half its range")?

Anchors are textbook facts independent of the papers: cos x >= -1; the FRW constraint
3H^2 = rho - 3k/a^2 (8 pi G = 1); a canonical scalar has rho = taudot^2/2 + V,
p = taudot^2/2 - V.

H is taken from the constraint (H = +sqrt(R/3), R = rho_total + 3 Omega_k0 a^-2), so a
turnaround registers only where R reaches zero. (A first version integrated H by the
Raychaudhuri equation; its conserved constraint residual, -4.5e-4, acted as a spurious
negative cosmological constant and produced a false turnaround for c = 1.)

Parts
 A. Sign structure of the written potential for BOTH signs of V0, of a bare cosine, of
    the hilltop quadratic expansion, of the toy note's "tau-type" potential, and of the
    general offset form V0[c + cos x].
 B. Flat FRW + dust + canonical tau in V0[c + cos(tau/f)], V0 tuned to Omega_tau = 0.7
    today (H0 = 1): is there a turnaround, and when? c = 1 is the documents' form;
    c = 0 is the bare cosine.
 C. BBT's own extra terms: the a^-6 Planck-mass factor (sign-neutral), the dual-frame
    dictionary (sign-preserving), negative dark radiation (closed dual curvature); and
    positive spatial curvature of OUR space, which is NOT in the documents' Friedmann
    equation (#1 s6), as the only route to a turnaround with V >= 0.
"""
import numpy as np
import sympy as sp

print("=== A. sign structure ===")
x = sp.symbols('x', real=True)
I = sp.Interval(0, 2 * sp.pi)
for V0 in (1, -1):
    V = V0 * (1 + sp.cos(x))
    print(f"V0 = {V0:+d}: V0[1+cos x] has min {sp.minimum(V, x, I)}, max {sp.maximum(V, x, I)} over one period")
grid = np.linspace(0, 2 * np.pi, 400001)[:-1]
print("fraction of period with V0[1+cos x] < 0 (V0=+1):", np.mean(1 + np.cos(grid) < 0))
print("fraction of period with V0[1+cos x] > 0 (V0=-1):", np.mean(-(1 + np.cos(grid)) > 0))
print("fraction of period with bare V0 cos x < 0 (V0=+1):", np.mean(np.cos(grid) < 0))
quad = sp.series(1 + sp.cos(x), x, 0, 3).removeO()
print("hilltop quadratic expansion of 1+cos x about x=0:", quad,
      "; zero at x =", [r for r in sp.solve(sp.Eq(quad, 0), x) if r > 0],
      "; true minimum of 1+cos x at x = pi =", float(sp.pi), "with value", (1 + sp.cos(sp.pi)))
phi, mu = sp.symbols('phi mu', real=True)
Vtoy = -2 * mu * (1 + sp.cos(2 * phi))
print("toy note tau-type potential -2mu(1+cos 2phi) at mu=1: min",
      sp.minimum(Vtoy.subs(mu, 1), phi, I), "max", sp.maximum(Vtoy.subs(mu, 1), phi, I))
c, V0s = sp.symbols('c V0', positive=True)
print("general V0[c + cos x], V0 > 0: minimum =", sp.simplify(sp.minimum(V0s * (c + sp.cos(x)), x, I)),
      "-> negative somewhere iff c < 1; the written form has c = 1")

print("\n=== B. FRW: dust + canonical tau, H0 = 1, Omega_m = 0.3 ===")
OM = 0.3
RHO_M0 = 3 * OM


def R_of(y, V0, cc, f, rho_dr0, omk0):
    N, tau, td = y
    return (RHO_M0 * np.exp(-3 * N) + rho_dr0 * np.exp(-4 * N) + 0.5 * td * td
            + V0 * (cc + np.cos(tau / f)) + 3 * omk0 * np.exp(-2 * N))


def run(V0, cc, f, xi, ai=0.01, t_max=2000.0, rho_dr0=0.0, omk0=0.0, stop_at_today=False):
    def H_of(y):
        return np.sqrt(max(R_of(y, V0, cc, f, rho_dr0, omk0), 0.0) / 3)

    def rhs(y):
        N, tau, td = y
        H = H_of(y)
        return np.array([H, td, -3 * H * td + (V0 / f) * np.sin(tau / f)])

    y = np.array([np.log(ai), xi * f, 0.0])
    t = 0.0
    m_eff = np.sqrt(abs(V0)) / f
    today = None
    Hmin = np.inf
    while t < t_max:
        H = H_of(y)
        dt = min(0.005 / max(H, 1e-12), 0.01 / m_eff, 0.02)
        k1 = rhs(y); k2 = rhs(y + 0.5 * dt * k1); k3 = rhs(y + 0.5 * dt * k2); k4 = rhs(y + dt * k3)
        y_new = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if today is None and y[0] < 0 <= y_new[0]:
            s = -y[0] / (y_new[0] - y[0])
            yt = y + s * (y_new - y)
            Vt = V0 * (cc + np.cos(yt[1] / f))
            rt = 0.5 * yt[2] ** 2 + Vt
            today = dict(t=t + s * dt, H=H_of(yt), rho_tau=rt, w=(0.5 * yt[2] ** 2 - Vt) / rt)
            if stop_at_today:
                return today, None, None
        R0, R1 = R_of(y, V0, cc, f, rho_dr0, omk0), R_of(y_new, V0, cc, f, rho_dr0, omk0)
        if R0 > 0 >= R1:
            s = R0 / (R0 - R1)
            yt = y + s * (y_new - y)
            return today, dict(t=t + s * dt, a=np.exp(yt[0]), V=V0 * (cc + np.cos(yt[1] / f))), None
        y, t = y_new, t + dt
        if today is not None:
            Hmin = min(Hmin, H_of(y))
    return today, None, dict(t=t, a=np.exp(y[0]), H=H_of(y), Ht=H_of(y) * t, Hmin=Hmin,
                             Vend=V0 * (cc + np.cos(y[1] / f)), R=R_of(y, V0, cc, f, rho_dr0, omk0))


def tune_V0(cc, f, xi, target, **kw):
    lo, hi = 1e-3, 1e3
    for _ in range(60):
        mid = np.sqrt(lo * hi)
        today, _, _ = run(mid, cc, f, xi, stop_at_today=True, **kw)
        if today is None:          # crunched before a = 1: the trial V0 rolls too early
            hi = mid
        elif today["rho_tau"] < target:
            lo = mid
        else:
            hi = mid
    return np.sqrt(lo * hi)


def report(label, cc, f, xi, target=3 - RHO_M0, **kw):
    V0 = tune_V0(cc, f, xi, target, **{k: v for k, v in kw.items() if k in ("rho_dr0", "omk0", "ai")})
    today, turn, end = run(V0, cc, f, xi, **kw)
    if today is None or abs(today["H"] - 1) > 1e-3 or abs(today["rho_tau"] - target) > 1e-3:
        print(f"{label}: c={cc}, f={f}, tau_i/f={xi}: no V0 gives the target tau density at a = 1 "
              f"(the field rolls before today); row skipped")
        return
    print(f"{label}: c={cc}, f={f}, tau_i/f={xi}: V0={V0:.4f}, min V = V0(c-1) = {V0*(cc-1):.4f}; "
          f"today H={today['H']:.4f}, Omega_tau={today['rho_tau']/3:.4f}, w0={today['w']:.4f}")
    if turn is not None:
        print(f"    TURNAROUND (R = 0) at t - t_today = {turn['t']-today['t']:.3f}/H0, a={turn['a']:.4f}, "
              f"V(tau) there = {turn['V']:.4f}")
    else:
        print(f"    no turnaround up to t = {end['t']:.0f}/H0: a = {end['a']:.4g}, min H after today = {end['Hmin']:.4g}, "
              f"H*t = {end['Ht']:.4f} (dust-like value 2/3 = 0.6667), V(tau) at end = {end['Vend']:.3e}, "
              f"R = 3H^2 = {end['R']:.3e}")


for f, xi in ((1.0, 0.5), (0.5, 0.3)):
    for cc in (0.0, 0.5, 0.9, 0.99, 1.0):
        report("flat", cc, f, xi)

print("\n=== C. BBT extras and curvature ===")
a, MP, Mt = sp.symbols('a M_P Mt', positive=True)
print("C1. #1 s6: 3H^2 (M_P^2 + Mt^2 a^-6) = rho; the factor is positive for all a > 0:",
      sp.ask(sp.Q.positive(3 * (MP**2 + Mt**2 * a**-6))), "-> H = 0 iff rho = 0")
rt, at = sp.symbols('rhotilde atilde', real=True)
print("C2. dictionary (#1 s6): rho_eff = E/a^3, E = rhotilde*atilde^3, atilde = 1/a  ->  rho_eff =",
      sp.simplify((rt * at**3 / a**3).subs(at, 1 / a)), "(sign of rhotilde preserved)")
print("C3. negative dark radiation (closed dual curvature), exaggerated to Omega_dr = -1e-3, written form c = 1:")
report("flat+dr", 1.0, 1.0, 0.5, target=3 - RHO_M0 + 3e-3, ai=0.1, rho_dr0=-3e-3)
print("C4. NOT in the documents (their Friedmann equation, #1 s6, has no curvature term): closed OUR-frame")
print("    space with the written form c = 1. Omega_k0 = -0.1 is excluded by data; it is used only so the")
print("    recollapse falls inside the integration window. It shows the mechanism, not a viable model.")
report("closed", 1.0, 0.5, 0.3, target=3 - RHO_M0 + 0.3, omk0=-0.1, t_max=5000.0)
print("    same closed space with f = 1 (tau settles later, so its dust-like energy is larger): ")
report("closed", 1.0, 1.0, 0.5, target=3 - RHO_M0 + 0.3, omk0=-0.1, t_max=5000.0)
