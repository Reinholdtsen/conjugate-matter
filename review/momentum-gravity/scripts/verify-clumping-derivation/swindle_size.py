"""Size of what the Jeans swindle drops in the gated model (C1 caveat, C10-C12, C20).
Background mean field of an isothermal halo with the Gaussian gate on canonical momenta:
  Phi(x,v) = -m Psi(x) [G + Gt Wavg(v)],  Psi = Int rho(x')/|x-x'| d^3x',
  Wavg(v) = Int p0(v') W(|v-v'|/v*) d^3v' = (1+r^2)^(-3/2) exp(-v^2 r^2/(2 sigma^2 (1+r^2)))   [D, Gaussian convolution]
Anomalous velocity grad_p Phi = Gt Psi v Wavg(v)/(sigma^2+v*^2), so for slow particles
  xdot = v [1 + (Gt/G)(G Psi/sigma^2) r^2 (1+r^2)^(-5/2)].
Potential depth: uniform sphere of the local density with radius r_c = 3 sigma t_ff (the local
model's own core): G Psi(0) = 2 pi G rho r_c^2 = 4.5 sigma^2 [D]. A real halo is deeper (the
envelope adds to Psi), so these ratios are lower bounds. Also printed: the Gibbs-state exponent
difference between v=0 and v=sigma, (Gt/G)(G Psi/sigma^2)[Wavg(0) - Wavg(sigma)]."""
import numpy as np
GPsi = 4.5
def ratio(r): return GPsi * r**2 * (1 + r**2) ** -2.5
def gibbs(r): return GPsi * (1 + r**2) ** -1.5 * (1 - np.exp(-r**2 / (2 * (1 + r**2))))
envs = {'dwarf': (30/120, [0.1152, 4.026]), 'MW': (155/120, [28.07, 127.5, 161.2, 280.7, 1000.0]),
        'cluster': (1000/120, [152.2, 798.8, 1598.0, 2929.0])}
for name, (r, gts) in envs.items():
    print(f"{name}: r={r:.4f}; anomalous/canonical velocity (slow particles) = {ratio(r):.4g} x Gt/G;"
          f" Gibbs exponent difference v=0 vs v=sigma = {gibbs(r):.4g} x Gt/G")
    for gt in gts:
        print(f"    Gt/G={gt:g}: anomalous velocity ratio = {ratio(r)*gt:.3g}, Gibbs exponent difference = {gibbs(r)*gt:.3g}")
for name, (r, _) in envs.items():
    print(f"{name}: Gt/G at which the anomalous velocity equals the canonical one = {1/ratio(r):.3g}")
