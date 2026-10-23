---
title: "Partially massless gravity"
weight: 80
status: established
description: "A massive spin-2 field on de Sitter space at the mass where a gauge symmetry removes its helicity-0 mode, and the bimetric parameter point studied as partially massless bimetric gravity, which lies inside the program's palindromic branch at α = 1."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §14 item 2"
  - "papers/broken-born-checkpoint-v2.md ref [24]"
  - "papers/broken-born-checkpoint-v2.md ref [25]"
  - "HANDOFF.md §2"
  - "HANDOFF.md §8"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md ref [6]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "review/wiki-build-flags.md item 9"
---

*Partially massless gravity is a spin-2 field on [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space), the spacetime of a universe expanding at a constant rate under a positive [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant), whose mass takes the one value at which an extra gauge symmetry appears and removes the field's helicity-0 polarization [T]. That value is the edge of the [Higuchi bound](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-higuchi-bound), below which a massive spin-2 field on de Sitter space carries a [ghost](/wiki/gravity/spin-2-fields/ghosts#the-higuchi-ghost). [Bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) has a parameter point, studied as partially massless bimetric gravity, at which the theory has de Sitter solutions in which the two metrics are proportional, with a ratio that the equations leave undetermined, and its potential is symmetric under exchange of the two metrics. The point matters to the program because at α = 1, which in the literature's usual notation means equal [Planck masses](/wiki/gravity/spin-2-fields/planck-units#two-metrics-two-planck-masses) for the two metrics, it lies inside the [palindromic branch](/wiki/gravity/palindromic-branch) that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) selects. That raises the open question whether reciprocity is the origin of the partially massless symmetry, and it means the program's [vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) must be compared with this literature before it can be called new.*

**Status:** Established — [T] — the linear theory is standard, and the bimetric parameter point is cited in the [checkpoint](/wiki/history/documents/checkpoint) as [24S], retrieved by live search. Its relation to the program is open: whether reciprocity is the origin of the partially massless symmetry is [O], part of open problem 2 of #11 §14, [the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison).

## A massive spin-2 field on de Sitter space

### De Sitter space

[De Sitter space](/wiki/cosmology/dark-energy/de-sitter-space) is the spacetime of a universe expanding at a constant Hubble rate H under a positive cosmological constant Λ = 3H² [T], the relation [the round-3 audit](/wiki/method/review/round-3/rulings) uses to convert Higuchi's bound below (`review/round3/referee/audit-notes.md`, Step 1). On this page H is the Hubble rate, not the program's phase-space metric H.

### Five polarizations

A massive spin-2 field in four dimensions has five polarizations — [calc note #6](/wiki/history/documents/debt-1-notes) counts "its five polarizations" for the [momentum graviton X](/wiki/gravity/momentum-graviton) (#6 §3) — with helicities ±2, ±1 and 0 [T]. A massless graviton keeps only the helicity ±2 pair; its gauge symmetry, linearized diffeomorphisms, removes the others [T] ([general relativity and the graviton](/wiki/gravity/spin-2-fields/general-relativity)).

### The Higuchi bound

In flat space any positive mass is allowed. On de Sitter space a massive spin-2 field must satisfy the Higuchi bound [T]:

```text
m² ≥ 2H²
```

The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) cites it as reference [6], A. Higuchi, Nucl. Phys. B 282, 397 (1987). The round-3 audit read the bound from Higuchi's abstract, "M^2 cannot be between 0 and 2/3 x (cosmological constant)", converted it with "Lambda = 3H^2" to "m^2 >= 2H^2", and found that the reference supports the statement (audit notes, Step 1).

For masses between zero and the bound, the helicity-0 polarization has negative norm: it is a ghost, and the theory is not unitary [T]. A field much heavier than H satisfies the bound trivially, which is how #14 treated the momentum graviton; see [the Higuchi bound under bimetric cosmology](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-higuchi-bound).

### The partially massless value

At the edge of the bound, m² = 2H², the field's linear equations acquire a scalar gauge symmetry [T]:

```text
δh_μν = (∇_μ∇_ν + H² g_μν) ξ          (ξ any function; mostly-plus sign convention)
```

Here h_μν is the spin-2 field, g_μν the de Sitter metric and ∇ its covariant derivative. The symmetry removes the helicity-0 polarization, so the field propagates helicities ±2 and ±1 only. It has a mass and more polarizations than a massless graviton, yet it carries a gauge symmetry as a massless field does: hence "partially massless" [T]. The point needs a cosmological constant. With H = 0 the edge of the bound is m = 0, the ordinary massless graviton.

## The partially massless point of bimetric gravity

### Proportional de Sitter backgrounds

[Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) has two dynamical metrics, g and f, each with its own Einstein–Hilbert term and Planck mass, M_g and M_f, and a potential whose five coefficients β₀ to β₄ multiply the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) of √(g⁻¹f) [T]. Among its solutions are proportional backgrounds, f = c²g with c a constant, in which each metric solves Einstein's equations with an effective cosmological constant [T]; the case that concerns this page is the one in which both are de Sitter. Around such a background the fluctuations separate into a massless spin-2 mode and a massive one [T].

### The parameter point

The checkpoint states the point from the partially massless bimetric literature [24S]:

```text
β₀ = 3α⁻²β₂,      β₁ = β₃ = 0,      β₄ = 3α²β₂
```

In its words, "the PM point β₀ = 3α⁻²β₂, β₁ = β₃ = 0, β₄ = 3α²β₂ makes the potential g↔f symmetric, with proportional de Sitter solutions of undetermined ratio [24S]" (#11 §7.4). PM stands for partially massless. The undetermined ratio is the constant c: at this point the field equations do not fix it.

The checkpoint does not define α or c. In the bimetric literature's usual notation α is the ratio of the two Planck masses, M_f/M_g, and c is the constant in f = c²g [T]; the wiki reads #11 with that notation. The round-3 audit's quotation from a bimetric paper uses α in a way consistent with this reading: "the alpha->0 limit brings bimetric theory arbitrarily close to GR [general relativity]", and heavy spin-2 fields are "not excluded as long as ... M_f is sufficiently small" (audit notes, Step 1; see [bimetric cosmology](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-heavy-spin-2-regime)). The program's documents do not discuss how far the extra gauge symmetry extends beyond the linear theory, a question studied in the partially massless literature [T].

The reference, as the checkpoint lists it:

- [24][S] Partially massless bimetric gravity and its exchange-symmetric parameter point, arXiv:1609.09515.

The checkpoint gives this descriptive title and no authors (see flag 9 in `review/wiki-build-flags.md`), and the [handoff](/wiki/history/documents/handoff) cites the arXiv number without a mark (HANDOFF §2, §8). The wiki does not supply the authors.

## Inside the palindromic branch

### The branch

The program's [frame-tier](/wiki/gravity/tuning-test/frame-tier) potential is a Hassan–Rosen potential whose coefficients reciprocity restricts to βₙ = β₄₋ₙ: β₀ = β₄ and β₁ = β₃, with β₂ free ([#8](/wiki/history/documents/debt-1-notes) §1; [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome)).

### At α = 1

Setting α = 1 in the three conditions gives β₀ = β₄ = 3β₂ and β₁ = β₃ = 0, which satisfies βₙ = β₄₋ₙ. The checkpoint: "At α = 1 the PM point lies **inside** our palindromic branch", so partially massless gravity "is a special point of the reciprocity-symmetric family, raising the open question of whether reciprocity is the origin of the PM symmetry [O]" (#11 §7.4).

On the literature's reading of α, α = 1 means equal Planck masses. Calc note #8 states that reciprocity forces "equal effective Planck masses" (#8 §3), so on this reading α = 1 is the case that applies to the program; #11 does not draw this link itself. The handoff states the finding without the condition: the partially massless bimetric point "is g↔f symmetric and sits inside the palindromic branch" (HANDOFF §2). The checkpoint, which ranks above the handoff, adds "At α = 1".

### A different point of the same branch

The program's vacuum-energy identity selects its own point of the branch. "Note the PM point sits at Λ ≠ 0 with c undetermined; our flat-aligned-vacuum identity selects a *different* point of the same branch (β₁ ≠ 0 generically, β₀ = −4β₁ − 3β₂)" (#11 §7.4). The identity concerns a flat vacuum at the aligned point, where the two frames coincide; the partially massless point concerns de Sitter backgrounds with c left free. See [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity).

## The comparison still to be made

The literature check that found this point downgraded the identity's novelty. The handoff's one-screen state records that the partially massless bimetric point "(arXiv:1609.09515) is g↔f symmetric and sits inside the palindromic branch; Hossenfelder arXiv:0807.2838 has a different exchange-symmetric cancellation. Detailed comparison still owed." (HANDOFF §2). The checkpoint downgraded the novelty claim "from 'likely standalone result' to 'requires detailed comparison with the PM and exchange-symmetric literature'" (#11 §7.4). Hossenfelder's theory, reference [25S] of the checkpoint, cancels vacuum energy by a different mechanism, "where twin-sector source terms cancel identically"; the program's identity "is sector-internal (no twin matter required) and, to our current knowledge, distinct" (#11 §7.4).

The comparison is open problem 2 of the checkpoint: "**PM-adjacency:** detailed comparison of the palindromic branch with partially-massless bimetric [24S]; is reciprocity the origin of the PM symmetry? Convention-careful check of the vacuum-energy identity against [24S, 25S] — the queued novelty audit [O]" (#11 §14). The handoff's queue named three comparisons: "arXiv:1609.09515 / 0807.2838 / the Schmidt-May–von Strauss review's no-protecting-symmetry statement" (HANDOFF §8 item 5); the third belongs to [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem). Since the handoff the comparison is part of item 1 of the current queue (`CLAUDE.md`, "Since the handoff"). It has its own page, [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison), and is listed with the program's [open problems](/wiki/status/open-problems).

## Standard references

- A. Higuchi, Nucl. Phys. B 282, 397 (1987): the bound m² ≥ 2H². It is #14's reference [6], unmarked there; the round-3 audit found that it supports the statement.
- [24][S] arXiv:1609.09515: the partially massless bimetric parameter point, cited by #11 with a descriptive title.
- [25][S] S. Hossenfelder, "A bi-metric theory with exchange symmetry," Phys. Rev. D 78, 044015 (2008), arXiv:0807.2838: the exchange-symmetric cancellation by a different mechanism, cited by #11.
- Added by the wiki from model memory (†): S. Deser and R. I. Nepomechie (1984)†, on gauge invariance and masslessness of fields on de Sitter space; S. Deser and A. Waldron (2001)†, on partial masslessness of higher-spin fields; S. F. Hassan, A. Schmidt-May and M. von Strauss (2012)†, on partially massless bimetric gravity.

## Used by

- [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison) — the comparison with this point, still to be made.
- [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — the branch that contains this point at α = 1.
- [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) — selects a different point of the same branch.
- [Bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology) — the Higuchi bound, at whose edge this field sits.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.4 — the parameter point, its place in the palindromic branch at α = 1, the open question, the different point the identity selects, and the novelty downgrade.
- `papers/broken-born-checkpoint-v2.md` §14 item 2, refs [24], [25] — the open comparison; the citations, marked [S].
- `HANDOFF.md` §2, §8 — the literature check that downgraded the identity's novelty; the three comparisons in queue item 5.
- `CLAUDE.md` 'Since the handoff' — the comparison in item 1 of the current queue.
- `notes/knot-dark-matter-standalone.md` §1, ref [6] — the Higuchi bound and its citation (manuscript withdrawn for an unrelated error: its Kibble estimate of the relic abundance had been normalized too low).
- `review/round3/referee/audit-notes.md` Step 1 — Higuchi's abstract and the conversion with Λ = 3H².
- `notes/debt1a-ii-X-classification.md` §3 — the five polarizations of a massive spin-2 field.
- `notes/debt1a-iv-beta-coefficients.md` §1, §3 — the palindromic constraint; equal effective Planck masses forced by reciprocity.
- `review/wiki-build-flags.md` item 9 — reference [24][S], with no authors and a title that may be descriptive; awaiting Paul's ruling.
