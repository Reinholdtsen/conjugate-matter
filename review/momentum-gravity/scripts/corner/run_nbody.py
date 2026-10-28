"""Direct-summation N-body toy for the corner model (round 3, label "corner").

Pair energy U_ij = -G m^2 [1 + eps exp(-|w_i-w_j|^2/(2 v*^2))] / sqrt(r_ij^2 + b^2)  (G = M = 1, m = 1/N).
Reading H (default; record-faithful): Hamiltonian with the gate on the canonical momentum per mass w,
  xdot = w + dU/dp (anomalous velocity), wdot = -dU/dx / m.   Integrator: implicit midpoint rule
  (symplectic, time-symmetric; fixed-point iteration to tol), so energy and momenta are conserved
  up to O(dt^2) bounded oscillation.
Reading F (comparison only): xdot = w, same wdot; not Hamiltonian, energy not conserved.
Initial conditions: N particles drawn from the Plummer sphere (G = M = a = 1; sampled from the eps = 0
model of equilibrium.py, which reproduces the analytic Plummer density to 4e-4).  The gated term is
switched on adiabatically: eps(t) = eps_f S(t/T_ramp), S(u) = 3u^2 - 2u^3 (u <= 1), then held fixed.
The self-consistent F(e) solver of equilibrium.py did not converge for eps > 0 (see equilibrium.out),
so the eps > 0 equilibria are built dynamically this way.  v* is fixed in N-body units,
v* = sigma_0 / r_g with sigma_0 = sqrt(1/6) the Plummer central 1D dispersion.
Output: npz with snapshots of x, w, xdot, phi every dt_out, and a log of E, P, L, iteration counts.
"""
import argparse
import ctypes
import os
import pickle
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_lib = ctypes.CDLL(os.path.join(HERE, "libgated.so"))
_dp = ctypes.POINTER(ctypes.c_double)
_lib.deriv.argtypes = [ctypes.c_int, _dp, _dp, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                       ctypes.c_double, ctypes.c_int, _dp, _dp, _dp]
_lib.deriv.restype = None


def deriv(x, w, Gm, eps, vs2inv, b2, ham):
    n = x.shape[0]
    x = np.ascontiguousarray(x); w = np.ascontiguousarray(w)
    xd = np.empty_like(x); wd = np.empty_like(w); phi = np.empty(n)
    _lib.deriv(n, x.ctypes.data_as(_dp), w.ctypes.data_as(_dp), Gm, eps, vs2inv, b2, int(ham),
               xd.ctypes.data_as(_dp), wd.ctypes.data_as(_dp), phi.ctypes.data_as(_dp))
    return xd, wd, phi


def load_model(eps, r_g):
    import equilibrium as EQ
    fn = os.path.join(HERE, f"model_eps{eps:g}_rt{r_g:g}.pkl")
    if os.path.exists(fn):
        with open(fn, "rb") as fh:
            return pickle.load(fh)
    m = EQ.solve(eps, r_g)
    with open(fn, "wb") as fh:
        pickle.dump(m, fh)
    return m


def ramp(t, T_ramp):
    if T_ramp <= 0:
        return 1.0
    u = min(max(t / T_ramp, 0.0), 1.0)
    return 3 * u * u - 2 * u ** 3


def run(eps, r_g, N, seed, T, dt, b, reading="H", dt_out=1.0, T_ramp=15.0, tol=1e-9, maxit=14,
        out=None, quiet=False):
    import equilibrium as EQ
    m = load_model(0.0, 1.0)
    x, w = EQ.sample(m, N, seed)
    vstar = np.sqrt(1.0 / 6.0) / r_g
    Gm = 1.0 / N
    vs2inv = 1.0 / vstar**2
    b2 = b * b
    ham = (reading == "H")
    nout = int(round(T / dt_out))
    per = int(round(dt_out / dt))
    snaps_x = np.empty((nout + 1, N, 3), np.float32)
    snaps_w = np.empty((nout + 1, N, 3), np.float32)
    snaps_v = np.empty((nout + 1, N, 3), np.float32)
    snaps_phi = np.empty((nout + 1, N), np.float32)
    log = []

    def record(k, t, x, w, its):
        e_now = eps * ramp(t, T_ramp)
        xd, wd, phi = deriv(x, w, Gm, e_now, vs2inv, b2, ham)
        snaps_x[k] = x; snaps_w[k] = w; snaps_v[k] = xd; snaps_phi[k] = phi
        E = 0.5 * Gm * np.sum(w**2) + 0.5 * Gm * np.sum(phi)
        P = Gm * w.sum(axis=0)
        L = Gm * np.cross(x, w).sum(axis=0)
        log.append((t, E, *P, *L, its, e_now))
        return xd, wd

    t = 0.0
    xd, wd = record(0, t, x, w, 0)
    t0 = time.time()
    for k in range(1, nout + 1):
        its_blk = 0
        for _ in range(per):
            e_mid = eps * ramp(t + 0.5 * dt, T_ramp)
            x1 = x + dt * xd; w1 = w + dt * wd
            for it in range(maxit):
                xm = 0.5 * (x + x1); wm = 0.5 * (w + w1)
                xd, wd, _p = deriv(xm, wm, Gm, e_mid, vs2inv, b2, ham)
                x1n = x + dt * xd; w1n = w + dt * wd
                err = max(np.abs(x1n - x1).max(), np.abs(w1n - w1).max())
                x1, w1 = x1n, w1n
                if err < tol:
                    break
            its_blk += it + 1
            x, w = x1, w1
            t += dt
        record(k, t, x, w, its_blk / per)
        if not quiet:
            print(f"t={t:6.2f} eps={log[-1][9]:.3f} E={log[-1][1]:.8f} its/step={its_blk/per:.2f} "
                  f"wall={time.time()-t0:.0f}s", flush=True)
    meta = dict(eps=eps, r_g=r_g, N=N, seed=seed, T=T, dt=dt, b=b, reading=reading, vstar=vstar,
                T_ramp=T_ramp, wall=time.time() - t0)
    if out:
        np.savez_compressed(out, x=snaps_x, w=snaps_w, v=snaps_v, phi=snaps_phi, log=np.array(log),
                            meta=np.array([repr(meta)]))
    return meta, np.array(log)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--eps", type=float, default=0.0)
    ap.add_argument("--rg", type=float, default=1.0)
    ap.add_argument("--N", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--T", type=float, default=30.0)
    ap.add_argument("--dt", type=float, default=0.01)
    ap.add_argument("--b", type=float, default=0.1)
    ap.add_argument("--reading", default="H")
    ap.add_argument("--dtout", type=float, default=1.0)
    ap.add_argument("--ramp", type=float, default=15.0)
    ap.add_argument("--out", default=None)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    out = a.out or os.path.join(HERE, "runs", f"run_{a.reading}_eps{a.eps:g}_rg{a.rg:g}_N{a.N}_s{a.seed}.npz")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    meta, log = run(a.eps, a.rg, a.N, a.seed, a.T, a.dt, a.b, a.reading, a.dtout, T_ramp=a.ramp, out=out, quiet=a.quiet)
    print("meta:", meta)
    post = log[:, 0] >= meta['T_ramp'] - 1e-9
    E0 = log[post][0, 1]
    print(f"energy after the ramp (eps fixed): max|dE/E| = {np.max(np.abs(log[post,1]/E0-1)):.2e}; "
          f"final P = {log[-1,2:5]}; final L = {log[-1,5:8]}; mean iterations/step = {np.mean(log[1:,8]):.2f}")
