---
title: "Born's question"
weight: 10
status: established
description: "Why does physics use only half of quantum kinematics' position–momentum symmetry? Born's 1938 question, the dynamical sources of the asymmetry, and general relativity's flat momentum fibers."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md refs [1]–[6], [26]"
  - "notes/broken-born-program-v1.md §1"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md Abstract, §3"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 4'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "verify/toy_s5.py"
  - "popsci/universes-other-half.md 'Two descriptions of one thing'"
  - "popsci/angle-of-the-mirror.md opening paragraphs"
---

*Born's question asks why physics singles out position when quantum kinematics treats position and momentum as equals. A quantum particle can be described by a wavefunction of its position or by a wavefunction of its momentum. The Fourier transform, the operation that turns a sound's waveform into its spectrum, converts either description into the other exactly, and exchanging the two variables, with one change of sign, leaves the rules of quantum kinematics unchanged. The laws of motion do not share this evenness: atoms are small in space rather than in speed, forces fall off with distance rather than with difference in velocity, and general relativity curves space-time while leaving the space of momenta flat. Max Born raised the question in 1938. The Comatter program is one proposed answer: the symmetry is exact in the laws and broken by the vacuum.*

**Status:** Established — [T]. [#11](/wiki/history/documents/checkpoint) cites Born [1†, 2†], the 2+1-dimensional result [5†] and the curved-momentum-space lineage [4†, 6†] from model memory (†). The [round-3](/wiki/method/review/round-3) audit, checking #14's citations of the same two Born papers, confirmed their metadata but did not read their text; the rest await [the † literature battery](/wiki/method/literature-battery). Casting these facts as the program's starting question is #11 §3's framing.

## The question

The kinematics of quantum mechanics treats position x and momentum p alike. Checkpoint #11 states it in one line: "Quantum kinematics is exactly invariant under ρ: (x,p) → (p,−x); the Fourier transform implements it unitarily [1†, 2†]" (#11 §3). The map ρ is [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity).

The dynamics does not share the symmetry. #11 §3 names the places where the asymmetry enters: "x-local interactions, the momentum-space mass shell, and general relativity's flat momentum fibers". The v1 paper gives the fuller list and its conclusion: "All asymmetry lives in dynamics: Hamiltonians are p²/2m + V(x), interactions are local in x, the mass shell is a momentum-space structure with no positional twin, and general relativity curves x-space while leaving momentum fibers flat" (#9 §1). The [popular article](/wiki/history/documents/popular-articles) #12 adds that the asymmetries all point one way: "Every known law that treats the two variables differently treats them differently in the same direction."

Born's question follows. If the kinematics is symmetric, why does every asymmetric law favour position? Max Born, who also gave the wave function its probability interpretation [T], raised it in 1938 [1†] and returned to reciprocity in 1949 [2†].

## The symmetry of the kinematics

For one degree of freedom, phase space is the plane of pairs (x, p), and ρ turns that plane by a quarter turn:

```text
ρ: (x, p) → (p, −x)          ρ = [[0, 1], [−1, 0]]          ρ²: (x, p) → (−x, −p)

[x, p] = iℏ   becomes   [p, −x] = −[p, x] = [x, p] = iℏ
```

The matrix "is symplectic and squares to −1" (toy-model note §1): it preserves the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form), and applying it twice gives the parity (x, p) → (−x, −p). The second line is the reason ρ is a symmetry of the kinematics [T]. The [canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator) [x, p] = iℏ, which contains the uncertainty principle and sets its scale ℏ, takes the same form in the new variables; in the v1 paper's words, "the canonical commutator is blind to it" (#9 §1).

On wavefunctions, ρ is carried out by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) [T]:

```text
ψ̃(p) = (2πℏ)^(−1/2) ∫ e^(−ipx/ℏ) ψ(x) dx
```

The transform is unitary, so it preserves probabilities, and it loses nothing: ψ(x) can be recovered from ψ̃(p) exactly. Applying it twice gives ψ(−x), the parity ρ². #12 builds its account on the comparison with sound: a chord "can be recorded as pressure varying in time — the waveform — or as a list of frequencies and their strengths — the spectrum. Neither description is an approximation of the other", and "A particle's description in terms of position and its description in terms of momentum are two complete readings of one underlying state, related by the same Fourier transform that relates a waveform to its spectrum."

In ordinary quantum mechanics ρ relates two equivalent descriptions of the same physics rather than constraining the dynamics, a distinction set out in [unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence). The program's claim that ρ is a symmetry of the laws themselves is its own postulate, [P3](/wiki/program/postulates/p3-reciprocity).

## Where the asymmetry lives

### The form of the Hamiltonian

A non-relativistic Hamiltonian H = p²/2m + V(x) puts the two variables in different roles [T]. Momentum enters only through the kinetic energy, quadratically and the same way for every system; position enters through the potential V, which carries all the interactions. Applying ρ gives x²/2m + V(p), a law in which the interaction depends on momentum, and no observed system follows such a law. The harmonic oscillator, whose Hamiltonian is quadratic in both variables, is the standard exception: with its mass and frequency scaled out, its Hamiltonian is unchanged by ρ, and its energy eigenfunctions are also eigenfunctions of the Fourier transform [T].

### Locality in position

Interactions act between particles that are close together in space, and their strength falls off with the distance between them [T]. No known interaction falls off with the difference between two particles' velocities. #11's plain-language passage puts it as "forces fade with distance, never with velocity difference". The program's [toy models](/wiki/symmetry-breaking/toy-models) turned this sentence into a test: their criterion S5 asks that matter coupled to the vacuum acquire "interactions local in the selected Lagrangian (x) and nonlocal in its complement (p)", which is "the content of the program's claim that 'forces fade with distance, never with velocity difference' because the vacuum is polarized" (toy worklog, 'Success criteria'; [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)).

### The mass shell

The energy and momentum of a free relativistic particle satisfy p_μp^μ = m²c² ([#13](/wiki/conjugate-relativity) §4; [special relativity](/wiki/conjugate-relativity/special-relativity)), which confines them to a hyperboloid in momentum space, the mass shell [T]. Nothing constrains a particle's position in the same way, so the mass shell is, in #9's words, "a momentum-space structure with no positional twin". The program's conjugate special relativity proposes such a twin for the opposite polarization, an [invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell) x_μx^μ = λ_χ² [D — structural] (#13 §4).

### Flat momentum fibers

The momenta available to a particle at one point of space-time form a fiber, and in [general relativity](/wiki/gravity/spin-2-fields/general-relativity) every fiber is flat, however strongly space-time is curved there [T]: general relativity curves the space of positions and leaves the space of momenta at each point flat. #11 §3 calls this "an architectural assumption, not a measurement". The fibers, their geometry in general relativity and in the program, and the dark-matter gate that acts along them are on [momentum fibers and the cotangent bundle](/wiki/phase-space/reciprocity/momentum-fibers).

## Flat momentum space is an assumption

#11 §3 gives the evidence that the flat fibers are a choice of formalism: the assumption is "false in the one exactly solved quantum gravity (2+1d, where momenta live on a curved group manifold [5†]; curved momentum space has an independent lineage from Snyder [4†] through relative locality [6†])". The three works, as #11 lists them (all †), and what each did [T]:

- **Snyder** (1947), "Quantized space-time" [4†]: took momentum space to be curved, which made the position coordinates operators that do not commute with one another.
- **Matschull and Welling** (1998), "Quantum mechanics of a point particle in 2+1 dimensional gravity" [5†]: in gravity with two space dimensions, which has no gravitational waves and can be solved exactly, a point particle's momentum takes values in a curved group manifold rather than a flat vector space.
- **Amelino-Camelia, Freidel, Kowalski-Glikman and Smolin** (2011), "The principle of relative locality" [6†]: made the curvature of momentum space a principle, with the consequence that whether two events coincide can depend on the observer.

The lineage, and the soccer-ball problem it raises, are on [curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space).

## Earlier work on the question

- **Born's own program.** #11's two Born references (both †) are [1] "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938), and [2] "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949). #13 §4 describes Born's aim as "a physics with a fundamental mass and a fundamental length on equal footing" ([Born's fundamental length](/wiki/phase-space/reciprocity/born-length#borns-fundamental-length)). The round-3 audit, which checked the same two papers in #14's reference list, found their metadata correct, but "1938 abstract does not state the rule; primary text paywalled", and graded the citation "partially verified (primary text not read)" (audit notes, Step 1; the first two words are in capitals in the original). Checking it against the source is part of [the † literature battery](/wiki/method/literature-battery).
- **Freidel, Leigh and Minic.** In metastring theory they wrote: "if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization, the space-time one" [26S, p. 3]. They "treat the breaking as kinematical and call the choice 'a dynamical question'" (#11 §3). Their work is the program's direct precedent, credited in #11 since v2.2: see [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality).
- **An exactly symmetric field theory.** Langmann and Szabo found a duality of noncommutative scalar field theory "that exchanges positions and momenta", "formulated for complex fields", and the [Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) is invariant under it at its self-dual point Ω = 1 (toy-model note §1, refs [5], [6]). For a real field the toy-model note finds the duality "only a covariance" (Abstract; §3). The program uses this model as its second toy model ([noncommutative field theory and the Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)).

#11's plain-language passage says "The question sat for 88 years", and #10 says it spent "eighty-eight years in a drawer". Both should be read with the credit that #11's technical text gives Freidel, Leigh and Minic since v2.2.

## The program's answer

The program's answer is its [hard core](/wiki/program/hard-core): "The program: ρ is exact and spontaneously broken" (#11 §3). The asymmetry would then belong to the vacuum, not to the laws, as a magnet's direction belongs to its state and not to the laws governing its atoms ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)). Some breaking is claimed to be unavoidable, because "[x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization" (#11 §3; [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking)), and postulate [P5](/wiki/program/postulates/p5-spontaneous-selection) says our vacuum is the position-tilted one. On the flat fibers the program gives [Born's answer](/wiki/gravity/momentum-graviton/borns-answer): momentum-space geometry is dynamical, carried by a massive, reciprocity-odd spin-2 field.

How far the answer reaches is recorded in the toy models. A coupling of matter to the [order parameter](/wiki/symmetry-breaking/order-parameter) makes interactions local in x in one vacuum and local in p in its mirror, which passes criterion S5 in its weak form [V] ([locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling); checked in `verify/toy_s5.py`, see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)). Nothing in the models forces that coupling. The worklog's conclusion: "the program's explanation of 'forces fade with distance' amounts to this: our matter is the x-polarized species", and "It does not derive x-locality from nothing" (toy worklog, 'Chunk 4'). Deriving it is [open](/wiki/symmetry-breaking/strong-locality).

## Used by

- [The hard core](/wiki/program/hard-core) — the program's answer: reciprocity is exact in the laws and spontaneously broken by the vacuum.
- [Mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking) — why some polarization must be selected at all.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — the postulate that our vacuum is the position-tilted one.
- [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) — the toy-model test of the claim that "forces fade with distance, never with velocity difference" because the vacuum is polarized (worklog criterion S5).
- [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) — the part of the question the toy models leave open.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) — the program's reply on the flat momentum fibers of general relativity.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — #13's positional twin of the mass shell.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the question, the dynamical asymmetry, the flat fibers, the program's answer and the Freidel–Leigh–Minic credit; refs [1]–[6], [26]
- `notes/broken-born-program-v1.md` §1 — the Hamiltonian p²/2m + V(x), the commutator and the mass shell (v1, superseded as reference by #11)
- `papers/conjugate-special-relativity.md` §4 — the mass shell p_μp^μ = m²c², its Born image, and Born's aim of a fundamental mass and length
- `papers/reciprocity-toy-models.md` §1 — ρ as a symplectic matrix squaring to −1; the Langmann–Szabo duality and the Grosse–Wulkenhaar model; Abstract and §3 — the duality only a covariance for real fields
- `notes/toy-lagrangian.md` 'Success criteria', 'Chunk 4' — criterion S5, which ties the locality asymmetry to the vacuum, and its outcome
- `review/round3/referee/audit-notes.md` Step 1 — the check of the Born citations
- `verify/toy_s5.py` — the machine check of the weak form of S5
- `popsci/universes-other-half.md` 'Two descriptions of one thing' — the waveform–spectrum picture and the one-direction observation (popular article; not a status source)
- `popsci/angle-of-the-mirror.md` opening paragraphs — Born's question as the program's starting point; "eighty-eight years in a drawer" (popular article)
