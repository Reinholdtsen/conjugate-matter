export const meta = {
  name: 'literature-check-verdicts',
  description: "A panel of independent judges tests the per-conjecture verdicts of the literature check on the verified evidence",
  phases: [
    { title: 'Judge', detail: 'three judges with different lenses for C1; one each for C4, C5, C6; one for C2, C3 and C7' },
  ],
}

const JUDGE = { type: 'object', properties: {
  conjectures: { type: 'array', items: { type: 'object', properties: {
    conjecture: { type: 'string', enum: ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'] },
    verdict: { type: 'string', enum: ['anticipated', 'partly anticipated', 'related only', 'nothing relevant'] },
    closest: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, why: { type: 'string' } }, required: ['id', 'why'] } },
    new_in_conjecture: { type: 'string', description: 'What the conjecture states that the literature found does not, in two to four plain sentences' },
    published_parts: { type: 'string', description: 'What of the conjecture is already published, by whom and since when, in two to four plain sentences' },
    label_disputes: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, current: { type: 'string' }, proposed: { type: 'string' }, reason: { type: 'string' } },
      required: ['id', 'current', 'proposed', 'reason'] } },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] } },
    required: ['conjecture', 'verdict', 'closest', 'new_in_conjecture', 'published_parts', 'label_disputes', 'confidence'] } },
  notes: { type: 'string' } },
  required: ['conjectures', 'notes'] }

const COMMON = `Read work/literature-check/BRIEF.md first: it defines P.R.'s conjectures C1-C7 and the relation labels. Three rounds of search and ` +
  `verification produced the evidence in work/literature-check/panel/<conjecture>.json: "strong_findings" (anticipates, partial, evidence-against, ` +
  `with summaries, differences, verbatim quotes checked by code, and the verifiers' verdicts), "related" and "collisions" in brief, and the ` +
  `searchers' and verifiers' "not_found_statements". You are a judge, not a searcher: do not hunt for new papers. You may and should read the ` +
  `cited passages yourself (python3 work/literature-check/tools/lit.py text ID --grep REGEX, or lit.py show ID) and the conjecture's sources in ` +
  `the repository (#11 is wiki/papers/broken-born-checkpoint-v2.md; the wiki page named in the brief). A conjecture's verdict is the strongest relation ` +
  `that survives your reading: anticipated (a work states the conjecture in substance), partly anticipated (a work states a central part, one of ` +
  `its forms, or a close variant), related only, or nothing relevant. Dispute any label you read differently, in either direction, with reasons. ` +
  `Then say plainly what of the conjecture is published (by whom, since when) and what it states that the literature found does not.`

const JUDGES = [
  { key: 'c1-content', conj: ['C1'], lens: `Your lens is physical content. Decide whether the works labeled "anticipates" state the same ` +
    `physical claim as C1. In particular: is the Minic school's dual spacetime x̃ the momentum (energy-momentum) side of phase space, as conjugate ` +
    `matter's momentum polarization is? Is "the dual Standard Model is the dark matter" the same claim as "dark matter is the momentum-polarized ` +
    `counterpart of ordinary matter, gravitating like ours"? Read the passages, and #11 §1, §3-§4, §8, §12 and App. A item 4.` },
  { key: 'c1-scope', conj: ['C1'], lens: `Your lens is scope and chronology. Decide which parts of C1 the literature covers: the identification; ` +
    `its two forms (χ particles with a velocity-gated self-interaction; conjugate monopoles); the coupling through gravity only (strict P4) and ` +
    `its consequence, a permanent direct-detection null; the spontaneous breaking that selects the polarization. Check the dates (the earliest ` +
    `statement and its venue) and say how a verdict of "anticipated" should be qualified, if at all.` },
  { key: 'c1-advocate', conj: ['C1'], lens: `Your lens is advocacy for novelty, held to evidence. Build the strongest honest case that C1, as the ` +
    `program states it, is not anticipated: that the published claims differ from it in substance. Then weigh that case against the evidence and ` +
    `give your own verdict. If the case fails, say exactly why.` },
  { key: 'c4', conj: ['C4'], lens: `Test every label in both directions. Note that #11 treats the full magnetic mirror family as established ` +
    `physics (Montonen-Olive; App. A item 11) and calls its placement in the momentum polarization the conjecture (§11.4): decide whether works ` +
    `that put magnetically charged dark matter in an ordinary hidden sector state a central part or form of C4, or only its established half.` },
  { key: 'c5', conj: ['C5'], lens: `Test every label in both directions. The partials come from other frameworks (conformal frames, double ` +
    `field theory, pre-big-bang, Dark Gravity): decide which of them state a central part, form or close variant of C5 and which share only its ` +
    `shape. Also judge the verifier's note that the program's dictionary w_eff = -w̃ is scale-factor duality with sources.` },
  { key: 'c6', conj: ['C6'], lens: `Test every label in both directions. The partials are Bose-condensation papers: decide whether Bose ` +
    `condensation of dark matter (condensation into low-momentum states) states a central part or form of C6, the clumping of dark matter in ` +
    `momentum space as ordinary matter clumps in position, or only shares its theme.` },
  { key: 'c2-c3-c7', conj: ['C2', 'C3', 'C7'], lens: `Each of these is "related only" on the evidence. Check whether anything in the ` +
    `evidence was understated (a work that states the conjecture, a central part or a close variant), whether the closest works named are the ` +
    `right ones, and whether any evidence-against item is overstated.` },
]

phase('Judge')
const out = await parallel(JUDGES.map(j => () => agent(
  `${COMMON}\n\nYou judge ${j.conj.join(', ')}; read panel/${j.conj.join('.json, panel/')}.json. ${j.lens}\n\n` +
  `Keep notes in work/literature-check/panel/${j.key}/. Before finishing, write your output as JSON to ` +
  `work/literature-check/panel/${j.key}.out.json. Return the structured output.`,
  { label: `judge:${j.key}`, phase: 'Judge', schema: JUDGE }).then(r => ({ key: j.key, result: r }))))
return { judges: out.filter(Boolean) }
