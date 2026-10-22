"""Independent audit of flag 19 (classicality corollary's regime, notes/debt3a-stream-stability.md).

Units: natural units, GeV. Conversions are built from the exact SI defining constants
(h, c, e), not copied from the flag's script, so the anchor is independent of the paper.
Inputs are the ones 3a states: S = sigma0/m = 30 cm^2/g, m = 70 MeV, v* = 120 km/s,
dwarf (1 GeV/cm^3, 30 km/s), MW local (0.4 GeV/cm^3, 155 km/s).
"""
import math
import numpy as np

# --- exact SI defining constants (2019 SI) ---
h = 6.62607015e-34          # J s
c_SI = 299792458.0          # m/s
e = 1.602176634e-19         # C
hbar = h / (2 * math.pi)
GeV_J = 1e9 * e             # 1 GeV in J
hbarc_GeV_m = hbar * c_SI / GeV_J          # GeV * m
cm = 1e-2 / hbarc_GeV_m                    # 1 cm in GeV^-1
gram = 1e-3 * c_SI**2 / GeV_J              # 1 g in GeV
c_kms = c_SI / 1e3
print(f"[units] hbar*c = {hbarc_GeV_m*1e2:.10e} GeV cm; 1 cm = {cm:.6e} GeV^-1; 1 g = {gram:.6e} GeV")

S = 30 * cm**2 / gram       # sigma0/m in GeV^-3
m_b = 0.070
vstar = 120 / c_kms
g_b = math.sqrt(math.pi * S / m_b)          # g = sqrt(pi sigma0/m^2), sigma0 = S m
print(f"[A] g at benchmark = {g_b:.4g} GeV^-2")

def rho_nat(rho_gev_cm3):
    return rho_gev_cm3 / cm**3

def broad(m, rho, sig):           # Limit 1: g n / (m sigma^2)
    g = math.sqrt(math.pi * S / m)
    return g * (rho / m) / (m * sig**2)

def narrow(m, rho, sig, vs):      # Limit 2 as 3a writes it: g n_gate/(m v*^2)
    g = math.sqrt(math.pi * S / m)
    ngate = (rho / m) * (vs / sig)**3 / (2 * math.pi)**1.5
    return g * ngate / (m * vs**2)

def unified(m, rho, sig, vs):     # 3a's unified criterion, regime picked by min(sigma, v*)
    return broad(m, rho, sig) if sig <= vs else narrow(m, rho, sig, vs)

# --- B. 3a's table ---
for name, r, s in [("dwarf core", 1.0, 30.0), ("MW local", 0.4, 155.0)]:
    print(f"[B] {name}: unified criterion at benchmark = {unified(m_b, rho_nat(r), s/c_kms, vstar):.3g}"
          f"  (regime: {'broad' if s/c_kms <= vstar else 'narrow'}; broad form would give {broad(m_b, rho_nat(r), s/c_kms):.3g})")

# --- C. the corollary at MW conditions ---
rho, sig = rho_nat(0.4), 155 / c_kms
mc_broad = (math.sqrt(math.pi * S) * rho / sig**2) ** 0.4
mc_narrow = (math.sqrt(math.pi * S) * rho * vstar / (sig**3 * (2 * math.pi)**1.5)) ** 0.4
Nocc = lambda m: rho / (m**4 * sig**3)
print(f"[C] m_crit broad  = {mc_broad:.3g} GeV = {mc_broad*1e12:.3g} meV; N_occ = {Nocc(mc_broad):.3g}; criterion check = {broad(mc_broad, rho, sig):.6f}")
print(f"[C] m_crit narrow = {mc_narrow:.3g} GeV = {mc_narrow*1e12:.3g} meV; N_occ = {Nocc(mc_narrow):.3g}; criterion check = {narrow(mc_narrow, rho, sig, vstar):.6f}")
print(f"[C] narrow/broad criterion ratio at MW = {(vstar/sig)/(2*math.pi)**1.5:.4f}; m_crit ratio = {mc_narrow/mc_broad:.4f}")
print(f"[C] log10 distance of each m_crit from 1e-13 GeV: broad {math.log10(mc_broad/1e-13):+.2f} dex, narrow {math.log10(mc_narrow/1e-13):+.2f} dex")
print(f"[C] MW sits near the crossover: sigma/v* = {sig/vstar:.3f}; mu/(m sigma) = {vstar/(math.sqrt(2)*sig):.3f} (v*=sqrt2 mu/m) or {vstar/sig:.3f} (v*=mu/m)")

# --- D. ceiling property: unified criterion <= broad form at every dispersion (3a's own formulas) ---
sigs = np.linspace(5, 3000, 5000) / c_kms
ratios = np.array([unified(m_b, rho, s, vstar) / broad(m_b, rho, s) for s in sigs])
print(f"[D] max over sigma in [5, 3000] km/s of unified/broad = {ratios.max():.6f} (attained in the broad regime); "
      f"max in narrow regime = {ratios[sigs > vstar].max():.4f}")

# --- E. what the wave-island note 3b holds fixed: reproduce its R_X table (t_age = 10 Gyr, kappa = 1) ---
t_age = 10.0
rho_d, sig_d = 1.0, 30.0
rows = [("Classical dwarf core", 1, 30, 0.1, "1e-2"), ("Ultra-faint dwarf", 20, 3, 0.01, "40"),
        ("MW inner 1 kpc", 10, 120, 0.02, "1e-2"), ("MW solar circle", 0.4, 155, 0.2, "4e-5"),
        ("Cluster", 0.03, 1000, 1.0, "~0")]
for name, r, s, tdyn, stated in rows:
    base = (tdyn / t_age) * (r / rho_d)**2 * (sig_d / s)**2
    gated = base * (min(s, 120.0) / s)**4
    print(f"[E] {name:22s} R_X with v*=120 km/s gate: {gated:.2g}   without gate factor: {base:.2g}   (3b states {stated})")

# --- F. the alternative 'mu held fixed' reading ---
mu_b = m_b * vstar / math.sqrt(2)                 # #1 sec 5.1: mu = m v*/sqrt2 ~ 20 keV
vstar_at_mcrit = math.sqrt(2) * mu_b / mc_broad   # in units of c
print(f"[F] benchmark mu = {mu_b*1e6:.3g} keV; if mu were held fixed, v* at m_crit = {vstar_at_mcrit:.3g} c (gate broad everywhere)")

# --- G. exact static operator of 3a's linearized Vlasov eq. (my own check, not in the documents) ---
# At omega -> 0, (k.grad_p f0)/(omega - k.v) -> f0/(m sigma^2) for a Maxwellian, so the threshold is
# (g/(m sigma^2)) * lambda_max[ f0^1/2 G f0^1/2 ] = 1. Energy-Casimir: below this, the equilibrium is stable.
# Gate in velocity: G = exp(-|dv|^2/(2 v*^2)) (amplitude whose square gives sigma_T ~ exp(-v^2/v*^2)).
def lam_numeric_1d(sig1, ell, N=1200, L=10.0):
    v = np.linspace(-L * sig1, L * sig1, N); dv = v[1] - v[0]
    p = np.exp(-v**2 / (2 * sig1**2)) / math.sqrt(2 * math.pi * sig1**2)
    K = np.sqrt(p)[:, None] * np.exp(-(v[:, None] - v[None, :])**2 / (2 * ell**2)) * np.sqrt(p)[None, :] * dv
    return np.linalg.eigvalsh(K).max()
def lam_mehler_1d(sig1, ell):   # Gaussian-kernel/Gaussian-weight top eigenvalue, closed form
    a, b = 1 / (4 * sig1**2), 1 / (2 * ell**2)
    A = a + b + math.sqrt(a * a + 2 * a * b)
    return math.sqrt(2 * a / A)
for ratio in [0.1, 0.5, 120 / 155, 1.0, 3.0, 30.0]:
    ln, la = lam_numeric_1d(1.0, ratio), lam_mehler_1d(1.0, ratio)
    print(f"[G] v*/sigma = {ratio:6.3f}: lambda_max/n (3D) numeric = {ln**3:.4f}, closed form = {la**3:.4f}, "
          f"3a narrow form/broad = {(ratio)/(2*math.pi)**1.5:.4f}")
lam3 = lam_mehler_1d(155.0, 120.0)**3
mc_static = mc_broad * lam3**0.4
print(f"[G] MW: exact static criterion = {lam3:.4f} x broad; m_crit(static) = {mc_static:.3g} GeV; N_occ = {Nocc(mc_static):.3g}")
