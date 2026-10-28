"""Independent linear power spectrum, growth and pair velocities (K3, and inputs for K5-K11).

Two transfer functions, both from memory (dagger):
  (1) Eisenstein & Hu 1998 no-wiggle fit;
  (2) BBKS 1986 with the Sugiyama 1995 shape parameter (a different fit, used as a cross-check).
Normalization: sigma8 = 0.8111 (Planck 2018, dagger). Growth factor D(z), f(z) from the
LambdaCDM growth ODE with radiation, integrated in ln a with a fixed-step RK4 written here.
Independent anchor at the Lyman-alpha pivot: the published Planck-based prediction
Delta^2_L = 0.3495 (+0.0095/-0.0071), n_eff = -2.3052 +- 0.0032 (Rogers & Poulin 2025, Table 2,
Planck+BAO+SNe, Sum m_nu model) [S].
"""
import numpy as np
import vcosmo as C

h, Om, omb, omc = C.h, C.Om, C.omb, C.omc
ns, sigma8 = 0.9649, 0.8111
om = Om*h*h
fb = omb/om
Theta = C.TCMB/2.7

def T_EH_nw(k):            # k in 1/Mpc
    s = 44.5*np.log(9.83/om)/np.sqrt(1+10*omb**0.75)
    aG = 1-0.328*np.log(431*om)*fb+0.38*np.log(22.3*om)*fb**2
    Geff = Om*h*(aG+(1-aG)/(1+(0.43*k*s)**4))
    q = k/h*Theta**2/Geff
    L0 = np.log(2*np.e+1.8*q)
    C0 = 14.2+731/(1+62.5*q)
    return L0/(L0+C0*q*q)

def T_BBKS(k):
    Gam = Om*h*np.exp(-omb/h**2-np.sqrt(2*h)*(omb/h**2)/Om)
    q = k/h/Gam
    return np.log(1+2.34*q)/(2.34*q)*(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**(-0.25)

# ---- growth factor (LambdaCDM, total matter, sub-horizon, radiation smooth)
def growth_table(lna0=np.log(1e-5), lna1=0.0, n=40000):
    Or, OL = C.Or, C.OL
    lna = np.linspace(lna0, lna1, n+1)
    dl = lna[1]-lna[0]
    def rhs(x, y):
        a = np.exp(x)
        E2 = Or/a**4+Om/a**3+OL
        dlnH = (-4*Or/a**4-3*Om/a**3)/(2*E2)
        Omm = Om/a**3/E2
        d, dp = y
        return np.array([dp, -(2+dlnH)*dp+1.5*Omm*d])
    a0 = np.exp(lna0)
    # radiation-era sub-horizon (Meszaros) growing mode: D ~ 1 + 1.5 a/a_eq -> start with D = a + (2/3)aeq, D' = a
    aeq = Or/Om
    y = np.array([a0+2*aeq/3, a0])
    D = np.empty(n+1); Dp = np.empty(n+1)
    D[0], Dp[0] = y
    for i in range(n):
        x = lna[i]
        k1 = rhs(x, y); k2 = rhs(x+dl/2, y+dl/2*k1); k3 = rhs(x+dl/2, y+dl/2*k2); k4 = rhs(x+dl, y+dl*k3)
        y = y+dl/6*(k1+2*k2+2*k3+k4)
        D[i+1], Dp[i+1] = y
    return lna, D, Dp

lna_t, D_t, Dp_t = growth_table()
D0 = D_t[-1]
def Dz(z):
    return np.interp(np.log(1/(1+z)), lna_t, D_t)/D0
def fz(z):
    x = np.log(1/(1+z))
    return np.interp(x, lna_t, Dp_t)/np.interp(x, lna_t, D_t)

def tophat(x):
    x = np.asarray(x, float)
    out = np.where(x < 1e-3, 1-x*x/10, 3*(np.sin(x)-x*np.cos(x))/np.maximum(x, 1e-30)**3)
    return out

kgrid = np.logspace(-5, 3, 6001)    # 1/Mpc
def make_P(Tfun):
    P0 = kgrid**ns*Tfun(kgrid)**2
    R8 = 8/h
    lk = np.log(kgrid)
    s2 = np.trapezoid(kgrid**3*P0*tophat(kgrid*R8)**2/(2*np.pi**2), lk)
    A = sigma8**2/s2
    return A*P0          # P(k, z=0) in Mpc^3

P_EH = make_P(T_EH_nw)
P_BB = make_P(T_BBKS)

def Pz(P, z):
    return P*Dz(z)**2

def j0(x):
    return np.where(np.abs(x) < 1e-4, 1-x*x/6, np.sin(x)/np.where(np.abs(x) < 1e-4, 1, x))

if __name__ == "__main__":
    print("growth: f(z=0) = %.4f ; Omega_m^0.55 = %.4f (dagger) ; D(z=3) = %.4f ; D(1089.92)=%.3e"
          % (fz(0), Om**0.55, Dz(3), Dz(1089.92)))
    # Lyman-alpha pivot
    z = 3
    conv = float(C.H(z))/(1+z)        # (km/s)/Mpc
    kp = 0.009*conv
    for name, P in [("EH98 no-wiggle", P_EH), ("BBKS+Sugiyama", P_BB)]:
        lk = np.log(kgrid); lP = np.log(Pz(P, z))
        lPk = np.interp(np.log(kp), lk, lP)
        dl = 0.01
        n = (np.interp(np.log(kp)+dl, lk, lP)-np.interp(np.log(kp)-dl, lk, lP))/(2*dl)
        D2 = kp**3*np.exp(lPk)/(2*np.pi**2)
        print("%-16s pivot z=3, k_p=%.4f/Mpc: Delta^2 = %.4f, n = %.4f   [published Planck-based: 0.3495, -2.3052]"
              % (name, kp, D2, n))
    print()
    print("pair velocity dispersion at the comoving gate radius (v*=120), EH98 and BBKS:")
    print("   z      f      s_c[Mpc]  s1_EH[km/s] s1_BB[km/s]  kNL_EH[1/Mpc] kNL_BB")
    lk = np.log(kgrid)
    for z in [1089.92, 100, 10, 3, 1, 0.5, 0]:
        Hz = float(C.H(z)); a = 1/(1+z)
        sc = 120*(1+z)/Hz
        out = []
        for P in (P_EH, P_BB):
            Pk = Pz(P, z)
            du2 = (a*Hz*fz(z))**2/np.pi**2*np.trapezoid(kgrid*Pk*(1-j0(kgrid*sc)), lk)
            s1 = np.sqrt(du2/3)
            D2 = kgrid**3*Pk/(2*np.pi**2)
            kNL = np.interp(0.0, np.log(D2), kgrid) if D2.max() > 1 else np.nan
            out += [s1, kNL]
        print("%8.2f  %.3f   %.4f    %8.2f    %8.2f      %8.3f    %8.3f" % (z, fz(z), sc, out[0], out[2], out[1], out[3]))
    # chi thermal velocity illustration (agent's assumption: dark bath at T_gamma until T_kd = m/20)
    m = 70e6   # eV
    for z in [1090, 0]:
        Tg = 8.617333e-5*C.TCMB*(1+z)
        v_noent = np.sqrt(3/20)*(Tg/(m/20))*C.c_kms
        v_ent = v_noent*(4/11)**(1/3)
        print("chi thermal v_rms (3D) at z=%d: %.3e km/s (no e+e- entropy factor) ; %.3e (with (4/11)^(1/3))" % (z, v_noent, v_ent))
