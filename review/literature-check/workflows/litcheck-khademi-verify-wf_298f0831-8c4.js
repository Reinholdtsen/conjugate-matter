export const meta = {
  name: 'litcheck-khademi-verify',
  description: 'Two independent judgments of Khademi 2009 against conjecture C3, with its abstract re-fetched and checked by code',
  phases: [{ title: 'Judge', detail: 'a strict judge and an advocate for the stronger label' }],
}
const REPO = '/home/paul/git/reinholdtsen/conjugate-matter'
const BASE = `You judge one paper for the literature check of P.R.'s conjectures in ${REPO}. Do NOT edit repository files; scratch only under work/literature-check/round5/khademi-<your label>/. Read review/literature-check/brief.md (the conjectures and the labels: anticipates = the paper states the conjecture in substance; partial = a close variant or a central part; related = the theme or mechanism, not the conjecture; evidence-against; collision = same words, other meaning). C3 is "Monopoles live in conjugate space, explaining non-detection" (#11 App. A item 5; wiki/papers/broken-born-checkpoint-v2.md §11.1 and §11.4 give its present setting, the shared-photon form: magnetic analogs in the p-polarization, unseen because they are not localized in position). P.R.'s own words (2026-10-28, review/wiki-build-flags.md item 62): "Our searches are in position space, conjugate monopoles by definition are compact in momentum space and we would not detect them. And btw, this explains their absence."

The paper: S. Khademi, "Why magnetic monopoles are not seen?", International Conference of Mathematical Sciences (Maltepe Üniversitesi, 2009), pp. 365-366; Maltepe University open-access repository, handle 20.500.12415/6128 (the repository returns HTTP 403); OpenAlex W3153563614. Its full text (a two-page PDF, 371.pdf) has not been retrieved. A searcher read its abstract from the Wayback Machine's capture of the repository item page (2021-05-10) and from OpenAIRE's harvest of the repository, and reported it as: "Dual symmetry of Maxwell's equations predicts the existence of magnetic monopoles which are not detected until now. As an important consequence of this prediction, the quantization of electric charge is obtained by P.A.M. Dirac. In this paper I show the uncertainty in the phase space quantum mechanics could be the responsible of the non-visibility of magnetic monopoles." The searcher's notes are in work/literature-check/round5/.

First fetch the abstract yourself from at least one of those two public routes (Wayback Machine availability API and capture; OpenAIRE's public search API), without registering for anything and without sending personal data, and confirm the text by code (normalize whitespace and quotes, then substring match); record the URL and the license field if present. Try once for the full text (the PDF bitstream in the Wayback Machine, or any public mirror). The same author's earlier paper, S. Khademi and S. Nasiri, J. Phys. Conf. Ser. 128, 012016 (2008), is in the record (review/literature-check/findings.json) and may show what "uncertainty in the phase space quantum mechanics" means in his work; read what is public of it.`
const SCHEMA = { type: 'object', properties: {
  abstract_confirmed: { type: 'boolean' }, abstract_text: { type: 'string' }, routes: { type: 'string' }, license: { type: 'string' },
  full_text: { type: 'string' },
  relation: { type: 'string', enum: ['anticipates', 'partial', 'related', 'evidence-against', 'collision'] },
  confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
  reason: { type: 'string' }, what_is_new_in_C3: { type: 'string' } },
  required: ['abstract_confirmed', 'abstract_text', 'routes', 'license', 'full_text', 'relation', 'confidence', 'reason', 'what_is_new_in_C3'] }
phase('Judge')
const out = await parallel([
  () => agent(`${BASE}\n\nYour lens: strict. Apply the labels as the brief defines them, to what the abstract actually says. Say what a reading of the full text could change.`, { label: 'judge:strict', phase: 'Judge', schema: SCHEMA }),
  () => agent(`${BASE}\n\nYour lens: advocate for the stronger label. First make the strongest honest case that this paper anticipates or partly anticipates C3 (in substance, not in words), then judge it fairly yourself. Say what a reading of the full text could change.`, { label: 'judge:advocate', phase: 'Judge', schema: SCHEMA }),
])
return { judges: out.filter(Boolean) }
