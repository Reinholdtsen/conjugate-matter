---
title: "Row 2: isotropic scattering below the gate"
weight: 30
status: alive
description: "Below the gate velocity, gated scattering through a heavy mediator is isotropic, unlike the forward-peaked scattering of light-mediator models; killed by halo morphology that demands forward peaking."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 2"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes)'"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-program-v1.md §9"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/wave-island.md 'Standing results after Chunks A+B'"
  - "notes/ufd-endpoint.md 'Verdict and closure of the clumping problem'"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §3"
  - "notes/gate-mechanism.md §5"
---

*Row 2 of [the predictions table](/wiki/predictions) concerns the directions into which colliding [dark-matter](/wiki/dark-matter) particles scatter. In the usual self-interacting models, where a light particle carries the force, most collisions deflect the particles only slightly, so the scattering is forward-peaked. In the program's gated model, collisions slower than the gate velocity scatter equally in all directions, because the gate depends on the speed of the collision and not on its angle. The two patterns move energy and momentum through a halo with different efficiencies, so in principle they leave different imprints on the shapes of relaxed halos. The row stands with one stated assumption, that the particle carrying the gated force is heavy. It holds for dark matter made of particles; for a wave field it has not been restated.*

**Status:** Alive — [D] in [the lab notebook](/wiki/history/documents/lab-notebook) (#1 §5.1), restated in #11 §8, whose amplitude is tagged [D — mechanism; shape [O]] — it follows from the gate's dependence on the relative momentum of the colliding pair rather than on the momentum transferred; it assumes a heavy mediator, holds on [the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem#the-particle-island) only, and is not machine-checked. No source records a test. The row is among the text that depends on the mechanism's tag: `notes/gate-mechanism.md` (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging #11 §7's X cannot produce the gate, and flag 55 in `review/wiki-build-flags.md` proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling; #11 is unchanged ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The argument for isotropy uses only the gate's dependence on k, so it does not depend on how the gate arises.

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 2:

| Observable | Standard expectation | Program requirement | Killed by |
| --- | --- | --- | --- |
| Scattering anisotropy | Forward-peaked (light mediators) | Isotropic below the gate | Morphology demanding forward peaking |

The row is the angular companion of [row 1](/wiki/predictions/self-interaction-knee): row 1 says how strongly dark matter scatters off itself at each speed, and row 2 says in which directions it scatters below the knee. Both come from the same scattering law, stated in one sentence of #11 §8: "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking" ([the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law#the-law); [Yukawa forward peaking](/wiki/gravity/spin-2-fields/yukawa-forces#the-light-mediator-limit-forward-peaking-and-the-coulomb-logarithm)).

## The observable

A collision between two particles of equal mass, viewed in their centre-of-mass frame, turns their momenta through some angle θ. The differential cross-section dσ/dΩ says how the collisions are distributed over angle. If it is the same for every θ, the scattering is isotropic; if it is concentrated at small θ, most collisions are grazing, and the scattering is forward-peaked [T].

The angle matters for a halo because a grazing collision moves little momentum or energy between particles. Self-scattering is therefore quoted through the momentum-transfer cross-section σ_T, which weights each angle by (1 − cos θ), and the conversion from cross-section to halo evolution depends on the angular pattern [T] ([the angular pattern](/wiki/dark-matter/halo-astrophysics/transfer-cross-section#the-angular-pattern-t)). The [lab notebook](/wiki/history/documents/lab-notebook) states the consequence the row relies on: "Energy- vs momentum-transport efficiencies differ, which feeds into halo relaxation morphology" (#1 §5.1; quotations from #1 on this page are transcribed from its LaTeX). Halo relaxation morphology, the structure a halo settles into as scattering redistributes heat, is the observable named in the earlier versions of the row: "Scattering anisotropy (via halo relaxation morphology)" (#1 §9), "Scattering anisotropy (halo relaxation morphology)" (#9 §9).

## The standard expectation

The usual model of self-interacting dark matter (SIDM) carries the force on a mediator of mass m_φ. In the Born approximation the amplitude goes as 1/(q² + m_φ²), where q is the momentum transfer [T]. For a collision with incoming relative momentum k, the transfer is q = 2k sin(θ/2), running from zero for a grazing collision to 2k for a head-on rebound [T] ([what a position-local force depends on](/wiki/dark-matter/conjugate-matter/velocity-gate#background-what-a-position-local-force-depends-on-t)).

When the mediator is light, so that m_φ is small compared with the transfers a collision can reach, the amplitude grows as 1/q² toward small q, the Rutherford form, and the collisions concentrate at small angles [T] ([contact and Yukawa forces](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#contact-and-yukawa-forces)). The lab notebook: "light-mediator Yukawa scattering is forward-peaked" (#1 §5.1). The same small-angle dominance gives the light-mediator cross-section its v⁻⁴ fall with a Coulomb logarithm, which is row 1's standard expectation.

## The program's requirement

### The argument

The lab notebook derives isotropy as the second of "Two structural signatures" that distinguish the gated law "from *every* x-local mediator model", x-local meaning local in position (#1 §5.1, [D]):

> "**Isotropy inside the gate.** Because the gate depends on k and the contact part is flat in q, scattering below v\* is isotropic; light-mediator Yukawa scattering is forward-peaked."

The argument runs through the amplitude of [conjugate matter χ](/wiki/dark-matter/conjugate-matter), as #11 §8 writes it:

```text
M(k, q) = 4πα̃ m_χ / (q² + m_φ²) · F(k²/μ²)
```

Here k is the incoming relative momentum, q the transfer, α̃ the coupling, m_φ the mediator mass, μ the momentum width of a χ quantum and F the gate function ([the velocity gate: the amplitude](/wiki/dark-matter/conjugate-matter/velocity-gate#the-amplitude)). The steps, as the wiki reads the notebook's one sentence:

1. **The gate does not depend on angle.** F depends on k, and k is fixed by the speed of the collision, the same before and after it. Whatever its shape, the gate multiplies every scattering angle by the same factor. That a factor of this kind exists at all is the distinctive feature of the program's force: k is "the variable no x-local mediator produces" (#11 §8), and the program obtains it from [exchange of the momentum graviton X](/wiki/dark-matter/conjugate-matter/gate-mechanism#the-derivation-as-the-sources-give-it) (not derived, according to flag 55 in `review/wiki-build-flags.md`, pending Paul's ruling; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The gate-mechanism note qualifies the quoted phrase: "§8's 'the variable no x-local mediator produces' holds only for the direct Born term. Exchange terms and near-threshold states of x-local forces do depend on k at fixed q" (`notes/gate-mechanism.md` §3). Of its two reconstructions of #6 §4's fiber overlap, the pair-channel reading R2 gives an amplitude that is "isotropic, and exactly §8's gate when the transfer factor is flat" (§3; one derivation), but it contains no X ([the fiber overlap, read two ways](/wiki/dark-matter/conjugate-matter/gate-mechanism#the-fiber-overlap-read-two-ways)).
2. **The contact part is flat in q.** The derivation assumes "a heavy transfer mediator (m_φ ≳ m_χ, contact-like in x)" (#1 §5.1). For slow particles q is at most 2k, far below m_χ, so with m_φ ≳ m_χ the factor 1/(q² + m_φ²) is close to the constant 1/m_φ² [T] ([the flat part](/wiki/dark-matter/conjugate-matter/scattering-law#how-the-lab-notebook-derived-it)).
3. **So the angular distribution is flat.** With neither factor depending on θ, dσ/dΩ is the same in every direction [T].

### The heavy-mediator assumption

Step 2 carries the assumption. The notebook's [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) uses the same choice, "With m_φ ∼ m_χ this fixes" the benchmark mass (#1 §5.1). #11 §8 restates the conclusion, "isotropic below the gate versus Yukawa forward-peaking", but not the assumption, and v1 does the same (#9 §6). No source discusses gated scattering through a light mediator, for which the first factor would again depend on the angle [T].

The notebook's other caveat concerns the Born approximation itself: "At α̃ ~ 1 the Born approximation is marginal (expect O(1) corrections); the *shape* claims above survive because they follow from the k- vs q-dependence, not from the coupling strength" (#1 §5.1). Isotropy is one of those shape claims.

### Below the gate

The requirement is stated "below the gate" (#11; v1) or "below v\*" (#1 §9), the speeds at which pairs pass through the gate and scatter with the full cross-section σ₀. Above the knee the scattering is suppressed, which is row 1's subject.

## What kills it

"Morphology demanding forward peaking" (#11 §13). Earlier wording was more specific about the method: "Morphology fits demanding forward-peaked kernels" (#1 §9), "Morphology demanding forward-peaked kernels" (#9 §9). A kernel here is the angular distribution of scattering used in a model of halo evolution; the condition is met if fits of observed halo structure require a forward-peaked kernel rather than an isotropic one.

The sources stop at that sentence. None computes how isotropic and forward-peaked scattering would differ in a halo's structure, names a morphological quantity or a dataset, or says how strong a preference would count as a kill. The row therefore states a direction of test rather than a quantitative one.

## The data situation

No source records a measurement or a fit that tests the row. #11 §15 names rows 1, 4 and 7 as the program's near-term falsification exposure; row 2 is not among them. Neither popular article (#10, #12) mentions the angular pattern; #12's account of dark matter's self-interaction covers only the knee ([the popular articles](/wiki/history/documents/popular-articles)).

## Particles only

The argument is a two-body Born calculation, and it holds on the particle island, where χ is a gas of classical particles. The clumping calc notes, which established that collective effects need a wave ([the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)), kept the row on that island and left it open on the other ([the clumping calc notes](/wiki/history/documents/clumping-notes)):

- Calc note #2: on the particle island "Rows 1–2 (exponential cliff, isotropy) **survive** — they are collisional"; on the wave island "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)" (`notes/stream-stability.md`, 'Consequences for the predictions table').
- Calc note #3: "Particle island: cliff (exponential) + isotropy live; no collective phenomena. Fully classical, fully collisional." (`notes/wave-island.md`, 'Standing results after Chunks A+B').
- Calc note #4 lists "the exponential cliff + in-gate isotropy (particle island)" among what remains distinctively the program's own (`notes/ufd-endpoint.md`, 'Verdict and closure of the clumping problem').

The wave-island suppression law answers the re-derivation for the knee's tail only. No document restates isotropy for [the wave island](/wiki/dark-matter/momentum-clumping/wave-island), and #11 §14 does not itemize the task ([Open: rows 1 and 2 in wave language](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#open-rows-1-and-2-in-wave-language)). The notes still speak of an "exponential cliff" because they predate the downgrade of row 1 to a knee.

## Where the row is used

- **The candidates.** #11 §12 lists "isotropic scattering" among the distinctive handles of [the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles), with "knee at v\*, sharp tail" and "permanent direct-detection null". The handles of [the X-condensate](/wiki/dark-matter/candidates/x-condensate) do not include it.
- **Row 11.** Rows 1–3 are the discriminators of [row 11, particles or condensate](/wiki/predictions/dark-sector-microstructure): "Particles vs condensate, separable via rows 1–3 + coherence signatures" (#11 §13).
- **The neighbouring rows.** [Row 1](/wiki/predictions/self-interaction-knee) tests the strength of the same scattering, and [row 3, the island discriminant](/wiki/predictions/island-discriminant), the shape of its tail.

## History

| Version | Observable | Requirement | Killed by |
| --- | --- | --- | --- |
| v0.1 (#1 §9) | "Scattering anisotropy (via halo relaxation morphology)" | "Isotropic below v\*" | "Morphology fits demanding forward-peaked kernels" |
| v1 (#9 §9) | "Scattering anisotropy (halo relaxation morphology)" | "Isotropic below the gate" | "Morphology demanding forward-peaked kernels" |
| #11 §13 | "Scattering anisotropy" | "Isotropic below the gate" | "Morphology demanding forward peaking" |

v0.1's standard expectation read "Forward-peaked (light mediator)", and v1 and #11 make it plural. After the clumping problem the lab notebook's v0.2 addendum listed "rows 1–2 (cliff, isotropy)" first among "The program's distinctive, still-live content". Unlike row 1, row 2 did not change in substance when the gate's mechanism was derived, because the argument uses only the gate's dependence on k, not its shape. The renumbering of the whole table is on [the history of the predictions table](/wiki/predictions/table-history).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 2 — the row; §8 — the amplitude, its tags and "isotropic below the gate versus Yukawa forward-peaking"; §12 — the χ-particle handles; §15 — the near-term exposure rows
- `notes/broken-born-theory.md` §5.1 — the derivation of isotropy [D], the heavy-mediator assumption, the Born caveat and the transport remark; §3 — the v0.1 amplitude and k; §9 — the v0.1 row 2; 'Addendum (v0.2, after the clumping notes)' — rows 1–2 among the live content
- `notes/broken-born-program-v1.md` §6, §9 — v1's statement and row 2
- `notes/stream-stability.md` 'Consequences for the predictions table' — rows 1–2 survive on the particle island, to be re-derived for waves
- `notes/gate-mechanism.md` §3 — "the variable no x-local mediator produces" holds only for the direct Born term; reading R2 isotropic; §5 — rows 1–3 among the text that depends on the tag
- `review/wiki-build-flags.md` item 55 — the gate's mechanism not derived, awaiting Paul's ruling
- `notes/wave-island.md` 'Standing results after Chunks A+B' and `notes/ufd-endpoint.md` 'Verdict and closure of the clumping problem' — in-gate isotropy as surviving particle-island content
