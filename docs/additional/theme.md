# Theme — @prasadkmd Manim Shorts

**Agent: read this before writing any scene.** Every color, font and stroke in a script must come from the tokens below (via `scripts/_theme.py`). Never hard-code a hex value or a Manim color constant inside a scene. To restyle the channel, edit this file and `_theme.py` only.

Active preset: **classic-dark** (3Blue1Brown-inspired, near-black background).

## 1. Color tokens

| Token | Hex | Manim origin | Use |
|---|---|---|---|
| `BG` | `#0F1115` | custom | Scene background |
| `SURFACE` | `#1A1D23` | custom | Panels, cards, caption backing |
| `GRID` | `#2A2F38` | custom | Axes, number planes, faint guides |
| `TEXT` | `#ECECEC` | custom | Body text, main equations |
| `TEXT_DIM` | `#9AA3AF` | custom | Secondary notes, units, captions' small print |
| `PRIMARY` | `#58C4DD` | `BLUE_C` | The main object / the "true" thing |
| `ACCENT` | `#F7D96F` | `YELLOW_C` | Highlight, "look here", key numbers |
| `POSITIVE` | `#83C167` | `GREEN_C` | Correct, converging, final result |
| `NEGATIVE` | `#FC6255` | `RED_C` | Error, paradox, the thing that goes wrong |
| `WARM` | `#F0AC5F` | `GOLD_C` | Second data series, secondary construction |

### Color rules
- **One meaning, one color.** A concept keeps the same color for the whole video (e.g. circle = `PRIMARY`, staircase = `NEGATIVE`, limit = `POSITIVE`).
- Max **4 hues** on screen at once. Everything else is `TEXT` / `TEXT_DIM` / `GRID`.
- `ACCENT` is for emphasis only: at most one accented element at a time.
- No pure white (`#FFFFFF`) large fills or full-screen flashes; they glare on phones.
- Text on `BG` must keep contrast ≥ 4.5:1. Never put `TEXT_DIM` on `SURFACE` at sizes below the body size.

## 2. Typography

| Role | Token | Size (`font_size`) | Notes |
|---|---|---|---|
| Hook / title | `FS_TITLE` | 56 | Bold, max 2 lines |
| Body text | `FS_BODY` | 40 | Max 3 lines on screen |
| Labels | `FS_LABEL` | 32 | Axis labels, annotations |
| Captions | `FS_CAPTION` | 34 | Burned-in subtitles, max 2 lines |
| Watermark | `FS_MARK` | 26 | `@prasadkmd` |

- Minimum anywhere on screen: **28**. Smaller is unreadable on a phone.
- Text font token: `FONT` (default `"Sans"` as a safe fallback). To use something nicer (e.g. Inter or Poppins), install it on the render machine, confirm with `python -c "import manimpango; print(manimpango.list_fonts())"`, then change `FONT` once.
- Math is always `MathTex`/`Tex` (LaTeX), never `Text`. Do not mix font styles inside one equation.
- Font size here behaves the same as in the default landscape frame (both are 135 px per unit), but the frame is only 8 units wide, so lines must be shorter. See `layout.md`.

## 3. Strokes and shapes

| Token | Value | Use |
|---|---|---|
| `SW_MAIN` | 6 | Primary curves and shapes |
| `SW_SECOND` | 4 | Secondary shapes |
| `SW_GRID` | 1 | Grid, axes ticks |
| `PANEL_RADIUS` | 0.2 | Rounded panels/cards |
| `PANEL_OPACITY` | 0.9 | `SURFACE` fill opacity |

## 4. Alternate presets (swap by replacing the token values)

| Preset | `BG` | `TEXT` | `PRIMARY` | `ACCENT` | Mood |
|---|---|---|---|---|---|
| classic-dark (active) | `#0F1115` | `#ECECEC` | `#58C4DD` | `#F7D96F` | Clean 3b1b look |
| blackboard | `#1F2A24` | `#F2F0E6` | `#A8D8B9` | `#F6C945` | Chalkboard, classroom |
| midnight-neon | `#0A0B1E` | `#E8E9FF` | `#4DE3FF` | `#FF5EA8` | High-energy, tech |
| paper-light | `#F6F3EC` | `#1E2227` | `#1F6FB2` | `#D9480F` | Print/textbook feel |

These palettes are starting points. Check contrast and view a still frame before committing to one.

## 5. `scripts/_theme.py` (companion code)

```python
from manim import *

# --- color tokens (keep in sync with this file) ---
BG, SURFACE, GRID = "#0F1115", "#1A1D23", "#2A2F38"
TEXT, TEXT_DIM = "#ECECEC", "#9AA3AF"
PRIMARY, ACCENT = "#58C4DD", "#F7D96F"
POSITIVE, NEGATIVE, WARM = "#83C167", "#FC6255", "#F0AC5F"

# --- typography ---
FONT = "Sans"
FS_TITLE, FS_BODY, FS_LABEL, FS_CAPTION, FS_MARK = 56, 40, 32, 34, 26

# --- strokes ---
SW_MAIN, SW_SECOND, SW_GRID = 6, 4, 1


def apply_theme(scene):
    scene.camera.background_color = BG


def label(text, size=FS_BODY, color=TEXT, **kw):
    return Text(text, font=FONT, font_size=size, color=color, **kw)
```

Scenes call `apply_theme(self)` first in `construct()`. This snippet has not been rendered against your environment yet; run a `-ql` preview after wiring it in.