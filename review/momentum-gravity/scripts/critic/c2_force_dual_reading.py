"""Critic check c2: the reading of 'momentum gravity' in the program's own dual
kinematics (#13), where the Born dual of velocity is force, |dp/dt| <= c~ = c^4/G.

(1) For a gravitating pair the mutual force over c~ is a product of compactnesses:
    F/c~ = (G m1 m2/r^2)/(c^4/G) = (G m1/(r c^2)) (G m2/(r c^2)).
    Dual-kinematic corrections enter as gamma~ - 1 = (1/2)(F/c~)^2 (#13 sec. 2).
(2) Anchor (independent of this script's pair table): #13 sec. 2 states ~1e12 N on a
    kilogram at a neutron-star surface gives gamma~ - 1 ~ 1e-65.
(3) The Siegel mixed block (program P5): X enters ordinary matter's line element
    linearly only through dx . X Y^-1 . dx~.  If the dual coordinate is x~ = (lambda/eps) p
    with lambda/eps = G/c^3 (metastring scales up to the O(1) factor rho, as quoted in
    the diameter note sec. 8.1 [S there]), then dx~/dt = (G/c^3) F and the linear
    mixed term relative to the position block is ~ v F G / c^5 = (power)/(c^5/G).
    This is an inference with stated assumptions, not a record result.
"""
G = 6.67430e-11
c = 2.99792458e8
Msun = 1.98847e30     # dagger: IAU nominal GM_sun / G
Mearth = 5.9722e24    # dagger
Mmoon = 7.342e22      # dagger
AU = 1.495978707e11
ctil = c**4 / G
Pplanck = c**5 / G
print(f"c~ = c^4/G = {ctil:.4e} N ; c^5/G = {Pplanck:.4e} W")

def pair(name, m1, m2, r, v):
    F = G * m1 * m2 / r**2
    x1, x2 = G * m1 / (r * c**2), G * m2 / (r * c**2)
    ratio = F / ctil
    assert abs(ratio / (x1 * x2) - 1) < 1e-12
    print(f"{name:34s} F = {F:.3e} N ; F/c~ = {ratio:.3e} = ({x1:.2e})({x2:.2e}) ; "
          f"gamma~-1 = {0.5*ratio**2:.2e} ; vF/(c^5/G) = {v*F/Pplanck:.2e}")

pair("Sun-Earth (1 AU, v = 29.78 km/s)", Msun, Mearth, AU, 29.78e3)
pair("Earth-Moon (384400 km, 1.02 km/s)", Mearth, Mmoon, 3.844e8, 1.022e3)
pair("Sun-Mercury (0.387 AU, 47.4 km/s)", Msun, 3.3011e23, 0.387 * AU, 47.36e3)
# double pulsar J0737-3039A/B: masses 1.338, 1.249 Msun (dagger), a ~ 8.8e8 m, v_rel ~ 600 km/s
pair("double pulsar (a = 8.8e8 m, 600 km/s)", 1.338 * Msun, 1.249 * Msun, 8.8e8, 6.0e5)
# equal-mass 30+30 Msun binary at separation r = 6 G m_tot/c^2 and r = 2 G m_tot/c^2 (illustrative)
m = 30 * Msun
for k in (6.0, 2.0):
    r = k * G * (2 * m) / c**2
    v = (G * 2 * m / r) ** 0.5
    pair(f"30+30 Msun at r = {k:.0f} G M/c^2", m, m, r, v)
# anchor: kilogram on a neutron star, M = 1.4 Msun, R = 12 km  (#13: ~1e12 N, gamma~-1 ~ 1e-65)
F = G * 1.4 * Msun * 1.0 / (12e3) ** 2
print(f"anchor: 1 kg on a 1.4 Msun, 12 km neutron star: F = {F:.2e} N (#13: ~1e12 N); "
      f"gamma~-1 = {0.5*(F/ctil)**2:.1e} (#13: ~1e-65)")
