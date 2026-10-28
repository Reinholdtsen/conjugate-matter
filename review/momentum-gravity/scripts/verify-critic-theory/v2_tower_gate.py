"""
v2_tower_gate.py  (verify-critic-theory, round 3) -- loophole T4: an infinite tower of spins.

Each spin-J exchange contributes (sign_J) g_J^2 P_J(gamma) (massive) at the pole.  A gate must
DECREASE with gamma, so it needs a sum over J with cancelling signs.

1. Entire gate G(gamma) = exp(-x (gamma - 1)).  Nonrelativistically gamma - 1 = v^2/(2c^2), so
   x = c^2/v*^2 reproduces the amplitude gate exp(-v^2/(2 v*^2)).  Its Legendre series
   follows from e^{z t} = sum_J (2J+1) i_J(z) P_J(t) (i_J modified spherical Bessel):
       G(gamma) = e^{x} sum_J (2J+1) (-1)^J i_J(x) P_J(gamma).
   Verified numerically below; the size of the individual terms relative to the net gate
   value G(1) = 1 measures the cancellation the tower needs.
2. Gates with a singularity on [-1,1] (rational in gamma, or Gaussian/rational in v^2 with
   v^2 = 1 - 1/gamma^2) have no Legendre series convergent off [-1,1] (Lehmann-ellipse argument:
   the series converges inside the largest ellipse with foci +-1 free of singularities).
   The singular points are printed.
"""
import math
import mpmath as mp

mp.mp.dps = 260   # cancellation of terms up to ~1e68 (x=80) needs >> 68 digits

def iJ(J, x):
    # modified spherical Bessel i_J(x) = sqrt(pi/(2x)) I_{J+1/2}(x)
    return mp.sqrt(mp.pi / (2 * x)) * mp.besseli(J + mp.mpf(1) / 2, x)

def PJ(J, g):
    return mp.legendre(J, g)

print("1. Legendre tower for G(gamma) = exp(-x(gamma-1))")
for x in [5, 20, 80]:
    x = mp.mpf(x)
    Jmax = int(6 * mp.e * float(x) * 3 + 80)   # series at gamma=3 converges once (x*5.83*e/2J) < 1
    coeffs = [mp.e ** x * (2 * J + 1) * (-1) ** J * iJ(J, x) for J in range(Jmax + 1)]
    for g in [1, mp.mpf('1.05'), mp.mpf('1.5'), 3]:
        s = mp.fsum(c * PJ(J, g) for J, c in enumerate(coeffs))
        exact = mp.e ** (-x * (g - 1))
        print(f"  x={mp.nstr(x,3):>4}, gamma={mp.nstr(g,4):>5}: tower sum = {mp.nstr(s, 12)}, exp(-x(gamma-1)) = {mp.nstr(exact, 12)}")
    mags = [abs(c) for c in coeffs]
    Jpk = max(range(len(mags)), key=lambda J: mags[J])
    signs = ''.join('+' if c > 0 else '-' for c in coeffs[:10])
    asym = (2 * Jpk + 1) * mp.e ** (2 * x) / (2 * x) * mp.e ** (-Jpk * (Jpk + 1) / (2 * x))
    print(f"    signs J=0..9: {signs}  (even J positive, odd J negative)")
    print(f"    largest single-spin term |a_J| at J={Jpk}: {mp.nstr(mags[Jpk], 6)}  (net G(1) = 1);"
          f" log10 = {mp.nstr(mp.log10(mags[Jpk]), 6)};  asymptotic (2J+1)e^(2x)/(2x) e^(-J(J+1)/2x) = {mp.nstr(asym, 6)}")

# asymptotic check at larger x, then extrapolate to x = c^2/v*^2
print("  asymptotic formula check at larger x (exact mpmath vs (2J+1) e^{2x}/(2x) exp(-J(J+1)/(2x)) at J ~ sqrt(x)):")
for x in [320, 1000, 3000]:
    x = mp.mpf(x)
    J = int(mp.sqrt(x))
    exact = mp.e ** x * (2 * J + 1) * iJ(J, x)
    asym = (2 * J + 1) * mp.e ** (2 * x) / (2 * x) * mp.e ** (-J * (J + 1) / (2 * x))
    print(f"    x={int(x)}, J={J}: log10 exact = {mp.nstr(mp.log10(exact), 8)}, log10 asym = {mp.nstr(mp.log10(asym), 8)}")

c_kms = mp.mpf('299792.458')
for vstar in [120, 85, 30]:
    x = (c_kms / vstar) ** 2
    J = mp.sqrt(x)
    log10max = mp.log10(2 * J + 1) + (2 * x) * mp.log10(mp.e) - mp.log10(2 * x) - (J * (J + 1) / (2 * x)) * mp.log10(mp.e)
    print(f"  v* = {vstar} km/s: x = c^2/v*^2 = {mp.nstr(x, 6)}; largest term at spin J ~ sqrt(x) = {mp.nstr(J, 5)};"
          f" largest single-spin term ~ 10^{mp.nstr(log10max, 7)} times the net gated force")

print("\n2. singular points of other gate shapes as functions of gamma (c = 1)")
for vstar in [120]:
    b = mp.mpf(vstar) / c_kms
    x = 1 / b ** 2
    g_lor_gamma = 1 - 1 / x
    g_lor_v2 = 1 / mp.sqrt(1 + b ** 2)
    print(f"  Lorentzian in (gamma-1): 1/(1 + x(gamma-1)) has a pole at gamma0 = 1 - 1/x = 1 - {mp.nstr(1/x, 6)}  (inside [-1,1])")
    print(f"  Lorentzian in v^2 = 1 - 1/gamma^2: 1/(1 + v^2/v*^2) has poles at gamma = +-1/sqrt(1+v*^2) = +-{mp.nstr(g_lor_v2, 12)} (inside [-1,1])")
    print(f"  Gaussian in v^2: exp(-(1 - 1/gamma^2)/(2 v*^2)) has an essential singularity at gamma = 0 (inside [-1,1])")
    print("  -> none of these has a Legendre (spin-tower) series that converges for gamma > 1;"
          " only gates entire in gamma, such as exp(-x(gamma-1)), can be built from a tower.")
