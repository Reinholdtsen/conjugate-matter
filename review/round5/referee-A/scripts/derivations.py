"""Referee A, step 3: independent symbolic (sympy) and numerical re-derivations."""
import sympy as sp
import numpy as np
import mpmath as mp

print("=" * 78)
print("(a) blackbody coefficient kappa from first principles")
x = sp.symbols('x', positive=True)
# Bose integrals: int_0^oo x^(s-1)/(e^x-1) dx = Gamma(s) zeta(s); checked numerically with mpmath
I2 = sp.gamma(3) * sp.zeta(3)
I3 = sp.gamma(4) * sp.zeta(4)
n2 = mp.quad(lambda t: t**2 / (mp.e**t - 1), [0, mp.inf]); n3 = mp.quad(lambda t: t**3 / (mp.e**t - 1), [0, mp.inf])
print("  int x^2/(e^x-1): numeric", mp.nstr(n2, 12), " Gamma(3)zeta(3) =", sp.N(I2, 12))
print("  int x^3/(e^x-1): numeric", mp.nstr(n3, 12), " Gamma(4)zeta(4) =", sp.N(I3, 12), "= pi^4/15:", sp.simplify(I3 - sp.pi**4/15) == 0)
T, hbar, c, kB, D = sp.symbols('T hbar c k_B D', positive=True)
g = 2
n = g / (2 * sp.pi**2) * (kB * T / (hbar * c))**3 * I2                 # photon number density
mean_p = (kB * T / c) * I3 / I2                                        # <|p|> = <E>/c
N = n * sp.pi / 6 * D**3                                               # sphere of diameter D
h = 2 * sp.pi * hbar
for label, Dp, Nreg in [("sphere, D_p = 2<|p|>", 2 * mean_p, N),
                        ("sphere, D_p = kT/c", kB * T / c, N),
                        ("sphere, D_p = <|p|>", mean_p, N),
                        ("cube side D, D_p = 2<|p|>", 2 * mean_p, n * D**3)]:
    k = sp.simplify(D * Dp / (h * Nreg**sp.Rational(1, 3)))
    print(f"  kappa [{label:28s}] = {sp.nsimplify(k)}  = {float(k):.5f}")
kap = 3**sp.Rational(1, 3) * sp.pi**sp.Rational(10, 3) / (30 * sp.zeta(3)**sp.Rational(4, 3))
k_sphere = sp.simplify(D * 2 * mean_p / (h * N**sp.Rational(1, 3)))
print("  manuscript closed form minus derived (should be 0):", sp.simplify(k_sphere - kap), float(k_sphere - kap))

print("=" * 78)
print("(b) where the radiation rectangle is square (Planck units hbar=c=kB=G=1)")
Nn, kk = sp.symbols('N kappa', positive=True)
side = sp.sqrt(2 * sp.pi * kk * Nn**sp.Rational(1, 3))
print("  side at square = sqrt(2 pi kappa N^(1/3)) =", sp.simplify(side), "; coefficient sqrt(2 pi kappa) =", float(sp.sqrt(2 * sp.pi * kap)))
mean_coef = float(I3 / I2)
coefT = float(sp.sqrt(2 * sp.pi * kap)) / (2 * mean_coef)
print("  T_sq/T_P = sqrt(2 pi kappa)/(2 <E>/kT) N^(1/6); coefficient =", round(coefT, 5))

print("=" * 78)
print("(c) reciprocity rho_lambda on rectangles")
lam, hb, L, P, l1, l2 = sp.symbols('lambda hbar L P lambda1 lambda2', positive=True)
R = lambda l: sp.Matrix([[0, l**2 / hb], [-hb / l**2, 0]])
J = sp.Matrix([[0, 1], [-1, 0]])
print("  symplectic: R^T J R - J =", sp.simplify(R(lam).T * J * R(lam) - J))
Lp, Pp = lam**2 * P / hb, hb * L / lam**2
A = lambda L_, P_: hb * L_ / (lam**2 * P_)
print("  area invariant:", sp.simplify(Lp * Pp - L * P) == 0, "; A' * A =", sp.simplify(A(Lp, Pp) * A(L, P)))
print("  self-dual lambda^2:", sp.solve(sp.Eq(A(L, P), 1), lam))
print("  rho_l1 rho_l2^-1 =", sp.simplify(R(l1) * R(l2).inv()))
# Fourier box [lP, L] x [hbar/L, hbar/lP]: image of x-interval under p' = (hbar/lam^2) x ... and of p-interval under x' = lam^2 p/hbar
lP = sp.symbols('l_P', positive=True)
sol = sp.solve([sp.Eq(lam**2 * (hb / L) / hb, lP), sp.Eq(lam**2 * (hb / lP) / hb, L)], lam, dict=True)
print("  Fourier box self-dual iff lambda =", sol)

print("=" * 78)
print("(d) Gaussian statements (hbar = lambda = 1)")
Zc = 0.3 + 0.7j
xs = np.linspace(-40, 40, 400001)
psi = np.exp(1j * Zc * xs**2 / 2)
ps = np.array([0.0, 0.5, 1.0, 1.5])
ft = np.array([np.trapezoid(psi * np.exp(-1j * p * xs), xs) for p in ps])
# fit ft(p) = C exp(i W p^2/2): W = 2 log(ft(p)/ft(0)) / (i p^2)
W = [2 * np.log(ft[i] / ft[0]) / (1j * ps[i]**2) for i in range(1, 4)]
print("  numerical FT exponent W at p = 0.5, 1, 1.5:", np.round(W, 5), "; -1/Z =", np.round(-1 / Zc, 5))
X, Y = sp.symbols('X Y', real=True)
xv = sp.symbols('x', real=True)
Zs = X + sp.I * Y
# position and momentum variances of exp(i Z x^2/2)
dens_x = sp.exp(-Y * xv**2)
var_x = sp.simplify(sp.integrate(xv**2 * dens_x, (xv, -sp.oo, sp.oo), conds='none') / sp.integrate(dens_x, (xv, -sp.oo, sp.oo), conds='none'))
Wm = -1 / Zs
ImW = sp.simplify(sp.im(sp.expand_complex(Wm)))
print("  Im(-1/Z) =", ImW)
var_p = sp.simplify(1 / (2 * ImW))
print("  Var x =", var_x, " Var p =", var_p, " (Var x/Var p) =", sp.simplify(var_x / var_p), "-> Dx/Dp = 1/|Z|")
# Wigner quadratic form G with W(x,p) ~ exp(-[Y x^2 + (p - X x)^2 / Y])
G = sp.Matrix([[Y + X**2 / Y, -X / Y], [-X / Y, 1 / Y]])
print("  det G =", sp.simplify(G.det()), "; on |Z|=1: G_xx = (X^2+Y^2)/Y, G_pp = 1/Y")
# Siegel distance vs |ln|Z||
def dist(Z):
    return float(mp.acosh(1 + abs(Z - 1j)**2 / (2 * Z.imag)))
rng = np.random.default_rng(1)
worst = 1e9
for _ in range(20000):
    Zr = complex(rng.normal(0, 3), abs(rng.lognormal(0, 2)))
    worst = min(worst, dist(Zr) - abs(np.log(abs(Zr))))
print("  min over 20000 random Z of [d(i,Z) - |ln|Z||] =", f"{worst:.3e}", "(>= 0 expected)")
print("  on slice: d(i, iY) for Y = e^-3:", dist(complex(0, np.exp(-3))), "(= 3 = |ln Y|)")
r = 1.7
print("  squeezed vacuum sigma_x = e^r/sqrt2 -> Y = e^-2r, d =", dist(complex(0, np.exp(-2 * r))), " 2r =", 2 * r)
# Fubini-Study metric for the family psi_Z, normalised: psi = (Y/pi)^(1/4) exp(i Z x^2/2)
psiN = (Y / sp.pi)**sp.Rational(1, 4) * sp.exp(sp.I * Zs * xv**2 / 2)
def ip(f, g_):
    return sp.simplify(sp.integrate(sp.simplify(sp.conjugate(f) * g_), (xv, -sp.oo, sp.oo), conds='none'))
dX = sp.diff(psiN, X); dY = sp.diff(psiN, Y)
gXX = sp.simplify(ip(dX, dX) - sp.Abs(ip(psiN, dX))**2)
gYY = sp.simplify(ip(dY, dY) - sp.Abs(ip(psiN, dY))**2)
gXY = sp.simplify(sp.re(ip(dX, dY) - ip(dX, psiN) * ip(psiN, dY)))
print("  FS metric g_XX =", sp.simplify(gXX), " g_YY =", sp.simplify(gYY), " g_XY =", gXY)
print("  ratio to Siegel 1/Y^2:", sp.simplify(gXX * Y**2), sp.simplify(gYY * Y**2))
print("  FS length of Siegel path 2r = 2r/sqrt(8) = r/sqrt(2): check 2*1.7/sqrt(8) =", 2 * 1.7 / np.sqrt(8), " 1.7/sqrt2 =", 1.7 / np.sqrt(2))
# degree d Siegel: ds^2 = tr(Y^-1 dZ Y^-1 dZbar) along Z = i e^t 1_d
d_ = 3
print(f"  degree {d_}: tr(1_d) = {d_} -> length sqrt(d)|ln y|")
# |Z| = 1 circle parametrisation
s = sp.symbols('s', real=True)
Zcirc = sp.tanh(s) + sp.I * sp.sech(s)
print("  |tanh s + i sech s|^2 =", sp.simplify(sp.tanh(s)**2 + sp.sech(s)**2))
coshd = sp.simplify(1 + (sp.tanh(s)**2 + (sp.sech(s) - 1)**2) / (2 * sp.sech(s)))
print("  cosh d(i, Z(s)) =", sp.simplify(coshd.rewrite(sp.exp)), "-> d = |s|; numeric s=2:", float(coshd.subs(s, 2)), float(sp.cosh(2)))

print("=" * 78)
print("(e) A(t) = sqrt(Omega_Lambda(t)) and Lambda = 3 lP^2/lambda^4")
H, Lam, cc, LL = sp.symbols('H Lambda c L_Lambda', positive=True)
lam2 = lP * LL
A_t = (cc / H) * lP / lam2
OmL = Lam * cc**2 / (3 * H**2)
print("  A(t)^2 - Omega_L(t) with L_Lambda = sqrt(3/Lambda):", sp.simplify((A_t**2 - OmL).subs(LL, sp.sqrt(3 / Lam))))
print("  3 lP^2/lambda^4 - Lambda:", sp.simplify((3 * lP**2 / lam2**2 - Lam).subs(LL, sp.sqrt(3 / Lam))))
print("  rho_lambda sends p = hbar/lP to x = lambda^2/lP = L_Lambda:", sp.simplify(lam2 / lP))

print("=" * 78)
print("(f) CKN comparison and the dark-energy identity (natural units hbar=c=1)")
MP, Lsym, H0, OL = sp.symbols('M_P L H_0 Omega_L', positive=True)
lPn = 1 / MP
print("  1/sqrt(lP L) - sqrt(M_P/L) =", sp.simplify(1 / sp.sqrt(lPn * Lsym) - sp.sqrt(MP / Lsym)))
rhoL = 3 * OL * (MP**2 / (8 * sp.pi)) * H0**2
print("  rho_L / (1/sqrt(lP/H0))^4 =", sp.simplify(rhoL / (1 / sp.sqrt(lPn / H0))**4), "-> ^(1/4) = (3 OL/8pi)^(1/4)")

print("=" * 78)
print("(g) bimetric Yukawa strength from mode decomposition, keeping the background ratio c")
Mg, Mf, cb = sp.symbols('M_g M_f c', positive=True)
# Background fbar = c^2 gbar. Perturbations: dg, df (df measured in units where fbar = c^2 eta).
# Kinetic terms ~ M_g^2 dg E dg + M_f^2 c^2 (df/c^2) E (df/c^2) * c^2 ... use Lueben et al. eq. (8): dg ~ dG - alpha^2 dM.
# Do it directly: quadratic kinetic matrix K = diag(M_g^2, M_f^2 c^2) for fields (h_g, h_f) normalised so that
# the Fierz-Pauli mass term is proportional to (h_g - h_f)^2  (h_f = df/c^2). Matter couples to h_g only.
hg, hf = sp.symbols('h_g h_f')
K = sp.diag(Mg**2, Mf**2 * cb**2)
# massless eigenvector: h_g = h_f ; massive: orthogonal w.r.t. K: M_g^2 u_g + M_f^2 c^2 u_f = 0
v0 = sp.Matrix([1, 1]); v1 = sp.Matrix([Mf**2 * cb**2, -Mg**2])
n0 = (v0.T * K * v0)[0]; n1 = (v1.T * K * v1)[0]
# amplitude for matter on g: propagator weight = (component of h_g)^2 / norm
w0 = sp.simplify(v0[0]**2 / n0); w1 = sp.simplify(v1[0]**2 / n1)
# static limit: massless tensor structure gives 1/2 rho rho, massive gives 2/3 rho rho
alpha_yuk = sp.simplify((w1 * sp.Rational(2, 3)) / (w0 * sp.Rational(1, 2)))
print("  Yukawa strength alpha =", sp.factor(alpha_yuk), " ; at M_f = M_g:", sp.simplify(alpha_yuk.subs(Mf, Mg)),
      " ; at M_f = M_g, c = 1:", alpha_yuk.subs({Mf: Mg, cb: 1}))
print("  Newton constant from massless mode: 1/(M_g^2 + c^2 M_f^2) (cf. Lueben et al.: m_Pl^2 = m_g^2 (1 + alpha^2 c^2))")

print("=" * 78)
print("(h) the a^-6 term: minisuperspace kinetic terms and a -> C/a")
a, adot, Cc, M, Mt = sp.symbols('a adot C M_P Mtilde', positive=True)
K1 = M**2 * a * adot**2
K2 = Mt**2 * Cc**3 * adot**2 / a**5
# under a -> C/a, adot -> -C adot/a^2
sub = {a: Cc / a, adot: -Cc * adot / a**2}
K1t = sp.simplify(K1.subs(sub, simultaneous=True)); K2t = sp.simplify(K2.subs(sub, simultaneous=True))
print("  K1(C/a) =", K1t, "  K2(C/a) =", K2t)
print("  exchange iff M~ = M_P:", sp.solve(sp.Eq(K1t, K2), Mt), "; equal at a^6 = C^3:", sp.solve(sp.Eq(K1, K2.subs(Mt, M)), a))
# kinetic term of the dual Einstein term from atilde = C/a: Mt^2 atilde atildedot^2
at = Cc / a; atdot = -Cc * adot / a**2
print("  Mt^2 atilde atildedot^2 =", sp.simplify(Mt**2 * at * atdot**2), "(= K2)")
