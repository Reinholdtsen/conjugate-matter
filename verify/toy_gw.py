#!/usr/bin/env python3
"""
toy_gw.py — the Grosse-Wulkenhaar route for the toy Lagrangian
(notes/toy-lagrangian.md, chunk 2): does the self-dual (Omega = 1) model
spontaneously break the Langmann-Szabo x <-> p duality?

    .venv/bin/python verify/toy_gw.py

Exit code 1 if any check fails. theta = 1 throughout.

Inputs taken from the sources, not from memory:
  - matrix base (de Goursac-Tanasa-Wallet 0709.3950, App. A): f_00 = 2 exp(-x^2/theta),
    f_mn = (m! n! theta^(m+n))^(-1/2) abar^*m * f_00 * a^*n, H * f_mn = theta (m+1/2) f_mn,
    f_mn * H = theta (n+1/2) f_mn, f_mn^dagger = f_nm, f_mn * f_kl = delta_nk f_ml;
  - the duality (Grosse-Wulkenhaar hep-th/0402093, eq. 1): phi^(p) <-> pi sqrt|det theta| phi(x),
    p = xtilde = 2 theta^-1 x, with the sign of the Fourier exponent alternating
    around the star-product vertex.
The explicit Laguerre form of f_mn used below is checked against the first
two properties exactly (sympy), so it is not taken on trust.
"""
import sys
from math import factorial, pi
import numpy as np
import sympy as sp

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)

# ---- explicit matrix base, symbolic
x1, x2 = sp.symbols("x1 x2", real=True)
TH = sp.Integer(1)
def f_sym(m, n):
    if n < m:
        return sp.conjugate(f_sym(n, m))
    l = n - m
    r2 = x1**2 + x2**2
    return (2*(-1)**m*sp.sqrt(sp.factorial(m)/sp.factorial(n))*(sp.sqrt(2/TH))**l*(x1 + sp.I*x2)**l
            * sp.assoc_laguerre(m, l, 2*r2/TH)*sp.exp(-r2/TH))
def H_left(g):   # H * g for H = (x1^2 + x2^2)/2, exact (the series stops at second order)
    return ((x1**2 + x2**2)/2*g + sp.I*TH/2*(x1*sp.diff(g, x2) - x2*sp.diff(g, x1))
            - TH**2/8*(sp.diff(g, x1, 2) + sp.diff(g, x2, 2)))
def H_right(g):  # g * H
    return ((x1**2 + x2**2)/2*g - sp.I*TH/2*(x1*sp.diff(g, x2) - x2*sp.diff(g, x1))
            - TH**2/8*(sp.diff(g, x1, 2) + sp.diff(g, x2, 2)))

print("== Anchors: the explicit matrix base")
ok_l = ok_r = True
for m in range(3):
    for n in range(3):
        f = f_sym(m, n)
        ok_l &= sp.simplify(H_left(f) - TH*(m + sp.Rational(1, 2))*f) == 0
        ok_r &= sp.simplify(H_right(f) - TH*(n + sp.Rational(1, 2))*f) == 0
check("H * f_mn = theta (m+1/2) f_mn for m, n <= 2 (exact)", ok_l)
check("f_mn * H = theta (n+1/2) f_mn for m, n <= 2 (exact)", ok_r)
check("f_00 = 2 exp(-x^2/theta) as in 0709.3950 (A.2)", sp.simplify(f_sym(0, 0) - 2*sp.exp(-(x1**2 + x2**2))) == 0)

# ---- numerics on a grid
NMAX = 4
fnum = {(m, n): sp.lambdify((x1, x2), f_sym(m, n), "numpy") for m in range(NMAX) for n in range(NMAX)}
L, NG = 6.0, 241
g = np.linspace(-L, L, NG); dA = (g[1] - g[0])**2
Y1, Y2 = np.meshgrid(g, g, indexing="ij")
F = {k: np.asarray(fn(Y1, Y2), dtype=complex)*np.ones_like(Y1) for k, fn in fnum.items()}
gram = max(abs(np.sum(np.conj(F[(k, l)])*F[(m, n)])*dA - (2*pi if (k, l) == (m, n) else 0))
           for k in range(NMAX) for l in range(NMAX) for m in range(NMAX) for n in range(NMAX))
check("orthogonality: int conj(f_kl) f_mn = 2 pi theta delta delta (grid)", gram < 1e-8, f"max dev {gram:.1e}")
check("int f_mn = 2 pi theta delta_mn (grid)",
      max(abs(np.sum(F[(m, n)])*dA - (2*pi if m == n else 0)) for m in range(NMAX) for n in range(NMAX)) < 1e-8)

print("\n== The duality on the matrix base")
rng = np.random.default_rng(7)
pts = rng.uniform(-2.0, 2.0, size=(12, 2))
def dual_at(fgrid, X1, X2):
    # (D f)(x) = (1/(pi theta)) int d^2y exp(-i xtilde.y) f(y), xtilde = 2 theta^-1 x, theta_12 = theta
    xt1, xt2 = -2*X2, 2*X1
    return np.sum(np.exp(-1j*(xt1*Y1 + xt2*Y2))*fgrid)*dA/pi
check("anchor: D f_00 = f_00 (the normalization pi sqrt|det theta|)",
      max(abs(dual_at(F[(0, 0)], *p) - fnum[(0, 0)](*p)) for p in pts) < 1e-8)
dev = {}
for (m, n), fg in F.items():
    dev[(m, n)] = max(abs(dual_at(fg, *p) - (-1)**m*complex(fnum[(m, n)](*p))) for p in pts)
check("D f_mn = (-1)^m f_mn for all m, n < 4: the duality is left multiplication by parity",
      max(dev.values()) < 1e-7, f"max dev {max(dev.values()):.1e}")

print("\n== The Omega = 1 kinetic form in the matrix base")
dF = {}
for (m, n) in F:   # exact derivatives, evaluated on the grid
    d1 = sp.lambdify((x1, x2), sp.diff(f_sym(m, n), x1), "numpy")
    d2 = sp.lambdify((x1, x2), sp.diff(f_sym(m, n), x2), "numpy")
    dF[(m, n)] = (np.asarray(d1(Y1, Y2), dtype=complex)*np.ones_like(Y1),
                  np.asarray(d2(Y1, Y2), dtype=complex)*np.ones_like(Y1))
Q = np.zeros((NMAX*NMAX, NMAX*NMAX), dtype=complex)
keys = list(F)
for i, a in enumerate(keys):
    ga = dF[a]
    for j, b in enumerate(keys):
        gb = dF[b]
        Q[i, j] = np.sum(np.conj(ga[0])*gb[0] + np.conj(ga[1])*gb[1] + 4*(Y1**2 + Y2**2)*np.conj(F[a])*F[b])*dA
diag = np.array([Q[i, i].real/(keys[i][0] + keys[i][1] + 1) for i in range(len(keys))])
off = np.max(np.abs(Q - np.diag(np.diag(Q))))
check("int |d phi|^2 + xtilde^2 |phi|^2 is diagonal in the matrix base", off < 1e-3*np.max(np.abs(Q)), f"max off-diag {off:.1e}")
check("and proportional to (m + n + 1)", np.ptp(diag) < 1e-3*np.mean(diag), f"ratio {np.mean(diag):.4f} (8 pi = {8*pi:.4f})")

print("\n== S1: is the duality a symmetry of the field space?")
N = 8
Pi = np.diag([(-1.0)**m for m in range(N)])
idx = np.add.outer(np.arange(N), np.arange(N)) + 1.0
def S_complex(phi, mu2=0.0, lam=1.0):
    P = phi.conj().T @ phi
    return float(np.sum((idx - mu2)*np.abs(phi)**2) + lam*np.trace(P @ P).real)
phis = [rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)) for _ in range(5)]
check("complex model: S[Pi phi] = S[phi] (duality is a field symmetry)",
      max(abs(S_complex(Pi @ p, 3.0) - S_complex(p, 3.0)) for p in phis) < 1e-9)
def diag_unitary():
    return np.diag(np.exp(1j*rng.uniform(0, 2*pi, N)))
check("complex model: S[U phi V^dag] = S[phi] for any diagonal unitaries U, V (a continuous U(1)^N x U(1)^N)",
      max(abs(S_complex(diag_unitary() @ p @ diag_unitary().conj().T, 3.0) - S_complex(p, 3.0)) for p in phis) < 1e-9)
herm = [(lambda a: a + a.conj().T)(rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))) for _ in range(5)]
check("real model: Pi phi is not Hermitian, so the duality leaves the real field space",
      min(np.max(np.abs(Pi @ h - (Pi @ h).conj().T)) for h in herm) > 1e-3)
check("real model: Tr((Pi phi)^4) != Tr(phi^4); the real action is only covariant (alternating legs)",
      min(abs(np.trace(np.linalg.matrix_power(Pi @ h, 4)) - np.trace(np.linalg.matrix_power(h, 4))) for h in herm) > 1e-3)
check("real model: its quartic is invariant in the alternating form Tr((psi psi^dag)^2), psi = Pi phi",
      max(abs(np.trace((Pi @ h @ (Pi @ h).conj().T) @ (Pi @ h @ (Pi @ h).conj().T)) - np.trace(np.linalg.matrix_power(h, 4)))
          for h in herm) < 1e-8)

print("\n== S2: vacua of the complex model (mu2 = 4: levels 0 and 1 condense)")
MU2, LAM = 4.0, 1.0
def descend(phi, steps=20000, eta=0.02):
    for _ in range(steps):
        phi = phi - eta*((idx - MU2)*phi + 2*LAM*(phi @ phi.conj().T @ phi))
    return phi
q_exact = np.array([max(0.0, -(2*m + 1 - MU2)/(2*LAM)) for m in range(N)])
S_exact = -np.sum(np.minimum(0, 2*np.arange(N) + 1 - MU2)**2)/(4*LAM)
vacua = [descend(0.3*(rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)))) for _ in range(6)]
check("every minimum found is diagonal", max(np.max(np.abs(v - np.diag(np.diag(v)))) for v in vacua) < 1e-6)
check("with |phi_mm|^2 = q_m = max(0, -(2m+1-mu2)/(2 lam))",
      max(np.max(np.abs(np.abs(np.diag(v))**2 - q_exact)) for v in vacua) < 1e-6, f"q = {q_exact[:3]}")
check("and S_min = -sum (2m+1-mu2)^2/(4 lam)", max(abs(S_complex(v, MU2) - S_exact) for v in vacua) < 1e-8, f"{S_exact}")
phases = [np.angle(np.diag(v)[1]/np.diag(v)[0]) for v in vacua]
check("the relative phase beta of levels 0 and 1 varies across minima (a flat direction)",
      np.ptp(phases) > 0.5, f"betas {np.round(phases, 2)}")
def vac(beta):
    return np.diag(np.sqrt(q_exact)*np.exp(1j*np.array([0.0, beta] + [0.0]*(N - 2))))
check("S is constant around the vacuum circle beta (Goldstone direction)",
      np.ptp([S_complex(vac(b), MU2) for b in np.linspace(0, 2*pi, 13)]) < 1e-12)
check("the duality maps vacuum beta to vacuum beta + pi", np.allclose(Pi @ vac(0.7), vac(0.7 + pi)))
check("no vacuum is duality-invariant once level 1 condenses (|phi_11| > 0)", np.sqrt(q_exact[1]) > 0.1)
check("the duality is the beta -> beta + pi element of the left phase rotations exp(-i alpha N)",
      np.allclose(np.diag(np.exp(-1j*pi*np.arange(N))), Pi))

print("\n== S3/S5 start: x-versus-p polarization of the vacuum profile")
def profile(beta):
    return np.sqrt(q_exact[0])*F[(0, 0)] + np.sqrt(q_exact[1])*np.exp(1j*beta)*F[(1, 1)]
def moment(fg):
    return float(np.sum((Y1**2 + Y2**2)*np.abs(fg)**2)*dA)
def dual_profile(beta):
    return np.sqrt(q_exact[0])*F[(0, 0)] - np.sqrt(q_exact[1])*np.exp(1j*beta)*F[(1, 1)]
check("dual of the vacuum profile computed two ways agrees (grid FT vs (-1)^m rule)",
      max(abs(dual_at(profile(0.4), *p) - (np.sqrt(q_exact[0])*fnum[(0, 0)](*p)
          - np.sqrt(q_exact[1])*np.exp(0.4j)*fnum[(1, 1)](*p))) for p in pts) < 1e-7)
betas = np.linspace(0, 2*pi, 9)
Delta = np.array([moment(profile(b)) - moment(dual_profile(b)) for b in betas])
D0 = Delta[0]
check("Delta(beta) = <x^2>_vacuum - <x^2>_dual is nonzero at beta = 0 and flips sign at beta = pi",
      abs(D0) > 1e-2 and abs(Delta[4] + D0) < 1e-8, f"Delta(0) = {D0:.4f}")
check("Delta(beta) = Delta(0) cos(beta): the polarization is an angle on the Goldstone circle",
      np.max(np.abs(Delta - D0*np.cos(betas))) < 1e-8)

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — Grosse-Wulkenhaar route checks pass.")
