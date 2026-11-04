export const meta = {
  name: 'litcheck-review-verify',
  description: 'Adversarially verify the two reviews of the literature-check write-up, and rerun the OpenAlex queries the check could not run',
  phases: [
    { title: 'Verify', detail: 'six skeptics, each refuting one group of review findings and proposing exact edits' },
    { title: 'Rerun', detail: 'the OpenAlex queries blocked by the quota on 2026-11-02, and another try at Khademi 2009' },
    { title: 'Check', detail: 'a verifier for each strong new finding from the rerun' },
  ],
}

const REPO = '/home/paul/git/reinholdtsen/conjugate-matter'

const COMMON = `You are verifying review findings on a write-up in the repository ${REPO}, a speculative physics research program (its root CLAUDE.md gives conventions and tags; the wiki's rules are in wiki/CLAUDE.md). Do NOT edit any file in the repository. Scratch files only under work/literature-check/verify/ (create a subfolder for yourself).

The write-up reports a literature check of P.R.'s conjectures (2026-11-02): notes/literature-check.md (the note), review/wiki-build-flags.md section "Found by the literature check" (flags 64-69), the root CLAUDE.md entries dated 2026-11-02, review/literature-check/README.md, verify/literature_check.py, and wiki edits (see \`git -C ${REPO} diff -- wiki/\` and the new pages wiki/method/literature-check.md and wiki/method/verification/literature-check-script.md).

The record behind it: review/literature-check/findings.json (287 merged findings with labels, verifier verdicts, quotes, summary, difference, basis), panel/*.out.json (seven judges), panel/C*.evidence.json, round1/ round2/ round3/ (agents' outputs and query logs), recheck.json and recheck.out (the code check of identifiers and quotations), preregistration.md, sources.json, quotes.json, tools/consolidate.py. The program's documents: papers/broken-born-checkpoint-v2.md (#11), notes/*.md (notably notes/velocity-gated-gravity.md), papers/phase-space-diameter.md. To read a paper's text use \`python3 ${REPO}/work/literature-check/tools/lit.py text <arXiv id> --grep '<regex>' --context 300\` (it has a cache; avoid OpenAlex).

Two independent reviewers reported the findings below: F1-F20 on the note, flags, CLAUDE.md and README; W1-W20 on the wiki. Reviewers can be wrong. For each finding assigned to you, try to refute it: open the files it cites and the record, and decide from the evidence. confirmed = the finding is right as stated; partly = right in part (say which part); refuted = wrong. Then give the exact edits that would fix what is confirmed: for each, the file, a short unique excerpt of the current text (copied exactly, so it can be found by string match), and the proposed replacement. Write the replacement in the file's own style: in the wiki, state the claim and not the discussion, name the person P.R., add no number that the note or another source does not contain, and carry tags over exactly; in the note and flags, plain precise prose. If a fix needs a decision only P.R. can make (a new flag, a change to #11), say so in needs_decision instead of proposing it as an edit. Keep each evidence string under 120 words.`

const REVIEWS = `${args.fidelity}\n\n=====\n\n${args.wiki}`

const GROUPS = [
  { key: 'c5-c7-content', ids: 'F1, F8, F16, F18 (the Delbourgo-Lashmar attribution part), F20 (the Guth et al. wording part); W1, W2, W16 (its Henry-Couannier and Delbourgo-Lashmar parts)' },
  { key: 'c1-novelty', ids: 'F2, F7, F14; W8, W11, W16 (its founding-suppositions part)' },
  { key: 'method-counts', ids: 'F3, F4, F5, F6, F17, F19; W6, W14, W15. For F4 and F5 compute exact counts from findings.json and recheck.json with code (how many findings are single-agent overall and among anticipates/partial/evidence-against; how many verdict-carrying quotations were found by code and how many only by web fetch, from which sources; how many identifiers did not resolve and what labels those findings carry), and report the code you ran.' },
  { key: 'c2-c3-c4-content', ids: 'F9, F10, F11, F15, F20 (the Govaerts wording part); W7, W16 (its Goldhaber part), and the closing remark of the wiki review on the C3 ground "electric-magnetic, not position-momentum" against Gibbons and Herdeiro 2001.' },
  { key: 'flags-and-pointers', ids: 'F12, F13, F18 (its flag 67 and flag 68 audit parts); W9, W13, W17' },
  { key: 'stale-wiki', ids: 'W3, W4, W5, W10, W12, W18, W19, W20. Search the whole wiki for further statements of the same kinds that the write-up made false (counts of flags or scripts, statements that the gate only checks arithmetic, statements of novelty contradicted by the note) and report them as extra findings named X1, X2, ...' },
]

const EDIT = { type: 'object', properties: { file: { type: 'string' }, current: { type: 'string' }, proposed: { type: 'string' } }, required: ['file', 'current', 'proposed'] }
const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    results: { type: 'array', items: { type: 'object', properties: {
      finding: { type: 'string' },
      verdict: { type: 'string', enum: ['confirmed', 'partly', 'refuted'] },
      evidence: { type: 'string' },
      edits: { type: 'array', items: EDIT },
      needs_decision: { type: 'string' },
    }, required: ['finding', 'verdict', 'evidence', 'edits', 'needs_decision'] } },
    notes: { type: 'string' },
  },
  required: ['results', 'notes'],
}

const QUOTE = { type: 'object', properties: { text: { type: 'string' }, where: { type: 'string' }, check: { type: 'string' } }, required: ['text', 'where', 'check'] }
const RERUN_SCHEMA = {
  type: 'object',
  properties: {
    queries_run: { type: 'array', items: { type: 'object', properties: {
      conjecture: { type: 'string' }, database: { type: 'string' }, query: { type: 'string' }, hits: { type: 'integer' },
      new_records_screened: { type: 'integer' }, read_in_full: { type: 'integer' } },
      required: ['conjecture', 'database', 'query', 'hits', 'new_records_screened', 'read_in_full'] } },
    findings: { type: 'array', items: { type: 'object', properties: {
      conjecture: { type: 'string' }, id: { type: 'string' }, citation: { type: 'string' },
      relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision'] },
      summary: { type: 'string' }, difference: { type: 'string' }, quotes: { type: 'array', items: QUOTE } },
      required: ['conjecture', 'id', 'citation', 'relation', 'summary', 'difference', 'quotes'] } },
    khademi_2009: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['queries_run', 'findings', 'khademi_2009', 'notes'],
}
const CHECK_SCHEMA = {
  type: 'object',
  properties: { id: { type: 'string' }, conjecture: { type: 'string' },
    verified_relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision', 'reject'] },
    metadata_ok: { type: 'boolean' }, quotes_ok: { type: 'string' }, reason: { type: 'string' } },
  required: ['id', 'conjecture', 'verified_relation', 'metadata_ok', 'quotes_ok', 'reason'],
}

const RERUN_PROMPT = `You complete the literature check of P.R.'s conjectures in ${REPO}. On 2026-11-02 its round-3 coverage sweeps ran out of OpenAlex's free daily quota (HTTP 429), so several planned queries never ran. Today the quota has reset. Do NOT edit any file in the repository outside work/literature-check/round5/ (create it; put your notes and outputs there).

Read review/literature-check/brief.md first: it states the seven conjectures C1-C7, the relation labels (anticipates, partial, related, evidence-against, collision) and the method. Then:
1. Collect every query recorded as not run (hits "not run", "OpenAlex error 429", "HTTP 429" or similar) in review/literature-check/round3/*.json (the "queries" lists) and in the query logs round3/*.queries.* and round1/*. List them with their conjecture.
2. Run each with the check's own tool: \`python3 ${REPO}/work/literature-check/tools/lit.py openalex '<query>' --field title_and_abstract --abstracts\` (see \`lit.py\` for options; one request per query, no repeats; stop if OpenAlex returns 429 again and say so). Where a query used another field, use it.
3. Screen the hits against what the check already assessed: the ids in review/literature-check/findings.json and review/literature-check/round3/known.json. For each new record whose title or abstract could bear on a conjecture, read it (lit.py show / text for arXiv; lit.py doi for Crossref) and judge its relation to the conjecture. Check every quotation you use with \`lit.py quote <id> '<verbatim text>'\` and record the result in "check".
4. Try once more to read the unread item for C3: S. Khademi, "Why magnetic monopoles are not seen" (2009), Maltepe University open-access repository, handle 20.500.12415/6128, OpenAlex W3153563614. Its repository returned HTTP 403 before. Try other public routes (the handle server, OAI-PMH, CORE, BASE, OpenAlex locations, Semantic Scholar's public API) without registering for anything and without sending any personal data. Report what it says, or that it stays unreadable, in khademi_2009.
Return every new finding at related or stronger, and list collisions only if they could mislead. Be conservative: anticipates only if a paper states the conjecture in substance.`

phase('Verify')
log(`Verifying ${GROUPS.length} groups of review findings; rerunning the blocked OpenAlex queries in parallel.`)

const verifyAll = parallel(GROUPS.map(g => () => agent(
  `${COMMON}\n\nYour assigned findings: ${g.ids}.\n\nThe two reviews:\n\n${REVIEWS}`,
  { label: `verify:${g.key}`, phase: 'Verify', schema: VERIFY_SCHEMA })))

const rerunAndCheck = (async () => {
  const rerun = await agent(RERUN_PROMPT, { label: 'rerun:openalex', phase: 'Rerun', schema: RERUN_SCHEMA })
  if (!rerun) return { rerun: null, checks: [] }
  const strong = (rerun.findings || []).filter(f => ['anticipates', 'partial', 'evidence-against'].includes(f.relation))
  log(`Rerun: ${(rerun.queries_run || []).length} queries run, ${(rerun.findings || []).length} new findings, ${strong.length} strong.`)
  const checks = await parallel(strong.map(f => () => agent(
    `You are an adversarial verifier for the literature check of P.R.'s conjectures in ${REPO}. Do NOT edit repository files; scratch only under work/literature-check/round5/check/. Read review/literature-check/brief.md for the conjectures and labels. A searcher reports this finding:\n\n${JSON.stringify(f, null, 1)}\n\nResolve the identifier (python3 ${REPO}/work/literature-check/tools/lit.py show <id>, or lit.py doi <doi>), check that the metadata matches the citation, find every quotation again with lit.py quote, read the passage in context, and decide the relation yourself. Default to the weaker label if in doubt; reject if the paper does not say what the finding claims.`,
    { label: `check:${f.id}`, phase: 'Check', schema: CHECK_SCHEMA })))
  return { rerun, checks: checks.filter(Boolean) }
})()

const [verifs, rc] = await Promise.all([verifyAll, rerunAndCheck])
return { verifications: verifs.filter(Boolean), rerun: rc.rerun, checks: rc.checks }
