"""
v3_eds_check.py -- growth exponents p (delta ~ a^p) in an Einstein-de Sitter, all-chi
universe in the local limit (y >> 1: RA, R1, Rv, B -> 1, yJ -> 0), for each reading.
Hand derivation (this verifier):
  (iii) force law:   p^2 + p(1/2 - eps/2) - (3/2)(1+eps) = 0      -> p-1 = 0.8 eps + O(eps^2)
  (i)  Hamiltonian:  p^2 + p/2 - (3/2)(1+eps)(1+eps/2) = 0        -> p-1 = 0.9 eps + O(eps^2)
  (ii) Lagrangian:   p^2 + p/2 - (3/2)(1+eps)/(1-eps/2) = 0       -> p-1 = 0.9 eps + O(eps^2)
  no velocity terms: p^2 + p/2 - (3/2)(1+eps) = 0                  -> p-1 = 0.6 eps
The script solves the quadratics with sympy and integrates the first-order systems
numerically (sanity check of the integrator's equations, local limit only).
"""
import numpy as np
import sympy as sp

p, e = sp.symbols('p e', positive=True)
quads = {
    'iii (force law)': p**2 + p*(sp.Rational(1,2) - e/2) - sp.Rational(3,2)*(1+e),
    'i (Hamiltonian)': p**2 + p/2 - sp.Rational(3,2)*(1+e)*(1+e/2),
    'ii (Lagrangian)': p**2 + p/2 - sp.Rational(3,2)*(1+e)/(1-e/2),
    'no velocity terms': p**2 + p/2 - sp.Rational(3,2)*(1+e),
}
for name, q in quads.items():
    root = [r for r in sp.solve(q, p) if sp.limit(r, e, 0) == 1][0]
    ser = sp.series(root, e, 0, 3).removeO()
    print(f"{name:18s}: p = {sp.simplify(ser)}   ; p(eps=0.1) = {float(root.subs(e, 0.1)):.6f}")

def integrate(reading, eps, nstep=20000, N1=6.0):
    kap = eps/2
    d, th = 1.0, 1.0
    dN = N1/nstep
    def rhs(d, th):
        grav = 1.5*d
        if reading == 'iii':
            return th, -0.5*th + grav + 3*kap*d + kap*th
        if reading == 'noad':
            return th, -0.5*th + grav + 3*kap*d
        if reading == 'i':
            return (1+kap)*th, -0.5*th + grav + 3*kap*d
        if reading == 'ii':
            thu = th/(1-kap)
            return thu, 0.5*th - thu + grav + 3*kap*d + kap*thu
    hist = []
    for i in range(nstep):
        k1 = rhs(d, th); k2 = rhs(d+0.5*dN*k1[0], th+0.5*dN*k1[1])
        k3 = rhs(d+0.5*dN*k2[0], th+0.5*dN*k2[1]); k4 = rhs(d+dN*k3[0], th+dN*k3[1])
        d += dN/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); th += dN/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        hist.append(d)
    hist = np.array(hist)
    # late-time logarithmic slope
    return (np.log(hist[-1]) - np.log(hist[-1001]))/(1000*dN)

for r in ('noad', 'iii', 'i', 'ii'):
    pp = integrate(r, 0.1)
    print(f"numerical EdS local-limit exponent, reading {r:5s}, eps=0.1: p = {pp:.6f}, (p-1)/eps = {(pp-1)/0.1:.4f}")
