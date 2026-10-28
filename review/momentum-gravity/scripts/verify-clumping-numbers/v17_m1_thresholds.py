"""Verifier v17: static existence thresholds of the gate-only m=+-1 (l=1) mode in the local model:
no re-virialization: gt*Lambda_g*q > Q;  agent's re-virialization model: gt*Lambda_g*q > Q (1 + gt <W>).
Lambda_g, q, <W> closed forms (verified numerically in v01, v03)."""
import numpy as np
def LG(r): return (0.5 + r*r + np.sqrt(1 + 4*r*r)/2) ** -1.5
def Q_(r): return 2*r*r/(1 + 2*r*r + np.sqrt(1 + 4*r*r))
def W(r): return (1 + 2*r*r) ** -1.5
for name, r, Qs in [('dwarf', 0.25, [np.pi**2/9, 4*np.pi**2/9]), ('MW', 155/120, [np.pi**2/2, 2*np.pi**2, 24.7714]),
                    ('cluster', 1000/120, [np.pi**2/9, 4*np.pi**2/9])]:
    a = LG(r) * Q_(r)
    print(f"{name}: Lambda_g q = {a:.5e}, <W> = {W(r):.5e}, cap Lambda_g q/<W> = {a/W(r):.4f}")
    for Q in Qs:
        nr = Q / a
        den = a - Q * W(r)
        rv = Q / den if den > 0 else float('inf')
        print(f"   Q={Q:.4f}: m=+-1 threshold no-revir gt={nr:.4g}, revir gt={rv:.4g}")
