"""Step 2c: relic abundances (W' overclosure; psi window) by numerical Boltzmann integration.
Own inputs: M_Pl=1.220890e19, s0=2891.2/cm^3, rho_c/h^2=1.053672e-5 GeV/cm^3 (PDG 2024), Omega_c h^2=0.120 (Planck 2018).
SM g*(T): built from particle content with massive-species integrals and a QCD step at 150 MeV (crude, ~10% level).
"""
import numpy as np
from math import pi, sqrt, log
from scipy.integrate import quad, solve_ivp
from scipy.special import kn, zeta

MPl = 1.220890e19; s0 = 2891.2; rhoc = 1.053672e-5; Oc = 0.120
alpha = 1/137.035999
gd = sqrt(16*pi*alpha); aW = gd**2/(4*pi)

# ------------------------------------------------------------------ detailed-balance sanity check with scalar QED
def sig_gg_SS(beta):  # Born gamma gamma -> S+S-, units of pi alpha^2/m^2 (s = 4m^2/(1-beta^2))
    s_over_m2 = 4/(1-beta**2)
    return (2/s_over_m2)*beta*(2-beta**2-(1-beta**4)/(2*beta)*np.log((1+beta)/(1-beta)))
b = 1e-3
sv_SS = sig_gg_SS(b)*(1/b**2)*(4/1)*0.5*(2*b)
print(f"[check] scalar QED via detailed balance: sigma v(S+S- -> gg) = {sv_SS:.4f} pi a^2/m^2 (textbook: 2)")
c_gg = 6.6666  # from ggww.py (integrated hep-ph/9405359 eq. 5.15 + detailed balance)

# ------------------------------------------------------------------ SM g*(T)
def _I(x, fermion):
    # energy & entropy integrals relative to massless (per dof)
    if x == 0: return 1.0, 1.0
    sgn = 1 if fermion else -1
    def rho_int(u):
        E = np.sqrt(u*u + x*x); return u*u*E/(np.exp(E)+sgn)
    def p_int(u):
        E = np.sqrt(u*u + x*x); return u**4/(3*E)/(np.exp(E)+sgn)
    r = quad(rho_int, 0, 60+x)[0]; p = quad(p_int, 0, 60+x)[0]
    r0 = (7/8 if fermion else 1)*pi**4/15; p0 = r0/3
    return r/r0, (r+p)/(r0+p0)
# (mass GeV, dof, fermion)
leptons = [(0.000511,4,1),(0.10566,4,1),(1.777,4,1),(0,6,1)]  # e, mu, tau, 3 nu (2 dof each incl. anti)
bosons_ew = [(80.4,6,0),(91.19,3,0),(125.1,1,0),(172.7,12,1)]
quarks = [(0.0022,12,1),(0.0047,12,1),(0.095,12,1),(1.27,12,1),(4.18,12,1)]
def gstar(T):
    gr = 2.0; gs = 2.0
    for m,g,f in leptons + bosons_ew:
        a, c = _I(m/T, f); w = (7/8 if f else 1)*g; gr += w*a; gs += w*c
    if T > 0.15:
        a1, c1 = 1, 1; gr += 16; gs += 16
        for m,g,f in quarks:
            a, c = _I(m/T, f); gr += 7/8*g*a; gs += 7/8*g*c
    else:
        for m in [0.1396, 0.1396, 0.1350]:
            a, c = _I(m/T, 0); gr += a; gs += c
    return gr, gs
Tgrid = np.logspace(-4, 4, 161)
G = np.array([gstar(T) for T in Tgrid])
def gs_of(T): return np.interp(np.log(T), np.log(Tgrid), G[:,1])
def gr_of(T): return np.interp(np.log(T), np.log(Tgrid), G[:,0])
print(f"[g*] g*_rho at 1e3,10,1,0.1,0.001 GeV: " + ", ".join(f"{gr_of(T):.2f}" for T in [1e3,10,1,0.1,1e-3]))

# ------------------------------------------------------------------ W' freeze-out (minimal adjoint-only model, shared temperature)
def relic_Y(m, sv, g_internal, gstar_const):
    lam = sqrt(pi/45)*sqrt(gstar_const)*MPl*m*sv  # s*sv/H at x=1, g*s=g*
    def Yeq(x):  # nonrel. Boltzmann, per species
        return 45/(2*pi**4)*sqrt(pi/8)*g_internal/gstar_const*x**1.5*np.exp(-x)
    def rhs(x, Y): return [-lam/x**2*(Y[0]**2 - Yeq(x)**2)]
    x0 = 3.0
    sol = solve_ivp(rhs, [x0, 1e4], [Yeq(x0)], method='Radau', rtol=1e-8, atol=1e-40)
    return sol.y[0,-1]
GeV2cm3s = 1.1673e-17  # 1 GeV^-2 * c in cm^3/s
for m in [4.901e11, 8.757e11]:
    for c in [1.0, c_gg, 10.0, 20.0]:
        sv = c*pi*aW**2/m**2
        Y = relic_Y(m, sv, 3, 108.75)
        Oh2 = 2*Y*m*s0/rhoc
        print(f"W': m={m:.3e} c={c:6.3f} <sv>={sv*GeV2cm3s:.2e} cm^3/s  Omega h^2 = {Oh2:.3e}  -> /0.12 = {Oh2/Oc:.2e}")

# ------------------------------------------------------------------ psi relic with separate hidden temperature
def psi_relic(m, xi0, a_d=alpha, nspecies=2):
    # hidden entropy dof: gamma' (2) + psi (nspecies Dirac = 4*nspecies dof, mass-suppressed)
    def gh(Th):
        a, c = _I(m/Th, 1); return 2 + 7/8*4*nspecies*a, 2 + 7/8*4*nspecies*c
    R = 16*xi0**3/106.75   # s_h/s_v fixed above v (hidden: 16 dof; visible 106.75)
    def Th_of(T):  # solve gh_s(Th) Th^3 = R gs(T) T^3
        Th = T*xi0
        for _ in range(60):
            Th_new = (R*gs_of(T)*T**3/gh(Th)[1])**(1/3)
            if abs(Th_new-Th) < 1e-10*Th: break
            Th = Th_new
        return Th
    sv = pi*a_d**2/m**2
    def rhs(lnT, Y):
        T = np.exp(lnT); Th = Th_of(T)
        rho = pi**2/30*(gr_of(T)*T**4 + gh(Th)[0]*Th**4)
        H = sqrt(8*pi*rho/3)/MPl
        s = 2*pi**2/45*gs_of(T)*T**3*(1+R)
        neq = 2*(m*Th/(2*pi))**1.5*np.exp(-m/Th) if m/Th > 5 else 2*_I(m/Th,1)[0]*0 + 2*3*zeta(3)/(4*pi**2)*Th**3*_n_rel(m/Th)
        Yeq = neq/s
        # d/dt = -H d/dlnT (ignoring dg*s/dT)
        return [s*sv*(Y[0]**2 - Yeq**2)/H]
    T0 = m/(xi0*2)
    Th0 = Th_of(T0)
    neq0 = 2*3*zeta(3)/(4*pi**2)*Th0**3*_n_rel(m/Th0)
    Y0 = neq0/(2*pi**2/45*gs_of(T0)*T0**3*(1+R))
    sol = solve_ivp(rhs, [np.log(T0), np.log(m/(2000))], [Y0], method='Radau', rtol=1e-7, atol=1e-30)
    Y = sol.y[0,-1]
    # today: s_total,0 = s0*(1+R) ; particle+antiparticle per species, nspecies species
    Om = 2*nspecies*Y*m*s0*(1+R)/rhoc
    return Om
def _n_rel(x):  # n(m,T)/n(0,T) for a fermion
    if x < 1e-6: return 1.0
    f = lambda u: u*u/(np.exp(np.sqrt(u*u+x*x))+1)
    return quad(f, 0, 60+x)[0]/(1.5*zeta(3))
for xi0 in [1.0, 0.76, 0.5]:
    out = []
    for m in [10, 30, 100, 200, 300, 600, 1000]:
        Om = psi_relic(m, xi0)
        out.append((m, Om))
    print(f"psi (alpha_d=alpha, 2 Dirac species, xi0={xi0}): " + "; ".join(f"m={m}GeV: Om h2={Om:.3e} ({Om/Oc*100:.1f}% DM)" for m,Om in out))
