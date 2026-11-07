export const meta = {
  name: 'dual-sector-finish',
  description: 'Second propagation round (Winn; leftovers), then a review of the whole change by fresh reviewers, each followed by a refuter',
  phases: [
    { title: 'Edit', detail: 'three editors on disjoint files, each followed by a checker' },
    { title: 'Review', detail: 'three reviewers on disjoint files, each followed by a refuter' },
  ],
}

const REPORT = {
  type: 'object',
  properties: {
    files_changed: { type: 'array', items: { type: 'string' } },
    changes: { type: 'array', items: { type: 'object', properties: { file: { type: 'string' }, what: { type: 'string' } }, required: ['file', 'what'] } },
    other_files_needing_change: { type: 'array', items: { type: 'string' } },
    gate_output: { type: 'string' },
    doubts: { type: 'array', items: { type: 'string' } },
  },
  required: ['files_changed', 'changes', 'other_files_needing_change', 'gate_output', 'doubts'],
}
const FINDINGS = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: {
      file: { type: 'string' }, passage: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' },
      severity: { type: 'string', enum: ['high', 'medium', 'low'] }, fixed: { type: 'boolean' }, fix: { type: 'string' } },
      required: ['file', 'passage', 'problem', 'evidence', 'severity', 'fixed', 'fix'] } },
    gate_output: { type: 'string' },
    overall: { type: 'string' },
  },
  required: ['findings', 'gate_output', 'overall'],
}

const COMMON = `You work in the repository /home/paul/git/reinholdtsen/conjugate-matter, the record of the Comatter research program. A close reading of the papers of Djordje Minic and coauthors on dark matter as the dual of visible matter (the "dual-sector investigation", 2026-11-06) is written up as notes/dual-sector.md, with its record review/dual-sector/, its gate script verify/dual_sector.py, a wiki page wiki/dark-matter/conjugate-matter/dual-standard-model.md, an addendum to flag 64 and flags 70-73 in review/wiki-build-flags.md, and an entry of 2026-11-06 in the root CLAUDE.md; a first round of agents carried it into notes/literature-check.md and about 25 wiki pages. Nothing is committed: git diff shows the whole change.

Read first, in full: notes/dual-sector.md (the source of record); work/dual-sector/inputs/propagation.md (the facts, the wording and quotations to reuse, every paper's link, and items 11-12 added after round 2); wiki/CLAUDE.md (above all Voice, Links, Symbols, Acronyms); review/wiki-build-flags.md item 64 with its addendum and items 70-73.

Rules: the wiki is derivative, every statement must be supported by notes/dual-sector.md (or the record it cites), named in the page's frontmatter sources and Sources list; no new numbers; quotations copied exactly from the note; on wiki pages, state the claim, not how the record's wording changed, and no "Paul" (write P.R.); flags are pointers ("flag 73, pending"); every cited paper is linked at its first mention on a page (a paper not in scripts/wiki-papers.tsv is added with .venv/bin/python scripts/wiki-papers.py arXiv:ID; run it alone, never while editing the registry by hand); define w beside its first use; spell out acronyms; change no claim's status; keep #11's own quotations verbatim and qualify beside them. Do not commit. Run .venv/bin/python scripts/check-wiki.py on files you touch and on the whole wiki at the end, and bash scripts/check.sh at the end; both must pass.`

const EDITORS = [
  { label: 'g1-winn', files: ['notes/literature-check.md', 'wiki/method/literature-check.md', 'wiki/electric-magnetic-duality/magnetic-identification.md', 'wiki/electric-magnetic-duality/monopole-explanation.md', 'wiki/dark-matter/candidates/momentum-space-monopoles.md', 'wiki/status/conjectures.md', 'wiki/status/open-problems.md'],
    task: `Carry propagation.md items 11 and 12 (Winn; the conference sweep; flag 73) to these files. notes/literature-check.md: in §2's table, the C4 row's closest published work and "Not found" cell, and C2's and C3's rows if they name the closest work; §4 (C2, C3) and §5 (C4), a sentence or two each with a pointer to notes/dual-sector.md §10 and flag 73, narrowing §5's "Not found" (one analog per charged particle is published; the placement in momentum is not), with no new reference-list entries and the verdicts and counts unchanged (run .venv/bin/python verify/literature_check.py: it must pass). wiki/method/literature-check.md: the same in the table's C2-C4 rows, and link Govaerts 2023, Vento 2025 and García-Moreno and Vento 2026 at their first mention (all registered); also add to the C1 row's "Not found" cell the spontaneous breaking of ρ with η as order parameter, as notes/literature-check.md §2 now lists it. The three conjecture pages: in each "In the literature" section, Winn with his relation to that conjecture; on monopole-explanation.md also note §6's point that the group's explanation of dark matter's null result has the shape of C3. status/conjectures.md and status/open-problems.md: flag 73 wherever flags 70-72 are listed, and its line among pending flags; counts of flags updated.` },
  { label: 'g2-leftovers', files: ['wiki/history/documents/checkpoint.md', 'wiki/method/lakatosian-methodology.md', 'wiki/status/alive.md', 'wiki/symmetry-breaking/mandatory-breaking.md', 'wiki/symmetry-breaking/toy-models/success-criteria.md', 'wiki/history/documents/project-instructions.md', 'wiki/history/timeline.md', 'wiki/references.md', 'verify/literature_check.py'],
    task: `Close items a first round left open. checkpoint.md (around line 176) and lakatosian-methodology.md (around lines 81 and 135): the identification proposed, not derived, first public in the talk of 9 September 2019 and in writing in 2020 (not "since 2020" alone), with a link to the new page, and flags 70-73 beside the literature check's flags where they bear on #11 or on novelty. alive.md: pointers to flag 70 beside its hard-core, P2′ and P5 lines and to flag 72 beside its a·ã = 1, maximum-force and no-phantom lines; move its 'current to' date only if the register then reflects the investigation. mandatory-breaking.md (around line 55) and toy-models/success-criteria.md (around line 82): flag 70 beside the quoted sentences of #11 §3 and of the worklog, with a one-clause statement of what it says. project-instructions.md and timeline.md: flags 70-72 become 70-73, and Winn (flag 73) is named among the investigation's results in the manner of those pages. references.md: add Winn 2012 (arXiv:1206.4590) and the Lepton-Photon 2025 talk to the group 'Literature the dual-sector investigation found', with links. verify/literature_check.py: its section F reads the flags file to its closing paragraph and so now also scans flags 70-73, which belong to verify/dual_sector.py (section E); restrict section F's scan to end at the heading '## Found by the dual-sector investigation (2026-11-06)', keep its label 'flags 64–69', and confirm both verify scripts pass.` },
  { label: 'g3-flag49-72', files: ['wiki/predictions/early-universe-step.md', 'wiki/cosmology/scale-factor-duality/duality-dictionary.md', 'wiki/cosmology/scale-factor-duality/closed-universe.md', 'wiki/method/review/round-5.md', 'wiki/phase-space/reciprocity/born-length.md', 'wiki/conjugate-relativity/maximum-force-conjectures.md', 'wiki/gravity/momentum-graviton/borns-answer.md', 'wiki/phase-space/reciprocity/momentum-fibers.md'],
    task: `Carry propagation.md fact 8 (flag 72). early-universe-step.md, duality-dictionary.md and closed-universe.md: where each says the dual Einstein term is not derived (flag 49), add that a dual Einstein term is treated in the literature with the opposite assignment, the dual space's curvature giving a positive cosmological constant (Berglund, Hübsch and Minić 2019, Phys. Lett. B; flag 72, pending), in a sentence. round-5.md (around line 209), where it quotes the diameter note's account of Hur et al. 2025 (w > −1): add the paper's other model, under the group's earlier relation, w below −1 and disfavoured by DESI's second release (flag 72), defining w. born-length.md and maximum-force-conjectures.md: Newton's constant as a space–momentum conversion factor (Freidel, Leigh and Minic 2014, Int. J. Mod. Phys. D, §1.2; flag 72), only where the page discusses the scale it bears on. borns-answer.md and momentum-fibers.md: curved momentum space in Freidel, Leigh and Minic 2014 (Phys. Lett. B), traced by them to Born (flag 72), only where the page states App. A item 10 or the lineage of curved momentum space.` },
]

const REVIEWERS = [
  { label: 'v-note', files: ['notes/dual-sector.md', 'review/wiki-build-flags.md (flag 64 addendum and flags 70-73 only)', 'CLAUDE.md (the 2026-11-06 entry and the open items it adds)', 'review/dual-sector/README.md'],
    task: `Review the note, the flags and the CLAUDE.md entry against the record in review/dual-sector/ (readers/, panel/, round2/, quotes.json, sources.json, events.json, workflows/usage.json, preregistration.md). For every statement: is it supported by the record, and stated with the strength the record supports (no stronger, no weaker)? Are the verdicts and relations those of the panel and the verifiers? Are dates, counts and attributions right (paper ids, which of two same-year papers)? Is anything in the record that bears on the three clauses left out? Is the prose plain, without anthropomorphism or hype? Fix each problem directly in these files, keeping every quotation exact (verify/dual_sector.py must pass: run it).` },
  { label: 'v-wiki', files: ['wiki/dark-matter/conjugate-matter/dual-standard-model.md', 'wiki/summary.md', 'wiki/dark-matter/conjugate-matter/_index.md', 'wiki/method/verification/dual-sector-script.md', 'wiki/method/verification/_index.md'],
    task: `Review these pages as a cold reader would, and against notes/dual-sector.md and wiki/CLAUDE.md. The new page must answer P.R.'s question plainly: is the claim true, what overlaps and what does not. Check each statement against the note; the voice rules; that every paper is linked and every link points at the paper named; that the summary's sentence is accurate in its 800 words; that the hub and verification index describe the new pages correctly. Fix each problem directly in these files.` },
  { label: 'v-sweep', files: ['every other file in git diff (report only; edit nothing)'],
    task: `Read the whole working-tree diff (git diff, and git status for new files) except the files the other two reviewers hold. Look for: statements made stale by the investigation and not updated (grep the wiki and the notes for "since 2020", "correlated with ours", "no such mechanism", "treated the breaking as kinematical", "no symmetry-breaking analysis", "flags 70–72" and similar); inconsistencies between pages (dates, flag numbers, counts, wording of the three clauses); a link added in the paper-link retrofit that points at the wrong paper (check a sample of 40 author–year links against scripts/wiki-papers.tsv and the surrounding citation); anything that changed a claim's status. Report each finding with its file and passage; fix nothing.` },
]

phase('Edit')
const edited = await pipeline(
  EDITORS,
  e => agent(`${COMMON}\n\nYour label: ${e.label}. Your files: ${e.files.join(', ')}.\n\n${e.task}\n\nEdit only your files; list others that need a change.`, { label: e.label, phase: 'Edit', schema: REPORT }),
  (rep, e) => rep === null ? null : agent(`${COMMON}\n\nYour label: ${e.label}-check. Check the work of editor ${e.label} on ${e.files.join(', ')}; its task was:\n${e.task}\n\nIts report:\n${JSON.stringify(rep)}\n\nRun git diff on those files and read every change against notes/dual-sector.md, propagation.md and wiki/CLAUDE.md: unsupported statements, inexact quotations, new numbers, narration on wiki pages, missing or wrong paper links, undefined w, acronyms, status changes, omissions against the task. Fix each problem in those files, rerun the gates, and report.`, { label: e.label + '-check', phase: 'Edit', schema: FINDINGS }).then(c => ({ label: e.label, report: rep, check: c })),
)

phase('Review')
const reviewed = await pipeline(
  REVIEWERS,
  r => agent(`${COMMON}\n\nYour label: ${r.label}. You are a fresh reviewer of the finished change. Your files: ${r.files.join(', ')}.\n\n${r.task}`, { label: r.label, phase: 'Review', schema: FINDINGS }),
  (out, r) => out === null ? null : agent(`${COMMON}\n\nYour label: ${r.label}-refute. Reviewer ${r.label} reviewed ${r.files.join(', ')} with the task:\n${r.task}\n\nIts findings and fixes:\n${JSON.stringify(out)}\n\nTry to refute each finding and each fix from the sources (the note, the record in review/dual-sector/, the papers through work/dual-sector/tools/lit.py run from work/dual-sector/). Where a fix made a passage wrong, worse or unsupported, restore or correct it in the same file, and say so. Where a finding marked unfixed is real and within the reviewer's files, fix it. Then run bash scripts/check.sh and report its result.`, { label: r.label + '-refute', phase: 'Review', schema: FINDINGS }).then(v => ({ label: r.label, review: out, refute: v })),
)
return { edited: edited.filter(Boolean), reviewed: reviewed.filter(Boolean) }
