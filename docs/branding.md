# Branding

## Watermark

Use the text `@prasadkmd` as a small, unobtrusive watermark.

- Place it consistently near a lower corner, inside the safe area.
- Use a restrained light gray rather than a bright accent color.
- Keep it small enough that the mathematics remains the visual focus.
- Maintain enough contrast to be legible against black without drawing attention away from the content.
- Do not place it over equations, graph labels, key points, or important geometry.
- Keep its size and relative placement consistent across scenes and aspect ratios.

## Implementation

- If the repository already provides a watermark helper, reuse it.
- Otherwise, create a reusable helper only after inspecting existing project structure.
- Keep the watermark separate from mathematical objects so it does not accidentally participate in transformations.
- Verify its placement in both vertical and horizontal formats.

## Restraint

The watermark should not animate continuously, flash, glow, or compete with the explanation. Do not add an opening logo, closing card, or additional branding unless explicitly requested.
