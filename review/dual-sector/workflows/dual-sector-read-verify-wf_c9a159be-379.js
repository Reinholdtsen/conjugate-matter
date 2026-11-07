export const meta = {
  name: 'dual-sector-read-verify',
  description: 'Deep-read the Minic school on dark matter as the dual sector; each reader followed by an adversarial verifier',
  phases: [
    { title: 'Read', detail: 'nine readers, one per cluster of papers' },
    { title: 'Verify', detail: 'one verifier per reader, trying to refute it from the sources' },
  ],
}

const BEARS = ['identification', 'what-dual-is', 'field-content', 'coupling', 'detection', 'gravity', 'dynamics', 'monopoles', 'polarization-selection', 'dark-energy', 'priority', 'other']

const READER_SCHEMA = {
  type: 'object',
  properties: {
    papers: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'arXiv id, recid:N or doi:...' },
          citation: { type: 'string', description: 'authors, title, journal or arXiv, year, as INSPIRE gives them' },
          first_posted: { type: 'string', description: 'first public date: arXiv v1 date, else INSPIRE earliest date' },
          read_how: { type: 'string', description: 'full text (arXiv HTML / ar5iv / PDF via ...), abstract only, or not retrieved: why' },
          mentions_dark_matter: { type: 'boolean' },
          statements: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                quote: { type: 'string' },
                where: { type: 'string' },
                bears_on: { type: 'array', items: { type: 'string', enum: BEARS } },
                reading: { type: 'string', description: 'what it says, plainly, and how it compares with the program (cite #11 section); inferences labeled as yours' },
                quote_check: { type: 'string', description: 'the lit.py quote verdict line, or: not code-checkable: read via ...' },
              },
              required: ['quote', 'where', 'bears_on', 'reading', 'quote_check'],
            },
          },
          summary: { type: 'string' },
        },
        required: ['id', 'citation', 'first_posted', 'read_how', 'mentions_dark_matter', 'statements', 'summary'],
      },
    },
    answers: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string', description: 'Q1 ... Q11, or a short name for another finding' },
          answer: { type: 'string' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          evidence: { type: 'array', items: { type: 'string' }, description: 'paper id and location of each supporting statement' },
        },
        required: ['question', 'answer', 'confidence', 'evidence'],
      },
    },
    contradicts_record: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          record_says: { type: 'string', description: 'the record statement, quoted, with its file and section' },
          source_says: { type: 'string', description: 'the primary-source passage, quoted, with paper id and location' },
          why: { type: 'string' },
        },
        required: ['record_says', 'source_says', 'why'],
      },
    },
    leads: { type: 'array', items: { type: 'string' }, description: 'papers found but not read, each with id and why it may matter' },
    not_retrieved: { type: 'array', items: { type: 'string' }, description: 'papers assigned but not read, each with the reason' },
  },
  required: ['papers', 'answers', 'contradicts_record', 'leads', 'not_retrieved'],
}

const VERDICT = { type: 'string', enum: ['confirmed', 'confirmed-in-part', 'refuted'] }

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    statements: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          paper_id: { type: 'string' },
          quote_start: { type: 'string', description: 'the first ~60 characters of the quotation' },
          quote_found: { type: 'boolean' },
          check_output: { type: 'string' },
          verdict: VERDICT,
          correction: { type: 'string', description: 'empty when confirmed' },
        },
        required: ['paper_id', 'quote_start', 'quote_found', 'check_output', 'verdict', 'correction'],
      },
    },
    answers: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string' },
          verdict: VERDICT,
          correction: { type: 'string' },
          counter_evidence: { type: 'array', items: { type: 'string' }, description: 'quoted passages with paper id and location' },
        },
        required: ['question', 'verdict', 'correction', 'counter_evidence'],
      },
    },
    record_contradictions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          record_says: { type: 'string' },
          verdict: VERDICT,
          note: { type: 'string' },
        },
        required: ['record_says', 'verdict', 'note'],
      },
    },
    missed: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          paper_id: { type: 'string' },
          quote: { type: 'string' },
          where: { type: 'string' },
          bears_on: { type: 'array', items: { type: 'string', enum: BEARS } },
          why_it_matters: { type: 'string' },
          quote_check: { type: 'string' },
        },
        required: ['paper_id', 'quote', 'where', 'bears_on', 'why_it_matters', 'quote_check'],
      },
    },
    retried: { type: 'array', items: { type: 'string' }, description: 'papers the reader could not retrieve: what a second attempt found' },
    overall: { type: 'string', description: 'two or three sentences: how far the reader output can be relied on' },
  },
  required: ['statements', 'answers', 'record_contradictions', 'missed', 'retried', 'overall'],
}

const READERS = [
  { label: 'r1-priority', focus: 'Priority: the earliest statement of the identification, and what the school wrote about dark matter before 2020.', papers: [
    '2003.00318: Minic, "From quantum foundations of quantum field theory, string theory and quantum gravity to dark matter and dark energy" (2020; the proceedings of a talk given in 2019). Read in full, §5 above all.',
    'recid:1590124: Freidel, Leigh, Minic, "Modular Spacetime and Metastring Theory", J. Phys. Conf. Ser. 804, 012032 (2017), not on arXiv; open-access PDF at IOP (doi:10.1088/1742-6596/804/1/012032).',
    'recid:1760046: Freidel, Leigh, Minic, "Manifest non-locality in quantum mechanics, quantum field theory and quantum gravity", Int. J. Mod. Phys. A 34, 1941004 (2019), not on arXiv.',
    'recid:1411938: Freidel, Leigh, Minic, "Modular spacetime" (2015), not on arXiv.',
    '1812.10821: Freidel, Kowalski-Glikman, Leigh, Minic, "Theory of metaparticles" (2018; Phys. Rev. D 2019).',
    '1905.08269: Berglund, Hübsch, Minić, "Dark Energy and String Theory" (2019).',
    '1905.09463: Berglund, Hübsch, Minić, "Dark energy and quantum gravity" (2019).',
    '2104.00802: Freidel, Kowalski-Glikman, Leigh, Minic, "Quantum gravity phenomenology in the infrared" (2021).',
  ], extra: 'Settle Q11 first: list every statement about dark matter in these papers, dated, so that the earliest statement of the identification is fixed. Minic 2020 says it is a talk presented at several venues: find which, with dates, and whether any version of the talk (slides, abstract, video) is public and earlier than the arXiv posting.' },
  { label: 'r2-dual-sm', focus: 'The dual Standard Model as the school builds it, 2020 to 2023.', papers: [
    '2010.15610: Berglund, Hübsch, Minic, "String Theory, the Dark Sector, and the Hierarchy Problem", LHEP 2021, 186. Read in full.',
    '2109.12763: Edmonds, Minic, Takeuchi, "On quantum gravity and quantum gravity phenomenology" (2021).',
    '2111.14205: Berglund, Hübsch, Minic, "Mirror Symmetry, Born Geometry and String Theory" (2021).',
    '2109.01122: Berglund, Hübsch, Minic, "Stringy Bubbles Solve de Sitter Troubles" (2021).',
    '2212.06086: Berglund, Hübsch, Minic, "On de Sitter Spacetime and String Theory", Int. J. Mod. Phys. D 32, 2330002 (2023): §6.5 and every passage on dark matter.',
    '2307.16712: Berglund, Hübsch, Minic, "String Theory Bounds on the Cosmological Constant, the Higgs Mass, and the Quark and Lepton Masses", Symmetry 15, 1660 (2023).',
  ], extra: 'Q3 and Q4 above all: write out the dual sector\'s field content and every term or mechanism that ties it to visible matter, with its stated strength and the limits in which it vanishes; then every observational consequence the papers state (Q5).' },
  { label: 'r3-gravitized', focus: 'The restatements in the school\'s papers on gravitized quantum theory, 2022 to 2026.', papers: [
    '2203.17137: Berglund, Hübsch, Mattingly, Minic, "Gravitizing the quantum" (2022).',
    '2303.15645: Berglund, Geraci, Hübsch, Mattingly, Minic, "Triple interference, non-linear Talbot effect and gravitization of the quantum" (2023).',
    '2305.12593: Minic, "The Vacuum Energy Problem in Quantum Gravity and the Masses of Elementary Particles" (2023); also INSPIRE recid:2778134, a 2024 version.',
    '2407.06207: Hübsch, Minic, "Quantum Gravity as Gravitized Quantum Theory" (2024); §3 above all.',
    '2604.19418: Hübsch, Minic, "Quantum Spacetime, Quantum Gravity and Gravitized Quantum Theory" (2026).',
    '2610.19522: Hübsch, Minic, "Nambu\'s Dynamics, Strings and Gravitized Quantum Theory" (2026).',
    'recid:3204269: Hübsch, Minic, "The Weight of Quantum" (2026), not on arXiv.',
  ], extra: 'How the statement of the identification evolves from 2022 to 2026: any new detail on the dark sector\'s dynamics, coupling, detectability, self-interaction or localization (Q4, Q5, Q7); and how the papers describe "dual" and the choice of polarization (Q2, Q9).' },
  { label: 'r4-pheno', focus: 'The school\'s phenomenology and multi-author papers, and its dark energy.', papers: [
    '2202.05104: Berglund et al. (12 authors), "Quantum Gravity and Phenomenology: Dark Matter, Dark Energy, Vacuum Selection, Emergent Spacetime, and Wormholes" (Snowmass 2022).',
    '2202.06890: Berglund, Freidel, Hübsch, Kowalski-Glikman, Leigh, Mattingly, Minic, "Infrared Properties of Quantum Gravity: UV/IR Mixing, Gravitizing the Quantum - Theory and Observation" (2022).',
    '2111.05659: Addazi et al. (162 authors), "Quantum gravity phenomenology at the dawn of the multi-messenger era - A review" (2021): only the passages on the metastring, the dual sector and dark matter.',
    '2312.00409: Alves Batista et al., "White paper and roadmap for quantum gravity phenomenology in the multi-messenger era" (2023): only the passages on the metastring, the dual sector and dark matter.',
    '2011.08852: Jejjala, Kavic, Minic, Takeuchi, "Dynamical dark energy and infinite statistics" (2020).',
    '2202.05266: Jejjala, Kavic, Minic, Takeuchi, "First Principles Phenomenology of H0" (2022).',
    '2503.20854: Hur, Jejjala, Kavic, Minic, Takeuchi, "Dynamical dark energy, dual spacetime, and DESI" (2025).',
    '2212.00901 and 2303.17495: Freidel, Kowalski-Glikman, Leigh, Minic, "Vacuum energy density and gravitational entropy" (2022) and "On the inevitable lightness of vacuum" (2023): only passages on a dark sector or the dual degrees of freedom.',
  ], extra: 'Q5 and Q10 above all: every stated prediction for the dark sector and for dark energy (values of w, w0, wa, and whether w goes below -1, the value for a cosmological constant), with numbers copied exactly; and what "vacuum selection" means in the Snowmass paper (Q9).' },
  { label: 'r5-mdm', focus: 'Modified Dark Matter (MDM): what the school\'s correlation between dark and visible matter is physically.', papers: [
    '1005.3537: Ho, Minic, Ng, "Cold Dark Matter with MOND Scaling" (2010).',
    '1105.2916: Ho, Minic, Ng, "Quantum Gravity and Dark Matter" (2011).',
    '1201.2365: Ho, Minic, Ng, "Dark Matter, Infinite Statistics and Quantum Gravity" (2012).',
    '1308.3252, 1601.00662, 1602.00055, 1709.04388, 1801.00160: Edmonds, Farrah, Ho, Minic, Ng, Takeuchi and coauthors, the MDM tests and review (2013 to 2018).',
    '2005.08927 and 2009.12915: Edmonds, Minic, Takeuchi, "Dark Matter, Dark Energy and Fundamental Acceleration" and "Presence of a Fundamental Acceleration Scale in Galaxy Clusters" (2020).',
    '2405.08744: Edmonds, Erlich, Minic, Takeuchi, "Universal acceleration and fuzzy dark matter" (2024).',
  ], extra: 'Q4 and Q5 above all: is MDM\'s tie between dark matter and baryons a non-gravitational interaction, a property of the dark quanta (their statistics, a sensitivity to the cosmological constant), or a phenomenological profile? What data do the fits use and what do they find, numbers copied exactly? When, and in which paper, are MDM\'s quanta first identified with the dual or metaparticle sector? Does MDM say anything about direct detection, self-interaction or wave dark matter (Q7)?' },
  { label: 'r6-foundations', focus: 'The foundations: what the school\'s "dual" is, and what selects spacetime.', papers: [
    '1307.7080: Freidel, Leigh, Minic, "Born Reciprocity in String Theory and the Nature of Spacetime", Phys. Lett. B 730, 302 (2014).',
    '1405.3949: Freidel, Leigh, Minic, "Quantum Gravity, Dynamical Phase Space and String Theory" (2014).',
    '1502.08005: Freidel, Leigh, Minic, "Metastring Theory and Modular Space-time", JHEP 06 (2015) 006.',
    '1606.01829: Freidel, Leigh, Minic, "Quantum Spaces are Modular" (2016).',
    '1706.03305: Freidel, Leigh, Minic, "Intrinsic non-commutativity of closed string theory" (2017).',
    '1707.00312: Freidel, Leigh, Minic, "Noncommutativity of closed string zero modes" (2017).',
    '1812.10821: Freidel, Kowalski-Glikman, Leigh, Minic, "Theory of metaparticles" (2018): the metaparticle\'s phase space, its constraints and its interactions.',
  ], extra: 'Q2 and Q9 above all. Is x-tilde the momentum of the same phase space or an independent coordinate; how do lambda, epsilon and hbar relate; what is a polarization in their language; do they ever treat matter in the dual polarization as a separate sector of matter? Do metaparticle interactions conserve or depend on dual momentum in a way that restricts which states interact, anything that would act like a gate in relative momentum (Q7)?' },
  { label: 'r7-vacuum', focus: 'The weakest link: whether the school treats the choice of polarization as made by the vacuum.', papers: [
    'Every school paper that bears on it, above all: 2003.00318 (its passage on vacuum selection), 2202.05104 ("Vacuum Selection" in its title), 1502.08005 ("a dynamical question"), 1405.3949, 1307.7080, 1606.01829, 2407.06207 ("corresponds to a choice of ... polarization"), 2604.19418, 2212.06086, 2111.14205, 2104.00802, 1812.10821.',
  ], extra: 'Q9 alone, as deeply as the texts allow. Search each full text for polariz, Lagrangian, vacuum selection, spontaneous, symmetry breaking, order parameter, dynamical, potential, choice of spacetime, section, and read every hit in context. Does any paper state that the vacuum, or a dynamical process, chooses which half of the doubled phase space is spacetime; does any give a potential, an order parameter, Goldstone modes or a mirror vacuum? #11 §3 says of Freidel, Leigh and Minic: "They treat the breaking as kinematical and call the choice \'a dynamical question\'. This program\'s addition is to read it as spontaneous breaking, with η as the order parameter." Test that sentence against the texts.' },
  { label: 'r8-outside', focus: 'Outside the school: independent statements of the identification, work that builds on the school\'s dark sector, and the two forms.', papers: [
    'Every paper on INSPIRE citing 2003.00318, 2010.15610, 2212.06086, 2407.06207 or 1812.10821 (tools/lit.py cites ID), screened by title and abstract, and read where it touches dark matter.',
    '2103.11235, 2304.00620 and INSPIRE recid:2704811: Maldonado and Mendez, "Bimetric universe with matter" (2021), "Dark matter in a bi-metric universe" (2023), "Axionic Dark Matter in a Bi-Metric Universe" (2023): what their second patch is, and whether its matter is a dual or momentum-side copy.',
    '2602.21407 and 2608.26413: Chouha (2026), metastrings, metaparticles and black-hole remnants: do they propose remnants or metaparticles as dark matter?',
    'doi:10.1139/cjp-2018-0097: Castro Perelman, "Is dark matter and black hole cosmology an effect of Born\'s reciprocal relativity theory?" (2018).',
    'Full-text and abstract queries on INSPIRE and arXiv: "dual standard model" with dark matter; metastring with dark matter; "dual spacetime" with dark matter; metaparticle with dark matter; "Born reciprocity" with dark matter after 2019; "momentum space" with dark matter and polarization.',
  ], extra: 'Q1, Q4, Q7, Q8 and Q11: any statement of the identification independent of the school; any that joins it to coupling by gravity alone; any dark sector with a self-interaction gated by relative velocity or momentum overlap; any magnetically charged or dyonic dark objects localized in momentum or a dual space. List every paper you screened, with a one-line verdict, under papers or leads.' },
  { label: 'r9-sweep', focus: 'A mechanical sweep of the whole corpus for passages the readers might miss.', papers: [
    'These arXiv papers: 2003.00318, 1812.10821, 1905.08269, 1905.09463, 2104.00802, 2010.15610, 2109.12763, 2111.14205, 2109.01122, 2212.06086, 2307.16712, 2203.17137, 2303.15645, 2305.12593, 2407.06207, 2604.19418, 2610.19522, 2202.05104, 2202.06890, 2011.08852, 2202.05266, 2503.20854, 2212.00901, 2303.17495, 1005.3537, 1105.2916, 1201.2365, 1308.3252, 1601.00662, 1602.00055, 1709.04388, 1801.00160, 2005.08927, 2009.12915, 2405.08744, 1307.7080, 1405.3949, 1502.08005, 1606.01829, 1706.03305, 1707.00312.',
  ], extra: 'Run tools/lit.py text ID --grep PATTERN on every paper, one family of patterns at a time, and read each hit in context. Families: (a) coupling: "only (through|via) gravit|gravitational(ly)? only|purely gravitational|gravity alone|portal|kinetic mixing|decoupl|correlat|entangl"; (b) detection: "direct detection|detector|detect(ed|ion)? (of )?dark|null result|not (been )?(seen|observed|detected)"; (c) dynamics: "self-interact|cross.section|relative velocit|velocity.depend|gate|momentum.space local|locali[sz]ed in (the )?(dual|momentum)|condensat|fuzzy|wave dark"; (d) monopoles: "monopole|dyon|magnetic charge"; (e) vacuum: "spontaneous|order parameter|vacuum selection|symmetry breaking|choice of polari[sz]ation|Goldstone"; (f) identification: "dual (standard model|SM|matter|sector|particle|field)|dark matter (is|are|as|could|would|from)". Return under papers each paper with the hits that bear on Q1 to Q11 (quote, location, reading, quote_check), and under answers, for each family, how many papers had hits and which. Do not interpret beyond the passage; flag anything surprising.' },
]

const readerPrompt = r => `You are reader ${r.label} in the dual-sector investigation of the Comatter program's record.

First read work/dual-sector/inputs/brief.md (the question, the tools, the rules and the questions Q1 to Q11) and work/dual-sector/inputs/program.md (the program's own statements, verbatim). Both bind you. Your scratch folder is work/dual-sector/scratch/${r.label}/. Run the literature tool from work/dual-sector/.

Your assignment: ${r.focus}

Your papers:
${r.papers.map(p => '- ' + p).join('\n')}

What matters most here: ${r.extra}

Read the full text wherever you can, not just the abstract: use tools/lit.py text with no --grep to see a paper's length and headings, then read the sections that bear on the questions with --grep and a wide --context, or read the whole text if it is short. For each paper return its statements that bear on Q1 to Q11, each quoted verbatim and code-checked. Then answer the questions your papers bear on, report every place where a primary source contradicts or qualifies the record's present statements about the school, and list leads and papers you could not retrieve.`

const verifyPrompt = (r, out) => `You are the verifier for reader ${r.label} in the dual-sector investigation of the Comatter program's record.

First read work/dual-sector/inputs/brief.md and work/dual-sector/inputs/program.md: the brief's tools and rules bind you too. Your scratch folder is work/dual-sector/scratch/${r.label}-verify/. Run the literature tool from work/dual-sector/.

The reader's assignment was: ${r.focus}
Its papers:
${r.papers.map(p => '- ' + p).join('\n')}

The reader's output, as JSON:
${JSON.stringify(out)}

Your job is to try to refute that output, item by item, from the primary sources. Do not take the reader's word for anything.
1. Every statement: run tools/lit.py quote on its quotation (for a source the tool cannot read, re-read it the way the reader did) and report whether it is found. Then read the passage in context (tools/lit.py text ID --grep 'a distinctive phrase' --context 1500) and judge the reader's reading: confirmed, confirmed-in-part (give the correction), or refuted (give the counter-passage).
2. Every answer: search the same papers for passages that contradict or qualify it, and judge it the same way. When an answer is imprecise, or stronger than its evidence, the verdict is confirmed-in-part with a correction.
3. Every contradicts_record item: check it against the source and against the record's own wording (root CLAUDE.md, 'Since the handoff', the 2026-11-02 entry; notes/literature-check.md §2 and §3; review/wiki-build-flags.md item 64).
4. Missed passages: passages in these papers, absent from the reader's output, that bear on Q1 to Q11, each quoted verbatim and code-checked.
5. Papers the reader could not retrieve: try once more by another route, and say what you found.`

const results = await pipeline(
  READERS,
  r => agent(readerPrompt(r), { label: r.label, phase: 'Read', schema: READER_SCHEMA }),
  (out, r) => out === null
    ? null
    : agent(verifyPrompt(r, out), { label: r.label + '-verify', phase: 'Verify', schema: VERIFY_SCHEMA })
        .then(v => ({ label: r.label, focus: r.focus, papers: r.papers, reader: out, verifier: v })),
)

const done = results.filter(Boolean)
log(`${done.length} of ${READERS.length} reader-verifier pairs returned`)
const missing = READERS.map(r => r.label).filter(l => !done.find(d => d.label === l))
if (missing.length) log('missing: ' + missing.join(', '))
return { pairs: done, missing }
