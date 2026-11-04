export const meta = {
  name: 'literature-check-coverage',
  description: 'Search venues and lineages the first two rounds could not reach; verify any strong match adversarially',
  phases: [
    { title: 'Sweep', detail: 'three OpenAlex and web sweeps by conjecture, one agent on older and separate lineages' },
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
  citation: { type: 'string', description: 'Authors, title, venue (journal, preprint, book, thesis, non-reviewed), year' },
  relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision'] },
  summary: { type: 'string' }, difference: { type: 'string' },
  quotes: { type: 'array', items: QUOTE },
  confidence: { type: 'string', enum: ['high', 'medium', 'low'] } },
  required: ['conjecture', 'id', 'citation', 'relation', 'summary', 'difference', 'quotes', 'confidence'] }
const QUERY = { type: 'object', properties: { database: { type: 'string' }, query: { type: 'string' }, hits: { type: 'string' } },
  required: ['database', 'query', 'hits'] }
const SWEEP = { type: 'object', properties: {
  sweep: { type: 'string' },
  findings: { type: 'array', items: FINDING },
  queries: { type: 'array', items: QUERY },
  not_found: { type: 'array', items: { type: 'object', properties: {
    conjecture: { type: 'string' }, statement: { type: 'string' } }, required: ['conjecture', 'statement'] } },
  unverified_leads: { type: 'array', items: { type: 'object', properties: {
    lead: { type: 'string' }, why_unverified: { type: 'string' } }, required: ['lead', 'why_unverified'] } },
  notes: { type: 'string' } },
  required: ['sweep', 'findings', 'queries', 'not_found', 'unverified_leads', 'notes'] }
const VERDICTS = { type: 'object', properties: {
  verdicts: { type: 'array', items: { type: 'object', properties: {
    id: { type: 'string' }, conjecture: { type: 'string' }, claimed_relation: { type: 'string' },
    verified_relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision', 'reject'] },
    metadata_ok: { type: 'boolean' }, quotes_ok: { type: 'string' }, reason: { type: 'string' } },
    required: ['id', 'conjecture', 'claimed_relation', 'verified_relation', 'metadata_ok', 'quotes_ok', 'reason'] } },
  notes: { type: 'string' } },
  required: ['verdicts', 'notes'] }

const COMMON = `Read work/literature-check/BRIEF.md first: it defines the conjectures C1-C7, the tools, the quoting standard and the relation labels. ` +
  `Two rounds of searching have already run, mostly through INSPIRE and arXiv. The papers they found are in work/literature-check/round3/known.json; ` +
  `report only papers that are not on that list (or, with reasons, a reading of a listed paper that differs substantially from its label there). ` +
  `Your job is coverage the earlier rounds could not reach. Use the new tool command lit.py openalex (OpenAlex indexes about 250 million works: ` +
  `journals, books, theses and proceedings outside arXiv and INSPIRE; phrase search with --field title_and_abstract '"phrase"', and --field fulltext ` +
  `where OpenAlex has the full text), WebSearch (mode extended for niche queries) and WebFetch, as well as the other lit.py commands. For a work ` +
  `outside arXiv, resolve its DOI with lit.py doi and quote from its abstract or a page you fetch; record "checked by WebFetch only" where the tool ` +
  `cannot reach the text. State each venue plainly, including non-reviewed ones (Zenodo, viXra, ResearchGate, personal sites), and do not label a ` +
  `non-reviewed work above "related" unless it states the conjecture itself. Record every query.`

const SWEEPS = [
  { key: 'oa-c1-c6-c7', task: `Conjectures C1, C6 and C7. Search for: dark matter as the matter of momentum space, the conjugate or reciprocal ` +
    `sector, the dual or "other half" of phase space, or a mirror copy organized in velocity; dark matter that clumps or condenses in velocity or ` +
    `momentum space, Jeans instability in velocity space, flocking or streams by velocity; and long-range attractions, gravitational or not, that ` +
    `act only (or most strongly) between bodies with similar velocities, including Weber-type and relational mechanics.` },
  { key: 'oa-c2-c3-c4', task: `Conjectures C2, C3 and C4. Search for: magnetic monopoles or magnetic charge in momentum space or phase space as ` +
    `matter or dark matter; explanations of the absence of observed monopoles by their living in another space, sector or representation; and ` +
    `a magnetically charged counterpart of every electrically charged particle placed in a dual, conjugate, reciprocal or momentum-space sector, ` +
    `including any work joining Born reciprocity, Fourier duality or T-duality to electric-magnetic duality.` },
  { key: 'oa-c5', task: `Conjecture C5. Search for: a dual, conjugate, reciprocal, mirror or momentum-space universe that contracts or collapses ` +
    `while ours expands, and whose contraction or collapse drives our accelerated expansion or acts as dark energy; stiff or kinetic-dominated ` +
    `matter in such a sector acting on ours as a cosmological constant; "their collapse is our acceleration" in any wording.` },
  { key: 'lineages', task: `All seven conjectures, through lineages the earlier rounds touched little or not at all. At least: Kadyshevsky's ` +
    `geometric approach with a curved (de Sitter or anti-de Sitter) momentum space and a fundamental mass, including any dark-matter or "exotic ` +
    `particle" proposal; Wheeler and Hazboun's biconformal gravity; Caianiello's quantum geometry and maximal acceleration; Takabayasi and ` +
    `Yukawa's bilocal fields; Born's own later papers and his school (Born, Green, Fuchs) on reciprocity; Weber-type velocity-dependent gravity ` +
    `(Assis's relational mechanics); J.-P. Petit's Janus cosmology; Moffat's momentum-representation gravity; Hess and Greiner's pseudo-complex ` +
    `general relativity; and any further lineage you find in which position and momentum are treated symmetrically in cosmology or matter. ` +
    `Follow each lineage's citation graph where INSPIRE or OpenAlex has it.` },
]

phase('Sweep')
const results = await pipeline(
  SWEEPS,
  (s) => agent(`${COMMON}\n\nYour sweep is ${s.key}. ${s.task}\n\nKeep notes in work/literature-check/round3/${s.key}/. Before finishing, write your ` +
    `output as JSON to work/literature-check/round3/${s.key}.json. Return the structured output.`,
    { label: `sweep:${s.key}`, phase: 'Sweep', schema: SWEEP }),
  (out, s) => {
    const strong = (out && out.findings || []).filter(f => f.relation === 'anticipates' || f.relation === 'partial')
    if (!strong.length) return { key: s.key, out, verify: null }
    return agent(
      `Read work/literature-check/BRIEF.md first. You are an independent, adversarial verifier. A sweep labeled the findings below as "partial" ` +
      `or "anticipates" for one of P.R.'s conjectures. Test each one in both directions: resolve the identifier (lit.py show, lit.py doi, or ` +
      `lit.py openalex for works outside arXiv) and confirm title, authors, year and venue; check every quote (lit.py quote, or WebFetch for ` +
      `works the tool cannot reach); read the passages the claim rests on; and decide whether the work states the conjecture or a central part ` +
      `of it, or only shares words or a theme. A non-reviewed work counts only if it states the conjecture itself. Set verified_relation, or ` +
      `"reject" with your reason. Write your output as JSON to work/literature-check/round3/${s.key}.verify.json before finishing.\n\n` +
      `Findings (JSON):\n${JSON.stringify(strong)}`,
      { label: `verify:${s.key}`, phase: 'Verify', schema: VERDICTS })
      .then(verify => ({ key: s.key, out, verify }))
  },
)
const done = results.filter(Boolean)
log(`${done.length} of ${SWEEPS.length} sweeps done`)
return { sweeps: done }
