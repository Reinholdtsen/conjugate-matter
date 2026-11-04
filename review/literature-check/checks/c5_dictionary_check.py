"""C5 judge: independent checks of the dictionary claims (not the g4 verifier's script).

Sources read for this script:
  #1 section 6 (notes/broken-born-theory.md): E = rho~ at~^3 enters our Hamiltonian constraint as E/a^3, at~ = 1/a.
  Gasperini-Veneziano 2003 (hep-th/0207130) sec. 2.2, eqs. (2.27)-(2.32), (2.35)-(2.38): string-frame equations with
    shifted variables rhobar = rho a^d, pbar = p a^d; duality a -> 1/a, phibar -> phibar, rhobar -> rhobar, pbar -> -pbar.
  Mukherjee-Jassal-Lochan 2024 (2207.02835) sec. 6, eqs. (46)-(47): Brans-Dicke w_BD = -4/3 de Sitter Jordan frame.

Checks:
  A. The program's rule gives w_eff = -w~, with our pressure taken from OUR continuity equation (no reflection assumed).
  B. GV's reflected pressure equals that pressure for any a(t): the two published maps agree (d = 3). Not by construction:
     A never reflects a pressure, B never uses our continuity equation.
  C. GV's string-frame power-law solutions: alpha(-gamma) = -alpha(gamma). The SFD partner of a stiff source (gamma = 1)
     is a ~ t^(-1/2) with gamma = -1: a power law with a running dilaton, not de Sitter.
  D. Einstein gravity without a dilaton: the same map does not take a Friedmann solution to a Friedmann solution;
     same-cosmic-time inversion of single-fluid solutions gives w -> -2 - w (phantom duality, the program's heuristic);
     same-conformal-time inversion gives w -> -2/3 - w (Camara da Silva et al.; Dark Gravity's kinematics).
  E. MJL sec. 6: Einstein-frame scale factor goes as a^(-1/2) at the same event, and eq. (47) is a contracting stiff
     FRW universe; the pairing is not a.at~ = 1.
  F. Which dual content gives our Lambda under each of the three inversions.
"""
import sympy as sp

t = sp.symbols("t", positive=True)
wt, w, C = sp.symbols("wt w C", real=True)

print("A. program rule (#1 sec. 6)")
at = sp.Function("at", positive=True)(t)          # conjugate scale factor, arbitrary
a = 1 / at
rho_t = C * at ** (-3 * (1 + wt))
E = rho_t * at**3
rho_eff = sp.simplify(E / a**3)
H = sp.diff(a, t) / a
p_eff = sp.simplify(-rho_eff - sp.diff(rho_eff, t) / (3 * H))   # our continuity: rho' + 3H(rho + p) = 0
w_eff = sp.simplify(p_eff / rho_eff)
print("   rho_eff =", rho_eff, "; p_eff/rho_eff from our continuity equation =", w_eff)
assert sp.simplify(w_eff + wt) == 0

print("B. GV eq. (2.32) applied to the conjugate solution, d = 3")
p_t = wt * rho_t
rhobar_conj = rho_t * at**3                       # (2.30)
pbar_conj = p_t * at**3
H_conj = sp.diff(at, t) / at
cont_conj = sp.simplify(sp.diff(rhobar_conj, t) + 3 * H_conj * pbar_conj)   # (2.31) on the conjugate side
print("   (2.31) holds on the conjugate side:", cont_conj == 0)
rho_GV = rhobar_conj / a**3                       # rhobar preserved, new scale factor 1/at = a
p_GV = -pbar_conj / a**3                          # pbar reversed
cont_GV = sp.simplify(sp.diff(rhobar_conj, t) + 3 * H * (-pbar_conj))       # (2.31) for the transformed set
print("   (2.31) holds after the map:", cont_GV == 0)
print("   rho_GV - rho_eff =", sp.simplify(rho_GV - rho_eff), "; p_GV - p_eff =", sp.simplify(p_GV - p_eff))
assert sp.simplify(p_GV - p_eff) == 0

print("C. GV string-frame power laws (2.33)-(2.38), d = 3")
d = 3
gam, al, be, rho0 = sp.symbols("gamma alpha beta rho0", real=True)
sol = sp.solve([sp.Eq(d * gam * al + be, 2), sp.Eq(2 * be - be**2 - d * al**2, 0)], [al, be], dict=True)
nontriv = [s for s in sol if sp.simplify(s[al]) != 0]
s = nontriv[0]
print("   non-flat solution:", s)
alpha_of = sp.simplify(s[al]); beta_of = sp.simplify(s[be])
assert sp.simplify(alpha_of - 2 * gam / (1 + d * gam**2)) == 0
# check (2.27), (2.28), (2.29) with a = t^alpha, phibar = -beta ln t, rhobar = rho0 a^(-d gamma)
aa = t**alpha_of; phib = -beta_of * sp.log(t); Hs = sp.diff(aa, t) / aa
rhob = rho0 * aa ** (-d * gam); pb = gam * rhob
r0 = sp.simplify((sp.diff(phib, t) ** 2 - d * Hs**2) / (sp.exp(phib) * rhob) * rho0)   # value of rho0 that (2.27) needs
eq27 = sp.simplify(sp.diff(phib, t) ** 2 - d * Hs**2 - sp.exp(phib) * rhob.subs(rho0, r0))
eq28 = sp.simplify(sp.diff(Hs, t) - Hs * sp.diff(phib, t) - sp.Rational(1, 2) * sp.exp(phib) * pb.subs(rho0, r0))
eq29 = sp.simplify(2 * sp.diff(phib, t, 2) - sp.diff(phib, t) ** 2 - d * Hs**2)
print("   residuals (2.27), (2.28), (2.29):", eq27, eq28, eq29)
assert eq27 == 0 and eq28 == 0 and eq29 == 0
print("   alpha(-gamma) + alpha(gamma) =", sp.simplify(alpha_of.subs(gam, -gam) + alpha_of),
      "; beta(-gamma) - beta(gamma) =", sp.simplify(beta_of.subs(gam, -gam) - beta_of))
print("   stiff gamma = 1: a ~ t^", alpha_of.subs(gam, 1), "; its SFD partner gamma = -1: a ~ t^", alpha_of.subs(gam, -1),
      "(power law with running dilaton beta =", beta_of.subs(gam, -1), "; not de Sitter)")

print("D. Einstein gravity, 8 pi G = 1, single fluid w, a = t^q, q = 2/(3(1+w))")
q = 2 / (3 * (1 + w))
aE = t**q
HE = sp.diff(aE, t) / aE
rhoE = 3 * HE**2
# apply the SFD-with-sources map: at = 1/a, rho~ at~^3 = rho a^3, w~ = -w; test Friedmann for the image
atE = 1 / aE
rho_img = rhoE * aE**3 / atE**3
H_img = sp.diff(atE, t) / atE
fried_resid = sp.simplify(H_img**2 - rho_img / 3)
print("   image of a Friedmann solution under the map: H~^2 - rho~/3 =", sp.factor(fried_resid),
      "(zero only where a = 1: not a solution of Einstein gravity)")
assert sp.simplify(fried_resid.subs({w: 0, t: 2})) != 0
wbar = sp.symbols("wbar", real=True)
w_cosmic = sp.solve(sp.Eq(2 / (3 * (1 + wbar)), -q), wbar)[0]
print("   same cosmic time, a -> 1/a between single-fluid solutions: wbar =", sp.simplify(w_cosmic), "(phantom duality, w -> -2 - w)")
eta = sp.symbols("eta", positive=True)
w_conf = sp.solve(sp.Eq(2 / (1 + 3 * wbar), -2 / (1 + 3 * w)), wbar)[0]
print("   same conformal time (a ~ eta^(2/(1+3w))): wbar =", sp.simplify(w_conf), "(w + wbar = -2/3)")

print("E. MJL 2024 sec. 6: Brans-Dicke w_BD = -4/3, U = 0")
H0, lam0, a0 = sp.symbols("H0 lambda0 a0", positive=True)
aJ = a0 * sp.exp(H0 * t)                 # (46a)
lamJ = lam0 * sp.exp(-3 * H0 * t)        # (46b)
aEin = sp.sqrt(lamJ) * aJ                # at~ = Omega a with Omega^2 proportional to f(lambda) = lambda (BD), constants dropped
k = sp.simplify(sp.log(aEin / (sp.sqrt(lam0) * a0)) / sp.log(aJ / a0))
print("   d ln at~ / d ln a =", k, "(the program has -1)")
assert k == sp.Rational(-1, 2)
tt, tc = sp.symbols("ttilde t_c", positive=True)
aS = (tc - tt) ** sp.Rational(1, 3)      # (47) up to constants: contracting toward t~ = t_c
HS = sp.diff(aS, tt) / aS
rhoS = 3 * HS**2
print("   eq. (47) form: H~ =", sp.simplify(HS), "; rho~ a~^6 =", sp.simplify(rhoS * aS**6), "(constant: stiff, w = 1, contracting)")

print("F. which conjugate content acts on ours as Lambda (w = -1)")
for name, rule in [("E carried (program; GV SFD with sources)", lambda x: -x),
                   ("densities identified, shared cosmic time (heuristic; phantom duality)", lambda x: -2 - x),
                   ("shared conformal time (Camara da Silva et al.; Dark Gravity)", lambda x: sp.Rational(-2, 3) - x)]:
    need = sp.solve(sp.Eq(rule(wt), -1), wt)[0]
    print("   %-72s dual w~ = %s ; dual dust -> %s ; dual stiff -> %s" % (name, need, rule(sp.Integer(0)), rule(sp.Integer(1))))
print("all checks passed")
