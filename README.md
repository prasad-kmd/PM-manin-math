# PM-Manim Math Video Design System — @prasadkmd

Manim Community v0.22.0 on Python 3.13 (Debian trixie). Setup per `instructions-manim.md` which give common instructions to setup the environment, but use it for setting up the workspace only.

## Layout
- `scripts/` — finalized scene scripts (`_template_shorts.py` is the starter)
- `videos/` — rendered output (`videos/<script>/<quality>/<Scene>.mp4`)
- `media/` — Manim cache and logs (not deliverables)
- `research/` - summary of researched content in `.md` format
- `manim.cfg` — config (`video_dir` points to `./videos`)

---

These Markdown files define the visual design rules for mathematical animations generated with Manim in the PM-Manim Math repository.

## Files ( `/docs` ) 

- `design-system.md`: core visual identity and precedence rules.
- `visual-theme.md`: background, palette, and color semantics.
- `layout-guidelines.md`: adaptive composition for vertical and horizontal videos.
- `typography.md`: text, equations, labels, and readability.
- `animation-style.md`: pacing, transitions, and motion principles.
- `mathematical-visualization.md`: rules for graphs, geometry, vectors, equations, and other mathematical objects.
- `branding.md`: subtle `@prasadkmd` watermark rules.
- `scene-structure.md`: recommended narrative flow and scene transitions.
- `design-examples.md`: practical examples of applying the system.
- `agent-workflow.md`: instructions for applying the rules while writing and validating Manim code.
- additionally there are another docs available at `/docs/additional/`, but these document may be inconsistent and incompatible with above docs, so use them as inspiration, references.

## How the agent should use these files

1. Read `design-system.md` first.
2. Read the other files relevant to the current task.
3. Inspect the repository's existing configuration, helper modules, and instructions before changing code.
4. Treat these documents as visual and implementation guidance, not as a reason to overwrite existing project requirements.
5. If an existing repository instruction conflicts with these files, identify the conflict and preserve explicit project constraints. Do not silently change rendering settings.
6. Adapt scene composition to the topic and aspect ratio while keeping the visual identity consistent.

## Current design defaults

- Background: pure black (`#000000`).
- Visual direction: original mathematical storytelling inspired by the clarity and conceptual visualization associated with 3Blue1Brown, without copying its exact visual identity.
- Color: one consistent palette with stable semantic assignments.
- Typography: clean sans-serif text with readable mathematical notation.
- Motion: smooth, deliberate, explanatory.
- Branding: small `@prasadkmd` watermark.
- Formats: support both 9:16 vertical and 16:9 horizontal layouts.

These are defaults. Topic-specific instructions may adapt the composition, but should not casually change the core identity.

## Ideas for videos

 - please check the `/ideas` for curated list of topics for videos.

## Health check
`manim checkhealth` → 4 PASSED (manim, executable, latex, dvisvgm).

--- 
GH: [@prasad-kmd](https://github.com/prasad-kmd)
YT: [@prasadkmd](https://youtube.com/@prasadkmd)