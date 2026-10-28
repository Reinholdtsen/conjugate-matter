"""Fast version of vkernels.py (numpy panel quadrature instead of mpmath quadosc; same integrals).

Checks, for the Gaussian and rational gates:
  R_B(y) = y Int sin(yt) W(t) dt (agent's density kernel) by closed form AND by direct quadrature;
  R_A(y) = y Int j1(yt) W(t) dt (reading-A density kernel) by direct quadrature AND via Int_0^1 R_B(y mu) d mu;
  both against a 2D brute-force (r, mu) quadrature of the force on a particle from delta = sin(kz)
  in reading A (only 1/r differentiated) and reading B (gradient of W(r/s)/r);
  the reading-A anti-drag coefficient (4 pi/3) G rho u / H by 2D brute force.
"""
import numpy as np
import mpmath as mp
from vkernels import W_g, Wp_g, W_r, Wp_r, RB_gauss_closed, avg_mu, brute_density, brute_antidrag

def panel_int(f, tmax, npan):
    xg, wg = np.polynomial.legendre.leggauss(40)
    edges = np.linspace(0, tmax, npan+1)
    a = edges[:-1][:, None]; b = edges[1:][:, None]
    t = 0.5*(b-a)*xg[None, :]+0.5*(b+a)
    return float(np.sum(0.5*(b-a)*wg[None, :]*f(t)))

def j1(x):
    x = np.asarray(x, float)
    xs = np.where(x < 1e-3, 1.0, x)
    return np.where(x < 1e-3, x/3, np.sin(xs)/xs**2-np.cos(xs)/xs)

def RB_q(y, W, tmax, npan): return y*panel_int(lambda t: np.sin(y*t)*W(t), tmax, npan)
def RA_q(y, W, tmax, npan): return y*panel_int(lambda t: j1(y*t)*W(t), tmax, npan)

def RB_rat_closed(z):
    if z < 1e-9: return 0.0
    b = mp.sqrt(2)*z
    return float(z/mp.sqrt(2)*(mp.exp(-b)*mp.ei(b)-mp.exp(b)*mp.ei(-b)))

if __name__ == "__main__":
    print("== Gaussian gate")
    print("   y      R_B closed  R_B quad   brute(B)  | R_A quad   Int_0^1 R_B   brute(A) | R_v=3Int mu^2 R_B | R_A/R_B")
    for y in [0.3055, 0.661, 1.0, 1.08, 2.0, 5.0]:
        rb = RB_gauss_closed(y); rbq = RB_q(y, W_g, 40.0, 800)
        bb = brute_density(y, W_g, Wp_g, "B")
        raq = RA_q(y, W_g, 40.0, 800); ra2 = avg_mu(RB_gauss_closed, y, n=200)
        ba = brute_density(y, W_g, Wp_g, "A")
        rv = 3*avg_mu(RB_gauss_closed, y, p=2, n=200)
        print("  %.4f  %.6f   %.6f  %.6f  | %.6f   %.6f      %.6f |  %.5f          | %.3f" % (y, rb, rbq, bb, raq, ra2, ba, rv, ra2/rb))
    print("== rational gate W = 1/(1+u^2/2)  (brute force truncated at r = 60 s)")
    for y in [1.0, 1.08]:
        rb = RB_rat_closed(y)
        ra2 = avg_mu(RB_rat_closed, y, n=120)
        rv = 3*avg_mu(RB_rat_closed, y, p=2, n=120)
        bb = brute_density(y, W_r, Wp_r, "B"); ba = brute_density(y, W_r, Wp_r, "A")
        print("  y=%.3f  R_B(Ei) %.6f brute(B) %.6f | Int_0^1 R_B %.6f brute(A) %.6f | R_v %.5f" % (y, rb, bb, ra2, ba, rv))
    print("== anti-drag in reading A: F/(Gt rho) for peculiar u (units v*, s=1) vs (4 pi/3) u")
    for u in [0.003, 0.03]:
        Fg = brute_antidrag(u, W_g, Wp_g); Fr = brute_antidrag(u, W_r, Wp_r)
        an = 4*np.pi/3*u
        print("  u=%.3f gauss %.6e rational %.6e analytic %.6e ratios %.5f %.5f" % (u, Fg, Fr, an, Fg/an, Fr/an))
    for eps in [1e-4]:
        p0 = (-0.5+np.sqrt(0.25+6*(1+eps)))/2
        b = 0.5-eps/2
        p1 = (-b+np.sqrt(b*b+6*(1+eps)))/2
        print("EdS growth exponent shift per eps: no anti-drag %.5f ; with anti-drag %.5f" % ((p0-1)/eps, (p1-1)/eps))
    print("(v*/c)^2 at 120 km/s = %.4e" % ((120/299792.458)**2))
