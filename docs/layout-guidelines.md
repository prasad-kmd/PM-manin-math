# Layout Guidelines

## General composition

Compose each scene around its central mathematical idea. There is no single fixed layout for every topic.

- Identify the main visual object before placing text.
- Establish a clear hierarchy: primary mathematical object, supporting objects, then labels and notes.
- Leave enough negative space around equations, diagrams, and moving objects.
- Keep labels close to their referents, but never let labels obscure important geometry.
- Align related equations and objects where alignment communicates a relationship.
- Avoid placing essential information at the extreme edges.
- Do not compress a complex scene merely to keep it on one screen. Split it into steps when needed.

## Aspect ratios

The project should support both 9:16 vertical and 16:9 horizontal video.

### Vertical 9:16

- Use a predominantly vertical reading path.
- Place the main visualization near the visual center, with equations or explanations above or below when useful.
- Prefer stacked stages over many side-by-side panels.
- Avoid overly wide equations and diagrams. Reorganize them, use a different representation, or split the explanation into scenes.
- Keep the watermark and essential labels inside conservative safe margins.

### Horizontal 16:9

- Use horizontal space for a diagram alongside an equation, derivation, or concise explanation when that improves understanding.
- A left-to-right progression is appropriate when showing a sequence, comparison, or derivation.
- Do not stretch diagrams merely to fill the frame.
- Keep the central mathematical object visually dominant.

## Safe areas and boundaries

- Keep essential text, labels, and diagram endpoints away from frame edges.
- Use the actual scene dimensions and coordinate system rather than assuming a particular resolution.
- Check all important objects at the target aspect ratio.
- Ensure moving objects and labels remain within the frame unless intentional entry or exit is part of the animation.
- Position the watermark consistently inside the frame.

## Adaptive layout

Choose the layout according to the mathematics:

- A single equation may be centered with a small amount of supporting context.
- A graph may need space for axes, labels, and a highlighted interval.
- A geometric proof may need a large construction and only a few labels.
- A derivation may benefit from vertically or horizontally aligned equations.
- A comparison may use two regions only if both remain readable at the target aspect ratio.

Do not force every scene to contain a title, central diagram, and footer. Use only the elements that support the explanation.

## Layout validation

Before rendering the final video, inspect for clipped objects, overlapping labels, unreadable equations, awkward empty space, and elements that leave the frame unexpectedly. Rework the composition rather than relying on viewers to infer missing information.
