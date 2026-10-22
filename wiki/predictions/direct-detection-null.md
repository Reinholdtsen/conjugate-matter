---
title: "Row 7: a permanent null in direct detection"
weight: 80
status: alive
description: "Both remaining dark-matter candidates couple to Standard Model matter only through gravity, and postulate P4, taken strictly since v2.1, lets no gauge force or kinetic mixing beyond gravity's cross the sectors; killed by any confirmed non-gravitational coupling of dark matter to the Standard Model."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 7"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions' item 1"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3/referee/audit-notes.md Step 1, citation [9]"
  - "review/v3-worklog.md 'Round-2 pending list' R4"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §11"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*Row 7 predicts that experiments searching for dark matter through any interaction other than gravity will never see it. Direct-detection experiments look for dark-matter particles striking atomic nuclei in shielded underground detectors, and collider experiments look for dark matter produced in particle collisions; both need dark matter to couple to ordinary matter, the particles of the Standard Model, through some interaction besides gravity [T]. In the program, the two remaining dark-matter candidates, [χ particles](/wiki/dark-matter/candidates/chi-particles) and [an X-condensate](/wiki/dark-matter/candidates/x-condensate), have no such coupling: postulate [P4](/wiki/program/postulates/p4-polarized-matter) lets no gauge force act across the two sectors of matter, and since 2026-10-19 it is read strictly, excluding even the small [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) that could otherwise link them. The expected signal is zero, permanently. One confirmed non-gravitational coupling would kill the row, which is one of the three that #11 lists as the program's near-term falsification exposure.*

**Status:** Alive — it rests on postulate P4 [P] (#11 §4), taken strictly since v2.1 by [round-3 Decision 1](/wiki/method/review/round-3/decisions): a postulate, and a reading of it adopted by decision, not a derivation — not machine-checked; no experiment has reported a confirmed signal.

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 7:

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| Direct detection / colliders | WIMP-type signal eventually | **Permanent null** (both dark-sector candidates SM-decoupled; P4 strict) | Any confirmed non-gravitational DM–SM coupling |

WIMP is a weakly interacting massive particle, SM the Standard Model and DM dark matter. "P4 strict" is the strict reading of [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter#the-strict-reading-since-v21).

## The observable [T]

Three kinds of search look for a non-gravitational coupling between dark matter and ordinary matter [T]:

- **Direct detection.** The Milky Way's dark-matter halo streams through the Earth at roughly the Galaxy's orbital speeds. A detector deep underground, shielded from cosmic rays and radioactivity, waits for a dark-matter particle to scatter off an atomic nucleus and leave a small recoil energy. The rate is proportional to the scattering cross-section, which a purely gravitational interaction makes far too small to see.
- **Colliders.** If dark matter couples to quarks or gluons, collisions can produce it. It leaves the detector unseen, and the event shows up as momentum missing from the balance of the visible products.
- **Indirect searches**, for the products of dark-matter annihilation or decay in space, are not named in the row.

All three are sensitive only to interactions other than gravity. A dark sector that interacts with ordinary matter only gravitationally gives none of them a signal [T].

## The standard expectation

"WIMP-type signal eventually" (#11 §13). A weakly interacting massive particle is the classic dark-matter candidate: a particle with an interaction strength of the order of the weak force, which in the early universe would freeze out of thermal equilibrium with about the observed abundance [T] ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)). Such a particle couples to ordinary matter, so the searches above should eventually see it. The [lab notebook](/wiki/history/documents/lab-notebook) defines "standard theory" for its table as the standard cosmological model with [general relativity](/wiki/gravity/spin-2-fields/general-relativity) and generic alternatives of the WIMP and Yukawa self-interacting kinds, and wrote the expectation as "Eventually expected (WIMP-type)" (#1 §9).

## The Broken-Born requirement

### Two sectors of matter, one gravity

Postulate P4, as #11 §4 states it:

```text
P4  Matter comes in x-polarized (Standard Model) and p-polarized (χ)
    representations; both couple universally to H; gauge forces do not
    cross polarizations. [P; taken strictly since v2.1: no kinetic mixing
    between the sectors beyond what gravity induces, which vanishes if
    hidden charge conjugation is exact and otherwise first appears at
    six loops, ε ≲ 10⁻¹³ [27S].]
```

The first two clauses make dark matter gravitate like ordinary matter. H is [the generalized metric](/wiki/phase-space/born-geometry/born-structures) of [phase space](/wiki/phase-space), which contains the spacetime metric g, and both kinds of matter couple to it in the same way. The lab notebook draws the consequence: "χ couples to g universally: it falls, orbits, and lenses like ordinary dark matter. Bullet Cluster lensing-centroid behavior is automatic" [D] (#1 §4); #11 §8 keeps it as "χ propagates on g (equivalence principle; Bullet-Cluster-safe)". The third clause rules out shared gauge forces: no particle carries the charges of both sectors ([two polarizations of matter](/wiki/program/postulates/p4-polarized-matter#two-polarizations-of-matter)).

### No gauge force across: kinetic mixing and the strict reading

Even with no particle charged under both, two sectors that each have an abelian gauge field, a photon of their own, can be linked by kinetic mixing [T]: a term in the action that couples the field strength of our photon to that of a hidden photon with a small coefficient ε. Its effect is that particles charged only under the hidden force acquire an electric charge of order ε times ours, which direct detection and other searches could register ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#what-kinetic-mixing-is)).

Since v2.1 #11 reads P4 as excluding kinetic mixing "beyond what gravity induces". Gravity couples to both sectors, so it is the one link P4 cannot remove. The amount it induces comes from Gherghetta, Kersten, Olive and Pospelov [27S]: none if hidden charge conjugation is exact, and otherwise a contribution that "first appears at six loops, ε ≲ 10⁻¹³" (#11 §4). The round-3 referee checked the paper and quoted it: "If C_A and C_X are separately good symmetries ..., then kinetic mixing cannot be induced at any perturbative order" (p. 5) and "kinetic mixing through gravity alone, requires at least six loops and could be as large as ~1e-13" (abstract) (`review/round3/referee/audit-notes.md`, Step 1, citation [9]; [mixing from gravity alone](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#a-mixing-from-gravity-alone)).

The strict reading was a decision. On 2026-10-19, after the round-3 review of the soliton manuscript #14, Paul delegated a set of decisions to Claude, keeping the veto; the first reads (`review/round3-adjudication.md`, 'Decisions'):

> **Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry.
> - It is the program's own postulate P4 ("gauge forces do not cross polarizations") taken at face value.
> - The alternative rested on an unsupported coefficient. The dimension-5 "O(1) at the Planck scale" estimate (ruling 7) has no source. The sources generate that operator only from bi-charged states, which P4 forbids.
> - It costs nothing and closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector.

The three channels belonged to #14's hidden sector, which is retired ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)); the reading stays as P4's. The root `CLAUDE.md` lists it among the changes since the handoff: "Strict sector separation (P4 at face value) is in force." The reasons are on [round-3 decisions](/wiki/method/review/round-3/decisions) and [why it was adopted](/wiki/program/postulates/p4-polarized-matter#why-it-was-adopted-round-3-decision-1).

### Both candidates

#11 §12 lists two candidates [D — framework; each candidate O] ([dark-sector candidates](/wiki/dark-matter/candidates)):

- **χ particles** are the p-polarized matter of P4, and P4 strict is the whole of their decoupling. #11 §12 lists a "permanent direct-detection null" among their distinctive handles ([the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles#handles-and-tests)).
- **The X-condensate** is a coherent oscillation of the [momentum graviton X](/wiki/gravity/momentum-graviton), a field of the geometry rather than of matter, with no gauge charges. X does couple to ordinary matter, with "SM couplings gravitational-strength and Yukawa-cut at 1/M_X" (#11 §7.5; [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)); the null concerns couplings other than gravity ([the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate#its-tests)).

The requirement's parenthesis, "both dark-sector candidates SM-decoupled", covers the pair. A null holds whichever candidate is right, so row 7 does not help to tell them apart ([row 11](/wiki/predictions/dark-sector-microstructure)).

### A postulate, not a derivation

The row derives nothing beyond P4. It carries no tag of its own; it rests on P4 [P], and "permanent" restates the postulate: if P4 holds as read, no non-gravitational signal exists to be found. #11 §15 counts the row among the three, rows 1, 4 and 7, that expose the program to near-term falsification. In the wiki's reading, the exposure is near-term because the searches are running now and one confirmed signal would end the claim, while no number of null results can confirm a permanent null.

## What kills it

"Any confirmed non-gravitational DM–SM coupling" (#11 §13): a confirmed signal in a direct-detection experiment or at a collider, or any other demonstrated interaction between dark matter and ordinary matter besides gravity. The condition has not changed since the lab notebook, which worded it "Any confirmed DM–SM non-gravitational coupling" (#1 §9), as did v1 (#9 §9); #11's word order dates from v2.0.

## The data situation

No direct-detection experiment or collider search has reported a confirmed dark-matter signal [T]. The program's documents cite no experimental result for this row; its standing in the record comes from the postulate. Gravitational evidence for dark matter, which the row leaves untouched, is what both candidates are built to supply: χ "falls, orbits, and lenses like ordinary dark matter" (#1 §4).

## What the record leaves unresolved

- **A ceiling or a floor.** #11 writes "ε ≲ 10⁻¹³". The round-3 referee notes that Gherghetta et al. present the figure as a floor, the "minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking", "consistent with "<~" only in the sense "up to"" (audit notes, Step 1; the referee sets "floor" in capitals). #11's wording stands, and the reading is unresolved ([an unresolved reading: ceiling or floor](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#an-unresolved-reading-ceiling-or-floor)).
- **Exact or gauged.** #11 says the mixing vanishes "if hidden charge conjugation is exact"; Decision 1 says "zero if hidden charge conjugation is a gauged symmetry". The v3 worklog gives the reason the distinction matters: "Quantum gravity forbids an exact global C [Banks–Seiberg 2011; Harlow–Ooguri 2021]; a gauged C (O(2)/O(3)-type) remains a loophole [Obied–Parikh, preprint]" (item R4). #11 outranks the adjudication, so its wording is the current statement ([how to read the bound and the zero](/wiki/program/postulates/p4-polarized-matter#how-to-read-the-bound-and-the-zero)).
- **Couplings that are not gauge forces.** P4 excludes gauge forces across the polarizations, and its strict reading excludes kinetic mixing. The documents do not discuss other kinds of coupling for χ or the X-condensate. The round-3 referee listed "The Higgs portal" among the constraints #14 had omitted for its hidden sector, accepted as a to-do and not individually re-checked (`review/round3-adjudication.md`, 'Rulings'); no document takes it up for the remaining candidates.
- **The handoff's open item.** [The handoff](/wiki/history/documents/handoff) listed "UV stability of sector separation / kinetic mixing" as open (`HANDOFF.md` §2, item 3), and its queue paired the † literature battery with "resolve the gravity-induced kinetic mixing question" (§8, item 6). The strict reading of P4 answers the first in the record's terms, and #11 §14 lists no kinetic-mixing item. [27S] is a live-searched reference [S], so it is outside the † battery ([Open: the † literature battery](/wiki/method/literature-battery)).

## A conflicting popular claim

The popular article #12 says "The momentum-polarized sector is the magnetic side of electromagnetism" ('Dark matter as the other polarization'). A sector magnetically charged under our photon would have exactly the coupling this row excludes, and the identification also contradicts strict P4. It is not a program claim and is dead: [Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification#it-contradicts-row-7). #12 presents the framework as if it were confirmed and is not a source for any claim's status ([the popular articles](/wiki/history/documents/popular-articles)).

## Superseded: earlier forms of the row

| Version | Requirement |
| --- | --- |
| v0.1 (#1 §9) | "**Permanent null**: χ has no non-gravitational SM coupling" |
| v1 (#9 §9) | "**Permanent null** — χ (or X-condensate) has no non-gravitational SM coupling" |
| #11 v2.0 | "**Permanent null** (all three trilemma candidates SM-decoupled)" |
| #11 v2.1, v2.2 | "**Permanent null** (both dark-sector candidates SM-decoupled; P4 strict)" |

The v2.0 wording survives only in the repository's history (commit 8d588f6, the imported checkpoint). The changes follow the candidates: v1 added the X-condensate, v2.0 the superheavy solitons as a third, and v2.1 retired the solitons and added "P4 strict" ([the history of the predictions table](/wiki/predictions/table-history#the-checkpoint-v21-after-round-3)).

In v0.1 the row was one of three flagships: "Rows 1, 3, and 7 are the flagship discriminants: no mainstream framework predicts an exponential scattering cliff, gravitationally-detectable macro-granularity of the local velocity distribution, *and* a guaranteed-null direct-detection program" (#1 §9). The cliff is now a knee and the granularity row is dead ([Obituary: velocity-space granularity in halos (old row 3)](/wiki/dark-matter/momentum-clumping/velocity-granularity)); the null survives unchanged. v1 moved the row, with rows 1 and 4, into its near-term falsification exposure (#9 §11), where #11 keeps it.

Kinetic mixing reached the row through the review of #14. Round 1 found "kinetic mixing unaddressed", and v2 of the manuscript added "postulate + ε ≲ 10⁻⁵ exclusion"; round 2 disputed a gravity-induced channel, with the handoff's summary that "v2's "forbidden to all orders" is too strong either way; soften and resolve by literature" (`HANDOFF.md` §6). The v3 worklog resolved it from the literature: "Pure gravity: ε = 0 if dark charge conjugation C is exact. Otherwise it needs at least 6 loops and gives ≲10⁻¹³ [Gherghetta–Kersten–Olive–Pospelov, PRD 100, 095001 (2019)]. The referee is right that it exists, and it is negligible." (item R4). Round 3 and Decision 1 followed, and #11 v2.1 wrote the result into P4 ([how the record reached it](/wiki/program/postulates/p4-polarized-matter#how-the-record-reached-it)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 7 — the row; §4 — P4 and its strict reading [P], [27S]; §7.5 — X's couplings to ordinary matter; §8 — χ on g; §12 — the candidates and their handles; §15 — the near-term exposure
- `CLAUDE.md` 'Since the handoff' — strict sector separation in force
- `review/round3-adjudication.md` 'Decisions' item 1 — the strict reading and its reasons; 'Rulings' — rulings 7 and 9 and the omitted constraints, among them the Higgs portal
- `review/round3/referee/audit-notes.md` Step 1, citation [9] — the quotations from [27S] and the floor reading
- `review/v3-worklog.md` 'Round-2 pending list', item R4 — the literature resolution of gravity-induced mixing and the exact-versus-gauged point
- `HANDOFF.md` §2 item 3, §6, §8 item 6 — the open item, the review history of kinetic mixing and the queued question
- `notes/broken-born-theory.md` §1 — P4 in v0.1; §4 — χ falls, orbits and lenses [D]; §9 — v0.1's row 7, the standard theory and the flagships (quotations from #1 are transcribed from its LaTeX)
- `notes/broken-born-program-v1.md` §9, §11 — v1's row 7 and its exposure rows
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the dead magnetic identification; not a status source
