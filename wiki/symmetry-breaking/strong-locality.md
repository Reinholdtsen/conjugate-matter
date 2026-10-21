---
title: "Open: forced locality and the P4 lock"
weight: 110
status: open
description: "Nothing yet forces matter to couple through K; without the P4 lock, matter's section and K's sign are independent orders, so x-locality comes packaged with a p-local mirror sector rather than derived."
provenance: [O]
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/reciprocity-toy-models.md Abstract"
  - "notes/toy-lagrangian.md 'Success criteria (fixed 2026-10-19, before any construction)'"
  - "notes/toy-lagrangian.md 'Predictions (written before construction)'"
  - "notes/toy-lagrangian.md 'Chunk 1 results (2026-10-19)'"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions (written before construction)'"
  - "review/round4-adjudication.md 'Rulings' F3"
---

*This open problem asks whether anything forces matter to be local in position, rather than leaving that as an input. In the coset toy model the vacuum's order parameter fixes a pair of candidate directions in the position–momentum plane and marks one of them as position, and a suitable coupling makes matter local in whichever direction is marked; but nothing in the model requires matter to use that coupling. Without such a link, the line a matter field lives on and the sign of the order parameter are two independent choices. In the toy the link is supplied by postulate P4, which places ordinary matter in the position-polarized representation and its mirror image in the momentum-polarized one. The toy therefore explains locality in position only as part of a package that includes a momentum-local mirror sector, the program's dark-matter candidate, and does not derive it. The toy-model worklog notes that the question is also open in the literature.*

**Status:** Open — [O] (#11 §14 item 11: "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4") — named among the toy work's open ends in the root `CLAUDE.md` ("the strong form of matter locality"); the worklog adds that it is "also open in the literature". Listed at [Open problems and the queue](/wiki/status/open-problems).

## The question

The toy work's criterion S5 asks that matter coupled to the order parameter acquire "interactions local in the selected Lagrangian (x) and nonlocal in its complement (p)" in the selected vacuum, and the reverse in its ρ-image (worklog, 'Success criteria'; [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)). It is meant to carry "the program's claim that 'forces fade with distance, never with velocity difference' because the vacuum is polarized", part of the program's answer to [Born's question](/wiki/program/borns-question). Here and below, "worklog" is `notes/toy-lagrangian.md` and "toy note" is `papers/reciprocity-toy-models.md`, version 2.

The criterion has two strengths:

- **The weak form** holds [V]: once matter couples through a coupling built from the metric H and the real structure K, its interactions are local in x in one vacuum and in p in the mirror vacuum, "as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given" (toy note §5). See [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).
- **The strong form**, "locality forced, not chosen", is the open problem. The worklog: "Strong form (locality forced, not chosen): not achieved. It is also open in the literature." ('Chunk 4', S5 conclusion).

Three documents list it:

- #11 §14 item 11: "Still open [O]: a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4." ([Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion));
- the toy note's "Not shown" list: "a mechanism forcing the (H, K)-coupling of matter;" and "anything beyond d = 1." (§6);
- the root `CLAUDE.md`, among the open ends of the toy work: "the strong form of matter locality;".

## What the toy shows, and where it stops

The worklog's S5 conclusion takes the toy apart in two steps ('Chunk 4').

### The pair of lines comes from K

> (i) the pair {L+, L−} is the eigenline pair of K. It is spontaneously selected only in the continuous version (3+1, angle φ a Goldstone); with the τ-type potential it is fixed by K_ref.

The real structure K of [model I](/wiki/symmetry-breaking/toy-models/coset-model) has two eigenlines, L+ (eigenvalue +1) and L− (eigenvalue −1). They are the null lines of the neutral metric η = ωK, and a section condition built from η confines each matter field to one of them [V] ([the section condition](/wiki/symmetry-breaking/section-condition)). Where the pair comes from depends on how the polarization is made definite:

- In 1+1 dimensions the toy needs a ρ-preserving potential, and that potential fixes the pair by hand: with it, the pair "is fixed by K_ref", the potential's reference real structure ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).
- A spontaneous selection of the pair would need the continuous version, in which the polarization angle φ is a Goldstone direction ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). The worklog places that in 3+1 dimensions, where, in its words, "Coleman–Mermin–Wagner does not apply" ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). That case is a worklog remark and was not computed; the note covers 1+1 dimensions with d = 1 only (§6).

### Matter is tied to the sign of K only by the coupling

> (ii) Which member is "position" is the spontaneously broken ρ, but matter's section is locked to K's sign only through the K-covariant coupling. Without that lock, matter's choice of section and K's sign are independent orders.

Two things are chosen in the toy, and nothing ties them together:

1. **The sign of K.** In the vacuum +K the line L+ is position, and ρ sends K to −K (toy note §2), which exchanges the roles of the two lines. Which sign the vacuum has is the spontaneously broken ρ.
2. **Each matter field's section**, the line its dependence is confined to. The section condition built from η allows either line, and it is the same condition whether built from η or from −η, so it carries no information about the sign of K: it "selects the unordered pair {L+, L−} and cannot tell position from momentum" (worklog, part B [V]).

The phrase "independent orders" means that each choice can take either value whatever the other one is: in a vacuum with K = +K_ref, a matter field could depend on the coordinate along L+ or on the coordinate along L−, and the section condition allows both. What ties the two choices is a coupling that depends on the sign of K. The toy's coupling I, built from H and K, does this: it is local along whichever line is L+ in the current vacuum ([Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling); the worklog's "K-covariant" was revised to "(H, K)-covariant" in round 4). But "Nothing here forces that coupling" (toy note §5), and nothing in the toy excludes a K-blind coupling such as ∫W², which "shows no asymmetry" between the vacua (§5).

The same coupling does a second job. Without it, the vacuum of model I keeps a twisted element, ρ combined with the flip K → −K, that acts on the metric exactly as ρ does, so the breaking of ρ has no physical content. The round-4 adjudication: "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K. This sharpens the S5 conclusion rather than contradicting it." (`review/round4-adjudication.md`, F3; [the twisted element](/wiki/symmetry-breaking/twisted-element)). The lock between matter and K's sign is therefore what makes the breaking physical and what makes locality follow the vacuum, and the toy's dynamics do not supply it.

## The lock is P4

The worklog names what supplies the lock:

> **The lock is P4** (x-polarized matter, and its ρ-image, p-polarized matter). So in the toy, the program's explanation of "forces fade with distance" amounts to this: our matter is the x-polarized species. The explanatory gain is that x-locality comes packaged with a p-local mirror sector, the program's dark-matter claim. It does not derive x-locality from nothing. (worklog, 'Chunk 4')

[P4](/wiki/program/postulates/p4-polarized-matter) is a postulate [P]: "Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations." (#11 §4). P4 posits both species: ordinary matter, local in x, and its ρ-image χ, local in p. #11 §14 item 11 states the result in one clause: locality beyond the weak form "in the toy reduces to P4".

What the package contains is the subject of [conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter): χ is the program's proposal for dark matter, and [the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) is one of its two remaining dark-sector candidates. In the toy, then, the account of why forces fade with distance and the existence of a momentum-local mirror sector rest on the same postulate.

## Routes tried, and the literature

- **The route expected to do better.** Before construction the worklog wrote: "The candidate route that might do better is a field theory on phase space whose own vacuum breaks x ↔ p, with no separate K field", recalling Langmann–Szabo duality and the Grosse–Wulkenhaar model at its self-dual point as prior art (†, unverified at the time) ('Predictions'). That route became [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar). In its complex form the breaking "does not survive quantization" (toy note, Abstract; [quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)), and the worklog planned and carried out S5 in model I, through "the section-condition logic of double field theory, which ties locality to η" ('Chunk 3 results', plan for S5; 'Chunk 4').
- **Langmann and Szabo on locality.** The prior-art survey found that in the noncommutative field theory in which Langmann and Szabo found their position–momentum duality, locality in x does not come from a vacuum: "Langmann–Szabo (p. 6): at θ = 0 the position vertex is 'fully local' and the momentum vertex non-local; 'for non-singular θ, both vertex functions have the same non-local form'. In that literature, locality in x arises only at the singular θ → 0 limit, not from a vacuum." ('Chunk 1 results', "Bearing on S5"; [noncommutative field theory and the Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)).
- **Double field theory on selecting a section.** The worklog's live-searched survey [S]: consistency confines fields to one section, but that the choice is dynamical is "Claimed only in words" (Freidel–Rudolph–Svoboda: "might be subject to a dynamical selection rule"; Freidel–Leigh–Minic: "a dynamical question"), and "Open: a mechanism that picks L over L̃. Each candidate in the literature either selects the pair only, or uses outside input: which modes are light, distance-dependent interactions, or a curved position space." ('Chunk 4', 'S5 literature'; [double field theory](/wiki/phase-space/born-geometry/double-field-theory)). Here L and L̃ are the two members of the pair, the program's L+ and L−.

Hence the worklog's "also open in the literature".

## Bearing on the main critique

The toy work set two tiers of criteria: the referees' letter (S0–S3) and the spirit (S4–S5), "what would answer round 3", the critique that the framework does no work ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)). Before construction the worklog wrote down what a failure of S5 would mean: "If S1–S4 pass and S5 fails, the honest conclusion is that acceptance criterion 1 as the referees worded it is too weak to answer 'the framework does no work'. That would be reported as such." ('Predictions'). Its assessment scored that forecast a "Hit": "Criterion 1 as worded is now met (coset + τ potential). The round-3 critique is only partly answered" ('Assessment against the predictions'; the potential that meets the criterion is now the bounded one of round 4). The verdict on [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) gives the reason:

> The round-3 critique ("the framework does no work") is only partly answered. The toy makes the program's structures cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling. (worklog, 'Assessment against the predictions')

The forecast for S5 itself also scored a "Hit": "S5 not passed at first attempt; locality defined relative to K by hand" against the outcome "Weak form only; the strong form is open here and in the literature".

## What remains open

- **A mechanism that forces the coupling** of matter to the order parameter [O] (toy note §6; #11 §14 item 11).
- **The continuous case.** Whether the pair is selected spontaneously when the polarization angle is a Goldstone direction, in 3+1 dimensions, is a worklog remark, not computed.
- **Beyond d = 1.** The toy has one position and one momentum coordinate; for d > 1 the section condition already leaves "a continuous family of sections" (toy note §5), and "anything beyond d = 1" is not shown (§6).

The current work queue in the root `CLAUDE.md` (the `HANDOFF.md` §8 items 5–7, then an optional round-5 review of the toy note) does not include this item.

## Sources

- `CLAUDE.md` 'Since the handoff' — "the strong form of matter locality" among the toy work's open ends; the current queue
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — still open [O]: locality beyond the weak form, which in the toy reduces to P4; §4 — P4
- `papers/reciprocity-toy-models.md` §5 — the coupling, "Nothing here forces that coupling", the d > 1 family; §6 — "Not shown": a mechanism forcing the coupling, anything beyond d = 1; §2 — ρ sends K to −K; Abstract — the complex model's restoration
- `notes/toy-lagrangian.md` 'Chunk 4' — parts B and C, the S5 conclusion (i)–(ii), the P4 lock and the section-selection literature [S]; 'Success criteria', 'Predictions', 'Assessment against the predictions' — the wording of S5, the forecasts and their scores, the round-3 critique "only partly answered"; 'Chunk 1 results' — Langmann–Szabo on locality; 'Chunk 3 results' — the plan for S5
- `review/round4-adjudication.md` 'Rulings' F3 — the K-odd coupling that makes the breaking physical, "for example P4-type matter through I_K"
