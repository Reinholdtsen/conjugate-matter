"""Referee A: re-derive the torsion-balance range bound from J. G. Lee's thesis (UW 2020), Table 11.4.
Rows transcribed by hand from downloads/lee_thesis/thesis.txt (pages 134-135): lambda [mm], +alpha95, -alpha95, |alpha95|.
Log-log linear interpolation between tabulated points."""
import numpy as np

rows = [  # lambda_mm, +a95, -a95, |a95|
    (0.0250, 7.9, -1.27, 6.4),
    (0.0280, 4.51, -0.886, 3.73),
    (0.0320, 2.56, -0.507, 2.08),
    (0.0350, 1.77, -0.36, 1.45),
    (0.0400, 1.06, -0.226, 0.877),
    (0.0450, 0.699, -0.157, 0.585),
    (0.0500, 0.494, -0.117, 0.419),
    (0.0560, 0.35, -0.0884, 0.3),
    (0.0630, 0.251, -0.0685, 0.218),
    (0.0710, 0.183, -0.055, 0.162),
    (0.0790, 0.14, -0.0469, 0.126),
    (0.0890, 0.106, -0.0407, 0.097),
    (0.1000, 0.0813, -0.0365, 0.0766),
]
lam = np.array([r[0] for r in rows]) * 1e3  # um
cols = {"+alpha95 (attractive, one-sided)": np.array([r[1] for r in rows]),
        "-alpha95 (repulsive, one-sided)": -np.array([r[2] for r in rows]),
        "|alpha95| (two-sided)": np.array([r[3] for r in rows])}

def lam_limit(alpha, a95):
    """largest lambda for which a Yukawa of strength alpha is still allowed (alpha95 decreasing in lambda)."""
    la, lb = np.log(lam), np.log(a95)
    for i in range(len(lam) - 1):
        if a95[i] >= alpha >= a95[i + 1]:
            f = (np.log(alpha) - lb[i]) / (lb[i + 1] - lb[i])
            return np.exp(la[i] + f * (la[i + 1] - la[i]))
    return np.nan

hbarc_eVum = 0.1973269804  # eV um
for name, a95 in cols.items():
    print(name)
    for alpha in [1.0, 4/3, 8/3, 16/3]:
        L = lam_limit(alpha, a95)
        print(f"   alpha = {alpha:6.4f}: lambda < {L:6.2f} um  ->  M c^2 > {hbarc_eVum / L * 1e3:5.3f} meV")
print()
print("Published checks: |alpha95| at alpha = 1 should give 38.6 um (PRL abstract); alpha = 8/3 should give R < 30 um (thesis 11.5)")
# monotonicity check over full transcribed range
for name, a95 in cols.items():
    print(f"  {name}: strictly decreasing over 25-100 um: {bool(np.all(np.diff(a95) < 0))}")
# coupling with a background ratio c (Lueben et al. eq. 9): alpha = (4/3) c^2 (M_f/M_g)^2, at M_f = M_g
print()
print("If the Yukawa strength is (4/3) c^2 at equal Planck masses (Lueben et al. eq. 9 / Enander-Moertsell eq. 4.1):")
for c2 in [1.0, 0.75, 0.5, 0.1]:
    alpha = 4/3 * c2
    a95 = cols["+alpha95 (attractive, one-sided)"]
    L = lam_limit(alpha, a95)
    print(f"   c^2 = {c2:4.2f}: alpha = {alpha:5.3f} -> lambda < {L:6.2f} um" if not np.isnan(L) else f"   c^2 = {c2:4.2f}: alpha = {alpha:5.3f} -> outside 25-100 um table (bound at lambda > 100 um or none)")
A0 = 5.193e92
print(f"   c = 1/A0 = {1/A0:.2e} (self-dual epoch at 1e14 T_P, sections 6 and 8.4): alpha = {4/3/A0**2:.1e} -> no laboratory bound")
