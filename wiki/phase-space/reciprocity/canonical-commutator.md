---
title: "The canonical commutator and the uncertainty principle"
weight: 10
status: established
description: "[x, p] = iℏ: why position and momentum cannot both be sharp, and why the commutator is blind to the quarter-turn ρ."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "notes/broken-born-program-v1.md §1"
  - "papers/reciprocity-toy-models.md §1"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/knot-dark-matter-standalone.md §1"
  - "verify/battery.py T2"
  - "popsci/universes-other-half.md 'An asymmetry that cannot be avoided'"
---

*The canonical commutator [x, p] = iℏ is the rule of quantum mechanics that position and momentum do not commute: measuring one and then the other is not the same as the reverse. Its best-known consequence is the uncertainty principle: no state has sharp values of both, and the product of the two spreads cannot fall below a bound set by Planck's constant ℏ. The rule is unchanged when position and momentum are exchanged by the quarter-turn [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), so on its own it treats the two variables alike. The program leans on it twice. It argues that because nothing can be sharp in both variables, any world with local physics has to favor one of them; and it reads the fixed value of ℏ as the one rigid structure of phase space.*

**Status:** Established — textbook quantum mechanics [T]; [#11](/wiki/history/documents/checkpoint) §3 states the commutator untagged, as the premise of its mandatory-breaking argument — not machine-checked, and not in question. The program's two uses of it carry their own status: [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking) is an alive claim, and the rigidity of ℏ is part of the postulate [P2′](/wiki/program/postulates/p2-prime) [P].

## What the commutator says

In quantum mechanics a particle's position and momentum are operators, x̂ and p̂, acting on its state [T]. In the position representation, where the state is a wavefunction ψ(x), position multiplies and momentum differentiates:

```text
x̂ ψ(x) = x ψ(x)          p̂ ψ(x) = −iℏ dψ/dx
[x̂, p̂] ψ = (x̂p̂ − p̂x̂) ψ = iℏ ψ
```

The commutator [x̂, p̂] = x̂p̂ − p̂x̂ measures how much the order of the two operations matters, and the answer is the same constant for every state. Planck's constant ℏ is its only scale [T]. With d degrees of freedom, d positions xᵃ and their momenta p_a, the relations are

```text
[xᵃ, p_b] = iℏ δᵃ_b        [xᵃ, xᵇ] = 0        [p_a, p_b] = 0
```

so each position fails to commute only with its own momentum [T]. The program's [lab notebook](/wiki/history/documents/lab-notebook) works on flat phase space ℝ^{2d} "with coordinates (x^a, p_a), d=4" (#1 §2).

The relation was first written down in 1925, by Born and Jordan and independently by Dirac [T]; it is the same Max Born who later proposed reciprocity.

### The classical counterpart

Classical mechanics has the same pairing in the Poisson bracket, {x, p} = 1: positions pair with their own momenta, antisymmetrically, and with nothing else [T]. Geometrically this pairing is the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω of phase space. Dirac's rule of quantization replaces a Poisson bracket {A, B} by the commutator [Â, B̂]/(iℏ) [T], so [x, p] = iℏ is the quantum form of ω. This is the motivation for the program's postulate that treats ω and ℏ as one structure (below).

## The uncertainty principle

For any state, the spreads (standard deviations) Δx and Δp of position and momentum satisfy

```text
Δx · Δp ≥ ℏ/2
```

[T]. The bound follows from the commutator alone. For any two observables A and B, ΔA · ΔB ≥ |⟨[A, B]⟩|/2 (Robertson's inequality) [T], and for x and p the commutator is the constant iℏ. A Gaussian wavepacket reaches the bound when its width parameter is real, that is, a Gaussian envelope times a plane wave [T].

The same fact has a Fourier reading. The momentum wavefunction ψ̃(p) is the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of ψ(x), and a function and its Fourier transform cannot both be narrow [T]: a state concentrated near one position contains a broad spread of momenta, and the reverse. This is the trade-off between a signal's duration and its bandwidth, applied to the wavefunction. "Sharp in x" and "sharp in p" are the two ends of one trade-off, and no state sits at both.

## What the commutator does not distinguish

Exchange position and momentum with one sign change, ρ: (x, p) → (p, −x). The new pair has the same commutator [T]:

```text
x′ = p,  p′ = −x:      [x′, p′] = [p, −x] = [x, p] = iℏ
```

The sign matters. The plain swap (x, p) → (p, x) would give [p, x] = −iℏ; the sign makes ρ preserve the symplectic form, which is the classical content of the same statement. The [toy-model note](/wiki/symmetry-breaking/toy-models) writes this as "ρ = [[0, 1], [−1, 0]] is symplectic and squares to −1" (§1), and [the v1 paper](/wiki/history/documents/checkpoint) as "the canonical commutator is blind to it" (#9 §1). More generally, every linear map of (x, p) that preserves ω preserves the commutator [T]; ρ is the quarter-turn among them ([the symplectic form and Sp(2d, ℝ)](/wiki/phase-space/reciprocity/symplectic-form)).

Because the relation is unchanged, ρ carries one representation of the commutation relations into another, and the Fourier transform is the unitary operator that relates the two [T]. As ordinarily encountered, then, ρ is a change of description. The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) states the point the program has to answer: "as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action" (#14 §1). The distinction, and the referees' demand for an action in which ρ is a genuine symmetry, are on [unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence).

## First use: some polarization must be chosen

#11 §3 makes the uncertainty principle the premise of its claim that the breaking in its [hard core](/wiki/program/hard-core) is unavoidable: "The breaking is *mandatory*: [x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization. The magnet must point." The sentence carries no tag in #11. "Joint locality" is locality in both variables at once; the v1 paper's wording is "nothing can be local in both variables at once, so any universe with local physics must pick a polarization" (#9 §1). A world whose physics is local must therefore be local in one variable at the cost of the other. The choice of variable is a [Lagrangian polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations), a choice of which phase-space directions count as position. The [popular article](/wiki/history/documents/popular-articles) #12 gives the plain-language version: "a universe containing definite structures — atoms, crystals, instruments — must be definite in one variable at the expense of the other" ("An asymmetry that cannot be avoided"; a popular article, never a status source).

The argument's reach is limited in two ways, both recorded in #11:

- **It does not pick the variable.** The commutator rules out joint sharpness; it does not say which variable is sharp. The postulate P5 leaves that to the vacuum: "The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful." [P] (#11 §4; [P5](/wiki/program/postulates/p5-spontaneous-selection)).
- **Version 2.2 qualifies it.** From the toy models, #11 §4 adds to P2′ that with only ω rigid, "ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (checked by [the toy-model scripts](/wiki/method/verification/toy-model-scripts)); that a definite polarization "needs a ρ-preserving potential on that angle"; and that "the breaking of ρ is physical only once matter couples to the sign of K (P4)". See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [the twisted element](/wiki/symmetry-breaking/twisted-element).

The argument and its current status are on [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking).

## Second use: ℏ as the one rigid structure

The program's corrected postulate reads: "**P2′** Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral metric η is emergent" [P] (#11 §4; [P2′](/wiki/program/postulates/p2-prime)). The relations above motivate the identification, which remains a postulate. The commutator is the quantum form of ω, and ℏ is its only scale, so a symplectic form fixed once and for all amounts to a Planck constant that does not vary.

The lab notebook glossed it this way under the original P2: "the symplectic structure *is* the constancy of ℏ — phase-space cells do not stretch" (#1 §1). The [original P2](/wiki/program/postulates/original-p2) also froze the [neutral metric η](/wiki/phase-space/born-geometry/born-structures) and was superseded; [the calc note](/wiki/history/documents/debt-1-notes) that forced the change kept the ω half: "Freeze ω only — that is genuinely ℏ" (#5 §B).

Two results of the program carry the same reading:

- **The cosmological constraint.** "ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run)" [D] (#11 §10; [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint)).
- **Unimodularity.** On the slice where the metric is compatible with both structures, det H = 1 holds identically. #11 §5 reads this as "ℏ-rigidity is *geometric*", and the calc note as "phase-space volume is not a dynamical field. ℏ-rigidity is manifest in the geometry, not imposed on it" (#5 §A). #11 adds, calling it machine-verified, that unimodularity "persists across the whole modular family of §6" (the metrics of [the modular field Z](/wiki/phase-space/modular-field/modular-field-z)). Battery test T2 checks "det H_Z = 1" at one randomly sampled member of that family (d = 4), so the statement for the whole family is derived [D], not machine-verified ([the verification battery](/wiki/method/verification/battery)). See [the corollaries of the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-corollaries).

## Standard references

These are added by the wiki from model memory (†); the program's documents cite none of them.

- M. Born and P. Jordan (1925)†, and P. A. M. Dirac (1925)†: the commutation relation and the bracket-to-commutator rule.
- W. Heisenberg (1927)†: the uncertainty principle; E. H. Kennard (1927)†: the inequality Δx · Δp ≥ ℏ/2.
- H. P. Robertson (1929)†: the inequality for any pair of observables.

## Used by

- [Mandatory breaking: the uncertainty argument](/wiki/symmetry-breaking/mandatory-breaking) — no state is local in both variables, so a polarization must be chosen.
- [The hard core](/wiki/program/hard-core) — the commutator is the premise of the claim that the breaking is mandatory.
- [P1: the phase-space arena](/wiki/program/postulates/p1-arena) — a quantum state cannot sit at a point of phase space.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — reads the rigid ω as the constancy of ℏ.
- [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity) — ρ leaves the commutator unchanged, so it is ordinarily a change of description.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — nothing is sharp in both variables, so the vacuum selects one.
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — a fixed comoving phase-space cell, because ℏ does not run.
- [Corollaries: unimodularity, no B-field, slaved momentum metric](/wiki/phase-space/born-geometry/compatibility-corollaries) — det H = 1 as ℏ-rigidity built into the geometry.
- [The phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter) — the phase-space area of order h that one quantum state occupies, applied at cosmic scale.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the commutator as the premise of mandatory breaking (untagged); ρ implemented by the Fourier transform [1†, 2†].
- `papers/broken-born-checkpoint-v2.md` §4 — P2′ ("symplectic rigidity ≡ constancy of ℏ"), P5, and the v2.2 refinement.
- `papers/broken-born-checkpoint-v2.md` §5 — det H = 1 as geometric ℏ-rigidity, across the modular family.
- `papers/broken-born-checkpoint-v2.md` §10 — a·ã = 1 from ω-rigidity.
- `papers/reciprocity-toy-models.md` §1 — ρ is symplectic and squares to −1.
- `notes/debt1a-geometric-core.md` §A, §B — unimodularity read as ℏ-rigidity; "Freeze ω only".
- `notes/broken-born-program-v1.md` §1 — "the canonical commutator is blind to it"; "nothing can be local in both variables at once" (v1, superseded as reference by #11).
- `notes/broken-born-theory.md` §1, §2 — the original P2's gloss on ℏ; coordinates (xᵃ, p_a) with d = 4.
- `notes/knot-dark-matter-standalone.md` §1 — ρ as a unitary equivalence of representations (withdrawn paper; the framing sentence is still the program's).
- `verify/battery.py` T2 — det H_Z = 1 at one sampled member of the modular family.
- `popsci/universes-other-half.md` "An asymmetry that cannot be avoided" — plain-language framing only (popular article; never a status source).
