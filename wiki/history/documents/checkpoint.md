---
title: "The checkpoint: #9 to #11 v2.2"
weight: 60
status: record
description: "The first consolidation (v1.0, #9) and the current reference (#11) through v2.0, v2.1 and v2.2: what each version changed, commit by commit, #11 section by section with the wiki's homes for each part, its internal inconsistencies and the flags that concern it."
sources:
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §1–§15"
  - "papers/broken-born-checkpoint-v2.md App. A"
  - "papers/broken-born-checkpoint-v2.md References"
  - "papers/broken-born-checkpoint-v2.md footer"
  - "notes/broken-born-program-v1.md"
  - "HANDOFF.md §3"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4-adjudication.md 'Revisions for v2 of the note'"
  - "verify/battery.py"
  - "review/wiki-build-flags.md items 1, 5, 6, 7, 9, 20, 23, 27, 28, 32, 36, 38, 39, 42, 43"
---

*The checkpoint is the program's paper-length statement of everything it has derived, predicted, retracted and left open, with every claim tagged by where it came from. Its first version, #9 ("The Broken-Born Program" v1.0), consolidated the [lab notebook](/wiki/history/documents/lab-notebook) and the calc notes into one document with a plain-language passage opening every section. Its successor, #11, is the current reference for the full program. Version 2.0 added a methodological preface with a machine-verification battery, sections on charge lattices and on the dark-sector candidates, a reference list and an audit of the founding ideas; version 2.1 recorded the outcome of review round 3, retiring the [soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) and putting the [dark-energy prediction](/wiki/predictions/dark-energy-drift) under pressure; version 2.2 recorded the [toy-model](/wiki/symmetry-breaking/toy-models) results. #11 is a working checkpoint, not to be submitted until its citations from memory have been checked against their sources.*

**Status:** Record — #11 v2.2 is rank 2 in the wiki's precedence order and "the current reference for the full program" (root `CLAUDE.md`); #9 is superseded by #11 and kept as the audit trail (`HANDOFF.md` §3: "v1.0 — superseded by #11"; #11 header: "Supersedes v2.1, v2.0 and v1.0"). #11's versions are in `git log -- papers/broken-born-checkpoint-v2.md`: v2.0 as imported (8d588f6, 2026-10-19), v2.1 (e1c1f67, 2026-10-19) and v2.2 (6ee74d0 and 6606734, 2026-10-19 and 20).

## What the checkpoint is

#11 is titled "The Broken-Born Program: A Working Checkpoint" and states its form in the header: "Every section opens with a plain-language passage (italic), followed by the technical record." Every claim carries a provenance tag, [D] derived in the program, [T] established literature, [P] postulate, [O] open or [V] machine-verified, and every reference a mark, [S] for "retrieved by live search during this project" or † for "cited from model memory — verify against the source before external use" ([provenance tags and citation marks](/wiki/method/provenance-tags)). Its footer gives the attribution, "conjecture and direction, P. R.; derivations, counterexamples, verification battery, and drafting, Claude (Anthropic)", and the condition on its use: "Working checkpoint — not for submission until the † audit (open item 10) completes" ([Open: the † literature battery](/wiki/method/literature-battery); [the collaboration](/wiki/method/collaboration)).

The wiki takes its top-level structure from #11: "The top level follows the program's argument as #11 builds it" (`wiki/CLAUDE.md`). Most pages cite #11 first, and where #11 and an older document differ, #11 governs, unless the root `CLAUDE.md` says otherwise ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## #9: "The Broken-Born Program", v1.0

The header: "Version 1.0 — consolidation of the full development arc. Each section opens with a plain-language passage, then the technical record. Provenance tags: [D] derived here, [T] established literature, [P] postulate, [O] open." #9 is undated; it follows the Debt-1 notes and precedes the first popular article in `HANDOFF.md` §3's creation order, and the handoff describes it as the "First paper-shaped consolidation; lay passage opening every section; tag system [D]/[T]/[P]/[O]". It was imported with the other files on 2026-10-19 and placed in `notes/` as superseded (commit 008c3ee).

Its sections are §0 "Two abstracts", §1 "The question", §2 "Postulates — including the one the mathematics rejected", §3 the kinematic core and the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), §4 the modular field, §5 "The second graviton and its mass (Debt 1: paid)", §6 "Conjugate matter and the gate (Debt 2: mechanism paid)", §7 "The death of momentum clumping (Debt 3: closed, negative)", §8 cosmology, §9 predictions and kill conditions, §10 open problems and §11 "Assessment" ([the three debts](/wiki/history/debts)). It cites literature without a reference list and asks that "All citations flagged [T — verify] should be checked against sources before any submission." Its provenance note reads "developed in dialogue; conjecture and direction by P. R.; derivations, counterexamples, and drafting by Claude (Anthropic)", without the verification battery that #11 adds.

Its assessment counted "at least two results that stand on their own regardless of its fate", the [symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner) and "the palindrome theorem cancelling the symmetric-bimetric vacuum energy", and said that "The word 'theory' awaits items 1–2 of §10". #11 revised both ([Assessment](/wiki/program/assessment#superseded-the-v1-assessment)).

## #11 v2.0: what it added

#11 v2.0 arrived in the repository with the import of 2026-10-19 (commit 8d588f6), subtitled "Spontaneously broken reciprocity, a massive momentum-space graviton, polarized charge lattices, and the dark-sector trilemma". The handoff lists what it added to v1.0: "Supersedes #1 and #9. Adds: methodological preface + 7-test machine-verification battery; charge-lattice §11; dark-sector trilemma §12; 25 references flagged † (memory — verify) vs [S] (live-searched); PM/Hossenfelder novelty downgrade; Appendix A supposition audit (11 items with fates)" (`HANDOFF.md` §3), PM being [partially massless](/wiki/gravity/spin-2-fields/partially-massless-gravity). In the wiki:

- the preface is §2, with Tier 1 checked by [the verification battery](/wiki/method/verification/battery) and the tiers on [claim tiers and selection bias](/wiki/method/claim-tiers);
- §11 is [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) and the rest of [electric–magnetic duality](/wiki/electric-magnetic-duality);
- the trilemma offered three dark-matter candidates, [χ particles](/wiki/dark-matter/candidates/chi-particles), [an X-condensate](/wiki/dark-matter/candidates/x-condensate) and "Conjugate knots", [topological solitons](/wiki/symmetry-breaking/topological-defects#topological-and-non-topological-solitons-t) of a p-local gauge sector ([dark-sector candidates](/wiki/dark-matter/candidates));
- the reference list ran [1]–[25] ([References](/wiki/references));
- the novelty downgrade is §7.4, "Literature position (updated by this session's search — honesty upgrade)" ([Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison));
- the audit is Appendix A ([founding suppositions and their fates](/wiki/program/founding-suppositions)).

In v2.0 the compatibility theorem was tagged "[D][V]", as derived in the program, and §9's plain-language passage promised "in §12, one loophole for individual knots". The predictions table gained row 11 ([history of the predictions table](/wiki/predictions/table-history#the-checkpoint-v20-eleven-rows)).

## v2.1: after round 3

v2.1 was committed on 2026-10-19 at 17:29 (e1c1f67), the same afternoon as the round-3 decisions ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). The current header lists its changes: "the soliton candidate is retired (§12); the compatibility theorem is re-attributed to the Born-geometry literature (§5); P4 is taken strictly (§4); §10 records DESI DR2's phantom crossing", DESI DR2 being Data Release 2 of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi). The footer adds: "v2.1 amendments: decisions delegated by P. R. to Claude; record in `review/round3-adjudication.md`."

The changes in detail:

- **Title and abstracts.** "the dark-sector trilemma" became "the dark-sector question". The plain abstract now ends that the topological candidate "was worked out, failed its own abundance arithmetic, and is retired, leaving particles or a condensate".
- **§2.** A caution: "a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review" ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **§4.** [P2′](/wiki/program/postulates/p2-prime) notes that "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]". P4 is "taken strictly since v2.1: no kinetic mixing between the sectors beyond what gravity induces, … ε ≲ 10⁻¹³ [27S]" ([P4](/wiki/program/postulates/p4-polarized-matter)).
- **§5.** The compatibility theorem becomes [T][V]: "It is the Born-geometry compatibility statement of Freidel, Leigh and Minic … The block proof and the machine check are this program's." The plain passage was rewritten to match ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)).
- **§10.** The paragraph "**Under pressure (v2.1):**" records DESI DR2's own statement of "a phantom crossing to w < −1 above redshifts z ≃ 0.4", and concludes: "The framework's strict w ≥ −1 therefore stands against the direct reading of the data" ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).
- **§11.1 and §12.** The candidacy of [conjugate monopoles](/wiki/electric-magnetic-duality/conjugate-monopoles) "as the dark matter itself is retired", and the trilemma becomes "two candidates, and the obituary of a third", with the obituary in the form what was claimed, how it was tested, why it failed, what survives ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Its [V] numbers are gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).
- **§13–§15 and Appendix A.** Rows 3, 4, 7 and 11 and the withdrawn list change; §14 items 8 and 9 lose the soliton items; §15 adds the obituary, the re-attribution and DR2 to the degeneration risks; Appendix A items 3–5 record the retirement.
- **References.** "[21] upgraded to [S]; [26]-[29] added, all INSPIRE-checked" (commit e1c1f67).

## v2.2: the toy-model results

v2.2 came in two commits. On 2026-10-19 at 22:29 (6ee74d0), §3 gained an attribution marked "(v2.2)", while the header still read 2.1: "the idea that a preferred polarization breaks Born duality is Freidel, Leigh and Minic's", with the program's addition stated as reading it "as *spontaneous* breaking, with η as the order parameter" ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)). The commit message: "Toy-derived amendments to secs. 10 and 14 wait for the round-4 review."

On 2026-10-20 at 18:54 (6606734), after the round-4 adjudication, the header became "Version 2.2 (checkpoint), amended 2026-10-20", with the change list "§3 credits Freidel–Leigh–Minic for 'broken Born duality'; P2′ (§4), §10 and §14 item 11 record the toy-model results." The three toy-model additions:

- **P2′'s refinement**: "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]", with the consequences that a definite polarization needs a [ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) and that breaking ρ is physical only once matter couples to the sign of K ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle); [the twisted element](/wiki/symmetry-breaking/twisted-element)).
- **§10's "Toy-model support (v2.2) [D][V]"**, which ends: "None of this tests the cosmology; it only shows the structure is consistent."
- **§14 item 11**, the toy Lagrangian, "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential", with three open ends ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)).

The same commit made the toy-model note v2 and applied the round-4 revisions ([review round 4](/wiki/method/review/round-4)), except the comparison with an exactly solved model that revision 4 asked for, which v2 says it has not carried out (flag 42 in `review/wiki-build-flags.md`). The root `CLAUDE.md` bullet "#11 is now v2.1" was not updated ([CLAUDE.md and the README](/wiki/history/documents/project-instructions); flag 38 in `review/wiki-build-flags.md`).

## #11 v2.2, section by section

| Section | What it holds | Where the wiki covers it |
| --- | --- | --- |
| §1 | two abstracts | [the research program](/wiki/program) |
| §2 | the methodological preface: tiers, the battery, the caution | [claim tiers](/wiki/method/claim-tiers); [the battery](/wiki/method/verification/battery) |
| §3 | the question, mandatory breaking, the attribution to Freidel–Leigh–Minic | [Born's question](/wiki/program/borns-question); [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking); [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality) |
| §4 | postulates P1, P2′, P3, P4, P5 | [postulates P1–P5](/wiki/program/postulates) |
| §5 | the split-quaternion algebra, the compatibility theorem, the nontriviality theorem | [Born geometry](/wiki/phase-space/born-geometry); [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) |
| §6 | the modular field Z = X + iY | [the modular field](/wiki/phase-space/modular-field) |
| §7 | the massive momentum graviton: the chain, the tuning test, the palindrome, the literature position, the spectrum, Born's answer | [the momentum graviton X](/wiki/gravity/momentum-graviton); [the tuning test](/wiki/gravity/tuning-test); [the palindromic branch](/wiki/gravity/palindromic-branch) |
| §8 | conjugate matter and the gate | [conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter) |
| §9 | the obituary of momentum clumping | [momentum clumping (Debt 3)](/wiki/dark-matter/momentum-clumping) |
| §10 | cosmology: the constraint, the dictionary, dark energy, the pressure from DR2, the toy-model support | [cosmology](/wiki/cosmology): [scale-factor duality](/wiki/cosmology/scale-factor-duality); [dark energy](/wiki/cosmology/dark-energy) |
| §11 | polarized charge lattices | [electric–magnetic duality](/wiki/electric-magnetic-duality) |
| §12 | the two candidates and the soliton obituary | [dark-sector candidates](/wiki/dark-matter/candidates), in [dark matter](/wiki/dark-matter) |
| §13 | predictions and kill conditions, rows 1–11 | [predictions and kill conditions](/wiki/predictions) |
| §14 | open problems 1–11 | [open problems and the queue](/wiki/status/open-problems) |
| §15 | the assessment | [assessment](/wiki/program/assessment) |
| App. A | the founding suppositions and their fates | [founding suppositions](/wiki/program/founding-suppositions) |
| References | [1]–[29], marked † or [S] | [references](/wiki/references) |

#9's sections map onto #11's as §0 → §1, §1 → §3, §2 → §4, §3 → §5, §4 → §6, §5 → §7, §6 → §8, §7 → §9, §8 → §10, §9 → §13, §10 → §14 and §11 → §15. #11's §2, §7.4, §11, §12, Appendix A and reference list have no counterpart in #9.

## Inconsistencies inside #11

Some statements in #11 disagree with others in the same document or overstate what the gate checks. The wiki records each where it arises and lists them on [conflicts between sources](/wiki/history/documents/source-conflicts):

- **§10's plain passage and its technical paragraph.** The italic passage still ends "The sky is voting now: DESI's hints of weakening dark energy are exactly the required drift", a sentence that stood in v2.0; the "Under pressure (v2.1)" paragraph below it reads the data the other way. The wiki follows the paragraph and the root `CLAUDE.md`.
- **The loophole.** §12 says the Debt-3 loophole "remains untested, but has no candidate"; §14 item 8 says "The soliton-spectrum and p-localization items are closed by the §12 obituary" ([Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).
- **"The empty set" or "measure zero".** §11.1 and Appendix A item 5 word P.R.'s correction differently ([conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)).
- **J or K.** P2′ calls J "the real structure"; §14 item 11 makes η = ωK the order parameter ([the order parameter](/wiki/symmetry-breaking/order-parameter)).
- **What the machine checks.** §2's "det H = 1 across the whole family" rests on a test of one random member, and §7.2's "provably outside the linear-in-eₙ span (T7)" on a numerical test of p₄ alone; §7.2's "the 66.58-vs-63.72 test of §2" points to a section that does not print the figures, which are in `HANDOFF.md` §5 and the battery's output (flag 36 in `review/wiki-build-flags.md`). The wiki tags the family-wide and nonlinear statements [D] ([the verification battery](/wiki/method/verification/battery)).
- **Undefined symbols.** §8 uses α̃, m_φ and F without defining them; the wiki takes them from #1 §3 and #9 §6 ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)).

## What the wiki flags

`review/wiki-build-flags.md` lists suspected errors in #11 or #9, quoted on the wiki's pages as written: item 1, the "discrete" polarizations of §5 (and #9 §3); item 5, "M_X ∝ 2(β₁+β₂)" in §7.5 (and #9 §5 item 6), where the source note has the squared mass ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)); item 6, §7.3's "by symmetry"; item 7, "The unique consistent structure" in §7.1; item 9, reference [24][S], which has no authors; item 20, reference [23]†, whose title and arXiv number belong to different papers; item 23, the identification of a·ã = 1 with the |Z| = 1 locus in §6 and §10; item 27, the sign of [τ's potential](/wiki/cosmology/dark-energy/tau-quintessence) V = V₀[1 + cos(τ/f)] in §10 (and #9 §8), against the turnaround it needs ([Open: the sign of V(τ)](/wiki/cosmology/dark-energy/potential-sign)); item 28, the formula 4π/e² beside the [magnetic coupling](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) ≈ 34 in §11.2; item 36, §7.2's pointer to §2 for the figures 66.58 and 63.72; item 39, §7.5's reciprocity parities, which hold for reciprocity as §7.3's frame exchange and not under §6's Z → −Z⁻¹ ([two actions of reciprocity](/wiki/gravity/momentum-graviton/spectrum-and-parity#two-actions-of-reciprocity)); and item 43, §10's [thawing corridor](/wiki/cosmology/dark-energy/thawing-and-freezing#where-the-classes-lie-in-the-wwₐ-plane) (and #9 §8), which lies in the region of the w₀–wₐ plane where DESI DR2's fits lie, a relation §10 does not state although it gives the corridor and DR2's crossing in one paragraph ([the corridor and DR2's crossing](/wiki/cosmology/dark-energy/cpl-parametrization#the-corridor-and-dr2s-crossing)). The flags' audit (2026-10-22) confirmed all of these except item 39, which depends on which action of reciprocity is meant. Item 32 is a lead, not a source error: the status of CMB-S4, the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#row-10s-probe-cmb-s4) experiment [row 10](/wiki/predictions/early-universe-step) names as a probe, is unchecked and belongs to the † battery. Item 38 concerns the root `CLAUDE.md`'s statement of #11's version (above).

## What the wiki does not copy

Some of #11's plain-language passages use phrasing the wiki's register excludes (`wiki/CLAUDE.md`, 'Voice'): physics that "plays favorites" (§1), a field that "wants" to be a second copy of gravity and "nature forbids identical twins of the graviton" (§7), and "one state, two ledgers" and "one event, two ledgers" (Appendix A items 2 and 7), with "the conjugate ledger" in §10. The wiki states the same content without attributing intentions to fields or nature, and writes "two descriptions" for the two ledgers ([the conjugate universe](/wiki/program/conjugate-universe)).

## Sources

- `papers/broken-born-checkpoint-v2.md` header — the version line and the v2.1 and v2.2 change lists; §1–§15, Appendix A and References — the sections in the table; footer — the provenance line and the submission condition. Its earlier versions are in the repository's history: commit 8d588f6 (v2.0 as imported), e1c1f67 (v2.1), 6ee74d0 and 6606734 (v2.2), with their commit messages.
- `notes/broken-born-program-v1.md` — #9's header, sections, assessment and provenance note
- `HANDOFF.md` §3 rows 9 and 11 — v1.0's standing and what v2.0 added
- `CLAUDE.md` 'Layout' — #11 as "the current reference for the full program" and #9 "superseded by #11"; 'Since the handoff' — the v2.1 changes
- `review/round3-adjudication.md` 'Decisions' — the decisions v2.1 records; `review/round4-adjudication.md` 'Revisions for v2 of the note' — the round behind v2.2
- `verify/battery.py` — the Tier-1 checks of §2
- `review/wiki-build-flags.md` items 1, 5, 6, 7, 9, 20, 23, 27, 28, 36, 39 and 43 — suspected errors in #11 and #9, with their audit verdicts; item 32 — a lead on row 10; item 38 — the root `CLAUDE.md`'s stale version of #11; item 42 — the round-4 revision that v2 did not carry out
