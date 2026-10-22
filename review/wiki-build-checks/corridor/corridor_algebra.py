"""Audit of the wiki-build observation on the thawing corridor (checkpoint #11 section 10).

Observation under test: on the corridor  w_a = -1.5 (1 + w_0)  with w_0 > -1, the CPL
early-time value w_0 + w_a is below -1, so the corridor written in CPL lies in the
quadrant {w_0 > -1, w_0 + w_a < -1} that reads as a phantom crossing.

Steelman questions handled here (pure algebra, sympy):
  1. the exact sign of w_0 + w_a + 1 on the corridor, for every w_0 > -1;
  2. WHERE the corridor's CPL line crosses -1 (scale factor a_c, redshift z_c);
  3. what slope k = -w_a/(1 + w_0) a CPL line needs to cross at DR2's quoted z ~ 0.4;
  4. the corridor's CPL w(z) on 0.4 < z < 2, where DR2's favoured w(z) is below -1;
  5. the Taylor reading: k equals the log-slope d ln(1+w)/d ln a at a = 1.
Only numbers taken from the documents are used: the corridor slope 1.5 (#11 sec. 10) and
the crossing redshift z ~ 0.4 quoted from DR2 [21S] in #11 sec. 10.
"""
import sympy as sp

w0, a, z = sp.symbols('w_0 a z', real=True)
k = sp.symbols('k', positive=True)
t = sp.symbols('t', positive=True)          # t = 1 + w_0 > 0  (w_0 > -1)

print("=== 1. Sign of w0 + wa + 1 on the corridor ===")
K = sp.Rational(3, 2)                        # #11 sec. 10: w_a ~ -1.5 (1 + w_0)
wa_corr = -K * (1 + w0)
s = sp.simplify(w0 + wa_corr + 1)
print("w0 + wa + 1 =", sp.factor(s))
print("solve(w0 + wa + 1 < 0) over reals:", sp.solve_univariate_inequality(s < 0, w0, relational=False))
print("at w0 = -1 (LambdaCDM point):", s.subs(w0, -1))
# general slope k
sk = sp.simplify(w0 + (-k * (1 + w0)) + 1)
print("general slope k: w0 + wa + 1 =", sp.factor(sk), " -> negative for t = 1 + w0 > 0 iff k > 1")
print("  with t = 1 + w0:", sp.factor(sk.subs(w0, t - 1)))

print()
print("=== 2. Where the corridor's CPL line crosses -1 ===")
wa = sp.symbols('w_a', real=True)
a_c_general = sp.solve(sp.Eq(w0 + wa * (1 - a), -1), a)[0]
print("a_c (any CPL line) =", sp.simplify(a_c_general))
a_c_k = sp.simplify(a_c_general.subs(wa, -k * (1 + w0)))
z_c_k = sp.simplify(1 / a_c_k - 1)
print("on wa = -k(1+w0):  a_c =", a_c_k, ",  z_c =", sp.simplify(z_c_k), "  (independent of w0)")
print("corridor k = 3/2:  a_c =", a_c_k.subs(k, K), ",  z_c =", z_c_k.subs(k, K))
print("literature-style k = 1.58 (dagger, model memory, for comparison only): z_c =",
      sp.N(z_c_k.subs(k, sp.Rational(158, 100)), 4))
print("k = 1 (boundary):", sp.limit(z_c_k, k, 1, '+'), " ; k = 3:", z_c_k.subs(k, 3))

print()
print("=== 3. Slope needed for a CPL crossing at DR2's quoted z ~ 0.4 ===")
zq = sp.Rational(2, 5)
k_needed = sp.solve(sp.Eq(z_c_k, zq), k)
print("k such that z_c = 0.4:", k_needed, " -> wa = -%s (1 + w0)" % k_needed[0])
print("ratio to the corridor's 1.5:", sp.Rational(k_needed[0]) / K, "=", sp.N(sp.Rational(k_needed[0]) / K, 4))
# a CPL line that crosses at z = 0.4: its value at a -> 0
print("w0 + wa + 1 for k = 7/2:", sp.factor(sk.subs(k, k_needed[0])))

print()
print("=== 4. The corridor's CPL w(z) + 1, as a multiple of (1 + w0) ===")
wz = w0 + wa_corr * z / (1 + z)
ratio = sp.simplify((wz + 1) / (1 + w0))
print("(w(z) + 1)/(1 + w0) =", sp.factor(ratio))
for zz in [0, sp.Rational(2, 5), 1, sp.Rational(3, 2), 2, sp.Rational(233, 100), 5, 1090]:
    print("   z = %-7s (w+1)/(1+w0) = %+.4f" % (zz, float(ratio.subs(z, zz))))
print("   z -> oo  (w+1)/(1+w0) =", sp.limit(ratio, z, sp.oo))
sol = sp.solve(sp.Eq(ratio, 0), z)
print("zero of (w+1) at z =", sol, "; (w+1) > 0 on 0 <= z < 2, so the corridor's CPL line is not phantom on 0.4 < z < 2")

print()
print("=== 4b. Numbers on the corridor for a few w0 (CPL only, extrapolation flagged) ===")
print(" w0      wa       w0+wa    w(z=0.4)  w(z=1)   w(z=2)   w(z=2.33)  depth below -1 at a=0")
for v in [-0.99, -0.95, -0.9, -0.8, -0.75, -0.7, -0.5]:
    wav = -1.5 * (1 + v)
    def w_of(zz):
        return v + wav * zz / (1 + zz)
    print("%6.3f  %7.4f  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f   %7.4f"
          % (v, wav, v + wav, w_of(0.4), w_of(1.0), w_of(2.0), w_of(2.33), -(v + wav + 1)))

print()
print("=== 5. Taylor reading: k = d ln(1 + w)/d ln a at a = 1 ===")
# If w0 = w(1) and wa = -dw/da(1) (the first-order expansion the CPL page uses), then
# k = -wa/(1 + w0) = w'(1)/(1 + w(1)) = d ln(1 + w)/d ln a at a = 1.
f = sp.Function('f')
wfun = -1 + f(a)            # f = 1 + w >= 0 for a canonical field with rho > 0
w0_T = wfun.subs(a, 1)
wa_T = -sp.diff(wfun, a).subs(a, 1)
kT = sp.simplify(-wa_T / (1 + w0_T))
logslope = sp.simplify((a * sp.diff(sp.log(f(a)), a)).subs(a, 1))
print("k (Taylor CPL) =", kT, " ; d ln(1+w)/d ln a |_(a=1) =", logslope, " ; equal:", sp.simplify(kT - logslope) == 0)
print("So a never-phantom field lands in the CPL crossing quadrant (Taylor reading) iff its 1 + w")
print("grows faster than a^1 today; 1 + w ~ a^p gives k = p. Thawing from rest in matter domination")
print("has 1 + w ~ a^3 at early times (field speed ~ t, kinetic energy ~ t^2 ~ a^3).")
p, eps = sp.symbols('p epsilon', positive=True)
g = eps * a**p                                   # 1 + w = eps a^p
k_pow = sp.simplify(sp.diff(g, a).subs(a, 1) / g.subs(a, 1))
print("example 1 + w = eps a^p: k =", k_pow)
# check the a^3 claim: phi'' + 3H phi' = -V' with H = 2/(3t), phi' = c t
tt, Vp = sp.symbols('t Vprime', positive=True); c = sp.symbols('c', real=True)
eq = sp.Eq(sp.diff(c * tt, tt) + 3 * (sp.Rational(2, 3) / tt) * c * tt, -Vp)
csol = sp.solve(eq, c)[0]
print("matter era, constant slope: phi_dot = c t with c =", csol, "; kinetic energy ~ t^2; a ~ t^(2/3) => KE ~ a^3")
