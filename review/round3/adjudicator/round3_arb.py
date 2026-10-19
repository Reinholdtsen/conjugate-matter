from math import pi, sqrt, log
M_PL=1.22089e19; M_PL_RED=2.43536e18; S0=2891.2; RHO_DM=0.120*1.05371e-5
gs=100.0
# H = 1.66 sqrt(g*) T^2 / M_Pl  (radiation era, non-reduced Planck mass)
print("1.66 check: sqrt(8 pi^3/90) =", round(sqrt(8*pi**3/90),4))
def p_one_per_hubble(mpl_reduced=False):
    pref = sqrt(pi**2*gs/90) if mpl_reduced else sqrt(8*pi**3*gs/90)
    return pref**3 * 45/(2*pi**2*gs)
print("p, one defect per H^-3, non-reduced M_Pl:", round(p_one_per_hubble(),2))
print("p, one defect per H^-3, reduced M_Pl:    ", round(p_one_per_hubble(True),3))
print("p used in v3 (45/(2 pi^2 g*)):            ", round(45/(2*pi**2*gs),4))
g_d = 2*sqrt(4*pi/137.035999)
for f in (1.0, 1.787):
    r = 4*pi*f/g_d
    v = (RHO_DM*M_PL**3/(r*p_one_per_hubble()*S0))**0.25
    print(f"f={f}: M* (Kibble minimum production) = {r*v:.2e} GeV; v = {v:.2e}; 3e13 overproduced x{(3e13/(r*v))**4:.1e}")
# psi relic: Dirac fermion, sigma v = pi alpha^2/m^2 exact s-wave; count psi+psibar and both doublet members
CM3S=3.8938e-28*2.99792458e10
def omega(m, gstar):
    sig=pi*(1/137.036)**2/m**2
    xf=20.0
    for _ in range(100): xf=log(0.038*2*M_PL*m*sig/sqrt(gstar))-0.5*log(xf)
    return 1.07e9*xf/(sqrt(gstar)*M_PL*sig)
for gstar in (80.0, 106.75):
    for mult,label in ((1,"v3 counting"),(4,"psi+psibar, two doublet members")):
        lo,hi=1.0,1e6
        for _ in range(200):
            m=sqrt(lo*hi); o=mult*omega(m,gstar)
            lo,hi=(m,hi) if o<0.12 else (lo,m)
        m100=m; lo,hi=1.0,1e6
        for _ in range(200):
            m=sqrt(lo*hi); o=mult*omega(m,gstar)
            lo,hi=(m,hi) if o<0.012 else (lo,m)
        print(f"g*={gstar:6.2f} {label:33s}: 100% at {m100:6.0f} GeV, 10% at {m:5.0f} GeV")
