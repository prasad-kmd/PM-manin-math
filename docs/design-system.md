# Core Design System

## Purpose

Create mathematically rigorous, visually coherent, easy-to-follow animations. The design should help viewers understand a mathematical idea, not compete with it.

## Visual identity

- Use a pure black background by default.
- Use a consistent, restrained color palette across all topics.
- Prefer clear geometric construction, visual reasoning, and meaningful transformations.
- Use clean sans-serif typography for ordinary text and Manim's mathematical text rendering for equations where appropriate.
- Animate with deliberate timing. Give viewers time to inspect important changes.
- Keep `@prasadkmd` branding small and unobtrusive.

## Design priorities

Apply these priorities in order:

1. Mathematical correctness.
2. Visual clarity and legibility.
3. Explanatory value of each animation.
4. Consistency with this design system.
5. Decorative polish.

If a visual effect makes the mathematics harder to understand, remove the effect.

## Consistency rules

- Keep the meaning of each palette color stable between scenes and videos.
- Keep labels close to the objects they describe without obscuring them.
- Use a consistent stroke-weight hierarchy for primary objects, secondary guides, and auxiliary construction lines.
- Avoid unnecessary boxes, panels, shadows, glows, particles, and decorative motion.
- Do not add a title, subtitle, legend, or explanatory paragraph unless it serves the scene.
- Avoid overcrowding. Split a complicated explanation into multiple scenes instead of shrinking everything.
- Preserve object identity when a mathematical object transforms into another representation. Prefer a clear transformation over unrelated replacement animations.

## Inspiration and originality

The target is concept-driven mathematical storytelling. Use geometric intuition, careful sequencing, and elegant transformations as general principles. Do not reproduce another creator's exact compositions, signature scenes, branding, or distinctive visual assets.

## Format support

Support both vertical 9:16 and horizontal 16:9 videos. The layout may change between formats, but palette semantics, typography hierarchy, animation principles, and watermark treatment should remain consistent.

Do not assume a specific output resolution without checking the repository configuration and the current task. Use the project's configured dimensions or the dimensions explicitly requested by the user.

## Conflict handling

Inspect existing repository instructions and configuration before editing. These files govern visual intent. Existing project requirements, rendering constraints, and explicit task instructions still need to be respected. If two requirements cannot both be satisfied, explain the conflict rather than silently ignoring one.
