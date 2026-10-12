# Visual Theme and Color Palette

## Background

- Default background: pure black, `#000000`.
- Avoid gradients or textured backgrounds by default.
- Do not add a grid or coordinate plane unless it helps explain the concept.
- Use a subtle secondary guide line only when it improves spatial understanding.

## Palette

Use the following stable palette as the default. Confirm that the colors remain distinguishable in the final render.

| Role | Hex | Intended use |
|---|---|---|
| Primary text | `#F2F2F2` | Main text and important labels |
| Secondary text | `#B8B8B8` | Supporting notes and less prominent labels |
| Blue | `#4EA5FF` | Primary mathematical object or reference object |
| Yellow | `#FFD166` | Emphasis, key result, or highlighted relationship |
| Teal | `#4ECDC4` | Secondary object or transformed representation |
| Coral | `#FF6B6B` | Contrast object, error, or alternative case |
| Purple | `#B69CFF` | Auxiliary construction or a distinct mathematical role |
| Green | `#7BD88F` | Valid result, selected region, or positive change |
| Muted guide | `#666666` | Axes, grids, construction lines, and inactive geometry |

## Semantic color rules

- Assign colors by mathematical role, not by decoration.
- Once a color identifies an object or quantity, preserve that assignment throughout the explanation unless the meaning explicitly changes.
- For a vector decomposition, for example, keep the original vector, components, and resultant visually distinct and consistent.
- Highlight a key step or result with one accent color. Avoid highlighting every object at once.
- Do not rely on color alone to distinguish objects. Use labels, line styles, position, or shape when needed.
- Check that adjacent colors have enough contrast against black and against one another.

## Color restraint

- Use only the colors needed in a given scene.
- Keep axes, grids, and construction lines quieter than the main mathematical objects.
- Avoid constant color cycling, rainbow gradients, and random colors.
- Do not use glow or bloom effects as the default. Use them sparingly only when they communicate emphasis or direction.

## Implementation

If the repository has a shared palette or theme helper, use it instead of defining duplicate colors in each scene. Inspect the codebase before adding a new helper. Keep the palette centralized where practical.
