import runpy, numpy as np
from math import pi, sqrt
ns = runpy.run_path("step2c_psi.py", run_name="lib")
evolve, gs_of, gr_of, s0, rhoc, Oc = ns['evolve'], ns['gs_of'], ns['gr_of'], ns['s0'], ns['rhoc'], ns['Oc']
alpha = 1/137.035999; gd = sqrt(16*pi*alpha); aW = gd**2/(4*pi)
# (1) W' relic with a colder hidden sector (constant xi, hidden radiation gamma' only besides W')
for xi in [1.0, 0.76]:
    for m in [4.901e11, 8.757e11]:
        c = 6.6666; sv = c*pi*aW**2/m**2
        R = 16*xi**3/106.75
        Y = evolve(m, sv, lambda T: xi*T, 3, lambda T,Th: pi**2/30*2*Th**4,
                   lambda T: 2*pi**2/45*106.75*T**3*(1+R), m/(2*xi), m/(3000*xi), nstep=20000)
        print(f"W' xi={xi} m={m:.3e}: Omega/Omega_DM = {2*Y*m*s0*(1+R)/rhoc/Oc:.2e}")
# (2) corrected Kibble-minimum M* including xi^(3/4)
MPl = 1.220890e19; rho_DM = Oc*rhoc
p = sqrt(8*pi**3*100/90)**3/(2*pi**2/45*100)
for k in [4*pi/gd, 4*pi*1.7867/gd]:
    for xi in [1.0, 0.76]:
        Ms = (rho_DM*k**3*MPl**3/(p*s0))**0.25*xi**0.75
        print(f"Kibble-minimum M* (p={p:.1f}, k={k:.2f}, xi={xi}) = {Ms:.3e} GeV ; benchmark overproduction (3e13/M*)^4 = {(3e13/Ms)**4:.2e}")
# (3) visible electric charge of the DM monopole via hidden theta + kinetic mixing (Bruemmer-Jaeckel-Khoze eq. 3.19): q = chi*theta/(2pi) * e2/e1
for chi in [1e-7, 1e-6]:
    for th in [0.1, 1.0, pi]:
        print(f"chi={chi:.0e}, theta_d={th:.2f}: monopole visible charge ~ {chi*th/(2*pi)*(gd/2)/sqrt(4*pi*alpha):.2e} e")
