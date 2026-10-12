# Animation Style and Motion

## Core principle

Every animation should explain a mathematical relationship, reveal a change, guide attention, or help the viewer follow the reasoning. Motion without a clear purpose should be removed.

## Pacing

- Prefer smooth, deliberate motion over rapid cuts or constant movement.
- Give important equations and diagrams enough time to appear and be understood.
- Use pauses after major transformations or results.
- Keep the pace appropriate to the complexity of the concept.
- Avoid animating every object simultaneously. Sequence changes when this improves comprehension.

## Preferred animation techniques

Use Manim animations that preserve mathematical continuity where practical:

- `Create` or `DrawBorderThenFill` for constructing an object.
- `Write` for equations and text.
- `Transform` or `ReplacementTransform` when one representation meaningfully becomes another.
- `Indicate` or a restrained color change to emphasize a relevant part.
- `MoveAlongPath` when movement along a curve or path is mathematically meaningful.
- `FadeIn` and `FadeOut` for simple, unobtrusive entrances and exits.

These are examples, not mandatory choices. Select the animation that best communicates the idea and is supported by the installed Manim version.

## Easing and timing

- Use smooth easing for ordinary transitions where appropriate.
- Avoid abrupt movement unless discontinuity is part of the mathematics.
- Keep related objects synchronized when they represent one mathematical process.
- Use short transitions for minor changes and longer transitions for conceptual transformations.
- Do not add arbitrary motion simply to make a scene appear more active.

## Continuity

- Preserve object identity and spatial relationships where possible.
- Make transformations traceable. Viewers should be able to see what changed and what remained invariant.
- If an object changes meaning, label or explain the change.
- Avoid unnecessary camera movement, zooming, spinning, and parallax.
- Use camera movement only when it helps reveal structure or follow an object.

## Visual emphasis

- Direct attention to one main event at a time.
- Use color, stroke weight, position, or a brief indication to emphasize the relevant object.
- Avoid repeated flashing, continuous pulsing, excessive particle effects, and default glow effects.
- Ensure the final state of a transformation is clear and stable.

## Technical discipline

- Use animation timing deliberately and keep total runtime in mind.
- Avoid overlapping animations that cause objects to collide or labels to detach from their targets.
- Confirm that all animated objects end in the intended final state.
- Test the actual render, especially for transformations involving equations, graphs, and moving labels.
