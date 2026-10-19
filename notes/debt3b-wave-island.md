# Debt 3, Chunk B: Gated condensation on the wave island

*Working note. Status: rate derived, environments evaluated, verdict reached. Coefficients heuristic at O(1)–O(10) level; calibration against Levkov–Panin–Tkachev (LPT) numerics is a flagged to-do.*

## Setup

Wave island: $m \lesssim 0.1$ meV, per-mode occupation $N_{\rm occ} = \rho/(m^4\sigma^3) \gg 1$. The halo is an incoherent classical field; relaxation proceeds by wave kinetics — the Boltzmann collision integral with Bose enhancement, rate $\Gamma \sim n\,\sigma_{\rm scat}\, v \times N_{\rm occ}$. This is the mechanism LPT established for gravity (Bose condensation of virialized wave DM into solitons); here the gated contact attraction adds a channel. Same conventions as Chunk A: $\sigma_0 \equiv g^2 m^2/\pi$, gate width $v_*$ in relative velocity.

## The rate [D, heuristic coefficients]

With peak occupation $N_{\rm occ} \approx (2\pi)^{3/2}\rho/(m^4\sigma^3)$, scatterer density restricted to the gate, and relative velocities $\min(\sigma, v_*)$:

$$
\boxed{\ \Gamma_{\rm self} \;\approx\; c\,\frac{g^2 \rho^2\, \min(\sigma, v_*)^4}{m^3\,\sigma^6}\ }, \qquad c = O(5\text{–}15).
$$

Gate-open ($\sigma \lesssim v_*$): $\Gamma \approx c\,g^2\rho^2/(m^3\sigma^2)$. Gate-narrow: suppressed by $(v_*/\sigma)^4$ — **a power law, not an exponential**. Two corollaries before any numbers:

1. **Island discriminant.** The velocity suppression of self-interaction effects is $e^{-v^2/v_*^2}$ on the particle island but $(v_*/\sigma)^4$ on the wave island. The cliff's *sharpness* distinguishes the islands observationally.
2. **Gravity floor.** The gravitational channel $\Gamma_{\rm gr} \approx 8\pi G^2\rho^2\Lambda/(m^3\sigma^6)$ [T: LPT] always runs; the gated channel dominates iff $g \gtrsim G\sqrt{8\pi\Lambda/c}/\min(\sigma,v_*)^2 \sim 10^{-31}\,\mathrm{GeV^{-2}}$ (MW numbers) — an easy floor. For $m \gg 10^{-20}$ eV the gravity channel is negligible on Hubble times; the gated channel is the only game.

## What pins $g$? Two scenarios

**Scenario A — the gated channel is the core-maker.** On the wave island, $\Gamma_{\rm self}$ *is* the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo). Fitting classical-dwarf cores means $\Gamma_{\rm self}(\text{dwarf}) \cdot t_{\rm age} = \kappa \sim 1$, which spends $g^2/m^3$. Streams need the much harder $\Gamma_{\rm self} \gtrsim \Omega = 1/t_{\rm dyn}$. Eliminating $g^2/m^3$:

$$
R_X \equiv \frac{\Gamma_{\rm self}(X)}{\Omega_X} = \kappa\,\frac{t_{\rm dyn,X}}{t_{\rm age}}\left(\frac{\rho_X}{\rho_d}\right)^2\left(\frac{\sigma_d}{\sigma_X}\right)^2\left(\frac{\min(\sigma_X, v_*)}{\sigma_X}\right)^4 .
$$

| Environment ($\rho$ in GeV/cm³, $\sigma$ in km/s) | $t_{\rm dyn}$ | $R_X$ ($\kappa=1$) |
|---|---|---|
| Classical dwarf core (1, 30) | 0.1 Gyr | $\sim 10^{-2}$ |
| **Ultra-faint dwarf (20, 3)** | 0.01 Gyr | $\sim \mathbf{40}$ |
| MW inner 1 kpc (10, 120) | 0.02 Gyr | $\sim 10^{-2}$ |
| MW solar circle (0.4, 155) | 0.2 Gyr | $\sim 4\times10^{-5}$ |
| Cluster (0.03, 1000) | 1 Gyr | $\sim 0$ |

**Verdict A:** streams lose everywhere by $10^2$–$10^4$ — *except ultra-faint dwarfs*, where $\rho^2/\sigma^2$ leverage wins by ~40. In UFDs, condensation is then mandatory and halo-wide: power drains into the lowest relative momenta on sub-dynamical timescales. Because the interaction is **attractive**, the endpoint is not a placid stream: a growing condensate with attractive self-interaction has a critical mass, $M_{\rm crit} \approx 3.6\,M_P/(m\sqrt{g}\,)$ [T: dilute-boson-star bound, Chavanis-type], above which it collapses (bosenova). The surviving descendant of old rows 3–4 is therefore a sharply localized prediction: **anomalous central objects, density spikes, or disruption signatures in ultra-faint dwarfs, absent in classical dwarfs and the MW.** Quantifying the endpoint (soliton growth rate vs. $M_{\rm crit}$; survival constraints from observed UFDs) is Chunk 3c.

**Scenario B — cores come from elsewhere** (fuzzy-end quantum pressure at $m \sim 10^{-22}$ eV, or baryonic feedback), leaving $g$ free. Writing $X \equiv gn/(m\sigma^2)$ (the Chunk-A mean-field parameter, with $X < 1$ required so halos aren't modulationally unstable), the stream condition $\Gamma_{\rm self} \geq \Omega$ becomes $X \geq \sqrt{\Omega\sigma^2/(c\,m\,v_*^4)}$. MW numbers, $m = 0.1$ meV: window $X \in [5\times10^{-11},\,1]$ — ten orders of magnitude. **Verdict B: streams are *tunable*, not mandatory.** In Lakatos terms from the earlier discussion: on this branch the granularity prediction is no longer a novel *requirement* of the program, only an option — a degeneration flag.

## Bonus: the relic debt closes itself

A field this light with only gravitational + self couplings is produced by misalignment, like an axion. Open problem #5 (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism, and $\Omega_\chi$ trades against $(m, \chi_i)$ in the standard way. The 5.4:1 question remains (polarization-genesis), but the *production channel* is no longer exotic.

## Standing results after Chunks A+B

- Particle island: cliff (exponential) + isotropy live; no collective phenomena. Fully classical, fully collisional.
- Wave island: collective phenomena live but tunable, except Scenario A's mandatory UFD signature; cliff softens to $(v_*/\sigma)^4$; relic debt resolved by misalignment.
- Row 3 as written (Gaia/GD-1 granularity in MW-like halos) is dead on both islands as a *mandatory* signature. The predictions table needs revision (pending).

## Next

**Chunk 3c** (small): UFD endpoint — condensate growth vs. $M_{\rm crit}$, survival constraints, turn Scenario A into a pass/fail against known ultra-faints. Completes Debt 3.
**Then Chunk 1a** (large): linearize $S_H$ on the broken vacuum; leaning on the known linearized-DFT spectrum, identify propagating modes and check quadratic-order ghost freedom. Born's debt, first installment.
