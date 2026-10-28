"""Critic, tension (a): the reciprocity-symmetric dual-curvature reading in a convention-free form.

Minisuperspace analyst: closure units a = R/lambda, a*atilde = C (C_ms).
Momentum-space analyst: a0 = 1 today, a*atilde = C (C_mom), dual comoving radius = ours.
Both use L = 3M_P^2[-a adot^2 + k a] + v 3Mt^2[-at atdot^2 + kt at], at = C/a.

Symmetric reading: v Mt^2 = M_P^2, kt = k (same comoving curvature in the chosen units).
Claim to test [D]: then, as functions of the PHYSICAL radius R,
   eps6(R)  = (a^-6 term)/M_P^2        = (R_sd/R)^6
   r(R)     = (dual curvature)/(ours)   = (R_sd/R)^2
with one length R_sd (the self-dual radius), and
   C_ms = (R_sd/lambda)^2,  C_mom = (R_sd/R0)^2.
The dual S^3 has momentum radius P = hbar R_sd^2/(lambda^2 R) (via rho_lambda),
so the antipodal cap is n <= pi R_sd^2/lambda^2 (mode index n = p R/hbar, constant in time).
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
print("=== (1) symbolic: both conventions give eps6 = (R_sd/R)^6 and r = (R_sd/R)^2 ===")
R, lam, R0, C, Mp = sp.symbols('R lambda R0 C M_P', positive=True)
# generic: our comoving unit ell (a = R/ell, k = 1/ell^2 in units where a is dimensionless and
# the comoving metric has curvature 1 in units of ell); at = C/a
ell = sp.symbols('ell', positive=True)
a = R/ell
eps6 = C**3/a**6                      # (v Mt^2 C^3 a^-6)/M_P^2 with v Mt^2 = M_P^2
r = C/a**2                            # (3 v Mt^2 kt C/a^4)/(3 M_P^2 k/a^2) with kt = k
Rsd = sp.sqrt(C)*ell
print("eps6 - (Rsd/R)^6 =", sp.simplify(eps6 - (Rsd/R)**6))
print("r    - (Rsd/R)^2 =", sp.simplify(r - (Rsd/R)**2))
print("minisuperspace convention ell = lambda: C_ms = (R_sd/lambda)^2; C_ms = 1 <=> R_sd = lambda")
print("momentum-space convention ell = R0    : C_mom = (R_sd/R0)^2;   C_mom = 1 <=> R_sd = R0")
# momentum cap: dual sphere physical radius (length units) = at * ell_dual; in ms convention
# at is measured in hbar/lambda: P = at*hbar/lambda = C lambda/R * hbar/lambda = C hbar/R
P_ms = C*sp.Symbol('hbar')/R
P_from_Rsd = sp.Symbol('hbar')*(Rsd.subs(ell, lam))**2/(lam**2*R)
print("cap: P_ms - hbar R_sd^2/(lambda^2 R) =", sp.simplify(P_ms - P_from_Rsd.subs(C, C)))
# mom convention: dual frame comoving radius R0, scale at = C/a, physical length C R0/a,
# read as momentum through rho_lambda: P = hbar * C R0/a / lambda^2 with a = R/R0
P_mom = sp.Symbol('hbar')*C*R0/(R/R0)/lam**2
print("cap: P_mom - hbar R_sd^2/(lambda^2 R) =",
      sp.simplify(P_mom - sp.Symbol('hbar')*(sp.sqrt(C)*R0)**2/(lam**2*R)))
print("=> one physical point per (lambda, R_sd); 'C = 1' names R_sd = lambda (ms) or R_sd = R0 (mom).")

print()
print("=== (2) numbers ===")
c = mp.mpf(299792458); hbar = mp.mpf('1.054571817e-34'); G = mp.mpf('6.67430e-11')
eV = mp.mpf('1.602176634e-19'); kB = mp.mpf('1.380649e-23'); Mpc = mp.mpf('3.0856775814913673e22')
lP = mp.sqrt(hbar*G/c**3)
hbarc_eVm = hbar*c/eV
H0 = 67.4e3/Mpc
T0 = mp.mpf('2.7255'); T0eV = kB*T0/eV
cH0 = c/H0
gs0 = mp.mpf('3.909')
a_bbn = (T0eV/mp.mpf('1e6'))*(gs0/mp.mpf('10.75'))**(mp.mpf(1)/3)
Einf = mp.mpf('1.39e25')       # eV (1.39e16 GeV, the record's inflation-scale bound)
gstar = mp.mpf('106.75')
Trh = Einf*(30/(mp.pi**2*gstar))**(mp.mpf(1)/4)
a_end = (T0eV/Trh)*(gs0/gstar)**(mp.mpf(1)/3)
Omega_nu1 = mp.mpf('1.23632e-05')   # one neutrino species, h = 0.674 (momentum-space verifier)
lam2 = mp.sqrt(lP*cH0)
print(f"l_P = {mp.nstr(lP,6)} m; lambda2 = sqrt(l_P c/H0) = {mp.nstr(lam2,6)} m; a_BBN = {mp.nstr(a_bbn,5)}; a_end = {mp.nstr(a_end,5)}")

def nmode(p_eV, R0m):
    return p_eV*R0m/hbarc_eVm

for Ok in ['1e-2', '1e-3', '1e-4', '1e-5']:
    Ok = mp.mpf(Ok)
    R0m = cH0/mp.sqrt(Ok)
    R_bbn = a_bbn*R0m
    R_end = a_end*R0m
    n_cmb = mp.mpf('2.70118')*T0eV*R0m/hbarc_eVm
    n_lhc = nmode(mp.mpf('6.8e12'), R0m)
    n_uhe = nmode(mp.mpf('3.2e20'), R0m)
    print(f"\n|Omega_k| = {mp.nstr(Ok,2)}: R0 = {mp.nstr(R0m,5)} m, R(1 MeV) = {mp.nstr(R_bbn,4)} m, R_end = {mp.nstr(R_end,4)} m")
    # upper bounds on R_sd
    up_bbn10 = mp.mpf('0.1')**(mp.mpf(1)/6)*R_bbn
    up_bbn64 = mp.mpf('0.064')**(mp.mpf(1)/6)*R_bbn
    up_neff = R0m*mp.sqrt(mp.mpf('4.871e-6')/Ok)
    print(f"  R_sd upper: BBN (eps6<=0.1) {mp.nstr(up_bbn10,4)} m; BBN (Alvey eps6<=0.064) {mp.nstr(up_bbn64,4)} m;"
          f" N_eff (|Omega_kt|<4.871e-6) {mp.nstr(up_neff,4)} m")
    for N in [50, 55, 60]:
        print(f"  R_sd upper, standard inflation (R_sd < R at pivot exit, N_* = {N}): {mp.nstr(R_end*mp.e**(-N),4)} m")
    # the two 'C = 1' points
    for name, Rsd in [('ms C=1, lambda=l_P (R_sd = l_P)', lP), ('mom C=1 (R_sd = R0)', R0m)]:
        dneff = -(Rsd/R0m)**2*Ok/Omega_nu1
        e6b = (Rsd/R_bbn)**6
        ncap_lP = mp.pi*(Rsd/lP)**2
        print(f"  {name}: Delta N_eff = {mp.nstr(dneff,4)}; eps6(1 MeV) = {mp.nstr(e6b,4)};"
              f" cap n_max (lambda = l_P) = {mp.nstr(ncap_lP,4)} vs n_CMB = {mp.nstr(n_cmb,4)}")
    # surviving lambda
    for nname, n in [('CMB photons', n_cmb), ('LHC 6.8 TeV', n_lhc), ('UHECR 3.2e20 eV', n_uhe)]:
        lam_late = up_bbn10*mp.sqrt(mp.pi/n)
        lam_inf = R_end*mp.e**(-55)*mp.sqrt(mp.pi/n)
        print(f"  cap from {nname} (n = {mp.nstr(n,4)}): R_sd >= lambda sqrt(n/pi); survives N_eff+BBN iff lambda <= {mp.nstr(lam_late,4)} m;"
              f" + standard inflation (N_*=55) iff lambda <= {mp.nstr(lam_inf,4)} m = {mp.nstr(lam_inf/lP,4)} l_P")
    for lname, L in [('l_P', lP), ('lambda2', lam2)]:
        lo = L*mp.sqrt(n_lhc/mp.pi)
        lo_c = L*mp.sqrt(n_cmb/mp.pi)
        print(f"  lambda = {lname}: R_sd window (LHC cap .. BBN) = [{mp.nstr(lo,4)}, {mp.nstr(up_bbn10,4)}] m -> "
              f"{'open' if lo < up_bbn10 else 'EMPTY'}; inflation needs R_sd < {mp.nstr(R_end*mp.e**(-55),3)} m, "
              f"CMB-photon cap alone already needs R_sd >= {mp.nstr(lo_c,4)} m -> "
              f"{'compatible' if lo_c < R_end*mp.e**(-55) else 'a^-6 term dominates at pivot exit'}")
