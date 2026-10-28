"""Remaining checks: eigenvector structure (C8, C9), near-threshold slope (C11/C2),
3a ratios and benchmark shortfalls (C6), local scales (C10), classicality, Rutherford and
relaxation numbers (C13-C15), X-range conversions (C16). Constants from CODATA/PDG values
typed from memory (dagger) -- they are standard and printed so they can be checked."""
import numpy as np, sys
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-clumping-derivation')
import thresholds_radial as TR
from dynamic_eig2 import unstable_mapped
from dynamic_eig import fmt

# ---------- C8/C9: top static eigenvector structure (own radial Nystrom) ----------
V, sq = TR.V, TR.sq
def topvec(gate, r, gt):
    K = gt * TR.mats(gate, r) + np.outer(sq, sq)
    w, U = np.linalg.eigh(K)
    psi = U[:, -1]
    a = sq / np.linalg.norm(sq)
    ov = abs(psi @ a)
    # delta f(v) on radial nodes ~ p0^(1/2) psi / (node measure^(1/2)); weights: sq^2 = 4 pi v^2 w p0
    # with psi_i = sqrt(measure_i p0_i) * dPhi_i, delta f_i = p0_i dPhi_i ; moments with measure 4 pi v^2 w
    df_meas = sq * psi              # = measure_i * p0_i * dPhi_i  (signed)
    m0 = df_meas.sum(); m2 = (V**2 * df_meas).sum()
    return w[-1], w[-2], ov, np.sqrt(m2 / m0)
print("C8/C9 top static mode: (Lambda_0, 2nd l=0 eigenvalue, overlap with density mode, rms speed of delta f [sigma])")
for r, gt in [(1.2917, 1.0), (0.25, 1.0), (1.2917, 100.0), (4.0, 1e4), (8.333, 1e4)]:
    L0, L1, ov, rms = topvec('gauss', r, gt)
    print(f"  r={r} gt={gt:g}: {L0:.6f}, {L1:.6f}, {ov:.5f}, {rms:.4f}")
print("  Maxwellian density mode rms speed sqrt(3) =", round(np.sqrt(3), 4))

# ---------- C11: near-threshold slope, one case, resolved small growth rate ----------
r, gt = 1.2917, 10.0
L0 = TR.lam0('gauss', r, gt)
for frac in [0.95, 0.98]:
    k2 = frac * L0
    ev, ns, dt = unstable_mapped(np.sqrt(k2), gt, r, v0=0.0, alpha=0.1, ds=0.05, Lz=5.5, npp=10, thr=1e-3)
    G = ev[0].imag if len(ev) else 0.0
    print(f"C11 near threshold r={r} gt={gt}: kap^2={frac}*Lambda_0, Gamma={G:.5f}, Gamma/(1-frac)={G/(1-frac):.4f}  [{fmt(ev)}]")

# ---------- C6: 3a's narrow form vs the linearized threshold ----------
def Lg(r):
    a = 0.25; b = r*r/2; c = np.sqrt(a*a+2*a*b); A = a+b+c
    return np.sqrt(2*a/A)**3
print("C6 required-g ratio exact/3a-narrow = (2pi)^-1.5/(r Lam_g):")
for r in [0.25, 1.2917, 8.333, 32.0]:
    print(f"  r={r}: {(2*np.pi)**-1.5/(r*Lg(r)):.4f};  exact/3a-broad = 1/Lam_g = {1/Lg(r):.4f};  (2pi)^-1.5 r^2 = {(2*np.pi)**-1.5*r*r:.4f}")
hbarc_cm = 1.973269804e-14       # GeV cm
c_kms = 299792.458
m = 0.070                         # GeV
cm2g = 30.0; GeV_g = 1.78266192e-24
sig0 = cm2g * m * GeV_g / hbarc_cm**2   # GeV^-2
g = np.sqrt(np.pi * sig0) / m
print(f"C6 benchmark coupling g = sqrt(pi sigma0)/m = {g:.1f} GeV^-2 (3a's g = sqrt(pi sigma0/m^2))")
vstar = 120.0
for name, rho, sig in [('dwarf', 1.0, 30.0), ('MW', 0.4, 155.0), ('cluster', 0.03, 1000.0)]:
    n = rho / m * hbarc_cm**3        # GeV^3
    r = sig / vstar
    kin = m * (sig / c_kms)**2
    lin = g * n * Lg(r) / kin
    if sig < vstar:
        a3 = g * n / kin
    else:
        a3 = g * n * (vstar/sig)**3 * (2*np.pi)**-1.5 / (m * (vstar/c_kms)**2)
    print(f"  {name}: g n = {g*n:.4g} GeV, m sigma^2 = {kin:.4g} GeV, 3a-form ratio = {a3:.3g}, linearized g n Lam_g/(m sigma^2) = {lin:.3g}")

# ---------- C10/C11: local scales ----------
G = 6.67430e-11; GeVkg = 1.78266192e-27; kpc = 3.0856776e19; Myr = 3.15576e13; Msun = 1.98841e30
for name, rho, sig in [('dwarf', 1.0, 30.0), ('MW', 0.4, 155.0), ('cluster', 0.03, 1000.0)]:
    rho_si = rho * GeVkg / 1e-6
    tff = 1/np.sqrt(4*np.pi*G*rho_si)
    lamJ = 2*np.pi*sig*1e3*tff
    rc = 3*sig*1e3*tff
    print(f"C10 {name}: t_ff={tff/Myr:.2f} Myr, lambda_J={lamJ/kpc:.3f} kpc, r_c=3 sigma t_ff={rc/kpc:.3f} kpc, t_cross=r_c/sigma={rc/(sig*1e3)/Myr:.1f} Myr")
R0 = 8.2*kpc; vc = 230e3
tff_mw = 1/np.sqrt(4*np.pi*G*0.4*GeVkg/1e-6)
print(f"  MW: (lambda_J/R0)^2 = {(2*np.pi*155e3*tff_mw/R0)**2:.3f}; t_orb = 2 pi R0/v_c = {2*np.pi*R0/vc/Myr:.1f} Myr")
for Gam in [0.7783, 1.2222, 1.3448, 1.8540, 2.1679]:
    print(f"  MW growth {Gam}/t_ff -> e-fold {tff_mw/Gam/Myr:.1f} Myr = {tff_mw/Gam/(2*np.pi*R0/vc):.3f} t_orb")
tff_cl = 1/np.sqrt(4*np.pi*G*0.03*GeVkg/1e-6)
for Gam in [0.06531, 0.06496, 0.0272]:
    print(f"  cluster growth {Gam}/t_ff -> e-fold {tff_cl/Gam/Myr:.0f} Myr = {tff_cl/Gam/(3*tff_cl):.2f} t_cross")

# ---------- C13-C15 ----------
rho_si = 1.0 * GeVkg / 1e-6
tff = 1/np.sqrt(4*np.pi*G*rho_si); rc = 3*30e3*tff
M = rho_si * 4/3*np.pi*rc**3
mkg = m * GeVkg
N = M / mkg
EGr = G*M*mkg/rc / (GeVkg * (299792458.0)**2)   # GeV
print(f"C13 dwarf core: r_c={rc/kpc:.3f} kpc, M={M/Msun:.4g} Msun, N={N:.4g}, lnN={np.log(N):.2f}")
print(f"  G M m/r_c = {EGr:.4g} GeV; contact g n = {g*(1.0/m*hbarc_cm**3):.4g} GeV; ratio {EGr/(g*(1.0/m*hbarc_cm**3)):.4g}; m sigma^2 = {m*(30/c_kms)**2:.4g} GeV")
print(f"  ratio (G M m/r_c)/(m sigma^2) = {EGr/(m*(30/c_kms)**2):.3f} (independent of m: = G M/(r_c sigma^2))")
for nm, rho, sig in [('dwarf', 1.0, 30.0), ('MW', 0.4, 155.0)]:
    Nocc = rho*hbarc_cm**3 / (m**4 * (sig/c_kms)**3)
    print(f"  N_occ {nm} = rho/(m^4 sigma^3) = {Nocc:.4g}")
v = 30e3
b90 = 2*G*mkg/v**2
sT = 4*np.pi*b90**2*np.log(N)
print(f"C14 b90 = {b90:.4g} m, sigma_T/m = {sT/mkg*10:.4g} cm^2/g, G~/G for 30 cm^2/g = {np.sqrt(30/(sT/mkg*10)):.4g}")
print(f"C15 N/(8 lnN) = {N/(8*np.log(N)):.4g}")
# ---------- C16 ----------
hbarc_eVm = 1.973269804e-7
print(f"C16 37.7 um / 1 kpc = {37.7e-6/kpc:.4g}; hbar c/1 kpc = {hbarc_eVm/kpc:.4g} eV; hbar c/37.7 um = {hbarc_eVm/37.7e-6*1e3:.4g} meV; ratio = {(hbarc_eVm/37.7e-6)/(hbarc_eVm/kpc):.4g}")
