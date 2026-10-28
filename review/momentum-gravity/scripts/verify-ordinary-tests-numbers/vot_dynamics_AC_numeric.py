# Numerical (mpmath, 40 digits) replacement for parts (A) and (C) of vot_dynamics.py: the explicit-W
# sympy version (vot_dynamics_AC.py) did not finish in 900 s.  Both routes use the first-order
# Hamiltonian H = (p_r^2 + l^2/r^2)/2 - (1/r)(1 + eps W(|p|/v*)), GM = 1, l = 1.
#  (A) circular orbit dH/dr = 0, Omega = dH/dl -> (Omega^2 r^3 - 1)/eps vs K(u) = W - uW'
#  (C) epicyclic frequency omega_r^2 = H_rr H_pp at p_r = 0 -> 2 pi (Omega/omega_r - 1)/eps vs pi u (uW')'
import mpmath as mp
mp.mp.dps = 40
eps = mp.mpf('1e-12')
shapes = {'Gaussian': lambda y: mp.e**(-y**2), 'Lorentzian': lambda y: 1/(1 + y**2)}
for name, W in shapes.items():
    K = lambda y: W(y) - y*mp.diff(W, y)
    adv_formula = lambda y: mp.pi*y*mp.diff(lambda t: t*mp.diff(W, t), y)
    for u in [mp.mpf('0.3'), mp.mpf('0.7071067811865475'), mp.mpf(1), mp.mpf('1.6'), mp.mpf(3)]:
        vs = 1/u          # zeroth order: r0 = 1, |p| = 1 -> u = 1/v*
        H = lambda r, pr, l: (pr**2 + l**2/r**2)/2 - (1/r)*(1 + eps*W(mp.sqrt(pr**2 + l**2/r**2)/vs))
        r0 = mp.findroot(lambda r: mp.diff(lambda rr: H(rr, 0, 1), r), 1)
        Om = mp.diff(lambda l: H(r0, 0, l), 1)
        kep = (Om**2*r0**3 - 1)/eps
        Hrr = mp.diff(lambda rr: H(rr, 0, 1), r0, 2)
        Hpp = mp.diff(lambda p: H(r0, p, 1), 0, 2)
        dw = 2*mp.pi*(Om/mp.sqrt(Hrr*Hpp) - 1)/eps
        print(f"{name:10s} u = {mp.nstr(u, 6):>8s}: (Omega^2 r^3 - 1)/eps = {mp.nstr(kep, 12):>16s} ; K(u) = {mp.nstr(K(u), 12):>16s} ;"
              f" epicyclic dw/eps = {mp.nstr(dw, 12):>16s} ; pi u (uW')' = {mp.nstr(adv_formula(u), 12)}")
