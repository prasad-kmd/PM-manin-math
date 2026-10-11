# Research Notes — The π = 4 Staircase Paradox

Target: 75–90 s, 9:16 FHD, @prasadkmd. Audience: general / undergraduate.

## 1. The paradox (setup)
- Circle of diameter 1 (radius 1/2), circumscribed by the unit square (perimeter 4).
- Repeatedly "fold" the square's corners inward with right-angle notches so that
  the boundary converges to the circle. At every stage the perimeter is still 4.
- Conclusion claimed: π = 4. Obviously false (π ≈ 3.14159).

## 2. Simpler sibling (use as the hook / first beat)
- Unit square, diagonal length √2 ≈ 1.414.
- Staircase of horizontal/vertical steps from corner to corner: always length 2.
- Staircases converge (uniformly) to the diagonal, yet lengths stay 2 ≠ √2.
  (Wikipedia: "Staircase paradox")

## 3. Resolution (the key insight)
- Arc length of a smooth curve: L = ∫ √(x'(t)² + y'(t)²) dt  (Euclidean ds).
- Staircase segments are axis-aligned, so along a staircase the length element is
  |dx| + |dy|  (taxicab / L1 length), not √(dx²+dy²).
- At 45°, |dx|+|dy| = √2·ds. For the diagonal, ratio = 2/√2 = √2. ✔ (matches sibling)
- For the circle (diameter 1), average over all directions:
  taxicab length = 4, Euclidean length = π.
  Ratio = 4/π (≈ 1.2732). Verified numerically (python): taxi=4.0000, ratio matches 4/π to 1e-12.
- So the staircase measures the circle with the wrong ruler: 4 = π · (4/π).

- Concept: arc length is NOT continuous under uniform convergence of curves.
  Shapes converge (every staircase point gets close to the circle) but tangents/derivatives
  do not: staircase slope is always 0 or ∞ (in the sense of axis steps), circle slope changes continuously.
  Length needs derivatives to converge, not just the points.
- Limits don't commute: lim(length of staircase_n) = 4 ≠ length(lim staircase_n) = π.
- Ties to the "why calculus works" question: polygon approximation with *inscribed/circumscribed* chords
  or with chords whose directions converge to the tangent DOES converge to arc length.

## 4. Misconceptions to address (from forum/textbook discussion)
- "Smaller steps must approach the true length" — intuitive, false here.
- "Integration is a limit of small pieces, so it must work" — integration gives AREA here,
  and the area does converge (staircase area → π/4 for the quarter-circle-type area argument).
- "The staircase is a bad circle" — no, it converges to the circle pointwise AND uniformly.
  The failure is about direction, not position.

## 5. Recommended narrative (Pattern 1 Mystery → Investigation → Resolution, + Wrong → Less wrong → Right)
1. Hook (~10 s): "Can we get π = 4?" Show the square-around-circle, the staircase shrinking.
2. Setup (~15 s): perimeter stays 4 at every stage; the shape converges to the circle.
3. Investigate (~25 s): zoom into one step; show the step is horizontal + vertical;
   contrast with the true tangent direction (45° → √2 factor).
4. Resolution (~20 s): taxicab vs Euclidean ruler; ratio 4/π; π·(4/π) = 4.
5. Recap / takeaway (~10 s): "Shapes can converge while lengths don't. Limits don't commute with length."

## 6. Key numbers for on-screen
- Staircase perimeter: 4 (for diameter 1) at every n.
- π ≈ 3.14159; 4 − π ≈ 0.858 (the "error" never shrinks).
- Diagonal of unit square: √2 ≈ 1.4142; staircase: 2.
- Taxicab/Euclidean ratio for the circle: 4/π ≈ 1.2732.

## 7. Sources
- Wikipedia, "Staircase paradox" (definition, unit-square example, arc length not continuous, Gardner/Moscovich refs):
  https://en.wikipedia.org/wiki/Staircase_paradox
- Stack Exchange, "The staircase paradox, or why π≠4" (accepted discussion: uniform convergence vs arc length;
  "the perimeter stays 4 at every stage"; 4 ≈ π bound; limsup argument):
  https://math.stackexchange.com/questions/12906/the-staircase-paradox-or-why-pi-ne4
- Sarath Tharayil, "The Staircase That Looks Straight" (2026; derivatives don't converge; π=4 cousin via folding):
  https://www.saraththarayil.com/writeups/staircase-paradox
- Farrell, M. A. (1975), "An intuitive leap or an unscholarly lapse?", The Mathematics Teacher 68(2): 149–152. doi:10.5951/mt.68.2.0149
- Thompson & Gardner, Calculus Made Easy (1998), Appendix pp. 305–306 (classic "staircase" recreational problem).
- Moscovich, Loopy Logic Problems (2006), p. 23.
- Sinitsky & Ilany (2016), Change and Invariance, pp. 375–376 (arc length / limits).

## 8. Open questions for the user
- Include the square-diagonal sibling as a hook, or only the circle?
- Exact on-screen formula level (show integral, or only the ratio 4/π)?
- Narration language/voice (for voiceover) — to be chosen later.
