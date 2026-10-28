"""
v6_medium_mediator.py  (verify-critic-theory, round 3) -- loopholes T6/T7: a mediator with
propagation speed c_s ~ v* (a medium, or a Lorentz-violating mediator with its own rest frame).

Scalar mediator: (1/c_s^2) phi_tt - lap phi = delta^3(x - V t) (unit source moving at V along x,
in the frame where the mediator propagates isotropically).  With beta = V/c_s, xi = x - V t,
rho = transverse distance:
  subsonic  (beta < 1): phi = 1/(4 pi sqrt(xi^2 + (1-beta^2) rho^2))           (Heaviside ellipsoid)
  supersonic(beta > 1): phi = 1/(2 pi sqrt(xi^2 - (beta^2-1) rho^2)) for xi < -sqrt(beta^2-1) rho, else 0
Checks: the PDE away from the source (sympy); the source strength from the comoving equation
(1-beta^2) phi_xixi + phi_yy + phi_zz = -delta^3, i.e. rescaling xi = sqrt(1-beta^2) xi'.
Then the force on a second body (coupling -g int dt phi(x_2)) at fixed offset from the first,
both moving with the same V: relative velocity zero, force a function of V/c_s.
"""
import sympy as sp

xi, y, z, t, V, cs, X = sp.symbols('xi y z t V c_s x', real=True)
b = sp.symbols('beta', positive=True)

# subsonic
r_sub = sp.sqrt((X - V * t) ** 2 + (1 - V ** 2 / cs ** 2) * (y ** 2 + z ** 2))
phi_sub = 1 / (4 * sp.pi * r_sub)
pde_sub = sp.simplify(sp.diff(phi_sub, t, 2) / cs ** 2 - sp.diff(phi_sub, X, 2) - sp.diff(phi_sub, y, 2) - sp.diff(phi_sub, z, 2))
print("subsonic Heaviside ellipsoid: (1/c_s^2) phi_tt - lap phi away from source =", pde_sub)
print("  V -> 0 limit:", sp.simplify(phi_sub.subs(V, 0)))
# source strength: flux of the comoving operator's 'field' through a small ellipsoid -> check by rescaling
xp = sp.symbols('xp', real=True)
phi_resc = phi_sub.subs(X - V * t, xi).subs(xi, sp.sqrt(1 - V ** 2 / cs ** 2) * xp)
print("  in rescaled coordinate xi = sqrt(1-beta^2) xi':  phi =", sp.simplify(phi_resc),
      " = (1/sqrt(1-beta^2)) / (4 pi r') -> lap' phi = -delta^3(r')/sqrt(1-beta^2), i.e. strength 1 in xi")

# supersonic
r_sup = sp.sqrt((X - V * t) ** 2 - (V ** 2 / cs ** 2 - 1) * (y ** 2 + z ** 2))
phi_sup = 1 / (2 * sp.pi * r_sup)
pde_sup = sp.simplify(sp.diff(phi_sup, t, 2) / cs ** 2 - sp.diff(phi_sup, X, 2) - sp.diff(phi_sup, y, 2) - sp.diff(phi_sup, z, 2))
print("supersonic Mach-cone field: PDE residual inside the cone =", pde_sup)
# its normalization: 2+1 retarded Green function theta(tau - rho)/(2 pi sqrt(tau^2 - rho^2)) with tau = -xi/s, s = sqrt(beta^2-1),
# and delta(xi) = delta(tau)/s  ->  phi = theta(-xi - s rho)/(2 pi sqrt(xi^2 - s^2 rho^2))

print("\nforce on body 2 from body 1, both moving at V (relative velocity 0), separation d, units g^2/(4 pi d^2):")
d = sp.symbols('d', positive=True)
rho = sp.symbols('rho', positive=True)
for beta in [0, sp.Rational(1, 2), sp.Rational(9, 10), sp.Rational(99, 100), 2]:
    if beta < 1:
        ph = 1 / (4 * sp.pi * sp.sqrt(xi ** 2 + (1 - beta ** 2) * rho ** 2))
        F_side = sp.simplify(-sp.diff(ph, rho).subs({xi: 0, rho: d}) * 4 * sp.pi * d ** 2)
        F_inline_behind = sp.simplify(sp.diff(ph, xi).subs({xi: -d, rho: 0}) * 4 * sp.pi * d ** 2)  # body 2 trails at xi = -d
        F_inline_ahead = sp.simplify(-sp.diff(ph, xi).subs({xi: d, rho: 0}) * 4 * sp.pi * d ** 2)
        print(f"  V/c_s = {str(beta):6s}: side-by-side |F| = {sp.nsimplify(F_side)} ; trailing body |F| = {F_inline_behind} ; leading body |F| = {F_inline_ahead}")
    else:
        s = sp.sqrt(beta ** 2 - 1)
        ph = 1 / (2 * sp.pi * sp.sqrt(xi ** 2 - s ** 2 * rho ** 2))
        F_inline_behind = sp.simplify(sp.diff(ph, xi).subs({xi: -d, rho: 0}) * 4 * sp.pi * d ** 2)
        print(f"  V/c_s = {str(beta):6s}: side-by-side |F| = 0 (outside the cone, xi = 0 > -s d) ; trailing body |F| = {F_inline_behind} ;"
              " leading body |F| = 0 (ahead of the source)")
print("  -> at zero relative velocity the interaction depends on V/c_s, the velocity relative to the mediator's frame;"
      " when V > c_s the action-reaction pair is broken (momentum goes into the medium)")
