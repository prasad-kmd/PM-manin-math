"""
Taylor Series: Approximating Smooth Curves with Polynomials — 9:16 FHD explainer (@prasadkmd)

Style: Classic 3Blue1Brown visual storytelling aligned with repository /docs design system.
Plan:  research/taylor_series/scenes.md
Facts: research/taylor-series-research.md

Final render:
  manim -qh --fps 60 -r 1080,1920 scripts/taylor_series.py TaylorSeries

Beat durations are read from research/taylor_series/beats.json (narration-driven).
Actual beat timings are written to research/taylor_series/timeline.json.
"""
import json
import math
import os

import numpy as np
from manim import *

# ---------------------------------------------------------------- format (9:16 FHD)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#000000"

# ---------------------------------------------------------------- palette (/docs/visual-theme.md)
BG = "#000000"
TEXT_PRIMARY = "#F2F2F2"
TEXT_SECONDARY = "#B8B8B8"
BLUE_ = "#4EA5FF"      # Target smooth function f(x) = cos(x)
YELLOW_ = "#FFD166"    # Taylor polynomial approximation P_n(x) & key emphasis
TEAL_ = "#4ECDC4"      # 1st derivative / slope matching
CORAL_ = "#FF6B6B"     # Error / divergence barrier
PURPLE_ = "#B69CFF"    # Anchor point x = 0 / (x - a)
GREEN_ = "#7BD88F"     # 2nd derivative / factorial cancellation / convergence interval
GUIDE_ = "#666666"     # Axes, construction lines, quiet guides
HANDLE = "@prasadkmd"

# ---------------------------------------------------------------- layout anchors
TITLE_Y = 5.35
GRAPH_CENTER = np.array([0.0, 1.75, 0.0])
EQ_TOP_Y = -1.55
EQ_MID_Y = -2.75
EQ_BOT_Y = -3.95
WATERMARK_POS = np.array([0.0, -6.35, 0.0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BEATS_FILE = os.path.join(ROOT, "research", "taylor_series", "beats.json")
TIMELINE_FILE = os.path.join(ROOT, "research", "taylor_series", "timeline.json")

DEFAULT_BEATS = [
    ("hook", 7.751),
    ("setup", 9.276),
    ("slope", 8.23),
    ("curvature", 12.492),
    ("factorial", 13.17),
    ("hug", 12.273),
    ("formula", 8.496),
    ("caveat", 9.6),
    ("lesson", 7.969),
]


def load_beats():
    if os.path.exists(BEATS_FILE):
        with open(BEATS_FILE) as f:
            data = json.load(f)
        return [(b["name"], float(b["dur"])) for b in data]
    return DEFAULT_BEATS


def pt(x, y):
    return np.array([x, y, 0.0])


def fit_width(mob, max_w=6.8):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def taylor_cos(x, deg):
    """Evaluate Maclaurin polynomial of degree `deg` for cos(x)."""
    total = 0.0
    for k in range(0, deg // 2 + 1):
        sign = -1.0 if (k % 2 == 1) else 1.0
        total += sign * (x ** (2 * k)) / math.factorial(2 * k)
    return total


# Precomputed x-limits so |P_n(x)| <= 2.15 stays strictly inside the axes box
COS_XLIM = {
    0: 6.0,
    2: 2.50,
    4: 3.22,
    6: 3.98,
    8: 4.72,
    10: 5.45,
    12: 6.0,
}


def build_cos_axes():
    axes = Axes(
        x_range=[-6.3, 6.3, math.pi],
        y_range=[-2.2, 2.2, 1.0],
        x_length=6.8,
        y_length=4.4,
        axis_config={
            "color": GUIDE_,
            "stroke_width": 2.5,
            "include_tip": False,
        },
    ).move_to(GRAPH_CENTER)
    x_lbl = MathTex("x", font_size=32, color=TEXT_SECONDARY).next_to(axes.x_axis.get_end(), DOWN, buff=0.18)
    y_lbl = MathTex("y", font_size=32, color=TEXT_SECONDARY).next_to(axes.y_axis.get_end(), LEFT, buff=0.18)
    # Add subtle tick labels for -pi, pi, 1, -1
    ticks = VGroup(
        MathTex(r"-\pi", font_size=26, color=TEXT_SECONDARY).next_to(axes.c2p(-math.pi, 0), DOWN, buff=0.15),
        MathTex(r"\pi", font_size=26, color=TEXT_SECONDARY).next_to(axes.c2p(math.pi, 0), DOWN, buff=0.15),
        MathTex(r"1", font_size=26, color=TEXT_SECONDARY).next_to(axes.c2p(0, 1), LEFT, buff=0.15).shift(UP * 0.18),
        MathTex(r"-1", font_size=26, color=TEXT_SECONDARY).next_to(axes.c2p(0, -1), LEFT, buff=0.15),
    )
    return axes, VGroup(x_lbl, y_lbl, ticks)


class TaylorSeries(Scene):
    def construct(self):
        self.t = 0.0
        self.timeline = []
        self._beat = None
        self.beats = {name: dur for name, dur in load_beats()}

        # Persistent subtle watermark (/docs/branding.md)
        self.brand = Text(HANDLE, font="Sans", font_size=26, color=TEXT_SECONDARY)
        self.brand.set_opacity(0.65).move_to(WATERMARK_POS)
        self.add(self.brand)

        # ============================================================ 1. hook
        self.next_beat("hook")
        hook_q = MathTex(r"\cos(x) = \, ?", font_size=76, color=BLUE_).move_to(pt(0, 2.7))
        ops_note = Text("Calculator only knows:   +   −   ×", font="Sans", font_size=32, color=TEXT_SECONDARY)
        fit_width(ops_note, 6.6).move_to(pt(0, 1.35))

        poly_hook = MathTex(
            r"\cos(x)", r"\approx", r"c_0 + c_1 x + c_2 x^2 + c_3 x^3 + \cdots",
            font_size=46, color=TEXT_PRIMARY
        )
        poly_hook[0].set_color(BLUE_)
        poly_hook[2].set_color(YELLOW_)
        fit_width(poly_hook, 6.8).move_to(pt(0, -0.4))

        self.play_t(FadeIn(hook_q, scale=0.85), run_time=0.9)
        self.play_t(FadeIn(ops_note, shift=UP * 0.15), run_time=0.9)
        self.wait_t(0.7)
        self.play_t(Write(poly_hook), run_time=1.6)
        self.play_t(Indicate(poly_hook[2], color=YELLOW_, scale_factor=1.06), run_time=0.9)

        header = Text("Taylor Series", font="Sans", font_size=42, color=TEXT_PRIMARY).move_to(pt(0, TITLE_Y))
        self.play_t(
            FadeOut(hook_q, ops_note, poly_hook),
            FadeIn(header),
            run_time=0.9,
        )
        self.header = header

        # ============================================================ 2. setup
        self.next_beat("setup")
        axes, axes_labels = build_cos_axes()
        cos_curve = axes.plot(lambda x: math.cos(x), x_range=[-6.0, 6.0], color=BLUE_, stroke_width=5)
        cos_tag = MathTex(r"f(x) = \cos(x)", font_size=36, color=BLUE_).move_to(pt(1.95, 3.85))

        anchor_dot = Dot(axes.c2p(0, 1), radius=0.10, color=PURPLE_)
        anchor_lbl = MathTex(r"f(0) = 1", font_size=36, color=PURPLE_).next_to(anchor_dot, UP + RIGHT, buff=0.16)

        p0_curve = axes.plot(lambda x: 1.0, x_range=[-6.0, 6.0], color=YELLOW_, stroke_width=5)
        eq_p0 = MathTex(r"P_0(x) = 1", font_size=50, color=YELLOW_).move_to(pt(0, EQ_TOP_Y))
        note_p0 = Text("Matches height at x = 0", font="Sans", font_size=30, color=TEXT_SECONDARY).move_to(
            pt(0, EQ_MID_Y)
        )

        self.play_t(Create(axes), FadeIn(axes_labels), run_time=1.2)
        self.play_t(Create(cos_curve), FadeIn(cos_tag), run_time=1.4)
        self.play_t(FadeIn(anchor_dot, scale=1.4), Write(anchor_lbl), run_time=1.1)
        self.play_t(Create(p0_curve), Write(eq_p0), FadeIn(note_p0), run_time=1.6)
        self.play_t(Indicate(anchor_dot, color=PURPLE_, scale_factor=1.3), run_time=0.8)

        # ============================================================ 3. slope
        self.next_beat("slope")
        slope_arrow = DoubleArrow(
            axes.c2p(-1.4, 1.0), axes.c2p(1.4, 1.0),
            color=TEAL_, stroke_width=6, buff=0, max_tip_length_to_length_ratio=0.12
        )
        deriv1_eq = MathTex(r"f'(0) = -\sin(0) = 0", font_size=42, color=TEAL_).move_to(pt(0, EQ_MID_Y))
        eq_p1_step = MathTex(r"P_1(x) = 1 + 0 \cdot x", font_size=50, color=YELLOW_).move_to(pt(0, EQ_TOP_Y))
        eq_p1_Step2 = MathTex(r"P_1(x) = 1", font_size=50, color=YELLOW_).move_to(pt(0, EQ_TOP_Y))
        note_slope = Text("Flat tangent slope → no x term", font="Sans", font_size=30, color=TEAL_).move_to(
            pt(0, EQ_BOT_Y)
        )

        self.play_t(
            FadeOut(note_p0),
            FadeIn(slope_arrow),
            Write(deriv1_eq),
            run_time=1.4,
        )
        self.play_t(Transform(eq_p0, eq_p1_step), FadeIn(note_slope), run_time=1.3)
        self.wait_t(0.6)
        self.play_t(
            Transform(eq_p0, eq_p1_Step2),
            FadeOut(slope_arrow),
            run_time=1.1,
        )

        # ============================================================ 4. curvature
        self.next_beat("curvature")
        deriv2_eq = MathTex(r"f''(0) = -\cos(0) = -1", font_size=42, color=GREEN_).move_to(pt(0, EQ_MID_Y))
        p2_curve = axes.plot(
            lambda x: taylor_cos(x, 2),
            x_range=[-COS_XLIM[2], COS_XLIM[2]],
            color=YELLOW_,
            stroke_width=5,
        )
        eq_p2 = MathTex(
            r"P_2(x) = 1", r"- \frac{1}{2}x^2",
            font_size=50, color=YELLOW_
        ).move_to(pt(0, EQ_TOP_Y))
        eq_p2[1].set_color(GREEN_)
        note_curv = Text("Same downward bend at x = 0", font="Sans", font_size=30, color=GREEN_).move_to(
            pt(0, EQ_BOT_Y)
        )

        self.play_t(
            ReplacementTransform(deriv1_eq, deriv2_eq),
            FadeOut(note_slope),
            run_time=1.2,
        )
        self.play_t(
            Transform(p0_curve, p2_curve),
            Transform(eq_p0, eq_p2),
            FadeIn(note_curv),
            run_time=2.2,
        )
        self.play_t(Indicate(eq_p0[1], color=GREEN_, scale_factor=1.12), run_time=1.0)
        self.wait_t(0.8)

        # ============================================================ 5. factorial
        self.next_beat("factorial")
        # Clear the graph cleanly so the power-rule cascade has full focus and zero overlap
        self.play_t(
            FadeOut(deriv2_eq, note_curv, anchor_lbl, axes, axes_labels, cos_curve, cos_tag, p0_curve, anchor_dot),
            eq_p0.animate.move_to(pt(0, 3.75)).scale(0.92),
            run_time=1.0,
        )

        why_title = Text("Why divide by n! ?", font="Sans", font_size=38, color=YELLOW_).move_to(pt(0, 2.45))
        d0 = MathTex(r"\text{Term: } c_n x^n", font_size=46, color=TEXT_PRIMARY).move_to(pt(0, 1.25))
        d1 = MathTex(r"\text{1st deriv: } n \cdot c_n x^{n-1}", font_size=44, color=TEAL_).move_to(pt(0, 0.15))
        d2 = MathTex(r"\text{2nd deriv: } n(n-1) \cdot c_n x^{n-2}", font_size=44, color=TEAL_).move_to(pt(0, -0.95))
        dn = MathTex(
            r"n\text{-th deriv at } 0: \quad n! \cdot c_n = f^{(n)}(0)",
            font_size=42, color=GREEN_
        )
        fit_width(dn, 6.7).move_to(pt(0, -2.15))
        cn_box = MathTex(
            r"\Longrightarrow \quad c_n = \frac{f^{(n)}(0)}{n!}",
            font_size=50, color=YELLOW_
        ).move_to(pt(0, -3.55))

        self.play_t(FadeIn(why_title), Write(d0), run_time=1.4)
        self.play_t(Write(d1), run_time=1.3)
        self.play_t(Write(d2), run_time=1.3)
        self.play_t(Write(dn), run_time=1.5)
        self.play_t(Write(cn_box), run_time=1.3)
        self.play_t(Indicate(cn_box, color=GREEN_, scale_factor=1.08), run_time=0.9)

        # ============================================================ 6. hug
        self.next_beat("hug")
        self.play_t(
            FadeOut(why_title, d0, d1, d2, dn, cn_box),
            FadeIn(axes, axes_labels, cos_curve, cos_tag, p0_curve, anchor_dot),
            eq_p0.animate.scale(1.0 / 0.92).move_to(pt(0, EQ_TOP_Y)),
            run_time=1.0,
        )

        # Interval bar showing how wide the polynomial hugs cos(x)
        hug_bar = Line(axes.c2p(-1.4, -1.75), axes.c2p(1.4, -1.75), color=GREEN_, stroke_width=7)
        hug_lbl = Text("Accurate interval widens", font="Sans", font_size=28, color=GREEN_).move_to(
            pt(0, EQ_BOT_Y)
        )
        self.play_t(Create(hug_bar), FadeIn(hug_lbl), run_time=0.7)

        stages = [
            (4, r"P_4(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!}", 2.2),
            (6, r"P_6(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!}", 3.1),
            (8, r"P_8(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!}", 4.0),
            (10, r"P_{10}(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots - \frac{x^{10}}{10!}", 4.9),
        ]

        for deg, tex_str, span in stages:
            xlim = COS_XLIM[deg]
            next_curve = axes.plot(
                lambda x, d=deg: taylor_cos(x, d),
                x_range=[-xlim, xlim],
                color=YELLOW_,
                stroke_width=5,
            )
            next_eq = MathTex(tex_str, font_size=42, color=YELLOW_)
            fit_width(next_eq, 6.7).move_to(pt(0, EQ_TOP_Y))
            next_bar = Line(axes.c2p(-span, -1.75), axes.c2p(span, -1.75), color=GREEN_, stroke_width=7)
            self.play_t(
                Transform(p0_curve, next_curve),
                Transform(eq_p0, next_eq),
                Transform(hug_bar, next_bar),
                run_time=1.8,
            )
            self.wait_t(0.25)

        # ============================================================ 7. formula
        self.next_beat("formula")
        gen_title = Text("General Taylor Series (centered at x = a)", font="Sans", font_size=30, color=TEXT_SECONDARY)
        fit_width(gen_title, 6.7).move_to(pt(0, EQ_TOP_Y + 0.2))

        taylor_formula = MathTex(
            r"f(x) = \sum_{n=0}^{\infty}",
            r"\frac{f^{(n)}(a)}{n!}",
            r"(x - a)^n",
            font_size=52,
            color=TEXT_PRIMARY,
        ).move_to(pt(0, EQ_MID_Y - 0.05))
        taylor_formula[0].set_color(BLUE_)
        taylor_formula[1].set_color(YELLOW_)
        taylor_formula[2].set_color(PURPLE_)

        role_notes = VGroup(
            MathTex(r"f^{(n)}(a) \text{ : derivatives at anchor}", font_size=34, color=YELLOW_),
            MathTex(r"n! \text{ : cancels power-rule cascade}", font_size=34, color=GREEN_),
        ).arrange(DOWN, buff=0.20).move_to(pt(0, EQ_BOT_Y - 0.35))

        self.play_t(
            FadeOut(eq_p0, hug_bar, hug_lbl),
            FadeIn(gen_title),
            Write(taylor_formula),
            run_time=1.8,
        )
        self.play_t(FadeIn(role_notes, shift=UP * 0.15), run_time=1.2)
        self.play_t(Indicate(taylor_formula[1], color=YELLOW_, scale_factor=1.1), run_time=1.0)

        # ============================================================ 8. caveat
        self.next_beat("caveat")
        self.play_t(
            FadeOut(axes, axes_labels, cos_curve, cos_tag, p0_curve, anchor_dot, gen_title, taylor_formula, role_notes),
            run_time=0.8,
        )

        cav_axes = Axes(
            x_range=[-2.2, 2.2, 1.0],
            y_range=[-1.8, 1.8, 1.0],
            x_length=6.6,
            y_length=4.2,
            axis_config={"color": GUIDE_, "stroke_width": 2.5, "include_tip": False},
        ).move_to(GRAPH_CENTER)

        f_cav = cav_axes.plot(lambda x: 1.0 / (1.0 + x * x), x_range=[-2.1, 2.1], color=BLUE_, stroke_width=5)
        p_cav = cav_axes.plot(
            lambda x: 1.0 - x**2 + x**4 - x**6 + x**8 - x**10,
            x_range=[-1.13, 1.13],
            color=YELLOW_,
            stroke_width=5,
        )
        wall_left = DashedLine(
            cav_axes.c2p(-1.0, -1.7), cav_axes.c2p(-1.0, 1.7),
            color=CORAL_, stroke_width=3.5, dash_length=0.12
        )
        wall_right = DashedLine(
            cav_axes.c2p(1.0, -1.7), cav_axes.c2p(1.0, 1.7),
            color=CORAL_, stroke_width=3.5, dash_length=0.12
        )
        wall_lbl_l = MathTex(r"x = -1", font_size=30, color=CORAL_).next_to(wall_left, UP, buff=0.12)
        wall_lbl_r = MathTex(r"x = +1", font_size=30, color=CORAL_).next_to(wall_right, UP, buff=0.12)

        cav_eq = MathTex(
            r"\frac{1}{1+x^2} = 1 - x^2 + x^4 - x^6 + \cdots",
            font_size=42, color=TEXT_PRIMARY
        )
        fit_width(cav_eq, 6.7).move_to(pt(0, EQ_TOP_Y))
        cav_note = Text("Converges only inside radius |x| < 1", font="Sans", font_size=32, color=CORAL_)
        fit_width(cav_note, 6.7).move_to(pt(0, EQ_MID_Y))

        self.play_t(Create(cav_axes), Create(f_cav), Write(cav_eq), run_time=1.6)
        self.play_t(Create(p_cav), run_time=1.5)
        self.play_t(
            Create(wall_left), Create(wall_right),
            FadeIn(wall_lbl_l), FadeIn(wall_lbl_r),
            FadeIn(cav_note),
            run_time=1.4,
        )
        self.play_t(Indicate(cav_note, color=CORAL_, scale_factor=1.05), run_time=0.9)

        # ============================================================ 9. lesson
        self.next_beat("lesson")
        self.play_t(
            FadeOut(cav_axes, f_cav, p_cav, wall_left, wall_right, wall_lbl_l, wall_lbl_r, cav_eq, cav_note),
            run_time=0.8,
        )

        # Final visual: clean cosine curve + degree-12 Taylor polynomial hugging it + takeaway
        fin_axes, _ = build_cos_axes()
        fin_axes.move_to(pt(0.0, 2.15))
        fin_cos = fin_axes.plot(lambda x: math.cos(x), x_range=[-6.0, 6.0], color=BLUE_, stroke_width=5)
        fin_poly = fin_axes.plot(
            lambda x: taylor_cos(x, 12), x_range=[-6.0, 6.0], color=YELLOW_, stroke_width=5
        )
        fin_dot = Dot(fin_axes.c2p(0, 1), radius=0.11, color=PURPLE_)

        t1 = Text("Every derivative at one point", font="Sans", font_size=40, color=TEXT_PRIMARY)
        t2 = Text("rebuilds the curve far away.", font="Sans", font_size=40, color=YELLOW_)
        takeaway = VGroup(t1, t2).arrange(DOWN, buff=0.28)
        fit_width(takeaway, 6.7).move_to(pt(0.0, -2.1))

        outro_handle = Text(HANDLE, font="Sans", font_size=44, color=BLUE_).move_to(pt(0.0, -3.85))

        self.play_t(FadeIn(fin_axes), Create(fin_cos), FadeIn(fin_dot, scale=1.3), run_time=1.2)
        self.play_t(Create(fin_poly), run_time=1.5)
        self.play_t(Write(t1), Write(t2), run_time=1.6)
        self.play_t(FadeIn(outro_handle, shift=UP * 0.15), run_time=0.8)

        self.end_beat()
        with open(TIMELINE_FILE, "w") as f:
            json.dump({"beats": self.timeline, "total": round(self.t, 3)}, f, indent=2)

    # ---------------------------------------------------------- timing helpers
    def play_t(self, *anims, run_time=1.0, **kw):
        self.play(*anims, run_time=run_time, **kw)
        self.t += run_time

    def wait_t(self, d):
        self.wait(d)
        self.t += d

    def next_beat(self, name):
        if self._beat is not None:
            self.end_beat()
        dur = self.beats.get(name, 5.0)
        self._beat = (name, dur, self.t)
        self.timeline.append({"beat": name, "start": round(self.t, 3), "dur": dur})

    def end_beat(self):
        name, dur, start = self._beat
        pad = start + dur - self.t
        if pad < -0.05:
            print(f"WARNING: beat '{name}' overruns its target by {-pad:.2f}s")
        if pad > 0.0:
            self.wait_t(pad)
        self._beat = None
        for b in self.timeline:
            if b["beat"] == name and "end" not in b:
                b["end"] = round(self.t, 3)
