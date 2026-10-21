# wiki/ — the program's wiki

A fine-grained, hierarchical, interlinked wiki of the Broken-Born program's topics.
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
  2. `papers/broken-born-checkpoint-v2.md` (#11, v2.2) and `papers/reciprocity-toy-models.md` (v2);
  3. `review/round4-adjudication.md`, `review/round3-adjudication.md`;
  4. `papers/conjugate-special-relativity.md` (#13);
  5. `HANDOFF.md` (its §2 soliton candidate and its §8 queue are superseded);
  6. `notes/`: calc notes #2–#8 are final for their own scope; #1 and #9 are superseded
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
"## Chat-only: …", "## Popsci-only: …"), and the registers deep-link that heading.

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
- **Analogies.** Wave and Fourier analogies work. Position and momentum relate as a
  waveform and its spectrum, and this is literal, since the Fourier transform implements
  ρ. Ball-rolling metaphors do not work, and neither do ledger or bookkeeping metaphors.
  Where #11 says "two ledgers", write "two descriptions".
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
- Link every wiki concept on its first mention on each page. When the concept is a
  section of a larger page, deep-link the section (`/wiki/a/b#heading-slug`). Slugs are
  GitHub-style: lowercase, punctuation dropped, each space a hyphen.
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

`scripts/check-wiki.py` runs inside `scripts/check.sh` and checks links, anchors,
section maps, source paths, frontmatter, the italic opening, the status line, fences and
acronyms. Run it on the files you touched with
`.venv/bin/python scripts/check-wiki.py wiki/x/y.md`; links still resolve wiki-wide.
`scripts/check.sh` must pass before work is called finished. Do not weaken a check to
make it pass.

## Keeping it current

- **A source document changes.** Find the dependent pages with
  `grep -rl 'papers/broken-born-checkpoint-v2.md' wiki/` (frontmatter sources), update
  them, and update the status registers.
- **A claim dies.** Set `status: dead` and rewrite the page as an obituary. Add it to the
  graveyard register, and fix every page that relied on it.
- **A new topic.** Place it by the taxonomy rules, link it from its parent's map and from
  every page that mentions it, and run the gate.

## Build state

This section records the progress of the initial build so that a cold session can resume.
Delete it when the build is complete.

- **2026-10-20.** Gate committed (`scripts/check-wiki.py`). Thirteen inventories, a master
  topic list (371 topics, 115 background concepts, 151 resolved source conflicts) and
  taxonomy proposals B and C were produced in the session scratchpad. B was adopted:
  278 entries.
- **2026-10-21.** Breadth pass committed (`7b9438b`): all 278 pages, averaging about 800
  words each. Starred symbols escaped; the gate now checks them.
- **2026-10-21, depth wave 1.** `program/` and `phase-space/` are at full depth: 52 files,
  committed page by page. The verifiers checked 1,882 claims and fixed 104 of 107 findings.
  Two suspected errors in the source documents themselves are quoted faithfully and await
  Paul's ruling:
  - #5 §B and #11 §5 call the η-null Lagrangian polarizations "discrete"; for d ≥ 2 they
    form Grassmannian families, though the conclusion (no Maslov circle) survives;
  - toy note §5 calls I "odd in K", but I ≥ 0, so it is only not invariant under K → −K.
- **2026-10-21, depth wave 2.** `symmetry-breaking/` and `gravity/` are at full depth and
  verified. The usage limit cut the workflow off midway; the remaining verifiers ran as
  single background agents. Further source flags (15 in all) are collected in
  `review/wiki-build-flags.md`.
- **Depth waves still to run** (as of wave 2):
  - `dark-matter/`;
  - `cosmology/` and `electric-magnetic-duality/`;
  - `conjugate-relativity/` and `predictions/`;
  - `method/` and `history/`;
  - then the registers (home, `status/`, glossary, notation, references), link density,
    and a completeness check against the inventories.
- **Plan.**
  1. Breadth pass: every page at gist level (italic gist, Status line, Key facts,
     Sources), in one commit.
  2. Depth pass, section by section, with one commit per section. Each page gets its full
     technical record and a fresh-context fidelity review.
  3. Registers, linking density and a completeness check.
- **To resume after a lost session.** The committed tree is the plan. A page still at gist
  level has a `## Key facts` section and no other technical sections; deepen those first.
