---
title: "Obituary: conjugate monopoles explain the null result"
weight: 50
status: dead
description: "The founding claim that monopoles live in conjugate space, which is why we find none: wrong duality (electric–magnetic, not x ↔ p), and inflation already suffices."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md App. A item 5"
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §9"
  - "notes/knot-dark-matter-standalone.md §3"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "README.md (one-line description)"
  - "review/wiki-build-flags.md item 37"
---

*This was the claim that [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles) exist but belong to the conjugate, momentum-polarized half of physics, which would explain why no experiment has found one. It was the program's [founding supposition 5](/wiki/program/founding-suppositions). [The checkpoint](/wiki/history/documents/checkpoint)'s audit of its monopole claims split the supposition in two and killed this explanatory half on two counts: the symmetry that exchanges electric and magnetic charge is [electric–magnetic duality](/wiki/electric-magnetic-duality/s-duality), not the position–momentum [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) the program is built on, and [inflation](/wiki/cosmology/early-universe/inflation-and-dilution) already accounts for the absence of monopoles without new physics. The claim is dead and stays dead. The other half, that such monopoles may exist and would gravitate, survives on [a separate page](/wiki/electric-magnetic-duality/conjugate-monopoles), and so does [the prediction](/wiki/predictions/monopole-null) that no monopole of our sector will be found.*

**Status:** Dead — [D] for the audit, with inflationary dilution [T] (#11 §11.1); [the handoff](/wiki/history/documents/handoff) lists it among the dead claims ("wrong duality; inflation suffices", `HANDOFF.md` §2). The verdict is an argument, and no script checks it. Home section: [electric–magnetic duality](/wiki/electric-magnetic-duality); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

A magnetic monopole is a particle carrying magnetic charge alone: a north pole without a south pole. Many theories that unify the forces predict them, and none has been detected ([magnetic monopoles](/wiki/electric-magnetic-duality/monopoles); [monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches)) [T].

P.R.'s founding supposition 5 offered an explanation drawn from the program's picture of two polarizations of matter: "Monopoles live in conjugate space, explaining non-detection" ([#11](/wiki/history/documents/checkpoint) App. A item 5; [founding suppositions and their fates](/wiki/program/founding-suppositions)). In the program's postulates, matter comes in an x-polarized sector, ours, and a p-polarized sector, χ, and "gauge forces do not cross polarizations" (#11 §4, P4; [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter)). On the supposition, the monopoles belong to the second sector, so detectors built of our matter do not register them.

The supposition left one trace in the technical record before the audit, in [row 8](/wiki/predictions/monopole-null) of the [lab notebook](/wiki/history/documents/lab-notebook)'s [prediction table](/wiki/predictions/table-history) (`notes/broken-born-theory.md` §9):

| # | Observable | Standard expectation | BBT requirement | Kill condition |
| --- | --- | --- | --- | --- |
| 8 | Magnetic monopoles | Model-dependent | Permanent null (p-polarized solitons); Berry-curvature monopoles in solids as the only shadow | Direct monopole detection |

BBT is the Broken-Born program's name for itself. The parenthesis "(p-polarized solitons)" is the explanation. The first paper-shaped consolidation, v1 (#9; [the checkpoint and its predecessor](/wiki/history/documents/checkpoint)), already carried the row without it, "Permanent null; Berry-curvature monopoles in solids as the only shadow", and had no section on monopoles (`notes/broken-born-program-v1.md` §9). The repository's one-line description still reads "Physics hypothesis explaining dark matter and missing magnetic monopoles" (`README.md`), which is stale (flag 37 in `review/wiki-build-flags.md`; [CLAUDE.md and the README](/wiki/history/documents/project-instructions)).

## How it was tested

By argument, not by calculation. The checkpoint's v2.0, which added the charge-lattice section 11 (`HANDOFF.md` §3), carries the audit as §11.1, "The monopole audit, revised [D]", and repeats its verdict in the audit of founding suppositions (App. A item 5). No earlier version of the audit is in the repository. The verdict is reasoning from established physics; no script and no review round checked it.

## Why it failed

#11 §11.1:

> As an explanation of the null result: dead — the relevant duality is electric–magnetic (E↔B, g → 1/g), not x↔p, and inflationary dilution already accounts for absence [T].

The sentence gives two reasons, and they do not depend on each other.

### The wrong duality

Two different symmetries are in play.

- **Electric–magnetic duality** acts on fields and charges: it exchanges the electric and magnetic fields, E ↔ B, and with them electric and magnetic charges. Because Dirac's condition fixes the product of the two kinds of charge, it also exchanges weak and strong coupling, the "g → 1/g" of #11's sentence ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality); [Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization)) [T].
- **Born reciprocity**, the symmetry the program is built on, acts on phase space: ρ: (x, p) → (p, −x), implemented on quantum states by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) (#11 §3; [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)).

The supposition used the second symmetry to explain a fact about the first. Whether a particle carries magnetic charge is a question about where it sits among electric and magnetic charges; which polarization its matter belongs to is a question about position and momentum. The duality that relates magnetic charges to electric ones, and that bears on why one kind is seen and the other is not, is electric–magnetic duality. The same section of the checkpoint finds that this duality has its own account of why magnetic particles are not seen: Dirac's condition makes them strongly coupled and heavy ([the magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family)). The observation of §11.3 that the two dualities share a matrix is a structural comparison, not a mechanism that moves monopoles between sectors ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)).

### Inflation suffices [T]

The absence of monopoles has a standard explanation that needs no new physics. A symmetry-breaking transition in the early universe that can produce monopoles produces at least about one per causally connected region ([the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism)), and for superheavy monopoles this is far too many: "density of such monopoles in the early universe is estimated to be unacceptably large" (Preskill 1979, as [the round-3 audit](/wiki/method/review/round-3/rulings) quotes the abstract). Annihilation does not remove enough of them; the v3 worklog records Preskill's result that "annihilation cannot reduce n/T³ below ~10⁻¹⁰ at m ≈ 10¹⁶ GeV" ('Findings neither referee raised', F1). A period of inflation after the monopoles form dilutes them to an unobservable density ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem); [inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)).

With that account available, the null result gives no support to a conjugate sector: it is expected without one.

## The split

The audit did not kill the whole supposition. #11 App. A item 5:

> Monopoles live in conjugate space, explaining non-detection — **split**: as explanation, dead (wrong duality; inflation suffices); as ontology, alive and consequence-bearing (P.R.'s "true-but-irrelevant is measure zero"); the knot candidate it fed is retired (§12).

The other half, conjugate monopoles as objects that may exist, survives because the program's postulate P4 couples both matter sectors to the same geometry, so that such objects would gravitate ([conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)). P.R. supplied the correction that a conjugate object cannot be "true but irrelevant".

### Two wordings, one verdict (unresolved)

#11 states the correction twice, in different words. §11.1: "true but irrelevant" is "the empty set (a correction supplied by P.R.)". App. A item 5: "P.R.'s "true-but-irrelevant is measure zero"". The empty set says there is no such case; measure zero says such cases are negligible. The checkpoint does not reconcile the two, and the verdict on the explanation is the same under either.

## What survives

- **The ontology** [D]: if conjugate-sector monopoles exist, they gravitate ([conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)).
- **The prediction for our sector.** [Row 8](/wiki/predictions/monopole-null) of #11 §13 keeps a permanent null for "Magnetic monopoles (ours)", with "Berry-curvature monopoles in solids as the only shadow", and is killed by "Direct detection". The parenthesis "(p-polarized solitons)" is gone. #11 gives the row no separate rationale; its account of the absence of monopoles, in §11.1, is inflationary dilution [T].
- **The laboratory shadow**: "Weyl semimetals host catalogued families of momentum-space Berry-curvature monopoles [16†] — right geometry, different flux" (#11 §11.1).
- **The charge lattice.** The same section of #11 adds the observation that choosing which charges count as electric is itself a polarization [D — structural; math T] ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)).

The candidate the supposition fed is dead as well. Superheavy monopoles of a hidden gauge sector were proposed as the [dark matter](/wiki/dark-matter), worked up as the standalone manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate), and retired on 2026-10-19 after [round 3](/wiki/method/review/round-3) of [blind review](/wiki/method/review) found their abundance misnormalized ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## History

- **v0.1, the lab notebook** (#1 §9): row 8's "Permanent null (p-polarized solitons)" carries the explanation.
- **v1.0** (#9 §9): the row without the parenthesis; no monopole section.
- **v2.0, the checkpoint** (#11 §11.1, App. A item 5): the audit splits the supposition and kills the explanation; the handoff lists it as dead, "Conjugate monopoles as the *explanation* of our monopole non-detection (wrong duality; inflation suffices)" (`HANDOFF.md` §2).
- **v2.1** (2026-10-19): the knot candidate the supposition fed is retired (#11 §11.1, §12).
- **Now**: the README's tagline still names the dead explanation (flag 37 in `review/wiki-build-flags.md`).

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.1 — the audit and the two reasons [D, T]; App. A item 5 — the supposition and its split fate; §3 — ρ and the Fourier transform; §4 — P4; §13 — row 8 as it stands.
- `HANDOFF.md` §2 — listed as dead: "wrong duality; inflation suffices"; §3 — §11 added in v2.0.
- `notes/broken-born-theory.md` §9 — row 8 in the lab notebook, with "(p-polarized solitons)".
- `notes/broken-born-program-v1.md` §9 — row 8 in v1, without the parenthesis.
- `review/v3-worklog.md` 'Findings neither referee raised' (F1) — Preskill's annihilation bound, verified from the scan.
- `review/round3/referee/audit-notes.md` Step 1 — Preskill's abstract, as the round-3 referee quotes it.
- `notes/knot-dark-matter-standalone.md` §3 — Preskill 1979 as #14 cites it (withdrawn manuscript).
- `README.md` — the stale one-line description; `review/wiki-build-flags.md` item 37 records it.
