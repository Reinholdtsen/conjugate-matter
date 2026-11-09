---
title: "Bounds on fuzzy dark matter"
weight: 50
status: established
description: "Ultra-faint-dwarf kinematics (Dalal–Kravtsov, bound ≈ 3×10⁻¹⁹ eV) and Lyman-α forest limits exclude very light wave dark matter, setting the wave island's lower edge; the figure awaits the † check."
provenance: [T]
sources:
  - "notes/ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
  - "notes/ufd-endpoint.md 'The data'"
  - "notes/ufd-endpoint.md 'Verdict and closure of the clumping problem'"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [15]"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes): resolution of open problem 3'"
  - "notes/velocity-gated-gravity.md §6"
---

*The bounds on fuzzy dark matter are observational lower limits on the mass of wave dark matter at its light extreme, where the particles are so light that their de Broglie wavelength is comparable to the core of a small galaxy. Two kinds of observation set them. In a fuzzy halo the interfering dark-matter waves form density fluctuations that heat stars over time, so the compact, cold stellar populations of [ultra-faint dwarf galaxies](../halo-astrophysics/dwarf-galaxies.md) exclude the lightest masses; and fuzzy dark matter suppresses small-scale structure, which the Lyman-α forest — the absorption lines of intergalactic hydrogen in quasar spectra — would reveal. In the Comatter program these bounds set the lower edge of [the wave island](../momentum-clumping/wave-island/_index.md) and close the light-mass escape from the ultra-faint-dwarf test of [Scenario A](../momentum-clumping/wave-island/scenario-a.md), a scenario under review.*

**Status:** Established — [T], with the Dalal–Kravtsov citation † (from model memory) — the [clumping notes](../../history/documents/clumping-notes.md) flag its figure "verify exact figure before publication", no source cites a paper or gives a number for the Lyman-α limit on this mass, and both await [the † literature battery](../../method/literature-battery.md).

## Fuzzy dark matter [T]

When dark matter is light enough, its de Broglie wavelength in a galaxy reaches the scale of the galaxy's own structure, and the halo must be described as a wave ([occupation number](occupation-number.md)). At the light extreme, near the m ~ 10⁻²² eV that the clumping notes associate with "fuzzy-end quantum pressure" ([`notes/wave-island.md`](../../../notes/wave-island.md)), the wavelength is comparable to the cores of dwarf galaxies. Three features follow from the wave nature:

- **Quantum pressure.** A wave cannot be confined to a region smaller than its wavelength without an energy cost, the Fourier relation between a waveform's extent and its spectrum's width. This opposes gravitational collapse below a [Jeans](../momentum-clumping/vlasov-stability.md#the-static-threshold-and-the-jeans-instability)-like scale and suppresses small structures.
- **Solitonic cores.** The center of each halo holds a coherent ground-state core, a Bose star ([wave kinetics and Bose-star formation](wave-kinetics.md)), whose size grows as the particle mass falls.
- **Granules.** Outside the core, waves of different momenta interfere, and the density is a pattern of granules of about one de Broglie wavelength that reshuffle continually.

Each feature becomes more pronounced as the mass falls, and each gives an observational bound.

## Bounds from ultra-faint dwarfs [T]

[Ultra-faint dwarf galaxies](../halo-astrophysics/dwarf-galaxies.md) are small, cold, old and dominated by dark matter. In a fuzzy halo the granules act on the stars as fluctuating masses: each passing granule gives the stars a small gravitational kick, and over billions of years the kicks add up, heating the stellar system and making it expand. The lighter the particle, the larger and heavier the granules and the stronger the heating. A compact, cold stellar population that has survived for most of the age of the universe therefore excludes the lightest masses. Dalal and Kravtsov turned the sizes and the stellar kinematics of ultra-faint dwarfs into such a bound, [the checkpoint](../../history/documents/checkpoint.md)'s reference [15]†; calc note [#4](../../../notes/ufd-endpoint.md)'s parenthesis names the argument "granule-heating arguments".

## Bounds from the Lyman-α forest [T]

Light from a distant quasar passes through clouds of neutral hydrogen in intergalactic space on its way to the observer. Each cloud absorbs at the Lyman-α wavelength of hydrogen, shifted by the cloud's own [redshift](../../cosmology/scale-factor-duality/redshift.md), so the quasar's spectrum shows a forest of absorption lines whose pattern traces the density of the intergalactic gas along the line of sight. Its small-scale fluctuations measure the matter power spectrum on scales where fuzzy dark matter's quantum pressure suppresses it. The observed small-scale power excludes the lightest masses. No source in the program's record cites an analysis or gives a number for this limit on the mass of wave dark matter; the Lyman-α data the record does cite test a different model ([a long-range velocity-gated attraction](../momentum-clumping/long-range-gated-attraction.md#the-lyman-α-forest)).

## How the program uses the bounds

### The light branch of Scenario A

[Scenario A](../momentum-clumping/wave-island/scenario-a.md) of the wave island, a claim under review, has two branches. The light one, m ≲ 5×10⁻²¹ eV, is where the condensate of an [attractive self-interaction](attractive-condensates.md) would grow as a stable core rather than drain the halo. Calc note #4 closes it with these bounds:

> **Branch (ii), m ≲ 5×10⁻²¹ eV:** M_crit ≳ M_core; the condensate grows as a stable soliton — ordinary fuzzy-DM phenomenology with an attractive perturbation. But this mass range is independently excluded: UFD sizes and stellar kinematics (granule-heating arguments, Dalal & Kravtsov 2022 [T — bound ≈ 3×10⁻¹⁹ eV; verify exact figure before publication]) and Lyman-α forest limits already forbid wave DM this light.

([`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md), 'The attractive endpoint: criticality and the drain'; DM is dark matter and UFD an ultra-faint dwarf.) Its summary in 'The data': "Branch (ii) is excluded before we arrive."

### The wave island's lower edge

The same bound fixes the bottom of the surviving wave island: "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" (calc note #4, 'Verdict and closure of the clumping problem'). [The lab notebook](../../history/documents/lab-notebook.md)'s addendum v0.2 states the same range without a citation.

### In v1 and the checkpoint

[Program v1](../../history/documents/checkpoint.md) keeps the figure and the flag: "The light-mass escape is independently excluded (UFD heating bounds ≈ 3×10⁻¹⁹ eV, Dalal & Kravtsov 2022 [T — verify figure]; Lyman-α)" ([#9 §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)). [The checkpoint](../../history/documents/checkpoint.md) keeps the conclusion and drops the figure: "the light-mass escape is closed independently [15†, Lyman-α]" ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). The wiki quotes the figure as the notes give it, with their flag.

## What remains to verify

- **The figure.** Calc note #4 attaches "verify exact figure before publication" to it, and v1 lists "Dalal–Kravtsov exact bound [O]" among its literature verifications ([#9 §10 item 8](../../../notes/broken-born-program-v1.md#10-open-problems)).
- **The reference.** [15]† is cited from model memory. The checkpoint requires every † reference to be source-checked before external use: "Literature battery completion; every † reference source-checked [O]" ([#11 §14 item 10](../../papers/broken-born-checkpoint-v2.md#14-open-problems), OP10).
- **The Lyman-α limit.** The record gives it no reference and no number, here or anywhere.

## An unresolved conflict: Scenario B's fuzzy cores

[Scenario B](../momentum-clumping/wave-island/scenario-b.md), the surviving branch of the wave island, lets dark-matter cores come from "fuzzy-end quantum pressure at m ~ 10⁻²² eV, or baryonic feedback" ([`notes/wave-island.md`](../../../notes/wave-island.md), 'What pins g? Two scenarios'). The fuzzy option sits at a mass below the lower edge that calc note #4 later sets with these bounds, 3×10⁻¹⁹ eV. Neither note addresses the difference, and [the record of conflicts between sources](../../history/documents/source-conflicts.md) lists it as unresolved. Baryonic feedback, the other option, is unaffected.

## References

- The checkpoint's [15]†: N. Dalal, A. Kravtsov, "Excluding fuzzy dark matter with sizes and stellar kinematics of ultrafaint dwarf galaxies," Phys. Rev. D 106, 063517 (2022), [arXiv:2203.05750](https://arxiv.org/abs/2203.05750).

The program cites nothing for the Lyman-α limit or for fuzzy dark matter in general. Added by the wiki from model memory (†):

- W. Hu, R. Barkana, A. Gruzinov, "Fuzzy cold dark matter," Phys. Rev. Lett. (2000)†.
- V. Iršič, M. Viel, M. G. Haehnelt, J. S. Bolton, G. D. Becker, "First constraints on fuzzy dark matter from Lyman-α forest data and hydrodynamical simulations," Phys. Rev. Lett. (2017)†.
- E. Armengaud et al., Mon. Not. R. Astron. Soc. (2017)†: a Lyman-α forest bound on the mass of light bosonic dark matter.

## Used by

- [Under review: Scenario A and the ultra-faint-dwarf endpoint](../momentum-clumping/wave-island/scenario-a.md) — these bounds close Scenario A's light-mass escape.
- [The wave island](../momentum-clumping/wave-island/_index.md) — its lower edge.
- [Scenario B: tunable streams](../momentum-clumping/wave-island/scenario-b.md) — its fuzzy-core option lies below the bound.
- [The net theorem](../momentum-clumping/net-theorem.md) — "viable" excludes Scenario A's light-mass branch, which these bounds rule out.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested), [§14 item 10](../../papers/broken-born-checkpoint-v2.md#14-open-problems), ref [15] — the checkpoint's statement without the figure; the † battery; the reference; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — Scenario A under review
- [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) 'The attractive endpoint: criticality and the drain', 'The data', 'Verdict and closure of the clumping problem' — the exclusion of the light branch, the figure and its flag, the island's range
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'What pins g? Two scenarios' — Scenario B's fuzzy-core option at m ~ 10⁻²² eV
- [`notes/broken-born-program-v1.md` §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative), [§10](../../../notes/broken-born-program-v1.md#10-open-problems) — v1's statement with the figure; the verification to-do
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.2, after the clumping notes): resolution of open problem 3' — the island range in the lab notebook
- [`notes/velocity-gated-gravity.md` §6](../../../notes/velocity-gated-gravity.md#6-what-observations-allow-at-the-records-gate-width) — Lyman-α data the record cites, for a different model
