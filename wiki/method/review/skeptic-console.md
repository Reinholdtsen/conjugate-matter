---
title: "The skeptic review console"
weight: 20
status: record
description: "The browser page that sent #14 to a fresh referee with web search and an adversarial prompt in rounds 1–2; it embeds #14 v2, a draft of the withdrawn soliton manuscript."
sources:
  - "review/skeptic-review-console.html"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "review/round3-preregistration.md"
  - "papers/broken-born-checkpoint-v2.md §12"
---

*The skeptic review console is a single HTML page, artifact #15 (`review/skeptic-review-console.html`), that sends a manuscript to a fresh Claude model with no conversation context, an adversarial referee prompt and web search turned on, and prints the review it gets back. It was the tool of review rounds 1 and 2, both on the soliton dark-matter manuscript #14. Its prompt defines the A/B/C verdict scale that the later rounds kept. The referee it calls can search the web but cannot execute code, the limitation behind the referees' arithmetic errors in those rounds. The page embeds #14 version 2 verbatim and is kept as the record of rounds 1 and 2; the proposal in it has since been [retired](/wiki/dark-matter/candidates/soliton-candidate/obituary).*

**Status:** Record — untagged — a tool of rounds 1–2, not used since: rounds 3 and 4 ran as subagents that could execute code (`review/v3-worklog.md`). The handoff's "tool, current" (`HANDOFF.md` §3) is out of date, since the page embeds a draft of the withdrawn #14.

## Key facts

- **What it does**, in the page's own note: it "sends the standalone manuscript (embedded below in code, exactly as in knot-dark-matter-standalone.md) to a fresh Claude instance with **no conversation context**, an adversarial reviewer prompt, and web search enabled for citation checking. The reviewer is told the paper may be AI confabulation and is asked to find out."
- **How it works.** The page calls the Messages API with the model `claude-sonnet-4-6`, `max_tokens: 4000` and the server-side tool `web_search_20250305`, through what the handoff calls "the keyless artifact API route". It starts on page load, continues the same conversation when a response stops on `pause_turn` (the API pausing a long turn that uses the search tool) or `max_tokens`, for at most 12 requests, and has "Re-run review" and "Copy review text" buttons.
- **The referee prompt** opens: "You are a skeptical theoretical physicist refereeing an anonymous manuscript. Important context: the manuscript may have been generated wholly or partly by an AI and may contain confabulated physics dressed in correct-sounding jargon." It asks which of three the paper is: "(A) coherent speculative physics that uses established results correctly, (B) flawed but containing salvageable ideas, or (C) confabulation." This is the scale of [the review protocol](/wiki/method/review/review-protocol).
- **What the referee must check**: whether the references are real and support their use ("use web search"); whether the named theorems ("multi-graviton no-go, Dirac quantization, Kibble mechanism, Parker bound, Hassan-Rosen") are correctly invoked; internal consistency, "especially whether calling the dark sector 'magnetic' while claiming zero coupling to our photon is coherent or a bait-and-switch"; the arithmetic; and "fatal known constraints the authors omitted". It must name "the single weakest link", and is told "Do not be polite; do not grade on a curve." It ends with a verdict, a confidence (low, medium or high) and "one sentence on what would change your verdict".
- **The embedded manuscript** is #14 v2, "Dark Matter as Superheavy Magnetic Solitons of a Spontaneously Broken Phase-Space Duality", which fixed the hidden coupling as "alpha_d = 1/(4 alpha) ~ 34" by a conjectured duality ([obituary of that coupling](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)). The worklog: the console "embeds v2 verbatim. It is kept as the record of rounds 1–2. Round 3 runs as a subagent here, not through the console." #11 §12 records that v2 normalized the Kibble estimate at p = 1, which [round 3](/wiki/method/review/round-3) showed to be wrong ([the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)).
- **Its limitation.** The referee had web search but no code execution. The round-3 pre-registration describes "the arithmetic failure mode of rounds 1–2, which had no code execution" ([the measured failure mode](/wiki/method/review/referee-failure-mode)).
- **Its outputs are not in the repository.** "Paul also holds two referee-report text files (round 1 and round 2 outputs of #15)" (`HANDOFF.md` §3); their verdicts are summarized in [rounds 1 and 2](/wiki/method/review/rounds-one-and-two).

## Sources

- `review/skeptic-review-console.html` — the page itself: its note, the referee prompt, the request parameters and the embedded #14 v2
- `HANDOFF.md` §3 (row 15) — "tool, current"; the keyless route; the two referee-report files Paul holds
- `HANDOFF.md` §6 — the rounds the console ran
- `review/v3-worklog.md` 'v3 as drafted (2026-10-19)' — the console kept as the record of rounds 1–2
- `review/round3-preregistration.md` — the console rounds had no code execution
- `papers/broken-born-checkpoint-v2.md` §12 — v2's p = 1 normalization
