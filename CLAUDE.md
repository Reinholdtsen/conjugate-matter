# conjugate-matter

The Broken-Born program (BBT): a speculative physics research program built on
spontaneously broken Born reciprocity. It was developed with Claude on claude.ai
in September–October 2026 and continues here. Status: a Lakatosian research
program, not a theory.

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
- [popsci/](popsci/) — #10 `angle-of-the-mirror.md`, #12 `universes-other-half.md`.
- [notes/](notes/) — the audit trail, superseded as reference but kept.
  - #1 `broken-born-theory.md` — the lab notebook, addenda v0.2–v0.6.
  - #2–#8 calc notes: `debt3a/b/c-*`, `debt1a-*`.
  - #9 `broken-born-program-v1.md` — superseded by #11.
  - #14 `knot-dark-matter-standalone.md` — v3, **withdrawn** after failing round-3 review.
- [review/](review/) — #15 `skeptic-review-console.html`; referee reports and adjudications go here.
- [verify/](verify/) — `battery.py` (HANDOFF Appendix A); `soliton_obituary.py` (the round-3 record); arbitration and audit scripts go here.

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
- HANDOFF §8 queue item 3 is dropped. The current queue, in order:
  1. HANDOFF §8 items 5–7: the partially-massless comparison, the
     † literature battery, the phase-space-diameter note.
  2. Optional: a round-5 review of the toy note, but only before any
     external use.
- Reasons are in the adjudication's "Decisions" section.

## The gate

[scripts/check.sh](scripts/check.sh) is the definition of done. It runs every
script in `verify/` and exits non-zero on any failure. It must pass before work
is called finished. Do not weaken a check to make it pass. New verification
scripts get wired into it.

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
