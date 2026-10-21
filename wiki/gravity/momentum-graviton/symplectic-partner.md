---
title: "The symplectic partner of the graviton is another graviton"
weight: 30
status: alive
description: "Doubling geometry with η pairs the metric with a harmless 2-form; doubling with ω pairs it with a second graviton — the program's account of why string theory's doubling works and Born's stalled."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §11"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/broken-born-theory.md §1"
---

*This observation compares two ways of extending spacetime geometry to a doubled geometry by pairing the metric with a partner field. In [double field theory](/wiki/phase-space/born-geometry/double-field-theory), the doubled geometry of string theory, the pairing uses the neutral metric η and the partner is the antisymmetric B-field, a 2-form whose gauge theory is harmless as far as spin goes. In the symplectic doubling this program uses, built on ω, the partner is the momentum graviton X, which is symmetric and has its own [linearized diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms), so it is a second graviton; two interacting massless gravitons are inconsistent. [Checkpoint #11](/wiki/history/documents/checkpoint) offers this as the structural reason string theory's doubling works while Born's stalled, and its assessment lists it as the one observation that stands regardless of the program's fate. It is derived and rests on literature [D + T]; it is a structural argument, not a computation a script could check.*

**Status:** Alive — [D + T] in #11 §7.1 and calc note #6 (`notes/debt1a-ii-X-classification.md` §2) — structural, not machine-checked; #11 §15 lists it as the program's one observation that "stands regardless of its fate".

## Key facts

- #11 §7.1, step (ii), in which DFT stands for double field theory: "Locally, dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎ — a second linearized-diff gauge field, because X is symmetric (contrast DFT's antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin)."
- Calc note #6 §2 [D + T], in which DFT is again double field theory: "Contrast DFT: there the doubled partner is the antisymmetric B-field, δB = dλ, a 2-form gauge theory — spin-wise harmless. The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field. This is the structural reason string theory's η-doubling exists and naive ω-doubling is hard: the symplectic partner of the graviton is another graviton."
- The phrase "η antisymmetric-pairing" is quoted unchanged and not paraphrased: η itself is a "neutral (split-signature) metric" (lab notebook #1 §1, postulate P1), so the phrase is ambiguous as written. The structures ω and η are described on [The structures ω, η, H and the split-quaternion algebra](/wiki/phase-space/born-geometry/born-structures).
- #11 §15: "The program has produced one observation that stands regardless of its fate (the symplectic partner of the graviton is another graviton — why string theory's doubling works and Born's stalled), one identity awaiting a novelty verdict" ([Assessment: a live research program](/wiki/program/assessment)). The identity is [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity).
- The superseded v1 paper (#9 §11) had counted "at least two results that stand on their own", this observation and the vacuum-energy cancellation; #11 §15 keeps only the observation as standing and leaves the identity awaiting a novelty verdict.
- A related corollary of the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem): with ω and η both rigid there is "No Kalb–Ramond analog. The off-diagonal block — DFT's B-field — is frozen out by the extra symplectic compatibility" (calc note #5, `notes/debt1a-geometric-core.md` §A; [Corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)).
- What it leads to: because X must couple, the [multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) applies, and [X must be massive](/wiki/gravity/momentum-graviton/forcing-chain).

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1 — the current statement; §15 for its standing in the assessment
- `notes/debt1a-ii-X-classification.md` §2 — the original statement [D + T]
- `notes/broken-born-program-v1.md` §5, §11 — the superseded v1 statement and its "two results" count
- `notes/debt1a-geometric-core.md` §A — the no-Kalb–Ramond corollary
- `notes/broken-born-theory.md` §1 — postulate P1, η as a neutral metric
