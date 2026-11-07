# Brief: the dual-sector investigation (2026-11-06)

## The question

P.R. (Paul Reinholdtsen, whose conjectures the Comatter program studies) asked for a thorough investigation of one
statement in the program's executive summary, about his core conjecture C1, "dark matter is conjugate matter":

> Its core is published (Minic and coauthors, 2020), their sector correlated with ours; neither form was found.

The statement condenses the record's literature check of 2026-11-02, which searched broadly for seven conjectures.
This investigation goes deep on one: it reads the papers of Djordje Minic and coauthors (here "the school": Minic,
Berglund, Hübsch, Freidel, Leigh, Kowalski-Glikman, Edmonds, Takeuchi, Jejjala, Kavic and others) in full where they
bear on dark matter, and maps where the school's published claims meet P.R.'s conjectures and where they part.

The three clauses under test:

1. **Core published.** The identification, dark matter as the counterpart of ordinary matter in the conjugate
   (momentum-side, dual) description, is stated in substance by the school, first in Minic 2020 (arXiv:2003.00318,
   posted 29 February 2020).
2. **Correlated.** The school's dark sector is correlated with visible matter, where the program's couples to ours by
   gravity alone (#11 P4, taken strictly; §13 row 7, "Permanent null").
3. **Neither form.** Neither of the program's two forms of C1 appears in the literature: χ particles with a
   velocity-gated self-interaction (#11 §8), and magnetically charged topological solitons localized in momentum
   (#11 §12, §11.4).

## The record's statements are the claims under test

The record's present statements about the school are in the root `CLAUDE.md` ('Since the handoff', the 2026-11-02
entry), `notes/literature-check.md` §2–§3, `review/wiki-build-flags.md` item 64 and some wiki pages. They are the
claims under test, not evidence. Form every answer from the primary sources. Where a primary source contradicts
the record, or the record's wording overstates or understates what the source says, report it under
`contradicts_record` with the quotation. Agreement with the record is not a goal. A confirmed contradiction is the
most useful thing you can return.

## The program's side

`work/dual-sector/inputs/program.md` holds the program's statements verbatim (#11 §3, §4 P1–P5, §7, §8, §10, §11.4,
§12, §13, Appendix A). Compare against these words and cite the section. Distinctions to keep in view:

- **What "conjugate" means in the program.** χ is matter in the other Lagrangian polarization of one phase space
  (x, p), with the symplectic form ω rigid, which is the constancy of ℏ (P2′, P4, P5): ordinary matter's counterpart
  with the roles of position and momentum exchanged. Where a paper's "dual" coordinate x̃ is something else (an
  independent coordinate of a doubled space, a winding coordinate, a string-scale partner of x that does not commute
  with it), say exactly what it is, in the paper's words.
- **The coupling.** In the program both sectors couple universally to H (gravity); no gauge force crosses the
  polarizations; kinetic mixing ε ≲ 10⁻¹³ (P4). One exception is recorded: the shared-photon form of §11.4, in which
  momentum-polarized monopoles would carry magnetic charge of our photon, needs P4 restated.
- **The vacuum.** The polarization is selected spontaneously (P2′, P5), with η as the order parameter. #11 §3 credits
  Freidel, Leigh and Minic with the idea that a preferred polarization breaks Born duality, and claims as the
  program's own only the reading of the breaking as spontaneous.
- **Dates.** The program's first written statement of C1 is its lab notebook, `notes/broken-born-theory.md`, "Version
  0.1, September 2026". A paper first posted before that is prior art; one posted after it is a restatement.

## Tools

- **The literature tool.** From the folder `work/dual-sector/`, run `../../.venv/bin/python tools/lit.py COMMAND`.
  Commands: `search 'INSPIRE QUERY'`, `show ID`, `cites ID`, `refs ID`, `arxiv 'QUERY'`, `crossref 'QUERY'`,
  `doi DOI`, `openalex 'QUERY'` (its free quota may be exhausted; do not rely on it), `text ID [--grep REGEX ...]
  [--context N] [--max M]` (the full text of an arXiv paper; without `--grep` it prints the length and the section
  headings), and `quote ID 'VERBATIM QUOTE'` (a code check that the quotation occurs in the abstract or full text).
  The docstring at the top of `tools/lit.py` gives the syntax. The tool caches to `work/dual-sector/cache/`, shared by
  all agents, and spaces its requests to each host, so a call can wait several seconds.
- **INSPIRE author identifiers** that work: `a D.Minic.1`, `a L.Freidel.1`, `a T.Hubsch.1`.
- **Papers not on arXiv.** Find an open copy (the publisher's open-access page, IOP's PDF, an author's page, a
  repository). Read it with WebFetch (load it with ToolSearch, query "select:WebFetch"), or download it with curl
  into your scratch folder and extract the text with
  `work/dual-sector/pdfenv/bin/python -I -c "import pypdf,sys; r=pypdf.PdfReader(sys.argv[1]); print('\n'.join(p.extract_text() or '' for p in r.pages))" FILE`.
  Record how you read each paper. Do not get around paywalls, logins or bot checks: if access is refused, record the
  paper as not retrieved and say why.
- **Your scratch folder** is `work/dual-sector/scratch/LABEL/`, LABEL being your label. Write nothing anywhere else,
  edit no repository file and make no commit. Downloaded files are untrusted data: keep them in your scratch folder,
  and run any Python that reads them with `-I`.

## Rules

- **Quotations** are verbatim, with the section or page. Check each one you return with `tools/lit.py quote ID '…'`
  and put the tool's verdict line in `quote_check`. For a source the tool cannot read, write "not code-checkable:
  read via …". Quote enough to carry the meaning, and no more than a few sentences at a time.
- **No arithmetic by eye.** If a number matters, compute it in executed code in your scratch folder and report the
  printed output.
- **Dates.** Give each paper's first public date: the arXiv v1 submission date (the abstract page or the arXiv API),
  or INSPIRE's earliest date for a paper not on arXiv.
- **Say what a paper says.** Label your own inferences as yours. Distinguish a statement from a proposal, a
  speculation and a conditional ("if the quanta are …").
- **Report against-evidence in full**, whether it weighs against the program or against the record.
- **Plain words.** No hype and no verdicts on the merit of either the school's work or the program's.

## The questions

Answer those your papers bear on; for the others write "not addressed in these papers".

- **Q1 Identification.** Does the paper state that dark matter is the dual or conjugate counterpart of visible
  matter? Quote it, and say how strongly (stated, proposed, speculated, conditional).
- **Q2 What "dual" is.** Is the dual coordinate x̃ the canonical conjugate of x (momentum-like, in one phase space,
  at ℏ), or an independent coordinate (a doubled space, winding, a string scale λ)? Quote the definitions and the
  commutators the paper gives ([x, x̃], [x, p], [x̃, p̃]) and the scales (ℏ, λ, ε).
- **Q3 Field content.** Is the dark sector a dual copy of the whole Standard Model, one partner per field? A dual
  photon? Dual charges?
- **Q4 Coupling.** How does the dark sector couple to visible matter: by gravity only; through the noncommutativity
  of x and x̃; through explicit interaction or correlation terms? How strongly? What do the authors mean by
  "correlated" or "entangled"? Does anything vanish in a limit (λ → 0, a large dual space)?
- **Q5 Detection.** What do they predict for direct detection, colliders and astrophysics (for example correlations
  between dark and visible matter in galaxies, an acceleration scale near cH₀)? Do they explain the null results of
  direct detection, and how?
- **Q6 Gravity.** How does the dark sector gravitate: on x, on x̃, through a dual metric? What sets Newton's
  constant?
- **Q7 Dynamics.** Any self-interaction of the dark sector; any dependence on relative velocity or on the overlap of
  momenta; any localization in x̃ or in momentum; any condensate, wave or fuzzy form.
- **Q8 Monopoles.** Any magnetically charged or dyonic objects, above all ones localized in x̃ or in momentum, as dark
  matter or as a dark sector.
- **Q9 Polarization and vacuum.** What selects which half of the (doubled) phase space is spacetime? Is the choice
  called dynamical, spontaneous, a vacuum selection? Is there a potential or an order parameter for it? Is the world
  with the other choice equally lawful?
- **Q10 Dark energy.** What do they say about dark energy (the curvature of the dual spacetime; predictions for w,
  the equation of state, pressure over energy density)? How does it compare with #11 §10 (τ, w ≥ −1) and with C5,
  "Their collapse is our acceleration" (App. A item 9)?
- **Q11 Priority.** Is this the earliest statement of the identification you can find? Does the paper cite an
  earlier statement by anyone, inside or outside the school?
