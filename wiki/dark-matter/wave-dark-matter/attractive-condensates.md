---
title: "Attractive condensates: critical mass and the bosenova"
weight: 30
status: established
description: "Above a critical mass M_crit ≈ 3.6M_P/(m√g) an attractive condensate collapses, ejects fast waves and regrows: the bosenova cycle."
provenance: [T]
sources:
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
  - "notes/ufd-endpoint.md 'The data'"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [14]"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [13]"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes): resolution of open problem 3'"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
---

*An attractive condensate is a [Bose star](wave-kinetics.md) — a self-gravitating clump of a light boson field, all in one coherent state — whose particles also attract one another through a self-interaction. Gravity and the self-attraction both pull inward against the outward pressure that comes from the field's wave nature, and the self-attraction grows faster with density, so such a condensate has a maximum stable mass. Above it the condensate collapses, throws off part of its mass as fast waves in a burst called a bosenova, and the remnant grows again. In the Comatter program this cycle is the endpoint that, in [Scenario A](../momentum-clumping/wave-island/scenario-a.md) of [the wave island](../momentum-clumping/wave-island/_index.md), would have drained the dark matter out of the [ultra-faint dwarf galaxies](../halo-astrophysics/dwarf-galaxies.md); the data contradict that drain, and Scenario A is under review.*

**Status:** Established — [T] — the critical mass is a "dilute-boson-star bound, Chavanis-type" (calc note [#3](../../../notes/wave-island.md); [the checkpoint](../../history/documents/checkpoint.md)'s [14]†) and the collapse cycle an "LPT 2017-type result" (calc note [#4](../../../notes/ufd-endpoint.md); [13]†), where LPT is Levkov–Panin–Tkachev — not machine-checked; the coefficient 3.6, the conventions for the coupling g and for M_P, and both citations are unchecked.

## Why there is a maximum mass [T]

A Bose star is the ground state of a self-gravitating boson field ([wave kinetics and Bose-star formation](wave-kinetics.md)). Its size is set by a balance of energies. A rough estimate shows the balance for a star of mass M and radius R, made of bosons of mass m; it is a standard order-of-magnitude argument [T], given here as explanation, and the clumping notes do not make it (units with ℏ = c = 1):

```text
E(R) ≈ + (gradient energy)       ∝ M/(m² R²)
       − (gravitational energy)  ∝ G M²/R
       − (attractive contact)    ∝ g M²/(m² R³)
```

The gradient term is the "quantum pressure" of the wave: confining a wave to a region of size R costs energy, because its spectrum must then be at least of width 1/R, the Fourier relation between a waveform and its spectrum. Gravity alone always finds a balance with it, at a radius that shrinks as the mass grows. The contact term counts pairs of particles per volume, and so falls off faster with R than the other two. As M grows, the stable equilibrium becomes shallower; at a critical mass the stable (dilute) equilibrium and an unstable (dense) one merge, and above it no equilibrium exists. The estimate gives a critical mass of the form M_P/(m√g), where M_P = G^{−1/2} is the [Planck mass](../../gravity/spin-2-fields/planck-units.md) and g the contact coupling; a full calculation fixes the numerical factor. A "dilute" boson star is one on the stable, weak-field branch, and the bound is the upper end of that branch.

The clumping notes take the result from the literature: "a growing condensate with attractive self-interaction has a critical mass, M_crit ≈ 3.6 M_P/(m√g) [T: dilute-boson-star bound, Chavanis-type], above which it collapses (bosenova)" ([`notes/wave-island.md`](../../../notes/wave-island.md), 'What pins g? Two scenarios'). Here g is the gated contact coupling of [the clumping notes](../../history/documents/clumping-notes.md), in GeV⁻², the strength of [conjugate matter](../conjugate-matter/_index.md)'s gated self-interaction ([the velocity gate](../conjugate-matter/velocity-gate.md)). M_crit is the largest stable mass of a condensate. It is a different quantity from m_crit, the particle-mass threshold of [the classicality theorem](../momentum-clumping/classicality-theorem.md).

## The bosenova [T]

A condensate pushed past the critical mass implodes. As it contracts, its density rises steeply, and the self-interaction converts part of its mass into waves moving at speeds close to that of light, which escape. What remains settles back onto the stable branch and grows again by absorbing quanta from its surroundings, until it reaches the critical mass once more. Simulations of collapsing [axion stars](../../cosmology/dark-energy/axion-like-fields.md#as-dark-matter) by Levkov, Panin and Tkachev (the 2017 paper in [13]†) found such collapses ending in bursts of relativistic axions. The name comes from the collapse and explosion of Bose–Einstein condensates of atoms with attractive interactions in the laboratory.

Calc note #4 writes the cycle as: "grow to M_crit → collapse → eject an O(0.1–1) fraction as fast/relativistic waves (bosenova; LPT 2017-type result [T]) → remnant regrows" ([`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md), 'The attractive endpoint: criticality and the drain'). The speed of the ejected waves is what matters for a galaxy: "Ejecta velocities are set by the dense collapse stage and vastly exceed a UFD escape velocity of ~10 km/s", where UFD stands for [ultra-faint dwarf](../halo-astrophysics/dwarf-galaxies.md) galaxy.

## How the program uses it

### The endpoint of mandatory condensation

On the [wave island](../momentum-clumping/wave-island/_index.md), the light end of conjugate matter's mass range, the gated attraction drives condensation ([the gated condensation rate](../momentum-clumping/wave-island/condensation-rate.md)). Under [Scenario A](../momentum-clumping/wave-island/scenario-a.md), in which the gated channel is also what makes dwarf-galaxy cores, calc note #3 found the condensation mandatory and halo-wide in the ultra-faint dwarfs. Because the interaction attracts, it then asked where the condensation ends: "Because the interaction is **attractive**, the endpoint is not a placid stream" (calc note #3). Calc note #4 answered with the critical mass and the bosenova cycle.

### M_crit as a function of m alone

Scenario A fixes the coupling by requiring the gated channel to fit classical dwarf cores, "which spends g²/m³" (calc note #3). With g²/m³ fixed, M_crit depends on the particle mass alone. Calc note #4: "Under the Scenario-A normalization (which pins g²/m³, hence pins M_crit as a function of m alone)":

```text
M_crit = 3.6 M_P/(m√g) ≈ 2.9×10⁻³⁰ (m/eV)^{−7/4} M_⊙
```

The exponent follows from the two statements, a step the note does not write out: fixing g²/m³ makes g grow as m^{3/2}, so m√g grows as m^{7/4}. The two expressions are the same quantity under that normalization, and the −7/4 form holds only under Scenario A. The checkpoint quotes the same scaling with [14]† ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)).

"This crosses the UFD core mass (~10⁶ M_⊙) at m ≈ 5×10⁻²¹ eV" (calc note #4), which divides the wave island into two branches:

- **Branch (i).** For "m ≳ 10⁻²⁰ eV (the bulk of the wave island): M_crit ≪ M_core — often absurdly so (10⁻⁷ M_⊙ at 10⁻¹³ eV)". The condensate "reaches criticality almost immediately and enters the known attractive-collapse cycle", and since the ejecta escape, "**the condensate is a mass drain.**" The drain is not elastic: even if heating and expansion throttle the rate down to about 1/t_age, "an O(1) fraction of the core mass is processed *and removed* within the lifetime — unlike SIDM, where relaxation is elastic and mass stays" ([self-interacting dark matter](../halo-astrophysics/self-interacting-dark-matter.md), SIDM). "Prediction of Branch (i): UFDs today should be low-density, inflated, or gone."
- **Branch (ii).** For "m ≲ 5×10⁻²¹ eV: M_crit ≳ M_core; the condensate grows as a stable soliton — ordinary fuzzy-DM phenomenology with an attractive perturbation", with DM for dark matter. That mass range is excluded by the [bounds on fuzzy dark matter](fuzzy-dark-matter-bounds.md).

Calc note #4's comparison with the data ('The data'): "Branch (i) predicts the opposite of what is observed; Branch (ii) is excluded before we arrive." The checkpoint records the outcome: the attractive endpoint "cycles above M_crit ≈ 2.9×10⁻³⁰(m/eV)^{−7/4} M_⊙ [14†] and drains the halo — **falsified** by observed UFD density and longevity" ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). [The lab notebook](../../history/documents/lab-notebook.md)'s addendum v0.2 states it with the general form: "the attractive endpoint (bosenova cycling above M_crit≈3.6M_P/(m√g)) drains their dark matter". The full record is on [Under review: Scenario A and the ultra-faint-dwarf endpoint](../momentum-clumping/wave-island/scenario-a.md).

## What is unchecked

No `verify/` script covers any number on this page; of the clumping numbers, the gate checks only calc note [#2](../../../notes/stream-stability.md)'s shortfall ratios, in section D of [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) ([the velocity-gated-gravity script](../../method/verification/velocity-gated-gravity-script.md)). The coefficient 3.6 and the conventions for g and M_P in the critical mass have not been checked against the cited paper, and both references are cited from model memory (†). The clumping notes do not define M_P; M_P = G^{−1/2} in the estimate above is the wiki's choice of symbol. The checkpoint requires every † reference to be source-checked before external use ([#11 §14 item 10](../../papers/broken-born-checkpoint-v2.md#14-open-problems), OP10), the task of [the † literature battery](../../method/literature-battery.md).

## References

- The checkpoint's [14]†: P.-H. Chavanis, "Mass–radius relation of self-gravitating Bose–Einstein condensates with attractive self-interaction," Phys. Rev. D 84, 043531 (2011), [arXiv:1103.2050](https://arxiv.org/abs/1103.2050).
- The checkpoint's [13]† includes D. G. Levkov, A. G. Panin, I. I. Tkachev, "Relativistic axions from collapsing Bose stars," Phys. Rev. Lett. 118, 011301 (2017).

Added by the wiki from model memory (†):

- E. A. Donley et al., "Dynamics of collapsing and exploding Bose–Einstein condensates," Nature (2001)†: the laboratory bosenova.

## Used by

- [Under review: Scenario A and the ultra-faint-dwarf endpoint](../momentum-clumping/wave-island/scenario-a.md) — the bosenova cycle drains the ultra-faint dwarfs.
- [The wave island](../momentum-clumping/wave-island/_index.md) — the attractive endpoint of gated condensation.
- [The net theorem](../momentum-clumping/net-theorem.md) — "fatal (committed wave)" rests on this endpoint.
- [Conjecture: velocity clumping, the founding image](../momentum-clumping/founding-image.md) — the collapse cycle above M_crit is what makes clumping fatal where it is mandatory, the committed-wave part of the evidence against the image.
- [Under review: Fornax friction suppression (old row 4)](../momentum-clumping/fornax-friction.md) — where condensation is mandatory, the attractive endpoint is a collapse, not a superfluid core.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested), refs [13]–[14] — the checkpoint's statement and the references; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — Scenario A under review
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'What pins g? Two scenarios' — the critical mass and its tag; the attractive endpoint as Scenario A's question
- [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) 'The attractive endpoint: criticality and the drain', 'The data' — the Scenario-A scaling, the bosenova cycle, the two branches, the comparison with observed ultra-faint dwarfs
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.2, after the clumping notes): resolution of open problem 3' — the general form of M_crit in the lab notebook
- [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) section D — calc note #2's shortfall ratios, the only clumping numbers the gate checks; none on this page
