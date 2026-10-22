"""Which halo reproduces 3a's m_crit ~ 1e-13 GeV? Broad-form m_crit and N_occ per environment (3a/3b inputs)."""
import math
h=6.62607015e-34; c=299792458.0; e=1.602176634e-19
hbarc=h/(2*math.pi)*c/(1e9*e); cm=1e-2/hbarc; gram=1e-3*c**2/(1e9*e); ckms=c/1e3
S=30*cm**2/gram; vstar=120/ckms
for name,r,s in [("MW local (3a table)",0.4,155),("MW inner 1 kpc (3b)",10,120),("dwarf core",1,30),("UFD Segue 1 (3c)",100,3.7)]:
    rho=r/cm**3; sig=s/ckms
    mb=(math.sqrt(math.pi*S)*rho/sig**2)**0.4
    regime="broad" if sig<=vstar else "narrow"
    print(f"{name:22s} regime {regime:6s} m_crit(broad form) = {mb:.2g} GeV = {mb*1e12:.2g} meV, N_occ = {rho/(mb**4*sig**3):.2g}")
