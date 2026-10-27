# conjugate-matter

The Comatter program: a speculative physics research program built on
spontaneously broken Born reciprocity. It was developed with Claude on claude.ai
in September–October 2026 and continues here. Status: a Lakatosian research
program, not a theory. Until 2026-10-26 it was the Broken-Born program (BBT).
The records (`HANDOFF.md`, `notes/`, `review/`, `verify/`) and all file names
keep the old name; current documents, the wiki and the site use the new one.

**Read [HANDOFF.md](HANDOFF.md) first.** It is the project's state at the move
from claude.ai: what is alive, dead and open (§2), results that exist only in
the old chat (§4), review history and the referees' measured failure mode (§6),
and the ranked next-actions queue (§8). Its §3 numbers the artifacts; the map
below gives their paths.

## Layout

- [papers/](papers/) — current references only.
  - #11 `broken-born-checkpoint-v2.md` — **the current reference for the full program.**
  - #13 `conjugate-special-relativity.md`
  - `reciprocity-toy-models.md` — the toy-Lagrangian note: two models of spontaneously broken ρ. Blind-review format. Round 4: B; v2 applies the revisions. The worklog is `notes/toy-lagrangian.md`.
  - `phase-space-diameter.md` — the phase-space-diameter note: the size of the universe in position and in momentum. Round 5: B; v1.1 applies the revisions. The worklog is `notes/phase-space-diameter-worklog.md`.
- [popsci/](popsci/) — #10 `angle-of-the-mirror.md`, #12 `universes-other-half.md`.
- [notes/](notes/) — the audit trail, superseded as reference but kept.
  - #1 `broken-born-theory.md` — the lab notebook, addenda v0.2–v0.6.
  - #2–#8 calc notes: `debt3a/b/c-*`, `debt1a-*`.
  - #9 `broken-born-program-v1.md` — superseded by #11.
  - #14 `knot-dark-matter-standalone.md` — v3, **withdrawn** after failing round-3 review.
- [review/](review/) — #15 `skeptic-review-console.html`; referee reports and adjudications go here.
- [verify/](verify/) — `battery.py` (HANDOFF Appendix A); `soliton_obituary.py` (the round-3 record); `toy_*.py` (the toy note); `phase_space_diameter.py` (the diameter note); arbitration and audit scripts go here.
- [wiki/](wiki/) — the program's wiki: one page per topic, explaining and indexing everything above, with each page's status and sources in its frontmatter. It is derivative: when it and a document disagree, the document wins. Its conventions are in `wiki/CLAUDE.md`.
- [site/](site/) — the Hugo site (hugo-book theme) that publishes `wiki/` to Cloudflare Workers static assets. It mounts `../wiki` as its content and holds no copy of it. Paul deploys it by hand: `npx wrangler login` once per machine, then `npm run deploy` in `site/`, which runs the site's gate first. It serves at https://comatter.science/. Building, checking, previewing, deploying and adding a domain are in `site/CLAUDE.md`.

Read order for a fresh session: #11 → HANDOFF §6 →
[review/round3-adjudication.md](review/round3-adjudication.md) → calc notes
only as a task needs them.

**Since the handoff (2026-10-19):**

- #14 went to v3, failed round-3 review (verdict C) and was withdrawn. The
  superheavy soliton candidate in HANDOFF §2 is **dead** as a program-native
  proposal. The framework is merely compatible with known PeV-scale
  topological dark matter (prior art).
- Strict sector separation (P4 at face value) is in force.
- #11 is now v2.1: soliton obituary (§12); compatibility theorem re-tagged
  [T] (Freidel–Leigh–Minic); P4 strict (§4); DESI DR2 favors a phantom
  crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The
  dark-energy sector is under real pressure ahead of DR3.
- The toy Lagrangian (HANDOFF §8 item 4) is done to the referees' wording;
  see `papers/reciprocity-toy-models.md` and #11 v2.2 §14 item 11. Its open
  ends:
  - a Monte Carlo with H dynamical;
  - a derivation of the ρ-preserving potential;
  - the strong form of matter locality;
  - the real Grosse–Wulkenhaar model's one-loop preference for the
    position-sharp vacuum, a lead.
- The phase-space-diameter note (HANDOFF §8 item 7) is done:
  `papers/phase-space-diameter.md` v1.1, round-5 verdict B
  (`review/round5-adjudication.md`). Its results:
  - the chat-only relation is standard physics: D_x·D_p = κ h N^{1/3} is
    an identity of blackbody statistics, constant for a fixed comoving
    region; a·ã = 1 is its one-cell form, and none of it tests the program;
  - "square exactly at the bounce" is withdrawn (obituary in §6);
  - the self-dual length √(l_P L) ≈ 50 μm is prior art (Freidel,
    Kowalski-Glikman, Leigh and Minic 2023, among others), and the program
    can use it neither as #13's Born length nor as X's range;
  - new bound: in the program's aligned bimetric vacuum (background ratio
    u = 1), X's range is below 37.7 μm, M_X c² > 5.2 meV.
- 2026-10-26: the program is renamed Comatter (formerly Broken-Born, BBT).
  #11's §13 column "Broken-Born requirement" is now "Program requirement".
  Where the wiki quotes a record that says BBT, it glosses BBT as Broken-Born
  theory, the program's earlier name.
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

## The gate

[scripts/check.sh](scripts/check.sh) is the definition of done. It runs every
script in `verify/`, then `scripts/check-wiki.py` on the wiki, and exits non-zero
on any failure. It must pass before work is called finished. Do not weaken a check to make it pass. New verification
scripts get wired into it.

The site's own pre-deploy gate is `npm run check` in `site/`: `scripts/check.sh`,
then the Hugo build, which fails on a link to a missing page, then
`scripts/check-site.py`, which checks every link, asset and `#fragment` in the
built HTML, that every wiki page was built, and that each heading has the ID
`scripts/check-wiki.py` computes. `check-site.py` needs a built site, so it runs
there and not in `scripts/check.sh`. Nothing is deployed with a red check.

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
- Report negative results prominently. Claims listed as dead in HANDOFF §2 stay
  dead.

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
