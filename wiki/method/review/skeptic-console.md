---
title: "The skeptic review console"
weight: 20
status: record
description: "The browser page (#15) that sent #14 to a fresh referee with web search and an adversarial prompt in rounds 1–2: how it works, the prompt that defines the A/B/C scale, the embedded #14 v2 and what became of its claims, and why it is a record, not a tool."
sources:
  - "review/skeptic-review-console.html"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "review/v3-worklog.md 'Round-2 pending list', 'Findings neither referee raised', 'Verified references for v3', 'v3 as drafted (2026-10-19)'"
  - "review/round3-preregistration.md"
  - "papers/broken-born-checkpoint-v2.md §12"
---

*The skeptic review console is a single HTML page, artifact #15 (`review/skeptic-review-console.html`), that sends a manuscript to a fresh Claude model with no conversation context, an adversarial referee prompt and web search turned on, and prints the review it gets back. It was the tool of review rounds 1 and 2, both on #14, the standalone manuscript proposing superheavy hidden-sector solitons as dark matter. Its prompt defines the A/B/C verdict scale that the later rounds kept. The referee it calls can search the web but cannot execute code, the limitation behind the referees' arithmetic errors in those rounds. The page embeds #14 version 2 verbatim and is kept as the record of rounds 1 and 2; the proposal in it has since been [retired](/wiki/dark-matter/candidates/soliton-candidate/obituary).*

**Status:** Record — untagged. A tool of rounds 1–2, not used since: rounds 3 and 4 ran as subagents that could execute code (`review/v3-worklog.md`). The handoff's status for it, "tool, current" (`HANDOFF.md` §3), is out of date, since the page embeds a draft of the withdrawn #14.

## What the page is

The page's own note describes it: it "sends the standalone manuscript (embedded below in code, exactly as in knot-dark-matter-standalone.md) to a fresh Claude instance with **no conversation context**, an adversarial reviewer prompt, and web search enabled for citation checking. The reviewer is told the paper may be AI confabulation and is asked to find out."

The handoff lists it as artifact #15: "Browser page that sends #14 verbatim to a fresh Claude (claude-sonnet-4-6, web search on, adversarial referee prompt) via the keyless artifact API route; auto-runs on load; copy button. Used for review rounds 1–2." (`HANDOFF.md` §3). It is one of the artifacts of the project's claude.ai period, listed in the inventory the handoff carried to Claude Code.

## How it works

The page holds two constants, the manuscript (`PAPER`) and the referee prompt (`SYSTEM`), and a short script:

- **The request.** It posts to the Messages API with the model `claude-sonnet-4-6`, `max_tokens: 4000`, the prompt as the system message, and one server-side tool, `web_search_20250305`. The first user message is "Referee the following manuscript per your instructions." followed by the manuscript. The request carries no API key; the handoff calls this "the keyless artifact API route".
- **The loop.** A long review can stop before it is finished. If the response stops with `pause_turn`, the stop reason the API gives when it pauses a turn that is using a server tool, the page appends the response and sends the conversation again. If it stops at `max_tokens`, the page appends the response and adds "Continue your review exactly from where you stopped. Do not repeat earlier text. Finish with the required VERDICT line." It sends at most 12 requests, counts the web searches, and reports whether the review completed or "Output above may be partial".
- **The controls.** "Review starts automatically when this page loads." A "Re-run review" button sends a fresh request, and a "Copy review text" button copies the result.

Each run is a new referee: the conversation starts from the prompt and the manuscript alone, so nothing from the project's discussions reaches it. That is what made the review blind ([the blind-review protocol](/wiki/method/review/review-protocol)).

## The referee prompt

The prompt, quoted here as record, opens:

> You are a skeptical theoretical physicist refereeing an anonymous manuscript. Important context: the manuscript may have been generated wholly or partly by an AI and may contain confabulated physics dressed in correct-sounding jargon. You have no other information about its origin.

It asks which of three the manuscript is: "(A) coherent speculative physics that uses established results correctly, (B) flawed but containing salvageable ideas, or (C) confabulation." This is the verdict scale of every later round. The prompt then lists five checks:

1. "whether the cited references are real and support the uses made of them - use web search";
2. "whether the named theorems (multi-graviton no-go, Dirac quantization, Kibble mechanism, Parker bound, Hassan-Rosen) are correctly invoked";
3. "internal consistency - especially whether calling the dark sector 'magnetic' while claiming zero coupling to our photon is coherent or a bait-and-switch";
4. "the arithmetic (abundance, flux, cross-section numbers)";
5. "fatal known constraints the authors omitted".

It requires the referee to "Name the single weakest link explicitly", tells it "Do not be polite; do not grade on a curve.", and asks it to end with a verdict line, `VERDICT: [A/B/C], CONFIDENCE: [low/medium/high]`, "and one sentence on what would change your verdict."

Three features of the later protocol are already here: the A/B/C grade, the confidence and the single weakest link. Three are not: the referee has no code to re-check numbers, there is no independent re-derivation step, and there are no four lists of verified, failed, unverifiable and omitted items. The checks are also written for #14 in particular: the named theorems and the "magnetic" question are #14's.

## The embedded manuscript: #14 version 2

The constant `PAPER` holds #14 v2, "Dark Matter as Superheavy Magnetic Solitons of a Spontaneously Broken Phase-Space Duality", the version that round 2 reviewed. The worklog: the console "embeds v2 verbatim. It is kept as the record of rounds 1–2." The file the page's note names, `notes/knot-dark-matter-standalone.md`, now holds v3, and v2 is otherwise in git history. Version 1, which round 1 reviewed, is not in the repository ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

v2 proposed, in its abstract, "that dark matter consists of superheavy topological solitons of a hidden gauge sector, where the hidden sector is the momentum-polarized half of a spontaneously broken Born reciprocity and is conjectured to be the S-dual image of the electric sector". Its main claims, and what became of each:

- **The coupling.** v2 fixed the hidden sector's coupling "to the image of ours" by "the reciprocity map, acting as the modular S transformation": "alpha_d = 1/(4 alpha) ~ 34, quoted in the Dirac normalization". Round 2 named this derivation the weakest link ("numerology"). While cutting v3, the author found that v2 "uses the weak value in §3 and the strong value in §2 and §4" of the coupling that sets the soliton mass, and v3 dropped S-duality as what fixes α_d (`review/v3-worklog.md`, F2; [obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).
- **The abundance.** v2 used the Kibble estimate n/s ~ p (Λ_c/M_Pl)³ "with p = O(1)" and obtained "a self-consistent Lambda_c ~ 3e11 GeV and M ~ 3e13 GeV". #11 §12 records that v2 normalized at p = 1, and round 3 showed that one defect per Hubble volume gives p ≈ 104 ([obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)).
- **The mass window.** v2: "the window M ~ 1e13 to 1e17 GeV is the Kibble-only estimate", with a benchmark of M = 1e16 GeV. The worklog found instead that "Kibble with p = 1 closes at a single point, M\* ≈ 3.0×10¹³ GeV", and that the observed density at the 10¹⁶ benchmark needs entropy dilution of 1.3×10¹⁰ (F1; [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).
- **Sector separation and kinetic mixing.** v2 postulated that no field carries charge under both sectors, which it said "forbids radiative mixing to all orders in field theory", and held that a mixing ε would give the solitons "an effective magnetic charge epsilon g under our photon". Round 2 found "forbidden to all orders" too strong, and the worklog's literature check found the second premise "wrong for its own setup": with a massless dark photon, mixing gives a dark monopole no ordinary magnetic flux (L1, R4; [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).
- **The flux exclusion.** v2 showed why the solitons cannot be monopoles of our electromagnetism: their flux at dark-matter density "exceeds the Parker bound (~1e-15) [9] by five orders and direct flux limits (MACRO, ~1.4e-16) [10] by six", MACRO being the Monopole, Astrophysics and Cosmic Ray Observatory. Round 2 pointed to the extended Parker bound, and the worklog computed the excess at the 10¹⁶ benchmark as "6.98 orders [V]" (R3; [monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches)).
- **The references.** The worklog's literature report found "v2's [1]–[10] are all correct as cited", with corrections to Kibble's title and to the source for the 10⁻¹⁵ Parker value.

v2 also gave benchmark densities that the round-2 referee misread: "mean number density n ~ 1.3e-22 /cm^3" and, for the local halo, "one soliton per ~25 km^3". The handoff records that the referee "conflated mean vs local density labels (manuscript's 1.3×10⁻²² mean and one-per-25-km³ local are both exactly right)" ([the measured failure mode](/wiki/method/review/referee-failure-mode)).

v2 closed with three acceptance criteria, the first being "exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter". That criterion came from round 1 and outlived #14: it is now [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion), met in the referees' wording by the toy models.

## Its limitation

The referee had web search but no code execution. The handoff's measured result: fresh referees of this kind are "strong on structure, literature and logic; **unreliable on unaided arithmetic**" (`HANDOFF.md` §6). The round-3 pre-registration describes "the arithmetic failure mode of rounds 1–2, which had no code execution", and the protocol that replaced the console gives the referee shell and Python ([the measured failure mode](/wiki/method/review/referee-failure-mode)).

## Why it is a record

The worklog decided the console's role when v3 was cut: "It is kept as the record of rounds 1–2. Round 3 runs as a subagent here, not through the console." Its outputs are not in the repository either: "Paul also holds two referee-report text files (round 1 and round 2 outputs of #15). Their verdicts and the adjudications are summarized in §6, which is sufficient if those files are absent." (`HANDOFF.md` §3). The verdicts were "B / medium" for v1 and "B near B/C / medium" for v2 ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

## Sources

- `review/skeptic-review-console.html` — the page itself: its note, the referee prompt, the request parameters, the continuation loop and the embedded #14 v2
- `HANDOFF.md` §3 (row 15) — "tool, current"; the keyless route; the two referee-report files Paul holds
- `HANDOFF.md` §6 — the rounds the console ran; the measured failure mode; the round-2 referee's misreading of v2's densities
- `review/v3-worklog.md` 'Round-2 pending list', 'Findings neither referee raised', 'Verified references for v3', 'v3 as drafted (2026-10-19)' — what became of v2's claims; the console kept as the record of rounds 1–2
- `review/round3-preregistration.md` — the console rounds had no code execution
- `papers/broken-born-checkpoint-v2.md` §12 — v2's p = 1 normalization
