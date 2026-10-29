---
title: "Claims that stand"
weight: 20
status: record
description: "Every program claim that currently stands, grouped by section, one line each with its tags as the sources give them and what verifies it — a gated script, a review round, or derivation, postulate and citation alone — with the claims under pressure marked."
sources:
  - "notes/velocity-gated-gravity.md §2"
  - "notes/velocity-gated-gravity.md §3"
  - "notes/velocity-gated-gravity.md §9"
  - "notes/gate-mechanism.md §5"
  - "verify/velocity_gated_gravity.py"
  - "verify/gate_mechanism.py"
  - "review/wiki-build-flags.md items 16, 55, 56, 58"
  - "CLAUDE.md 'Since the handoff'"
  - "papers/phase-space-diameter.md §3"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §7"
  - "papers/phase-space-diameter.md §8"
  - "papers/phase-space-diameter.md §9"
  - "review/round5-adjudication.md 'Verdict'"
  - "review/round5-adjudication.md 'Rulings'"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "verify/phase_space_diameter.py"
  - "papers/broken-born-checkpoint-v2.md §2–§15"
  - "papers/broken-born-checkpoint-v2.md App. A"
  - "papers/reciprocity-toy-models.md §2–§6"
  - "papers/conjugate-special-relativity.md §1–§7"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4/referee/audit-notes.md Step 2"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "HANDOFF.md §2"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "notes/geometric-core.md §C, §E"
  - "notes/x-classification.md §1–§4"
  - "notes/tuning-test.md §2–§4"
  - "notes/beta-coefficients.md §1–§3"
  - "notes/stream-stability.md 'Corollary (the classicality theorem)'"
  - "notes/wave-island.md 'The rate [D, heuristic coefficients]'"
  - "notes/broken-born-theory.md §2, §4, §5.1, §6, §7"
  - "notes/broken-born-program-v1.md §7"
  - "verify/battery.py"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
  - "verify/soliton_obituary.py"
  - "scripts/check.sh"
  - "review/wiki-build-flags.md items 16, 19, 20, 23, 27, 29, 30, 39, 43"
  - "notes/closed-universe.md §2–§8"
  - "verify/closed_universe.py"
  - "review/wiki-build-flags.md items 27 (addendum), 45, 46, 47, 48, 49, 51, 52, 53"
---

*This register lists the Comatter program's claims that currently stand: postulates, derived results and predictions that no calculation, review or observation has killed. Each line gives the claim, the tags its sources attach and what verifies it, grouped by the sections of the wiki. Standing is not the same as confirmed: most of these claims are untested by experiment, a machine check confirms the algebra but not whether the algebra describes nature, and the dark-energy sector is under pressure from current data.*

**Status:** Record, a register current to 2026-10-28 — each line carries the tags its page gives, copied from the sources; the register adds none and upgrades none — machine checks are the ten scripts in `verify/`, run by the gate `scripts/check.sh`, and a line with no script rests on derivation [D], postulate [P] or the literature [T]. Under pressure, in the root `CLAUDE.md`'s words: "The dark-energy sector is under real pressure ahead of DR3" (Data Release 3).

## How to read the tables

- **Claim** links the claim's page and states the claim in brief, in the order of the wiki's sections. Established literature results, such as [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), are not program claims and are not listed; neither are open problems, which are in [open problems and the queue](/wiki/status/open-problems).
- **Tags** are the [provenance tags](/wiki/method/provenance-tags) the page's status line gives, as its sources attach them: [D] derived in the program, [T] literature, [P] postulate, [O] open, [V] machine-verified; † marks a citation from memory and [S] one found by live search. A dash-style tag such as [D — structural] is the source's own qualifier.
- **What verifies it** names a script in `verify/` run by [the gate](/wiki/method/verification/the-gate), a [blind review](/wiki/method/review) round that re-derived the claim, or *not machine-checked* where the claim rests on its derivation, its postulate or its citations. #11 §2 sets the limit of a script: "a verification script confirms arithmetic, not the model it encodes".

## What the machine checks cover

- `verify/battery.py`, [the verification battery](/wiki/method/verification/battery), tests T1–T7, of which #11 §2 records "All seven passed [V]": the compatibility theorem (T1), the modular parametrization (T2), the misalignment blocks (T3), the failures of the metric tier (T4 and T7), and the integer identity behind V(1) = 2T with its linearization coefficients (T5 and T6).
- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py` and `verify/toy_s5.py`, [the toy-model scripts](/wiki/method/verification/toy-model-scripts): the results of the two toy models and the v2.2 refinement of the hard core.
- `verify/soliton_obituary.py`, [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script): the two standing results about the retired soliton candidate's model.
- `verify/phase_space_diameter.py`, [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script): every number that the phase-space-diameter note (`papers/phase-space-diameter.md` v1.1) computes, against anchors independent of the note such as the CODATA Planck units and the Particle Data Group's photon and entropy densities. Figures the note quotes from the literature are not recomputed, except where a check reproduces them, and the torsion-balance limits are typed in from the source table (the script's docstring).
- `verify/closed_universe.py`, [the closed-universe script](/wiki/method/verification/closed-universe-script): every number of the closed-universe note (`notes/closed-universe.md`, 2026-10-27, not reviewed), after anchors independent of it; everything after the anchors is a regression check of the investigation's own numbers (the script's docstring).
- `verify/velocity_gated_gravity.py`, [the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script): the numbers of the velocity-gated-gravity note (`notes/velocity-gated-gravity.md`, 2026-10-28, not reviewed), after anchors independent of it, among them calc note #2's two shortfall ratios (section D, flag 16's addendum); the note's N-body runs are checked against their kept logs, not rerun.
- `verify/gate_mechanism.py`, [the gate-mechanism script](/wiki/method/verification/gate-mechanism-script): the arithmetic and algebra of the gate-mechanism note (`notes/gate-mechanism.md`, 2026-10-28, not reviewed), including the benchmark's σ₀/m; in the note's words it "does not test their physics".
- No script checks the other numbers of [the clumping problem](/wiki/history/main-problems), the record's derivation of the velocity gate's mechanism, the derivations of #11's cosmology or of conjugate special relativity (#13), or the predictions as such; those claims rest on their derivations. The phase-space-diameter script checks only what the note adds to them, among it #13's maximum force at the Planck length, c⁴/G = 1.21×10⁴⁴ N, and the exchange of row 10's two kinetic terms under a → C/a when M̃ = M_P.

## Under pressure

- **The dark-energy sector.** The second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (#11 §10; root `CLAUDE.md`; [the phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)). It bears on τ's quintessence, the no-phantom bound and row 4.
- **Degeneration risks**, #11 §15: "tunable wave-island collective sector (quarantined); gate tail not yet forced; the novelty demotion of §7.4 as a standing caution, joined in v2.1 by the §12 soliton obituary and the §5 re-attribution of the compatibility theorem", and the phantom crossing.
- **Falsification exposure**: #11 §15 names rows 1, 4 and 7 as exposed to falsification in the near term.
- **Row 5's premise.** With the potential as written the turnaround needs a closed universe, and in the program's model class the data disfavour closure at about 2σ, a background fit without supernovae (flag 27 addendum; [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#what-the-data-say)).
- **The gate's mechanism.** The gate-mechanism note of 2026-10-28 finds that exchanging #11 §7's X cannot produce #11 §8's gate, and flag 55 proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The gate itself is not refuted; rows 1–3 depend on the tag, and whether row 3's island discriminant survives is open.
- **Conjugate special relativity** rests on #13 alone. No review round has examined #13, no `verify/` script covers its derivations, and #11 v2.2 does not mention it; its standing comes from `HANDOFF.md` §2 and from the root `CLAUDE.md`, which lists #13 among the current papers.

## Standing claims by section

### The research program

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The hard core](/wiki/program/hard-core): Born reciprocity is an exact symmetry of the laws, spontaneously broken by the vacuum; only ω is rigid, and η is the emergent order parameter | [P]: the content of postulates P1–P5 (#11 §4) | a postulate; #11 §15 records it as intact after two forced corrections (P2′; the w-dictionary); the v2.2 refinement from the toy models is [D][V], gated in `verify/toy_coset.py`, `verify/toy_s4.py` and `verify/toy_s5.py` |
| [P1: the phase-space arena](/wiki/program/postulates/p1-arena): physics lives on phase space with a symplectic form ω and a positive generalized metric H | [P] | assumed, not derived; the algebra built on its two structures is checked, I[Z]² = −1 [V] (battery test T2) |
| [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem): the program has content beyond general relativity plus self-interacting dark matter if and only if η is emergent | [D] (#11 §4); "[D — structural]" in the note that derived it | not machine-checked as a whole; its input, the compatibility theorem, is [T][V] (battery test T1) |
| [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime): ω is fixed and η = HJ is chosen by the vacuum; v2.2 adds that the polarization is a Goldstone angle | [P]; the correction from the original P2 forced [D]; the Goldstone-angle sentence [D][V] | the correction is forced by the nontriviality theorem; the toy-model scripts check the v2.2 sentence, which shows the structure is consistent and does not test the postulate |
| [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity): the action is invariant under the Born rotation generated by I = ω⁻¹H | [P] | realized in the coset toy model, whose invariance under ρ is checked symbolically in `verify/toy_coset.py`; consistency, not evidence that P3 holds in nature |
| [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter): the Standard Model is x-polarized, conjugate matter χ is p-polarized, and no gauge force crosses polarizations; strict since v2.1, with gravity-induced mixing ε ≲ 10⁻¹³ | [P]; the gravity-only bound [27S] | strict by decision (round-3 Decision 1, 2026-10-19), not by derivation; whether 10⁻¹³ is a ceiling or a floor is unresolved |
| [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection): our vacuum is x-tilted, and the mirror vacuum is equally lawful | [P] | postulated; the toy models give a consistent realization, an ordered ℤ₂ phase of the frozen-H reduction (`verify/toy_s4.py`), not a test |
| [The conjugate universe](/wiki/program/conjugate-universe): the momentum-space description of the one physical state, synchronized with ours rather than causally linked; founding supposition 2, "alive, transformed"; under reciprocity at the Planck length, today's radiation maps to a region 1.0×10⁻³¹ l_P across with momenta spread over 5.4×10⁶¹ m_P c, so the conjugate description's extents lie beyond the Planck scale in both variables | no tag (#11 App. A); the relations that carry it, a·ã = 1 and the corrected dictionary, [D]; the image of today's radiation [D][V] (phase-space-diameter note §8.3) | not machine-checked as a whole; the image of today's radiation is gated in `verify/phase_space_diameter.py` |

### Phase-space geometry

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The Born length λ](/wiki/phase-space/reciprocity/born-length): #13's name for the reference length that, with ε = ℏ/λ, puts position and momentum on a common scale; #13 sets it equal to the Planck length, which gives the maximum force c̃ = c⁴/G; reciprocity with Born length λ keeps a phase-space rectangle's area and inverts its aspect ratio, so every rectangle is self-dual for exactly one λ, and the program's action singles out no Born length | the name and the identification untagged (#13 §1); the Planck closure at that value [D] (#13 §4); the need for some reference length [T]; the rectangle algebra [T][V] and "the program fixes no λ" [D] (phase-space-diameter note §5) | #13 unreviewed, and #11 v2.2 does not mention it; the rectangle algebra is gated in `verify/phase_space_diameter.py`; the cosmic box's self-dual length cannot serve as the Born length ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)) |
| [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z): Im Z = g is the spacetime metric and Re Z = X the momentum graviton | [D] (#11 §6); "[D — structural; math facts standard]" (calc note #5 §C) | only the parametrization identities, such as I[Z]² = −1, are [V]: battery test T2, at one sampled point |
| [Reciprocity as modular inversion Z → −Z⁻¹](/wiki/phase-space/modular-field/modular-inversion): the fixed point is Z = i; on the vacuum slice the inversion is scale-factor duality, and the circle \|Z\| = 1 is identified with a·ã = 1 (flag 23); on [Gaussian wave packets](/wiki/phase-space/modular-field/gaussian-states) the inversion is the Fourier transform, and \|Z\| = 1 (the square rectangles, Δx = Δp), Z = i (the one round state) and det H = 1 (every Z) are three different loci | [D] (#11 §6); "[D — structural]" (calc note #5 §C); the transform on wave packets [T][V] and the three loci [D][V] (phase-space-diameter note §5) | d = 1 checked symbolically in `verify/toy_coset.py`; general d by the argument alone; the cosmological reading is structural; the transform and the three loci are gated in `verify/phase_space_diameter.py` |
| [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase): the dark-energy field τ is the angle around the Maslov circle of Λ(d), the Shilov boundary of the Siegel domain | the identification [D] (#11 §6); the Shilov boundary and π₁ = ℤ [T]; the periodicity [D]; τ's lightness [P] (#1 §2) | not machine-checked; the toy model supports only the consistency of the structure |
| [Reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity): on a closed position space no unitary map exchanges position and momentum as wholes, while the flat transform exchanges a packet of width σ to relative accuracy (2/3)(σ/R)²; on T\*S³ only the position polarization is integrable, so closure cuts the U(1) of polarizations to Z₂ (flag 47); no product of a closed position space and a closed momentum space is symplectic, while Gr̃(2,5) is a compact phase space with Born reciprocity as an automorphism | [D][V] (closed-universe note §5); the integrability result [D][V] from the note's critic alone, not independently verified; Gr̃(2,5) [S][V] | `verify/closed_universe.py` section E (E3–E5); computed, not reviewed |

### Spontaneous breaking of reciprocity

#### The mechanism

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [Mandatory breaking: the uncertainty argument](/wiki/symmetry-breaking/mandatory-breaking): [x, p] = iℏ rules out joint locality in x and p, so a world with local physics must select a Lagrangian polarization | untagged in #11 §3, part of the hard core, whose postulates are [P]; its v2.2 qualifications [D][V] where #11 §4 tags them | a qualitative argument, not machine-checked |
| [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter): reciprocity is broken if and only if the vacuum carries a definite η | [P] (P2′, #11 §4) | in the coset toy model the order parameter O = K₁₁ flips sign under ρ [V] (`verify/toy_coset.py`, S3); the naming, J in #11 and K in the toy-model note, is unreconciled |
| [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle): where ρ sits inside a continuous U(1), the x-sharp and p-sharp vacua are joined by a flat direction, so a definite polarization needs a ρ-preserving potential | [D][V] (#11 §4, §10) | gated in `verify/toy_coset.py` and `verify/toy_gw.py`; the link to τ is consistency only |
| [The twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element): it leaves the vacuum invariant, so breaking ρ is physical only once matter couples to the sign of K | no tag of its own; stated in #11's v2.2 refinement of P2′, whose Goldstone-angle sentence is [D][V] | round-4 finding F3, upheld; gated in `verify/toy_coset.py` |
| [The section condition: what η fixes](/wiki/symmetry-breaking/section-condition): a section condition built from η confines matter to one of η's null lines without telling the two apart; a clean pair only for d = 1 | [V]; the section condition itself [T], imposed in the toy; the curved-background question [O] | gated in `verify/toy_s5.py`, parts A and B |
| [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling): the coupling I_K is local in x in one vacuum and local in p in the other, the weak form of matter locality | [V] | gated in `verify/toy_s5.py`, part C, and reproduced independently by the round-4 referee; finding F5 narrowed it to a coupling built from H as well as K; the strong form is [open](/wiki/symmetry-breaking/strong-locality) |

#### The toy models

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [Acceptance criterion 1: the toy Lagrangian (OP11)](/wiki/symmetry-breaking/toy-models/acceptance-criterion): met "in the referees' wording" by model I with a bounded potential (#11 §14 item 11) | met; the remaining parts [O] | model I's checks gated in `verify/toy_coset.py` and `verify/toy_s4.py`; the toy-model note graded B in [review round 4](/wiki/method/review/round-4) and revised to version 2 |
| [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries): an Sp(2, ℝ)-invariant action of (H, K), also invariant under K → −K | [V] | criterion S1, gated in `verify/toy_coset.py`; confirmed independently by the round-4 referee |
| [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua): ρ maps K(φ) to −K(φ), the stabilizer is {±1}, and O = K₁₁ flips sign | [V] | criteria S2 and S3 and the spectrum, gated in `verify/toy_coset.py`; confirmed by the round-4 referee |
| [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential): bounded by Cauchy–Schwarz and stable with H dynamical, with Hessian eigenvalues 0, 0.764, 2, 5.236; put in by hand | [D][V] (#11 §10) | gated in `verify/toy_coset.py`; upheld in round 4 as "the repair"; its origin is [open](/wiki/symmetry-breaking/rho-preserving-potential) |
| [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction): the Monte Carlo simulates model I's polarization angle at H = 1, stated as a reduction | untagged | required by round-4 revision 1; simulated in `verify/toy_s4.py` |
| [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo): ⟨\|m\|⟩ = 0.954 at L = 16, 32 and 64, means over four independent seeds, for the frozen-H reduction only | [V] | gated in `verify/toy_s4.py`; the ordered-phase values agree with the round-4 referee "to about 1%"; the control values were corrected in version 2 |
| [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base): the self-dual (Ω = 1) Grosse–Wulkenhaar model on the matrix base | [V] | the anchors and the kinetic form gated in `verify/toy_gw.py`; reproduced by the round-4 referee; the route built on it fails criterion S4 |
| [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma): left multiplication by parity, D f_mn = (−1)^m f_mn, recorded as a credited lemma | [V] | gated in `verify/toy_gw.py`; confirmed by the round-4 referee, "Correct, but not a new structural fact" |
| [Complex versus real fields: symmetry versus covariance](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields): a field symmetry for complex fields, only a covariance for real ones | [V]; partly prior art | criterion S1 for this route, gated in `verify/toy_gw.py`; reproduced by the round-4 referee |
| [Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua): the vacuum's position-versus-momentum spread varies as Δ(0) cos β along a flat direction; classical only | [V] | criteria S2 and S3 for this route, gated in `verify/toy_gw.py`; reproduced by the round-4 referee |
| [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration): the classical breaking does not survive quantization, ⟨Δ⟩ = 0; a negative result | [D] (the worklog: "S4 fails, by an exact argument [D]") | its premise and the logarithmic tadpole gated in `verify/toy_gw.py`; the round-4 referee confirmed the conclusion "in substance"; one step is "argued against, not proven", and the comparison with the exact solution is open |

### Gravity and the momentum graviton

#### The momentum graviton X

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [Shift symmetry: X is never auxiliary](/wiki/gravity/momentum-graviton/shift-symmetry): the rigid Sp(2d, ℝ) contains Z → Z + B | [D — rigorous] (calc note #6 §1); step (i) of #11 §7.1's chain, [D + T] | a symmetry argument, not machine-checked |
| [Dual diffeomorphisms: a second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms): δX_μν = ∂₍μλ_ν₎ is a second linearized diffeomorphism, because X is symmetric | [D + T] (calc note #6 §2; step (ii) of #11 §7.1) | structural, not machine-checked |
| [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner): doubling geometry with ω pairs the metric with a second graviton, where doubling with η gives a harmless 2-form | [D + T] (#11 §7.1; calc note #6 §2) | structural, not machine-checked; #11 §15 counts it the observation that "stands regardless of its fate" |
| [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain): a massless X is excluded by the multi-graviton no-go, an ungauged X by [Lorentz signature](/wiki/gravity/spin-2-fields/signature-obstruction) | [D + T] (#11 §7.1; calc note #6 §2) | a chain of symmetry and no-go arguments, not machine-checked |
| [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs): the polarization choice breaks the dual diffeomorphisms, and X eats the would-be Goldstones | [D — structural] (calc note #6 §3); step (iii) of #11 §7.1, [D + T] | not machine-checked; M_X has no value in any source, only the lower bound M_X c² > 5.2 meV in the aligned vacuum ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)) |
| [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten): τ lives in the compact sector, not the [Stückelberg sector](/wiki/symmetry-breaking/stuckelberg-fields#τ-is-outside-the-stückelberg-sector) | [D — leading order] (calc note #8 §3), carried in #11 §7.5, [D] | an argument from where each mode comes from, not machine-checked; the residual mixing is [OP6](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) |
| [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity): five βₙ reduce to two parameters; the massless graviton is reciprocity-even and X odd, with reciprocity as the frame exchange (flag 39) | [D] (#11 §7.5); [D + T] (calc note #8 §3) | no battery test covers the count or the parities; its machine-checked inputs are V(1) = 2T and the coefficients of T (battery tests T5 and T6) |
| [Safety by range: X and ordinary matter](/wiki/gravity/momentum-graviton/fifth-force-safety): Standard Model couplings to X have gravitational strength but are cut off by the [Yukawa range](/wiki/gravity/spin-2-fields/yukawa-forces#the-range) 1/M_X | [D + T] (calc note #8 §3); [D] (#11 §7.5) | not machine-checked; calc note #8 cites no force measurement, and the phase-space-diameter note finds its range statement "consistent with the bound but gave no number" (§8.2; next row) |
| [The laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound): in the program's aligned bimetric vacuum, background ratio u = 1, X acts on ordinary matter as a Yukawa force of strength α = (4/3)u² = 4/3, and torsion-balance tests of the inverse-square law then bound its range, λ_X < 37.7 μm, M_X c² > 5.2 meV; for other u the bound moves, 57.0 μm at u = 0.5, 42.5 μm at 0.8 and 30.8 μm at 1.5 | the bound [V][S]; the program's vacuum u = 1 [D][V][O], "the only proportional vacuum with zero wedge vacuum energy; persistence under expansion open" (phase-space-diameter note §8.2, §9) | gated in `verify/phase_space_diameter.py`, whose interpolation of the experiment's table reproduces the published 38.6 μm and 30 μm; round 5's shared weakest link was the background ratio, dropped in version 1.0 (ruling R1, upheld in substance), and version 1.1 states u = 1; it assumes X adds the only Yukawa term, and whether the aligned vacuum persists as the universe expands is [open](/wiki/status/open-problems#gravity) |
| [X between ordinary bodies: a Yukawa term, not a velocity gate](/wiki/gravity/momentum-graviton/ordinary-bodies): in the aligned vacuum (u = 1) and unscreened, X's dependence on relative velocity is the O(v²/c²) spin-2 factor (3γ² − 1)/2, 1 + 2.40×10⁻⁷ at 120 km/s against 1 + 3.20×10⁻⁷ for the graviton, not a gate; a potential in momentum differences exerts no force; a relative-velocity gate acting between all bodies is bounded to \|ε\| < 8.7×10⁻⁹ for Gaussian gates of width 0.3–3000 km/s, and to 3.5×10⁻¹¹ at the record's width | the factor [D][V; two verifiers by different methods]; the bounds [D; data S; two verifiers] (velocity-gated-gravity note §§2–3) | `verify/velocity_gated_gravity.py` sections B and C; computed, not reviewed; #13's two readings give 4.3×10⁻⁴⁴ and 0 (flag 56) |
| [The momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe): with f dynamical at M_f = M_g, f closes with the same k and stays aligned, 1 − y = 1.5×10⁻⁶¹ today at the smallest M_X; the branch needs β₁ > 0 (flag 51); the turnaround is regular; G_eff = 2G_N for H ≫ M_X, halfway at T ≈ 1.55–1.58 TeV (flag 52); the Higuchi bound holds through the dressed mass (flag 53); Könnig's gradient instability operates above about 1.3 TeV; a frozen f contradicts the record | [D][V] (closed-universe note §6); unequal curvatures inconsistent [T] (Comelli, Crisostomi, Nesti, Pilo 2012) | `verify/closed_universe.py` section D, with two published anchors; computed, not reviewed |
| [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer): momentum-space geometry is a reciprocity-odd massive spin-2 field | no tag of its own: a summary of results tagged [D + T], [D — structural], [D] and [D][V] | as for the results it assembles |

#### The tuning test

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential): X's mass is an energy cost for misalignment between J and Z, measured by {J, I[Z]} = [[S, A], [A, S]] | [D][V] (#11 §7.2); [D — rigorous] (calc note #7 §2) | the blocks: battery test T3, at one sampled point; the reading of their zero set has no test |
| [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures): potentials built from metrics give no Fierz–Pauli trace term (66.58 vs 63.72) and a structure outside the Hassan–Rosen span (rms 3.29); a negative result | [D — rigorous] (calc note #7 §2); [D][V] (#11 §7.2) | battery tests T4 and T7; the second invariant rests on the derivation alone |
| [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier): wedge polynomials of the symplectic vielbein are the Hinterbichler–Rosen class, [ghost-free](/wiki/gravity/spin-2-fields/ghosts) by construction | [D — structural, resting on T] (calc note #7 §3); the class cited from memory [12†] | no battery test covers it; selected, not derived ([OP1](/wiki/gravity/tuning-test/wedge-reduction)) |
| [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass): the theory fails in second-order variables and passes if and only if it is formulated in first-order ones | [D][V] (#11 §7.2) | the metric-tier half: battery tests T3, T4 and T7; the frame-tier half is [D — structural, resting on T], with no test |
| [Constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric): Hassan–Rosen bimetric gravity with the second frame confined to the compact Λ(4) | [D — structural] (calc note #7 §4); the bimetric facts [T] | not machine-checked |

#### The palindromic branch

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome): on the broken vacuum reciprocity acts as the exchange of the two frames | [D] (calc note #8 §1; #11 §7.3) | #11 tags §7.3 [D][V], but the [V] belongs to the integer identity (battery test T5); no script checks the palindrome's derivation |
| [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity): the integer identity [2,8,6] = 2·[1,4,3] makes a flat aligned vacuum force T = 0 and V(1) = 0 | [D][V] (#11 §7.3); "[D — rigorous, four lines]" (calc note #8 §2) | battery tests T5 and T6; the novelty claim was downgraded (#11 §7.4) and waits on the partially-massless comparison ([OP2](/wiki/gravity/palindromic-branch/pm-comparison)) |

### Dark matter

#### Conjugate matter and the gate

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate): the self-interaction amplitude depends on the incoming relative momentum through F(k²/μ²) | [D — mechanism; shape [O]] (#11 §8) | the mechanism is derived structurally in the field-equation notes; no script; the shape is [OP4](/wiki/dark-matter/conjugate-matter/gate-shape); not derived according to the gate-mechanism note, and flag 55 proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)) |
| [Dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress): the momentum-side counterpart of stress-energy, the quantity X couples to | [D — structural] (calc note #5 §E) | a definition in words with no explicit formula; not machine-checked; its enhancement is [OP5](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement); the gate-mechanism note's record audit finds no formula for T̃ and no χχX vertex (flag 55) |
| [The gate mechanism: X exchange over fiber overlap](/wiki/dark-matter/conjugate-matter/gate-mechanism): X exchange between dual-stress bilinears, acting over the overlap of [momentum-fiber](/wiki/phase-space/reciprocity/momentum-fibers#quanta-with-a-width-along-the-fiber) wavepackets of width μ | [D — mechanism; shape [O]] (#11 §8); [D — structural] (calc notes #5 and #6) | no explicit propagator, vertex or overlap integral exists in any source; the gate-mechanism note (two derivations, the second blind; not reviewed) finds that exchanging X cannot produce the gate [D][V], rerun in `verify/gate_mechanism.py`, and flag 55 proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)) |
| [What could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers): exchange of a spin-J field gives a degree-J polynomial in γ that grows with speed on the scale c; an order-one rise at 120 km/s needs J ≈ 3533–4996; a tower of every spin needs terms about 10^5421169 times the net; a medium gates velocity through the medium; a continuous-spin particle has the right shape but a threshold that falls with distance | finite spin [D][V; two derivations]; the tower and the medium [D][V; one derivation]; the no-go theorems [T][S]; continuous spin [T][S, read twice: by the run-3 theory verifier and by the drafting session, whose fetch is in the session transcript, not the record; numbers D] (velocity-gated-gravity note §9) | `verify/velocity_gated_gravity.py` section I and `verify/gate_mechanism.py` section G; computed, not reviewed |
| [The gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law): σ_T(v) = σ₀F(v²/v\*²), with a robust knee at v\* and isotropic scattering below the gate | [D], with the shape [O] (#11 §8) | not machine-checked; tested by rows 1 and 2; its mechanism not derived according to flag 55, pending Paul's ruling |
| [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark): m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} | [D] (#1 §5.1; carried by #11 §8) | `verify/gate_mechanism.py` section D recomputes σ₀/m = 32.0 cm²/g at 70 MeV, or m = 71.5 MeV for 30 cm²/g; contact Born physics that needs no mechanism (gate-mechanism note §5) |

#### Momentum clumping

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion): the criterion g·n_gate ≥ m·min(σ, v\*)² fails at the scattering benchmark | [D] (#11 §9 (i)) | the two shortfall ratios are reproduced in `verify/velocity_gated_gravity.py` section D since 2026-10-28, which backs the handoff's ✓; the record's tag stays [D] until Paul rules (flag 16, addendum); #2's narrow-gate form overstates the Milky Way shortfall about 3×, verdict unchanged (flag 58) |
| [The classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem): meeting the criterion forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ | [D] (#11 §9 (i)) | not machine-checked; a recomputation made while building the wiki is outside the gate (flag 19) |
| [The net theorem: clumping is nowhere mandatory](/wiki/dark-matter/momentum-clumping/net-theorem): "forbidden (particles), fatal (committed wave), decorative (free wave)" | [D] (#9 §7); untagged in #11 §9 (iii), resting on (i) [D] and (ii) [D + T] | not machine-checked |
| [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate): Γ ≈ c·g²ρ²min(σ, v\*)⁴/(m³σ⁶) on the wave island | "[D, heuristic coefficients]" (calc note #3); inside #11 §9 (ii), [D + T], with "coefficients [O]" | not machine-checked |
| [Scenario B: tunable streams (quarantined)](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b): with the coupling free, streams are tunable across ~10 orders, "optional, never required" | part of #11 §9 (ii), [D + T] | not machine-checked; a degeneration risk (#11 §15) |
| [Relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic): free relic abundance via misalignment, on the wave island only | no tag of its own (the clumping problem's salvage, #11 §9) | not machine-checked; the claim contains no number |

#### The candidates

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles): mirror-polarized particles of assumed stability, with a knee at v\* and a sharp tail | "[D — framework; each candidate O]" (#11 §12); its gravitational behaviour [D]; its gate [D — mechanism; shape [O]] | nothing machine-checked |
| [The X-condensate candidate](/wiki/dark-matter/candidates/x-condensate): a coherent oscillation of the massive momentum graviton, protected by its mass | "[D — framework; each candidate O]" (#11 §12); the field [D + T]; its lineage [23†] (flag 20) | nothing machine-checked |
| [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction): the abundance closes at M\* = 2.9–4.4×10¹² GeV, and the 3×10¹³ GeV benchmark is overproduced 2.1×10³–1.2×10⁴ times; a result about the withdrawn model | [V] (#11 §12) | gated in `verify/soliton_obituary.py`; round-3 ruling 2, upheld; the referee's Kibble–Zurek figures are accepted, not verified |
| [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure): stable W′± would overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark | [V] (#11 §12) | gated in `verify/soliton_obituary.py`; conditional on the withdrawn benchmark |

### Cosmology

#### Scale-factor duality

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint): ω-rigidity fixes the comoving phase-space cell; founding supposition 6, "promoted to theorem"; it fixes the area of one cell, not the number of occupied cells | [D] (#11 §10); the one-cell reading [D] (phase-space-diameter note §3) | the derivation is not machine-checked; det H = 1 on the whole slice X = 0, the fact behind flag 23, is gated in `verify/phase_space_diameter.py`; the identification with the \|Z\| = 1 locus awaits a ruling (flag 23), which the round-5 adjudication recommends accepting |
| [The duality dictionary w_eff = −w̃](/wiki/cosmology/scale-factor-duality/duality-dictionary): a dual-frame fluid with equation of state w̃ contributes w_eff = −w̃ | [D — corrected en route] (#11 §10) | derived in the lab notebook (#1 §6); no script |
| [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce): if V(τ) goes negative our expansion reverses, and by a·ã = 1 the same event is the conjugate universe's bounce | [D] for the bounce identity; [T] for the cited fits | not machine-checked; long horizon; its premise conflicts with the potential as written (flag 27), with which a turnaround needs a closed universe (flag 27 addendum); only one of the cited fits supports the clause (flag 45) |
| [The phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter): for blackbody radiation filling a sphere, D_x·D_p = κ h N_γ^{1/3} with κ = 1.708, the corrected form of a chat-only relation, constant for a fixed comoving region; for today's observable universe N_γ = 1.43×10⁸⁹ and S = 1.01×10⁹⁰ k_B, the chat's ~10⁹⁰ being the radiation entropy; the aspect ratio, 5.2×10⁹² in Planck units, grows as a², and its logarithm is a clock that "reparametrizes ln a and adds no dynamics" | the identity [D][V]; its constancy [T]; today's values [V]; the clock [D][V] (phase-space-diameter note §3, §5, §9) | gated in `verify/phase_space_diameter.py`; the note graded B by both referees of [review round 5](/wiki/method/review/round-5); standard cosmology, so it cannot test the program (note §3); its chat-only square at the bounce is dead ([obituary](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)) |
| [The self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box): the Fourier box [l_P, L] × [ħ/L, ħ/l_P] maps onto itself under reciprocity exactly when λ = √(l_P L), 47–84 μm, the Cohen–Kaplan–Nelson length and the cell length of Freidel, Kowalski-Glikman, Leigh and Minic; its match to the dark-energy scale is the Friedmann equation, (3Ω_Λ/8π)^{1/4} = 0.535; with λ² = l_P L_Λ the Hubble box's aspect ratio is √Ω_Λ(t), 0.83 today, and Λ = 3l_P²/λ⁴ | the self-dual length [T][V], with its prior art [S]; the dark-energy match, A = √Ω_Λ(t) and Λ = 3l_P²/λ⁴ [D][V] (phase-space-diameter note §7, §9) | gated in `verify/phase_space_diameter.py`; A = √Ω_Λ(t) holds "by construction"; round 5 added prior art and corrected the reformulation of Λ to a fourth root (rulings R7, R10, R15); it predicts nothing unless λ is fixed by other physics, and the length is dead as a program scale ([obituary](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)) |
| [A closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe): nothing derives closure, but with V₀[1 + cos(τ/f)] ≥ 0 a turnaround exists only if k = +1 (flag 27 addendum); in the program's model class the data disfavour closure at about 2σ, and w₀wₐ+Ω_K is the wrong proxy; the data give only lower bounds on the largest size, R_max > 1.174×10⁵ Gpc and t_turn > 6.015×10⁵ Gyr at 95% given closure; the momentum fibre stays flat (flag 48) and closure only makes momenta discrete; a compact momentum space would be a new postulate, and its symmetric reading is dead unless postulated | [D][V], data [S], prior art [T] and [S] (closed-universe note §2–§4, §7, §8) | `verify/closed_universe.py` sections B, C and E; computed and checked by independent agents, not reviewed |

#### Dark energy

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence): V = V₀[1 + cos(τ/f)], [thawing](/wiki/cosmology/dark-energy/thawing-and-freezing) along the corridor wₐ ≈ −1.5(1 + w₀); under real pressure | [D + T] (#11 §10); the cited fits [S]; the toy-model support [D][V], consistency only | no script tests the cosmology; the phantom crossing leans against it; the corridor lies in the w₀–wₐ region of the second data release's fits and is separated from them by its slope (flag 43) |
| [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force): as a [pseudo-Goldstone field](/wiki/cosmology/dark-energy/axion-like-fields#τ-an-axion-like-dark-energy-field), τ couples derivatively, with no tree-level Yukawa coupling to Standard Model matter | [D] (#1 §4) | argued in the lab notebook only; #11 does not restate it; no script |
| [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound): τ is a canonical scalar, so w ≥ −1 strictly; under real pressure | [D] (#1 §7 item 1), within #11 §10's [D + T] | not machine-checked; its test is row 4 |
| [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint): two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) | [D] (#1 §7 item 4), within #11 §10's [D + T] | a counting result, not machine-checked; its third leg is long-horizon (flag 27); in a closed universe Ω_k is a third input and the data bound t_turn only from below (flag 46) |

### Electric–magnetic duality

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles): if conjugate-sector solitons exist they gravitate, so "true but irrelevant" is the empty set; their candidacy as the dark matter is retired | [D] (#11 §11.1) | an argument from P4, with no calculation or script |
| [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice): the Dirac–Schwinger–Zwanziger pairing makes charge space symplectic, and choosing a duality frame is choosing a Lagrangian polarization | [D — structural; math T] (#11 §11.3); the pairing's citation [17†] | no script checks the charge-lattice statements; the phase-space side of the shared matrix is gated for d = 1 in `verify/toy_coset.py` |

### Conjugate special relativity

All seven claims come from #13, and all are unreviewed: no review round has examined #13, no `verify/` script checks its derivations, and #11 v2.2 does not mention it. The phase-space-diameter script computes one of #13's numbers, the maximum force at the Planck length. The tags are #13's own.

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [Two causal cones](/wiki/conjugate-relativity/two-causal-cones): H = diag(g, g⁻¹) gives two null cones, and the dual one bounds \|dp/dt\| by c̃ | the block form it starts from [D — compatibility theorem] and the role of X [D — §7 of the checkpoint] (#13 §1; flags 30 and 29); the cones untagged | unreviewed; no script |
| [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force): c⁴/G ≈ 1.2 × 10⁴⁴ N at the Planck value of the [Born length](/wiki/phase-space/reciprocity/born-length), four times the literature's c⁴/4G | the value untagged, listed under "Numerical anchors" (#13 §7); the factor of 4 [O] | listed alive in `HANDOFF.md` §2 without a check mark; the value c⁴/G = 1.21×10⁴⁴ N is computed in `verify/phase_space_diameter.py` (phase-space-diameter note §8.1), which also finds 1.4×10⁻¹⁷ N at the self-dual length, dead as a Born length ([obituary](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)); Low 2006, whose reciprocal relativity bounds forces by a constant [S], is prior art for #13's maximum force, a lead the root `CLAUDE.md` does not queue |
| [Force boosts and force composition](/wiki/conjugate-relativity/force-boosts): the dual Lorentz group on (t, p); forces compose so as to saturate at c̃ | the group [D — structural]; the composition law [D]; the merger arena [O — flagged, not derived] | unreviewed; no script; under §5's dual rest the merger arena gets a second answer (flag 56) |
| [Force dilation](/wiki/conjugate-relativity/force-dilation): dτ̃ = dt√(1 − F²/c̃²) for conjugate-polarized systems | [D — structural; which physical clocks respond is polarization-dependent, O] (#13 §3) | unreviewed; no script |
| [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell): x_μx^μ = λ_χ², and E = λc̃ is the [Planck energy](/wiki/gravity/spin-2-fields/planck-units#planck-closure) at λ = l_P | the shell [D — structural]; Planck closure [D]; the gate-scale reading [D — structural] (#13 §4) | unreviewed; no script; the λ_χ description is unreconciled with #11 §8 |
| [Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia): trajectories of constant dp/dt are dual-inertial | [D] (on #13 §7's fixed list); the dual second law "conjecture-tier" | unreviewed; no script; it gives freely falling pairs no dual-kinematic correction, against §2's merger arena (flag 56) |
| [The equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle): the equivalence of all force-free frames is the [equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle) reached from kinematics | [D — structural] (#13 §5); the long-range/short-range asymmetry [D — checkpoint §7] (#13 §6; flag 29) | unreviewed; no script |

### Predictions

Rows 1–10 of #11 §13 stand. Row 11, particles or condensate, is a diagnostic still [open](/wiki/predictions/dark-sector-microstructure), and the withdrawn rows are in [the graveyard](/wiki/status/graveyard#withdrawn-predictions).

| Claim | Tags | What verifies it |
| --- | --- | --- |
| [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee): a knee at v\* ~ 10² km/s and zero cluster signal for particle χ | the scattering law behind it [D] for the mechanism, [O] for the shape of the tail (#11 §8) | not machine-checked; near-term falsification exposure (#11 §15); the mechanism not derived according to flag 55, pending Paul's ruling |
| [Row 2: isotropic scattering below the gate](/wiki/predictions/scattering-isotropy): unlike the forward-peaked scattering of light-mediator models | [D] (#1 §5.1; restated in #11 §8) | not machine-checked; particle island only; depends on the gate's tag (flag 55) |
| [Row 3: the island discriminant](/wiki/predictions/island-discriminant): the knee's tail is sharp for particles and falls as (v\*/σ)⁴ for waves; a diagnostic | [D]; the tail's shape on the particle side [O] (#11 §14 item 4) | not machine-checked; under the gate-mechanism note's reading R1 the particle tail is a power law, and whether the discriminant survives is open (flag 55) |
| [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift): w₀ > −1, wₐ < 0, never phantom; under real pressure | [D + T] (#11 §10) | not machine-checked; the second data release "already favors a crossing above z ≈ 0.4" (#11 §13; round-3 ruling 11) |
| [Row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion): the turnaround is the conjugate bounce | the bounce identity [D]; the supporting fits [T] | not machine-checked; long horizon (flag 27); with the potential as written it needs k = +1, disfavoured at about 2σ in the program's model class ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)) |
| [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton): the reciprocity-even spin-2 eigenstate is exactly massless (on the parity, flag 39) | [D] (#11 §7.5); [D + T] (calc note #8 §3) | no check covers the parity assignment; V(1) = 2T is [V] (battery test T5) |
| [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null): both candidates are decoupled from the Standard Model, with P4 strict | [P] (#11 §4), strict by round-3 Decision 1 | a postulate and a decision, not a derivation; not machine-checked |
| [Row 8: no monopoles of our sector](/wiki/predictions/monopole-null): a permanent null, with Berry-curvature monopoles in solids as the only shadow | the row untagged; the audit behind it [D], the dilution [T], the analog [16†] (#11 §11.1) | not machine-checked |
| [Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion): the linear term is exactly zero, protected by ρ², and the quadratic term is suppressed | [D, schematic] for the protection, [T] for the observational statement (#1 §4) | not machine-checked; no program document cites the bound |
| [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step): an optional a⁻⁶ step in G_eff, and negative ΔN_eff if the dual space is closed; if reciprocity fixes the dual Planck mass M̃ = M_P, the step sits at the self-dual epoch, which must lie before nucleosynthesis | [D] (#1 §6); the self-dual placement, conditional, [D][V] (phase-space-diameter note §8.4, §9) | the row is not machine-checked; bounded by its free parameters, and no document compares it with data; the exchange of the two kinetic terms under a → C/a at M̃ = M_P is gated in `verify/phase_space_diameter.py`; the dual Einstein–Hilbert term behind the step is derived in no document (flag 49), and a closed universe does not close the dual space, so the negative ΔN_eff needs an unstated postulate (flag 48) |

## Sources

- `CLAUDE.md` "Since the handoff" — the current state: strict P4, the toy Lagrangian done to the referees' wording, the dark-energy sector under pressure, the phase-space-diameter note's results and the lead on Low 2006.
- `papers/phase-space-diameter.md` §3, §5, §7, §8, §9 — the diameter relation and its clock; the rectangle algebra, the unfixed Born length and the three loci; the self-dual cosmic box; the bound on X's range, the conjugate image of today's radiation and the self-dual placement of row 10's step; the tags of each.
- `review/round5-adjudication.md` "Verdict", "Rulings", "Recommendations to Paul" — verdict B; rulings R1, R7, R10 and R15; the recommendation on flag 23.
- `verify/phase_space_diameter.py`, run by `scripts/check.sh` — the note's gated numbers.
- `papers/broken-born-checkpoint-v2.md` §2–§15, App. A — the claims and their tags, the verification battery, the predictions table, the assessment and the fates of the founding suppositions.
- `papers/reciprocity-toy-models.md` §2–§6 — the toy-model results.
- `papers/conjugate-special-relativity.md` §1–§7 — the dual-relativity claims and their tags.
- `review/round4-adjudication.md` "Rulings" and `review/round4/referee/audit-notes.md` Step 2 — findings F2, F3 and F5 and the referee's reproductions of the toy-model results.
- `review/round3-adjudication.md` "Rulings", "Decisions", "What survives v3" — ruling 2, Decision 1, and the soliton results that survive.
- `HANDOFF.md` §2 — the alive list at the move from claude.ai, including the maximum force.
- `notes/toy-lagrangian.md` "Chunk 3 results (2026-10-19): S4, quantum stability" — the tag on quantum restoration.
- `notes/geometric-core.md` §C, §E, `notes/x-classification.md` §1–§4, `notes/tuning-test.md` §2–§4, `notes/beta-coefficients.md` §1–§3 — the tags of calc notes #5–#8.
- `notes/stream-stability.md`, `notes/wave-island.md` — the tags of the clumping results.
- `notes/broken-born-theory.md` §2, §4, §5.1, §6, §7 — τ's assumed lightness, its fifth-force safety, the benchmark, the dictionary and the dark-energy items.
- `notes/broken-born-program-v1.md` §7 — the net theorem's tag.
- `verify/battery.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py`, `verify/soliton_obituary.py`, `verify/phase_space_diameter.py`, `verify/closed_universe.py`, run by `scripts/check.sh` — the machine checks.
- `notes/closed-universe.md` §2–§8 — the closed-universe note's results and tags; computed, not reviewed.
- `review/wiki-build-flags.md` items 27 (addendum), 45–49, 51–53 — the flags from the closed-universe investigation named in the tables; awaiting Paul's ruling.
- `review/wiki-build-flags.md` items 16, 19, 20, 23, 27, 29, 30, 39, 43 — the suspected source errors named in the tables; the flags' audit (2026-10-22) found items 19, 30 and 39 to depend on a convention or a reading and confirmed the others.
- `notes/velocity-gated-gravity.md` §§2, 3, 9 and `notes/gate-mechanism.md` §5 — X between ordinary bodies, the universal gate, the carriers, and flag 55's proposal; `verify/velocity_gated_gravity.py` and `verify/gate_mechanism.py` — the two scripts; `review/wiki-build-flags.md` items 16 (addendum), 55, 56 and 58
