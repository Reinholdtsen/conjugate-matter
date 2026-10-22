"""Independent recomputation for flag 28 (#11 sec. 11.2):
   "Dirac's condition e*g ~ 2*pi pins the magnetic coupling near 4*pi/e^2 ~ 34".

Does not use review/wiki-build-checks/dirac_coupling_check.py.

A. Derive Dirac's condition from the Wu-Yang two-patch construction, in
   Heaviside-Lorentz (HL) and in Gaussian units, with sympy.
B. Define the couplings physically and unit-independently:
   alpha   = F_ee r^2/(hbar c)  (two elementary electric charges),
   alpha_m = F_gg r^2/(hbar c)  (two minimal monopoles),
   and show alpha * alpha_m = 1/4 at the Dirac minimum in both unit systems.
C. Evaluate the source's expression 4*pi/e^2 in each unit system.
D. Find which normalization of e*g makes 4*pi/e^2 the magnetic coupling.
E. The one rescue reading: e = twice the smallest charge.
F. Montonen-Olive / S-duality check (tau -> -1/tau).
"""
import sympy as sp

r, th, ph = sp.symbols('r theta phi', positive=True)
e, g, hbar, c = sp.symbols('e g hbar c', positive=True)
n = sp.symbols('n', integer=True)

def curl_phi_only(Aphi):
    """Curl of A = Aphi(r,theta) phi_hat in spherical coordinates -> (B_r, B_theta, B_phi)."""
    Br = sp.simplify(sp.diff(sp.sin(th) * Aphi, th) / (r * sp.sin(th)))
    Bth = sp.simplify(-sp.diff(r * Aphi, r) / r)
    return Br, Bth, sp.Integer(0)

print("=== A. Dirac's condition from Wu-Yang patches ===")
for units, pref in [("HL (hbar=c=1)", 1 / (4 * sp.pi)), ("Gaussian", sp.Integer(1))]:
    AN = pref * g * (1 - sp.cos(th)) / (r * sp.sin(th))      # north patch, regular at theta=0
    AS = -pref * g * (1 + sp.cos(th)) / (r * sp.sin(th))     # south patch, regular at theta=pi
    BrN, BthN, _ = curl_phi_only(AN)
    BrS, BthS, _ = curl_phi_only(AS)
    flux = sp.integrate(sp.integrate(BrN * r**2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
    # A_N - A_S = grad(chi), chi = k*phi: (grad chi)_phi = k/(r sin theta)
    diff_phi = sp.simplify(AN - AS)
    k = sp.simplify(diff_phi * r * sp.sin(th))               # chi = k * phi
    print(f"[{units}] B_r = {BrN}  (south patch gives {BrS}); B_theta = {BthN}")
    print(f"[{units}] total flux through a sphere = {sp.simplify(flux)}")
    print(f"[{units}] A_N - A_S = grad(chi) with chi = ({k}) * phi")
    if units.startswith("HL"):
        # covariant derivative D = d - i e A; psi_N = exp(i e chi) psi_S
        phase_coeff = e * k            # exp(i * phase_coeff * phi) must be single valued
        cond = sp.solve(sp.Eq(phase_coeff, n), g)
        print(f"[{units}] single-valued exp(i e chi): e*g/(2pi) = n  ->  g = {cond[0]}  ->  e*g = {sp.simplify(e*cond[0])}")
        g_HL = sp.simplify(cond[0].subs(n, 1))
    else:
        phase_coeff = e * k / (hbar * c)
        cond = sp.solve(sp.Eq(phase_coeff, n), g)
        print(f"[{units}] single-valued exp(i e chi/(hbar c)): 2 e g/(hbar c) = n  ->  g = {cond[0]}  ->  e*g = {sp.simplify(e*cond[0])}")
        g_G = sp.simplify(cond[0].subs(n, 1))

print()
print("=== B. Physical couplings (Coulomb force between like charges, F r^2/(hbar c)) ===")
# HL (hbar=c=1): F_ee = e^2/(4 pi r^2);  monopoles F_gg = g * B = g^2/(4 pi r^2)
alpha_HL = e**2 / (4 * sp.pi)
alpham_HL = g_HL**2 / (4 * sp.pi)
print(f"HL:       alpha = {alpha_HL},  minimal g = {g_HL},  alpha_m = g^2/(4pi) = {sp.simplify(alpham_HL)}")
print(f"HL:       alpha * alpha_m = {sp.simplify(alpha_HL * alpham_HL)}")
# Gaussian: F_ee = e^2/r^2 ; F_gg = g * B = g^2/r^2
alpha_G = e**2 / (hbar * c)
alpham_G = g_G**2 / (hbar * c)
print(f"Gaussian: alpha = {alpha_G},  minimal g = {g_G},  alpha_m = g^2/(hbar c) = {sp.simplify(alpham_G)}")
print(f"Gaussian: alpha * alpha_m = {sp.simplify(alpha_G * alpham_G)}")

print()
print("=== numbers (alpha^-1 = 137.035999, CODATA, model memory; insensitive at shown digits) ===")
ainv = sp.Rational(137035999, 1000000)
a = 1 / ainv
eHL = sp.sqrt(4 * sp.pi * a)          # hbar=c=1
eG = sp.sqrt(a)                        # Gaussian, hbar=c=1
am = sp.N(1 / (4 * a), 8)
print(f"alpha_m at Dirac minimum = 1/(4 alpha) = {am}")

print()
print("=== C. The source's expression 4*pi/e^2, evaluated as written ===")
print(f"HL       (alpha = e^2/4pi): e = {sp.N(eHL, 6)},  4pi/e^2 = {sp.N(4*sp.pi/eHL**2, 8)},  pi/e^2 = {sp.N(sp.pi/eHL**2, 8)}")
print(f"Gaussian (alpha = e^2)    : e = {sp.N(eG, 6)},  4pi/e^2 = {sp.N(4*sp.pi/eG**2, 8)},  1/(4e^2) = {sp.N(1/(4*eG**2), 8)}")
print("Gaussian Dirac condition is e*g = 1/2 (hbar=c=1), so 'e*g ~ 2pi' is itself the HL form.")

print()
print("=== D. When is 4pi/e^2 the magnetic coupling g^2/4pi (HL)? ===")
sol = sp.solve(sp.Eq(g**2 / (4 * sp.pi), 4 * sp.pi / e**2), g)
print(f"g^2/(4pi) = 4pi/e^2  <=>  g = {sol}  i.e. e*g = {[sp.simplify(e*s) for s in sol]}  (Dirac n = 2, the Schwinger/'t Hooft-Polyakov normalization)")
print("Other candidate meanings of 'magnetic coupling' at the Dirac minimum g = 2pi/e (HL, e = electron):")
gmin = 2 * sp.pi / eHL
for label, expr in [("g", gmin), ("g^2", gmin**2), ("g^2/4pi", gmin**2/(4*sp.pi)),
                    ("g/e (g_D in units of e)", gmin/eHL), ("g^2/4pi at e*g = 4pi", (4*sp.pi/eHL)**2/(4*sp.pi))]:
    print(f"   {label:28s} = {sp.N(expr, 6)}")

print()
print("=== E. Rescue reading: e := gauge coupling = 2 x smallest charge (SU(2) doublets at e/2) ===")
emin = eHL                     # smallest charge = electron's
egauge = 2 * emin
gm = 4 * sp.pi / egauge        # 't Hooft-Polyakov charge relative to the gauge coupling
print(f"e_min*g_m = {sp.N(emin*gm, 6)} (= 2pi: {sp.simplify(emin*gm - 2*sp.pi) == 0}),  e_gauge*g_m = {sp.N(egauge*gm, 6)} (= 4pi: {sp.simplify(egauge*gm - 4*sp.pi) == 0})")
print(f"4pi/e_gauge^2 = {sp.N(4*sp.pi/egauge**2, 8)}  = g_m^2/4pi = {sp.N(gm**2/(4*sp.pi), 8)}")
print("-> the sentence holds only if its 'e' in e*g ~ 2pi is e_min and its 'e' in 4pi/e^2 is 2 e_min.")

print()
print("=== F. Montonen-Olive S-duality: tau = theta/2pi + 4 pi i/e^2, S: tau -> -1/tau, theta = 0 ===")
tau = sp.I * 4 * sp.pi / e**2
tauD = sp.simplify(-1 / tau)
eD = sp.symbols('e_D', positive=True)
eD_sol = sp.solve(sp.Eq(sp.im(tauD), 4 * sp.pi / eD**2), eD)
print(f"-1/tau = {tauD};  dual coupling e_D = {eD_sol};  alpha_D = e_D^2/4pi = {sp.simplify(eD_sol[0]**2/(4*sp.pi))}")
print(f"with e = electron (HL): alpha_D = {sp.N((eD_sol[0]**2/(4*sp.pi)).subs(e, eHL), 8)}")
