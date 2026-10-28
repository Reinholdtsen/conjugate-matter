"""Kernels of the gated force about the Hubble flow (K4), derived and checked independently.

Medium: uniform density rho with Hubble flow v = H x; gate W(|v-v'|/v*), s = v*/H.
Reading A (the agent's stated reading): force on a particle = -grad_x U at FIXED velocities,
i.e. only 1/r is differentiated:  F/m = Gt * Int d^3r rho(x+r) W(|v(x+r)-v(x)|/v*) rhat/r^2.
Reading B (static effective potential): F = -grad of Phi(x) = -Gt Int rho W(r/s)/r, W differentiated too.

Density kernels (force from delta = sin(k z) at the origin, in units of the Newtonian 4 pi G rho delta/k):
  R_B(y) = y Int_0^inf sin(y t) W(t) dt           (agent's R)
  R_A(y) = y Int_0^inf j1(y t) W(t) dt            (what reading A gives)
Claimed identity (derived here by parts):  R_A(y) = Int_0^1 R_B(y mu) d mu.
Velocity kernel of reading A (anti-drag): R_v(y) = 3 Int_0^1 mu^2 R_B(y mu) d mu (agent's).
All checked by direct 2D quadrature in (r, mu) of the force integrals, without the identities.
"""
import numpy as np
import mpmath as mp

def W_g(t): return np.exp(-t*t/2)
def Wp_g(t): return -t*np.exp(-t*t/2)
def W_r(t): return 1/(1+t*t/2)
def Wp_r(t): return -t/(1+t*t/2)**2

def RB_gauss_closed(y):
    # sqrt2 * y * Dawson(y/sqrt2), Dawson(x) = sqrt(pi)/2 exp(-x^2) erfi(x)
    x = mp.mpf(y)/mp.sqrt(2)
    daw = mp.sqrt(mp.pi)/2*mp.exp(-x*x)*mp.erfi(x)
    return float(mp.sqrt(2)*y*daw)

def RB_num(y, W):
    # y Int_0^inf sin(yt) W(t) dt, oscillatory quadrature
    f = lambda t: mp.sin(y*t)*W(t)
    return float(y*mp.quadosc(f, [0, mp.inf], omega=y))

def Wg_mp(t): return mp.exp(-t*t/2)
def Wr_mp(t): return 1/(1+t*t/2)

def RA_num(y, W):
    j1 = lambda x: (mp.sin(x)/x**2-mp.cos(x)/x) if x > 1e-6 else x/3
    f = lambda t: j1(y*t)*W(t)
    return float(y*mp.quadosc(f, [0, mp.inf], omega=y))

def avg_mu(fun, y, p=0, n=400):
    # Int_0^1 mu^p fun(y mu) d mu, Gauss-Legendre
    x, w = np.polynomial.legendre.leggauss(n)
    mu = 0.5*(x+1); w = 0.5*w
    return float(np.sum(w*mu**p*np.array([fun(y*m) for m in mu])))

def brute_density(y, W, Wp, reading):
    """Force at origin from rho = rho0(1+delta sin(k z')), s = 1, k = y. 2D quadrature in (r, mu).
    Returns F_z in units of 4 pi G rho0 delta / k."""
    k = y
    # r grid: integrate to where W is negligible; use substitution r in [0, Rmax]
    Rmax = 60.0 if W is W_r else 12.0
    nr, nm = 6000, 200
    xr, wr = np.polynomial.legendre.leggauss(nr)
    # split r range in panels to resolve oscillations
    edges = np.linspace(0, Rmax, 61)
    xm, wm = np.polynomial.legendre.leggauss(nm)
    mu = xm; wmu = wm                    # mu in [-1,1]
    tot = 0.0
    xg, wg = np.polynomial.legendre.leggauss(100)
    for a, b in zip(edges[:-1], edges[1:]):
        r = 0.5*(b-a)*xg+0.5*(b+a); w = 0.5*(b-a)*wg
        R, M = np.meshgrid(r, mu, indexing="ij")
        WW = np.outer(w, wmu)
        if reading == "A":
            radial = W(R)/R**2                     # |force| per unit source mass, attractive
        else:
            radial = W(R)/R**2-Wp(R)/R             # -d/dr [W(r)/r] = W/r^2 - W'/r  (s=1)
        integrand = np.sin(k*R*M)*radial*M*R**2    # F_z: rhat_z = mu ; d^3r = 2 pi r^2 dr dmu
        tot += 2*np.pi*np.sum(WW*integrand)
    return tot/(4*np.pi/k)

def brute_antidrag(u, W, Wp, n_r=4000, n_m=400):
    """Reading A: particle with peculiar velocity u (units of v*) along z in a uniform Hubble-flow medium
    (s = 1, H = 1, v* = 1). F_z/(Gt rho) = Int d^3r W(|r - u zhat|) mu / r^2 ; analytic linear: (4 pi/3) u."""
    Rmax = 200.0 if W is W_r else 14.0
    edges = np.concatenate([np.linspace(0, 4, 81), np.linspace(4, Rmax, 81)[1:]])
    xg, wg = np.polynomial.legendre.leggauss(60)
    xm, wm = np.polynomial.legendre.leggauss(n_m)
    tot = 0.0
    for a, b in zip(edges[:-1], edges[1:]):
        r = 0.5*(b-a)*xg+0.5*(b+a); w = 0.5*(b-a)*wg
        R, M = np.meshgrid(r, xm, indexing="ij")
        rel = np.sqrt(R*R-2*R*u*M+u*u)            # |H r - u|
        tot += 2*np.pi*np.sum(np.outer(w, wm)*W(rel)*M)
    return tot

if __name__ == "__main__":
    print("== density kernels, Gaussian gate W = exp(-u^2/2)")
    print("  y     R_B closed  R_B quadosc  R_B brute(B) | R_A quadosc  Int_0^1 R_B(y mu)  R_A brute(A) | R_v")
    for y in [0.3055, 0.661, 1.0, 1.08, 2.0, 5.0]:
        rb = RB_gauss_closed(y); rbn = RB_num(y, Wg_mp); bb = brute_density(y, W_g, Wp_g, "B")
        ra = RA_num(y, Wg_mp); ra2 = avg_mu(RB_gauss_closed, y); ba = brute_density(y, W_g, Wp_g, "A")
        rv = 3*avg_mu(RB_gauss_closed, y, p=2)
        print("  %.4f  %.6f   %.6f    %.6f     | %.6f     %.6f          %.6f     | %.4f" % (y, rb, rbn, bb, ra, ra2, ba, rv))
    print("== rational gate W = 1/(1+u^2/2)")
    for y in [1.0, 1.08]:
        rbn = RB_num(y, Wr_mp); ra = RA_num(y, Wr_mp)
        RBr = lambda z: RB_num(z, Wr_mp) if z > 1e-8 else 0.0
        ra2 = avg_mu(RBr, y, n=60)
        rv = 3*avg_mu(RBr, y, p=2, n=60)
        print("  y=%.3f  R_B = %.6f  R_A = %.6f  Int_0^1 R_B = %.6f  R_v = %.4f" % (y, rbn, ra, ra2, rv))
    print("== anti-drag (reading A), linear coefficient check: F/(Gt rho) vs (4 pi/3) u")
    for u in [0.003, 0.03]:
        Fg = brute_antidrag(u, W_g, Wp_g); Fr = brute_antidrag(u, W_r, Wp_r)
        print("  u/v*=%.3f gauss %.6e rational %.6e analytic %.6e ratios %.5f %.5f" % (u, Fg, Fr, 4*np.pi/3*u, Fg/(4*np.pi/3*u), Fr/(4*np.pi/3*u)))
    print("== reading B (static effective potential): net force on a moving particle in a uniform medium")
    # In reading B the force is -grad of a function of r only (W(|Hr-u|)/r with u fixed): its integral is a surface term -> 0.
    # numerically: Int d^3r d/dz [W(|r-u z|)/r]  computed as Int (W(rel)/r^2 + ...) is identically a surface term; skip.
    print("  (surface term; zero analytically)")
    # growth exponents EdS single fluid, full gate
    for eps in [1e-4]:
        p0 = (-0.5+np.sqrt(0.25+6*(1+eps)))/2
        # anti-drag: friction coefficient (1/2 - eps/2)
        b = 0.5-eps/2
        p1 = (-b+np.sqrt(b*b+6*(1+eps)))/2
        print("EdS growth exponent shift per eps: no anti-drag %.5f ; with anti-drag %.5f" % ((p0-1)/eps, (p1-1)/eps))
    print("(v*/c)^2 at 120 km/s = %.4e" % ((120/299792.458)**2))
