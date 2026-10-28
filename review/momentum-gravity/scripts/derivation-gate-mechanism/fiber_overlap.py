#!/usr/bin/env python3
"""What #6 §4's 'exchange X only over their fiber overlap' gives in field-theory terms.

Wigner (phase-space) density of a field, convention W(x,p) = int dy e^{ipy} psi*(x+y/2) psi(x-y/2).
Its fiber coordinate p is the AVERAGE momentum of the annihilated and created quanta.
Reading R1 (one-body overlap): H = int dx dp dp' W(x,p) S(p-p') W(x,p'), S a fiber kernel of width mu.
Reading R2 (pair channel): H = B^dagger B, B(x) = int dy gt(y) psi(x+y/2) psi(x-y/2).
Units hbar = 1.
"""
import numpy as np
import sympy as sp

print("== A. momentum labels (translation invariance: k1 + k2 = k3 + k4) ==")
k1 = sp.Matrix(sp.symbols('k1x k1y k1z')); k2 = sp.Matrix(sp.symbols('k2x k2y k2z'))
k3 = sp.Matrix(sp.symbols('k3x k3y k3z')); k4 = k1 + k2 - k3
d13 = sp.simplify((k1 + k3) / 2 - (k2 + k4) / 2)      # bilinear A: 1 -> 3, bilinear B: 2 -> 4
d14 = sp.simplify((k1 + k4) / 2 - (k2 + k3) / 2)      # bilinear A: 1 -> 4, bilinear B: 2 -> 3
print("fiber separation, pairing (1->3, 2->4):", list(d13), " equals k1 - k4:", sp.simplify(d13 - (k1 - k4)) == sp.zeros(3, 1))
print("fiber separation, pairing (1->4, 2->3):", list(d14), " equals k1 - k3:", sp.simplify(d14 - (k1 - k3)) == sp.zeros(3, 1))
k, q, mu, c = sp.symbols('k q mu c', positive=True)
K1, K2 = sp.Matrix([k, 0, 0]), sp.Matrix([-k, 0, 0])
th = sp.acos(1 - q**2 / (2 * k**2))
K3 = sp.Matrix([k * sp.cos(th), k * sp.sin(th), 0]); K4 = -K3
print("CM: |k1-k3|^2 =", sp.simplify((K1 - K3).dot(K1 - K3)), "; |k1-k4|^2 =", sp.simplify((K1 - K4).dot(K1 - K4)),
      "; |k1-k2|^2 =", sp.simplify((K1 - K2).dot(K1 - K2)))
S = lambda d2: sp.exp(-d2 / (2 * mu**2))                # fiber kernel S(Delta) = exp(-Delta^2/(2 mu^2))
amp_R1 = S((K1 - K3).dot(K1 - K3)) + S((K1 - K4).dot(K1 - K4))
print("R1 Born amplitude (identical chi) = S(q) + S(q_u) =", sp.simplify(amp_R1))
print("  at q -> 0:", sp.simplify(sp.limit(amp_R1, q, 0)), " (the second term is #6's exp(-(p1-p2)^2/2mu^2) with p1-p2 = 2k)")
print("  limit k -> oo at q -> 0:", sp.limit(sp.limit(amp_R1, q, 0), k, sp.oo))

print("\n== B. R1 as an operator: the fiber integrals give an x-local two-body potential ==")
y, P, D = sp.symbols('y P Delta', real=True)
p, pp = P + D / 2, P - D / 2
print("Jacobian d(p,p')/d(P,Delta) =", sp.Matrix([[sp.diff(p, P), sp.diff(p, D)], [sp.diff(pp, P), sp.diff(pp, D)]]).det())
yy = sp.symbols('yp', real=True)
print("phase p y + p' y' =", sp.expand(p * y + pp * yy), " -> int dP gives 2 pi delta(y + y'); then the Delta integral:")
St = sp.integrate(sp.exp(sp.I * D * y) * sp.exp(-D**2 / (2 * mu**2)), (D, -sp.oo, sp.oo))
print("  St(y) = int dDelta e^{i Delta y} S(Delta) =", sp.simplify(St))
print("  so H = 2 pi int da db St(a - b) psi+(a) psi(b) psi+(b) psi(a) = 2 pi int da db St(a-b) :n(a) n(b): + one-body,")
print("  a two-body potential V(r) = 2 pi St(r), Gaussian of width 1/mu in position.")

print("\n== C. numerical check of the identity for two wavepackets (1D, quadrature) ==")


def packet(x, x0, p0, sx):
    return (2 * np.pi * sx**2) ** -0.25 * np.exp(-(x - x0) ** 2 / (4 * sx**2) + 1j * p0 * x)


def wigner(phi, x, y, pgrid):
    # W(x,p) = int dy e^{ipy} phi*(x + y/2) phi(x - y/2)
    X, Y = np.meshgrid(x, y, indexing='ij')
    integrand = np.conj(phi(X + Y / 2)) * phi(X - Y / 2)            # (Nx, Ny)
    dy = y[1] - y[0]
    return integrand @ np.exp(1j * np.outer(y, pgrid)) * dy        # (Nx, Np)


x = np.linspace(-9, 9, 361); dx = x[1] - x[0]
yg = np.linspace(-18, 18, 721)
pg = np.linspace(-7, 7, 281); dp = pg[1] - pg[0]
sx = 1.0
for (x1, p1, x2, p2, mu_) in ((0.0, 0.3, 0.7, -0.5, 0.8), (0.4, 1.0, -0.3, -0.2, 1.7)):
    ph1 = lambda z: packet(z, x1, p1, sx)
    ph2 = lambda z: packet(z, x2, p2, sx)
    W1, W2 = wigner(ph1, x, yg, pg), wigner(ph2, x, yg, pg)
    Smat = np.exp(-(pg[:, None] - pg[None, :]) ** 2 / (2 * mu_**2))
    I_phase = np.einsum('xp,pq,xq->', W1, Smat, W2) * dx * dp * dp
    A, B = np.meshgrid(x, x, indexing='ij')
    St_num = np.sqrt(2 * np.pi) * mu_ * np.exp(-mu_**2 * (A - B) ** 2 / 2)
    f = np.conj(ph1(x)) * ph2(x); g = np.conj(ph2(x)) * ph1(x)
    I_pos = 2 * np.pi * (f @ St_num @ g) * dx * dx
    print("packets (x1,p1)=(%.1f,%.1f) (x2,p2)=(%.1f,%.1f) mu=%.1f:  phase-space overlap = %.8f%+.2ej ; "
          "2pi x exchange integral of V = %.8f%+.2ej" % (x1, p1, x2, p2, mu_, I_phase.real, I_phase.imag, I_pos.real, I_pos.imag))

print("\n== D. the packet overlap itself (mu -> 0 limit): a state property, local in x as much as in p ==")
for (dxs, dps) in ((0.0, 1.0), (1.0, 0.0), (2.0, 0.0), (0.0, 2.0)):
    ph1 = lambda z: packet(z, 0.0, 0.0, sx)
    ph2 = lambda z: packet(z, dxs, dps, sx)
    ov = abs(np.sum(np.conj(ph1(x)) * ph2(x)) * dx) ** 2
    sp_ = 1 / (2 * sx)
    print("  dx=%.1f dp=%.1f: |<1|2>|^2 = %.6f ; exp(-dp^2/(4 sp^2) - dx^2/(4 sx^2)) = %.6f" %
          (dxs, dps, ov, np.exp(-dps**2 / (4 * sp_**2) - dxs**2 / (4 * sx**2))))
print("  (#6's exp(-(p1-p2)^2/2mu^2) is the p-factor with mu^2 = 2 sp^2, sp = the packet's momentum spread)")

print("\n== E. R2, the pair channel: its fiber coordinate is the relative momentum ==")
xs, ys = sp.symbols('x y', real=True)
ka, kb = sp.symbols('k_a k_b', real=True)
phase = sp.expand(sp.I * ka * (xs + ys / 2) + sp.I * kb * (xs - ys / 2))
print("psi(x+y/2) psi(x-y/2) on plane waves k_a, k_b: phase =", sp.collect(phase, [xs, ys]))
print("  -> int dy gt(y) e^{i (k_a-k_b) y/2} = g((k_a - k_b)/2): the vertex sees the pair's relative momentum;")
print("  Born amplitude g(k) g*(k'), on shell |k| = |k'| -> |g(k)|^2: a gate in k, isotropic for g = g(|k|).")

print("\n== F. transfer cross-sections implied by each reading (Born, shapes only) ==")
cc = sp.symbols('cc', real=True)                         # cos theta
SG = lambda q2: sp.exp(-q2 / (2 * mu**2))
qt2, qu2 = 2 * k**2 * (1 - cc), 2 * k**2 * (1 + cc)
sig_R2 = sp.exp(-2 * k**2 / mu**2)                       # record's gate: |F|^2, F = exp(-k^2/mu^2), isotropic
sig_R1_id = 2 * sp.pi * sp.integrate(sp.expand((1 - cc**2) * (SG(qt2) + SG(qu2)) ** 2), (cc, -1, 1))
sig_R1_maj = 2 * sp.pi * sp.integrate((1 - cc) * SG(qu2) ** 2, (cc, -1, 1))
Mx = sp.symbols('M_X', positive=True)
sig_yuk = 2 * sp.pi * sp.integrate((1 - cc) / (qt2 + Mx**2) ** 2, (cc, -1, 1))
print("R2 separable gate      : k^n sigma -> 0 for n = 2, 4, 8:",
      [sp.limit(k**n * sig_R2, k, sp.oo) for n in (2, 4, 8)])
print("R1 identical, sigma_V  : lim k^4 sigma_V =", sp.simplify(sp.limit(k**4 * sig_R1_id, k, sp.oo)),
      "; lim k^2 sigma_V =", sp.limit(k**2 * sig_R1_id, k, sp.oo))
print("R1 distinct (exchange-type), sigma_T : lim k^2 sigma_T =", sp.simplify(sp.limit(k**2 * sig_R1_maj, k, sp.oo)))
print("Yukawa t-channel, sigma_T : lim k^4 sigma_T / log(k) =", sp.simplify(sp.limit(k**4 * sig_yuk / sp.log(k), k, sp.oo)))
mu_v = 1.0
for kk in (0.5, 2.0, 5.0, 10.0):
    vals = [float(e.subs({k: kk, mu: mu_v, Mx: 2 * mu_v})) for e in (sig_R2 * 8 * sp.pi / 3, sig_R1_id, sig_R1_maj, sig_yuk)]
    print("  k/mu = %-5.1f  R2 sigma_V %.3e   R1 identical sigma_V %.3e   R1 distinct sigma_T %.3e   Yukawa(M=2mu) sigma_T %.3e"
          % (kk, *vals))
print("  (unit couplings; compare shapes, not normalizations)")
