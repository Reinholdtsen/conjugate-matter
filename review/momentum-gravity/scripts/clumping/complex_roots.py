"""Locate complex unstable modes (Im w > 0, Re w != 0) of the homogeneous gated+gravity problem
(Gaussian gate, factorized solver) at strong coupling.
Coupled modes: zeros of Dt(w) = D(w) * prod_{even N, unstable} det(1 - lambda_N T_z(w)) (poles removed).
Decoupled pure-gate modes: zeros of det(1 - lambda_N T_z(w)) for N = 1, 2 (perpendicular pairs not coupled to gravity).
Method: grid scan of log|f| on Re w in [0, X], Im w in [ymin, Y] (zeros come in pairs w, -w*), local minima
refined by the secant method; each root verified by |f| and an argument-principle count on a small box."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated

def funcs(model, kappa, w):
    tau, ub = model.spectral(kappa, w)
    lam = (model.gt/kappa**2)*model.t0**2*model.q**model.N
    F = np.array([np.sum(ub/(1 - l*tau)) for l in lam])
    D = kappa**2 - np.sum(model.A*F)
    dets = {}
    for N in range(0, 6):
        lN = (model.gt/kappa**2)*model.t0**2*model.q**N
        dets[N] = np.prod(1 - lN*tau)
    Dt = D
    for N in range(0, 6, 2):
        if model.gt*model.t0**3*model.q**N > 0.3*kappa**2:
            Dt = Dt*dets[N]
    return {'coupled': Dt, 'block1': dets[1], 'block2': dets[2]}

def secant(f, z0, z1, tol=1e-9, maxit=60):
    f0, f1 = f(z0), f(z1)
    for _ in range(maxit):
        if f1 == f0: break
        z2 = z1 - f1*(z1 - z0)/(f1 - f0)
        if z2.imag < 1e-4: z2 = complex(z2.real, 1e-4)
        z0, f0, z1 = z1, f1, z2
        f1 = f(z1)
        if abs(z1 - z0) < tol: break
    return z1, abs(f1)

def winding_box(f, c, h, n=48):
    pts = [c + h*complex(math.cos(t), math.sin(t)) for t in np.linspace(0, 2*math.pi, n + 1)]
    vals = [f(p) for p in pts]
    tot = sum(np.angle(vals[i + 1]/vals[i]) for i in range(n))
    return tot/(2*math.pi)

if __name__ == '__main__':
    cases = [(1.2917, 280.7, 4.9348), (1.2917, 1275.0, 19.7392)]
    for r, gt, k2 in cases:
        t1 = time.time()
        m = Gated(r, gt); k = math.sqrt(k2)
        X, Y, ymin = 2.5*k, 4.0, 0.03
        xs = np.linspace(0.0, X, 36); ys = np.geomspace(ymin, Y, 22)
        grid = {key: np.zeros((len(ys), len(xs))) for key in ('coupled', 'block1', 'block2')}
        for i, y in enumerate(ys):
            for j, x in enumerate(xs):
                fv = funcs(m, k, complex(x, y))
                for key in grid:
                    grid[key][i, j] = math.log(abs(fv[key]) + 1e-300)
        print(f"r={r}, gt={gt}, kappa^2={k2}: grid done ({time.time()-t1:.0f}s)")
        for key in grid:
            Gk = grid[key]
            found = []
            for i in range(1, len(ys) - 1):
                for j in range(0, len(xs) - 1):
                    nb = [Gk[i + di, j + dj] for di in (-1, 0, 1) for dj in (-1, 0, 1)
                          if 0 <= j + dj < len(xs) and not (di == 0 and dj == 0)]
                    if Gk[i, j] < min(nb):
                        z0 = complex(xs[j], ys[i])
                        f = lambda w, key=key: funcs(m, k, w)[key]
                        z, res = secant(f, z0, z0 + complex(0.01, 0.01))
                        if res < 1e-6*math.exp(np.median(Gk)) and z.imag > 0.02:
                            wn = winding_box(f, z, 0.02)
                            if not any(abs(z - zz) < 1e-4 for zz, _ in found):
                                found.append((z, wn))
            found.sort(key=lambda t: -t[0].imag)
            print(f"   {key}: zeros (w = omega t_ff, Re>=0 half; mirror -w* also a zero): " +
                  ", ".join(f"{z.real:.4f}+{z.imag:.4f}i[wind {wn:+.2f}]" for z, wn in found))
        print(f"   ({time.time()-t1:.0f}s)")
        sys.stdout.flush()
