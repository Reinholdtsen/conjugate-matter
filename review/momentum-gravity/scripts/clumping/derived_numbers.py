"""Derived conversions quoted in the write-up (no eyeball arithmetic)."""
import sys
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from static_threshold import Lam_g_closed, top_eigs
for name, r in [("dwarf", 0.25), ("MW", 1.2917), ("cluster", 8.3333)]:
    L = Lam_g_closed(r)
    L0 = top_eigs(r, 1.0, 0, nev=1)[0][0]
    print(f"{name}: r={r}, Lam_g={L:.5e}, stream-mode crossover gt=1/Lam_g={1/L:.4g}; Lambda_0(gt=1)={L0:.6f} <= 1+Lam_g={1+L:.6f}")
tff_MW, torb, tcr_MW = 40.98, 219.0, 122.9
for label, G in [("kscan gt=280.7 kappa^2=30", 0.7783), ("odd-softening peak gt=240 kappa^2=19.74", 0.7666),
                 ("kscan gt=280.7 kappa^2=8", 0.3517), ("kscan gt=56.14 kappa^2=8", 0.1742),
                 ("travelling gt=320 kappa^2=19.74", 0.1743), ("travelling gt=56.14 kappa^2=3", 0.0754)]:
    te = tff_MW/G
    print(f"MW {label}: Gamma={G}/t_ff -> e-fold {te:.1f} Myr = {te/torb:.3f} t_orb(219 Myr) = {te/tcr_MW:.3f} t_cross(122.9 Myr)")
