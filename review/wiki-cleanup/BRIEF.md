# Wiki clean-up: the rules

Paul, 2026-10-30, on `wiki/summary.md` and the wiki: "The tone sounds like an airing of dirty laundry. This
argument between you and me has no place in this wiki. An executive summary also does not need to list corpses."
He asked for the wiki to be cleaned up and checked for consistency.

## The diagnosis

Three working instructions to Claude were written into reader-facing prose:

1. Paul's rule on when a claim counts as dead, with its quotes, dates, questions and answers.
2. The history of each claim's status: recorded dead, reversed, restored, reviewed, in which version, by whose ruling.
3. Claude's own working conventions ("never describe Paul as retired", what "did not land", "Paul continues with go").

A reader wants the claim, what supports it, what weighs against it, and where it stands. A page tells that.

## The one rule

**A page states what a claim is, what supports it, what weighs against it and where it stands now. It does not tell
how the status came about, who ruled on it, or how the record's wording changed.**

## Hard invariants: a change breaking any of these is wrong

- **No claim's status changes.** Do not change the frontmatter `title`, `weight`, `status` or `provenance` of any page.
  Do not kill, revive, upgrade or downgrade anything. P.R.'s rule stands: nothing dies inside a large change.
- **No evidence is lost.** Keep every physics statement, number, tag ([D] [T] [P] [O] [V], †, [S]), negative result,
  contrary datum, caveat and statement of who or what checked a result ("not reviewed", "one agent", "no script
  checks it", "bounded only at frozen H"). The evidence against a claim stays in full, on its page. Cut only the
  narration around it. If a sentence mixes narration and evidence, keep the evidence and rewrite the sentence.
- **Add nothing.** No new numbers, claims, tags or citations. No commentary on this clean-up, no "the wiki no longer…".
- **URLs do not move.** No file is created, renamed or deleted.
- Only edit the files in your batch.

## What to cut

| Cut | Examples | Write instead |
| --- | --- | --- |
| The dispute over deaths | "concur", "concurrence", "did not concur", "the concurrence questions", "Restore all pending", "probably confusion on my part", "prematurely", "Don't kill them off…", "Paul's rule", "Paul's direction", "Paul's answers", "by his direction", "asked for that death alone" | nothing, or the current standing |
| "Not dead" wording | "not dead", "none of them is dead", "until he reviews it with Claude", "under Paul's review", "under his review", "recorded dead before 2026-10-29 without…" | "under review" |
| Reversal narrative | "recorded dead until", "was an obituary until", "restored", "reopened", "open again", "conjecture again", "returned", "reversed the obituary", "the graveyard listed it until", "this page was…", "since v2.4 it has been", "(v2.4)", "(v2.5)" | the present tense: "P.R.'s open conjecture [O]" |
| Wording history of the record | "Until v2.3 the passage read…", "From v2.0 to v2.4 §9 was titled…", "(amendment 1c80d01)", "#11 §1, until 2026-10-30, said…", "which §2 called … until …" | nothing |
| Decisions told as a story | "Paul narrowed Decision 2", "Paul withdrew F2", "a decision he delegated", "accepted by Paul", "applied under his instruction", "ruled option B" | the decision's current content: "Decision 2 covers #14's model, which used ordinary kinematics" |
| Ruling chatter | "awaiting Paul's ruling", "pending Paul's ruling", "unchanged until Paul rules", "Paul deferred the ruling", "It awaits his ruling" | keep the pointer alone: "(flag 55)", or "(flag 55, pending)" where it matters that it is unresolved |
| Working instructions to Claude | "Never describe Paul as retired", "he corrected this explicitly", "did not land", "glib AI", "continues with go", "Make the call", "do not work for Paul" | nothing |
| Version tags on citations | "#11 v2.5 §9", "#11 (v2.5) does not mention it", "as v2.4 words it" | "#11 §9", "#11 does not mention it" |

Calling a person: write **P.R.**, not Paul, wherever a person must be named ("P.R.'s conjecture", "P.R.'s argument"). A
conjecture stays attributed to P.R. A physics argument of his stays, without its date or the exchange it came from. Two
pages introduce "Paul (P.R.)": `wiki/_index.md` and `wiki/method/collaboration.md`. Literal source-section names in
citations stay as they are ('Working with Paul', 'Recommendations to Paul', `review/...` paths).

Do not quote a source's dispute wording even when the source says it, including #11's "he does not concur" and its
version notes, and the records' status notes. Quote a source only for physics. A quotation that contains both is
paraphrased, or cut at the physics. Do not leave a dangling quote around a removed clause.

The word "dead" is for `status: dead` only, which means #14's model and its own outputs. Elsewhere say what happened: "failed", "the
calculation found", "the evidence against it". "Obituary" is the title of that one page and the name of the script
`verify/soliton_obituary.py`; "the clumping obituary", "the obituary" and "its obituary" elsewhere are stale wording. A
calculation's own result stays when attributed: calc note #4 "Scenario A is falsified by the existence of ultra-faint
dwarfs" is evidence. Keep it, as the note's finding.

## What stays exactly as it is

- Physics corrections recorded as physics: the folded `## Superseded: …` sections, "the original P2", the heuristic
  dictionary w_eff = −2 − w̃, the exponential cliff. Technical refinements labelled by version where the version is
  the subject ("## The v2.2 refinement").
- Folded status headings: `## Open: …`, `## Under review: …`, `## Conjecture: …`, `## Superseded: …`, `## Chat-only: …`,
  `## Popsci-only: …`. Never rename or remove these: registers deep-link them and they show status.
- Calibration: "not reviewed", "computed", "one agent", "no script checks it", "cited from memory (†)", prior art, flag
  pointers ("flag 16 in `review/wiki-build-flags.md`").
- Dated notes as evidence: "`notes/closed-universe.md` (2026-10-27, not reviewed)".
- The page's structure: the italic opening first, then the `**Status:**` line, then its sections, then `## Sources`.

## Canonical wording

- **Under-review page, status line:** `**Status:** Under review — the evidence below weighs against it, and its final
  status awaits review.` Then what verifies it and its tags, unchanged, then "Home section: …; listed in [claims under
  review](/wiki/status/under-review)." Its italic opening ends with the physics; do not mention status history. Keep the section headings "The evidence against it" and "What stands".
- **Under review, meaning (registers, home page):** "the calculations or data weigh against the claim, and its final
  status awaits review".
- **Conjecture page, status line:** `**Status:** Conjecture — [O] — P.R.'s conjecture (#11 §N).` Then the evidence in a
  sentence or two, then what checks it.
- **The dead model, elsewhere:** "#14's model, built with ordinary kinematics, failed on its recomputed abundance
  ([Obituary: #14's superheavy-soliton model](/wiki/dark-matter/candidates/soliton-candidate/obituary))". Its status
  line and the graveyard say "dead". No page says who agreed to it.
- **The rule, once:** the only place the wiki states the rule is one neutral sentence on `/wiki/method/collaboration` and
  `/wiki/method/negative-results`: "A claim is recorded as dead only when theory and data kill it and P.R. agrees." Nowhere else.
- **The third candidate:** "conjugate monopoles localized in momentum, P.R.'s open conjecture"; "#14's model did not
  treat localization in momentum, so the candidate itself has not been tested".
- **The founding image:** "P.R.'s open conjecture [O]", with §9's results stated as results.
- **Collapse-powered expansion:** "P.R.'s open conjecture [O]; two versions failed (w = −2, which the data exclude, and dual
  dust, which the corrected dictionary maps to dust); the route that remains is dual stiff ↦ Λ".
- **The monopole explanation:** "P.R.'s open conjecture [O]". State both grounds against it, what its shared-photon
  setting needs, and that the null result is expected under several standard histories.

## Before and after

Before (`founding-image.md`, status line):

> Conjecture — [O] — P.R.'s founding supposition 3, "Matter clumps in momentum space", open since #11 v2.5 (§9, 'Status
> (v2.5)'; App. A item 3): on 2026-10-29 Paul did not concur in recording it dead (root `CLAUDE.md`, 'Since the handoff').
> As collective dynamics it fails for particle dark matter by 10²⁸–10³¹ (theory), …

After:

> Conjecture — [O] — P.R.'s founding supposition 3, "Matter clumps in momentum space" (#11 §9; App. A item 3). As
> collective dynamics it fails for particle dark matter by 10²⁸–10³¹ (theory), …

Before (`fornax-friction.md`, opening, last sentence):

> Recorded dead before 2026-10-29, the row is now under review, not dead, until Paul reviews it with Claude; the founding
> image itself is his open conjecture again.

After:

> The founding image itself is P.R.'s open conjecture.

Before (a typical pointer):

> (flag 16 in `review/wiki-build-flags.md`, addendum); #11 §9's tag stays [D] until Paul rules

After:

> (flag 16 in `review/wiki-build-flags.md`, addendum); #11 §9's tag is [D]

Before (Sources):

> - `CLAUDE.md` 'Since the handoff' (2026-10-29, Paul's answers to the concurrence questions) — "Restore all pending":
>   Fornax friction suppression is under review, not dead, until he reviews it

After:

> - `CLAUDE.md` 'Since the handoff' — Fornax friction suppression under review

Sections that exist only to tell the dispute or the wording history are deleted outright, such as a section "### An
obituary, v2.0 to v2.4", "### Open again since v2.5", "## Moved", or "## The earlier obituary and its reversal". Save any
physics in them elsewhere on the page first.

## History and record pages

`wiki/history/**`, `wiki/predictions/table-history.md` and `wiki/method/review/**` record documents and events, so they may
give dated, neutral document history: which version added or changed which physics claim or status label, with commit
hashes where the page uses them. For example: "#11 v2.4 (2026-10-29) lists the third candidate as P.R.'s open conjecture
[O], and v2.5 lists the founding image the same way." They still follow every other rule: no dispute, no quotes of
Paul's statements, no concurrence, no "restored". A heading "v2.4: Paul's rule on deaths" becomes "v2.4: three
founding ideas as open conjectures".

## Headings and anchors

Keep every heading unless it narrates the dispute. A heading you must rename or delete goes in your report with its page,
old text and the anchor that replaces it, so that inbound links can be fixed afterwards in one pass. Fix links inside your
own batch yourself. Do not edit other files to fix a link. A broken anchor that points outside your batch is expected until the fix-up pass.

## Mechanics

- Read a page before editing it. For a large register page (`glossary`, `notation`, `references`) find the affected
  lines with `/usr/bin/grep -nE` and edit those.
- Use absolute `/wiki/...` links. Write no LaTeX. Escape a starred symbol in prose: v\*, M\*, g\*.
- If you delete the sentence that spelled out an acronym, spell it out at its next use. The gate checks this.
- `description` in frontmatter is one neutral line about the subject. Rewrite it if it narrates.
- Section indexes: keep the status strip and map, each item short, with no history. The strip gives each item as a link
  and at most a clause.
- Check your files when done: `.venv/bin/python scripts/check-wiki.py <files>`. Your files must have no errors other
  than anchors pointing outside your batch.
- Science prose: a serious scientist explaining abstract material in plain language. No moralizing, no anthropomorphizing,
  no praise of the method. Plain words. Shorter is better when nothing physical is lost.
- `/usr/bin/grep` is the real grep here; the shell's `grep` is ugrep and skips some files.

## Section index strips

The strip's order is now **Stands · Conjectures · Open · Under review · Superseded · Died**. Reorder any strip you touch, and
omit a slot with nothing in it. `wiki/_index.md` and `wiki/summary.md` are finished: read them to see the voice and do not edit them.
