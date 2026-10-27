"""Referee B: computations behind the conceptual audit (Step 4).

A. Squeezed-mode reading of the withdrawn claim: e^{2r} for literature r values.
B. Section 4 claim "it holds at no other epoch": per-axis counts under three readings, vs redshift.
C. Scale-factor-duality / Section 8.4 reading: is the self-dual step a bounce? single-cell square temperature.
D. |Z| = 1 circle under the manuscript's own slice convention (Im Z ~ a^-2).
E. Bimetric premise: background equation with symmetric couplings; alpha_eff = (4/3) c^2; bound vs c.
F. Born 1938: b = h/(pi r0) -> b c.
Inputs: CODATA 2018, Planck 2018 (H0 = 67.4, Om = 0.315), T0 = 2.7255 K, N_eff = 3.046.
"""
import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 25
c = mp.mpf('299792458'); hbar = mp.mpf('1.054571817e-34'); kB = mp.mpf('1.380649e-23')
G = mp.mpf('6.67430e-11'); eV = mp.mpf('1.602176634e-19'); Mpc = mp.mpf('3.0856775814913673e22')
lP = mp.sqrt(hbar * G / c**3); mP = mp.sqrt(hbar * c / G); TP = mP * c**2 / kB; EP = mP * c**2
H0 = mp.mpf('67.4') * 1e3 / Mpc; Om = mp.mpf('0.315'); T0 = mp.mpf('2.7255'); Neff = mp.mpf('3.046')
rho_g = (mp.pi**2 / 15) * (kB * T0)**4 / (hbar * c)**3
rho_c = 3 * H0**2 * c**2 / (8 * mp.pi * G)
Og = rho_g / rho_c; Or = Og * (1 + mp.mpf(7) / 8 * (mp.mpf(4) / 11)**(mp.mpf(4) / 3) * Neff); OL = 1 - Om - Or
Hof = lambda a: H0 * mp.sqrt(Or / a**4 + Om / a**3 + OL)
zeta3 = mp.zeta(3)
gs0 = 2 + mp.mpf(7) / 8 * 2 * 3 * mp.mpf(4) / 11

print('=== A. Squeezed-mode reading ===')
for r in [50, 100, 105.9, 110, 120]:
    print(f'  r = {r:6.1f}: e^(2r) = 10^{float(2 * r / mp.log(10)):.1f}; Siegel distance 2r = {2 * r:.1f}')
print(f'  r giving aspect ratio 10^92: {float(92 * mp.log(10) / 2):.2f}  (literature today: ~100 [KP09, KPS98], ~120 [Gr93])')
print(f'  manuscript radiation-rectangle value: ln A0 = 213.5 -> equivalent r = {213.5 / 2:.2f}')

print('\n=== B. Section 4: per-axis counts, chat (S_rad^(1/3)) vs FKGLM (N^(1/4)) ===')
n_g0 = (2 * zeta3 / mp.pi**2) * (kB * T0 / (hbar * c))**3
s_per_g = 2 * mp.pi**4 / (45 * zeta3) * gs0 / 2  # photons+neutrinos entropy per photon today


def chi(a_lo, a_hi):  # comoving distance integral c * int da/(a^2 H)
    return c * mp.quad(lambda a: 1 / (a**2 * Hof(a)), [a_lo, a_hi])


R_obs0 = chi(mp.mpf(0), 1)
S_rad_fixed = s_per_g * n_g0 * 4 * mp.pi / 3 * R_obs0**3
S_dS = mp.pi * (c / (H0 * mp.sqrt(OL)) / lP)**2
print(f'  Reading A (fixed comoving region, fixed Lambda): ratio = {float(S_rad_fixed**(mp.mpf(1)/3) / S_dS**(mp.mpf(1)/4)):.3f} at ALL epochs (both constant)')
print('  Reading B (epoch-dependent: radiation entropy in the then-particle horizon vs Hubble-horizon entropy pi (c/H lP)^2)')
print('     z        T/T0      S_rad(PH)^(1/3)   S_H^(1/4)     ratio    kT/rho_L^(1/4)   kT/sqrt(M_P H)')
rho_L14 = (OL * rho_c * (hbar * c)**3)**(mp.mpf(1) / 4)
for z in [0, 1, 10, 100, 1100, 1e4, 1e6, 1e9]:
    a = 1 / (1 + mp.mpf(z))
    R_ph = a * chi(mp.mpf(0), a)  # proper particle-horizon radius (no g_s change below ~MeV; z <= 1e9 ok)
    S_rad = s_per_g * n_g0 / a**3 * 4 * mp.pi / 3 * R_ph**3
    H = Hof(a)
    S_H = mp.pi * (c / H / lP)**2
    kT = kB * T0 / a
    sqrtMH = mp.sqrt(EP * hbar * H)  # natural-units sqrt(M_P H)
    print(f'  {z:8.0e}  {float(1/a):9.3e}  {float(S_rad**(mp.mpf(1)/3)):14.3e}  {float(S_H**(mp.mpf(1)/4)):11.3e}  {float(S_rad**(mp.mpf(1)/3)/S_H**(mp.mpf(1)/4)):8.3f}  {float(kT/rho_L14):12.3e}  {float(kT/sqrtMH):12.3f}')
print('  Reading C (chat region fixed; FKGLM N at the then-Hubble scale): ratio = S_rad_fixed^(1/3)/S_H(z)^(1/4)')
for z in [0, 10, 1100, 1e6, 1e9]:
    a = 1 / (1 + mp.mpf(z))
    S_H = mp.pi * (c / Hof(a) / lP)**2
    print(f'     z = {z:8.0e}: ratio = {float(S_rad_fixed**(mp.mpf(1)/3) / S_H**(mp.mpf(1)/4)):.3e}')

print('\n=== C. Section 8.4 self-dual step as a candidate bounce ===')
# 3 H^2 (M^2 + M^2 C^3 a^-6) = rho_r a^-4 (+ optional dual radiation rho_r a^4/C^4); units M = 1, rho_r = 1
for Cv in [1.0]:
    for dual in [False, True]:
        f = lambda a: (a**-4 + (a**4 / Cv**4 if dual else 0)) / (3 * (1 + Cv**3 * a**-6))
        aa = np.logspace(-3, 3, 13)
        H2 = [f(x) for x in aa]
        print(f'  C={Cv}, dual radiation={dual}: min H^2 over a in [1e-3,1e3] = {min(H2):.3e} (>0: no H=0, so a is monotonic, no bounce)')
print('  max(a, C/a) is minimal at a = sqrt(C): a "bounce" only of the dominant-frame scale factor, not of a or a~.')
# single thermal cell (area h) square in Planck units: D_p = 2<p> = sqrt(2 pi) m_P c
meanp = mp.pi**4 / (30 * zeta3)
print(f'  single thermal cell (area h, D_p = 2<p>) square in Planck units at T = {float(mp.sqrt(2*mp.pi)/(2*meanp)):.3f} T_P')
kappa = 3**(mp.mpf(1)/3) * mp.pi**(mp.mpf(10)/3) / (30 * zeta3**(mp.mpf(4)/3))
N_g = n_g0 * 4 * mp.pi / 3 * R_obs0**3
Creg = 2 * mp.pi * kappa * N_g**(mp.mpf(1)/3)
print(f'  region-scale C (area per axis of the observable-universe rectangle in Planck units) = {float(Creg):.3e}; sqrt(C) = {float(mp.sqrt(Creg)):.3e}')

print('\n=== D. |Z|=1 circle under the slice convention Im Z ~ a^-2 ===')
s = sp.symbols('s', real=True)
Zc = sp.tanh(s) + sp.I * sp.sech(s)
Yc = sp.simplify(sp.im(Zc))
print('  |Z|^2 on the circle =', sp.simplify(sp.tanh(s)**2 + sp.sech(s)**2))
print('  Y = sech s; record convention a^2 = Y -> a max at s=0 (turnaround);  slice convention a^2 ~ 1/Y = cosh s -> a MIN at s=0 (bounce)')
print('  d^2(cosh s)/ds^2 at 0 =', sp.diff(sp.cosh(s), s, 2).subs(s, 0), '(>0: minimum)')

print('\n=== E. Bimetric background with g<->f symmetric couplings (M_f = M_g, beta_n = beta_{4-n}) ===')
cc, b0, b1, b2 = sp.symbols('c beta0 beta1 beta2')
alpha2 = 1  # (M_f/M_g)^2
beta = {0: b0, 1: b1, 2: b2, 3: b1, 4: b0}
lhs = alpha2 * (cc * beta[0] + 3 * cc**2 * beta[1] + 3 * cc**3 * beta[2] + cc**4 * beta[3])
rhs = beta[1] + 3 * cc * beta[2] + 3 * cc**2 * beta[3] + cc**3 * beta[4]
print('  background equation (Luben et al. eq. 5) factorises as:', sp.factor(sp.expand(lhs - rhs)))
print('  -> c = 1 (symmetric vacuum) or roots of beta1 c^2 + (3 beta2 - beta0) c + beta1 = 0, a (c, 1/c) pair (broken vacua)')
# Yukawa strength for matter on g: alpha_Y = (4/3) (M_f/M_g)^2 c^2 ; bound from thesis Table 11.4 (+alpha95 column)
lam_um = np.array([25, 28, 32, 35, 40, 45, 50, 56, 63, 71, 79, 89, 100.0])
plus = np.array([7.9, 4.51, 2.56, 1.77, 1.06, 0.699, 0.494, 0.35, 0.251, 0.183, 0.14, 0.106, 0.0813])


def lam_max(alpha):
    la, lp = np.log(lam_um), np.log(plus)
    if alpha >= plus[0] or alpha <= plus[-1]:
        return float('nan')
    return float(np.exp(np.interp(np.log(alpha), lp[::-1], la[::-1])))


for cv in [0.5, 0.6, 0.67, 0.8, 1.0, 1.25, 1.5, 2.0]:
    aY = 4 / 3 * cv**2
    lm = lam_max(aY)
    print(f'  c = {cv:4.2f}: alpha_Y = {aY:5.3f} -> lambda_X < {lm:5.1f} um, M_X c^2 > {float(hbar*c/eV/(lm*1e-6))*1e3:5.2f} meV')
# c at which the self-dual length 47.1 um becomes allowed
from scipy.optimize import brentq  # local venv
cstar = brentq(lambda cv: lam_max(4 / 3 * cv**2) - 47.1, 0.3, 1.0)
print(f'  the self-dual length 47.1 um (L = c/H0) is allowed for c < {cstar:.3f} (alpha_Y < {4/3*cstar**2:.3f})')
cstar2 = brentq(lambda cv: lam_max(4 / 3 * cv**2) - 84.0, 0.26, 0.9)
print(f'  84.0 um (particle horizon) is allowed for c < {cstar2:.3f} (alpha_Y < {4/3*cstar2**2:.3f})')

print('\n=== F. Born 1938: b = h/(pi r0) ===')
r0 = mp.mpf('2.8179403262e-15')
b = 2 * mp.pi * hbar / (mp.pi * r0)
print(f'  b = {float(b*1e5):.3e} g cm/s (Born 1938 eq. 26: 7.43e-15); b c = {float(b*c/eV):.3e} eV (Born eq. 37: 1.41e8 eV)')
