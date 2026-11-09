# conjugate-matter

The Comatter program: a speculative physics research program built on
spontaneously broken Born reciprocity. It was developed with Claude on claude.ai
in September–October 2026 and continues here. Status: a Lakatosian research
program, not a theory. Until 2026-10-26 it was the Broken-Born program (BBT).
The records (`HANDOFF.md`, `notes/`, `review/`, `verify/`) and all file names
keep the old name; current documents, the wiki and the site use the new one.

**Read [HANDOFF.md](HANDOFF.md) first.** It is the project's state at the move
from claude.ai: what is alive, dead and open (§2; its dead list is overtaken, since
none of it is dead after 2026-10-29), results that exist only in
the old chat (§4), review history and the referees' measured failure mode (§6),
and the ranked next-actions queue (§8). Its §3 numbers the artifacts; the map
below gives their paths.

## Layout

- [wiki/papers/](wiki/papers/) — current references only, published in full on the site at `/wiki/papers/`, as written. Until 2026-11-06 they were in `papers/`. They are the record, not wiki pages: each has Hugo frontmatter (title, weight, `status: record`, description) in place of its `# H1`, and `scripts/check-wiki.py` gives them only the checks that keep the site sound (`RECORD_DIRS`).
  - #11 `broken-born-checkpoint-v2.md` — **the current reference for the full program.**
  - #13 `conjugate-special-relativity.md`
  - `reciprocity-toy-models.md` — the toy-Lagrangian note: two models of spontaneously broken ρ. Blind-review format. Round 4: B; v2 applies the revisions. The worklog is `notes/toy-lagrangian.md`.
  - `phase-space-diameter.md` — the phase-space-diameter note: the size of the universe in position and in momentum. Round 5: B; v1.1 applies the revisions. The worklog is `notes/phase-space-diameter-worklog.md`.
- [popsci/](popsci/) — #10 `angle-of-the-mirror.md`, #12 `universes-other-half.md`.
- [notes/](notes/) — the audit trail, superseded as reference but kept.
  - #1 `broken-born-theory.md` — the lab notebook, addenda v0.2–v0.6.
  - #2–#8 calc notes: #2–#4 `stream-stability`, `wave-island`, `ufd-endpoint` (the clumping problem);
    #5–#8 `geometric-core`, `x-classification`, `tuning-test`, `beta-coefficients` (the field-equation problem).
  - #9 `broken-born-program-v1.md` — superseded by #11.
  - #14 `knot-dark-matter-standalone.md` — v3, **withdrawn** after failing round-3 review.
  - `closed-universe.md` — the closed-universe note (2026-10-27): what k = +1 implies for the program, and how big position space and how small momentum space get. Computed and verified by independent agents; not reviewed. Its record is `review/closed-universe/`.
  - `velocity-gated-gravity.md` — the momentum-gravity note (2026-10-28): whether the velocity-clumping obituary is premature, and whether momentum gravity is a relative-velocity perturbation of gravity. Computed and verified by independent agents; not reviewed. Its record is `review/momentum-gravity/`.
  - `gate-mechanism.md` — whether exchanging X produces #11 §8's dark-matter gate (2026-10-28). Two derivations, the second blind; not reviewed. Its record is `review/momentum-gravity/`; its result is flag 55.
  - `literature-check.md` — the literature check of P.R.'s conjectures (2026-11-02): which of seven are already published. Searched and verified by independent agents; not reviewed. Its record is `review/literature-check/`; its results for #11 are flags 64–69.
  - `dual-sector.md` — the dual-sector note (2026-11-06): what Minic and coauthors published on dark matter as the
    dual of visible matter, and where it meets P.R.'s conjectures. Read and verified by independent agents, weighed by
    a panel; not reviewed. Its record is `review/dual-sector/`; its results for #11 are flags 70–73 and an
    addendum to flag 64.
- [review/](review/) — #15 `skeptic-review-console.html`; referee reports and adjudications go here. The monopole sweep's record (2026-10-29) is `review/monopoles/`; the wiki clean-up's (2026-11-01), with the source conflicts no flag covers, is `review/wiki-cleanup/`; the literature check's (2026-11-02) is `review/literature-check/`; the dual-sector investigation's (2026-11-06) is `review/dual-sector/`; the relative-links change's (2026-11-07), with its three audits, is `review/relative-links/`.
- [verify/](verify/) — `battery.py` (HANDOFF Appendix A); `soliton_obituary.py` (the round-3 record); `toy_*.py` (the toy note); `phase_space_diameter.py` (the diameter note); `closed_universe.py` (the closed-universe note); `velocity_gated_gravity.py` and `gate_mechanism.py` (the momentum-gravity notes); `literature_check.py` (the literature-check note: its quotations, citations, verdicts and main counts against its record, and in section G the algebra behind flag 66); `dual_sector.py` (the dual-sector note: its quotations, citations, dates and counts against its record, and the quotations of its flags and wiki page); arbitration and audit scripts go here.
- [wiki/](wiki/) — the program's wiki: one page per topic, explaining and indexing everything above, with each page's status and sources in its frontmatter. It is derivative: when it and a document disagree, the document wins. The one exception is `wiki/papers/`, which holds the papers themselves. Its conventions are in `wiki/CLAUDE.md`. Its executive summary, `wiki/summary.md` (first in the site menu), gives the program's standing on one page, at most 800 words, and must be updated in the same change whenever what it says changes (`wiki/CLAUDE.md`, "Keeping it current").
- [site/](site/) — the Hugo site (hugo-book theme) that publishes `wiki/` to Cloudflare Workers static assets. It mounts `../wiki` as its content and holds no copy of it. Paul deploys it by hand: `npx wrangler login` once per machine, then `npm run deploy` in `site/`, which runs the site's gate first. It serves at https://comatter.science/. Building, checking, previewing, deploying and adding a domain are in `site/CLAUDE.md`.

Read order for a fresh session: #11 → HANDOFF §6 →
[review/round3-adjudication.md](review/round3-adjudication.md) → calc notes
only as a task needs them.

**Since the handoff (2026-10-19):**

- #14 went to v3, failed round-3 review (verdict C) and was withdrawn. The
  superheavy soliton candidate in HANDOFF §2 is **dead** as a program-native
  proposal. The framework is merely compatible with known PeV-scale
  topological dark matter (prior art). (Narrowed 2026-10-29: this covers #14's
  model, which used ordinary kinematics; the candidate it modeled, conjugate
  monopoles localized in momentum, is P.R.'s open conjecture, #11 v2.4 §12.)
- Strict sector separation (P4 at face value) is in force.
- #11 is now v2.1: soliton obituary (§12); compatibility theorem re-tagged
  [T] (Freidel–Leigh–Minic); P4 strict (§4); DESI DR2 favors a phantom
  crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The
  dark-energy sector is under real pressure ahead of DR3.
- The toy Lagrangian (HANDOFF §8 item 4) is done to the referees' wording;
  see `wiki/papers/reciprocity-toy-models.md` and #11 v2.2 §14 item 11. Its open
  ends:
  - a Monte Carlo with H dynamical;
  - a derivation of the ρ-preserving potential;
  - the strong form of matter locality;
  - the real Grosse–Wulkenhaar model's one-loop preference for the
    position-sharp vacuum, a lead.
- The phase-space-diameter note (HANDOFF §8 item 7) is done:
  `wiki/papers/phase-space-diameter.md` v1.1, round-5 verdict B
  (`review/round5-adjudication.md`). Its results:
  - the chat-only relation is standard physics: D_x·D_p = κ h N^{1/3} is
    an identity of blackbody statistics, constant for a fixed comoving
    region; a·ã = 1 is its one-cell form, and none of it tests the program;
  - "square exactly at the bounce" is withdrawn (obituary in §6; under Paul's review since 2026-10-29, not
    dead, note v1.2);
  - the self-dual length √(l_P L) ≈ 50 μm is prior art (Freidel,
    Kowalski-Glikman, Leigh and Minic 2023, among others), and the program
    can use it neither as #13's Born length nor as X's range;
  - new bound: in the program's aligned bimetric vacuum (background ratio
    u = 1), X's range is below 37.7 μm, M_X c² > 5.2 meV.
- 2026-10-26: the program is renamed Comatter (formerly Broken-Born, BBT).
  #11's §13 column "Broken-Born requirement" is now "Program requirement".
  Where the wiki quotes a record that says BBT, it glosses BBT as Broken-Born
  theory, the program's earlier name.
- 2026-10-27: the closed-universe note (`notes/closed-universe.md`, Paul's question; not reviewed). Its
  results:
  - nothing derives closure, but with V₀[1 + cos] ≥ 0 a turnaround (row 5) exists only if k = +1. In the
    program's model class the data disfavour closure at about 2σ; w₀wₐ+Ω_K is the wrong proxy;
  - position space: lower bounds only. At 95% given closure, R_max > 1.2×10⁵ Gpc and t_turn > 6×10⁵ Gyr;
  - momentum space: the fibre stays flat (k̃ = 0), and closure only makes momenta discrete. At the
    turnaround the momentum scale is below 1.1×10⁻³ of today's;
  - on T*S³ only the position polarization is integrable (the critic's result, one agent), so if the
    section condition requires integrability, P5's mirror vacuum has no global form;
  - flags 45–54 and a flag-27 addendum in `review/wiki-build-flags.md`. Flag 49: the dual
    Einstein–Hilbert term behind #11 §10's a⁻⁶ step is not derived.
- 2026-10-28: the momentum-gravity notes (`notes/velocity-gated-gravity.md`, `notes/gate-mechanism.md`;
  Paul's question of 2026-10-26; not reviewed). Their results:
  - the clumping obituary is not premature. It tested the program's contact-range gate on all three branches,
    and it says clumping is required nowhere, not that it is impossible (on 2026-10-29 Paul did not concur in
    the death: the founding image is his open conjecture, #11 v2.5 §9);
  - between ordinary bodies, in the aligned vacuum (u = 1) and unscreened, X is a Yukawa term of range below
    37.7 μm. Its dependence on relative velocity is the O(v²/c²) spin-2 factor, 1 + 2.40×10⁻⁷ at 120 km/s, not a
    gate. A relative-velocity gate acting on all bodies is bounded to |ε| < 8.7×10⁻⁹ (gate widths
    v* = 0.2–2100 km/s);
  - a long-range attraction among χ gated in relative velocity (Paul's picture) is outside the record: no field
    carries it. At v* = 120 km/s the Lyman-α forest allows ε < 0.057–0.106 (record's reading; a compressed
    estimate), clumping needs ε > 1 at every gate width, and cores would need G̃/G ≈ 3.6×10³¹, so it would be
    decorative. Narrow gates (v* < 30 km/s) are narrowed, not closed;
  - #11 §8's gate mechanism is not derived: exchanging §7's X gives a polynomial of degree two in k² with
    velocity scale c. Flag 55 suggests [P] for the gate and μ, [O] for the mechanism; it awaits Paul's ruling,
    and #11 is unchanged until then;
  - flags 55–58 in `review/wiki-build-flags.md`.
- 2026-10-28: #1's three most severe open problems are named by subject everywhere: the field-equation
  problem (1), the gate problem (2) and the clumping problem (3), together the three main problems. Commits
  before this date, and git history, call them Debt 1–3. No payment or ledger wording is used.
- 2026-10-29: the monopole discussion (Paul's questions of 2026-10-28 and 2026-10-29; a sweep of the record by
  nine agents, `review/monopoles/`; flags 59 and 60 accepted by Paul, 61 applied under his instruction to update
  the repo, 62 pending). #11 is now v2.3. Its results:
  - the monopole explanation stays dead, on restated grounds (flag 59). The null result is expected under
    several standard histories, inflation after a unification transition among them, so it lends the program
    no support; inflation is the standard account, not an observed epoch. Only the shared-photon form of the
    conjecture below contests "wrong duality", and whether that form would reopen the explanation is flag 62,
    Paul's to rule;
  - Paul's magnetic-mirror conjecture is #11 §11.4 [O] (flag 60): momentum matter is similar to position matter,
    each electrically charged x-polarized particle having a magnetically charged p-polarized analog. It joins
    founding suppositions 5 and 11. #14 v2 stated a related identification, the momentum-polarized sector as the
    S-dual image of the electric sector, which it called load-bearing for its dual coupling;
  - the wiki's obituary of the magnetic identification is reversed, because no review or document had killed
    it. Paul withdrew the worklog's decision F2 of 2026-10-19 ("S-duality is no longer what fixes α_d") as
    "probably confusion on my part"; F2's arithmetic finding stands. #14 stays withdrawn;
  - the conjecture's shared-photon form, magnetic charge of our own photon, conflicts with P4 as written. Localized
    in position at dark-matter density, such objects would exceed the Parker bound at #14's benchmark masses
    (not gated), so this form needs something to hide them, p-localization or binding into magnetically neutral
    composites, and nothing has shown either;
  - the polarization manifold has π₁(Λ(4)) = ℤ and π₂(Λ(4)) = ℤ₂ (for d = 4 and a global U(4)), so selecting the
    polarization can leave strings of τ and, where the order parameter ranges over the whole manifold, point
    defects of the program's own order parameter (flag 61; #11 §14 item 12). `verify/closed_universe.py`
    section F now gates the homotopy.

  (Overtaken later the same day: flag 62 ruled option B; #11 is v2.4; the explanation is open, P.R.'s
  conjecture. See the next entry.)
- 2026-10-29, later the same day: Paul's direction on deaths (see 'Method'). His words in full: "I think you
  prematurely killed off the most interesting parts of the comatter conjecture: that dark matter is conjugate
  (momentum) matter; and that magnetic monopoles exist in abundance in momentum space. Yes, I know
  electric/magnetic and space/momentum are different dualities. Also, conjugate gravitational collapse drives
  positional expansion acceleration. Don't kill them off unless theory and data kill them off and you ask me
  explicitly that I concur. Do not hide the killing in a massive change." #11 is now v2.4, and three of his
  founding ideas are open conjectures again [O]. None was killed by theory and data in general, and he concurred in none of
  the deaths:
  - dark matter is conjugate (momentum) matter: alive throughout (App. A item 4). Its momentum-localized form
    returns with the next item;
  - magnetic monopoles abundant in momentum space: a third dark-matter candidate again (#11 §12). #14's model
    used ordinary kinematics and never tested it; the model's failure stands. Retiring the candidate was a
    delegated decision (round-3 Decision 2, now narrowed). Their explanation of the monopole null result is
    open too (flag 62, ruled option B);
  - conjugate collapse powering our accelerating expansion (App. A item 9): the corrected dictionary's dual
    stiff ↦ Λ keeps a route. Two versions failed: the heuristic w = −2, excluded by data, and dual dust,
    which maps to dust.
- 2026-10-29, Paul's answers to the concurrence questions (#11 v2.5):
  - #14's ordinary-kinematics model of the third candidate: dead, with his concurrence (§12; round-3
    Decision 2's note);
  - the two failed versions of App. A item 9 (w = −2; dual dust): not concurred. They are failed versions of an
    open conjecture, not deaths (§10);
  - the founding image, matter clumping in momentum space (App. A item 3): not concurred. It is his open
    conjecture again, with the evidence of §9 stated in full;
  - every other death recorded before 2026-10-29: "Restore all pending". Each is under review, not dead, until
    he reviews it with Claude. They are: Scenario A; six pieces of #14's model (the Kibble normalization, the ψ
    relic window, the dimension-five operator, the hidden SU(2) → U(1) sector, α_d ≈ 34 via our photon, the √N
    floor); Fornax friction suppression; velocity-space granularity in halos; the self-dual length as a
    program scale; the square rectangle at the bounce; and the naive ρ-preserving potential.
    Hypothesis H, the third way #14 fixed α_d ≈ 34, is under review with that coupling, though the list does not
    name it: it was recorded dead as a component of #14 v3 when the model failed, no ruling addressed it by
    itself, and a failed model is not the death of each idea in it ('Method').
  - Found on 2026-10-30, after the answers: one more death recorded before 2026-10-29, the closed-universe note's
    symmetric reading of a compact momentum space (k̃ = k, §4), recorded on 2026-10-27 as "dead unless Paul adds a
    compact momentum space deliberately". The list of twelve was taken from the wiki's graveyard, which never held
    it. His answer for every other death recorded before 2026-10-29 covers it, so it is under review too.
- 2026-11-01: the wiki's voice (Paul, 2026-10-30: "This argument between you and me has no place in this wiki."). No claim's
  status changed. The record is `review/wiki-cleanup/`. Its results:
  - pages state what a claim is, what supports it, what weighs against it and where it stands now, and not how a status came
    about (`wiki/CLAUDE.md`, Voice). The rule on deaths under 'Method' stands: it governs how a status changes, and pages do not narrate it;
  - `wiki/summary.md` is one page; "Is anything new?" leads with Paul's conjectures, and it lists no dead claims or claims under review;
  - `scripts/check-wiki.py` gained the checks `status`, `voice` and `summary`;
  - the source documents keep their wording, including #11's header, §9, §10, §12, §13 and App. A, which still narrate this.
- 2026-11-02: the literature check of P.R.'s conjectures (Paul: "Do a literature check of my conjectures";
  `notes/literature-check.md`, written up 2026-11-03; 31 agents in four workflows, not reviewed). No claim's status
  changed: prior art kills nothing and confirms nothing. Its results:
  - dark matter is conjugate matter (App. A item 4) is published in its core. Minic and coauthors have identified dark
    matter with the degrees of freedom dual to visible matter in Born-reciprocal (metastring) string theory since 2020
    (Minic 2020; Berglund, Hübsch and Minić 2021; restated to April 2026, and in October 2026, after the program's first
    statement of it in September 2026). Their dual sector is correlated with ours. (The 2026-11-06 entry qualifies
    the date, "identified", "correlated" and the vacuum as a difference; "neither form" stands.)
    The program's couples by gravity alone (P4 strict, row 7; not in §11.4's shared-photon form, which needs P4
    restated, flag 63), with the polarization selected by the vacuum, and
    neither its χ form nor its monopole form was found in the literature;
  - the magnetic mirror (§11.4), conjugate collapse and our acceleration (App. A item 9) and clumping in momentum
    space (App. A item 3) are partly anticipated: magnetic dark sectors without the momentum placement; a contracting
    partner universe, and collapse in one frame as acceleration in another; Bose condensation of dark matter;
  - monopoles abundant in momentum space, their explanation of the null result and the long-range velocity-gated
    attraction were not found. The closest account of the null result, Khademi 2009, is read only in its abstract
    (the repository refuses access): it puts the non-visibility of monopoles down to uncertainty in phase-space
    quantum mechanics, without saying where they are; two judges labeled it related, and its full text could raise
    the verdict. OpenAlex queries planned for round 3 did not run once its free quota ran out; a rerun on 2026-11-03
    found the quota not yet renewed (`review/literature-check/round5/not-run-queries.json`);
  - flags 64–69 in `review/wiki-build-flags.md`, pending: prior art #11 does not cite (64 for App. A item 4, 65 for
    §11.4, §10 and App. A items 3 and 9); §10's dictionary is, as a map of fluid variables, scale-factor duality with sources (66); §11.3's bridge is a
    published remark (67); Brümmer et al. (arXiv 2025, before #14 v3; Phys. Rev. D 2026) published §12's exclusion of the minimal
    hidden sector first, independently (68);
    two fits mildly prefer a nonzero cross-section at cluster speeds, against row 1's "zero cluster signal" (69);
  - `verify/literature_check.py` checks the note's quotations, citations, verdicts and main counts against
    `review/literature-check/`, and in section G the algebra behind flag 66; two reviews of the write-up,
    a check of the edits merged by hand and a last sweep (2026-11-03; `review/literature-check/workflows/workflow5-result.json`,
    `workflow7-result.json` to `workflow9-result.json`) changed no verdict.
- 2026-11-03: symbols defined where they are used (Paul: "I keep seeing values of w and no definition of w"). No
  claim's status changed. w (the equation of state, pressure divided by energy density), w₀, wₐ and z (redshift) are
  defined in words beside their first use on every wiki page, and `scripts/check-wiki.py` gained the check `symbol`
  (`wiki/CLAUDE.md`, 'Symbols'). #11 and the phase-space-diameter note gained notation items without a change of
  version: #11's header and §10's technical record, the note's header and §7.
- 2026-11-06: the dual-sector investigation (Paul, of the summary's sentence "Its core is published (Minic and
  coauthors, 2020), their sector correlated with ours; neither form was found.": "Please investigate the highlighted
  claim more thoroughly. Create a page for it at the minimum, especially if the claim is true that there is overlap
  between our conjectures and theirs. Also, whenever referenced include a link to the paper itself if possible.";
  `notes/dual-sector.md`; 27 agents in three workflows, then 8 that carried the findings into the record, one that
  linked the papers, and 12 that finished the propagation and reviewed the whole change; not through a blind review
  round). No claim's status changed. Its results:
  - the core of C1 is published, as a proposal never derived: Minic's talk of 9 September 2019 (slides public),
    Minic 2020 §5–§6.2 (posted 29 February 2020), restated by him and coauthors to April 2026. Where the group builds
    its dark sector, its dual is a coordinate of a doubled phase space at the string length, with a momentum of its
    own; in its quantum-mechanics papers it is momentum rescaled at ℏ. Earlier papers (2016–2017) proposed only that
    non-local quanta of quantum gravity make up dark matter. Whether C1's substance includes the program's one phase space at ℏ
    and strict P4 stays Paul's reading (note §2);
  - "correlated with ours" holds for most of the group's papers, beyond leading order in the string length and of
    uncomputed strength; at leading order the sectors are independent, and Hübsch and Minic 2024 §5.3 have gravity
    alone below about 4.5×10¹⁴ GeV. The group explains past nulls and expects detection; the program requires a
    permanent null (row 7);
  - neither form was found, inside the group or outside it;
  - beyond C1, published before the program: a breaking tied to the choice of polarization "at the level of the
    vacuum sector" (Freidel, Kowalski-Glikman, Leigh and Minic 2021), for a dual Lorentz symmetry that is not a
    canonical transformation; U(d)/O(d) as the space of η-choices and η = HJ (Freidel, Leigh and Minic, 2013–2016);
    the positive form of #11 §5's compatibility statement (2016); inverse scalings like a·ã = 1; dark energy from the
    dual space, with both signs of 1 + w. Not found: the spontaneous breaking of the exact ρ with η as order parameter
    and a potential;
  - outside the group, Winn (arXiv 2012; talks and posters of 2025–2026) gives every charged Standard Model particle a
    magnetically charged partner under our own photon, bound into neutral composites as dark matter: partial for the
    magnetic mirror's shared-photon form (C4; in the verifier's words a close variant), without the momentum
    placement, and related to C1, C2, C3 and C6 (flag 73). A sweep of conference abstracts found the identification,
    in its phase-space sense, only in the group's talks, and neither form;
  - flags 70–73 in `review/wiki-build-flags.md`, pending, and an addendum to flag 64; the wiki page
    `wiki/dark-matter/conjugate-matter/dual-standard-model.md`; corrections to `notes/literature-check.md` (header,
    §2–§6, references), the summary and the pages that carried the claim;
  - Paul's link request is applied wiki-wide: every arXiv, DOI and handle identifier in the wiki is a link to the
    paper, and author–year citations of verified papers are linked at first mention. `scripts/wiki-papers.tsv`
    registers each linked paper (built online by `scripts/wiki-papers.py`), and `scripts/check-wiki.py` gained the
    check `paper` (`wiki/CLAUDE.md`, Links);
  - `verify/dual_sector.py` checks the note's quotations, citations, dates and counts against `review/dual-sector/`,
    the quotations of the wiki page and of the flags, and in section F the bracket behind "twice the dimension".
- 2026-11-06, later the same day: the papers published on the site (Paul: "Move the papers under the wiki directory so
  they show up on the public website"). No claim's status changed, and no paper's wording. Its results:
  - `papers/` is now `wiki/papers/`. The four serve at `/wiki/papers/<name>/`, linked from `wiki/papers/_index.md`
    (last in the menu), the home page's map and the documents register;
  - each paper's `# H1` became its frontmatter title, beside weight, `status: record` and a description; ten unescaped
    `v*` (nine in #11, one in #13) are written `v\*`, which renders the same;
  - every path to them is rewritten to `wiki/papers/…`, 3,209 in 389 files. Git refs into old commits
    (`d9a06ac:papers/…`), #14's old path and accounts of searches made over `papers/` keep the old name.
    `git log --follow` gives a paper's history across the move;
  - `scripts/check-wiki.py` treats `wiki/papers/` as the record (`RECORD_DIRS`): the papers get the checks that keep
    the site sound (link, anchor, heading, map, source, frontmatter, weight, section, star, h1, fence) and not the
    wiki-page rules (sources, gist, statusline, status, voice, summary, acronym, symbol, paper); `scripts/check-site.py`
    checks them like every wiki page. `scripts/wiki-papers.py` skips them too;
  - published as written, so the site shows what the wiki's voice rule keeps off its pages: #11's version header
    and §9, §10, §12, §13 and App. A narrate the concurrence questions, the toy note keeps its blind-review header
    ("Anonymous working manuscript submitted for adversarial review"), and † citations, to be checked "before any
    external use", appear unchecked. The repository is public on GitHub, so all of it was published there already;
    the site makes it easier to find. The queue's round-6 review of the toy note was to come "only before any external
    use". Not done: the papers' arXiv and DOI identifiers are not links.
- 2026-11-07: every citation a link (Paul asked why the papers were cited as code paths, then "So why can't everything
  work?", "Why not 4?", "go please"). No claim's status changed, and no wording. Its results:
  - every wiki link is a path relative to its file, replacing the absolute `/wiki/...` form of 2026-10-22, so that one
    link works on the site, on GitHub and in an editor (`wiki/CLAUDE.md`, Links). 17,907 links were rewritten;
  - repository paths are links: 7,514 inline-code paths became links, and the site's link hook
    (`site/layouts/_markup/render-link.html`) sends a path outside the wiki to the file on GitHub at `main`. The
    repository is public. `scripts/check-pushed.sh`, run by `npm run deploy`, refuses unless `main` is committed and
    pushed;
  - section citations are links: 10,967 link their heading. 7,984 name their document directly ("#11 §9", "`notes/x.md`
    §4", "the toy note §2", "checkpoint §7"), 918 continue such a citation ("§9 and §10"), 15 follow it ("§7 of the
    checkpoint"), and 2,050 take the nearest document named earlier on the line. The first mention of each artifact
    number on a page links its document (769). The papers' 15 numbered subsections became `###` headings, so they have
    anchors;
  - 2,714 section citations stay plain text (`review/relative-links/relink-unresolved.tsv` lists the script's 2,713; one more
    was unlinked by hand): outside papers' sections,
    sections inside quotations, sections after an unnamed "note", "paper" or version, bare sections on the documents
    pages and `references.md` (where they mean the page's own subject), and sections no rule settles. An auditor judged
    58 of a sample of 60 resolvable by a careful reader, so most could be linked by a reading pass;
  - three audits by independent agents (`review/relative-links/audit/`; the record is `review/relative-links/`). Before the rules were tightened, 8 of 160 links by
    the two weakest rules were wrong, and a second auditor found 55 more outside its sample; the page-sources rule was
    dropped, and 44 of the 49 cases named were then right or plain. After: 0 of 115 attached, continuation and "of"
    links wrong (95% interval up to 3.2%); 2 of 100 fresh nearest-rule links wrong, so about 41 of the 2,050 (95%
    interval 11 to 144), unidentified. The 4 wrong links named after the change were fixed by hand
    (`review/relative-links/scripts/hand_fixes.py`);
  - GitHub's heading IDs follow `github_slug` in `scripts/check-wiki.py`, checked against GitHub's own anchors for all
    4,555 headings of the repository's Markdown on 2026-11-07. Hugo and GitHub differ only on combining marks (3
    headings), and the gate rejects a link to such a heading. `scripts/check-site.py` checks every GitHub link (11,050)
    against tracked files and GitHub's headings.
- HANDOFF §8 queue item 3 is dropped. The current queue, in order:
  1. HANDOFF §8 items 5–6: the partially-massless comparison and the
     † literature battery (Born 1938 and 1949 were retrieved for the
     diameter note; see its §4).
  2. Optional: a round-6 review of the toy note, but only before any
     external use.
- Reasons for the queue are in the round-3 adjudication's "Decisions"
  section.
- Leads from the diameter note's literature sweep, not queued: Low 2006 is
  prior art for #13's maximum force; Lukierski, Meljanac, Mignemi and Pachoł
  2023 break an algebra containing a continuous Born rotation spontaneously
  in the Yang model, against the toy note's "no explicit model"; Shlivko and
  Steinhardt 2024 and Hur et al. 2025 bear on reading DESI's CPL quadrant
  against strict w ≥ −1; whether the aligned bimetric vacuum persists as the
  universe expands is open.
- Open from the closed-universe note, not queued:
  - derive the dual Einstein–Hilbert term from S_H (flag 49);
  - fit V₀[1 + cos(τ/f)] plus Ω_K to full CMB, BAO and supernova likelihoods;
  - Artigas, Mielczarek and Rovelli 2019 (a compact phase space makes the universe recollapse) is a lead.
- Open from the momentum-gravity notes, not queued:
  - Paul's ruling on flag 55 (the gate's tag), deferred by him on 2026-10-28; and, open either way, whether row 3's island discriminant
    survives;
  - a full Lyman-α likelihood and a nonlinear simulation of narrow gates, if the long-range variant is pursued;
  - whether the Hamiltonian reading is the right classical limit for a long-range gate;
  - whether the program's bimetric branch has Vainshtein screening at all (flag 57).
- Open from the monopole discussion, not queued:
  - the review with Paul of the claims under review, the twelve listed in 'Since the handoff' (2026-10-29), with
    hypothesis H, and the symmetric reading found on 2026-10-30: each stays not dead until he reviews it, and a
    death needs his explicit concurrence, in a change of its own;
  - for the restored candidate and the explanation: p-localization, and the kinematics of momentum-polarized
    matter, never modeled (#14 §1 assumed ordinary kinematics);
  - for App. A item 9: whether the contracting conjugate universe is kinetic-dominated, and how dual stiff ↦ Λ
    relates to τ's potential; in contraction anisotropy grows like a stiff fluid and dominates contents with w < 1,
    while the dictionary is derived for isotropic fluids (Erickson et al. 2004; `notes/literature-check.md` §6);
  - a mechanism by which one order parameter selects both the position polarization and the electric sublattice
    (acceptance criterion 1's clause, never attempted);
  - for the separate-photon form, which coupling of the p-sector is the S-image of ours, elementary or magnetic
    (F2's finding), and round 2's supersymmetry-exactness burden, which returns with the withdrawal of F2's decision;
  - for the shared-photon form, p-localization in the field profile and the momentum width that would hide the
    analogs from detectors, from the Parker bound and from the plasma before recombination, or their binding
    into magnetically neutral composites, or screening (Carneiro 2026; `notes/literature-check.md` §5). The Parker
    comparison at general mass is not gated (`knot_numbers.py`
    left the gate);
  - the dual coupling's convention, 1/(4α) or 1/α (`review/v3-worklog.md` R2; the formula in #11 §11.2 is flag 28);
  - whether a transition produced the polarization's point defects and τ-strings, and their fate (#11 §14 item 12).
- Open from the wiki clean-up, not queued (`review/wiki-cleanup/README.md` lists every choice only Paul can make and the
  conflicts in the sources that no flag covers). Three were put to him on 2026-11-02, and he kept them open ("Keep those
  questions open"):
  - "kills outright" (#11 §13 row 4): does a robust intrinsic w < −1 kill the τ sector (#1 §7 item 1, #14 §5) or the
    whole framework (`HANDOFF.md` §2)?
  - "the empty set" (#11 §11.1) or "measure zero" (App. A item 5), both attributed to him, for conjugate monopoles that
    exist and have no effect;
  - χ and the X-condensate have wiki status `alive`, while #11 §12 tags each candidate [O].
- Open from the literature check, not queued (`notes/literature-check.md` §2–§3, §9–§10):
  - Paul's rulings on flags 64–69;
  - which reading of C1, C4, C5 and C6 is his conjecture, on which their verdicts rest (note §2): whether strict P4,
    ordinary momentum at ħ, or interaction or localization in momentum belong to C1 (if so, partly anticipated);
    whether C4 is the momentum placement alone (if so, related only); whether the partner's identity is framework
    for C5 (if so, arguably anticipated for its founding sentence, though never for the kept route); whether C6 is only the founding image of several velocity
    flocks (if so, related only);
  - the full text of Khademi 2009, "Why magnetic monopoles are not seen?" (handle 20.500.12415/6128), two pages that
    could change the explanation's verdict (a CORE download link of unknown content, core.ac.uk/download/287420038.pdf,
    met a bot check and is unread); the 26 OpenAlex and four Semantic Scholar queries in
    `review/literature-check/round5/not-run-queries.json`, to run once the quota renews (00:00 UTC); literature not
    in English, not searched; Castro Perelman's output, read in part;
  - not assessed: Bordes, Chan and Tsou 2018 and Mathur and Sharatchandra 1991 (C4); Szabo 2017, arXiv:1709.10080
    (C2, C3); Comay 1985 (C3, behind a sign-in); the backreaction literature (C5);
  - whether observation can tell the program's dark sector from the Minic school's dual sector: the school names a
    dual photon correlated with ours, correlated accelerator events and the a₀ ∼ cH₀ correlation in galaxies, which
    ΛCDM may also produce, while Hübsch and Minic 2024 have gravity alone below about 4.5×10¹⁴ GeV, so the school's
    position is not single (`notes/dual-sector.md` §5–§6).
- Open from the dual-sector investigation, not queued (`notes/dual-sector.md` §2, §12):
  - Paul's rulings on flags 70–73 and on flag 64's addendum;
  - the full text of Freidel, Leigh and Minic, Int. J. Mod. Phys. A 34, 1941004 (2019), closed access, which may hold a
    written statement of the identification before Minic 2020 (Paul could ask an author for a copy); the Hübsch–Minić
    book *The Weight of Quantum* (2026); Freidel, Leigh and Minic's 2015 essay "Modular spacetime"; talks of 2018–2019
    with no surviving material; outside items read only in their abstracts (note §12); conference venues that refused
    automated access (Fermilab Indico, the APS meeting archive, INFN Indico) and Winn's slides behind bot checks;
  - resting on one agent, the critic, and unseen by the judges: the April 2026 paper's want of a coupling term (a
    search of its text), and the link of Freidel, Leigh and Minic's conversion factor (2014) and gravitational tension
    c⁴/G_N (2016) to #13 (both quotations found by code; the passages themselves were in the panel's evidence).

## The gate

[scripts/check.sh](scripts/check.sh) is the definition of done. It runs every
script in `verify/`, then `scripts/check-wiki.py` on the wiki, and exits non-zero
on any failure. It must pass before work is called finished. Do not weaken a check to make it pass. New verification
scripts get wired into it.

The site's own pre-deploy gate is `npm run check` in `site/`: `scripts/check.sh`,
then the Hugo build, which fails on a link to a missing page, then
`scripts/check-site.py`, which checks every link, asset and `#fragment` in the
built HTML (a GitHub link must name a tracked file and an existing heading), that
every wiki page was built, and that each heading has the ID
`scripts/check-wiki.py` computes. `check-site.py` needs a built site, so it runs
there and not in `scripts/check.sh`. `npm run deploy` then runs
`scripts/check-pushed.sh`, which refuses unless `main` is committed and equal to
`origin/main`, because the site links repository files on GitHub at `main`.
Nothing is deployed with a red check.

First time: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`

## Method (HANDOFF §5)

- Tag every claim: **[D]** derived here, **[T]** literature, **[P]** postulate,
  **[O]** open, **[V]** machine-verified. Citations: **†** from model memory
  (verify against the source before any external use), **[S]** live-searched.
- Iron rule: no arithmetic by eyeball. Every asserted or disputed number gets
  executed code with printed output, kept in `verify/`.
- Pre-register the expected verdict and weakest link before each review round.
  Keep the prediction out of the commit subject: subagents see recent commit
  subjects in their git-status context, and round 3's auditor saw it.
- A verification check confirms arithmetic, not the model. An anchor must be
  independent of the paper (a textbook identity, a published value). A check
  that reproduces the paper's own number is circular. Round 3 caught a wrong
  Kibble normalization that a circular anchor had passed.
- When numerics run on a reduced model (fields frozen), check the unreduced
  model's stability — boundedness, and the Hessian with all fields dynamical —
  and say in the text that it is a reduction. Round 4 found a potential that
  was bounded only at frozen H.
- Monte Carlo numbers need error bars from independent runs. A fixed seed makes
  a number reproducible, not accurate.
- When a result rests on a formula from the literature, carry every parameter
  the cited formula has and state what fixes each one. Round 5 found a dropped
  background ratio in a bimetric coupling.
- A claim about how a quantity behaves over time ("holds at no other epoch")
  needs executed code like any number.
- Report negative results prominently: a failed calculation or a contrary datum is stated in full, where
  the claim is discussed.
- A claim is dead only when theory and data kill it and Paul explicitly concurs. Paul, 2026-10-29: "Don't
  kill them off unless theory and data kill them off and you ask me explicitly that I concur. Do not hide
  the killing in a massive change."
  - Ask him for each death, separately, and record his answer with the date.
  - Make each death its own change, never part of a larger one.
  - Until he concurs, a claim against which theory or data weigh is recorded as open, or as his
    conjecture, with the evidence against it stated.
  - A failed model or version of an idea is not the death of the idea.
  - Paul answered for the deaths recorded before 2026-10-29 on the same day. He concurred only in #14's
    model. Every other one is under review, not dead, until he reviews it (wiki status `under-review`), or
    restored where he did not concur ('Since the handoff', 2026-10-29).

## Working with Paul

- Roles: Paul — conjecture, direction, veto. Claude — derivations,
  counterexamples, drafting, verification. Paper attribution line:
  "conjecture and direction, P.R.; derivations, counterexamples, verification,
  drafting, Claude (Anthropic)."
- Paul is an independent developer (Stanford Ginzton Lab background in scanning
  acoustic microscopy, which is where the Fourier-domain intuition comes from).
  Never describe Paul as retired.
- Paul cannot independently verify most of the technical physics and relies on
  the tags, the machine checks and pre-registration to tell sound results from
  confabulation. Keep that calibration explicit.
- Work in chunks and save state after each one, so a cold session can resume.
  Paul continues with "go".
- Working communication: simple bullets. Make the call and recommend; don't ask
  questions Paul can't answer.
- Science prose: a serious scientist explaining abstract material in plain
  language. No anthropomorphizing, no moralizing, no detective-story reveals.
  Wave/Fourier analogies work; ball-rolling and ledger/bookkeeping metaphors
  don't.
- Papers: every section opens with an italic plain-language passage, then the
  tagged technical record.
