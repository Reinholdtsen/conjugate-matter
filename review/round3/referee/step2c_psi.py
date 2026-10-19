"""psi relic with separate hidden temperature: implicit-Euler Boltzmann (unconditionally stable), tabulated g*'s.
Validation: same integrator applied to a standard visible-sector WIMP with <sv>=2.2e-26 cm^3/s (Majorana-like, g=2, 100 GeV)
must give Omega h^2 ~ 0.1."""
import numpy as np
from math import pi, sqrt
from scipy.integrate import quad
from scipy.special import zeta
import importlib.util, sys
MPl = 1.220890e19; s0 = 2891.2; rhoc = 1.053672e-5; Oc = 0.120
alpha = 1/137.035999
GeV2cm3s = 1.1673e-17

def _I(x, fermion):
    if x < 1e-8: return 1.0, 1.0
    if x > 200: return 0.0, 0.0
    sgn = 1 if fermion else -1
    r = quad(lambda u: u*u*np.sqrt(u*u+x*x)*np.exp(-np.sqrt(u*u+x*x))/(1+sgn*np.exp(-np.sqrt(u*u+x*x))), 0, 60+x)[0]
    p = quad(lambda u: u**4/(3*np.sqrt(u*u+x*x))*np.exp(-np.sqrt(u*u+x*x))/(1+sgn*np.exp(-np.sqrt(u*u+x*x))), 0, 60+x)[0]
    r0 = (7/8 if fermion else 1)*pi**4/15
    return r/r0, (r+p)/(4*r0/3)
def nrel(x):  # fermion number density ratio to massless
    if x < 1e-8: return 1.0
    if x > 200: return 0.0
    return quad(lambda u: u*u*np.exp(-np.sqrt(u*u+x*x))/(1+np.exp(-np.sqrt(u*u+x*x))), 0, 60+x)[0]/(1.5*zeta(3))
# SM g*
leptons = [(0.000511,4,1),(0.10566,4,1),(1.777,4,1)]
heavy = [(80.4,6,0),(91.19,3,0),(125.1,1,0),(172.7,12,1)]
quarks = [(0.0022,12,1),(0.0047,12,1),(0.095,12,1),(1.27,12,1),(4.18,12,1)]
def gsm(T):
    gr = 2 + 7/8*6; gs = gr
    for m,g,f in leptons+heavy:
        a,c = _I(m/T,f); w = (7/8 if f else 1)*g; gr += w*a; gs += w*c
    if T > 0.15:
        gr += 16; gs += 16
        for m,g,f in quarks:
            a,c = _I(m/T,f); gr += 7/8*g*a; gs += 7/8*g*c
    else:
        for m in [0.1396,0.1396,0.1350]:
            a,c = _I(m/T,0); gr += a; gs += c
    return gr, gs
lT = np.linspace(np.log(1e-5), np.log(1e4), 400)
GS = np.array([gsm(np.exp(t)) for t in lT])
gr_of = lambda T: np.interp(np.log(T), lT, GS[:,0]); gs_of = lambda T: np.interp(np.log(T), lT, GS[:,1])
# hidden-sector tables vs x = m/Th
lx = np.linspace(np.log(1e-3), np.log(300), 400)
IX = np.array([_I(np.exp(t),1) for t in lx]); NX = np.array([nrel(np.exp(t)) for t in lx])
Ir = lambda x: np.interp(np.log(x), lx, IX[:,0]); Is = lambda x: np.interp(np.log(x), lx, IX[:,1]); Nr = lambda x: np.interp(np.log(x), lx, NX)

def evolve(m, sv, Th_of_T, g_int, rho_h, s_tot, T0, T1, nstep=40000):
    """implicit Euler in lnT. Y=n/s_tot per species (particle only), g_int internal dof."""
    lnTs = np.linspace(np.log(T0), np.log(T1), nstep)
    T = np.exp(lnTs[0]); Th = Th_of_T(T)
    Y = g_int*3*zeta(3)/(4*pi**2)*Th**3*Nr(m/Th)/s_tot(T)
    for i in range(1, nstep):
        T = np.exp(lnTs[i]); Th = Th_of_T(T)
        rho = pi**2/30*gr_of(T)*T**4 + rho_h(T, Th)
        H = sqrt(8*pi*rho/3)/MPl
        s = s_tot(T)
        x = m/Th
        neq = g_int*(m*Th/(2*pi))**1.5*np.exp(-x) if x > 30 else g_int*3*zeta(3)/(4*pi**2)*Th**3*Nr(x)
        Yeq = neq/s
        h = (lnTs[i-1]-lnTs[i])          # positive step in -lnT
        lam = h*s*sv/H
        Y = (-1 + np.sqrt(1 + 4*lam*(Y + lam*Yeq**2)))/(2*lam)
    return Y

# validation: visible WIMP, g=2 Majorana-like (particle = antiparticle): Omega = Y m s0/rhoc
m = 100.0; sv = 2.2e-26/GeV2cm3s
if __name__ == "__main__":
  Yw = evolve(m, sv, lambda T: T, 2, lambda T,Th: 0.0, lambda T: 2*pi**2/45*gs_of(T)*T**3, m/2, m/3000)
  print(f"[validation] visible Majorana WIMP 100 GeV, <sv>=2.2e-26: Omega h^2 = {Yw*m*s0/rhoc:.4f} (expect ~0.10-0.12)")

def psi(m, xi0, a_d=alpha, nsp=2):
    R = 16*xi0**3/106.75
    def gh(Th): x = m/Th; return 2 + 7/8*4*nsp*Ir(x), 2 + 7/8*4*nsp*Is(x)
    def Th_of(T):
        Th = T*xi0
        for _ in range(100):
            Tn = (R*gs_of(T)*T**3/gh(Th)[1])**(1/3)
            if abs(Tn-Th) < 1e-9*Th: break
            Th = 0.5*(Th+Tn)
        return Th
    s_tot = lambda T: 2*pi**2/45*gs_of(T)*T**3*(1+R)
    rho_h = lambda T, Th: pi**2/30*gh(Th)[0]*Th**4
    sv = pi*a_d**2/m**2
    Y = evolve(m, sv, Th_of, 2, rho_h, s_tot, m/(2*xi0), m/(3000*xi0), nstep=20000)
    return 2*nsp*Y*m*s0*(1+R)/rhoc   # particle+antiparticle, nsp species; today's total entropy s0(1+R)
if __name__ == "__main__":
  for xi0 in [1.0, 0.76, 0.5]:
      res = [(m, psi(m, xi0)) for m in [30, 100, 200, 300, 600, 1000]]
      print(f"xi0={xi0}: " + "; ".join(f"m={m}: {O/Oc*100:.1f}%" for m,O in res))
