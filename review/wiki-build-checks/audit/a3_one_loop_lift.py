"""Audit of flag 12, part 3: is V_b's classical flat line lifted at one loop in 1+1?

Part 2 found the masses m_a^2(y) along H = diag(y, 1/y), K = K_ref vary with y while their product
(nonzero ones) does not. A 0-dimensional Gaussian integral (1/2) sum ln m^2 would therefore not lift
the line; the 1+1 field theory's one-loop potential is (1/2) sum_a int d^2p/(2pi)^2 ln(p^2 + m_a^2),
which is not a function of the product alone. Evaluate it two ways:
  (a) on a unit-spacing square lattice, phat^2 = 4 sin^2(p1/2) + 4 sin^2(p2/2) (fully regularized);
  (b) continuum, normal-ordered at scale M = 1: (1/8 pi) sum m^2 [ln(m^2/M^2) - 1]; its log-divergent
      piece is (ln Lambda^2 / 8 pi) Tr M^2, and Tr M^2 = Laplacian of V on target space (part 2).
Positive control: the exactly squeeze-invariant naive potential gives a y-independent result (its
negative mode is dropped; it is a saddle, so only the y-(in)dependence of the other modes is meaningful).
The mass matrices are part 2's closed forms (lambda = mu = f_H = f_K = 1 unless stated).
"""
import numpy as np

def M2_b(y, fH=1., fK=1., lam=1., mu=1.):
    return np.array([[4*lam/fH**2, 0, -2*lam*y**2/fH**2, 2*lam/fH**2],
                     [0, 0, 0, 0],
                     [-2*lam/(fK**2*y**2), 0, (lam*y**2 + 2*mu)/(fK**2*y**2), -lam/(fK**2*y**2)],
                     [2*lam/fK**2, 0, -lam*y**2/fK**2, (lam + 2*mu*y**2)/fK**2]])

def M2_mu(y, fH=1., fK=1., lam=1., mu=1.):
    return np.array([[4*lam/fH**2, 0, -2*lam*y**2/fH**2, 2*lam/fH**2],
                     [0, 0, 0, 0],
                     [-2*lam/(fK**2*y**2), 0, lam/fK**2, (-lam + 8*mu)/(fK**2*y**2)],
                     [2*lam/fK**2, 0, y**2*(-lam + 8*mu)/fK**2, lam/fK**2]])

n = 400
p = 2*np.pi*(np.arange(n) + 0.5)/n          # midpoint grid on the Brillouin zone
P1, P2 = np.meshgrid(p, p)
phat2 = 4*np.sin(P1/2)**2 + 4*np.sin(P2/2)**2

def lattice_V1(ms):
    return sum(0.5*np.mean(np.log(phat2 + m)) for m in ms)

def cont_V1(ms):
    return sum(m*(np.log(m) - 1)/(8*np.pi) for m in ms)

for name, M2f in (("V_b (bounded)", M2_b), ("control V_mu (naive; positive modes only)", M2_mu)):
    print(f"== {name}")
    base_l = base_c = None
    for yv in (1.0, 1.25, 1.5, 2.0, 4.0):
        ev = np.sort(np.linalg.eigvals(M2f(yv)).real)
        ms = ev[ev > 1e-12]                 # drop the zero mode (y-independent) and any negative mode
        vl, vc = lattice_V1(ms), cont_V1(ms)
        if base_l is None:
            base_l, base_c = vl, vc
        print(f"   y = {yv:<5}: masses^2 {np.array2string(ms, precision=5)}  prod = {np.prod(ms):.6f}"
              f"  lattice V1(y) - V1(1) = {vl - base_l:+.6f}  continuum V1(y) - V1(1) = {vc - base_c:+.6f}"
              f"  Tr M^2 = {ms.sum():.5f}")
print("\n== V_b at other couplings (f_H = 1, f_K = 2, lambda = 3, mu = 0.5): lattice V1(y) - V1(1)")
b0 = None
for yv in (1.0, 1.5, 2.0):
    ev = np.sort(np.linalg.eigvals(M2_b(yv, 1., 2., 3., 0.5)).real); ms = ev[ev > 1e-12]
    v = lattice_V1(ms); b0 = v if b0 is None else b0
    print(f"   y = {yv}: {v - b0:+.6f}")
print("\nlattice-integral sanity anchor: 0.5*mean ln(phat^2 + m^2) at m^2 = 1 vs fine grid n = 1600:")
q = 2*np.pi*(np.arange(1600) + 0.5)/1600; Q1, Q2 = np.meshgrid(q, q)
fine = 0.5*np.mean(np.log(4*np.sin(Q1/2)**2 + 4*np.sin(Q2/2)**2 + 1.0))
print(f"   n = 400: {0.5*np.mean(np.log(phat2 + 1.0)):.8f}   n = 1600: {fine:.8f}")
