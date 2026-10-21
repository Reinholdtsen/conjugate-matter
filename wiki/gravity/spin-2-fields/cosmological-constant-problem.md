---
title: "The cosmological-constant problem"
weight: 100
status: established
description: "Why quantum vacuum energy is predicted far above the observed value, why bimetric theory is no better placed than general relativity on it, and why the program's vacuum-energy identity, which concerns only the spin-2 potential, does not by itself address it."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md ref [22]"
  - "HANDOFF.md §8"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §11"
  - "popsci/universes-other-half.md 'The second geometry, and why it has never been seen'"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
---

*The cosmological-constant problem is the mismatch between the energy density of empty space that quantum field theory predicts, from the zero-point fluctuations and loops of matter fields, and the far smaller value that the accelerating expansion of the universe indicates. No accepted mechanism explains the gap, and [bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) is no better placed than [general relativity](/wiki/gravity/spin-2-fields/general-relativity) to explain it. For the program this page marks a boundary. The program's [vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) sets to zero only the vacuum energy of the spin-2 interaction potential at the aligned point; it does not by itself address the vacuum energy of matter loops. The program assigns the observed [dark energy](/wiki/cosmology/dark-energy) to a separate field, [τ](/wiki/cosmology/dark-energy/tau-quintessence).*

**Status:** Established — [T] — an unsolved problem of physics, recorded here as literature. The [checkpoint](/wiki/history/documents/checkpoint) cites [22S], retrieved by live search, for the statement that bimetric theory is no better placed than general relativity on it (#11 §7.3).

## What the problem is

### Vacuum energy in quantum field theory

In quantum field theory every mode of every field keeps a zero-point energy proportional to its frequency, even in the vacuum [T]. Summed over modes up to the highest energy at which the theory is trusted, these give a vacuum energy density set by that cutoff. Loops of massive particles add contributions set by their masses, and each phase transition in the early universe, such as electroweak symmetry breaking, shifts the vacuum energy by an amount set by its own energy scale [T].

### Vacuum energy gravitates

General relativity couples gravity to every form of energy [T]. The vacuum looks the same to every observer, so its stress-energy tensor is proportional to the metric, T_μν = −ρ_vac g_μν (mostly-plus sign convention), which is exactly the form of a cosmological constant. A vacuum energy density ρ_vac therefore adds to the cosmological constant Λ, and only the total, the constant in the gravitational action plus all vacuum contributions, is observable [T].

### The size of the mismatch

The expansion of the universe is accelerating, consistent with a small positive cosmological constant [T] ([dark energy](/wiki/cosmology/dark-energy)). The program's documents state the size of the mismatch only in a popular article: "straightforward estimates exceed the measured value by some hundred and twenty orders of magnitude" (#12, 'The second geometry, and why it has never been seen'; [the popular articles](/wiki/history/documents/popular-articles)). The article gives no citation, and no verification script checks the figure. It is the usual statement of the problem [T], quoted here with that provenance.

### Why it is hard

To match the observed value, the constant in the action must cancel the vacuum contributions to very high precision, and the cancellation would have to be redone at each order of perturbation theory and across each phase transition [T]. In the language of naturalness, a small parameter is stable against quantum corrections when setting it to zero enlarges the symmetry of the theory; a fermion mass, protected by chiral symmetry, is the standard example. No unbroken symmetry of the Standard Model coupled to general relativity requires the vacuum energy to vanish, so nothing protects a small value [T].

In a common usage, the "old" problem asks why the vacuum energy is not enormous, and a newer one asks why it is small but not zero [T]. The checkpoint uses the word in the first sense: matter-loop vacuum energy is "the 'old' cosmological-constant problem" (#11 §7.3).

## Bimetric theory and the problem

### Two constant terms

[Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) has two metrics, g and f, and a potential √|g| Σ βₙ eₙ(√(g⁻¹f)) with five constant coefficients β₀ to β₄ [T]. Two of its terms have the form of a cosmological constant. The n = 0 term, √|g| β₀, is a cosmological constant for g. The n = 4 term equals √|f| β₄, because e₄(√(g⁻¹f)) = √(det f / det g), so it is a cosmological constant for f [T] ([elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials#inversion-reverses-the-order)). A vacuum energy of matter that couples to g has the same form as the β₀ term [T].

### No better placed than general relativity

On matter-loop vacuum energy, the checkpoint states, "bimetric theory is otherwise no better placed than GR [22S]" (#11 §7.3), GR being general relativity. Its reference:

- [22][S] A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), arXiv:1512.00021.

### The no-protecting-symmetry statement

The [handoff](/wiki/history/documents/handoff)'s queue asked whether the program's identity survives a convention-careful comparison with three works, the last being "the Schmidt-May–von Strauss review's no-protecting-symmetry statement" (HANDOFF §8 item 5). The handoff names the statement without quoting it, and the repository does not record its wording. The comparison is part of [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison), which is in item 1 of the current queue (`CLAUDE.md`, "Since the handoff").

## How the program relates to it

### What the identity cancels

The program's gravity sector has a Hassan–Rosen potential whose coefficients [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) restricts to βₙ = β₄₋ₙ ([the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome)). At the aligned point, where the two frames coincide, the potential's value V(1) and its tadpole T then satisfy V(1) = 2T, and a flat aligned vacuum forces T = 0 and V(1) = 0 ([#8](/wiki/history/documents/debt-1-notes) §2; #11 §7.3). Battery test T5 checks the integer identity behind it ([the verification battery](/wiki/method/verification/battery)). In the checkpoint's words, "the wedge sector contributes zero cosmological constant, by symmetry" (#11 §7.3, italic in the original). The derivation is on [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity).

### What it does not cancel

The checkpoint states the limit directly:

> Scope, stated carefully: this cancels the spin-2 interaction potential's vacuum contribution at the aligned point — it does **not** by itself address matter-loop vacuum energy, the "old" cosmological-constant problem, on which bimetric theory is otherwise no better placed than GR [22S]. (#11 §7.3)

The identity relates combinations of the potential's own coefficients. By #11's statement it does not by itself address the vacuum energy that matter loops contribute, which is the subject of this page.

### Where the observed dark energy goes

Calc note #8 draws the consequence for cosmology: "The massive-gravity sector contributes *nothing* to the cosmological constant; dark energy is left entirely to the τ sector, which is precisely the architecture the cosmology chapter had assumed" (#8 §2). The τ field is [hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence). That sector is under pressure from data: [Dark Energy Spectroscopic Instrument (DESI)](/wiki/cosmology/dark-energy/desi) Data Release 2 favors a phantom crossing above z ≈ 0.4, "against the framework's strict w ≥ −1" ([the no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound)), and "The dark-energy sector is under real pressure ahead of DR3" (`CLAUDE.md`, "Since the handoff"; DR3 is Data Release 3). See [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).

### Reading the popular articles

#12 gives the hundred-and-twenty-orders figure in the paragraph that describes the program's cancellation, and #10 frames the cancellation by calling the energy of empty space "among the most notorious embarrassments in physics" (#10, 'What refused to die'). #12 says only that the new field, "which might have been expected to worsen the problem — contributes precisely zero", but setting the two side by side invites a reading that #11 §7.3 rules out: the cancellation does not by itself address the hundred-and-twenty-orders gap. The popular articles are never a source for a claim's status.

## Superseded: the cancellation framed as a cosmological-constant result

Earlier documents described the result more broadly than #11 does:

- The v1 program paper, #9 ([the checkpoint's versions](/wiki/history/documents/checkpoint)): "A cosmological-constant cancellation for free, from symmetry." (§5, plain-language passage); "*the massive sector's vacuum energy is zero by symmetry.*" (§5 item 5); and in its assessment, "the last one paid out a cosmological-constant cancellation nobody ordered", with "the palindrome theorem cancelling the symmetric-bimetric vacuum energy" among "two results that stand on their own" (§11).
- The [lab notebook](/wiki/history/documents/lab-notebook), #1: "the massive-gravity sector contributes zero cosmological constant, by symmetry rather than tuning" ('Addendum (v0.6)').

The checkpoint replaced these with a narrower statement. The cancellation concerns the [wedge sector](/wiki/gravity/spin-2-fields/vielbein-formulation), the spin-2 interaction potential, at the aligned point; the identity does not by itself address matter-loop vacuum energy (#11 §7.3); and the identity's novelty is downgraded pending a literature comparison (#11 §7.4), leaving "one identity awaiting a novelty verdict" (#11 §15). #9 and #1 are superseded as reference by #11. The current statement lives on [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity).

## Standard references

- [22][S] A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), arXiv:1512.00021 — cited by #11.
- Added by the wiki from model memory (†): S. Weinberg, "The cosmological constant problem," Rev. Mod. Phys. 61, 1 (1989)†, the classic review; J. Martin (2012)†, a more recent review of the problem.

## Used by

- [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) — the identity's scope limit.
- [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison) — the comparison includes the review's no-protecting-symmetry statement.
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — the observed dark energy is assigned to τ.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.3, ref [22] — the identity's scope, "the 'old' cosmological-constant problem", and the citation, marked [S].
- `papers/broken-born-checkpoint-v2.md` §7.4, §15 — the novelty downgrade; "one identity awaiting a novelty verdict".
- `HANDOFF.md` §8 item 5 — the no-protecting-symmetry statement in the queued comparison.
- `CLAUDE.md` 'Since the handoff' — the dark-energy sector under pressure; the comparison in the current queue.
- `notes/debt1a-iv-beta-coefficients.md` §2 — the derivation; dark energy left to the τ sector.
- `notes/broken-born-theory.md` 'Addendum (v0.6)' — the earlier framing (superseded as reference).
- `notes/broken-born-program-v1.md` §5, §11 — v1's "cosmological-constant cancellation for free" (superseded by #11).
- `popsci/universes-other-half.md` 'The second geometry, and why it has never been seen' — the hundred-and-twenty-orders figure (a popular article, never a status source).
- `popsci/angle-of-the-mirror.md` 'What refused to die' — the cancellation framed through the cosmological constant (a popular article).
