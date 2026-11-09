---
title: "Open: the two dual cones"
weight: 100
status: open
description: "#13 §1 uses a 3+1 cone in (t, p) with slope c̃, while §6 calls E = c|p| the dual null cone, which belongs to the 4D map; which construction governs — and the Fermi-LAT 'joint test' that depends on it — is unsettled."
sources:
  - "review/v3-worklog.md 'New open items'"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §2"
  - "wiki/papers/conjugate-special-relativity.md §4"
  - "wiki/papers/conjugate-special-relativity.md §6"
  - "wiki/papers/conjugate-special-relativity.md preamble"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 9"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "notes/broken-born-theory.md §4"
  - "notes/knot-dark-matter-standalone.md §1"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/wiki-build-flags.md item 30"
---

*This open problem is an inconsistency inside [#13](_index.md), the paper on the special relativity of the [momentum polarization](../phase-space/reciprocity/lagrangian-polarizations.md): two of its sections use different momentum-space light cones. Section 1 builds the dual cone in time and momentum, with time shared between the two polarizations and the [maximum force c̃](maximum-force.md) as its slope. Section 6 instead calls light's ordinary energy–momentum relation, E = c|p|, the dual null cone; that cone lives in energy and momentum, has slope c, and, in the analysis of the v3 worklog, belongs to a different construction, the [four-dimensional Born map](four-dimensional-born-map.md) that also exchanges time and energy and has not been built. Section 6's claim that [photon-dispersion measurements](../predictions/photon-dispersion.md) test both cones at once depends on the second reading. P.R. raised the problem while the [withdrawn soliton manuscript](../dark-matter/candidates/soliton-candidate/obituary.md) was being revised, and the worklog asks that the two cones be fixed and the governing construction settled before any paper claims more. It is on neither [#11](../papers/broken-born-checkpoint-v2.md)'s [list of open problems](../status/open-problems.md) nor the current queue, and no later document takes it up.*

**Status:** Open — no tag in the source (worklog item O3) — raised by P.R. in [`review/v3-worklog.md`](../../review/v3-worklog.md); not in [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems), the current queue in [`CLAUDE.md`](../../CLAUDE.md) or the [round-3 decisions](../method/review/round-3/decisions.md); unresolved. It qualifies [two causal cones](two-causal-cones.md), and [#13](../papers/conjugate-special-relativity.md) itself is unreviewed, with no script checking its derivations, and not mentioned in [#11](../history/documents/checkpoint.md). Listed in [Open problems and the queue](../status/open-problems.md).

## The two cones

### §1: a cone in time and momentum

[#13 §1](../papers/conjugate-special-relativity.md#1-two-causal-cones) starts from the block form H = diag(g, g⁻¹), which gives position space the metric g and momentum space its inverse: "Each metric defines a null cone. Ours bounds trajectories x(t): |dx/dt| ≤ c. The dual cone bounds trajectories p(t):"

```text
|dp/dt| ≤ c̃ = ε/(λ/c) = ℏc/λ²
```

with λ the [Born length](../phase-space/reciprocity/born-length.md) and ε = ℏ/λ ([two causal cones](two-causal-cones.md); [the maximum force c̃ = c⁴/G](maximum-force.md)). §2 writes the corresponding interval, "The dual interval on (t, **p**) is ds̃² = c̃²dt² − d**p**², preserved by rotations in the (c̃t, p) planes — the dual Lorentz group [D — structural]" ([force boosts and force composition](force-boosts.md)). A trajectory is dual-null when ds̃² = 0, that is when |dp/dt| = c̃: the cone has slope c̃ in the (t, p) plane, and its null directions are motions through momentum space at the maximum force. Time is the coordinate both polarizations share. The worklog's summary: "§1 uses the 3+1 version (shared time): the cone lives in (t, p) with slope c̃."

### §6: a cone in energy and momentum

A massless particle has E = c|p|, the mass shell p_μp^μ = m²c² at m = 0 [T]. In the space of energy and momentum this is a cone of slope c, on which the energy and momentum of every photon lie ([special relativity: the template](special-relativity.md)). [#13 §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) identifies it with the dual cone:

> "One free consistency check already available: since our massless dispersion E = c|p| *is* the dual null cone, the Fermi-LAT bounds excluding linear photon-dispersion violations [T] constrain both cones at once — every test of our light cone's rigidity has been, unknowingly, a test of theirs."

The worklog places that identification in the other construction: it "belongs to the 4D Born map (t ↔ E): a cone in (E, p) with slope c. Under the 4D map, anything on our light cone is automatically dual-null." The same §6 lists that map as open: "the fully covariant construction with the four-dimensional Born map (t ↔ E), in which the dual "time" direction is our energy axis" ([Open: the four-dimensional Born map and dual dynamics](four-dimensional-born-map.md)). With energy as the dual time direction, a dual cone is a cone in (E, p), and E = c|p| is one.

### Side by side

| | [#13 §1](../papers/conjugate-special-relativity.md#1-two-causal-cones) (and [§2](../papers/conjugate-special-relativity.md#2-force-boosts)) | [#13 §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) |
| --- | --- | --- |
| coordinates | time and momentum, (t, p) | energy and momentum, (E, p) |
| slope | c̃, a force | c, a speed |
| construction | 3+1: space and momentum exchanged, time shared | the four-dimensional Born map, t ↔ E (unbuilt) |
| on the null cone | a trajectory with \|dp/dt\| = c̃; "a λ = 0 quantum" (worklog) | "anything on our light cone" (worklog), such as a photon |

## What depends on the choice

### The photon-dispersion argument

Some approaches to quantum gravity allow the speed of light to depend on its energy, with a correction linear in E divided by a large energy scale [T]. A distant gamma-ray burst emits photons of very different energies at nearly the same moment, so their arrival times bound such a term; [the lab notebook](../history/documents/lab-notebook.md) records that bounds from bursts seen by the Fermi Large Area Telescope (Fermi-LAT) "exclude linear Planck-scale dispersion" ([#1 §4](../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured), [T], no reference given). The checkpoint's own requirement is "Linear exactly zero (ρ²-protected); quadratic suppressed", killed by a "Confirmed linear-in-E dispersion" ([#11 §13 row 9](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions); [Row 9: no linear photon dispersion](../predictions/photon-dispersion.md)), stated without reference to #13.

[#13 §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open)'s step from these bounds to "both cones at once" uses the [§6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) identification of E = c|p| as the dual null cone. #13 gives no version of the argument for the [§1](../papers/conjugate-special-relativity.md#1-two-causal-cones) cone, whose null directions are rates of change of momentum at the maximum force, and the worklog supplies none.

### Which quanta are dual-null

The worklog's item O3 notes that "a λ = 0 quantum would sit on the dual null cone with |dp/dt| = c̃", which is the null condition of the §1 cone; λ is the invariant length that [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) assigns to conjugate quanta ([the invariant-length shell](invariant-length-shell.md)). Under the four-dimensional map, "anything on our light cone is automatically dual-null", massless quanta included. The two readings thus make different quanta dual-null, and the worklog assigns the resulting question to the dual dynamics:

> Whether the dark photon is m = 0, λ = 0, or both is part of #13's open "dual dynamics" item.

### The rest of #13

#13's other kinematics use the shared time of [§1](../papers/conjugate-special-relativity.md#1-two-causal-cones): the force boosts of [§2](../papers/conjugate-special-relativity.md#2-force-boosts), the dual proper time of [§3](../papers/conjugate-special-relativity.md#3-force-dilation-and-its-mirror) ([force dilation](force-dilation.md)) and the dual-inertial condition dp/dt = 0 of [§5](../papers/conjugate-special-relativity.md#5-inertia-dualized) ([dual inertia](dual-inertia.md)). [§6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open)'s plain-language passage describes that choice as "the tidiest version of this construction treats space and momentum as partners while leaving time alone". The invariant-length shell of [§4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) is written with four-vectors, and #13 does not say which construction it belongs to ([the invariant-length shell: what #13 leaves unspecified](invariant-length-shell.md#what-13-leaves-unspecified)). The worklog cites [§4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) only for its labelling of conjugate quanta by a length.

## How it was found

The problem was found while the soliton manuscript [#14](../../notes/knot-dark-matter-standalone.md) was being revised to its v3, on 2026-10-19. The worklog's item O3, headed "the dark sector in dual kinematics", begins:

> "#14 describes the dark sector entirely in our kinematics: GeV masses, 10⁻³ c drift, an ordinary massless dark photon moving at c. [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) labels conjugate quanta by an invariant length λ instead of a mass, and a λ = 0 quantum would sit on the dual null cone with |dp/dt| = c̃. The papers were never reconciled."

[#14 §1](../../notes/knot-dark-matter-standalone.md#1-framework) had stated its choice: "Throughout, the hidden sector is described by ordinary relativistic quantum field theory." The decision for v3 was to "keep the dark sector in ordinary kinematics and say so explicitly. L1 and O2 both rest on that." (L1 and O2 are the worklog's findings that [kinetic mixing](../dark-matter/candidates/soliton-candidate/kinetic-mixing.md) does not give the monopoles a visible charge and that dark radiation is not fatal if the dark sector is cooler.) #14 was later withdrawn on other grounds ([Obituary: #14's superheavy-soliton model](../dark-matter/candidates/soliton-candidate/obituary.md); [Under review: the hidden SU(2) → U(1) proposal](../dark-matter/candidates/soliton-candidate/hidden-sector.md)). The item closes with the task P.R. raised:

> "Before any paper claims more: fix #13's two cones and settle which construction governs"

[#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) quotes the same sentence of [#14 §1](../../notes/knot-dark-matter-standalone.md#1-framework). #14's model did not treat localization in momentum, so the candidate itself has not been tested: conjugate monopoles localized in momentum are P.R.'s open conjecture ([Conjecture: magnetic monopoles abundant in momentum space](../dark-matter/candidates/momentum-space-monopoles.md)).

## What settling it involves

The item names two tasks: fix the two cones, and settle which construction governs. #13 itself frames the alternatives. Its §1–§3 and §5 are written in the 3+1 presentation, and [§6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) calls the four-dimensional map "the natural home of this paper's kinematics and a required step before the dual dynamics (their Maxwell, their field theory) can be written". The map is unbuilt, so a choice for it depends on [the open construction](four-dimensional-born-map.md); a choice for the 3+1 cone leaves [§6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open)'s joint-test claim without the cone it uses. No document has attempted either.

Both cones are Lorentzian objects, and #13's preamble inherits the checkpoint's open signature caveat: "The Euclidean/Lorentzian caveat of the main checkpoint is inherited throughout" ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](../phase-space/born-geometry/lorentzian-dressing.md)). Flag 30 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) records the same point against §1's tag [D — compatibility theorem]: the theorem's g is positive-definite and has no null cone. The flags' audit found the tag on the block form H = diag(g, g⁻¹) rather than on the cones, and rated the flag as a question of tagging convention.

## Where it stands

The item appears only in the worklog. It is not among [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems)'s twelve open problems, not in the current queue in [`CLAUDE.md`](../../CLAUDE.md) ('Since the handoff'), and not in the round-3 decisions ([`review/round3-adjudication.md`](../../review/round3-adjudication.md), 'Decisions'). #13 has not been revised in substance since its import on 2026-10-19, so not since the problem was raised, and no review round has covered it ([conjugate special relativity](_index.md)). The conflict is recorded as unresolved on [conflicts between sources](../history/documents/source-conflicts.md).

## Sources

- [`review/v3-worklog.md`](../../review/v3-worklog.md) 'New open items' — item O3: the two cones, the dark-sector kinematics, the dark-photon question, the v3 decision and the two tasks.
- [`wiki/papers/conjugate-special-relativity.md` §1](../papers/conjugate-special-relativity.md#1-two-causal-cones), [§2](../papers/conjugate-special-relativity.md#2-force-boosts) — the 3+1 cone and the dual interval; [§4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) for the invariant length; [§6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) for E = c|p| as the dual null cone, the photon-dispersion argument, the open four-dimensional map and the 3+1 presentation; preamble for the inherited Euclidean/Lorentzian caveat.
- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — #14's ordinary kinematics, which left the candidate it modeled untested; §13 row 9 — #11's own photon-dispersion requirement; [§14](../papers/broken-born-checkpoint-v2.md#14-open-problems) for the open problems, which do not include this item.
- [`notes/broken-born-theory.md` §4](../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured) — the Fermi-LAT bounds on linear dispersion (superseded as a reference).
- [`notes/knot-dark-matter-standalone.md` §1](../../notes/knot-dark-matter-standalone.md#1-framework) — #14's ordinary kinematics (withdrawn).
- [`CLAUDE.md`](../../CLAUDE.md) 'Since the handoff' — the current queue.
- [`review/round3-adjudication.md`](../../review/round3-adjudication.md) 'Decisions' — the round-3 decisions, which do not include it.
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 30 — §1's tag [D — compatibility theorem] on the block form from which #13 reads cones that the theorem's positive-definite g cannot have; a question of tagging convention in the flags' audit; pending.
