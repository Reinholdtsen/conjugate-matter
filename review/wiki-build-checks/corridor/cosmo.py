# Shared numerics for the corridor audit (numpy + math only; no scipy on this machine).
#
# Model: flat FRW, matter + radiation + a canonical scalar tau with V = V0 [1 + cos(tau/f)]
# (#1 s3, #11 s10).  Units: 8 pi G = 1 (reduced Planck mass 1) and H0 = 1, i.e. H(a = 1) = 1.
# V0 is fixed by Omega_DE by shooting (#1 s7 item 4: "V0 is fixed by Omega_DE").
# Time variable N = ln a; state (tau, y = dtau/dN); H from the Friedmann constraint:
#   3 H^2 = rho_m + rho_r + H^2 y^2 / 2 + V   =>   H^2 = (rho_m + rho_r + V) / (3 - y^2 / 2)
#   tau'' = -(3 - eps) y - V'(tau) / H^2,     eps = -Hdot/H^2 = (rho_m + 4/3 rho_r + H^2 y^2) / (2 H^2)
# Initial condition: tau = tau_i, dtau/dt = 0 deep in the radiation era (frozen by Hubble friction).
import math
import numpy as np

OM = 0.30          # Omega_m today (illustrative)
OR = 9.0e-5        # Omega_r today (illustrative; negligible below z = 2.5)
A_I = 1e-4         # start of integration
DN = 2e-3          # RK4 step in N
ZSTAR = 1090.0     # CMB distance anchor redshift (used by one fit variant)


def run(V0, f, tau_i, om=OM, orr=OR, a_i=A_I, dN=DN, N_end=0.0, store=False):
    N0 = math.log(a_i)
    n = int(math.ceil((N_end - N0) / dN - 1e-9))
    h = (N_end - N0) / n
    c3m, c3r, inv_f, V0f = 3.0 * om, 3.0 * orr, 1.0 / f, V0 / f

    def d(N, tau, y):
        e3 = math.exp(-3.0 * N)
        rm = c3m * e3
        rr = c3r * e3 * math.exp(-N)
        H2 = (rm + rr + V0 * (1.0 + math.cos(tau * inv_f))) / (3.0 - 0.5 * y * y)
        eps = (rm + rr * (4.0 / 3.0) + H2 * y * y) / (2.0 * H2)
        return y, -(3.0 - eps) * y + V0f * math.sin(tau * inv_f) / H2

    tau, y, N = tau_i, 0.0, N0
    if store:
        Ns, taus, ys = [N], [tau], [y]
    for i in range(n):
        a1, b1 = d(N, tau, y)
        a2, b2 = d(N + 0.5 * h, tau + 0.5 * h * a1, y + 0.5 * h * b1)
        a3, b3 = d(N + 0.5 * h, tau + 0.5 * h * a2, y + 0.5 * h * b2)
        a4, b4 = d(N + h, tau + h * a3, y + h * b3)
        tau += h / 6.0 * (a1 + 2 * a2 + 2 * a3 + a4)
        y += h / 6.0 * (b1 + 2 * b2 + 2 * b3 + b4)
        N = N0 + (i + 1) * h
        if store:
            Ns.append(N); taus.append(tau); ys.append(y)
    if not store:
        rm, rr = 3 * om * math.exp(-3 * N), 3 * orr * math.exp(-4 * N)
        return (rm + rr + V0 * (1 + math.cos(tau / f))) / (3 - 0.5 * y * y)   # H^2 at N_end
    N = np.array(Ns); tau = np.array(taus); y = np.array(ys)
    a = np.exp(N)
    rm, rr = 3 * om * a**-3, 3 * orr * a**-4
    V = V0 * (1 + np.cos(tau / f))
    H2 = (rm + rr + V) / (3 - 0.5 * y * y)
    K = 0.5 * H2 * y * y                      # kinetic energy density (1/2) taudot^2
    return dict(N=N, a=a, tau=tau, y=y, H=np.sqrt(H2), K=K, V=V, rho=K + V, w=(K - V) / (K + V),
                rm=rm, rr=rr, V0=V0, f=f, tau_i=tau_i, om=om, orr=orr)


def illinois(g, lo, hi, glo, ghi, tol=1e-13, itmax=200):
    """root of g in [lo, hi] with g(lo) < 0 < g(hi) (Illinois false position)"""
    side = 0
    for _ in range(itmax):
        x = (lo * ghi - hi * glo) / (ghi - glo)
        gx = g(x)
        if abs(gx) < tol or abs(hi - lo) < tol * max(1.0, abs(x)):
            return x
        if gx < 0:
            lo, glo = x, gx
            if side == -1:
                ghi *= 0.5
            side = -1
        else:
            hi, ghi = x, gx
            if side == +1:
                glo *= 0.5
            side = +1
    return x


def shoot_V0(f, tau_i, om=OM, orr=OR, **kw):
    """smallest V0 (on a geometric scan) with H(a = 1) = 1, i.e. Omega_tau = 1 - om - orr today"""
    OL = 1.0 - om - orr
    g = lambda V0: run(V0, f, tau_i, om=om, orr=orr, **kw) - 1.0
    lo = 0.5 * 1.5 * OL                      # V(top) = 2 V0 = 3 OL / 2 at this V0: too little
    glo = g(lo)
    if glo >= 0:
        raise RuntimeError("no bracket (low end)")
    hi = lo
    for _ in range(60):
        hi *= 1.15
        ghi = g(hi)
        if ghi > 0:
            return illinois(g, hi / 1.15, hi, g(hi / 1.15), ghi)
    raise RuntimeError("no bracket (high end)")


def solve(f, tau_i, **kw):
    V0 = shoot_V0(f, tau_i, **kw)
    return run(V0, f, tau_i, store=True, **kw)


# ---------- CPL helpers ----------

def cpl_w(a, w0, wa):
    return w0 + wa * (1 - a)


def cpl_X(a, w0, wa):
    """rho_DE(a)/rho_DE(1) for CPL, closed form"""
    return a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))


def cumtrap_from_end(xgrid, fvals):
    """I(x) = integral from x to x_end of f, on an increasing grid (trapezoid)"""
    seg = 0.5 * (fvals[1:] + fvals[:-1]) * np.diff(xgrid)
    out = np.zeros_like(fvals)
    out[:-1] = np.cumsum(seg[::-1])[::-1]
    return out


def comoving_distance(N, H):
    """chi(N) = int_N^0 dN' / (a H)  (= int_0^z dz'/H), H0 = 1 units, flat"""
    return cumtrap_from_end(N, 1.0 / (np.exp(N) * H))


def wls_line(x, yv, wt):
    """weighted least squares yv ~ c0 + c1 x"""
    W = np.sqrt(wt)
    X = np.column_stack([np.ones_like(x), x]) * W[:, None]
    c, *_ = np.linalg.lstsq(X, yv * W, rcond=None)
    return c


def lm(resfun, p0, itmax=200, tol=1e-12):
    """Levenberg-Marquardt with central-difference Jacobian"""
    p = np.array(p0, float)
    r = resfun(p)
    cost = r @ r
    lam = 1e-3
    for _ in range(itmax):
        J = np.empty((r.size, p.size))
        for j in range(p.size):
            dp = np.zeros_like(p)
            dp[j] = 1e-6 * max(1.0, abs(p[j]))
            J[:, j] = (resfun(p + dp) - resfun(p - dp)) / (2 * dp[j])
        A, gr = J.T @ J, J.T @ r
        improved = False
        while lam < 1e14:
            step = np.linalg.solve(A + lam * np.diag(np.diag(A) + 1e-30), -gr)
            pn = p + step
            rn = resfun(pn)
            cn = rn @ rn
            if np.isfinite(cn) and cn < cost:
                p, r, cost = pn, rn, cn
                lam = max(lam / 10, 1e-15)
                improved = True
                break
            lam *= 10
        if not improved or np.max(np.abs(step)) < tol:
            break
    return p, cost
