# Remaining checks: P8 CM-frame / general-frame algebra; P14 impulse-approximation anchor for the
# contact-model deflections; P20 accuracy of the leading-order gated precession at Mercury's
# GM/(a v*^2) = 0.159 and e = 0.2056 (small beta, so first order in beta, all orders in GM/(a v*^2)).
import sys
import sympy as sp
from math import exp, sqrt, pi, atan2
# ---- P8 algebra
v = sp.Matrix(sp.symbols('vx vy vz', real=True)); n = sp.Matrix(sp.symbols('nx ny nz', real=True))
m1, m2 = sp.symbols('m1 m2', positive=True); Mt = m1 + m2; nu = m1*m2/Mt**2
v1 = m2*v/Mt; v2 = -m1*v/Mt
dot = lambda a, b: (a.T*b)[0]
eih = sp.Rational(3, 2)*(dot(v1, v1) + dot(v2, v2)) - sp.Rational(7, 2)*dot(v1, v2) - sp.Rational(1, 2)*dot(n, v1)*dot(n, v2)
mas = (dot(v1, v1) + dot(v2, v2)) - sp.Rational(5, 2)*dot(v1, v2) - sp.Rational(1, 2)*dot(n, v1)*dot(n, v2)
print("CM: EIH - [(3+nu)v^2 + nu (n.v)^2]/2 =", sp.simplify(eih - ((3 + nu)*dot(v, v) + nu*dot(n, v)**2)/2))
print("CM: massive - [(1 + nu/2) v^2 + nu (n.v)^2/2] =", sp.simplify(mas - ((1 + nu/2)*dot(v, v) + nu*dot(n, v)**2/2)))
a = sp.Matrix(sp.symbols('a1:4', real=True)); b = sp.Matrix(sp.symbols('b1:4', real=True))
eihg = sp.Rational(3, 2)*(dot(a, a) + dot(b, b)) - sp.Rational(7, 2)*dot(a, b) - sp.Rational(1, 2)*dot(n, a)*dot(n, b)
alt = sp.Rational(3, 2)*dot(a - b, a - b) - sp.Rational(1, 2)*dot(a, b) - sp.Rational(1, 2)*dot(n, a)*dot(n, b)
print("general frame: EIH velocity terms - [3/2|v1-v2|^2 - 1/2 v1.v2 - 1/2 (n.v1)(n.v2)] =", sp.simplify(eihg - alt))
# ---- P14 impulse approximation for H = p^2/2 - g exp(-r^2/2) exp(-p^2): theta ~ g e^{-v^2} b e^{-b^2/2} sqrt(2 pi)/v^2
g = 0.05
print("P14 impulse-approximation deflections (valid when small):")
for bb in (0.5, 3.0, 10.0):
    for vv in (0.3, 1.0, 3.0):
        th = g*exp(-vv**2)*bb*exp(-bb**2/2)*sqrt(2*pi)/vv**2
        print(f"   b = {bb:4.1f}, v = {vv:3.1f}: {th:.4e}")
# ---- P20 precession accuracy at Mercury's parameters
src = open(sys.argv[1]).read().split('print("== precession')[0]
exec(src)
x = 0.15915; e = 0.20563
for beta in (0.01, 0.2):
    m, adv, dH, dL, nst = precession(beta, 1/x, e, 1 + beta, n_orb=6)
    f = -4*pi*beta*x/(1 - e**2)
    print(f"P20: beta = {beta}: measured {m:.5e} rad/orbit, leading-order formula {f:.5e}, ratio {m/f:.4f}")
