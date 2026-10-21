---
title: "Obituary: Planck-suppressed adjoint mixing"
weight: 130
status: dead
description: "The operator Φ^a F^a B/M_* exists in the literature (Baumgart's footnote, ruling 8), but its O(1)-at-Planck coefficient is unsupported and its sources need bi-charged states that P4 excludes."
sources:
  - "review/round3-adjudication.md 'Rulings' 7–8"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §5"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(b)"
  - "review/v3-worklog.md 'Round-2 pending list'"
---

*Planck-suppressed adjoint mixing was #14 v3's estimate of how strongly its hidden photon would mix with ours. The hidden Higgs field Φ permits a gauge-invariant interaction Φ^a F^a_μν B^μν / M_\*, which links the hidden field strength to the field strength of our hypercharge; once Φ takes its vacuum value v, it produces a kinetic mixing ε ~ v/M_\*. v3 assumed the operator appears with a coefficient of order one at the Planck scale, which gives ε ~ 10⁻⁷–10⁻⁶. The round-3 review found no source for that assumption: every paper that derives the operator obtains it at one loop from particles charged under both forces, which the program's own sector separation excludes, and the estimate those papers give is three orders of magnitude smaller. The estimate is dead, and the program then took sector separation strictly.*

**Status:** Dead — round-3 ruling 7, upheld: the "O(1) coefficient at the Planck scale" is unsupported, and "the literature generates it at one loop from bi-charged states, which sector separation forbids" ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)). The operator itself exists: ruling 8 overturned the referee's claim that a cited paper lacked it. Decision 1 replaced the estimate with strict sector separation ([P4](/wiki/program/postulates/p4-polarized-matter); [round-3 decisions](/wiki/method/review/round-3/decisions)). Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **What v3 claimed** (#14 §2(b)): "Phi^a F^a_mu-nu B^mu-nu / M_* is gauge invariant and gives epsilon ~ v/M_* once Phi condenses [10]. For an O(1) coefficient at the Planck or reduced Planck scale, epsilon ~ 1e-7 to 1e-6. The operator is odd under Phi -> -Phi, so a discrete symmetry acting as hidden charge conjugation forbids it - but only if that symmetry is gauged". #14's exclusion condition 3 was built on the resulting window: "m_psi from the MeV scale to ~0.1 TeV at visible charge ~ (1e-7 to 1e-6) e" (#14 §5).
- **The arithmetic** (audit notes, Step 2): ε ~ v/M_* comes out at "6.6e-8 - 5.9e-7", "CONFIRMED as arithmetic (order of magnitude)". With the one-loop factor "g_d g' y/16pi^2" that the sources use, it becomes "9e-11 - 8e-10": "the cited sources' own estimate is 3 orders smaller".
- **Ruling 7** (upheld): "Consistent with the round-2 literature report: Chen–Cline–Frey "induced at one loop by a heavy particle X which carries both…". Sec. 2(a) and 2(b) of v3 are in tension." The referee found that all the sources that derive the operator get it at one loop from fields charged under both groups (Chen–Cline–Frey, Brümmer–Jaeckel, Gherghetta et al.), fields "exactly what the sector-separation postulate excludes": "The eps ~ 1e-7-1e-6 window therefore contradicts the manuscript's own postulate" (Step 4(a) item 6).
- **Ruling 8** (overturned). The referee reported that Baumgart et al. contains no adjoint dimension-5 operator (Step 4(b)). The adjudicator found it in "arXiv:0901.0283v2, p. 5, footnote 5, verbatim: "It is actually possible to achieve mixing without an abelian factor through an S parameter type operator Tr[Φw_μν]B^μν, where Φ is some operator that transforms as an adjoint of the non-abelian group." The referee missed the footnote." The operator exists; what died is the size v3 gave it.
- **The worklog's estimate** (R4): "The dimension-5 adjoint operator is in the literature [Baumgart et al. 2009 fn.; Chen–Cline–Frey 2009; Brümmer–Jaeckel 2009, χ = v/M]. Our estimate: ε ≈ 2.4×10⁻⁸ at M = M_Pl [V]." Its range "≈ 10⁻⁸–10⁻⁷" and #14's "1e-7 to 1e-6" come from different stages of the benchmark and were never reconciled; both are moot.
- **Decision 1**: "The alternative rested on an unsupported coefficient. The dimension-5 "O(1) at the Planck scale" estimate (ruling 7) has no source. The sources generate that operator only from bi-charged states, which P4 forbids." The mixing that remains is gravity's ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).
- **The pre-registration** had predicted "Zero surviving numerical indictments"; the outcome was "Three survive (p; the ψ window; ξ), plus the ε coefficient" ([round-3 pre-registration](/wiki/method/review/round-3/preregistration)).

## Sources

- `review/round3-adjudication.md` 'Rulings' 7–8 — the unsupported coefficient and the Baumgart footnote; 'Decisions' 1 — strict sector separation; 'Pre-registration scored' — the ε coefficient among the indictments
- `review/round3/referee/audit-notes.md` Step 2 — the arithmetic and the one-loop estimate; Step 4(a) — the contradiction with sector separation; Step 4(b) — the literature check
- `review/v3-worklog.md` 'Round-2 pending list' — R4's estimate
- `notes/knot-dark-matter-standalone.md` §2(b) — the claim; §5 — exclusion condition 3
