"""Audit of flag 5, part C: what "Yukawa-cut at 1/M_X" pins, and how M_X scales with the betas.

Input from part B (derived there from the action and printed):
    pole mass^2 = m^2 (b1 + 2 b2 + b3)        (f frozen; bimetric multiplies by a constant)
Here, on palindromic betas with the flat-vacuum condition T = 0 (#8 sections 1-3):
  (i)  the static Green's function of (-Laplacian + M^2) is computed numerically
       (radial Fourier integral, mpmath.quadosc) and its decay constant is fitted:
       it equals M, so the Yukawa range 1/M_X fixes M_X as the pole mass (not its square);
  (ii) the log-derivative d ln M_X / d ln(b1 + b2) is computed: 1/2, not 1;
  (iii) doubling (b1 + b2) multiplies M_X by sqrt(2), whereas "M_X ∝ 2(b1+b2)" predicts 2.
"""
import mpmath as mp

mp.mp.dps = 30
m = mp.mpf(1)  # overall potential scale, units


def betas(b1, b2):
    b1, b2 = mp.mpf(b1), mp.mpf(b2)
    b0 = -4 * b1 - 3 * b2                  # T = b0 + 4 b1 + 3 b2 = 0 on the palindrome
    b = [b0, b1, b2, b1, b0]               # palindrome b_n = b_{4-n}
    tad_g = b[0] + 3 * b[1] + 3 * b[2] + b[3]
    tad_f = b[1] + 3 * b[2] + 3 * b[3] + b[4]
    assert abs(tad_g) < 1e-25 and abs(tad_f) < 1e-25
    return b


def MX(b):
    return mp.sqrt(m**2 * (b[1] + 2 * b[2] + b[3]))


def green(r, M):
    # G(r) = 1/(2 pi^2 r) Int_0^inf k sin(k r)/(k^2 + M^2) dk
    f = lambda kk: kk * mp.sin(kk * r) / (kk**2 + M**2)
    return mp.quadosc(f, [0, mp.inf], omega=r) / (2 * mp.pi**2 * r)


print('set        b1    b2    b1+2b2+b3   M_X=m*sqrt(.)   fitted decay const   G(1)*4pi*e^M (should be 1)')
rows = []
for (b1, b2) in [(0.3, 0.2), (0.6, 0.4), (1.2, 0.8)]:
    b = betas(b1, b2)
    M = MX(b)
    r1, r2 = mp.mpf(1), mp.mpf(2)
    G1, G2 = green(r1, M), green(r2, M)
    kappa = (mp.log(r1 * G1) - mp.log(r2 * G2)) / (r2 - r1)
    rows.append((b1 + b2, M, kappa))
    print(f'          {b1:5.2f} {b2:5.2f}   {mp.nstr(b[1] + 2*b[2] + b[3], 6):>8}    {mp.nstr(M, 10):>12}'
          f'      {mp.nstr(kappa, 10):>12}         {mp.nstr(G1 * 4 * mp.pi * mp.e**M, 10)}')

print('ratio M_X(set2)/M_X(set1) =', mp.nstr(rows[1][1] / rows[0][1], 10),
      ' (claim "M_X ∝ 2(b1+b2)" predicts', mp.nstr(mp.mpf(rows[1][0]) / rows[0][0], 10), ')')
print('ratio M_X(set3)/M_X(set1) =', mp.nstr(rows[2][1] / rows[0][1], 10),
      ' (claim predicts', mp.nstr(mp.mpf(rows[2][0]) / rows[0][0], 10), ')')

# log-derivative at a generic point
s0 = mp.mpf('0.5')
F = lambda s: mp.log(MX(betas(0.6 * s, 0.4 * s)))
dlog = mp.diff(lambda u: F(mp.e**u), mp.log(s0))
print('d ln M_X / d ln(b1+b2) =', mp.nstr(dlog, 12), '(M_X ∝ (b1+b2)^p with p = this)')
dlog2 = mp.diff(lambda u: 2 * F(mp.e**u), mp.log(s0))
print('d ln M_X^2 / d ln(b1+b2) =', mp.nstr(dlog2, 12))
