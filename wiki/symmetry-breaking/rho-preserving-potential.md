---
title: "Open: the origin of the ρ-preserving potential"
weight: 70
status: open
description: "A definite polarization needs a potential on the Goldstone angle — a rigid, unordered pair of axes, more structure than ω alone — and no derivation of it exists."
provenance: [O]
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/broken-born-theory.md §3"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
---

*This open problem asks where the potential that fixes the polarization angle comes from. In the toy models the vacuum's polarization is a freely rotating angle, and a definite polarization appears only after a potential is added that keeps Born reciprocity but pins the angle to one of two opposite settings; the program gives its dark-energy field τ a potential of the same kind. Such a potential brings in a fixed pair of axes, which is more fixed structure than the program's postulate P2′ ("only ω is rigid") provides, and it has not been derived from anything deeper. Its first proposed origin, the rigid background of the original postulate P2, disappeared when P2 was replaced.*

**Status:** Open — [O] (#11 §14 item 11, "a derivation of the potential"; the root `CLAUDE.md` lists "a derivation of the ρ-preserving potential" among the toy work's open ends) — the toy's bounded form is checked by `verify/toy_coset.py`, but its origin is not derived. Listed at [Open problems and the queue](/wiki/status/open-problems).

## Key facts

- **The requirement.** #11 §4, P2′ refinement: "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η." It qualifies [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [P2′](/wiki/program/postulates/p2-prime).
- **What the toy uses.** "To get a definite polarization we add a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group." (toy-model note §4). The first form, −μ[Tr(K K_ref)]², "is unbounded below once H is dynamical" ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded, "−μ ≤ V_b ≤ 0 by Cauchy–Schwarz", and "At H = 1, V_b = −(μ/2)(1 + cos 2φ)." ([The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)).
- **Not derived.** The note lists as not shown "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes" (§6). #11 §14 item 11 keeps "a derivation of the potential" open [O] ([Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)).
- **What it costs.** The round-4 referee's reading: the potential fixes the unordered pair of axes by hand, so the spontaneous part of the breaking is only which of the two preset axes is position (`review/round4/referee/audit-notes.md`, Step 3). The worklog's verdict: the toy supports broken reciprocity as "a pseudo-Goldstone polarization angle with a ρ-symmetric potential", not "only ω rigid, nothing else" ('Chunk 3 results').
- **τ's potential.** #11 §10 posits the same structure for dark energy: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology" [D + T], and "A definite polarization requires the ρ-preserving potential this section posits. That potential must be bounded with all fields dynamical" ([τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). Whether V(τ) can go negative, as the turnaround needs, is a separate unresolved question ([Open: the sign of V(τ)](/wiki/cosmology/dark-energy/potential-sign)).
- **History of the origin question.** v0.1 gave the potential's existence to "the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle" [P/O] (#1 §3; [Original P2](/wiki/program/postulates/original-p2)). After P2 → P2′ the Debt-1 note listed as open "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" (Debt-1 Chunk A §F). v2.2 adds that with ω alone the polarization is a Goldstone angle, so the potential is "more structure than ω alone" (#11 §4).
- **In 3+1 (worklog only; uncomputed).** Continuous breaking would be allowed there, but "§10's τ has a potential, so the explicit breaking is in the program anyway" (worklog, 'Chunk 3 results'; [The Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)).

## Sources

- `CLAUDE.md` 'Since the handoff' — "a derivation of the ρ-preserving potential" as an open end of the toy work
- `papers/broken-born-checkpoint-v2.md` §4 — the P2′ refinement: the potential and its cost
- `papers/broken-born-checkpoint-v2.md` §10 — τ's potential; boundedness with all fields dynamical
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — "a derivation of the potential" still open [O]
- `papers/reciprocity-toy-models.md` §4, §6 — the naive and bounded forms; "Not shown"
- `review/round4/referee/audit-notes.md` Step 3 — the axis pair is fixed by hand
- `notes/debt1a-geometric-core.md` §F — the origin of τ's potential under P2′ listed as open
- `notes/broken-born-theory.md` §3 — v0.1's attribution to the rigid ω (superseded)
- `notes/toy-lagrangian.md` 'Chunk 3 results' — the pseudo-Goldstone reading; the 3+1 remark
