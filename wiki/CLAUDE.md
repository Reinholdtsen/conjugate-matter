# wiki/ — the program's wiki

A fine-grained, hierarchical, interlinked wiki of the Comatter program's topics.
Content only: Markdown in hugo-book form, with no site scaffolding here. It mounts into a
Hugo site as `content/wiki` (`BookSection = 'wiki'`, `ignoreFiles = ['CLAUDE\.md$']`, the
same setup as `~/git/bitsy-services/wiki`), and it reads well in an editor or on GitHub as is.

It is written for three readers:

- a casual reader who wants the gist of a topic;
- a motivated reader (undergraduate physics or better) who wants to learn the topic,
  including the established physics the program builds on;
- Claude in a later session, looking up a concept, its current status, where it is
  derived, and what verifies it.

## The wiki is derivative

- The papers, notes, review records and `verify/` scripts are the record. The wiki
  explains and indexes them and adds no results. When the wiki and a source disagree,
  the source wins and the wiki gets fixed.
- **Source precedence**, most current first:
  1. the root `CLAUDE.md`, section "Since the handoff";
  2. `papers/broken-born-checkpoint-v2.md` (#11, v2.2), `papers/reciprocity-toy-models.md` (v2) and
     `papers/phase-space-diameter.md` (v1.1);
  3. `review/round5-adjudication.md`, `review/round4-adjudication.md`, `review/round3-adjudication.md`;
  4. `papers/conjugate-special-relativity.md` (#13);
  5. `HANDOFF.md` (its §2 soliton candidate and its §8 queue are superseded);
  6. `notes/`: calc notes #2–#8 are final for their own scope; `notes/closed-universe.md`
     (2026-10-27, not reviewed) is current for its scope, a closed universe; `notes/velocity-gated-gravity.md`
     and `notes/gate-mechanism.md` (2026-10-28, not reviewed) are current for theirs, momentum gravity as a
     velocity-dependent force and the gate's mechanism; #1 and #9 are superseded
     as reference; #14 is withdrawn;
  7. `popsci/`. #12 presents the framework as if it were confirmed. It is never a source
     for a claim's status.
- **No new numbers.** Every number on a page is copied from a source document or a
  `verify/` output, and the page names that source. Nothing is computed, rounded or
  converted by eye (the iron rule). A number the sources do not contain does not appear.
- **Dead stays dead.** Claims killed in `HANDOFF.md` §2, #11 §9 and §12, and the
  adjudications are reported as dead, prominently, on their own pages.
- **Tags carry over exactly.** The tags are [D] derived here, [T] literature,
  [P] postulate, [O] open and [V] machine-verified. Citations are marked † (from model
  memory, unverified) or [S] (live-searched). A page never upgrades a tag. Explanations
  of established physics written from general knowledge are [T], and any citation they
  add is †.

## URLs

`wiki/a/b.md` serves at `/wiki/a/b`. `wiki/a/_index.md` is the section page `/wiki/a`.
`wiki/_index.md` is `/wiki`. Moving a page breaks every inbound link, so place a page
deliberately the first time.

## The tree

The top level follows the program's argument as #11 builds it. Within a section,
established physics comes first and the program's claims follow in derivation order, so
what is known and what is claimed read as a sequence.

| Section | Holds |
| --- | --- |
| `program/` | the question, the hard core, postulates P1–P5, founding suppositions, the main critique, the self-assessment |
| `phase-space/` | Born reciprocity, Born geometry and its theorems, the modular field |
| `symmetry-breaking/` | the mechanism of the hard core: order parameter, Goldstone angle, ρ-preserving potential, matter locality, the two toy models |
| `gravity/` | spin-2 theory (massless and massive) and the Debt-1 results on the momentum graviton X |
| `dark-matter/` | halo and wave-dark-matter physics, the gated conjugate sector (Debt 2), the momentum-clumping obituary (Debt 3), the candidates and the retired soliton candidate |
| `cosmology/` | scale-factor duality, dark energy, early-universe physics |
| `electric-magnetic-duality/` | monopoles, dualities, charge lattices, the polarization identification |
| `conjugate-relativity/` | #13: the kinematics of the momentum polarization |
| `predictions/` | one test page per row of #11 §13, plus the table's history |
| `status/` | registers: graveyard (first), alive, open problems and the queue, conjectures, superseded |
| `method/` | Lakatos, the collaboration, provenance, verification (one page per script family), blind review |
| `history/` | timeline, the three debts, the documents and the conflicts between them |
| `glossary`, `notation`, `references` | single register pages |

**Status is visible in titles.**

| Status | Title pattern |
| --- | --- |
| `dead` | "Obituary: …" |
| `open` | "Open: … (OPn)", where OPn is #11 §14's item number when it has one |
| `superseded` | "… (superseded)" |
| chat-only conjectures | "… (chat-only)" |
| popsci-only claims | "… (popsci-only)" |
| prediction pages | "Row n: …" |

`established` and `alive` carry no marker. The status line and the section map separate
them.

**Section indexes** run in this order:

1. the italic definition;
2. a status strip ("Stands: … · Died: … · Open: …", each item linked). Add "Superseded:"
   and "Conjectures:" slots when the section holds such pages. A section holding only
   literature, method or record pages replaces the strip with one line that says so and
   links the status registers;
3. the `## Map`, in weight order;
4. `## Boundaries`.

The home page adds its brief, attribution, reading guide and reading paths between the
strip and the Map.

**Folded items.** A page sometimes holds a minor item of another status, such as an open
sub-question on an established page or a superseded earlier form of an alive claim. Such
an item gets its own status-headed section ("## Open: …", "## Superseded: …",
"## Chat-only: …", "## Popsci-only: …", "## Conjecture: …"; "###" when it sits inside a
larger section), and the registers deep-link that heading.

**OPn** means item n of #11 §14 (the checkpoint's open problems). It is registered and
may be used in body text.

**Registers.** The registers (status pages, glossary, notation, references, timeline,
documents) have status `record`.

**The linking plan:**

- Every obituary links the claim's home section, the calculation or ruling that killed it,
  and `/wiki/status/graveyard`.
- Each prediction row links its derivation pages, and each derivation links its row.
- Every "Open:" page links `/wiki/status/open-problems` and the claim it qualifies.
- Every established-physics page ends with a short "Used by" list of the program pages
  that rely on it.
- Every machine-checked claim links its script's page under `/wiki/method/verification/`.

## Taxonomy rules

1. A node is a subject, not a container, and a section's name predicts its contents.
   No form-named sections ("background", "misc", "notes", "reference").
2. The top level is for fields or major subjects. Named things (a model, a paper, a
   theorem) go inside the field that explains them.
3. Siblings are the same kind of thing and comparable in grain.
4. Depth is at most 5 segments after `wiki/`, and 4 or fewer is better.
5. A section has at most about 15 children. Past that, subdivide by subject.
6. A section below the top level needs at least 3 pages. Otherwise it is a page.
7. Every `_index.md` is a real page: a definition of the subject, a prose map of the
   children in reading order (each child linked; the gate checks it), and a boundary
   statement naming the neighbouring sections that hold related material.
8. A subject with two plausible parents goes under the charter that names it and is
   linked from the other. Pages are never duplicated.
9. Weights put siblings in reading order (prerequisites first), numbered in tens and
   unique among siblings. Existing weights are never renumbered.
10. Slugs are lowercase hyphenated ASCII. No file may be named `claude.md` in any case.
11. One concept, mechanism, result, obituary, test or event per page.
12. Established physics gets its own pages (status `established`), placed in the field
    it belongs to.
13. Every dead claim has its own obituary page, and the graveyard register indexes them.

## Page anatomy

```text
---
title: "Compatibility theorem"
weight: 30
status: alive
description: "With ω and η both rigid, the only positive generalized metrics are H = diag(g, g⁻¹)."
provenance: [T, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §5"
  - "notes/debt1a-geometric-core.md §A"
  - "verify/battery.py T1"
---

*One italic paragraph for the casual reader. Its first sentence names the thing
concretely. The rest says what it does in the program and where it stands.*

**Status:** Alive. Literature result [T] (Freidel–Leigh–Minic); the block proof and the
machine check [V] (`verify/battery.py`, test T1) are this program's.

## Statement
...technical sections, at ## and ###...

## Sources
- `papers/broken-born-checkpoint-v2.md` §5 — current statement and attribution
```

- **Frontmatter** (the gate checks it):
  - `title`, `weight` (an integer), `status` and a one-line `description` are required;
  - `sources` (repo paths, each followed by a section) is required on every page that is
    not a section index;
  - `bookCollapseSection: true` is required on every `_index.md`;
  - `provenance` is optional: the tags of the page's central claim.
- **Statuses** (one per page):

  | Status | Meaning |
  | --- | --- |
  | `established` | literature |
  | `alive` | a program claim that currently stands |
  | `conjecture` | not derived; includes the chat-only results of `HANDOFF.md` §4 |
  | `open` | an open problem |
  | `dead` | killed, and stays dead |
  | `superseded` | replaced by a corrected version |
  | `method` | how the program works |
  | `record` | history, reviews, documents |
  | `hub` | a section index |

- **Opening**: the body begins with the italic passage (the gate checks this). Every
  page that is not a section index then has a `**Status:**` line, which the gate also
  checks. The status line states the status in words, then the tags, then what verifies
  the claim.
- **Body**: no `# H1`, because hugo-book renders the title. Sections start at `##`.
  Order the sections by the questions a cold reader asks: what is it, what is it made of,
  how does it work, what follows, what is open, where it comes from. A dead claim's page
  is an obituary: what was claimed, how it was tested, why it failed, what survives.
- **Sources**: end every page with a `## Sources` list of repo paths (as inline code) and
  sections, most authoritative first. The gate checks that every inline-code repo path
  exists.

## Voice

Write as a serious scientist explaining abstract material in plain language. Three tests
apply to the finished page, borrowed from `~/git/bitsy-services/wiki/.claude/rules/wiki-voice.md`:

1. After the first paragraph, can a reader say what the thing is?
2. Does every sentence parse when read aloud?
3. Is every term plain English, glossed in the same sentence, or linked *and* glossed?

Rules on wording:

- **No anthropomorphizing.** A field does not *want*, nature does not *forbid* or *play
  favorites*, and a theory does not *refuse to die*. Some of #11's italic passages do
  this. Do not copy those passages.
- **No moralizing, no hype, no detective-story reveals.** Words like "remarkably",
  "crucially", "the culprit" and "it turns out" do not belong. Show significance as a
  consequence: the number, the failure it causes, what it makes possible.
- **Negative results are stated, not celebrated.** Report a dead or rejected claim as a
  fact: what was claimed, what killed it, what survives. Do not draw lessons from it about
  the program's honesty, rigor or skepticism, and do not present a death as a credit to the
  method. Phrases such as "the machinery working", "a theory that cannot lose bets cannot
  win them", "killed by its own mathematics" used as praise, and "genuine science" do not
  belong in the wiki's voice. Where a source says such things (#11 §9 and §15, #10), quote it
  only on the page that reports that document's self-assessment, attributed and without
  endorsement.
- **Analogies.** Wave and Fourier analogies work. Position and momentum relate as a
  waveform and its spectrum, and this is literal, since the Fourier transform implements
  ρ. Ball-rolling metaphors do not work, and neither do ledger or bookkeeping metaphors.
  Where #11 says "two ledgers", write "two descriptions".
- **The program's name.** The program is the Comatter program, capital C. Until
  2026-10-26 it was the Broken-Born program, abbreviated BBT, and the records keep that
  name. Quote them as written, and gloss BBT beside the quotation as Broken-Born theory,
  the program's earlier name.
- **Explanation is in the third person.** Second-person imperatives are for procedures.
- **Status and attribution.** A topic's status comes from #11, never from the popsci
  framing. Paul is an independent developer and is never described as retired. Roles
  follow the attribution line: conjecture and direction, P.R.; derivations,
  counterexamples, verification, drafting, Claude (Anthropic).

## Math

Write math inline in Unicode, as #11 does: H = diag(g, g⁻¹), Z → −Z⁻¹, βₙ = β₄₋ₙ,
w ≥ −1. Display equations go in fenced `text` blocks, because the gate requires a
language on every fence. Do not use LaTeX: without site configuration it renders nowhere.
Use the symbols on the notation page.

Escape the asterisk of a starred symbol in prose: write v\*, M\*, g\*. An unescaped
`v*` can close an emphasis span, which ends an italic opening in the wrong place. The
gate checks for this. Code spans and `text` fences need no escaping.

## Links

- Use absolute `/wiki/...` links only. Repo files are not linked; cite them as inline
  code paths (`papers/broken-born-checkpoint-v2.md` §5), which the gate checks exist.
  The prefix is a settled choice (Paul, 2026-10-22), matching `bitsy-services/wiki`; do not
  switch forms. The trade-off: these links do not resolve when the raw Markdown is browsed
  (on GitHub, for example). In a Hugo site they work as written at the domain root. Under a
  subpath they work in `site/`, whose `BookPortableLinks = 'error'` resolves each link to its
  page's URL (`site/CLAUDE.md`).
- Link every wiki concept on its first mention on each page. When the concept is a
  section of a larger page, deep-link the section (`/wiki/a/b#heading-slug`). Slugs are
  Hugo's GitHub-style IDs: lowercase, punctuation dropped, each space a hyphen. Letters of
  any script and `_` stay, but subscript and superscript digits are dropped: the heading
  "What w₀ and wₐ mean" has the slug `what-w-and-wₐ-mean`. The gate computes slugs the
  way Hugo does. Headings are plain text, and code spans in them are fine. A link,
  emphasis or a `{#id}` block in a heading fails the gate: Hugo builds such a heading's ID
  from only part of its text, or takes the `{#id}`, and the gate does not reproduce that.
- Every page is linked from its parent section's map, which the gate checks. Aim for at
  least 3 inbound links from other pages; `scripts/check-wiki.py --stats` lists the
  pages short of that.
- Program pages link to the established physics they use, and established-physics pages
  link to the program pages that use them. Every mention of a dead claim links to its
  obituary.

## Acronyms

Spell out every acronym on first use on each page, or make the acronym a link. The
registry is `scripts/wiki-acronyms.txt`, and an unregistered acronym fails the gate.
While several agents are writing at once, none of them edits the registry. Each one
spells out new acronyms, or reports them to be added.

- GW means Grosse–Wulkenhaar in this wiki. Always write "gravitational waves" in full,
  and paraphrase any quotation that uses GW in that sense.
- All-caps words in quotations ("NOT", "ONLY") fail the gate. Paraphrase them, or set
  them in lower case inside the quotation and say so.

## The gate

`scripts/check-wiki.py` runs inside `scripts/check.sh` and checks links, anchors, markup
in headings, section maps, source paths, frontmatter, the italic opening, the status line,
fences and acronyms. Run it on the files you touched with
`.venv/bin/python scripts/check-wiki.py wiki/x/y.md`; links still resolve wiki-wide.
`scripts/check.sh` must pass before work is called finished. Do not weaken a check to
make it pass.

## Publishing

`site/` builds this folder into a static site: Hugo mounts `wiki/` as `content/wiki`, so
pages are written here and never copied into `site/`. Building, checking, previewing and
deploying are in `site/CLAUDE.md`. Paul publishes by hand: `npx wrangler login` once per
machine, then `npm run deploy` in `site/`. Its gate, `npm run check`, runs
`scripts/check.sh` first, then builds the site and checks every link and anchor in the
HTML, that every page was built, and that every heading got the ID this gate computes.

## Keeping it current

- **A source document changes.** Find the dependent pages with
  `grep -rl 'papers/broken-born-checkpoint-v2.md' wiki/` (frontmatter sources), update
  them, and update the status registers.
- **A claim dies.** Set `status: dead` and rewrite the page as an obituary. Add it to the
  graveyard register, and fix every page that relied on it.
- **A new topic.** Place it by the taxonomy rules, link it from its parent's map and from
  every page that mentions it, and run the gate.
- **A flag is ruled on.** `review/wiki-build-flags.md` lists suspected errors in the source
  documents found while the wiki was built, each with its audit verdict; pages quoting a
  flagged statement point to its number (`grep -rn 'flag N' wiki/`). When Paul rules, correct
  the source if the ruling accepts the flag, then update those pages and the flag's entry.

The initial build (2026-10-20 to 2026-10-22) is recorded on `/wiki/history/timeline`.
