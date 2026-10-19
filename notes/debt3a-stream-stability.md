# Debt 3, Chunk A: Linear stability of the conjugate sector's velocity-space fragmentation

*Working note. Status: calculation complete. Result: negative on the particle island, with a structural corollary.*

## Setup

Nonrelativistic mean-field (Vlasov) limit of the gated interaction. Single-particle energy:

$$
\varepsilon(\mathbf x,\mathbf p) = \frac{p^2}{2m} + m\Phi_{\rm grav}(\mathbf x) - g\int d^3p'\; G\!\left(\frac{\mathbf p-\mathbf p'}{\mu}\right) f(\mathbf x,\mathbf p'),
\qquad g \equiv \frac{4\pi\tilde\alpha}{m_\phi^2} = \sqrt{\frac{\pi\,\sigma_0}{m^2}},
$$

with $G$ the Gaussian gate, $G(0)=1$, attractive sign, and the $x$-range collapsed to contact (range $1/m_\phi$, microscopic). Linearize the Vlasov equation about a homogeneous Maxwellian $f_0(\mathbf p)$ of dispersion $\sigma$; perturbations $\delta f \propto e^{i(\mathbf k\cdot\mathbf x - \omega t)}$ give

$$
\delta\varepsilon(\mathbf p) = g\int d^3p'\; G(\mathbf p-\mathbf p')\,
\frac{\mathbf k\cdot\nabla_{p'} f_0}{\omega - \mathbf k\cdot\mathbf v'}\;\delta\varepsilon(\mathbf p') .
$$

An eigenvalue problem (the "potential" lives on momentum space), not a scalar dispersion relation. Two solvable limits bracket it.

## Limit 1 — broad gate ($\mu \gg m\sigma$; dwarf regime)

$G \to 1$, $\delta\varepsilon$ constant, scalar relation. Static threshold (standard plasma-function algebra):

$$
\boxed{\ \frac{g\,n}{m\,\sigma^2} \;\geq\; 1\ }
\qquad\text{i.e.}\qquad \varepsilon_{\rm int} \equiv g\,n \;\geq\; m\sigma^2 .
$$

Below threshold: Landau-damped, stable. **There is no race with orbital stirring below threshold — the flocking never starts.** The earlier "γ vs Ω" framing presumed growth exists; it exists only above this line.

## Limit 2 — narrow gate ($\mu \ll m\sigma$; MW/cluster regime)

Patch modes: $\delta\varepsilon$ supported on a momentum ball of radius $\sim\mu$. Same algebra with $n \to n_{\rm gate} \approx n\,(v_*/\sigma)^3/(2\pi)^{3/2}$ (co-movers only) and $\sigma \to v_*$ (internal spread of the patch):

$$
\frac{g\,n_{\rm gate}}{m\,v_*^2} \;\geq\; O(1).
$$

Unified criterion: $\varepsilon_{\rm gate} \gtrsim m\cdot\min(\sigma, v_*)^2$.

## Numbers at the scattering benchmark

The dwarf-core fit fixes $\sigma_0/m = 30\ \mathrm{cm^2/g}$, hence $g$ is *spent* — no freedom remains. With $m_\chi = 70$ MeV, $v_* = 120$ km/s:

| System | $\varepsilon_{\rm gate}$ (GeV) | $m\cdot\min(\sigma,v_*)^2$ (GeV) | Ratio |
|---|---|---|---|
| Dwarf core ($\rho \sim 1\,\mathrm{GeV/cm^3},\ \sigma\sim30$ km/s) | $\sim 3\times10^{-37}$ | $\sim 7\times10^{-10}$ | $\sim 10^{-28}$ |
| MW halo, local ($\rho\sim0.4$, $\sigma\sim155$ km/s) | $\sim 3\times10^{-39}$ | $\sim 10^{-8}$ | $\sim 10^{-31}$ |

**Fails by 28–31 orders of magnitude.** Robust to every dropped $O(1)$: halos are dilute, the force is contact-range, and a mean-field instability needs interaction energy density competitive with kinetic — scattering fits only need $\Gamma t \sim 1$ over Gyr, which is ~30 orders cheaper. The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in $10^{30}$.

## Corollary (the classicality theorem)

At fixed $S \equiv \sigma_0/m$ and halo $(\rho,\sigma)$, the criterion scales as $\sqrt{\pi S}\,\rho\,/(m^{5/2}\sigma^2)$. Setting it to 1 gives $m_{\rm crit} = [\sqrt{\pi S}\,\rho/\sigma^2]^{2/5} \approx 10^{-13}$ GeV $\sim 0.1$ meV for MW conditions. At that mass the per-mode occupation is

$$
N_{\rm occ} = n\,\lambda_{\rm dB}^3 = \frac{\rho}{m^4\sigma^3} \;\sim\; 10^{20} \gg 1 .
$$

**By the time the coupling is strong enough for collective behavior, the sector is deep in the wave regime.** Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework. This is a theorem-grade statement at mean-field level, not a benchmark accident.

## Consequences for the predictions table

- **Particle island** ($m_\chi \sim$ MeV–GeV): Rows 1–2 (exponential cliff, isotropy) **survive** — they are collisional. Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them. On this island BBT is cliff-shaped SIDM plus Maslov quintessence.
- **Wave island** ($m_\chi \lesssim$ meV, $N_{\rm occ}\gg1$): the collective sector is reborn in field language. The halo is an incoherent wave field; the gated attraction drives condensation in $k$-space — power flowing into narrow-momentum streams — which is the original "clumps in momentum space" intuition in its natural habitat. The known anchor is Levkov–Panin–Tkachev gravitational Bose condensation (kinetic relaxation with Bose-enhancement factors $\propto N_{\rm occ}$); our gated quartic adds a channel and the gate turns the effective coupling *off* in high-dispersion systems, so a cliff-analog survives as $(v_*/\sigma)^3$ suppression rather than an exponential. Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable).

## Next chunk (3b)

Compute the gated wave-kinetic condensation rate: Boltzmann collision integral for the field with Bose enhancement and the momentum gate, $\Gamma_{\rm cond}(m, g, v_*; \rho, \sigma)$, compared to orbital stirring $\Omega$ per environment. Deliverable: the wave-island analog of the criterion above, the surviving-parameter window, and whether stream formation is mandatory, tunable, or forbidden there. Anchor scalings against LPT before trusting coefficients.
