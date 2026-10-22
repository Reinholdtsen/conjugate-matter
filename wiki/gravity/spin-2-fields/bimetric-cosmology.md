---
title: "Bimetric cosmology and its instabilities"
weight: 90
status: established
description: "Known instabilities of bimetric cosmological branches, the heavy-spin-2 regime shown to be linearly stable when the second Planck mass is much smaller, and the Higuchi bound in de Sitter: the literature behind the open question of X's stability at equal Planck masses."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "notes/knot-dark-matter-standalone.md refs [4]–[6]"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3-adjudication.md 'Rulings' 12"
  - "HANDOFF.md §6"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "review/wiki-build-flags.md item 5"
---

*Bimetric cosmology studies expanding-universe solutions of [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), in which both metrics take the homogeneous and isotropic form of standard cosmology. Published analyses of its solution branches find gradient or ghost instabilities in the perturbations when the massive spin-2 field is about as light as today's Hubble rate and the two metrics have comparable Planck masses, though not in every model. A heavy spin-2 field has been shown to be linearly stable at late times when the second metric's Planck mass is much smaller than the first. Separately, a massive spin-2 field on de Sitter space must satisfy the Higuchi bound m² ≥ 2H², which a heavy field meets trivially. For the program the known stable regime is out of reach: [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) sets the two Planck masses equal, so the cosmological stability of a heavy [momentum graviton X](/wiki/gravity/momentum-graviton) is an open question.*

**Status:** Established — [T] — literature as summarized in the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) (§1) and in item R7 of the [round-2](/wiki/method/review/rounds-one-and-two) pending list in `review/v3-worklog.md`. The [round-3](/wiki/method/review/round-3) audit confirmed that the cited papers exist and support the statements, and ruling 12 accepted its finding that #14's reference [4] is over-generalized ([round-3 rulings](/wiki/method/review/round-3/rulings)). The consequence for X is [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability).

## Cosmological solutions of bimetric gravity

In Hassan–Rosen bimetric gravity both metrics, g and f, are dynamical, each with its own Planck mass, M_g and M_f [T]. A cosmological solution takes each metric in the homogeneous and isotropic Friedmann–Lemaître–Robertson–Walker (FLRW) form ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)), with a scale factor of its own. The field equations then give a Friedmann equation for each metric, in which the interaction potential acts like an extra energy density, and a constraint that ties the two scale factors together. The solutions fall into families called branches, which differ in how the second scale factor follows the first [T].

Much of this literature studies the interaction potential as the source of the late-time acceleration of the universe ([dark energy](/wiki/cosmology/dark-energy)), which puts the spin-2 mass near the present Hubble rate H₀ [T]. That is the regime #14 says the instability analyses assume.

## Kinds of instability

Small perturbations around a cosmological solution can grow in several ways [T]:

- **Ghost.** A mode whose kinetic term has the wrong sign carries negative energy. Coupled to ordinary modes it lets the vacuum decay into pairs of positive- and negative-energy excitations, so the solution is not a stable ground state. The Boulware–Deser ghost that generic massive-gravity potentials revive is one example ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)). The ghost-free bimetric potential removes that mode, but perturbations around particular backgrounds can still have wrong-sign kinetic terms; the Higuchi ghost below is one.
- **Gradient instability.** A mode whose squared propagation speed is negative grows exponentially instead of oscillating, and the shorter its wavelength, the faster it grows.
- **Strong coupling.** When the kinetic term of a mode becomes small, its interactions dominate and linear perturbation theory cannot be trusted. The outcome then needs the nonlinear theory.

The round-3 audit describes one of the cited results as an "exponential Jeans-like instability" (audit notes, Step 1). The term refers to growth of the kind that drives gravitational collapse on scales above the Jeans length [T].

## What the published analyses found

The withdrawn manuscript summarizes them: "The published analyses of bimetric cosmological branches find gradient or ghost instabilities, but they assume a spin-2 mass of order the present Hubble rate and comparable Planck masses for the two metrics [4]" (#14 §1). Its reference [4] groups three papers:

- D. Comelli, M. Crisostomi, L. Pilo, JHEP 06 (2012) 085, arXiv:1202.1986;
- F. Könnig, Y. Akrami, L. Amendola, M. Motta, A. R. Solomon, Phys. Rev. D 90, 124014 (2014), arXiv:1407.4331;
- M. Lagos, P. G. Ferreira, JCAP 12 (2014) 026, arXiv:1410.0207.

The round-3 audit checked each against its abstract and text (`review/round3/referee/audit-notes.md`, Step 1). It records an "exponential Jeans-like instability in 2nd branch" for Comelli et al., "instabilities for several classes" for Könnig et al. and "generally exponential instabilities" for Lagos–Ferreira. It also found exceptions: the Könnig et al. abstract identifies a stable model, infinite-branch bigravity, and Lagos and Ferreira "find stable scalar perturbations for a particular parameter choice". The audit judged that [4] supports "find gradient or ghost instabilities" with a "slight over-generalisation", and that the premise of "m ~ H0 and comparable Planck masses" is "consistent with [5]'s framing ('Previous work has suggested ... generically plagued by instabilities')". Ruling 12 of the round-3 adjudication accepted the point among the minor citation issues, "[4] over-generalized" (`review/round3-adjudication.md`, 'Rulings'). The instabilities are common in these analyses but not universal.

## The heavy spin-2 regime

The manuscript continues: "A heavy spin-2 field has been shown to be linearly stable at late times in the regime where the second metric's Planck mass is much smaller than the first [5]" (#14 §1). Reference [5] is Y. Akrami, S. F. Hassan, F. Könnig, A. Schmidt-May, A. R. Solomon, Phys. Lett. B 748, 37 (2015), arXiv:1503.07521. The audit quotes the paper's p. 7: "the alpha->0 limit brings bimetric theory arbitrarily close to GR [general relativity] even for ... m >> H0. The presence of heavy spin-2 fields ... is therefore not excluded as long as ... M_f is sufficiently small" (audit notes, Step 1).

The worklog states what the result does not cover: "Three limits on that: their viable regime takes **M_f ≪ M_g**; it holds at linear order only, with tuned βₙ; and the strong-coupling era H > H⋆ is unresolved" (`review/v3-worklog.md`, R7). It writes H⋆ without defining it; the round-2 finding it answers says that the "early universe remains open" (HANDOFF §6). One further result is named but unread: "Whether a large mass alone is enough at M_f = M_g is open (De Felice et al. 2014, cited in Akrami et al.: 'the instability becomes negligible for large values of m'; not yet read)" (R7).

## The Higuchi bound

De Sitter space is the spacetime of a universe expanding at a constant Hubble rate H under a positive cosmological constant. On this page H is the Hubble rate, not the program's phase-space metric H. On it a massive spin-2 field must satisfy [T]

```text
m² ≥ 2H²
```

For smaller positive masses the field's helicity-0 polarization has negative norm, a ghost [T]. #14 cites the bound as its reference [6], A. Higuchi, Nucl. Phys. B 282, 397 (1987). The audit read it from Higuchi's abstract, "M^2 cannot be between 0 and 2/3 x (cosmological constant)", converted it with "Lambda = 3H^2" to "m^2 >= 2H^2", and found that the reference supports the statement (audit notes, Step 1). At the edge, m² = 2H², a gauge symmetry removes the helicity-0 polarization and the field is [partially massless](/wiki/gravity/spin-2-fields/partially-massless-gravity).

For a heavy field the bound is no constraint: it "is satisfied trivially by the heavy field" (#14 §1), "trivially satisfied by a heavy X" (R7).

## The consequence for the momentum graviton X

The program's X is the massive spin-2 field of a Hassan–Rosen theory whose second frame is confined to a compact space ([constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)). Calc note [#8](/wiki/history/documents/debt-1-notes) states that the same symmetry that sorts the spin-2 eigenstates forces "equal effective Planck masses" for the two metrics (#8 §3), M_f = M_g; see [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity).

The worklog's item R7 names the tension: calc note #8 §3 "says reciprocity forces equal effective Planck masses (M_f = M_g), which rules out the M_f ≪ M_g escape". Its instruction for the manuscript was "v3: state this as an open consistency item, not as evaded." Version 3 of #14 did so: "The framework's reciprocity, acting as exchange of the two metrics, instead sets the two Planck masses equal, so the stability of a heavy spin-2 field at equal Planck masses is an open consistency condition (Sec. 5, item 7)" (#14 §1). Its §5 item 7 lists "instability of a heavy spin-2 field at equal Planck masses" among the internal exclusion conditions, and its §6 lists "the ghost-free landing of the mass mechanism and its cosmological stability at equal Planck masses" as conjectural.

The question assumes that X is heavy, as #14 and the worklog do. The [checkpoint](/wiki/history/documents/checkpoint) fixes no value for X's mass; it gives only M_X ∝ 2(β₁+β₂) (#11 §7.5; see flag 5 in `review/wiki-build-flags.md`).

The item appears only in #14 and the worklog; #11 §14 does not list it. The wiki keeps it as an open item on its own page, [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability). #14 itself was withdrawn after round 3 because its Kibble estimate of the monopole relic abundance had been normalized too low ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). That error does not bear on this item: the question concerns X, which stands.

## How the item entered the record

- **Round 2.** The referee's valid findings on #14 v2 included "bimetric cosmological-branch instability severity (mass hierarchy may evade — the analyses assume light second metric; early universe remains open; cite properly)" (HANDOFF §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).
- **The v3 worklog.** Item R7 was marked "ready, with a tension", with the evidence above. The worklog's reference list adds Akrami et al. and Higuchi as new references for v3, checked against the literature databases "unless noted" ('Verified references for v3'), and v3 added the stability question to exclusion item 7: "The bimetric instability at equal Planck masses is added to item 7" ('v3 as drafted (2026-10-19)').
- **Round 3.** The audit checked references [4]–[6] (Step 1), and ruling 12 accepted the over-generalization of [4] as a minor citation issue.

## Standard references

- #14's references [4]–[6], as listed above; #14's list is unmarked. The round-3 audit found that all 23 of #14's references resolve with matching bibliographic data (audit notes, Step 1).
- De Felice et al. (2014): named in the worklog as cited by Akrami et al., and not read.
- A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), arXiv:1512.00021: a review of bimetric theory, which the checkpoint cites as [22S] for a different statement (#11 §7.3; see [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)).

## Used by

- [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability) — the open consistency condition for X.
- [Partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity) — the field at the edge of the Higuchi bound.
- [The X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) — the open cosmological stability of a heavy X at equal Planck masses.

## Sources

- `notes/knot-dark-matter-standalone.md` §1, §5, §6, refs [4]–[6] — the literature summary, the open consistency condition, the exclusion condition and the conjectural status; the citations (manuscript withdrawn for an unrelated error: its Kibble estimate of the relic abundance had been normalized too low).
- `review/v3-worklog.md` 'Round-2 pending list', item R7 — the three limits on the heavy-spin-2 result, the tension with equal Planck masses, De Felice et al.
- `review/v3-worklog.md` 'Verified references for v3', 'v3 as drafted (2026-10-19)' — the new references; the addition to exclusion item 7.
- `review/round3/referee/audit-notes.md` Step 1 — the checks of #14's references [4], [5] and [6].
- `review/round3-adjudication.md` 'Rulings' 12 — the over-generalization of reference [4], accepted.
- `HANDOFF.md` §6 — the round-2 finding.
- `notes/debt1a-iv-beta-coefficients.md` §3 — equal effective Planck masses forced by reciprocity.
- `papers/broken-born-checkpoint-v2.md` §7.5, §14 — no value for X's mass; the open problems, which do not list this item.
- `review/wiki-build-flags.md` item 5 — M_X versus M_X² in #11 §7.5; awaiting Paul's ruling.
