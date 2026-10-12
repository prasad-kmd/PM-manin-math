"""
Frame + zone setup for both supported aspect ratios.

docs/design-system.md: "Support both vertical 9:16 and horizontal 16:9 videos."
docs/layout-guidelines.md: "Use the actual scene dimensions and coordinate
system rather than assuming a particular resolution."

Import and call `use_vertical()` or `use_horizontal()` BEFORE `Scene`
construction (module import time), because Manim reads the frame size when the
scene is instantiated.

Manim's default is 16:9 at 14.2222 x 8.0 units (135 px/unit at 1080p).
The vertical preset keeps the same 135 px/unit scale by narrowing the width,
so font sizes behave identically in both formats (see docs/typography.md).
"""
from __future__ import annotations

from manim import config

PX_PER_UNIT = 135.0


def use_vertical(pixel_width: int = 1080, pixel_height: int = 1920) -> None:
    """9:16 FHD — the channel's primary Shorts/Reels format."""
    config.pixel_width = pixel_width
    config.pixel_height = pixel_height
    config.frame_height = pixel_height / PX_PER_UNIT   # 14.2222
    config.frame_width = pixel_width / PX_PER_UNIT     # 8.0


def use_horizontal(pixel_width: int = 1920, pixel_height: int = 1080) -> None:
    """16:9 FHD — long-form companion format."""
    config.pixel_width = pixel_width
    config.pixel_height = pixel_height
    config.frame_height = pixel_height / PX_PER_UNIT   # 8.0
    config.frame_width = pixel_width / PX_PER_UNIT     # 14.2222


def zones():
    """Return the safe-area boxes for the current frame as (name, width, height, centre).

    Ordered with the primary reading path of `docs/layout-guidelines.md`:
    a vertical video reads top-to-bottom, a horizontal one left-to-right.
    Reserving margins keeps essential content away from platform UI overlays
    and from the frame edges.
    """
    import numpy as np

    W, H = config.frame_width, config.frame_height
    if H > W:  # vertical: title / main / captions stacked
        margin_x, margin_y = W * 0.08, H * 0.08
        usable_h = H - 2 * margin_y
        title_h, cap_h = usable_h * 0.12, usable_h * 0.10
        main_h = usable_h - title_h - cap_h
        y_title = H / 2 - margin_y - title_h / 2
        y_cap = -H / 2 + margin_y + cap_h / 2
        y_main = (y_title - title_h / 2 + y_cap + cap_h / 2) / 2
        return [
            ("title", W - 2 * margin_x, title_h, np.array([0.0, y_title, 0.0])),
            ("main", W - 2 * margin_x, main_h, np.array([0.0, y_main, 0.0])),
            ("caption", W - 2 * margin_x, cap_h, np.array([0.0, y_cap, 0.0])),
        ]
    # horizontal: one main band, generous side margins
    margin_x, margin_y = W * 0.06, H * 0.10
    return [
        ("main", W - 2 * margin_x, H - 2 * margin_y, np.array([0.0, 0.0, 0.0])),
    ]


def debug_zones():
    """Overlay the safe areas, for a layout check render. Remove before final.

    docs/layout-guidelines.md, "Layout validation": inspect rather than assume.
    """
    from manim import Rectangle, VGroup

    from _theme import AUX, GREEN, YELLOW

    colors = {"title": YELLOW, "main": GREEN, "caption": AUX}
    return VGroup(
        *[
            Rectangle(width=w, height=h, stroke_color=colors.get(name, GREEN), stroke_width=2)
            .move_to(centre)
            for name, w, h, centre in zones()
        ]
    )


def main_center():
    """Centre of the primary canvas zone — the anchor for the main visual."""
    for name, _w, _h, centre in zones():
        if name == "main":
            return centre
    return None
