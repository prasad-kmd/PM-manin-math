# Agent Workflow for Manim Generation

## Before writing code

1. Read `design-system.md`.
2. Read the relevant theme, layout, typography, animation, visualization, branding, and scene-structure instructions.
3. Inspect the repository's existing agent instructions, `manim.cfg`, dependencies, helper functions, and scene examples.
4. Identify the topic, intended audience, learning objective, target aspect ratio, output dimensions, and expected runtime.
5. Determine which visual representation best explains the concept.
6. Plan the scene sequence before implementing detailed animations.

## While writing code

- Reuse existing helpers and palette definitions where possible.
- Avoid duplicating constants or introducing conflicting theme definitions.
- Keep mathematical computation and visual styling understandable.
- Use stable semantic color assignments.
- Choose layout based on actual frame dimensions and aspect ratio.
- Prefer purposeful animation over decoration.
- Keep labels attached to the objects they describe when those objects move.
- Follow the installed Manim version and repository conventions. Do not assume a method or parameter exists without checking the project's version or examples.

## Before finalizing

1. Render a preview using the repository's expected command and configuration.
2. Inspect rendered frames or the preview video, not just the Python source.
3. Check mathematical correctness and notation.
4. Check text legibility, clipping, overlaps, safe margins, and watermark placement.
5. Check that the animation timing allows the viewer to follow the reasoning.
6. When both aspect ratios are requested, inspect each format separately.
7. Fix visible issues and render again when practical.
8. Report what was tested and disclose any checks that could not be completed.

## Topic-specific adaptation

Use the repository's topic or idea files when available. Derive the visualization plan from the actual topic, its prerequisites, and the learning objective. Do not claim a topic is present in the repository unless it has been inspected.

## Do not

- Rewrite project configuration without a clear need.
- assume that a composition suitable for 16:9 will fit 9:16.
- change the established palette arbitrarily.
- shrink important text to solve layout problems.
- add decorative animation that distracts from the mathematics.
- claim that a render passed visual inspection if it was not inspected.
