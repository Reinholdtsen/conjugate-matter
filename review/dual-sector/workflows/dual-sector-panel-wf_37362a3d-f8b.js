export const meta = {
  name: 'dual-sector-panel',
  description: 'Panel on the Minic school vs C1: two advocates, a content judge, an overlap judge and a completeness critic',
  phases: [
    { title: 'Judge', detail: 'four judges and a critic, in parallel, on the verified evidence' },
  ],
}

const REL = { type: 'string', enum: ['same', 'close-variant', 'partial', 'related', 'different', 'absent-in-school', 'undetermined'] }
const VERD = { type: 'string', enum: ['holds', 'holds-with-qualification', 'does-not-hold', 'undetermined'] }
const CONF = { type: 'string', enum: ['high', 'medium', 'low'] }

const JUDGE_SCHEMA = {
  type: 'object',
  properties: {
    elements: {
      type: 'array',
      description: 'one entry for each of E1..E10',
      items: {
        type: 'object',
        properties: {
          element: { type: 'string', enum: ['E1 identification', 'E2 what conjugate or dual means', 'E3 field content', 'E4 coupling between the sectors', 'E5 detection', 'E6 gravity', 'E7 dynamics and self-interaction', 'E8 monopoles', 'E9 vacuum and the choice of polarization', 'E10 dark energy'] },
          program: { type: 'string', description: 'what the program states, with its #11 section' },
          school: { type: 'string', description: 'what the school states, with paper id, location and a short verbatim quotation' },
          relation: REL,
          note: { type: 'string' },
        },
        required: ['element', 'program', 'school', 'relation', 'note'],
      },
    },
    propositions: {
      type: 'array',
      description: 'one entry for each of P1..P4',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', enum: ['P1 core published', 'P2 their sector correlated with ours', 'P3 neither form found', 'P4 overlap beyond C1'] },
          verdict: VERD,
          confidence: CONF,
          reason: { type: 'string' },
          evidence: { type: 'array', items: { type: 'string' }, description: 'paper id, location, short quotation' },
          suggested_wording: { type: 'string', description: 'how the record should state it, one or two plain sentences' },
        },
        required: ['id', 'verdict', 'confidence', 'reason', 'evidence', 'suggested_wording'],
      },
    },
    priority: {
      type: 'object',
      properties: {
        earliest_public: { type: 'string', description: 'earliest public statement of the identification (any medium), with date and source' },
        earliest_in_print: { type: 'string', description: 'earliest written, posted or published statement, with date and source' },
        precursors: { type: 'array', items: { type: 'string' }, description: 'earlier statements of something narrower (e.g. metaparticles as dark-matter quanta), dated' },
        independent: { type: 'array', items: { type: 'string' }, description: 'statements outside the school, dated, with what they say and how close they are' },
      },
      required: ['earliest_public', 'earliest_in_print', 'precursors', 'independent'],
    },
    overlaps_beyond_c1: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          program_claim: { type: 'string', description: 'which conjecture or claim: C2..C7, App. A item n, P1..P5, the hard core, a derived result; with its #11 section' },
          school_work: { type: 'string', description: 'paper id, date, location, short quotation' },
          relation: REL,
          before_program: { type: 'boolean', description: 'posted before September 2026' },
          note: { type: 'string' },
        },
        required: ['program_claim', 'school_work', 'relation', 'before_program', 'note'],
      },
    },
    summary_line: {
      type: 'object',
      properties: {
        verdict: { type: 'string', description: 'on the sentence "Its core is published (Minic and coauthors, 2020), their sector correlated with ours; neither form was found."' },
        suggested: { type: 'string', description: 'a replacement of at most 35 words for an executive summary that states claims, not how statuses came about' },
      },
      required: ['verdict', 'suggested'],
    },
    record_changes: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string', description: 'repo path and section' },
          passage: { type: 'string', description: 'the passage as it stands, quoted' },
          change: { type: 'string', description: 'what it should say, or what to add' },
          evidence: { type: 'string' },
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
        required: ['file', 'passage', 'change', 'evidence', 'severity'],
      },
    },
    dissent: { type: 'string', description: 'where you disagree with the verifiers or with the evidence as assembled, and why' },
  },
  required: ['elements', 'propositions', 'priority', 'overlaps_beyond_c1', 'summary_line', 'record_changes', 'dissent'],
}

const CRITIC_SCHEMA = {
  type: 'object',
  properties: {
    gaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          gap: { type: 'string' },
          kind: { type: 'string', enum: ['paper not read', 'question unanswered', 'claim unverified', 'search not run', 'reading disputed', 'record not checked', 'other'] },
          could_change: { type: 'string', description: 'which proposition or element it could change, and in which direction' },
          action: { type: 'string', description: 'what to do, concretely: which paper, which query, which passage' },
          priority: { type: 'string', enum: ['high', 'medium', 'low'] },
          tried_now: { type: 'string', description: 'if you tried it yourself: what you found; else empty' },
        },
        required: ['gap', 'kind', 'could_change', 'action', 'priority', 'tried_now'],
      },
    },
    overall: { type: 'string' },
  },
  required: ['gaps', 'overall'],
}

const COMMON = `You sit on the panel of the dual-sector investigation of the Comatter program's record.

Read first, in full: work/dual-sector/inputs/brief.md (the question, the three clauses under test, the tools and rules), work/dual-sector/inputs/program.md (the program's own statements, verbatim from #11) and work/dual-sector/panel/by-question.md (about 420 KB: every answer of nine readers who read some 45 papers of Djordje Minic and coauthors, each followed by an independent verifier's verdict and correction, and 45 points where a reader or verifier found the record contradicted or qualified, each with a verdict). Read by-question.md in chunks until you have read all of it. Supporting files: work/dual-sector/panel/papers.md (each reader's papers, how each was read, leads), panel/missed.md (201 passages the verifiers added), panel/statements.json (all 995 quoted statements with their verdicts; search it with grep or python). Where a verifier's correction and a reader's answer differ, the verifier governs unless you re-read the source and find otherwise; say so under dissent.

Every quotation in the evidence was found again in its source by code. You may re-read any source with the literature tool (from work/dual-sector/: ../../.venv/bin/python tools/lit.py text ID --grep '...' --context 1500, or lit.py quote ID '...'). You must re-read the source yourself before resting a verdict on a passage whose verification was confirmed-in-part or refuted. Your scratch folder is work/dual-sector/scratch/LABEL/ (LABEL your label); write nothing elsewhere and edit no repository file.

The elements to compare, the program against the school: E1 identification (dark matter as the counterpart of ordinary matter in the conjugate or dual description); E2 what "conjugate" or "dual" means (the program: the other Lagrangian polarization of one phase space at hbar; the school: x-tilde, in which senses); E3 field content; E4 coupling between the sectors; E5 detection; E6 gravity; E7 dynamics and self-interaction (the program's chi form has a velocity-gated self-interaction, #11 §8); E8 monopoles (the program's other form: magnetically charged solitons localized in momentum, #11 §12, §11.4); E9 vacuum and the choice of polarization (#11 §3, P2', P5); E10 dark energy (#11 §10).

The propositions: P1 "Its core is published (Minic and coauthors, 2020)": the identification is published, and by when; P2 "their sector correlated with ours": as a difference from the program, whose sectors couple by gravity alone (P4 strict, §13 row 7); P3 "neither form was found": neither the chi form nor the monopole form is in the literature; P4 the school's published claims overlap with other conjectures or core claims of the program beyond C1 (P.R.'s conjectures C2 to C7, Appendix A's founding suppositions, the hard core and postulates P1 to P5, derived results such as a*a-tilde = 1 or the compatibility theorem).

Rules for your verdicts: prior art says who stated an idea first and changes no claim's status; a restatement after September 2026 is not prior art; label inferences as yours; plain words, no hype, no merit verdicts on either side.`

const JUDGES = [
  { label: 'j-identity', role: 'You are the judge asked to argue for overlap. First make the strongest honest case that the school\'s published proposal is P.R.\'s conjecture C1 in substance, and that the record and the summary line understate the overlap, on every element. Then, separately and on the evidence, give your own verdicts: they need not follow your case.' },
  { label: 'j-difference', role: 'You are the judge asked to argue for difference. First make the strongest honest case that the school\'s proposal differs from C1 in substance, and that the record and the summary line overstate the overlap, on every element. Then, separately and on the evidence, give your own verdicts: they need not follow your case.' },
  { label: 'j-content', role: 'You are the content judge. Compare element by element, neutrally, and give your verdicts. Spend most care on P1 (dates: the 2019 slides, the 2016-2017 precursors, FLM 2019 unread) and P2 (what "correlated" means in each paper, and Hübsch and Minic 2024 §5.3, "only gravitationally").' },
  { label: 'j-overlap', role: 'You are the overlap judge. Fill the elements briefly, and spend most care on P4: map every place where the school\'s published work meets a conjecture or core claim of the program other than C1, with its date and closeness: among others the preferred polarization and its selection (2104.00802 "at the level of the vacuum sector"; 2212.06086 "effectively spontaneously broken"; 2610.19522 §3.2 eta = HJ), the compatibility theorem for positive H (1606.01829), a*a-tilde = 1 against Hur et al. 2025 (delta x delta x-tilde ~ lambda^2), dark energy and C5, the E8 Langlands pairing and C4, the null-detection explanations and C3 or §13 row 7, and anything else in the evidence. For each, say what #11 or the wiki would need to cite or change.' },
]

phase('Judge')
const tasks = JUDGES.map(j => () => agent(`${COMMON}\n\nYour label: ${j.label}.\n\n${j.role}\n\nThen list record_changes: every passage of the record (root CLAUDE.md 'Since the handoff', notes/literature-check.md, review/wiki-build-flags.md item 64 and its neighbours, wiki/papers/broken-born-checkpoint-v2.md, wiki pages) that the evidence shows needs changing, with the change. Changes to #11 itself are proposals for P.R.'s ruling; say so.`, { label: j.label, phase: 'Judge', schema: JUDGE_SCHEMA }))
tasks.push(() => agent(`${COMMON}\n\nYour label: critic.\n\nYou are the completeness critic. Do not judge the propositions. Find what is missing: assigned papers not read or read only by abstract; questions without primary evidence; statements resting on a single reader with no verifier; leads no one followed (papers.md lists them); search modalities not run (for example forward citations of the 2019 Belgrade slides' content, conference abstracts, the school's 2026 papers after 14 October 2026, other languages); readings the verifiers disputed and left unresolved; record files no one checked. For each gap say what it could change and what to do. Where a gap can be closed with a few tool calls, close it now and report what you found under tried_now. Rank by how likely the gap is to change a verdict.`, { label: 'critic', phase: 'Judge', schema: CRITIC_SCHEMA }))

const out = await parallel(tasks)
const names = JUDGES.map(j => j.label).concat(['critic'])
const result = {}
out.forEach((o, i) => { result[names[i]] = o })
log('returned: ' + names.filter((n, i) => out[i]).join(', '))
return result
