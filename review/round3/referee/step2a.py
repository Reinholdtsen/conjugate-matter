"""Step 2a: recompute the manuscript's numerical statements (Secs. 2-4) with independently sourced constants.

Constants and sources (independent of manuscript inputs):
  alpha(0)^-1 = 137.035999     CODATA 2018 / PDG 2024 physical constants
  alpha_hat^(5)(MZ)^-1 = 127.930 (MSbar)   PDG 2024 "Electroweak model" review, p.4 (dl/pdgew)
  MZ = 91.1876 GeV             PDG
  M_Pl = 1.220890e19 GeV       PDG 2024 astrophysical constants (dl/pdgastro)
  reduced M_Pl = M_Pl/sqrt(8 pi)
  rho_crit/h^2 = 1.053672e-5 GeV cm^-3   PDG 2024 astrophysical constants
  Omega_c h^2 = 0.120          Planck 2018 VI abstract
  s0 = 2891.2 cm^-3            PDG 2024 astrophysical constants
  hbar c = 1.973269804e-14 GeV cm ; 1 GeV^-2 = 3.893794e-28 cm^2 ; 1 GeV = 1.78266192e-24 g ; c = 2.99792458e10 cm/s
  local DM density: manuscript uses 0.4 GeV/cm^3; PDG canonical 0.3 "within factor 2-3" -> also report 0.3
  Planck 2018 eq. (67b): N_eff = 2.99 +0.34 -0.33 (95%); N_eff,SM = 3.044 (Bennett et al 2021) or 3.046 (Planck's value)
"""
import numpy as np
from math import pi, sqrt, log, log10

a0inv = 137.035999
aMZinv_MS = 127.930
MZ = 91.1876
MPl = 1.220890e19
MPl_red = MPl / sqrt(8 * pi)
rhoc_h2 = 1.053672e-5
Oc_h2 = 0.120
s0 = 2891.2
hbarc = 1.973269804e-14
GeV2cm2 = 3.893794e-28
GeV_g = 1.78266192e-24
c_cm = 2.99792458e10

def hdr(t):
    print("\n" + "=" * 8 + " " + t + " " + "=" * 8)

# ---------------------------------------------------------------- couplings
hdr("COUPLINGS")
alpha = 1 / a0inv
gd = sqrt(16 * pi * alpha)              # (gd/2)^2/4pi = alpha
aW = gd**2 / (4 * pi)
am = (4 * pi / gd)**2 / (4 * pi)
print(f"H: (gd/2)^2/4pi = alpha -> gd = {gd:.5f}, alpha_W' = {aW:.6f} = 1/{1/aW:.3f}, alpha_m = g_m^2/4pi = {am:.3f}")
print(f"check alpha_m * alpha_W' = {am*aW:.6f} (should be 1)")
# variant: match W' charge (gd) to e
print(f"variant W'-charge matched: alpha_W'=alpha -> alpha_m = 1/alpha = {a0inv:.3f}")
# variant: smallest SM charge is e/3 (down quark), not e
am_third = 1 / (4 * alpha / 9)
print(f"variant psi charge matched to e/3 (smallest SM charge): alpha_m = 9/(4 alpha) = {am_third:.1f}")
# one-loop SM running of alpha_em from MZ to 1e12 GeV:  d(alpha^-1)/dlnmu = -(b_Y + b_2)/(2pi), b_Y=41/6, b_2=-19/6
for lab, ainv_start in [("MSbar 127.930", aMZinv_MS), ("on-shell-ish 128.95", 128.95)]:
    L = log(1e12 / MZ)
    ainv12 = ainv_start - (41 / 6 - 19 / 6) / (2 * pi) * L
    print(f"running ({lab}): alpha^-1(1e12 GeV) = {ainv12:.2f} -> alpha_m = alpha^-1/4 = {ainv12/4:.2f}")
# naive QED-only running from 0 with only the electron (illustration of why the hadronic part matters)
# not used.

# ---------------------------------------------------------------- monopole mass relation
hdr("MONOPOLE MASS RELATION M = 4 pi f v / g_d")
f_inf = 1.7867   # step2b_inf.py: 1.7857 on [1e-3,L] + 1e-3 from [0,1e-3] (K~1-a xi^2)
k_lo, k_hi = 4 * pi / gd, 4 * pi * f_inf / gd
print(f"4 pi/g_d = {k_lo:.3f};  4 pi f_inf/g_d = {k_hi:.3f}  -> M = ({k_lo:.1f} - {k_hi:.1f}) v")

# ---------------------------------------------------------------- benchmark v and W' mass
hdr("BENCHMARK M = 3e13 GeV: v and m_W'")
M = 3e13
v_hi, v_lo = M / k_lo, M / k_hi
print(f"v = {v_lo:.3e} - {v_hi:.3e} GeV ; m_W' = g_d v = {gd*v_lo:.3e} - {gd*v_hi:.3e} GeV")

# ---------------------------------------------------------------- DM density, Kibble abundance
hdr("DARK MATTER DENSITY")
rho_DM = Oc_h2 * rhoc_h2  # GeV/cm^3
print(f"rho_DM mean = {rho_DM:.4e} GeV/cm^3 = {rho_DM*1e6:.3f} keV/cm^3")

hdr("KIBBLE: n/s for one monopole per horizon volume")
def Hubble(T, gstar, mpl=MPl):
    return sqrt(8 * pi**3 * gstar / 90) * T**2 / mpl
for gs in [100.0, 106.75]:
    T = 1.0  # n/s / (T/MPl)^3 is T-independent
    H = Hubble(T, gs)
    s = 2 * pi**2 / 45 * gs * T**3
    p_H3 = H**3 / s / (T / MPl)**3
    p_sph = p_H3 / (4 * pi / 3)
    print(f"g*={gs}: H = {sqrt(8*pi**3*gs/90):.3f} sqrt-factor * T^2/MPl ; "
          f"p(one per H^-3) = {p_H3:.2f} ; p(one per (4pi/3)H^-3) = {p_sph:.2f}")
print(f"manuscript p = 0.023 ; 45/(2 pi^2 * 100) = {45/(2*pi**2*100):.4f}  <- equals n=(T^2/MPl)^3 i.e. H without 1.66 sqrt(g*)")
print(f"missing factor (1.66 sqrt(100))^3 = {sqrt(8*pi**3*100/90)**3:.1f}")

def Mstar(p, k, mpl=MPl, rho=rho_DM, s=s0):
    # rho = M * n = M * p (v/mpl)^3 s  with v = M/k
    return (rho * k**3 * mpl**3 / (p * s))**0.25

print("\nM* reproduction with manuscript inputs (p in [0.023,1], k in [21,37], MPl=1.22e19):")
for p in [0.023, 1.0]:
    for k in [k_lo, k_hi]:
        print(f"   p={p:<6} k={k:6.2f}: M* = {Mstar(p,k):.3e} GeV")
print("M* with p from one-per-Hubble-volume (g*=100):")
p100 = sqrt(8 * pi**3 * 100 / 90)**3 / (2 * pi**2 / 45 * 100)  # n=H^3, s=(2pi^2/45)g T^3, per (T/MPl)^3
for p, lab in [(p100, "H^-3"), (p100 / (4 * pi / 3), "(4pi/3)H^-3")]:
    print(f"   p={p:7.2f} ({lab}): M* = {Mstar(p,k_lo):.3e} - {Mstar(p,k_hi):.3e} GeV")
for p in [p100]:
    for k in [k_lo, k_hi]:
        print(f"   overproduction at benchmark 3e13 (p={p:.1f}, k={k:.1f}): (M/M*)^4 = {(3e13/Mstar(p,k))**4:.3e}")
print(f"reduced-Planck 'convention' factor (MPl/MPl_red)^(3/4) = {(MPl/MPl_red)**0.75:.3f}")
print(f"dilution needed at M=1e16 with M*=3e13: (1e16/3e13)^4 = {(1e16/3e13)**4:.3e}; with M*=0.9e13: {(1e16/0.9e13)**4:.3e}; "
      f"with corrected M*={Mstar(p100,k_hi):.2e}: {(1e16/Mstar(p100,k_hi))**4:.3e}")
for xi in [0.77, 0.76]:
    print(f"xi^(3/4) at xi={xi}: {xi**0.75:.3f}")

# ---------------------------------------------------------------- benchmark densities
hdr("BENCHMARK DENSITIES (M = 3e13 GeV)")
n_mean = rho_DM / M
print(f"mean n = {n_mean:.3e} /cm^3")
for rho_loc in [0.4, 0.3]:
    n_loc = rho_loc / M
    vol = 1 / n_loc  # cm^3
    print(f"rho_loc={rho_loc}: n = {n_loc:.3e}/cm^3, volume per monopole = {vol*1e-15:.4f} km^3, spacing n^-1/3 = {vol**(1/3)/100:.1f} m")

# ---------------------------------------------------------------- counterfactual flux
hdr("COUNTERFACTUAL FLUX (if magnetically charged under our U(1))")
n_loc = 0.4 / M
for vlab, vel in [("1e-3 c", 1e-3), ("PDG eq.95.8 v_mag=1e-3c(1e17/M)^0.5", 1e-3 * sqrt(1e17 / M))]:
    F = n_loc * vel * c_cm / (4 * pi)
    parker = 1e-15
    macro = 2.8e-16
    ext = 1e-16 * (M / 1e17)
    ext_pdg = 1e-16 * (M / 1e17 + 3e-6)
    print(f"v={vlab} ({vel:.3e} c): F = {F:.3e} /cm^2/s/sr ; log10 excess: Parker {log10(F/parker):.2f}, "
          f"MACRO(2.8e-16) {log10(F/macro):.2f}, ext.Parker {log10(F/ext):.2f} (PDG form {log10(F/ext_pdg):.2f})")

# ---------------------------------------------------------------- kinetic mixing
hdr("KINETIC MIXING eps ~ v/M_*")
for v in [v_lo, v_hi]:
    for lab, Ms in [("MPl", MPl), ("MPl_red", MPl_red)]:
        print(f"v={v:.2e}, M_*={lab}: v/M_* = {v/Ms:.2e}")
gY = 0.357  # hypercharge coupling g' near MZ (g'=e/cos thetaW); ~0.46 at 1e12 GeV
loop = gd * gY / (16 * pi**2)
print(f"one-loop UV-completion factor g_d g' y/(16 pi^2) with y=1, g'={gY}: {loop:.2e} -> eps range "
      f"{loop*v_lo/MPl:.1e} - {loop*v_hi/MPl_red:.1e} (Lambda=MPl..MPl_red)")
# visible charge of psi: eps * (g_d/2)/e * cos(thetaW) [B -> photon projection]
cw = 0.8815
print(f"psi visible charge = eps*cos(thetaW)*((g_d/2)/e) e; (g_d/2)/e = {(gd/2)/sqrt(4*pi*alpha):.3f}, cos thetaW={cw}")

# ---------------------------------------------------------------- Delta N_eff
hdr("DARK RADIATION")
g_h_high = 2 * 3 + 3 + 7 / 8 * (2 * 4)  # SU(2) gauge (3x2) + real adjoint (3) + Dirac doublet (2x4 x 7/8)
g_h_late = 2.0
for g_vis_high in [106.75]:
    for g_nu_dec in [10.75]:
        r = ((g_h_high / g_h_late) / (g_vis_high / g_nu_dec))**(1 / 3)   # T_h/T_nu after all annihilations
        dN = 8 / 7 * r**4
        print(f"g_h(high)={g_h_high}, g_h(late)={g_h_late}, g_vis(high)={g_vis_high}: T_h/T_nu = {r:.4f}, DeltaN_eff = {dN:.4f}")
        # cross-check with Planck eq.(65)-type: thermalized boson with g=2 decoupling at g_s, then heated by hidden entropy
        for Nsm in [3.044, 3.046]:
            dNmax = 2.99 + 0.34 - Nsm
            print(f"   N_eff,SM={Nsm}: DeltaN_max(95%) = {dNmax:.3f} -> xi_max = {(dNmax/dN)**0.25:.4f}")
        print(f"   xi needed for DeltaN<0.30: {(0.30/dN)**0.25:.4f}")

# ---------------------------------------------------------------- self interaction
hdr("SIGMA_T / M")
vrel = 1e-3
for lnL in [10, 30]:
    sig = 8 * pi * am**2 * lnL / ((M / 2)**2 * vrel**4) * GeV2cm2  # manuscript formula
    sig_mine = 4 * pi * am**2 * lnL / ((M / 2)**2 * vrel**4) * GeV2cm2  # sigma_T = 4 pi alpha^2 lnL/(mu^2 v^4)
    print(f"lnL={lnL}: manuscript formula sigma_T/M = {sig/(M*GeV_g):.3e} cm^2/g ; standard 4pi a^2 lnL/(mu^2 v^4): {sig_mine/(M*GeV_g):.3e} cm^2/g")
print(f"orders below 1 cm^2/g: {-log10(8*pi*am**2*20/((M/2)**2*vrel**4)*GeV2cm2/(M*GeV_g)):.1f}")

# ---------------------------------------------------------------- GW peak frequency
hdr("GW PEAK FREQUENCY  f0 = 1.65e-5 Hz (f*/H*) (T*/100 GeV) (g*/100)^(1/6)")
for Tst in [v_lo, v_hi]:
    for ratio in [1, 100]:
        for g in [106.75, 106.75 + 16]:
            f0 = 1.65e-5 * ratio * (Tst / 100) * (g / 100)**(1 / 6)
            print(f"T*={Tst:.2e} f*/H*={ratio:<3} g*={g}: f0 = {f0:.2e} Hz")
