"""Referee's independent construction of the Moyal matrix base and the Langmann-Szabo/GW duality.

Anchors used (independent of the manuscript):
  * [x1, x2]_* = i theta with the differential Moyal product
        f*g = f exp( (i theta/2)(<d1 d2> - <d2 d1>) ) g      (checked on x1, x2 below)
  * integral kernel for the same product, sign fixed by comparing with the differential series
  * Weyl symbol of |m><n| built from Hermite functions (QM cross-Wigner function), theta = 1
  * GW eq.(1): phi^(p_a) = int d^Dx e^{(-1)^a i p_a.x} phi(x),  phi^(p) <-> pi^{D/2} sqrt|det theta| phi(x),
    p <-> x~ = 2 theta^{-1} x   (read from hep-th/0402093 source, adapted to D=2)
"""
import itertools, math
import sympy as sp
import numpy as np
from scipy.special import eval_genlaguerre, eval_hermite

x1, x2 = sp.symbols('x1 x2', real=True)
th = sp.Integer(1)

def moyal_diff(f, g, theta, order):
    """Differential Moyal product truncated at given order (exact if one factor is polynomial of degree <= order)."""
    res = 0
    for n in range(order + 1):
        # (i theta/2)^n / n! * sum_k binom(n,k) (-1)^k d1^{n-k} d2^k f * d2^{n-k} d1^k g
        term = 0
        for k in range(n + 1):
            df = sp.diff(f, x1, n - k, x2, k) if n > 0 else f
            dg = sp.diff(g, x2, n - k, x1, k) if n > 0 else g
            term += sp.binomial(n, k) * (-1)**k * df * dg
        res += (sp.I*theta/2)**n / sp.factorial(n) * term
    return sp.expand(res)

print("== anchor: [x1,x2]_* =", sp.simplify(moyal_diff(x1, x2, th, 2) - moyal_diff(x2, x1, th, 2)))

def f_lag(m, n, theta=th):
    """Manuscript's explicit Laguerre form (n>=m); for n<m use f_mn = conj(f_nm)."""
    r2 = x1**2 + x2**2
    if n >= m:
        return (2*(-1)**m*sp.sqrt(sp.factorial(m)/sp.factorial(n))*(sp.sqrt(2/theta))**(n-m)
                *(x1 + sp.I*x2)**(n-m)*sp.assoc_laguerre(m, n-m, 2*r2/theta)*sp.exp(-r2/theta))
    return sp.conjugate(f_lag(n, m, theta)).subs({sp.conjugate(x1): x1, sp.conjugate(x2): x2})

Hh = (x1**2 + x2**2)/2
print("\n== exact H-eigenrelations (H quadratic -> Moyal series terminates at order 2)")
ok = True
for m in range(4):
    for n in range(4):
        f = f_lag(m, n)
        l = sp.simplify((moyal_diff(Hh, f, th, 2) - th*(m + sp.Rational(1, 2))*f)/sp.exp(-(x1**2+x2**2)))
        r = sp.simplify((moyal_diff(f, Hh, th, 2) - th*(n + sp.Rational(1, 2))*f)/sp.exp(-(x1**2+x2**2)))
        ok &= (l == 0 and r == 0)
        if not (l == 0 and r == 0):
            print("  FAIL", m, n, l, r)
print("  H*f_mn = theta(m+1/2) f_mn and f_mn*H = theta(n+1/2) f_mn for all m,n<=3:", ok)

# ---------- exact Gaussian integrator ----------
def gauss_integral(expr, vars_, ):
    """int expr d^n v where expr = poly(v) * exp(quadratic(v)) with neg-def real part. Exact via generating fn."""
    expr = sp.expand(expr)
    # split into sum of poly*exp(Q)
    terms = sp.Add.make_args(expr)
    total = 0
    cache = {}
    for t in terms:
        coeff, expo = sp.S(1), sp.S(0)
        for fac in sp.Mul.make_args(t):
            if fac.func == sp.exp:
                expo += fac.args[0]
            elif fac.is_Pow and fac.base.func == sp.exp:
                expo += fac.base.args[0]*fac.exp
            else:
                coeff *= fac
        expo = sp.expand(expo)
        key = expo
        if key not in cache:
            A = sp.Matrix(len(vars_), len(vars_), lambda i, j: -sp.Rational(1, 2)*sp.diff(expo, vars_[i], vars_[j]))
            bvec = sp.Matrix([sp.diff(expo, v).subs({w: 0 for w in vars_}) for v in vars_])
            c0 = expo.subs({w: 0 for w in vars_})
            cache[key] = (A, bvec, c0)
        A, bvec, c0 = cache[key]
        bs = sp.symbols('bb0:%d' % len(vars_))
        bsv = sp.Matrix(bs)
        Ainv = A.inv()
        G = sp.pi**sp.Rational(len(vars_), 2)/sp.sqrt(A.det())*sp.exp((bsv.T*Ainv*bsv)[0, 0]/4 + c0)
        poly = sp.Poly(coeff, *vars_)
        for mon, cf in poly.terms():
            d = G
            for b_, p_ in zip(bs, mon):
                if p_:
                    d = sp.diff(d, b_, p_)
            total += cf*d.subs(dict(zip(bs, list(bvec))))
    return sp.simplify(total)

y1, y2, z1, z2 = sp.symbols('y1 y2 z1 z2', real=True)

def star_int(f, g, theta=th, sigma=1):
    """(f*g)(x) = (pi theta)^-2 int d2y d2z f(x+y) g(x+z) exp(sigma 2i/theta (y1 z2 - y2 z1))."""
    integrand = f.subs({x1: x1 + y1, x2: x2 + y2}, simultaneous=True)*g.subs({x1: x1 + z1, x2: x2 + z2}, simultaneous=True) \
        * sp.exp(sigma*2*sp.I/theta*(y1*z2 - y2*z1))
    return gauss_integral(integrand, [y1, y2, z1, z2])/(sp.pi*theta)**2

print("\n== fix the sign of the integral kernel against the differential series (theta=1/5, Gaussians off-centre)")
ths = sp.Rational(1, 5)
fa = sp.exp(-((x1 - sp.Rational(1, 3))**2 + x2**2))
gb = sp.exp(-(x1**2 + (x2 + sp.Rational(1, 2))**2))
pt = {x1: sp.Rational(1, 7), x2: sp.Rational(-1, 5)}
ser = complex(sp.N(moyal_diff(fa, gb, ths, 10).subs(pt), 20))
for s in (1, -1):
    val = complex(sp.N(star_int(fa, gb, ths, s).subs(pt), 20))
    print(f"  sigma={s:+d}: integral {val:.12f}   series(order 10) {ser:.12f}   |diff| {abs(val-ser):.2e}")

print("\n== f_mn * f_kl = delta_nk f_ml (integral kernel, sigma=+1, theta=1), all indices <= 1, plus a few with 2")
idx = list(itertools.product(range(2), repeat=4)) + [(2, 1, 1, 0), (0, 2, 2, 1), (1, 2, 1, 2), (2, 2, 2, 0)]
maxerr = 0
for (m, n, k, l) in idx:
    lhs = star_int(f_lag(m, n), f_lag(k, l))
    rhs = f_lag(m, l) if n == k else 0
    for ptt in [{x1: sp.Rational(3, 10), x2: sp.Rational(-7, 10)}, {x1: sp.Rational(-1, 2), x2: sp.Rational(1, 4)}]:
        e = abs(complex(sp.N((lhs - rhs).subs(ptt), 25)))
        maxerr = max(maxerr, e)
print(f"  max |f_mn*f_kl - delta_nk f_ml| over {len(idx)} index sets x 2 points: {maxerr:.2e}")
print("  f00*f00 - f00 =", sp.simplify(star_int(f_lag(0, 0), f_lag(0, 0)) - f_lag(0, 0)))

print("\n== QM anchor: Weyl symbol of |m><n| from Hermite functions (theta=1, x1=q, x2=p)")
def psi(n, q):
    return np.exp(-q**2/2)*eval_hermite(n, q)/math.sqrt(2**n*math.factorial(n)*math.sqrt(math.pi))
yy = np.linspace(-14, 14, 4001); dy = yy[1]-yy[0]
def weyl_mn(m, n, q, p):
    return np.sum(psi(m, q - yy/2)*psi(n, q + yy/2)*np.exp(1j*p*yy))*dy
fl = {(m, n): sp.lambdify((x1, x2), f_lag(m, n), 'numpy') for m in range(4) for n in range(4)}
err = 0
for m in range(4):
    for n in range(4):
        for (q, p) in [(0.3, -0.7), (1.1, 0.4), (-0.6, 1.3)]:
            err = max(err, abs(weyl_mn(m, n, q, p) - fl[(m, n)](q, p)))
print(f"  max |WeylSymbol(|m><n|) - Laguerre f_mn| (m,n<=3, 3 points): {err:.2e}")

print("\n== orthogonality and integrals (exact)")
X1, X2 = x1, x2
maxo, maxi = 0, 0
for (m, n) in itertools.product(range(3), repeat=2):
    I1 = gauss_integral(f_lag(m, n), [X1, X2])
    maxi = max(maxi, abs(complex(sp.N(I1 - (2*sp.pi*th if m == n else 0)))))
    for (k, l) in itertools.product(range(3), repeat=2):
        ov = gauss_integral(sp.expand(sp.conjugate(f_lag(m, n)).subs({sp.conjugate(x1): x1, sp.conjugate(x2): x2})*f_lag(k, l)), [X1, X2])
        target = 2*sp.pi*th if (m, n) == (k, l) else 0
        maxo = max(maxo, abs(complex(sp.N(ov - target))))
print(f"  max |int f_mn - 2 pi theta delta_mn| = {maxi:.1e};  max |int conj(f_mn) f_kl - 2 pi theta delta delta| = {maxo:.1e}  (m,n,k,l<=2)")

print("\n== GW/LS duality on the matrix base, exact Gaussian integrals")
def duality(f, theta, sign):
    """D_sign f(x) = (pi theta)^-1 int d2y exp(sign * i x~.y) f(y),  x~_mu = 2 (theta^-1)_{mu nu} x_nu,  theta_{12}=theta."""
    Th = sp.Matrix([[0, theta], [-theta, 0]])
    xt = 2*Th.inv()*sp.Matrix([x1, x2])
    fy = f.subs({x1: y1, x2: y2}, simultaneous=True)
    integrand = sp.exp(sign*sp.I*(xt[0]*y1 + xt[1]*y2))*fy
    return gauss_integral(integrand, [y1, y2])/(sp.pi*theta)

for theta in (sp.Integer(1), sp.Rational(1, 2), sp.Integer(3)):
    resm, resp = [], []
    for m in range(4):
        for n in range(4):
            f = f_lag(m, n, theta)
            Dm = duality(f, theta, -1)
            Dp = duality(f, theta, +1)
            rm = sp.simplify(Dm/f) if f != 0 else None
            rp = sp.simplify(Dp/f)
            resm.append(((m, n), rm)); resp.append(((m, n), rp))
    okm = all(r == (-1)**mn[0] for mn, r in resm)
    okp = all(r == (-1)**mn[1] for mn, r in resp)
    print(f"  theta={theta}: D_minus f_mn / f_mn == (-1)^m for all m,n<=3: {okm};  D_plus f_mn / f_mn == (-1)^n: {okp}")
    if theta == 1:
        print("    sample ratios D_minus:", [(mn, r) for mn, r in resm[:8]])
        print("    sample ratios D_plus :", [(mn, r) for mn, r in resp[:8]])

print("\n== Omega=1 quadratic form int |d phi|^2 + x~^2 |phi|^2 in the matrix base (theta=1, exact)")
def conjf(f):
    return sp.conjugate(f).subs({sp.conjugate(x1): x1, sp.conjugate(x2): x2})
basis = [(m, n) for m in range(3) for n in range(3)]
Q = sp.zeros(len(basis))
for i, (m, n) in enumerate(basis):
    for j, (k, l) in enumerate(basis):
        fa_, fb_ = f_lag(m, n), f_lag(k, l)
        integrand = sp.expand(conjf(sp.diff(fa_, x1))*sp.diff(fb_, x1) + conjf(sp.diff(fa_, x2))*sp.diff(fb_, x2)
                              + 4*(x1**2 + x2**2)/th**2*conjf(fa_)*fb_)
        Q[i, j] = gauss_integral(integrand, [x1, x2])
offd = max(abs(complex(sp.N(Q[i, j]))) for i in range(len(basis)) for j in range(len(basis)) if i != j)
diag = [(basis[i], sp.nsimplify(sp.simplify(Q[i, i]/(8*sp.pi)))) for i in range(len(basis))]
print("  max |off-diagonal| =", offd)
print("  diagonal / (8 pi):", diag, "  expected m+n+1")
