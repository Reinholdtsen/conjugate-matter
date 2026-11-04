# Are P.R.'s conjectures already published? A literature check

*Working note, 2026-11-03. Status: searched and verified; not through a blind review round (agents reviewed the
write-up, §11). The check ran on 2026-11-02, with 31 agents in four workflows: searchers looked through the physics
literature for seven of Paul's conjectures, a second agent checked all but four of the findings that carry a verdict,
and a panel of seven judges reread the evidence for each verdict, those four included. Every quotation from the
literature in this note was found again in its source by code, and `verify/literature_check.py` checks the note's
quotations, citations, verdicts and main counts against the stored record, and the algebra behind flag 66, on every
run of the gate. The record (briefs, queries, findings, verdicts, the panel, the pre-registration and the
tools) is in `review/literature-check/`. Finding prior art changes no claim's status: each conjecture keeps its
status, the one #11 gives C1–C6 and, for C7, that of P.R.'s conjecture outside the record (§9). Six suspected
omissions in #11 are proposed to Paul as flags 64–69 in `review/wiki-build-flags.md`; #11 is unchanged until he
rules.
Conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic).*

## 1. The question, the conjectures, the method

*In plain terms: Paul asked whether his conjectures are already in the published literature. Agents searched in
three rounds, a second agent checked all but four of the findings that place a paper close to a conjecture or
against it, a panel reread those four, and code found every quotation in this note again in its source. A conjecture
counts as anticipated only where a paper states it in substance. Prior art says who said something first. It does
not make a conjecture more or less likely to be true.*

**The request.** Paul, 2026-11-02: "Do a literature check of my conjectures".

**The conjectures, as the record states them.**
- C1, dark matter is conjugate matter: founding supposition 4, "P.R.'s core conjecture" (#11 App. A item 4).
- C2, magnetic monopoles abundant in momentum space: "P.R. conjectures that they are abundant in momentum space"
  (#11 §11.1), the third dark-matter candidate of #11 §12.
- C3, that is why none has been found: "Monopoles live in conjugate space, explaining non-detection" (#11 App. A
  item 5).
- C4, the magnetic mirror: "momentum matter is similar to position matter, each electrically charged x-polarized
  particle having a magnetically charged p-polarized analog" (#11 §11.4).
- C5, conjugate collapse drives our accelerating expansion: "Their collapse is our acceleration" (#11 App. A item
  9), with the route #11 §10 keeps, dual stiff ↦ Λ.
- C6, matter clumps in momentum space, the founding image: "Matter clumps in momentum space" (#11 App. A item 3).
- C7, a long-range attraction among χ gated by relative velocity: "Dark-matter particles attract each other at long
  range, like gravity, but only when they move at similar velocities" (`notes/velocity-gated-gravity.md` §5).

**How the literature was searched** [S].
- Round 1: five searchers, one per theme (conjugate matter; monopoles; the magnetic mirror; collapse and
  acceleration; momentum clumping), searching INSPIRE, arXiv, Crossref and the web. Each was followed by a verifier
  who reread every finding at its source and searched again. Ten agents.
- Round 2: a citation screen. Every INSPIRE record citing one of ten anchors of the Born-reciprocity literature
  (Born 1938 and 1949; six papers of Freidel, Leigh, Minic and coauthors on Born geometry and the metastring; Low's
  reciprocal relativity; Bolognesi's trans-Planckian cosmology) was screened by title, abstract and full text
  against each conjecture: 498 distinct records. Four readers read the 143 flagged records that no searcher had
  assessed, and verifiers checked the strong matches. Seven agents.
- Round 3: coverage sweeps outside INSPIRE (OpenAlex, Crossref, DataCite, Zenodo, HAL and the web), three by
  conjecture and one of older lineages, with verifiers of the strong matches. Seven agents.
- Round 4: a verdict panel of seven judges, each given the evidence for its conjectures: three for C1 (one asked to
  argue for novelty, one judging scope, one judging content), one each for C4, C5 and C6, and one for C2, C3 and C7.

**How a verdict was reached.**
- Each finding relates one paper to one conjecture: *anticipates* (the paper states the conjecture in substance),
  *partial* (a close variant or a central part), *related* (the theme or mechanism, not the conjecture),
  *evidence-against* (a result or datum that weighs against it) or *collision* (the same words with another
  meaning).
- A verifier's label replaces the finder's; where verifiers disagreed the weaker label was kept; a restatement is
  labeled no closer than the paper it restates, which lowered two findings for C5 from a verifier's partial to
  related (Addazi et al. 2022 and Hübsch and Minic, October 2026, which restate Berglund, Hübsch and Minić 2019);
  the panel's changes apply last (`review/literature-check/tools/consolidate.py`). The result is 287 findings
  (`review/literature-check/findings.json`). Khademi 2009, labeled by two judges in round 5 from its abstract
  (§4, §11), is not among them.
- A conjecture's verdict is the strongest relation that survives: anticipated, partly anticipated, related only or
  nothing relevant. The rule was fixed in the pre-registration before any search agent was launched.
- Every quotation in a finding that carries a verdict (one labeled anticipates, partial or evidence-against) was
  found again in the source's abstract or full text by code (`review/literature-check/recheck.out`), except six
  from two sources the code could not read, which agents read through a web fetch (Henry-Couannier 2018, four;
  Goldhaber 2017, two; §10). Every identifier was looked up and, where it resolved, its title, first author and
  year compared with the citation; eight of the 287 did not resolve, none of them in a finding that carries a
  verdict. In all the code check flagged 23 of the 287 findings, for an unresolved identifier, a quotation not
  found or a citation year missing or different from the record's. The references below are built from INSPIRE,
  Crossref or arXiv metadata, and Khademi 2009's from its OpenAlex record and archived repository page
  (`review/literature-check/sources.json`), not from the agents' strings: one agent had named two wrong coauthors,
  which `findings.json` keeps.

## 2. The verdicts

*In plain terms: one conjecture is published in its core, three have close published relatives, and three were not
found. What the check did not find in the literature is mostly the program's setting joined to the identification:
a vacuum that selects a polarization, and a dark sector coupled to ours by gravity alone, as the program's is in
every form but one (monopoles carrying magnetic charge of our own photon). Copies of ordinary matter coupled to ours
mainly or only by gravity (mirror and twin matter) and a preferred polarization that breaks Born duality are each
published; their combination with the identification was not found. Objects localized in momentum were not found.*

| | Conjecture | Verdict | Closest published work | Not found |
|---|---|---|---|---|
| C1 | dark matter is conjugate matter | anticipated | Minic 2020; Berglund, Hübsch and Minić 2021; their school to 2026 | the identification joined to a gravity-only, never-detected sector (mirror and twin matter couple by gravity without reciprocity); the χ form with a velocity gate; the monopole form |
| C2 | monopoles abundant in momentum space | related only | Szabo 2019 (magnetic charge mapped to momentum space as a background); Berry-curvature monopoles; monopole dark matter in position space | magnetically charged solitons localized in momentum, as matter |
| C3 | that is why none has been found | related only | Khademi 2009, read in its abstract only (phase-space uncertainty; its full text could raise the verdict); other hiding places: a second time dimension, neutral cores, superpositions of +g and −g, a dark sector, screening by a magnetic condensate | hiding by localization in momentum |
| C4 | the magnetic mirror | partly anticipated | Govaerts 2023; Vento 2025; García-Moreno and Vento 2026 (magnetic dark sectors); Gibbons and Herdeiro 2001 (the bridge, as a remark) | the analogs in the momentum polarization, one per charged particle |
| C5 | conjugate collapse drives our acceleration | partly anticipated | Henry-Couannier 2013, 2018 (the equations from 2010); Gasperini and Veneziano 1993, 2003; Mukherjee, Jassal and Lochan 2024 | the partner as the momentum description of our own universe |
| C6 | matter clumps in momentum space | partly anticipated | Bose condensation of dark matter: Riotto and Tkachev 2000; Sikivie and Yang 2009; Levkov, Panin and Tkachev 2018 | velocity flocks formed by an attraction between similar velocities |
| C7 | long-range velocity-gated attraction | related only | Delbourgo and Lashmar 2008 | a 1/r attraction among dark matter only, gated in relative velocity at a fixed width |

**The findings behind the verdicts** (`review/literature-check/findings.json`; anticipates, partial, related,
evidence-against, collision):

| | Findings | anticipates | partial | related | against | collision |
|---|---|---|---|---|---|---|
| C1 | 53 | 9 | 4 | 31 | 2 | 7 |
| C2 | 34 | 0 | 0 | 23 | 3 | 8 |
| C3 | 30 | 0 | 0 | 26 | 1 | 3 |
| C4 | 59 | 0 | 3 | 48 | 1 | 7 |
| C5 | 75 | 0 | 6 | 61 | 1 | 7 |
| C6 | 25 | 0 | 4 | 18 | 1 | 2 |
| C7 | 11 | 0 | 0 | 9 | 1 | 1 |

Each verdict rests on at least one finding that a second agent confirmed. Four findings that carry a verdict had no
verifier and were labeled by their finder alone (Minic 2023 for C1, Goldhaber 2017 for C3, Gasperini and Veneziano
1993 for C5, Riotto and Tkachev 2000 for C6); a panel judge reread each and kept its label, and no verdict depends
on them. The panel changed no verdict. It proposed six label changes, and five were applied; the sixth, the content
judge's anticipates for Berglund, Freidel et al. 2022, was not: the paper keeps its verifier's partial, which the
other two judges for C1 also gave it, and is treated like Berglund et al. 2022 (§3). The panel's judges rated their
confidence high for C1 (two of three judges; the third, medium), C2, C4, C5 and C7, and medium for C3 and C6.

Four verdicts rest on a reading of the conjecture that the judges state. C1: counting strict P4 and ordinary momentum
at ħ as part of its substance (the content judge's reason for medium confidence), or reading the brief's gloss of C1,
*organized around momentum*, as a clause about dynamics, dark matter that interacts or is localized in momentum (a
dissent the judge asked to argue for novelty kept on record), makes the published claim a close variant (the content
judge) or only a central part (the dissent), and the verdict partly anticipated. C4: the verdict counts the magnetic
dark sectors of §5 as close variants of the separate-photon form; if the placement in momentum alone is the
conjecture, it is related only, the closest work then being a 2021 conference paper of Berglund, Hübsch and Minic in
which the Born-geometry pairing makes the heterotic string's two E8 factors each other's Langlands, electric–magnetic,
duals, both with visible fields and each with a dark dual in the same algebra, for gauge groups only (`findings.json`,
C4; §5). C5: the verdict counts the partner's identity, the momentum description of our own universe, as part of the
conjecture. If that identity is counted as framework, Dark Gravity (§6), which, in the words of the panel judge for
C5, states the founding sentence's configuration and causal arrow in conjugate vocabulary, could be called an
anticipation of "Their collapse is our acceleration", though never of the kept route. The judge states this reading
and does not adopt it: Dark Gravity differs in physical claim (a time-reversed twin whose matter acts on us as
negative mass, a postulated exchange of regimes, a power law, dust as the driver). The round-1 verifier for C5 finds
that Dark Gravity, read kinematically, holds the founding sentence in a different framework, and that an anticipation
could be argued only for the sentence read as a kinematic identity, not for the kept route: Henry-Couannier describes
the driver as the dominance of the conjugate side's matter, not as collapse, and in the verifier's script that side's
source term weakens as the side contracts, so the contraction does not power the acceleration
(`review/literature-check/checks/dg_exponents.py`, step 4). C6: the verdict counts Bose condensation of dark matter,
the record's condensed form, as a form of C6; restricted to the founding image of several velocity flocks, it is
related only.
The other readings of C1, C4 and C6 would lower their verdicts; that of C5 would raise its verdict.

## 3. Dark matter is conjugate matter (C1): the identification is published

*In plain terms: a group around Djordje Minic has proposed since 2020 that dark matter is the dual of the Standard
Model in a Born-reciprocal formulation of string theory, where the dual coordinates are the momentum-like half of a
doubled phase space. That is P.R.'s identification. Their dark sector differs from the program's: it is correlated
with ours by construction, where the program's couples to ours by gravity alone and is never detected directly, in
every form but one, monopoles carrying magnetic charge of our own photon. Coupling by gravity alone is itself
published, for mirror and twin matter; joined to the identification it was not found. Separately, two fits of halo
data mildly prefer dark matter that scatters off itself in galaxy clusters, where the program's particle form
predicts no such scattering.*

**What is published** [S].
- Minic 2020 (arXiv, 29 February 2020), abstract: "metaparticle quanta (the zero modes of the metastring) as the
  natural quanta of dark matter in this approach".
- Berglund, Hübsch and Minić 2021 (LHEP; arXiv, October 2020), abstract: "dark energy is generated by the dynamical
  geometry of the dual spacetime while dark matter, on the other hand, comes from the degrees of freedom dual to the
  visible matter".
- The same school restates it through 2026: "Thus the entire SM would have a dual SM (which we propose, describes
  the dark matter sector)." (Edmonds, Minic and Takeuchi 2021, §4); "the dual matter degrees of freedom naturally
  appear as dark matter degrees of freedom" (Berglund, Hübsch and Minic 2023, Int. J. Mod. Phys. D, §6.5); "We will argue that dual
  particles, correlated to visible particles, represent dark matter." (Hübsch and Minic 2024, §3); "it is a
  candidate for the invisible matter sector (dual to the observed, visible, Standard Model sector)" (Hübsch and
  Minic, October 2026, §3.2). Nine papers state it in substance (the anticipates of §2's table). The last, posted on 14 October 2026, is later than
  P.R.'s first written statement of the conjecture (the lab notebook, v0.1, September 2026), so it is a restatement
  and not prior art; the eight before it are prior. All nine come from one group and carry one priority, Minic 2020,
  dated no later than its posting; two earlier items were not read, the September 2019 talk behind it, whose content
  is unknown, and a 2019 paper of Freidel, Leigh and Minic not on arXiv, whose abstract mentions metaparticles but not
  dark matter. No statement independent of the group was found; Finkelstein 2008 (arXiv 2006) only speculates, in one
  sentence, that the momentum-energy coordinates of quantum events may contribute to dark matter (related, one
  agent's label).
- Two multi-author papers of 2022 state it in a weaker form: "each observed quantum field has a 'dual', which could be associated
  with dark matter degrees of freedom" (Berglund, Freidel, Hübsch, Kowalski-Glikman, Leigh, Mattingly and Minic
  2022); and a Snowmass paper (Berglund et al. 2022), "Essentially, in this approach, dark matter should be viewed
  as a dual SM, where 'dual' refers to the dual spacetime that is found in such a general formulation of string
  theory." Both are labeled partial, because neither says on its own pages that the dual is the momentum side. The
  label of Berglund et al. 2022 is the panel's: the judge asked to argue for novelty lowered it from anticipates.
  That of Berglund, Freidel et al. 2022 is its verifier's, which two judges shared; the content judge proposed
  anticipates. A review with 162 authors (Addazi et al. 2022) and Jejjala, Kavic, Minic and Takeuchi 2022 are
  partial too.

**What their "dual" is** [S].
- In the foundations it is the momentum side. Freidel, Leigh and Minic 2014 (Phys. Lett. B): "so we will refer to Y
  as coordinates in momentum space", and "T-duality is cast essentially as a Fourier transform". Berglund, Hübsch
  and Minić 2021 speak of the "canonically conjugate dual space". Hübsch and Minic 2024, §3: "Classical spacetime
  label x of canonical QFT corresponds to a choice of (classical spacetime) polarization in modular (quantum)
  spacetime".
- In the model their dark-matter statements rest on, the metaparticle, the dual coordinate x̃ is a coordinate of a
  doubled phase space at the string scale, with [x, x̃] = iλ², beside an ordinary momentum p with [x, p] = iħ =
  [x̃, p̃] (Hübsch and Minic 2024, §3). The identification matches C1 in their foundations; their model doubles phase
  space where the program polarizes one.
- The judge asked to argue for novelty found the duality the same, not a shared word: the school's dual coordinates
  are the canonical conjugate of x. The content judge drew the distinction above between the foundations and the
  metaparticle, and rated its confidence medium because, if strict P4 and ordinary momentum at ħ belong to C1's
  substance, the published claim is a close variant (§2).

**What differs** (not found joined to the identification).
- The coupling. Their dual sector is correlated with ours by construction: "the dark matter sector can be seen as
  coming from a dual Standard Model with a dynamics that is entangled/correlated with the visible Standard Model"
  (Berglund, Hübsch and Minic 2023, Symmetry); "Dark matter, dark energy and visible matter are naturally correlated
  in this description" (Berglund, Freidel et al. 2022). All three judges for C1 read this as predicting couplings
  between dark and visible matter beyond gravity: Minic 2020 expects dark quanta to be detectable through a
  Berry-phase-like entanglement with visible matter, and Berglund, Hübsch and Minić 2021 a dual photon correlated
  with ours, correlated events at accelerators and a dark–visible correlation at the Hubble scale, which they tie to
  modified dark matter. The round-1 verifier for C1 found the gap narrower: the 2021 paper calls that correlation
  invisible in effective field theory, vanishing as λ → 0 or L → ∞, and the school, like the program, expects no
  standard direct-detection signal. The scope judge answers that the school still expects a detection, through the
  entanglement, and states no permanent null. Whether observation can tell the two sectors apart is open (root
  `CLAUDE.md`). In the program, P4 is strict and #11 §13 row 7 requires a
  "Permanent null" in direct detection. C1's monopole form need not meet this: in the shared-photon form of #11 §11.4, the setting of C3, conjugate monopoles would carry magnetic charge of our photon, with P4 restated, and row 7 names only two candidates (flag 63; the judge asked to argue for novelty). Coupling by gravity alone is published without reciprocity: copies of
  ordinary matter coupled to ours mainly or only by gravity, as mirror matter and as twin matter on a second metric
  (C1's related findings in `findings.json`), and for dark matter coupled by gravity alone a permanent null is
  generic (the scope judge). What was not found is that coupling joined to the identification.
- The vacuum. #11's polarization is selected spontaneously (P5). #11 §3 credits the preferred polarization that
  breaks Born duality to Freidel, Leigh and Minic ([26S]) and counts as its own addition only the spontaneous
  reading, with η as the order parameter. The check found no such mechanism in the school's papers, where the
  classical spacetime label "corresponds to a choice" of polarization.
- The two forms of #11 §12: χ particles with a velocity-gated self-force, and conjugate monopoles localized in
  momentum (C2).

**Already in the record.** The phase-space-diameter note cites Berglund, Hübsch and Minic 2023 [S] for the
cosmological constant as a reciprocity image (`papers/phase-space-diameter.md` §7). The same paper's §6.5 states
the identification. The record cited the paper for another result and did not note this one.

**Two data papers on the χ form** [S]. They bear on #11 §13 row 1, "zero cluster signal (particle χ)", not on the
identification. Kaplinghat, Tulin and Yu 2016, fitting halos from dwarfs to clusters: "Our results prefer a mildly
velocity-dependent cross section", from about 2 cm²/g on galaxy scales to about 0.1 cm²/g on cluster scales
(abstract). Sagunski et al. 2021: "For both groups and clusters, our results show a mild preference for a nonzero
cross section compared with cold collisionless dark matter.", with 0.19 ± 0.09 cm²/g in clusters and an upper limit
of 0.35 cm²/g at 95% confidence (abstract). Kaplinghat, Tulin and Yu prefer a cross-section that falls with velocity, as the knee does, and Sagunski et al. find their data consistent with one (0.5 ± 0.2 cm²/g in groups);
both prefer a nonzero value at cluster speeds, where row 1 gives particle χ none. #11 §8 leaves the gate's tail open,
Gaussian or rational; a rational tail would soften the conflict (the judge asked to argue for novelty), and whether
it could match the fits was not assessed. A mild preference is not the "Robust self-interaction at v ≫ v*" that
row 1 names as its kill condition (flag 69). The pattern itself, strong scattering in dwarfs and weak in clusters,
also has an ordinary published mechanism besides the Yukawa power law that row 1 lists as the standard expectation:
resonant self-interaction (Chu, Garcia-Cely and Murayama 2019; labeled related by one agent, the round-1 verifier for
C1). The knee alone therefore does not single out the gate; its origin and tail shape are what was not found
(that verifier).

## 4. Monopoles in momentum space (C2) and the null result (C3): not found

*In plain terms: the papers found have monopoles as dark matter, but always located in ordinary space, and they
have monopoles in momentum space, but only as a geometric property of electrons in crystals or of a string
background, not as particles. No paper the check read proposes magnetically charged objects localized in momentum,
or that this is why searches find none. The nearest, a two-page conference contribution of 2009 read only in its
abstract, attributes the non-visibility of monopoles to uncertainty in phase-space quantum mechanics without saying
where they are.*

**Closest published work for C2** [S].
- Szabo 2019 maps magnetic charge to momentum space with Born reciprocity: "We apply Born reciprocity to map this
  system to the phase space of closed strings propagating in R-flux backgrounds of string theory". The magnetic
  charge becomes a background flux on momentum space, not a particle (also Lüst, Malek and Szabo 2017).
- Bérard and Mohrbach 2004: "We find consequently that this field must be obligatorily a dual Dirac monopole in
  momentum space." This is a Berry-curvature monopole, the geometry #11 §11.1 already names as the laboratory shadow:
  "right geometry, different flux". Related, not the conjecture: the panel judge for C2 calls it the closest single
  object found, a field of the vacuum with its singularity at p = 0 that acts on probes, not magnetically charged
  matter.
- Harvey and Jensen 2005 localize a Kaluza–Klein monopole in winding space, the T-dual of a compact dimension, which
  is not the momentum polarization.
- Monopoles as dark matter are published in position space with ordinary kinematics, from Murayama and Shu 2010
  (hidden-sector 't Hooft–Polyakov monopoles, #11's [28][S]) to Brümmer, Ferrante, Fischer and Frigerio 2026, who
  find for the minimal model: "dark monopoles cannot constitute a sizeable fraction of dark matter" (Phys. Rev. D
  2026; flag 68). In "The price for monopole dark matter" (arXiv:2607.29492) the same authors construct a model
  beyond the minimal content in which monopoles of about 10⁸ GeV or more are the dark matter, in a specific window of
  parameters, with a light stable dark fermion.

**Bounds on the shared-photon form, if its analogs are localized in position** [S]. #11 §11.4 already records that
such objects would exceed the Parker bound at #14's benchmark masses. The literature bounds monopoles of Dirac charge
as the dark matter by mass. Adams et al. 1993 extend the Parker bound to rule out monopoles much lighter than
10¹⁷ GeV as the closure density (abstract). Zhang et al. 2024 bound the flux for masses from 10¹³ to 10¹⁶ GeV and
add: "For larger monopole masses the scenarios in which magnetic monopoles account for all or the majority of dark
matter are disfavored." Kobayashi and Perri 2023 find that monopoles of Dirac charge must be heavier than 10¹⁸ GeV
to cluster with our Galaxy, and for those the Parker bounds are weaker than the dark-matter density: "Such monopoles
can thus make up the entire dark matter." Above 10¹⁸ GeV the two papers disagree: Kobayashi and Perri allow
monopoles that cluster with our Galaxy to be all of the dark matter, while Zhang et al., from the Andromeda Parker
bound, disfavour heavy monopoles as all or most of it. The case against monopoles of Dirac charge localized in
position as the dark matter is agreed below about 10¹⁸ GeV and contested above it (the panel judge for C2, C3 and
C7). None of these bounds applies to objects localized in momentum, for which no model was found, and they need
modification where the magnetic field is screened (Carneiro 2026; §5).

**Closest published work for C3** [S].
- Other accounts of why magnetic charge goes unseen: a second time dimension acting at the Planck length (Elsborg and
  Köhn 2022); elementary particles whose structure "consists of a magnetically neutral core of matter containing a
  distribution of magnetic charge density in stratified layers" (Kursunoglu 1974); magnetic charges occurring only in
  superpositions of +g and −g with vanishing mean charge, which "cannot be split in electromagnetic interactions by
  energy measurements" (Barut 1972); a dark magnetic sector, with Govaerts 2023 asking "how to possibly access
  experimentally its 'dark' dual magnetic sector through the use of the purely electric sector which makes up our
  visible world"; and screening, in a vacuum where only a magnetic Higgs field condenses, so that magnetic charge of
  our photon has no long-range field (Carneiro 2026, a preprint; §5).
- Against spreading a monopole's charge: Goldhaber 2017 (a letter in Physics Today) argues that in quantum
  electrodynamics and the Standard Model a monopole's charge cannot be spread out, since fractions of it would violate
  the quantization condition, and that by field energy a monopole's radius should be at least an order of magnitude
  above its Compton wavelength, so its charge must in fact be spread, which those theories cannot do; finding a
  monopole would then imply new objects at
  lower energy scales. The letter was read through a web fetch by the agent that found it and again by the panel
  judge for C3, who confirmed both quotations; code could not check it. It bears on hiding by spreading in position:
  the judge keeps it as weak evidence against, which raises the cost of that option without refuting it and does not
  touch binding into neutral composites. How it bears on localization in momentum is not computed.
- The closest account found is read only in its abstract: Khademi 2009, "Why magnetic monopoles are not seen?", a
  two-page contribution to the International Conference of Mathematical Sciences (Maltepe University), whose
  repository refuses access from here. Its abstract (CC0), read from the Wayback Machine's capture of the repository
  page and from OpenAIRE's harvest of the repository, and found by code in both: "In this paper I show the
  uncertainty in the phase space quantum mechanics could be the responsible of the non-visibility of magnetic
  monopoles." It asks C3's question and answers it from the position–momentum structure of quantum mechanics, C3's
  own kind of mechanism; none of the other 30 findings for C3 does. It does not say where the monopoles are or what
  is uncertain, and in Khademi's other papers "phase space quantum mechanics" is the Wigner and Kirkwood formulation
  of ordinary quantum mechanics, not a sector of matter. Two judges (round 5, §11), one asked to argue for the
  stronger label, labeled it related with medium confidence: its full text, not retrieved, could raise it to partial,
  or to anticipates if it places the monopoles in momentum and blames searches in position for missing them. C3's
  verdict is provisional until it is read. Khademi and Nasiri 2008 (a related finding for C4), read in full by both judges, obtain electric-charge
  quantization from a gauge symmetry in phase space, without monopoles.

## 5. The magnetic mirror (C4): partly anticipated

*In plain terms: a dark world of magnetically charged matter, mirroring our electrically charged one, is published,
but in every paper found as a separate sector in ordinary space. The idea that electric–magnetic duality is a case
of Born's reciprocity, as a rotation in the phase space of the electromagnetic field, is published as a remark.
Putting the magnetic analogs in the momentum polarization, one for each charged particle of ours, was not found. If
that placement alone is the conjecture, the verdict is related only (§2).*

**Magnetic dark sectors** [S].
- Govaerts 2023 asks whether dual electrodynamics gives "a dark parallel world of purely magnetically charged
  matter".
- Vento 2025: "we generalize QED to a two photon theory where the extraordinary photon and the monopole belong to
  the dark sector, and the ordinary photon and the electron to the non-dark sector". García-Moreno and Vento 2026:
  "The new photon and the monopoles form the dark matter sector." Posted on 1 October 2026, at about the time of
  the program's statement, it restates Vento 2025's dark QED and adds nothing for C4 beyond it (the panel judge for
  C4).
- Vento's dark sector, extended by García-Moreno and Vento, is magnetically charged matter with a photon of its own,
  the separate-photon form of #11 §11.4 without its placement in momentum. Govaerts's is the magnetic half of one
  dual electrodynamics, written with two gauge potentials: the shared-photon form in its wording. Under the
  force law he derives from his action, though, electric charges feel only the fields of electric charges and magnetic
  charges only those of magnetic charges, unless one new coupling opens a portal between the two, so the panel
  judge for C4 finds it closer in physics to the separate-photon form. None places the magnetic matter in momentum,
  and none pairs each charged particle of ours with an analog.
- Scott et al. 2018: with only one kind of charged field, a duality rotation removes either the electric or the
  magnetic charge. Analogs that are the only charges of the p-sector's own photon can then be described as electric
  just as well, so unless that sector also holds electric charges, the separate-photon form's content lies in its
  coupling, the S-image of ours, which F2's finding leaves open (#11 §11.4; the round-1 verifier for C4; the panel
  judge for C4, as its own inference).

**Hiding the shared-photon form's analogs** [S]. #11 §11.4 names two ways to hide them, p-localization and binding
into magnetically neutral composites. Carneiro 2026, a preprint, hides magnetic charge of our photon a third way, by
screening, in a vacuum where only a magnetic Higgs field condenses and electric charge stays long-ranged: the nearest
published case of a vacuum selecting the electric frame, though not a polarization of phase space (the round-1
verifiers for C3 and C4; the panel judge for C4). Evslin and Gudnason 2012, a preprint, make the halo of each of the
lightest dwarf spheroidal galaxies a single monopole of a hidden SU(2), a field profile spread over the halo as §11.4's
hiding condition asks, though of a hidden gauge field, not our photon (the round-1 verifier for C2 and C3; the panel
judge for C2, C3 and C7).

**The full magnetic family** [S]. It is established, as #11 §11.2 says: Montonen and Olive 1977, monopoles that
form a gauge multiplet "with magnetic replacing electric charge"; and Vachaspati 1996: "We construct a model in
which stable magnetic monopoles have magnetic charges that are identical to the electric charges on leptons and
quarks".

**The bridge between the two dualities** [S]. Gibbons and Herdeiro 2001: "electric-magnetic duality is a special
case of Born-Reciprocity", "a transformation which acts as a rotation in phase space". The phase space they name is
the electromagnetic field's, with B and D = ∂L/∂E as the conjugate pair, not the position and momentum of matter.
The remark supports §11.3's observation that the two dualities share one rotation; it does not show that ρ, acting
on position and momentum, exchanges electric and magnetic charge, which §11.1's first ground denies. Russo and
Townsend 2025 remark
that in the quantum theory the duality group of self-dual nonlinear electrodynamics is broken to a Z₂, which "is an
example of Born-reciprocity". Born himself sought the number 137, the inverse
fine-structure constant, from reciprocity (Born 1940). Further published work reaches parts of the bridge:
- Berglund, Hübsch and Minic, in a 2021 conference paper (arXiv:2111.14205), read the heterotic string's second E8,
  built on the dual internal coordinates, as the Langlands dual of the first, which they gloss as its
  electric–magnetic dual. Both E8 factors have visible gauge fields, and each has a dark dual, a field on the dual
  spacetime coordinates x̃ valued in the same algebra; a correlation term pairs the visible fields of each factor with
  the dark fields of the other. Their dark sector is therefore not the electric–magnetic dual of ours (the round-1
  verifier for C4). The claim concerns gauge groups only, with no charged matter, magnetic charges or couplings, and
  E8 is its own Langlands dual, so the two are "physically indistinguishable". The panel judge for C4 reads the paper
  as the closest published form of #14 v2's identification of the momentum-polarized sector as "the S-dual image of
  the electric sector" (#11 §11.4); the round-1 verifier for C4 reads it as prior art for §11.3's identification,
  not for §11.4's mirror. Their 2023 review, which the record cites for another result (§3), repeats the passage.
- Freidel, Leigh and Minic 2014 (Phys. Lett. B), the first paper of #11's [3]†: once vertex operators carry both
  momentum and dual momentum, the worldsheet's electrostatic picture becomes one of electric and magnetic charges,
  dyons, and the Dirac–Schwinger–Zwanziger quantization of their charges is the diffeomorphism constraint.
- S-duality as a canonical transformation of a gauge theory's phase space (Lozano 1995), as the momentum–winding
  T-duality (Harvey, Moore and Strominger 1995; Kapustin and Witten 2007), and, perturbatively, as a Fourier
  transform (Galakhov, Mironov and Morozov 2014).

The panel judge for C4 reads these works as reaching parts of the unification #11 §15 counts among the program's
products, and as bearing on round 2's objection that a shared matrix is not a shared physics (#11 §11.4). #11 §11.3
draws the bridge as its own observation, "the third appearance of one matrix in this program" (flag 67).
The unification conjecture itself, one enlarged modular structure in which one vacuum event selects both
polarizations, was not found.

## 6. Conjugate collapse drives our acceleration (C5): partly anticipated

*In plain terms: a partner universe that contracts while ours expands, and drives our acceleration, is published,
as is the general fact that collapse in one description of a universe can be accelerated expansion in another. What
was not found is the partner as the momentum-space description of our own universe, a·ã = 1. The verdict counts that
identity as part of the conjecture; without it, the published partner could be read as anticipating the founding
sentence, "Their collapse is our acceleration", though never the route #11 keeps (§2). The rule by which the
program carries the partner's contents into our universe is, as a formula, a known symmetry of string cosmology,
and the rule it replaced is another known formula; using the rule inside ordinary gravity, so that a contracting
partner dominated by kinetic energy acts on ours as a cosmological constant, was not found.*

**A contracting partner that drives our acceleration** [S]. Henry-Couannier's Dark Gravity (on arXiv from 2006; the
source-driven acceleration from its 2010 version) pairs our
metric with a conjugate one whose scale factor is the inverse of ours. In his 2018 proceedings the dark side
contracts as ours expands and, after a permutation of the two sides' regimes, drives our recent acceleration without
a cosmological constant (read by the finder and its verifier through a web fetch; the proceedings exist only as a
PDF, which the code checks cannot read). His review (arXiv:gr-qc/0610079; the passage dates from its 2013 version) states the mechanism: "If one or both are evolving in a
cold era, there is a dominant source term determined by the content of the side with greater scale factor." His
partner is a time-reversed twin, not the momentum description of the same universe, and its driver is dust, the
version #11's corrected dictionary maps to dust.

**Collapse in one frame, acceleration in another** [S].
- Gasperini and Veneziano 1993: "The inflationary scenarios suggested by the duality properties of string cosmology
  in the Brans-Dicke (or String) frame are shown to correspond to accelerated contraction (deflation) when
  Weyl-transformed to the Einstein frame." Their 2003 review: "Inflation in the S-frame, for instance, can be
  represented as gravitational collapse in the E-frame". Buonanno, Damour and Veneziano 1999: "Each such singular
  space-like hypersurface of gravitational collapse becomes, in the string-frame metric, the usual big-bang t=0
  hypersurface".
- For present-day dark energy, Mukherjee, Jassal and Lochan 2024: "the effect of dark energy can equivalently be seen
  as collapse of space in a conformally connected universe". The dark energy is put in by hand there, and the
  collapse is a second description of it, not its source; in the main construction the timing is set by a free
  parameter, and for ΛCDM the conformally connected universe collapses in the matter era and expands again after a
  bounce, through the dark-energy era, the reverse of C5's timing (the round-3 verifier for C5; the panel judge for
  C5).
- These are two frames of one universe, the same structure as the program's two descriptions, and the collapsing
  side's content is kinetic in both: a massless scalar in Gasperini and Veneziano's Einstein frame (2003, §3.3), and
  in Mukherjee, Jassal and Lochan's §6 a stiff fluid in a contracting Einstein frame, paired with a de Sitter Jordan
  frame that mimics the dark-energy era. That is the pairing of the kept route (dual stiff ↦ Λ), as one exact
  solution of Brans–Dicke gravity at a chosen value of its parameter, with separate clocks, not as a dictionary.
- Not found: the partner as the momentum description of our own universe, contracting throughout our expansion by
  a·ã = 1, and with it the kept route as #11 §10 derives it: with one shared lapse a dual-frame fluid contributes
  w_eff = −w̃, so the conjugate energy enters our own Friedmann equation, and a contracting conjugate universe with
  kinetic-dominated contents would act on ours as a cosmological constant (the panel judge for C5).
- Bearing on the route's open question: in a contracting universe anisotropy grows like a stiff fluid and comes to
  dominate contents with w < 1; it keeps a fixed ratio to stiff contents, and only contents with w > 1 contract
  isotropically (Erickson, Wesley, Steinhardt and Turok 2004). A contracting conjugate universe whose contents have
  w̃ < 1 would then be stiff-like in scaling but anisotropic, while #11's dictionary is derived for isotropic fluids
  (the round-1 verifier for C5).

**Against the first version** [S]. Planck 2018 (Aghanim et al. 2020), with supernovae and baryon acoustic
oscillations and wₐ fixed at 0, measures w₀ = −1.028 ± 0.031, consistent with a cosmological constant: a
measurement for #11 §10's statement that the data exclude the heuristic version's w = −2, which #11 makes without a
citation (flag 65). It does not bear on the kept route, which gives w = −1 for exactly stiff contents (the round-1
verifier for C5; the panel judge for C5).

**Related** [S]: Bolognesi 2015, a Born-reciprocal theory in which "The trans-Planckian theory provides an
explanation for the present acceleration of the universe scale factor."; Berglund, Hübsch and Minić 2019, where "the
curvature of the canonically conjugate dual space provides for a positive cosmological constant to leading order";
Hur et al. 2025, "In our model, dark energy stems from the curvature of the dual spacetime"; Wu and Yang 2014, where
"we demonstrate that the contraction of the dual space automatically leads to both an inflation phase and a
decelerated expansion of the ordinary space" in double field theory. None has a collapsing partner driving our
present acceleration.

**The dictionary** [S]. #11 §10's corrected dictionary, w_eff = −w̃, is as a map of fluid variables the scale-factor
duality of string cosmology with sources: Gasperini and Veneziano 2003, §2.2, "The above equations with sources are
invariant under time reflection and under the duality transformation" (their eq. 2.32). The transformation, which
holds the shifted dilaton φ̄ fixed, sends each scale factor aᵢ → 1/aᵢ and the pressure p̄ → −p̄ at fixed ρ̄, where
ρ̄ = ρ∏aᵢ and p̄ = p∏aᵢ, so the equation of state p = γρ goes to γ → −γ. They credit Veneziano 1991, whose abstract
reads "The string-modified, Einstein-Friedman equations are then shown to possess physically-inequivalent,
duality-related solutions". The round-1 verifier for C5 and the panel judge for C5 each did the algebra for three
spatial dimensions in an executed script and found the program's w_eff = −w̃ (`review/literature-check/checks/`);
`verify/literature_check.py` repeats the judge's checks in the gate (section G), among them those behind the
statements below on the partner of a stiff source and on the other published inversions. #11 tags the dictionary [D — corrected en route] and §15 counts it among the corrections
that sharpened the hard core (flag 66). What the program adds is its derivation, from a·ã = 1 with one shared lapse
(#11 §10), and its use. Scale-factor duality maps one solution of string-frame dilaton gravity to another, a pairing
that "has no analogue in the context of the Einstein cosmology, where there is no dilaton, and the duality symmetry
cannot be implemented" (§2.2); within it the partner of a stiff source is not de Sitter (the panel judge for C5; section G of the gate shows that no
de Sitter universe has the partner's source, whatever the sign of its energy density).
Entering the conjugate's energy as a source in our Einstein-gravity constraint, so that dual stiff acts as Λ, is the
program's step. The superseded heuristic, −2 − w̃, is also a published map: the phantom duality of flat Friedmann
models, which keeps the density and the cosmic time (Chimento and Lazkoz 2003; Dąbrowski, Stachowiak and Szydłowski
2003, who pair dust with a phantom of w = −2). The correction #11 §15 counts therefore moved the dictionary from one
published map to another. A third map, at shared conformal time, gives w + w̃ = −2/3 (Camara da Silva, Lima and
Sotkov 2015) and is Dark Gravity's kinematics; under it the conjugate content that acts on ours as Λ is radiation,
and Dark Gravity pairs a de Sitter phase of ours, in an inflation-like epoch, with a radiation-like contracting
conjugate side. Which identification of the two sides holds decides which content acts as Λ: stiff under the
program's, Λ itself under the phantom duality, radiation at shared conformal time (the round-1 verifier for C5 and the
panel judge for C5, each in an executed script).

## 7. Clumping in momentum space (C6): partly anticipated

*In plain terms: dark matter collecting into a single momentum state, a Bose–Einstein condensate, is published in
several forms. Paul's image is different: a smooth spread of velocities breaking into several flocks of similar
velocity because similar velocities attract. That was not found. The verdict counts condensation as a form of the
conjecture; restricted to the flocks, it would be related only (§2). Two consequences the lab notebook drew from
clumping, weaker drag on the globular clusters of the Fornax dwarf galaxy and grainy velocity structure in halos,
have published counterparts that need no clumping.*

**Condensation in momentum** [S]. Riotto and Tkachev 2000: "However, with time the Bose-condensation will occur";
Sikivie and Yang 2009: "We show that cold dark matter axions thermalize and form a Bose-Einstein condensate.", and
"Axion BEC means that (almost) all axions go to one state."; Berezhiani and Khoury 2015, a condensate "giving rise to
a superfluid core within galaxies"; Levkov, Panin and Tkachev 2018: "We study Bose-Einstein condensation and
formation of Bose stars in the virialized dark matter halos/miniclusters by universal gravitational interactions."
#11 already lists the last as its reference [13]†, among the wave-dark-matter papers behind the wave island (§9).

**Against the form of Sikivie and Yang** [S]. Guth, Hertzberg and Prescod-Weinstein 2015: "we conclude that while a
Bose-Einstein condensate is formed, the claim of long-range correlation is unjustified". Under attractive
interactions, gravity among them, the condensate forms clumps localized in position, not one momentum state spread
through space. The paper treats no attraction acting in velocity, so it does not test the founding image.

**Related** [S]. In bounded-confidence models of opinion dynamics, "When the opinions of two agents are sufficiently
close, they both acquire the average of their initial opinions; otherwise, they do not interact." (Ben-Naim,
Krapivsky and Redner 2003). "Generically, the system reaches a steady state with a finite number of isolated,
noninteracting opinion clusters", which is the shape of velocity flocks under a gated attraction, in another field.
Sikivie, Tkachev and Wang 1995: "The cold dark matter spectrum on earth is expected to have peaks in velocity
space.", from infall streams, not from clumping.

**Consequences the lab notebook drew** [S]. Two consequences the lab notebook drew from momentum-space clumping (#1
§5.2, §9), now under review as Fornax friction suppression and velocity-space granularity in halos (#11 §13), have
published counterparts without it: wave or superfluid dark matter resolves the timing of Fornax's globular clusters
and suppresses dynamical friction (Hui, Ostriker, Tremaine and Witten 2017; Berezhiani, Elder and Khoury 2019), and
streams in velocity are expected in outer halos from infall (Zemp et al. 2009), so the test the momentum-gravity note
proposes (`notes/velocity-gated-gravity.md` §4) would have to look at inner halos or at stream widths; all three
labeled related by the round-1 verifier for C6 and C7. The panel judge for C6 reads Berezhiani and Khoury 2015 as
the notebook's condensed-core sentence nearly word for word.

## 8. A long-range velocity-gated attraction (C7): not found

*In plain terms: no paper the check read proposes that dark-matter particles attract each other at long range only
when their velocities are close. The nearest is a Born-reciprocal partner of Newton's potential that depends on
velocity differences, but it acts on all matter and exerts no force in position.*

- Delbourgo and Lashmar 2008 apply Born reciprocity to the 1/r potential: "We investigate this idea for atomic
  physics and galactic motion, where one is basically dealing with a 1/r potential". Their Hamiltonian adds a
  momentum-space partner of Newton's term. Summed over a galaxy's masses and their relative speeds, it
  goes as 1/|v − v′|, and the finder and the panel judge for C6 read it as an attraction. It does not depend on
  position, so in their equations of motion (eq. 4) it changes the relation between velocity and momentum, not the
  force: the finder noted this, its verifier lowered the finding from partial to related on that ground, and the
  panel judge for C7 upheld related. It acts on all masses.
- Velocity-dependent forces of the Weber type are long-established (Bunchaft and Carneiro 1997), with velocity scale
  c, not a gate.
- Against [S]: Kesden and Kamionkowski 2006 bound a force acting on dark matter alone with the tidal streams of the
  Sagittarius dwarf: "The Sgr dwarf galaxy is seen to have roughly equal streams, challenging models in which DM and
  baryons accelerate differently by more than 10%." C7's attraction acts among χ only and is gated, so the bound
  applies at the satellite's relative speed. The momentum-gravity note maps it to ε ≲ O(1), 0.2–2.5 at v* = 120 km/s,
  depending on how the gate is averaged over the orbit and on the reading, and records that the 10% level is stated
  without a confidence level and disputed by Keselman, Nusser and Peebles; the bound never beats the Lyman-α forest
  in the record's reading (`notes/velocity-gated-gravity.md` §6).

## 9. What follows for the record

*In plain terms: no status changes. The conjectures stay what #11 makes them. What changes is what #11 should cite,
and six such points are flagged for Paul's ruling.*

**Statuses** [P.R.'s rule, root `CLAUDE.md` 'Method']. Prior art kills nothing and confirms nothing. C1 stays alive,
P.R.'s core conjecture; C2, C3, C4, C5 and C6 stay open [O], his conjectures; C7 stays his conjecture outside the
record.

**Flags** (`review/wiki-build-flags.md`, pending).
- 64: C1's identification is published (Minic and coauthors, 2020 on) and #11 cites none of it.
- 65: partial prior art for C4, C5 and C6 is uncited in #11 §11.4, §10 and App. A items 3 and 9, and so is a
  measurement for §10's statement that the data exclude the heuristic version's w = −2 (Planck 2018).
- 66: §10's dictionary is, as a map of fluid variables, scale-factor duality with sources; its use in Einstein
  gravity is the program's.
- 67: §11.3's bridge between the two dualities is a published remark.
- 68: §12's exclusion of the minimal hidden sector was published first, independently, by Brümmer et al. (arXiv
  2025, before #14 v3; Phys. Rev. D 2026).
- 69: row 1's "zero cluster signal" meets two fits that mildly prefer a nonzero cross-section at cluster speeds.

**Incidentally, for the † battery** (OP10): the metadata of #11's [3]† (both papers), [13]† (its first paper) and
[18]† (Montonen and Olive) match INSPIRE. Whether they support what #11 cites them for was not checked. The check
also found sources for two [T] statements of §11.3 that carry no citation of their own: U-duality containing T- and
S-duality (Hull and Townsend 1995, verified) and a duality frame as the choice of a polarization (Lopes Cardoso and
Mohaupt 2020, labeled by one agent); and it verified three of the histories of the monopole null result that flag 59
cites with † (Langacker and Pi 1980; Dvali, Melfo and Senjanovic 1995; Dvali, Liu and Vachaspati 1998).

## 10. Limits

*In plain terms: "not found" means not found by these searches. The searches reach most of the English-language
physics literature indexed online; they could miss a paper in another language, in a venue no database indexes, or
behind a closed repository.*

- OpenAlex's free daily quota ran out during round 3, so the sweeps finished on Crossref, DataCite, Zenodo, HAL and
  the web, and the OpenAlex queries planned after that point did not run: among them four on explanations of the
  null result (C3), others on monopoles in momentum space, on electric–magnetic duality with position and momentum
  and on a magnetic counterpart for each charged particle (C2, C4), three on velocity alignment and velocity streams
  (C6, C7), and some for C5 and the older lineages (`review/literature-check/round3/`). The panel judge for C3 rated
  its confidence medium for this reason and for the unread Khademi item. No API key was requested. A rerun on
  2026-11-03 (round 5) found the quota not yet renewed (it renews at 00:00 UTC) and stopped after one refused query;
  the 26 OpenAlex queries, with four for Semantic Scholar, which also refused, are listed in
  `review/literature-check/round5/not-run-queries.json`. Two arXiv queries of the list ran and found nothing new.
- Khademi 2009 is read only in its abstract; its two pages could change C3's verdict (§4).
- Two leads for C4 that the round-1 verifier for C1 passed on were never assessed: Bordes, Chan and Tsou 2018
  (arXiv:1806.08268), a hidden sector parallel to ours with flavour and colour interchanged, proposed as dark matter,
  and Mathur and Sharatchandra 1991, dual matter fields of dyons. Either could bear on §5's finding that none of
  the magnetic dark sectors found pairs each charged particle of ours with an analog.
- Literature not in English was not searched.
- Not assessed: arXiv:1709.10080 (Szabo 2017, monopoles and nonassociative quantum theory), surfaced in round 5;
  Comay 1985 on whether monopoles would register in our instruments (C3), behind a sign-in; the backreaction
  literature for C5, which the lineage sweep recommended and no sweep covered.
- Carlos Castro Perelman's large output on Born's reciprocal relativity was screened through INSPIRE and read only
  in part.
- Six quotations in two findings that carry a verdict come from sources the code checks could not read, a PDF
  (Henry-Couannier 2018, four) and a letter on the Physics Today website (Goldhaber 2017, two); agents read them
  through a web fetch. The note paraphrases them and names how they were read.
- The labels are agents' judgments. Verification, the panel and the code checks test them; they do not replace a
  human expert's reading.

## 11. Record

*In plain terms: how the check ran, what it cost, how the expected verdicts written down beforehand scored, and how
agents reviewed this write-up twice, checked the edits written or merged by hand and swept it for stale statements.*

**Scale.** Four workflows (search and verify; the citation screen; coverage; the panel), 31 agents, about
11.2 million tokens as the workflow tool reported them; the two reviews of this write-up, round 5, the check of
the merges and the last sweep (below) came after and are not counted. A reboot stopped the panel's first launch before any judge
returned; it ran again from the start.

**Pre-registration, scored** (`review/literature-check/preregistration.md`, written before any search agent was
launched, after a test of the search tools had shown three papers, which it discloses, and kept
out of the agents' reach). Four of seven predicted verdicts were right (C2, C3, C5, C7); C3's hit, like its verdict and the second overall
prediction below, is provisional until Khademi 2009's full text is read (§4). The three misses all
underestimated the prior art: C1 was predicted partly anticipated and is anticipated; C4 and C6 were predicted related
only and are partly anticipated. They are also three of the four verdicts that rest on a reading of the conjecture
(§2): under the other readings the judges state, each would have been a hit, and C5's hit a miss. For C6 the
prediction named the condensation literature itself and labeled it related; the panel counts it as a form of C6.
Both overall predictions held: at least one of C1 and C5 at least partly anticipated;
C2 and C3 meeting phrase collisions but no proposal of monopoles in momentum space. The weakest link named, recall in
venues the tools could not reach, is where the remaining risk sits (§10).

**Files** (`review/literature-check/`): `README.md`; `brief.md`, the agents' brief; `preregistration.md`; `round1/`
to `round3/` and `panel/`, each agent's findings, verdicts and query logs; `screen/`, the citation screen;
`findings.json`, the 287 merged findings; `recheck.json` and `recheck.out`, the code check of identifiers and
quotations; `sources.json` and `quotes.json`, the metadata snapshots and quotations the gate checks; `round5/`, round 5's
attempted rerun of the blocked queries, its reading of Khademi 2009 and the runner for the queries still to run;
`checks/`, the two agents' executed scripts for the dictionary (§6); `workflows/`, the workflow scripts and their results; `tools/`, the search and consolidation
scripts.

**The review of this write-up** (2026-11-03). Two fresh reviewers read the first draft against the record, one the
note, the flags, the root `CLAUDE.md` entry and the record's README (20 findings), one the wiki (20 findings and a closing remark). Six further agents each tried to
refute a group of their findings, and one listed ten more stale statements in the wiki: none was refuted, and of the 56 verdicts (some findings were judged in parts), 41 confirmed and 15 confirmed in part, and their corrections
are applied here (`review/literature-check/workflows/workflow5-result.json`). The largest: §8 had said that the bound
from the Sagittarius streams was never applied to the gated force, which the momentum-gravity note does; §6 had
presented kinetic contents as a difference from the literature; §1 and §2 overstated how many findings a second agent
checked and how many quotations code found. Round 5, run beside the review (`review/literature-check/round5/`),
tried to rerun the blocked queries, which OpenAlex and Semantic Scholar still refused (§10), and read Khademi 2009's
abstract, which two judges then labeled (§4). No verdict changed.

**The second review** (2026-11-03). Three fresh reviewers read the corrected write-up, one the note, the flags, the
root `CLAUDE.md` entries and the record's README (23 findings), one the wiki (25), and one what was missing or
unverified (23); each was followed by an agent that tried to refute its findings. None was refuted, 64 were confirmed
and 7 confirmed in part, and their corrections are applied here, merged where two touched the same passage
(`review/literature-check/workflows/workflow7-result.json`). The largest: §2, §5, flag 67 and the wiki had read
Berglund, Hübsch and Minic 2021 as making the dark sector the electric–magnetic dual of the visible one, where both of
its gauge groups have visible fields; §2 left out that C5's verdict also rests on a reading, the only one that would
raise a verdict; the note left out verified findings that bear on #11 (§4–§7, §9); and the algebra behind flag 66 had
no script in the gate, which section G of `verify/literature_check.py` now supplies. No verdict changed.

**A check of the merges** (2026-11-03). Four further agents, each followed by one that tried to refute its findings,
checked the edits written or merged by hand in applying the second review, the new section G and the note as a
whole: 47 findings, none refuted, 43 confirmed and 4 confirmed in part, applied here
(`review/literature-check/workflows/workflow8-result.json`). The largest: the power laws section G used for a stiff
source and its partner have negative energy density in the string frame, so section G now also shows that within scale-factor duality no de
Sitter universe has the partner's source; the gate now finds the counts that section B recomputes in the note's
prose, at the one place where it looks for each; and §2 now gives the round-1 verifier's qualification of the
one reading that would raise a verdict. No verdict changed.

**A last sweep** (2026-11-03). One agent, followed by one that tried to refute its findings, checked the texts written
by hand in applying that check and swept the repository for statements the edits had left stale: 14 findings, none
refuted, 13 confirmed and 1 confirmed in part, applied here
(`review/literature-check/workflows/workflow9-result.json`). The largest: this section had said that the gate finds
each count it recomputes in the note's prose, where it looks for each at one place; and two wiki pages gave only
the panel judge's side of the reading that would raise C5's verdict. No verdict changed.

## References

All retrieved by live search for this note [S]; metadata in `review/literature-check/sources.json`.

- A. Addazi et al. (162 authors), "Quantum gravity phenomenology at the dawn of the multi-messenger era—A review", Prog. Part. Nucl. Phys. 125, 103948 (2022), arXiv:2111.05659
- F. C. Adams, M. Fatuzzo, K. Freese, G. Tarlé, R. Watkins, M. S. Turner, "Extension of the Parker bound on the flux of magnetic monopoles", Phys. Rev. Lett. 70, 2511 (1993), doi:10.1103/PhysRevLett.70.2511
- N. Aghanim et al. (181 authors), "Planck 2018 results. VI. Cosmological parameters", Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209
- A. O. Barut, "Superselection rule for magnetic charges and the search for magnetic monopoles", Phys. Lett. B 38, 97 (1972), doi:10.1016/0370-2693(72)90749-6
- E. Ben-Naim, P. L. Krapivsky, S. Redner, "Bifurcations and Patterns in Compromise Processes", Physica D 183, 190 (2003), arXiv:cond-mat/0212313
- A. Bérard, H. Mohrbach, "Monopole and Berry phase in momentum space in noncommutative quantum mechanics", Phys. Rev. D 69, 127701 (2004), arXiv:hep-th/0310167
- L. Berezhiani, B. Elder, J. Khoury, "Dynamical Friction in Superfluids", JCAP 10, 074 (2019), arXiv:1905.09297
- L. Berezhiani, J. Khoury, "Theory of dark matter superfluidity", Phys. Rev. D 92, 103510 (2015), arXiv:1507.01019
- P. Berglund, D.-C. Dai, D. Edmonds, Y.-H. He, T. Hübsch, V. Jejjala, M. J. Kavic, D. Minic, S. Powers, J. H. Simonetti, D. Stojkovic, T. Takeuchi, "Quantum Gravity and Phenomenology: Dark Matter, Dark Energy, Vacuum Selection, Emergent Spacetime, and Wormholes" (2022), arXiv:2202.05104
- P. Berglund, L. Freidel, T. Hübsch, J. Kowalski-Glikman, R. G. Leigh, D. Mattingly, D. Minic, "Infrared Properties of Quantum Gravity: UV/IR Mixing, Gravitizing the Quantum — Theory and Observation" (2022), arXiv:2202.06890
- P. Berglund, T. Hübsch, D. Minić, "Dark Energy and String Theory", Phys. Lett. B 798, 134950 (2019), arXiv:1905.08269
- P. Berglund, T. Hübsch, D. Minic, "String Theory, the Dark Sector, and the Hierarchy Problem", LHEP 2021, 186 (2021), arXiv:2010.15610
- P. Berglund, T. Hübsch, D. Minic, "Mirror Symmetry, Born Geometry and String Theory" (2021), arXiv:2111.14205
- P. Berglund, T. Hübsch, D. Minic, "On de Sitter Spacetime and String Theory", Int. J. Mod. Phys. D 32, 2330002 (2023), arXiv:2212.06086
- P. Berglund, T. Hübsch, D. Minic, "String Theory Bounds on the Cosmological Constant, the Higgs Mass, and the Quark and Lepton Masses", Symmetry 15, 1660 (2023), arXiv:2307.16712
- S. Bolognesi, "A cosmology of a trans-Planckian theory and dark energy", Int. J. Mod. Phys. D 23, 1450046 (2014), arXiv:1207.5514
- S. Bolognesi, "Born Reciprocity and Cosmic Accelerations" (2015), arXiv:1506.02187
- M. Born, "Reciprocity and the Number 137. Part I", Proc. Roy. Soc. Edinburgh 59, 219 (1940), doi:10.1017/s037016460001230x
- F. Brümmer, G. Ferrante, T. Fischer, M. Frigerio, "No room for minimal monopole dark matter", Phys. Rev. D 113, L091701 (2026), arXiv:2509.21924
- F. Brümmer, G. Ferrante, T. Fischer, M. Frigerio, "The price for monopole dark matter" (2026), arXiv:2607.29492
- F. Bunchaft, S. Carneiro, "Weber-like interactions and energy conservation", Found. Phys. Lett. 10, 393 (1997), arXiv:gr-qc/9708047
- A. Buonanno, T. Damour, G. Veneziano, "Pre-big bang bubbles from the gravitational instability of generic string vacua", Nucl. Phys. B 543, 275 (1999), arXiv:hep-th/9806230
- U. Camara da Silva, A. A. Lima, G. M. Sotkov, "Scale Factor Self-Dual Cosmological Models", JHEP 07, 017 (2015), arXiv:1502.06497
- S. Carneiro, "Dual symmetry breaking and magnetic charge screening" (2026), arXiv:2609.25324
- L. P. Chimento, R. Lazkoz, "On the link between phantom and standard cosmologies", Phys. Rev. Lett. 91, 211301 (2003), arXiv:gr-qc/0307111
- X. Chu, C. Garcia-Cely, H. Murayama, "Velocity Dependence from Resonant Self-Interacting Dark Matter", Phys. Rev. Lett. 122, 071103 (2019), arXiv:1810.04709
- M. P. Dąbrowski, T. Stachowiak, M. Szydłowski, "Phantom cosmologies", Phys. Rev. D 68, 103519 (2003), arXiv:hep-th/0307128
- R. Delbourgo, D. Lashmar, "Born reciprocity and the 1/r potential", Found. Phys. 38, 995 (2008), arXiv:0709.0776
- G. R. Dvali, H. Liu, T. Vachaspati, "Sweeping away the monopole problem", Phys. Rev. Lett. 80, 2281 (1998), arXiv:hep-ph/9710301
- G. R. Dvali, A. Melfo, G. Senjanovic, "Is There a monopole problem?", Phys. Rev. Lett. 75, 4559 (1995), arXiv:hep-ph/9507230
- D. Edmonds, D. Minic, T. Takeuchi, "On quantum gravity and quantum gravity phenomenology" (2021), arXiv:2109.12763
- J. Elsborg, C. Köhn, "Magnetic monopoles in two time dimensions", Int. J. Mod. Phys. A 37, 2250141 (2022), doi:10.1142/S0217751X2250141X
- J. K. Erickson, D. H. Wesley, P. J. Steinhardt, N. Turok, "Kasner and mixmaster behavior in universes with equation of state w >= 1", Phys. Rev. D 69, 063514 (2004), arXiv:hep-th/0312009
- J. Evslin, S. B. Gudnason, "Dwarf Galaxy Sized Monopoles as Dark Matter?" (2012), arXiv:1202.0560
- D. R. Finkelstein, "Homotopy approach to quantum gravity", Int. J. Theor. Phys. 47, 534 (2008), arXiv:gr-qc/0608086
- L. Freidel, R. G. Leigh, D. Minic, "Born Reciprocity in String Theory and the Nature of Spacetime", Phys. Lett. B 730, 302 (2014), arXiv:1307.7080
- L. Freidel, R. G. Leigh, D. Minic, "Quantum Gravity, Dynamical Phase Space and String Theory", Int. J. Mod. Phys. D 23, 1442006 (2014), arXiv:1405.3949
- D. Galakhov, A. Mironov, A. Morozov, "S-Duality and Modular Transformation as a non-perturbative deformation of the ordinary pq-duality", JHEP 06, 050 (2014), arXiv:1311.7069
- J. García-Moreno, V. Vento, "Electron and monopole properties in a dark matter model" (2026), arXiv:2610.02083
- M. Gasperini, G. Veneziano, "Inflation, deflation, and frame independence in string cosmology", Mod. Phys. Lett. A 8, 3701 (1993), arXiv:hep-th/9309023
- M. Gasperini, G. Veneziano, "The Pre-big bang scenario in string cosmology", Phys. Rept. 373, 1 (2003), arXiv:hep-th/0207130
- G. W. Gibbons, C. A. R. Herdeiro, "Born-Infeld theory and stringy causality", Phys. Rev. D 63, 064006 (2001), arXiv:hep-th/0008052
- A. S. Goldhaber, "Magnetic monopole search, past and present", Physics Today 70, 12 (2017), doi:10.1063/PT.3.3571
- J. Govaerts, "Magnetic monopoles with no strings attached: a portal to the dark side of dual electrodynamics", Eur. Phys. J. C 83, 158 (2023), arXiv:2302.03526
- A. H. Guth, M. P. Hertzberg, C. Prescod-Weinstein, "Do Dark Matter Axions Form a Condensate with Long-Range Correlation?", Phys. Rev. D 92, 103513 (2015), arXiv:1412.5930
- J. A. Harvey, S. Jensen, "Worldsheet instanton corrections to the Kaluza-Klein monopole", JHEP 10, 028 (2005), arXiv:hep-th/0507204
- J. A. Harvey, G. W. Moore, A. Strominger, "Reducing S duality to T duality", Phys. Rev. D 52, 7161 (1995), arXiv:hep-th/9501022
- F. Henry-Couannier, "The Dark Side of Gravity", Global J. Sci. Front. Res. A 13, 1 (2013), arXiv:gr-qc/0610079
- F. Henry-Couannier, "The Dark Side of Gravity and the Acceleration of the Universe", PoS EDSU2018, 047 (2018), doi:10.22323/1.335.0047
- T. Hübsch, D. Minic, "Quantum Gravity as Gravitized Quantum Theory" (2024), arXiv:2407.06207
- T. Hübsch, D. Minic, "Quantum Spacetime, Quantum Gravity and Gravitized Quantum Theory" (2026), arXiv:2604.19418
- T. Hübsch, D. Minic, "Nambu's Dynamics, Strings and Gravitized Quantum Theory" (2026), arXiv:2610.19522
- L. Hui, J. P. Ostriker, S. Tremaine, E. Witten, "Ultralight scalars as cosmological dark matter", Phys. Rev. D 95, 043541 (2017), arXiv:1610.08297
- C. M. Hull, P. K. Townsend, "Unity of superstring dualities", Nucl. Phys. B 438, 109 (1995), arXiv:hep-th/9410167
- S. Hur, V. Jejjala, M. J. Kavic, D. Minic, T. Takeuchi, "Dynamical dark energy, dual spacetime, and DESI", JCAP 11, 054 (2025), arXiv:2503.20854
- V. Jejjala, M. J. Kavic, D. Minic, T. Takeuchi, "Dynamical dark energy and infinite statistics", Int. J. Mod. Phys. A 37, 2242001 (2022), arXiv:2011.08852
- M. Kaplinghat, S. Tulin, H.-B. Yu, "Dark Matter Halos as Particle Colliders: Unified Solution to Small-Scale Structure Puzzles from Dwarfs to Clusters", Phys. Rev. Lett. 116, 041302 (2016), arXiv:1508.03339
- A. Kapustin, E. Witten, "Electric-Magnetic Duality And The Geometric Langlands Program", Commun. Num. Theor. Phys. 1, 1 (2007), arXiv:hep-th/0604151
- M. Kesden, M. Kamionkowski, "Galilean Equivalence for Galactic Dark Matter", Phys. Rev. Lett. 97, 131303 (2006), arXiv:astro-ph/0606566
- S. Khademi, S. Nasiri, "Generalized gauge transformations in phase space picture of quantum mechanics: Kirkwood representation", J. Phys. Conf. Ser. 128, 012016 (2008), doi:10.1088/1742-6596/128/1/012016
- S. Khademi, "Why magnetic monopoles are not seen?", International Conference of Mathematical Sciences (Maltepe Üniversitesi), pp. 365–366 (2009), handle 20.500.12415/6128, OpenAlex W3153563614; abstract read, full text not retrieved
- T. Kobayashi, D. Perri, "Parker bounds on monopoles with arbitrary charge from galactic and primordial magnetic fields", Phys. Rev. D 108, 083005 (2023), arXiv:2307.07553
- B. Kursunoglu, "Gravitation and Magnetic Charge", Phys. Rev. D 9, 2723 (1974), doi:10.1103/PhysRevD.9.2723
- P. Langacker, S.-Y. Pi, "Magnetic Monopoles in Grand Unified Theories", Phys. Rev. Lett. 45, 1 (1980), doi:10.1103/PhysRevLett.45.1
- D. G. Levkov, A. G. Panin, I. I. Tkachev, "Gravitational Bose-Einstein condensation in the kinetic regime", Phys. Rev. Lett. 121, 151301 (2018), arXiv:1804.05857
- G. Lopes Cardoso, T. Mohaupt, "Special geometry, Hessian structures and applications", Phys. Rept. 855, 1 (2020), arXiv:1909.06240
- Y. Lozano, "S duality in gauge theories as a canonical transformation", Phys. Lett. B 364, 19 (1995), arXiv:hep-th/9508021
- D. Lüst, E. Malek, R. J. Szabo, "Non-geometric Kaluza-Klein monopoles and magnetic duals of M-theory R-flux backgrounds", JHEP 10, 144 (2017), arXiv:1705.09639
- D. Minic, "From quantum foundations of quantum field theory, string theory and quantum gravity to dark matter and dark energy" (2020), arXiv:2003.00318
- D. Minic, "The Vacuum Energy Problem in Quantum Gravity and the Masses of Elementary Particles" (2023), arXiv:2305.12593
- C. Montonen, D. I. Olive, "Magnetic Monopoles as Gauge Particles?", Phys. Lett. B 72, 117 (1977), doi:10.1016/0370-2693(77)90076-4
- D. Mukherjee, H. K. Jassal, K. Lochan, "Bouncing and collapsing universes dual to late-time cosmological models", Eur. Phys. J. C 84, 318 (2024), arXiv:2207.02835
- H. Murayama, J. Shu, "Topological Dark Matter", Phys. Lett. B 686, 162 (2010), arXiv:0905.1720
- A. Riotto, I. Tkachev, "What if dark matter is bosonic and selfinteracting?", Phys. Lett. B 484, 177 (2000), arXiv:astro-ph/0003388
- J. G. Russo, P. K. Townsend, "Causal chiral 2-form electrodynamics", JHEP 07, 048 (2025), arXiv:2504.01467
- L. Sagunski, S. Gad-Nasr, B. Colquhoun, A. Robertson, S. Tulin, "Velocity-dependent Self-interacting Dark Matter from Groups and Clusters of Galaxies", JCAP 01, 024 (2021), arXiv:2006.12515
- J. Scott et al. (5 authors), "Dirac and non-Dirac conditions in the two-potential theory of magnetic charge", Eur. Phys. J. C 78, 382 (2018), arXiv:1805.09649
- P. Sikivie, I. I. Tkachev, Y. Wang, "The Velocity peaks in the cold dark matter spectrum on earth", Phys. Rev. Lett. 75, 2911 (1995), arXiv:astro-ph/9504052
- P. Sikivie, Q. Yang, "Bose-Einstein Condensation of Dark Matter Axions", Phys. Rev. Lett. 103, 111301 (2009), arXiv:0901.1106
- R. J. Szabo, "An Introduction to Nonassociative Physics", PoS CORFU2018, 100 (2019), arXiv:1903.05673
- T. Vachaspati, "An Attempt to construct the Standard Model with monopoles", Phys. Rev. Lett. 76, 188 (1996), arXiv:hep-ph/9509271
- G. Veneziano, "Scale factor duality for classical and quantum strings", Phys. Lett. B 265, 287 (1991), doi:10.1016/0370-2693(91)90055-U
- V. Vento, "Dark monopoles" (2025), arXiv:2507.06697
- H. Wu, H. Yang, "Double Field Theory Inspired Cosmology", JCAP 07, 024 (2014), arXiv:1307.0159
- M. Zemp et al. (8 authors), "The Graininess of Dark Matter Haloes", Mon. Not. R. Astron. Soc. 394, 641 (2009), arXiv:0812.2033
- C. Zhang, S.-H. Zhang, B. Fu, J.-F. Zhang, X. Zhang, "On the cosmological abundance of magnetic monopoles", JHEP 08, 220 (2024), arXiv:2404.04926

## Sources

- #11 `papers/broken-born-checkpoint-v2.md` §3, §4 (P4, P5), §8, §9, §10, §11.1–§11.4, §12, §13 rows 1 and 7, §14 item 10, §15, App. A
  items 3, 4, 5, 9, 11, References [3], [13], [18], [26], [28]; `notes/broken-born-theory.md` (v0.1 header; §5.2, §6, §9); `notes/velocity-gated-gravity.md` §4, §5, §6; `papers/phase-space-diameter.md`
  §4, §7.
- `review/literature-check/`: `findings.json`, `recheck.out`, `sources.json`, `quotes.json`, `screen/screen.json`,
  `round1/*.verify.json`, `round3/`, `round5/`, `panel/*.out.json`, `brief.md`, `preregistration.md`, `checks/`,
  `tools/consolidate.py`, `workflows/workflow*-result.json`.
- `review/wiki-build-flags.md` items 59 and 63, which this note cites, and 64–69, which it proposes.
- `verify/literature_check.py` — the gate's check of this note, and in section G of the algebra behind flag 66.
