import numpy as np, sys
sys.argv = ["x"]
src = open("verify/toy_s4.py").read().split("SIZES = ")[0]
exec(src.replace("failures = []", "failures = []").replace('import sys\n', ''))
for seed in (116, 1, 2, 3):
    r = run(16, 3.0, 1.0, seed=seed)
    print(f"L=16 T=3 seed={seed}: <|m|> = {r[0]:.4f}")
r = run(16, 3.0, 1.0, seed=5, therm=2000, sweeps=40000)
print(f"L=16 T=3 long run (40000 sweeps): <|m|> = {r[0]:.4f}")
for L in (32, 64):
    r = run(L, 3.0, 1.0, seed=7, sweeps=20000)
    print(f"L={L} T=3 long run: <|m|> = {r[0]:.4f}")
