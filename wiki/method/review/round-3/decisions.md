---
title: "Round-3 decisions and lessons"
weight: 30
status: record
description: "Decision 1 strict sector separation, Decision 2 the soliton candidate retired (routes a, b and c), Decision 3 the √N floor dropped, Decision 4 the toy Lagrangian next; their execution the same day; and the two lessons, the blindness leak and independent anchors."
sources:
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/v3-worklog.md 'Round 3 outcome (2026-10-19)'"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md footer"
  - "review/round3/referee/audit-notes.md Step 1"
  - "notes/knot-dark-matter-standalone.md banner"
  - "verify/soliton_obituary.py"
  - "CLAUDE.md 'Since the handoff (2026-10-19)'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "CLAUDE.md 'Working with Paul'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §8"
  - "review/round4-preregistration.md"
  - "review/wiki-build-flags.md item 33"
---

*The round-3 decisions are the four choices that set the Broken-Born program's course after its third blind review failed the [soliton dark-matter manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary), recorded at the end of `review/round3-adjudication.md` together with the round's two lessons. Paul delegated the decisions on 2026-10-19, Claude made them, and Paul keeps the veto. Decision 1 took at face value the postulate that gauge forces do not cross between the two polarizations of matter, so that the hidden and visible photons mix no more than gravity makes them. Decision 2 retired the soliton candidate rather than keep it alive with a free [dilution factor](/wiki/cosmology/early-universe/relic-yield-and-dilution#entropy-dilution-t) or claim a published model as the program's own. Decision 3 dropped a queued calculation whose premise the review had inverted, and Decision 4 made the toy Lagrangian the next task, after a cleanup of the checkpoint. The lessons were to keep a review's forecast out of the commit subject, and to check numbers against anchors that do not come from the paper being checked.*

**Status:** Record — untagged; the decisions are in force. Each is carried out in a current document: Decision 1 in postulate P4 (#11 §4), Decision 2 in the obituary of #11 §12, Decision 3 in the root `CLAUDE.md` queue, and Decision 4 in #11 v2.1 and the toy-model note (#11 §14 item 11), which [review round 4](/wiki/method/review/round-4) examined. Both lessons are rules in the root `CLAUDE.md`, 'Method'.

## How the decisions were made

The round left decisions open for Paul. The v3 worklog closed by naming the main one: "This worklog is closed. The next step is Paul's decision on the soliton candidate." The adjudication records how it was settled: "Paul delegated these on 2026-10-19 ("You make the decisions for me and give rational"). Claude made them. Paul keeps the veto."

The delegation crosses the program's usual division of labour. The root `CLAUDE.md` gives the roles as "Paul — conjecture, direction, veto. Claude — derivations, counterexamples, drafting, verification", so direction is normally Paul's ([the collaboration](/wiki/method/collaboration#decisions-and-the-veto)). Paul's request asked for the reasoning with the decisions, and each decision states its reasons, which he can read before using the veto. The root `CLAUDE.md`'s working instruction points the same way: "Make the call and recommend; don't ask questions Paul can't answer." #11's footer marks the amendments that followed as "decisions delegated by P. R. to Claude; record in `review/round3-adjudication.md`", and the root `CLAUDE.md` points to the same place: "Reasons are in the adjudication's "Decisions" section."

## Decision 1: strict sector separation

> **Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry.

Two gauge forces that no particle feels jointly can still be linked by [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing), a term in the action that couples the field strength of one photon to that of the other with a small coefficient ε. Particles charged only under the hidden force then carry a small charge under ours, about ε times their hidden charge [T]. The program's postulate [P4](/wiki/program/postulates/p4-polarized-matter) says that "gauge forces do not cross polarizations". The question was how strictly to read it.

The reasons, as the adjudication gives them:

- "It is the program's own postulate P4 ("gauge forces do not cross polarizations") taken at face value."
- "The alternative rested on an unsupported coefficient. The dimension-5 "O(1) at the Planck scale" estimate (ruling 7) has no source. The sources generate that operator only from bi-charged states, which P4 forbids."
- "It costs nothing and closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector."

The alternative was #14 v3's estimate, ε ~ 10⁻⁷–10⁻⁶ from a Planck-suppressed operator, which ruling 7 found unsupported ([Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)). The three channels were findings of the review: a millicharged ψ, constrained by the supernova and [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#nucleosynthesis-limits-on-a-millicharged-ψ) limits the referee listed ([omitted constraints](/wiki/method/review/round-3/rulings#supernova-sn1987a-and-nucleosynthesis-limits)); a visible electric charge on the monopoles through [the Witten effect](/wiki/electric-magnetic-duality/monopoles/witten-effect) ([ruling 9](/wiki/method/review/round-3/rulings#ruling-9-the-witten-effect)); and the return of the hidden sector to our temperature ([re-thermalization](/wiki/method/review/round-3/rulings#re-thermalization-through-a-millicharge)).

The decision's two clauses come from the literature #14 had cited. Mixing generated by gravity alone vanishes if hidden charge conjugation is an exact symmetry, and otherwise first appears at six loops, with ε ≲ 10⁻¹³ as #11 writes it (Gherghetta, Kersten, Olive and Pospelov [27S]). Quantum gravity is believed to admit no exact global symmetry, so the zero needs charge conjugation to be part of the gauge group [T] ([gauged, not global](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#b-gauged-not-global)). #11 v2.1 wrote the reading into P4:

> [P; taken strictly since v2.1: no kinetic mixing between the sectors beyond what gravity induces, which vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³ [27S].]

The root `CLAUDE.md`: "Strict sector separation (P4 at face value) is in force." The decision fixes how a postulate is read: P4 is tagged [P], and its strict reading is a choice, not a derivation ([why it was adopted](/wiki/program/postulates/p4-polarized-matter#why-it-was-adopted-round-3-decision-1)).

### A reading left unresolved: ceiling or floor

The round-3 referee's reading of the gravity-only figure differs from the decision's. It notes that Gherghetta et al. present 10⁻¹³ as a floor, the "minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking", "consistent with "<~" only in the sense "up to"" (audit notes, Step 1). #11 and the decision write ε ≲ 10⁻¹³. No document reconciles the two readings, and #11's wording stands as the current statement ([an unresolved reading](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#an-unresolved-reading-ceiling-or-floor); [conflicts between sources](/wiki/history/documents/source-conflicts#kinetic-mixing)).

## Decision 2: the soliton candidate retired

> **The soliton candidate: retired as a program-native proposal (route c).** The surviving version is noted as prior art (route a). Rejected route (b): superheavy plus a named dilution.

Checkpoint v2.0 had offered [three answers](/wiki/dark-matter/candidates) to the question of what dark matter is, and the adjudication says why the third had earned its row: "The row earned its place in the checkpoint's trilemma on two claims: topology makes it stable for free, and the mass came out of the abundance with no free dilution. Round 3 removed the second." The review's verdict had left two ways to keep a monopole candidate: "a superheavy monopole that needs a named dilution mechanism, or a model at v ≲ 100 PeV that already exists in the literature" ([the verdict](/wiki/method/review/round-3/rulings#the-verdict)). The decision took each in turn.

**Route (b), superheavy plus a named dilution: rejected.** A period after the monopoles form in which the universe gains entropy, such as the decay of a field that briefly dominated its energy, dilutes their number per unit entropy and so their final density [T] ([inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)). The adjudication:

> Route (b) restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction, and the program does not trade falsifiability for survival.

The factor of 10³–10⁴ is the overproduction at minimum production, 2.1×10³–1.2×10⁴ at the benchmark of 3×10¹³ GeV; "far more" refers to realistic production, which only adds monopoles ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). A dilution factor chosen to fit would make the mass an output of the fit; the page on Lakatos's methodology reads such a factor as an ad hoc adjustment (the wiki's reading; [the declined rescue](/wiki/method/lakatosian-methodology#the-declined-rescue-of-the-soliton-candidate)).

**Route (a), the low-scale model: noted as prior art, not claimed.**

> Route (a), v ≲ 100 PeV, works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model. Nothing in it depends on Born reciprocity (the referee and the pre-registration agree), so claiming it would add no testable content and would misattribute it.

The pre-registration had predicted the referee would say "the dark-matter proposal stands or falls independently of the phase-space framework", and the referee had said so ([the round-3 pre-registration](/wiki/method/review/round-3/preregistration); [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

**Route (c), retirement: chosen.** "The program's precedent is the Debt 3 obituary: a dead claim is reported prominently and stays dead." The precedent is the death of momentum clumping, the program's founding image, in the Debt-3 calculations ([Obituary: velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image); [negative results and dead claims](/wiki/method/negative-results)).

The consequence: "the trilemma becomes two program-native candidates (gated χ particles; the X-condensate), plus the remark that the framework is compatible with known PeV-scale topological dark matter" ([χ particles](/wiki/dark-matter/candidates/chi-particles); [the X-condensate](/wiki/dark-matter/candidates/x-condensate)). #11 §12 records the verdict: "Retired as a program-native candidate. The framework is compatible with the prior-art PeV-scale scenario and adds nothing testable to it." The root `CLAUDE.md`: "The superheavy soliton candidate in HANDOFF §2 is **dead** as a program-native proposal. The framework is merely compatible with known PeV-scale topological dark matter (prior art)." The candidate's obituary is [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary), and it is listed in [the graveyard](/wiki/status/graveyard).

## Decision 3: the √N floor dropped

The handoff's queue had a calculation waiting for the candidate, item 3: "√N-floor freeze-out estimate (open item #2) — resolves "Sommerfeld probably fatal" into a number; Preskill-style kinetic calculation; decides whether the soliton candidate's abundance window exists" (`HANDOFF.md` §8). Its open item 2 stated the idea: [Kibble production](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) "leaves a net-charge residue annihilation cannot remove", a chat-only argument that would bound "the relic abundance between Kibble ceiling and √N floor" (§2). The decision:

> **HANDOFF §8 queue item 3 (the "√N floor"): dropped.**
> - Its premise, Kibble as a ceiling, is inverted (ruling 3).
> - Under decision 2 it has no candidate left to serve.

Ruling 3 had established that one monopole per Hubble volume is the least a transition produces, so the Kibble count the argument treated as a ceiling is a floor. Ruling 10 bears on the same item: the strong-coupling annihilation the estimate was to address is, in the ruling's words, "Preskill's Dirac case, already done for hidden sectors". The root `CLAUDE.md`: "HANDOFF §8 queue item 3 is dropped." ([Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor))

## Decision 4: the toy Lagrangian next

> **What comes next: the toy Lagrangian (HANDOFF §8 item 4), after one short cleanup.**
> - Every referee across three rounds converges on "the framework does no work". The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes.
> - Candidate-level work is downstream of it.

The toy Lagrangian is an explicit action in which reciprocity is a genuine symmetry, spontaneously broken ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). The referees' shared objection is that nothing numerical in the program's proposals depends on its [hard core](/wiki/program/hard-core), spontaneously broken [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity); an action in which the breaking happens is the item the decision names as able to change that ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)).

The cleanup came first, "so the current reference stops asserting what round 3 killed: amend checkpoint #11 with the soliton obituary (§11–§15), check the Freidel–Leigh–Minic prior art and re-tag the compatibility theorem if confirmed, and give §10 the DESI DR2 phantom-crossing nuance (ruling 11)". DESI DR2 is Data Release 2 of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi). #11 v2.1, the same day, lists the changes "after the round-3 review": "the soliton candidate is retired (§12); the compatibility theorem is re-attributed to the Born-geometry literature (§5); P4 is taken strictly (§4); §10 records DESI DR2's phantom crossing". It also added to §2 "A caution added in v2.1: a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review" ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem#attribution-history); [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

The toy Lagrangian followed. The root `CLAUDE.md` records it as "done to the referees' wording", in `papers/reciprocity-toy-models.md`, and #11 §14 item 11 calls the criterion "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential", with [a Monte Carlo with H dynamical](/wiki/symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo), a [derivation of the potential](/wiki/symmetry-breaking/rho-preserving-potential) and the [stronger form of matter locality](/wiki/symmetry-breaking/strong-locality) still open [O] ([toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models)). Round 4 reviewed the note ([review round 4](/wiki/method/review/round-4)).

## Executed the same day

The adjudication lists what was done on 2026-10-19:

- "v3 moved to `notes/` with a withdrawal banner." The banner opens: "**Withdrawn (2026-10-19) after failing round-3 review (verdict C). Kept as the audit trail; not for circulation.**" The manuscript is `notes/knot-dark-matter-standalone.md`.
- The script that had checked v3's claims, `knot_numbers.py`, "was replaced by `verify/soliton_obituary.py`, which checks every number this record quotes, with independent anchors. The v3 checks are in history at 96f58da." The old script no longer exists in the working tree. Flag 33 in `review/wiki-build-flags.md` notes that the new script does not check every number the record quotes: the referee's numbers in rulings 3 and 4, ruling 6's figure and the surviving benchmark arithmetic are not among its checks ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).
- "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything."

The last point applies a rule of [the gate](/wiki/method/verification/the-gate) to a withdrawal. The root `CLAUDE.md` forbids weakening a check to make it pass; the adjudication's argument is that retiring the checks of a withdrawn paper is not that, since the gate tests what current documents claim. The repository's history dates the steps: the decisions were committed the same day (5b6efaa), and #11 v2.1 followed (e1c1f67) ([the timeline](/wiki/history/timeline)).

## The lessons

The adjudication's 'Lessons (now in CLAUDE.md)' records two.

### Lesson 1: keep the forecast out of the commit subject

> Keep the prediction out of the pre-registration commit subject. The auditor's auto-attached git status showed it. The auditor says it did not use it, and its verdict differed from the prediction, which argues against anchoring. But the round was less blind than intended.

The forecast had been committed before the referee was dispatched, as the rule requires, but the commit's subject line stated it, and the harness that launched the referee attached a summary of recent commits to its context ([the leak](/wiki/method/review/round-3/preregistration#the-leak)). The rule in the root `CLAUDE.md` now reads: "Pre-register the expected verdict and weakest link before each review round. Keep the prediction out of the commit subject: subagents see recent commit subjects in their git-status context, and round 3's auditor saw it." The next pre-registration applied it: "Per the round-3 lesson, the commit subject does not state the prediction" (`review/round4-preregistration.md`; [pre-registration](/wiki/method/review/pre-registration)).

### Lesson 2: anchors independent of the paper

> An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume.

An anchor is a check of a script against a value fixed outside the work being checked, such as a textbook identity or a published number, run before the script computes anything new. A check that reproduces the paper's own number confirms only that the script and the paper agree, which they will if both contain the same mistake. The two replacement anchors are the coefficient in the [radiation-era](/wiki/cosmology/early-universe/radiation-era) expansion rate, H = 1.66 √g\* T²/M_Pl, and the published normalization of one defect per Hubble volume, which the gate takes from Gangui (astro-ph/0110285) ([the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization#why-the-manuscripts-own-check-missed-it)). The gate's soliton script now runs four anchors before any of the record's numbers; from the current run:

```text
== Anchors
PASS  Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl
PASS  one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)  [p = 104.31]
PASS  freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)
PASS  Delta N_eff: one extra neutrino species at T_nu gives 1
```

The rule in the root `CLAUDE.md`: "A verification check confirms arithmetic, not the model. An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular. Round 3 caught a wrong Kibble normalization that a circular anchor had passed." The lesson is the program's response to ruling 13, "The code checked the arithmetic of a wrong model" ([independent anchors](/wiki/method/verification/independent-anchors); [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

## Where the decisions stand

| Decision | Recorded in | The root `CLAUDE.md` |
| --- | --- | --- |
| 1, strict sector separation | #11 §4, P4 | "Strict sector separation (P4 at face value) is in force." |
| 2, the soliton candidate retired | #11 §12 | "**dead** as a program-native proposal" |
| 3, the √N floor dropped | the queue | "HANDOFF §8 queue item 3 is dropped." |
| 4, the toy Lagrangian next | #11 §14 item 11; `papers/reciprocity-toy-models.md` | "done to the referees' wording" |

The queue now runs, in the root `CLAUDE.md`'s order, through the remaining handoff items 5–7 and an optional round-5 review of the toy note ([open problems and the queue](/wiki/status/open-problems)).

## Sources

- `review/round3-adjudication.md` 'Decisions' — the delegation, Decisions 1–4 with their reasons, routes (a)–(c) and the same-day execution; 'Lessons (now in CLAUDE.md)' — the two lessons; 'Verdict' — the two routes; 'Rulings' — rulings 2, 3, 7, 9, 10, 11 and 13 as the decisions cite them
- `CLAUDE.md` 'Since the handoff (2026-10-19)' — the decisions in force and the queue; 'Method (HANDOFF §5)' — both lessons as rules; 'Working with Paul' — the roles and "Make the call and recommend"
- `papers/broken-born-checkpoint-v2.md` header — the v2.1 changes; §2 — the caution added in v2.1; §4 — P4 strict; §12 — the obituary and verdict; §14 item 11 — the toy Lagrangian; footer — "decisions delegated by P. R. to Claude"
- `review/round3/referee/audit-notes.md` Step 1 — the referee's reading of Gherghetta et al.'s 10⁻¹³ as a floor
- `review/v3-worklog.md` 'Round 3 outcome (2026-10-19)' — the decision left to Paul
- `HANDOFF.md` §2 — open item 2, the √N floor; §8 — queue items 3 and 4
- `notes/knot-dark-matter-standalone.md` banner — the withdrawal
- `verify/soliton_obituary.py` — the anchors in the current run
- `review/round4-preregistration.md` — lesson 1 applied
- `review/wiki-build-flags.md` item 33 — the soliton script's coverage
