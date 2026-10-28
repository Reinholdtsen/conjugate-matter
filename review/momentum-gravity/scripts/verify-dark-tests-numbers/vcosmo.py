"""Independent background cosmology for verifying the dark-tests analysis (K2).

Planck 2018 TT,TE,EE+lowE+lensing parameters (from memory, dagger):
h = 0.6736, omega_b = 0.02237, omega_c = 0.1200, Omega_m = 0.3153 (incl. 0.06 eV nu),
T_CMB = 2.7255 K, N_eff = 3.046, n_s = 0.9649, sigma8 = 0.8111.
Radiation: photons from a_rad T^4 computed here (not copied), neutrinos massless at early times.
Integration: mpmath quadrature (different method from an RK4 grid).
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 30
c_kms = 299792.458
h = 0.6736
H0 = 100*h                     # km/s/Mpc
omb, omc = 0.02237, 0.1200
Om = 0.3153                    # includes massive neutrino (Planck convention)
Neff = 3.046
TCMB = 2.7255

# photon density from first principles: rho_gamma = (pi^2/15) (kT)^4/(hbar c)^3
kB = 1.380649e-23; hbar = 1.054571817e-34; cl = 2.99792458e8; G = 6.67430e-11
Mpc = 3.0856775814913673e22
rho_g = (np.pi**2/15)*(kB*TCMB)**4/(hbar*cl)**3/cl**2       # kg/m^3
H0si = H0*1e3/Mpc
rho_crit = 3*H0si**2/(8*np.pi*G)
Og = rho_g/rho_crit
Or = Og*(1+0.2271*Neff)
OL = 1-Om-Or

def E(z):
    zp = mp.mpf(1)+z
    return mp.sqrt(Or*zp**4+Om*zp**3+OL)

def H(z):
    return H0*E(z)

if __name__ == "__main__":
    print("Omega_gamma h^2 = %.4e   Omega_r = %.5e   Omega_L = %.5f" % (Og*h*h, Or, OL))
    # age
    Gyr = 3.15576e16
    tH = Mpc/1e3/H0/Gyr            # 1/H0 in Gyr
    age = mp.quad(lambda z: 1/((1+z)*E(z)), [0, 10, 1000, 1e5, mp.inf])*tH
    print("Age = %.4f Gyr  [Planck 2018 Table 2 (Plik): 13.797 +- 0.023, S]" % age)
    print("z_eq (Om incl nu) = %.1f ; z_eq (omega_b+omega_c only) = %.1f  [Planck: 3402 +- 26, dagger]"
          % (Om/Or-1, (omb+omc)/(h*h)/Or-1))
    print()
    vstar = 120.0
    print("v*=120 km/s: z, H(z) [km/s/Mpc], proper r_gate [kpc], comoving r_gate [Mpc]")
    for z in [3402, 1089.92, 100, 10, 3, 1, 0.5, 0]:
        Hz = H(z)
        rp = vstar/Hz            # Mpc proper
        print("  z=%8.2f  H=%14.2f  proper=%10.4f kpc  comoving=%8.4f Mpc" % (z, Hz, rp*1e3, rp*(1+z)))
    # peak of comoving radius = minimum of aH = H/(1+z)
    f = lambda z: H(z)/(1+z)
    zmin = mp.findroot(lambda z: mp.diff(f, z), 0.6)
    print("min of aH at z = %.4f, aH = %.3f km/s/Mpc -> comoving r_gate max = %.4f Mpc" % (zmin, f(zmin), vstar/f(zmin)))
    print("analytic (no radiation) q=0: z = (2 OL/Om)^(1/3)-1 = %.4f" % ((2*OL/Om)**(1/3)-1))
    # pivot conversion
    z = 3
    conv = H(z)/(1+z)
    print("k_p = 0.009 s/km at z=3 -> %.4f 1/Mpc = %.4f h/Mpc ; k_p * s_c = k_p*v* = %.4f (exact)"
          % (0.009*conv, 0.009*conv/h, 0.009*vstar))
