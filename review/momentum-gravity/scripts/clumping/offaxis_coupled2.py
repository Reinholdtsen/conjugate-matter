"""Off-axis (travelling) gravity-coupled modes at r = 1.2917, Gt/G = 280.7, kappa^2 = 19.7392:
winding counts on the right rectangle Re w in [0.01, X], Im w in [0.004, 5] for D and det B_N, then
grid + secant location of zeros of Dt (= D with even-block poles removed)."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from complex_omega_check import winding, mult, NB
from complex_roots import funcs, secant, winding_box
for k2 in [19.7392]:
    t1 = time.time()
    m = Gated(1.2917, 280.7); k = math.sqrt(k2)
    X = 4*k + 4
    right = [complex(0.01, 0.004), complex(X, 0.004), complex(X, 5.0), complex(0.01, 5.0)]
    wD, wB, n = winding(m, k, right)
    coupled = wD + sum(mult(N)[0]*wB[N] for N in range(NB))
    print(f"kappa^2={k2}: right rect wind(D)={wD:+.3f}, wind(det B_N)={np.round(wB,3)} -> coupled zeros (Re>0.01) = {coupled:+.3f} [{n} evals, {time.time()-t1:.0f}s]")
    sys.stdout.flush()
    xs = np.linspace(0.02, 3.0*k, 34); ys = np.geomspace(0.01, 3.0, 22)
    Gd = np.array([[math.log(abs(funcs(m, k, complex(x, y))['coupled']) + 1e-300) for x in xs] for y in ys])
    f = lambda w: funcs(m, k, w)['coupled']
    found = []
    for i in range(len(ys)):
        for j in range(len(xs)):
            nb = [Gd[i+di, j+dj] for di in (-1,0,1) for dj in (-1,0,1) if 0 <= i+di < len(ys) and 0 <= j+dj < len(xs) and not (di == 0 and dj == 0)]
            if Gd[i, j] < min(nb):
                z0 = complex(xs[j], ys[i]); z, res = secant(f, z0, z0*(1+0.01j) + 0.005)
                if res < 1e-8 and z.imag > 3e-3 and z.real > 1e-3 and not any(abs(z-zz) < 1e-4 for zz, _ in found):
                    found.append((z, winding_box(f, z, min(0.02, 0.5*z.imag))))
    found.sort(key=lambda t: -t[0].imag)
    print(f"   off-axis coupled zeros (Re>0): " + ", ".join(f"{z.real:.4f}+{z.imag:.4f}i[wind {wn:+.2f}]" for z, wn in found) + f"  ({time.time()-t1:.0f}s)")
    sys.stdout.flush()
