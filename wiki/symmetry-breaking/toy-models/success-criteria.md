---
title: "Success criteria S0–S5 and the pre-registered predictions"
weight: 20
status: method
description: "The six criteria fixed before construction (the letter, S0–S3; the spirit, S4–S5), the forecasts written with them, the S0 prior-art survey, the scorecards, the self-scored assessment and the unpredicted findings."
sources:
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Plan'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Chunk 4: S5'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §6"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Revisions'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
---

*The success criteria are six pass-or-fail tests, S0 to S5, written down on 19 October 2026 before either toy model was built, together with a forecast of how each would come out. Four of them encode the referees' literal demand: prior work is cited, the action is symmetric, the symmetry permutes the vacua, and an [order parameter](/wiki/symmetry-breaking/order-parameter) distinguishes them. Two encode the deeper objection that [the framework does no work](/wiki/program/framework-does-no-work): the breaking must survive quantum fluctuations, and it must make matter's interactions local in position. Fixing the tests first means the results are judged by standards chosen before the results were known, as the program's pre-registered forecasts do for its review rounds. The worklog scored all four forecasts as hits, before the round-4 review narrowed several of the results that the scoring relied on.*

**Status:** Method — the criteria carry no tags; the prior-art survey's citations are [S] ("every citation retrieved [S], nothing from memory"); written down and self-scored in `notes/toy-lagrangian.md`, before [review round 4](/wiki/method/review/round-4).

## Why the criteria were fixed first

The program pre-registers its expected verdict and weakest link before each review round, so that a confident forecast that fails is visible as a failure ([pre-registration](/wiki/method/review/pre-registration); root `CLAUDE.md`, 'Method'). The toy-Lagrangian worklog applied the same rule to a construction. Its heading reads "Success criteria (fixed 2026-10-19, before any construction)", followed by "Predictions (written before construction)". The commit that fixed them, "Toy Lagrangian: fix success criteria and predictions before construction" (d9e61f0), precedes the first results commit, "Toy Lagrangian chunk 1: coset baseline meets S1-S3 classically" (0e0f51e), in the repository's history.

The demand being answered was [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion), an explicit action in which [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ, the exchange of position and momentum, is a genuine symmetry that the vacuum breaks. The worklog split it in two: "The referees' wording (rounds 1–2): 'an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η the order parameter'. Round 3 adds that the framework does no work. So the criteria come in two tiers. The first tier is the referees' letter; the second is what would answer round 3." ('Success criteria'; [the 'framework does no work' critique](/wiki/program/framework-does-no-work)).

## Tier 1: the letter

- **S0 — prior art.** "Establish what already exists before claiming anything. Each element of the toy is either new or cited. (Lesson of the compatibility theorem, which turned out to be Freidel–Leigh–Minic's.)" The [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) had been treated as the program's own result until a literature check credited it to Freidel, Leigh and Minic; S0 makes the check come first.
- **S1 — symmetry of an action.** "An explicit action S[fields] on which ρ acts as a symmetry: S is invariant, not merely related to its image by a unitary equivalence. Invariance is verified symbolically." This is the referees' central point: ordinarily ρ is a change of description, implemented by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform), not a symmetry of any action ([unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence)).
- **S2 — ρ-related degenerate vacua.** "The minima of S form a set on which ρ acts without fixed points: no vacuum is ρ-invariant, and ρ maps each vacuum to another one. Verified." This is the classical content of [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking).
- **S3 — η as order parameter.** "A local operator built from η (equivalently the real structure K, with η = ωK) has a nonzero expectation value in each vacuum and is odd under ρ. Verified." ([the order parameter](/wiki/symmetry-breaking/order-parameter)).

## Tier 2: the spirit

**S4 — quantum stability.** "The breaking survives quantum fluctuations in the stated dimension."

- "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry, so the toy starts in 1+1."
- "In 1+1, a discrete symmetry can break (as in the 2D Ising model). A continuous compact one cannot (Coleman–Mermin–Wagner), though there is a claimed exception for non-amenable groups, to be checked."
- "Pass requires a citation-backed argument, and preferably a lattice simulation showing the order parameter stays nonzero."

The criterion separates classical breaking, a property of the minima of an action, from breaking in the quantum theory, where fluctuations can restore the symmetry. In quantum mechanics a particle in a double well tunnels between the minima, and the ground state is symmetric [T]. In two dimensions the theorem of Mermin, Wagner and Coleman rules out ordering of a compact continuous symmetry, while a discrete one can order ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). The "non-amenable" exception concerns non-compact symmetry groups; the prior-art survey found it in hyperbolic sigma models, whose non-compact symmetry breaks even in two dimensions ([coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models)).

**S5 — the vacuum choice has a consequence for matter.**

- "Matter coupled to the order parameter through ρ-symmetric couplings acquires, in the selected vacuum, interactions local in the selected Lagrangian (x) and nonlocal in its complement (p). In the ρ-image vacuum it is the other way round."
- "This is the analogue of a Yukawa coupling giving masses through a vacuum expectation value. It is the content of the program's claim that 'forces fade with distance, never with velocity difference' because the vacuum is polarized."
- "Pass requires an explicit computation, e.g. of a two-point function or an effective interaction, showing the anisotropy."

S5 is the answer to [round 3](/wiki/method/review/round-3): a vacuum choice that changes nothing in matter's interactions does no work. In the standard model the Higgs field's vacuum value gives fermions their masses, but only because [Yukawa couplings](/wiki/gravity/spin-2-fields/yukawa-forces#a-name-collision-the-yukawa-coupling) link the fermions to the Higgs field [T] ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)); S5 asks for the analogous link between the polarization and locality.

## The forecasts

Written with the criteria, before construction ('Predictions'):

- "**S1–S3 will pass easily.** A coset sigma model on the space of compatible (H, K) pairs does it classically, which is close to a construction by definition. Expect S0 to find it, or something close, in the Born-geometry literature."
- "**S4 will pass only for a discrete reduction** (the symmetry group cut down to the group generated by ρ) or via the non-amenability exception. The continuous U(1) of phase-space rotations that contains ρ would be restored in 1+1."
- "**S5 is the real test, and I expect it not to pass at the first attempt.** The likely outcome is that locality has to be defined relative to K by hand." The forecast named one route that might do better, "a field theory on phase space whose own vacuum breaks x ↔ p, with no separate K field", and its "Recalled prior art for that route (†, unverified): Langmann–Szabo duality and the Grosse–Wulkenhaar model at its self-dual point." Here † is the citation mark, a reference recalled from model memory; the prior-art survey then retrieved both by live search [S] ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)).
- "**If S1–S4 pass and S5 fails,**" then "acceptance criterion 1 as the referees worded it is too weak to answer 'the framework does no work'".

The plan that followed had three steps: an S0 survey by a literature subagent, "with nothing from memory"; a baseline coset model "checked against S1–S3 in sympy"; and a choice of route for S4–S5 "from what step 1 finds" ('Plan').

## S0: the prior-art survey

The survey ran on 19 October 2026: "literature subagent, 2026-10-19; every citation retrieved [S], nothing from memory" ('Chunk 1 results').

**The result.** "**Result: no existing action has Born reciprocity exactly symmetric and spontaneously broken with η or K as order parameter.** Zero phrase hits on INSPIRE full text and arXiv abstracts. INSPIRE's coverage is incomplete, so this is evidence of absence, not proof."

**The ingredients, which exist separately:**

- **The idea**, Freidel–Leigh–Minic: they make both η and the related structure J dynamical and tie a fixed η to locality, but "write no potential and do no symmetry-breaking analysis, and call Born's breaking kinematical, not spontaneous"; "**They have priority on the idea and must be cited.**" [#11](/wiki/history/documents/checkpoint) v2.2 now credits them in §3 ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)).
- **An interacting action exactly invariant under x ↔ p**: the Grosse–Wulkenhaar model at Ω = 1, with an all-orders vanishing β-function, under Langmann and Szabo's duality. Its vacua had been found, but "**Nobody has asked whether they break the duality.** Stripe phases in this literature break translations, not x ↔ p." This became [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar).
- **Non-compact symmetries can break in low dimension**: Niedermaier–Seiler and Duncan–Niedermaier–Seiler, "SO(1,N) broken in D ≥ 2, evading Mermin–Wagner".
- **Related, not the same**: Born sigma models choose the polarization by gauging (Marotta–Szabo); in [double field theory](/wiki/phase-space/born-geometry/double-field-theory) with spontaneously broken O(D,D), "there H is the order parameter, with η fixed" (Angus–Kim–Park); and a contraction rather than a breaking (Govaerts–Jarvis–Morgan–Low).
- **Bearing on S5**: in Langmann and Szabo's work, "locality in x arises only at the singular θ → 0 limit, not from a vacuum."

**What round 4 added.** The referee found prior work missing from the note's first version, and the adjudication accepted it "as citations and reframing": "Langmann–Szabo–Zarembo exact solution (hep-th/0308043); Smolin 2007.05957; Marotta–Szabo; Fosco–Moreno (0710.0818); GW 0401128 ('manifest' in the matrix base); Royer (parity-operator form of Weyl symbols)" ('Rulings'; GW is Grosse–Wulkenhaar; Royer's form is on [the Wigner function and Weyl symbols](/wiki/phase-space/reciprocity/wigner-function)). On Smolin: "Smolin breaks a triality *down to* Born duality, leaving it unbroken, so it does not contradict 'no model breaks ρ itself'. It still has to be cited." Version 2 states the outcome as "The idea has been stated before, but we found no explicit model of ρ itself being spontaneously broken" (Abstract), and its §1 sorts the prior work by topic. A second survey of the same kind, on the dynamical selection of a section in double field theory, ran for S5 in chunk 4 ([the section condition](/wiki/symmetry-breaking/section-condition)).

## How each criterion came out

The worklog kept a scorecard after each chunk. The last full one, after chunk 3 ('Chunk 3 results'):

| Criterion | Status |
|---|---|
| S0 | Done |
| S1–S3 | Pass (both toys) |
| S4 | Pass for coset + τ potential; fail for both exactly self-dual versions in 1+1 / at fixed μ² |
| S5 | Open |

The "τ potential" in the S4 row is the [naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), now dead (below). Chunk 4 then settled S5: "**Weak form: passes [V].** A ρ-covariant coupling of matter to K makes interactions local in L+ in one vacuum and in L− in the other." "**Strong form (locality forced, not chosen): not achieved.** It is also open in the literature." ('Chunk 4: S5').

What each line rests on now, after round 4:

- **S1–S3.** In [model I](/wiki/symmetry-breaking/toy-models/coset-model), an action invariant under [Sp(2, ℝ)](/wiki/phase-space/reciprocity/symplectic-form), vacua that ρ maps to one another, and O = K₁₁ as order parameter ([action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries); [vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). In model II, the duality as a symmetry of the complex field, a circle of vacua it moves, and the polarization Δ(β) ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields); [complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). Round 4 added that model I's vacuum keeps a twisted element ρ∘(K → −K), so its breaking of ρ is physical only once a coupling odd in K is present ([the twisted element](/wiki/symmetry-breaking/twisted-element)). The S1–S3 checks are gated in `verify/toy_coset.py` for model I and `verify/toy_gw.py` for model II ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).
- **S4.** The "τ potential" of the chunk-3 pass is the [naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), unbounded below once H is dynamical and now dead. Version 2 restates the pass with [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), as an ordered ℤ₂ phase in [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) only ([the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)). The lattice simulation is gated in `verify/toy_s4.py`, and V_b's stability with H dynamical in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). Model II fails S4 ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)). The non-amenability route was "not needed, not tested".
- **S5.** The weak form passes with the coupling the worklog called "a ρ-covariant coupling of matter to K"; the worklog's [V] for it rests on `verify/toy_s5.py`, which the gate runs ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). Round 4 found that the coupling needs H as well as K (finding F5), and version 2 calls it "a coupling built from (H, K)", which "is covariant under the SO(2) fixing H = 1, not under Sp(2,ℝ)" (§5; [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)). The strong form is open ([Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality)).

## Scoring the forecasts

The worklog's assessment, written after chunk 4 and before round 4 ('Assessment against the predictions'):

| Prediction | Outcome | Score |
|---|---|---|
| S1–S3 pass easily | Pass in both toys, close to by construction | Hit |
| S4 needs a discrete reduction or non-amenability | Coset passes only with a ρ-preserving τ-type potential (Ising class, MC). The [Grosse–Wulkenhaar] route fails S4 outright: zero mode, no stiffness. Non-amenability not needed, not tested | Hit |
| S5 not passed at first attempt; locality defined relative to K by hand | Weak form only; the strong form is open here and in the literature | Hit |
| If S1–S4 pass and S5 fails, the referees' criterion 1 is too weak to answer "the framework does no work" | Criterion 1 as worded is now met (coset + τ potential). The round-3 critique is only partly answered | Hit |

(MC is Monte Carlo; the worklog's "GW" is written out.) The scoring is the author's own. Two outcomes it relies on were later revised: the S4 pass used the [naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), and "Ising class" became "ordered ℤ₂ phase" for the frozen-H reduction (round-4 revision 1). The worklog's verdict on criterion 1 is superseded for the same reasons ([the worklog's first verdict](/wiki/symmetry-breaking/toy-models/acceptance-criterion#superseded-the-worklogs-first-verdict)). The first forecast also expected S0 to find the coset construction "or something close" in the Born-geometry literature; the survey found no such action, only related constructions such as Marotta and Szabo's Born sigma models, and the table does not score that part separately.

## Findings that were not predicted

The assessment lists three ('Assessment against the predictions'; on the first, see flag 10 in `review/wiki-build-flags.md`):

1. "At every self-dual point, ρ sits inside a continuous U(1). The polarization is therefore a Goldstone angle; in the coset toy it is Λ(1), the checkpoint's τ. This is structural support for §10." Λ(1) is [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian), and τ the program's dark-energy field ([τ quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). Round 4 restricted the Goldstone-angle reading to model I and the complex model II ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).
2. "The self-dual complex Grosse–Wulkenhaar vacua break the Langmann–Szabo duality classically, as a cos β polarization (new as far as the S0 search found). The breaking does not survive quantization." ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)).
3. "In 1+1, 'only ω rigid' is not enough for a definite polarization. A ρ-preserving potential on the polarization circle is required. In 3+1 the continuous breaking is allowed, and §10's potential supplies the explicit breaking anyway." ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). The 3+1 remark was not computed, and version 2 covers 1+1 with d = 1 only.

## Where the criteria are used

- [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion): the demand the criteria encode, and #11's verdict on it.
- [Model I: the coset sigma model](/wiki/symmetry-breaking/toy-models/coset-model) and [Model II: the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar): each page cites the criterion it tests.
- [Review round 4](/wiki/method/review/round-4): the blind review that graded the results and narrowed the scoring.
- [The toy-model scripts](/wiki/method/verification/toy-model-scripts): the gated checks of criteria S1–S5.

## Sources

- `notes/toy-lagrangian.md` 'Success criteria' — the six criteria, quoted above
- `notes/toy-lagrangian.md` 'Predictions', 'Plan' — the four forecasts and the one recalled citation; the plan
- `notes/toy-lagrangian.md` 'Chunk 1 results' — the S0 prior-art survey [S]
- `notes/toy-lagrangian.md` 'Chunk 2 results', 'Chunk 3 results', 'Chunk 4: S5' — the scorecards and the S5 conclusion
- `notes/toy-lagrangian.md` 'Assessment against the predictions' — the scoring and the unpredicted findings
- `papers/reciprocity-toy-models.md` §1, §5, §6, Abstract — the prior work, the (H, K)-built coupling and the scope as version 2 states them
- `review/round4-adjudication.md` 'Rulings', 'Revisions' — the omitted prior work added in round 4; "ordered ℤ₂ phase"
- `CLAUDE.md` 'Method (HANDOFF §5)' — the pre-registration rule
- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py` — the gated checks behind the S1–S5 outcomes
