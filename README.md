# Manim Workspace — @prasadkmd

Manim Community v0.22.0 on Python 3.13 (Debian trixie). Setup per `uploads/instructions-manim.md`.

## Layout
- `scripts/` — finalized scene scripts (`_template_shorts.py` is the starter)
- `videos/` — rendered output (`videos/<script>/<quality>/<Scene>.mp4`)
- `media/` — Manim cache and logs (not deliverables)
- `manim.cfg` — config (`video_dir` points to `./videos`)

## Standard
- Format: FHD 9:16 → `-r 1080,1920`, frame 8.0 × 14.22
- Final render: `manim -qh --fps 60 -r 1080,1920 scripts/<file>.py <Scene>`
- Preview: `manim -ql -r 1080,1920 scripts/<file>.py <Scene>`
- Branding: handle `@prasadkmd`

## Health check
`manim checkhealth` → 4 PASSED (manim, executable, latex, dvisvgm).
