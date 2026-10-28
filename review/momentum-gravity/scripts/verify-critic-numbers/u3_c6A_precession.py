"""verify-critic-numbers, claim c6A: first-order gated apsidal precession.

Setup taken from the program derivation verifier's v4c (the values the critic compared with):
H = p^2/2 - (1/r)(1 + beta exp(-p^2)), units GM = mu = v* = 1 (so W = exp(-v^2/v*^2), the ordinary-tests /
program convention), e = 0.3, quoted values are first order in beta times beta = 0.2.

My method (different from O7's Delaunay averaging and from orbit integration): the exact apsidal angle at
fixed energy E and angular momentum L.  Because H depends on p only through s = |p|^2,
dphi/dr = (dH/dL)/(dH/dp_r) = L/(r^2 p_r) exactly, with p_r^2 = s(r) - L^2/r^2 and s(r) solving
s/2 - beta e^{-s}/r = E + 1/r.  So  Delta_phi = 2 int_{r1}^{r2} L dr/(r^2 sqrt(s(r) - L^2/r^2)).
First-order coefficient by a symmetric difference in beta (1e-12, 50 digits); at first order the choice
(E, L) = Kepler values of (a, e) versus osculating (a, e) does not matter.
Also evaluated: O7's formula  dw = 2 pi beta sqrt(1-e^2)/e dPhi/de,  Phi = (1/2pi) int W(u_c sqrt((1+e cosE)/(1-e cosE))) dE,
and O7's small-e limit pi beta u(uW')' = -4 pi beta u^2 (1-u^2) e^{-u^2}.
"""
import mpmath as mp

mp.mp.dps = 50


def s_of_r(r, E, beta):
    rhs = E + 1 / r
    s = 2 * rhs  # beta = 0 value
    for _ in range(200):
        f = s / 2 - beta * mp.e**(-s) / r - rhs
        fp = mp.mpf(1) / 2 + beta * mp.e**(-s) / r
        ds = f / fp
        s -= ds
        if abs(ds) < mp.mpf(10) ** (-45):
            break
    return s


def apsidal(a, e, beta):
    E = -1 / (2 * a)
    L = mp.sqrt(a * (1 - e**2))
    g = lambda r: s_of_r(r, E, beta) - L**2 / r**2
    r1 = mp.findroot(g, a * (1 - e))
    r2 = mp.findroot(g, a * (1 + e))
    c, h = (r1 + r2) / 2, (r2 - r1) / 2

    def integrand(psi):
        r = c - h * mp.cos(psi)
        pr2 = g(r)
        return L / (r**2 * mp.sqrt(pr2)) * h * mp.sin(psi)
    return 2 * mp.quad(integrand, [0, mp.pi / 2, mp.pi])


def first_order(x, e, beta_q=mp.mpf('0.2'), db=mp.mpf('1e-12')):
    a = 1 / mp.mpf(x)
    d = (apsidal(a, e, db) - apsidal(a, e, -db)) / (2 * db)
    return beta_q * d


def o7_formula(x, e, beta=mp.mpf('0.2')):
    uc = mp.sqrt(mp.mpf(x))
    W = lambda u: mp.e**(-u**2)
    Phi = lambda ee: mp.quad(lambda E: W(uc * mp.sqrt((1 + ee * mp.cos(E)) / (1 - ee * mp.cos(E)))), [0, mp.pi, 2 * mp.pi]) / (2 * mp.pi)
    return 2 * mp.pi * beta * mp.sqrt(1 - e**2) / e * mp.diff(Phi, e)


def o7_small_e(x, beta=0.2):
    u2 = mp.mpf(x)
    return -4 * mp.pi * beta * u2 * (1 - u2) * mp.e**(-u2)


e = mp.mpf('0.3')
ref_v4c = {0.3: -3.9248e-01, 1.0: 4.0047e-02, 2.0: 6.1760e-01}
print("e = 0.3, beta = 0.2, first order: x = GM/(a v*^2) | exact-apsidal-angle derivative | O7 formula | O7 small-e | v4c")
for x in (0.01, 0.1, 0.3, 0.5, 1.0, 2.0, 30.0):
    fo = first_order(x, e)
    o7 = o7_formula(x, e)
    print(f"  {x:6.2f}  {mp.nstr(fo, 7):>14s}  {mp.nstr(o7, 7):>14s}  {mp.nstr(o7_small_e(x), 7):>14s}  {ref_v4c.get(x, '')}")

print("\nnonlinear check at beta = 0.2 itself (exact apsidal angle minus 2 pi), e = 0.3:")
for x in (0.3, 1.0, 2.0, 30.0):
    a = 1 / mp.mpf(x)
    print(f"  x = {x:5.1f}: Delta_phi - 2 pi = {mp.nstr(apsidal(a, e, mp.mpf('0.2')) - 2*mp.pi, 7)}")

print("\nanchor (independent of the gate): beta = 0 gives Delta_phi = 2 pi (Kepler):",
      mp.nstr(apsidal(mp.mpf(3), e, mp.mpf(0)) - 2 * mp.pi, 5))
