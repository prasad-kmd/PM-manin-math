# Research Notes — Kirchhoff's Circuit Laws

Target: 75–90 s, 9:16 FHD, @prasadkmd. Audience: general / undergraduate.
Style: classic 3Blue1Brown — black background, one idea per beat, the algebra
earns its place after the physical picture.

## 1. The two laws

| Law | Statement | Founded on |
|---|---|---|
| **KCL** — Kirchhoff's current law (junction rule) | The algebraic sum of currents at any node is zero; total current in equals total current out. `ΣI = 0` | Conservation of **charge** |
| **KVL** — Kirchhoff's voltage law (loop rule) | The algebraic sum of potential differences around any closed loop is zero. `ΣV = 0` | Conservation of **energy** |

Published 1845 by Gustav Kirchhoff, aged 21, generalising Ohm's work and
preceding Maxwell. They are the basis of all network analysis (nodal and mesh
analysis are just these two laws systematised).

## 2. Why they are true

- **KCL** follows from conservation of charge. In steady state no charge can
  accumulate at a junction, so the net rate of charge flow in must be zero.
  Formally: continuity equation `∇·J + ∂ρ/∂t = 0`; with `∂ρ/∂t = 0` this becomes
  `∇·J = 0`, and integrating `∮J·da = 0` over a surface enclosing the node gives
  `ΣI_k = 0`.
- **KVL** follows from conservation of energy. Voltage is potential energy per
  unit charge; returning to the starting point must be a net-zero change in
  potential. Formally: Faraday's law `∇×E = −∂B/∂t`; in the static/low-frequency
  limit `∇×E = 0`, so `E = −∇φ` and `∮E·dl = 0`, giving `ΣV_k = 0`.

## 3. Scope and honesty about the idealisation

Both laws are statements about the **lumped-element model**. They are exact for
DC, and for AC while the circuit is small compared to the wavelength. KVL
genuinely fails when a changing magnetic field threads the loop (that is exactly
what an inductor or a transformer exploits), and the classical `∇·J = 0` form of
KCL is a low-frequency approximation that neglects displacement current
`ε₀ ∂E/∂t`. Worth one clause if the narration has room; not worth a scene at
85 seconds. Do **not** imply the laws are universally exact without the
qualifier.

## 4. Sign conventions (the thing students actually get wrong)

- **KCL:** choose a direction. Currents *into* the node positive, *out* negative
  (or the reverse — the equation is the same).
- **KVL:** pick a traversal direction around the loop and stick to it.
  Crossing a source from − to + is a rise `+E`; from + to − is `−E`.
  Crossing a resistor *with* the current is a drop `−IR`; *against* it `+IR`.
- Consistency matters more than the particular choice.

## 5. Worked circuit for this video (numbers verified exactly, fractions)

Battery `E = 12 V`; series resistor `R₁ = 4 Ω`; then two parallel branches
`R₂ = 12 Ω` and `R₃ = 6 Ω` between node A and node B.

| Quantity | Value |
|---|---|
| `R₂ ∥ R₃` | `(12·6)/(12+6)` = **4 Ω** |
| `R_total` | `4 + 4` = **8 Ω** |
| `I_total` | `12/8` = **1.5 A** |
| `V_A − V_B` | `1.5 × 4` = **6 V** |
| `I` through `R₂` | `6/12` = **0.5 A** |
| `I` through `R₃` | `6/6` = **1.0 A** |

Checks (all exactly zero):
- **KCL at node A:** `1.5 − (0.5 + 1.0) = 0`
- **KVL loop (E, R₁, R₂):** `12 − 1.5(4) − 0.5(12) = 12 − 6 − 6 = 0`
- **KVL loop (E, R₁, R₃):** `12 − 1.5(4) − 1.0(6) = 12 − 6 − 6 = 0`
- **KVL outer loop (R₂, R₃):** `0.5(12) − 1.0(6) = 0`

Three clean numbers — 1.5 A, 0.5 A, 1.0 A — and a 6 V node. No rounding anywhere,
so nothing on screen is approximate except the idealisation itself.

Hook circuit: a 2×2 mesh → 7 branches. One is the battery, leaving **six unknown
branch currents**. That count is stated on screen and must match the drawing.

## 6. Misconceptions to pre-empt

- "Current is used up as it flows." No — current is not consumed; energy is.
  KCL is precisely the statement that current is not used up.
- "Voltage is a property of one point." Voltage is a *difference*; KVL only
  makes sense as a difference around a closed path.
- "The two laws are separate physics." They are one conservation statement each:
  charge, and energy. Sign conventions are bookkeeping, not physics.

## 7. Narrative (Pattern 1 Mystery → Investigation → Resolution
   + Pattern 3 Two Perspectives → Unity)

1. **Hook** — a tangled circuit with six unknown currents; two rules tame it.
2. **Build** — the concrete circuit, nodes and loops named.
3. **KCL** — follow the current into node A and watch it split.
4. **Why** — charge cannot pile up at a point.
5. **KVL** — walk the loop, add the rises and drops.
6. **Why** — you return to the same potential; energy in equals energy out.
7. **Resolution** — two conservation laws; everything else is algebra.

Recurring motif: the **same circuit** in every beat. Objects are transformed and
re-focused, never replaced, so the viewer keeps their bearings.

## 8. Sources

- Wikipedia, "Kirchhoff's circuit laws" — statements, 1845 attribution, KVL
  derivation from the Maxwell–Faraday equation in the lumped model, and the
  low-frequency validity condition:
  https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws
- Purdue ECE 604 Lecture 24 (Chew), "Circuit Theory Revisited" — KCL from the
  continuity equation `∇·J = −jωρ`, KVL from Faraday's law:
  https://engineering.purdue.edu/wcchew/ece604s19/Lecture%20Notes/Lect24.pdf
- Wikipedia / standard texts on the lumped-element model and displacement
  current limits of the classical laws.
- Physics Fundamentals, "What Are Kirchhoff's Laws? KCL, KVL and Worked
  Examples" — sign conventions and exam-level statement:
  https://physicsfundamentals.org/blog/electric-circuits-kirchhoffs-laws

## 9. Open questions for the user

- Show the full 1.5 / 0.5 / 1.0 solutions, or stop at the symbolic `ΣI = 0`,
  `ΣV = 0`? (Plan: show the numbers — they are the payoff.)
- Mention the displacement-current caveat? (Plan: one clause in the outro if the
  narration has room; otherwise omit rather than imply universality.)
