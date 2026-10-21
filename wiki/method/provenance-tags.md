---
title: "Provenance tags and citation marks"
weight: 30
status: method
description: "[D] derived, [T] literature, [P] postulate, [O] open, [V] machine-verified; † recalled from memory and [S] live-searched; and how the tag system grew from v0.1 to v2.2."
sources:
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md 'References'"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "CLAUDE.md 'Method'"
  - "HANDOFF.md §5"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §0"
  - "notes/broken-born-program-v1.md header"
  - "notes/broken-born-program-v1.md §11"
  - "papers/conjugate-special-relativity.md header"
  - "papers/reciprocity-toy-models.md header"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
---

*Provenance tags are the bracketed labels that the program's papers attach to every claim to say where it comes from: [D] derived in the program, [T] taken from the established literature, [P] postulated, [O] open, or [V] checked by machine. Citations carry a second mark: [S] if the reference was retrieved by a live search during the project, † if it was recalled from the model's memory and still has to be checked against the source. The tags let a reader who cannot check the physics see what kind of support each statement has. The wiki copies them exactly as the sources attach them and never upgrades one.*

**Status:** Method, in force — the tags define themselves — current form in #11's header and root `CLAUDE.md` ('Method'); checking every † reference is the open [literature battery](/wiki/method/literature-battery).

## Key facts

- **The current definitions.** #11's header: "[D] derived in this program, [T] established literature, [P] postulate, [O] open, [V] machine-verified this session. References carry [S] (retrieved by live search during this project) or † (cited from model memory — verify against the source before external use)." Root `CLAUDE.md` gives the same list, with † "from model memory (verify against the source before any external use)" and [S] "live-searched".
- **Reading them.** In #11's text a citation appears as "[24S]" or "[8†]"; the reference list writes "[24][S]" and "[8]†" (see [References](/wiki/references)). Tags combine and qualify: "[T][V]" on [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) marks a literature result that the program has also checked by machine, and #11 uses forms such as "[D + T]" and "[D — corrected en route]". #11's "[V] machine-verified this session" was written during the claude.ai phase; in the repository the machine checks are the scripts in `verify/`, run by [the gate](/wiki/method/verification/the-gate).
- **A tag changed by review.** The compatibility theorem was presented as derived in v2.0. After review round 3 identified it as a result of Freidel, Leigh and Minic, v2.1 re-tagged it [T][V]: "The block proof and the machine check are this program's." (#11 §5). The tags record where a claim comes from, so a claim found in the literature moves from [D] to [T] even when nothing in the mathematics changes.
- **Tiers.** #11 groups the tags into [claim tiers](/wiki/method/claim-tiers): Tier 1 is machine-checked algebra ([V]), Tier 2 the literature, Tier 3 the program's own structural physics.
- **Variants in other documents.** `HANDOFF.md` §2 marks machine checks with ✓: "Alive (derived, machine-verified where marked ✓)". #13 uses [D] [T] [P] [O] with † and qualified forms such as "[D — structural]", "[O — flagged, not derived]" and "[conjecture-tier; …]". The toy-model note, written as an anonymous manuscript for blind review, carries no tags, and its † is the Hermitian adjoint (φ†φ), not a citation mark. The `verify/` scripts carry no tags.
- **History, v0.1.** The lab notebook's "Epistemic scope" (#1 §0): "[P] postulate — assumed, with motivation"; "[D] derived — follows from the postulates by calculation shown or sketched here"; "[T] theorem — established in the literature, cited"; "[O] open — a debt the program owes". It also uses mixed forms such as "[D, schematic]", "[O, sketched]" and "[P/O]", and states its scope: the document "is not a UV-complete quantum gravity"; "Rigor changed an answer; that is the point of rigor." See [The lab notebook (#1) and its addenda](/wiki/history/documents/lab-notebook).
- **History, v1.0 to v2.2.** The v1 paper (#9 header): "[D] derived here, [T] established literature, [P] postulate, [O] open", with qualified forms such as "[D — rigorous]", "[T — verify figure]" and "[O — direction, deliberately unopened]"; its provenance note asks that "All citations flagged [T — verify] should be checked against sources before any submission." Checkpoint #11 added [V], the citation marks [S] and †, and the claim tiers. See [The checkpoint: #9 to #11 v2.2](/wiki/history/documents/checkpoint).
- **In the wiki.** Each page copies its sources' tags exactly and never upgrades one; an explanation of established physics written from general knowledge is [T], and any citation it adds is † (`wiki/CLAUDE.md`).

## Sources

- `papers/broken-born-checkpoint-v2.md` header and 'References' preamble — the current definitions; §5 — the re-tagged compatibility theorem
- Root `CLAUDE.md` 'Method' and `HANDOFF.md` §5 — the rule "Tag every claim"
- `HANDOFF.md` §2 — the ✓ mark
- `notes/broken-born-theory.md` §0 — the v0.1 tags and scope statement
- `notes/broken-born-program-v1.md` header and §11 — the v1 tags and the [T — verify] flag
- `papers/conjugate-special-relativity.md` header — #13's tag set and qualified forms
- `papers/reciprocity-toy-models.md` header — an untagged manuscript for blind review
- `wiki/CLAUDE.md` 'The wiki is derivative' — how the wiki carries tags
