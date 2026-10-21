---
title: "Open: the origin of the ρ-preserving potential"
weight: 70
status: open
description: "A definite polarization needs a potential on the Goldstone angle — a rigid, unordered pair of axes, more structure than ω alone — and no derivation of it exists."
provenance: [O]
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "review/round4-adjudication.md 'Rulings' F1–F2"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Chunk 1 results (2026-10-19)'"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions (written before construction)'"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §12"
  - "verify/toy_coset.py"
---

*This open problem asks where the potential that fixes the polarization angle comes from. In the program's toy models the vacuum's polarization, the choice of which direction in the position–momentum plane counts as position, is an angle that can take any value at no cost in energy. In wave terms the angle runs continuously from describing a state by its waveform to describing it by its spectrum, through the intermediate descriptions that fractional Fourier transforms give. A definite polarization appears only after a potential is added that keeps Born reciprocity as a symmetry but pins the angle to one of two opposite settings. The program gives its dark-energy field τ a potential of the same kind. Such a potential brings in a fixed, unordered pair of axes, which is more fixed structure than the program's postulate P2′ ("only ω is rigid") provides, and nothing in the program derives it. Its first proposed origin, the rigid background of the original postulate P2, disappeared when P2 was replaced.*

**Status:** Open — [O] (#11 §14 item 11, "a derivation of the potential") — the bounded form the toy uses is checked in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)), but where any such potential comes from is not derived. Listed at [Open problems and the queue](/wiki/status/open-problems).

## The question

Checkpoint #11 states the requirement in the v2.2 refinement of its postulate [P2′](/wiki/program/postulates/p2-prime), drawn from the toy models:

> with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]. Two things follow. A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η. (#11 §4)

The open problem is where that potential comes from. Three documents list it:

- #11 §14 item 11 keeps "a derivation of the potential" open [O], next to "a Monte Carlo with H dynamical" and the strong form of matter locality ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion));
- the toy-model note (`papers/reciprocity-toy-models.md`, version 2; "toy note" below) lists under "Not shown" "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes" (§6);
- the root `CLAUDE.md` names "a derivation of the ρ-preserving potential" among the open ends of the toy work.

In the toy models the potential is put in by hand. The problem qualifies [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and the postulate P2′.

## Why a potential is needed

### The polarization is an angle

[Model I](/wiki/symmetry-breaking/toy-models/coset-model), the coset toy model, has two fields: a phase-space metric H and a real structure K, whose two eigenlines are the candidate position and momentum directions ([the order parameter](/wiki/symmetry-breaking/order-parameter)). At H = 1 its vacua form a circle,

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]                        (toy note §2)
```

and [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ acts on it as "K(φ) → K(φ + π) = −K(φ)" (toy note §2). So ρ is one element of a continuous group of rotations of the angle φ, "the U(1) stabilizer of H that rotates K" (worklog, 'Chunk 2 results'; the worklog is `notes/toy-lagrangian.md`). Moving along the circle costs no energy: the compact angle φ is one of model I's three Goldstone directions, and it "parametrizes the Lagrangian Grassmannian Λ(1)" (toy note §2; [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua); [Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)). The worklog's reading: "'which polarization' is an angle on a Goldstone circle, not a discrete choice. The x-sharp and p-sharp vacua are joined by a flat direction." ('Chunk 2 results').

In wave terms the circle is literal [T]. Each point of it takes a different line through the origin of the (x, p) plane as "position" ([Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)). Describing a quantum state along a rotated line amounts to applying a fractional Fourier transform to its wavefunction, and the two familiar descriptions, the waveform ψ(x) and its spectrum ψ̃(p), sit a quarter turn of phase space apart on this circle ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)). A Goldstone angle leaves the choice among all of these descriptions open.

### In 1+1 dimensions the angle cannot order by itself

Model I lives on a 1+1-dimensional base, and there a compact continuous symmetry cannot break spontaneously: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." (toy note §4; [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). The lattice simulation of the angle without a potential finds "No true order" (toy note §4; [the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)). Whether the full model, with its metric sector free, breaks ρ's SO(2) without a potential is a separate open question ([Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).

The worklog's summary of the 1+1 result: "In 1+1, Born reciprocity is spontaneously broken only after the continuous polarization rotation is explicitly broken down to a discrete group containing ρ." ('Chunk 3 results'). Its third unpredicted finding: "In 1+1, 'only ω rigid' is not enough for a definite polarization. A ρ-preserving potential on the polarization circle is required." ('Assessment against the predictions').

### What the potential has to do

The note's requirement: "To get a definite polarization we add a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group." (toy note §4). Its three clauses:

- **Invariant under ρ.** The laws stay reciprocity-symmetric, so that whatever distinguishes position from momentum is the vacuum, not the potential: the breaking of ρ stays spontaneous ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)).
- **Invariant under K → −K.** Model I has this flip as a second, separate symmetry (toy note §2), and the potential keeps it ([the twisted element](/wiki/symmetry-breaking/twisted-element)).
- **Reduces the U(1) to a discrete group.** The potential breaks the continuous rotation of φ explicitly. A potential that repeats when φ advances by π is unchanged by ρ, which acts as φ → φ + π, and leaves isolated minima instead of a flat circle.

An explicit term that breaks a continuous symmetry gives the would-be Goldstone direction a potential, and the mode is then called a pseudo-Goldstone mode [T]. The worklog's revised conclusion uses that language: the toy supports "broken reciprocity" in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential", not "only ω rigid, nothing else" ('Chunk 3 results'). The lab notebook had already called τ "a (pseudo-)Goldstone: derivatively coupled" (#1 §4; [fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force)).

## The potential the toy uses

The toy has used two forms; their full records are on their own pages. Both are built from a fixed reference real structure K_ref, diag(1, −1) in the scripts (`verify/toy_coset.py`).

### The naive form, dead

```text
V = −μ [Tr(K K_ref)]²,        at H = 1:  −2μ(1 + cos 2φ)        (worklog, 'Chunk 3 results')
```

It keeps ρ and the flip, and at H = 1 its minima are the two vacua ±K_ref, which ρ exchanges. But "The naive choice −μ[Tr(K K_ref)]² is unbounded below once H is dynamical": along a family of boosts "the potential reaches −8.9 × 10⁶ μ at boost parameter 4", and "The point (1, K_ref) is a saddle (Hessian eigenvalue −6.47 at λ = μ = 1)" (toy note §4). Round 4 upheld both points as findings F1 and F2 (`review/round4-adjudication.md`). See [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential).

### The bounded form V_b

```text
V_b = −μ [Tr(K K_ref)]² / (2 Tr KᵀK),      −μ ≤ V_b ≤ 0         (toy note §4)
at H = 1:  V_b = −(μ/2)(1 + cos 2φ)
```

The note records that it is "bounded, −μ ≤ V_b ≤ 0 by Cauchy–Schwarz, since Tr K_refᵀK_ref = 2", that "It is ρ- and flip-invariant", and that "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236", with "Vacuum manifold: {diag(y, 1/y)} × {±K_ref}" (toy note §4). The round-4 referee proposed it, and the gate checks each property, from "V_b is rho-invariant" to "with V_b, (1, K_ref) is stable: Hessian eigenvalues >= 0 with exactly one zero" (`verify/toy_coset.py`). The frozen-H lattice simulation uses it, "with V_b up to a constant and normalization", and finds an ordered ℤ₂ phase in 1+1 (toy note §4; [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)). See [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).

Since round 4, #11 sets boundedness as a condition on any such potential: "That potential must be bounded with all fields dynamical — the round-4 review found the naive form unbounded once H moves" (#11 §10). V_b meets the condition in the toy. It does not answer the open problem: it is chosen to be bounded, not derived.

## What the potential costs: a rigid, unordered pair of axes

K_ref enters V_b only inside the square [Tr(K K_ref)]², so K_ref and −K_ref define the same potential. The potential therefore fixes the pair of eigenlines of K_ref, a pair of axes, but not which of the two is position. Which of the two minima ±K_ref the vacuum takes is the spontaneous part of the breaking, and ρ exchanges them. #11 calls this "a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" (#11 §4); the worklog, "a rigid, unordered pair of axes (K_ref up to sign)" ('Chunk 3 results').

The three levels of fixed structure that the sources compare:

| Fixed in advance | What it fixes | The polarization | Source |
|---|---|---|---|
| ω alone (P2′) | no axes | a Goldstone angle, any value | #11 §4 |
| ω and a ρ-preserving potential | an unordered pair of axes | one of two settings, exchanged by ρ | #11 §4; worklog 'Chunk 3 results' |
| ω and η (the original P2) | the pair of axes, ordered | discrete: "no Grassmannian, no Maslov circle, no dark-energy field" | #11 §5; #5 §B |

The sources read this cost the same way:

- the worklog, when it first proposed the potential: "The cost: a rigid, unordered pair of axes. That is weaker than a rigid η, but it is still background structure." ('Chunk 1 results');
- the worklog, after the simulation: "That is more rigid structure than P2′'s 'only ω is rigid', though less than a rigid η." ('Chunk 3 results');
- the round-4 pre-registration, predicting the review's weakest link: "in 1+1, the 'spontaneous' breaking of ρ rests on an explicit, rigid background. The ρ-preserving potential needs a fixed unordered pair of axes K_ref. A referee can reasonably call model I's 1+1 result an ordinary Z₂ breaking of an explicitly chosen axis pair." (`review/round4-preregistration.md`). The adjudication scored it "Partial: right location, missed severity", since the defect found at that spot was the unbounded potential;
- the round-4 referee: "But the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is 'position'." (`review/round4/referee/audit-notes.md`, Step 3);
- the worklog, on matter locality: the pair of lines that matter can live on "is spontaneously selected only in the continuous version (3+1, angle φ a Goldstone); with the τ-type potential it is fixed by K_ref" ('Chunk 4'; [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality)).

## The same potential in the cosmology: τ

The program's dark-energy field τ lives on the same circle. In the lab notebook the space of polarizations is the Lagrangian Grassmannian Λ(d), whose fundamental group ℤ is generated by the Maslov circle, and τ is the angle on that circle (#1 §2; [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian); [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)). #11 §10 gives it a potential: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology" [D + T] ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)).

#11 §10's toy-model paragraph [D][V] ties the two: "In the coset model that angle parametrizes Λ(1): it is τ's circle. A definite polarization requires the ρ-preserving potential this section posits. That potential must be bounded with all fields dynamical", and it ends: "None of this tests the cosmology; it only shows the structure is consistent." The potential on the polarization angle and the potential §10 posits for τ are therefore one object in the program, and the open problem is the same for both. The worklog's first consequence of the Goldstone angle says the same for postulate [P5](/wiki/program/postulates/p5-spontaneous-selection): "(i) P5's 'the vacuum selects a polarization; ours is x-tilted' needs explicit breaking of that U(1) — a potential on the circle — to make the selection definite." ('Chunk 2 results').

What topology fixes and what it leaves open are separate. The periodicity of τ's potential "is forced by the Maslov topology **[D]**"; its existence and its magnitude are not: "Its *magnitude* V₀ is a free parameter here. **[P/O]**" (#1 §3). Whether V(τ) can become negative, as the program's predicted turnaround of the expansion requires, is a further unresolved question ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)).

### The 3+1 remark (worklog only, not computed)

The worklog adds a remark about the program's actual dimension:

> In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply. There the self-dual coset model can break the continuous U(1) itself, with τ an exactly massless Goldstone. §10's τ has a potential, so the explicit breaking is in the program anyway. (worklog, 'Chunk 3 results')

The toy-model note works in 1+1 with d = 1 and lists "anything beyond d = 1" as not shown (§6); the remark was not computed. It does not remove the question: on its own reading, the potential is present in 3+1 because §10 gives τ one, and that potential is no better derived there.

## History of the origin question

1. **v0.1 (September 2026).** The lab notebook gave the potential's existence to the rigid ω of its original postulate P2, [P/O] (#1 §3). That attribution is superseded; see the section below.
2. **The postulate repair (Debt 1).** With η emergent the polarizations again form Λ(d), "π₁ = ℤ, Maslov circle intact, τ restored" (#5 §B), and the source of τ's potential became an open item: "(3) the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" (#5 §F; [the Debt-1 notes](/wiki/history/documents/debt-1-notes)). No later document derives the potential from either candidate. The toy work's section condition does select an unordered pair of lines, "the same information as K_ref", but cannot tell which is position (worklog, 'Chunk 3 results', plan for S5; [the section condition](/wiki/symmetry-breaking/section-condition)).
3. **The toy models (2026-10-19).** The polarization is a Goldstone angle, and in 1+1 a definite polarization needs a potential, first the naive form, with its cost stated from the start (worklog, chunks 1–3).
4. **Round 4 and #11 v2.2 (2026-10-19/20).** The naive form fails with H dynamical and V_b replaces it ([review round 4](/wiki/method/review/round-4)); #11 adds the refinement of P2′, the boundedness condition of §10 and the open item in §14 item 11.

The current work queue in the root `CLAUDE.md` (the `HANDOFF.md` §8 items 5–7, then an optional round-5 review of the toy note) does not schedule the derivation.

## What remains open

- **The derivation** of a ρ-preserving potential, or of τ's potential, from something deeper than a choice of K_ref [O] (#11 §14 item 11; toy note §6; root `CLAUDE.md`).
- **Stability beyond the reduction.** V_b's stability with H dynamical is established from the Hessian; the lattice result is for the frozen-H reduction, and "a Monte Carlo with H dynamical" is open (#11 §14 item 11; [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)).
- **Without a potential.** "whether ρ's SO(2) breaks in the coupled model without a potential" (toy note §6; [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).
- **Beyond the toy.** "anything beyond d = 1" (toy note §6).

## Superseded: the rigid symplectic form as the source of the tilt

The lab notebook (#1, v0.1) wrote τ's potential as V(τ) = V₀[1 + cos(τ/f)] and accounted for it in three parts:

> The potential's *periodicity* is forced by the Maslov topology **[D]**; its *existence* comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the "instanton" that tilts the circle. Its *magnitude* V₀ is a free parameter here. **[P/O]** (#1 §3)

Its one-paragraph summary describes the program as built on "a single spontaneously broken symmetry ... with a rigid symplectic form as its explicit tilt" (#1 §12). The picture is that of explicit breaking by a fixed background: a non-dynamical structure that is not invariant under the rotations of the circle tilts it, as a background field does in the standard treatment [T] ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)).

The attribution did not survive the repair of the postulates. Under the original P2 both ω and η were rigid, and with both rigid the compatible polarizations are discrete: "No Lagrangian Grassmannian, no Maslov circle, **no τ field**" (#5 §B), so there was no circle to tilt ([Original P2](/wiki/program/postulates/original-p2); [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)). Under P2′ only ω is rigid, and the toy models find that ω alone leaves the polarization a Goldstone angle, so that a definite polarization needs "more structure than ω alone" (#11 §4). The register of [superseded statements](/wiki/status/superseded) lists the attribution with P2's "triple duty".

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the P2′ refinement: a Goldstone angle [D][V], and the potential as "a rigid, unordered pair of axes"; §5 — discrete polarizations under strict P2; §10 — τ's potential [D + T], the toy-model paragraph [D][V] and the boundedness condition; §14 item 11 — "a derivation of the potential" still open [O]
- `CLAUDE.md` 'Since the handoff' — "a derivation of the ρ-preserving potential" as an open end of the toy work; the current queue
- `papers/reciprocity-toy-models.md` §2 — the circle of vacua and how ρ acts on it; §4 — Mermin–Wagner for the compact SO(2), the requirement on the potential, the naive and bounded forms, the frozen-H simulation; §6 — "Not shown"
- `verify/toy_coset.py` — the gated checks of V_b and of the naive form's saddle
- `review/round4-adjudication.md` 'Rulings' F1–F2, 'Pre-registration scored' — the naive form's failure; the weakest-link forecast scored
- `review/round4-preregistration.md` 'Predictions' — the weakest link forecast at the rigid axis pair
- `review/round4/referee/audit-notes.md` Step 3 — the axis pair fixed by hand
- `notes/toy-lagrangian.md` 'Chunk 1 results' — the fallback potential and its cost; 'Chunk 2 results' — the Goldstone circle and consequence (i) for P5; 'Chunk 3 results' — the 1+1 result, the price, the pseudo-Goldstone reading, the 3+1 remark and the plan for S5; 'Chunk 4' — the pair fixed by K_ref; 'Assessment against the predictions' — finding 3
- `notes/debt1a-geometric-core.md` §B — discrete polarizations under strict P2, Λ(d) restored under P2′; §F — the origin of τ's potential under P2′ as open item 3, with its two candidates
- `notes/broken-born-theory.md` §2 — Λ(d) and the Maslov circle; §3 — the v0.1 attribution to the rigid ω (superseded); §4 — τ as a pseudo-Goldstone; §12 — "a rigid symplectic form as its explicit tilt"
