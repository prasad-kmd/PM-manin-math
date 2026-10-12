# Design Examples

These examples describe intended visual behavior. They are not complete Manim programs.

## Example 1: Derivative as a limit

**Composition**
- Keep a coordinate plane and curve as the main visual.
- Use one accent color for the selected point and another for the secant line.
- Show the second point moving toward the first.
- Transition the secant toward the tangent while keeping the relevant points and slope relationship clear.
- Present the limit expression only when the visual has established what is approaching what.

**Avoid**
- Rapidly moving the point so the limiting behavior is hard to inspect.
- Overloading the graph with unnecessary ticks and labels.
- Suggesting that a finite sequence of frames proves the limit.

## Example 2: Vector decomposition

**Composition**
- Use a consistent color for the original vector.
- Use separate, stable colors for component vectors and the resultant.
- Draw component projections as quieter guide lines.
- Animate the components in an order that makes their relationship clear.
- Keep axes secondary to the vectors.

**Avoid**
- Changing vector colors halfway through the explanation.
- Using arrowheads or labels that overlap.
- Changing the scale without indicating it.

## Example 3: Geometric proof

**Composition**
- Construct the main figure first.
- Add auxiliary lines only when they become relevant.
- Highlight the current angle, segment, or relationship.
- Keep vertex labels near their points and away from line intersections.
- Use muted construction lines and a brighter color for the relationship being established.

**Avoid**
- Showing every auxiliary construction at the start.
- Presenting a schematic figure as exactly to scale when it is not.
- Letting labels obscure the geometry.

## Example 4: Vertical and horizontal adaptation

**Vertical**
- Stack a graph and its equation when both need substantial space.
- Use a clear top-to-bottom progression.
- Split a wide derivation across successive scenes when needed.

**Horizontal**
- Place a graph beside an equation when their relationship is the main point.
- Use left-to-right space for comparisons or transformations.
- Keep the same palette semantics as the vertical version.

## Example 5: Key result

- Let the result emerge from the derivation.
- Use one accent color to emphasize the final expression.
- Reduce the visual prominence of supporting objects.
- Hold the final state briefly.
- Do not add extra motion after the key insight has been established.
