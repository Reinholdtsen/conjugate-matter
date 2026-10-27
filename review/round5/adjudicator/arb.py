#!/usr/bin/env python3
"""
arb.py — round-5 arbitration for papers/phase-space-diameter.md v1.0.

    .venv/bin/python review/round5/adjudicator/arb.py > review/round5/adjudicator/arb.out

Each block arbitrates one referee finding (A = referee A, B = referee B; the
numbering follows review/round5-adjudication.md). Inputs as in
verify/phase_space_diameter.py: CODATA 2018, Planck 2018, T0 = 2.7255 K, three
massless neutrinos, flat. The torsion-balance rows are typed in from J. G. Lee,
PhD thesis (University of Washington, 2020), Table 11.4, as retrieved for the
note: lambda in mm, then the one-sided +alpha95 and the two-sided |alpha95|.
"""
from math import pi, sqrt, log, log10, exp
import mpmath as mp
import sympy as sp

HBAR = 6.62607015e-34/(2*pi); C = 299792458.0; G = 6.67430e-11; KB = 1.380649e-23; EV = 1.602176634e-19
L_P = sqrt(HBAR*G/C**3); M_P = sqrt(HBAR*C/G); P_P = M_P*C; E_P = M_P*C**2; T_P = E_P/KB
MPC = 3.0856775814913673e22; H0 = 67.4e3/MPC; OM = 0.315; T0 = 2.7255; ZETA3 = 1.2020569031595942
G_S0 = 2 + (7/8)*6*(4/11); G_S_SM = 106.75
RHO_CRIT = 3*H0**2/(8*pi*G)
OR = (pi**2/15)*(KB*T0)**4/(HBAR*C)**3/C**2*(1 + 3*(7/8)*(4/11)**(4/3))/RHO_CRIT
OL = 1 - OM - OR
E = lambda a: sqrt(OR/a**4 + OM/a**3 + OL)
CHI = C/H0*float(mp.quad(lambda a: 1/(a**2*E(float(a))), [0, 1e-6, 1e-4, 1e-2, 1]))
L_H, L_L = C/H0, C/(H0*sqrt(OL))
MEAN_X = pi**4/(30*ZETA3)
S0 = (2*pi**2/45)*G_S0*(KB*T0/(HBAR*C))**3
DX, DP = 2*CHI, 2*MEAN_X*KB*T0/C
A0 = (DX/L_P)/(DP/P_P)
gfac = (G_S0/G_S_SM)**(1/3)

TAB = [  # Lee 2020 thesis, Table 11.4: lambda [mm], +alpha95, |alpha95|
    (0.025, 7.9, 6.4), (0.028, 4.51, 3.73), (0.032, 2.56, 2.08), (0.035, 1.77, 1.45),
    (0.040, 1.06, 0.877), (0.045, 0.699, 0.585), (0.050, 0.494, 0.419), (0.056, 0.35, 0.3),
    (0.063, 0.251, 0.218), (0.071, 0.183, 0.162), (0.079, 0.14, 0.126), (0.089, 0.106, 0.097),
    (0.100, 0.0813, 0.0766)]
def lam_bound(alpha, col=0):
    """range [m] at which the column reaches alpha (log-log interpolation)"""
    for (l1, *a1), (l2, *a2) in zip(TAB, TAB[1:]):
        y1, y2 = a1[col], a2[col]
        if (y1 - alpha)*(y2 - alpha) <= 0:
            t = log(y1/alpha)/log(y1/y2)
            return exp(log(l1) + t*log(l2/l1))*1e-3
    return None
def alpha_at(lam_m, col=0):
    """the column's value at range lam_m (log-log interpolation)"""
    lmm = lam_m*1e3
    for (l1, *a1), (l2, *a2) in zip(TAB, TAB[1:]):
        if l1 <= lmm <= l2:
            t = log(lmm/l1)/log(l2/l1)
            return exp(log(a1[col]) + t*log(a2[col]/a1[col]))
    return None

print("== A1/B1 (major): the background ratio c in alpha = (4/3)(M_f c/M_g)^2")
c, b0, b1, b2 = sp.symbols('c beta0 beta1 beta2', real=True)
b3, b4 = b1, b0                                              # palindrome beta_n = beta_{4-n}
# Hassan-Rosen proportional backgrounds f = c^2 g, equal Planck masses (units m^4/M^2 = 1):
Lg = b0 + 3*b1*c + 3*b2*c**2 + b3*c**3
Lf = (b1*c + 3*b2*c**2 + 3*b3*c**3 + b4*c**4)/c**2
bg = sp.factor(sp.expand((Lg - Lf)*c**2))
print("  background equation (Lambda_g - Lambda_f) c^2 =", bg)
quad = b1*c**2 + (3*b2 - b0)*c + b1
print("  factor check:", sp.simplify(bg - c*(c - 1)*(c + 1)*quad) == 0)
flat = {b0: -4*b1 - 3*b2}                                    # the program's flat aligned vacuum, T = 0
qf = sp.expand(quad.subs(flat))
print("  with the program's flat aligned vacuum (beta0 = -4 beta1 - 3 beta2): broken vacua solve", qf, "= 0")
print("  real positive roots c != 1 need beta1 < 0 and beta2 > |beta1| (with M_X^2 ~ beta1 + beta2 > 0):")
for (v1, v2) in [(1.0, 0.5), (1.0, -0.5), (-1.0, 0.5), (-1.0, 2.0), (-1.0, 5.0)]:
    roots = [complex(r) for r in sp.Poly(qf.subs({b1: v1, b2: v2}), c).nroots()]
    pos = [r.real for r in roots if abs(r.imag) < 1e-12 and r.real > 0]
    lam_vac = [float((Lg.subs(flat)).subs({b1: v1, b2: v2, c: r})) for r in pos]
    mfp = 2*(v1 + v2)
    print(f"    beta1 = {v1:+.1f}, beta2 = {v2:+.1f}: positive broken roots {[round(r, 4) for r in pos]}; "
          f"Lambda_g there / (m_FP^2 scale 2(beta1+beta2) = {mfp:+.1f}) = {[round(L/mfp, 3) for L in lam_vac] if mfp else '-'}")
print("  -> where the broken (c, 1/c) vacua exist they carry Lambda_g of the order of the spin-2 mass squared;")
mx = HBAR*C/37.68e-6
print(f"     for M_X c^2 >= {mx/EV*1e3:.2f} meV that is (M_X/H0)^2 = {(mx/(HBAR*H0))**2:.2e} times H0^2: excluded.")
print("     Only the aligned point c = 1 has zero wedge vacuum energy (the palindrome identity).")
print("  the bound as a function of c, from the one-sided +alpha95 column at alpha = (4/3) c^2:")
for cv in (0.5, 0.67, 0.8, 1.0, 1.25, 1.5):
    lb = lam_bound(4/3*cv**2)
    print(f"    c = {cv:4.2f}: alpha = {4/3*cv**2:.3f}, lambda_X < {lb*1e6:5.1f} um, M_X c^2 > {HBAR*C/lb/EV*1e3:.2f} meV")
for L, name in [(L_H, "c/H0"), (CHI, "particle horizon")]:
    lam = sqrt(L_P*L)
    a_need = alpha_at(lam)
    print(f"  X at sqrt(l_P L) = {lam*1e6:.1f} um ({name}) is allowed iff alpha < {a_need:.3f}, i.e. c < {sqrt(3*a_need/4):.3f}")
print("  referee A's identification c = a~/a: the record's second frame is f = E0[J], the polarization frame on the")
print("  compact moduli space, with the vacuum at the aligned point X = sqrt(g^-1 f) = 1 (notes/debt1a-iii §4,")
print("  notes/debt1a-iv §1-2). a~ belongs to the slaved block g~ = g^-1, a different object, so c0 = a~0/a0 does not follow.")

print("\n== A2/B2: the per-axis counts 'hold at no other epoch'")
S_obs = S0*4*pi/3*CHI**3
S_dS = pi*L_L**2/L_P**2
print(f"  fixed comoving region against S_dS: S^(1/3)/S_dS^(1/4) = {S_obs**(1/3)/S_dS**0.25:.3f}, constant (both counts conserved)")
gs = G_S_SM
for gstar in (106.75, 10.75, 3.36):
    # radiation-era Hubble sphere, Planck units: H = sqrt(8 pi^3 g/90) T^2, s = (2 pi^2/45) g T^3
    T = sp.symbols('T', positive=True)
    Hh = sp.sqrt(8*sp.pi**3*gstar/90)*T**2
    S_rad = (2*sp.pi**2/45)*gstar*T**3*sp.Rational(4, 3)*sp.pi/Hh**3
    S_BH = sp.pi/Hh**2
    r = sp.simplify(S_rad**sp.Rational(1, 3)/S_BH**sp.Rational(1, 4))
    r34 = sp.simplify(S_rad/S_BH**sp.Rational(3, 4))
    print(f"  Hubble sphere, radiation era, g = {gstar}: S^(1/3)/S_BH^(1/4) = {float(r):.3f}, S/S_BH^(3/4) = {float(r34):.3f}, "
          f"both independent of T: {sp.diff(r, T) == 0 and sp.diff(r34, T) == 0}")
print("  -> CKN's S_max ~ S_BH^(3/4) (their eq. 3) is the reason the two kinds of count agree for radiation.")

print("\n== A3: the one-cell row")
print(f"  a cell of wavelength w and momentum hbar/w has area hbar = {1/(2*pi):.3f} h; with momentum h/w (de Broglie), area h")

print("\n== A6/B4: the TeV numerology")
lam2 = L_P*L_L
a_free = sqrt(lam2*DP/(HBAR*DX))
T_free = KB*T0/a_free
a_sm = sqrt(gfac*lam2*DP/(HBAR*DX)); T_sm = gfac*KB*T0/a_sm
print(f"  square in units of sqrt(l_P L_Lambda): kT = {T_free/(1e12*EV):.3f} TeV (photons alone), {T_sm/(1e12*EV):.3f} TeV (SM g_s)")
print(f"  sqrt(k T0 E_P) = {sqrt(KB*T0*E_P)/(1e12*EV):.3f} TeV; BHM-type sqrt(rho_L^(1/4) E_P) = "
      f"{sqrt((OL*RHO_CRIT*C**2*(HBAR*C)**3)**0.25*E_P)/(1e12*EV):.2f} TeV")

print("\n== A7/B3: the exponent")
lam_lp = sqrt(lam2)/L_P
print(f"  log10(Lambda l_P^2) = {log10(3*L_P**2/L_L**2):.2f}; log10(lambda/l_P) = {log10(lam_lp):.2f}; "
      f"log10(L_Lambda/l_P) = {log10(L_L/L_P):.2f}: a quarter of the first, half of the third")

print("\n== A9: CKN conventions, ratio to hbar c/sqrt(l_P L)")
for name, f in [("CKN literal, unreduced M_P", 1.0), ("reduced Planck mass", (8*pi)**-0.25),
                ("sphere of radius L, M_BH = L c^2/2G", (3/(8*pi))**0.25), ("cube of side L, r_s = L", 0.5**0.25),
                ("sphere, one scalar's zero-point energy Lambda^4/16 pi^2", (6*pi)**0.25)]:
    print(f"  {name}: {f:.4f}")

print("\n== B9: the two columns of the exclusion table")
for a in (1.0, 4/3, 8/3):
    print(f"  alpha = {a:.3f}: one-sided +alpha95 {lam_bound(a, 0)*1e6:.2f} um, two-sided |alpha95| {lam_bound(a, 1)*1e6:.2f} um")
print("  -> the published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3) are reproduced by the |alpha95| column;")
print("     the note's 37.7 um is the +alpha95 column at 4/3 (more conservative than the |alpha95| 35.8 um).")

print("\n== B10: readings of the withdrawn claim")
for r in (100.0, 105.9, 120.0):
    print(f"  squeezed mode, r = {r}: aspect e^(2r) = 10^{2*r/log(10):.1f}")
s = sp.symbols('s', real=True)
Y = sp.sech(s)
print("  on |Z| = 1 with Im Z = sech s: with a^2 = Im Z (the record) the apex s = 0 is a maximum of a;",
      "with Im Z ~ a^-2 (section 5's wave-packet convention) it is a minimum of a:",
      sp.solve(sp.diff(Y, s), s) == [0] and sp.diff(Y, s, 2).subs(s, 0) < 0 and sp.diff(1/sp.sqrt(Y), s, 2).subs(s, 0) > 0)
for TGeV in (1e17,):
    TK = TGeV*1e9*EV/KB
    print(f"  radiation rectangle at a string-scale bounce, kT = {TGeV:.0e} GeV: A = {A0*(T0/TK)**2*gfac:.1e}")

print("\n== Referee A, unverifiable: Born's b")
r_e = 2.8179403262e-15
b = 6.62607015e-34/(pi*r_e)
print(f"  b = h/(pi r0) = {b*1e5:.3e} g cm/s (Born eq. 26 prints 7.43e-15); b c = {b*C/EV:.3e} eV = 2 hbar c/r0")
