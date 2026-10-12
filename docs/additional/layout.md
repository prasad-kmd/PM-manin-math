# Layout — 9:16 vertical frame

**Agent: place every element using the zones below. Do not position by eye.**

## 1. Canvas

- Render: `-r 1080,1920`, frame **8.0 wide × 14.22 tall** (origin at center).
- Scale: **135 px per unit**. x runs −4.0 → +4.0, y runs −7.11 → +7.11.

## 2. Safe area

Shorts/Reels/TikTok overlay their own UI on the top, bottom and right edge. These margins are conservative defaults; adjust if you target one platform.

- Keep all important content inside **|x| ≤ 3.4** (0.6 side margin).
- Top ~10% (y > 5.7) and bottom ~20% (y < −4.2) are **no-go zones** for anything the viewer must read.

## 3. Zones

```
 y = +7.11  ┌──────────────────────┐
            │  (UI overlay)  mark  │  y 5.7 → 7.11   watermark only
 y = +5.6   ├──────────────────────┤
            │        TITLE         │  y 4.4 → 5.6    center 5.0
 y = +4.0   ├──────────────────────┤
            │                      │
            │     MAIN CANVAS      │  y 4.0 → −2.6   center 0.7
            │   6.8 w × 6.6 h      │
            │                      │
 y = −2.6   ├──────────────────────┤
            │       CAPTIONS       │  y −2.9 → −4.1  center −3.5
 y = −4.2   ├──────────────────────┤
            │   (UI overlay)       │  y < −4.2       nothing important
 y = −7.11  └──────────────────────┘
```

| Zone | Center | Max size (w × h) | Contents |
|---|---|---|---|
| Watermark | (−3.2, 6.4) | small | `@prasadkmd` at 50% opacity, `FS_MARK` |
| Title | (0, 5.0) | 6.8 × 1.2 | Hook line / section title, ≤ 2 lines |
| Main canvas | (0, 0.7) | 6.8 × 6.6 | Graphs, geometry, equations: the visual story |
| Captions | (0, −3.5) | 6.8 × 1.2 | Burned-in subtitles, ≤ 2 lines |

## 4. Composition rules

1. **One focal point.** Only one thing is the star of the main canvas at a time. Fade or dim the rest (to `TEXT_DIM` / opacity 0.3).
2. **Stack, don't spread.** Vertical format favors top-to-bottom layouts. Avoid side-by-side comparisons wider than 6.8 units; use two stacked panels instead.
3. **Equations.** If `MathTex(...).width > 6.8`, call `.scale_to_fit_width(6.8)` or split into multiple lines. Never let an equation touch the safe-area edge.
4. **Line length.** Roughly 26–30 characters per line at caption size. Confirm in a preview still, since glyph widths vary by font.
5. **Spacing.** Minimum 0.3 units between unrelated elements, 0.15 between a label and its object.
6. **Layer order (back → front).** background grid → axes → shapes → highlights → labels → captions → watermark. Set `z_index` explicitly for captions (10) and watermark (11).
7. **Titles and captions never share a frame with a dense equation block.** If the main canvas is full, hide the title.
8. **Alignment.** Titles and captions are centered. Annotations are anchored with `.next_to(obj, direction, buff=0.15)`.

## 5. Layout constants (add to `scripts/_theme.py` or `scripts/_layout.py`)

```python
import numpy as np
from manim import *

FRAME_W, FRAME_H = 8.0, 14.22
SAFE_X = 3.4

TITLE_POS     = np.array([0, 5.0, 0])
MAIN_CENTER   = np.array([0, 0.7, 0])
MAIN_W, MAIN_H = 6.8, 6.6
CAPTION_POS   = np.array([0, -3.5, 0])
WATERMARK_POS = np.array([-3.2, 6.4, 0])


def fit_width(mob, max_w=6.8):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def debug_zones():
    """Draw the zones for a layout check; remove before the final render."""
    def box(w, h, pos, col):
        return Rectangle(width=w, height=h, stroke_color=col, stroke_width=2).move_to(pos)
    return VGroup(
        box(6.8, 1.2, TITLE_POS, ACCENT),
        box(MAIN_W, MAIN_H, MAIN_CENTER, POSITIVE),
        box(6.8, 1.2, CAPTION_POS, NEGATIVE),
    )
```

## 6. Layout check (before every final render)

1. Add `self.add(debug_zones())` temporarily.
2. Render a still of the busiest moment: `manim -ql -s -r 1080,1920 scripts/<file>.py <Scene>` (`-s` saves the last frame as an image).
3. Verify nothing important leaves its zone or the safe area, then remove the debug call.