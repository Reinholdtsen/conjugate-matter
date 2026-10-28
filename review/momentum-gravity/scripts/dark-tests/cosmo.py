"""Background cosmology and linear power for the dark-tests analysis.

Planck 2018 base-LCDM, TT,TE,EE+lowE+lensing column of Table 2 [S: arXiv:1807.06209,
retrieved 2026-10-26 via ar5iv]:
  Omega_b h^2 = 0.02237, Omega_c h^2 = 0.1200, H0 = 67.36, Omega_m = 0.3153,
  sigma_8 = 0.8111, n_s = 0.9649, z_drag = 1059.94, z_* = 1089.92,
  anchors (not inputs): z_eq = 3402, Age = 13.797 Gyr, r_drag = 147.09 Mpc.
Radiation: T_cmb = 2.7255 K, N_eff = 3.046 massless neutrinos [T] (the 0.06 eV
neutrino of the Planck base model is treated as massless: a reduction).

Linear transfer function: Eisenstein & Hu 1998 (ApJ 496, 605) 'no-wiggle' fit,
eqs. 26 and 28-31 [T, formula from memory (dagger); every parameter carried:
Omega_m h^2, f_b = Omega_b/Omega_m, theta_2.7 = T_cmb/2.7, h].  Checked against
published numbers in dark-tests scripts (Planck-predicted Lyman-alpha compressed
parameters), not against itself.
"""
import numpy as np

C_KMS = 299792.458          # km/s
MPC_KM = 3.0856775814913673e19
GYR_S = 3.15576e16
G_SI = 6.67430e-11          # m^3 kg^-1 s^-2 [T, CODATA 2018]
MSUN = 1.98847e30           # kg
KPC_M = 3.0856775814913673e19
EV_KG = 1.78266192e-36      # kg per eV/c^2

h = 0.6736
H0 = 100.0 * h              # km/s/Mpc
omb = 0.02237
omc = 0.1200
Om = 0.3153                  # Planck's quoted Omega_m (includes 0.06 eV neutrino)
Ob = omb / h**2
Oc = omc / h**2
sigma8 = 0.8111
ns = 0.9649
z_drag = 1059.94
z_star = 1089.92
T_cmb = 2.7255
N_eff = 3.046

# photon density: Omega_gamma h^2 = 2.4728e-5 (T/2.7255)^4  [T]
ogam = 2.4728e-5 * (T_cmb / 2.7255) ** 4
Orad = ogam * (1.0 + 0.2271 * N_eff) / h**2
OL = 1.0 - Om - Orad
f_c = Oc / (Oc + Ob)        # CDM fraction of the clustering matter
f_b = Ob / (Oc + Ob)


def E(a):
    a = np.asarray(a, dtype=float)
    return np.sqrt(Orad / a**4 + Om / a**3 + OL)


def Hz(z):
    return H0 * E(1.0 / (1.0 + np.asarray(z, dtype=float)))


def dlnH_dlna(a):
    a = np.asarray(a, dtype=float)
    num = -4 * Orad / a**4 - 3 * Om / a**3
    return 0.5 * num / E(a) ** 2


def Omega_m_a(a):
    return Om / a**3 / E(a) ** 2


def age_gyr(z=0.0, n=200000):
    # t = int_0^a da/(a H); integrate in ln a
    lna = np.linspace(np.log(1e-9), np.log(1.0 / (1.0 + z)), n)
    a = np.exp(lna)
    integrand = 1.0 / (H0 * E(a))   # (km/s/Mpc)^-1 per unit ln a
    t = np.trapezoid(integrand, lna) * MPC_KM / GYR_S
    return t


def _solve_growth(a_i=1e-6, a_f=1.5, n=30000):
    """Sub-horizon matter growth with smooth radiation and Lambda (Meszaros equation
    generalized), started on the Meszaros growing mode D = 1 + 3y/2, y = a/a_eq [T]."""
    a_eq = Orad / Om
    lna = np.linspace(np.log(a_i), np.log(a_f), n)
    y0 = a_i / a_eq
    y = np.array([1 + 1.5 * y0, 1.5 * y0])  # D, dD/dlna

    def rhs(N, y):
        a = np.exp(N)
        return np.array([y[1], -(2 + dlnH_dlna(a)) * y[1] + 1.5 * Omega_m_a(a) * y[0]])

    D = np.empty(n); Dp = np.empty(n)
    D[0], Dp[0] = y
    for i in range(n - 1):
        N, dN = lna[i], lna[i + 1] - lna[i]
        k1 = rhs(N, y); k2 = rhs(N + dN / 2, y + dN / 2 * k1)
        k3 = rhs(N + dN / 2, y + dN / 2 * k2); k4 = rhs(N + dN, y + dN * k3)
        y = y + dN / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        D[i + 1], Dp[i + 1] = y
    return lna, D, Dp


_g_lna, _g_D, _g_Dp = _solve_growth()
_g_D1 = np.interp(0.0, _g_lna, _g_D)


def growth_LCDM(a_eval):
    """Linear growth factor D(a)/D(1) (Meszaros growing mode with smooth radiation and Lambda)."""
    return np.interp(np.log(a_eval), _g_lna, _g_D) / _g_D1


def growth_rate_f(a):
    """f = dlnD/dlna from the same solution."""
    return np.interp(np.log(a), _g_lna, _g_Dp / _g_D)


def T_EH_nowiggle(k_mpc):
    """Eisenstein & Hu 1998 no-wiggle transfer function; k in 1/Mpc."""
    k = np.asarray(k_mpc, dtype=float)
    omh2 = Om * h**2
    fb = Ob / Om
    th = T_cmb / 2.7
    s = 44.5 * np.log(9.83 / omh2) / np.sqrt(1.0 + 10.0 * (omb) ** 0.75)   # Mpc, eq. 26
    alpha = 1.0 - 0.328 * np.log(431.0 * omh2) * fb + 0.38 * np.log(22.3 * omh2) * fb**2  # eq. 31
    Gam = Om * h * (alpha + (1.0 - alpha) / (1.0 + (0.43 * k * s) ** 4))  # eq. 30
    q = k / h * th**2 / Gam            # eq. 28 (k/h in h/Mpc)
    L0 = np.log(2 * np.e + 1.8 * q)
    C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
    return L0 / (L0 + C0 * q**2)


def _tophat(x):
    x = np.asarray(x, dtype=float)
    out = np.where(x < 1e-3, 1.0 - x**2 / 10.0,
                   3.0 * (np.sin(x) - x * np.cos(x)) / np.maximum(x, 1e-300) ** 3)
    return out


_kgrid = np.logspace(-5, 3, 6000)   # 1/Mpc


def _norm():
    Pk_un = _kgrid**ns * T_EH_nowiggle(_kgrid) ** 2
    R8 = 8.0 / h
    integrand = _kgrid**3 * Pk_un * _tophat(_kgrid * R8) ** 2 / (2 * np.pi**2)
    s2 = np.trapezoid(integrand, np.log(_kgrid))
    return sigma8**2 / s2


A_s_norm = _norm()


def P_lin(k_mpc, z=0.0):
    """Linear matter power, Mpc^3, k in 1/Mpc, LCDM (EH98 no-wiggle, sigma8-normalized)."""
    D = growth_LCDM(1.0 / (1.0 + z)) if z != 0 else 1.0
    k = np.asarray(k_mpc, dtype=float)
    return A_s_norm * k**ns * T_EH_nowiggle(k) ** 2 * D**2


def sigma_R(R_mpc, z=0.0):
    k = _kgrid
    integrand = k**3 * P_lin(k, z) * _tophat(k * R_mpc) ** 2 / (2 * np.pi**2)
    return np.sqrt(np.trapezoid(integrand, np.log(k)))


if __name__ == "__main__":
    print("Omega_b=%.5f Omega_c=%.5f Omega_r=%.4e Omega_L=%.5f f_c=%.4f" % (Ob, Oc, Orad, OL, f_c))
    zeq = Om / Orad - 1.0
    print("z_eq (computed, Omega_m/Omega_r - 1) = %.1f   [Planck 2018 Table 2: 3402 +- 26]" % zeq)
    print("Age (computed) = %.3f Gyr   [Planck 2018 Table 2: 13.797 +- 0.023]" % age_gyr())
    print("sigma_8 check (should be 0.8111): %.4f" % sigma_R(8.0 / h))
    s_EH = 44.5 * np.log(9.83 / (Om * h**2)) / np.sqrt(1.0 + 10.0 * omb ** 0.75)
    print("EH98 eq.26 sound horizon = %.2f Mpc   [Planck r_drag 147.09; EH98 fit quoted ~2%% accurate]" % s_EH)
    print("growth rate f(z=0) = %.4f   [independent anchor: Omega_m^0.55 = %.4f (Linder 2005 fit, dagger)]"
          % (growth_rate_f(1.0), Om ** 0.55))
    print("D(z=3)/D(0) = %.4f ; f(z=3) = %.4f ; f(z=1089.92) = %.4f" %
          (growth_LCDM(0.25), growth_rate_f(0.25), growth_rate_f(1 / 1090.92)))
