---
title: "The lab notebook (#1) and its addenda"
weight: 30
status: record
description: "Version 0.1 of September 2026, the program's first formal write-up, section by section, and the addenda v0.2–v0.6 that recorded each resolved debt and correction; superseded as a reference, its unedited body still reads dead claims as live."
sources:
  - "notes/broken-born-theory.md §0–§12"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "HANDOFF.md §3"
  - "CLAUDE.md 'Layout'"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "papers/broken-born-checkpoint-v2.md header"
  - "review/wiki-build-flags.md items 1, 6, 10, 17, 18, 23, 25, 27, 31, 39"
---

*The lab notebook, artifact #1, is the program's first formal write-up: version 0.1, dated September 2026, with five postulates, an action, checks against established physics, a predictions table with kill conditions, and a ranked list of open problems. As the first calculations came in, their results were appended as addenda v0.2 to v0.6 rather than edited into the text, so the notebook preserves the order in which the program changed. Because the body was never revised, claims that later died, [momentum-space clumping](/wiki/dark-matter/momentum-clumping/founding-image) among them, still read there as live, and the [original form of postulate P2](/wiki/program/postulates/original-p2), which the first Debt-1 calculation overturned, still stands among its postulates. The notebook was consolidated into the program v1.0 (#9), superseded as a reference by checkpoint #11, and is kept as the audit trail.*

**Status:** Record, superseded as reference — v0.1 uses the tags [P], [D], [T] and [O] only (no [V], † or [S]), and the addenda are untagged — rank 6 in the wiki's precedence order (`wiki/CLAUDE.md`: "#1 and #9 are superseded as reference"); `HANDOFF.md` §3 lists it as "v0.6 — superseded as reference", to be kept for the audit trail. No `verify/` script checks its sections. The file is unchanged since its import on 2026-10-19 (commit 8d588f6; moved to `notes/` in 008c3ee).

## What the notebook is

The file is titled "Broken-Born Theory (BBT)", subtitled "A falsifiable effective framework for spontaneously broken Born reciprocity", with the header "Working title — rename at will. Version 0.1, September 2026." BBT is the notebook's abbreviation for Broken-Born theory. Its §0 sets the level: "This document is written at the rigor level of a phenomenology paper: explicit postulates, an action, derivations where they can be done, and numbered predictions with kill conditions." It adds that it "is **not** a UV-complete quantum gravity", that is, not a theory of quantum gravity valid at all energies.

[The handoff](/wiki/history/documents/handoff) describes it as the "Original rigorous formalization (postulates, action, predictions table) plus addenda v0.2–v0.6 recording each debt payment and correction in sequence. The program's lab notebook." (`HANDOFF.md` §3). Each addendum summarizes working notes that followed: v0.2 the Debt-3 notes #2–#4, and v0.3 to v0.6 the Debt-1 notes #5–#8, one note each. Only v0.1 is dated; the v0.3 addendum is headed "overnight".

The notebook writes its mathematics in LaTeX. Quotations on this page and elsewhere in the wiki transcribe it into Unicode.

## Its standing

Two documents followed the notebook as the program's reference. The program v1.0 (#9) consolidated it with the calc notes, and checkpoint #11 v2.0 "Supersedes #1 and #9" (`HANDOFF.md` §3, row 11; [the checkpoint](/wiki/history/documents/checkpoint)). The root `CLAUDE.md` files it with the other notes as "the audit trail, superseded as reference but kept", and the wiki's precedence order places it at rank 6, below `HANDOFF.md` and above the popular articles.

The notebook is still the only record of the program as first conceived, before any of the debts was resolved, and the addenda are the only record of the corrections in the order they were made. Where a later document states the same result, the wiki cites the later one. Where only the notebook gives a statement or a number, the wiki cites #1 and says so.

## Version 0.1, section by section

### §0, epistemic scope

§0 defines the notebook's tags: "[P] postulate — assumed, with motivation", "[D] derived — follows from the postulates by calculation shown or sketched here", "[T] theorem — established in the literature, cited" and "[O] open — a debt the program owes". The checkpoint later added [V] for machine-verified results and the citation marks † and [S] ([provenance tags and citation marks](/wiki/method/provenance-tags)).

§0 also records a correction made by calculation while the notebook was written: the duality dictionary for cosmological fluids "is w_eff = −w̃, not w_eff = −2−w̃. The correction is what makes the dark-energy sector work. Rigor changed an answer; that is the point of rigor." The heuristic −2 − w̃ had underpinned the idea that the [conjugate universe](/wiki/program/conjugate-universe)'s collapse powers our acceleration ([the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary#superseded-the-earlier-heuristic-rule); [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)).

### §1, postulates

Five postulates, each tagged [P]:

- **P1 (Arena)**: phase space with "a symplectic form ω, a neutral (split-signature) metric η, and a positive generalized metric H, mutually compatible". Under the later P2′, η is no longer fundamental ([P1](/wiki/program/postulates/p1-arena#superseded-the-v01-arena-with-three-structures)).
- **P2 (Rigidity of ℏ)**: "ω and η are non-dynamical; only H carries degrees of freedom." The notebook credits it with "triple duty": it "kills the would-be second graviton (no Boulware–Deser ghost, §6)", "enforces the cosmological constraint a ã = const (§7)" and "supplies the explicit breaking that gives the dark-energy field its potential (§5)". The first calculation of Debt 1 showed that this postulate leaves the program with no content of its own, and it was replaced by P2′ ([Original P2 (superseded)](/wiki/program/postulates/original-p2)).
- **P3 (Reciprocity)**: the action is invariant under the Born rotation ρ: (x, p) → (p, −x) ([P3](/wiki/program/postulates/p3-reciprocity)).
- **P4 (Polarized matter, universal gravity)**: x-polarized Standard Model fields and p-polarized χ fields, both coupled to H; "Gauge interactions do not connect the two representations" ([P4](/wiki/program/postulates/p4-polarized-matter)).
- **P5 (Spontaneous breaking)**: "The vacuum selects a Lagrangian polarization of 𝒫; ours is x-tilted" ([P5](/wiki/program/postulates/p5-spontaneous-selection)).

Some of the section pointers in P2 are off: the potential is in §3, not §5, and the cosmological constraint is derived in §6, not §7 (`review/wiki-build-flags.md` items 10 and 25). The wiki therefore cites the notebook by heading.

### §2, the kinematic core

§2 defines the endomorphisms I ≡ ω⁻¹H, J ≡ η⁻¹H and K ≡ η⁻¹ω, finds "I² = −𝟙, J² = +𝟙, K² = +𝟙, and IJ = K: a split-quaternion (para-quaternionic) algebra", and identifies a compatible triple with a [Born geometry](/wiki/phase-space/born-geometry) in the sense of Freidel, Leigh and Minic [T] ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). The Born rotation preserves ω and H and flips η [D] ([Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)). Hence "The order parameter of the theory is J = η⁻¹H", and "The breaking pattern is ℤ₄ → ℤ₂" [D], a discrete pattern that the [toy models](/wiki/symmetry-breaking/toy-models) of v2.2 replaced with a continuous one ([the order parameter](/wiki/symmetry-breaking/order-parameter#superseded-the-discrete-breaking-pattern)).

It cites "A theorem of Freidel, Rudolph & Svoboda (2018)" for the unique compatible connection [T] ([the Born connection](/wiki/phase-space/born-geometry/born-connection)), and it leaves open the consistency of a section condition "as in double field theory" [O] ([the section condition](/wiki/symmetry-breaking/section-condition#open-the-section-condition-on-curved-backgrounds)). It introduces the vacuum manifold, the Lagrangian Grassmannian Λ(d) ≅ U(d)/O(d), "of dimension d(d+1)/2 = 10 for d=4" [T], its Maslov circle, and the angle τ ≡ f · arg det²(·) that becomes the dark-energy field; periodicity is "topology [D]", and that τ is the lightest modulus "is assumed [P]" ([the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian); [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)).

### §3, the action

The action is S = S_H + S_τ + S_x[SM; g] + S_p[χ; g, g̃] + S_mix, SM being the Standard Model ([the geometric action and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action)). Two of its parts were later replaced:

- **The potential of τ**, V(τ) = V₀[1 + cos(τ/f)]: its periodicity "is forced by the Maslov topology [D]", its existence "comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2)", and "Its *magnitude* V₀ is a free parameter here. [P/O]". The origin in the rigid ω did not survive P2′ ([τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence#superseded-the-potentials-origin-in-the-rigid-ω); [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). Whether this potential can turn negative is unresolved (below).
- **The conjugate-sector amplitude**, the boxed M(k, q) = 4πα̃m_χ/(q² + m_φ²) · e^{−k²/μ²}, with q the momentum transfer and "k = m_χ v_rel/2 the incoming **relative** momentum". The Gaussian gate was a postulate: "Deriving the precise gate shape from S_H + S_mix is open [O]; that the gate exists … is the EFT-level content of 'conjugate matter interacts in momentum space.' [P]", EFT being effective field theory ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate#superseded-the-gaussian-gate-of-v01)). Its exponent and calc note #6's are compared in flag 17 of `review/wiki-build-flags.md`.

### §4, consistency with everything already measured

"GR and the SM. Exact at tree level in the x-sector by construction (P4, P5). [D]", GR being [general relativity](/wiki/gravity/spin-2-fields/general-relativity). The section adds: no linear Lorentz violation, because operators linear in energy are odd under the residual ρ² [D, schematic], with gamma-ray-burst bounds from the Fermi Large Area Telescope (LAT) cited [T] and quadratic effects said to "sit ∼10 orders below current sensitivity", a figure no script backs (a lead, flag 31 in `review/wiki-build-flags.md`; [row 9](/wiki/predictions/photon-dispersion)); fifth-force safety of τ as a derivatively coupled pseudo-Goldstone field [D] ([fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force)); the equivalence principle and lensing for χ [D]; and "Ghost accounting", whose "There is no second independent metric" the v0.4 addendum reversed ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain#superseded-no-second-graviton-under-the-original-p2)). #11 has no counterpart section.

### §5, the conjugate sector

- **§5.1, the scattering law [D].** σ_T(v) = σ₀ e^{−v²/v\*²}, with v\* ≡ √2μ/m_χ (on the √2, see flag 17 in `review/wiki-build-flags.md`) and σ₀ = 16πα̃²m_χ²/m_φ⁴: "An exponential cliff, not a power-law tail", isotropic below v\*. The benchmark fits dwarf cores with σ₀/m_χ ≈ 30 cm²/g at v\* ≈ 120 km/s, giving m_χ ≈ 70 MeV × α̃^{2/3}(…)^{−1/3} and μ ≈ 20 keV, and the notebook then "*predicts*, with zero remaining freedom", σ_T/m (300 km/s) ≈ 6×10⁻² cm²/g and σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0. The cliff became a knee in v0.4 ([the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law#superseded-the-exponential-cliff-of-v01); [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark#superseded-the-v01-predictions-from-the-benchmark)).
- **§5.2, "Collective behavior: clumping in momentum space [D at mean-field level; O beyond]".** The founding image: a smooth halo fragmenting "into discrete velocity streams of width Δv ∼ v\*", condensed cores and suppressed dynamical friction. It names the growth rate γ against orbital phase-mixing as "the theory's most important undone calculation on the astrophysics side". That calculation became Debt 3 and killed the image ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image); [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model#superseded-racing-stream-growth-against-orbital-stirring)).
- **§5.3, relic abundance [O].** A light, strongly self-coupled sector connected to ours only by gravity "cannot freeze out thermally without cannibalism problems", so "the abundance must be set asymmetrically — by *polarization-genesis* (§8)" ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)).

### §6, cosmology I: the constraint and the corrected dictionary

From the rigidity of ω, "each mode occupies (aã)³ × (comoving cell) = ℏ³", so a ã = const ≡ 1 [D]: "This is not an extra assumption; it is the statement that ℏ does not run" ([the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint)). In minisuperspace the dual Einstein term becomes 3H²(M_P² + M̃²a⁻⁶) = ρ, "a stiff-like (a⁻⁶) modification of the effective Planck mass", predicting "a step in G_eff before BBN", Big Bang nucleosynthesis ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology); [row 10](/wiki/predictions/early-universe-step)). The corrected dictionary w_eff = −w̃ follows, with its table: dual kinetic energy appears as a cosmological constant, a dual cosmological constant as a stiff fluid, dual curvature as dark radiation, and dust as dust ([the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary)). It finds that "the natural source of a near-constant dark energy is **kinetic energy in the dual frame**" and names τ as "The obvious candidate for a free-rolling field". §7 then places τ near the top of its potential, and no document derives the link between the two pictures ([Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link)).

### §7, cosmology II: dark energy, its drift and the turnaround

Dark energy is τ near the top of its cosine potential, "hilltop axion quintessence", with these consequences:

1. "w ≥ −1 always", since τ is a canonical scalar [D] ([the no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound)).
2. A thawing shape, "w₀ > −1, wₐ < 0, on the standard thawing corridor wₐ ≈ −1.5(1+w₀)", described as "the *sign pattern DESI reports*" [T], DESI being the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) ([τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). That reading is superseded by the phantom crossing in its second data release ([the earlier readings of DESI](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#superseded-the-earlier-readings-of-desi)).
3. The turnaround: "A cosine potential is negative over half its range. Once τ rolls past V = 0, the effective vacuum energy is negative, expansion halts, and slow contraction begins", supported by a [quintessence](/wiki/cosmology/dark-energy/quintessence) fit that finds "a **93.8% preference for a future transition to anti-de Sitter space with eventual cosmological collapse**" [T]; through a ã = 1 the event is the conjugate bounce [D] ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)). As `review/wiki-build-flags.md` item 27 notes, the sentence on the cosine holds for V₀cos(τ/f) but not for the potential of §3, V₀[1 + cos(τ/f)], which is never negative for V₀ > 0 ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)).
4. Parameter economy: "Three measurements, two parameters: one over-constraint. [D]" ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)).

### §8, polarization-genesis [O, sketched]

A sketch of why dark and ordinary matter stand at "Ω_χ : Ω_b = 5.4 : 1": the heavy Grassmannian moduli decay at reheating, with a branching set by the vacuum tilt. "Status: a shape, not a mechanism — the same maturity baryogenesis had in 1966." ([Open: polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)). The year is queried in `review/wiki-build-flags.md` item 18. The sketch needs the nine heavy moduli to exist and decay, while calc note #5 later expects most of them to be eliminated, and no document reconciles the two ([conflicts between sources](/wiki/history/documents/source-conflicts)).

### §9 to §12

- **§9, predictions.** Rows 1–10, each with the standard expectation, the requirement and a kill condition, of which "Rows 1, 3, and 7 are the flagship discriminants". Rows 3 and 4 died with Debt 3, and the numbering changed in v1 ([history of the predictions table](/wiki/predictions/table-history)).
- **§10, parameter count.** Two parameters per sector for [conjugate matter](/wiki/dark-matter/conjugate-matter), dark energy and geometry ([the parameter count, superseded](/wiki/predictions/table-history#superseded-the-parameter-count)).
- **§11, open problems "in order of severity".** Items 1–3 became [the three debts](/wiki/history/debts): "The field equation for H beyond minisuperspace — Born's 88-year debt", the gate-shape derivation, and the stream-instability growth rate. Items 4–6 are polarization-genesis, relic abundance without cannibalism, and "Extensivity (the soccer ball)" ([curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space#open-extensivity-the-soccer-ball-problem)).
- **§12, one-paragraph summary.** It ends with "Two parameters per sector, kill conditions in every row of §9, and three named debts standing between this document and a paper."

## The addenda

Each addendum is a short account of a resolved debt or a forced correction, appended in order and naming its working note.

- **v0.2, "post Debt-3", the resolution of open problem 3.** "Debt 3 is paid, and the answer went against the theory (working notes: debt3a/3b/3c)." On the particle island the mean-field criterion "fails by 28–31 orders of magnitude at the scattering benchmark"; on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) the one mandatory scenario is "falsified by the observed density and longevity of Segue 1-class systems". "**Net:** velocity-space clumping is nowhere a mandatory prediction of BBT. Rows 3–4 are struck from §9 permanently; open problems 3 and 5 close (5 via misalignment production on the wave island)", and the cliff-sharpness island discriminant replaces them. See [the Debt-3 calc notes](/wiki/history/documents/debt-3-notes), [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) and [row 3](/wiki/predictions/island-discriminant).
- **v0.3, "overnight": axiom correction and the modular core.** From calc note #5: "a rigorous compatibility theorem … and with it an axiom-level inconsistency: strict P2 makes the polarization choice discrete", leaving "GR plus one bespoke SIDM model", SIDM being [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter). "**P2 is therefore replaced by P2′:** only ω is rigid (that is ℏ); **η is emergent — the order parameter itself**". The geometry gathers into the modular field Z = X + iY, the gate's mechanism becomes X exchange, and the next step is "the quadratic-order classification of X (healthy / auxiliary / ghost)". See [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes), [P2′](/wiki/program/postulates/p2-prime) and [the modular field Z](/wiki/phase-space/modular-field/modular-field-z). The "discrete" polarizations are queried in `review/wiki-build-flags.md` item 1, and the reading of a·ã = 1 as "the |Z| = 1 locus" in item 23.
- **v0.4: the X classification.** From calc note #6: X is axion-like, a second graviton, excluded as massless, and becomes "a **massive spin-2** with M_X = the polarization-breaking scale"; the geometric sector is "healthy **iff** the η-selection generates a Hassan–Rosen-class potential". Row 1 is amended: "the exponential cliff weakens to a *sharp knee at v\* with tail shape (Gaussian vs rational) diagnosing the vertex completion*". It also opens the X-condensate as a direction ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate)).
- **v0.5: the tuning test.** From calc note #7: "The dRGT tuning test is done" (dRGT being [de Rham–Gabadadze–Tolley massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity)); metric-tier potentials fail, frame-tier ones pass, and "**the theory passes iff formulated in first-order variables, which is the formulation the geometry prefers anyway.**" The picture is [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) "with the second frame confined to the compact moduli space Λ(d)" ([the tuning test](/wiki/gravity/tuning-test)).
- **v0.6: "the β coefficients — Debt 1 closed".** From calc note #8: the palindrome βₙ = β₄₋ₙ; V(1) = 2T, so a flat aligned vacuum forces "**T = 0 and V(1) = 0 exactly**"; "Parameter count: five → two"; the massless graviton "reciprocity-even" and X "reciprocity-odd" (on the parities under #11 §6's Z → −Z⁻¹, see flag 39 in `review/wiki-build-flags.md`); and "**Born's question now has an answer inside BBT**". See [the palindrome](/wiki/gravity/palindromic-branch/palindrome), [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) and [Born's answer](/wiki/gravity/momentum-graviton/borns-answer). Its phrase "by symmetry rather than tuning" is queried in `review/wiki-build-flags.md` item 6, and its "Debt 1 closed" is stronger than #8's own "structurally paid".

## What is superseded

The body of v0.1 was never edited, so it still states, as live:

- **the original P2** and **the triple duty** (§1), replaced by P2′ in v0.3;
- **η as a fundamental structure** (§1, §2) and **the discrete breaking ℤ₄ → ℤ₂** (§2);
- **the potential's origin in the rigid ω** (§3);
- **the Gaussian gate as a postulate** and **the exponential cliff with its predictions** (§3, §5.1), replaced by X exchange and the knee in v0.3–v0.4;
- **momentum-space clumping** (§5.2) and **rows 3–4** (§9), dead since v0.2;
- **"no second independent metric"** (§4), reversed in v0.4;
- **DESI's sign pattern as support** (§7), superseded in #11 v2.1.

The replacements are collected on [superseded statements](/wiki/status/superseded), and the dead claims, each with its obituary, in [the graveyard](/wiki/status/graveyard).

## What the wiki flags

- **Suspected errors inside the notebook**, quoted as written and listed in `review/wiki-build-flags.md`: item 10 and item 25, the section pointers of §1; item 18, "1966"; item 27, the sign of the potential; item 6, v0.6's "by symmetry rather than tuning"; item 17, the gate's exponent and the √2 in v\* ≡ √2μ/m_χ, compared with calc note #6; item 31, a lead rather than a confirmed error, on the "∼10 orders" of §4, which no script backs; and item 39, the parities that v0.6 carries over from calc note #8, which hold for reciprocity as the frame exchange and not under #11 §6's Z → −Z⁻¹. The flags' audit (2026-10-22) found items 17, 31 and 39 to depend on a convention or a reading, left item 18 unclear because the usual dating rests on model memory, and confirmed the rest.
- **Conflicts with other documents**, on [conflicts between sources](/wiki/history/documents/source-conflicts): the year of the Freidel–Rudolph–Svoboda theorem (2018 here, 2019 in #11); the two forms of the gate; dual kinetic energy against τ's potential; the sign of V(τ); the reach of the closure of the notebook's open problem 5, relic abundance; and the row numbers, which the Debt-3 notes share with §9 but #9 and #11 do not.
- **Numbers found only here.** μ ≈ 20 keV and the two predicted cross-sections of §5.1, and the "93.8%" of §7, appear in no later document and in no `verify/` output. The wiki cites them as the notebook's and unverified ([the iron rule](/wiki/method/verification/iron-rule)).

## Sources

- `notes/broken-born-theory.md` — the notebook: v0.1 §0–§12 and the addenda v0.2–v0.6, cited by heading
- `HANDOFF.md` §3 rows 1 and 11 — its description and standing, and #11 "Supersedes #1 and #9"
- `CLAUDE.md` 'Layout' — "the audit trail, superseded as reference but kept"
- `wiki/CLAUDE.md` 'The wiki is derivative' — its rank in the precedence order
- `papers/broken-born-checkpoint-v2.md` header — "Supersedes v2.1, v2.0 and v1.0"
- `review/wiki-build-flags.md` items 1, 6, 10, 17, 18, 23, 25, 27, 31 and 39 — suspected errors in statements the notebook makes or shares, and one lead, with their audit verdicts
