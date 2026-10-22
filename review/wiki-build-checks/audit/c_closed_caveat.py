# Flag 27 audit, part C (caveat to the flag's "a turnaround needs V < 0"): that holds for a flat
# universe. With the documents' V >= 0, a CLOSED universe can still recollapse, by curvature.
# After tau settles into oscillation about its V = 0 minimum it redshifts like dust (rho_tau a^3 ~ const,
# checked below), so the late phase is the closed-dust cycloid a = A(1 - cos eta),
# t = (A/sqrt k)(eta - sin eta), A = D/(6k), D = rho a^3. The cycloid is validated against the full
# integration over a stretch that is feasible, then used to extrapolate to the turnaround.
import numpy as np
import b_turnaround_numerics as b


def cycloid_eta(a, A):
    return np.arccos(1 - a / A)


def cycloid_t(eta, A, k):
    return (A / np.sqrt(k)) * (eta - np.sin(eta))


f, ti = 1.0, 0.2
for Ok in (-0.05, -0.002):
    k = -Ok
    V0 = b.shoot_V0(f, ti * f, 0.0, Ok)
    T1, T2 = 60.0, 1500.0
    o1 = b.run(V0, f, ti * f, 0.0, k=k, t_after=T1, project=True)
    N1, H1, tau1, v1 = o1["final"]
    a1 = np.exp(N1)
    D = (3 * b.OM * a1**-3 + 0.5 * v1 * v1 + b.pot(V0, f, 0.0)[0](tau1)) * a1**3
    A = D / (6 * k)
    print(f"Ok = {Ok}: V0 = {V0:.4f}; at t-t0 = {T1:.0f}/H0: a = {a1:.4g}, D = (rho_m + rho_tau) a^3 = {D:.5g}", flush=True)
    # validation: full integration to t-t0 = T2 versus the cycloid started at (a1, t1)
    o2 = b.run(V0, f, ti * f, 0.0, k=k, t_after=T2, project=True)
    N2, H2, tau2, v2 = o2["final"]
    a2_full = np.exp(N2)
    D2 = (3 * b.OM * a2_full**-3 + 0.5 * v2 * v2 + b.pot(V0, f, 0.0)[0](tau2)) * a2_full**3
    t_needed = o2["t_total"] - o2["t_today"] - (o1["t_total"] - o1["t_today"])
    eta1 = cycloid_eta(a1, A)
    lo, hi = eta1, np.pi
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if cycloid_t(mid, A, k) - cycloid_t(eta1, A, k) < t_needed:
            lo = mid
        else:
            hi = mid
    a2_cyc = A * (1 - np.cos(0.5 * (lo + hi)))
    print(f"   validation at t-t0 = {T2:.0f}/H0: full a = {a2_full:.5g} (D = {D2:.5g}, H = {H2:.4g} > 0, V(tau) = "
          f"{b.pot(V0, f, 0.0)[0](tau2):+.2e}), cycloid a = {a2_cyc:.5g}, ratio {a2_full/a2_cyc:.5f};"
          f" max rel. constraint violation {o2['maxviol']:.1e}", flush=True)
    a_turn = 2 * A
    dt_turn = (o1["t_total"] - o1["t_today"]) + cycloid_t(np.pi, A, k) - cycloid_t(eta1, A, k)
    print(f"   extrapolated turnaround (curvature-driven, V(tau) ~ 0+ there, never < 0): a = {a_turn:.4g},"
          f" t - t0 = {dt_turn:.4g}/H0 = {dt_turn*b.GYR_PER_HUBBLE:.3g} Gyr", flush=True)
