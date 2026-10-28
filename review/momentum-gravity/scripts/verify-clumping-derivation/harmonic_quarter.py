"""Quarter period of a uniform-density core: Omega^2 = 4 pi G rho/3 = 1/(3 t_ff^2)."""
import numpy as np
q = (np.pi/2)*np.sqrt(3)
print(f'harmonic core: Omega = t_ff^-1/sqrt(3) = {1/np.sqrt(3):.4f}/t_ff; quarter period (pi/2)/Omega = {q:.3f} t_ff')
for n, t in [('dwarf', 25.92), ('MW local', 40.98), ('cluster', 149.62)]:
    print(f'  {n}: quarter period = {q*t:.1f} Myr')
