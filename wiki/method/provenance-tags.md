---
title: "Provenance tags and citation marks"
weight: 30
status: method
description: "[D] derived, [T] literature, [P] postulate, [O] open, [V] machine-verified; † recalled from memory and [S] live-searched; how they combine, how a tag changes, the variants in other documents, and how the system grew from v0.1 to v2.3."
sources:
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md 'References'"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "CLAUDE.md 'Method'"
  - "HANDOFF.md §5"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "notes/broken-born-theory.md §0"
  - "notes/broken-born-program-v1.md header"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §11"
  - "papers/conjugate-special-relativity.md header"
  - "papers/conjugate-special-relativity.md §1, §2, §5, §6"
  - "papers/reciprocity-toy-models.md header"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/wiki-build-flags.md items 16, 29, 30"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
---

*Provenance tags are the bracketed labels that the program's papers attach to every claim to say where it comes from: [D] derived in the program, [T] taken from the established literature, [P] postulated, [O] open, or [V] checked by machine. Citations carry a second mark: [S] if the reference was retrieved by a live search during the project, † if it was recalled from the model's memory and still has to be checked against the source. The tags let a reader who cannot check the physics see what kind of support each statement has, and they change only when the support changes. The wiki copies them exactly as the sources attach them and never upgrades one.*

**Status:** Method, in force — the tags define themselves — current form in #11's header and root `CLAUDE.md` ('Method'); checking every † reference is the open [literature battery](/wiki/method/literature-battery).

## Why the program tags its claims

[Checkpoint #11](/wiki/history/documents/checkpoint) gives the reason in its methodological preface: "AI-generated physics has a known failure mode — fluent confabulation — so every claim here carries a tag saying where it came from" (§2). A derivation drafted by an AI reads with the same fluency whether it is correct, borrowed from the literature without credit, or wrong. A tag does not make a claim true; it says what kind of support the claim has, so that a reader knows which statements rest on the program's own reasoning, which on published work, which on assumption, and which on executed code. Paul, who cannot check most of the physics himself, relies on the tags for exactly this ([the collaboration](/wiki/method/collaboration)). The rule in the root `CLAUDE.md` and `HANDOFF.md` §5 is "Tag every claim".

## The tags and the marks

#11's header defines them: "[D] derived in this program, [T] established literature, [P] postulate, [O] open, [V] machine-verified this session. References carry [S] (retrieved by live search during this project) or † (cited from model memory — verify against the source before external use)." The root `CLAUDE.md` gives the same list, with † "from model memory (verify against the source before any external use)" and [S] "live-searched".

| Mark | Meaning | Example in #11 |
| --- | --- | --- |
| [D] | derived in this program | the corrected [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary), "[D — corrected en route]" (§10) |
| [T] | established literature | strongly coupled monopoles in a weakly coupled hidden sector, "by Dirac quantization [T]" (§12) |
| [P] | postulate | the [postulates P1–P5](/wiki/program/postulates) (§4) |
| [O] | open | the twelve items of §14 ([open problems](/wiki/status/open-problems)) |
| [V] | machine-verified | the [soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)'s numbers, "gated in `verify/soliton_obituary.py`" (§12) |
| [S] | reference retrieved by live search | [26S], Freidel–Leigh–Minic's [metastring paper](/wiki/phase-space/reciprocity/broken-born-duality) |
| † | reference cited from model memory | [8†], [the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go) |

The first five are claim tags; [S] and † are marks on citations. In #11's text a citation appears as "[24S]" or "[8†]"; the reference list writes "[24][S]" and "[8]†" (see [References](/wiki/references)).

## Reading combined and qualified tags

Tags combine when a claim has more than one kind of support, and a dash adds a qualifier:

- **Combined.** "[T][V]" on [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) marks a literature result that the program has also checked by machine. "[D][V]" on the toy-model refinement of [P2′](/wiki/program/postulates/p2-prime) (§4) marks a derivation of the program's own with a machine check. "[D + T]" (three times in #11) marks an argument that joins the program's own steps to literature results.
- **Qualified.** "[D — corrected en route]" (§10), "[D — framework; each candidate O]" (§12), "[D — structural; math T]" (§11.3): the qualifier says how far the derivation goes or which part rests on what.
- **[V] and its scope.** #11's "[V] machine-verified this session" was written during the claude.ai phase. In the repository the machine checks are the scripts in `verify/`, run by [the gate](/wiki/method/verification/the-gate). A [V] confirms the arithmetic of the model the script encodes, not that the model is the right physics: #11 §2 added in v2.1 that "a verification script confirms arithmetic, not the model it encodes" ([Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

Tags record where a claim comes from; how far it can be trusted is a separate grading, #11's [claim tiers](/wiki/method/claim-tiers).

## How a tag changes

A tag changes when the support for a claim changes, and the record shows three kinds of change.

- **[D] to [T][V]: a derivation found in the literature.** #11 v2.0 presented the compatibility theorem as derived. Review round 3 identified it as essentially a [Born-geometry](/wiki/phase-space/born-geometry) result of Freidel, Leigh and Minic, and the adjudication concluded: "Unless a comparison shows otherwise, the checkpoint's "[D] derived here" tag on it should become [T] with that citation." (`review/round3-adjudication.md`). v2.1 re-tagged it [T][V]: "The block proof and the machine check are this program's." (#11 §5). Nothing in the mathematics changed. The toy-model worklog drew the lesson for later work, making a prior-art search its first [success criterion](/wiki/symmetry-breaking/toy-models/success-criteria): "Each element of the toy is either new or cited. (Lesson of the compatibility theorem, which turned out to be Freidel–Leigh–Minic's.)" (`notes/toy-lagrangian.md`, 'Success criteria', S0).
- **† to [S]: a memory citation checked.** In #11 v2.0 reference [21], the second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI), was marked †. v2.1 retrieved it and changed the mark: "References [21] upgraded to [S]; [26]-[29] added, all INSPIRE-checked" (repository history, commit e1c1f67). The remaining † references are the [literature battery](/wiki/method/literature-battery).
- **A flag to a mark.** The v1 paper tagged the [quintessence](/wiki/cosmology/dark-energy/quintessence) fits it cited "[T — refresh citations before publication]" (#9 §8); #11 cites the same works as [19][S] and [20][S].

## Variants in other documents

- **The handoff's ✓.** `HANDOFF.md` §2 marks machine checks with ✓: "Alive (derived, machine-verified where marked ✓)". One ✓, on the [clumping shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion) "criterion fails by 10²⁸–10³¹ ✓", had no `verify/` script behind it, and #11 §9 tags the same result [D]; see flag 16 in `review/wiki-build-flags.md`. Since 2026-10-28 section D of `verify/velocity_gated_gravity.py` reproduces the two ratios, and the flag's addendum reads: "The ✓ is now backed by a script; #11 §9's tag [D] is unchanged until Paul rules" ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)). The wiki keeps the tag [D].
- **#13.** [Conjugate special relativity](/wiki/conjugate-relativity) uses [D] [T] [P] [O] with †, "[D — structural]", "[O — flagged, not derived]" and "[conjecture-tier; the full dual dynamics awaits the formalization of §6]", and three that name their basis: "[D — §7 of the checkpoint]" (§1), "[D — checkpoint §7]" (§6) and "[D — compatibility theorem]" (§1). The wiki build flagged all three (`review/wiki-build-flags.md`). #11 §7 never mentions a dual cone and gives the [momentum graviton](/wiki/gravity/momentum-graviton)'s [range in position](/wiki/gravity/spin-2-fields/yukawa-forces#conjugate-special-relativity-a-range-in-momentum), "Yukawa-cut at 1/M_X" (flag 29, confirmed by the flags' audit). The compatibility theorem's metric is positive-definite, with no null cone, while #13 reads its [two causal cones](/wiki/conjugate-relativity/two-causal-cones) off the block form it tags (flag 30); the audit found the tag itself, on H = diag(g, g⁻¹), supported by the theorem, and the cone sentence untagged and covered only by #13's inherited Euclidean/Lorentzian caveat, so it rated flag 30 as a question of tagging convention. The flags await Paul's ruling, and the wiki quotes the tags as written.
- **The toy-model note.** Written as an anonymous manuscript for blind review, it carries no tags, and its † is the Hermitian adjoint (φ†φ), not a citation mark ([the toy models](/wiki/symmetry-breaking/toy-models)).
- **The `verify/` scripts** carry no tags; the checks they print as passed are what a [V] refers to.

## History of the system

- **v0.1, the lab notebook.** #1 §0, "Epistemic scope": "[P] postulate — assumed, with motivation"; "[D] derived — follows from the postulates by calculation shown or sketched here"; "[T] theorem — established in the literature, cited"; "[O] open — not yet derived or decided". It also uses mixed forms such as "[D, schematic]", "[O, sketched]" and "[P/O]", and states its scope: the document is "not a UV-complete quantum gravity". See [The lab notebook (#1) and its addenda](/wiki/history/documents/lab-notebook).
- **v1.0.** The v1 paper (#9 header): "[D] derived here, [T] established literature, [P] postulate, [O] open", with qualified forms such as "[D — rigorous]", "[T — verify figure]" and "[O — direction, deliberately unopened]". Its provenance note asks that "All citations flagged [T — verify] should be checked against sources before any submission." (#9 §11).
- **v2.0 to v2.3.** Checkpoint #11 added [V], the citation marks [S] and †, and the claim tiers. The handoff summarizes v2.0 as having "25 references flagged † (memory — verify) vs [S] (live-searched)" (`HANDOFF.md` §3). v2.1 changed the compatibility theorem's tag and reference [21]'s mark, and added references [26]–[29] marked [S]. See [The checkpoint: #9 to #11 v2.3](/wiki/history/documents/checkpoint).

## In the wiki

Each page copies its sources' tags exactly and never upgrades one; an explanation of established physics written from general knowledge is [T], and any citation it adds is † (`wiki/CLAUDE.md`). Every page's status line states the tags of its central claim, and its frontmatter may list them under `provenance`. Where a tagged statement is among the suspected source errors collected during the wiki build, the page quotes it as written and points to its item in `review/wiki-build-flags.md`.

## Sources

- `papers/broken-born-checkpoint-v2.md` header and 'References' preamble — the current definitions; §2 — the reason and the v2.1 caution; §5 — the re-tagged compatibility theorem; §10, §11.3, §12 — qualified forms
- Root `CLAUDE.md` 'Method' and `HANDOFF.md` §5 — the rule "Tag every claim"
- `review/round3-adjudication.md` 'Rulings' — the re-tagging recommendation
- Repository history, commit e1c1f67 — reference [21] upgraded to [S], [26]–[29] added
- `HANDOFF.md` §2 — the ✓ mark; §3 — #11 v2.0's reference marks
- `review/wiki-build-flags.md` items 16, 29, 30 — the unscripted ✓, with item 16's addendum of 2026-10-28, and two of #13's tags
- `verify/velocity_gated_gravity.py` section D — the script now behind the ✓
- `notes/broken-born-theory.md` §0 — the v0.1 tags and scope statement
- `notes/broken-born-program-v1.md` header, §8 and §11 — the v1 tags, a citation flag, the [T — verify] note
- `papers/conjugate-special-relativity.md` header — #13's tag set; §1, §2, §5, §6 — its qualified forms and the three tags that name their basis
- `papers/reciprocity-toy-models.md` header — an untagged manuscript for blind review
- `notes/toy-lagrangian.md` 'Success criteria' — S0, the prior-art lesson
- `wiki/CLAUDE.md` 'The wiki is derivative' — how the wiki carries tags
