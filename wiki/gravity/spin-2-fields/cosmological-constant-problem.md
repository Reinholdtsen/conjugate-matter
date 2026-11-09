---
title: "The cosmological-constant problem"
weight: 100
status: established
description: "Why quantum vacuum energy is predicted far above the observed value, why bimetric theory is no better placed than general relativity on it, and why the program's vacuum-energy identity, which concerns only the spin-2 potential, does not by itself address it; with the Cohen–Kaplan–Nelson bound that ties field theory's ultraviolet cutoff to the size of the region it describes, the geometric-mean length √(l_P L) it implies, and the problem restated through reciprocity as a fourth root."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.3"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [22]"
  - "wiki/papers/phase-space-diameter.md §4"
  - "wiki/papers/phase-space-diameter.md §5"
  - "wiki/papers/phase-space-diameter.md §7"
  - "wiki/papers/phase-space-diameter.md §8.1"
  - "wiki/papers/phase-space-diameter.md §8.2"
  - "wiki/papers/phase-space-diameter.md §8.6"
  - "wiki/papers/phase-space-diameter.md 'References'"
  - "verify/phase_space_diameter.py 'Extent, resolution and the published answers (note §4)'"
  - "verify/phase_space_diameter.py 'The self-dual box (note §7)'"
  - "review/round5-adjudication.md 'Rulings' R7, R9"
  - "HANDOFF.md §8"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/beta-coefficients.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §11"
  - "popsci/universes-other-half.md 'The second geometry, and why it has never been seen'"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
  - "review/wiki-build-flags.md item 6"
  - "notes/dual-sector.md §9"
  - "review/wiki-build-flags.md item 72"
---

*The cosmological-constant problem is the mismatch between the energy density of empty space that quantum field theory predicts, from the zero-point fluctuations and loops of matter fields, and the far smaller value that the accelerating expansion of the universe indicates. No accepted mechanism explains the gap, and [bimetric gravity](hassan-rosen-bimetric.md) is no better placed than [general relativity](general-relativity.md) to explain it. For the program this page marks a boundary. The program's [vacuum-energy identity](../palindromic-branch/vacuum-energy-identity.md) sets to zero only the vacuum energy of the spin-2 interaction potential at the aligned point; it does not by itself address the vacuum energy of matter loops. The program assigns the observed [dark energy](../../cosmology/dark-energy/_index.md) to a separate field, [τ](../../cosmology/dark-energy/tau-quintessence.md). A bound due to Cohen, Kaplan and Nelson ties the highest energy at which field theory can be trusted to the size of the region it describes, and for a region the size of the Hubble radius it puts that energy within a factor of two of the observed dark-energy scale; by its authors' own statement it does not predict the cosmological constant's value.*

**Status:** Established — [T] — an unsolved problem of physics, recorded here as literature. The [checkpoint](../../history/documents/checkpoint.md) cites [22S], retrieved by live search, for the statement that bimetric theory is no better placed than general relativity on it ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)). The Cohen–Kaplan–Nelson bound [T] is quoted from the phase-space-diameter note, which retrieved the paper by live search [S] ([`wiki/papers/phase-space-diameter.md` §4](../../papers/phase-space-diameter.md#4-extent-and-resolution-and-the-published-answers)), and the bound's value for the Hubble radius and its conventions are printed by [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) ([the phase-space-diameter script](../../method/verification/phase-space-diameter-script.md)).

## What the problem is

### Vacuum energy in quantum field theory

In quantum field theory every mode of every field keeps a zero-point energy proportional to its frequency, even in the vacuum [T]. Summed over modes up to the highest energy at which the theory is trusted, these give a vacuum energy density set by that cutoff. Loops of massive particles add contributions set by their masses, and each phase transition in the [early universe](../../cosmology/early-universe/_index.md), such as electroweak symmetry breaking, shifts the vacuum energy by an amount set by its own energy scale [T].

### Vacuum energy gravitates

General relativity couples gravity to every form of energy [T]. The vacuum looks the same to every observer, so its stress-energy tensor is proportional to the metric, T_μν = −ρ_vac g_μν (mostly-plus sign convention), which is exactly the form of a [cosmological constant](../../cosmology/dark-energy/cosmological-constant.md#λ-as-vacuum-energy-t). A vacuum energy density ρ_vac therefore adds to the cosmological constant Λ, and only the total, the constant in the gravitational action plus all vacuum contributions, is observable [T].

### The size of the mismatch

The expansion of the universe is accelerating, consistent with a small positive cosmological constant [T] ([dark energy](../../cosmology/dark-energy/_index.md)). A popular article of the program states the size of the mismatch: "straightforward estimates exceed the measured value by some hundred and twenty orders of magnitude" ([#12](../../../popsci/universes-other-half.md), 'The second geometry, and why it has never been seen'; [the popular articles](../../history/documents/popular-articles.md)). The article gives no citation, and no verification script checks the figure. It is the usual statement of the problem [T], quoted here with that provenance. The phase-space-diameter note states the observed constant in Planck units, "Λl_P² ~ 10⁻¹²²", and [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) prints log₁₀(Λl_P²) = −121.5 [V] ([`wiki/papers/phase-space-diameter.md` §7](../../papers/phase-space-diameter.md#7-a-self-dual-cosmic-box)).

### Why it is hard

To match the observed value, the constant in the action must cancel the vacuum contributions to very high precision, and the cancellation would have to be redone at each order of perturbation theory and across each phase transition [T]. In the language of naturalness, a small parameter is stable against quantum corrections when setting it to zero enlarges the symmetry of the theory; a fermion mass, protected by chiral symmetry, is the standard example. No unbroken symmetry of the Standard Model coupled to general relativity requires the vacuum energy to vanish, so nothing protects a small value [T].

In a common usage, the "old" problem asks why the vacuum energy is not enormous, and a newer one asks why it is small but not zero [T]. The checkpoint uses the word in the first sense: matter-loop vacuum energy is "the 'old' cosmological-constant problem" ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)).

## Ultraviolet and infrared cutoffs tied by gravity [T]

### The Cohen–Kaplan–Nelson bound

The estimate above depends on the highest energy at which field theory is trusted, its ultraviolet cutoff. A field theory applied to a finite region also has a largest length, the size of the region, which is its infrared cutoff [T]. In ordinary field theory the two cutoffs are independent. Cohen, Kaplan and Nelson tie them through gravity: in the phase-space-diameter note's summary, they require that an effective field theory in a box of size L, cut off at energy Λ_UV, hold no more energy than a black hole of the same size ([`wiki/papers/phase-space-diameter.md` §4](../../papers/phase-space-diameter.md#4-extent-and-resolution-and-the-published-answers)). Their inequality, and the bound on the cutoff it gives, are

```text
L³Λ⁴ ≲ L M_P²        so        Λ_UV ≲ (M_P/L)^(1/2)        (natural units)
```

with M_P the unreduced Planck mass ([two conventions for the Planck mass](planck-units.md#two-conventions-for-the-planck-mass-t)). In their formulas Λ is the ultraviolet cutoff, not the cosmological constant. The larger the region, the lower the energy to which a field theory describing it can be trusted. For an infrared cutoff at the present horizon they find "Λ ∼ 10^{−2.5} eV"; with L = c/H₀, the Hubble radius, the bound is 4.19 meV, and [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) prints the base-ten logarithm of the bound in electronvolts, −2.378, beside their −2.5 [V] (note §4). They add:

> "This observation does not predict the cosmological constant's value" (Cohen, Kaplan and Nelson 1999 [S], as quoted in note §4)

The bound also limits the entropy such a theory can hold. When it is near saturation, "the entropy is S_max ≃ S_BH^{3/4}", with S_BH the black-hole entropy of a region of the same size (their eq. 3, quoted in note §4).

### The geometric-mean length

With ħ and c restored, the bound's energy is the energy of a length (note §7) [T][V]:

```text
ħc/√(l_P L) = √(E_P ħc/L)
```

where E_P is the unreduced Planck energy and √(l_P L) is the geometric mean of the Planck length and the size of the region: 47.1 μm for the Hubble radius. Other conventions change the energy by a factor of order one: 0.45 with the reduced Planck mass, 0.59 or 0.84 with an explicit black-hole mass for a sphere or a cube of size L, and 2.08 if the vacuum energy is taken as one scalar field's zero-point energy Λ⁴/16π² [V] (note §7; round-5 ruling R9 asked for that assumption to be stated).

For the Hubble radius the bound's energy, 4.19 meV, lies within a factor of two of the observed dark-energy scale ρ_Λ^{1/4} = 2.24 meV. The note shows that the ratio of the two is (3Ω_Λ/8π)^{1/4} = 0.535 for any value of H₀, so the agreement restates the Friedmann equation with Ω_Λ of order one today and "carries no further information" [D][V] (note §7).

The same length is the cell length of the Born-geometry papers of Freidel, Kowalski-Glikman, Leigh and Minic, who tie it to the vacuum energy, and the one Born length for which [Born reciprocity](../../phase-space/reciprocity/born-reciprocity.md) maps the phase-space box from the Planck length to L onto itself: [the self-dual cosmic box](../../cosmology/scale-factor-duality/self-dual-cosmic-box.md), which also lists the length's earlier appearances in the literature (note §4, §7).

### Holographic dark energy

If the infrared length follows the expansion, a vacuum energy set at the bound changes with time [T]. With the Hubble radius as that length, the vacuum energy tracks the matter density, which is excluded [S: [Hsu 2004](https://arxiv.org/abs/hep-th/0403052)]; holographic dark energy with the event horizon as its infrared length is the variant that survives [S: [Li 2004](https://arxiv.org/abs/hep-th/0403127)] (note §7). In the Born-geometry lineage, a dual-spacetime model with ultraviolet–infrared mixing gives a dark energy whose [equation of state](../../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state) w, the ratio of its pressure to its energy density, varies in time with w > −1 (−1 is the value for a cosmological constant), and its authors find it compatible with the data of the [Dark Energy Spectroscopic Instrument (DESI)](../../cosmology/dark-energy/desi.md) [S: [Hur, Jejjala, Kavic, Minic and Takeuchi 2025](https://arxiv.org/abs/2503.20854)] (note §7). That is the second of the paper's two models. Under an ultraviolet–infrared relation from its authors' earlier work the same paper finds the opposite sign, "Clearly, w(a)<-1 for all a as anticipated", and "this model is clearly disfavored" by DESI's second data release (the paper's §3.3); w(a) ≥ −1 holds in all cases only under the alternative relation (its §3.4). The sign follows from an assumed relation, so the authors make no fixed prediction on the program's [row 4](../../predictions/dark-energy-drift.md), the test of w ≥ −1 ([`notes/dual-sector.md` §9](../../../notes/dual-sector.md#9-other-overlaps); flag 72, pending; [further overlaps with the program](../../dark-matter/conjugate-matter/dual-standard-model.md#further-overlaps-with-the-program)). The root [`CLAUDE.md`](../../../CLAUDE.md) lists the paper among the leads of the note's literature sweep that bear on reading DESI's data against the program's strict w ≥ −1, not on the work queue ('Since the handoff').

## Bimetric theory and the problem

### Two constant terms

[Hassan–Rosen bimetric gravity](hassan-rosen-bimetric.md) has two metrics, g and f, and a potential √|g| Σ βₙ eₙ(√(g⁻¹f)) with five constant coefficients β₀ to β₄ [T]. Two of its terms have the form of a cosmological constant. The n = 0 term, √|g| β₀, is a cosmological constant for g. The n = 4 term equals √|f| β₄, because e₄(√(g⁻¹f)) = √(det f / det g), so it is a cosmological constant for f [T] ([elementary symmetric polynomials](elementary-symmetric-polynomials.md#inversion-reverses-the-order)). A vacuum energy of matter that couples to g has the same form as the β₀ term [T].

### No better placed than general relativity

On matter-loop vacuum energy, the checkpoint states, "bimetric theory is otherwise no better placed than GR [22S]" ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)), GR being general relativity. Its reference:

- [22][S] A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), [arXiv:1512.00021](https://arxiv.org/abs/1512.00021).

### The no-protecting-symmetry statement

The [handoff](../../history/documents/handoff.md)'s queue asked whether the program's identity survives a convention-careful comparison with three works, the last being "the Schmidt-May–von Strauss review's no-protecting-symmetry statement" ([HANDOFF §8 item 5](../../../HANDOFF.md#8-ranked-next-actions-queue)). The handoff names the statement without quoting it, and the repository does not record its wording. The comparison is part of [Open: the partially-massless comparison (OP2)](../palindromic-branch/pm-comparison.md), which is in item 1 of the current queue ([`CLAUDE.md`](../../../CLAUDE.md), "Since the handoff").

## How the program relates to it

### What the identity cancels

The program's gravity sector has a Hassan–Rosen potential whose coefficients [Born reciprocity](../../phase-space/reciprocity/born-reciprocity.md) restricts to βₙ = β₄₋ₙ ([the palindrome βₙ = β₄₋ₙ](../palindromic-branch/palindrome.md)). At the aligned point, where the two frames coincide, the potential's value V(1) and its tadpole T then satisfy V(1) = 2T, and a flat aligned vacuum forces T = 0 and V(1) = 0 ([#8](../../history/documents/field-equation-notes.md) [§2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines); [#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)). Battery test T5 checks the integer identity behind it ([the verification battery](../../method/verification/battery.md)). In the checkpoint's words, "the wedge sector contributes zero cosmological constant, by symmetry" ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv), italic in the original; on "by symmetry", see flag 6 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The derivation is on [the vacuum-energy identity V(1) = 2T](../palindromic-branch/vacuum-energy-identity.md).

### What it does not cancel

The checkpoint states the limit directly:

> Scope, stated carefully: this cancels the spin-2 interaction potential's vacuum contribution at the aligned point — it does **not** by itself address matter-loop vacuum energy, the "old" cosmological-constant problem, on which bimetric theory is otherwise no better placed than GR [22S]. ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv))

The identity relates combinations of the potential's own coefficients. By #11's statement it does not by itself address the vacuum energy that matter loops contribute, which is the subject of this page.

### Where the observed dark energy goes

Calc note [#8](../../../notes/beta-coefficients.md) draws the consequence for cosmology: "The massive-gravity sector contributes *nothing* to the cosmological constant; dark energy is left entirely to the τ sector, which is precisely the architecture the cosmology chapter had assumed" ([#8 §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines)). The τ field is [hilltop quintessence on the Maslov circle](../../cosmology/dark-energy/tau-quintessence.md). That sector is under pressure from data: [Dark Energy Spectroscopic Instrument (DESI)](../../cosmology/dark-energy/desi.md) Data Release 2 favors a phantom crossing above [redshift](../../cosmology/scale-factor-duality/redshift.md) z ≈ 0.4 (z is the stretching of light by the expansion of the universe since the light was emitted, and larger z means earlier), "against the framework's strict w ≥ −1" ([the no-phantom bound](../../cosmology/dark-energy/no-phantom-bound.md)), and "The dark-energy sector is under real pressure ahead of DR3" ([`CLAUDE.md`](../../../CLAUDE.md), "Since the handoff"; DR3 is Data Release 3). See [DESI DR2's phantom crossing](../../cosmology/dark-energy/desi-dr2-phantom-crossing.md).

### The problem restated through reciprocity

The phase-space-diameter note writes the observed constant through the self-dual length λ = √(l_P L_Λ), with L_Λ the de Sitter radius ([`wiki/papers/phase-space-diameter.md` §7](../../papers/phase-space-diameter.md#7-a-self-dual-cosmic-box)). Then L_Λ = λ²/l_P, the de Sitter radius is where Born reciprocity sends the Planck momentum ħ/l_P, and

```text
Λ = 3 l_P² / λ⁴,        λ/l_P = 3.2×10³⁰ = √(L_Λ/l_P)
```

[D][V], which is Berglund, Hübsch and Minic's λ_cc = l_P²/l_Λ⁴ up to the factor 3 they drop [S]. The problem, Λl_P² ~ 10⁻¹²², becomes the hierarchy λ/l_P = 3.2×10³⁰; [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) prints log₁₀(Λl_P²) = −121.5 against log₁₀(λ/l_P) = 30.5. The note's verdict: "This takes the fourth root of the problem and explains nothing while λ is defined through Λ. It would predict Λ only if λ were fixed by other physics." (§7; round-5 ruling R7 finds a fourth root, not a halving of the exponent.) With the Born length at the Planck length instead, as [the program's paper on conjugate special relativity](../../conjugate-relativity/_index.md) sets it, the cosmic box has the aspect ratio "A = L/l_P = 8.5×10⁶⁰ for the Hubble radius, and the cosmological-constant problem is the size of that number squared" (§8.1). The note excludes the self-dual length as the program's own Born length, and the claim that the length is a program scale is under review ([Under review: the self-dual length as a program scale](../../cosmology/scale-factor-duality/self-dual-length-obituary.md)); the record derives neither λ nor the momentum graviton's mass from the program's dynamics, which the note sets as the condition for a prediction (§5, §8.2, §8.6; [the self-dual cosmic box](../../cosmology/scale-factor-duality/self-dual-cosmic-box.md)).

### Reading the popular articles

#12 gives the hundred-and-twenty-orders figure in the paragraph that describes the program's cancellation, and [#10](../../../popsci/angle-of-the-mirror.md) frames the cancellation by calling the energy of empty space "among the most notorious embarrassments in physics" (#10, 'What refused to die'). #12 says only that the new field, "which might have been expected to worsen the problem — contributes precisely zero", but setting the two side by side invites a reading that [#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv) rules out: the cancellation does not by itself address the hundred-and-twenty-orders gap. The popular articles are never a source for a claim's status.

## Superseded: the cancellation framed as a cosmological-constant result

Earlier documents described the result more broadly than #11 does:

- The v1 program paper, [#9](../../../notes/broken-born-program-v1.md) ([the checkpoint's versions](../../history/documents/checkpoint.md)): "A cosmological-constant cancellation for free, from symmetry." ([§5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), plain-language passage); "*the massive sector's vacuum energy is zero by symmetry.*" ([§5 item 5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved)); and in its assessment, "the last one yielded a cosmological-constant cancellation nobody ordered", with "the palindrome theorem cancelling the symmetric-bimetric vacuum energy" among "two results that stand on their own" ([§11](../../../notes/broken-born-program-v1.md#11-assessment)).
- The [lab notebook](../../history/documents/lab-notebook.md), [#1](../../../notes/broken-born-theory.md): "the massive-gravity sector contributes zero cosmological constant, by symmetry rather than tuning" ('Addendum (v0.6)'; see flag 6 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

The checkpoint replaced these with a narrower statement. The cancellation concerns the [wedge sector](vielbein-formulation.md), the spin-2 interaction potential, at the aligned point; the identity does not by itself address matter-loop vacuum energy ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)); and the identity's novelty is downgraded pending a literature comparison ([#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade)), leaving "one identity awaiting a novelty verdict" ([#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment)). #9 and #1 are superseded as reference by #11. The current statement lives on [the vacuum-energy identity V(1) = 2T](../palindromic-branch/vacuum-energy-identity.md).

## Standard references

- [22][S] A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), [arXiv:1512.00021](https://arxiv.org/abs/1512.00021) — cited by #11.
- [S] A. G. Cohen, D. B. Kaplan, A. E. Nelson, "Effective field theory, black holes, and the cosmological constant," Phys. Rev. Lett. 82, 4971 (1999), [arXiv:hep-th/9803132](https://arxiv.org/abs/hep-th/9803132) — retrieved for the phase-space-diameter note.
- [S] S. D. H. Hsu, "Entropy bounds and dark energy," Phys. Lett. B 594, 13 (2004), [arXiv:hep-th/0403052](https://arxiv.org/abs/hep-th/0403052); M. Li, "A model of holographic dark energy," Phys. Lett. B 603, 1 (2004), [arXiv:hep-th/0403127](https://arxiv.org/abs/hep-th/0403127) — retrieved for the same note.
- [S] S. Hur, V. Jejjala, M. J. Kavic, D. Minic, T. Takeuchi, "Dynamical dark energy, dual spacetime, and DESI," JCAP 11 (2025) 054, [arXiv:2503.20854](https://arxiv.org/abs/2503.20854) — retrieved for the same note; its two models, of opposite signs of 1 + w, are read in [`notes/dual-sector.md` §9](../../../notes/dual-sector.md#9-other-overlaps).
- Added by the wiki from model memory (†): S. Weinberg, "The cosmological constant problem," Rev. Mod. Phys. 61, 1 (1989)†, the classic review; J. Martin (2012)†, a more recent review of the problem.

## Used by

- [The vacuum-energy identity V(1) = 2T](../palindromic-branch/vacuum-energy-identity.md) — the identity's scope limit.
- [Open: the partially-massless comparison (OP2)](../palindromic-branch/pm-comparison.md) — the comparison includes the review's no-protecting-symmetry statement.
- [τ: hilltop quintessence on the Maslov circle](../../cosmology/dark-energy/tau-quintessence.md) — the observed dark energy is assigned to τ.
- [The self-dual cosmic box](../../cosmology/scale-factor-duality/self-dual-cosmic-box.md) — the Cohen–Kaplan–Nelson cutoff as the energy of the self-dual length; Λ = 3l_P²/λ⁴, the problem's fourth root.
- [Under review: the self-dual length as a program scale](../../cosmology/scale-factor-duality/self-dual-length-obituary.md) — at the Planck value of the Born length, the problem is the square of the cosmic box's aspect ratio.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv), ref [22] — the identity's scope, "the 'old' cosmological-constant problem", and the citation, marked [S].
- [`wiki/papers/broken-born-checkpoint-v2.md` §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade), [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the novelty downgrade; "one identity awaiting a novelty verdict".
- [`wiki/papers/phase-space-diameter.md` §4](../../papers/phase-space-diameter.md#4-extent-and-resolution-and-the-published-answers) — the Cohen–Kaplan–Nelson bound, its quotations and its saturation entropy
- [`wiki/papers/phase-space-diameter.md` §7](../../papers/phase-space-diameter.md#7-a-self-dual-cosmic-box) — the bound's energy as that of the length √(l_P L), its conventions, the Friedmann identity 0.535, holographic dark energy (Hsu, Li), the dual-spacetime dark energy of Hur et al., Λ = 3l_P²/λ⁴ and the fourth root; [§8.1](../../papers/phase-space-diameter.md#81-not-the-born-length-of-the-dual-special-relativity-dv) — the problem as the square of the box's aspect ratio at the Planck length; [§5](../../papers/phase-space-diameter.md#5-what-reciprocity-adds-invariant-area-inverted-shape) — the action singles out no Born length; [§8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs) — M_X with "no value in the record"; [§8.6](../../papers/phase-space-diameter.md#86-what-would-test-this) — a prediction only if the program derived λ or M_X; 'References' — the citations, marked [S]
- [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) — sections "Extent, resolution and the published answers (note §4)" and "The self-dual box (note §7)": 4.19 meV, −2.378, the conventions, 0.535, −121.5 and 30.5
- [`review/round5-adjudication.md`](../../../review/round5-adjudication.md) 'Rulings' R7, R9 — the fourth root in place of "halves the exponent"; the conventions spelled out
- [`HANDOFF.md` §8 item 5](../../../HANDOFF.md#8-ranked-next-actions-queue) — the no-protecting-symmetry statement in the queued comparison.
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the dark-energy sector under pressure; the comparison in the current queue; Hur et al. 2025 among the leads, not queued.
- [`notes/beta-coefficients.md` §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines) — the derivation; dark energy left to the τ sector.
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.6)' — the earlier framing (superseded as reference).
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), [§11](../../../notes/broken-born-program-v1.md#11-assessment) — v1's "cosmological-constant cancellation for free" (superseded by #11).
- [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'The second geometry, and why it has never been seen' — the hundred-and-twenty-orders figure (a popular article, never a status source).
- [`popsci/angle-of-the-mirror.md`](../../../popsci/angle-of-the-mirror.md) 'What refused to die' — the cancellation framed through the cosmological constant (a popular article).
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 6 — "by symmetry rather than tuning" recorded as an overstatement, and [#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)'s "by symmetry" marked for checking (pending).
- [`notes/dual-sector.md` §9](../../../notes/dual-sector.md#9-other-overlaps); [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 72 — Hur et al. 2025's two models, w(a) < −1 under the group's earlier ultraviolet–infrared relation and w(a) ≥ −1 under the alternative, of which the diameter note cites the second (pending)
