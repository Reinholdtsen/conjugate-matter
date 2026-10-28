"""Cluster (r = sigma/v* = 8.333) growth times of the purely growing gravity-coupled mode at kappa^2 = Q,
leaner z-grid (L = 6, panel = v*, order 8); checked against the closed-form Jeans root and the static limit."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated, jeans_closed
from static_threshold import top_eigs
from env_growth import Dtilde

def root(model, kappa, Ghi=6.0, Glo=2e-3, n=40):
    Gs = np.geomspace(Ghi, Glo, n)
    vals = [Dtilde(model, kappa, G)[0] for G in Gs]
    for i in range(len(Gs) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            a, b, fa = Gs[i], Gs[i + 1], vals[i]
            for _ in range(30):
                m = math.sqrt(a*b); fm = Dtilde(model, kappa, m)[0]
                if np.sign(fm) == np.sign(fa): a, fa = m, fm
                else: b = m
            m = math.sqrt(a*b)
            return m, abs(model.D(kappa, 1j*m))
    return 0.0, None

r = 8.3333
tff = 149.62; tcross = 3*tff
if __name__ == '__main__':
    t1 = time.time()
    m0 = Gated(r, 0.0, L=6.0)
    G0, res = root(m0, 0.5)
    print(f"check gt=0, kappa=0.5: Gamma={G0:.6f} closed form {jeans_closed(0.5):.6f} ({time.time()-t1:.0f}s)"); sys.stdout.flush()
    for Q, gt, label in [(1.0966, 1598.0, "2x revir threshold 798.8"), (1.0966, 304.4, "2x no-revir threshold 152.2"),
                         (1.0966, 1522.0, "10x no-revir threshold"), (4.3865, 5858.0, "2x no-revir threshold 2929")]:
        t1 = time.time()
        m = Gated(r, gt, L=6.0)
        L0 = top_eigs(r, gt, 0, nev=1)[0][0]
        if label.startswith("2x revir"):
            Gs, rs = root(m, math.sqrt(0.99*L0))
            print(f"   static-limit check gt={gt}: kappa^2=0.99 Lambda_0 -> Gamma={Gs:.5f}, Gamma/0.01={Gs/0.01:.3f}")
        G, res = root(m, math.sqrt(Q))
        te = tff/G if G > 0 else float('inf')
        print(f"cluster Q={Q} gt={gt} ({label}): Lambda_0={L0:.4f}, Gamma={G:.5f}/t_ff, e-fold={te:.0f} Myr, "
              f"t_e/t_cross={te/tcross:.3f}  |D|={res} ({time.time()-t1:.0f}s)")
        sys.stdout.flush()
