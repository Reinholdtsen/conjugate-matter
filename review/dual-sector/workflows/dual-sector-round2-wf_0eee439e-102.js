export const meta = {
  name: 'dual-sector-round2',
  description: 'Verify Winn 2025 independently and sweep conference abstracts; each followed by a refuter',
  phases: [
    { title: 'Find', detail: 'Winn verifier and conference-abstract sweep' },
    { title: 'Refute', detail: 'one refuter per finder' },
  ],
}

const CONJ = { type: 'string', enum: ['C1 identification', 'C1 chi form', 'C1 monopole form', 'C2', 'C3', 'C4 shared-photon form', 'C4 separate-photon form', 'C5', 'C6', 'C7', 'hard core', 'none'] }
const LABEL = { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision', 'not relevant'] }

const FIND_SCHEMA = {
  type: 'object',
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          source: { type: 'string', description: 'URL or identifier, authors, title, venue' },
          first_public: { type: 'string', description: 'date and how established (page date, PDF metadata, archive capture)' },
          read_how: { type: 'string' },
          quotes: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                quote: { type: 'string' },
                where: { type: 'string', description: 'page or slide number' },
                check: { type: 'string', description: 'how the quotation was found again by code in the text you extracted' },
              },
              required: ['quote', 'where', 'check'],
            },
          },
          relations: {
            type: 'array',
            items: {
              type: 'object',
              properties: { conjecture: CONJ, label: LABEL, reason: { type: 'string' } },
              required: ['conjecture', 'label', 'reason'],
            },
          },
          summary: { type: 'string' },
        },
        required: ['source', 'first_public', 'read_how', 'quotes', 'relations', 'summary'],
      },
    },
    searched: { type: 'array', items: { type: 'string' }, description: 'every venue and query run, with the number of hits screened' },
    not_reached: { type: 'array', items: { type: 'string' }, description: 'venues refused (bot checks, logins) or not tried, and why' },
    overall: { type: 'string' },
  },
  required: ['items', 'searched', 'not_reached', 'overall'],
}

const REFUTE_SCHEMA = {
  type: 'object',
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          source: { type: 'string' },
          quotes_found: { type: 'string', description: 'how many of the item\'s quotations you found again yourself, and which not' },
          date_confirmed: { type: 'boolean' },
          verdict: { type: 'string', enum: ['confirmed', 'confirmed-in-part', 'refuted'] },
          relation_corrections: { type: 'string', description: 'corrections to the relation labels, or empty' },
          note: { type: 'string' },
        },
        required: ['source', 'quotes_found', 'date_confirmed', 'verdict', 'relation_corrections', 'note'],
      },
    },
    missed: { type: 'array', items: { type: 'string' }, description: 'sources the finder missed in its own venues, each with what it says' },
    overall: { type: 'string' },
  },
  required: ['items', 'missed', 'overall'],
}

const CONTEXT = `You work on the dual-sector investigation of the Comatter program's record. Read work/dual-sector/inputs/brief.md (tools, rules) and work/dual-sector/inputs/program.md (the program's statements, verbatim from #11) first. P.R.'s conjectures, as the record numbers them: C1 dark matter is conjugate matter (the counterpart of ordinary matter in the other polarization of phase space, momentum for position), with two forms, chi particles with a self-interaction gated by relative velocity (#11 §8) and magnetically charged solitons localized in momentum (#11 §12); C2 magnetic monopoles abundant in momentum space (#11 §11.1, §12); C3 that is why none has been found (App. A item 5); C4 the magnetic mirror, each electrically charged position-polarized particle having a magnetically charged momentum-polarized analog (#11 §11.4), in two forms: the shared-photon form (the analogs carry magnetic charge of our own photon; #11 §11.4 names two ways to hide them, localization in momentum and binding into magnetically neutral composites) and the separate-photon form (the analogs are magnetic under a photon of their own); C5 conjugate collapse drives our acceleration; C6 matter clumps in momentum space; C7 a long-range attraction among dark-matter particles gated by relative velocity. Labels: anticipates (states the conjecture in substance), partial (a close variant or a central part), related (theme or mechanism), evidence-against, collision (same words, other meaning), not relevant. A source posted before September 2026 (the program's first written statement) is prior art. Do not get around bot checks, logins or paywalls; record what refused you. Keep downloads in your scratch folder work/dual-sector/scratch/LABEL/ and run Python on them with -I; extract PDF text with work/dual-sector/pdfenv/bin/python -I and pypdf, and find every quotation you return again by code in the extracted text. Write nothing outside your scratch folder.`

const FINDERS = [
  { label: 'v-winn', task: `Verify, independently and from the original files, a finding another agent made: David R. Winn (Fairfield University), "A Dual to Ordinary Matter Yielding Composite Flavored Scalar Dark Matter", Lepton-Photon 2025 (Madison), Indico https://indico.cern.ch/event/1493037/contributions/6549576 , with slides (talk 25 August 2025) and a written summary dated 10 November 2025. Download the files yourself from Indico (do not use other agents' copies), extract the text, and read the slides and the summary in full. Establish: the first public date (Indico timetable, PDF metadata, any archive capture); what the Dual is (one per Standard Model particle? electric charge swapped for magnetic? which photon couples to it? elementary or solitonic? where is it located: anywhere a momentum-space, phase-space, reciprocity or conjugate-variable placement?); how the duals become dark matter (binding into neutral composites, self-interaction, abundance); what it says about monopole searches; its own caveats (no Lagrangian?). Then search for every other public version: arXiv and INSPIRE (author Winn, D.R.), APS meeting abstracts, other Indico events, Fairfield University pages, 2015 to 2026, and read any you find. Label its relation to each of C1 (and its forms), C2, C3, C4 (both forms). Quote verbatim with page or slide numbers.` },
  { label: 's-conf', task: `Run a systematic sweep of conference abstracts and talks, a search modality no earlier agent ran, for 2015 to 2026: CERN Indico (indico.cern.ch search), Fermilab Indico, the APS Bulletin of meeting abstracts (meetings.aps.org), and the books of abstracts or contribution lists of IDM, TeVPA, ICHEP, PATRAS (axion-WIMP), DSU (Dark Side of the Universe), Planck, PASCOS, SUSY, Lepton-Photon and the Marcel Grossmann meetings where reachable. Queries to run (adapt to each search engine): dark matter as the dual, mirror, conjugate or momentum-space counterpart of ordinary matter; "dual standard model" dark matter; "momentum space" dark matter; Born reciprocity dark matter; magnetic dual of each Standard Model particle, or magnetically charged mirror matter, as dark matter; monopoles in momentum space; why magnetic monopoles are not seen; dark-matter self-interaction gated by relative velocity or by the overlap of momenta. Screen every hit by title and abstract; read the slides or proceedings of any hit that comes close to C1 to C7. Report each relevant item with its quotations, date and labels; list every venue and query you ran with hit counts, and every venue that refused you. The item already found, Winn 2025 at Lepton-Photon 2025, is being verified by another agent: list it if you meet it, but do not spend effort on it.` },
]

phase('Find')
const results = await pipeline(
  FINDERS,
  f => agent(`${CONTEXT}\n\nYour label: ${f.label}.\n\n${f.task}`, { label: f.label, phase: 'Find', schema: FIND_SCHEMA }),
  (out, f) => out === null ? null : agent(`${CONTEXT}\n\nYour label: ${f.label}-refute.\n\nTry to refute the following output of agent ${f.label}, whose task was:\n${f.task}\n\nIts output, as JSON:\n${JSON.stringify(out)}\n\nFor every item: fetch the source yourself, find each quotation again by code in text you extracted yourself, confirm or correct the date, and check every relation label against the conjecture's wording in program.md; a label stronger than its evidence is confirmed-in-part with a correction. Then search the same venues briefly for items the finder missed.`, { label: f.label + '-refute', phase: 'Refute', schema: REFUTE_SCHEMA }).then(v => ({ label: f.label, finder: out, refuter: v })),
)
return results.filter(Boolean)
