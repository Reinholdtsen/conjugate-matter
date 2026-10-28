"""Locate the travelling (Re w != 0) unstable modes of the N=1 pure-gate block, and the purely growing
coupled roots, for the deep strong-coupling case r = 1.2917, gt = 100, kappa^2 = 2 (where the
argument-principle count found 3 coupled zeros on the imaginary axis and an N=1 travelling pair).
Also the MW case gt = 280.7, kappa^2 = 4.9348 with a finer near-axis grid."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from env_growth import Dtilde
from complex_roots import secant, winding_box

def detB(m, k, w, N):
    tau, ub = m.spectral(k, w)
    lN = (m.gt/k**2)*m.t0**2*m.q**N
    return np.prod(1 - lN*tau)

def imag_roots(m, k, Gs):
    vals = [Dtilde(m, k, G)[0] for G in Gs]
    roots = []
    for i in range(len(Gs) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            a, b, fa = Gs[i], Gs[i + 1], vals[i]
            for _ in range(30):
                mm = math.sqrt(a*b); fm = Dtilde(m, k, mm)[0]
                if np.sign(fm) == np.sign(fa): a, fa = mm, fm
                else: b = mm
            roots.append(round(math.sqrt(a*b), 5))
    return roots

if __name__ == '__main__':
    for r, gt, k2 in [(1.2917, 100.0, 2.0), (1.2917, 280.7, 4.9348)]:
        t1 = time.time()
        m = Gated(r, gt); k = math.sqrt(k2)
        print(f"r={r}, gt={gt}, kappa^2={k2}: purely growing coupled roots (Dtilde sign changes): "
              f"{imag_roots(m, k, np.geomspace(6.0, 2e-3, 70))}  ({time.time()-t1:.0f}s)"); sys.stdout.flush()
        xs = np.linspace(0.02, 3.5*k, 40); ys = np.geomspace(0.004, 3.0, 26)
        G = np.zeros((len(ys), len(xs)))
        for i, y in enumerate(ys):
            for j, x in enumerate(xs):
                G[i, j] = math.log(abs(detB(m, k, complex(x, y), 1)) + 1e-300)
        found = []
        f = lambda w: detB(m, k, w, 1)
        for i in range(len(ys)):
            for j in range(len(xs)):
                nb = [G[i + di, j + dj] for di in (-1, 0, 1) for dj in (-1, 0, 1)
                      if 0 <= i + di < len(ys) and 0 <= j + dj < len(xs) and not (di == 0 and dj == 0)]
                if G[i, j] < min(nb):
                    z0 = complex(xs[j], ys[i])
                    z, res = secant(f, z0, z0*(1 + 0.01j) + 0.005)
                    if res < 1e-8 and z.imag > 1e-3 and not any(abs(z - zz) < 1e-4 for zz, _ in found):
                        found.append((z, winding_box(f, z, min(0.02, 0.5*z.imag))))
        found.sort(key=lambda t: -t[0].imag)
        print("   N=1 block zeros (Re>0): " + ", ".join(f"{z.real:.4f}+{z.imag:.4f}i[wind {wn:+.2f}]" for z, wn in found)
              + f"  ({time.time()-t1:.0f}s)")
        sys.stdout.flush()
