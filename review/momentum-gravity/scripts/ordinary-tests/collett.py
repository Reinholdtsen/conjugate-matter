"""Galaxy-scale lensing vs dynamics (Collett et al. 2018: gamma = 0.97 +- 0.09, 68%).
Photons outside the gate: gamma_eff - 1 = -2 eps <K> (same algebra as the Cassini case)."""
g, s = 0.97 - 1.0, 0.09
lo, hi = -(g + 2*s)/2, -(g - 2*s)/2
print(f"eps*<K> in [{lo:.3f}, {hi:.3f}] (2 sigma) -> |eps <K>| < {max(abs(lo), abs(hi)):.3f}")
