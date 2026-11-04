export const meta = {
  name: 'literature-check',
  description: "Search the published literature for each of P.R.'s seven conjectures, then verify every finding independently",
  phases: [
    { title: 'Search', detail: 'five agents, one per group of conjectures, at least five search modalities each' },
    { title: 'Verify', detail: 'an independent verifier per group: identifiers, quotes, labels, and a hunt for missed prior art' },
  ],
}

const QUOTE = { type: 'object', properties: {
  text: { type: 'string' },
  where: { type: 'string', description: 'abstract, or the full-text section' },
  check: { type: 'string', description: "lit.py quote verdict, or 'checked by WebFetch only'" } },
  required: ['text', 'where', 'check'] }
const FINDING = { type: 'object', properties: {
  conjecture: { type: 'string', enum: ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'] },
  id: { type: 'string', description: 'arXiv id, doi:..., or recid:N' },
  citation: { type: 'string', description: 'Authors, title, venue (journal with volume and page, arXiv preprint only, proceedings, book, non-reviewed), year' },
  relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision'] },
  summary: { type: 'string', description: 'What the paper proposes or shows, as it bears on the conjecture, in plain words' },
  difference: { type: 'string', description: "How it differs from P.R.'s conjecture" },
  quotes: { type: 'array', items: QUOTE },
  confidence: { type: 'string', enum: ['high', 'medium', 'low'] } },
  required: ['conjecture', 'id', 'citation', 'relation', 'summary', 'difference', 'quotes', 'confidence'] }
const QUERY = { type: 'object', properties: {
  database: { type: 'string' }, query: { type: 'string' }, hits: { type: 'string' } },
  required: ['database', 'query', 'hits'] }
const SEARCH = { type: 'object', properties: {
  group: { type: 'string' },
  findings: { type: 'array', items: FINDING },
  closest: { type: 'array', items: { type: 'object', properties: {
    conjecture: { type: 'string' }, id: { type: 'string' }, why: { type: 'string' } }, required: ['conjecture', 'id', 'why'] } },
  not_found: { type: 'array', items: { type: 'object', properties: {
    conjecture: { type: 'string' }, statement: { type: 'string' }, searches: { type: 'string' } }, required: ['conjecture', 'statement', 'searches'] } },
  queries: { type: 'array', items: QUERY },
  unverified_leads: { type: 'array', items: { type: 'object', properties: {
    lead: { type: 'string' }, why_unverified: { type: 'string' } }, required: ['lead', 'why_unverified'] } },
  notes: { type: 'string' } },
  required: ['group', 'findings', 'closest', 'not_found', 'queries', 'unverified_leads', 'notes'] }
const VERIFY = { type: 'object', properties: {
  group: { type: 'string' },
  verdicts: { type: 'array', items: { type: 'object', properties: {
    id: { type: 'string' }, conjecture: { type: 'string' }, claimed_relation: { type: 'string' },
    verified_relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision', 'reject'] },
    metadata_ok: { type: 'boolean' },
    quotes_ok: { type: 'string', description: 'for example "3/3 FOUND", or which quotes failed' },
    reason: { type: 'string' } },
    required: ['id', 'conjecture', 'claimed_relation', 'verified_relation', 'metadata_ok', 'quotes_ok', 'reason'] } },
  new_findings: { type: 'array', items: FINDING },
  scoop_searches: { type: 'array', items: QUERY },
  not_found_assessment: { type: 'array', items: { type: 'object', properties: {
    conjecture: { type: 'string' }, holds: { type: 'boolean' }, reason: { type: 'string' } }, required: ['conjecture', 'holds', 'reason'] } },
  notes: { type: 'string' } },
  required: ['group', 'verdicts', 'new_findings', 'scoop_searches', 'not_found_assessment', 'notes'] }

const GROUPS = [
  { key: 'g1-conjugate-matter', conj: ['C1'], areas: `
- Born reciprocity and reciprocal relativity: Born; S. G. Low; Govaerts, Jarvis, Morgan and Low; C. Castro Perelman (many papers, often outside arXiv); S. Bolognesi's "trans-Planckian theory" (arXiv:1207.5514, 1506.02187).
- Metastring theory, modular spacetime, Born geometry and metaparticles (Freidel, Leigh, Minic, Kowalski-Glikman, Rudolph, Svoboda), and the phenomenology of dark matter or of a dual sector in that school (Minic, Jejjala, Kavic, Takeuchi, Berglund, Hübsch, Ng, Edmonds, Farrah, Ho).
- Double field theory and doubled geometry (Hull, Zwiebach, Hohm, Park and collaborators): any dark-matter proposal from dual or winding coordinates.
- Relative locality and curved momentum space (Amelino-Camelia, Freidel, Kowalski-Glikman, Smolin), doubly special relativity, the Yang model, noncommutative phase space: any proposal of matter localized in momentum or of a dark sector.
- Mirror and twin matter (Lee–Yang, Kobzarev–Okun–Pomeranchuk, Foot, Berezhiani), as the structural precedent of a copy of our matter that meets ours only through gravity.
- Dark matter whose self-interaction acts only at low relative velocity, where a paper ties it to momentum-space structure.
- Collisions to note: phase-space density bounds (Tremaine–Gunn) and phase-space methods for halos.` },
  { key: 'g2-monopoles', conj: ['C2', 'C3'], areas: `
- Monopoles in momentum space in condensed matter and semiclassical dynamics: Berry-curvature monopoles (Fang et al. 2003; Xiao, Chang and Niu 2010; Bérard and Mohrbach 2004; Horvathy; Bliokh; Son and Yamamoto 2012; Stephanov and Yin 2012; Weyl semimetals). The question for C2 is whether any paper proposes monopoles localized in momentum as physical objects, as matter or as dark matter.
- Nonassociative phase spaces: the magnetic-monopole phase space and its momentum-space dual, R-flux backgrounds in string theory (Jackiw; Bakas and Lüst; Blumenhagen and Plauschinn; Mylonas, Schupp and Szabo; Lüst, Malek and Szabo; Szabo; Kupriyanov).
- Monopoles under Born reciprocity, T-duality, or in doubled or metastring geometry; Dirac quantization in momentum space; dual monopoles.
- Monopoles and dyons as dark matter, hidden-sector or not, beyond what the record cites.
- Explanations of the absence of monopoles other than inflation (Langacker–Pi; Dvali, Liu and Vachaspati; confinement by strings; monopoles hidden in a mirror or hidden sector, in extra dimensions or in another space), and what present searches assume (MoEDAL, IceCube, MACRO, the Parker bound).` },
  { key: 'g3-magnetic-mirror', conj: ['C4'], areas: `
- Electric–magnetic duality with a full magnetic spectrum: Montonen–Olive, Seiberg, Sen, the dual superconductor ('t Hooft, Mandelstam); two-potential formulations (Cabibbo–Ferrari, Zwanziger).
- Any paper linking position–momentum reciprocity (Born, T-duality, Fourier, symplectic structure) to electric–magnetic duality, so that a conjugate or dual sector is the magnetic one: U-duality joining T- and S-duality (Hull–Townsend); Born geometry or metastring theory and electromagnetic duality; reciprocal or phase-space electrodynamics; the x↔k with B↔Ω duality of semiclassical Berry-curvature dynamics.
- Dark sectors with magnetic charge, under a dark photon or under ours (Terning–Verhaaren; Brummer–Jaeckel; Hook–Huang; millimagnetic charges; magnetic dark matter), and mirror worlds whose particles are magnetic.
- Collisions to note: "magnetic mirror" in plasma confinement and in optics.` },
  { key: 'g4-collapse-acceleration', conj: ['C5'], areas: `
- Scale-factor duality and pre-big-bang cosmology (Veneziano; Gasperini–Veneziano; Tseytlin–Vafa; Brandenberger–Vafa string gas), and how the duality acts on equations of state (w ↔ −w, a contracting dual phase).
- Dark energy from a dual spacetime or a dual sector: metastring and modular-spacetime cosmology (Berglund, Hübsch, Minic; Hur, Jejjala, Kavic, Minic, Takeuchi; Freidel, Kowalski-Glikman, Leigh, Minic); S. Bolognesi's trans-Planckian theory (arXiv:1207.5514, 1506.02187).
- Twin, mirror or partner universes and the cosmological constant or acceleration (Linde 1988; Kaplan–Sundrum 2005; Hossenfelder 2008; J.-P. Petit's Janus model; CPT-symmetric universes).
- Acceleration driven by gravitational collapse (cosmologically coupled black holes: Croker, Weiner, Farrah et al. 2023), and stiff matter in a dual or contracting sector acting as a cosmological constant.
- Collisions to note: wavefunction "collapse" and dark energy; unrelated meanings of "dual".` },
  { key: 'g5-momentum-clumping', conj: ['C6', 'C7'], areas: `
- Condensation and clumping in momentum space: Bose–Einstein condensation as condensation in momentum space; gravitational condensation of dark matter (Sikivie–Yang 2009; Levkov, Panin and Tkachev 2018; Chavanis); kinetic theory of wave dark matter.
- Gravity or attraction acting in momentum space: Born-reciprocal gravity, momentum-space gravity, curved or dynamical momentum space, momentum-space black holes; any paper in which matter clumps in velocity under a force.
- Dark-matter structure in velocity space: streams, caustics (Sikivie), velocity-space substructure; instabilities in velocity space (two-stream), as mechanisms or collisions.
- Long-range or velocity-dependent dark-matter interactions: velocity-dependent self-interaction (Feng, Kaplinghat and Yu; Loeb and Weiner; Tulin, Yu and Zurek), interactions acting only at low relative velocity, long-range forces between dark-matter particles, and any force gated by relative velocity.` },
]

phase('Search')
log('Five searchers start; each search goes to its own verifier as soon as it finishes.')

const results = await pipeline(
  GROUPS,
  (g) => agent(
    `Read work/literature-check/BRIEF.md first and follow it. Your group is ${g.key}: conjecture(s) ${g.conj.join(' and ')}.\n\n` +
    `Areas to cover at least. They are pointers for orientation, not conclusions; go beyond them:${g.areas}\n\n` +
    `Run the method in the brief. Aim for completeness over speed: dozens of queries across the modalities, the citation graph of ` +
    `every paper you label anticipates or partial, and full-text reading wherever a label rests on more than the abstract. ` +
    `Keep notes in work/literature-check/${g.key}/. Before finishing, write your output as JSON to ` +
    `work/literature-check/${g.key}/search.json. Return the structured output.`,
    { label: `search:${g.key}`, phase: 'Search', schema: SEARCH }),
  (search, g) => agent(
    `Read work/literature-check/BRIEF.md first. You are the independent verifier for group ${g.key}: conjecture(s) ${g.conj.join(' and ')}. ` +
    `A search agent returned the findings below. Your job is to test them, not to agree with them.\n\n` +
    `For every finding:\n` +
    `1. Resolve the identifier (lit.py show, or lit.py doi) and confirm that title, authors and year match the citation.\n` +
    `2. Run lit.py quote on every quote. A quote that neither the tool nor WebFetch can find fails.\n` +
    `3. Read the abstract and the passages the claim rests on, and judge the relation yourself. Test it in both directions: is ` +
    `"anticipates" or "partial" overstated (the same words for different physics, or a framework so different that the claim is not ` +
    `the conjecture)? Is "related" understated (the paper does state the conjecture)? Set verified_relation, or "reject" for a citation ` +
    `that is wrong or irrelevant, and give the reason.\n\n` +
    `Then hunt for missed prior art: run at least eight searches of your own, different from the searcher's queries listed below, each ` +
    `aimed at a paper that anticipates or partly anticipates one of the conjectures, and assess each "not found" statement. Report any ` +
    `new paper under new_findings, to the brief's standards (quotes checked with lit.py quote).\n\n` +
    `Keep notes in work/literature-check/${g.key}/. Before finishing, write your output as JSON to work/literature-check/${g.key}/verify.json.\n\n` +
    `The searcher's output (JSON):\n${JSON.stringify(search)}`,
    { label: `verify:${g.key}`, phase: 'Verify', schema: VERIFY })
    .then((verify) => ({ key: g.key, conj: g.conj, search, verify })),
)

const done = results.filter(Boolean)
log(`${done.length} of ${GROUPS.length} groups searched and verified`)
return { groups: done }
