# Typography and Mathematical Notation

## General text

- Use a clean, legible sans-serif font for titles, labels, and explanatory text.
- Prefer a small, consistent set of font styles and weights.
- Use sentence case for ordinary headings unless the project has an established convention.
- Keep explanatory text concise. A video should not become a slide filled with paragraphs.
- Establish hierarchy through size, weight, and placement rather than through many unrelated styles.

## Mathematical notation

- Use Manim's mathematical text tools, such as `MathTex`, for equations and symbolic expressions when appropriate.
- Use `Tex` for text that requires LaTeX formatting, and use ordinary text objects for plain labels.
- Preserve standard mathematical notation. Do not replace conventional symbols with decorative alternatives.
- Check subscripts, superscripts, fractions, radicals, integrals, vector notation, and delimiters in the rendered output.
- Avoid placing long explanatory prose inside mathematical expressions.
- Ensure that equations are large enough to read at the final video size.

## Hierarchy

Use a practical hierarchy rather than fixed sizes that may fail across aspect ratios:

1. Main statement or key result.
2. Main equation or diagram labels.
3. Supporting equations and annotations.
4. Secondary labels, axes, and quiet notes.

Actual font sizes should be chosen based on the frame dimensions, text length, and viewing format. Never shrink essential text until it is technically on-screen but difficult to read.

## Labels and equations

- Keep labels brief.
- Prefer direct labels when their meaning is obvious, and use a legend only when direct labeling would clutter the scene.
- Avoid label collisions with curves, arrows, points, and equations.
- Use consistent notation throughout a video.
- If notation changes, explicitly show or explain the change.

## Rendering checks

Inspect actual rendered frames. Source code alone cannot establish whether text is legible or whether a formula has been clipped. Check long equations in both vertical and horizontal formats when both are requested.
