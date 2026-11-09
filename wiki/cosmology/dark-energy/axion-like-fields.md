---
title: "Axion-like fields and pseudo-Goldstone bosons"
weight: 14
status: established
description: "A field that is an angle: a shift symmetry keeps it light and coupled only through its derivatives, and a small explicit breaking leaves the periodic potential V₀[1 + cos(φ/f)]. The axion, axion-like dark matter and dark energy, and the program's uses: τ's hilltop potential and fifth-force safety, the toy models' pseudo-Goldstone polarization angle, X 'axion-like' in the exact-shift sense, and wave χ produced 'like an axion'."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 6"
  - "wiki/papers/broken-born-checkpoint-v2.md refs [13], [20]"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §7"
  - "HANDOFF.md §2"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "verify/toy_coset.py"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/x-classification.md §1"
  - "notes/x-classification.md §3"
  - "notes/geometric-core.md §F"
  - "notes/beta-coefficients.md §3"
  - "notes/wave-island.md 'Bonus: the relic-abundance problem solves itself'"
  - "review/wiki-build-flags.md item 27"
  - "review/wiki-build-flags.md item 54"
  - "notes/closed-universe.md §2"
---

*An axion-like field is a scalar field whose value is an angle. Its interactions are unchanged when the field is shifted by a constant, φ → φ + c, except for a small explicit breaking of that symmetry, which leaves a potential that repeats as the angle goes around its circle, in its standard form V₀[1 + cos(φ/f)]. Such a field is a pseudo-Goldstone boson: the massless mode that a spontaneously broken continuous symmetry leaves behind, given a small mass by a slight explicit breaking. The shift symmetry keeps the field light and lets it couple to other matter only through how it changes in space and time. The axion of the strong interaction is the original example; it and lighter fields of the same kind are studied as dark matter, and the lightest as dark energy. The Comatter program's dark-energy field [τ](tau-quintessence.md) is one: an angle with a cosine potential, starting near the potential's maximum. The program also calls its [momentum graviton X](../../gravity/momentum-graviton/_index.md) "axion-like" for its exact shift symmetry, and the worklog of its toy models describes the vacuum's choice of position and momentum as "a pseudo-Goldstone polarization angle".*

**Status:** Established — [T] — textbook particle physics and cosmology, written here from general knowledge, with the literature it names marked †; no `verify/` script checks it. The program's uses carry their own tags: τ's potential [D + T] ([checkpoint #11](../../history/documents/checkpoint.md) [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology)), τ as a pseudo-Goldstone field [D] ([lab notebook](../../history/documents/lab-notebook.md) [#1 §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured)), the polarization as a Goldstone angle [D][V] ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)) and the shift symmetry of X [D — rigorous] (calc note [#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous)).

## Goldstone and pseudo-Goldstone bosons [T]

When the lowest-energy state of a system breaks a continuous symmetry of its laws, the equally good ground states form a continuous family, and moving the whole system along that family costs no energy. A long-wavelength wave of that motion costs arbitrarily little, so it describes a massless particle, a Goldstone boson ([Goldstone's theorem](../../symmetry-breaking/goldstone-and-higgs.md#goldstones-theorem)). A uniform shift along the family changes nothing physical, so at low energies the Goldstone field enters the interactions only through its derivatives [T].

If a small term in the laws breaks the symmetry explicitly, the family of ground states is tilted: its members no longer have equal energy ([spontaneous versus explicit breaking](../../symmetry-breaking/spontaneous-symmetry-breaking.md#spontaneous-versus-explicit-breaking)). The would-be Goldstone boson then moves in a shallow potential and has a small mass, which vanishes as the explicit term is switched off, and its couplings stay derivative apart from terms proportional to that term. It is called a pseudo-Goldstone boson. The pions are the standard example: the chiral symmetry of the strong interaction is broken spontaneously, the small quark masses break it explicitly, and the pions are light rather than massless [T]. The general account, with the program's toy-model applications and the zero mode that no symmetry protects, is on [pseudo-Goldstone modes](../../symmetry-breaking/goldstone-and-higgs.md#pseudo-goldstone-modes).

## A field that is an angle [T]

### The shift symmetry

When the broken symmetry is a single rotation, a U(1), the family of ground states is a circle and the Goldstone field is an angle θ. It is written as a field with units of energy, φ = fθ, where the constant f, called the decay constant, is set by the scale of the symmetry breaking. The values φ and φ + 2πf describe the same point of the circle. The rotation acts on the field as a shift, φ → φ + c. If that symmetry is exact, the field has no potential at all, and the action can depend on φ only through its derivatives [T]. The exceptions are terms that the shift changes only by a total derivative, which leaves the field equations unchanged, such as the axion's coupling to the electromagnetic field [T].

### The periodic potential

A small explicit breaking gives the field a potential. Because φ and φ + 2πf are the same point, the potential repeats with period 2πf, so it can be written as a Fourier series in φ/f, a sum of harmonics of the angle. Keeping the constant term and the first harmonic, with the constant equal to the amplitude so that the minimum is zero, gives the standard form, the one Frieman, Hill, Stebbins and Waga † used for dark energy:

```text
V(φ) = V₀[1 + cos(φ/f)]                  V(φ + 2πf) = V(φ)

maximum:   cos(φ/f) = +1      V″ = −V₀/f²
minimum:   cos(φ/f) = −1      V = 0,   V″ = +V₀/f² = m²
```

The form V₀[1 − cos(φ/f)], also common, is the same potential with φ shifted by πf. Of the continuous shift symmetry only the discrete shift φ → φ + 2πf survives [T].

Two properties follow.

- **Lightness.** The mass m at the minimum satisfies m² = V₀/f², in units with ħ = c = 1. It is small when the explicit breaking V₀ is small, and quantum corrections cannot generate a potential beyond what the explicit breaking allows, so the potential stays as small as that breaking [T].
- **Derivative couplings.** Apart from the potential and effects proportional to V₀, the field couples only through its derivatives ∂_μφ or through such total-derivative terms, so it carries no long-range static force between ordinary, unpolarized bodies ([why a shift symmetry removes the force](tau-fifth-force.md#why-a-shift-symmetry-removes-the-force-t)) [T].

Expanded about its minimum, the cosine gives the mass term and then a quartic term of negative sign, so the field's quanta attract one another [T]. In a dense clump of such a field the attraction sets a maximum mass, above which the clump collapses ([attractive condensates](../../dark-matter/wave-dark-matter/attractive-condensates.md)).

## The axion and axion-like particles [T]

The axion was proposed to explain why the strong interaction preserves the combined symmetry of charge conjugation and parity (CP) so closely, although its laws admit a term that breaks it. Peccei and Quinn † added a U(1) symmetry, broken spontaneously, and Weinberg † and Wilczek † identified its pseudo-Goldstone boson as a new light particle, the axion. The explicit breaking comes from the strong interaction itself, whose non-perturbative effects (instantons among them) generate the periodic potential; for this axion the mass and the decay constant are tied together [T].

"Axion-like" names any field with the same structure, an angle with an approximate shift symmetry, whose potential comes from some other explicit breaking; its mass and decay constant are then independent parameters [T].

### As dark matter

A light axion-like field displaced from its minimum in the early universe is held in place by the expansion and later oscillates about the minimum, and the oscillation behaves as cold matter: the [misalignment mechanism](../../dark-matter/wave-dark-matter/misalignment-mechanism.md), first worked out for the axion. For a very light field the quanta are so numerous in each region one de Broglie wavelength across that the dark matter behaves as a classical wave ([occupation number: particles or waves](../../dark-matter/wave-dark-matter/occupation-number.md); [wave dark matter](../../dark-matter/wave-dark-matter/_index.md)), and observations limit how light it can be ([bounds on fuzzy dark matter](../../dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds.md)). The attraction from the cosine gives dense clumps of axions, axion stars, a maximum mass. Levkov, Panin and Tkachev's simulations of their collapse, "Relativistic axions from collapsing Bose stars", are part of the checkpoint's reference [13]† ([the bosenova](../../dark-matter/wave-dark-matter/attractive-condensates.md#the-bosenova-t)).

### As dark energy

A field light enough to be still evolving today, with its energy mostly potential energy, acts as dark energy, a form of [quintessence](quintessence.md). Frieman, Hill, Stebbins and Waga (1995, [astro-ph/9505060](https://arxiv.org/abs/astro-ph/9505060)) proposed an ultralight pseudo-Nambu–Goldstone field with the potential V₀[1 + cos(φ/f)] for this role [T]. The wiki first cited the paper from model memory (†); the closed-universe note cites it as retrieved by live search [S], at its eq. 6, and records that neither the lab notebook (#1) nor checkpoint #11 cites the origin of the program's potential ([`notes/closed-universe.md` §2](../../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys); flag 54 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The shift symmetry addresses two standard difficulties of quintessence: it keeps the potential flat and the field light against quantum corrections, and it removes the long-range force that a light field coupled to ordinary matter through its value would produce [T].

A field near the maximum of the cosine is a hilltop model, and hilltop models thaw: the expansion holds the field nearly still, with w close to −1, w being the ratio of pressure to energy density, until the expansion has slowed enough for the field to move away from the top ([hilltop models](thawing-and-freezing.md#hilltop-models)). The curvature at the top, V″ = −V₀/f², sets how quickly it then moves.

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) cites an axion-quintessence analysis of data from the [Dark Energy Spectroscopic Instrument](desi.md) (DESI), Ureña-López et al., [arXiv:2503.20178](https://arxiv.org/abs/2503.20178) [20S]. The lab notebook says that "Hilltop/axion potentials of exactly this class have been fit directly to DESI DR1/DR2 by the collaboration and others" ([#1 §7 item 2](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround)), DR1 and DR2 being Data Release 1 and Data Release 2. The fits concern the class of models, not the program's identification of its field.

## How the program uses the idea

The record uses "axion-like" and "pseudo-Goldstone" in three senses, and compares one more field with the axion.

### τ: an axion-like dark-energy field

The program's dark-energy field is τ, the angle around the [Maslov circle](../../phase-space/modular-field/maslov-phase.md), a circle in the space of ways the vacuum can divide [phase space](../../phase-space/_index.md), the space of positions and momenta taken together, into position and momentum. [#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology): "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology". The lab notebook calls the model "hilltop axion quintessence" ([#1 §7](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround)), and the [handoff](../../history/documents/handoff.md) "hilltop/axion quintessence on the Maslov circle" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)).

The parts of the standard picture have different standing in the program.

- **The angle and its period.** For an axion the period 2πf comes from the scale at which a U(1) breaks. For τ the circle is a fact of topology: the lab notebook defines τ as "a compact, 2πf-periodic modulus of the vacuum" and states "Periodicity is topology **[D]**" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core), transcribed from its LaTeX; [τ as the Maslov phase of the boundary](../../phase-space/modular-field/maslov-phase.md)).
- **The cosine.** The topology fixes only the period; the cosine keeps the constant term and the first harmonic, the standard axion-like form ([why a cosine](tau-quintessence.md#why-a-cosine)).
- **The explicit breaking.** The lab notebook attributed the potential's existence to "the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle" [P/O] ([#1 §3](../../../notes/broken-born-theory.md#3-action)), the rotations being those of [the Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md), the space of polarizations; for the axion, the tilt comes from instanton effects of the strong interaction [T]. The account is superseded, and what breaks τ's shift symmetry is open ([Superseded: the potential's origin in the rigid ω](tau-quintessence.md#superseded-the-potentials-origin-in-the-rigid-ω); [Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md)).
- **Derivative couplings.** "τ is a (pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter, safe from torsion-balance bounds despite being ultralight. **[D]**" ([#1 §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured)), SM being the Standard Model ([fifth-force safety of τ](tau-fifth-force.md)).
- **The hilltop.** τ starts near the maximum of the cosine and thaws ([thawing and freezing quintessence](thawing-and-freezing.md)), the behaviour that [row 4](../../predictions/dark-energy-drift.md) tests.
- **The minimum.** As written the potential's lowest value is zero, while the documents' account of the program's far-future turnaround needs a negative vacuum energy; none of them reconciles the two ([Open: the sign of V(τ) and the turnaround](potential-sign.md); flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The flag's addendum (2026-10-27) finds that in a closed universe the expansion still turns around: τ passes the zero-energy minimum, oscillates about it as dust, and curvature reverses the expansion ([a closed Comatter universe](../scale-factor-duality/closed-universe.md)).

### The polarization angle in the toy models

The [toy models](../../symmetry-breaking/toy-models/_index.md) find that with only the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω rigid, [Born reciprocity](../../phase-space/reciprocity/born-reciprocity.md) ρ "sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]", and that "A definite polarization needs a ρ-preserving potential on that angle" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates); [the polarization as a Goldstone angle](../../symmetry-breaking/goldstone-angle.md)). In [model I](../../symmetry-breaking/toy-models/coset-model/_index.md), with its phase-space metric H at the value 1, the bounded potential is "V_b = −(μ/2)(1 + cos 2φ)" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [the bounded potential V_b](../../symmetry-breaking/toy-models/coset-model/bounded-potential.md)), a reduction that [`verify/toy_coset.py`](../../../verify/toy_coset.py) checks ([the toy-model scripts](../../method/verification/toy-model-scripts.md)). It is a cosine on the polarization circle with period π, unchanged by ρ, which acts as φ → φ + π. Its two minima are the vacua ±K_ref, which the worklog reads as "x is position" and "p is position" ('Chunk 3 results'). [#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) identifies the circle with τ's: "In the coset model that angle parametrizes Λ(1): it is τ's circle."

The worklog's revised conclusion uses this page's terms: the toy supports broken reciprocity in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential". For the program's own dimension it adds: "§10's τ has a potential, so the explicit breaking is in the program anyway" ([`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md), 'Chunk 3 results'). No document relates the toy's μ and φ quantitatively to τ's V₀ and f.

### X: axion-like in the exact sense

[#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t), step (i): "The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is shift-symmetric — axion-like, never auxiliary." [Calc note #6](../../history/documents/field-equation-notes.md) states the consequence: "X has no potential and no non-derivative couplings from the geometric sector alone — it is axion-like" ([#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous), [D — rigorous]). Here the word means an exact shift symmetry with no explicit breaking, and X differs from an axion-like field in two ways.

- **Not an angle.** X is a symmetric tensor field, the real part of the [modular field](../../phase-space/modular-field/modular-field-z.md) Z = X + iY, and the shift is by any constant symmetric matrix B; nothing in the record makes X periodic.
- **Mass from absorbed modes, not a tilt.** "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be." ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). X becomes massive by absorbing the Goldstone modes of broken [dual diffeomorphisms](../../gravity/momentum-graviton/dual-diffeomorphisms.md): "X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale" ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t), step (iii); [the gravitational Higgs mechanism](../../gravity/momentum-graviton/gravitational-higgs.md)).

The program's page for the symmetry is [shift symmetry: X is never auxiliary](../../gravity/momentum-graviton/shift-symmetry.md).

### Wave χ: produced "like an axion"

On [the wave island](../../dark-matter/momentum-clumping/wave-island/_index.md), the light end of the mass range of [conjugate matter](../../dark-matter/conjugate-matter/_index.md) χ, [calc note #3](../../history/documents/clumping-notes.md) borrows the axion's production route: "A field this light with only gravitational + self couplings is produced by misalignment, like an axion." ('Bonus: the relic-abundance problem solves itself'; [relic abundance by misalignment on the wave island](../../dark-matter/momentum-clumping/wave-island/misalignment-relic.md)). The comparison concerns production only. The lab notebook takes χ to be a "complex scalar or Dirac fermion" ([#1 §3](../../../notes/broken-born-theory.md#3-action)), and no document gives χ a shift symmetry or a periodic potential; its self-attraction on the wave island is a gated contact coupling, not the quartic term of a cosine ([attractive condensates](../../dark-matter/wave-dark-matter/attractive-condensates.md#why-there-is-a-maximum-mass-t)).

## What the record leaves open

- **What breaks τ's shift symmetry.** [Calc note #5](../../history/documents/field-equation-notes.md) lists "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" among the open problems ([#5 §F](../../../notes/geometric-core.md#f-status-after-tonight)); the toy models restate it as the need for a ρ-preserving potential ([Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md)).
- **The sign of the potential.** [Open: the sign of V(τ) and the turnaround](potential-sign.md); flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), whose addendum finds that a closed universe turns around with the potential as written.
- **Couplings beyond tree level.** The lab notebook claims "no tree-level Yukawa" and does not estimate couplings induced through the potential; it gives no mass for τ and no coupling scale ([why "pseudo"-Goldstone](tau-fifth-force.md#why-pseudo-goldstone-t)).
- **Mixing with the absorbed modes.** [Calc note #8](../../history/documents/field-equation-notes.md) logs "Residual τ–Stückelberg mixing through the potential: logged, expected small by compactness" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)), and it is item 6 of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) ([Open: τ–Stückelberg mixing (OP6)](../../gravity/momentum-graviton/tau-stuckelberg-mixing.md)).

## Standard references

Added by the wiki from model memory (†); the program's documents cite none of them, except Frieman et al., below.

- R. D. Peccei and H. R. Quinn †: the U(1) symmetry that removes the strong interaction's violation of charge conjugation and parity; S. Weinberg †; F. Wilczek †: the axion, its pseudo-Goldstone boson.
- J. A. Frieman, C. T. Hill, A. Stebbins and I. Waga (1995), [astro-ph/9505060](https://arxiv.org/abs/astro-ph/9505060): an ultralight pseudo-Nambu–Goldstone field as dark energy, with the potential V₀[1 + cos(φ/f)]. First added here †; the closed-universe note cites it [S] ([§2](../../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys); flag 54).
- D. J. E. Marsh, "Axion cosmology," Phys. Rep. (2016)†: a review, including ultralight axion-like fields.

Cited by the program: the checkpoint's [13]† includes D. G. Levkov, A. G. Panin, I. I. Tkachev, "Relativistic axions from collapsing Bose stars," Phys. Rev. Lett. 118, 011301 (2017).

## Used by

- [τ: hilltop quintessence on the Maslov circle](tau-quintessence.md) — the cosine, "the standard form for an axion-like field".
- [Fifth-force safety of τ](tau-fifth-force.md) — τ as a pseudo-Goldstone field, coupled through its derivatives.
- [τ as the Maslov phase of the boundary](../../phase-space/modular-field/maslov-phase.md) — the angle of a nearly flat direction.
- [Row 4: thawing dark energy, never phantom](../../predictions/dark-energy-drift.md) — the cosine as "the standard potential of an axion-like field".
- [The polarization as a Goldstone angle](../../symmetry-breaking/goldstone-angle.md) — a pseudo-Goldstone angle once a potential is added.
- [Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md) — the explicit breaking that the angle needs.
- [The bounded potential V_b](../../symmetry-breaking/toy-models/coset-model/bounded-potential.md) — a cosine on the polarization circle.
- [Shift symmetry: X is never auxiliary](../../gravity/momentum-graviton/shift-symmetry.md) — "axion-like" in the exact-shift sense.
- [Why X must be massive](../../gravity/momentum-graviton/forcing-chain.md) — step (i), "X is shift-symmetric — axion-like".
- [Relic abundance by misalignment on the wave island](../../dark-matter/momentum-clumping/wave-island/misalignment-relic.md) — χ "produced by misalignment, like an axion".

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) — τ as hilltop quintessence with V = V₀[1 + cos(τ/f)], periodicity by topology, the axion-quintessence fits, the coset model's angle as τ's circle; [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — the polarization as a Goldstone angle that needs a ρ-preserving potential [D][V]; [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — X shift-symmetric, "axion-like, never auxiliary", and its mass from the absorbed Goldstones; [§14 item 6](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — τ–Stückelberg mixing [O]
- [`wiki/papers/broken-born-checkpoint-v2.md`](../../papers/broken-born-checkpoint-v2.md) refs [13], [20] — relativistic axions from collapsing Bose stars (†); the axion-quintessence analysis of DESI data (live-searched)
- [`wiki/papers/reciprocity-toy-models.md` §4](../../papers/reciprocity-toy-models.md#4-quantum-stability) — V_b at H = 1 and its vacua ±K_ref
- [`verify/toy_coset.py`](../../../verify/toy_coset.py) — the check of V_b at H = 1
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — "hilltop/axion quintessence on the Maslov circle"
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Chunk 3 results' — the vacua ±K_ref as "x is position" and "p is position"; "a pseudo-Goldstone polarization angle with a ρ-symmetric potential"; the explicit breaking "in the program anyway"
- [`notes/x-classification.md` §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous) — X has no potential from geometry, "it is axion-like" [D — rigorous]; [§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the mass cannot be written by hand
- [`notes/geometric-core.md` §F](../../../notes/geometric-core.md#f-status-after-tonight) — the origin of τ's potential under P2′, open
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — residual τ–Stückelberg mixing "expected small by compactness"
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'Bonus: the relic-abundance problem solves itself' — χ produced by misalignment, "like an axion"
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core) — τ as a compact, 2πf-periodic modulus, periodicity [D]; [§3](../../../notes/broken-born-theory.md#3-action) — the potential, its v0.1 origin in the rigid ω [P/O], and χ as a complex scalar or Dirac fermion; [§4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured) — τ as a (pseudo-)Goldstone [D]; [§7](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround) — "hilltop axion quintessence" and the fits of hilltop and axion potentials
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 27 — the potential as written cannot go negative; its addendum — the closed turnaround
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 54 and [`notes/closed-universe.md` §2](../../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys) — the potential is Frieman, Hill, Stebbins and Waga's, uncited in #1 and #11, retrieved [S]
