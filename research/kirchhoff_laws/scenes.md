# Kirchhoff's Laws — Scene Plan

## Overview
- **Topic**: Kirchhoff's circuit laws — KCL (current into a node = current out) and KVL (voltages around a loop sum to zero)
- **Hook**: A tangled circuit with six unknown currents — two rules tame all of it
- **Target Audience**: General / undergraduate; assumes current, voltage, resistance are already met
- **Estimated Length**: ~86 s (target 75–90 s), 9:16 FHD (1080×1920), 60 fps
- **Key Insight**: Both laws are conservation laws wearing circuit clothing — KCL is conservation of charge, KVL is conservation of energy. Sign conventions are bookkeeping, not new physics.

## Narrative Arc
We open on a mess: a network of branches whose currents are unknown. Instead of
solving it by escalating algebra, we shrink to one honest circuit, follow the
current into a single node and watch it split without being used up — that is
KCL, and charge conservation is why. Then we walk a loop and find the battery's
rise exactly cancelled by the drops — that is KVL, and energy conservation is
why. The video ends with the mesh from the opening now fully solved, which is
the payoff for the two rules.

---

## Scene 1: hook
**Duration**: ~5.5 s
**Purpose**: Pose the problem at full difficulty before reducing it.

### Visual Elements
- 2×2 mesh: 3 horizontal branches crossed by 3 vertical branches, drawn in muted guide colour
- 6 short arrows on the interior branches, with `i₁ … i₆`
- Battery on the left margin
- Counter readout: `6` unknown currents

### Content
The network draws itself. Six arrows bloom one after another. A line under it
reads "6 unknown currents". A beat of hesitation — then the tangle fades and we
move to a circuit small enough to reason about.

### Narration Notes
Short and confident. Name the promise: two rules solve all of it. Do not explain
anything yet.

### Technical Notes
- `Line`/`VGroup` for branches, `Arrow` for currents, `MathTex(i_1..i_6)`
- Schematic: equal branch lengths, so branch count is legible even though the
  components are not to scale (see Mathematical Content)
- Must not look like a solved circuit — no values on screen

---

## Scene 2: build
**Duration**: ~13 s
**Purpose**: Set up the single circuit used for the whole video.

### Visual Elements
- Battery `12 V` (left edge), series resistor `R₁ = 4 Ω`, node A, node B
- Two parallel branches `R₂ = 12 Ω`, `R₃ = 6 Ω` between A and B
- Node A and node B emphasised; the outer rectangle highlighted as "the loop"

### Content
The circuit is drawn deliberately left-to-right: source, series resistor, then
the splitting point. Node A and node B appear as dots and are named. The outer
path lights up and is labelled "a loop". Both current arrows are drawn entering
node A.

### Narration Notes
Establish the cast and the two places we will visit: a node, and a loop. Say the
values out loud — they are the numbers we will use.

### Technical Notes
- `Arrow` with `tip_length` for branch currents, rounded corners via
  `set_points_as_corners` on a polyline
- Node dots as `Dot`, labels as `MathTex("A")` offset outward so they never sit
  on the wire (docs/mathematical-visualization.md, "Geometry")
- L-shaped resistor symbols are *schematic*; the accompanying numbers carry the
  quantitative meaning

---

## Scene 3: kcl
**Duration**: ~16 s
**Purpose**: State and apply KCL.

### Visual Elements
- Node A enlarged; the two outgoing arrows coloured distinctly from the incoming one
- Equation `ΣI_in = ΣI_out`
- Numeric line `1.5 = 0.5 + 1.0` (shown only after the rule)

### Content
The incoming current is followed into the node. It splits into two, visually
smaller streams. The general rule appears above: current in equals current out
at any node. Then the actual numbers for this circuit resolve. Emphasis lands on
the arrow entering A (`1.5`) and the two leaving it (`0.5`, `1.0`). Node B is
then flashed — the same accounting holds there, with the arrows merely reversed.

### Narration Notes
Lead with the rule, then the numbers. Stress that nothing is lost at a junction.

### Technical Notes
- Animate the split with two `Arrow`s whose stroke width is proportional to
  current (`1.5` vs `0.5`/`1.0`) — a quantitative cue, and stated in narration
- `Indicate` on node B (not a colour change) so the colour ledger stays stable
- Numbers exact: 1.5 = 0.5 + 1.0 (verified in fractions)

---

## Scene 4: kcl_why
**Duration**: ~11 s
**Purpose**: Justify KCL from charge conservation.

### Visual Elements
- The node drawn large, wires entering and leaving
- Incoming charge crosses shown as discrete dots/ticks; outgoing marks counted
- Balance caption that settles when the rates match

### Content
Charges flow in and out. The count arriving and the count leaving are kept
side by side and stay equal. If they did not, charge would pile up at the node
and its potential would drift without limit — which a steady circuit does not
do. Cut to the takeaway: this is conservation of charge.

### Narration Notes
One line, one idea: charge does not pile up at a point. Avoid saying "electrons
are used up" — the whole point is that they are not.

### Technical Notes
- Discrete markers, not a fluid, so "count" is literally what the viewer does
- Keep the marker rate constant and modest (WCAG 2.2: no flashing)
- Reuse the exact node geometry from Scene 3 so continuity is unmistakable

---

## Scene 5: kvl
**Duration**: ~17 s
**Purpose**: State and apply KVL.

### Visual Elements
- A travelling marker walking the loop E → R₁ → A → R₃ → B → E
- Rise/drop tags appearing behind the marker: `+12`, `−6`, `−6`
- Equation `12 − 6 − 6 = 0`
- General rule `ΣV = 0` around any closed loop

### Content
The marker starts at the battery's negative terminal and moves. As it crosses
the source the tag `+12` appears; crossing each resistor the matching drop tag
appears. It returns to the start with the running total at zero, and the tags
collapse into `12 − 6 − 6 = 0`. The rule is then stated in general form. The
other two loops are flashed briefly to show they close too.

### Narration Notes
Walk the loop in the same order the marker walks it, and say "rise" and "drop"
as the tags appear. The numbers must be spoken with the tags on screen.

### Technical Notes
- `MoveAlongPath` with `linear` rate (continuous process — docs/animation-style.md)
- Tags as `MathTex` with sign colour: rises in the positive colour, drops in the contrast colour
- Traversal order fixed and identical to the narration; the marker never jumps
- All three loop sums are exactly zero (verified)

---

## Scene 6: kvl_why
**Duration**: ~11 s
**Purpose**: Justify KVL from energy conservation.

### Visual Elements
- A vertical potential "hill" profile around the loop: up at the source, down across each resistor, returning to the start height
- The marker from Scene 5 continuing around the same profile

### Content
Each voltage is redrawn as a change in height. The source lifts the marker; each
resistor lets it back down. Returning to the starting point means returning to
the starting *height* — every volt gained has been spent. Net zero, necessarily.

### Narration Notes
"Back where you started" is the whole argument. Keep it physical, not algebraic.

### Technical Notes
- This is the one intentional re-representation: the circuit is deliberately
  *not* shown beside it, to avoid implying the hill is a second circuit
  (docs/layout-guidelines.md; one focal point)
- Heights `+12`, `−6`, `−6` are to scale with one another so the picture is
  quantitatively honest

---

## Scene 7: resolve
**Duration**: ~11 s
**Purpose**: Land the conclusion on the original tangled circuit.

### Visual Elements
- The 2×2 mesh from Scene 1 returns
- The six unknowns now filled with the method: node equations and loop equations
- Two rules restated side by side: `ΣI = 0` (charge) and `ΣV = 0` (energy)

### Content
The network from the opening comes back — deliberately, so the video closes the
loop it opened. Where there were six question marks there are now equations. The
two laws are placed beside each other, each labelled with the conservation
principle it expresses. Final hold on that pairing.

### Narration Notes
The takeaway is not "use these formulas" but "these are conservation laws
wearing circuit clothing". State it plainly and stop. Do not add a call to action
beyond the watermark.

### Technical Notes
- Reuse the Scene 1 mobject for the mesh so it is visibly the same object
- Do not re-derive; the algebra is deliberately left off screen
- End on the two laws; the watermark is already present and does not animate

---

## Transitions & Flow

### Scene Connections
- 1 → 2: the tangle fades out; the simple circuit is drawn fresh on the left-to-right reading path
- 2 → 3: camera-free; the existing node A scales up, everything else dims (continuity over replacement)
- 3 → 4: the split arrows are held; charge markers enter along the same paths
- 4 → 5: node dims, the loop highlight from Scene 2 returns
- 5 → 6: the circuit resolves into the potential profile (a deliberate re-representation, announced by the narration)
- 6 → 7: the profile fades; the opening mesh returns

### Recurring Visual Motifs
- One circuit carried through the entire video — same wires, same nodes, same colours
- Node A and node B keep their dot-and-label treatment everywhere
- The travelling marker is the same object colour in both KVL beats
- Circuit paths use rounded-corner polylines throughout, never freehand

---

## Color Palette

Authoritative source: `docs/visual-theme.md`. Colour is assigned by
mathematical role and held for the whole video (`docs/design-system.md`).

| Role | Colour | Hex | Usage |
|------|--------|-----|-------|
| Primary object / reference | Blue | `#4EA5FF` | The circuit itself, battery, branch currents |
| Secondary / transformed | Teal | `#4ECDC4` | Parallel branch `R₃`, the split path after the node |
| Emphasis / key result | Yellow | `#FFD166` | The node, the current being discussed, final `Σ = 0` |
| Contrast / alternative case | Coral | `#FF6B6B` | Voltage drops, the "what if it piled up" case |
| Auxiliary construction | Purple | `#B69CFF` | Guides, loop highlight, the potential profile |
| Valid result | Green | `#7BD88F` | Confirmed balance `1.5 = 0.5 + 1.0` and `= 0` |
| Muted guide | Grey | `#666666` | Unfocused wires, axes-free construction lines |
| Primary / secondary text | `#F2F2F2` / `#B8B8B8` | — | Labels, annotations, watermark |

Background `#000000`. At most four hues on screen in any single beat.

---

## Mathematical Content

### Equations to Render
1. `\Sigma I_{\text{in}} = \Sigma I_{\text{out}}` — Scene 3
2. `1.5 = 0.5 + 1.0` — Scene 3
3. `\Sigma V = 0` — Scene 5
4. `12 - 6 - 6 = 0` — Scene 5
5. `\Sigma I = 0` (charge) and `\Sigma V = 0` (energy) — Scene 7

### Numeric Content
- `E = 12 V`, `R₁ = 4 Ω`, `R₂ = 12 Ω`, `R₃ = 6 Ω`
- `R₂ ∥ R₃ = 4 Ω`, `R_total = 8 Ω`, `I_total = 1.5 A`
- `V_A − V_B = 6 V`, `I(R₂) = 0.5 A`, `I(R₃) = 1.0 A`
- All verified exactly in `Fraction` arithmetic — no rounding on screen

### Geometric Objects
1. **Main circuit** — schematic topology, rounded-corner conductors; persists from Scene 2 to Scene 6
2. **2×2 mesh** — 7 branches, 6 interior current arrows; appears in Scenes 1 and 7 only
3. **Node dots** — `Dot` with an outward-offset label
4. **Current arrows** — stroke width proportional to magnitude
5. **Potential profile** — one polyline, heights proportional to `+12`, `−6`, `−6`

### Scope statement
Drawings are schematic, not to scale. Per `docs/mathematical-visualization.md`,
quantitative meaning is carried by the printed values, not by the drawing.

---

## Implementation Order

1. **theme/layout glue** — `scripts/_theme.py`, `scripts/_layout.py` (done)
2. **Scene 2 (build)** — establishes the circuit every later scene reuses
3. **Scene 5 (kvl)** — most technically demanding: path traversal + synchronised tags
4. **Scene 3 (kcl)** — needs the Scene 2 node geometry
5. **Scene 1 / 7 (mesh)** — a self-contained pair, and 7 depends on 1's mobject
6. **Scene 4 / 6 (the two "why" beats)** — visual derivations on top of 3 and 5
7. **Beat padding + timeline dump** — after narration durations are known

### Shared Components
- `build_circuit()` — the single circuit, used by Scenes 2, 3, 4, 5, 6
- `build_mesh()` — the 2×2 network, used by Scenes 1 and 7
- `node_dot()` / `branch_arrow()` — consistent node and arrow treatment
- `tag(value, kind)` — rise/drop annotation with the sign colour rule

---

## Accuracy Checks
- [x] Branch count in the hook mesh (6 unknowns) matches the drawing
- [x] All KCL/KVL arithmetic exact in `Fraction`
- [x] `ΣV = 0` verified for all three loops of the circuit
- [x] Sign convention stated once and applied consistently
- [x] Lumped-element / low-frequency caveat kept in `research/`, not asserted away
- [x] Arrow widths proportional to current magnitudes
- [x] Potential-profile heights proportional to the printed voltages

## Open Questions / Decisions Needed
- [ ] Voice + narration deliverable confirmed by the user
- [ ] Whether to state the displacement-current caveat on screen (space permitting)
