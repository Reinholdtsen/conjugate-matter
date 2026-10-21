---
title: "The dual superconductor"
weight: 30
status: established
description: "Confinement by monopole condensation ('t Hooft–Mandelstam): color-electric flux squeezed into strings, the leading picture of why free quarks are never seen."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.2"
  - "papers/broken-born-checkpoint-v2.md App. A item 11"
  - "papers/broken-born-checkpoint-v2.md §11 (italic opening)"
  - "HANDOFF.md §3"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The dual superconductor is the leading picture of quark confinement, the observed fact that quarks are never found in isolation. In an ordinary superconductor a condensate of paired electrons expels magnetic field and squeezes whatever magnetic flux remains into thin tubes. In the dual picture, proposed by 't Hooft and Mandelstam, the vacuum of the strong interaction holds a condensate of magnetic monopoles, which squeezes the color-electric field between quarks into a string whose energy grows with its length, so that pulling two quarks apart never frees either of them. It is one of the three pieces of established physics that absorbed the program's founding supposition 11, a magnetic counterpart for every electric particle; the program adds no claim of its own here.*

**Status:** Established — [T] — the checkpoint tags the picture [T] and credits 't Hooft–Mandelstam†, a citation from model memory with no entry in its reference list, so it awaits [the † literature battery](/wiki/method/literature-battery). The explanations below are textbook physics [T], and the references they add are marked †. No program document computes anything about confinement.

## What confinement is [T]

Quarks carry a charge called color, the source of the strong interaction, which is described by quantum chromodynamics (QCD). Every particle ever observed is color-neutral: a quark bound to an antiquark (a meson) or three quarks bound together (a baryon, such as the proton). No experiment has isolated a single quark.

The reason is the way the energy of a quark–antiquark pair grows with their separation r. Between an electron and a positron the field spreads into all of space, and the energy needed to separate them approaches a finite value. Between a quark and an antiquark the color-electric field does not spread: it is concentrated in a narrow tube, a "string", whose energy per unit length is constant, so the energy grows in proportion to r. Pulling the pair apart stores energy in the string until it becomes cheaper to create a new quark–antiquark pair from the vacuum. The string then breaks into two shorter strings, each ending on a quark and an antiquark, and the result is two mesons rather than a free quark.

Numerical simulations of QCD on a space-time lattice show this behaviour, but no analytic derivation of confinement from the theory's equations exists. The dual superconductor is a mechanism proposed to explain why the field forms a tube.

## The ordinary superconductor [T]

Below a critical temperature, the electrons of a superconductor bind into pairs that condense into one coherent quantum state (the Bardeen–Cooper–Schrieffer (BCS) theory). The condensate is electrically charged, and it expels magnetic field from the bulk of the material: the Meissner effect. In type II superconductors a strong field penetrates only along thin tubes, Abrikosov vortices, each carrying one quantum of magnetic flux and costing a fixed energy per unit length.

Suppose a magnetic monopole and an antimonopole were embedded in such a material. Their magnetic flux could not spread out; it would run through one tube between them, and the energy would grow in proportion to their separation. In a superconductor, magnetic charges would be confined.

## The dual picture [T]

The dual superconductor exchanges the roles of electric and magnetic fields in that thought experiment, which is [electric–magnetic duality](/wiki/electric-magnetic-duality) applied to a medium:

| | ordinary superconductor | dual superconductor (QCD vacuum) |
| --- | --- | --- |
| what condenses | electrically charged pairs | magnetically charged monopoles |
| what is expelled | magnetic field | color-electric field |
| what is confined into tubes | magnetic flux | color-electric flux |
| what is confined | magnetic charges | color-electric charges: quarks |

#11 states it in one line: "the dual-superconductor picture of confinement — chromomagnetic monopole condensation squeezing color-electric flux into strings — is the leading mechanism for why free quarks are never seen [T, 't Hooft–Mandelstam†]" (§11.2). Chromomagnetic monopoles are magnetic charges of the color field; monopoles in general are the subject of [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles).

QCD has no Higgs field of the kind that produces ['t Hooft–Polyakov monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole), so the monopoles of the picture have to be identified another way. 't Hooft's proposal was to fix the gauge so that only the abelian, electromagnetism-like part of the color symmetry is left; the gauge-fixing then leaves point-like defects that behave as magnetic monopoles of the remaining abelian fields [T]. Lattice studies in such gauges have been used to test whether these monopoles condense in the confining phase. The picture remains a mechanism rather than a derivation, and other accounts of confinement exist [T].

The cleanest realization is in a supersymmetric theory. In N = 2 super Yang–Mills theory with its supersymmetry partly broken, Seiberg and Witten found the exact low-energy description, in which magnetic monopoles become light, condense, and confine electric charge in just this way [T]. It is the same body of work in which electric–magnetic duality is under good control ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)).

## Where it enters the program

The dual superconductor is one of the three established results that #11 lists against P.R.'s founding supposition 11, a magnetic counterpart for every electrically charged particle:

- **The fate of the supposition** (#11 App. A item 11): "A full magnetic mirror-family, quarks included — alive as established physics (Montonen–Olive, Seiberg, dual superconductor), absorbed as §11 with the polarization identification as the program-native addition" ([the magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family); [founding suppositions and their fates](/wiki/program/founding-suppositions)).
- **The vocabulary.** Magnetic counterparts of quarks appear in Seiberg's dualities: "magnetic quarks" is "standard vocabulary via Seiberg duality [18†]" (#11 §11.2).
- **How #11 describes the idea's standing.** The italic opening of §11 says the mirror-family is "suspected today of being the very mechanism that confines quarks". The technical record's word is "leading", and its tag is [T].

The program's own addition to the supposition is not about confinement. It is the observation that choosing which particles count as electric is a choice of polarization ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)).

## Popsci-only: "inside every proton"

[The popular article #12](/wiki/history/documents/popular-articles) calls the dual superconductor the mechanism "most widely credited" for confinement and draws a conclusion from it ('Dark matter as the other polarization'): "If that picture is correct, magnetic analogs of quarks are not hypothetical inhabitants of a hidden sector; their condensed form is at work inside every proton."

The second sentence is conditional, and #12 is never a source for a claim's status. The same passage goes on to place the "free spectrum" of the magnetic family in the momentum-polarized sector, a claim found only in #12 and recorded as dead ([Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification)). The handoff lists the "magnetic-quark/dual-superconductor section" among #12's contents (`HANDOFF.md` §3).

## Standard references

The checkpoint's attribution is "'t Hooft–Mandelstam†", with no entry in its reference list. Added by the wiki from model memory (†):

- Y. Nambu (1974)†; S. Mandelstam (1976)†; G. 't Hooft (1976, 1981)†: confinement as a dual Meissner effect, and 't Hooft's abelian gauge-fixing.
- J. Bardeen, L. N. Cooper and J. R. Schrieffer (1957)†: the theory of superconductivity.
- A. A. Abrikosov (1957)†: flux tubes in type II superconductors.
- N. Seiberg and E. Witten (1994)†: monopole condensation and confinement in N = 2 super Yang–Mills theory broken to N = 1.

## Used by

- [The magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family) — one of the three established results that absorbed founding supposition 11.
- [Founding suppositions and their fates](/wiki/program/founding-suppositions) — item 11, "alive as established physics".

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.2 — the statement, tagged [T] with 't Hooft–Mandelstam†; §11 italic opening — "suspected today of being the very mechanism that confines quarks"; App. A item 11 — the fate of founding supposition 11.
- `HANDOFF.md` §3 — #12's "magnetic-quark/dual-superconductor section".
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the popular account and its conditional "inside every proton" (not a status source).
