# Independent checks of round-2 ordinary-tests claims O17, O18, O19, O21 (constituent-level gating).
# Methods differ from the agent's composite.py / nucleon_level.py:
#  - Gaussian convolution checked by Monte Carlo with error bars from independent runs (agent: quadrature)
#  - Lorentzian s >> v* limit by 1D radial quadrature (mpmath)
#  - Fermi-sphere pair average by the exact overlap-volume formula (agent: Monte Carlo)
#  - MICROSCOPE bound recomputed both with eta = eps (<W>_A - <W>_B) (agent's choice) and with the
#    circular-orbit coupling K_X = <W>_X - V d<W>_X/dV, which is what a co-orbiting body feels
#    (the K = W - uW' result of O5 applied to the smeared gate)
import numpy as np
import mpmath as mp

rng = np.random.default_rng(20261027)
print("=== O17: Gaussian gate averaged over 3D Gaussian internal velocities (1D dispersion s) ===")
def formula(V, s, vs):
    return (1 + 2*s**2/vs**2)**-1.5*np.exp(-V**2/(vs**2 + 2*s**2))
for V, s, vs in [(0.0, 1.0, 0.1), (1.0, 0.5, 1.0), (7.5, 1.0, 10.0), (0.3, 0.3, 0.2)]:
    runs = []
    for k in range(8):
        w = rng.normal(0.0, s, size=(400000, 3))
        d2 = (V + w[:, 0])**2 + w[:, 1]**2 + w[:, 2]**2
        runs.append(np.mean(np.exp(-d2/vs**2)))
    runs = np.array(runs)
    print(f"  V={V:4.1f} s={s:4.1f} v*={vs:4.1f}: MC {runs.mean():.6e} +- {runs.std(ddof=1)/np.sqrt(len(runs)):.1e} (8 runs)"
          f"  formula {formula(V, s, vs):.6e}")
mp.mp.dps = 20
for ratio in [10, 100]:
    s = mp.mpf(ratio); vs = mp.mpf(1)
    val = mp.quad(lambda w: 4*mp.pi*w**2*(2*mp.pi*s**2)**-1.5*mp.e**(-w**2/(2*s**2))/(1 + w**2/vs**2), [0, 1, 10, s, 20*s])
    print(f"  Lorentzian, s/v* = {ratio}: <W> = {mp.nstr(val, 8)} ; (v*/s)^2 = {mp.nstr((vs/s)**2, 8)} ;"
          f" with next term (v*/s)^2 - sqrt(pi/2)(v*/s)^3 = {mp.nstr((vs/s)**2 - mp.sqrt(mp.pi/2)*(vs/s)**3, 8)}")
# Earth rotation numbers
wE = 7.2921150e-5; RE = 6378.137   # rad/s, km (dagger: standard values)
print(f"  Earth: omega R = {wE*RE:.4f} km/s ; max element-element relative speed {2*wE*RE:.3f} km/s ;"
      f" Moon (1.0245 km/s) vs elements, coplanar extremes {1.0245 - wE*RE:.3f} - {1.0245 + wE*RE:.3f} km/s")
for lat in [35.7, 48.8]:
    print(f"  lab at latitude {lat}: {wE*RE*np.cos(np.radians(lat)):.4f} km/s relative to Earth's CM")

print()
print("=== O18: atom-level gating, EP tests ===")
kB = 1.380649e-23; amu = 1.66053907e-27
A = {'Be': 9.012182, 'Al': 26.981539, 'Ti': 47.867, 'Pt': 195.084}   # standard atomic weights (dagger)
sT = {k: np.sqrt(kB*300/(m*amu))/1e3 for k, m in A.items()}            # km/s, 1D
print("  1D thermal dispersions at 300 K (km/s): " + ", ".join(f"{k} {v:.3f}" for k, v in sT.items()))
EW_lim = max(abs(0.3 - 3.6), abs(0.3 + 3.6))*1e-13
sig_mic = np.hypot(2.3, 1.5)
MIC_lim = max(abs(-1.5 - 2*sig_mic), abs(-1.5 + 2*sig_mic))*1e-15
print(f"  2 sigma |eta| limits: Eot-Wash {EW_lim:.2e}, MICROSCOPE {MIC_lim:.3e}")
def Wbar(V, s2, vs):
    return (1 + 2*s2/vs**2)**-1.5*np.exp(-V**2/(vs**2 + 2*s2))
def Kbar(V, s2, vs):
    w2 = vs**2 + 2*s2
    return (1 + 2*s2/vs**2)**-1.5*(1 + 2*V**2/w2)*np.exp(-V**2/w2)
VMIC = np.sqrt(398600.4356/(6378.137 + 710.))   # km/s at 710 km altitude (dagger altitude)
print(f"  MICROSCOPE orbital speed at 710 km altitude: {VMIC:.3f} km/s")
for sE in [0.5, 1.0, 2.0]:
    for vs in [0.1, 1.0, 10.0, 120.0, 1000.0]:
        dEW = Wbar(0.0, sT['Be']**2 + sE**2, vs) - Wbar(0.0, sT['Ti']**2 + sE**2, vs)
        dMW = Wbar(7.5, sT['Ti']**2 + sE**2, vs) - Wbar(7.5, sT['Pt']**2 + sE**2, vs)
        dMK = Kbar(7.5, sT['Ti']**2 + sE**2, vs) - Kbar(7.5, sT['Pt']**2 + sE**2, vs)
        print(f"  s_E={sE:3.1f} v*={vs:7.1f}: Eot-Wash |eps| < {EW_lim/abs(dEW):.3g} ;"
              f" MICROSCOPE with W: {MIC_lim/abs(dMW):.3g} ; with K (co-orbiting): {MIC_lim/abs(dMK):.3g}"
              f" ; ratio K/W bound {abs(dMW/dMK):.2f}")
# smeared Mars bound at v* = 120 (solar ion dispersion s_sun), Gaussian
GMsun = 132712440041.94
def adv(uc, e, NE=4096):
    E = np.arange(NE)*2*np.pi/NE; cE = np.cos(E)
    s = np.sqrt((1 + e*cE)/(1 - e*cE)); dsde = cE/(s*(1 - e*cE)**2)
    dW = -2*uc*s*np.exp(-(uc*s)**2)
    return 2*np.pi*np.sqrt(1 - e**2)/e*np.mean(dW*uc*dsde)
RAD2MAS = 180/np.pi*3600e3
vM = np.sqrt(GMsun/228.0e6)
for ssun in [100., 200., 300.]:
    vs = 120.
    w = np.sqrt(vs**2 + 2*ssun**2); Aamp = (1 + 2*ssun**2/vs**2)**-1.5
    sig = Aamp*adv(vM/w, 0.094)*36525/687.0*RAD2MAS
    print(f"  Mars, v* = 120, s_sun = {ssun:.0f}: smeared width {w:.1f} km/s, amplitude {Aamp:.4f}, |eps| < {0.094/abs(sig):.3g}")

print()
print("=== O19: nucleon-level gate, exact pair average over two Fermi spheres ===")
mN = 938.919   # MeV, mean of p and n (dagger)
for kF in [200., 250., 270.]:
    print(f"  k_F = {kF:.0f} MeV/c: v_F (relativistic p c^2/E) = {kF/np.sqrt(kF**2 + mN**2)*299792.458:.0f} km/s ;"
          f" nonrelativistic p/m = {kF/mN*299792.458:.0f} km/s")
mp.mp.dps = 30
def pair_avg(x):   # x = v*/v_F; relative-velocity density of two uniform unit spheres: overlap volume / V^2
    V = 4*mp.pi/3
    f = lambda w: (mp.pi/12)*(4 + w)*(2 - w)**2/V**2
    return mp.quad(lambda w: 4*mp.pi*w**2*f(w)*mp.e**(-(w/x)**2), [0, x, 5*x, 2])
for x in [0.05, 0.02, 0.0130, 1.3e-3, 1.3e-6]:
    ex = pair_avg(mp.mpf(x)); lead = 3*mp.sqrt(mp.pi)/4*mp.mpf(x)**3
    print(f"  v*/v_F = {x:9.3g}: exact {mp.nstr(ex, 8)} ; (3 sqrt(pi)/4)(v*/v_F)^3 = {mp.nstr(lead, 8)} ; ratio {mp.nstr(ex/lead, 6)}")
# own Monte Carlo at v*/v_F = 0.05, independent runs
def mc(x, n=1_000_000, runs=8):
    out = []
    for k in range(runs):
        def ball(n):
            d = rng.normal(size=(n, 3)); d /= np.linalg.norm(d, axis=1)[:, None]
            return d*rng.random(n)[:, None]**(1/3)
        w = ball(n) - ball(n)
        out.append(np.mean(np.exp(-np.sum(w**2, axis=1)/x**2)))
    out = np.array(out)
    return out.mean(), out.std(ddof=1)/np.sqrt(runs)
m, e = mc(0.05)
print(f"  own MC at v*/v_F = 0.05: {m:.4e} +- {e:.1e} (8 runs of 1e6 pairs)")
vF = 77137.
for vs in [0.1, 1., 10., 120., 1000.]:
    W = 3*np.sqrt(np.pi)/4*(vs/vF)**3
    print(f"  v* = {vs:7.1f}: <W> = {W:.3g} ; best-case MICROSCOPE |eps| < {MIC_lim/W:.2g}")

print()
print("=== O21: rotor-averaged K (agent's hybrid model: rotor elements gated individually, Earth as a point) ===")
def Kg(u): return (1 + 2*u**2)*np.exp(-u**2)
rho = (np.arange(400) + 0.5)/400; phi = np.arange(720)*2*np.pi/720
R_, P_ = np.meshgrid(rho, phi, indexing='ij'); wgt = R_   # uniform disk: area weight rho
for vrim, vs, lat in [(60, 0.1, 48.8), (30, 0.1, 35.7), (60, 0.3, 48.8), (30, 1.0, 35.7)]:
    V = wE*RE*np.cos(np.radians(lat))
    vx = V - vrim*1e-3*R_*np.sin(P_); vy = vrim*1e-3*R_*np.cos(P_)
    Kav = np.sum(Kg(np.hypot(vx, vy)/vs)*wgt)/np.sum(wgt)
    dK = Kav - Kg(V/vs)
    print(f"  v_rim={vrim} m/s v*={vs} km/s lat={lat}: Delta K = {dK:+.3g} -> |eps| < {1e-6/abs(dK):.2g} per 1e-6 weighing sensitivity")
