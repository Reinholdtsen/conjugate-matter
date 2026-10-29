"""Numbers for whether calc note #2's classicality theorem and H-theorem argument carry over to a long-range gate.
m = 70 MeV (benchmark), dwarf core rho = 1 GeV/cm^3, sigma = 30 km/s, isothermal core r_c = 3 sigma t_ff.
1. N particles in the core, two-body relaxation t_relax/t_cross ~ N/(8 ln N) [Binney-Tremaine form, dagger].
2. Occupation per de Broglie cell N_occ = rho/(m^4 sigma^3) (natural units, 3a's definition).
3. Mean field per particle of a 1/r force vs a contact force: for gravity-like coupling the mean-field energy
   per particle is ~ G~ M m / R, independent of m at fixed rho; compare with the contact benchmark g n.
4. Two-body transfer cross-section of an attractive 1/r force of strength G~ (Rutherford with Coulomb log,
   sigma_T ~ 4 pi b90^2 ln Lambda, b90 = 2 G~ m / v^2 for equal masses, relative speed v) vs 30 cm^2/g.
"""
import math
G = 6.67430e-11; GeV_kg = 1.78266192e-27; kpc = 3.0856776e19
m_kg = 0.070*GeV_kg
rho = 1.0*GeV_kg/1e-6
sig = 30e3
tff = 1/math.sqrt(4*math.pi*G*rho)
rc = 3*sig*tff
M = 4*math.pi/3*rc**3*rho
N = M/m_kg
print(f"r_c = {rc/kpc:.3f} kpc, M(<r_c, uniform rho) = {M/1.989e30:.3e} Msun, N = {N:.3e}, ln N = {math.log(N):.1f}")
print(f"t_relax/t_cross ~ N/(8 ln N) = {N/(8*math.log(N)):.3e}")
# occupation (natural units): rho [GeV^4], m [GeV], sigma [c]
cm = 5.0677307e13
for name, rg, s in [("dwarf core", 1.0, 30.0), ("MW local", 0.4, 155.0)]:
    rho_nat = rg/cm**3
    Nocc = rho_nat/(0.070**4*(s/2.99792458e5)**3)
    print(f"{name}: N_occ = rho/(m^4 sigma^3) at m = 70 MeV = {Nocc:.3e}")
# mean field per particle: 1/r force (G~ = G) vs contact benchmark
g_nat = 2483.0   # GeV^-2, 3a benchmark contact coupling
n_nat = (1.0/cm**3)/0.070
eps_contact = g_nat*n_nat           # GeV
eps_grav = G*M*m_kg/rc/GeV_kg/(2.99792458e8)**2   # GeV  (G M m / r_c in GeV)
print(f"mean-field energy per particle: contact benchmark g n = {eps_contact:.3e} GeV; 1/r force at G~=G: G M m/r_c = {eps_grav:.3e} GeV; ratio = {eps_grav/eps_contact:.3e}")
print(f"kinetic scale m sigma^2 = {0.070*(sig/2.99792458e8)**2:.3e} GeV")
# scattering by a 1/r force of strength G~ = G
for v in [30e3, 120e3]:
    b90 = 2*G*m_kg/v**2
    lnL = math.log(N)
    sT = 4*math.pi*b90**2*lnL              # m^2
    sT_per_m = sT*1e4/(m_kg*1e3)           # cm^2/g
    need = math.sqrt(30.0/sT_per_m)
    print(f"v = {v/1e3:.0f} km/s: b90 = {b90:.3e} m, sigma_T/m (G~=G, lnLambda=ln N) = {sT_per_m:.3e} cm^2/g; "
          f"G~/G needed for 30 cm^2/g (sigma_T ~ G~^2) = {need:.3e}")
