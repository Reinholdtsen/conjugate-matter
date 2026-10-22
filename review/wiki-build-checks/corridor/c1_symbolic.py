# Part 1 (symbolic): where does the thawing corridor w_a = -s(1 + w0), s = 3/2 (#11 s10), lie
# relative to the CPL crossing boundary w0 + w_a = -1?
#
# CPL: w(a) = w0 + w_a (1 - a).  A fit with w0 > -1 has a CPL line that crosses w = -1 at
# a_c = 1 + (1 + w0)/w_a, which lies in the past (0 < a_c < 1) iff w0 + w_a < -1.
# Everything here is exact algebra on the stated forms; no physics input.
import sympy as sp

w0, wa, a, s, z = sp.symbols("w0 w_a a s z", real=True)
x = sp.symbols("x", positive=True)            # x = 1 + w0 > 0, i.e. w0 > -1

print("== CPL crossing boundary, independent check of the condition ==")
a_c = sp.solve(sp.Eq(w0 + wa * (1 - a), -1), a)[0]
print("w(a_c) = -1  =>  a_c =", sp.simplify(a_c))
# with w0 = -1 + x (x > 0) and w_a < 0 (write w_a = -y, y > 0):
y = sp.symbols("y", positive=True)
ac_xy = sp.simplify(a_c.subs({w0: -1 + x, wa: -y}))
print("  with w0 = -1 + x, w_a = -y (x, y > 0): a_c =", ac_xy, " (always < 1)")
print("  a_c > 0  <=>  y > x  <=>  -w_a > 1 + w0  <=>  w0 + w_a < -1 :",
      sp.simplify((sp.numer(sp.together(ac_xy)) )), "> 0 over denominator", sp.denom(sp.together(ac_xy)))

print("\n== The corridor, general slope s: w_a = -s (1 + w0) ==")
corr = -s * (1 + w0)
g = sp.factor(sp.expand(w0 + corr + 1))
print("w0 + w_a + 1 on the corridor =", g)
g15 = sp.factor(g.subs(s, sp.Rational(3, 2)))
print("at s = 3/2:                  =", g15)
print("  with w0 = -1 + x (x > 0):  =", sp.simplify(g15.subs(w0, -1 + x)),
      "-> sign:", sp.sign(sp.simplify(g15.subs(w0, -1 + x))))
print("  so for every w0 > -1 the corridor point has w0 + w_a < -1 (strictly); at w0 = -1 it is the")
print("  Lambda point itself, on the boundary.")

ac_corr = sp.simplify(a_c.subs(wa, corr))
print("\nCrossing scale factor of the corridor's CPL line: a_c =", ac_corr)
print("  at s = 3/2: a_c =", ac_corr.subs(s, sp.Rational(3, 2)),
      ", z_c = 1/a_c - 1 =", sp.simplify(1 / ac_corr.subs(s, sp.Rational(3, 2)) - 1),
      "(independent of w0)")
zc = sp.simplify(1 / ac_corr - 1)
print("  general slope: z_c =", zc, "; the line is in the crossing region iff s > 1")

print("\n== Margin: how wrong could the slope 1.5 be before the conclusion changes? ==")
print("  boundary slope s = 1 (w_a = -(1 + w0) is the line w0 + w_a = -1 itself)")
print("  1.5 must be overestimated by a factor 1.5 (to s <= 1) for the corridor to leave the region")

print("\n== Comparison: the crossing redshift DR2 reports, z ~ 0.4 (#11 s10 quoting [21S]) ==")
s_04 = sp.solve(sp.Eq(zc, sp.Rational(2, 5)), s)[0]
print("  a CPL line with w0 > -1 crossing at z_c = 0.4 has s = -w_a/(1 + w0) =", s_04,
      "=", float(s_04))
print("  the corridor's lines all cross at z_c =", zc.subs(s, sp.Rational(3, 2)),
      ": same region (w0 > -1, w0 + w_a < -1), different direction within it")

print("\n== Numeric spot checks (exact rationals) ==")
for w0v in [sp.Rational(-99, 100), sp.Rational(-9, 10), sp.Rational(-3, 4), sp.Rational(-1, 2), 0]:
    wav = sp.Rational(-3, 2) * (1 + w0v)
    print(f"  w0 = {str(w0v):>7}  w_a = {str(wav):>8}  w0 + w_a = {str(w0v + wav):>8}"
          f"  (+1 = {str(w0v + wav + 1):>7})  a_c = {str(1 + (1 + w0v) / wav):>4}"
          f"  w(a=0) < -1: {bool(w0v + wav < -1)}")
