"""Composite bodies: which velocities does the gate see?

If the gate acts pairwise on constituents a (body A) and b (body B), the A-B coupling is
  G [1 + eps <W(|V + w_a - w_b|/v*)>],  V = CM relative velocity, w = internal velocities.
For a Gaussian W = exp(-u^2) and Maxwellian internal velocities (1D dispersions s_A, s_B; s^2 = s_A^2 + s_B^2):
  <W>(V) = (1 + 2 s^2/v*^2)^(-3/2) exp(-V^2/(v*^2 + 2 s^2))           (exact Gaussian convolution, checked below)
i.e. a Gaussian gate in V of width v*_eff = sqrt(v*^2 + 2 s^2) and amplitude eps_eff = eps (1+2s^2/v*^2)^(-3/2).
The amplitude depends on the constituents' thermal speeds, sqrt(kT/m): composition and temperature dependent coupling,
which equivalence-principle tests bound.  Assumptions are printed with each number.
"""
import numpy as np
import mpmath as mp

k_B = 1.380649e-23
amu = 1.66053907e-27

# ------------------------------------------------------------ check the convolution formula numerically
def W_avg_numeric(V, s, vstar, shape='gauss'):
    """<W(|V + w|/v*)> over an isotropic Maxwellian w with 1D dispersion s (radial + angle quadrature)."""
    def Wf(x):
        return mp.e**(-x * x) if shape == 'gauss' else 1 / (1 + x * x)
    def radial(w):
        if V == 0:
            ang = Wf(w / vstar)
        else:
            ang = mp.quad(lambda mu_: Wf(mp.sqrt(V * V + w * w + 2 * V * w * mu_) / vstar), [-1, 1]) / 2
        return 4 * mp.pi * w * w * (2 * mp.pi * s * s)**(-1.5) * mp.e**(-w * w / (2 * s * s)) * ang
    return mp.quad(radial, [0, s, 3 * s, 10 * s])


def W_avg_gauss(V, s, vstar):
    return (1 + 2 * s * s / vstar**2)**(-1.5) * np.exp(-V * V / (vstar**2 + 2 * s * s))


mp.mp.dps = 20
print("Check of the Gaussian convolution formula (km/s units):")
for (V, s, vs) in [(0.0, 1.0, 0.1), (0.5, 1.0, 1.0), (7.5, 1.0, 10.0), (30.0, 200.0, 120.0)]:
    num = W_avg_numeric(V, s, vs)
    print(f"  V={V:6.2f} s={s:6.1f} v*={vs:6.1f}: quadrature {mp.nstr(num, 10)}  formula {W_avg_gauss(V, s, vs):.10g}")
print("Lorentzian, s >> v*: <W> -> (v*/s)^2 (derived);  quadrature at s/v* = 100:",
      mp.nstr(W_avg_numeric(0.0, 100.0, 1.0, 'lorentz'), 8), " vs (v*/s)^2 = 1e-4 (next order ~ sqrt(pi/2) (v*/s)^3)")


def sig_th(A, T):
    """1D thermal velocity dispersion (km/s), classical."""
    return np.sqrt(k_B * T / (A * amu)) / 1e3


T_LAB = 300.0
mat = {'Be': 9.012, 'Al': 26.98, 'Ti': 47.87, 'Pt': 195.08}
print()
print("Classical 1D thermal dispersions at 300 K (km/s): " +
      ", ".join(f"{m} {sig_th(A, T_LAB):.3f}" for m, A in mat.items()))
print("  (Be has Debye temperature well above 300 K, so its true kinetic spread is larger than classical; not modeled.)")

# ------------------------------------------------------------ EP tests
EOTWASH = (0.3e-13, 1.8e-13)                     # eta(Be,Ti) Schlamminger et al. 2008
MICRO = (-1.5e-15, np.hypot(2.3e-15, 1.5e-15))   # eta(Ti,Pt) Touboul et al. 2022, stat (+) syst in quadrature
two = lambda x, s: max(abs(x - 2 * s), abs(x + 2 * s))
V_MICRO = 7.5     # km/s, low-Earth-orbit speed relative to the Earth (assumed ~ sqrt(GM/7080 km))
VSTARS = [0.1, 1.0, 10.0, 120.0, 1000.0]

print()
print("Atom-level gate (Gaussian W, Maxwellian thermal velocities). eta(A,B) = eps [<W>_A - <W>_B].")
print("Source = Earth with effective 1D dispersion s_E of its constituents relative to the lab (thermal + rotation),")
print("bracketed 0.5-2 km/s.  Eot-Wash: lab bodies at rest on Earth (V ~ 0); MICROSCOPE: V = 7.5 km/s.")
print(f"{'v*':>7} {'s_E':>5} {'<W>_Be':>10} {'<W>_Ti':>10} {'EW |eps|<':>10} {'<W>_Ti(orb)':>12} {'<W>_Pt(orb)':>12} {'MICRO |eps|<':>12}")
for vs in VSTARS:
    for sE in [0.5, 1.0, 2.0]:
        wBe = W_avg_gauss(0.0, np.hypot(sig_th(mat['Be'], T_LAB), sE), vs)
        wTi = W_avg_gauss(0.0, np.hypot(sig_th(mat['Ti'], T_LAB), sE), vs)
        ew = two(*EOTWASH) / abs(wBe - wTi)
        oTi = W_avg_gauss(V_MICRO, np.hypot(sig_th(mat['Ti'], T_LAB), sE), vs)
        oPt = W_avg_gauss(V_MICRO, np.hypot(sig_th(mat['Pt'], T_LAB), sE), vs)
        mic = two(*MICRO) / abs(oTi - oPt) if abs(oTi - oPt) > 0 else np.inf
        print(f"{vs:7.1f} {sE:5.1f} {wBe:10.3e} {wTi:10.3e} {ew:10.2e} {oTi:12.3e} {oPt:12.3e} {mic:12.2e}")

# ------------------------------------------------------------ orbital tests with atom-level smearing (Gaussian)
from bounds import dom, dvarpi, planets, vc, RAD2MAS, RAD2MUAS, v_moon, E_MOON, P_MOON, LLR_PERIGEE_2SIG_MUAS


def two_sided(x, s):
    return max(abs(x - 2 * s), abs(x + 2 * s))


print()
print("Orbital tests when the gate acts on constituents: effective Gaussian gate v*_eff = sqrt(v*^2+2s^2),")
print("amplitude (1+2s^2/v*^2)^(-3/2).  Sun: ion thermal dispersion s_sun (assumed 100-300 km/s, interior")
print("temperatures ~1e6-1e7 K); Earth-Moon: s = 1.1 km/s (assumed).")
for vs in VSTARS:
    row = []
    for ssun in [100.0, 200.0, 300.0]:
        amp = (1 + 2 * ssun**2 / vs**2)**(-1.5)
        veff = np.sqrt(vs**2 + 2 * ssun**2)
        a, P, e, m = planets['Mars']
        rate = amp * dom(vc['Mars'] / veff, e, 'gauss') * 36525 / P * RAD2MAS
        row.append(two_sided(*dvarpi['Mars']) / abs(rate))
    sEM = 1.1
    amp = (1 + 2 * sEM**2 / vs**2)**(-1.5)
    veff = np.sqrt(vs**2 + 2 * sEM**2)
    rate_m = amp * dom(v_moon / veff, E_MOON, 'gauss') * 365.25 / P_MOON * RAD2MUAS
    llr = LLR_PERIGEE_2SIG_MUAS / abs(rate_m)
    print(f"  v* = {vs:7.1f}: Mars-precession bound |eps| < {row[0]:.2e} / {row[1]:.2e} / {row[2]:.2e} (s_sun 100/200/300);"
          f" LLR |eps| < {llr:.2e} (v*_eff = {veff:.2f} km/s)")

# ------------------------------------------------------------ nucleon-level gate: Fermi motion
print()
m_N_MeV = 938.9
for kF in [200.0, 250.0, 270.0]:
    vF = kF / np.sqrt(kF**2 + m_N_MeV**2) * 299792.458
    supp = {vs: 3 * np.sqrt(np.pi) / 4 * (vs / vF)**3 for vs in VSTARS}
    print(f"Nucleon-level gate, Fermi gas k_F = {kF:.0f} MeV/c (assumed), v_F = {vF:.0f} km/s: "
          f"<W> ~ (3 sqrt(pi)/4)(v*/v_F)^3 = " + ", ".join(f"{supp[v]:.1e} @ {v} km/s" for v in VSTARS))
print("  (the gate width seen in CM velocity becomes ~v_F ~ 0.2-0.3 c: no orbital velocity dependence survives;"
      " only a composition-dependent rescaling of G)")

# ------------------------------------------------------------ spinning rotor (body-level and atom-level), parametric
print()
print("Spinning-rotor weighing, parametric (rotor rim speed v_rim is an assumption; published runs reached 2.2e4 rpm).")
print("Body-level gate: lab mass moves at V_lab = 0.465 cos(lat) km/s relative to Earth's CM; weight ~ 1 + eps K.")
print("Rotor adds horizontal velocities; uniform disk: <v^2> = v_rim^2/2.  Second-order average of K over the rotor:")


def K_g(u):
    return (1 + 2 * u * u) * np.exp(-u * u)


def rotor_dK(vs, Vlab, vrim, n=2000):
    # average K(|V + v|/v*) over a uniform disk spinning in the horizontal plane, V horizontal
    rho = np.sqrt(np.linspace(0, 1, n, endpoint=False) + 0.5 / n)  # area-uniform radii
    ph = np.linspace(0, 2 * np.pi, 360, endpoint=False)
    R, PH = np.meshgrid(rho, ph)
    vx = Vlab - vrim * R * np.sin(PH)
    vy = vrim * R * np.cos(PH)
    return np.mean(K_g(np.hypot(vx, vy) / vs)) - K_g(Vlab / vs)


for vrim in [0.03, 0.06]:
    for vs in [0.1, 0.3, 1.0]:
        for lat in [35.7, 48.8]:
            V = 0.465 * np.cos(np.radians(lat))
            dK = rotor_dK(vs, V, vrim)
            print(f"  v_rim={vrim*1e3:4.0f} m/s v*={vs:4.1f} km/s lat={lat:4.1f}: Delta K = {dK:+.2e} ->"
                  f" |eps| < {1e-6/abs(dK):.1e} per 1e-6 weighing sensitivity")
