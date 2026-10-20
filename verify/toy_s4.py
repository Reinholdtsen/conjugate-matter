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
T_LOW, T_HIGH, H = 0.6, 3.0, 1.0

print("== Model A: with the tau-type potential (h = 1), T = 0.6")
A = {L: run(L, T_LOW, H, seed=L) for L in SIZES}
for L in SIZES:
    print(f"      L={L:3d}: <|m|> = {A[L][0]:.4f}, Binder = {A[L][1]:.4f}")
check("ordered: <|m|> stays above 0.8 at every size", min(A[L][0] for L in SIZES) > 0.8)
check("and is size-independent (changes < 2% from L = 16 to 64)",
      abs(A[64][0]/A[16][0] - 1) < 0.02, f"ratio {A[64][0]/A[16][0]:.4f}")
check("Binder cumulant near 2/3 (an ordered Z2 phase)", min(A[L][1] for L in SIZES) > 0.6)

print("\n== Control: model A at high temperature, T = 3.0")
C = {L: run(L, T_HIGH, H, seed=100 + L) for L in SIZES}
for L in SIZES:
    print(f"      L={L:3d}: <|m|> = {C[L][0]:.4f}, Binder = {C[L][1]:.4f}")
check("disordered: <|m|> falls with size (L = 64 below half of L = 16)", C[64][0] < 0.5*C[16][0],
      f"{C[16][0]:.4f} -> {C[64][0]:.4f}")

print("\n== Model B: exactly self-dual (h = 0), T = 0.6")
B = {L: run(L, T_LOW, 0.0, seed=200 + L) for L in SIZES}
for L in SIZES:
    print(f"      L={L:3d}: <|M|> = {B[L][2]:.4f}, <|m|> = {B[L][0]:.4f}")
eta = T_LOW/(2*np.pi)
pred = (64/16)**(-eta/2)
check("no true order: the U(1) magnetization falls with size (> 3% from L = 16 to 64)",
      B[64][2]/B[16][2] < 0.97, f"ratio {B[64][2]/B[16][2]:.4f}; spin-wave estimate {pred:.4f}")

if failures:
    print(f"\nFAILED {len(failures)} check(s): " + "; ".join(failures))
    sys.exit(1)
print("\nOK — S4: rho is spontaneously broken in 1+1 only with the tau-type potential.")
