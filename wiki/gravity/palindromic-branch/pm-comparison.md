---
title: "Open: the partially-massless comparison (OP2)"
weight: 30
status: open
description: "The palindromic branch contains the partially-massless point, and Hossenfelder's exchange-symmetric cancellation is a different mechanism; a convention-careful comparison is still to be made (queue item 1), and the novelty claim stays downgraded."
provenance: [O]
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §14 item 2"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md refs [22], [24], [25]"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §8"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §10"
  - "notes/broken-born-program-v1.md §11"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
  - "popsci/universes-other-half.md 'The second geometry, and why it has never been seen'"
  - "review/wiki-build-flags.md item 9"
---

*The partially-massless comparison is a pending literature check on the two results of this section, [the palindrome](/wiki/gravity/palindromic-branch/palindrome) and [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity). A live literature search found that the palindromic branch contains the [partially massless point](/wiki/gravity/spin-2-fields/partially-massless-gravity) of [bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), a parameter point with an extra gauge symmetry, and that Hossenfelder's exchange-symmetric bimetric theory already cancels vacuum energy by a different mechanism. The comparison asks whether the identity is new, whether it holds up against that literature once conventions are aligned, and whether [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) is the origin of the partially massless symmetry. Until it is done, the identity is presented as adjacent to known results rather than as new. It is open problem 2 of [the checkpoint](/wiki/history/documents/checkpoint) and part of the first item of [the current work queue](/wiki/status/open-problems), and no calculation for it exists yet.*

**Status:** Open — [O] — [#11](/wiki/history/documents/checkpoint) §14 item 2; listed with the program's [open problems](/wiki/status/open-problems) and in item 1 of the current queue ([the project instructions](/wiki/history/documents/project-instructions), "Since the handoff"). No calculation, note or verification script for it is in the repository yet.

## The open problem

#11 §14 item 2, with PM standing for partially massless:

> **PM-adjacency:** detailed comparison of the palindromic branch with partially-massless bimetric [24S]; is reciprocity the origin of the PM symmetry? Convention-careful check of the vacuum-energy identity against [24S, 25S] — the queued novelty audit [O].

The [handoff](/wiki/history/documents/handoff) lists it among its open items as "PM-point comparison and the Λ=0 novelty audit" (HANDOFF §2, open item 4) and states it in full as queue item 5:

> **PM-point comparison** (is reciprocity the origin of the partially-massless symmetry? does the Λ=0 identity survive convention-careful comparison with arXiv:1609.09515 / 0807.2838 / the Schmidt-May–von Strauss review's no-protecting-symmetry statement?). (HANDOFF §8)

The item bundles three questions:

1. **Is the identity new?** This is the novelty audit: whether the vacuum-energy identity, the "Λ = 0 property of interchange-symmetric bimetric" in the words of [calc note #8](/wiki/history/documents/debt-1-notes) (§2), is already in the literature.
2. **Does it survive?** In the handoff's wording, whether the identity will "survive convention-careful comparison" with [24S], [25S] and the review [22S].
3. **Is reciprocity the origin of the partially massless symmetry?** Whether the reciprocity that forces the branch also accounts for the extra gauge symmetry of the partially massless point inside it [O].

## What it qualifies

The comparison bears on [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) [D] and [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) [D][V], both alive. The identity's integer arithmetic is machine-checked (battery test T5; [the verification battery](/wiki/method/verification/battery)). What remains to be settled is whether the identity is new and whether it survives comparison with the cited works. For the palindrome, part of the literature question is already settled: the branch itself is known (#11 §7.4), and what stays open is whether reciprocity explains the partially massless symmetry.

## What prompted it

#11 v2.0 added the downgrade; the handoff's inventory lists a "PM/Hossenfelder novelty downgrade" among that version's additions (HANDOFF §3, row 11). #11 §7.4, its literature position, records the outcome of a live literature search. It opens: "Exchange-symmetric bimetric potentials are *not* unexplored territory." The search found the two precedents (a) and (b) below, and #11 drew the consequence: "the novelty claim is hereby **downgraded from 'likely standalone result' to 'requires detailed comparison with the PM and exchange-symmetric literature,'** queued as an open item." In §2, #11 says the selection-versus-derivation bias "is acknowledged explicitly where it operates (§7.4)" ([claim tiers and selection bias](/wiki/method/claim-tiers)).

The handoff records the same finding: "the partially-massless (PM) bimetric point (arXiv:1609.09515) is g↔f symmetric and sits inside the palindromic branch; Hossenfelder arXiv:0807.2838 has a different exchange-symmetric cancellation. Detailed comparison still owed." (HANDOFF §2). The two popular articles ([#10 and #12](/wiki/history/documents/popular-articles)) report the question in the same terms: "whether the cancellation is new or a rediscovery awaits a careful comparison" (#10, 'What refused to die'), and "Whether that cancellation is new or a rediscovery of structure already implicit in the literature on related theories is an unresolved question" (#12, 'The second geometry, and why it has never been seen').

## The literature to compare against

### (a) Partially massless bimetric gravity [24S]

Partially massless gravity is a massive spin-2 field on [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space) at the one special mass at which an extra gauge symmetry appears and removes its helicity-0 polarization [T]; bimetric gravity has a parameter point with that property ([partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity)). #11 §7.4 (a):

> The interchange-symmetric parameter choice appears in the partially-massless (PM) bimetric literature: the PM point β₀ = 3α⁻²β₂, β₁ = β₃ = 0, β₄ = 3α²β₂ makes the potential g↔f symmetric, with proportional de Sitter solutions of undetermined ratio [24S]. At α = 1 the PM point lies **inside** our palindromic branch — so partially massless gravity, with its celebrated extra gauge symmetry, is a special point of the reciprocity-symmetric family, raising the open question of whether reciprocity is the origin of the PM symmetry [O].

The point lies in the branch because β₁ = β₃ = 0 already satisfies β₁ = β₃, and at α = 1 the expressions for β₀ and β₄ coincide, so the coefficient list reads the same in both directions.

It is not the program's point. #11 §7.4 continues: "Note the PM point sits at Λ ≠ 0 with c undetermined; our flat-aligned-vacuum identity selects a *different* point of the same branch (β₁ ≠ 0 generically, β₀ = −4β₁ − 3β₂)." The two points share the branch but not the vacuum: the partially massless point has a nonzero [cosmological constant Λ](/wiki/cosmology/dark-energy/cosmological-constant), and the identity's point is the flat aligned vacuum.

Reference [24][S] in #11: "Partially massless bimetric gravity and its exchange-symmetric parameter point, arXiv:1609.09515". #11 gives no authors, and the handoff cites the same arXiv number without a title (HANDOFF §2, §8). Flag 9 in `review/wiki-build-flags.md` adds that the title may be a description rather than the paper's own title, and that, being marked [S], the entry falls outside the [† literature battery](/wiki/method/literature-battery) (open problem 10), which checks the citations made from model memory. The record therefore identifies the partially massless paper this comparison is against only by its arXiv number and a possibly descriptive title.

### (b) Hossenfelder's exchange-symmetric bimetric theory [25S]

#11 §7.4 (b): "The theme 'exchange symmetry cancels vacuum energy in a two-metric theory' has a precedent in a different mechanism: Hossenfelder's exchange-symmetric bimetric, where twin-sector source terms cancel identically [25S]. Our identity is sector-internal (no twin matter required) and, to our current knowledge, distinct".

The contrast as #11 draws it: in Hossenfelder's theory the cancellation comes from the source terms of a twin matter sector, while the program's identity comes from the coefficients of the spin-2 potential itself and needs no second matter sector. The phrase "to our current knowledge" marks the distinction as provisional until the comparison is made.

Reference [25][S]: S. Hossenfelder, "A bi-metric theory with exchange symmetry," Phys. Rev. D 78, 044015 (2008), arXiv:0807.2838.

### (c) The Schmidt-May–von Strauss review [22S]

The handoff adds a third comparison: "the Schmidt-May–von Strauss review's no-protecting-symmetry statement" (HANDOFF §8 item 5). No document quotes that statement. #11 cites the same review for the identity's scope: on matter-loop vacuum energy, "bimetric theory is otherwise no better placed than GR [22S]" (#11 §7.3), GR being [general relativity](/wiki/gravity/spin-2-fields/general-relativity) ([the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)). Reference [22][S]: A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), arXiv:1512.00021.

## What a convention-careful comparison involves

The sources ask for a "convention-careful" check (#11 §14 item 2) without listing the conventions. Normalizations that the record leaves undefined include:

- #11 writes the partially massless point with α and c and defines neither; [partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity) gives their usual meanings in the bimetric literature [T].
- #8 writes the program's potential with the prefactor 2m²M² and its exchange identity with the symbol Sₙ, and defines none of m, M and Sₙ (#8 §1; [the palindrome](/wiki/gravity/palindromic-branch/palindrome)).
- Reciprocity forces "equal effective Planck masses (forced by the same symmetry)" (#8 §3; [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity); [equal Planck masses](/wiki/gravity/spin-2-fields/planck-units#equal-planck-masses-in-the-bimetric-sector)); no document relates that normalization to the α of [24S].

The [S] marks mean that all three works were retrieved by live search during the project. They therefore lie outside the [† literature battery](/wiki/method/literature-battery), open problem 10, which source-checks the references cited from model memory; that battery is the second task of the same queue item.

## Why it matters

- **The word "theory".** #11 §15's plain-language opening ends: "the word 'theory' still waits on items 1–3 above". The three are the derivation of the wedge sector from the geometric action ([OP1](/wiki/gravity/tuning-test/wedge-reduction)), this comparison, and the [Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing); see [the assessment](/wiki/program/assessment).
- **A standing caution.** #11 §15 lists "an unsolicited identity (§7.3)" among the program's progressive signs and "the novelty demotion of §7.4 as a standing caution" among its degeneration risks ([Lakatosian methodology](/wiki/method/lakatosian-methodology)). Its plain-language opening describes the demotion as one "from 'likely new' to 'adjacent to known territory, comparison required'".

## Place in the queue

- The handoff ranked the comparison fifth in its next-actions queue (HANDOFF §8 item 5), after cutting and re-auditing the soliton manuscript, whose candidate has since died ([obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)), the [√N-floor freeze-out estimate](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) and the [toy Lagrangian](/wiki/symmetry-breaking/toy-models).
- Since the handoff, items 1, 2 and 4 of that queue have been done and item 3 dropped. Root `CLAUDE.md`, "Since the handoff": "HANDOFF §8 queue item 3 is dropped. The current queue, in order: 1. HANDOFF §8 items 5–7: the partially-massless comparison, the † literature battery, the phase-space-diameter note. 2. Optional: a round-5 review of the toy note, but only before any external use."
- The comparison is therefore the first-named task of the first queue item, beside [the † literature battery](/wiki/method/literature-battery) and [the phase-space-diameter note](/wiki/cosmology/scale-factor-duality/phase-space-diameter) ([open problems and the queue](/wiki/status/open-problems)). No calculation, note or script for it exists in the repository.

## Superseded: the standalone-result claim

Before the literature search, the program expected the identity to be new:

- Calc note #8 §2: "(Whether the Λ = 0 property of interchange-symmetric bimetric was previously noticed in the literature: flagged to verify; if not, it is a standalone publishable observation.)" Its §5 lists "(v) literature check on the Λ = 0 palindrome observation" in the open residue of [Debt 1](/wiki/history/debts).
- [The lab notebook](/wiki/history/documents/lab-notebook)'s v0.6 addendum ends its residual open items with "literature check on the Λ = 0 observation".
- [#9](/wiki/history/documents/checkpoint), the v1.0 consolidation, §5 item 5: "(Literature check on whether this Λ = 0 property of symmetric bimetric was previously noticed: flagged [O]; if not, it is a standalone result.)" The section's plain-language opening called the result "A cosmological-constant cancellation for free, from symmetry"; §10 item 8 listed "symmetric-bimetric Λ = 0" among the literature verifications still to be done; and the assessment counted "at least two results that stand on their own regardless of its fate", the palindrome theorem being one of them (#9 §11).

#11 replaced the expectation with the downgrade of §7.4 quoted above. Its §15 now counts "one observation that stands regardless of its fate", which is [the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner), and "one identity awaiting a novelty verdict". The handoff records the same change: "Novelty downgraded after literature check" (HANDOFF §2; the original sets "downgraded" in capitals). The identity's derivation and its machine check were not affected. What was downgraded is the claim that it is a standalone new result; whether it is new waits on this comparison.

## Sources

- `CLAUDE.md` 'Since the handoff' — the current queue, with this comparison in item 1.
- `papers/broken-born-checkpoint-v2.md` §7.4, §14 item 2 — the literature position, the selected point, the downgrade and the open item.
- `papers/broken-born-checkpoint-v2.md` §7.3, §2, §15, refs [22], [24], [25] — the review cited for the scope; the selection-versus-derivation bias; the self-assessment and the gate on "theory"; the three references, marked [S].
- `HANDOFF.md` §2, §3, §8 — the downgrade after the literature check and open item 4; the v2.0 inventory row; the three comparisons in queue item 5 and the queue's order.
- `notes/debt1a-iv-beta-coefficients.md` §2, §3, §5 — the original "standalone" flag; the equal Planck masses; the open residue of Debt 1.
- `notes/broken-born-theory.md` 'Addendum (v0.6)' — the residual literature check as first recorded.
- `notes/broken-born-program-v1.md` §5, §10, §11 — v1's "standalone result", its open literature check and its "two results that stand on their own" (superseded by #11).
- `popsci/angle-of-the-mirror.md` 'What refused to die'; `popsci/universes-other-half.md` 'The second geometry, and why it has never been seen' — the popular accounts of the open question (never a status source).
- `review/wiki-build-flags.md` item 9 — reference [24][S]: no authors, a title that may be descriptive, and outside the † battery; awaiting Paul's ruling.
