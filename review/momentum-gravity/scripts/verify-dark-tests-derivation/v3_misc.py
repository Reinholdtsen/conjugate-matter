"""
v3_misc.py -- verifier's checks of K2, K5 kernel values, K7 (no-anti-drag variant),
K8 (eBOSS, per reading), K9 (BOSS mapping, per reading), K10 (peculiar gate under the
Hamiltonian reading), K11 (small-scale power at each reading's boundary), K13-K15 (gate
averages), K16 (scattering), and the singular-inertia threshold of readings i/ii.
"""
import numpy as np
import mpmath as mp
from v3_cosmo import grow, kpivot, Hof, Om_a, Oc, Om, OL, Or, H0, h, C_KMS, kern
from v3_lya import transfer, cov, chi2

print("=== K2: gate radius v*/H (proper) and (1+z) v*/H (comoving), v* = 120 km/s ===")
for z in (3402, 1089.92, 100, 10, 3, 0):
    a = 1/(1+z); Hz = Hof(a)
    print(f"  z={z:8.2f}: H={Hz:12.2f} km/s/Mpc  proper {120/Hz*1e3:10.4f} kpc  comoving {120/(a*Hz):8.4f} Mpc")
aa = np.linspace(0.3, 1.0, 700001)
aH = aa*Hof(aa); i = np.argmin(aH)
print(f"  min aH = {aH[i]:.3f} km/s/Mpc at z = {1/aa[i]-1:.4f}; s_c,max = {120/aH[i]:.4f} Mpc;"
      f" analytic q=0 point a^3 = Om/(2 OL) (radiation neglected): z = {(2*OL/Om)**(1/3)-1:.4f}")

print("\n=== K5: kernels at the pivot (k_p v* = 1.08 at z=3; s_c(z) = v*/(aH)) ===")
kp = kpivot()
for z in (1089.92, 50, 10, 3):
    a = 1/(1+z); y = kp*120/(a*Hof(a)); K = kern('gauss', np.array([y]))
    print(f"  z={z:8.2f}: y={y:.4f}  RA={K['RA'][0]:.4f}  R1(force-law density kernel)={K['R1'][0]:.4f}  Rv={K['Rv'][0]:.4f}  B={K['B'][0]:+.4f}  yJ={K['yJ'][0]:+.4f}")

print("\n=== singular-inertia threshold (readings i, ii): min_y B(y) ===")
yy = np.logspace(-2, 3, 20001)
for gate in ('gauss', 'rational'):
    Kb = kern(gate, yy)['B']; j = np.argmin(Kb)
    print(f"  {gate}: min B = {Kb[j]:+.4f} at y = {yy[j]:.3f}; max B = {Kb.max():+.4f};"
          f" 1 + kappa B = 0 at kappa = {-1/Kb[j]:.3f} (i), 1 - kappa B = 0 at kappa = {1/Kb.max():.3f} (ii);"
          f" kappa = eps Omega_c(a)/2, Omega_c(z=10) = {Om_a(1/11,'c'):.3f}")

print("\n=== K7 variant: agent's system without anti-drag, v*=120 (agent: 0.0345) ===")
C = cov((0.0083, 0.0032))
eps_grid = np.concatenate([[0.0], np.logspace(-3.5, np.log10(12.0), 200)])
def bnd(T2, dn, Cm):
    c2 = chi2(T2, dn, Cm); i0 = np.argmin(c2); d = c2 - c2[i0]
    for i in range(i0, len(c2)-1):
        if d[i] < 3.84 <= d[i+1]:
            lo = max(eps_grid[i], 1e-5); f = (3.84-d[i])/(d[i+1]-d[i])
            return np.exp(np.log(lo) + f*(np.log(eps_grid[i+1])-np.log(lo))), eps_grid[i0], c2[0]-c2[i0]
    return np.nan, eps_grid[i0], c2[0]-c2[i0]
tr = transfer('agent_noad', 120, eps_grid)
print(f"  matter bound = {bnd(*tr['m'], C)[0]:.4f}")

print("\n=== K8: eBOSS compressed (0.310 +- 0.020, -2.340 +- 0.006, r = 0.512) per reading ===")
import v3_lya as L
def cov_e():
    s = np.array([0.020, 0.006]); r = 0.512
    c = np.array([[s[0]**2, r*s[0]*s[1]], [r*s[0]*s[1], s[1]**2]]) + np.diag(np.array([0.0083, 0.0032])**2)
    return c
Ce = cov_e()
def chi2_e(T2, dn):
    Ci = np.linalg.inv(Ce)
    d = np.stack([0.3495*T2 - 0.310, -2.3052 + dn + 2.340], axis=-1)
    return np.einsum('...i,ij,...j->...', d, Ci, d)
for rd in ('agent', 'iii', 'i'):
    for vs in (30, 120, 300):
        T2, dn = transfer(rd, vs, eps_grid)['m']
        c2 = chi2_e(T2, dn); i0 = np.argmin(c2)
        d = c2 - c2[i0]
        up = np.nan
        for i in range(i0, len(c2)-1):
            if d[i] < 3.84 <= d[i+1]:
                lo = max(eps_grid[i], 1e-5); f = (3.84-d[i])/(d[i+1]-d[i])
                up = np.exp(np.log(lo) + f*(np.log(eps_grid[i+1])-np.log(lo))); break
        print(f"  {rd:5s} v*={vs:4d}: chi2(eps=0) = {c2[0]:.2f}, best eps = {eps_grid[i0]:.4f} (chi2 = {c2[i0]:.2f}, "
              f"T^2 = {T2[i0]:.4f}, dn = {dn[i0]:+.4f}), upper bound = {up:.5f}")

print("\n=== K9: BOSS-scale mapping per reading (excess at k = 0.2 h/Mpc, z = 0.57) ===")
kB = np.array([0.2*h])
dc, db, dm = grow(kB, 0.0048, 120, 'ungated', a_end=1/1.57)
dc0, db0, dm0 = grow(kB, 0.0, 120, 'lcdm', a_end=1/1.57)
ex_u = (dm[0]/dm0[0])**2 - 1
print(f"  ungated beta = 0.0048 excess = {ex_u:.4f} (agent: 0.0377)")
for rd in ('agent', 'iii', 'i'):
    out = []
    for vs in (120, 300, 1000, 2000, 3000):
        d1 = grow(kB[:, None], eps_grid[None, :], vs, rd, a_end=1/1.57)[2]
        ex = (d1[0]/dm0[0])**2 - 1
        j = np.argmax(ex > ex_u)
        eq = np.interp(ex_u, ex[:j+1], eps_grid[:j+1]) if ex[j] > ex_u else np.nan
        exmin = ex.min()
        out.append(f"v*={vs}: {eq:.4f}" + (f" (min excess {exmin:+.4f})" if exmin < 0 else ""))
    print(f"  {rd:5s}: " + "; ".join(out))

print("\n=== K10: peculiar-velocity gate under the Hamiltonian reading ===")
# Psi(w) = -Gt m rhobar W(|w|/v*) int d^3s/s = -Gt m rhobar W 2 pi R^2  (uniform medium, radius R)
# -> inverse-mass renormalization kappa_pec = 2 pi Gt rhobar R^2 |W''(0)|/v*^2
#    = (3/4) eps Omega_c(a) (H R / v*)^2 for the Gaussian gate (|W''(0)| = 1)
for z in (0.0, 3.0):
    a = 1/(1+z)
    for vs in (120.0,):
        kap_pec = 0.75*Om_a(a, 'c')*(C_KMS/vs)**2      # R = c/H
        print(f"  z={z}: kappa_pec/eps (R = c/H, v* = {vs:.0f}) = {kap_pec:.3e};  Hubble-flow gate kappa/eps = {0.5*Om_a(a,'c'):.3f}")

print("\n=== K11: T_m^2 at k = 10/Mpc, z = 3, at each reading's DESI matter boundary ===")
bounds = {'agent': {120: 0.0285, 10: 3.0865}, 'iii': {120: 0.0585, 10: 6.9609}, 'i': {120: 0.0573, 10: 3.1347}}
for rd, bd in bounds.items():
    for vs, e in bd.items():
        d1 = grow(np.array([10.0]), e, vs, rd, a_end=0.25)[2]; d0 = grow(np.array([10.0]), 0.0, vs, 'lcdm', a_end=0.25)[2]
        print(f"  {rd:5s} v*={vs:4d} eps={e:.4f}: T_m^2(10/Mpc, z=3) = {(d1[0]/d0[0])**2:.3f}")

print("\n=== K13-K15: Gaussian gate averaged over a Maxwellian relative velocity ===")
def W_avg_closed(V, s, vs): return (vs**2/(vs**2+s**2))**1.5*np.exp(-V**2/(2*(vs**2+s**2)))
def W_avg_num(V, s, vs, n=400001):
    # isotropic Gaussian of 1D dispersion s centred at V zhat; integrate over |w| and cos
    w = np.linspace(0, V + 12*s, 4001)
    mu, wm = np.polynomial.legendre.leggauss(200)
    Wg, Mg = np.meshgrid(w, mu, indexing='ij')
    pdf = np.exp(-(Wg**2 - 2*Wg*V*Mg + V**2)/(2*s**2))/(2*np.pi*s**2)**1.5
    integ = 2*np.pi*Wg**2*pdf*np.exp(-Wg**2/(2*vs**2))
    return np.trapezoid(np.sum(integ*wm, axis=1), w)
cases = [("Sgr: V=311.1, s^2 = 149.9^2 + 12^2", 311.1, np.hypot(149.9, 12.0), 120.0),
         ("Bullet inter-cluster: V=2600, s^2 = 1250^2 + 210^2", 2600.0, np.hypot(1250.0, 210.0), 120.0),
         ("Bullet within main: V=0, s = sqrt2*1250", 0.0, np.sqrt(2)*1250, 120.0),
         ("dSph sigma=10: V=0, s = sqrt2*10", 0.0, np.sqrt(2)*10, 120.0),
         ("MW sigma=155: V=0, s = sqrt2*155", 0.0, np.sqrt(2)*155, 120.0),
         ("dSph sigma=10 at v*=30", 0.0, np.sqrt(2)*10, 30.0)]
for lab, V, s, vs in cases:
    wc = W_avg_closed(V, s, vs); wn = W_avg_num(V, s, vs)
    print(f"  {lab:50s} v*={vs:5.0f}: closed {wc:.4e}  numeric {wn:.4e}")
wS = W_avg_closed(311.1, np.hypot(149.9, 12.0), 120.0)
print(f"  Sgr translated limit (eps <W> < 0.1): eps < {0.1/wS:.3f}")
# Hamiltonian-reading inertia term for the satellite's chi in the host's gated potential:
# Psi_sat(r,P) ~ eps <W>(V) m Phi_N(r) with Phi_N the host's Newtonian potential (zero at infinity).
# inverse-mass shifts: transverse eta_perp = eps |Phi_N| <W>/S^2 ; longitudinal eta_par = -eps |Phi_N| <W> (V^2/S^2 - 1)/S^2
S2 = 120.0**2 + 149.9**2 + 12.0**2
vc = 212.0
for rt in (200.0, 300.0):
    PhiN = vc**2*(1 + np.log(rt/18.11))       # truncated singular isothermal sphere, |Phi| at 18.11 kpc (assumption)
    eta_perp = PhiN*wS/S2; eta_par = -PhiN*wS*(311.1**2/S2 - 1)/S2
    print(f"  Sgr, Hamiltonian reading, isothermal host truncated at {rt:.0f} kpc (assumed): |Phi_N| = {PhiN:.3e} km^2/s^2,"
          f" eta_perp/eps = {eta_perp:+.3f}, eta_par/eps = {eta_par:+.3f}, direct force <W> = {wS:.3f}")

print("\n=== K16: Rutherford/Born transfer cross-section, m = 70 MeV, Gt = G ===")
G = 6.67430e-11; hbar = 1.054571817e-34; eVkg = 1.78266192e-36; kpc = 3.0856775814913673e19
m = 70e6*eVkg; mu_r = m/2; kap = G*m**2
for v_kms in (10, 30, 100, 300):
    v = v_kms*1e3
    lnB = np.log(2*mu_r*v*kpc/hbar) - 0.5
    sT = 4*np.pi*(kap/(mu_r*v**2))**2*lnB          # m^2
    eta = kap/(hbar*v)
    print(f"  v={v_kms:4d} km/s: eta = {eta:.2e}, Born lnLambda(b=1 kpc) = {lnB:.2f}, sigma_T/m = {sT*1e4/(m*1e3):.3e} cm^2/g")
v = 30e3; lnB = np.log(2*mu_r*v*kpc/hbar) - 0.5; sT = 4*np.pi*(kap/(mu_r*v**2))**2*lnB*1e4/(m*1e3)
print(f"  G~/G for 30 cm^2/g at 30 km/s: {np.sqrt(30/sT):.3e};  fraction of sigma_T from theta>90 deg: {np.log(np.sqrt(2))/lnB:.4f}")
