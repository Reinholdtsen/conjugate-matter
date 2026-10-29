# Wiki build — rulings worksheet

*One entry for each of the 44 flags in [wiki-build-flags.md](wiki-build-flags.md): the text as it
stands, a proposed correction, and what would follow from accepting it. The proposals come from
each flag and its audit; where these leave a choice, the entry sets out the options. Prepared
2026-10-22. Line numbers refer to the files at commit 0990cc3.*

**How to rule.** On each entry's **Ruling** line, tick accept, reject or modify and add notes, or
give Claude the rulings in chat. Where an entry offers options (A, B, …), name the one chosen. A
modification is applied as its notes say.

Some proposals edit the same passage, so their edits will need merging: 3 and 4 (#7 §2); 5 and 39
(#11 §7.5, #9 §5 item 6); 6 and 7 (#11 §15, #9 §11); 10 and 25 (#1 §1); 33 and 34 (the obituary
script's docstring); and 6, 23, 27 and 43, which all edit #11 §10's technical paragraph (line 107),
with flag 27 also sharing lines with 6 and 23 in #9, #11 and #12. Other flags are best ruled
together: 3 and 23 (the circle |Z| = 1), 16 and 19 (one check script), 21 and 33 (the round-3
adjudication), 29 and 30 (#13 §1), and 24 and 27 (flag 27's option decides flag 24's wording).
Several proposals edit #11; one version bump, to v2.3, can carry them all.

**What an accepted ruling does.**

- The source document is corrected as proposed.
- Where the entry names an executed check, the check moves into `verify/` and is wired into
  `scripts/check.sh`.
- The wiki pages that point to the flag are updated.
- The flag's entry in `review/wiki-build-flags.md` records the ruling.

A rejected flag is recorded as rejected in `review/wiki-build-flags.md`, and its pointers in the
wiki stay. Nothing in the sources changes until Paul rules.

**Reading the entries.** Document numbers are HANDOFF §3's: #1 the lab notebook, #2–#4 the clumping problem
calc notes, #5–#8 the field-equation calc notes, #9 the superseded program paper (v1), #10 and #12 the
popular articles, #11 the checkpoint, #13 conjugate special relativity, #14 the withdrawn knot
dark-matter note. The toy note is `papers/reciprocity-toy-models.md` and the toy worklog
`notes/toy-lagrangian.md`; the adjudications, the round-3 pre-registration and the round-4
referee's notes are under `review/`. "Wiki pages (N)" counts the wiki pages that point to the
flag. Where an entry compares that list with "the task's grep" (or the requested, given or
prescribed grep), it means a case-sensitive search for "flag N", or for N after "flags" in the
same sentence; that search misses pages that write "Flag N" or "item N".

## Index

The first thirteen rows follow the "Where to start" list of `review/wiki-build-flags.md`, which
orders flags by consequence for the program's claims; the other thirty follow in number order. The
entries below keep this order.

| Flag | Short title | Audit verdict | Documents affected |
|---|---|---|---|
| 27 | τ's potential never goes negative; the turnaround needs it to | Confirmed (2 checks) | #11, #9, #1, HANDOFF; Option B also #4, #10, #12 |
| 43 | The thawing corridor lies in the CPL crossing quadrant, and no document says so | Confirmed (2 checks) | #11, #1 |
| 23 | a·ã = 1 is not the \|Z\| = 1 circle | Confirmed (2 checks) | #11, #5, #9, #1, HANDOFF |
| 39 | Two actions of ρ on the spin-2 sector | Convention or reading (2 checks) | #8, #11, #9 (Option A) |
| 3 | The misalignment potential's zero set is larger than #7 states | Confirmed (2 checks) | #7 |
| 6 | "By symmetry" overstates the vacuum-energy cancellation | Confirmed (2 checks) | #11, #8, #9, #1, #10, #12, HANDOFF |
| 1 | The "discrete" polarizations under strict P2 | Confirmed (2 checks) | #5, #11, #9, #1 |
| 33 | The soliton-obituary script claims more coverage than it has | Confirmed (1 check) | `verify/soliton_obituary.py`, round-3 adjudication |
| 34 | Typed-in constants called "PDG and Planck 2018 values" | Confirmed (1 check) | `verify/soliton_obituary.py` |
| 42 | A requested comparison recorded as applied | Confirmed (1 check) | Round-4 adjudication, toy worklog, #11, root `CLAUDE.md` |
| 41 | Restoration listed as shown by executed code | Confirmed (1 check) | Toy note |
| 5 | M_X written where M_X² is meant | Confirmed (2 checks) | #11, #9 |
| 28 | The formula beside "≈ 34" is the 137 one | Confirmed (2 checks) | #11 |
| 2 | The coupling I called "odd in K" | Confirmed (1 check) | Toy note; round-4 adjudication under the audit's reading |
| 4 | −h² missing from #7's expansion of S | Confirmed (1 check) | #7 |
| 7 | "Unique consistent structure" without "known" | Confirmed (1 check) | #11, #6, #9, HANDOFF, #10 |
| 8 | "Five-function" where "five-parameter" is meant | Confirmed (1 check) | #8 |
| 9 | #11 reference [24]: no authors, a descriptive title | Confirmed (1 check) | #11 |
| 10 | Four small pointer and wording slips | Confirmed (1 check) | #1, toy worklog, `verify/toy_s5.py`, round-4 referee notes (an annotation) |
| 11 | Tadpole growth in model II: ln N or 2 ln N | Convention or reading | Toy note, toy worklog, `verify/toy_gw.py` (Option A) |
| 12 | V_b's flat direction called an exact symmetry | Confirmed (2 checks) | Round-4 adjudication |
| 13 | The error bar "± 0.0001 at every size" | Confirmed (1 check) | Toy note, `verify/toy_s4.py` |
| 14 | Which square root's eigenvalues give Tr(g²) | Convention or reading | #7 (Option A) |
| 15 | "η antisymmetric-pairing" in #6 | Confirmed (1 check) | #6 |
| 16 | A ✓ (machine-verified) with no script behind it | Confirmed (1 check) | HANDOFF (variant 1); variant 2 gates the figure instead |
| 17 | Two forms of the gate's exponent, and a √2 in μ | Convention or reading (2 checks) | #6 (Option A or A′) |
| 18 | The year given for baryogenesis's "maturity" | Unclear (model memory) | #1, if a live check dates the conditions to 1967 |
| 19 | The gate regime of the classicality corollary | Convention or reading | #2 (Option A) |
| 20 | #11 reference [23]: one paper's title, another's arXiv number | Confirmed (1 check) | #11 |
| 21 | Ruling 3's overproduction range mixes two sources | Confirmed (1 check) | Round-3 adjudication |
| 22 | Planck's asymmetric N_eff interval written as symmetric | Confirmed (1 check) | #14 |
| 24 | "Square exactly at the bounce" does not say which bounce | Confirmed (1 check) | HANDOFF |
| 25 | #1 points to §7 for the constraint §6 derives | Confirmed (1 check) | #1 |
| 26 | DESI DR3 called "three-year data" | Confirmed (1 check) | HANDOFF |
| 29 | #13 cites #11 §7 for a range "in momentum" | Confirmed (1 check) | #13 |
| 30 | The tag on #13's two causal cones | Convention or reading | #13 (Option A) |
| 31 | "~10 orders" below sensitivity for quadratic photon dispersion | Convention or reading | #1 (Option A) |
| 32 | CMB-S4, row 10's probe, may have lost its funding | Unclear (model memory) | None until a live check; then possibly row 10 of #11, #9, #1 |
| 35 | The pre-registration cites HANDOFF §6 for §5's record | Confirmed (1 check) | Round-3 pre-registration |
| 36 | 66.58 and 63.72 placed in #11 §2, which does not print them | Confirmed (1 check) | `verify/battery.py`, #11 |
| 37 | The README's "missing magnetic monopoles" | Confirmed (1 check) | `README.md` |
| 38 | Stale details in the root CLAUDE.md and the gate's header | Confirmed (1 check) | Root `CLAUDE.md`, `scripts/check.sh` |
| 40 | "Bounded only at frozen H" in the root CLAUDE.md | Convention or reading (2 checks) | Root `CLAUDE.md` (Option A) |
| 44 | "Without the gauge invariance" in #6 §2 | Not yet audited | #6 |

## Entries

### Flag 27: τ's potential as written never goes negative, but the turnaround needs it to

**Audit:** confirmed (2 independent checks)

**Where it appears:**
- (a) The potential as written, V₀[1 + cos(τ/f)], whose minimum is 0:
  - `notes/broken-born-theory.md` line 89 (§3, Polarization sector), with its tag sentence on line 92
  - `notes/broken-born-program-v1.md` line 90 (§8, Dark energy)
  - `papers/broken-born-checkpoint-v2.md` line 107 (§10, Dark energy)
- (b) Statements that need V < 0: the turnaround, "goes negative", and t_turn in the over-constraint:
  - `notes/broken-born-theory.md` line 202 (§7 heading). The flag and the audit do not list it.
  - `notes/broken-born-theory.md` line 208 (§7 item 3)
  - `notes/broken-born-theory.md` line 209 (§7 item 4, t_turn)
  - `notes/broken-born-theory.md` line 230 (§9 row 6)
  - `notes/broken-born-theory.md` line 245 (§10, parameter count, t_turn)
  - `notes/broken-born-theory.md` line 263 (§12, one-paragraph summary)
  - `notes/broken-born-program-v1.md` line 12 (§0, technical abstract)
  - `notes/broken-born-program-v1.md` line 86 (§8, plain-language passage)
  - `notes/broken-born-program-v1.md` line 90 (§8; its t_turn sentence is in group (a))
  - `notes/broken-born-program-v1.md` line 102 (§9 row 5)
  - `notes/broken-born-program-v1.md` line 128 (§11, the over-constraint as a progressive sign)
  - `papers/broken-born-checkpoint-v2.md` line 105 (§10, plain-language passage)
  - `papers/broken-born-checkpoint-v2.md` line 107 (§10; its t_turn sentence is in group (a))
  - `papers/broken-born-checkpoint-v2.md` line 168 (§13 row 5)
  - `papers/broken-born-checkpoint-v2.md` line 206 (§15, the over-constraint as a progressive sign)
  - `papers/broken-born-checkpoint-v2.md` line 218 (App. A item 7)
  - `HANDOFF.md` line 23 (§2)
  - `notes/ufd-endpoint.md` line 43
  - `popsci/angle-of-the-mirror.md` line 33 (#10)
  - `popsci/universes-other-half.md` line 55 (#12)
  - `popsci/universes-other-half.md` line 73 (#12)
- Not the flagged statement, no change: the toy models' −2μ(1 + cos 2φ) and −(μ/2)(1 + cos 2φ) (`papers/reciprocity-toy-models.md` line 116, `notes/toy-lagrangian.md` line 320, `verify/toy_s4.py`, `verify/toy_coset.py`). The second auditor calls them a different object: a lattice potential taken "up to a constant", with no gravity.

**Now reads:**

(a) `notes/broken-born-theory.md` line 89:
> V(\tau) = V_0\left[1 + \cos(\tau/f)\right].

`notes/broken-born-theory.md` line 92:
> The potential's *periodicity* is forced by the Maslov topology **[D]**; its *existence* comes from the explicit breaking of Grassmannian rotations by the rigid $\omega$ (P2) — the rigidity is the "instanton" that tilts the circle. Its *magnitude* $V_0$ is a free parameter here. **[P/O]**

`notes/broken-born-program-v1.md` line 90:
> τ is hilltop quintessence on the Maslov circle: V = V₀[1 + cos(τ/f)], periodicity by topology, V₀ fixed by Ω_DE, two remaining parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint. Strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1+w₀).

`papers/broken-born-checkpoint-v2.md` line 107:
> **Dark energy [D + T]:** τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint.

(b)

`notes/broken-born-theory.md` line 202 (§7 heading):
> 7. Cosmology II: dark energy, its drift, and the turnaround

`notes/broken-born-theory.md` line 208 (§7 item 3):
> 3. **The turnaround.** A cosine potential is negative over half its range. Once $\tau$ rolls past $V = 0$, the effective vacuum energy is negative, expansion halts, and slow contraction begins.

`notes/broken-born-theory.md` line 209 (§7 item 4, t_turn):
> 4. **Parameter economy.** $V_0$ is fixed by $\Omega_{\rm DE}$; the observables $(w_0, w_a, t_{\rm turn})$ are then functions of two numbers, $(f, \tau_i)$. Three measurements, two parameters: one over-constraint. **[D]**

`notes/broken-born-theory.md` line 230 (§9 row 6):
> | 6 | Fate of expansion | Eternal de Sitter | Turnaround after $V(\tau)<0$; AdS transition preferred by current quintessence fits | — (long-horizon; the near-term test is row 5) |

`notes/broken-born-theory.md` line 245 (§10, parameter count, t_turn):
> | Dark energy | $f,\ \tau_i$ (2; $V_0$ fixed by $\Omega_{\rm DE}$) | $w_0,\ w_a,\ t_{\rm turn}$ (3) |

`notes/broken-born-theory.md` line 263 (§12, one-paragraph summary):
> a dark energy field that is literally the Maslov angle of the vacuum, forced by topology to a periodic potential, hence thawing, never phantom, and destined to go negative (turnaround = the conjugate bounce, by constraint);

`notes/broken-born-program-v1.md` line 12 (§0, technical abstract):
> Cosmology reduces to hilltop axion-like quintessence on the Maslov circle: thawing, never phantom, with an eventual turnaround identified with the conjugate frame's bounce by constraint.

`notes/broken-born-program-v1.md` line 86 (§8, plain-language passage):
> Dark energy is the compass angle of the vacuum's polarization, confined by topology to a circle, so its potential must be periodic: it therefore drifts, can never cross the phantom line, and eventually goes negative — at which point our expansion halts and reverses, an event that in the conjugate description is a collapsing universe rebounding.

`notes/broken-born-program-v1.md` line 90 (§8; its t_turn sentence is in group (a)):
> The turnaround is the conjugate bounce by the constraint identity: one event, two descriptions.

`notes/broken-born-program-v1.md` line 102 (§9 row 5):
> | 5 | Fate of expansion | Eternal de Sitter | Turnaround after V(τ) < 0 = conjugate bounce | (Long-horizon; near-term test is row 4) |

`notes/broken-born-program-v1.md` line 128 (§11, the over-constraint as a progressive sign):
> **Progressive signs** — forced convergence onto consistency islands (no-go → Higgs → HR class → palindrome); novel predictions not previously posed (island discriminant; knee shape; even-eigenstate masslessness as a bimetric-parity statement); an unsolicited theorem (Λ_wedge = 0); one over-constraint in the DE sector.

`papers/broken-born-checkpoint-v2.md` line 105 (§10, plain-language passage):
> Dark energy is the compass angle of the vacuum's polarization, confined by topology to a circle, so it must drift, can never cross the phantom line, and eventually goes negative — at which point our expansion halts and reverses, an event that in the conjugate description is a collapsing universe rebounding.

`papers/broken-born-checkpoint-v2.md` line 107 (§10; its t_turn sentence is in group (a)):
> The turnaround is the conjugate bounce by constraint identity.

`papers/broken-born-checkpoint-v2.md` line 168 (§13 row 5):
> | 5 | Fate of expansion | Eternal de Sitter | Turnaround = conjugate bounce | (Long horizon; near-term test is row 4) |

`papers/broken-born-checkpoint-v2.md` line 206 (§15, the over-constraint as a progressive sign):
> **Progressive signs:** forced convergence onto consistency islands; predictions not previously posed (rows 3, 11); an unsolicited identity (§7.3); one over-constraint (DE sector); the §11.3 unification generating new questions.

`papers/broken-born-checkpoint-v2.md` line 218 (App. A item 7):
> 7. Our expansion reverses at their bounce — **alive, corrected**: one event, two descriptions; live at DESI DR3.

`HANDOFF.md` line 23 (§2):
> Cosmology: duality dictionary w_eff = −w̃ (corrected from an earlier wrong −2−w̃); τ = hilltop/axion quintessence on the Maslov circle; thawing, w ≥ −1 always, eventual negative V ⇒ turnaround = conjugate bounce (one event, two descriptions). Consistent with DESI DR1/DR2 drift hints.

`notes/ufd-endpoint.md` line 43:
> What remains distinctively BBT's own: the exponential cliff + in-gate isotropy (particle island), the cliff-sharpness **island discriminant** (exponential vs (v*/σ)⁴), the dark-energy sector (thawing, no-phantom, turnaround — live at DESI DR3), and the permanent nulls (direct detection, monopoles, linear dispersion).

`popsci/angle-of-the-mirror.md` line 33 (#10):
> Continued weakening keeps it alive — shared credit with other dynamical-dark-energy models, but alive, and pointing at a spectacular long-term corollary: a weakening that eventually goes negative means our expansion one day stalls and reverses. In this theory, that far-future turnaround and the conjugate universe's rebound from collapse are one event, described twice.

`popsci/universes-other-half.md` line 55 (#12):
> The decline has an endpoint. The orientation's energy landscape dips below zero, and once the stored energy goes negative, the cosmic push becomes a pull: expansion slows, halts, and reverses.

`popsci/universes-other-half.md` line 73 (#12):
> And a revised ending for the universe: not indefinite expansion into cold, but an eventual turnaround — equivalently, in the other description, a contraction reaching bottom and rebounding.

**Proposed:** the audit favours Option A. Both auditors give it first, as the minimal repair that keeps every downstream claim; both name Option B and a free offset as the alternatives.

*Option A: write the potential as V₀cos(τ/f), with its negative minimum posited.* Group (b) then stands as written, apart from the w ≥ −1 knock-on under "If accepted, also", and #1 §7 item 3's "negative over half its range" becomes exact. Under A the turnaround rests on that posit: #1 §3 derives the potential's periodicity [D], but nothing in the documents fixes its zero point.

`notes/broken-born-theory.md` line 89:
> V(\tau) = V_0\cos(\tau/f).

`notes/broken-born-theory.md` line 92 (one sentence appended):
> The potential's *periodicity* is forced by the Maslov topology **[D]**; its *existence* comes from the explicit breaking of Grassmannian rotations by the rigid $\omega$ (P2) — the rigidity is the "instanton" that tilts the circle. Its *magnitude* $V_0$ is a free parameter here. **[P/O]** Its negative minimum $-V_0$ (an anti-de Sitter vacuum) is posited, not derived. **[P]**

`notes/broken-born-program-v1.md` line 90:
> τ is hilltop quintessence on the Maslov circle: V = V₀cos(τ/f) (negative minimum −V₀, posited [P], not derived), periodicity by topology, V₀ fixed by Ω_DE, two remaining parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint. Strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1+w₀).

`papers/broken-born-checkpoint-v2.md` line 107:
> **Dark energy [D + T]:** τ is hilltop quintessence on the Maslov circle, V = V₀cos(τ/f) (negative minimum −V₀, posited [P], not derived), periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint.

*Option B: keep V₀[1 + cos(τ/f)] and withdraw the turnaround.* This is the audit's alternative, given as instructions rather than drafted text:
- Replace each negativity claim in group (b) with "τ settles at V = 0 and dilutes like dust; there is no turnaround without a negative offset [O]".
- Drop t_turn from the over-constraint (#1 lines 209 and 245; #9 line 90; #11 line 107). That leaves (f, τᵢ) for (w₀, wₐ), so "one over-constraint" also leaves #9 §11 and #11 §15.
- Rewrite row 5 (#1 §9 row 6; #9 §9 row 5; #11 §13 row 5) as eternal, decelerating expansion.
- The plain-language passages, abstracts, #1's §7 heading, App. A item 7, HANDOFF §2, ufd-endpoint and the two popular articles follow.

A variant both auditors name: keep [1 + cos] and add an explicit free negative offset. That restores the turnaround, but the offset is a third parameter, so it removes the over-constraint.

When ruling, name the option (A, B or the offset variant) in the notes.

**If accepted, also:**
- Wiki pages (32): `wiki/_index.md`, `wiki/cosmology/_index.md`, `wiki/cosmology/dark-energy/_index.md`, `wiki/cosmology/dark-energy/cosmological-constant.md`, `wiki/cosmology/dark-energy/cpl-parametrization.md`, `wiki/cosmology/dark-energy/de-sitter-space.md`, `wiki/cosmology/dark-energy/over-constraint.md`, `wiki/cosmology/dark-energy/potential-sign.md`, `wiki/cosmology/dark-energy/quintessence.md`, `wiki/cosmology/dark-energy/tau-quintessence.md`, `wiki/cosmology/scale-factor-duality/_index.md`, `wiki/cosmology/scale-factor-duality/conjugate-bounce.md`, `wiki/dark-matter/momentum-clumping/net-theorem.md`, `wiki/glossary.md`, `wiki/gravity/tuning-test/geometric-action.md`, `wiki/history/documents/checkpoint.md`, `wiki/history/documents/handoff.md`, `wiki/history/documents/lab-notebook.md`, `wiki/history/documents/source-conflicts.md`, `wiki/notation.md`, `wiki/phase-space/modular-field/maslov-phase.md`, `wiki/predictions/_index.md`, `wiki/predictions/dark-energy-drift.md`, `wiki/predictions/fate-of-expansion.md`, `wiki/predictions/table-history.md`, `wiki/program/assessment.md`, `wiki/program/conjugate-universe.md`, `wiki/program/founding-suppositions.md`, `wiki/status/alive.md`, `wiki/status/open-problems.md`, `wiki/status/superseded.md`, `wiki/symmetry-breaking/rho-preserving-potential.md`. The task grep returns 27 files, 26 of them real. The 27th, `wiki/history/timeline.md`, names flag 27 only as flag 43's position in a list. The grep misses 6 pages that write "item 27" or "Flag 27": cosmological-constant, checkpoint, lab-notebook, source-conflicts, dark-energy-drift and table-history. Option A changes the potential that 30 pages quote; Option B changes the 6 pages quoting "negative over half its range" and every page stating the turnaround.
- Executed check: `review/wiki-build-checks/v_sign_check.py`, which only prints. In `verify/`, written with `check()` calls, it would assert:
  - 1 + cos x ≥ 0, with minimum 0 at x = π, so no sign change;
  - cos x < 0 on half the period;
  - for Option A's knock-on, ρ + p = τ̇² while w = −3 at τ̇ = 1, V = −1.

  For the turnaround itself (finite t_turn for V₀cos(τ/f); none up to 2000/H₀ for [1 + cos]), the auditors' algebra and integrations are `review/wiki-build-checks/audit/a_potential_algebra.py`, `audit/b_turnaround_numerics.py` (with `audit/d_convergence.py`) and `audit/v_sign_steelman.py`. Their anchors are independent of the paper: the flat Friedmann equation (H = 0 needs ρ = 0) and 1 + cos x = 2cos²(x/2).
- Also, under Option A: the audit's knock-on on w ≥ −1, set out after this list.
- Also, under either option:
  - a #11 version bump (v2.3);
  - #1 and #9 are superseded records, so the same choice between an edit and an erratum line arises as for flag 25;
  - the wiki's conflicts-register entry C20 resolved;
  - flag 24's wording depends on the choice (Option B removes "the turnaround");
  - #11 line 107 also carries flag 43's insertion, which is independent of this edit.

The knock-on under Option A: w ≥ −1 then holds only while ρ_τ > 0. `notes/broken-born-theory.md` line 206 (§7 item 1) now reads:
> 1. **$w \geq -1$ always.** $\tau$ is a canonical scalar; the null energy condition holds; phantom crossing is impossible. **[D]**

and would read:
> 1. **$w \geq -1$ while $\rho_\tau > 0$.** $\tau$ is a canonical scalar; the null energy condition holds ($\rho_\tau + p_\tau = \dot\tau^2 \geq 0$ always); phantom crossing is impossible. **[D]**

The same qualifier goes on "Strictly w ≥ −1" (#9 line 90), "strictly w ≥ −1" (#11 line 107) and "w ≥ −1 always" (`HANDOFF.md` line 23). The bound is restated, each time against DR2's crossing, at #11 line 107 ("The framework's strict w ≥ −1 therefore stands…"), #11 line 206 (§15) and root `CLAUDE.md` line 43. Other wordings of it ("never phantom", "no-phantom", "can never cross the phantom line") are at #1 lines 229, 263 and 275, #9 lines 12, 86 and 101, #11 lines 105 and 167, `notes/ufd-endpoint.md` line 43 and both popular articles; the ruling should say whether these take the qualifier too.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 43: The thawing corridor lies in the CPL quadrant that reads as a crossing, and no document says so

**Audit:** confirmed (2 independent checks). This audit is recorded in `review/wiki-build-flags.md` and `review/wiki-build-checks/corridor/`. `flag-audit.json` has no entry for flag 43.

**Where it appears:**
- `papers/broken-born-checkpoint-v2.md` line 107 (§10). It states the corridor, and DR2's crossing, in one paragraph without relating them.
- `notes/broken-born-theory.md` line 207 (§7 item 2). It compares signs only.
- `notes/broken-born-program-v1.md` line 90 (§8). It states the corridor but not DR2's crossing.
- Not the flagged statement, no change:
  - the corridor in the predictions tables (#1 line 229, §9 row 5; #9 line 101, §9 row 4), which do not compare it with DESI's fits;
  - #11 line 167 (§13 row 4), which already states the pressure by redshift ("DR2 already favors a crossing above z ≈ 0.4 (§10)"), the basis the flag says the pressure rests on;
  - root `CLAUDE.md` lines 42–44, whose statement of the pressure the flag says stands.

**Now reads:**

`papers/broken-born-checkpoint-v2.md` line 107 (the corridor, and DR2's crossing):
> **Dark energy [D + T]:** τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint.

> **Under pressure (v2.1):** DESI DR2 itself reports that in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4", and that this preference "is thus rather independent of parametrization choices made in the analysis" [21S]. The framework's strict w ≥ −1 therefore stands against the direct reading of the data.

`notes/broken-born-theory.md` line 207:
> 2. **Thawing shape.** Hilltop initial conditions give $w \approx -1$ in the past, rising now: $w_0 > -1$, $w_a < 0$, on the standard thawing corridor $w_a \approx -1.5\,(1+w_0)$. This is the *sign pattern DESI reports*.

`notes/broken-born-program-v1.md` line 90:
> Strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1+w₀).

**Proposed:** neither the flags file nor `flag-audit.json` gives suggested wording for flag 43. The text below states only what the flag establishes, and it uses #11's own "z ≃ 0.4" rather than the audit's DR2 Table 5 numbers. No source document uses the name "CPL", so the text writes the line w₀ + wₐ(1 − a) instead. In #1 the inserted [D] keeps the item's closing [T] from covering the derived crossing.

`papers/broken-born-checkpoint-v2.md` line 107 (three sentences inserted after "[21S]."):
> **Under pressure (v2.1):** DESI DR2 itself reports that in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4", and that this preference "is thus rather independent of parametrization choices made in the analysis" [21S]. The thawing corridor lies in the same quadrant as DR2's (w₀, wₐ) fits [21S], w₀ > −1 with w₀ + wₐ < −1 (on the corridor w₀ + wₐ + 1 = −(1 + w₀)/2), where the line w₀ + wₐ(1 − a) passes below −1 in the past; (w₀, wₐ) fits to fields that never fall below −1 can land there too [D]. What separates the two is the slope: the corridor's line crosses −1 at z = 2 for every w₀ [D], DR2's fits near z ≃ 0.4. The pressure rests on that crossing redshift, not on the quadrant. The framework's strict w ≥ −1 therefore stands against the direct reading of the data.

`notes/broken-born-theory.md` line 207:
> 2. **Thawing shape.** Hilltop initial conditions give $w \approx -1$ in the past, rising now: $w_0 > -1$, $w_a < 0$, on the standard thawing corridor $w_a \approx -1.5\,(1+w_0)$. This is the *sign pattern DESI reports*; the slope differs: the corridor's line $w_0 + w_a(1-a)$ crosses $w = -1$ at $z = 2$ **[D]**, DESI DR2's fits near $z \approx 0.4$.

`notes/broken-born-program-v1.md` line 90: no change. It is superseded by #11, which would carry the relation, and it does not state DR2's crossing.

**If accepted, also:**
- Wiki pages (12): `wiki/_index.md`, `wiki/cosmology/dark-energy/_index.md`, `wiki/cosmology/dark-energy/cpl-parametrization.md`, `wiki/cosmology/dark-energy/desi-dr2-phantom-crossing.md`, `wiki/cosmology/dark-energy/quintessence.md`, `wiki/cosmology/dark-energy/tau-quintessence.md`, `wiki/glossary.md`, `wiki/history/documents/checkpoint.md`, `wiki/history/documents/lab-notebook.md`, `wiki/predictions/dark-energy-drift.md`, `wiki/status/alive.md`, `wiki/status/open-problems.md`. The task grep returns 8 files. The 8th, `wiki/history/timeline.md`, records flag 43's history in its status line, log rows and sources; a ruling would add a row rather than edit these. The grep misses 5 pages that write "item 43" or "Flag 43": desi-dr2-phantom-crossing, tau-quintessence, checkpoint, lab-notebook and dark-energy-drift. `wiki/notation.md`'s "Flags 1–43" is a general entry. 5 pages quote "sign pattern DESI reports".
- Executed check: the scripts in `review/wiki-build-checks/corridor/` only print. `c2_anchors.py` prints PASS or FAIL for each of its anchors but sets no exit status. A `verify/` script would assert:
  - from `corridor_algebra.py` §1–2 or `c1_symbolic.py`: w₀ + wₐ + 1 = −(1 + w₀)/2 on the corridor, and its CPL line crosses −1 at z = 2 for every w₀;
  - from `dr2_comparison.py` part 1: DR2's four CPL fits (Table 5 values typed in, [S]) cross at 0.35 ≤ z ≤ 0.50;
  - from `hilltop_cpl.py` or `c3_fits.py`: integrated fields with min(1 + w) ≥ 0 give fits with w₀ > −1 and w₀ + wₐ < −1.

  Anchors independent of the paper: the CPL definition, DR2's published fits, and `c2_anchors.py`'s checks (analytic ΛCDM H(z), the CPL closed form, the Dutta–Scherrer shape). The rough Gaussian comparison (`dr2_comparison.py` part 2) is not needed by the proposed wording. The inserted [D] tags become [D][V] once the check is wired in.
- Also:
  - a #11 version bump (v2.3), which can be shared with flags 9, 27 and 28;
  - #11 line 107 also carries flag 27's potential, which is independent of this edit;
  - no numbered conflicts-register entry is affected. The register's "The reading of DESI" entry, settled by precedence, quotes #1's "sign pattern DESI reports", which the proposal keeps.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 23: a·ã = 1 is not the |Z| = 1 circle

**Audit:** confirmed (2 independent checks)

**Where it appears:** The statement appears in 14 places. The flag names #11 §6 and §10, #5 §C, #1 v0.3 and HANDOFF §2. The first auditor found the other nine: #11 lines 63, 105 and 217, #5 lines 58 and 82, and #9 lines 44, 50, 86 and 88.

- `papers/broken-born-checkpoint-v2.md` line 63 (#11 §6, plain-language passage)
- `papers/broken-born-checkpoint-v2.md` line 65 (#11 §6)
- `papers/broken-born-checkpoint-v2.md` line 105 (#11 §10, plain-language passage)
- `papers/broken-born-checkpoint-v2.md` line 107 (#11 §10)
- `papers/broken-born-checkpoint-v2.md` line 217 (#11 Appendix A item 6)
- `notes/geometric-core.md` line 55 (#5 §C)
- `notes/geometric-core.md` line 58 (#5 §C)
- `notes/geometric-core.md` line 82 (#5 §F)
- `notes/broken-born-theory.md` line 283 (#1 addendum v0.3)
- `notes/broken-born-program-v1.md` line 44 (#9 §4, plain-language passage)
- `notes/broken-born-program-v1.md` line 50 (#9 §4)
- `notes/broken-born-program-v1.md` line 86 (#9 §8, plain-language passage)
- `notes/broken-born-program-v1.md` line 88 (#9 §8)
- `HANDOFF.md` line 19 (§2)

**Now reads:**

`papers/broken-born-checkpoint-v2.md` line 63 (#11 §6, plain):

> the circle |Z| = 1 is the duality between our expanding universe and its contracting conjugate;

`papers/broken-born-checkpoint-v2.md` line 65 (#11 §6):

> **ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹, and the cosmological constraint a·ã = 1 (§10) is the |Z| = 1 locus.

`papers/broken-born-checkpoint-v2.md` line 105 (#11 §10, plain):

> Our expanding universe and its contracting conjugate are one motion written twice, like a number and its reciprocal — a relation forced by the constancy of Planck's constant and identical to the |Z| = 1 circle of the modular field.

`papers/broken-born-checkpoint-v2.md` line 107 (#11 §10):

> **Constraint [D]:** ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus.

`papers/broken-born-checkpoint-v2.md` line 217 (#11 App. A item 6):

> Conjugate universe shrinks as ours expands — **promoted to theorem** (a·ã = 1 from ℏ-rigidity; the |Z| = 1 locus).

`notes/geometric-core.md` line 55 (#5 §C):

> The cosmological constraint a·ã = 1 is the |Z| = 1 self-dual circle — the minisuperspace duality was the shadow of this modular action.

`notes/geometric-core.md` line 58 (#5 §C):

> One object now carries the whole geometric program: **metric (Im Z), momentum geometry and gate mediator (Re Z), scale-factor duality (|Z|), dark energy (boundary phase of Z).**

`notes/geometric-core.md` line 82 (#5 §F):

> the modular unification (reciprocity = Z → −Z⁻¹, cosmological duality = |Z| = 1).

`notes/broken-born-theory.md` line 283 (#1 v0.3):

> Born reciprocity = Z → −Z⁻¹ with self-dual point Z = i, and the cosmological constraint a·ã = 1 as the |Z| = 1 locus.

`notes/broken-born-program-v1.md` line 44 (#9 §4, plain):

> the self-dual point Z = i is the vacuum, the circle |Z| = 1 is the cosmological duality between our expanding universe and its contracting conjugate, and dark energy lives on the boundary of the domain as a phase.

`notes/broken-born-program-v1.md` line 50 (#9 §4):

> At X = 0 it sends g → g⁻¹: scale-factor duality. The minisuperspace constraint a·ã = 1 (§8) is the |Z| = 1 locus.

`notes/broken-born-program-v1.md` line 86 (#9 §8, plain):

> Our expanding universe and its contracting conjugate are one motion described twice — like a number and its reciprocal — a relation that turns out to be forced by the constancy of Planck's constant, and to be the |Z| = 1 circle of the modular field.

`notes/broken-born-program-v1.md` line 88 (#9 §8):

> **The constraint [D].** ω-rigidity fixes the comoving phase-space cell: a·ã = 1. Not an assumption — the statement that ℏ does not run; geometrically, the |Z| = 1 self-dual locus.

`HANDOFF.md` line 19 (§2):

> Modular field Z = X + iY on Siegel domain Sp(2d,R)/U(d); Im Z = metric, Re Z = X = momentum graviton; reciprocity = Z → −1/Z; a·ã = 1 is the |Z|=1 locus; dark energy τ = Maslov phase of the Shilov boundary Λ(4) ✓ (parametrization identities)

**Proposed:** The wording comes from the two auditors' suggestions and makes three points. First, a·ã = 1 holds along the whole vacuum slice X = 0, where it is det H = 1. Second, at X = 0, ρ carries a to ã = 1/a by inversion in the circle |Z| = 1, and that circle meets the slice only at Z = i. Third, in the plain-language passages the circle becomes the duality's mirror. The wording avoids "the circle is where a = ã", which holds under some readings of (a, ã) and not others (audit, `review/wiki-build-checks/audit/flag23_readings.out`). No number changes.

`papers/broken-born-checkpoint-v2.md` line 63 (#11 §6, plain):

> the circle |Z| = 1 is the mirror of the duality between our expanding universe and its contracting conjugate;

`papers/broken-born-checkpoint-v2.md` line 65 (#11 §6):

> **ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹, which carries a to ã = 1/a by inversion in the circle |Z| = 1. The cosmological constraint a·ã = 1 (§10) holds along the whole slice X = 0, where it is det H = 1, and the circle meets the slice only at the self-dual vacuum Z = i.

`papers/broken-born-checkpoint-v2.md` line 105 (#11 §10, plain):

> Our expanding universe and its contracting conjugate are one motion written twice, like a number and its reciprocal — a relation forced by the constancy of Planck's constant, whose mirror is the |Z| = 1 circle of the modular field.

`papers/broken-born-checkpoint-v2.md` line 107 (#11 §10):

> **Constraint [D]:** ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — det H = 1, satisfied along the whole vacuum slice X = 0, where ρ maps a to ã = 1/a by inversion in the circle |Z| = 1.

`papers/broken-born-checkpoint-v2.md` line 217 (#11 App. A item 6):

> Conjugate universe shrinks as ours expands — **promoted to theorem** (a·ã = 1 from ℏ-rigidity; on the vacuum slice X = 0 it is det H = 1).

`notes/geometric-core.md` line 55 (#5 §C):

> The cosmological constraint a·ã = 1 holds along the whole slice X = 0 (it is det H = 1), where Z → −Z⁻¹ carries a to ã = 1/a by inversion in the |Z| = 1 self-dual circle; the circle meets the slice only at Z = i — the minisuperspace duality was the shadow of this modular action.

`notes/geometric-core.md` line 58 (#5 §C): No change. At d = 1 on the slice X = 0, |Z| = Y = a², and the duality inverts it, since ρ(iY) = i/Y (audit). The line names the variable that the duality acts on, not the locus. It is listed here because the first auditor listed it.

`notes/geometric-core.md` line 82 (#5 §F):

> the modular unification (reciprocity = Z → −Z⁻¹, cosmological duality = inversion in |Z| = 1).

`notes/broken-born-theory.md` line 283 (#1 v0.3):

> Born reciprocity = Z → −Z⁻¹ with self-dual point Z = i, and the cosmological constraint a·ã = 1 as det H = 1 along the vacuum slice X = 0, which the self-dual circle |Z| = 1 meets only at Z = i.

`notes/broken-born-program-v1.md` line 44 (#9 §4, plain):

> the self-dual point Z = i is the vacuum, the circle |Z| = 1 is the mirror of the cosmological duality between our expanding universe and its contracting conjugate, and dark energy lives on the boundary of the domain as a phase.

`notes/broken-born-program-v1.md` line 50 (#9 §4):

> At X = 0 it sends g → g⁻¹: scale-factor duality, by inversion in the circle |Z| = 1. The minisuperspace constraint a·ã = 1 (§8) holds along the whole slice X = 0 (it is det H = 1), which the circle meets only at Z = i.

`notes/broken-born-program-v1.md` line 86 (#9 §8, plain):

> Our expanding universe and its contracting conjugate are one motion described twice — like a number and its reciprocal — a relation that turns out to be forced by the constancy of Planck's constant, and to have the |Z| = 1 circle of the modular field as its mirror.

`notes/broken-born-program-v1.md` line 88 (#9 §8):

> **The constraint [D].** ω-rigidity fixes the comoving phase-space cell: a·ã = 1. Not an assumption — the statement that ℏ does not run; geometrically, det H = 1 along the whole vacuum slice X = 0, where ρ maps a to ã = 1/a by inversion in the |Z| = 1 self-dual locus.

`HANDOFF.md` line 19 (§2):

> Modular field Z = X + iY on Siegel domain Sp(2d,R)/U(d); Im Z = metric, Re Z = X = momentum graviton; reciprocity = Z → −1/Z; a·ã = 1 holds on the whole slice X = 0 (det H = 1), which the |Z|=1 circle meets only at Z = i; dark energy τ = Maslov phase of the Shilov boundary Λ(4) ✓ (parametrization identities)

**If accepted, also:**

- Wiki pages (25). Of these, 23 discuss the statement. `wiki/_index.md` uses "see flag 23" as its example of a flag pointer and would need another example. The `wiki/history/timeline.md` row ("Flags 7 and 23 extended") is history and stays. The pages are `wiki/_index.md`, `wiki/cosmology/_index.md`, `wiki/cosmology/scale-factor-duality/_index.md`, `wiki/cosmology/scale-factor-duality/cosmological-constraint.md`, `wiki/cosmology/scale-factor-duality/phase-space-diameter.md`, `wiki/glossary.md`, `wiki/history/main-problems.md`, `wiki/history/documents/checkpoint.md`, `wiki/history/documents/field-equation-notes.md`, `wiki/history/documents/handoff.md`, `wiki/history/documents/lab-notebook.md`, `wiki/history/documents/source-conflicts.md`, `wiki/history/timeline.md`, `wiki/notation.md`, `wiki/phase-space/modular-field/_index.md`, `wiki/phase-space/modular-field/modular-field-z.md`, `wiki/phase-space/modular-field/modular-inversion.md`, `wiki/phase-space/modular-field/siegel-domain.md`, `wiki/predictions/fate-of-expansion.md`, `wiki/program/conjugate-universe.md`, `wiki/program/founding-suppositions.md`, `wiki/program/postulates/original-p2.md`, `wiki/program/postulates/p3-reciprocity.md`, `wiki/status/alive.md` and `wiki/status/open-problems.md`. The requested grep misses the 8 pages that cite "item 23" or "Flag 23".
- Executed check: the obvious candidate is part 3 of `review/wiki-build-checks/self_dual_locus.py`, but its "|Z| = 1 only at Y = 1" is a typed string, not a computed result (audit). A `verify/` version should be based on `review/wiki-build-checks/audit/flag23_readings.py` and `flag23_independent.py`. It would assert:
  - at X = 0, H_Z = diag(Y, Y⁻¹), with det H_Z = 1;
  - a·ã = 1 for every Y > 0, with a² = Im Z and ã² = the momentum block;
  - solving |Z| = 1 on that slice gives only Y = 1;
  - ρ(iY) = i/Y.

  The independent anchors are textbook facts: the Siegel action (AZ + B)(CZ + D)⁻¹ with H_{M·Z} = M H_Z Mᵀ, det M = 1 for a symplectic matrix, and −1/z as a reflection composed with inversion in |z| = 1. Part 1 of the same script could go in with it; it checks the dictionary w_eff = −w̃ against the falsified −2 − w̃. The scripts print without asserting, so the port needs assertions before it is wired into `scripts/check.sh`.
- Also:
  - #11 would become v2.3.
  - `HANDOFF.md` §2's line ends in "✓ (parametrization identities)". Battery T2 checks det H = 1, but no `verify/` script tests the |Z| = 1 identification (audit), so the ✓ never covered it.
  - `HANDOFF.md`, #1, #5 and #9 have not been edited since the import. Paul can choose between editing them in place and adding a dated note.
  - Nothing downstream changes. The dictionary and the turnaround use ã = 1/a for every a, which is the axis reading (audit).
  - Flag 3 concerns the same circle: at d = 1 the misalignment potential vanishes on the whole circle. Ruling the two flags together keeps their wording consistent.
  - The flag's entry in `review/wiki-build-flags.md` needs updating.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 39: Two actions of ρ on the spin-2 sector

**Audit:** depends on a convention or reading (both of 2 checks)

**Where it appears:** The parity statements below hold under the frame exchange g ↔ f, and not under §6's Z → −Z⁻¹ if the graviton is the fluctuation of Im Z (audit).

- `notes/beta-coefficients.md` line 34 (#8 §3)
- `papers/broken-born-checkpoint-v2.md` line 81 (#11 §7.5)
- `papers/broken-born-checkpoint-v2.md` line 169 (#11 §13, row 6)
- `notes/broken-born-program-v1.md` line 64 (#9 §5 item 6)
- `notes/broken-born-program-v1.md` line 103 (#9 §9, row 6)
- `notes/broken-born-program-v1.md` line 128 (#9 §11)
- `notes/broken-born-theory.md` line 305 (#1 addendum v0.6)

Each action is stated in several places, and neither option changes those sentences:

- The frame exchange: #8 §1 (line 7), #11 §7.3 (line 77), #9 §5 item 5 (line 63) and #1 v0.6 (line 305).
- The Möbius map Z → −Z⁻¹: #11 §6 (line 65), #5 §C (line 55), #9 §4 (line 50), #1 v0.3 (line 283) and `HANDOFF.md` §2 (line 19). It is also stated in #11's abstract (line 17), §6 plain-language passage (line 63) and §11.3 (line 119), #9's abstract (line 12) and §4 plain-language passage (line 44), #5 §F (line 82) and the toy note §2 (line 53).

X is odd under both actions (audit), so the statements that X is "reciprocity-odd", such as #11 line 83, are unaffected.

**Now reads:**

`notes/beta-coefficients.md` line 34 (#8 §3):

> **Eigenstates and parity:** the massless graviton is the reciprocity-**even** combination (e + f); X is reciprocity-**odd** (e − f). Reciprocity is a selection rule on vertices.

`papers/broken-born-checkpoint-v2.md` line 81 (#11 §7.5):

> Massless graviton = reciprocity-even (GW graviton-mass bounds satisfied identically); X = reciprocity-odd; SM couplings gravitational-strength and Yukawa-cut at 1/M_X; τ un-eaten (compact J-sector, not the Stückelberg sector).

`papers/broken-born-checkpoint-v2.md` line 169 (#11 §13, row 6, the BBT cell):

> Massless eigenstate exactly massless (reciprocity-even)

`notes/broken-born-program-v1.md` line 64 (#9 §5 item 6):

> Massless graviton = reciprocity-even (GW graviton-mass bounds satisfied identically); X = reciprocity-odd;

`notes/broken-born-program-v1.md` line 103 (#9 §9, row 6, the BBT cell):

> Massless eigenstate exactly massless (reciprocity-even); massive X short-range

`notes/broken-born-program-v1.md` line 128 (#9 §11):

> even-eigenstate masslessness as a bimetric-parity statement

`notes/broken-born-theory.md` line 305 (#1 v0.6):

> Spectrum: massless graviton = reciprocity-even, X = reciprocity-odd;

**Proposed:**

Option A names the action wherever a parity is stated and records the gap once, in #11 §7.5.

`notes/beta-coefficients.md` line 34 (#8 §3):

> **Eigenstates and parity** (reciprocity as the frame exchange of §1): the massless graviton is the reciprocity-**even** combination (e + f); X is reciprocity-**odd** (e − f). Reciprocity is a selection rule on vertices.

`papers/broken-born-checkpoint-v2.md` line 81 (#11 §7.5):

> Under reciprocity as the frame exchange of §7.3: massless graviton = reciprocity-even (GW graviton-mass bounds satisfied identically); X = reciprocity-odd. Under §6's ρ: Z → −Z⁻¹, which linearizes to −1 at Z = i, the metric fluctuation is odd as well; relating the two actions waits on the wedge reduction from S_H (§14 item 1) [O]. SM couplings gravitational-strength and Yukawa-cut at 1/M_X; τ un-eaten (compact J-sector, not the Stückelberg sector).

`papers/broken-born-checkpoint-v2.md` line 169 (#11 §13, row 6):

> Massless eigenstate exactly massless (reciprocity-even under the frame exchange, §7.3)

`notes/broken-born-program-v1.md` line 64 (#9 §5 item 6):

> Under the frame exchange of item 5, massless graviton = reciprocity-even (GW graviton-mass bounds satisfied identically); X = reciprocity-odd;

`notes/broken-born-program-v1.md` line 103 (#9 §9, row 6):

> Massless eigenstate exactly massless (reciprocity-even under the frame exchange); massive X short-range

`notes/broken-born-program-v1.md` line 128 (#9 §11): No change. "Bimetric-parity" already names the frame exchange.

`notes/broken-born-theory.md` line 305 (#1 v0.6): No change. The same paragraph's second sentence reads "Born reciprocity acts on the wedge sector as the frame exchange".

Option B makes no change anywhere. Each document that states a parity also states the frame exchange (#8 §1, #11 §7.3, #9 §5 item 5, #1 v0.6). The gap with §6's action would stay unrecorded in the documents, though the wiki records it.

The audit does not choose between them. Both checks find the parities right under the frame exchange, which the spin-2 sections state and the palindrome needs. Both find them wrong under §6's Möbius map if the graviton is δIm Z. Both leave the choice of action to the open wedge reduction (#11 §14 item 1). Both checks add that row 6's masslessness does not depend on the label; the first check gives the reason, V(g, g) = √det g · V(1) = 0. What depends on the label is "reciprocity-even" itself and #8 §3's "selection rule on vertices".

**If accepted, also:**

- Wiki pages (26). The five mentions in `wiki/history/timeline.md` are history and stay. The pages are `wiki/conjugate-relativity/equivalence-principle.md`, `wiki/dark-matter/candidates/x-condensate.md`, `wiki/glossary.md`, `wiki/gravity/momentum-graviton/_index.md`, `wiki/gravity/momentum-graviton/borns-answer.md`, `wiki/gravity/momentum-graviton/fifth-force-safety.md`, `wiki/gravity/momentum-graviton/gravitational-higgs.md`, `wiki/gravity/momentum-graviton/spectrum-and-parity.md`, `wiki/gravity/palindromic-branch/palindrome.md`, `wiki/gravity/palindromic-branch/vacuum-energy-identity.md`, `wiki/gravity/spin-2-fields/general-relativity.md`, `wiki/gravity/spin-2-fields/hassan-rosen-bimetric.md`, `wiki/gravity/tuning-test/constrained-bimetric.md`, `wiki/history/main-problems.md`, `wiki/history/documents/checkpoint.md`, `wiki/history/documents/field-equation-notes.md`, `wiki/history/documents/lab-notebook.md`, `wiki/history/timeline.md`, `wiki/phase-space/modular-field/field-content.md`, `wiki/phase-space/modular-field/modular-inversion.md`, `wiki/predictions/_index.md`, `wiki/predictions/massless-graviton.md`, `wiki/predictions/table-history.md`, `wiki/program/postulates/p3-reciprocity.md`, `wiki/status/alive.md` and `wiki/status/open-problems.md`. The requested grep misses `field-equation-notes.md` ("item 39") and `open-problems.md`.
- Executed check: under Option A, two scripts would move into `verify/`.
  - `review/wiki-build-checks/rho_parity.py` checks the Möbius side. It would assert that −Z⁻¹ linearized at Z = i is −(x + ih) for d = 1, 2 and 3, and that δY + δ(Y⁻¹) has no linear part. Its anchor is the textbook derivative d(−1/z)/dz = z⁻² = −1 at z = i.
  - The auditors' `review/wiki-build-checks/audit/bimetric_parity.py` checks the frame-exchange side. With palindromic βₙ, the Hassan–Rosen potential is swap-symmetric, the (u, u) direction is exactly massless, and the mass term sits on the (u, −u) direction. Its anchor is the Fierz–Pauli form Tr u² − (Tr u)² of the quadratic potential at a flat proportional background, which defines the dRGT/HR family.

  Both scripts print without asserting, so each needs assertions before it is wired into `scripts/check.sh`. Under Option B no check moves.
- Also:
  - Under Option A, #11 would become v2.3.
  - The flag was reworded after the audit. Its first text "said the documents do not state which action applies", and the audit found that they state both. The flag and the audit now agree.
  - The flag's entry in `review/wiki-build-flags.md` needs updating.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 3: The misalignment potential vanishes on a larger set than #7 states

**Audit:** confirmed (2 independent checks)

**Where it appears:**

1. `notes/tuning-test.md` line 26 (§2, consequence 1): the statement itself.
2. `notes/tuning-test.md` line 7 (§1): the definition the flag also cites. Both audits leave it as written: one calls it true, the other takes it as the definition that consequence 1 contradicts.

No other source states this zero set. #9 §4 (`notes/broken-born-program-v1.md` line 48) and #11 §6 (`papers/broken-born-checkpoint-v2.md` line 65) speak of "the η-compatible locus X = 0", and #5 §C (`notes/geometric-core.md` line 53) of "the η-compatible locus of Theorem A" at X = 0. That is Theorem A's notion, a different one, and neither audit proposes changing it.

**Now reads:**

(1) `notes/tuning-test.md` line 26:

> **The compatible locus is X = 0 *and* Y = Y⁻¹** (i.e. g pinned to the J-frame reference metric): the Higgs sector is inevitably a *two-tensor* potential V(g, X; reference) — a massive-gravity-type potential, confirming the structural landing point of Chunk A-ii from the opposite direction.

(2) `notes/tuning-test.md` line 7:

> The natural incompatibility measure is the anticommutator {J, I[Z]} (zero exactly on the compatible locus).

**Proposed:**

(1) Line 26, merging the two audits' wordings and cutting them to the minimum:

> **The compatible locus is [X, Y] = 0 *and* X² + Y² = 1** (ZZ̄ = 1: a d(d+1)/2-dimensional family through Z = i, tangent there to the X directions; at d = 1 the upper half of the circle |Z| = 1). Along it g is tied to X and the J-frame reference metric, to which it is pinned only on the slice X = 0 (Y = Y⁻¹): the Higgs sector is inevitably a *two-tensor* potential V(g, X; reference) — a massive-gravity-type potential, confirming the structural landing point of Chunk A-ii from the opposite direction.

Optional, line 27 (consequence 2). This records the flat direction that the flag and both audits name, in one audit's optional wording. Insert after "a graviton mass **without** the −(Tr h)² companion":

> — and no mass for x, which runs along the compatible locus

(2) Line 7: no change.

On the flag's question (is the degeneracy intended, and does it affect the vacuum claims?), the audits find:

- The degeneracy is structural, not a choice. One audit: every potential that is a function of {J₀, I[Z]} alone, vanishing only where {J₀, I[Z]} does, has this zero set, which is forced by the subgroup of Sp(2d) that commutes with J₀. The other: only adding X = 0, or the abandoned rigid η₀ of P2, cuts the set down to Z = i.
- It lies in the metric tier, which the program already rejects (one audit).
- Consequences 2 and 3 and the two-tensor conclusion stand (both audits).

Neither audit tested #8's frame-tier potential; one says so explicitly.

**If accepted, also:**

- Wiki pages (11):
  - `wiki/gravity/tuning-test/misalignment-potential.md`
  - `wiki/gravity/tuning-test/_index.md`
  - `wiki/gravity/momentum-graviton/gravitational-higgs.md`
  - `wiki/phase-space/modular-field/modular-field-z.md`
  - `wiki/phase-space/born-geometry/born-structures.md`
  - `wiki/method/verification/battery.md`
  - `wiki/method/verification/arithmetic-not-model.md`
  - `wiki/notation.md`
  - `wiki/history/documents/field-equation-notes.md`
  - `wiki/history/main-problems.md`
  - `wiki/status/open-problems.md`

  The task's grep finds 7 of these. The other 4 were found through the "Flag 3" and "items 1, 3, 4…" / "items 1, 3–8" forms, which that grep misses. Its 7 hits on "flagship" and on other numbered lists are excluded.

  `wiki/status/alive.md` has no flag-3 pointer, but its line 133, "the reading of their zero set has no test", changes if the check below moves into `verify/`.
- Executed check: `review/wiki-build-checks/zero_locus.py`, moved into `verify/` and wired into `scripts/check.sh`. At d = 4 it would assert:
  - {J₀, I[Z]} vanishes (≈ 2e-15) at a point with X ≠ 0, [X, Y] = 0 and X² + Y² = 1;
  - it does not vanish at X = 0 with generic Y (printed 19.3425).

  The independent anchor comes from the audit: the textbook Siegel action of the subgroup of Sp(2d) commuting with J₀ moves Z = i along an orbit of dimension d(d+1)/2 (10 at d = 4), and the orbit stays on the zero set. Scripts: `review/wiki-build-checks/audit/flag3_recompute.py` part 4 and `audit/b_numeric_anchor_and_readings.py`.
- Also:
  - No #11 change: §7.2 does not restate the locus.
  - Line 27 is also edited by flag 4. Merge the two edits if both are accepted.
  - The flag's entry in `review/wiki-build-flags.md`, and its place in "Where to start", records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 6: "By symmetry" overstates the vacuum-energy cancellation

**Audit:** confirmed (2 independent checks)

**Where it appears:**

The flag names #1 v0.6, #10, #11 §1, §7 and §7.3, #9 §5 and #8 §2's closing sentence. The two audits add the other places below; each is marked (flag), (both audits) or (one audit).

- #11, `papers/broken-born-checkpoint-v2.md`:
  - (1) line 15 (§1, plain-language passage) (flag)
  - (2) line 71 (§7, plain-language passage) (flag)
  - (3) line 77 (§7.3) (flag)
  - (4) line 83 (§7, "Born's answer") (both audits)
  - (5) line 107 (§10) (one audit)
  - (6) line 204 (§15, plain-language passage) (both audits)
- #8, `notes/beta-coefficients.md`:
  - (7) line 3 (status line) (both audits)
  - (8) line 29 (§2, closing sentence) (flag)
  - (9) line 41 (§4) (one audit)
- #1, `notes/broken-born-theory.md`:
  - (10) line 305 (Addendum v0.6) (flag)
  - (11) line 307 (Addendum v0.6) (both audits)
- #9, `notes/broken-born-program-v1.md`:
  - (12) line 10 (§0, plain-language passage) (both audits)
  - (13) line 55 (§5, plain-language passage) (flag)
  - (14) line 63 (§5 item 5) (flag)
  - (15) line 90 (§8) (one audit)
  - (16) line 126 (§11, plain-language passage) (one audit)
  - (17) line 128 (§11) (one audit)
- #10, `popsci/angle-of-the-mirror.md`:
  - (18) line 27 ("What refused to die") (flag; one audit names "wasn't ordered", the other the whole "twin turned out to be useful" passage)
- #12, `popsci/universes-other-half.md`:
  - (19) line 31 ("The second geometry, and why it has never been seen") (both audits)
  - (20) line 73 ("What one assumption purchases") (one audit)
- `HANDOFF.md`:
  - (21) line 57 (§3, row 8) (one audit)
- Optional, where the flag and the audits differ:
  - (22) #8 line 29 (§2): "two tunings in generic bimetric"
  - (23) #9 line 63 (§5 item 5): the same comparison

The audits judge these accurate as written, so they get no change:

- #8 line 29's bold sentence (the conditional "the existence of a flat aligned vacuum forces …");
- #11 line 17 and #9 line 12 (the technical abstracts);
- `HANDOFF.md` line 21 (§2);
- #11 line 79 (§7.4, where flatness "selects a different point").

#11 line 206, "an unsolicited identity (§7.3)", names the identity V(1) = 2T, not Λ = 0, so it is left alone.

**Now reads:**

(1) `papers/broken-born-checkpoint-v2.md` line 15:

> gravity acquires a hidden massive twin whose vacuum energy cancels by symmetry;

(2) `papers/broken-born-checkpoint-v2.md` line 71:

> X's entire contribution to the energy of empty space cancels exactly, by symmetry.

(3) `papers/broken-born-checkpoint-v2.md` line 77:

> *the wedge sector contributes zero cosmological constant, by symmetry.*

(4) `papers/broken-born-checkpoint-v2.md` line 83:

> its wedge vacuum energy zero by identity.

(5) `papers/broken-born-checkpoint-v2.md` line 107:

> §7.3 guarantees the wedge sector contributes nothing that competes with τ.

(6) `papers/broken-born-checkpoint-v2.md` line 204:

> the last one yielding a vacuum-energy cancellation nobody ordered

(7) `notes/beta-coefficients.md` line 3:

> Reciprocity fixes the potential's structure, cancels its vacuum energy by theorem, and cuts the free parameters from five to two.

(8) `notes/beta-coefficients.md` line 29:

> What was an assumption is now a theorem of the symmetry.

(9) `notes/beta-coefficients.md` line 41:

> two free parameters, vacuum energy exactly zero by the palindrome theorem,

(10) `notes/broken-born-theory.md` line 305:

> — the massive-gravity sector contributes zero cosmological constant, by symmetry rather than tuning, leaving dark energy entirely to τ as the cosmology chapter had assumed.

(11) `notes/broken-born-theory.md` line 307:

> its vacuum energy zero by theorem.

(12) `notes/broken-born-program-v1.md` line 10:

> that twin's contribution to the energy of empty space cancels exactly by symmetry,

(13) `notes/broken-born-program-v1.md` line 55:

> by a four-line theorem, X's entire contribution to the energy of empty space cancels exactly. A cosmological-constant cancellation for free, from symmetry.

(14) `notes/broken-born-program-v1.md` line 63:

> *the massive sector's vacuum energy is zero by symmetry.*

(15) `notes/broken-born-program-v1.md` line 90:

> §5's Λ theorem guarantees the massive-gravity sector contributes nothing to compete with τ.

(16a) `notes/broken-born-program-v1.md` line 126:

> and the last one yielded a cosmological-constant cancellation nobody ordered.

(16b) `notes/broken-born-program-v1.md` line 126:

> and the palindrome theorem cancelling the symmetric-bimetric vacuum energy

(17) `notes/broken-born-program-v1.md` line 128:

> an unsolicited theorem (Λ_wedge = 0);

(18a) `popsci/angle-of-the-mirror.md` line 27:

> Zero, by symmetry rather than by the fine-tuning such theories normally require.

(18b) `popsci/angle-of-the-mirror.md` line 27:

> so a cancellation that falls out unbidden made for a good evening.

(18c) `popsci/angle-of-the-mirror.md` line 27:

> Either way it wasn't ordered; it arrived.

(19a) `popsci/universes-other-half.md` line 31:

> a short calculation shows that, under this pattern, the field's contribution to the energy density of empty space cancels exactly.

(19b) `popsci/universes-other-half.md` line 31:

> either way, it is a consequence of the symmetry, not an assumption fed in.

(20) `popsci/universes-other-half.md` line 73:

> The quietness of empty space, at least as concerns that field: the palindromic cancellation.

(21) `HANDOFF.md` line 57:

> V(1) = 2T ⇒ Λ_wedge = 0

(22) `notes/beta-coefficients.md` line 29:

> — one condition does the work that takes two tunings in generic bimetric gravity.

(23) `notes/broken-born-program-v1.md` line 63:

> One condition does what generic bimetric needs two tunings for:

**Proposed:**

Every replacement below rests on the same audited statement. Under the palindrome V(1) = 2T holds identically. A flat aligned vacuum needs one condition on the βₙ, T = 0 (β₀ = −4β₁ − 3β₂), which the symmetry does not impose. Given that condition, V(1) = 0 too. The phrases "once one condition … is imposed" and "which the palindrome (symmetry) makes sufficient but does not supply" are the audits' own.

(1)

> gravity acquires a hidden massive twin whose vacuum energy cancels once one condition on its couplings is imposed;

(2)

> X's entire contribution to the energy of empty space cancels exactly once one condition on its couplings is imposed.

(3)

> *the wedge sector contributes zero cosmological constant, given the one condition T = 0, which the symmetry makes sufficient but does not supply.*

(4)

> its wedge vacuum energy zero by identity once one condition (T = 0) holds.

(5)

> Given its one condition (T = 0), §7.3 guarantees the wedge sector contributes nothing that competes with τ.

(6) This sentence is also edited by flag 7; merge if both are accepted.

> the last one yielding a vacuum-energy identity nobody ordered

(7)

> Reciprocity fixes the potential's structure, cancels its vacuum energy by theorem given one condition (T = 0), and cuts the free parameters from five to two.

(8)

> What was an assumption is now a theorem of the symmetry plus one condition on the βₙ (T = 0).

(9)

> two free parameters, vacuum energy exactly zero by the palindrome theorem given one condition (T = 0),

(10)

> — the massive-gravity sector contributes zero cosmological constant at the cost of one condition on the βₙ (T = 0, i.e. β₀ = −4β₁ − 3β₂), which the palindrome makes sufficient but does not supply, leaving dark energy entirely to τ as the cosmology chapter had assumed.

(11)

> its vacuum energy zero by theorem given one condition on the βₙ (T = 0).

(12)

> that twin's contribution to the energy of empty space cancels exactly once one condition on its couplings is imposed,

(13)

> by a four-line theorem, X's entire contribution to the energy of empty space cancels exactly once one condition on its couplings is imposed. A cosmological-constant cancellation at the price of a single condition, which the symmetry makes sufficient but does not supply.

(14)

> *the massive sector's vacuum energy is zero given that one condition (T = 0), which the symmetry makes sufficient but does not supply.*

(15)

> Given its one condition (T = 0), §5's Λ theorem guarantees the massive-gravity sector contributes nothing to compete with τ.

(16a) This passage is also edited by flag 7; merge if both are accepted.

> and the last one yielded a cosmological-constant identity nobody ordered.

(16b)

> and the palindrome theorem cancelling the symmetric-bimetric vacuum energy given one condition

(17)

> an unsolicited theorem (V(1) = 2T, so Λ_wedge = 0 given T = 0);

(18a)

> Zero, once a single condition on the twin's couplings is imposed — the symmetry makes that one condition enough, but does not supply it.

(18b)

> so an identity that falls out unbidden made for a good evening.

(18c)

> Either way the identity wasn't ordered; it arrived.

(19a)

> a short calculation shows that, under this pattern and one further condition on the couplings, the field's contribution to the energy density of empty space cancels exactly.

(19b)

> either way, it is a consequence of the symmetry together with one condition on the couplings, which the symmetry makes sufficient but does not supply.

(20)

> The quietness of empty space, at least as concerns that field: the palindromic cancellation, given one condition on the field's couplings.

(21)

> V(1) = 2T ⇒ Λ_wedge = 0 given flatness (T = 0)

(22) and (23) are optional. Here the flag and the audits differ:

- The flag calls #8 §2's wording "the accurate one".
- Both audits add that "two tunings in generic bimetric" holds only when the generic theory must have g = f exactly. With the ratio of the two metrics free, generic bimetric also needs only one condition (`review/wiki-build-checks/audit/flag6_audit.py` part F; `audit/flag6_recompute.py` part E).
- The wording is from the recompute audit.

(22)

> — one condition does the work that takes two conditions in generic bimetric gravity when g = f is required.

(23)

> One condition does what generic bimetric needs two conditions for when g = f is required:

**If accepted, also:**

- Wiki pages (13):
  - `wiki/gravity/palindromic-branch/vacuum-energy-identity.md`
  - `wiki/gravity/spin-2-fields/cosmological-constant-problem.md`
  - `wiki/cosmology/dark-energy/cosmological-constant.md`
  - `wiki/predictions/dark-energy-drift.md`
  - `wiki/program/assessment.md`
  - `wiki/history/documents/checkpoint.md`
  - `wiki/history/documents/field-equation-notes.md`
  - `wiki/history/documents/lab-notebook.md`
  - `wiki/history/documents/popular-articles.md`
  - `wiki/history/main-problems.md`
  - `wiki/history/timeline.md` (build-history rows, which stay as they are; the ruling adds a row)
  - `wiki/status/superseded.md`
  - `wiki/status/open-problems.md`

  The task's grep finds 4 of these. Its hit on `wiki/conjugate-relativity/invariant-length-shell.md` concerns #6, not flag 6, and is excluded.

  Eight more pages have no flag-6 pointer but quote wording that the edits above change or qualify:
  - `wiki/gravity/momentum-graviton/borns-answer.md` lines 49, 53, 67 and 100: (4), (9), (11), (16b);
  - `wiki/gravity/palindromic-branch/palindrome.md` line 97: (4);
  - `wiki/program/founding-suppositions.md` line 106: (4);
  - `wiki/cosmology/dark-energy/tau-quintessence.md` line 114: (5);
  - `wiki/cosmology/dark-energy/no-phantom-bound.md` line 45: (5);
  - `wiki/gravity/palindromic-branch/pm-comparison.md` line 113: (13);
  - `wiki/gravity/momentum-graviton/symplectic-partner.md` line 117: (16b);
  - `wiki/notation.md` line 207: (17).

  Two state the cancellation without its condition in the wiki's own words ("adds no vacuum energy"): `wiki/cosmology/dark-energy/_index.md` line 41 and `tau-quintessence.md` line 170. If (21) is accepted, `wiki/history/documents/handoff.md` line 184, which lists the flags that concern the handoff, also gains flag 6.
- Executed check: none required for the wording. If gated, a `verify/` script would assert three facts the audits executed:
  - flatness adds exactly one condition beyond the palindrome: rank 2 becomes rank 3, leaving two free βₙ (`review/wiki-build-checks/audit/flag6_recompute.py` part B; `audit/flag6_audit.py` part D);
  - Λ of the aligned vacuum equals T, and T is not identically zero on the palindromic family (`flag6_audit.py` parts D–E);
  - the palindromic partially-massless point has T = 6β₂ (`flag6_recompute.py` part C).

  Independent anchors from the audit: the exchange identity √det f·eₙ(√(f⁻¹g)) = √det g·e₄₋ₙ(√(g⁻¹f)) (max relative error 8.82e-16), and G_μν(c²g) = G_μν(g) (`flag6_audit.py` parts A–B). Battery T5 (V(1) = 2T) is unaffected.
- Also:
  - #11 needs a changelog line covering §1, §7, §7.3, §10 and §15; with the other #11 edits, a v2.3.
  - #11 line 204 and #9 line 126 are shared with flag 7.
  - The documents can be ruled separately:
    - #1 and #9 are superseded;
    - #10 and #12 are popular articles;
    - HANDOFF is the move-in snapshot.
  - The queued partially-massless comparison (root `CLAUDE.md` queue item 1; #11 §14 item 2) examines this identity and would start from the corrected wording.
  - The flag's entry in `review/wiki-build-flags.md`, and its place in "Where to start", records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 1: The "discrete" polarizations under strict P2

**Audit:** confirmed (2 independent checks)

**Where it appears:**

- `notes/geometric-core.md` line 27 (#5 §B)
- `papers/broken-born-checkpoint-v2.md` line 57 (#11 §5)
- `notes/broken-born-program-v1.md` line 40 (#9 §3)
- `notes/broken-born-theory.md` line 281 (#1 addendum v0.3). The flag does not list this place; the first auditor found it.

**Now reads:**

`notes/geometric-core.md` line 27 (#5 §B):

> The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is **discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**. The dark-energy sector as constructed contradicts P2.

`papers/broken-born-checkpoint-v2.md` line 57 (#11 §5):

> Under strict P2 the compatible polarizations are discrete, so no Grassmannian, no Maslov circle, no dark-energy field, and S_H is a functional of g alone: **nontriviality theorem** — the program has content iff η is emergent.

`notes/broken-born-program-v1.md` line 40 (#9 §3):

> Under strict P2 the space of compatible polarizations is discrete (the 2^d coordinate splittings), so there is no Grassmannian, no Maslov circle, no τ — no dark-energy sector — and S_H is a functional of g alone.

`notes/broken-born-theory.md` line 281 (#1 addendum v0.3):

> and with it an axiom-level inconsistency: strict P2 makes the polarization choice discrete, eliminating the Lagrangian Grassmannian, the Maslov circle, and hence the entire τ/dark-energy sector, while also slaving g̃ = g⁻¹ and removing any geometric origin for the χ gate.

**Proposed:** The wording comes from the two auditors' suggestions and changes only the description of the set. The conclusion stands as the flag and both audits give it: det² is constant on each family and the x-polarization is isolated, so there is no Maslov circle and no τ under strict P2. The rest of each sentence, the nontriviality theorem included, stays as written.

`notes/geometric-core.md` line 27 (#5 §B):

> The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is the set of splittings V ⊕ V^⊥ (V in x-space, V^⊥ in p-space): d + 1 Grassmannians Gr(k, d), continuous for 0 < k < d, with det² = (−1)^(d−k) constant on each and the x-polarization isolated. No Lagrangian Grassmannian, no Maslov circle, **no τ field**. The dark-energy sector as constructed contradicts P2.

`papers/broken-born-checkpoint-v2.md` line 57 (#11 §5):

> Under strict P2 the compatible polarizations carry a constant Maslov phase (det² = ±1 on each of their families), with the x-polarization isolated, so no Lagrangian Grassmannian, no Maslov circle, no dark-energy field, and S_H is a functional of g alone: **nontriviality theorem** — the program has content iff η is emergent.

`notes/broken-born-program-v1.md` line 40 (#9 §3):

> Under strict P2 the space of compatible polarizations carries a constant Maslov phase (det² = ±1 on each of its families, the x-polarization isolated), so there is no Lagrangian Grassmannian, no Maslov circle, no τ — no dark-energy sector — and S_H is a functional of g alone.

`notes/broken-born-theory.md` line 281 (#1 addendum v0.3):

> and with it an axiom-level inconsistency: strict P2 freezes the polarization's Maslov phase, eliminating the Lagrangian Grassmannian, the Maslov circle, and hence the entire τ/dark-energy sector, while also slaving g̃ = g⁻¹ and removing any geometric origin for the χ gate.

The second auditor also allows a narrower edit of #11 §5 alone: keep "discrete" and say that it means the eigen-splitting of K = η⁻¹ω, which is discrete (two polarizations). #5 and #9, which say "the 2^d coordinate splittings", need the wording above either way.

**If accepted, also:**

- Wiki pages (18). The list comes from the requested grep plus the "Flag 1" and "item 1" forms it misses; its hits on "flagship", "flags 1–42" and stray numerals after "flags" (such as "1.3×10¹¹") are not about flag 1 and are left out. The pages are `wiki/cosmology/dark-energy/tau-quintessence.md`, `wiki/gravity/tuning-test/geometric-action.md`, `wiki/history/main-problems.md`, `wiki/history/documents/checkpoint.md`, `wiki/history/documents/field-equation-notes.md`, `wiki/history/documents/lab-notebook.md`, `wiki/phase-space/born-geometry/compatibility-corollaries.md`, `wiki/phase-space/born-geometry/compatibility-theorem.md`, `wiki/phase-space/modular-field/_index.md`, `wiki/phase-space/modular-field/lagrangian-grassmannian.md`, `wiki/phase-space/reciprocity/lagrangian-polarizations.md`, `wiki/predictions/photon-dispersion.md`, `wiki/program/hard-core.md`, `wiki/program/postulates/_index.md`, `wiki/program/postulates/nontriviality-theorem.md`, `wiki/program/postulates/original-p2.md`, `wiki/status/open-problems.md` (its pending-rulings line) and `wiki/symmetry-breaking/rho-preserving-potential.md`.
- Executed check: `review/wiki-build-checks/verifier_null_lagrangians.py` covers only d = 2 and 3, at H = 1, along one path per family (audit). The auditors' `review/wiki-build-checks/audit/flag1_recompute.py` and `flag1_audit.py` add d = 4, show that the set holds nothing else, and show that the x-polarization is isolated. A `verify/` version would assert three things:
  - ω and η vanish on V ⊕ V^⊥ for random V at d = 2, 3 and 4;
  - at each coordinate splitting the tangent dimension of the solution set is k(d − k), which is 0 at the x-polarization;
  - det² = (−1)^(d−k) holds on every member of each family.

  The independent anchor is the textbook dimension k(d − k) of Gr(k, d), with dim Λ(d) = d(d + 1)/2 as the control. The scripts print their results without asserting them, so the port needs assertions before it is wired into `scripts/check.sh`.
- Also:
  - #11 would become v2.3. Its header lists each version's changes, and amended passages carry an inline label such as "*Attribution (v2.1):*".
  - #5, #9 and #1 have not been edited since the import (commit 008c3ee). Paul can choose between editing them in place and adding a dated erratum line.
  - The flag's entry in `review/wiki-build-flags.md` needs updating. `HANDOFF.md` does not make this statement, so it needs no change.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 33: The soliton-obituary script claims more coverage than it has

**Audit:** confirmed (1 independent check)

**Where it appears:**
1. `verify/soliton_obituary.py` lines 3–5 (docstring).
2. `verify/soliton_obituary.py` line 114 (the closing line printed on success).
3. `review/round3-adjudication.md` lines 12–13 (header list).
4. `review/round3-adjudication.md` lines 150–153 (Decisions, "Executed the same day"). The claim itself is on lines 151–152.

The audit proposes no change to four related lines:
- `verify/soliton_obituary.py` line 14 ("What is checked here is the corrected record."). The audit notes that "the corrected record" includes ruling 6's ≳ 20–30 MeV, which is not checked, but offers no wording for this line.
- `notes/knot-dark-matter-standalone.md` line 3 (#14's banner: "The corrected numbers are in [review/round3-adjudication.md](../review/round3-adjudication.md), checked by `verify/soliton_obituary.py`."). The banner's preceding sentences name the Kibble normalization, the mass band, the benchmark and the ψ relic window. The script checks the corrected figures for all four. The audit notes that the banner, like line 14 and adjudication line 12, says "corrected" of a record that still contains ruling 6's ≳ 20–30 MeV, which is not checked; it offers no wording for the banner.
- Root `CLAUDE.md` line 27 (Layout: "`soliton_obituary.py` (the round-3 record)"). The audit read the file and proposes no change; flag 38 concerns the same line for another reason.
- `papers/broken-born-checkpoint-v2.md` line 154 (#11 §12, "The [V] numbers here are gated"). The audit finds this accurate: all 4 of the [V] numbers are gated.

**Now reads:**
1. `verify/soliton_obituary.py` lines 3–5:
> soliton_obituary.py — every number that review/round3-adjudication.md and the
> §12 obituary of papers/broken-born-checkpoint-v2.md (v2.1) quote
> for the withdrawn soliton candidate (#14 v3), recomputed and checked.
2. `verify/soliton_obituary.py` line 114:
> print("\nOK — every number the round-3 record quotes reproduces.")
3. `review/round3-adjudication.md` lines 12–13:
>   The corrected inputs now live in `verify/soliton_obituary.py`, which checks
>   every number this record quotes.
4. `review/round3-adjudication.md` lines 150–153:
> - `verify/knot_numbers.py` (v3's claims) was replaced by
>   `verify/soliton_obituary.py`, which checks every number this record
>   quotes, with independent anchors. The v3 checks are in history at
>   96f58da.

**Proposed:** The audit counts six computed figures that the record quotes for the candidate and the script never recomputes:
- the referee's Kibble–Zurek range (ruling 3);
- the referee's Boltzmann ranges (ruling 4);
- ruling 6's ≳ 20–30 MeV;
- α_m ≈ 34 (ruling 10);
- ε ~ 1e-7–1e-6 (the omitted-constraints list);
- "within ×1.6" (ruling 4).

1. `verify/soliton_obituary.py` lines 3–5 (the audit's wording, rewrapped):
> soliton_obituary.py — the figures review/round3-adjudication.md computes
> itself (rulings 1, 2, 4, 5; the lesson-2 anchors) and every [V] number of the
> §12 obituary of papers/broken-born-checkpoint-v2.md (v2.1), for the withdrawn
> soliton candidate (#14 v3), recomputed and checked. Not recomputed here:
> figures the record quotes from the referee or the literature, or accepts
> without re-checking (rulings 3, 6, 9, 10; the omitted-constraints list), and
> its 'within ×1.6' comparison.
2. `verify/soliton_obituary.py` line 114:
> print("\nOK — the adjudicator's recomputed round-3 figures and the §12 [V] numbers reproduce.")
3. `review/round3-adjudication.md` lines 12–13:
>   The corrected inputs now live in `verify/soliton_obituary.py`, which checks
>   the figures this record recomputes (rulings 1, 2, 4, 5) and #11 §12's [V]
>   numbers.
4. `review/round3-adjudication.md` lines 150–153:
> - `verify/knot_numbers.py` (v3's claims) was replaced by
>   `verify/soliton_obituary.py`, which checks the figures this record
>   recomputes (rulings 1, 2, 4, 5) and #11 §12's [V] numbers, with
>   independent anchors. The v3 checks are in history at 96f58da.

Places 2–4 differ from the audit's wording by one word each. Place 2 adds "recomputed" to the audit's "the adjudicator's round-3 figures"; places 3 and 4 have "recomputes" where the audit has "computes itself". The reason is that ruling 4's "within ×1.6" is a figure the record computes itself, and it is not checked; place 1 can keep "computes itself" because it lists the ×1.6 as an exception. The audit's inventory finds the coverage complete, 21 of 21, exactly for "the adjudicator's recomputed figures plus the §12 [V] numbers".

**If accepted, also:**
- Wiki pages (13). The search matched "flag 33", "Flag 33", "item(s) 33" and lists or ranges such as "33–34": `wiki/dark-matter/candidates/soliton-candidate/_index.md`, `wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic.md`, `wiki/glossary.md`, `wiki/method/review/review-protocol.md`, `wiki/method/review/round-3/arbitration.md`, `wiki/method/review/round-3/decisions.md`, `wiki/method/review/round-3/rulings.md`, `wiki/method/verification/_index.md`, `wiki/method/verification/arithmetic-not-model.md`, `wiki/method/verification/soliton-obituary-script.md`, `wiki/method/verification/the-gate.md`, `wiki/status/open-problems.md`, `wiki/status/superseded.md`.
- Executed check: none, because this is wording only. The script's 16 checks are unchanged and must still pass in `scripts/check.sh`.
- Also:
  - The flag's fourth item, "the surviving benchmark arithmetic (flux, densities, σ_T/M)", quotes no number in the record ("What survives v3", line 92), so the audit does not count it. The predecessor `knot_numbers.py` (96f58da) gated those three; the current script does not.
  - The other way to make the claim true would be to add checks for the six figures. The audit did not propose this. If it is chosen, note one detail from the audit: "within ×1.6" holds against the referee's unrounded 28.3 GeV (ratio 1.597) but not against the rounded 28 (1.614).
  - The same docstring is edited by flag 34, and the same adjudication file by flag 21, so these edits can go together.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 34: The script calls typed-in constants "PDG and Planck 2018 values"

**Audit:** confirmed (1 independent check)

**Where it appears:**
1. `verify/soliton_obituary.py` line 20 (docstring). The constants themselves are hard-coded at lines 32–38.

**Now reads:**
1. `verify/soliton_obituary.py` line 20:
> 5.43-5.45. Reference constants: PDG and Planck 2018 values.

   For comparison, the caveat that was dropped, from `96f58da:verify/knot_numbers.py` lines 27–28 (the predecessor, no longer in `verify/`; an identical copy is `review/wiki-build-checks/audit/knot_numbers_96f58da.py`):
> bracketed, not computed. Reference constants (PDG, Planck 2018) are from
> model memory except the N_eff bound (Planck 2018 VI, live-checked).

**Proposed:**
1. `verify/soliton_obituary.py` line 20 (the audit's wording, wrapped to two lines):
> 5.43-5.45. Reference constants: PDG and Planck 2018 values, typed in from
> model memory except the N_eff bound (Planck 2018 VI, live-checked).

**If accepted, also:**
- Wiki pages (7). The search matched "flag 34", "Flag 34", "item(s) 34" and lists or ranges such as "33–34": `wiki/cosmology/early-universe/cosmic-microwave-background.md`, `wiki/dark-matter/candidates/soliton-candidate/overproduction.md`, `wiki/gravity/spin-2-fields/planck-units.md`, `wiki/method/review/round-3/arbitration.md`, `wiki/method/verification/soliton-obituary-script.md`, `wiki/references.md`, `wiki/status/open-problems.md`.
- Executed check: none, because this is wording only and the values are unchanged.
- Also:
  - Flag 33 edits the same docstring, so apply the two together.
  - The audit notes that S0 = 2891.2 matches the round-3 referee's "PDG 2024 astro" value (`review/round3/referee/audit-notes.md` line 94). But the script cites no retrieval.
  - Retrieving the constants by live search would be a stronger fix. The audit did not propose it.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 42: A requested comparison recorded as applied

**Audit:** confirmed (1 independent check)

**Where it appears:**

- (1) `review/round4-adjudication.md` line 66 (the heading of 'Revisions for v2 of the note').
- (2) `notes/toy-lagrangian.md` line 507 ('Write-up and review (2026-10-19/20)'). Its list, lines 508–521, names no comparison.
- (3) `papers/broken-born-checkpoint-v2.md` line 198 (#11 §14 item 11). The audit says the same qualifier belongs here.
- (4) `CLAUDE.md` line 19 (Layout). The audit says the same qualifier belongs here.

The facts:

- Revision 4 (`review/round4-adjudication.md` lines 85–87) asks v2 to "compare with Langmann–Szabo–Zarembo".
- v2 §4 (`papers/reciprocity-toy-models.md` line 103) says: "The exact solution of the related model [8] is the natural independent check. We have not carried it out." Reference [8] is Langmann–Szabo–Zarembo (line 189).
- The flag's quoted "not carried out" paraphrases v2's actual words, "We have not carried it out" (an audit note).

**Now reads:**

(1) `review/round4-adjudication.md` line 66:

> ## Revisions for v2 of the note (all accepted; applied 2026-10-20 in commit 6606734)

(2) `notes/toy-lagrangian.md` line 507:

> - **v2 applies every accepted revision:**

(3) `papers/broken-born-checkpoint-v2.md` line 198 (excerpt):

> Round-4 blind review: verdict B; v2 applies the accepted revisions.

(4) `CLAUDE.md` line 19:

> - `reciprocity-toy-models.md` — the toy-Lagrangian note: two models of spontaneously broken ρ. Blind-review format. Round 4: B; v2 applies the revisions. The worklog is `notes/toy-lagrangian.md`.

**Proposed:**

(1) The audit's wording:

> ## Revisions for v2 of the note (all accepted; applied 2026-10-20 in commit 6606734, except revision 4's comparison with Langmann–Szabo–Zarembo, which v2 §4 records as not carried out)

(2) The audit's wording:

> - **v2 applies every accepted revision except the Langmann–Szabo–Zarembo comparison (revision 4), which v2 §4 names as the natural independent check and has not carried out:**

(3) The same qualifier. The audit gives no exact text for this place.

> Round-4 blind review: verdict B; v2 applies the accepted revisions except revision 4's comparison with Langmann–Szabo–Zarembo, which it has not carried out.

(4) The same qualifier. The audit gives no exact text for this place.

> - `reciprocity-toy-models.md` — the toy-Lagrangian note: two models of spontaneously broken ρ. Blind-review format. Round 4: B; v2 applies the revisions except revision 4's comparison with Langmann–Szabo–Zarembo, which it has not carried out. The worklog is `notes/toy-lagrangian.md`.

**If accepted, also:**

- Wiki pages (10):
  - `wiki/history/documents/checkpoint.md`
  - `wiki/history/documents/project-instructions.md`
  - `wiki/method/review/_index.md`
  - `wiki/method/review/review-protocol.md`
  - `wiki/method/review/round-4.md`
  - `wiki/program/assessment.md`
  - `wiki/status/open-problems.md`
  - `wiki/symmetry-breaking/toy-models/_index.md`
  - `wiki/symmetry-breaking/toy-models/acceptance-criterion.md`
  - `wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration.md`

  `wiki/history/timeline.md` lines 174 and 177 name flag 42 in dated commit rows, which are history and need no edit.

  Three more pages quote the adjudication heading word for word in their frontmatter `sources`, without citing the flag. These are `wiki/method/verification/monte-carlo-error-bars.md`, `wiki/method/verification/reduced-model-stability.md` and `wiki/status/superseded.md`; `acceptance-criterion.md` does the same. `scripts/check-wiki.py` checks only that a source file exists, so after a heading change these quotes would be stale without failing the gate.
- Executed check: none (wording only). The audit's `review/wiki-build-checks/audit/flag42_check.py` checks the documents and the git history, not physics.
- Also:
  - Change (3) edits #11, so #11's header needs a line under "v2.2 changes", or a v2.3 note.
  - `CLAUDE.md` holds Paul's own instructions, so any edit there is his call.
  - Optional, beyond the audit's wording: no list of open ends names the comparison. The audit checked v2 §6 "Not shown", root `CLAUDE.md` "Its open ends" and #11 §14 item 11 "Still open". Adding it to those lists would be a separate choice.
  - Flags 41 and 42 share a bullet ("42, 41", the ninth) in the "Where to start" list of `review/wiki-build-flags.md`.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 41: Restoration listed as shown by executed code

**Audit:** confirmed (1 independent check)

**Where it appears:**

- (1) `papers/reciprocity-toy-models.md` line 159 and line 165 (§6, "Shown (each by executed code)", item 5).
- The tags elsewhere already match the audit:
  - `notes/toy-lagrangian.md` line 297 tags the result [D], "by an exact argument", with only its premise gated (line 300);
  - §4 (lines 95–103) gives the argument with no script pointer.

**Now reads:**

(1) `papers/reciprocity-toy-models.md` line 159:

> **Shown** (each by executed code):

`papers/reciprocity-toy-models.md` line 165:

> - Model II: complex fields — classical breaking along a flat polarization angle, and restoration under quantization.

**Proposed:**

(1) Leave the heading at line 159 unchanged. Replace line 165 with the audit's wording:

> - Model II: complex fields — classical breaking along a flat polarization angle. (Restoration under quantization is argued in §4 from the exact U(1)^N × U(1)^N symmetry; executed code checks the symmetry, not the argument.)

A possible modification: §4's argument has a second premise, that "Nothing supplies a volume factor" (line 98). The audit's evidence says no code touches that step. Naming it would give "…argued in §4 from the exact U(1)^N × U(1)^N symmetry and the absence of a volume factor; executed code checks the symmetry, not the argument."

**If accepted, also:**

- Wiki pages (4):
  - `wiki/method/verification/toy-model-scripts.md`
  - `wiki/status/open-problems.md`
  - `wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/_index.md`
  - `wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration.md`

  `wiki/history/timeline.md` lines 174 ("Flags 39–42") and 177 name flag 41 in dated commit rows, which are history and need no edit.
- Executed check: none (wording only). The README of `review/wiki-build-checks/` maps no check to flag 41. The audit's `review/wiki-build-checks/audit/flag41_audit.py` lists what `verify/toy_gw.py` checks, and all of it is classical. The audit adds that a Monte Carlo of the complex model would show the finite-truncation part by code, but the no-volume-factor step would still be an argument.
- Also:
  - Flags 41 and 42 share a bullet ("42, 41", the ninth) in the "Where to start" list of `review/wiki-build-flags.md`, so that list changes once they are ruled.
  - #11 tags the U(1)/Goldstone structure [D][V] (§4, §10), but not the restoration, so it needs no change.
  - Record the wording fix in the worklog section 'Write-up and review (2026-10-19/20)'.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 5: M_X written where the squared mass is meant

**Audit:** confirmed (2 independent checks)

**Where it appears:**

1. `papers/broken-born-checkpoint-v2.md` line 81 (§7.5)
2. `notes/broken-born-program-v1.md` line 64 (§5 item 6)

Two places are correct as written and need no change (both audits):

- `notes/beta-coefficients.md` line 33 (§3). This is the source of the formula: "m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**".
- `notes/broken-born-theory.md` line 305 (Addendum v0.6): "five → two (M_X and one cubic-shape parameter)".

**Now reads:**

(1) `papers/broken-born-checkpoint-v2.md` line 81:

> **7.5 Spectrum [D].** Five βₙ → two parameters (M_X ∝ 2(β₁+β₂); one cubic shape).

(2) `notes/broken-born-program-v1.md` line 64:

> **Spectrum and parameters [D].** Five βₙ → two (M_X ∝ 2(β₁+β₂) and one cubic-shape parameter).

**Proposed:**

Both audits give the same wording.

(1) Line 81:

> **7.5 Spectrum [D].** Five βₙ → two parameters (M_X² ∝ 2(β₁+β₂); one cubic shape).

(2) Line 64:

> **Spectrum and parameters [D].** Five βₙ → two (M_X² ∝ 2(β₁+β₂) and one cubic-shape parameter).

**If accepted, also:**

- Wiki pages (13):
  - `wiki/gravity/momentum-graviton/spectrum-and-parity.md`
  - `wiki/gravity/momentum-graviton/gravitational-higgs.md`
  - `wiki/gravity/spin-2-fields/fierz-pauli.md`
  - `wiki/gravity/spin-2-fields/yukawa-forces.md`
  - `wiki/gravity/spin-2-fields/bimetric-cosmology.md`
  - `wiki/dark-matter/candidates/bigravity-dark-matter.md`
  - `wiki/dark-matter/candidates/x-condensate.md`
  - `wiki/predictions/massless-graviton.md`
  - `wiki/notation.md`
  - `wiki/history/documents/checkpoint.md`
  - `wiki/history/documents/field-equation-notes.md`
  - `wiki/history/main-problems.md`
  - `wiki/status/open-problems.md`

  The task's grep finds 6 of these; the rest use the "Flag 5" or "item 5" forms. Its hits on `velocity-granularity.md` ("flagship") and `wiki/history/documents/handoff.md` ("§5") are excluded.
- Executed check: none required. The audit calls this notation only, and no number depends on it. There is no flag-5 script in `review/wiki-build-checks/` itself. If Paul wants it gated, three audit scripts would serve:
  - `review/wiki-build-checks/audit/a_potential_expansion.py`: with both tadpoles set to zero (a flat aligned vacuum), the potential's quadratic term is (β₁ + 2β₂ + β₃)/8 · [Tr D² − (Tr D)²], D = h − l, on every draw, and β₁ + 2β₂ + β₃ → 2(β₁ + β₂) under the palindrome.
  - The textbook anchor in `audit/flag5_mass_scaling.py` part D: the static Green's function of (−∇² + k) decays at rate √k, so the mass is the square root of the quadratic coefficient. `audit/c_yukawa_scaling.py` prints d ln M_X / d ln(β₁+β₂) = 0.5.
- Also:
  - #11 needs a changelog line; with the other #11 edits in this batch, that makes a v2.3.
  - #9 is superseded and kept as the audit trail. Correcting #11 alone is the lighter option.
  - The flag's entry in `review/wiki-build-flags.md` records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 28: The formula beside "≈ 34" in #11 §11.2 is the 137 one

**Audit:** confirmed (2 independent checks)

**Where it appears:**
- `papers/broken-born-checkpoint-v2.md` line 117 (§11.2). This is the only place a source writes 4π/e² for our magnetic coupling. #14 v2's soliton mass M ~ (4π/e_d²)Λ_c uses the dark charge e_d and is a different formula (`review/skeptic-review-console.html` line 53; `review/v3-worklog.md` line 53, finding F2).
- Not the flagged statement, no change: `popsci/universes-other-half.md` line 41 gives the number without a formula ("about 34, against our 1/137"). The α_d ≈ 34 of the dead soliton episode (`HANDOFF.md` lines 32, 36 and 90; #14; `review/v3-worklog.md` R2) is a different quantity, as the flag says.

**Now reads:**

`papers/broken-born-checkpoint-v2.md` line 117:
> Non-observation is structural: Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34 — the magnetic world is our strong-coupling mirror, heavy and bound.

**Proposed:**

`papers/broken-born-checkpoint-v2.md` line 117 (the second auditor's wording; the first differs only in where "g²/4π" sits):
> Non-observation is structural: Dirac's condition e·g ~ 2π pins the magnetic coupling near g²/4π = π/e² = 1/(4α) ≈ 34 (α = e²/4π) — the magnetic world is our strong-coupling mirror, heavy and bound.

The bare minimum, changing the formula only:
> Non-observation is structural: Dirac's condition e·g ~ 2π pins the magnetic coupling near π/e² ≈ 34 — the magnetic world is our strong-coupling mirror, heavy and bound.

**If accepted, also:**
- Wiki pages (12): `wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling.md`, `wiki/electric-magnetic-duality/_index.md`, `wiki/electric-magnetic-duality/magnetic-identification.md`, `wiki/electric-magnetic-duality/magnetic-mirror-family.md`, `wiki/electric-magnetic-duality/monopoles/dirac-quantization.md`, `wiki/glossary.md`, `wiki/history/documents/checkpoint.md`, `wiki/method/verification/independent-anchors.md`, `wiki/method/verification/iron-rule.md`, `wiki/notation.md`, `wiki/predictions/monopole-null.md`, `wiki/status/open-problems.md`. The task grep returns 7 files, all real. It misses 5 pages that write "item 28" or "Flag 28": alpha-d-coupling, checkpoint, iron-rule, monopole-null and open-problems. 11 pages quote "4π/e²".
- Executed check: `review/wiki-build-checks/dirac_coupling_check.py`, which only prints. In `verify/` it would assert that, with α = e²/4π and e·g = 2π, g²/4π = π/e² = 1/(4α) ≈ 34.26, while 4π/e² = 1/α ≈ 137.04, a factor of 4 apart. The anchor independent of the paper is the Wu–Yang derivation of e·g = 2πn, with the monopole flux integrated symbolically in `review/wiki-build-checks/audit/flag28_recompute.py` and numerically in `audit/flag28_audit.py`. α⁻¹ = 137.035999 is typed in from memory (CODATA, †).
- Also: a #11 version bump (v2.3).

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 2: The toy note calls the coupling I "odd in K"

**Audit:** confirmed (1 independent check)

**Where it appears:**

- (1) `papers/reciprocity-toy-models.md` line 152 (§5, "A coupling built from (H, K)"). This is the flagged sentence.
- (2) `review/round4-adjudication.md` line 32 (Rulings, F3). It gives I_K as its example of "a coupling odd in K". The flag says F3's usage is fine. The audit says F3 "shares the slip". **The flag and the audit disagree here.**
- (3) `review/round4/referee/audit-notes.md` line 105 (Step 3, Internal consistency, C1). The referee also calls I_K "a K-odd coupling". Neither the flag nor the audit cites this line.
- (4) Places that use "a coupling odd in K" only as a requirement. The flag says this usage is fine, and the audit does not address these lines:
  - `papers/reciprocity-toy-models.md` line 10 (Abstract);
  - `papers/reciprocity-toy-models.md` line 54 (§2, Vacua);
  - `review/round4-adjudication.md` lines 77–78 (Revisions for v2, item 2);
  - `review/round4/referee/audit-notes.md` line 127 (Step 4, Verdict), the referee's own record.

**Now reads:**

(1) `papers/reciprocity-toy-models.md` line 152:

> - For ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, the two vacua give 0.4070 and 0.3600. **I is odd in K**, so it breaks the K → −K symmetry and makes the breaking of ρ physical (§2).

(2) `review/round4-adjudication.md` line 32:

> | F3 | The twisted ρ, ρ∘(K → −K), fixes the vacuum | **Upheld** | `arb.py`: (1, K₀) is mapped to itself. Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K. This sharpens the S5 conclusion rather than contradicting it. |

(3) `review/round4/referee/audit-notes.md` line 105 (excerpt):

> Sec. 2's "no vacuum is rho-invariant" is true for rho alone; "Born reciprocity is broken" in model I is a labelling choice until a K-odd coupling (Sec. 5's I_K: K->-K alone changes it by -0.046925) is added.

(4) `papers/reciprocity-toy-models.md` line 10:

> - Because the action is also invariant under K → −K, a twisted combination of ρ with that flip leaves the vacuum invariant. Breaking ρ becomes physical only once a coupling odd in K is present.

`papers/reciprocity-toy-models.md` line 54:

> - But the twisted element ρ∘(K → −K) maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present (§5).

`review/round4-adjudication.md` lines 77–78:

> 2. **§2/§6:** state the twisted ρ (F3). Breaking ρ is physical only with a
>    K-odd coupling.

`review/round4/referee/audit-notes.md` line 127 (excerpt):

> Both are repairable (bounded potential plus a K-odd coupling, or an honest restriction to a frozen-H toy), so B rather than C.

**Proposed:**

(1) Use the audit's wording. The flag's wording is the same without the parenthesis.

> - For ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, the two vacua give 0.4070 and 0.3600. **I is not invariant under K → −K** (it has a K-odd part), so it breaks the K → −K symmetry and makes the breaking of ρ physical (§2).

(2) This depends on which reading Paul takes:

- **The flag's reading:** no change.
- **The audit's reading:** change "odd in K" to "with a K-odd part". The audit gives no wording for F3; this follows its wording for line 152:

> | F3 | The twisted ρ, ρ∘(K → −K), fixes the vacuum | **Upheld** | `arb.py`: (1, K₀) is mapped to itself. Breaking ρ means something physically only once a coupling with a K-odd part breaks the K → −K symmetry, for example P4-type matter through I_K. This sharpens the S5 conclusion rather than contradicting it. |

To keep the arbitration as it was written, the same correction could go in a dated note below the Rulings table instead.

(3) No change. This line is the blind referee's own record.

(4) No change.

My own observation, not proposed by the flag or the audit: the "(§5)" at the end of line 54 points to §5's I as the coupling it means. If F3 is changed for the audit's reason, the same small change could be made to line 54, and to line 10, so the three places match.

**If accepted, also:**

- Wiki pages (9):
  - `wiki/method/review/round-4.md`
  - `wiki/method/verification/toy-model-scripts.md`
  - `wiki/notation.md`
  - `wiki/phase-space/reciprocity/wigner-function.md`
  - `wiki/program/hard-core.md`
  - `wiki/program/postulates/p4-polarized-matter.md`
  - `wiki/status/open-problems.md`
  - `wiki/symmetry-breaking/matter-coupling.md`
  - `wiki/symmetry-breaking/twisted-element.md`

  `round-4.md` and `open-problems.md` write "Flag 2" with a capital, which a case-sensitive grep misses. If F3 also changes, `twisted-element.md` line 102 quotes F3 in full and needs the new wording. So does `wiki/symmetry-breaking/strong-locality.md`, which does not cite the flag: line 68 quotes F3's sentence, and line 110 paraphrases it.
- Executed check: none (wording only). No script in `review/wiki-build-checks/` backs flag 2. The gate's `verify/toy_s5.py` already checks the two quoted values (line 105).
  - Optional: add one assertion there that both values are positive and unequal, so I is neither invariant nor odd under K → −K.
  - The audit's own scratch check split I into an even part (0.3835) and an odd part (0.0235). That check was not kept in the repository.
- Also: record the wording fix in the worklog section 'Write-up and review (2026-10-19/20)', which lists what v2 changed.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 4: A term missing from #7's expansion of S

**Audit:** confirmed (1 independent check)

**Where it appears:**

1. `notes/tuning-test.md` line 27 (§2, consequence 2).

No other source carries the expansion. A grep of papers/, notes/, popsci/, review/, verify/ and HANDOFF.md finds none.

**Now reads:**

(1) `notes/tuning-test.md` line 27:

> With Y = 1 + h, X = x: S = 2h + x² + O(3), A = [h, x] + O(3).

**Proposed:**

(1) Line 27, in the audit's wording:

> With Y = 1 + h, X = x: S = 2h + x² − h² + O(3), A = [h, x] + O(3).

The expansion of A is right as written; the audit checked it exactly at d = 2.

**If accepted, also:**

- Wiki pages (8):
  - `wiki/gravity/tuning-test/metric-tier-failures.md`
  - `wiki/gravity/spin-2-fields/fierz-pauli.md`
  - `wiki/method/verification/battery.md`
  - `wiki/method/verification/arithmetic-not-model.md`
  - `wiki/notation.md`
  - `wiki/history/documents/field-equation-notes.md`
  - `wiki/history/main-problems.md`
  - `wiki/status/open-problems.md`

  The task's grep finds 3 of these; the rest use the "Flag 4" or "item 4" forms. Its 4 other hits concern prediction row 4 or "flagship" and are excluded.
- Executed check: `review/wiki-build-checks/s_expansion.py`, moved into `verify/` and wired into `scripts/check.sh`, which runs only the scripts it lists. It would assert:
  - S − (2h + x²) is second order with coefficient −h² (printed 1.644231 at ε = 0.001, against |h²| = 1.644139);
  - S − (2h + x² − h²) is third order (printed 4.637607 after dividing by ε³);
  - Tr(S²)/ε² still tends to 4Tr(h²).

  The independent anchor is the textbook Neumann series (1 + εh)⁻¹ = 1 − εh + ε²h² − …. The audit's exact symbolic version, with h and x non-commuting at d = 2, is `review/wiki-build-checks/audit/flag4_audit.py` part 2.
- Also:
  - Battery T4 is unaffected. Its ε² term is exactly 4Tr(h²), and the missing term first enters Tr(S²) at third order (audit).
  - Flag 3's optional addition also touches line 27.
  - The flag's entry in `review/wiki-build-flags.md` records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 7: "Unique consistent structure" without the qualifier "known"

**Audit:** confirmed (1 independent check)

**Where it appears:**

1. `papers/broken-born-checkpoint-v2.md` line 73 (§7.1 (iii))
2. `papers/broken-born-checkpoint-v2.md` line 204 (§15, plain-language passage)
3. `notes/x-classification.md` line 48 (§5)
4. `notes/broken-born-program-v1.md` line 61 (§5 item 3)
5. `HANDOFF.md` line 12 (§1)
6. `notes/broken-born-program-v1.md` line 126 (§11, plain-language passage). This one is not in the flag's or the audit's list; a grep found it.
7. `popsci/angle-of-the-mirror.md` line 23 ("What refused to die"). This one is also not in either list; a grep found it.

Three places keep "known" and need no change:

- `notes/x-classification.md` line 3 (status line);
- `notes/x-classification.md` line 30 (§3);
- `notes/tuning-test.md` line 52 (§5).

**Now reads:**

(1) `papers/broken-born-checkpoint-v2.md` line 73:

> The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†].

(2) `papers/broken-born-checkpoint-v2.md` line 204:

> four consecutive consistency tests each forced the theory onto the unique consistent structure available,

(3) `notes/x-classification.md` line 48:

> and the unique consistent target structure named (HR class).

(4) `notes/broken-born-program-v1.md` line 61:

> The unique consistent home for a massive spin-2 coupled to gravity is the Fierz–Pauli/dRGT/Hassan–Rosen structure [T].

(5) `HANDOFF.md` line 12:

> the structural core survived four consecutive consistency tests by being forced onto unique consistent structures each time.

(6) `notes/broken-born-program-v1.md` line 126:

> instead forced it onto the unique consistent structure available at that junction

(7) `popsci/angle-of-the-mirror.md` line 23:

> by being repeatedly *forced*, at gunpoint, into the one consistent shape available.

**Proposed:**

(1) and (4) state the structure, and they take the audit's wording, "The only known consistent …". (2), (3) and (5) insert "known" as the audit asks, in #7 §5's own phrasing, "the unique known consistent structure". (6) and (7), which neither the flag nor the audit lists, get the same one-word insertion.

(1)

> The only known consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†].

(2) This sentence is also edited by flag 6; merge if both are accepted.

> four consecutive consistency tests each forced the theory onto the unique known consistent structure available,

(3)

> and the unique known consistent target structure named (HR class).

(4)

> The only known consistent home for a massive spin-2 coupled to gravity is the Fierz–Pauli/dRGT/Hassan–Rosen structure [T].

(5)

> the structural core survived four consecutive consistency tests by being forced onto unique known consistent structures each time.

(6) This passage is also edited by flag 6; merge if both are accepted.

> instead forced it onto the unique known consistent structure available at that junction

(7)

> by being repeatedly *forced*, at gunpoint, into the one known consistent shape available.

**If accepted, also:**

- Wiki pages (18):
  - `wiki/gravity/momentum-graviton/forcing-chain.md`
  - `wiki/gravity/momentum-graviton/gravitational-higgs.md`
  - `wiki/gravity/spin-2-fields/drgt-massive-gravity.md`
  - `wiki/gravity/tuning-test/conditional-pass.md`
  - `wiki/gravity/tuning-test/wedge-reduction.md`
  - `wiki/dark-matter/candidates/bigravity-dark-matter.md`
  - `wiki/program/assessment.md`
  - `wiki/method/_index.md`
  - `wiki/method/claim-tiers.md`
  - `wiki/glossary.md`
  - `wiki/references.md`
  - `wiki/history/documents/checkpoint.md`
  - `wiki/history/documents/field-equation-notes.md`
  - `wiki/history/documents/handoff.md`
  - `wiki/history/documents/source-conflicts.md`
  - `wiki/history/main-problems.md`
  - `wiki/history/timeline.md` (build-history rows; the ruling adds a row)
  - `wiki/status/open-problems.md`

  The task's grep finds 11 of these. Its hits on `yukawa-forces.md` and `metric-tier-failures.md` ("#7"/"§7.5") and on `direct-detection-null.md` ("flagship") are excluded.

  `wiki/gravity/spin-2-fields/hassan-rosen-bimetric.md` has no flag-7 pointer but calls the Hassan–Rosen class "the consistent structure" in its own words (lines 117 and 140).
- Executed check: none (wording only).
- Also:
  - #11 needs a changelog line; with the other #11 edits, a v2.3.
  - HANDOFF §1 is the move-in snapshot, #9 is superseded and #10 is a popular article. Each can be ruled separately.
  - The flag's entry in `review/wiki-build-flags.md` records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 8: "Five-function" where "five-parameter" is meant

**Audit:** confirmed (1 independent check)

**Where it appears:**

1. `notes/beta-coefficients.md` line 33 (§3, "Parameter count").

That is the only place. #7 line 42's "fewer free functions", the "predictive truncation" this sentence quantifies, describes the second frame rather than the βₙ. The flag and the audit do not touch it.

**Now reads:**

(1) `notes/beta-coefficients.md` line 33:

> The "predictive truncation" of Chunk A-iii is now quantified: HR bimetric's five-function freedom collapses to two numbers.

**Proposed:**

(1) Line 33, in the audit's wording:

> The "predictive truncation" of Chunk A-iii is now quantified: HR bimetric's five-parameter freedom collapses to two numbers.

**If accepted, also:**

- Wiki pages (6):
  - `wiki/gravity/spin-2-fields/hassan-rosen-bimetric.md`
  - `wiki/gravity/tuning-test/constrained-bimetric.md`
  - `wiki/gravity/momentum-graviton/spectrum-and-parity.md`
  - `wiki/history/documents/field-equation-notes.md`
  - `wiki/history/main-problems.md`
  - `wiki/status/open-problems.md`

  The task's grep finds 3 of these. Its hits on `wiki/_index.md` and `open-problems.md` line 146 (the count "8 depend on a convention"), on `metric-tier-failures.md` and on `round-4.md` (reference [8]) are excluded.
- Executed check: none (wording only).
- Also: the flag's entry in `review/wiki-build-flags.md` records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 9: #11's reference [24] has no authors and a descriptive title

**Audit:** confirmed (1 independent check)

**Where it appears:**
- `papers/broken-born-checkpoint-v2.md` line 253 (References, entry [24][S]).
- Not the flagged statement, no change: #11's in-text citations [24S] at line 17 (§1, technical abstract), line 79 (§7.4) and line 185 (§14 item 2); `HANDOFF.md` line 21 (§2) and line 112 (§8 item 5), which cite the arXiv number alone.

**Now reads:**

`papers/broken-born-checkpoint-v2.md` line 253:
> [24][S] Partially massless bimetric gravity and its exchange-symmetric parameter point, arXiv:1609.09515.

**Proposed:**

`papers/broken-born-checkpoint-v2.md` line 253 (the audit's wording; same layout as [22] and [25]):
> [24][S] L. Apolo, S. F. Hassan, A. Lundkvist, "Gauge and global symmetries of the candidate partially massless bimetric gravity," Phys. Rev. D 94, 124055 (2016), arXiv:1609.09515.

Authors, title and journal come from the audit's live fetch of the arXiv abstract page, so the [S] mark stays. The audit checked the record and the abstract's subject. It did not check that the paper contains what #11 §7.4 cites [24S] for (the partially-massless point's βₙ values and the proportional de Sitter solutions with an undetermined ratio). That check belongs to the partially-massless comparison, current queue item 1.

**If accepted, also:**
- Wiki pages (8): `wiki/_index.md`, `wiki/gravity/palindromic-branch/pm-comparison.md`, `wiki/gravity/spin-2-fields/hassan-rosen-bimetric.md`, `wiki/gravity/spin-2-fields/partially-massless-gravity.md`, `wiki/history/documents/checkpoint.md`, `wiki/method/literature-battery.md`, `wiki/references.md`, `wiki/status/open-problems.md`. The task grep returns 13 files. 7 are false hits on "flagship discriminants … §9": chi-particles, scattering-law, halo-substructure, direct-detection-null, table-history, graveyard, superseded. It misses pm-comparison and checkpoint, which write "Flag 9" or "item 9". 4 of the pages quote the old entry text ("exchange-symmetric parameter point"); the wiki gate does not compare quotations with sources.
- Executed check: none (wording only).
- Also: a #11 version bump (v2.3, with a changes line), shared with any other #11 edits.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 10: Four small pointer and wording slips

**Audit:** confirmed (1 independent check)

**Where it appears:**

- (1) `notes/broken-born-theory.md` line 25 (§1, P2). It points to §5 for the dark-energy potential, but the potential is in §3 (lines 86–92). §5 is "Conjugate-sector phenomenology".
- (2) `notes/toy-lagrangian.md` lines 463–465 ('Assessment against the predictions', "Findings that were not predicted", item 1). The worklog's own 'Predictions (written before construction)', lines 57–60, had already anticipated this.
- (3) `verify/toy_s5.py` lines 15–17 (docstring, part C) and line 78 (the printed heading of part C). Both say "built from K", but v2 of the note (§5, lines 148–150) says the coupling is built from (H, K) and is SO(2)-covariant.
  - Left as dated record: the worklog's 'S5 conclusion' (Chunk 4, `notes/toy-lagrangian.md` lines 433 and 442) says "A ρ-covariant coupling of matter to K" and "the K-covariant coupling". It was committed on 2026-10-19 (bed9306), before round 4's F5. The worklog's 'Write-up and review' (line 519) records the v2 change, "I_K stated as (H, K)-covariant".
- (4) `review/round4/referee/audit-notes.md` line 101 (Step 2(c), residual symmetry) and line 107 (Step 3, C3). These use "boost" for the diagonal squeeze diag(a, 1/a). The runaway family of F1 (line 49) is the hyperbolic S(t) = [[cosh t, sinh t],[sinh t, cosh t]], and line 101 calls that a boost too.
  - The referee's scripts mix the two in the same way: `review/round4/referee/ref_sec5.py` line 98 has "boost S = diag(l, 1/l)" (its printed heading at line 76 says "vs a boost" for the same map), and `ref_model1.py` line 126 has "hyperbolic 'boost'".
  - The adjudication and the toy note keep the two apart, calling one "squeeze" and the other "boost".

**Now reads:**

(1) `notes/broken-born-theory.md` line 25 (excerpt, the last sentence of P2):

> This single postulate does triple duty below: it kills the would-be second graviton (no Boulware–Deser ghost, §6), it enforces the cosmological constraint $a\tilde a = \text{const}$ (§7), and it supplies the explicit breaking that gives the dark-energy field its potential (§5).

(2) `notes/toy-lagrangian.md` lines 57–60 (Predictions):

> - **S4 will pass only for a discrete reduction** (the symmetry group cut
>   down to the group generated by ρ) or via the non-amenability exception.
>   The continuous U(1) of phase-space rotations that contains ρ would be
>   restored in 1+1.

`notes/toy-lagrangian.md` lines 463–465 (finding 1):

> 1. At every self-dual point, ρ sits inside a continuous U(1). The
>    polarization is therefore a Goldstone angle; in the coset toy it is
>    Λ(1), the checkpoint's τ. This is structural support for §10.

(3) `verify/toy_s5.py` lines 15–17:

> ```
>   C. A rho-covariant matter interaction built from K (the "marginal" form)
>      is local in L+ and nonlocal in L-; a K-blind phase-space interaction
>      shows no asymmetry.
> ```

`verify/toy_s5.py` line 78:

> ```
> print("\n== C: a rho-covariant interaction built from K (numerical, hbar = 1)")
> ```

(4) `review/round4/referee/audit-notes.md` line 101:

> - Residual symmetry once the potential is added (sympy): S^-1 K_ref S = +K_ref -> S = diag(a, 1/a); = -K_ref -> S = [[0, -1/c],[c, 0]]. So the potential leaves a NON-COMPACT boost subgroup unbroken plus {+-1, +-rho} (Z4) in SO(2). Combined with F1/F2: in model I proper, the boost direction is where the potential runs away.

`review/round4/referee/audit-notes.md` line 107 (excerpt):

> But it uses the Euclidean Tr(K^T K), which breaks the residual boosts explicitly; the vacuum analysis with H dynamical would have to be redone.

**Proposed:**

(1) Change only "§5" to "§3". The "(§7)" in the same sentence is flag 25, so rule on the two together.

> This single postulate does triple duty below: it kills the would-be second graviton (no Boulware–Deser ghost, §6), it enforces the cosmological constraint $a\tilde a = \text{const}$ (§7), and it supplies the explicit breaking that gives the dark-energy field its potential (§3).

(2) Leave the Predictions unchanged, because they were pre-registered. Reword finding 1 with the audit's wording:

> 1. At every self-dual point, not only in the coset model the Predictions
>    anticipated, ρ sits inside a continuous U(1). The polarization is
>    therefore a Goldstone angle; in the coset toy it is Λ(1), the
>    checkpoint's τ. This is structural support for §10.

(3) Use the audit's wording "built from (H, K), SO(2)-covariant". The checks themselves do not change.

> ```
>   C. A rho-covariant matter interaction built from (H, K), SO(2)-covariant
>      (the "marginal" form), is local in L+ and nonlocal in L-; a K-blind
>      phase-space interaction shows no asymmetry.
> ```

> ```
> print("\n== C: a rho-covariant interaction built from (H, K), SO(2)-covariant (numerical, hbar = 1)")
> ```

(4) Do not edit the referee's record. Following the audit ("annotate rather than edit"), add one marked line below line 101:

> - [Annotation, not the referee's, added on the date of the ruling: "boost" here names two different families. The residual subgroup S = diag(a, 1/a), which C3 below calls "the residual boosts", is the diagonal squeeze. The runaway direction of F1 (Step 2(a)) is the hyperbolic boost S(t) = [[cosh t, sinh t],[sinh t, cosh t]].]

**If accepted, also:**

- Wiki pages (15), grouped by item:
  - Item 1:
    - `wiki/cosmology/dark-energy/tau-quintessence.md`
    - `wiki/history/documents/lab-notebook.md`
    - `wiki/history/documents/source-conflicts.md`
    - `wiki/program/postulates/original-p2.md`
  - Item 2:
    - `wiki/symmetry-breaking/goldstone-angle.md`
    - `wiki/symmetry-breaking/toy-models/success-criteria.md`
  - Item 3:
    - `wiki/method/verification/toy-model-scripts.md` (it also quotes the printed heading at line 250)
    - `wiki/status/superseded.md`
    - `wiki/symmetry-breaking/matter-coupling.md`
  - Item 4:
    - `wiki/method/review/round-4.md`
    - `wiki/notation.md`
    - `wiki/phase-space/reciprocity/symplectic-form.md`
    - `wiki/symmetry-breaking/toy-models/coset-model/bounded-potential.md`
    - `wiki/symmetry-breaking/toy-models/coset-model/naive-potential.md`
  - All four items: `wiki/status/open-problems.md`.

  `tau-quintessence.md`, `lab-notebook.md` and `source-conflicts.md` cite the flag as "item 10", which the prescribed grep misses. Other grep hits were false matches: "§10", "2026-10-20", "flagship", and #11's "open item 10".
- Executed check: none (wording only). No script in `review/wiki-build-checks/` backs flag 10. Item 3 changes only a docstring and a printed heading of a script the gate already runs, not its checks.
- Also:
  - Item 1 shares a sentence with flag 25.
  - Item 2 changes the worklog's scoring of its pre-registered predictions, not the predictions themselves.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 11: Tadpole growth in model II, ln N or 2 ln N

**Audit:** depends on a convention or reading

**Where it appears:**

- (1) `papers/reciprocity-toy-models.md` line 101 (§4, model II restoration, first caveat) says "ln N".
- (2) `review/round4-adjudication.md` line 35 (Rulings, F6) says "2 ln N".
- (3) `review/round4-adjudication.md` lines 85–87 (Revisions for v2, item 4) says "2 ln N".
- (4) `review/round4/referee/audit-notes.md` line 87 (Step 2(c), F6) and line 113 (Step 3, Model II) say "2 ln N". Line 87 gives the averaged vertex as 2 Σ_k (G₀ₖ + Gₖ₀) and quotes T₀(N) − 2 ln N → −0.8455. T₀ itself, T₀(N) = Σ_k [G₀ₖ + Gₖ₀], a sum of two harmonic sums, is defined in the referee's script `review/round4/referee/ref_model2_quantum.py` (lines 33–37).
- (5) `notes/toy-lagrangian.md` line 518 ('Write-up and review') says "the ln N tadpole".
- (6) `verify/toy_gw.py` lines 207–210 (the F6 check) tests a single harmonic series, "~ ln N".

**Now reads:**

(1) `papers/reciprocity-toy-models.md` line 101:

> - The bare μ² is itself renormalized. The level-0 tadpole grows as ln N (it is a harmonic sum), so fixed bare μ² is not a consistent large-N limit.

(2) `review/round4-adjudication.md` line 35:

> | F6 | "Increasing the truncation adds only massive levels" ignores the 2 ln N mass renormalization | **Accepted, not re-checked** | 2D φ⁴ needs mass renormalization. The no-breaking conclusion is unaffected; the argument must be restated. |

(3) `review/round4-adjudication.md` lines 85–87:

> 4. **§4, model II:** restate the restoration argument (exact independence of
>    the condensate phases, no volume factor), add the 2 ln N mass
>    renormalization, and compare with Langmann–Szabo–Zarembo.

(4) `review/round4/referee/audit-notes.md` line 87 (excerpt):

> One-loop: d^2 Tr((phi^+phi)^2)/dphi00 dconj(phi00) averaged = "4*G00 + 2*G01 + 2*G02 + 2*G10 + 2*G20" (N=3), i.e. 2 sum_k (G_0k + G_k0); with G_ij = 1/(i+j+1+M^2): T_0(N) - 2 ln N -> -0.8455 (N=10^5), i.e. the tadpole grows as 2 ln N.

`review/round4/referee/audit-notes.md` line 113 (excerpt):

> The tadpole grows as 2 ln N (F6), so "fixed mu^2" needs renormalisation.

(5) `notes/toy-lagrangian.md` line 518:

> - the restoration argument restated, with the ln N tadpole;

(6) `verify/toy_gw.py` lines 207–210:

> ```
> print("\n== Mass renormalization: the tadpole grows logarithmically with the truncation (round-4 F6)")
> Hn = [sum(1/(k + 1) for k in range(n)) - np.log(n) for n in (10, 1000, 100000)]
> check("sum_{k<N} 1/(k+1) - ln N -> Euler's gamma (the level-0 tadpole with G_0k = 1/(k+1) is ~ ln N)",
>       abs(Hn[-1] - 0.5772156649) < 1e-4, str(np.round(Hn, 5)))
> ```

**Proposed:**

The audit finds both figures correct, each under its own normalization:

- The level-0 tadpole is made of two equal harmonic sums, one over the row index and one over the column index.
- One sum grows as ln N. That is the note's figure.
- The two together grow as 2 ln N. That is the referee's T₀, and the adjudication uses it.
- The averaged vertex grows as 4 ln N.

The audit proposes no wording and **states no preference between A and B**.

- **Option A (state the normalization).** Places (2)–(4) stay as they are, because their 2 ln N is the growth of the referee's two-sum T₀ (defined in `ref_model2_quantum.py`).
  - (1):

    > - The bare μ² is itself renormalized. The level-0 tadpole grows logarithmically, as ln N for each of its two equal harmonic sums (row and column), so fixed bare μ² is not a consistent large-N limit.

  - (5):

    > - the restoration argument restated, with the logarithmic tadpole (ln N per harmonic sum);

  - (6): keep the single-series check, and add a second check for the referee's two-sum form (see below).
- **Option B:** no change anywhere. The wiki then keeps its conflict entry C29 open.

**If accepted, also:**

- Wiki pages (11):
  - `wiki/history/documents/source-conflicts.md` (entry C29)
  - `wiki/method/review/review-protocol.md`
  - `wiki/method/review/round-4.md`
  - `wiki/method/verification/arithmetic-not-model.md`
  - `wiki/method/verification/independent-anchors.md`
  - `wiki/method/verification/toy-model-scripts.md` (it also quotes the gate's output at line 184)
  - `wiki/notation.md`
  - `wiki/status/open-problems.md`
  - `wiki/status/superseded.md`
  - `wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/_index.md`
  - `wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration.md`

  `wiki/history/timeline.md` line 177 names flag 11 in a dated commit row, which is history and needs no edit. The "§14 item 11" hits on other pages refer to #11's item 11, not this flag.
- Executed check: no script in `review/wiki-build-checks/` backs flag 11. The audit's sympy check (`audit_checks.py`) was not kept in the repository.
  - Under Option A, extend the F6 check in `verify/toy_gw.py`, which the gate already runs. It would assert that the referee's T₀ = Σ_k (G₀ₖ + Gₖ₀), with G_ij = 1/(i + j + 1 + M²), is two equal harmonic sums.
  - At M² = 1, T₀ − 2 ln N should then tend to 2(γ − 1) ≈ −0.8456. The anchor H_n − ln n → γ is a textbook limit, independent of the paper.
  - The referee's `review/round4/referee/out_model2_quantum.txt` prints −0.8455 at N = 10⁵. A rerun for this worksheet agrees: `/tmp/claude-1000/-home-paul-git-reinholdtsen-conjugate-matter/f914ff8b-9e54-489b-92fe-c443048774ac/scratchpad/g3-work/tadpole_limits.py`.
  - Optional: also gate the vertex identity ⟨∂²Tr((φ†φ)²)/∂φ₀₀∂φ̄₀₀⟩ = 2 Σ_k (G₀ₖ + Gₖ₀). The referee prints it at N = 3, and the audit checked it at N = 3 and 4.
- Also: Option A closes wiki conflict C29. #11 does not state the coefficient, so it needs no change.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 12: The adjudication calls V_b's flat direction an exact symmetry

**Audit:** confirmed (2 independent checks)

**Where it appears:**

- (1) `review/round4-adjudication.md` line 31 (Rulings, F2).
- (2) `review/round4-adjudication.md` lines 69–70 (Revisions for v2, item 1).
- Already correct, no change needed:
  - `papers/reciprocity-toy-models.md` line 114 (§4), "not symmetry-protected";
  - the referee's `review/round4/referee/audit-notes.md` line 107 (C3), "breaks the residual boosts explicitly";
  - `verify/toy_coset.py` line 183, which checks only that the line is flat.

**Now reads:**

(1) `review/round4-adjudication.md` line 31 (excerpt):

> The referee's bounded variant −μ[Tr(K K_ref)]²/(2Tr KᵀK) gives eigenvalues [0, 0.764, 2, 5.236]. Its zero mode is the residual diagonal squeeze, which is an exact symmetry, and the boost family rises from −1 to −0.5. **This is the repair.**

(2) `review/round4-adjudication.md` lines 69–70:

> - Use the bounded potential. Show it is stable with H dynamical (local
>   minimum up to the exact residual squeeze).

**Proposed:**

(1) Use auditor 1's wording, keeping the word "residual". Auditors 1 and 2 are the first and second flag-12 entries in `review/wiki-build-checks/flag-audit.json`.

> The referee's bounded variant −μ[Tr(K K_ref)]²/(2Tr KᵀK) gives eigenvalues [0, 0.764, 2, 5.236]. Its zero mode is the classical flat line H = diag(y, 1/y), K = K_ref, swept out by the residual diagonal squeeze. The squeeze is not a symmetry of V_b (its Tr KᵀK breaks it), so the line is not symmetry-protected, and the boost family rises from −1 to −0.5. **This is the repair.**

Auditor 2's version adds "off K = ±K_ref". Both auditors note that V_b is also squeeze-invariant where Tr(K K_ref) = 0, and auditor 1 calls that qualifier "slightly loose". It is left out here.

(2) Use auditor 2's wording:

> - Use the bounded potential. Show it is stable with H dynamical (local
>   minimum up to the classical flat squeeze line, which is not
>   symmetry-protected).

To keep the arbitration as it was written, both corrections could go in a dated note below the Rulings table instead.

**If accepted, also:**

- Wiki pages (9):
  - `wiki/history/documents/source-conflicts.md` (entry C28, cited as "item 12")
  - `wiki/method/review/round-4.md`
  - `wiki/method/verification/_index.md`
  - `wiki/method/verification/reduced-model-stability.md`
  - `wiki/method/verification/toy-model-scripts.md`
  - `wiki/phase-space/reciprocity/symplectic-form.md`
  - `wiki/status/open-problems.md`
  - `wiki/symmetry-breaking/goldstone-and-higgs.md`
  - `wiki/symmetry-breaking/toy-models/coset-model/bounded-potential.md`
- Executed check: move `review/wiki-build-checks/squeeze_check.py` into `verify/`, for example beside the flat-line check at line 183 of `verify/toy_coset.py`, which the gate already runs. The script only prints today. In the gate it would assert:
  - (a) the squeeze S = diag(a, 1/a) leaves the λ-term invariant (positive control);
  - (b) V_b(S⁻¹KS) − V_b(K) is not identically zero, giving its factorized form and the example a = 2, K = [[1/2, 1], [3/4, −1/2]] → 320/1683;
  - (c) the difference vanishes on K = K_ref, so the line is flat but the squeeze is not a symmetry.

  Two audit scripts could back this further:
  - `review/wiki-build-checks/audit/a1_symmetry_group.py`: V_b has no continuous Sp(2,ℝ) symmetry;
  - `a2_flat_line_spectrum.py`: the fluctuation masses change along the line.
- Also: nothing else. Toy note v2 is already right, and #11 does not mention the zero mode.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 13: The Monte Carlo error bar "± 0.0001 at every size"

**Audit:** confirmed (1 independent check)

**Where it appears:**

- (1) `papers/reciprocity-toy-models.md` line 125 (§4, Monte Carlo table, first row).
- (2) `verify/toy_s4.py` lines 74–75 (the gate's "quoted:" check). Its label repeats the note's wording, but its test is standard error < 0.0002.
- Not affected: `notes/toy-lagrangian.md` line 325 gives 0.954 with no error bar.

**Now reads:**

(1) `papers/reciprocity-toy-models.md` line 125:

> ```
> | With the potential (J = h = 1), T = 0.6 | ⟨\|m\|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667 | Ordered ℤ₂ phase |
> ```

(2) `verify/toy_s4.py` lines 74–75:

> ```
> check("quoted: <|m|> = 0.954 +- 0.0001 at every size, Binder 0.667",
>       all(round(A[L][0][0], 3) == 0.954 and A[L][1][0] < 0.0002 and round(A[L][0][1], 3) == 0.667 for L in SIZES))
> ```

**Proposed:**

(1) Use the audit's wording:

> ```
> | With the potential (J = h = 1), T = 0.6 | ⟨\|m\|⟩ = 0.954 at every size (standard error ≤ 0.0001); Binder cumulant 0.667 | Ordered ℤ₂ phase |
> ```

(2) Change the label to match the note:

> ```
> check("quoted: <|m|> = 0.954 at every size (standard error <= 0.0001), Binder 0.667",
> ```

Optional: tighten the test so that the gate asserts what the text says. This makes the check stricter, not weaker. Replace `A[L][1][0] < 0.0002` with `round(A[L][1][0], 4) <= 0.0001`. With the fixed seeds the script prints ± 0.0001, ± 0.0001 and ± 0.0000 at L = 16, 32 and 64, so the tighter test would pass. Both the audit's run and a rerun for this worksheet printed these values.

**If accepted, also:**

- Wiki pages (11). Each quotes "0.954 ± 0.0001 at every size".
  - `wiki/method/review/round-4.md`
  - `wiki/method/verification/monte-carlo-error-bars.md` (also quotes the gate's output)
  - `wiki/method/verification/toy-model-scripts.md` (also quotes the gate's output, including the "quoted:" label at line 218)
  - `wiki/program/hard-core.md`
  - `wiki/program/postulates/p5-spontaneous-selection.md`
  - `wiki/status/open-problems.md`
  - `wiki/symmetry-breaking/goldstone-angle.md`
  - `wiki/symmetry-breaking/mermin-wagner-coleman.md`
  - `wiki/symmetry-breaking/order-parameter.md`
  - `wiki/symmetry-breaking/toy-models/acceptance-criterion.md`
  - `wiki/symmetry-breaking/toy-models/coset-model/monte-carlo.md`
- Executed check: none to move. No script in `review/wiki-build-checks/` backs flag 13. The check is `verify/toy_s4.py` itself, already in the gate; only its label changes, and optionally its tolerance.
- Also: record the wording fix in the worklog section 'Write-up and review (2026-10-19/20)'. #11 does not quote the figure.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 14: Which square root's eigenvalues give Tr(g²)

**Audit:** depends on a convention or reading

**Where it appears:**

1. `notes/tuning-test.md` line 28 (§2, consequence 3).

That is the only place that names the eigenvalues. Four places restate the conclusion without naming them: #11 §7.2 (line 75), #9 §5 item 4 (line 62), #1 v0.5 (line 297) and `HANDOFF.md` §2 (line 22). Each says Tr(g²) + Tr(g⁻²) lies outside the Hassan–Rosen span. The audit finds that this conclusion stands under either reading, so they need no change.

**Now reads:**

(1) `notes/tuning-test.md` line 28:

> Tr(g²) = p₄ of the square-root eigenvalues is a *nonlinear* polynomial in the eₙ, hence outside the family.

**Proposed:**

Option A states the convention explicitly. It is the audit's first edit and the flag's reading, and it keeps the root that the family Σβₙeₙ(√(g⁻¹f)) uses:

> Tr(g⁻²) = p₄ of the eigenvalues of √(g⁻¹f) is a *nonlinear* polynomial in the eₙ, hence outside the family.

The audit's other edit names √(f⁻¹g) and keeps Tr(g²). That version holds only if the potential's measure is g-independent, so #7 would then also have to say so.

Option B: no change. The sentence is defensible if "square-root eigenvalues" means the square roots of g's eigenvalues (the eigenvalues of √(f⁻¹g) at f = 1) and the measure is g-independent. #7 fixes neither the root nor the measure.

The audit closes with the two edits as its "disambiguating edit" and calls the flag's reading, Option A's, the more natural, since √(g⁻¹f) stands next to the phrase. The conclusion (outside the eₙ span, battery T7) stands either way.

**If accepted, also:**

- Wiki pages (11):
  - `wiki/gravity/spin-2-fields/elementary-symmetric-polynomials.md`
  - `wiki/gravity/spin-2-fields/drgt-massive-gravity.md`
  - `wiki/gravity/tuning-test/metric-tier-failures.md`
  - `wiki/method/verification/battery.md`
  - `wiki/method/verification/independent-anchors.md`
  - `wiki/method/verification/arithmetic-not-model.md`
  - `wiki/notation.md`
  - `wiki/history/documents/field-equation-notes.md`
  - `wiki/history/main-problems.md`
  - `wiki/history/timeline.md` (build-history row; the ruling adds a row)
  - `wiki/status/open-problems.md`

  The task's grep finds 9 of these; the other 2 use the "Flag 14" or "items 4, 14" forms.
- Executed check: `review/wiki-build-checks/sqrt_eig_check.py`, moved into `verify/` and wired into `scripts/check.sh`. At f = 1 it would assert p₄(eig √(g⁻¹f)) = Tr(g⁻²) and p₄(eig √(f⁻¹g)) = Tr(g²); the script prints both pairs. Its independent anchor is Newton's identity, p₄ = e₁⁴ − 4e₁²e₂ + 2e₂² + 4e₁e₃ − 4e₄, which it prints as "Newton p4 identity: True". The audit's `review/wiki-build-checks/audit/flag14_audit.py` part 6 would add the membership test: Tr(S²) lies outside the eₙ span under either measure (rms 7.974 and 7.262, against HR controls at 4.245e-14 and 1.433e-13).
- Also:
  - Battery T7 is unaffected: it tests p₄ of generic eigenvalues, not which root they come from.
  - The flag's entry in `review/wiki-build-flags.md` records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 15: "η antisymmetric-pairing" in calc note #6

**Audit:** confirmed (1 independent check)

**Where it appears:**

- `notes/x-classification.md` line 17 (#6 §2). This is the only place. The related sentence in #11 §7.1 (line 73) and #9 §5 item 2 (line 60) reads "the symmetry type of the rigid pairing dictates the partner's spin". It gives η no symmetry type and needs no change.

**Now reads:**

`notes/x-classification.md` line 17 (#6 §2):

> The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field.

**Proposed:** This is the audit's suggested wording. The partners' symmetry types are the ones the same paragraph already states: the B-field is antisymmetric and X is symmetric.

`notes/x-classification.md` line 17 (#6 §2):

> The symmetry type of the rigid structure — η symmetric (its partner, B, antisymmetric) vs ω antisymmetric (its partner, X, symmetric) — dictates the symmetry type of the partner field.

**If accepted, also:**

- Wiki pages (5): `wiki/gravity/momentum-graviton/symplectic-partner.md`, `wiki/history/main-problems.md` (which cites items 14–17), `wiki/history/documents/field-equation-notes.md`, `wiki/phase-space/born-geometry/double-field-theory.md` and `wiki/status/open-problems.md`. The requested grep finds only 2 of these. Its one other hit, "#1–#15" on the home page, is not about the flag.
- Executed check: none (wording only).
- Also: #6 has not been edited since the import. The flag's entry in `review/wiki-build-flags.md` needs updating.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 16: A ✓ (machine-verified) with no script behind it

**Audit:** confirmed (1 independent check)

**Where it appears:**
1. `HANDOFF.md` line 29 (§2, "Dead"): the clumping figure carries ✓. Line 16 (§2) defines ✓ as machine-verified.

The same figure appears elsewhere without a ✓. These need no change: `HANDOFF.md` line 51 (§3, artifact #2); `notes/stream-stability.md` line 53 ("Numbers at the scattering benchmark"); `notes/broken-born-theory.md` line 271 (addendum v0.2); `notes/broken-born-program-v1.md` line 80 (§7); `papers/broken-born-checkpoint-v2.md` line 99 (§9, tagged [D]). Two more state it in words and need no change either: `papers/broken-born-checkpoint-v2.md` line 97 (§9's plain-language passage, "thirty orders of magnitude") and `popsci/angle-of-the-mirror.md` line 17 (#10, "a factor of ten to the thirtieth").

**Now reads:**
1. `HANDOFF.md` line 29 (§2):
> - DM clumping in momentum space as dynamics: impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓), fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact), tunable elsewhere. Rows withdrawn permanently. Loophole: *topological* p-localization of individual solitons untouched.

   The legend, `HANDOFF.md` line 16 (§2):
> **Alive (derived, machine-verified where marked ✓):**

**Proposed:** The audit offers two ways to fix this.
1. `HANDOFF.md` line 29. Variant 1 changes the mark (the audit's wording):
> - DM clumping in momentum space as dynamics: impossible for particle DM (criterion fails by 10²⁸–10³¹; [D], not yet gated in verify/), fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact), tunable elsewhere. Rows withdrawn permanently. Loophole: *topological* p-localization of individual solitons untouched.

   Variant 2 makes no text change. The ✓ stays, and the figure gets gated in `verify/` with an independent anchor (see below), which makes the ✓ true as written.

**If accepted, also:**
- Wiki pages (17). The search matched "flag 16", "Flag 16", "item(s) 16" and lists that contain 16: `wiki/_index.md`, `wiki/dark-matter/momentum-clumping/_index.md`, `wiki/dark-matter/momentum-clumping/founding-image.md`, `wiki/dark-matter/momentum-clumping/instability-criterion.md`, `wiki/glossary.md`, `wiki/history/main-problems.md`, `wiki/history/documents/clumping-notes.md`, `wiki/history/documents/handoff.md`, `wiki/history/documents/source-conflicts.md`, `wiki/method/_index.md`, `wiki/method/negative-results.md`, `wiki/method/provenance-tags.md`, `wiki/method/verification/independent-anchors.md`, `wiki/method/verification/iron-rule.md`, `wiki/method/verification/the-gate.md`, `wiki/status/alive.md`, `wiki/status/open-problems.md`. `wiki/history/timeline.md` line 170 also names flag 16, but it is a dated build row and stays as written.
- Executed check: `review/wiki-build-checks/stream_stability_check.py` reproduces the ratios: 3.9e-28 for the dwarf core and 2.9e-31 for the local Milky Way. It only prints them. The README says an accepted flag's check moves into `verify/`. Once there, it would assert both ratios ("fails by 10²⁸–10³¹"), exit non-zero on failure, and be added to the script list on `scripts/check.sh` line 21. Under Variant 2 this check is what makes the ✓ true. The check reproduces #2's own inputs, so it needs an anchor independent of #2 (CLAUDE.md). The flag-19 audit's recomputation in `review/wiki-build-checks/audit/flag19_audit.py` builds its units from the exact SI constants, sharing no hard-coded values with `stream_stability_check.py` (audit), and prints the same ratios, 3.89e-28 and 2.86e-31. Its inputs are #2's, so it cross-checks the arithmetic and the units, not #2's inputs.
- Also:
  - Flag 19 uses the same script, so one `verify/` script can serve both flags.
  - Update flag 16's entry in `review/wiki-build-flags.md`, and the `stream_stability_check.py` row of `review/wiki-build-checks/README.md`, whose Flag column reads "—".
  - Variant 1 edits the dated handoff (prepared 2026-10-19). Variant 2 leaves the handoff untouched.
  - #11 §9's [D] tag stays correct either way. Under Variant 2 the result could also carry [V], which is optional and would need a #11 version bump.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 17: Two forms of the gate's exponent, and a √2 in μ

**Audit:** depends on a convention or reading (both of 2 checks)

**Where it appears:**
1. `notes/x-classification.md` line 40 (#6 §4): the overlap form e^{−(p₁−p₂)²/2μ²}. The note does not say whether it applies to the amplitude or to the rate.
2. `notes/broken-born-theory.md` lines 99 and 102 (#1 §3): the amplitude gate e^{−k²/μ²}, with k = m_χv_rel/2.
3. `notes/broken-born-theory.md` lines 127 and 138 (#1 §5.1): v* ≡ √2μ/m_χ and μ ≈ 20 keV.
4. `papers/conjugate-special-relativity.md` line 73 (#13 §4): μ as the momentum-space width, used with v* = √2μ/m_χ.

Five more places state the documents' convention that #1's μ is the fiber width. None changes under any option: `notes/broken-born-theory.md` line 291 (addendum v0.4); `notes/beta-coefficients.md` line 47 (#8 §5); `notes/broken-born-program-v1.md` line 72 (#9 §6); `papers/broken-born-checkpoint-v2.md` line 91 (#11 §8); `HANDOFF.md` line 24 (§2). `notes/broken-born-theory.md` line 253 (#1 §11, open problem 2) restates the amplitude gate as e^{−k²/μ²}; it does not change under any option either.

**Now reads:**
1. `notes/x-classification.md` line 40 (#6 §4):
> Wavepacket overlap of Gaussian profiles gives exactly $e^{-(p_1-p_2)^2/2\mu^2}$ — the postulated gate, with **μ = the χ quantum's own p-width**, a physical identification the EFT lacked.
2. `notes/broken-born-theory.md` line 99 (#1 §3):
> \boxed{\ \mathcal M(k, q) \;=\; \frac{4\pi\,\tilde\alpha\, m_\chi}{q^2 + m_\phi^2}\; e^{-k^2/\mu^2}\ }

   `notes/broken-born-theory.md` line 102 (#1 §3):
> where $q$ is the momentum **transfer** and $k = m_\chi v_{\rm rel}/2$ the incoming **relative** momentum.
3. `notes/broken-born-theory.md` line 127 (#1 §5.1):
> \boxed{\ \sigma_T(v) \;=\; \sigma_0\, e^{-v^2/v_*^2}, \qquad v_* \equiv \sqrt{2}\,\mu/m_\chi, \qquad \sigma_0 = \frac{16\pi\tilde\alpha^2 m_\chi^2}{m_\phi^4}\ }

   `notes/broken-born-theory.md` line 138 (#1 §5.1):
> m_\chi \approx 70\ \mathrm{MeV} \times \tilde\alpha^{2/3}\left(\frac{\sigma_0/m}{30\ \mathrm{cm^2 g^{-1}}}\right)^{-1/3}, \qquad \mu = \frac{m_\chi v_*}{\sqrt 2} \approx 20\ \mathrm{keV}\ (\tilde\alpha \approx 1).
4. `papers/conjugate-special-relativity.md` line 73 (#13 §4):
> The conjugate quantum's invariant extent fixes its intrinsic momentum-space width μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v* = √2 μ/m_χ.

**Proposed:** At most one place changes, #6 §4. Places 2–4 (#1 and #13) stay as they are under every option.
- Option A states the convention, reading #6's form as the factor on the rate. Under this reading all the documents agree. The change is to `notes/x-classification.md` line 40:
> Wavepacket overlap of Gaussian profiles gives exactly $e^{-(p_1-p_2)^2/2\mu^2}$ — the postulated gate at the level of the rate (with $p_1-p_2 = 2k$ it is the square of the flagship's amplitude gate $e^{-k^2/\mu^2}$, and equals its $\sigma_T$ factor $e^{-v^2/v_*^2}$, $v_* = \sqrt2\,\mu/m_\chi$), with **μ = the χ quantum's own p-width**, a physical identification the EFT lacked.
- Option A′ states the same convention at the level of the amplitude. It is one check's one-line fix: the exponent 2μ² becomes 4μ², which with p₁ − p₂ = 2k equals #1 §3's e^{−k²/μ²}. Line 40 would read:
> Wavepacket overlap of Gaussian profiles gives exactly $e^{-(p_1-p_2)^2/4\mu^2}$ — the postulated gate, with **μ = the χ quantum's own p-width**, a physical identification the EFT lacked.
- Option B makes no change. No stated number changes under any option. The only stated μ is #1's ≈ 20 keV, which is in #1's convention. #1's σ_T/m values at 300 and 1500 km/s use v* only.
- The audit does not choose among A, A′ and B. Both checks find #13 §4 right under the documents' convention. So any change belongs in #6 §4, not in #13 §4, where the flag places the mix. One check names a clause in #6 §4 as what would decide the question.
- The flag's own reading takes #6's form as the amplitude gate and uses it to define μ. That reading would instead give v* = μ/m_χ in #13 §4 and μ = 28 keV. No document states that value, and neither check recommends this reading.

**If accepted, also:**
- Wiki pages (18). The search matched "flag 17", "Flag 17", "item(s) 17" and lists that contain 17: `wiki/conjugate-relativity/_index.md`, `wiki/conjugate-relativity/invariant-length-shell.md`, `wiki/dark-matter/candidates/chi-particles.md`, `wiki/dark-matter/conjugate-matter/benchmark.md`, `wiki/dark-matter/conjugate-matter/gate-mechanism.md`, `wiki/dark-matter/conjugate-matter/gate-shape.md`, `wiki/dark-matter/conjugate-matter/scattering-law.md`, `wiki/dark-matter/conjugate-matter/velocity-gate.md`, `wiki/dark-matter/momentum-clumping/gated-vlasov-model.md`, `wiki/history/main-problems.md`, `wiki/history/documents/field-equation-notes.md`, `wiki/history/documents/lab-notebook.md`, `wiki/history/documents/source-conflicts.md`, `wiki/notation.md`, `wiki/predictions/_index.md`, `wiki/predictions/self-interaction-knee.md`, `wiki/status/open-problems.md`, `wiki/status/superseded.md`. `wiki/history/timeline.md` line 177 also names flag 17, but it is a dated build row and stays as written. Two more pages cite the flag-17 audit's output, `review/wiki-build-checks/audit/flag17_recompute.out`, for the Born σ_T without a gate and the v0.1 values, not for the flagged statement: `wiki/gravity/spin-2-fields/yukawa-forces.md` (lines 135 and 195 say "the flag-17 audit") and `wiki/dark-matter/halo-astrophysics/transfer-cross-section.md`. They need no change under any option.
- Executed check: `review/wiki-build-checks/gate_conventions.py` only prints. It would move into `verify/` under A or A′; under B, nothing moves.
  - Under A it would assert, symbolically, that e^{−(p₁−p₂)²/2μ²} = (e^{−k²/μ²})² = e^{−v²/v*²} with v* = √2μ/m_χ. It would also assert that #1's benchmark gives μ = m_χv*/√2 ≈ 19.8 keV.
  - Under A′ it would assert that #6's corrected form equals #1's gate.
  - The independent anchor would be the Gaussian-overlap identity, checked by quadrature as in part 4b of `review/wiki-build-checks/audit/flag17_recompute.py`.
  - The script's comment on line 7 calls #6's form "amplitude-level", which #6 itself does not say. That comment has to match the ruling.
- Also: update flag 17's entry in `review/wiki-build-flags.md` and the `gate_conventions.py` row of `review/wiki-build-checks/README.md`. #6 is a "final" calc note in `notes/`, the audit trail.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 18: The year given for baryogenesis's "maturity"

**Audit:** unclear (model memory)

**Where it appears:**
1. `notes/broken-born-theory.md` line 215 (#1 §8).

**Now reads:**
1. `notes/broken-born-theory.md` line 215 (#1 §8):
> Status: a shape, not a mechanism — the same maturity baryogenesis had in 1966.

**Proposed:**
1. No text change until a check decides it. The check: find the publication year of Sakharov's paper stating the conditions for baryogenesis by live search, and record the result as [S]. If the source gives 1967, change "1966" to "1967" in this sentence. If it gives 1966, the flag lapses. The sentence names no work (audit), so the check settles the date of the conditions, not which event the author meant.

**If accepted, also:**
- Wiki pages (6). The search matched "flag 18", "Flag 18", "item(s) 18" and lists that contain 18: `wiki/dark-matter/candidates/polarization-genesis.md`, `wiki/dark-matter/candidates/relic-abundance.md`, `wiki/history/documents/lab-notebook.md`, `wiki/history/documents/source-conflicts.md` (line 68, as conflict C54, "item 18"), `wiki/references.md`, `wiki/status/open-problems.md`. `wiki/history/timeline.md` line 177 also names flag 18, but it is a dated build row and stays as written.
- Executed check: none, because this is a date, not arithmetic.
- Also: the flags file treats the 1967 dating as model memory (†), so the † battery (OP10) is the natural place to record the search. Update flag 18's entry in `review/wiki-build-flags.md`.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 19: Which gate regime the classicality corollary is evaluated in

**Audit:** depends on a convention or reading

**Where it appears:**
1. `notes/stream-stability.md` line 57 (#2, "Corollary (the classicality theorem)"): the broad-gate formula, evaluated "for MW conditions". #2 itself puts the Milky Way in the narrow-gate regime in two places. Line 34 heads Limit 2 as the "MW/cluster regime". The MW row of the table, line 51, is computed with the narrow form, which the audit reproduces.

Four more places use the result as a ceiling ("m ≲ 0.1 meV"). None changes under any option: `papers/broken-born-checkpoint-v2.md` line 99 (#11 §9); `notes/broken-born-program-v1.md` line 80 (#9 §7); `HANDOFF.md` line 51 (§3, artifact #2); `notes/wave-island.md` line 7 (#3). `notes/broken-born-theory.md` line 271 (#1 addendum v0.2) states the corollary without a number.

**Now reads:**
1. `notes/stream-stability.md` line 57 (#2, Corollary):
> At fixed $S \equiv \sigma_0/m$ and halo $(\rho,\sigma)$, the criterion scales as $\sqrt{\pi S}\,\rho\,/(m^{5/2}\sigma^2)$. Setting it to 1 gives $m_{\rm crit} = [\sqrt{\pi S}\,\rho/\sigma^2]^{2/5} \approx 10^{-13}$ GeV $\sim 0.1$ meV for MW conditions. At that mass the per-mode occupation is

**Proposed:**
- Option A states the reading: the number is a ceiling. The change is to `notes/stream-stability.md` line 57:
> At fixed $S \equiv \sigma_0/m$ and halo $(\rho,\sigma)$, the criterion scales as $\sqrt{\pi S}\,\rho\,/(m^{5/2}\sigma^2)$. Setting it to 1 gives $m_{\rm crit} = [\sqrt{\pi S}\,\rho/\sigma^2]^{2/5} \approx 10^{-13}$ GeV $\sim 0.1$ meV for MW conditions (an upper bound: this is the broad-gate form, which the unified criterion never exceeds; the narrow-gate form at fixed $v_*$, which the table above uses for the MW, gives $\approx 4.2\times10^{-14}$ GeV). At that mass the per-mode occupation is
- Option B makes no change. The audit finds that "≈ 10⁻¹³ GeV" and N_occ ≫ 1 hold under both readings. Every later document already uses the number as a ceiling.
- The audit does not choose.
  - Read as a ceiling, the corollary is right. This is the reading of #11 §9, #9 §7, HANDOFF §3 and #3, and #2's own formulas support it.
  - Read as the Milky Way threshold, it is about 3× high: 4.2e-14 GeV against 1.4e-13 GeV. #2's Limit-2 label, its table, and #3's fixed v* = 120 km/s support this reading.
  - Option A writes the ceiling reading into #2.

**If accepted, also:**
- Wiki pages (14). The search matched "flag 19", "Flag 19", "item(s) 19" and lists that contain 19: `wiki/dark-matter/candidates/chi-particles.md`, `wiki/dark-matter/conjugate-matter/benchmark.md`, `wiki/dark-matter/momentum-clumping/_index.md`, `wiki/dark-matter/momentum-clumping/classicality-theorem.md`, `wiki/dark-matter/momentum-clumping/founding-image.md`, `wiki/dark-matter/momentum-clumping/net-theorem.md`, `wiki/dark-matter/wave-dark-matter/_index.md`, `wiki/dark-matter/wave-dark-matter/occupation-number.md`, `wiki/history/main-problems.md`, `wiki/history/documents/clumping-notes.md`, `wiki/notation.md`, `wiki/predictions/island-discriminant.md`, `wiki/status/alive.md`, `wiki/status/open-problems.md`. `wiki/history/timeline.md` lines 170 and 177 also name flag 19, but they are dated build rows and stay as written.
- Executed check: under Option A, it is `review/wiki-build-checks/stream_stability_check.py`, the same script as flag 16. It prints m_crit = 1.4e-13 GeV (broad form) and 4.2e-14 GeV (narrow form, v* fixed). Under Option B there is none. A `verify/` version would assert:
  - those two values, and their ratio ≈ 0.30;
  - N_occ ≫ 1 at both masses;
  - the ceiling property: the unified criterion never exceeds the broad form for σ from 5 to 3000 km/s, as `review/wiki-build-checks/audit/flag19_audit.py` [D] computes.

  It would build its units from the exact SI constants, as that script does.
- Also:
  - Rule on this flag together with flag 16, because they share the script.
  - Outside this flag, the audit found that the broad-form ceiling depends on the halo. For Segue 1 it is 26 meV. So #11 §9's "m ≲ 0.1 meV", which names no halo, "holds for Milky Way conditions only". That point would need its own flag; it is not part of this ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 20: #11 reference [23] pairs one paper's title with another's arXiv number

**Audit:** confirmed (1 independent check)

**Where it appears:**
1. `papers/broken-born-checkpoint-v2.md` line 252 (#11, References, [23]). The entry is cited at line 132 (§12, "[23†]"). That citation needs no change unless the mark changes.

**Now reads:**
1. `papers/broken-born-checkpoint-v2.md` line 252 (#11, References):
> [23]† E. Babichev, L. Marzola, M. Raidal, A. Schmidt-May, F. Urban, H. Veermäe, M. von Strauss, "Bigravitational origin of dark matter," Phys. Rev. D 94, 084055 (2016), arXiv:1607.03497.

**Proposed:**
1. `papers/broken-born-checkpoint-v2.md` line 252. Only the arXiv number changes; the † stays (see "Also"):
> [23]† E. Babichev, L. Marzola, M. Raidal, A. Schmidt-May, F. Urban, H. Veermäe, M. von Strauss, "Bigravitational origin of dark matter," Phys. Rev. D 94, 084055 (2016), arXiv:1604.08564.

**If accepted, also:**
- Wiki pages (9). The search matched "flag 20", "Flag 20", "item(s) 20" and lists that contain 20: `wiki/dark-matter/candidates/bigravity-dark-matter.md`, `wiki/dark-matter/candidates/x-condensate.md`, `wiki/history/documents/checkpoint.md`, `wiki/method/_index.md`, `wiki/method/literature-battery.md`, `wiki/predictions/dark-sector-microstructure.md`, `wiki/references.md`, `wiki/status/alive.md`, `wiki/status/open-problems.md`. The given grep also hits `wiki/_index.md` and `wiki/history/timeline.md`, but only on the date "2026-10-20". Those hits are not about flag 20.
- Executed check: none, because this is a reference.
- Also:
  - #11 needs a version bump past v2.2, with a line in the header's change list. One bump can cover any other accepted #11 flags.
  - The audit's live fetch (arxiv.org/abs/1604.08564; journals.aps.org for PRD 94, 084055) confirmed the authors, title, journal and number. The audit's suggested wording drops the † and puts no mark in its place. #11 marks every reference † or [S], so dropping the † means re-tagging the entry [S] on the strength of the audit's fetch, which would also change "[23†]" at §12 line 132.
  - The arXiv listing's own title is "Gravitational Origin of Dark Matter". The journal title is the one #11 gives.
  - Record the check in the † battery (OP10).

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 21: Ruling 3's overproduction range mixes the referee's integration with an analytic estimate

**Audit:** confirmed (1 independent check)

**Where it appears:**
1. `review/round3-adjudication.md` line 32 (Rulings table, ruling 3, Evidence column).

**Now reads:**
1. `review/round3-adjudication.md` line 32 (ruling 3):
> I did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction).

**Proposed:**
1. `review/round3-adjudication.md` line 32 (the audit's wording). The same cell already names Liveoak–Maharana–Wells in full, and the record abbreviates them LMW in ruling 10:
> I did not re-run the referee's Kibble–Zurek integration (1.1e12–2.2e12 overproduction; the LMW analytic estimate gives 1.2e9–2.2e11).

**If accepted, also:**
- Wiki pages (10). The search matched "flag 21", "Flag 21", "item(s) 21" and lists that contain 21: `wiki/dark-matter/candidates/soliton-candidate/obituary.md`, `wiki/dark-matter/candidates/soliton-candidate/overproduction.md`, `wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor.md`, `wiki/electric-magnetic-duality/monopoles/kibble-mechanism.md`, `wiki/history/documents/source-conflicts.md`, `wiki/method/review/round-3/arbitration.md`, `wiki/method/review/round-3/rulings.md`, `wiki/method/verification/soliton-obituary-script.md`, `wiki/references.md`, `wiki/status/open-problems.md`. The given grep also hits three pages that are not about flag 21: `wiki/_index.md` (the link anchor "…-2026-10-20-and-21"), `wiki/history/timeline.md` (the dates "2026-10-20 and 21" and "2026-10-21") and `wiki/method/literature-battery.md` ("[21][S]").
- Executed check: none, because this is an attribution. The figures are the referee's printed output in `review/round3/referee/step4.out` §3: the Kibble–Zurek rows give 1.14e12–2.22e12 and the LMW eq. (25) rows give 1.24e9–2.16e11. `review/round3/referee/audit-notes.md` line 171 summarizes them.
- Also:
  - Flag 33 edits the same file at lines 12–13 and 150–153, so the edits can go together.
  - The verdict and decision 2 ("probably far more (ruling 3)") are unaffected.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 22: #14 writes Planck's asymmetric N_eff interval as symmetric

**Audit:** confirmed (1 independent check)

**Where it appears:**
1. `notes/knot-dark-matter-standalone.md` line 61 (#14 §4, "Dark radiation").

**Now reads:**
1. `notes/knot-dark-matter-standalone.md` line 61 (#14 §4):
> That is excluded by Planck 2018 (N_eff = 2.99 +- 0.34 at 95%) [23].

**Proposed:**
1. `notes/knot-dark-matter-standalone.md` line 61. The signs are in ASCII, as #14 writes them; the audit's wording uses "−":
> That is excluded by Planck 2018 (N_eff = 2.99 +0.34/-0.33 at 95%) [23].

**If accepted, also:**
- Wiki pages (8). The search matched "flag 22", "Flag 22", "item(s) 22" and lists that contain 22: `wiki/cosmology/early-universe/cosmic-microwave-background.md`, `wiki/cosmology/early-universe/radiation-era.md`, `wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history.md`, `wiki/method/review/round-3/rulings.md`, `wiki/method/verification/soliton-obituary-script.md`, `wiki/predictions/early-universe-step.md`, `wiki/references.md`, `wiki/status/open-problems.md`. The given grep also hits five pages only on the date "2026-10-22": `wiki/history/main-problems.md`, `wiki/history/documents/checkpoint.md`, `wiki/history/documents/lab-notebook.md`, `wiki/history/timeline.md`, `wiki/status/alive.md`. Those hits are not about flag 22.
- Executed check: none. The one number built on this interval is the bound ΔN_eff < 0.286 = 2.99 + 0.34 − 3.044. It uses only the upper side and is already gated (`verify/soliton_obituary.py` lines 95–98).
- Also: #14 is withdrawn and "Kept as the audit trail" (banner, line 3). Paul may prefer to leave #14's text as it is and record the correction only in the flags file. Nothing else changes.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 24: "Square exactly at the bounce" does not say which bounce

**Audit:** confirmed (1 independent check)

**Where it appears:**
- `HANDOFF.md` line 72 (§4, results that exist only in the chat). The diameter relation appears in no other source.
- Not the flagged statement, no change: everywhere else the documents use the word, their "bounce" is the turnaround (`HANDOFF.md` line 23, §2: "turnaround = conjugate bounce"; #1 lines 208 and 263, §7 item 3 and §12; #9 lines 12, 90 and 102, §0, §8 and §9 row 5; #11 lines 107, 168 and 218, §10, §13 row 5 and App. A item 7).

**Now reads:**

`HANDOFF.md` line 72:
> **Phase-space diameter relation:** D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck units) exactly at the bounce; aspect ratio today ~10⁹² = a clock measuring distance from self-duality. Conjecture-tier; candidate for a future note.

**Proposed:**

`HANDOFF.md` line 72 (the audit's wording):
> **Phase-space diameter relation:** D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck units) where a = ã, near 10⁻⁴⁶ of today's scale factor — not at the turnaround (the conjugate bounce), where it is most elongated; aspect ratio today ~10⁹² = a clock measuring distance from self-duality. Conjecture-tier; candidate for a future note.

The 10⁻⁴⁶ figure is the audit's arithmetic. It assumes D_x ∝ a and uses N ~ 10⁹⁰ and D_x today ~ 8.7×10⁶⁰ Planck lengths. The script behind it (`audit_checks.py`, named in the audit's evidence) was not kept: it is in neither `review/wiki-build-checks/` nor the scratchpad. Under the iron rule, either re-run that arithmetic and keep it, or use the number-free form below. That form also drops "where a = ã", an identification the audit's wording adds; "self-duality" is the handoff's own word, in the same sentence:
> **Phase-space diameter relation:** D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck units) at self-duality, not at the turnaround (the conjugate bounce), where it is most elongated; aspect ratio today ~10⁹² = a clock measuring distance from self-duality. Conjecture-tier; candidate for a future note.

**If accepted, also:**
- Wiki pages (6): `wiki/cosmology/scale-factor-duality/conjugate-bounce.md`, `wiki/cosmology/scale-factor-duality/phase-space-diameter.md`, `wiki/gravity/spin-2-fields/planck-units.md`, `wiki/history/documents/handoff.md`, `wiki/status/conjectures.md`, `wiki/status/open-problems.md`. The task grep returns 5 files, with 2 false hits: `wiki/history/timeline.md` (the time "23:24") and `wiki/method/literature-battery.md` ("[24][S]", flag 9's subject). It misses conjugate-bounce, handoff and open-problems, which write "item 24" or "Flag 24". 5 pages quote "exactly at the bounce".
- Executed check: none for the wording (`review/wiki-build-checks/README.md` lists no script for flag 24). If the 10⁻⁴⁶ figure is kept, a new script in `verify/` would assert D_x·D_p ~ 10³⁰ per dimension in Planck units, aspect ratio today ~10⁹², and a square at a/a₀ ~ 10⁻⁴⁶.
- Also: `HANDOFF.md` is the record of the move from claude.ai. If Paul prefers not to edit it, the correction can go into the queued phase-space-diameter note instead (CLAUDE.md queue item 1; HANDOFF §8 item 7). This entry depends on flag 27: under its Option B there is no turnaround, and the "not at the turnaround" clause goes.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 25: #1 points to §7 for the cosmological constraint, which §6 derives

**Audit:** confirmed (1 independent check)

**Where it appears:**
- `notes/broken-born-theory.md` line 25 (§1, P2).
- `notes/broken-born-theory.md` line 116 (§4, Ghost accounting).

**Now reads:**

`notes/broken-born-theory.md` line 25:
> This single postulate does triple duty below: it kills the would-be second graviton (no Boulware–Deser ghost, §6), it enforces the cosmological constraint $a\tilde a = \text{const}$ (§7), and it supplies the explicit breaking that gives the dark-energy field its potential (§5).

`notes/broken-born-theory.md` line 116:
> **Ghost accounting.** There is no second independent metric: $\tilde g$'s cosmological mode is eliminated by the P2 constraint (§7), so no Boulware–Deser sector arises in minisuperspace. **[D]**

**Proposed:**

`notes/broken-born-theory.md` line 25 (the audit's wording; only "(§7)" changes):
> This single postulate does triple duty below: it kills the would-be second graviton (no Boulware–Deser ghost, §6), it enforces the cosmological constraint $a\tilde a = \text{const}$ (§6), and it supplies the explicit breaking that gives the dark-energy field its potential (§5).

The same sentence's "(§5)" for the potential, which is in §3, is flag 10's first item. Rule on the two together; this entry leaves it alone.

`notes/broken-born-theory.md` line 116:
> **Ghost accounting.** There is no second independent metric: $\tilde g$'s cosmological mode is eliminated by the P2 constraint (§6), so no Boulware–Deser sector arises in minisuperspace. **[D]**

**If accepted, also:**
- Wiki pages (7): `wiki/cosmology/scale-factor-duality/cosmological-constraint.md`, `wiki/gravity/momentum-graviton/forcing-chain.md`, `wiki/gravity/tuning-test/geometric-action.md`, `wiki/history/documents/lab-notebook.md`, `wiki/history/documents/source-conflicts.md` (entry C21, shared with flag 10), `wiki/program/postulates/original-p2.md`, `wiki/status/open-problems.md`. The task grep returns 3 files, all real; the other 4 write "item 25" or "Flag 25". 4 pages quote the "(§7)" pointer: forcing-chain, geometric-action, lab-notebook, original-p2.
- Executed check: none (wording only).
- Also: #1 is the superseded lab notebook, kept as the audit trail (root `CLAUDE.md`, Layout). Paul may prefer an erratum line to an edit.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 26: The handoff calls DESI DR3 "three-year data"

**Audit:** confirmed (1 independent check)

**Where it appears:**
- `HANDOFF.md` line 44 (§2, External clock). No other source gives DR3's data span.
- Not the flagged statement, no change: the other DR3 mentions (#1 lines 229, 275; #9 line 101; #11 lines 107, 167, 218; `notes/ufd-endpoint.md` line 43; root `CLAUDE.md` line 44).

**Now reads:**

`HANDOFF.md` line 44:
> **External clock:** DESI DR3 (three-year data, expected late 2026).

**Proposed:**

`HANDOFF.md` line 44 (the audit's wording):
> **External clock:** DESI DR3 (the release after DR2's three-year data, expected late 2026).

The audit's evidence is a live fetch of the abstract of [21S] (arXiv:2503.14738), which says DR2 is "based on three years of operation". "Expected late 2026" is the handoff's own date and is not part of this flag.

**If accepted, also:**
- Wiki pages (8): `wiki/cosmology/dark-energy/desi-dr2-phantom-crossing.md`, `wiki/cosmology/dark-energy/desi.md`, `wiki/history/documents/handoff.md`, `wiki/method/literature-battery.md`, `wiki/predictions/dark-energy-drift.md`, `wiki/program/assessment.md`, `wiki/references.md`, `wiki/status/open-problems.md`. The task grep returns 4 files, with 1 false hit: `wiki/history/timeline.md` ("now holds 26 items"). It misses 5 pages that write "item 26" or "Flag 26". 8 pages quote "three-year data".
- Executed check: none (wording only).
- Also: the same note on editing `HANDOFF.md` as for flag 24.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 29: #13 cites #11 §7 for a range "in momentum"

**Audit:** confirmed (1 independent check)

**Where it appears:**

- `papers/conjugate-special-relativity.md` line 26 (#13 §1)
- `papers/conjugate-special-relativity.md` line 85 (#13 §6)
- The momentum reading has one source, `HANDOFF.md` line 75 (§4, chat-only): "dual Newtonian limit = Yukawa in momentum = the gate". #11 §7.5 (line 81) and #8 §3 (line 34) say "Yukawa-cut at 1/M_X", which is a range in position. #13 §6's plain-language passage (line 83, "theirs is short-ranged") restates the claim without a tag.

**Now reads:**

`papers/conjugate-special-relativity.md` line 26 (#13 §1):

> One refinement from the main program: the dual cone is the causal structure of the *slaved* geometry g⁻¹; the independently dynamical part of momentum-space geometry is the massive field X, which modifies the dual cone only at short range in momentum [D — §7 of the checkpoint].

`papers/conjugate-special-relativity.md` line 85 (#13 §6):

> Broken: the long-range/short-range asymmetry — our null structure is policed by massless gravity, the dual structure's dynamical part by the massive X, so dual-geometric effects are Yukawa-cut in momentum [D — checkpoint §7].

**Proposed:** This is the audit's suggested tag. Only the tag changes.

`papers/conjugate-special-relativity.md` line 26 (#13 §1):

> One refinement from the main program: the dual cone is the causal structure of the *slaved* geometry g⁻¹; the independently dynamical part of momentum-space geometry is the massive field X, which modifies the dual cone only at short range in momentum [O — chat-only, HANDOFF §4; not in the checkpoint].

`papers/conjugate-special-relativity.md` line 85 (#13 §6):

> Broken: the long-range/short-range asymmetry — our null structure is policed by massless gravity, the dual structure's dynamical part by the massive X, so dual-geometric effects are Yukawa-cut in momentum [O — chat-only, HANDOFF §4; not in the checkpoint].

A narrower variant keeps the [D] and changes only the pointer, to "[D — chat-only, HANDOFF §4]" in both places. HANDOFF §4 lists the result untagged, under results that exist "ONLY in the chat (not in any artifact)", so no document records its derivation. Either way, the current tag points to a section that does not contain the claim.

**If accepted, also:**

- Wiki pages (14): `wiki/conjugate-relativity/_index.md`, `wiki/conjugate-relativity/equivalence-principle.md`, `wiki/conjugate-relativity/two-causal-cones.md`, `wiki/gravity/momentum-graviton/chat-only-results.md`, `wiki/gravity/momentum-graviton/fifth-force-safety.md`, `wiki/gravity/spin-2-fields/yukawa-forces.md`, `wiki/history/documents/handoff.md`, `wiki/history/documents/source-conflicts.md`, `wiki/method/_index.md`, `wiki/method/provenance-tags.md`, `wiki/phase-space/born-geometry/compatibility-corollaries.md`, `wiki/status/alive.md`, `wiki/status/conjectures.md` and `wiki/status/open-problems.md`. The requested grep misses `handoff.md` and `source-conflicts.md`, which cite "item 29", and `open-problems.md`, which writes "Flag 29".
- Executed check: none (wording only).
- Also:
  - #13 has no version line and has not been edited since the import.
  - Flags 29 and 30 and the open #13 item in `review/v3-worklog.md` (lines 149–150, "fix #13's two cones and settle which construction governs") all concern #13 §1. One #13 revision could carry all three.
  - The flag's entry in `review/wiki-build-flags.md` needs updating.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 30: The tag on #13's two causal cones

**Audit:** depends on a convention or reading

**Where it appears:**

- `papers/conjugate-special-relativity.md` line 14 (#13 §1). The convention in question is #13's header (line 4): "The Euclidean/Lorentzian caveat of the main checkpoint is inherited throughout." The theorem takes g ∈ Sym⁺(d) (#11 §5, line 55). The Lorentzian dressing is open (#11 §14 item 3, line 186).

**Now reads:**

`papers/conjugate-special-relativity.md` line 14 (#13 §1):

> The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. Each metric defines a null cone.

**Proposed:**

Option A states the convention at the cone sentence itself:

> The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. With g taken Lorentzian, each metric defines a null cone [O — the Lorentzian dressing, checkpoint §14 item 3].

Option B makes no change. The header caveat covers the sentence.

The audit does not choose between them. It finds the tag accurate where it sits, on H = diag(g, g⁻¹), which the theorem gives. It notes that the untagged cone sentence presumes a Lorentzian g, and it calls the question of whether the header's blanket caveat is enough "a tagging-convention call".

**If accepted, also:**

- Wiki pages (14). The `wiki/history/timeline.md` row is history and stays. The pages are `wiki/conjugate-relativity/_index.md`, `wiki/conjugate-relativity/special-relativity.md`, `wiki/conjugate-relativity/two-causal-cones.md`, `wiki/conjugate-relativity/two-cones-inconsistency.md`, `wiki/history/documents/source-conflicts.md`, `wiki/history/timeline.md`, `wiki/method/_index.md`, `wiki/method/provenance-tags.md`, `wiki/phase-space/born-geometry/born-structures.md`, `wiki/phase-space/born-geometry/compatibility-corollaries.md`, `wiki/phase-space/born-geometry/compatibility-theorem.md`, `wiki/phase-space/born-geometry/lorentzian-dressing.md`, `wiki/status/alive.md` and `wiki/status/open-problems.md`. The requested grep misses `two-cones-inconsistency.md` ("Flag 30"), `source-conflicts.md` ("item 30") and `open-problems.md`. Its hit on `wiki/dark-matter/halo-astrophysics/transfer-cross-section.md` ("30·exp") is not about the flag.
- Executed check: none (wording only).
- Also:
  - The audit adds a side note: #13's "[D]" on the theorem is itself stale. #11 §5 has tagged the theorem [T][V] (Freidel–Leigh–Minic) since v2.1. Fixing that tag is a separate one-tag change, and either option could carry it.
  - #13 has not been edited since the import. Flag 29's entry suggests one combined #13 revision.
  - The flag's entry in `review/wiki-build-flags.md` needs updating.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 31: "~10 orders" below sensitivity for quadratic photon dispersion

**Audit:** depends on a convention or reading. The flag calls it a lead resting on a † bound; the audit then retrieved the bound by live search [S].

**Where it appears:**
- `notes/broken-born-theory.md` line 110 (§4, No linear Lorentz violation). This is the only source that gives a figure.
- Not the flagged statement, no change: row 9 in #1 (line 233), #9 (line 106) and #11 (line 172), which give no number; #13 line 85 (§6), which cites the Fermi-LAT bounds for linear dispersion only.

**Now reads:**

`notes/broken-born-theory.md` line 110:
> Fermi-LAT gamma-ray-burst bounds exclude linear Planck-scale dispersion; quadratic effects at $M_B \sim M_P$ sit $\sim 10$ orders below current sensitivity. Consistent. **[T]**

**Proposed:** the audit leans to Option A. It offers the rewrite below as the clarifying fix, and it finds:
- The words "effects … below sensitivity" suggest the size of the effect. On that reading the gap is 14.5–17 orders, so "~10" is wrong.
- Counted in the energy scale, the way Lorentz-violation limits are quoted, the gap is 8.0–8.6 orders (7.3–7.9 with #1's reduced M_P), so "~10" holds only loosely.
- "Consistent" survives either reading.

*Option A: name the measure.* This is the audit's clarifying rewrite, in #1's notation:
> Fermi-LAT gamma-ray-burst bounds exclude linear Planck-scale dispersion; quadratic effects at $M_B \sim M_P$ sit $\sim 8$ orders in the energy scale ($\sim 16$ in the size of the effect) below current sensitivity. Consistent. **[T]**

The figures use the Fermi-LAT gamma-ray-burst bound E_QG,2 > 1.3×10¹¹ GeV (Vasileiou et al., PRD 87, 122001, 2013, which the audit retrieved [S]) and the unreduced Planck mass. With #1's reduced M_P they are 7.3 and 14.5. With LHAASO's 2024 bound, which the audit also retrieved, they are 6.5–7.2 and 13.0–14.4.

*Option B: no change.* "~10" stays, read as a coarse rounding of the energy-scale gap.

When ruling, name the option (A or B) in the notes.

**If accepted, also:**
- Wiki pages (5): `wiki/gravity/spin-2-fields/planck-units.md`, `wiki/history/documents/lab-notebook.md`, `wiki/predictions/photon-dispersion.md`, `wiki/references.md`, `wiki/status/open-problems.md`. The task grep returns 4 files. The 4th, `wiki/history/timeline.md`, names it only in a dated log row, which a ruling would not edit. The grep misses photon-dispersion and open-problems, which write "Flag 31". The same 5 pages quote the "~10 orders" figure. Six other pages quote a different "~10 orders", the clumping problem's Scenario B streams "tunable across ~10 orders", which this flag does not concern.
- Executed check: `review/wiki-build-checks/quadratic_gap.py`, which only prints. Its header still marks the bound †. In `verify/` it would assert, for E_QG,2 = 1.3×10¹¹ GeV [S], an energy-scale gap of log₁₀(M_P/E_QG,2) ≈ 8.0 (7.3 with reduced M_P) and twice that for the effect. Its anchor, independent of #1, is `review/wiki-build-checks/audit/flag31_audit.py`. That script reproduces the Fermi-LAT paper's own κ₁ = 1.03, κ₂ = 1.50 and E_QG,2 = 3.3×10¹⁰ GeV from τ₂; the source text is `audit/vasileiou2013.txt`.
- Also: none outside #1; #11 gives no number.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 32: CMB-S4, named as row 10's probe, may have lost its funding

**Audit:** unclear (model memory); the flag itself calls it a lead, not a source error.

**Where it appears:**
- `papers/broken-born-checkpoint-v2.md` line 173 (§13 row 10)
- `notes/broken-born-program-v1.md` line 107 (§9 row 10)
- `notes/broken-born-theory.md` line 234 (§9 row 10)
- `review/skeptic-review-console.html` line 63: §4 of the withdrawn #14, as embedded in the console. The flag and the audit do not list it.

**Now reads:**

`papers/broken-born-checkpoint-v2.md` line 173:
> | 10 | Early universe | Standard G, N_eff | Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff | (Knob-bounded; CMB-S4 probes) |

`notes/broken-born-program-v1.md` line 107:
> | 10 | Early universe | Standard G, N_eff | Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff | (Bounds constrain knobs; CMB-S4 probes) |

`notes/broken-born-theory.md` line 234:
> | 10 | Early universe | Standard $G$, $N_{\rm eff}$ | $a^{-6}$ step in $G_{\rm eff}$; optional negative $\Delta N_{\rm eff}$ from closed dual curvature; conditional step in primordial GW spectrum | (Bounds constrain knobs; CMB-S4 $N_{\rm eff}$ at ±0.03 probes the curvature term) |

`review/skeptic-review-console.html` line 63:
> Relativistic dual-sector radiation from the transition contributes dark radiation, and a closed dual-curvature term contributes negatively: a Delta N_eff signature within reach of CMB-S4 for favorable parameters.

**Proposed:** no text change until CMB-S4's current status has been checked against a live source and recorded [S]. That check is part of the † literature battery (#11 §14 item 10; current queue item 1). If the status has changed, Paul rules separately on what row 10 names in #11, #9 and #1. The console's copy of the withdrawn #14 needs no change. Here "accept" means: run the check.

**If accepted, also:**
- Wiki pages (11): `wiki/cosmology/early-universe/big-bang-nucleosynthesis.md`, `wiki/cosmology/early-universe/cosmic-microwave-background.md`, `wiki/cosmology/early-universe/phase-transition-gravitational-waves.md`, `wiki/cosmology/early-universe/radiation-era.md`, `wiki/cosmology/scale-factor-duality/duality-dictionary.md`, `wiki/history/documents/checkpoint.md`, `wiki/predictions/_index.md`, `wiki/predictions/early-universe-step.md`, `wiki/predictions/table-history.md`, `wiki/references.md`, `wiki/status/open-problems.md`. The task grep returns 12 files. 2 are not pointers: `wiki/_index.md` ("32 were confirmed", a count) and `wiki/history/timeline.md` (a dated log row). It misses `wiki/history/documents/checkpoint.md` ("items … 32" and "Item 32"). open-problems matched only on a count, but it also points to the flag as "Flags 20 and 32" and "Flag 32".
- Executed check: none; this is a literature check, not arithmetic.
- Also: the result and its source go into the † battery's record.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 35: The round-3 pre-registration cites the wrong handoff section for the 2-for-2 record

**Audit:** confirmed (1 independent check)

**Where it appears:**
1. `review/round3-preregistration.md` lines 4–5 (opening paragraph). The same file's line 16 cites "(HANDOFF §6, round 3)" for the protocol, which is correct.

**Now reads:**
1. `review/round3-preregistration.md` lines 4–5:
> prediction cannot be fitted to the outcome. Rounds 1 and 2 were pre-registered
> the same way and scored 2 for 2 on verdicts (HANDOFF §6).

**Proposed:**
1. `review/round3-preregistration.md` lines 4–5 (the audit's wording):
> prediction cannot be fitted to the outcome. Rounds 1 and 2 were pre-registered
> the same way and scored 2 for 2 on verdicts (HANDOFF §5).

**If accepted, also:**
- Wiki pages (5). The search matched "flag 35", "Flag 35", "item(s) 35" and lists that contain 35: `wiki/history/documents/handoff.md`, `wiki/method/review/pre-registration.md`, `wiki/method/review/round-3/preregistration.md`, `wiki/method/review/rounds-one-and-two.md`, `wiki/status/open-problems.md`. `wiki/history/timeline.md` line 177 also names flag 35, but it is a dated build row and stays as written.
- Executed check: none, because this is a pointer.
- Also:
  - The record itself is `HANDOFF.md` line 83 (§5): "scored 2-for-2 on verdicts".
  - The file is the pre-registration committed before the review was dispatched (cc05705). Git keeps the original, and the edit touches only the pointer, not the prediction.
  - Update flag 35's entry in `review/wiki-build-flags.md`.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 36: The figures 66.58 and 63.72 placed in a section that does not print them

**Audit:** confirmed (1 independent check)

**Where it appears:**

1. `verify/battery.py` lines 12–14 (module docstring)
2. `papers/broken-born-checkpoint-v2.md` line 75 (§7.2)

The figures appear in `HANDOFF.md` line 84 (§5) and in #11 line 75 (§7.2) itself. #11 line 25 (§2) prints only "rms residual 3.29".

**Now reads:**

(1) `verify/battery.py` lines 12–14:

> The computations, seeds and RNG call order are Appendix A's, unchanged, so
> the printed figures are the ones quoted in papers/broken-born-checkpoint-v2.md
> §2 (66.58 vs 63.72; rms 3.29). Those quoted figures are checked as well

(2) `papers/broken-born-checkpoint-v2.md` line 75:

> (non-FP at linear order — the 66.58-vs-63.72 test of §2)

**Proposed:**

(1) The docstring, in the audit's wording and the file's line layout. Line 15 continues unchanged with `("parity"): …`.

> The computations, seeds and RNG call order are Appendix A's, unchanged, so
> the printed figures are the ones quoted in HANDOFF.md §5 and
> papers/broken-born-checkpoint-v2.md §7.2 (66.58 vs 63.72) and §2 (rms 3.29).
> Those quoted figures are checked as well

(2) Line 75, in the audit's wording without its inner parentheses:

> (non-FP at linear order — the 66.58-vs-63.72 battery test T4, described in §2)

**If accepted, also:**

- Wiki pages (9):
  - `wiki/method/verification/battery.md`
  - `wiki/gravity/tuning-test/metric-tier-failures.md`
  - `wiki/gravity/spin-2-fields/fierz-pauli.md`
  - `wiki/method/claim-tiers.md`
  - `wiki/history/documents/checkpoint.md`
  - `wiki/history/documents/handoff.md`
  - `wiki/history/documents/source-conflicts.md`
  - `wiki/history/timeline.md` (build-history row; the ruling adds a row)
  - `wiki/status/open-problems.md`

  The task's grep finds 7 of these; the other 2 use the "Flag 36" or "item 36" forms.
- Executed check: none (wording only). The docstring edit leaves every check in `verify/battery.py` unchanged, including "T4 parity: 66.58 vs 63.72 as quoted". Re-run `scripts/check.sh` after the edit.
- Also:
  - #11 needs a changelog line; with the other #11 edits, a v2.3.
  - The flag's entry in `review/wiki-build-flags.md` records the ruling.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 37: The README still says "missing magnetic monopoles"

**Audit:** confirmed (1 independent check)

**Where it appears:**

- `README.md` line 2, the repository's one-line description. Three places in the record contradict it: `HANDOFF.md` §2 (line 31, under "Dead"), #11 §11.1 (line 115, "As an explanation of the null result: dead") and #11 Appendix A item 5 (line 216).

**Now reads:**

`README.md` line 2:

> Physics hypothesis explaining dark matter and missing magnetic monopoles

**Proposed:** This is the audit's suggested wording.

`README.md` line 2:

> Physics hypothesis about dark matter, from spontaneously broken Born reciprocity

A narrower variant deletes only " and missing magnetic monopoles".

**If accepted, also:**

- Wiki pages (7): `wiki/electric-magnetic-duality/monopole-explanation.md`, `wiki/history/documents/project-instructions.md`, `wiki/history/timeline.md` (its initial-commit row carries a pointer that would need updating), `wiki/predictions/monopole-null.md`, `wiki/program/_index.md`, `wiki/status/open-problems.md` and `wiki/status/superseded.md`. The requested grep misses `open-problems.md`.
- Executed check: none (wording only).
- Also:
  - The GitHub description of the public repository `Reinholdtsen/conjugate-matter` carries the same line; `gh repo view` read it on 2026-10-22. It lives outside the repository, and `gh repo edit --description` would change it.
  - The flag's entry in `review/wiki-build-flags.md` needs updating.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 38: Stale details in the root CLAUDE.md and the gate's header

**Audit:** confirmed (1 independent check)

**Where it appears:**

- `CLAUDE.md` line 41 ("Since the handoff") says "#11 is now v2.1". #11 itself says "Version 2.2" (line 4), and `CLAUDE.md` line 46 cites "#11 v2.2".
- `CLAUDE.md` line 27 (Layout) names only `battery.py` and `soliton_obituary.py`, but `scripts/check.sh` line 21 runs six scripts; it also runs `toy_coset.py`, `toy_gw.py`, `toy_s4.py` and `toy_s5.py`. The same line says that arbitration and audit scripts go in `verify/`.
- `scripts/check.sh` line 4 (header) says the same of arbitration and audit scripts. The round arbitration scripts are `review/round3/adjudicator/round3_arb.py`, `review/round4/adjudicator/arb.py` and `review/round4/adjudicator/ctrl.py`, and `scripts/check.sh` runs none of them.

**Now reads:**

`CLAUDE.md` line 41:

> #11 is now v2.1: soliton obituary (§12); compatibility theorem re-tagged

`CLAUDE.md` line 27:

> [verify/](verify/) — `battery.py` (HANDOFF Appendix A); `soliton_obituary.py` (the round-3 record); arbitration and audit scripts go here.

`scripts/check.sh` line 4:

> `# script fails. New arbitration and audit scripts in verify/ get added here.`

**Proposed:**

`CLAUDE.md` line 41 (the rest of the bullet stays as it is; rewrap):

> #11 is now v2.2. Its v2.1 changes: soliton obituary (§12); compatibility theorem re-tagged

`CLAUDE.md` line 27 (the audit's wording for the arbitration scripts; "audit scripts go here", which the flag does not question, stays):

> [verify/](verify/) — `battery.py` (HANDOFF Appendix A); `soliton_obituary.py` (the round-3 record); `toy_coset.py`, `toy_gw.py`, `toy_s4.py`, `toy_s5.py` (the toy Lagrangian); audit scripts go here. Round arbitration scripts live in `review/roundN/adjudicator/` and are not gated.

`scripts/check.sh` line 4:

> `# script fails. New verification scripts in verify/ get added here.`

The last point has another resolution: keep both texts as they are and move the three arbitration scripts into `verify/` and the gate. Those scripts only print; none of the three contains an assert or exit call, so they would need assertions before they could fail the gate. The audit's wording takes the first resolution.

**If accepted, also:**

- Wiki pages (11). The three `wiki/history/timeline.md` rows are history and stay. The pages are `wiki/history/documents/checkpoint.md`, `wiki/history/documents/project-instructions.md`, `wiki/history/documents/source-conflicts.md`, `wiki/history/timeline.md`, `wiki/method/review/review-protocol.md`, `wiki/method/review/round-3/arbitration.md`, `wiki/method/review/round-4.md`, `wiki/method/verification/iron-rule.md`, `wiki/method/verification/the-gate.md`, `wiki/status/open-problems.md` and `wiki/status/superseded.md`. The requested grep misses `source-conflicts.md` ("item 38") and `open-problems.md`.
- Executed check: none under the audit's wording. Under the other resolution, the three arbitration scripts move into `verify/` and `scripts/check.sh` once they assert their results.
- Also:
  - `wiki/CLAUDE.md` makes the root `CLAUDE.md`'s "Since the handoff" the wiki's highest-precedence source, so the stale version sits at the top of the wiki's precedence order.
  - A related line is not flagged: the iron rule (`CLAUDE.md` lines 74–75) also says that executed code is "kept in `verify/`". Paul should read the choice of resolution against it.
  - The flag's entry in `review/wiki-build-flags.md` needs updating.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 40: "Bounded only at frozen H" in the root CLAUDE.md

**Audit:** depends on a convention or reading (both of 2 checks)

**Where it appears:**

- (1) `CLAUDE.md` lines 85–86, in the reduced-model rule under 'Method (HANDOFF §5)'. The bullet spans lines 83–86. According to the audit, it was added with the round-4 adjudication in commit e3ce9eb.
- The adjudication's own version of this lesson, `review/round4-adjudication.md` lines 60–62, does not contain the sentence.

**Now reads:**

(1) `CLAUDE.md` lines 83–86:

> - When numerics run on a reduced model (fields frozen), check the unreduced
>   model's stability — boundedness, and the Hessian with all fields dynamical —
>   and say in the text that it is a reduction. Round 4 found a potential that
>   was bounded only at frozen H.

**Proposed:**

Both auditors confirm the flag's mathematics. Hold H at 1 but let K move freely on its hyperboloid. Then the naive potential is V = −4μ + 4μu² + (λ − 4μ)t². At the gated couplings λ = μ = 1 it is unbounded below: the frozen-H Hessian has eigenvalue −6, and V = −30004 at t = 100. It is bounded in that setting only when λ ≥ 4μ.

The sentence is right under the documents' own "frozen-H reduction": H = 1 with K kept on its circle K(φ). There V = −2μ(1 + cos 2φ), which stays within [−4μ, 0].

Neither auditor proposes wording, so the audit **states no preference between A and B**. One auditor adds that at λ = μ = 1 the reduction also freezes an unstable K mode, which no source mentions.

- **Option A (state the convention):**

  > - When numerics run on a reduced model (fields frozen), check the unreduced
  >   model's stability — boundedness, and the Hessian with all fields dynamical —
  >   and say in the text that it is a reduction. Round 4 found a potential that
  >   was bounded only at frozen H (the frozen-H reduction: H = 1, with K held on
  >   its circle K(φ)).

  If Paul wants the rule to carry the flag's point too, A could add that with only H frozen the potential is also unbounded at λ = μ = 1. That finding is the flag's, made later than round 4.
- **Option B:** no change.

**If accepted, also:**

- Wiki pages (6):
  - `wiki/history/documents/project-instructions.md`
  - `wiki/method/verification/reduced-model-stability.md`
  - `wiki/status/open-problems.md`
  - `wiki/symmetry-breaking/toy-models/coset-model/bounded-potential.md`
  - `wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction.md`
  - `wiki/symmetry-breaking/toy-models/coset-model/naive-potential.md`

  `wiki/history/timeline.md` lines 174 and 177 name flag 40 in dated commit rows, which are history and need no edit.
- Executed check: move `review/wiki-build-checks/frozen_h_naive.py` into `verify/`, for example into `verify/toy_coset.py`, whose chart and V_λ it reuses. A new file would also need adding to the script list on line 21 of `scripts/check.sh`. The script only prints today. In the gate it would assert:
  - at H = 1, V = (λ − 4μ)t² + 4μu² − 4μ exactly;
  - the frozen-H Hessian at K_ref is diag(8μ, 2λ − 8μ), which gives (8, −6) at λ = μ = 1;
  - V(t = 100) = −30004 there;
  - on the circle (t = 0), V = 4μ(u² − 1), within [−4μ, 0].

  Independent anchors, as the auditors used: K² + det K·1 = 0 (Cayley–Hamilton) and KᵀωK = det K·ω. The full audit checks, including grid minima and the λ ≥ 4μ threshold, are in `review/wiki-build-checks/audit/flag40_recompute.py` and `flag40_audit.py`.
- Also:
  - `CLAUDE.md` holds Paul's own instructions, so any edit there is his call.
  - Outside this flag, one auditor noticed related wording elsewhere. The toy note (abstract, §4), #11 §10 and adjudication F2 attribute the naive potential's instability to H being dynamical. At λ = μ = 1 the −6.47 saddle is mostly a K direction (94.7%), so that attribution holds only for λ ≥ 4μ. The statements are still true as written, since with H dynamical the potential is unbounded for every λ. No change is proposed.

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

### Flag 44: "Without the gauge invariance" (#6 §2)

**Audit:** not yet audited (raised after the audit by one page verifier)

**Where it appears:** `notes/x-classification.md` line 21 (§2)

**Now reads:**
> Without the gauge invariance, no ghost-free two-derivative kinetic term for a Lorentz-covariant symmetric tensor exists (mixed time–space components enter with the wrong sign under any invariant contraction; this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all). [T — standard]

**Proposed:**
> Without a gauge invariance, no ghost-free two-derivative kinetic term for a Lorentz-covariant symmetric tensor exists (…). [T — standard]

Option A: the one-word change above ("the" → "a"), which keeps the conclusion and admits the
smaller transverse-diffeomorphism-plus-Weyl symmetry of linearized unimodular gravity. Option B: no
change. Before ruling, the two † references should be checked (they are from model memory).

**If accepted, also:**
- Wiki pages (1): `wiki/gravity/spin-2-fields/signature-obstruction.md` (its "full gauge symmetry against none" bullet).
- Executed check: none (wording only).
- Also: add the two references to the † literature battery (OP10).

**Ruling:** ☐ accept ☐ reject ☐ modify — notes:

