# Flag 27 audit, part B: does tau's hilltop quintessence produce a turnaround?
# Full background dynamics (no slow-roll shortcut): Friedmann constraint monitored, Raychaudhuri +
# Klein-Gordon integrated (RK4, adaptive step), matter + tau, optional spatial curvature.
# Units 8 pi G = 1 (reduced Planck mass 1), H0 = 1 defined by H(a = 1) = 1.
# Potential family: V = V0 [1 + cos(tau/f)] - c V0.
#   c = 0 : the documents' form (#1 s3, #9 s8, #11 s10)
#   c = 1 : V0 cos(tau/f), the form #1 s7's "negative over half its range" describes
#   other c: an unwritten negative offset V_c = -c V0
# V0 is fixed by Omega_DE by shooting, as the documents say ("V0 fixed by Omega_DE").
import sys
import numpy as np

OM = 0.3                           # Omega_m today (illustrative)
GYR_PER_HUBBLE = 977.792 / 67.4    # 1/H0 in Gyr for H0 = 67.4 km/s/Mpc (unit conversion only)
A_I = 1e-2                         # start deep in matter domination, tau frozen by Hubble friction
HFAC = 3e-3


def pot(V0, f, c):
    V = lambda tau: V0 * (1 + np.cos(tau / f)) - c * V0
    dV = lambda tau: -(V0 / f) * np.sin(tau / f)
    d2V = lambda tau: -(V0 / f**2) * np.cos(tau / f)
    return V, dV, d2V


def rhs(y, dV, k):
    N, H, tau, v = y
    rho_m = 3 * OM * np.exp(-3 * N)
    return np.array([H, -0.5 * (rho_m + v * v) + k * np.exp(-2 * N), v, -3 * H * v - dV(tau)])


def run(V0, f, tau_i, c, k=0.0, t_after=200.0, stop_today=False, project=False):
    """project=True re-imposes the Friedmann constraint on H after each step, but only while the
    effective density is far from zero (> 5% of the largest term), i.e. never near a turnaround,
    where H is left to the Raychaudhuri equation. 3H^2 - rho is conserved exactly by the equations,
    so without projection an absolute error made in the dense early phase persists and becomes
    large relative to rho at very late times."""
    V, dV, d2V = pot(V0, f, c)
    N = np.log(A_I)
    rho_m = 3 * OM * np.exp(-3 * N)
    y = np.array([N, np.sqrt((rho_m + V(tau_i)) / 3 - k * np.exp(-2 * N)), tau_i, 0.0])
    t, t_today = 0.0, None
    out = {"today": None, "turn": None, "collapsed_before_today": False}
    maxviol, minH, minrho = 0.0, np.inf, np.inf
    checkpoints = []
    m_top = np.sqrt(abs(V0)) / f            # fixed field-frequency scale (largest |V''|^(1/2))
    while True:
        Nn, H, tau, v = y
        rho_m = 3 * OM * np.exp(-3 * Nn)
        s = abs(H) + m_top + np.sqrt(rho_m + v * v + abs(V(tau))) + np.sqrt(abs(k) * np.exp(-2 * Nn))
        dt = HFAC / s
        k1 = rhs(y, dV, k); k2 = rhs(y + 0.5 * dt * k1, dV, k)
        k3 = rhs(y + 0.5 * dt * k2, dV, k); k4 = rhs(y + dt * k3, dV, k)
        yn = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        rm = 3 * OM * np.exp(-3 * yn[0])
        kin, Vn = 0.5 * yn[3]**2, V(yn[2])
        rho_tau = kin + Vn
        curv = 3 * k * np.exp(-2 * yn[0])
        # relative to the largest individual term (kinetic and |V| separately: their sum cancels at a turnaround)
        Cabs = abs(3 * yn[1]**2 - (rm + rho_tau - curv))
        scale = max(3 * yn[1]**2, rm, kin, abs(Vn), abs(curv))
        viol = Cabs / scale
        maxviol = max(maxviol, viol)
        out["Cabs_last"] = Cabs
        if project:
            rho_eff = rm + rho_tau - curv
            if rho_eff > 0.05 * max(rm, kin, abs(Vn), abs(curv)):
                yn[1] = np.sign(yn[1]) * np.sqrt(rho_eff / 3)
        if t_today is None:
            if yn[1] <= 0:                       # turned around before reaching a = 1
                out["collapsed_before_today"] = True
                out["maxviol"] = maxviol
                return out
            if y[0] < 0 <= yn[0]:
                fr = -y[0] / (yn[0] - y[0])
                out["today"] = y + fr * (yn - y)
                t_today = t + fr * dt
                if stop_today:
                    out["maxviol"] = maxviol
                    return out
        else:
            minH = min(minH, yn[1]); minrho = min(minrho, rm + rho_tau)
            if y[1] > 0 >= yn[1]:
                fr = y[1] / (y[1] - yn[1])
                yt = y + fr * (yn - y)
                out["turn"] = dict(dt=t + fr * dt - t_today, a=np.exp(yt[0]), V=V(yt[2]), tau_f=yt[2] / f,
                                   rho_m=3 * OM * np.exp(-3 * yt[0]), kin=0.5 * yt[3]**2,
                                   curv=3 * k * np.exp(-2 * yt[0]))
                break
            if len(checkpoints) < 4 and (t + dt - t_today) >= [25, 50, 100, 200][len(checkpoints)] * t_after / 200:
                checkpoints.append((t + dt - t_today, np.exp(yn[0]), rho_tau * np.exp(3 * yn[0]), yn[1] * (t + dt)))
            if t + dt - t_today > t_after:
                break
        y, t = yn, t + dt
    out.update(maxviol=maxviol, minH=minH, minrho=minrho, final=yn, t_total=t + dt, t_today=t_today,
               checkpoints=checkpoints)
    return out


def rho_de_today(V0, f, tau_i, c, k):
    o = run(V0, f, tau_i, c, k=k, stop_today=True)
    if o["collapsed_before_today"]:
        return None
    N, H, tau, v = o["today"]
    return 0.5 * v * v + pot(V0, f, c)[0](tau)


def shoot_V0(f, tau_i, c, Ok=0.0):
    """V0 with today's dark-energy density 3(1 - OM - Ok), i.e. H(a=1) = 1.
    rho_tau is non-increasing while H > 0 (d rho/dt = -3 H taudot^2), so rho_DE(today) <= V(tau_i):
    lo = target / V(tau_i)/V0 is a guaranteed lower bracket."""
    k = -Ok
    target = 3 * (1 - OM - Ok)
    lo = target / (1 + np.cos(tau_i / f) - c)
    hi = None
    for j in range(1, 200):
        trial = lo * (1 + 0.02 * j)
        r = rho_de_today(trial, f, tau_i, c, k)
        if r is None:
            break
        if r > target:
            hi = trial
            break
        lo = trial
    if hi is None:
        return None
    for _ in range(35):
        mid = 0.5 * (lo + hi)
        r = rho_de_today(mid, f, tau_i, c, k)
        if r is not None and r < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def w_today(o, V0, f, c):
    N, H, tau, v = o["today"]
    V, dV, _ = pot(V0, f, c)
    K, Vv = 0.5 * v * v, V(tau)
    Kd, Vd = -3 * H * v * v - v * dV(tau), dV(tau) * v
    wdot = 2 * (Kd * Vv - K * Vd) / (K + Vv)**2
    return (K - Vv) / (K + Vv), -wdot / H        # w0 and -dw/da at a = 1 (local slope, not a CPL fit)


def report(label, f, ti, c, Ok=0.0, t_after=200.0, project=False):
    tau_i = ti * f
    V0 = shoot_V0(f, tau_i, c, Ok)
    head = f"{label:22s} f={f:<4} tau_i/f={ti:<4} c={c:<5} Ok={Ok:<6}"
    if V0 is None:
        print(head, "| no V0 reproduces Omega_DE = 0.7 (field rolls through before today)", flush=True)
        return None
    o = run(V0, f, tau_i, c, k=-Ok, t_after=t_after, project=project)
    w0, wa = w_today(o, V0, f, c)
    vmin = pot(V0, f, c)[0](np.linspace(0, 2 * np.pi * f, 20001)).min()
    head += f" V0={V0:.4f} minV={vmin:+.4f} w0={w0:+.3f} (-dw/da)={wa:+.3f}"
    if o["turn"] is not None:
        tr = o["turn"]
        print(head, f"| TURNAROUND t-t0 = {tr['dt']:.3f}/H0 = {tr['dt']*GYR_PER_HUBBLE:.1f} Gyr, a = {tr['a']:.3f},"
              f" V = {tr['V']:+.4f}, rho_m = {tr['rho_m']:.4f}, kin = {tr['kin']:.4f}, 3k/a^2 = {tr['curv']:.4f},"
              f" tau/f = {tr['tau_f']:.3f} | max rel. constraint violation {o['maxviol']:.1e}", flush=True)
    else:
        N, H, tau, v = o["final"]
        print(head, f"| NO turnaround in {t_after:.0f}/H0 ({t_after*GYR_PER_HUBBLE:.0f} Gyr) after today:"
              f" min H = {o['minH']:.3e}, min rho_tot = {o['minrho']:.3e}, a_end = {np.exp(N):.3e},"
              f" H*t at end = {H*o['t_total']:.4f} | max rel. constraint violation {o['maxviol']:.1e},"
              f" absolute |3H^2 - rho| at end {o['Cabs_last']:.1e} (projected: {project})", flush=True)
        for (dt_, a_, Da, Ht) in o["checkpoints"]:
            print(f"      t-t0 = {dt_:7.1f}: a = {a_:.3e}, rho_tau*a^3 = {Da:.4f}, H*t = {Ht:.4f}", flush=True)
    return o


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "all"
    print(f"Units 8piG = 1, H0 = 1, Omega_m = {OM}; 1/H0 = {GYR_PER_HUBBLE:.2f} Gyr; start a = {A_I}", flush=True)
    if part in ("all", "1"):
        print("\n== 1. The documents' potential V0[1 + cos(tau/f)] (c = 0) ==", flush=True)
        for f, ti in ((1.0, 0.2), (0.5, 0.1), (2.0, 0.5), (0.3, 0.1)):
            report("doc form V0[1+cos]", f, ti, 0.0)
        print("   same, with the constraint re-imposed (cross-check of a_end and H*t):", flush=True)
        for f, ti in ((1.0, 0.2), (0.5, 0.1)):
            report("doc form, projected", f, ti, 0.0, project=True)
    if part in ("all", "2"):
        print("\n== 2. V0 cos(tau/f) (c = 1): same shape, minimum -V0 ==", flush=True)
        for f, ti in ((1.0, 0.2), (0.5, 0.1), (2.0, 0.5), (1.0, 0.1), (1.0, 0.4), (0.3, 0.1)):
            report("V0 cos", f, ti, 1.0)
        print("   cross-check with the constraint re-imposed away from the turnaround:", flush=True)
        report("V0 cos, projected", 1.0, 0.2, 1.0, project=True)
    if part in ("all", "3"):
        print("\n== 3. Free negative offset V_c = -c V0, fixed (f, tau_i/f) = (1.0, 0.2) ==", flush=True)
        for c in (0.25, 0.5, 1.0, 1.5):
            report("V0[1+cos] - c V0", 1.0, 0.2, c)
