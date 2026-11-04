# Pre-registration: the literature check of P.R.'s conjectures

Written 2026-11-02 by the main session, before any search agent was launched. Not to be named in any agent prompt.

Disclosure: written after scouting. Testing the search tools surfaced three papers whose abstracts I read:
Bolognesi 2015 (arXiv:1506.02187, a Born-reciprocal "trans-Planckian theory" with a matter field "to be identified
with dark matter" that explains the present acceleration), Castro Perelman 2019 (Can. J. Phys., "Is dark matter and
black hole cosmology an effect of Born's reciprocal relativity theory?", title only) and Bérard–Mohrbach 2004
(hep-th/0310167, a Berry-phase monopole in momentum space). The priors below were formed partly before and partly
after seeing them.

Verdict categories, per conjecture: **anticipated** (a paper states the conjecture in substance), **partly
anticipated** (a close variant or a central part is published), **related only** (the theme or mechanism is
published, the conjecture is not found), **nothing relevant**.

| | Conjecture | Predicted verdict | P(anticipated) | P(at least partly) |
|---|---|---|---|---|
| C1 | dark matter is conjugate (momentum-polarized) matter | partly anticipated (Born-reciprocity lineage: Bolognesi, Castro, FLM/metastring) | 0.35 | 0.70 |
| C2 | magnetic monopoles abundant in momentum space, as dark matter | related only; phrase collisions certain (Berry monopoles, R-flux) | 0.07 | 0.20 |
| C3 | they are unseen because searches are made in position space | related only or nothing | 0.05 | 0.12 |
| C4 | magnetic mirror: each charged x-particle has a magnetic p-analog | related only (Montonen–Olive, U-duality, Berry x↔k / B↔Ω) | 0.07 | 0.25 |
| C5 | conjugate collapse drives our accelerating expansion | partly anticipated (Bolognesi; dual-spacetime dark energy; scale-factor duality w ↔ −w; twin-universe models) | 0.25 | 0.55 |
| C6 | matter clumps in momentum space (the founding image) | related only (BEC as momentum-space condensation; gravitational BEC of axion dark matter) | 0.10 | 0.35 |
| C7 | long-range attraction among χ gated by relative velocity | related only (velocity-dependent self-interaction, short range) | 0.05 | 0.25 |

Expected overall: at least one conjecture (C1 or C5) at least partly anticipated, P = 0.85. The monopole conjectures
(C2, C3) meet phrase collisions but no proposal of momentum-space monopoles as dark matter or as the reason for the
null result, P = 0.80.

Weakest link of the check: recall. The Born-reciprocity literature is spread over non-arXiv journals (Castro
Perelman alone has a large output) and conference proceedings; a "not found" rests on the searches recorded, and a
scoop in a venue no tool indexes would be missed. Second: label inflation or deflation by searchers, which the
verifiers are told to test.

Scoring rule, fixed now: a conjecture's verdict is the strongest relation that survives verification (anticipated >
partly > related > nothing). A prediction counts as right if the verified verdict equals the predicted one.

## Scoring (2026-11-02, after verification and the verdict panel)

Verified verdicts, by the rule fixed above (`work/literature-check/results.json`, kept in the record as
`findings.json`; panel in `panel/*.out.json`):

| | Predicted | Verified | |
|---|---|---|---|
| C1 | partly anticipated | **anticipated** (Minic school, 2019/2020 on) | miss |
| C2 | related only | related only | hit |
| C3 | related only or nothing | related only | hit |
| C4 | related only | **partly anticipated** (magnetic dark sectors, no momentum placement) | miss |
| C5 | partly anticipated | partly anticipated | hit |
| C6 | related only | **partly anticipated** (Bose condensation of dark matter) | miss |
| C7 | related only | related only | hit |

4 of 7 right. All three misses underestimate the prior art: the literature held more than predicted. The two overall
predictions held: C1 or C5 at least partly anticipated (P = 0.85), true; C2 and C3 met collisions but no momentum-space
monopole proposal (P = 0.80), true. The weakest link named, recall in venues the tools could not reach, is where the
residual risk sits: OpenAlex's free quota ran out in round 3, one closed-repository item (Khademi 2009, "Why magnetic
monopoles are not seen") is unread, and non-English literature was not searched.
