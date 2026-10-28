"""
v3_pairvel.py -- K3 check: rms 1D linear pair-velocity difference at the comoving gate
radius, s1 = sqrt(<|du|^2>/3), <|du|^2> = (aHf)^2/pi^2 int dk P(k)[1 - j0(kr)],
on an Eisenstein-Hu 1998 no-wiggle transfer function (formula from memory, dagger),
sigma_8 = 0.8111, n_s = 0.9649 (Planck 2018 Table 2).  Also the nonlinear wavenumber
Delta^2_lin(k_nl) = 1.  Independent implementation of the same model as dark-tests.
"""
import numpy as np
from v3_cosmo import Hof, Om, Ob, h, TCMB, Om_a, HdotH2

ns, s8 = 0.9649, 0.8111
wm = (Om)*h**2; wb = Ob*h**2; fb = wb/wm; th = TCMB/2.7
s_snd = 44.5*np.log(9.83/wm)/np.sqrt(1 + 10*wb**0.75)
aG = 1 - 0.328*np.log(431*wm)*fb + 0.38*np.log(22.3*wm)*fb**2
def T_nw(k):           # k in 1/Mpc
    Ge = Om*h*(aG + (1 - aG)/(1 + (0.43*k*s_snd)**4))
    q = (k/h)*th**2/Ge
    L0 = np.log(2*np.e + 1.8*q); C0 = 14.2 + 731/(1 + 62.5*q)
    return L0/(L0 + C0*q**2)

# growth D(a) and f(a): single-fluid matter growth with smooth radiation and Lambda
N = np.linspace(np.log(1e-6), 0.0, 60001); dN = N[1] - N[0]
from v3_cosmo import Or
aeq = Or/Om
yi = 1e-6/aeq
D = np.empty_like(N); Dp = np.empty_like(N); D[0] = 1 + 1.5*yi; Dp[0] = 1.5*yi   # Meszaros growing mode [T]
def rhs(n, d, dp):
    a = np.exp(n); return dp, -(2 + HdotH2(a))*dp + 1.5*Om_a(a, 'm')*d
for i in range(len(N)-1):
    d, dp = D[i], Dp[i]
    k1 = rhs(N[i], d, dp); k2 = rhs(N[i]+dN/2, d+dN/2*k1[0], dp+dN/2*k1[1])
    k3 = rhs(N[i]+dN/2, d+dN/2*k2[0], dp+dN/2*k2[1]); k4 = rhs(N[i]+dN, d+dN*k3[0], dp+dN*k3[1])
    D[i+1] = d + dN/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); Dp[i+1] = dp + dN/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
def Dz(z): return np.interp(np.log(1/(1+z)), N, D)/D[-1]
def fz(z): return np.interp(np.log(1/(1+z)), N, Dp/D)

k = np.logspace(-5, 3, 40001)
def W_th(x): return 3*(np.sin(x) - x*np.cos(x))/x**3
P0 = k**ns*T_nw(k)**2
sig2 = np.trapezoid(P0*W_th(k*8/h)**2*k**3/(2*np.pi**2), np.log(k))
A = s8**2/sig2
def P(kk, z): return A*kk**ns*T_nw(kk)**2*Dz(z)**2

print(f"growth anchor: f(z=0) = {fz(0):.4f}  vs Omega_m^0.55 = {Om**0.55:.4f} (Linder fit, dagger)")
for z in (1089.92, 100, 10, 3, 1, 0.5, 0):
    a = 1/(1+z); r = 120/(a*Hof(a))
    x = k*r; j0 = np.where(x < 1e-4, 1 - x**2/6, np.sin(x)/np.maximum(x, 1e-300))
    du2 = (a*Hof(a)*fz(z))**2/np.pi**2*np.trapezoid(P(k, z)*(1 - j0)*k, np.log(k))
    D2 = k**3*P(k, z)/(2*np.pi**2)
    knl = k[np.argmax(D2 > 1)] if (D2 > 1).any() and z < 20 else np.nan
    print(f"z={z:8.2f}: r_gate = {r:.4f} Mpc, f = {fz(z):.3f}, s1 = {np.sqrt(du2/3):7.2f} km/s, k_nl = {knl:.3f} /Mpc")
