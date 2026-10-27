# Round 5 — pre-registration

Written **before** the round-5 audit is dispatched. It was kept outside the
repository, in the session scratchpad, until both referees had returned, so
that neither could read it. It is not committed: this session has no commit
authorization. Its SHA-256, and that of the manuscript copy sent to the
referees, were written into `notes/phase-space-diameter-worklog.md` and into
the session transcript before dispatch.

- **Manuscript:** `papers/phase-space-diameter.md` v1.0 (the
  phase-space-diameter note).
- **Referees:** two fresh subagents with shell, Python (numpy, sympy, mpmath)
  and web. Each gets only a copy of the manuscript and the protocol, and is
  told to read nothing else on the machine.
  - Referee A follows the five-step protocol of rounds 3 and 4.
  - Referee B follows the same protocol, weighted towards §4 and §7–§8 and
    towards prior art.
- **Limitation:** same model family as the author. The program documents the
  note cites ([H1], [H2], [P1]–[P4]) are unavailable to the referees, so the
  premises taken from them can be checked for consistent use only.

## Predictions

- **Verdict: B** (flawed but salvageable) from both referees, confidence
  medium.
  - Not C: every number is gated by a script and matched by an independent
    recomputation; most claims are standard physics tagged [T] with
    retrieved sources; the speculative identifications are tested and
    rejected in the text.
  - Not A: the program-specific content is thin, and a note this long will
    have attribution or wording errors that a referee counts as flaws.
- **Weakest link: the bound on X in §8.2.** It inherits the program's own,
  unreviewed premise that X couples to ordinary matter at gravitational
  strength (equal Planck masses, α = 4/3), which the referee cannot check. A
  referee may also call the bound vacuous for any plausible M_X.
- **Runner-up weakest links**, in order:
  1. The obituary (§6). A referee proposes a reading of "the bounce" or of N
     under which the claim survives, or calls the |Z| = 1 "origin" paragraph
     speculation presented as diagnosis.
  2. "The program fixes no λ" (§5) rests on documents the referee cannot see.
  3. §8.4 (the a⁻⁶ step) and §8.5 (the lever arm) are conditional to the
     point of carrying no content.
- **Arithmetic:** zero surviving numerical indictments. If one survives, a
  convention: κ's definition, the CKN factor, the one-sided against
  two-sided α₉₅ column, g_* at the Planck temperature, or the 2π between
  cells of area ħ and h.
- **Citations:** all literature citations resolve. The likeliest "cited for
  more than it says": Ohsawa or de Gosson for the Fourier transform as
  Z → −1/Z; Slepian 1983; the Egan–Lineweaver numbers; the location of the
  quoted Mignemi sentence; the Lee thesis interpolation.
- **Novelty:** no prior art for the self-dual length beyond what §4 and §7
  already cite; possibly prior art for |Z| = 1 ⟺ Δx = Δp, or for de Sitter
  space as a self-dual state.
