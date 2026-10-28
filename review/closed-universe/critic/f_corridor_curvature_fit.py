"""Critic, tension (f): is w0waCDM+Omega_K a valid proxy for the program's thawing cosine field?

A crude background-level likelihood, built from the DESI DR2 paper itself (arXiv:2503.14738 source TeX,
downloaded by the observations-applicability verifier; numbers typed from Table 'tab:alphas' and eqs.
CMB_compression_mean/cov, rdformula):
  - DESI DR2 BAO: BGS D_V/r_d; LRG1, LRG2, LRG3+ELG1, ELG2, QSO, Lya: (D_M/r_d, D_H/r_d) with r_M,H.
  - CMB compressed prior on (theta_*, omega_b, omega_bc) (Lemos-Lewis compression), as DESI uses it.
  - r_d from DESI's fitting formula; theta_* = r_*/D_M(z_*) with r_* integrated and z_* from Hu-Sugiyama,
    calibrated so that DESI's CMB-only LCDM (Omega_m = 0.3169, H0 = 67.14) gives 100 theta_* = 1.04110.
No supernovae. Models, each profiled over (omega_b, omega_bc, h, DE parameters) at fixed Omega_K:
  LCDM+K; w0wa+K (CPL free); corridor+K: CPL on the program's corridor w_a = -s(1+w0), s = 1.5 (record)
  and s = 2.0 (upper end of the dynamics analysis's least-squares slope), with w0 in [-1, -0.3] (thawing,
  never phantom: w0 >= -1).
Calibration check: flat w0wa with DESI+(theta_*, omega_b, omega_bc)_CMB is published as
  w0 = -0.43 +- 0.22, wa = -1.72 +- 0.64; flat LCDM DESI+CMB Omega_m = 0.3027, H0 = 68.17.
This is a reduction: background distances only, Gaussian likelihoods, no SNe, no CMB lensing/ISW.
"""
import numpy as np

c_kms = 299792.458
omega_gamma = 2.4728e-5            # T0 = 2.7255 K
Neff = 3.044
omega_r = omega_gamma*(1 + 0.22711*Neff)
omega_nu_m = 0.06/93.14            # one massive neutrino, 0.06 eV, counted as matter at late times

# DESI DR2 BAO (Table tab:alphas)
bao_2d = [  # z, DM/rd, sig, DH/rd, sig, r
    (0.510, 13.588, 0.167, 21.863, 0.425, -0.459),
    (0.706, 17.351, 0.177, 19.455, 0.330, -0.404),
    (0.934, 21.576, 0.152, 17.641, 0.193, -0.416),
    (1.321, 27.601, 0.318, 14.176, 0.221, -0.434),
    (1.484, 30.512, 0.760, 12.817, 0.516, -0.500),
    (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]
bao_dv = (0.295, 7.942, 0.075)
mu_cmb = np.array([1.04110e-2, 0.02223, 0.14208])
C_cmb = 1e-9*np.array([[0.006621, 0.12444, -1.1929], [0.12444, 21.344, -94.001], [-1.1929, -94.001, 1488.4]])
Cinv_cmb = np.linalg.inv(C_cmb)

lnz = np.linspace(0, np.log(1 + 1200.0), 6000)
zg = np.expm1(lnz)

def E2(z, h, om_m, Ok, de):
    a = 1/(1 + z)
    Om = om_m/h**2; Or = omega_r/h**2
    if de is None:
        f = 1.0
    else:
        w0, wa = de
        f = a**(-3*(1 + w0 + wa))*np.exp(-3*wa*(1 - a))
    Ode = 1 - Om - Or - Ok
    return Or*(1+z)**4 + Om*(1+z)**3 + Ok*(1+z)**2 + Ode*f

def zstar(ob, om):
    g1 = 0.0783*ob**-0.238/(1 + 39.5*ob**0.763)
    g2 = 0.560/(1 + 21.1*ob**1.81)
    return 1048*(1 + 0.00124*ob**-0.738)*(1 + g1*om**g2)

def rstar(ob, om, zs):
    lz = np.linspace(np.log(1 + zs), np.log(1 + 1e8), 4000)
    z = np.expm1(lz)
    R = 3*ob/(4*omega_gamma)/(1 + z)
    cs = c_kms/np.sqrt(3*(1 + R))
    H = 100*np.sqrt(omega_r*(1+z)**4 + om*(1+z)**3)
    integrand = cs/H*(1 + z)          # dz = (1+z) d ln(1+z)
    return np.trapezoid(integrand, lz)

def rd(ob, obc):
    return 147.05*(ob/0.02236)**-0.13*(obc/0.1432)**-0.23*(Neff/3.04)**-0.1

def comoving(h, om_m, Ok, de, zq):
    Ez = np.sqrt(E2(zg, h, om_m, Ok, de))
    integ = (1 + zg)/Ez
    chi = np.concatenate([[0], np.cumsum(0.5*(integ[1:] + integ[:-1])*np.diff(lnz))])
    chiq = np.interp(np.log1p(zq), lnz, chi)
    DH0 = c_kms/(100*h)
    if Ok > 0:
        DM = DH0/np.sqrt(Ok)*np.sinh(np.sqrt(Ok)*chiq)
    elif Ok < 0:
        DM = DH0/np.sqrt(-Ok)*np.sin(np.sqrt(-Ok)*chiq)
    else:
        DM = DH0*chiq
    return DM, DH0/np.sqrt(E2(zq, h, om_m, Ok, de))

CAL = 1.0
def theta_star(ob, obc, h, Ok, de):
    om = obc + omega_nu_m
    zs = zstar(ob, om)
    DM, _ = comoving(h, om, Ok, de, np.array([zs]))
    return CAL*rstar(ob, om, zs)/DM[0]

# calibration on DESI's CMB-only LCDM point
h_ref = 0.6714; om_ref = 0.3169*h_ref**2
CAL = 1.04110e-2/theta_star(0.02223, om_ref - omega_nu_m, h_ref, 0.0, None)

def chi2(params, Ok, model):
    ob, obc, h = params[:3]
    if model == 'LCDM':
        de = None
    elif model == 'w0wa':
        de = (params[3], params[4])
    else:
        s = {'corr1.5': 1.5, 'corr2.0': 2.0}[model]
        w0 = params[3]
        if w0 < -1 or w0 > -0.3:
            return 1e9
        de = (w0, -s*(1 + w0))
    if not (0.015 < ob < 0.03 and 0.10 < obc < 0.18 and 0.5 < h < 0.9):
        return 1e9
    om = obc + omega_nu_m
    try:
        th = theta_star(ob, obc, h, Ok, de)
    except FloatingPointError:
        return 1e9
    d = np.array([th, ob, obc]) - mu_cmb
    x2 = d @ Cinv_cmb @ d
    r_d = rd(ob, obc)
    zq = np.array([b[0] for b in bao_2d] + [bao_dv[0]])
    DM, DH = comoving(h, om, Ok, de, zq)
    if not np.all(np.isfinite(DM)) or np.any(DM <= 0):
        return 1e9
    for i, (z, dm, sdm, dh, sdh, r) in enumerate(bao_2d):
        v = np.array([DM[i]/r_d - dm, DH[i]/r_d - dh])
        Cv = np.array([[sdm**2, r*sdm*sdh], [r*sdm*sdh, sdh**2]])
        x2 += v @ np.linalg.solve(Cv, v)
    z = bao_dv[0]
    DV = (z*DM[-1]**2*DH[-1])**(1/3)
    x2 += ((DV/r_d - bao_dv[1])/bao_dv[2])**2
    return x2

def nelder_mead(f, x0, step, iters=1500, tol=1e-8):
    n = len(x0)
    pts = [np.array(x0, float)]
    for i in range(n):
        x = np.array(x0, float); x[i] += step[i]; pts.append(x)
    vals = [f(p) for p in pts]
    for _ in range(iters):
        order = np.argsort(vals); pts = [pts[i] for i in order]; vals = [vals[i] for i in order]
        if abs(vals[-1] - vals[0]) < tol:
            break
        cen = np.mean(pts[:-1], axis=0)
        xr = cen + (cen - pts[-1]); fr = f(xr)
        if fr < vals[0]:
            xe = cen + 2*(cen - pts[-1]); fe = f(xe)
            if fe < fr: pts[-1], vals[-1] = xe, fe
            else: pts[-1], vals[-1] = xr, fr
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = cen + 0.5*(pts[-1] - cen); fc = f(xc)
            if fc < vals[-1]:
                pts[-1], vals[-1] = xc, fc
            else:
                for i in range(1, n+1):
                    pts[i] = pts[0] + 0.5*(pts[i] - pts[0]); vals[i] = f(pts[i])
    i = int(np.argmin(vals))
    return pts[i], vals[i]

def best(Ok, model, starts):
    out = None
    for x0 in starts:
        step = [0.0003, 0.002, 0.01] + ([0.05] if model.startswith('corr') else []) + ([0.1, 0.3] if model == 'w0wa' else [])
        x, v = nelder_mead(lambda p: chi2(p, Ok, model), x0, step)
        x, v = nelder_mead(lambda p: chi2(p, Ok, model), x, [s/5 for s in step])
        if out is None or v < out[1]:
            out = (x, v)
    return out

np.seterr(all='ignore')
print(f"theta_* calibration factor CAL = {CAL:.5f}")
base = [0.02223, 0.14208, 0.68]
starts = {'LCDM': [base], 'w0wa': [base + [-0.45, -1.6], base + [-0.8, -0.6], base + [-1.0, 0.0]],
          'corr1.5': [base + [-0.95], base + [-0.8]], 'corr2.0': [base + [-0.95], base + [-0.8]]}

print("\n=== calibration: flat fits ===")
for m in ['LCDM', 'w0wa']:
    x, v = best(0.0, m, starts[m])
    om = (x[1] + omega_nu_m)/x[2]**2
    print(f"  {m:5s} flat: chi2 = {v:.2f}, Omega_m = {om:.4f}, H0 = {100*x[2]:.2f}"
          + (f", w0 = {x[3]:.3f}, wa = {x[4]:.3f}  (published DESI+(theta,wb,wbc)_CMB: -0.43+-0.22, -1.72+-0.64)" if m == 'w0wa' else
             "  (published DESI+CMB LCDM: 0.3027, 68.17)"))

print("\n=== profiles in Omega_K ===")
grid = np.round(np.arange(-0.008, 0.0121, 0.001), 4)
results = {}
for m in ['LCDM', 'corr1.5', 'corr2.0', 'w0wa']:
    prof = []
    for Ok in grid:
        x, v = best(float(Ok), m, starts[m])
        prof.append((float(Ok), v, x))
    results[m] = prof
    vmin = min(p[1] for p in prof)
    ibest = int(np.argmin([p[1] for p in prof]))
    print(f"  {m}: absolute chi2 minimum on the grid = {vmin:.2f} at Omega_K = {prof[ibest][0]:+.4f}"
          f" (16 data points: 13 BAO + 3 CMB-prior)")
    for Ok, v, x in prof:
        extra = f" w0 = {x[3]:.3f}" if m.startswith('corr') else (f" w0 = {x[3]:.3f} wa = {x[4]:.3f}" if m == 'w0wa' else "")
        print(f"     Omega_K = {Ok:+.4f}: dchi2 = {v - vmin:7.3f}  H0 = {100*x[2]:.2f}{extra}")

print("\n=== Gaussian reading of each profile (parabola through dchi2 near the minimum) ===")
from math import erf, sqrt
def Phi(x): return 0.5*(1 + erf(x/sqrt(2)))
for m, prof in results.items():
    O = np.array([p[0] for p in prof]); V = np.array([p[1] for p in prof])
    sel = V - V.min() < 6
    A = np.polyfit(O[sel], V[sel], 2)
    mean = -A[1]/(2*A[0]); sig = 1/np.sqrt(A[0])
    pc = Phi((0 - mean)/sig)
    # closed-conditional 95% bound: P(-x < O < 0) = 0.95 P(O < 0)
    lo, hi = 0.0, 0.05
    for _ in range(80):
        mid = 0.5*(lo + hi)
        frac = (Phi((0 - mean)/sig) - Phi((-mid - mean)/sig))/pc
        if frac < 0.95: lo = mid
        else: hi = mid
    print(f"  {m:8s}: Omega_K = {mean:+.5f} +- {sig:.5f}; P(Omega_K < 0) = {pc:.4f}; "
          f"95% bound given closure |Omega_K| < {hi:.5f}; dchi2(closed |Ok| = 0.002) = "
          f"{np.interp(-0.002, O, V) - V.min():.2f}")
