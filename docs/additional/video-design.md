# Video Design — pacing, motion, captions, branding

**Agent: follow this for every video.** Setup, render commands and the research/script workflow stay in `manim.md` and `instructions-manim.md`. If anything here conflicts with those files on *look and feel*, this file wins. Colors and fonts come from `theme.md`, positions from `layout.md`.

## 1. Structure (75–90 s target)

| Segment | Time | Purpose |
|---|---|---|
| Hook | 0–6 s | Show the surprising visual or claim immediately. No logo, no "hi". |
| Setup | 6–20 s | Introduce the objects and what is normally true. |
| Build | 20–55 s | Step-by-step construction; one idea per beat. |
| Twist / insight | 55–75 s | The reveal: why it works or where it breaks. |
| Resolution + outro | last 8–10 s | One-sentence takeaway, then handle card `@prasadkmd`. |

- Narration budget: about **150 words per minute**, so roughly **190–225 words** for 75–90 s. Write narration with the `clarity` skill.
- Every beat must have a visual change at least every 3–4 s. A static frame longer than 4 s needs something moving (a highlight, a trace, a counter).

## 2. Motion rules

| Situation | Animation | `run_time` |
|---|---|---|
| New object appears | `FadeIn` / `Create` (curves, shapes) / `Write` (text, equations) | 0.6–1.2 s |
| Object leaves | `FadeOut` | 0.4–0.6 s |
| Transform one state into the next | `Transform` / `ReplacementTransform` | 1.0–1.6 s |
| Highlight | `Indicate` or color change to `ACCENT` | 0.6–0.8 s |
| Camera-style emphasis | `scale` / `move_to` on the main group | 0.8–1.2 s |

- Default easing: `smooth`. Use `linear` only for continuous processes (a tracer moving along a path).
- **One big motion at a time.** Use `LaggedStart` (lag_ratio 0.1–0.2) for groups instead of animating everything at once.
- Hold **0.5–1.0 s** after each reveal before the next animation, so the viewer can read.
- Avoid spinning, bouncing or shaking text. No effects that exist only to look flashy.
- Equations: reveal term by term (`TransformMatchingTex` or substring coloring) rather than all at once.
- When an element is no longer the focus, dim it (opacity 0.3) instead of deleting it, unless the frame is crowded.

## 3. Transitions between segments

- Clear the main canvas with a coordinated `FadeOut` (0.5 s), keep title and watermark if the title is still relevant.
- Title changes use a cross-fade, never a hard cut.
- No full-screen wipes or flashes.

## 4. Captions and narration sync

- Burned-in captions use `FS_CAPTION`, `TEXT` on a `SURFACE` backing panel (opacity 0.9, `PANEL_RADIUS`), centered in the caption zone.
- Max **2 lines**, about 26–30 characters per line. Split at phrase boundaries, not mid-phrase.
- A caption stays on screen at least 1.2 s and never disappears before its audio ends.
- Visuals lead the narration slightly: the object appears **0.2–0.4 s before** the word that names it.
- Still deliver the separate `.srt` alongside the video as per `manim.md`; captions in the `.srt` and the burned-in text must match.
- Audio: voice clear and dry, no music louder than −20 dB under the voice, final mix around −14 LUFS.

## 5. Branding

- Handle: `@prasadkmd`.
- Watermark in the top-left corner (see `layout.md`), 50% opacity, present from 1.0 s to the outro.
- Outro card (last 3 s): centered handle in `PRIMARY` at `FS_TITLE`, with a short call to action in `TEXT_DIM`. Hold at least 2 s so it can be read.
- No intro animation or logo sting before the hook.

## 6. Visual density limits

- At most **3 text items** on screen at once (title, one body/label group, caption).
- At most **1 equation block** (≤ 3 lines) in the main canvas at a time.
- Labels directly on objects beat legends. No legends.
- Every on-screen number or symbol that appears must be said or explained within the same beat.

## 7. Final QA checklist

- [ ] Runtime within 75–90 s (or the length the brief asked for)
- [ ] Colors only from theme tokens; one meaning per color
- [ ] Nothing important outside the safe area (`layout.md` §6 check done)
- [ ] No text smaller than 28; captions ≤ 2 lines
- [ ] Hook visual appears in the first 2 s
- [ ] `.srt` matches the on-screen captions and audio
- [ ] Handle watermark and outro card present
- [ ] Final render uses `-qh --fps 60 -r 1080,1920` and lands in `/videos/`