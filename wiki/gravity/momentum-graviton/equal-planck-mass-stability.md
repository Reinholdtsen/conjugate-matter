---
title: "Open: stability at equal Planck masses"
weight: 100
status: open
description: "The known late-time stability of a heavy spin-2 field assumes the second metric's Planck mass is much smaller than the first; reciprocity forces equal Planck masses, which closes that escape, so stability is open."
sources:
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Evidence used so far'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "notes/knot-dark-matter-standalone.md 'References'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3/referee/audit-notes.md 'Step 1 - Citations'"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "HANDOFF.md §6"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "CLAUDE.md 'Since the handoff'"
---

*This open problem asks whether a heavy massive spin-2 field such as the [momentum graviton X](/wiki/gravity/momentum-graviton) can be stable in an expanding universe when its metric and the ordinary metric have equal Planck masses, the coefficients that set how strongly each metric responds to matter [T]. Published analyses of bimetric cosmologies find instabilities when the spin-2 field is light, and the work that finds a heavy spin-2 field linearly stable at late times assumes that the second metric's Planck mass is much smaller than the first. Reciprocity forces the two Planck masses to be equal, which excludes that regime, and whether a large mass alone is enough has not been checked. The question came out of the second blind review of the soliton manuscript #14, since withdrawn. It is recorded only in the review worklog and the manuscript; [checkpoint #11](/wiki/history/documents/checkpoint) §14 does not list it.*

**Status:** Open — no tag in the sources — round-2 item R7 in `review/v3-worklog.md` ("state this as an open consistency item, not as evaded"), and #14 §1 and §5 item 7; absent from #11 §14; no calculation and no `verify/` script. Listed in [Open problems and the queue](/wiki/status/open-problems).

## The question

The v3 worklog states it as one sentence of item R7: "Whether a large mass alone is enough at M_f = M_g is open". Here M_g and M_f are the Planck masses of the two metrics: g, the ordinary metric, and f, the second metric of the program's [bimetric](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) gravity sector, whose fluctuation, combined with g's, gives X. The manuscript #14 put it the same way: "the stability of a heavy spin-2 field at equal Planck masses is an open consistency condition (Sec. 5, item 7)" (§1).

What the item qualifies is X's consistency as a field in an expanding universe. #14 counted "instability of a heavy spin-2 field at equal Planck masses" among the internal conditions that would exclude its proposal (§5, item 7), and listed "the ghost-free landing of the mass mechanism and its cosmological stability at equal Planck masses" among its conjectural ingredients (§6).

## Background: Planck masses and bimetric cosmology [T]

In bimetric gravity each metric has its own Einstein–Hilbert term. Its coefficient is that metric's Planck mass, and it sets how strongly the metric responds to sources; in general relativity there is one such coefficient, M_P [T]. The bimetric theory has expanding-universe solutions in which both metrics take the homogeneous, isotropic form of cosmology, and they fall into separate families, or branches [T]. Small perturbations about such a solution can be unstable in two ways [T]. A gradient instability makes short-wavelength perturbations grow exponentially, because a squared propagation speed is negative. A ghost is a mode with negative kinetic energy, which makes the vacuum unstable once it interacts. The background is on [Bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology).

A massive spin-2 field in a de Sitter universe with Hubble rate H must also satisfy the Higuchi bound, m² ≥ 2H²: for masses between zero and that value, its helicity-0 mode has negative norm [T]. The round-3 audit read the bound in Higuchi's abstract as "M^2 cannot be between 0 and 2/3 x (cosmological constant)", which with Λ = 3H² is m² ≥ 2H². #14 §1: "The Higuchi bound m^2 >= 2H^2 [6] is satisfied trivially by the heavy field". At the bound itself sits the [partially massless](/wiki/gravity/spin-2-fields/partially-massless-gravity) case [T].

## What the cited literature finds

The worklog's item R7 sorts the literature by two properties, the spin-2 mass and the ratio of the Planck masses:

| Spin-2 mass | Planck masses | Finding | Works (#14's references) |
| --- | --- | --- | --- |
| of order today's Hubble rate, m ~ H₀ | comparable, M_f ~ M_g | gradient or ghost instabilities | Comelli–Crisostomi–Pilo; Könnig et al.; Lagos–Ferreira [4] |
| heavy | M_f ≪ M_g | linearly stable at late times | Akrami–Hassan–Könnig–Schmidt-May–Solomon [5] |
| heavy | M_f = M_g | open | De Felice et al. 2014, cited in [5], not read |

In the worklog's words: "The instability analyses assume a spin-2 mass m ~ H₀ and M_f ~ M_g", and "A heavy spin-2 is linearly stable at late times". #14 §1 has the same two statements: the analyses "find gradient or ghost instabilities, but they assume a spin-2 mass of order the present Hubble rate and comparable Planck masses for the two metrics [4]", and "A heavy spin-2 field has been shown to be linearly stable at late times in the regime where the second metric's Planck mass is much smaller than the first [5]."

The round-3 audit quotes the stable regime from Akrami et al. (p. 7): "the alpha->0 limit brings bimetric theory arbitrarily close to GR even for ... m >> H0. The presence of heavy spin-2 fields ... is therefore not excluded as long as ... M_f is sufficiently small" (GR is general relativity). The worklog names three limits on that result: "their viable regime takes **M_f ≪ M_g**; it holds at linear order only, with tuned βₙ; and the strong-coupling era H > H⋆ is unresolved."

The works, as #14's reference list gives them (unmarked there; full entries on [the references page](/wiki/references)):

- [4] D. Comelli, M. Crisostomi, L. Pilo, JHEP 06 (2012) 085, arXiv:1202.1986; F. Könnig, Y. Akrami, L. Amendola, M. Motta, A. R. Solomon, Phys. Rev. D 90, 124014 (2014), arXiv:1407.4331; M. Lagos, P. G. Ferreira, JCAP 12 (2014) 026, arXiv:1410.0207.
- [5] Y. Akrami, S. F. Hassan, F. Könnig, A. Schmidt-May, A. R. Solomon, Phys. Lett. B 748, 37 (2015), arXiv:1503.07521.
- [6] A. Higuchi, Nucl. Phys. B 282, 397 (1987).

## Why the program cannot use the escape

Reciprocity acts on the program's spin-2 sector as an exchange of the two frames, and calc note #8 §3 records that the same symmetry forces "equal effective Planck masses" ([equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses)). The worklog draws the consequence under the heading "Tension": calc note #8 §3 "says reciprocity forces equal effective Planck masses (M_f = M_g), which rules out the M_f ≪ M_g escape." #14 §1 says the same: "The framework's reciprocity, acting as exchange of the two metrics, instead sets the two Planck masses equal".

The program's case therefore falls in neither studied regime. X is heavy, unlike the light spin-2 fields of the instability analyses, and its Planck masses are equal, unlike the stable regime. The same equality is why ordinary matter feels X at gravitational strength ([safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)).

## What is open

- **A large mass at equal Planck masses.** The worklog's open question, with its one lead: "(De Felice et al. 2014, cited in Akrami et al.: 'the instability becomes negligible for large values of m'; not yet read)". No document gives the reference's details or reports reading it.
- **Beyond linear order.** The stable regime "holds at linear order only, with tuned βₙ". The program's own coefficients are fixed to the palindromic branch with two free parameters ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)); no document compares them with the tuned coefficients of that regime.
- **The early universe.** "the strong-coupling era H > H⋆ is unresolved" (R7; the worklog does not define H⋆), and the handoff's summary of the round-2 finding ends "early universe remains open" (`HANDOFF.md` §6).

## How the citations were checked

The worklog's evidence for the round-2 items came from a literature report in which "a subagent with web access pulled each record from INSPIRE, arXiv, the PDG 2024 monopole review and the scanned Preskill 1979 paper, with no citations from memory" ('Evidence used so far'; PDG is the Particle Data Group). The round-3 audit then checked #14's 23 references and found that all resolve, and it checked what each is cited for (`review/round3/referee/audit-notes.md`, Step 1):

- **[4]** supports "find gradient or ghost instabilities", but is a "slight over-generalisation": "Koennig et al. abstract identifies a" stable model "(infinite-branch bigravity), and Lagos-Ferreira find stable scalar perturbations for a particular parameter choice" (the audit sets "stable" in capitals). The audit adds that "The 'm ~ H0 and comparable Planck masses' premise is consistent with [5]'s framing". The adjudication accepted the point as ruling 12, "[4] over-generalized" ([round-3 rulings](/wiki/method/review/round-3/rulings)).
- **[5]** supports the claim, with the quotation above.
- **[6]** supports the bound, read as m² ≥ 2H².

So the instability literature is not uniformly negative even for light spin-2 fields. The open question concerns the heavy, equal-Planck-mass case, which, on the worklog's account of their assumptions, none of the works in [4] and [5] covers.

## Where the item is recorded

- **The finding.** The second blind review of #14 counted among its valid findings the "bimetric cosmological-branch instability severity (mass hierarchy may evade — the analyses assume light second metric; early universe remains open; cite properly)" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).
- **The worklog.** Item R7 of the round-2 pending list, marked "ready, with a tension", with the decision "v3: state this as an open consistency item, not as evaded." When v3 was drafted, "The bimetric instability at equal Planck masses is added to item 7" of its exclusion conditions ('v3 as drafted (2026-10-19)').
- **The manuscript.** #14 v3 states it in §1, lists it in §5 item 7 and §6. #14 was withdrawn on 2026-10-19 after failing round-3 review for its abundance arithmetic, and its soliton candidate is retired ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Round 3 ruled on R7 only through the citation point of ruling 12.
- **Its standing now.** The question concerns X, which stands ([The momentum graviton X](/wiki/gravity/momentum-graviton)), not the retired candidate. #11 §14 does not list it, it is not on the current queue in the root `CLAUDE.md`, and no later document closes it, so the wiki keeps it as an open item.

## Sources

- `review/v3-worklog.md` 'Round-2 pending list' — item R7: the literature, its limits, the tension and the decision; 'Evidence used so far' — how the literature report was made; 'v3 as drafted (2026-10-19)' — the item added to #14's exclusion conditions
- `notes/knot-dark-matter-standalone.md` §1 — the open consistency condition and the Higuchi bound as stated in the withdrawn manuscript; §5 item 7 — the exclusion condition; §6 — the conjectural ingredients; 'References' [4]–[6]
- `review/round3-adjudication.md` 'Rulings' — ruling 12, reference [4] over-generalized
- `review/round3/referee/audit-notes.md` 'Step 1 - Citations' — what references [4], [5] and [6] support
- `notes/debt1a-iv-beta-coefficients.md` §3 — equal effective Planck masses forced by reciprocity
- `HANDOFF.md` §6 — the round-2 finding the item answers
- `papers/broken-born-checkpoint-v2.md` §14 — the current list of open problems, which does not include the item
- `CLAUDE.md` 'Since the handoff' — the current queue
