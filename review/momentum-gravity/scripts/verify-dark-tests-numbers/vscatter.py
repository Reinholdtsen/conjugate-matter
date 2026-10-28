"""Pairwise scattering by the long-range gated potential (K16), recomputed by direct numerical
integration of the Born amplitude for a screened 1/r potential (screening length b_max), in SI units.
The gate (W ~ 1 for v << v*) is ignored, as in the agent's estimate. Identical-particle exchange is ignored.
CODATA constants [T].
"""
import numpy as np
import mpmath as mp

G = 6.67430e-11; hbar = 1.054571817e-34; c = 2.99792458e8
eV = 1.602176634e-19
kpc = 3.0856775814913673e19
m = 70e6*eV/c**2                   # kg
mu = m/2
kappa = G*m*m                      # J m (G~ = G)

def sigmaT_born_numeric(v, b):
    """sigma_T = Int (1 - cos th) |f|^2 dOmega with f = -2 mu kappa/(hbar^2 (q^2 + 1/b^2)), q = 2k sin(th/2)."""
    k = mu*v/hbar
    pref = (2*mu*kappa/hbar**2)**2
    # integrate over x = ln q from q_min tiny to 2k: dOmega = 2 pi q dq / k^2 ; 1-cos = q^2/(2k^2)
    f = lambda lq: (lambda q: pref/(q*q+b**-2)**2*(q*q/(2*k*k))*2*mp.pi*q*q/(k*k))(mp.e**lq)
    lo = mp.log(1e-8/b); hi = mp.log(2*k)
    return float(mp.quad(f, mp.linspace(lo, hi, 40)))

def frac_back(v, b):
    k = mu*v/hbar
    pref = (2*mu*kappa/hbar**2)**2
    f = lambda lq: (lambda q: pref/(q*q+b**-2)**2*(q*q/(2*k*k))*2*mp.pi*q*q/(k*k))(mp.e**lq)
    tot = mp.quad(f, mp.linspace(mp.log(1e-8/b), mp.log(2*k), 40))
    back = mp.quad(f, [mp.log(mp.sqrt(2)*k), mp.log(2*k)])
    return float(back/tot)

if __name__ == "__main__":
    b = 1.0*kpc
    print("m = 70 MeV = %.4e kg ; kappa = G m^2 = %.4e J m" % (m, kappa))
    for vkms in [10, 30, 100, 300]:
        v = vkms*1e3
        eta = kappa/(hbar*v)
        sT = sigmaT_born_numeric(v, b)            # m^2
        s_cm2_g = sT*1e4/(m*1e3)
        k = mu*v/hbar
        lnL_born = 0.5*(np.log(1+4*k*k*b*b)-1)
        lnL_cl = np.log(b*mu*v*v/kappa)
        print("v=%4d km/s: eta = %.3e ; Born numeric sigma_T/m = %.3e cm^2/g ; Born log %.2f ; classical log %.2f (ratio %.2f)"
              % (vkms, eta, s_cm2_g, lnL_born, lnL_cl, lnL_cl/lnL_born))
    v = 30e3
    s30 = sigmaT_born_numeric(v, b)*1e4/(m*1e3)
    print("G~/G needed for 30 cm^2/g at 30 km/s: %.3e (sigma scales as G~^2; Born log independent of G~)" % np.sqrt(30/s30))
    print("ratio to benchmark at G~ = G: %.3e" % (s30/30))
    print("fraction of sigma_T from theta > 90 deg (Born, 30 km/s, b=1 kpc): %.4f" % frac_back(v, b))
