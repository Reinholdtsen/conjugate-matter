#!/usr/bin/env python3
"""
toy_s4.py — criterion S4 for the coset toy (notes/toy-lagrangian.md, chunk 3):
does the spontaneous breaking of rho survive fluctuations in 1+1 dimensions?

    .venv/bin/python verify/toy_s4.py

Exit code 1 if any check fails. Fixed seeds, so the run is deterministic.

At H = 1 the coset toy's polarization field is the angle phi of
K(phi) = [[cos phi, sin phi], [sin phi, -cos phi]]; rho acts as phi -> phi + pi.
Its kinetic term (f_K^2/4) Tr(dK^T dK) = (f_K^2/2)(d phi)^2 is an XY stiffness.
The tau-type potential -mu [Tr(K K_ref)]^2 = -2 mu (1 + cos 2 phi) keeps rho and
leaves two vacua, phi = 0 and pi (K = +K_ref, -K_ref), exchanged by rho.
On a square lattice (Euclidean 2D):
    E = -J sum_<ij> cos(phi_i - phi_j) - h sum_i cos(2 phi_i).
Model A: h > 0 (with the tau potential). Model B: h = 0 (exactly self-dual).
Order parameter for rho: m = mean cos(phi) (odd under phi -> phi + pi).
This is the FROZEN-H reduction of the coset toy (H = 1 held fixed); the unreduced
model's stability with the bounded potential V_b is checked in toy_coset.py.
Note: the energy here is the frozen-H form, -h cos(2 phi), which equals the bounded
V_b at H = 1 up to a constant and a factor (both depend on phi only through cos 2 phi).
All runs use a cold start (phi = 0). Error bars: standard error over 4 independent seeds.
For model B the natural order parameter is the U(1) magnetization |mean exp(i phi)|.
"""
import sys
import numpy as np

failures = []
def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        failures.append(name)

def run(L, T, h, J=1.0, therm=1500, sweeps=4000, seed=0):
    rng = np.random.default_rng(seed)
    phi = np.zeros((L, L))                      # ordered start; equilibration tested by the high-T control
    ii, jj = np.indices((L, L))
    masks = [(ii + jj) % 2 == 0, (ii + jj) % 2 == 1]
    step = 1.0
    ms, Ms = [], []
    for s in range(therm + sweeps):
        for mask in masks:
            prop = phi + rng.uniform(-step, step, size=phi.shape)
            nb = [np.roll(phi, 1, 0), np.roll(phi, -1, 0), np.roll(phi, 1, 1), np.roll(phi, -1, 1)]
            dE = -J*sum(np.cos(prop - n) - np.cos(phi - n) for n in nb) - h*(np.cos(2*prop) - np.cos(2*phi))
            acc = mask & (rng.random(phi.shape) < np.exp(-np.clip(dE, -50, 50)/T))
            phi = np.where(acc, prop, phi)
        if s >= therm:
            ms.append(np.mean(np.cos(phi)))
            Ms.append(abs(np.mean(np.exp(1j*phi))))
    ms, Ms = np.array(ms), np.array(Ms)
    binder = 1 - np.mean(ms**4)/(3*np.mean(ms**2)**2)
    return np.mean(np.abs(ms)), binder, np.mean(Ms)

SIZES = (16, 32, 64)
SEEDS = 4
T_LOW, T_HIGH, H = 0.6, 3.0, 1.0
def stats(L, T, h, base):
    r = np.array([run(L, T, h, seed=base + 1000*k) for k in range(SEEDS)])
    mean = r.mean(0); sem = r.std(0, ddof=1)/np.sqrt(SEEDS)
    return mean, sem

print("== Model A: with the rho-preserving potential (h = 1), T = 0.6")
A = {L: stats(L, T_LOW, H, L) for L in SIZES}
for L in SIZES:
    print(f"      L={L:3d}: <|m|> = {A[L][0][0]:.4f} +- {A[L][1][0]:.4f}, Binder = {A[L][0][1]:.4f}")
check("ordered: <|m|> > 0.8 at every size", min(A[L][0][0] for L in SIZES) > 0.8)
sig = np.hypot(A[64][1][0], A[16][1][0])
check("size-independent within errors (|m64 - m16| < 3 sigma + 0.002)",
      abs(A[64][0][0] - A[16][0][0]) < 3*sig + 0.002, f"diff {A[64][0][0] - A[16][0][0]:.4f}, sigma {sig:.4f}")
check("Binder cumulant near 2/3 (an ordered Z2 phase)", min(A[L][0][1] for L in SIZES) > 0.6)
check("quoted: <|m|> = 0.954 +- 0.0001 at every size, Binder 0.667",
      all(round(A[L][0][0], 3) == 0.954 and A[L][1][0] < 0.0002 and round(A[L][0][1], 3) == 0.667 for L in SIZES))

print("\n== Control: model A at high temperature, T = 3.0")
C = {L: stats(L, T_HIGH, H, 100 + L) for L in SIZES}
for L in SIZES:
    print(f"      L={L:3d}: <|m|> = {C[L][0][0]:.4f} +- {C[L][1][0]:.4f}")
ratio_c = C[16][0][0]/C[64][0][0]
check("disordered: <|m|> scales as 1/L (m16/m64 within [3.3, 4.8], expected 4)", 3.3 < ratio_c < 4.8, f"{ratio_c:.3f}")
check("quoted: 0.0653 +- 0.0043, 0.0338 +- 0.0013, 0.0155 +- 0.0004",
      [(round(C[L][0][0], 4), round(C[L][1][0], 4)) for L in SIZES] == [(0.0653, 0.0043), (0.0338, 0.0013), (0.0155, 0.0004)])

print("\n== Model B: exactly symmetric (h = 0), T = 0.6")
B = {L: stats(L, T_LOW, 0.0, 200 + L) for L in SIZES}
for L in SIZES:
    print(f"      L={L:3d}: <|M|> = {B[L][0][2]:.4f} +- {B[L][1][2]:.4f}")
eta = T_LOW/(2*np.pi)
pred = (64/16)**(-eta/2)
sigB = np.hypot(B[64][1][2], B[16][1][2])
check("no true order: the U(1) magnetization falls with size by more than 3 sigma",
      B[16][0][2] - B[64][0][2] > 3*sigB, f"ratio {B[64][0][2]/B[16][0][2]:.4f}; spin-wave estimate {pred:.4f}")
check("quoted: 0.8369 +- 0.0007, 0.8025 +- 0.0039, 0.7736 +- 0.0038; ratio 0.924 vs spin-wave 0.936",
      [(round(B[L][0][2], 4), round(B[L][1][2], 4)) for L in SIZES] == [(0.8369, 0.0007), (0.8025, 0.0039), (0.7736, 0.0038)]
      and round(B[64][0][2]/B[16][0][2], 3) == 0.924 and round(pred, 3) == 0.936)

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — S4: rho is spontaneously broken in 1+1 (frozen-H reduction) only with the rho-preserving potential.")
