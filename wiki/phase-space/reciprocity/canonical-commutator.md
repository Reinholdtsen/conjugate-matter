---
title: "The canonical commutator and the uncertainty principle"
weight: 10
status: established
description: "[x, p] = iℏ: why position and momentum cannot both be sharp, and why the commutator is blind to the quarter-turn ρ."
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "notes/broken-born-program-v1.md §1"
  - "papers/reciprocity-toy-models.md §1"
  - "notes/knot-dark-matter-standalone.md §1"
  - "popsci/universes-other-half.md 'An asymmetry that cannot be avoided'"
---

*The canonical commutator [x, p] = iℏ is the rule of quantum mechanics that position and momentum do not commute, so that no state has sharp values of both; this is the uncertainty principle, and Planck's constant ℏ sets its scale. The rule is unchanged when position and momentum are exchanged by the quarter-turn [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), so on its own it treats the two variables alike. The program leans on it twice. It argues that because nothing can be sharp in both variables, any world with local physics has to favor one of them, and it reads the fixed value of ℏ as the one rigid structure of phase space.*

**Status:** Established — textbook quantum mechanics [T], which #11 §3 cites through Born [1†, 2†] — not machine-checked and not in question; the program's use of it as the premise of [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking) is a program claim with its own status.

## Key facts

- **The relation.** [x, p] = iℏ [T]. It is the quantum form of the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, the antisymmetric pairing of positions with momenta.
- **Blind to ρ.** #9 §1: "the Fourier transform implements it unitarily and the canonical commutator is blind to it". The reason is general [T]: linear maps that preserve ω preserve the commutator, and ρ = [[0, 1], [−1, 0]] "is symplectic and squares to −1" (toy-model note §1). The [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) is the operator that carries ρ out on wavefunctions.
- **Premise of mandatory breaking.** #11 §3: "[x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization." The selected object is a [Lagrangian polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations). Version 2.2 of #11 qualifies the argument: the polarization is a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) that needs a potential, and the breaking is physical only once matter couples to the sign of K (the [twisted element](/wiki/symmetry-breaking/twisted-element)).
- **ℏ as the rigid structure.** P2′ (#11 §4): "Only ω is rigid (symplectic rigidity ≡ constancy of ℏ)." [P] — see [P2′](/wiki/program/postulates/p2-prime). Two derived consequences: "ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run)" [D] (#11 §10; [the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint)), and det H = 1, read as "ℏ-rigidity is *geometric*" (#11 §5; [the corollaries of the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-corollaries)).
- **A change of description, ordinarily.** Because the commutator is unchanged, ρ maps one representation of it to another; #14 §1 calls this "a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action" — see [unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence).

## Used by

- [Mandatory breaking: the uncertainty argument](/wiki/symmetry-breaking/mandatory-breaking) — no state is local in both variables, so a polarization must be chosen.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — reads the rigid ω as the constancy of ℏ.
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — a fixed comoving phase-space cell, because ℏ does not run.
- [Corollaries: unimodularity, no B-field, slaved momentum metric](/wiki/phase-space/born-geometry/compatibility-corollaries) — det H = 1 as ℏ-rigidity built into the geometry.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the commutator as the premise of mandatory breaking; ρ implemented by the Fourier transform [1†, 2†].
- `papers/broken-born-checkpoint-v2.md` §4 — P2′, symplectic rigidity as the constancy of ℏ, and the v2.2 refinement.
- `papers/broken-born-checkpoint-v2.md` §10 — a·ã = 1 from ω-rigidity.
- `papers/reciprocity-toy-models.md` §1 — ρ is symplectic and squares to −1.
- `notes/broken-born-program-v1.md` §1 — "the canonical commutator is blind to it".
- `notes/knot-dark-matter-standalone.md` §1 — ρ as a unitary equivalence of representations (withdrawn paper; the framing sentence is still the program's).
- `popsci/universes-other-half.md` "An asymmetry that cannot be avoided" — plain-language framing only (popular article; never a status source).
