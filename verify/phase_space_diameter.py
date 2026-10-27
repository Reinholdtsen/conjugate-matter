#!/usr/bin/env python3
"""
phase_space_diameter.py — every number that papers/phase-space-diameter.md (the
phase-space-diameter note) computes, recomputed and checked. Figures the note
quotes from the literature (Egan and Lineweaver's entropies, the squeezing
values, FKGLM's estimates) are not recomputed, except where a check below
reproduces them; the torsion-balance limits are typed in from the source table.

    .venv/bin/python verify/phase_space_diameter.py

Exit code 1 if any check fails. Anchors come first and are independent of the
note: CODATA 2018's published Planck units, the PDG photon and entropy
densities and dark-energy scale, a Bose integral evaluated two ways, a
published comoving horizon, and the two published limits of Lee et al. 2020
that the exclusion-table interpolation must reproduce.

Inputs: CODATA 2018 constants; Planck 2018 cosmology (H0 = 67.4 km/s/Mpc,
Omega_m = 0.315), T_CMB = 2.7255 K, three massless neutrinos at
(4/11)^(1/3) T, flat, Omega_Lambda = 1 - Omega_m - Omega_r. Standard Model
g_s = 106.75 at high temperature. The radiation rectangle is a sphere of
blackbody photons: D_x its diameter, D_p twice the mean photon momentum.
"""
import sys
from math import pi, sqrt, log, log10, exp, cosh, acosh
import mpmath as mp
import numpy as np
import sympy as sp

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def close(x, y, rel):
    return abs(x/y - 1) < rel

# CODATA 2018 (h, c, k_B, e exact; G measured)
HBAR = 6.62607015e-34/(2*pi); H_PL = 2*pi*HBAR; C = 299792458.0; G = 6.67430e-11
KB = 1.380649e-23; EV = 1.602176634e-19; GEV = 1e9*EV
EPS0 = 8.8541878128e-12; A_BOHR = 5.29177210903e-11; R_E = 2.8179403262e-15
L_P = sqrt(HBAR*G/C**3); M_P = sqrt(HBAR*C/G); P_P = M_P*C; E_P = M_P*C**2
T_P = E_P/KB; T_PL = L_P/C
MPC = 3.0856775814913673e22; GLY = 9.4607304725808e24; AU = 1.495978707e11
H0 = 67.4e3/MPC; OM = 0.315; T0 = 2.7255
ZETA3 = 1.2020569031595942
G_S0 = 2 + (7/8)*6*(4/11); G_S_SM = 106.75; G_N_SM = 28 + 0.75*90

# radiation: photons + 3 massless neutrinos; flat
RHO_CRIT = 3*H0**2/(8*pi*G)
RHO_GAMMA = (pi**2/15)*(KB*T0)**4/(HBAR*C)**3/C**2
OR = RHO_GAMMA*(1 + 3*(7/8)*(4/11)**(4/3))/RHO_CRIT
OL = 1 - OM - OR
def E(a):
    return sqrt(OR/a**4 + OM/a**3 + OL)
CHI = C/H0*float(mp.quad(lambda a: 1/(a**2*E(float(a))), [0, 1e-6, 1e-4, 1e-2, 1]))    # particle horizon
CEH = C/H0*float(mp.quad(lambda a: 1/(a**2*E(float(a))), [1, 10, 100, mp.inf]))        # event horizon
L_H = C/H0
L_L = C/(H0*sqrt(OL))
N_GAMMA = 2*ZETA3/pi**2*(KB*T0/(HBAR*C))**3
S0 = (2*pi**2/45)*G_S0*(KB*T0/(HBAR*C))**3
MEAN_X = float(mp.quad(lambda x: x**3/(mp.e**x - 1), [0, mp.inf])/mp.quad(lambda x: x**2/(mp.e**x - 1), [0, mp.inf]))
RHO_L = OL*RHO_CRIT*C**2
# Lee 2020 thesis, Table 11.4 (lambda in mm; +alpha95; |alpha95|), the rows bracketing the crossings
TAB = [(0.025, 7.9, 6.4), (0.028, 4.51, 3.73), (0.032, 2.56, 2.08), (0.035, 1.77, 1.45), (0.040, 1.06, 0.877),
       (0.045, 0.699, 0.585), (0.050, 0.494, 0.419), (0.056, 0.35, 0.3), (0.063, 0.251, 0.218),
       (0.071, 0.183, 0.162), (0.079, 0.14, 0.126), (0.089, 0.106, 0.097), (0.100, 0.0813, 0.0766)]
def crossing(col, target):
    for (l1_, *a1), (l2_, *a2) in zip(TAB, TAB[1:]):
        y1, y2 = a1[col], a2[col]
        if (y1 - target)*(y2 - target) <= 0:
            t = log(y1/target)/log(y1/y2)
            return exp(log(l1_) + t*log(l2_/l1_))*1e-3
    return None
E14 = (RHO_L*(HBAR*C)**3)**0.25                                  # rho_Lambda^(1/4) as an energy

print("== Anchors (independent of the note)")
check("CODATA 2018 Planck length 1.616255e-35 m", close(L_P, 1.616255e-35, 2e-6), f"{L_P:.6e}")
check("CODATA 2018 Planck mass 2.176434e-8 kg", close(M_P, 2.176434e-8, 2e-6), f"{M_P:.6e}")
check("CODATA 2018 Planck temperature 1.416784e32 K", close(T_P, 1.416784e32, 2e-6), f"{T_P:.6e}")
check("CODATA 2018 Planck time 5.391247e-44 s", close(T_PL, 5.391247e-44, 2e-6), f"{T_PL:.6e}")
check("PDG: photon number density 410.73 cm^-3 at 2.7255 K", close(N_GAMMA/1e6, 410.73, 1e-4), f"{N_GAMMA/1e6:.2f}")
check("PDG: entropy density s/k = 2891.2 cm^-3", close(S0/1e6, 2891.2, 1e-4), f"{S0/1e6:.1f}")
check("blackbody mean photon energy: quadrature = pi^4/(30 zeta(3)) = 2.701 kT",
      abs(MEAN_X - pi**4/(30*ZETA3)) < 1e-12 and round(MEAN_X, 3) == 2.701, f"{MEAN_X:.6f}")
check("comoving particle horizon: 'about 46 Glyr' (Davis-Lineweaver 2004), within 1%", close(CHI/GLY, 46.0, 0.01),
      f"{CHI/GLY:.2f} Gly")
OL_PDG, H_PDG = 0.68, 0.67
E14_PDG = (OL_PDG*3*(H_PDG*1e5/MPC)**2/(8*pi*G)*C**2*(HBAR*C)**3)**0.25
check("PDG Big-Bang review: dark energy ~ (2.2 meV)^4 for Omega_v = 0.68, h = 0.67", round(E14_PDG/EV*1e3, 1) == 2.2,
      f"{E14_PDG/EV*1e3:.3f} meV")

print("\n== The conserved area (note §3)")
z3, spi = sp.zeta(3), sp.pi
KAPPA = float(sp.Integer(3)**sp.Rational(1, 3)*spi**sp.Rational(10, 3)/(30*z3**sp.Rational(4, 3)))
def nden(T):
    return 2*ZETA3/pi**2*(KB*T/(HBAR*C))**3
def sphere(R, T):
    """sphere of radius R filled with blackbody photons at T: (D_x, D_p = 2<p>, N)"""
    return 2*R, 2*MEAN_X*KB*T/C, nden(T)*4*pi/3*R**3
ratios = [sphere(R, T)[0]*sphere(R, T)[1]/H_PL/sphere(R, T)[2]**(1/3) for R, T in [(CHI, T0), (1.0, 1e10), (1e-30, 1e32)]]
check("D_x D_p = kappa h N^(1/3), kappa = 3^(1/3) pi^(10/3)/(30 zeta(3)^(4/3)) = 1.708, at any R and T",
      all(abs(r - KAPPA) < 1e-9 for r in ratios) and round(KAPPA, 3) == 1.708, f"kappa = {KAPPA:.6f}")
DX, DP, N_OBS = sphere(CHI, T0)
k_kT = DX*(KB*T0/C)/H_PL/N_OBS**(1/3)
k_mean = DX*(MEAN_X*KB*T0/C)/H_PL/N_OBS**(1/3)
k_cube = DX*DP/H_PL/(nden(T0)*DX**3)**(1/3)
check("other definitions: kappa = 0.316 (D_p = kT/c), 0.854 (<p>), 1.377 (cube of side D_x)",
      round(k_kT, 3) == 0.316 and round(k_mean, 3) == 0.854 and round(k_cube, 3) == 1.377,
      f"{k_kT:.4f}, {k_mean:.4f}, {k_cube:.4f}")
V_OBS = 4*pi/3*CHI**3; V_H = 4*pi/3*L_H**3
S_OBS = S0*V_OBS
PROD = DX*DP/H_PL
print(f"      D_x = {DX:.4e} m, D_p = {DP:.4e} kg m/s, N_gamma = {N_OBS:.4e}, S = {S_OBS:.4e} k_B")
check("observable universe: radius 46.1 Gly; D_x = 8.73e26 m, D_p = 6.78e-31 kg m/s",
      round(CHI/GLY, 1) == 46.1 and round(DX/1e24) == 873 and round(DP/1e-33) == 678)
check("N_gamma = 1.43e89, S = 1.01e90 k_B (the chat's ~10^90 is S)",
      round(N_OBS/1e87) == 143 and round(S_OBS/1e88) == 101, f"{N_OBS:.3e}, {S_OBS:.3e}")
check("S^(1/3) = 1.0e30; area D_x D_p = 8.9e29 h", round(S_OBS**(1/3)/1e29) == 10 and round(PROD/1e28) == 89,
      f"{S_OBS**(1/3):.3e}, {PROD:.3e}")
check("entropy per photon: 3.60 (photons alone), 7.04 (with neutrinos)",
      round(2*pi**4/(45*ZETA3), 2) == 3.60 and round(S0/N_GAMMA, 2) == 7.04, f"{S0/N_GAMMA:.4f}")
check("(arithmetic of the quoted factors) photon number jumps by 11/4 at annihilation (before it: 4/11 of today's), "
      "aT by (11/4)^(1/3) = 1.40; (106.75/3.909)^(1/3) = 3.01", round(((11/4)**(1/3))**3, 12) == 2.75 and round((11/4)**(1/3), 2) == 1.40
      and round((G_S_SM/G_S0)**(1/3), 2) == 3.01)

print("\n== Extent, resolution and the published answers (note §4)")
NC = L_H/L_P
check("c/H0 = 1.37e26 m; L/l_P = 8.49e60 cells per axis; the cube 6.12e182",
      round(L_H/1e24) == 137 and round(NC/1e58) == 849 and round(NC**3/1e180) == 612, f"{NC:.4e}")
check("Gibbons-Hawking pi L^2/l_P^2 = 3.31e122 for L_Lambda = 1.66e26 m; 3.0e122 for the event horizon, 16.7 Gly",
      round(L_L/1e24) == 166 and round(pi*L_L**2/L_P**2/1e120) == 331 and round(pi*CEH**2/L_P**2/1e121) == 30
      and round(CEH/GLY, 1) == 16.7, f"CEH {CEH/GLY:.2f} Gly")
CKN = lambda L: sqrt(E_P*HBAR*C/L)
check("CKN cutoff (M_P/L)^(1/2) = 4.19 meV for L = c/H0 (CKN's own estimate: ~10^-2.5 eV)",
      round(CKN(L_H)/EV*1e3, 2) == 4.19 and abs(log10(CKN(L_H)/EV) + 2.5) < 0.2, f"{log10(CKN(L_H)/EV):.3f}")
B_BORN = H_PL/(pi*R_E)                                 # Born 1938: r0 = h/(pi b)
check("Born 1938: b from the classical electron radius by r0 = h/(pi b), b c = 2 hbar c/r0 = 1.4e8 eV",
      round(B_BORN*C/EV/1e7) == 14 and close(B_BORN*C, 2*HBAR*C/R_E, 1e-12), f"{B_BORN*C/EV:.4e} eV")
check("Grosse-Wulkenhaar: Omega = (l_P/L)^2 = 1.4e-122 for L = c/H0", round((L_P/L_H)**2*1e123) == 14,
      f"{(L_P/L_H)**2:.3e}")
S_DS = pi*L_L**2/L_P**2
check("per-axis counts: radiation S^(1/3) = 1.0e30 against FKGLM's S_dS^(1/4) = 4.3e30",
      round(S_OBS**(1/3)/1e29) == 10 and round(S_DS**0.25/1e29) == 43, f"{S_DS**0.25:.3e}")
check("both counts are conserved for the fixed region, so S^(1/3)/S_dS^(1/4) = 0.235 at every epoch",
      round(S_OBS**(1/3)/S_DS**0.25, 3) == 0.235, f"{S_OBS**(1/3)/S_DS**0.25:.4f}")
Ts = sp.symbols('T', positive=True)
ckn = []
for gst in (3.36, 106.75):                              # radiation-era Hubble sphere, Planck units
    Hh = sp.sqrt(8*sp.pi**3*gst/90)*Ts**2
    Srad = (2*sp.pi**2/45)*gst*Ts**3*sp.Rational(4, 3)*sp.pi/Hh**3
    SBH = sp.pi/Hh**2
    rr = sp.simplify(Srad**sp.Rational(1, 3)/SBH**sp.Rational(1, 4))
    ckn.append((float(rr), sp.diff(rr, Ts) == 0, sp.diff(sp.simplify(Srad/SBH**sp.Rational(3, 4)), Ts) == 0))
check("CKN saturation: a radiation-era Hubble sphere has S^(1/3)/S_BH^(1/4) = 0.79-1.05 (g = 3.36-106.75) "
      "and S proportional to S_BH^(3/4), at every temperature",
      [round(x[0], 2) for x in ckn] == [0.79, 1.05] and all(x[1] and x[2] for x in ckn), f"{[round(x[0], 4) for x in ckn]}")

print("\n== Reciprocity on a rectangle; wave packets (note §5)")
lam, l1, l2, hb, Lx, Pp = sp.symbols('lambda lambda1 lambda2 hbar L P', positive=True)
Rl = lambda l: sp.Matrix([[0, l**2/hb], [-hb/l**2, 0]])
W = sp.Matrix([[0, 1], [-1, 0]])
check("rho_lambda is symplectic for every lambda (R^T w R = w)", sp.simplify(Rl(lam).T*W*Rl(lam) - W) == sp.zeros(2))
L2, P2 = lam**2*Pp/hb, hb*Lx/lam**2
A_of = lambda L_, P_: hb*L_/(lam**2*P_)
check("the area L P is invariant for every lambda", sp.simplify(L2*P2 - Lx*Pp) == 0)
check("the aspect ratio A = hbar L/(lambda^2 P) goes to 1/A", sp.simplify(A_of(L2, P2)*A_of(Lx, Pp) - 1) == 0)
check("A = 1 iff lambda^2 = hbar L/P", sp.solve(sp.Eq(A_of(Lx, Pp), 1), lam) == [sp.sqrt(hb*Lx/Pp)])
check("two Born lengths differ by a squeeze: rho_l1 rho_l2^-1 = diag((l1/l2)^2, (l2/l1)^2)",
      sp.simplify(Rl(l1)*Rl(l2).inv() - sp.diag(l1**2/l2**2, l2**2/l1**2)) == sp.zeros(2))
# Gaussian psi ~ exp(i Z x^2/2), hbar = lambda = 1: widths
x, X_, Y_ = sp.symbols('x X Y', real=True)
Ypos = sp.symbols('Ypos', positive=True)
rho_x = sp.exp(-Ypos*x**2)                                         # |psi|^2
dx2 = sp.integrate(x**2*rho_x, (x, -sp.oo, sp.oo))/sp.integrate(rho_x, (x, -sp.oo, sp.oo))
check("Delta x^2 = 1/(2Y) for psi_Z", sp.simplify(dx2 - 1/(2*Ypos)) == 0)
# momentum width from the Fourier transform -1/Z: Im(-1/Z) = Y/|Z|^2, so Delta p^2 = |Z|^2/(2Y)
Zs = X_ + sp.I*Ypos
imz = sp.simplify(sp.im(-1/Zs))
check("Fourier image has Im(-1/Z) = Y/|Z|^2, so Delta p^2 = |Z|^2/(2Y) and Delta x/Delta p = 1/|Z|",
      sp.simplify(imz - Ypos/(X_**2 + Ypos**2)) == 0)
NX = 2**14; DXG = 80/NX
xg = (np.arange(NX) - NX//2)*DXG
Zn = 0.3 + 0.7j
psi = np.exp(1j*Zn*xg**2/2)
pg = 2*pi*np.fft.fftshift(np.fft.fftfreq(NX, d=DXG))
phi = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(psi)))
k = np.abs(pg) < 3
ph = np.polyfit(pg[k]**2/2, np.unwrap(np.angle(phi[k])), 1)
mg = np.polyfit(pg[k]**2/2, np.log(np.abs(phi[k])), 1)
Zt = ph[0] - 1j*mg[0]
check("Fourier transform maps Z = 0.3 + 0.7i to -1/Z = -0.5172 + 1.2069i (numerical FFT)",
      abs(Zt - (-1/Zn)) < 1e-6 and round(Zt.real, 4) == -0.5172 and round(Zt.imag, 4) == 1.2069, f"{Zt:.6f}")
pw = np.abs(phi)**2; pw /= pw.sum()
xw = np.abs(psi)**2; xw /= xw.sum()
ratio_num = sqrt((xw*xg**2).sum())/sqrt((pw*pg**2).sum())
check("numerically Delta x/Delta p = 1/|Z| for Z = 0.3 + 0.7i", abs(ratio_num - 1/abs(Zn)) < 1e-6, f"{ratio_num:.6f}")
def d_half(z, w):
    return acosh(1 + abs(z - w)**2/(2*z.imag*w.imag))
check("half-plane distance from i to iY is |ln Y| (Y = 3, 1/7, 1e5)",
      all(abs(d_half(1j, 1j*y) - abs(log(y))) < 1e-9 for y in (3.0, 1/7, 1e5)))
zs = [0.3 + 0.7j, -2.0 + 0.1j, 0.5 + 3.0j, 1e-3 + 0.2j]
check("off the slice |ln(Delta x/Delta p)| = |ln|Z|| is smaller than d(i, Z); equal on the slice",
      all(abs(log(abs(z))) < d_half(1j, z) for z in zs) and abs(abs(log(abs(0.2j))) - d_half(1j, 0.2j)) < 1e-12)
Yv = 0.2; sx, spp = sqrt(1/(2*Yv)), sqrt(Yv/2); r = log(sqrt(2)*sx)
check("for Z = iY, sigma_x/sigma_p = 1/Y and the distance |ln Y| = 2r (sigma_x = e^r/sqrt 2)",
      abs(sx/spp - 1/Yv) < 1e-12 and abs(abs(log(Yv)) - 2*r) < 1e-12)
# Fubini-Study metric along Z = iY, numerically: g_FS = <dpsi|dpsi> - |<psi|dpsi>|^2 with dpsi = d psi/dY
def psiz(Z):
    w = np.exp(1j*Z*xg**2/2); return w/sqrt((np.abs(w)**2).sum()*DXG)
def g_fs(Z, dZ):
    """Fubini-Study metric component along the direction dZ (complex step), numerically"""
    h = 1e-5
    p0, dps = psiz(Z), (psiz(Z + h*dZ) - psiz(Z - h*dZ))/(2*h)
    return ((np.abs(dps)**2).sum()*DXG - abs((np.conj(p0)*dps).sum()*DXG)**2)
fs = [(Z, g_fs(Z, d)*Z.imag**2) for Z in (0.7j, 0.3 + 0.7j, -1.2 + 0.4j) for d in (1.0, 1j)]
check("Fubini-Study metric on Gaussians is 1/8 of the Siegel metric (dX^2 + dY^2)/Y^2, in both directions, on and off "
      "the slice (so Siegel length 2r = FS length r/sqrt 2)",
      all(abs(v - 1/8) < 1e-6 for _, v in fs), f"{[round(float(v), 6) for _, v in fs]}")
def dist_siegel(Y1, Y2):
    mu = np.linalg.eigvals(np.linalg.solve(Y1, Y2)).real
    return sqrt(sum(log(m)**2 for m in mu))
check("Siegel degree 3: distance from i1 to iy1 is sqrt(3)|ln y|; rho maps iy1 to (i/y)1",
      abs(dist_siegel(np.eye(3), 5.0*np.eye(3)) - sqrt(3)*log(5.0)) < 1e-12 and
      np.allclose(-np.linalg.inv(1j*5.0*np.eye(3)), 1j/5.0*np.eye(3)))
Yd = sp.symbols('Yd', positive=True)
HZ = sp.Matrix([[Yd + X_**2/Yd, X_/Yd], [X_/Yd, 1/Yd]])
check("det H_Z = 1 at every Z; on X = 0, H = diag(Y, 1/Y)", sp.simplify(HZ.det()) == 1 and
      HZ.subs(X_, 0) == sp.diag(Yd, 1/Yd))
A0 = (DX/L_P)/(DP/P_P)
check("the clock: ln A0 = 213.5 per axis, 369.8 for the isotropic degree-3 point; 106.7 e-folds",
      round(log(A0), 1) == 213.5 and round(sqrt(3)*log(A0), 1) == 369.8 and round(log(A0)/2, 1) == 106.7,
      f"{log(A0):.3f}")

print("\n== Where the radiation rectangle is square, lambda = l_P (note §6)")
check("aspect ratio today (D_x/l_P)/(D_p/m_P c) = 5.2e92, log10 92.72", round(A0/1e91) == 52 and
      round(log10(A0), 2) == 92.72, f"{A0:.4e}")
A_SQ = A0**-0.5; T_SQ = T0/A_SQ
check("square at a/a0 = 4.4e-47, T = 4.4e14 T_P (free streaming back from today)",
      round(A_SQ/1e-48) == 44 and round(T_SQ/T_P/1e13) == 44, f"{A_SQ:.3e}, {T_SQ/T_P:.3e}")
check("closed form: sides sqrt(2 pi kappa) N^(1/6) = 3.28 N^(1/6); T_sq = 0.61 N^(1/6) T_P; N^(1/6) ~ 1e15",
      close(sqrt(2*pi*PROD), sqrt(2*pi*KAPPA)*N_OBS**(1/6), 1e-9) and round(sqrt(2*pi*KAPPA), 2) == 3.28 and
      close(T_SQ/T_P, sqrt(2*pi*KAPPA)/(2*MEAN_X)*N_OBS**(1/6), 1e-9) and
      round(sqrt(2*pi*KAPPA)/(2*MEAN_X), 2) == 0.61 and round(log10(N_OBS**(1/6))) == 15)
g = (G_S0/G_S_SM)**(1/3)
A_SQ_SM = sqrt(g/A0); T_SQ_SM = g*T0/A_SQ_SM
check("with the SM's g_s = 106.75: a/a0 = 2.5e-47, T = 2.5e14 T_P", round(A_SQ_SM/1e-48) == 25 and
      round(T_SQ_SM/T_P/1e13) == 25, f"{A_SQ_SM:.3e}, {T_SQ_SM/T_P:.3e}")
def A_at_T(TK):
    """radiation-rectangle aspect when the bath temperature is TK (SM g_s above the electroweak scale)"""
    return A0*(T0/TK)**2*g
check("at T = T_P (SM counting) the rectangle is still long by 6.4e28", round(A_at_T(T_P)/1e27) == 64,
      f"{A_at_T(T_P):.3e}")
E_INF = 1.39e16*GEV                                     # Soman et al. 2025, from r < 0.036
T_RH = (30/(pi**2*G_S_SM))**0.25*E_INF
check("instant reheating at E_inf < 1.39e16 GeV: T_rh < 5.7e15 GeV; the rectangle then has A = 2.9e35",
      round(T_RH/GEV/1e14) == 57 and round(A_at_T(T_RH/KB)/1e34) == 29, f"{T_RH/GEV:.3e} GeV, {A_at_T(T_RH/KB):.3e}")
HC = sqrt(8*pi**3*G_S_SM/90)                            # H = HC T^2 in Planck units
T_HSQ = (2/(HC*2*MEAN_X))**(1/3); R_HSQ = 1/(HC*T_HSQ**2)
N_HSQ = ZETA3/pi**2*G_N_SM*T_HSQ**3*4*pi/3*R_HSQ**3
check("Hubble sphere (radiation era, SM): square at T = 0.28 T_P, radius 0.75 l_P, about 0.45 quanta inside",
      round(T_HSQ, 2) == 0.28 and round(R_HSQ, 2) == 0.75 and round(N_HSQ, 2) == 0.45,
      f"T = {T_HSQ:.4f} T_P, R = {R_HSQ:.3f}, N = {N_HSQ:.3f}")
A_H0 = (2*L_H/L_P)/(2*MEAN_X*KB*T0/C/P_P); N_H = N_GAMMA*V_H
check("Hubble sphere today: aspect ratio 1.6e92, N_H = 4.4e87", round(A_H0/1e91) == 16 and round(N_H/1e86) == 44,
      f"{A_H0:.3e}, {N_H:.3e}")
a_hsq = g*T0/(T_HSQ*T_P)
DX_hsq = DX*a_hsq
n_patch = (DX_hsq/2/(R_HSQ*L_P))**3
check("two regions: at that epoch the observable universe was 1.2e30 l_P across, 5.6e89 Hubble patches, "
      "its rectangle long by 8e29", round(DX_hsq/L_P/1e29) == 12 and round(n_patch/1e88) == 56 and
      round(A_at_T(T_HSQ*T_P)/1e29) == 8, f"{DX_hsq/L_P:.3e}, {n_patch:.3e}, {A_at_T(T_HSQ*T_P):.3e}")
r_sq = log(1e92)/2
check("a squeezed mode with aspect 1e92 has r = 105.9, inside the literature's 100-120", round(r_sq, 1) == 105.9)
T_STR = 1e17*GEV/KB
check("at a string-scale bounce, kT = 1e17 GeV, the radiation rectangle is still long by A = 9.5e32",
      round(A_at_T(T_STR)/1e31) == 95, f"{A_at_T(T_STR):.3e}")
check("(identity) A grows as a^2, so a turnaround (maximum of a) is the maximum of A",
      all((a2 > a1) == (A0*a2**2 > A0*a1**2) for a1, a2 in [(0.5, 1.0), (1.0, 2.0), (2.0, 1.5)]))
s_ = sp.symbols('s', real=True)
Zc = sp.tanh(s_) + sp.I*sp.sech(s_)
check("the record's |Z| = 1 path Z = tanh s + i sech s: |Z| = 1, Im Z peaks at s = 0 (Z = i)",
      sp.simplify(sp.Abs(Zc)**2 - 1) == 0 and sp.solve(sp.diff(sp.sech(s_), s_), s_) == [0])
check("on |Z| = 1, H_xx = H_pp = 1/Y: the position and momentum extents are equal at all times",
      sp.simplify(HZ[0, 0].subs(X_, sp.sqrt(1 - Yd**2)) - 1/Yd) == 0)
M_X_MIN = HBAR*C/crossing(0, 4/3)                       # the interpolated one-sided bound at alpha = 4/3
check("an order-one X today: (M_X/H0)^2 = 1.3e61 for M_X c^2 = 5.2 meV", round((M_X_MIN/(HBAR*H0))**2/1e60) == 13,
      f"{(M_X_MIN/(HBAR*H0))**2:.3e}")

print("\n== The self-dual box (note §7)")
for L, um, mev in [(L_H, 47.1, 4.19), (L_L, 51.8, 3.81), (CHI, 84.0, 2.35)]:
    lam_sd = sqrt(L_P*L)
    check(f"lambda = sqrt(l_P L) = {um} um, hbar c/lambda = {mev} meV, equal to the CKN cutoff (unreduced)",
          round(lam_sd*1e6, 1) == um and round(HBAR*C/lam_sd/EV*1e3, 2) == mev and close(HBAR*C/lam_sd, CKN(L), 1e-12))
facs = [(8*pi)**-0.25, (3/(8*pi))**0.25, 0.5**0.25, (6*pi)**0.25]
check("CKN in other conventions: 0.45 (reduced M_P), 0.59 (sphere, M_BH = Lc^2/2G), 0.84 (cube, r_s = L), "
      "2.08 (one scalar's zero-point energy Lambda^4/16 pi^2)",
      [round(f, 2) for f in facs] == [0.45, 0.59, 0.84, 2.08], f"{[round(f, 4) for f in facs]}")
check("rho_Lambda^(1/4) = 2.24 meV, 88.1 um", round(E14/EV*1e3, 2) == 2.24 and round(HBAR*C/E14*1e6, 1) == 88.1)
ratio = E14/(HBAR*C/sqrt(L_P*L_H))
def de_ratio(h0_kms):
    h0 = h0_kms*1e3/MPC
    e14 = (OL*3*h0**2/(8*pi*G)*C**2*(HBAR*C)**3)**0.25
    return e14/(HBAR*C/sqrt(L_P*C/h0))
check("rho_Lambda^(1/4)/(hbar c/sqrt(l_P c/H0)) = (3 Omega_L/8 pi)^(1/4) = 0.535, at H0 = 60, 67.4 and 73",
      all(close(de_ratio(h), (3*OL/(8*pi))**0.25, 1e-10) for h in (60.0, 67.4, 73.0)) and round(ratio, 3) == 0.535,
      f"{ratio:.5f}")
check("the particle horizon's closer agreement comes from chi H0/c = 3.18", round(CHI*H0/C, 2) == 3.18 and
      close(E14/(HBAR*C/sqrt(L_P*CHI)), (3*OL/(8*pi))**0.25*sqrt(CHI*H0/C), 1e-10))
LAM2 = L_P*L_L
devs = [abs((C/(H0*E(a)))*L_P/LAM2 - sqrt(OL/E(a)**2)) for a in (1e-3, 0.1, 0.5, 1.0, 2.0, 10.0)]
check("with lambda^2 = l_P L_Lambda the Hubble box has A(t) = sqrt(Omega_Lambda(t)); 0.83 today",
      max(devs) < 1e-12 and round(sqrt(OL), 2) == 0.83, f"max deviation {max(devs):.1e}")
check("L_Lambda = lambda^2/l_P, Lambda = 3 l_P^2/lambda^4, lambda/l_P = 3.2e30 = sqrt(L_Lambda/l_P)",
      round(sqrt(LAM2)/L_P/1e29) == 32 and close(sqrt(LAM2)/L_P, sqrt(L_L/L_P), 1e-12) and
      close(3/L_L**2, 3*L_P**2/LAM2**2, 1e-12))
a_tev = sqrt(LAM2*DP/(HBAR*DX))                        # radiation rectangle square in units of sqrt(l_P L_Lambda)
a_tev_sm = sqrt(g*LAM2*DP/(HBAR*DX))
TEV = 1e12*EV
check("numerology: in units of sqrt(l_P L_Lambda) the radiation rectangle is square at kT = 1.0 TeV with the SM g_s, "
      "1.7 TeV for photons alone; sqrt(k T0 E_P) = 1.7 TeV; BHM-type sqrt(rho_L^(1/4) E_P) = 5.2 TeV",
      round(g*KB*T0/a_tev_sm/TEV, 1) == 1.0 and round(KB*T0/a_tev/TEV, 1) == 1.7 and
      round(sqrt(KB*T0*E_P)/TEV, 1) == 1.7 and round(sqrt(E14*E_P)/TEV, 1) == 5.2,
      f"{g*KB*T0/a_tev_sm/TEV:.3f}, {KB*T0/a_tev/TEV:.3f}, {sqrt(KB*T0*E_P)/TEV:.3f}, {sqrt(E14*E_P)/TEV:.2f} TeV")
check("the reformulation takes the fourth root: log10(Lambda l_P^2) = -121.5 against log10(lambda/l_P) = 30.5",
      abs(log10(sqrt(LAM2)/L_P)/log10(3*L_P**2/L_L**2) + 0.25) < 1e-3 and round(log10(sqrt(LAM2)/L_P), 1) == 30.5)
check("the Born length that makes today's radiation rectangle square: sqrt(hbar D_x/D_p) = 3.7e11 m, 2.5 au",
      round(sqrt(HBAR*DX/DP)/1e10) == 37 and round(sqrt(HBAR*DX/DP)/AU, 1) == 2.5)

print("\n== Consequences (note §8)")
F_P = C**4/G
check("c~ = c^4/G = 1.21e44 N at lambda = l_P", round(F_P/1e42) == 121 and close(HBAR*C/L_P**2, F_P, 1e-12))
CT_H, CT_L = HBAR*C/(L_P*L_H), HBAR*C/(L_P*L_L)
check("at the self-dual length c~ = 1.4e-17 N (c/H0), 1.2e-17 N (L_Lambda); c~/(c^4/G) = l_P/L",
      round(CT_H*1e18) == 14 and round(CT_L*1e18) == 12 and close(CT_H/F_P, L_P/L_H, 1e-12))
F_BOHR = EV**2/(4*pi*EPS0*A_BOHR**2)
check("hydrogen Coulomb force 8.24e-8 N (CODATA atomic unit 8.2387234983e-8 N) exceeds it by 5.8e9; 1 kg weight by 6.9e17",
      close(F_BOHR, 8.2387234983e-8, 1e-9) and round(F_BOHR/CT_H/1e8) == 58 and round(9.80665/CT_H/1e16) == 69)
check("with the Born length at l_P the Hubble box is long by L/l_P = 8.5e60", round(NC/1e59) == 85)
check("anchor: the interpolation reproduces Lee et al.'s published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3)",
      round(crossing(1, 1.0)*1e6, 1) == 38.6 and round(crossing(1, 8/3)*1e6) == 30,
      f"{crossing(1, 1.0)*1e6:.2f}, {crossing(1, 8/3)*1e6:.2f} um")
LX = crossing(0, 4/3)
check("attractive Yukawa with alpha = 4/3 (one-sided +alpha95): lambda_X < 37.7 um, M_X c^2 > 5.2 meV",
      round(LX*1e6, 1) == 37.7 and round(HBAR*C/LX/EV*1e3, 1) == 5.2, f"{LX*1e6:.2f} um, {HBAR*C/LX/EV*1e3:.3f} meV")
check("Lee et al.'s 5.1 meV is hbar c/38.6 um", round(HBAR*C/38.6e-6/EV*1e3, 1) == 5.1)
check("the two-sided |alpha95| column gives the stronger 35.8 um at alpha = 4/3", round(crossing(1, 4/3)*1e6, 1) == 35.8,
      f"{crossing(1, 4/3)*1e6:.2f} um")
cb = {cv: crossing(0, 4/3*cv**2) for cv in (0.5, 0.8, 1.5)}
check("for background ratio u (alpha = 4u^2/3; c in the cited papers): 57.0 um at u = 0.5, 42.5 at 0.8, 30.8 at 1.5",
      [round(cb[cv]*1e6, 1) for cv in (0.5, 0.8, 1.5)] == [57.0, 42.5, 30.8], f"{[round(cb[cv]*1e6, 2) for cv in cb]}")
def alpha_at(lam_m):
    lmm = lam_m*1e3
    for (l1_, a1, _), (l2_, a2, _) in zip(TAB, TAB[1:]):
        if l1_ <= lmm <= l2_:
            return exp(log(a1) + log(lmm/l1_)/log(l2_/l1_)*log(a2/a1))
c_crit = [sqrt(3*alpha_at(sqrt(L_P*L))/4) for L in (L_H, CHI)]
check("X at the self-dual length survives only for u < 0.67 (47.1 um) or u < 0.30 (84.0 um)",
      [round(x, 2) for x in c_crit] == [0.67, 0.30], f"{[round(x, 4) for x in c_crit]}")
cc, q0, q1, q2 = sp.symbols('c beta0 beta1 beta2', real=True)
Lg = q0 + 3*q1*cc + 3*q2*cc**2 + q1*cc**3                    # palindrome: beta3 = beta1, beta4 = beta0
Lf = (q1*cc + 3*q2*cc**2 + 3*q1*cc**3 + q0*cc**4)/cc**2
quad = q1*cc**2 + (3*q2 - q0)*cc + q1
check("proportional backgrounds of the palindromic theory: u(u - 1)(u + 1)(beta1 u^2 + (3 beta2 - beta0) u + beta1) = 0",
      sp.simplify(sp.expand((Lg - Lf)*cc**2) - cc*(cc - 1)*(cc + 1)*quad) == 0)
def broken(v1, v2):
    qf = quad.subs({q0: -4*v1 - 3*v2, q1: v1, q2: v2})
    rts = [complex(z) for z in sp.Poly(qf, cc).nroots()]
    pos = [z.real for z in rts if abs(z.imag) < 1e-12 and z.real > 0]
    return [float(Lg.subs({q0: -4*v1 - 3*v2, q1: v1, q2: v2, cc: z}))/(2*(v1 + v2)) for z in pos]
inside = [broken(-1.0, 2.0), broken(-1.0, 5.0), broken(-0.5, 0.6)]
outside = [broken(1.0, 0.5), broken(1.0, -0.5), broken(-1.0, 0.9), broken(-1.0, 0.5)]
check("on the flat branch the symmetry-breaking pair (u, 1/u) exists only for beta1 < 0 < |beta1| < beta2 (sampled), "
      "with vacuum energy of order the spin-2 mass squared",
      all(len(x) == 2 and all(abs(v) > 0.1 for v in x) for x in inside) and all(len(x) == 0 for x in outside),
      f"{[[round(v, 3) for v in x] for x in inside]}")
check("so X at the self-dual length (47-84 um) is excluded, and M_X exceeds the dark-energy scale by 2.3x",
      all(sqrt(L_P*L) > LX for L in (L_H, L_L, CHI)) and round((HBAR*C/LX)/E14, 1) == 2.3)
z_ = sp.symbols('z')
vdvz = sp.Rational(1, 1) - sp.Rational(1, 3), sp.Rational(1, 1) - sp.Rational(1, 2)
check("(arithmetic of the cited propagators) the 4/3: massive (1 - 1/3) over massless (1 - 1/2) tensor structure",
      vdvz[0]/vdvz[1] == sp.Rational(4, 3))
r_V = (2*(2*G*1.0/C**2)*(50e-6)**2)**(1/3)              # (r_S (1 + alpha^2)/m^2)^(1/3), 1 kg, alpha = 1, range 50 um
check("Vainshtein radius of a 1 kg test mass for a 50 um range: about 1e-12 m", round(log10(r_V)) == -12,
      f"{r_V:.2e} m")
check("rho_(l_P) image of today's radiation rectangle: 1.0e-31 l_P across, momenta 5.4e61 m_P c",
      round(DP/P_P*1e32) == 10 and round(DX/L_P/1e60) == 54)
a, Cc, Mt, Mp = sp.symbols('a C Mt Mp', positive=True)
ad = sp.symbols('adot', real=True)
T1 = Mp**2*a*ad**2
T2 = Mt**2*Cc**3*ad**2/a**5
dual = {a: Cc/a, ad: -Cc*ad/a**2}                      # a -> C/a, with adot transformed at the same time
swap = sp.simplify((T1 + T2).subs(dual, simultaneous=True) - (T1 + T2))
swapped = sp.simplify(T1.subs(dual, simultaneous=True) - Mp**2*Cc**3*ad**2/a**5) == 0
eq_pt = sp.solve(sp.Eq(T1, T2.subs(Mt, Mp)), a)
check("a -> C/a exchanges M_P^2 a adot^2 and M~^2 C^3 adot^2/a^5 iff M~ = M_P; then they are equal at a = sqrt(C)",
      swapped and sp.simplify(swap.subs(Mt, Mp)) == 0 and sp.simplify(swap.subs(Mt, 2*Mp)) != 0 and
      eq_pt == [sp.sqrt(Cc)])
check("lever arm per radian at the Bohr momentum: 4.9e-60 m (lambda = l_P), 42 m (lambda = sqrt(l_P c/H0))",
      round(L_P**2/A_BOHR*1e61) == 49 and round(L_P*L_H/A_BOHR) == 42)

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — every number the phase-space-diameter note computes reproduces.")
