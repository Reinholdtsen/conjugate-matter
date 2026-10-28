"""Growth times of the purely growing (gravity-coupled, l=0) mode at kappa^2 = Q for Gt/G above threshold,
Gaussian gate, local homogeneous model.  Gamma in units of 1/t_ff, t_ff = 1/sqrt(4 pi G rho).
Thresholds (no re-virialization) from halos.out; crossing time t_cross = 3 t_ff (isothermal core)."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from static_threshold import top_eigs

def Dtilde(model, kappa, G):
    """D(i G) times det(1 - lambda_N T_z) for the even blocks whose pure-gate mode can be unstable:
    removes the poles of D on the imaginary axis; real and continuous there."""
    Dv, tau, lam = model.D(kappa, 1j*G, return_parts=True)
    Lg = model.t0**3
    val = Dv
    for N in range(0, 200, 2):
        lN = (model.gt/kappa**2)*model.t0**2*model.q**N
        if model.gt*Lg*model.q**N < 0.3*kappa**2:
            break
        val = val*np.prod(1 - lN*tau)
    return val.real, abs(Dv)

def root(model, kappa):
    Gs = np.geomspace(8.0, 1e-3, 70)
    vals = [Dtilde(model, kappa, G)[0] for G in Gs]
    for i in range(len(Gs) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            a, b, fa = Gs[i], Gs[i + 1], vals[i]
            for _ in range(40):
                m = math.sqrt(a*b); fm = Dtilde(model, kappa, m)[0]
                if np.sign(fm) == np.sign(fa): a, fa = m, fm
                else: b = m
            m = math.sqrt(a*b)
            return m, abs(model.D(kappa, 1j*m))
    return 0.0, None

tff = {"dwarf core": 25.92, "MW local": 40.98, "cluster": 149.62}   # Myr, from halos.out
torb_MW = 219.0
cases = [("dwarf core", 0.25, 1.0966, 0.1152), ("dwarf core", 0.25, 4.3865, 4.026),
         ("MW local", 1.2917, 4.9348, 28.07), ("MW local", 1.2917, 19.7392, 127.5),
         ("cluster", 8.3333, 1.0966, 152.2), ("cluster", 8.3333, 1.0966, 798.8)]
if __name__ == '__main__':
    for name, r, Q, gc in cases:
        for fac in [2.0, 10.0]:
            t1 = time.time()
            gt = fac*gc
            m = Gated(r, gt)
            L0 = top_eigs(r, gt, 0, nev=1)[0][0]
            G, res = root(m, math.sqrt(Q))
            te = tff[name]/G if G > 0 else float('inf')
            extra = f", t_e/t_orb(MW sun)={te/torb_MW:.3f}" if name == "MW local" else ""
            print(f"{name:10s} r={r} Q={Q:.4f} gt={gt:.4g} (={fac}x{gc}): Lambda_0={L0:.4f}, Gamma={G:.5f} /t_ff, "
                  f"e-fold time={te:.1f} Myr, t_e/t_cross(=3t_ff)={1/(3*G) if G>0 else float('inf'):.3f}{extra}  |D|={res} ({time.time()-t1:.0f}s)")
            sys.stdout.flush()
