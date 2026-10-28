"""v3_ratios.py -- small ratios quoted in the verdicts (iron rule)."""
W_bullet = 1.0407e-04            # v3_misc.out, Gaussian, v*=120
for F in (0.4, 1.2):
    e = F/W_bullet
    print(f"Farrar-Rosen {F} x gravity needs eps = {e:.3e}; / agent bound 0.0285 = {e/0.0285:.2e}; / Hamiltonian bound 0.0573 = {e/0.0573:.2e}; / force-law bound 0.0585 = {e/0.0585:.2e}")
print(f"R(1.08)/R1(1.08) = {0.803130/0.311446:.3f}")
print(f"Sgr eta/<W>: {0.271/0.0656:.2f} .. {0.490/0.0656:.2f};  10% criterion with |eta| = 0.27-0.49: eps < {0.1/0.49:.2f} .. {0.1/0.27:.2f}")
print(f"eBOSS chi2 drop at v*=120 (Hamiltonian): {26.31-1.89:.2f}; at v*=30: {26.31-2.49:.2f}")
print(f"singular eps threshold (Gaussian, i): 2*0.934/Omega_c with Omega_c in [0.835, 0.84]: {2*0.934/0.84:.2f} .. {2*0.934/0.835:.2f}; (ii): {2*1.0/0.84:.2f} .. {2*1.0/0.835:.2f}")
