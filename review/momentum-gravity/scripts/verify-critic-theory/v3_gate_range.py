"""
v3_gate_range.py  (verify-critic-theory, round 3) -- item 4, 'gate-range'.

Question: the record's gate F(k^2/mu^2) acts on the incoming relative momentum k of two chi
quanta; its contact range comes from integrating out massive X. If the carrier of the
transfer were light, would the gate survive at separations r >> hbar/mu?

Model (non-relativistic, relative coordinate, hbar = mu = 1): the Hermitian form of the
record's factorized amplitude M(k,q) = V~(q) F(k^2/mu^2) is the sandwich
        A = F^{1/2}(p) V(x) F^{1/2}(p).
(a) Weyl symbol: for B = f(p) e^{iqx} g(p), W_B = e^{iqx} f(p + hbar q/2) g(p - hbar q/2)
    (derived in the docstring of part a). For a Gaussian F this gives EXACTLY
    W_A(x,p) = F(p) * [V smoothed by a Gaussian of width ~hbar/mu](x).   (sympy check)
(b) Direct quantum test, no symbol needed: <psi|A|psi> for wavepackets of relative separation
    x0 and relative momentum p0, computed exactly on an FFT grid, compared with the classical
    gated expectation <F(p)V(x)> over the packet's Wigner function, for Gaussian and Lorentzian
    gates and long-range V.
(c) 3D Gaussian case with Coulomb V: the smoothed potential is erf(r mu/hbar)/r (quadrature).
(d) record numbers: mu, hbar/mu, the dimensionless x = c^2/v*^2 of the relativistic
    continuation exp(-(gamma-1) c^2/v*^2), mean interparticle spacings.
"""
import math
import numpy as np
import sympy as sp
import mpmath as mp

# ------------------------------------------------------------------ (a)
print("(a) Gaussian sandwich symbol")
p, a, mu = sp.symbols('p a mu', real=True)
F = sp.exp(-p ** 2 / mu ** 2)
lhs = sp.sqrt(F.subs(p, p + a) * F.subs(p, p - a))
rhs = F * sp.exp(-a ** 2 / mu ** 2)
print("  [sqrt(F(p+a) F(p-a))]^2 / [F(p) exp(-a^2/mu^2)]^2 =", sp.simplify(sp.powsimp(sp.expand(lhs**2 / rhs**2), force=True)), "(both sides positive)")
# 3D: vectors
px, py, pz, ax, ay, az = sp.symbols('px py pz ax ay az', real=True)
F3 = lambda X, Y, Z: sp.exp(-(X ** 2 + Y ** 2 + Z ** 2) / mu ** 2)
lhs3 = sp.sqrt(F3(px + ax, py + ay, pz + az) * F3(px - ax, py - ay, pz - az))
rhs3 = F3(px, py, pz) * sp.exp(-(ax ** 2 + ay ** 2 + az ** 2) / mu ** 2)
print("  3D version, ratio of squares:", sp.simplify(sp.powsimp(sp.expand(lhs3**2 / rhs3**2), force=True)))
print("  with a = hbar q/2: W_A(x,p) = F(p) * Int dq/(2pi) V~(q) e^{iqx} exp(-hbar^2 q^2/(4 mu^2))  [exact]")
# Weyl symbol of f(p) e^{iqx} g(p): <x1|B|x2> = Int dk/2pi f(k) g(k-q) e^{ik x1} e^{-i(k-q) x2};
# W(x,p) = Int dy e^{-ipy} <x+y/2|B|x-y/2> = Int dk f(k) g(k-q) e^{iqx} delta(k - q/2 - p) = f(p+q/2) g(p-q/2) e^{iqx}.

# ------------------------------------------------------------------ (b)
print("\n(b) exact quantum expectation of A = F^{1/2}(p) V(x) F^{1/2}(p) for wavepackets (hbar = mu = 1)")
Lbox, dx = 6000.0, 0.25
N = int(Lbox / dx)
x = (np.arange(N) - N // 2) * dx
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
print(f"  grid: N = {N}, dx = {dx}, |p|max = {np.max(np.abs(k)):.2f}, box = {Lbox}")

def expect(psi, Fhalf, V):
    phi = np.fft.ifft(Fhalf * np.fft.fft(psi))
    phi = V * phi
    phi = np.fft.ifft(Fhalf * np.fft.fft(phi))
    return (np.vdot(psi, phi) * dx).real

gates = {"Gaussian exp(-p^2)": lambda q: np.exp(-q ** 2),
         "Lorentzian 1/(1+p^2)": lambda q: 1.0 / (1.0 + q ** 2)}
Lr = 300.0
pots = {"exp(-|x|/300)": lambda X: np.exp(-np.abs(X) / Lr),
        "1/sqrt(x^2+1)": lambda X: 1.0 / np.sqrt(X ** 2 + 1.0)}
s = 6.0                                    # packet position width; momentum width 1/(2s)
for gname, Fg in gates.items():
    Fhalf = np.sqrt(Fg(k))
    for vname, Vf in pots.items():
        V = Vf(x)
        print(f"  gate {gname}, V = {vname}:")
        for x0 in [3.0, 10.0, 30.0, 100.0, 300.0, 1000.0]:
            row = []
            for p0 in [0.0, 1.0, 2.0]:
                psi = np.exp(-(x - x0) ** 2 / (4 * s * s) + 1j * p0 * x)
                psi /= np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
                q_exp = expect(psi, Fhalf, V)
                # classical gated expectation over the packet's Wigner function (product of Gaussians)
                gx = np.exp(-(x - x0) ** 2 / (2 * s * s)); gx /= gx.sum()
                pv = np.linspace(p0 - 8 / (2 * s), p0 + 8 / (2 * s), 4001)
                gp = np.exp(-(pv - p0) ** 2 * 2 * s * s); gp /= gp.sum()
                cl = np.sum(gx * V) * np.sum(gp * Fg(pv))
                ungated = np.sum(gx * V)
                row.append((q_exp / cl, q_exp / ungated))
            print(f"    x0 = {x0:6.0f}: quantum/classical-gated at p0=0,1,2: " +
                  ", ".join(f"{r[0]:.6f}" for r in row) +
                  " | quantum/ungated <V>: " + ", ".join(f"{r[1]:.5f}" for r in row))

# ------------------------------------------------------------------ (c)
print("\n(c) 3D, Gaussian gate, Coulomb V: smoothed potential vs erf(r)/r (hbar = mu = 1)")
mp.mp.dps = 30
for r in [0.5, 1.0, 2.0, 3.0, 10.0]:
    r = mp.mpf(r)
    # Int d^3q/(2pi)^3 (4pi/q^2) e^{iq.r} e^{-q^2/4} = (2/pi) Int_0^inf sin(q r)/(q r) e^{-q^2/4} dq
    val = (2 / mp.pi) * mp.quad(lambda q: mp.sin(q * r) / (q * r) * mp.e ** (-q * q / 4), [0, mp.inf])
    print(f"  r = {mp.nstr(r,3):>4}: smoothed*r = {mp.nstr(val * r, 10)},  erf(r) = {mp.nstr(mp.erf(r), 10)}")

# ------------------------------------------------------------------ (d)
print("\n(d) record numbers (m_chi = 70 MeV, v* = 120 km/s, v* = sqrt2 mu/m as in #1 s5.1 and #13 s4)")
c = 299792458.0
hbarc_MeVfm = 197.3269804
m = 70.0                                   # MeV
vstar = 120e3
mu_MeV = m * (vstar / c) / math.sqrt(2)
print(f"  mu c = {mu_MeV*1e3:.3f} keV;  hbar/mu = {hbarc_MeVfm/mu_MeV*1e-15:.3e} m")
print(f"  x = c^2/v*^2 = {(c/vstar)**2:.4e}  (= (m c/mu)^2/2 = {(m/mu_MeV)**2/2:.4e})")
for name, rho_GeV_cm3 in [("dwarf core, 1 GeV/cm^3", 1.0), ("MW local, 0.4 GeV/cm^3", 0.4)]:
    n = rho_GeV_cm3 * 1e3 / m              # per cm^3
    print(f"  {name}: n = {n:.2f} /cm^3, mean spacing n^(-1/3) = {n**(-1/3)*1e-2:.3e} m")
pp1, pp2, mm, gg = sp.symbols('p1 p2 m gamma', real=True)
print("  on shell, -(p1-p2)^2 = -2 m^2 + 2 p1.p2 = 2 m^2 (gamma - 1)   [p1.p2 = m^2 gamma, mostly-minus]")
