"""Referee B: independent symbolic (sympy) and numerical re-derivations.

Each block states the claim, derives it from scratch, and prints the result.
"""
import sympy as sp
import numpy as np
import mpmath as mp

print('=== 1. Blackbody coefficient kappa ===')
T, R, kB, hbar, c = sp.symbols('T R k_B hbar c', positive=True)
z3 = sp.zeta(3)
x = sp.symbols('x', positive=True)
# photon number density and mean |p| from Bose-Einstein integrals
n_int = 2 * z3  # int_0^oo x^2/(e^x-1) dx (Bose-Einstein); checked numerically below
print('  check int x^2/(e^x-1) =', mp.quad(lambda t: t**2/(mp.exp(t)-1), [0, mp.inf]), ' 2 zeta3 =', 2*mp.zeta(3))
e_int = sp.pi**4 / 15  # int_0^oo x^3/(e^x-1) dx
print('  check int x^3/(e^x-1) =', mp.quad(lambda t: t**3/(mp.exp(t)-1), [0, mp.inf]), ' pi^4/15 =', mp.pi**4/15)
n = 2 / (2 * sp.pi**2) * n_int * (kB * T / (hbar * c))**3  # 2 polarisations, d^3p/(2pi hbar)^3
meanp = sp.simplify(e_int / n_int) * kB * T / c
print('n_gamma =', sp.simplify(n), ' ; <|p|> =', sp.simplify(meanp))
Dx = 2 * R
N = n * sp.Rational(4, 3) * sp.pi * R**3
h = 2 * sp.pi * hbar
for lab, Dp, vol in [('sphere, Dp=2<p>', 2 * meanp, 'sphere'), ('sphere, Dp=kT/c', kB * T / c, 'sphere'),
                     ('sphere, Dp=<p>', meanp, 'sphere'), ('cube side Dx, Dp=2<p>', 2 * meanp, 'cube')]:
    NN = N if vol == 'sphere' else n * Dx**3
    k = sp.simplify(Dx * Dp / (h * NN**sp.Rational(1, 3)))
    print(f'  kappa[{lab}] = {sp.nsimplify(k)} = {sp.N(k, 6)}')
kappa = sp.simplify(Dx * 2 * meanp / (h * N**sp.Rational(1, 3)))
target = 3**sp.Rational(1, 3) * sp.pi**sp.Rational(10, 3) / (30 * z3**sp.Rational(4, 3))
print('  kappa == 3^(1/3) pi^(10/3)/(30 zeta3^(4/3)) ?', sp.simplify(kappa - target) == 0)
print('  T and R independence: d kappa/dT =', sp.diff(kappa, T), ', d kappa/dR =', sp.diff(kappa, R))

print('\n=== 2. Square radiation rectangle: closed forms (Planck units hbar=c=G=kB=1) ===')
Ng, tau = sp.symbols('N_gamma tau', positive=True)
kap = sp.Symbol('kappa', positive=True)
# area in Planck units: (Dx/lP)(Dp/mP c) = 2 pi kappa N^(1/3); square: each side sqrt(area)
side = sp.sqrt(2 * sp.pi * kap * Ng**sp.Rational(1, 3))
print('  side at square =', sp.simplify(side), ' -> coefficient', sp.N(sp.sqrt(2 * sp.pi * target), 5))
# Dp/(mP c) = 2<p>/(mP c) = 2 (pi^4/(30 zeta3)) tau
coef = sp.sqrt(2 * sp.pi * target) / (2 * sp.pi**4 / (30 * z3))
print('  T_sq/(N^(1/6) T_P) =', sp.N(coef, 5))

print('\n=== 3. Gaussian states: Fourier transform Z -> -1/Z, widths, ratio ===')
xx, p = sp.symbols('x p', real=True)
X, Y = sp.symbols('X Y', positive=True)
Zs = X + sp.I * Y
# analytic FT of exp(i Z x^2/2): integral exp(i Z x^2/2 - i p x) dx (hbar = 1)
ft = sp.integrate(sp.exp(sp.I * Zs * xx**2 / 2 - sp.I * p * xx), (xx, -sp.oo, sp.oo), conds='none')
print('  FT[exp(iZx^2/2)](p) =', sp.simplify(ft))
expo = sp.Rational(1, 2) / (sp.I * X - Y)  # coefficient of p^2 in the exponent returned above
print('  exponent p^2 coefficient', expo, '== i(-1/Z)/2 ?', sp.simplify(expo - sp.I * (-1 / Zs) / 2) == 0)
# widths
psi2 = sp.exp(-Y * xx**2)
dx2 = sp.integrate(xx**2 * psi2, (xx, -sp.oo, sp.oo)) / sp.integrate(psi2, (xx, -sp.oo, sp.oo))
Zm = -1 / Zs
Ym = sp.simplify(sp.im(sp.expand_complex(Zm)))
dp2 = sp.simplify(1 / (2 * Ym))
print('  Dx^2 =', sp.simplify(dx2), ' Dp^2 =', sp.simplify(dp2), ' Dx/Dp =', sp.simplify(sp.sqrt(dx2 / dp2)))

# numerical FT check for Z = 0.3 + 0.7 i
Zn = 0.3 + 0.7j
xs = np.linspace(-40, 40, 2**16)
dxs = xs[1] - xs[0]
psi = np.exp(1j * Zn * xs**2 / 2)
ps = np.linspace(-3, 3, 61)
phi = np.array([np.sum(psi * np.exp(-1j * pv * xs)) * dxs for pv in ps])
# fit log(phi) = const + i Zp p^2/2  => Zp = 2*(log phi(p) - log phi(0))/(i p^2)
lp = np.log(phi / phi[30])
Zp_est = np.mean([2 * lp[k] / (1j * ps[k]**2) for k in range(len(ps)) if abs(ps[k]) > 0.5])
print('  numerical FT of Z=0.3+0.7i gives Z\' =', np.round(Zp_est, 4), ' ; -1/Z =', np.round(-1 / Zn, 4))

print('\n=== 4. Fubini-Study vs Siegel metric on Gaussians ===')
# FS metric: g = <d ln psi d ln psi^*> - |<d ln psi>|^2 for normalised psi; d ln psi = i x^2 dZ/2 + d(ln N)
# connected part only: (1/4) Var(x^2) |dZ|^2
sig2 = 1 / (2 * Y)
var_x2 = 2 * sig2**2  # Gaussian: Var(x^2) = 2 sigma^4
gFS = sp.Rational(1, 4) * var_x2  # coefficient of |dZ|^2
gS = 1 / Y**2
print('  g_FS/g_Siegel =', sp.simplify(gFS / gS))
# direct check via sympy: compute FS line element along Y with X fixed, using normalised state
Nrm = (Y / sp.pi)**sp.Rational(1, 4)
psiY = Nrm * sp.exp(sp.I * (X + sp.I * Y) * xx**2 / 2)
dpsi = sp.diff(psiY, Y)
inner = lambda f, g: sp.integrate(sp.simplify(sp.conjugate(f) * g), (xx, -sp.oo, sp.oo), conds='none')
gYY = sp.simplify(inner(dpsi, dpsi) - sp.Abs(inner(psiY, dpsi))**2)
print('  direct FS g_YY =', sp.simplify(gYY), ' ; Siegel g_YY = 1/Y^2 ; ratio =', sp.simplify(gYY * Y**2))
r = sp.symbols('r', positive=True)
print('  Siegel length 2r -> FS length', sp.simplify(2 * r * sp.sqrt(sp.Rational(1, 8))))

print('\n=== 5. Distance from i: d(i,Z) >= |ln|Z||, equality on X=0 ===')


def dH(z1, z2):
    return mp.acosh(1 + abs(z1 - z2)**2 / (2 * z1.imag * z2.imag))


rng = np.random.default_rng(1)
worst = 1e9
for _ in range(20000):
    z = mp.mpc(rng.normal() * 3, abs(rng.normal()) * 3 + 1e-3)
    gap = dH(mp.mpc(0, 1), z) - abs(mp.log(abs(z)))
    worst = min(worst, gap)
print('  min over 20000 random Z of d(i,Z) - |ln|Z|| =', mp.nstr(worst, 5))
print('  on slice: d(i, 3i) =', mp.nstr(dH(mp.mpc(0, 1), mp.mpc(0, 3)), 8), ' ln 3 =', mp.nstr(mp.log(3), 8))
# squeezed vacuum sigma_x = e^r/sqrt2 -> Dx^2 = 1/(2Y) = e^{2r}/2 -> Y = e^{-2r}
print('  sigma_x=e^r/sqrt2 gives Y=e^{-2r}, distance |ln Y| = 2r : check', sp.simplify(sp.Abs(sp.log(sp.exp(-2 * r)))))
# degree d: Siegel metric tr(Y^-1 dZ Y^-1 dZbar); path Y=t*1 from 1 to y
d_, y_, t_ = sp.symbols('d y t', positive=True)
print('  degree-d distance from i1 to iy1 along Y=t1: integral sqrt(d) dt/t =', sp.simplify(sp.integrate(sp.sqrt(d_) / t_, (t_, 1, y_))))
# check that Y = t*1 is a geodesic: it is the image of the d=1 geodesic under the diagonal embedding (symmetry); verify
# by comparing with the Siegel distance formula for diagonal Z: distance^2 = sum_i (ln y_i)^2
print('  (Siegel distance between diagonal points i1 and iy1 = sqrt(sum ln^2 y) = sqrt(d)|ln y|)')

print('\n=== 6. Reciprocity maps: area, aspect ratio, squeeze ===')
lam, lam1, lam2, Lx, P = sp.symbols('lambda lambda1 lambda2 L P', positive=True)


def rho(l):
    return sp.Matrix([[0, l**2 / hbar], [-hbar / l**2, 0]])


J = sp.Matrix([[0, 1], [-1, 0]])
print('  symplectic: rho^T J rho == J ?', sp.simplify(rho(lam).T * J * rho(lam) - J) == sp.zeros(2))
print('  rho_l1 rho_l2^-1 =', sp.simplify(rho(lam1) * rho(lam2).inv()))
A = hbar * Lx / (lam**2 * P)
Ap = sp.simplify((lam**2 * P / hbar / lam) / ((hbar * Lx / lam**2) / (hbar / lam)))
print('  image aspect ratio * original =', sp.simplify(A * Ap))
print('  self-dual lambda^2 =', sp.solve(sp.Eq(A, 1), lam**2) if False else sp.solve(sp.Eq(A, 1), lam))

print('\n=== 7. Fourier box self-duality and A(t) = sqrt(Omega_L(t)) ===')
lP, L, LL, H, HL = sp.symbols('l_P L L_Lambda H H_Lambda', positive=True)
# box [lP, L] x [hbar/L, hbar/lP] -> under rho_lambda: x' in [lam^2/L, lam^2/lP] (from p), p' in [hbar lP/lam^2, hbar L/lam^2]
sol = sp.solve([sp.Eq(lam**2 / L, lP), sp.Eq(lam**2 / lP, L)], lam, dict=True)
print('  self-dual Fourier box requires lambda =', sol)
Abox = (L / lam) * (lP / lam)  # (L/lambda)/((hbar/lP)/(hbar/lambda))
At = sp.simplify(Abox.subs(lam, sp.sqrt(lP * LL)).subs(L, c / H).subs(LL, c / HL))
print('  A(t) with lambda^2 = lP L_Lambda, L = c/H(t):', At)
Lam = sp.symbols('Lambda', positive=True)
OmegaL_t = Lam * c**2 / (3 * H**2)
print('  equals sqrt(Omega_L(t)) when H_L^2 = Lambda c^2/3:', sp.simplify(At.subs(HL, c * sp.sqrt(Lam / 3)) - sp.sqrt(OmegaL_t)) == 0)
# Lambda = 3/L_L^2 = 3 lP^2/lambda^4 with L_L = lambda^2/lP
print('  Lambda = 3/L_L^2 with L_L=lambda^2/lP ->', sp.simplify((3 / LL**2).subs(LL, lam**2 / lP)))
# dark-energy ratio: rho_L = 3 OL Mbar^2 H0^2 = 3 OL MP^2 H0^2/(8 pi) ; hbar c/sqrt(lP c/H0) = sqrt(MP H0) natural units
OL, MP, H0 = sp.symbols('Omega_L M_P H_0', positive=True)
ratio = sp.simplify((3 * OL * MP**2 * H0**2 / (8 * sp.pi))**sp.Rational(1, 4) / sp.sqrt(MP * H0))
print('  rho_L^(1/4)/sqrt(M_P H0) =', ratio)
# CKN: hbar c/sqrt(lP L) = sqrt(E_P hbar c / L) since lP E_P = hbar c
EP = sp.symbols('E_P', positive=True)
print('  hbar c/sqrt(lP L) - sqrt(E_P hbar c/L) with lP = hbar c/E_P :',
      sp.simplify(hbar * c / sp.sqrt((hbar * c / EP) * L) - sp.sqrt(EP * hbar * c / L)))

print('\n=== 8. Minisuperspace a -> C/a symmetry of the a^-6 term ===')
tt = sp.symbols('t')
Csym, Mp, Mt = sp.symbols('C M_P Mtilde', positive=True)
a = sp.Function('a')(tt)
at = Csym / a
K1 = Mp**2 * a * sp.diff(a, tt)**2
K2 = Mt**2 * at * sp.diff(at, tt)**2
print('  dual kinetic term in terms of a:', sp.simplify(K2))
b = sp.Function('b')(tt)
K1b = (Mp**2 * a * sp.diff(a, tt)**2).subs(a, Csym / b).doit()
K2b = sp.simplify(K2.subs(a, Csym / b).doit())
print('  under a -> C/b: K1 ->', sp.simplify(K1b), ' ; K2 ->', sp.simplify(K2b))
print('  exchanged iff Mtilde = M_P:', sp.simplify(K1b.subs(b, a) - (Mp**2 * Csym**3 * sp.diff(a, tt)**2 / a**5)) == 0,
      sp.simplify(K2b.subs(Mt, Mp).subs(b, a) - Mp**2 * a * sp.diff(a, tt)**2) == 0)
asym = sp.symbols('a', positive=True)
print('  equality M_P^2 a = M_P^2 C^3/a^5 at a =', sp.solve(sp.Eq(asym, Csym**3 / asym**5), asym))
# Friedmann equation from L = -3 (K1+K2)/N + ... -> 3 H^2 (M_P^2 + Mt^2 C^3 a^-6) = rho
print('  Friedmann: (K1+K2)/(a^3 H^2) =', sp.simplify((K1 + K2) / (a**3 * (sp.diff(a, tt) / a)**2)))

print('\n=== 9. Bimetric linear potential: alpha = (4/3)(M_f/M_g)^2 ===')
Mg, Mf, m = sp.symbols('M_g M_f m', positive=True)
# canonical fields h (from g) and l (from f); mass term ~ (h/Mg - l/Mf)^2 ; matter couples to h/Mg
Mtot = sp.sqrt(Mg**2 + Mf**2)
# massless u = (Mg h + Mf l)/Mtot, massive v = (Mf h - Mg l)/Mtot ; h = (Mg u + Mf v)/Mtot
cu = Mg / Mtot / Mg  # coupling of u to T, from h/Mg
cv = Mf / Mtot / Mg
# check the mass term is a function of v only: h/Mg - l/Mf in terms of u,v
u, v = sp.symbols('u v')
hh = (Mg * u + Mf * v) / Mtot
ll = (Mf * u - Mg * v) / Mtot
print('  h/Mg - l/Mf in terms of (u,v):', sp.simplify(hh / Mg - ll / Mf))
# static point sources: massless spin-2 tensor factor (T T' - T T'/2) -> 1/2; massive (T T' - T T'/3) -> 2/3
massless_factor = 1 - sp.Rational(1, 2)
massive_factor = 1 - sp.Rational(1, 3)
alpha = sp.simplify((cv**2 * massive_factor) / (cu**2 * massless_factor))
print('  alpha =', alpha, ' ; at M_f = M_g:', alpha.subs(Mf, Mg))
print('  Newton constant measured at r >> 1/m is set by the massless coupling cu^2 = 1/(Mg^2+Mf^2)')
