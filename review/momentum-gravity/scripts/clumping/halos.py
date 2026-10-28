"""Environment numbers for the long-range velocity-gated attraction.
Inputs: Debt 3a environments (dwarf core rho = 1 GeV/cm^3, sigma = 30 km/s; MW local rho = 0.4,
sigma = 155); cluster rho = 0.03 GeV/cm^3, sigma = 1000 km/s (3b's cluster row); v* = 120 km/s.
Local (WKB, Jeans-swindle) criterion: unstable at k iff Lambda_0(gt, r) > (k/k_J)^2 = Q.
Halo margins Q: isothermal core k_J r_c = 3 exactly (r_c = 3 sigma/sqrt(4 pi G rho0), King radius):
   wavelength 2 r_c -> Q = (pi/3)^2, wavelength r_c -> Q = (2pi/3)^2.
 singular isothermal sphere rho = sigma^2/(2 pi G r^2): k_J r = sqrt2:
   wavelength 2r -> Q = pi^2/2, wavelength r -> Q = 2 pi^2.
Two versions of the threshold:
  (a) no re-virialization:  Lambda_0(gt) = Q
  (b) re-virialized: the halo's own equilibrium absorbs the density-mode strength 1 + gt <W>,
      <W> = <p0^1/2|W|p0^1/2> (pair-averaged gate), so require Lambda_0(gt) = Q (1 + gt <W>)
"""
import sys, math
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from static_threshold import top_eigs, Lam_g_closed, q_closed, K_matrix, p0

G = 6.67430e-11            # m^3 kg^-1 s^-2
GeV_kg = 1.78266192e-27    # kg per GeV/c^2
cm3 = 1e-6                 # m^3
kpc = 3.0856776e19         # m
Myr = 3.15576e13           # s
hbarc_eVm = 1.973269804e-7 # eV m

def pair_avg_W(r, gate='gauss'):
    v, w, M = K_matrix(r, 1.0, 0, gate=gate, grav=False)
    d = np.sqrt(4*np.pi*w)*v*np.sqrt(p0(v))
    return float(d @ M @ d)

def crit(r, Q, gate='gauss', revir=False):
    Wbar = pair_avg_W(r, gate) if revir else 0.0
    f = lambda gt: top_eigs(r, gt, 0, gate=gate, nev=1)[0][0] - Q*(1 + gt*Wbar)
    lo, hi = 0.0, 1.0
    while f(hi) < 0:
        hi *= 2
        if hi > 1e8: return np.inf
    for _ in range(50):
        mid = 0.5*(lo + hi)
        if f(mid) < 0: lo = mid
        else: hi = mid
    return 0.5*(lo + hi)

envs = [("dwarf core", 1.0, 30.0), ("MW local", 0.4, 155.0), ("cluster", 0.03, 1000.0)]
vstar = 120.0

if __name__ == '__main__':
    print("=== 1. Timescales and lengths (local) ===")
    for name, rho_gev, sig in envs:
        rho = rho_gev*GeV_kg/cm3
        s = sig*1e3
        tff = 1/math.sqrt(4*math.pi*G*rho)
        lamJ = 2*math.pi*s*tff
        rc = 3*s*tff
        r = sig/vstar
        print(f"{name:10s}: rho={rho:.3e} kg/m^3, r=sigma/v*={r:.4f}, t_ff=1/sqrt(4piG rho)={tff/Myr:.2f} Myr, "
              f"lambda_J={lamJ/kpc:.3f} kpc, isothermal r_c=3 sigma t_ff={rc/kpc:.3f} kpc, t_cross=r_c/sigma={rc/s/Myr:.1f} Myr")
    # MW solar orbit (dagger values from memory): R0 = 8.2 kpc, v_c = 230 km/s
    R0, vc = 8.2*kpc, 230e3
    print(f"MW solar orbital period 2 pi R0/v_c (R0=8.2 kpc, v_c=230 km/s, dagger) = {2*math.pi*R0/vc/Myr:.0f} Myr")
    rhoMW = 0.4*GeV_kg/cm3
    lamJ_MW = 2*math.pi*155e3/math.sqrt(4*math.pi*G*rhoMW)
    print(f"MW local: (lambda_J/R0)^2 = {(lamJ_MW/R0)**2:.2f} (margin for a mode of wavelength R0)")
    print("Margins: core Q=(pi/3)^2=%.4f, (2pi/3)^2=%.4f; SIS Q=pi^2/2=%.4f, 2pi^2=%.4f" % ((math.pi/3)**2, (2*math.pi/3)**2, math.pi**2/2, 2*math.pi**2))

    print("\n=== 2. Gate factors at each environment ===")
    for name, rho_gev, sig in envs:
        r = sig/vstar
        Lg = Lam_g_closed(r); q = q_closed(r)
        Wg = pair_avg_W(r, 'gauss'); Wr = pair_avg_W(r, 'rat2')
        Lr = top_eigs(r, 1.0, 0, gate='rat2', grav=False, nev=1)[0][0]
        print(f"{name:10s} r={r:.4f}: Gaussian Lam_g={Lg:.5e}, q={q:.5f}, <W>={Wg:.5e} (closed (1+2r^2)^-1.5={(1+2*r*r)**-1.5:.5e}), "
              f"Lam_g/<W>={Lg/Wg:.4f}, l=1 top Lam_g q={Lg*q:.5e};  rat2 Lam={Lr:.5e}, <W>={Wr:.5e}, ratio={Lr/Wr:.4f}")
    for r in [0.5, 1, 2, 4, 8, 16, 32, 64]:
        Lg = Lam_g_closed(r)
        print(f"   r={r:5.1f}: Gaussian Lam_g/<W> = {Lg/(1+2*r*r)**-1.5:.4f}   (r->inf limit 2^1.5 = {2**1.5:.4f})")

    print("\n=== 3. Critical Gt/G (Gaussian and rat2 gates) ===")
    Qs = {"dwarf core": [(math.pi/3)**2, (2*math.pi/3)**2],
          "MW local": [math.pi**2/2, 2*math.pi**2, (lamJ_MW/R0)**2],
          "cluster": [(math.pi/3)**2, (2*math.pi/3)**2]}
    for name, rho_gev, sig in envs:
        r = sig/vstar
        for Q in Qs[name]:
            out = []
            for gate in ['gauss', 'rat2']:
                a = crit(r, Q, gate, revir=False)
                b = crit(r, Q, gate, revir=True)
                out.append(f"{gate}: no-revir {a:.4g}, revir {b:.4g}")
            print(f"{name:10s} Q={Q:7.4f}: " + " | ".join(out))

    print("\n=== 4. Debt 3a contact-range numbers with the linearized narrow-gate criterion ===")
    cm = 5.0677307e13; g_ = 5.6095886e23; c = 2.99792458e5
    m = 0.070; S = 30*cm**2/g_
    gc = math.sqrt(math.pi*S/m)
    print(f"g = {gc:.4g} GeV^-2 (3a's benchmark coupling)")
    for name, rho_gev, sig_kms in envs:
        rho = rho_gev/cm**3; s = sig_kms/c; vs = vstar/c; n = rho/m; r = sig_kms/vstar
        # 3a's own forms
        if s < vs: r3a = gc*n/(m*s*s)
        else: r3a = gc*n*(vs/s)**3/(2*math.pi)**1.5/(m*vs*vs)
        rex = gc*n*Lam_g_closed(r)/(m*s*s)
        print(f"{name:10s}: 3a-form ratio = {r3a:.3g};  linearized ratio g n Lam_g(r)/(m sigma^2) = {rex:.3g}")

    print("\n=== 5. Range of X versus halo scales ===")
    lamX = 37.7e-6
    print(f"lambda_X < 37.7 um (diameter note, u=1) -> lambda_X/1 kpc < {lamX/kpc:.3g}; carrier mass for range 1 kpc: hbar c/1kpc = {hbarc_eVm/kpc:.3g} eV")
    print(f"M_X c^2 > hbar c/37.7um = {hbarc_eVm/lamX*1e3:.3g} meV; ratio to 1-kpc carrier mass: {hbarc_eVm/lamX/(hbarc_eVm/kpc):.3g}")
