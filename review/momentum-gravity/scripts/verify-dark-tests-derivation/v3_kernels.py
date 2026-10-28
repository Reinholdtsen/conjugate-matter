"""
v3_kernels.py -- verifier's own derivation of the linear-response kernels of the
gated long-range force about the Hubble flow, for three readings of
    U = -Gt m^2 W(|v - v'|/v*) / |x - x'| .

Readings
  (i)   Hamiltonian H = sum p^2/2m + sum U(x_ij, (p_i - p_j)/m): gate on canonical
        momenta; Hamilton's eqs give an anomalous velocity xdot = p/m + dU/dp.
  (ii)  Lagrangian L = sum m v^2/2 - sum U(x_ij, v_i - v_j): gate on velocities.
  (iii) force law m vdot = -grad_x U at fixed velocities, xdot = v (dark-tests K4).

Mean field, cold fluid, Hubble-flow gate (relative velocity of comoving neighbours
at proper separation s is H s).  Units in this script: H = v* = 1 (so s_c = 1),
Gt*rhobar = 1, hence kappa = (4 pi/3) Gt rhobar / H^2 = 4 pi/3.

Kernels (y = k s_c, t = H s / v*):
  R1(y)  = int_0^inf W(x/y) j1(x) dx            density term of the force at fixed P or v
  RA(y)  = y int_0^inf sin(y t) W(t) dt         FT of grad[W(Hs/v*)/s] (dark-tests' R)
  J(y)   = int_0^inf t W'(t) j1(y t) dt         density term of the anomalous velocity
  Rv(y)  = 1 + int_0^inf W'(t) [3 j0 - 6 j1/x](y t) dt   velocity term of the force
  B(y)   = int t W''(A-1) + 2 int W'(3 j1/x - 1)  velocity term of the anomalous velocity
Claimed identities (derived by hand, checked here):
  R1 = int_0^1 RA(y mu) dmu ;  Rv = 3 int_0^1 mu^2 RA(y mu) dmu ;
  R1 - y J = RA ;  B = Rv + 3 y J .
Then an independent brute-force check: the exact (nonlinear) mean-field integrals for
a perturbed medium, evaluated by 2D quadrature at small amplitude, against the kernels.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30

def j0(x): return mp.sin(x)/x if x != 0 else mp.mpf(1)
def j1(x): return (mp.sin(x)/x**2 - mp.cos(x)/x) if x != 0 else mp.mpf(0)

GATES = {
    'gauss':    (lambda t: mp.exp(-t**2/2), lambda t: -t*mp.exp(-t**2/2),
                 lambda t: (t**2-1)*mp.exp(-t**2/2)),
    'rational': (lambda t: 1/(1+t**2/2), lambda t: -t/(1+t**2/2)**2,
                 lambda t: (-1/(1+t**2/2)**2 + 2*t**2/(1+t**2/2)**3)),
}

def quad_osc(f, y):
    # integrate f over (0, inf) with breakpoints at multiples of pi/y
    pts = [0] + [mp.pi*n/y for n in range(1, 400)]
    s = mp.quad(f, pts)
    tail = mp.quad(f, [pts[-1], mp.inf])
    return s + tail

def kernels(gate, y):
    W, dW, d2W = GATES[gate]
    y = mp.mpf(y)
    RA = y*quad_osc(lambda t: mp.sin(y*t)*W(t), y)
    R1 = 1 + quad_osc(lambda t: dW(t)*j0(y*t), y)            # = int W(x/y) j1(x) dx
    J  = quad_osc(lambda t: t*dW(t)*j1(y*t), y)
    A  = lambda x: 3*j0(x) - 6*j1(x)/x if x != 0 else mp.mpf(1)
    Rv = 1 + quad_osc(lambda t: dW(t)*A(y*t), y)
    B  = (quad_osc(lambda t: t*d2W(t)*(A(y*t)-1), y)
          + 2*quad_osc(lambda t: dW(t)*(3*j1(y*t)/(y*t) - 1) if t != 0 else mp.mpf(0), y))
    return dict(RA=RA, R1=R1, J=J, Rv=Rv, B=B)

def RA_closed_gauss(y):
    # sqrt2 y F(y/sqrt2), F Dawson = sqrt(pi)/2 exp(-x^2) erfi(x)
    x = mp.mpf(y)/mp.sqrt(2)
    F = mp.sqrt(mp.pi)/2*mp.exp(-x**2)*mp.erfi(x)
    return mp.sqrt(2)*y*F

print("=== Kernel identities (mpmath quadrature of the defining integrals) ===")
for gate in ('gauss', 'rational'):
    for y in (0.3, 1.0, 1.08, 3.0):
        K = kernels(gate, y)
        W = GATES[gate][0]
        RAy = lambda u: (mp.mpf(u)*y)*quad_osc(lambda t: mp.sin(mp.mpf(u)*y*t)*W(t), mp.mpf(u)*y) if u != 0 else mp.mpf(0)
        # mu-averages of RA (coarse Gauss-Legendre in mu, enough for 1e-6)
        mus, wts = np.polynomial.legendre.leggauss(24)
        mus = 0.5*(mus+1); wts = 0.5*wts
        RAvals = [RAy(m) for m in mus]
        R1_from_RA = sum(w*r for w, r in zip(wts, RAvals))
        Rv_from_RA = 3*sum(w*m**2*r for w, m, r in zip(wts, mus, RAvals))
        line = (f"{gate:8s} y={y:5.2f}: RA={float(K['RA']):.6f} R1={float(K['R1']):.6f} "
                f"[int RA dmu={float(R1_from_RA):.6f}] Rv={float(K['Rv']):.6f} "
                f"[3 int mu^2 RA={float(Rv_from_RA):.6f}] J={float(K['J']):.6f} B={float(K['B']):.6f}")
        print(line)
        print(f"          R1 - yJ = {float(K['R1']-y*K['J']):.6f} (vs RA {float(K['RA']):.6f});"
              f"  Rv + 3yJ = {float(K['Rv']+3*y*K['J']):.6f} (vs B {float(K['B']):.6f})"
              + (f";  closed-form RA (Dawson) = {float(RA_closed_gauss(y)):.6f}" if gate == 'gauss' else ""))

# ---------------------------------------------------------------------------
# Brute force: exact mean-field integrals for a perturbed medium (Gaussian gate),
# H = v* = 1, Gt rhobar = 1.  2D quadrature in (s, mu), azimuth trivial.
# ---------------------------------------------------------------------------
print("\n=== Brute force: exact mean-field integrals vs kernels (Gaussian gate) ===")
W  = lambda t: np.exp(-t**2/2)
dW = lambda t: -t*np.exp(-t**2/2)
xs, xw = np.polynomial.legendre.leggauss(400)
smax = 12.0
s = 0.5*smax*(xs+1); ws = 0.5*smax*xw
mu, wmu = np.polynomial.legendre.leggauss(400)
S, MU = np.meshgrid(s, mu, indexing='ij')
WGT = np.outer(ws, wmu)*2*np.pi          # d^3s = s^2 ds dmu dphi ; s^2 put in integrands
kappa = 4*np.pi/3

def brute(k, dens_amp=0.0, w_amp=0.0):
    # density rho = 1 + dens_amp*sin(k z); peculiar field w(r) = w_amp*cos(k z) zhat
    # particle at origin: w(0) = w_amp zhat; Delta w(s) = w_amp (cos(k s mu) - 1) zhat
    z = S*MU
    rho = 1 + dens_amp*np.sin(k*z)
    dw = w_amp*(np.cos(k*z) - 1)
    # vector Hs + Dw: components (perp, z) = (s sqrt(1-mu^2), s mu + dw)
    vz = S*MU + dw
    vperp = S*np.sqrt(1-MU**2)
    vmag = np.sqrt(vz**2 + vperp**2)
    # force per mass, z comp: Gt int rho W(|Hs+Dw|) (s_z/s^3) d^3s
    a_z = np.sum(WGT*S**2*rho*W(vmag)*MU/S**2)
    # anomalous velocity, z comp: (Gt/v*) int rho W'(|Hs+Dw|) (Hs+Dw)_z/(|Hs+Dw| s) d^3s
    dv_z = np.sum(WGT*S**2*rho*dW(vmag)*(vz/vmag)/S)
    return a_z, dv_z

for k in (0.5, 1.08, 2.0):
    Kg = kernels('gauss', k)
    eps = 1e-4
    ap, vp = brute(k, dens_amp=eps); am, vm = brute(k, dens_amp=-eps)
    a_dens = (ap-am)/(2*eps); v_dens = (vp-vm)/(2*eps)
    ap, vp = brute(k, w_amp=eps); am, vm = brute(k, w_amp=-eps)
    a_vel = (ap-am)/(2*eps); v_vel = (vp-vm)/(2*eps)
    print(f"y={k:4.2f}: force/density  brute {a_dens:.6f}  4pi R1/y {float(4*mp.pi*Kg['R1']/k):.6f}"
          f"  [4pi RA/y would be {float(4*mp.pi*Kg['RA']/k):.6f}]")
    print(f"        anom.vel/density brute {v_dens:.6f}  3 kappa J {float(3*kappa*Kg['J']):.6f}")
    print(f"        force/velocity brute {a_vel:.6f}  kappa Rv {float(kappa*Kg['Rv']):.6f}")
    print(f"        anom.vel/velocity brute {v_vel:.6f}  kappa B {float(kappa*Kg['B']):.6f}")

# local (y -> inf) limits and small-y expansions
print("\n=== Limits (Gaussian) ===")
for y in (10.0, 30.0):
    K = kernels('gauss', y)
    print(f"y={y}: RA={float(K['RA']):.6f} R1={float(K['R1']):.6f} Rv={float(K['Rv']):.6f} "
          f"yJ={float(y*K['J']):.2e} B={float(K['B']):.6f}")
for y in (0.05, 0.1):
    K = kernels('gauss', y)
    print(f"y={y}: RA/y^2={float(K['RA']/y**2):.5f} R1/y^2={float(K['R1']/y**2):.5f} "
          f"Rv/y^2={float(K['Rv']/y**2):.5f} J/y={float(K['J']/y):.5f} B/y^2={float(K['B']/y**2):.5f}")
