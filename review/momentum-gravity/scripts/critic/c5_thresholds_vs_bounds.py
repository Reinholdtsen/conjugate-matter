"""Critic check c5: clumping thresholds of the long-range gated model (clumping
analysis C3/C10, local homogeneous model, Gaussian gate W = exp(-s^2/2), no
re-virialization) against the observational bounds of the dark-tests analysis and
of this critic's c4/c4b, across v*.  No analysis made this comparison except at
v* = 120 km/s (clumping numbers verifier, Sgr only).

Static l = 0 operator (units sigma = 1, r = sigma/v*):
  K(v,v') = sqrt(p0 p0') [1 + g W0(v,v')],  W0 = exp(-(v^2+v'^2) r^2/2) sinh(v v' r^2)/(v v' r^2),
  measure 4 pi v'^2 dv',  p0 the unit Maxwellian.  Lambda_0 = top eigenvalue.
Anchors (independent of this code): Lambda_g closed form [1/2 + r^2 + sqrt(1+4r^2)/2]^(-3/2)
(Mehler), and gravity alone Lambda_0 = 1; cross-check against the clumping
analysis numbers (Lambda_0(1.2917, 10) = 2.30503422; g_crit(1.2917, 4.4) = 24.45;
g_crit(8.333, 1.1) = 157.3).
Validity of the local (swindle) model, from the clumping derivation verifier:
anomalous-velocity ratio per unit g = 4.5 r^2 (1+r^2)^(-5/2) must stay < 1.
"""
import numpy as np

def make_grid(n=500, vmax=9.0):
    x, w = np.polynomial.legendre.leggauss(n)
    v = 0.5 * vmax * (x + 1); wv = 0.5 * vmax * w
    return v, wv
V, WV = make_grid()
p0 = (2 * np.pi) ** -1.5 * np.exp(-V**2 / 2)
meas = 4 * np.pi * V**2 * WV
sq = np.sqrt(p0 * meas)

def W0(r):
    a = np.outer(V, V) * r**2
    with np.errstate(over='ignore', invalid='ignore'):
        # sinh(a)/a * exp(-(v^2+v'^2) r^2/2) computed stably: exp(a - ...)(1 - exp(-2a))/(2a)
        e = np.exp(a - (V[:, None]**2 + V[None, :]**2) * r**2 / 2)
        s = np.where(a > 1e-8, (1 - np.exp(-2 * a)) / (2 * np.where(a > 1e-8, a, 1)), 1.0)
        return e * s

def Lam0(g, r, Wm=None):
    if Wm is None: Wm = W0(r)
    K = sq[:, None] * (1 + g * Wm) * sq[None, :]
    return np.linalg.eigvalsh(K)[-1]
def Lam_g_closed(r): return (0.5 + r**2 + np.sqrt(1 + 4 * r**2) / 2) ** -1.5
def g_crit(Q, r):
    Wm = W0(r)
    if Lam0(0, r, Wm) >= Q: return 0.0
    lo, hi = 0.0, 1.0
    while Lam0(hi, r, Wm) < Q: hi *= 2
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if Lam0(mid, r, Wm) < Q: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

# anchors
for r in (0.25, 1.2917, 8.333):
    Wm = W0(r)
    Kg = sq[:, None] * Wm * sq[None, :]
    print(f"anchor r = {r}: Lambda_g numeric = {np.linalg.eigvalsh(Kg)[-1]:.7f}, closed = {Lam_g_closed(r):.7f}")
print(f"anchor gravity alone: Lambda_0 = {Lam0(0, 1.0):.7f}")
print(f"cross-check: Lambda_0(1.2917, 10) = {Lam0(10, 1.2917):.8f} (clumping C3: 2.30503422); "
      f"g_crit(1.2917, 4.4) = {g_crit(4.4, 1.2917):.2f} (C5: 24.45); g_crit(8.333, 1.1) = {g_crit(1.1, 8.333):.1f} (C5: 157.3)")

# bounds (eps_max) from c4 (reading a = dark-tests K4) and c4b (consistent reading), compressed DESI, matter ratio
lya_a = {10: 3.04, 30: 0.344, 50: 0.128, 120: 0.0282, 300: 0.0138}
lya_c = {10: 6.80, 30: 0.817, 50: 0.348, 120: 0.341, 300: 0.0113}
def sgr(vs, V=311.1, s=149.9):
    Wv = (vs**2 / (vs**2 + s**2))**1.5 * np.exp(-V**2 / (2 * (vs**2 + s**2)))
    return 0.10 / Wv
envs = [("UFD", 4.0, (1.0966, 4.3865)), ("classical dSph", 10.0, (1.0966, 4.3865)),
        ("dwarf core", 30.0, (1.0966, 4.3865)), ("MW local", 155.0, (4.9348, 24.77)),
        ("cluster core", 1000.0, (1.0966, 4.3865))]
print("\nper v*: g_crit(Q_low), g_crit(Q_high) [no re-virialization]; stream crossover 1/Lambda_g; "
      "local-model validity g < 1/(4.5 r^2 (1+r^2)^-2.5)")
for vs in (10, 30, 50, 120, 300):
    print(f"\nv* = {vs} km/s: Lyman-alpha eps_max (matter ratio) K4 reading {lya_a[vs]}, consistent reading {lya_c[vs]}; "
          f"Sgr eps_max = {sgr(vs):.3g}")
    for name, sig, (Ql, Qh) in envs:
        r = sig / vs
        if r <= 10:
            gl, gh = g_crit(Ql, r), g_crit(Qh, r)
        else:   # gate narrower than the grid resolves: narrow-gate asymptote Q/Lambda_g (clumping C5)
            gl, gh = Ql / Lam_g_closed(r), Qh / Lam_g_closed(r)
            name = name + "*"
        cross = 1 / Lam_g_closed(r)
        valid = 1 / (4.5 * r**2 * (1 + r**2) ** -2.5)
        best = min(lya_c[vs], sgr(vs))
        print(f"  {name:15s} r = {r:7.3f}: g_crit = {gl:9.3g}, {gh:9.3g}; crossover {cross:9.3g}; validity < {valid:9.3g}; "
              f"threshold/allowed(consistent, Sgr) = {max(gl, cross)/best:8.3g}")
