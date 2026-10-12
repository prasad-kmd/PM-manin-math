"""
Central palette + typography + stroke tokens for PM-Manim Math (@prasadkmd).

Source of truth: /docs (authoritative), specifically
  docs/visual-theme.md      -> background, palette, semantic color rules
  docs/typography.md        -> type hierarchy
  docs/branding.md          -> watermark
  docs/layout-guidelines.md -> safe areas

Scenes must import from here instead of hard-coding hex values or Manim
color constants, so that a palette change is a one-file change.

NOTE ON PRECEDENCE
------------------
`/docs/additional/theme.md` proposes a different palette (BG #0F1115,
PRIMARY #58C4DD, ...) and the earlier render in `scripts/pi4_staircase.py`
used a third set (BG #1C1C1C, #58C4DD / #FFFF00 / #83C167).
The repo README states `/docs/additional/` "may be inconsistent and
incompatible with above docs, so use them as inspiration, references",
and lists "Background: pure black (#000000)" as the design default.
This module therefore implements /docs. To adopt another preset, change
the values in the COLOR section below only.
"""
from __future__ import annotations

import numpy as np
from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Text,
    config,
)

# ------------------------------------------------------------------ COLOR
# Role -> hex, exactly as tabulated in docs/visual-theme.md.
BG = "#000000"          # pure black background (README design default)
TEXT = "#F2F2F2"        # primary text, important labels
TEXT_DIM = "#B8B8B8"    # secondary text, supporting notes
BLUE = "#4EA5FF"        # primary mathematical object / reference object
YELLOW = "#FFD166"      # emphasis, key result, highlighted relationship
TEAL = "#4ECDC4"        # secondary object / transformed representation
CORAL = "#FF6B6B"       # contrast object, error, alternative case
PURPLE = "#B69CFF"      # auxiliary construction, distinct mathematical role
GREEN = "#7BD88F"       # valid result, selected region, positive change
GUIDE = "#666666"       # axes, grids, construction lines, inactive geometry

# Semantic aliases, so a scene can read by *role* rather than by hue.
# Keep assignments stable for the whole video (docs/visual-theme.md).
PRIMARY = BLUE          # the main object of study
SECONDARY = TEAL        # a transformed / alternative representation
EMPHASIS = YELLOW       # the one thing being highlighted right now
CONTRAST = CORAL        # a contrasting or counterexample object
AUX = PURPLE            # auxiliary construction
RESULT = GREEN          # a confirmed result / selected region

# ------------------------------------------------------------------ TYPE
# docs/typography.md defines a *hierarchy*, not fixed sizes, and warns
# against shrinking essential text. Sizes below are in px-per-unit terms
# for the configured frame; they may be scaled per aspect ratio.
FS_TITLE = 56           # main statement / key result
FS_MATH = 48            # equations and diagram labels
FS_SUPPORT = 40         # supporting equations and annotations
FS_LABEL = 32           # secondary labels, axes
FS_MARK = 24            # watermark — deliberately small
FONT = "Inter"          # clean sans-serif; installed in this sandbox (see list_fonts)
FONT_FALLBACK = "sans"  # Pango default, used only if Inter is missing

# ------------------------------------------------------------------ STROKE
# docs/design-system.md: "consistent stroke-weight hierarchy for primary
# objects, secondary guides, and auxiliary construction lines".
SW_PRIMARY = 6
SW_SECONDARY = 4
SW_GUIDE = 2


# ------------------------------------------------------------------ WATERMARK
def brand(fs: int = FS_MARK):
    """The `@prasadkmd` watermark.

    docs/branding.md: small, restrained light gray, near a **lower corner**,
    inside the safe area, never animating, never over geometry.
    Since docs/layout-guidelines.md supports both aspect ratios, placement is
    resolved from the *actual* frame dimensions at call time.
    """
    t = Text("@prasadkmd", font=FONT, font_size=fs, color=TEXT_DIM, fill_opacity=0.55)
    return t.move_to(
        np.array([safe_x() - t.width / 2, -safe_y() + t.height / 2, 0.0])
    )


# ------------------------------------------------------------------ HELPERS
def apply_theme(scene) -> None:
    """Call first in construct(): sets the pure-black background."""
    scene.camera.background_color = BG


def safe_x() -> float:
    """Half-width of the horizontal safe area (last 8% of each side excluded)."""
    return config.frame_width / 2 * 0.92


def safe_y() -> float:
    """Half-height of the vertical safe area (vertical video reserves more top/bottom)."""
    return config.frame_height / 2 * 0.92


def fit_width(mob, max_w: float | None = None):
    """Scale a mobject down to the safe width. Never upscales."""
    limit = safe_x() * 2 if max_w is None else max_w
    if mob.width > limit:
        mob.scale_to_fit_width(limit)
    return mob


def label(text: str, size: int = FS_LABEL, color: str = TEXT, **kw) -> Text:
    """Plain-language label. Mathematical notation uses MathTex/Tex instead."""
    return Text(text, font=FONT, font_size=size, color=color, **kw)


def column(*rows, buff: float = 0.45):
    """Stack rows top-to-bottom, then centre the block on screen."""
    from manim import VGroup

    return VGroup(*rows).arrange(DOWN, buff=buff).move_to(np.array([0.0, 0.0, 0.0]))


def rows(*items, buff: float = 0.25):
    """Left-aligned horizontal row (for equation chains)."""
    from manim import VGroup

    g = VGroup(*items).arrange(RIGHT, buff=buff)
    g.move_to(np.array([0.0, 0.0, 0.0]))
    return g


__all__ = [
    "BG", "TEXT", "TEXT_DIM", "BLUE", "YELLOW", "TEAL", "CORAL", "PURPLE",
    "GREEN", "GUIDE", "PRIMARY", "SECONDARY", "EMPHASIS", "CONTRAST", "AUX",
    "RESULT", "FS_TITLE", "FS_MATH", "FS_SUPPORT", "FS_LABEL", "FS_MARK",
    "FONT", "SW_PRIMARY", "SW_SECONDARY", "SW_GUIDE", "brand", "apply_theme",
    "safe_x", "safe_y", "fit_width", "label", "column", "rows",
    "UP", "DOWN", "LEFT", "RIGHT",
]
