"""Probe the sign structure of D-tilde(i Gamma) and of the block determinants at strong coupling (MW, r=1.2917)."""
import sys, math
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from env_growth import Dtilde
for k2, gt in [(19.7392, 255.0), (19.7392, 1275.0)]:
    m = Gated(1.2917, gt); k = math.sqrt(k2)
    Gs = np.geomspace(8.0, 0.02, 90)
    prev = None
    print(f"kappa^2={k2}, gt={gt}: static-block eigen ratios gt*Lam_g*q^N/kappa^2 =",
          [round(gt*m.t0**3*m.q**N/k2, 3) for N in range(6)])
    for G in Gs:
        Dt, aD = Dtilde(m, k, G)
        Dv, tau, lam = m.D(k, 1j*G, return_parts=True)
        dets = [np.prod(1 - (gt/k2)*m.t0**2*m.q**N*tau).real for N in range(4)]
        sg = (np.sign(Dt), tuple(np.sign(dets)))
        if prev is not None and sg != prev:
            print(f"   sign change near Gamma={G:.4f}: sign(Dtilde)={sg[0]:+.0f}, sign(det B_N, N=0..3)={sg[1]}, |D|={aD:.3e}")
        prev = sg
