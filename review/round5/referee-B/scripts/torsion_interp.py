"""Referee B: interpolate Lee (2020) PhD thesis Table 11.4 (transcribed from downloads/thesis/thesis.txt, pp. 133-136).

Columns: lambda [mm], +alpha95, |alpha95|. Find lambda where the limit equals a given alpha.
Checks the manuscript's 37.7 um (alpha = 4/3, one-sided positive) and its claim that the same
interpolation reproduces 38.6 um (|alpha| = 1, PRL abstract) and 30 um (alpha = 8/3, thesis 11.5).
"""
import numpy as np

rows = [  # lambda_mm, +a95, |a95|
    (0.0250, 7.9, 6.4), (0.0280, 4.51, 3.73), (0.0320, 2.56, 2.08), (0.0350, 1.77, 1.45),
    (0.0400, 1.06, 0.877), (0.0450, 0.699, 0.585), (0.0500, 0.494, 0.419), (0.0560, 0.35, 0.3),
]
lam = np.array([r[0] for r in rows]) * 1e3  # um
plus = np.array([r[1] for r in rows])
absa = np.array([r[2] for r in rows])


def crossing(col, a, mode='loglog'):
    for i in range(len(lam) - 1):
        if (col[i] - a) * (col[i + 1] - a) <= 0:
            if mode == 'loglog':
                f = (np.log(col[i]) - np.log(a)) / (np.log(col[i]) - np.log(col[i + 1]))
                return float(np.exp(np.log(lam[i]) + f * (np.log(lam[i + 1]) - np.log(lam[i]))))
            f = (col[i] - a) / (col[i] - col[i + 1])
            return float(lam[i] + f * (lam[i + 1] - lam[i]))
    return None


for a, lab in [(1.0, 'alpha=1'), (4 / 3, 'alpha=4/3'), (8 / 3, 'alpha=8/3'), (16 / 3, 'alpha=16/3')]:
    print(f'{lab:<11s}  +a95: loglog {crossing(plus, a):.2f} um, linear {crossing(plus, a, "lin"):.2f} um'
          f'   |a95|: loglog {crossing(absa, a):.2f} um, linear {crossing(absa, a, "lin"):.2f} um')
hbarc_eVm = 1.054571817e-34 * 299792458 / 1.602176634e-19
for l in [37.7, 35.8, 38.6]:
    print(f'hbar c/({l} um) = {hbarc_eVm / (l * 1e-6) * 1e3:.3f} meV')
