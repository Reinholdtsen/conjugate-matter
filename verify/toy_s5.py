#!/usr/bin/env python3
"""
toy_s5.py — criterion S5 for the toy Lagrangian (notes/toy-lagrangian.md,
chunk 4): does the vacuum choice of K make matter interactions local in one
Lagrangian (x) and nonlocal in the other (p)?

    .venv/bin/python verify/toy_s5.py

Exit code 1 if any check fails. Phase space R^2, w = [[0,1],[-1,0]],
K(phi) = [[cos phi, sin phi], [sin phi, -cos phi]], eta = w K, hbar = 1.
  A. What the vacuum eta fixes: its null lines are K's eigenlines L+ and L-.
  B. The double-field-theory section condition built from eta forces all
     matter onto one null line, but cannot tell L+ from L- (eta and -eta
     have the same null lines).
  C. A rho-covariant matter interaction built from K (the "marginal" form)
     is local in L+ and nonlocal in L-; a K-blind phase-space interaction
     shows no asymmetry.
"""
import sys
import numpy as np
import sympy as sp

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)
def zero(e):
    return sp.simplify(e) == 0

phi = sp.symbols("phi", real=True)
w = sp.Matrix([[0, 1], [-1, 0]])
K = sp.Matrix([[sp.cos(phi), sp.sin(phi)], [sp.sin(phi), -sp.cos(phi)]])
eta = w*K
ep = sp.Matrix([sp.cos(phi/2), sp.sin(phi/2)])      # K-eigenvalue +1: L+
em = sp.Matrix([-sp.sin(phi/2), sp.cos(phi/2)])     # K-eigenvalue -1: L-
rho = sp.Matrix([[0, 1], [-1, 0]])

print("== A: what the vacuum eta fixes")
check("eta = w K is a symmetric neutral metric (det = -1)", zero((eta - eta.T).norm()) and zero(eta.det() + 1))
check("K e+ = e+, K e- = -e-", zero((K*ep - ep).norm()) and zero((K*em + em).norm()))
check("e+ and e- are null for eta, for every phi", zero((ep.T*eta*ep)[0]) and zero((em.T*eta*em)[0]))
check("they are the only null lines: eta(e+, e-) != 0", sp.simplify((ep.T*eta*em)[0]) != 0,
      str(sp.simplify((ep.T*eta*em)[0])))
check("L+ and L- are Lagrangian (w vanishes on each line trivially in d = 1) and transverse: w(e+, e-) != 0",
      sp.simplify((ep.T*w*em)[0]) != 0)
check("K -> -K sends eta -> -eta, with the same null lines", zero(((w*(-K)) + eta).norm()))
check("rho maps K to -K, and maps L+ onto L- (rho^-1 e+ is a K-eigenvector with eigenvalue -1)",
      zero((rho.inv()*K*rho + K).norm()) and zero((K*(rho.inv()*ep) + rho.inv()*ep).norm()))

print("\n== B: the section condition built from eta")
u, v = sp.symbols("u v", real=True)
F, G = sp.Function("F"), sp.Function("G")
E = sp.Matrix.hstack(ep, em)                        # xi = u e+ + v e-
etaE = sp.simplify(E.T*eta*E)                       # eta in (u, v) components
etaE_inv = sp.simplify(etaE.inv())
def pairing(f, g):
    df = sp.Matrix([sp.diff(f, u), sp.diff(f, v)]); dg = sp.Matrix([sp.diff(g, u), sp.diff(g, v)])
    return sp.simplify((df.T*etaE_inv*dg)[0])
def box(f):
    return sp.simplify(sum(etaE_inv[i, j]*sp.diff(f, [u, v][i], [u, v][j]) for i in range(2) for j in range(2)))
check("in null coordinates eta^-1 is purely off-diagonal (box = c d_u d_v)",
      zero(etaE_inv[0, 0]) and zero(etaE_inv[1, 1]) and not zero(etaE_inv[0, 1]))
check("fields on one null line pass: F(u), G(u)", zero(pairing(F(u), G(u))) and zero(box(F(u))))
check("fields on the other null line pass too: F(v), G(v)", zero(pairing(F(v), G(v))) and zero(box(F(v))))
check("mixing the two lines fails: eta(dF(u), dG(v)) = c F'(u) G'(v) != 0", not zero(pairing(F(u), G(v))),
      str(pairing(F(u), G(v))))
check("a field F(u) + G(v) fails against itself (its square violates the condition)",
      not zero(pairing(F(u) + G(v), F(u) + G(v))))
def pairing_neg(f, g):   # the same pairing built from -eta
    df = sp.Matrix([sp.diff(f, u), sp.diff(f, v)]); dg = sp.Matrix([sp.diff(g, u), sp.diff(g, v)])
    return sp.simplify((df.T*(-etaE_inv)*dg)[0])
check("with -eta the pairing only changes sign, so the same fields pass and fail: it cannot tell L+ from L-",
      zero(pairing_neg(F(u), G(v)) + pairing(F(u), G(v))) and zero(pairing_neg(F(u), G(u)))
      and zero(pairing_neg(F(v), G(v))))

print("\n== C: a rho-covariant interaction built from K (numerical, hbar = 1)")
# psi: a non-self-dual state (two displaced squeezed Gaussians); its Fourier transform in closed form
S_, A_, C_ = 0.35, 1.3, 0.6
def psi(x):
    return np.exp(-(x - A_)**2/(2*S_)) + C_*np.exp(-(x + A_)**2/(2*S_))
def psit(p):   # (2 pi)^-1/2 int psi(x) e^{-ipx} dx
    return np.sqrt(S_)*np.exp(-S_*p**2/2)*(np.exp(-1j*p*A_) + C_*np.exp(1j*p*A_))
xg = np.linspace(-9, 9, 721); dx = xg[1] - xg[0]
norm = np.sqrt(np.sum(np.abs(psi(xg))**2)*dx)
check("Fourier pair is consistent (Parseval)", abs(np.sum(np.abs(psit(xg))**2)*dx/norm**2 - 1) < 1e-10)
# Wigner function W(x, p) = (1/pi) int psi*(x+y) psi(x-y) e^{2ipy} dy
yg = xg.copy(); pg = np.linspace(-9, 9, 721); dp = pg[1] - pg[0]
X, Yy = np.meshgrid(xg, yg, indexing="ij")
prod = np.conj(psi(X + Yy))*psi(X - Yy)/norm**2
W = (prod @ np.exp(2j*np.outer(yg, pg))).real*dx/np.pi
check("Wigner marginal over p is |psi(x)|^2", np.max(np.abs(W.sum(1)*dp - np.abs(psi(xg))**2/norm**2)) < 1e-8)
check("Wigner marginal over x is |psi~(p)|^2", np.max(np.abs(W.sum(0)*dx - np.abs(psit(pg))**2/norm**2)) < 1e-8)
def I_marginal(Wgrid, K_sign):
    # I_K[W] = int_{L+} du ( int_{L-} dv W )^2 ; at K = +K_ref, L+ = x-axis; at K = -K_ref, L+ = p-axis
    return float(np.sum((Wgrid.sum(1)*dp)**2)*dx) if K_sign > 0 else float(np.sum((Wgrid.sum(0)*dx)**2)*dp)
Ix, Ip = I_marginal(W, +1), I_marginal(W, -1)
check("vacuum +K_ref: I = int |psi(x)|^4 dx (local in x)", abs(Ix - np.sum(np.abs(psi(xg))**4)*dx/norm**4) < 1e-8,
      f"{Ix:.6f}")
check("vacuum -K_ref: I = int |psi~(p)|^4 dp (local in p)", abs(Ip - np.sum(np.abs(psit(pg))**4)*dp/norm**4) < 1e-8,
      f"{Ip:.6f}")
check("the two vacua give different physics for the same state", abs(Ix - Ip) > 0.05*max(Ix, Ip),
      f"{Ix:.4f} vs {Ip:.4f}")
check("quoted: 0.4070 vs 0.3600", round(Ix, 4) == 0.4070 and round(Ip, 4) == 0.3600)
# round-4 F5: I_K needs a scale on L+ (from H); rescaling u -> u/s multiplies the density by s and I by s
dens = np.abs(psi(xg))**2/norm**2
I_s2 = float(np.sum((2*np.interp(2*xg, xg, dens, left=0, right=0))**2)*dx)
check("I_K is not K-covariant alone: rescaling the L+ coordinate by 2 doubles it (it needs H)",
      abs(I_s2/Ix - 2) < 1e-3, f"{Ix:.4f} -> {I_s2:.4f}")
# rho acts on states by the Fourier transform: psi -> psi~, and on K by K -> -K
Wrho = W.T[:, ::-1]   # W_{F psi}(x, p) = W_psi(-p, x): rotation of the phase plane
check("rho-covariance: I_{-K}[W_{F psi}] = I_{+K}[W_psi]", abs(I_marginal(Wrho, -1) - Ix) < 1e-8)
check("a K-blind phase-space interaction int W^2 (= 1/(2 pi) for pure states) shows no asymmetry",
      abs(np.sum(W**2)*dx*dp - np.sum(Wrho**2)*dx*dp) < 1e-8 and abs(np.sum(W**2)*dx*dp - 1/(2*np.pi)) < 1e-6)

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — S5 (weak form) and the section-condition structure check out.")
