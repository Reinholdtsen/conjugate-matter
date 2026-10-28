---
title: "Axion-like fields and pseudo-Goldstone bosons"
weight: 14
status: established
description: "A field that is an angle: a shift symmetry keeps it light and coupled only through its derivatives, and a small explicit breaking leaves the periodic potential V₀[1 + cos(φ/f)]. The axion, axion-like dark matter and dark energy, and the program's uses: τ's hilltop potential and fifth-force safety, the toy models' pseudo-Goldstone polarization angle, X 'axion-like' in the exact-shift sense, and wave χ produced 'like an axion'."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §14 item 6"
  - "papers/broken-born-checkpoint-v2.md refs [13], [20]"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §7"
  - "HANDOFF.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "verify/toy_coset.py"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt3b-wave-island.md 'Bonus: the relic debt closes itself'"
  - "review/wiki-build-flags.md item 27"
  - "review/wiki-build-flags.md item 54"
  - "notes/closed-universe.md §2"
---

*An axion-like field is a scalar field whose value is an angle. Its interactions are unchanged when the field is shifted by a constant, φ → φ + c, except for a small explicit breaking of that symmetry, which leaves a potential that repeats as the angle goes around its circle, in its standard form V₀[1 + cos(φ/f)]. Such a field is a pseudo-Goldstone boson: the massless mode that a spontaneously broken continuous symmetry leaves behind, given a small mass by a slight explicit breaking. The shift symmetry keeps the field light and lets it couple to other matter only through how it changes in space and time. The axion of the strong interaction is the original example; it and lighter fields of the same kind are studied as dark matter, and the lightest as dark energy. The Comatter program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is one: an angle with a cosine potential, starting near the potential's maximum. The program also calls its [momentum graviton X](/wiki/gravity/momentum-graviton) "axion-like" for its exact shift symmetry, and the worklog of its toy models describes the vacuum's choice of position and momentum as "a pseudo-Goldstone polarization angle".*

**Status:** Established — [T] — textbook particle physics and cosmology, written here from general knowledge, with the literature it names marked †; no `verify/` script checks it. The program's uses carry their own tags: τ's potential [D + T] ([checkpoint #11](/wiki/history/documents/checkpoint) §10), τ as a pseudo-Goldstone field [D] ([lab notebook](/wiki/history/documents/lab-notebook) #1 §4), the polarization as a Goldstone angle [D][V] (#11 §4) and the shift symmetry of X [D — rigorous] (calc note #6 §1).

## Goldstone and pseudo-Goldstone bosons [T]

When the lowest-energy state of a system breaks a continuous symmetry of its laws, the equally good ground states form a continuous family, and moving the whole system along that family costs no energy. A long-wavelength wave of that motion costs arbitrarily little, so it describes a massless particle, a Goldstone boson ([Goldstone's theorem](/wiki/symmetry-breaking/goldstone-and-higgs#goldstones-theorem)). A uniform shift along the family changes nothing physical, so at low energies the Goldstone field enters the interactions only through its derivatives [T].

If a small term in the laws breaks the symmetry explicitly, the family of ground states is tilted: its members no longer have equal energy ([spontaneous versus explicit breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking#spontaneous-versus-explicit-breaking)). The would-be Goldstone boson then moves in a shallow potential and has a small mass, which vanishes as the explicit term is switched off, and its couplings stay derivative apart from terms proportional to that term. It is called a pseudo-Goldstone boson. The pions are the standard example: the chiral symmetry of the strong interaction is broken spontaneously, the small quark masses break it explicitly, and the pions are light rather than massless [T]. The general account, with the program's toy-model applications and the zero mode that no symmetry protects, is on [pseudo-Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs#pseudo-goldstone-modes).

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
- **Derivative couplings.** Apart from the potential and effects proportional to V₀, the field couples only through its derivatives ∂_μφ or through such total-derivative terms, so it carries no long-range static force between ordinary, unpolarized bodies ([why a shift symmetry removes the force](/wiki/cosmology/dark-energy/tau-fifth-force#why-a-shift-symmetry-removes-the-force-t)) [T].

Expanded about its minimum, the cosine gives the mass term and then a quartic term of negative sign, so the field's quanta attract one another [T]. In a dense clump of such a field the attraction sets a maximum mass, above which the clump collapses ([attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)).

## The axion and axion-like particles [T]

The axion was proposed to explain why the strong interaction preserves the combined symmetry of charge conjugation and parity (CP) so closely, although its laws admit a term that breaks it. Peccei and Quinn † added a U(1) symmetry, broken spontaneously, and Weinberg † and Wilczek † identified its pseudo-Goldstone boson as a new light particle, the axion. The explicit breaking comes from the strong interaction itself, whose non-perturbative effects (instantons among them) generate the periodic potential; for this axion the mass and the decay constant are tied together [T].

"Axion-like" names any field with the same structure, an angle with an approximate shift symmetry, whose potential comes from some other explicit breaking; its mass and decay constant are then independent parameters [T].

### As dark matter

A light axion-like field displaced from its minimum in the early universe is held in place by the expansion and later oscillates about the minimum, and the oscillation behaves as cold matter: the [misalignment mechanism](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism), first worked out for the axion. For a very light field the quanta are so numerous in each region one de Broglie wavelength across that the dark matter behaves as a classical wave ([occupation number: particles or waves](/wiki/dark-matter/wave-dark-matter/occupation-number); [wave dark matter](/wiki/dark-matter/wave-dark-matter)), and observations limit how light it can be ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)). The attraction from the cosine gives dense clumps of axions, axion stars, a maximum mass. Levkov, Panin and Tkachev's simulations of their collapse, "Relativistic axions from collapsing Bose stars", are part of the checkpoint's reference [13]† ([the bosenova](/wiki/dark-matter/wave-dark-matter/attractive-condensates#the-bosenova-t)).

### As dark energy

A field light enough to be still evolving today, with its energy mostly potential energy, acts as dark energy, a form of [quintessence](/wiki/cosmology/dark-energy/quintessence). Frieman, Hill, Stebbins and Waga (1995, astro-ph/9505060) proposed an ultralight pseudo-Nambu–Goldstone field with the potential V₀[1 + cos(φ/f)] for this role [T]. The wiki first cited the paper from model memory (†); the closed-universe note cites it as retrieved by live search [S], at its eq. 6, and records that neither the lab notebook (#1) nor checkpoint #11 cites the origin of the program's potential (`notes/closed-universe.md` §2; flag 54 in `review/wiki-build-flags.md`). The shift symmetry addresses two standard difficulties of quintessence: it keeps the potential flat and the field light against quantum corrections, and it removes the long-range force that a light field coupled to ordinary matter through its value would produce [T].

A field near the maximum of the cosine is a hilltop model, and hilltop models thaw: the expansion holds the field nearly still, with w close to −1, w being the ratio of pressure to energy density, until the expansion has slowed enough for the field to move away from the top ([hilltop models](/wiki/cosmology/dark-energy/thawing-and-freezing#hilltop-models)). The curvature at the top, V″ = −V₀/f², sets how quickly it then moves.

#11 §10 cites an axion-quintessence analysis of data from the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI), Ureña-López et al., arXiv:2503.20178 [20S]. The lab notebook says that "Hilltop/axion potentials of exactly this class have been fit directly to DESI DR1/DR2 by the collaboration and others" (#1 §7 item 2), DR1 and DR2 being Data Release 1 and Data Release 2. The fits concern the class of models, not the program's identification of its field.

## How the program uses the idea

The record uses "axion-like" and "pseudo-Goldstone" in three senses, and compares one more field with the axion.

### τ: an axion-like dark-energy field

The program's dark-energy field is τ, the angle around the [Maslov circle](/wiki/phase-space/modular-field/maslov-phase), a circle in the space of ways the vacuum can divide [phase space](/wiki/phase-space), the space of positions and momenta taken together, into position and momentum. #11 §10: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology". The lab notebook calls the model "hilltop axion quintessence" (#1 §7), and the [handoff](/wiki/history/documents/handoff) "hilltop/axion quintessence on the Maslov circle" (`HANDOFF.md` §2).

The parts of the standard picture have different standing in the program.

- **The angle and its period.** For an axion the period 2πf comes from the scale at which a U(1) breaks. For τ the circle is a fact of topology: the lab notebook defines τ as "a compact, 2πf-periodic modulus of the vacuum" and states "Periodicity is topology **[D]**" (#1 §2, transcribed from its LaTeX; [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)).
- **The cosine.** The topology fixes only the period; the cosine keeps the constant term and the first harmonic, the standard axion-like form ([why a cosine](/wiki/cosmology/dark-energy/tau-quintessence#why-a-cosine)).
- **The explicit breaking.** The lab notebook attributed the potential's existence to "the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle" [P/O] (#1 §3), the rotations being those of [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian), the space of polarizations; for the axion, the tilt comes from instanton effects of the strong interaction [T]. The account is superseded, and what breaks τ's shift symmetry is open ([Superseded: the potential's origin in the rigid ω](/wiki/cosmology/dark-energy/tau-quintessence#superseded-the-potentials-origin-in-the-rigid-ω); [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).
- **Derivative couplings.** "τ is a (pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter, safe from torsion-balance bounds despite being ultralight. **[D]**" (#1 §4), SM being the Standard Model ([fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force)).
- **The hilltop.** τ starts near the maximum of the cosine and thaws ([thawing and freezing quintessence](/wiki/cosmology/dark-energy/thawing-and-freezing)), the behaviour that [row 4](/wiki/predictions/dark-energy-drift) tests.
- **The minimum.** As written the potential's lowest value is zero, while the program's far-future turnaround needs a negative vacuum energy; no document reconciles the two ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`). The flag's addendum (2026-10-27) finds that in a closed universe the expansion still turns around: τ passes the zero-energy minimum, oscillates about it as dust, and curvature reverses the expansion ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)).

### The polarization angle in the toy models

The [toy models](/wiki/symmetry-breaking/toy-models) find that with only the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω rigid, [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ "sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]", and that "A definite polarization needs a ρ-preserving potential on that angle" (#11 §4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). In [model I](/wiki/symmetry-breaking/toy-models/coset-model), with its phase-space metric H at the value 1, the bounded potential is "V_b = −(μ/2)(1 + cos 2φ)" (toy note §4; [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)), a reduction that `verify/toy_coset.py` checks ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). It is a cosine on the polarization circle with period π, unchanged by ρ, which acts as φ → φ + π. Its two minima are the vacua ±K_ref, which the worklog reads as "x is position" and "p is position" ('Chunk 3 results'). #11 §10 identifies the circle with τ's: "In the coset model that angle parametrizes Λ(1): it is τ's circle."

The worklog's revised conclusion uses this page's terms: the toy supports broken reciprocity in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential". For the program's own dimension it adds: "§10's τ has a potential, so the explicit breaking is in the program anyway" (`notes/toy-lagrangian.md`, 'Chunk 3 results'). No document relates the toy's μ and φ quantitatively to τ's V₀ and f.

### X: axion-like in the exact sense

#11 §7.1, step (i): "The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is shift-symmetric — axion-like, never auxiliary." [Calc note #6](/wiki/history/documents/debt-1-notes) states the consequence: "X has no potential and no non-derivative couplings from the geometric sector alone — it is axion-like" (#6 §1, [D — rigorous]). Here the word means an exact shift symmetry with no explicit breaking, and X differs from an axion-like field in two ways.

- **Not an angle.** X is a symmetric tensor field, the real part of the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, and the shift is by any constant symmetric matrix B; nothing in the record makes X periodic.
- **Mass from absorbed modes, not a tilt.** "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be." (#6 §3). X becomes massive by absorbing the Goldstone modes of broken [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms): "X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale" (#11 §7.1, step (iii); [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).

The program's page for the symmetry is [shift symmetry: X is never auxiliary](/wiki/gravity/momentum-graviton/shift-symmetry).

### Wave χ: produced "like an axion"

On [the wave island](/wiki/dark-matter/momentum-clumping/wave-island), the light end of the mass range of [conjugate matter](/wiki/dark-matter/conjugate-matter) χ, [Debt 3b](/wiki/history/documents/debt-3-notes) borrows the axion's production route: "A field this light with only gravitational + self couplings is produced by misalignment, like an axion." ('Bonus: the relic debt closes itself'; [relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)). The comparison concerns production only. The lab notebook takes χ to be a "complex scalar or Dirac fermion" (#1 §3), and no document gives χ a shift symmetry or a periodic potential; its self-attraction on the wave island is a gated contact coupling, not the quartic term of a cosine ([attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates#why-there-is-a-maximum-mass-t)).

## What the record leaves open

- **What breaks τ's shift symmetry.** [Calc note #5](/wiki/history/documents/debt-1-notes) lists "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" among the open problems (#5 §F); the toy models restate it as the need for a ρ-preserving potential ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).
- **The sign of the potential.** [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`, whose addendum finds that a closed universe turns around with the potential as written.
- **Couplings beyond tree level.** The lab notebook claims "no tree-level Yukawa" and does not estimate couplings induced through the potential; it gives no mass for τ and no coupling scale ([why "pseudo"-Goldstone](/wiki/cosmology/dark-energy/tau-fifth-force#why-pseudo-goldstone-t)).
- **Mixing with the absorbed modes.** [Calc note #8](/wiki/history/documents/debt-1-notes) logs "Residual τ–Stückelberg mixing through the potential: logged, expected small by compactness" (#8 §3), and it is item 6 of #11 §14 ([Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing)).

## Standard references

Added by the wiki from model memory (†); the program's documents cite none of them, except Frieman et al., below.

- R. D. Peccei and H. R. Quinn †: the U(1) symmetry that removes the strong interaction's violation of charge conjugation and parity; S. Weinberg †; F. Wilczek †: the axion, its pseudo-Goldstone boson.
- J. A. Frieman, C. T. Hill, A. Stebbins and I. Waga (1995), astro-ph/9505060: an ultralight pseudo-Nambu–Goldstone field as dark energy, with the potential V₀[1 + cos(φ/f)]. First added here †; the closed-universe note cites it [S] (§2; flag 54).
- D. J. E. Marsh, "Axion cosmology," Phys. Rep. (2016)†: a review, including ultralight axion-like fields.

Cited by the program: the checkpoint's [13]† includes D. G. Levkov, A. G. Panin, I. I. Tkachev, "Relativistic axions from collapsing Bose stars," Phys. Rev. Lett. 118, 011301 (2017).

## Used by

- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — the cosine, "the standard form for an axion-like field".
- [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force) — τ as a pseudo-Goldstone field, coupled through its derivatives.
- [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase) — the angle of a nearly flat direction.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the cosine as "the standard potential of an axion-like field".
- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) — a pseudo-Goldstone angle once a potential is added.
- [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) — the explicit breaking that the angle needs.
- [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) — a cosine on the polarization circle.
- [Shift symmetry: X is never auxiliary](/wiki/gravity/momentum-graviton/shift-symmetry) — "axion-like" in the exact-shift sense.
- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — step (i), "X is shift-symmetric — axion-like".
- [Relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic) — χ "produced by misalignment, like an axion".

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — τ as hilltop quintessence with V = V₀[1 + cos(τ/f)], periodicity by topology, the axion-quintessence fits, the coset model's angle as τ's circle; §4 — the polarization as a Goldstone angle that needs a ρ-preserving potential [D][V]; §7.1 — X shift-symmetric, "axion-like, never auxiliary", and its mass from the absorbed Goldstones; §14 item 6 — τ–Stückelberg mixing [O]
- `papers/broken-born-checkpoint-v2.md` refs [13], [20] — relativistic axions from collapsing Bose stars (†); the axion-quintessence analysis of DESI data (live-searched)
- `papers/reciprocity-toy-models.md` §4 — V_b at H = 1 and its vacua ±K_ref
- `verify/toy_coset.py` — the check of V_b at H = 1
- `HANDOFF.md` §2 — "hilltop/axion quintessence on the Maslov circle"
- `notes/toy-lagrangian.md` 'Chunk 3 results' — the vacua ±K_ref as "x is position" and "p is position"; "a pseudo-Goldstone polarization angle with a ρ-symmetric potential"; the explicit breaking "in the program anyway"
- `notes/debt1a-ii-X-classification.md` §1 — X has no potential from geometry, "it is axion-like" [D — rigorous]; §3 — the mass cannot be written by hand
- `notes/debt1a-geometric-core.md` §F — the origin of τ's potential under P2′, open
- `notes/debt1a-iv-beta-coefficients.md` §3 — residual τ–Stückelberg mixing "expected small by compactness"
- `notes/debt3b-wave-island.md` 'Bonus: the relic debt closes itself' — χ produced by misalignment, "like an axion"
- `notes/broken-born-theory.md` §2 — τ as a compact, 2πf-periodic modulus, periodicity [D]; §3 — the potential, its v0.1 origin in the rigid ω [P/O], and χ as a complex scalar or Dirac fermion; §4 — τ as a (pseudo-)Goldstone [D]; §7 — "hilltop axion quintessence" and the fits of hilltop and axion potentials
- `review/wiki-build-flags.md` item 27 — the potential as written cannot go negative; its addendum — the closed turnaround
- `review/wiki-build-flags.md` item 54 and `notes/closed-universe.md` §2 — the potential is Frieman, Hill, Stebbins and Waga's, uncited in #1 and #11, retrieved [S]
