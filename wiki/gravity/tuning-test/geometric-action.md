---
title: "The geometric action S_H and the v0.1 action (superseded)"
weight: 60
status: superseded
description: "The lab notebook's action S = S_H + S_τ + S_x + S_p + S_mix, its Einstein-like S_H with ω and η frozen, and its argument against a ghost — superseded by P2′, and the starting point of open problem 1."
provenance: [D]
sources:
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/debt3b-wave-island.md 'Next'"
  - "notes/debt3c-ufd-endpoint.md 'Next: Debt 1, Chunk 1a'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
---

*The v0.1 action is the complete action written in the program's [lab notebook](/wiki/history/documents/lab-notebook) (#1 §3): a sum of five terms, one each for the phase-space geometry, the dark-energy angle τ, the Standard Model, conjugate matter and an unspecified mixing term. Its geometric term S_H is an Einstein-like action for the phase-space metric H, written with both the symplectic form ω and the neutral metric η frozen, as the [original postulate P2](/wiki/program/postulates/original-p2) required. [Postulate P2′](/wiki/program/postulates/p2-prime) later made η emergent, and the Debt-1 calc notes replaced the notebook's argument against a ghost with the frame-tier argument, so this form of the action is superseded; [checkpoint #11](/wiki/history/documents/checkpoint) writes no full action. S_H survives as the action from which open problem 1 asks for the ghost-free frame-tier potential to be derived.*

**Status:** Superseded — S_H is [D, schematic], the argument against a ghost [D] with an [O] remainder, in `notes/broken-born-theory.md` §3–§4 — superseded by P2′ (the notebook's v0.3 addendum; #11 §4–§5) and by calc notes #5–#8. Listed in [Superseded statements](/wiki/status/superseded).

## Key facts

- The action, #1 §3:

  ```text
  S = S_H + S_τ + S_x[SM; g] + S_p[χ; g, g̃] + S_mix
  ```

  Here S_x is the Standard Model sector: "S_x is the Standard Model minimally coupled to g. Nothing is modified. [P4]"
- The geometric sector, #1 §3 [D, schematic]: "S_H = ½M_B² ∫_Σ √|H| R_B[H] over the section Σ, with ω, η frozen (P2). On the x-tilted vacuum, H decomposes into a spacetime metric g_μν(x) and a momentum-space metric g̃^μν; the g-block reproduces the Einstein–Hilbert action with M_P fixed by M_B and the section volume." R_B is the curvature of [the Born connection](/wiki/phase-space/born-geometry/born-connection); the Einstein–Hilbert action is described on [General relativity and the graviton](/wiki/gravity/spin-2-fields/general-relativity).
- The other terms, #1 §3: S_τ = ∫ √(−g) [½(∂τ)² − V(τ)] with V(τ) = V₀[1 + cos(τ/f)], where the sign this potential must take is an unresolved conflict between the documents ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)); and a conjugate sector carrying the postulated gate, where "Deriving the precise gate shape from S_H + S_mix is open [O]" ([The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)).
- The notebook's "Ghost accounting" paragraph, #1 §4: "There is no second independent metric: g̃'s cosmological mode is eliminated by the P2 constraint …, so no Boulware–Deser sector arises in minisuperspace. [D] The statement for full inhomogeneous H is open. [O]" The v0.4 addendum reversed this: X is "a second graviton", and ghost-freedom now comes from [the frame tier](/wiki/gravity/tuning-test/frame-tier).
- Why the form is superseded: under strict P2, "S_H is a functional of g alone" (#11 §5), which is the content of [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem); P2′ freezes only ω, so S_H's frozen η contradicts it.
- The plan before the Debt-1 notes, from the "Next" sections of calc notes #3 and #4: "linearize S_H on the broken vacuum; leaning on the known linearized-DFT spectrum, identify propagating modes and check quadratic-order ghost freedom" (DFT is double field theory), sub-planned as "(1a-i) mode content at quadratic order on flat background, importing the known linearized-DFT spectrum [T: graviton + two-form + dilaton]; (1a-ii) ghost check of the quadratic action with ω, η frozen; (1a-iii) extract the dynamical equation for the g̃-block". Calc notes #5–#8 made η emergent instead of frozen ([The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)).
- What survives: #11 §14 item 1, "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction)).

## Sources

- `notes/broken-born-theory.md` §3 — the v0.1 action and S_H; §4 for the "Ghost accounting" paragraph; 'Addendum (v0.3, overnight)' and 'Addendum (v0.4)' for the supersession
- `papers/broken-born-checkpoint-v2.md` §4 — postulate P2′; §5 for S_H under strict P2 and the nontriviality theorem; §14 item 1 for the open derivation
- `notes/debt3b-wave-island.md` 'Next' — the planned Chunk 1a
- `notes/debt3c-ufd-endpoint.md` 'Next: Debt 1, Chunk 1a' — its sub-plan with ω and η frozen
