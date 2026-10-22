"""Audit of flag 31: #1 §4 "quadratic effects at M_B ~ M_P sit ~10 orders below current sensitivity".

Literature inputs, live-searched [S] this session (not from any program document):
  Vasileiou et al., PRD 87, 122001 (2013), arXiv:1305.3463, read from the paper's text:
    eq.(1)  E^2 ~= p^2 c^2 [1 - s (E/E_QG)^n]          (s = +1 subluminal)
    eq.(3)  tau_n = Dt/(E_h^n - E_l^n) ~= s (1+n)/(2 H0) kappa_n / E_QG^n
    eq.(4)  kappa_n = int_0^z (1+z')^n / sqrt(OL + OM (1+z')^3) dz'
    cosmology OM = 0.272, OL = 0.728, H0 = 73.8 km/s/Mpc; E_Pl = 1.22e19 GeV
    Table I  GRB 090510: z = 0.903, kappa_1 = 1.03, kappa_2 = 1.50
    Table III SMM, GRB 090510, n=2: tau_2 upper limit 0.85e-3 s GeV^-2 (99% two-sided)
    Table IV  SMM, GRB 090510, n=2, s=+1: E_QG,2 > 13e10 GeV (95%), 3.3e10 GeV (99.5%)
              ML,  GRB 090510, n=2, s=-1: E_QG,2 > 9.4e10 GeV (95%)
    Table V   averaged, with intrinsic lags allowed, 090510 n=2: 4.0e10 (s=+1), 3.0e10 (s=-1) GeV
  LHAASO, PRL 133, 071501 (2024), arXiv:2402.06009: E_QG,2 > 6e-8 E_Pl (95%, time of flight)
  LHAASO, arXiv:2106.12350 (photon decay, superluminal only): second-order scale > 1e-3 M_pl
The 31 GeV highest-energy photon of GRB 090510 is named in the paper's text.
"""
import math
import numpy as np
import sympy as sp

E_PL = 1.22e19                       # GeV, the paper's E_Pl
M_RED = E_PL / math.sqrt(8 * math.pi)  # reduced Planck mass; #1 uses this form (S_H = 1/2 M_B^2 int R; 3H^2 M_P^2 = rho)
print(f"reduced Planck mass = {M_RED:.4g} GeV")

# --- Anchor 1: the paper's kappa_n for GRB 090510 (independent of #1) ---
OM, OL, z = 0.272, 0.728, 0.903
zz = np.linspace(0.0, z, 200001)
def kappa(n):
    return np.trapezoid((1 + zz) ** n / np.sqrt(OL + OM * (1 + zz) ** 3), zz)
k1, k2 = kappa(1), kappa(2)
print(f"anchor: kappa_1 = {k1:.3f} (paper 1.03), kappa_2 = {k2:.3f} (paper 1.50)")

# --- Anchor 2: reproduce the paper's 99.5% E_QG,2 from its tau_2 limit (formula use, units) ---
MPC_KM = 3.0857e19
H0 = 73.8 / MPC_KM                   # s^-1
inv_H0 = 1 / H0
tau2_99 = 0.85e-3                    # s GeV^-2
EQG2_995 = math.sqrt(1.5 * inv_H0 * k2 / tau2_99)
print(f"anchor: E_QG,2 from tau_2 < 0.85e-3 s/GeV^2 = {EQG2_995:.3g} GeV (paper Table IV SMM 99.5%: 3.3e10)")

# --- Convention map: #1's E^2 = p^2 + xi p^4/M_B^2  vs  eq.(1) E^2 = p^2 [1 - s (E/E_QG)^2] ---
p, M, EQ = sp.symbols("p M E_QG", positive=True)
xi, s = sp.symbols("xi s", real=True)
v1 = sp.series(sp.diff(sp.sqrt(p**2 + xi * p**4 / M**2), p), p, 0, 4).removeO()
# eq.(2): v = 1 - s (3/2) (E/E_QG)^2 with E ~= p at this order
v_paper = 1 - s * sp.Rational(3, 2) * p**2 / EQ**2
sol = sp.solve(sp.Eq(sp.expand(v1 - 1), sp.expand(v_paper - 1)), xi)
print(f"group velocity from #1: {sp.simplify(v1)};  match to eq.(2) gives xi = {sol}  (so |xi| = (M_B/E_QG,2)^2)")

# --- Gaps for each bound and each Planck-mass convention ---
bounds = [
    ("Fermi-LAT 2013, 090510, s=+1, 95% (abstract)", 1.3e11),
    ("Fermi-LAT 2013, 090510, s=-1, 95% best (ML)", 9.4e10),
    ("Fermi-LAT 2013, Table V with intrinsic lags, s=+1", 4.0e10),
    ("Fermi-LAT 2013, Table V with intrinsic lags, s=-1", 3.0e10),
    ("LHAASO 2024 GRB 221009A time of flight, 95%", 6e-8 * E_PL),
    ("LHAASO photon decay, superluminal only", 1e-3 * E_PL),
]
print("\n  bound                                               E_QG,2 [GeV]   scale gap (E_Pl / reduced)   effect gap (E_Pl / reduced)")
for name, b in bounds:
    sg = (math.log10(E_PL / b), math.log10(M_RED / b))
    print(f"  {name:50s} {b:10.3g}      {sg[0]:5.2f} / {sg[1]:5.2f}                 {2*sg[0]:5.2f} / {2*sg[1]:5.2f}")

# --- The effect itself, in seconds: 31 GeV photon from GRB 090510 ---
E = 31.0
def delay(EQG):
    return 1.5 * inv_H0 * k2 * E**2 / EQG**2   # eq.(3) with E_l << E_h
for name, Mx in (("E_Pl", E_PL), ("reduced M_P", M_RED)):
    print(f"Planck-scale quadratic delay at 31 GeV, M_B = {name}: {delay(Mx):.3g} s; "
          f"delay at the 95% bound 1.3e11 GeV: {delay(1.3e11):.3g} s; ratio 10^{math.log10(delay(1.3e11)/delay(Mx)):.2f}")
# the linear Planck-scale delay of the same photon, for scale
print(f"linear delay at 31 GeV for E_QG,1 = E_Pl: {1.0*inv_H0*k1*E/E_PL:.3g} s")

# --- What would make "~10 orders" exact ---
for name, Mx in (("E_Pl", E_PL), ("reduced M_P", M_RED)):
    print(f"'10 orders' needs a bound of {Mx/1e10:.3g} GeV (scale reading) or {Mx/1e5:.3g} GeV (effect reading), M_B = {name}")
