"""
Toolchain smoke test — NOT a deliverable. Confirms that a 9:16 FHD render
works end to end: frame setup, LaTeX MathTex, the shared theme, the watermark,
and the manim.cfg `video_dir` -> ./videos routing.

Run:
  manim -ql --fps 15 scripts/_smoketest.py SmokeTest
  manim -qh --fps 60 scripts/_smoketest.py SmokeTest
"""
from manim import *

from _layout import use_vertical
from _theme import (
    AUX,
    BLUE,
    EMPHASIS,
    FS_MATH,
    FS_TITLE,
    GREEN,
    GUIDE,
    RESULT,
    TEXT_DIM,
    apply_theme,
    brand,
    label,
)

use_vertical()  # must happen before Scene construction


class SmokeTest(Scene):
    def construct(self):
        apply_theme(self)

        # 1. LaTeX path
        eq = MathTex(r"\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}", font_size=FS_MATH)
        eq.set_color_by_tex(r"\pi", EMPHASIS)
        check = label("latex ok", FS_TITLE, RESULT).next_to(eq, DOWN, buff=0.5)

        # 2. Geometry + palette path
        circle = Circle(radius=1.0, color=BLUE, stroke_width=6)
        sq = Square(side_length=1.4, color=AUX, stroke_width=4)
        guides = NumberPlane(
            x_range=(-4, 4), y_range=(-6, 6), background_line_style={"stroke_color": GUIDE, "stroke_width": 2}
        )
        geo = VGroup(circle, sq).arrange(RIGHT, buff=0.8).move_to(DOWN * 2.2).scale(1.1)

        # 3. Text path + watermark
        note = label("toolchain check", 28, TEXT_DIM).next_to(geo, DOWN, buff=0.6)

        self.play(Create(guides), run_time=0.4)
        self.play(Write(eq), run_time=0.8)
        self.play(FadeIn(check, shift=0.2 * UP), run_time=0.4)
        self.play(Create(circle), Create(sq), run_time=0.8)
        self.play(FadeIn(note), run_time=0.3)
        self.add(brand())
        self.wait(0.6)
