---
title: "Open: the two dual cones"
weight: 100
status: open
description: "#13 §1 uses a 3+1 cone in (t, p) with slope c̃, while §6 calls E = c|p| the dual null cone, which belongs to the 4D map; which construction governs — and the Fermi-LAT 'joint test' that depends on it — is unsettled."
sources:
  - "review/v3-worklog.md 'New open items'"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §6"
  - "papers/conjugate-special-relativity.md preamble"
  - "papers/broken-born-checkpoint-v2.md §13 row 9"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "notes/broken-born-theory.md §4"
  - "notes/knot-dark-matter-standalone.md §1"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/wiki-build-flags.md item 30"
---

*This open problem is an inconsistency inside [#13](/wiki/conjugate-relativity), the paper on the special relativity of the [momentum polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations): two of its sections use different momentum-space light cones. Section 1 builds the dual cone in time and momentum, with time shared between the two polarizations and the [maximum force c̃](/wiki/conjugate-relativity/maximum-force) as its slope. Section 6 instead calls light's ordinary energy–momentum relation, E = c|p|, the dual null cone; that cone lives in energy and momentum, has slope c, and, in the analysis of the v3 worklog, belongs to a different construction, the [four-dimensional Born map](/wiki/conjugate-relativity/four-dimensional-born-map) that also exchanges time and energy and has not been built. Section 6's claim that [photon-dispersion measurements](/wiki/predictions/photon-dispersion) test both cones at once depends on the second reading. Paul raised the problem on 2026-10-19, while the [withdrawn soliton manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary) was being revised, with the instruction to fix the two cones and settle which construction governs before any paper claims more. It is on neither #11's [list of open problems](/wiki/status/open-problems) nor the current queue, and no document since has taken it up.*

**Status:** Open — no tag in the source (worklog item O3) — raised by Paul on 2026-10-19 in `review/v3-worklog.md`; not in #11 §14, the current queue in `CLAUDE.md` or the [round-3 decisions](/wiki/method/review/round-3/decisions); unresolved. It qualifies [two causal cones](/wiki/conjugate-relativity/two-causal-cones), and #13 itself is unreviewed, unchecked by any script, and not mentioned in [#11](/wiki/history/documents/checkpoint) v2.2. Listed in [Open problems and the queue](/wiki/status/open-problems).

## The two cones

### §1: a cone in time and momentum

#13 §1 starts from the block form H = diag(g, g⁻¹), which gives position space the metric g and momentum space its inverse: "Each metric defines a null cone. Ours bounds trajectories x(t): |dx/dt| ≤ c. The dual cone bounds trajectories p(t):"

```text
|dp/dt| ≤ c̃ = ε/(λ/c) = ℏc/λ²
```

with λ the Born length and ε = ℏ/λ ([two causal cones](/wiki/conjugate-relativity/two-causal-cones); [the maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force)). §2 writes the corresponding interval, "The dual interval on (t, **p**) is ds̃² = c̃²dt² − d**p**², preserved by rotations in the (c̃t, p) planes — the dual Lorentz group [D — structural]" ([force boosts and force composition](/wiki/conjugate-relativity/force-boosts)). A trajectory is dual-null when ds̃² = 0, that is when |dp/dt| = c̃: the cone has slope c̃ in the (t, p) plane, and its null directions are motions through momentum space at the maximum force. Time is the coordinate both polarizations share. The worklog's summary: "§1 uses the 3+1 version (shared time): the cone lives in (t, p) with slope c̃."

### §6: a cone in energy and momentum

A massless particle has E = c|p|, the mass shell p_μp^μ = m²c² at m = 0 [T]. In the space of energy and momentum this is a cone of slope c, on which the energy and momentum of every photon lie ([special relativity: the template](/wiki/conjugate-relativity/special-relativity)). #13 §6 identifies it with the dual cone:

> "One free consistency dividend already available: since our massless dispersion E = c|p| *is* the dual null cone, the Fermi-LAT bounds excluding linear photon-dispersion violations [T] constrain both cones at once — every test of our light cone's rigidity has been, unknowingly, a test of theirs."

The worklog places that identification in the other construction: it "belongs to the 4D Born map (t ↔ E): a cone in (E, p) with slope c. Under the 4D map, anything on our light cone is automatically dual-null." The same §6 lists that map as open: "the fully covariant construction with the four-dimensional Born map (t ↔ E), in which the dual "time" direction is our energy axis" ([Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map)). With energy as the dual time direction, a dual cone is a cone in (E, p), and E = c|p| is one.

### Side by side

| | #13 §1 (and §2) | #13 §6 |
| --- | --- | --- |
| coordinates | time and momentum, (t, p) | energy and momentum, (E, p) |
| slope | c̃, a force | c, a speed |
| construction | 3+1: space and momentum exchanged, time shared | the four-dimensional Born map, t ↔ E (unbuilt) |
| on the null cone | a trajectory with \|dp/dt\| = c̃; "a λ = 0 quantum" (worklog) | "anything on our light cone" (worklog), such as a photon |

## What depends on the choice

### The photon-dispersion argument

Some approaches to quantum gravity allow the speed of light to depend on its energy, with a correction linear in E divided by a large energy scale [T]. A distant gamma-ray burst emits photons of very different energies at nearly the same moment, so their arrival times bound such a term; [the lab notebook](/wiki/history/documents/lab-notebook) records that bounds from bursts seen by the Fermi Large Area Telescope (Fermi-LAT) "exclude linear Planck-scale dispersion" (#1 §4, [T], no reference given). The checkpoint's own requirement is "Linear exactly zero (ρ²-protected); quadratic suppressed", killed by a "Confirmed linear-in-E dispersion" (#11 §13 row 9; [Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion)), stated without reference to #13.

#13 §6's step from these bounds to "both cones at once" uses the §6 identification of E = c|p| as the dual null cone. #13 gives no version of the argument for the §1 cone, whose null directions are rates of change of momentum at the maximum force, and the worklog supplies none.

### Which quanta are dual-null

The worklog's item O3 notes that "a λ = 0 quantum would sit on the dual null cone with |dp/dt| = c̃", which is the null condition of the §1 cone; λ is the invariant length that #13 §4 assigns to conjugate quanta ([the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)). Under the four-dimensional map, "anything on our light cone is automatically dual-null", massless quanta included. The two readings thus make different quanta dual-null, and the worklog assigns the resulting question to the dual dynamics:

> Whether the dark photon is m = 0, λ = 0, or both is part of #13's open "dual dynamics" item.

### The rest of #13

#13's other kinematics use the shared time of §1: the force boosts of §2, the dual proper time of §3 ([force dilation](/wiki/conjugate-relativity/force-dilation)) and the dual-inertial condition dp/dt = 0 of §5 ([dual inertia](/wiki/conjugate-relativity/dual-inertia)). §6's plain-language passage describes that choice as "the tidiest version of this construction treats space and momentum as partners while leaving time alone". The invariant-length shell of §4 is written with four-vectors, and #13 does not say which construction it belongs to ([the invariant-length shell: what #13 leaves unspecified](/wiki/conjugate-relativity/invariant-length-shell#what-13-leaves-unspecified)). The worklog cites §4 only for its labelling of conjugate quanta by a length.

## How it was found

The problem was found while the soliton manuscript #14 was being revised to its v3, on 2026-10-19. The worklog's item O3, headed "the dark sector in dual kinematics", begins:

> "#14 describes the dark sector entirely in our kinematics: GeV masses, 10⁻³ c drift, an ordinary massless dark photon moving at c. #13 §4 labels conjugate quanta by an invariant length λ instead of a mass, and a λ = 0 quantum would sit on the dual null cone with |dp/dt| = c̃. The papers were never reconciled."

#14 §1 had stated its choice: "Throughout, the hidden sector is described by ordinary relativistic quantum field theory." The decision for v3 was to "keep the dark sector in ordinary kinematics and say so explicitly. L1 and O2 both rest on that." (L1 and O2 are the worklog's findings that [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) does not give the monopoles a visible charge and that dark radiation is not fatal if the dark sector is cooler.) #14 was later withdrawn on other grounds ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary); [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). The item closes with Paul's instruction:

> "Before any paper claims more: fix #13's two cones and settle which construction governs (raised by Paul, 2026-10-19)."

## What settling it involves

The instruction names two tasks: fix the two cones, and settle which construction governs. #13 itself frames the alternatives. Its §1–§3 and §5 are written in the 3+1 presentation, and §6 calls the four-dimensional map "the natural home of this paper's kinematics and a required step before the dual dynamics (their Maxwell, their field theory) can be written". The map is unbuilt, so a choice for it depends on [the open construction](/wiki/conjugate-relativity/four-dimensional-born-map); a choice for the 3+1 cone leaves §6's joint-test claim without the cone it uses. No document has attempted either.

Both cones are Lorentzian objects, and #13's preamble inherits the checkpoint's open signature caveat: "The Euclidean/Lorentzian caveat of the main checkpoint is inherited throughout" ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)). Flag 30 in `review/wiki-build-flags.md` records the same point against §1's tag [D — compatibility theorem]: the theorem's g is positive-definite and has no null cone. The flags' audit found the tag on the block form H = diag(g, g⁻¹) rather than on the cones, and rated the flag as a question of tagging convention.

## Where it stands

The item appears only in the worklog. It is not among #11 §14's eleven open problems, not in the current queue in `CLAUDE.md` ('Since the handoff'), and not in the round-3 decisions (`review/round3-adjudication.md`, 'Decisions'). #13 has not been revised since its import on 2026-10-19, so not since the problem was raised, and no review round has covered it ([conjugate special relativity](/wiki/conjugate-relativity)). The conflict is recorded as unresolved on [conflicts between sources](/wiki/history/documents/source-conflicts).

## Sources

- `review/v3-worklog.md` 'New open items' — item O3: the two cones, the dark-sector kinematics, the dark-photon question, the v3 decision and the instruction.
- `papers/conjugate-special-relativity.md` §1, §2 — the 3+1 cone and the dual interval; §4 for the invariant length; §6 for E = c|p| as the dual null cone, the photon-dispersion argument, the open four-dimensional map and the 3+1 presentation; preamble for the inherited Euclidean/Lorentzian caveat.
- `papers/broken-born-checkpoint-v2.md` §13 row 9 — #11's own photon-dispersion requirement; §14 for the open problems, which do not include this item.
- `notes/broken-born-theory.md` §4 — the Fermi-LAT bounds on linear dispersion (superseded as a reference).
- `notes/knot-dark-matter-standalone.md` §1 — #14's ordinary kinematics (withdrawn).
- `CLAUDE.md` 'Since the handoff' — the current queue.
- `review/round3-adjudication.md` 'Decisions' — the round-3 decisions, which do not include it.
- `review/wiki-build-flags.md` item 30 — §1's tag [D — compatibility theorem] on the block form from which #13 reads cones that the theorem's positive-definite g cannot have; a question of tagging convention in the flags' audit; awaits Paul's ruling.
