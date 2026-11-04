export const meta = {
  name: 'literature-check-screen',
  description: 'Read every paper the systematic citation screen flagged that no searcher assessed; verify any strong match',
  phases: [
    { title: 'Read', detail: 'four readers, one verdict per flagged paper' },
    { title: 'Verify', detail: 'an adversarial verifier for any partial or anticipating match' },
  ],
}

const QUOTE = { type: 'object', properties: {
  text: { type: 'string' }, where: { type: 'string' },
  check: { type: 'string', description: "lit.py quote verdict, or 'checked by WebFetch only'" } },
  required: ['text', 'where', 'check'] }
const FINDING = { type: 'object', properties: {
  conjecture: { type: 'string', enum: ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'] },
  id: { type: 'string', description: 'arXiv id, doi:..., or recid:N' },
  citation: { type: 'string', description: 'Authors, title, venue, year' },
  relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision'] },
  summary: { type: 'string' }, difference: { type: 'string' },
  quotes: { type: 'array', items: QUOTE },
  confidence: { type: 'string', enum: ['high', 'medium', 'low'] } },
  required: ['conjecture', 'id', 'citation', 'relation', 'summary', 'difference', 'quotes', 'confidence'] }
const READ = { type: 'object', properties: {
  reader: { type: 'string' },
  items: { type: 'array', items: { type: 'object', properties: {
    recid: { type: 'string' },
    verdict: { type: 'string', enum: ['finding', 'not-relevant', 'unavailable'] },
    reason: { type: 'string', description: 'at most about 20 words' } },
    required: ['recid', 'verdict', 'reason'] } },
  findings: { type: 'array', items: FINDING },
  notes: { type: 'string' } },
  required: ['reader', 'items', 'findings', 'notes'] }
const VERDICTS = { type: 'object', properties: {
  verdicts: { type: 'array', items: { type: 'object', properties: {
    id: { type: 'string' }, conjecture: { type: 'string' }, claimed_relation: { type: 'string' },
    verified_relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision', 'reject'] },
    metadata_ok: { type: 'boolean' }, quotes_ok: { type: 'string' }, reason: { type: 'string' } },
    required: ['id', 'conjecture', 'claimed_relation', 'verified_relation', 'metadata_ok', 'quotes_ok', 'reason'] } },
  notes: { type: 'string' } },
  required: ['verdicts', 'notes'] }

const READERS = ['r1-dark-matter', 'r2-monopoles-duality', 'r3-dark-energy', 'r4-triage']

phase('Read')
const results = await pipeline(
  READERS,
  (r) => agent(
    `Read work/literature-check/BRIEF.md first: it defines the conjectures C1-C7, the tools, the quoting standard and the relation labels. ` +
    `Your task is narrower than a search. A systematic screen collected every INSPIRE paper that cites the anchors of the Born-reciprocity ` +
    `lineage (Born 1938 and 1949, Freidel-Leigh-Minic 2013-2016, Born geometry, metaparticles, Low, Bolognesi) and flagged those whose ` +
    `title, abstract or full text mentions a conjecture's subject. Your list, in work/literature-check/round2/${r}.json, holds the flagged ` +
    `papers that no search agent assessed; its "flag" field says why each was flagged.\n\n` +
    `Give every item on the list a verdict. For each: read the abstract (lit.py show recid:N); if it has an arXiv id, grep its full text ` +
    `for the subject terms (lit.py text ID --grep ...) and read the passages; decide whether the paper bears on any of the conjectures ` +
    `named in the file. Most will not: record "not-relevant" with a short reason (for example "mentions dark matter only in the introduction" ` +
    `or "maximal acceleration, unrelated to cosmic acceleration"). Where a paper does bear on a conjecture, record "finding" and add a ` +
    `finding with the brief's relation label and verbatim quotes checked with lit.py quote. Use "unavailable" only when neither abstract ` +
    `nor text can be read. Be skeptical of your own labels: "partial" or "anticipates" needs the paper to state the claim, not share words.\n\n` +
    `Keep notes in work/literature-check/round2/${r}/. Before finishing, write your output as JSON to work/literature-check/round2/${r}.out.json.`,
    { label: `read:${r}`, phase: 'Read', schema: READ }),
  (read, r) => {
    const strong = (read && read.findings || []).filter(f => f.relation === 'anticipates' || f.relation === 'partial')
    if (!strong.length) return { reader: r, read, verify: null }
    return agent(
      `Read work/literature-check/BRIEF.md first. You are an independent, adversarial verifier. A reader labeled the findings below as ` +
      `"partial" or "anticipates" for one of P.R.'s conjectures. Test each one, in both directions: resolve the identifier (lit.py show or ` +
      `lit.py doi) and confirm title, authors and year; run lit.py quote on every quote; read the abstract and the passages the claim rests ` +
      `on; and decide whether the paper really states the conjecture or a central part of it, or only shares words or a theme. Set ` +
      `verified_relation, or "reject" for a wrong or irrelevant citation, with your reason. Write your output as JSON to ` +
      `work/literature-check/round2/${r}.verify.json before finishing.\n\nFindings (JSON):\n${JSON.stringify(strong)}`,
      { label: `verify:${r}`, phase: 'Verify', schema: VERDICTS })
      .then(verify => ({ reader: r, read, verify }))
  },
)
const done = results.filter(Boolean)
log(`${done.length} of ${READERS.length} reading lists done`)
return { readers: done }
