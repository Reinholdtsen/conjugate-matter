export const meta = {
  name: 'litcheck-final-sweep',
  description: 'Verify the last hand-written merges and sweep the repository for statements the literature-check edits left stale',
  phases: [{ title: 'Verify' }, { title: 'Skeptic' }],
}

const COMMON = `The repository /home/paul/git/reinholdtsen/conjugate-matter holds a speculative physics research program (its root CLAUDE.md gives conventions, tags and the Method; wiki/CLAUDE.md gives the wiki's rules). Do NOT edit any file in the repository. Scratch files only under work/literature-check/verify-custom/<your-label>/ (create it).

Background. A literature check of P.R.'s conjectures (2026-11-02) was written up: notes/literature-check.md (the note), flags 64-69 in review/wiki-build-flags.md, the record review/literature-check/ (findings.json, panel/*.out.json, round1-3/, round5/, checks/, sources.json, quotes.json, workflows/workflow1-8-result.json), entries in the root CLAUDE.md, and pages of wiki/. It went through two reviews by agents (workflows 5 and 7) and a check of the edits merged by hand (workflow 8, review/literature-check/workflows/workflow8-result.json: 47 findings, 43 confirmed, 4 in part). The main session applied workflow 8's edits, merging some by hand and writing a few more; those hand-written texts are listed as "was" -> "now" in work/literature-check/verify-custom/round8-custom.json (16 items). verify/literature_check.py now has a section G (the algebra behind flag 66), section B finds each count it recomputes in the note's prose, and both gates pass (.venv/bin/python verify/literature_check.py; .venv/bin/python scripts/check-wiki.py).

Rules that bind the texts: every statement supported by the record or the source documents, no overclaiming ("not found" means not found by these searches), no claim's status changes, the wiki adds no numbers not in a source and carries tags over exactly, wiki voice (wiki/CLAUDE.md "Voice"), plain science prose. P.R. relies on the tags, the machine checks and the record to tell sound results from confabulation.

Tools: read files directly; .venv/bin/python -I work/literature-check/tools/lit.py (show, text --grep, quote) reads abstracts and arXiv full texts from cache or arXiv/INSPIRE. No OpenAlex or Semantic Scholar queries. If you test edits, do it on a copy under your scratch folder; delete any copy of wiki pages or of the pre-registration afterwards.

Report only real defects, each with evidence and, for a text fix, an exact edit whose "current" occurs EXACTLY ONCE in the file as it stands now. If something can only be decided by P.R., say so in needs_decision and propose no edit. At most 20 findings, most severe first; an empty list is a valid answer.`

const TASK = `YOUR TASK, two parts.
(1) Test each of the 16 hand-written texts in work/literature-check/verify-custom/round8-custom.json, read in place, against the record and the sources: the merged §6 italic of the note (two sentences joined), the stiff-partner bullet on wiki/method/verification/literature-check-script.md against verify/literature_check.py section G, the W6 knee paragraph on wiki/predictions/self-interaction-knee.md, flag 69's new tail caveat and Chu label, the softened readings in CLAUDE.md and wiki/status/open-problems.md, the note §6 parenthetical on section G, the note §11 paragraph "A check of the merges" against workflow8-result.json, the README additions, the timeline sentence, and the three description edits.
(2) Sweep the repository for statements that the whole sequence of edits left stale or inconsistent, as a completeness critic. Grep, for example, for: "426", "515", "530" (old PASS counts); "eleven scripts" and "ten of the eleven"; "no \`verify/\` script" or "no script" near the duality dictionary; "two reviews" where the check of the merges should also be named, or the reverse; "four rounds"; "is published" for the program's two forms; "Three verdicts" or "three verdicts" (now four); "not reviewed" (the repository convention for notes, kept in CLAUDE.md; the note says "not through a blind review round"); "one verifier" for flag 66's algebra; "a ∝ t^(−1/2)" stated as the partner without the sign caveat; "founding image" used for C5; "reran"; "gravity alone" for the program without the shared-photon caveat on pages that discuss the literature check. Also check that every wiki page that says a script checks something links that script's page (wiki/CLAUDE.md linking plan), and that the summary (wiki/summary.md) is still true and under 800 words by the gate. Report each stale statement with an edit.`

const FINDINGS = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, file: { type: 'string' }, quote: { type: 'string' }, problem: { type: 'string' },
      evidence: { type: 'string' }, severity: { type: 'string', enum: ['high', 'medium', 'low'] },
      edits: { type: 'array', items: { type: 'object', properties: { file: { type: 'string' }, current: { type: 'string' }, proposed: { type: 'string' } }, required: ['file', 'current', 'proposed'] } },
      needs_decision: { type: 'string' } },
      required: ['id', 'file', 'problem', 'evidence', 'severity', 'edits'] } },
    notes: { type: 'string' },
  },
  required: ['findings', 'notes'],
}
const VERDICTS = {
  type: 'object',
  properties: { results: { type: 'array', items: { type: 'object', properties: {
    id: { type: 'string' }, verdict: { type: 'string', enum: ['confirmed', 'partly', 'refuted'] }, evidence: { type: 'string' },
    edits: { type: 'array', items: { type: 'object', properties: { file: { type: 'string' }, current: { type: 'string' }, proposed: { type: 'string' } }, required: ['file', 'current', 'proposed'] } } },
    required: ['id', 'verdict', 'evidence', 'edits'] } } },
  required: ['results'],
}

phase('Verify')
const rev = await agent(`${COMMON}\n\n${TASK}\n\nYour label (for your scratch folder): final-sweep.`, { label: 'verify:final-sweep', phase: 'Verify', schema: FINDINGS })
if (!rev || !rev.findings || rev.findings.length === 0) return { review: rev, verdicts: { results: [] } }
phase('Skeptic')
const ver = await agent(`${COMMON}\n\nYOU ARE THE SKEPTIC for the findings below, raised by a verifier given this task: ${TASK}\n\nTry to REFUTE each finding: reread the cited evidence yourself, at its source. Verdict "refuted" if the finding is wrong or the text is already right; "partly" if right only in part; "confirmed" if it holds. For confirmed and partly findings return the edits you would actually apply (revise the verifier's edits where wrong, overreaching, or themselves misstating the record); each "current" must occur exactly once in the file as it stands now. Return one result per finding id.\n\nThe findings:\n${JSON.stringify(rev.findings, null, 1)}\n\nThe verifier's notes: ${rev.notes}\n\nYour label (for your scratch folder): skeptic-final-sweep.`,
  { label: 'skeptic:final-sweep', phase: 'Skeptic', schema: VERDICTS })
return { review: rev, verdicts: ver }
