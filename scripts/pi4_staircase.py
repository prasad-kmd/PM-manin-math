"""
The π = 4 Staircase Paradox — 9:16 FHD explainer (@prasadkmd)

Style: classic 3Blue1Brown look + city-block (taxicab) metaphor + Shorts-style hook.
Plan:  research/pi4_staircase/scenes.md
Facts: research/pi4-staircase-research.md

Final render:
  manim -qh --fps 60 -r 1080,1920 scripts/pi4_staircase.py PiFourStaircase

Beat durations are read from research/pi4_staircase/beats.json (narration-driven).
Each beat is padded to its target duration, so audio can be aligned afterwards.
The timeline actually produced is written to research/pi4_staircase/timeline.json.
"""
import json
import math
import os

import numpy as np
from manim import *

# ---------------------------------------------------------------- format
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#1C1C1C"

# ---------------------------------------------------------------- palette
BG = "#1C1C1C"
BLUE_ = "#58C4DD"    # true circle / Euclidean length / π
YELLOW_ = "#FFFF00"  # staircase / taxicab length / 4
GREEN_ = "#83C167"   # |Δy| / identity
RED_ = "#FF6666"     # |Δx| / doubt
GREY_ = "#888888"
HANDLE = "@prasadkmd"

# ---------------------------------------------------------------- geometry
# Unit: the square's side = circle's diameter = 1, drawn at S scene units.
S = 3.6
R = S / 2
CX, CY = 0.0, 2.0    # figure centre
TITLE_Y = 5.4

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BEATS_FILE = os.path.join(ROOT, "research", "pi4_staircase", "beats.json")
TIMELINE_FILE = os.path.join(ROOT, "research", "pi4_staircase", "timeline.json")

DEFAULT_BEATS = [
    ("hook", 4.0),
    ("setup", 7.0),
    ("fold", 10.0),
    ("converge", 7.0),
    ("paradox", 7.0),
    ("taxi_sibling", 12.0),
    ("taxi_circle", 14.0),
    ("resolution", 8.0),
    ("lesson", 8.0),
]


def load_beats():
    if os.path.exists(BEATS_FILE):
        with open(BEATS_FILE) as f:
            data = json.load(f)
        return [(b["name"], float(b["dur"])) for b in data]
    return DEFAULT_BEATS


def pt(x, y):
    return np.array([x, y, 0.0])


def stair_pts(n, cx=CX, cy=CY, r=R):
    """Closed taxicab staircase around the circle, n steps per quarter.

    Vertices P_k lie on the circle; each step P_k -> C_k -> P_{k+1} is axis-aligned,
    where C_k is the bounding-box corner (always outside the circle).
    Total taxicab length = 8r per loop (= 4 when the diameter is 1), for every n.
    """
    N = 4 * n
    P = [(r * math.cos(2 * math.pi * k / N), r * math.sin(2 * math.pi * k / N)) for k in range(N)]
    out = []
    for k in range(N):
        x0, y0 = P[k]
        x1, y1 = P[(k + 1) % N]
        cxk = x0 if abs(x0) >= abs(x1) else x1
        cyk = y0 if abs(y0) >= abs(y1) else y1
        out.append((x0, y0))
        out.append((cxk, cyk))
    return [pt(x + cx, y + cy) for x, y in out]


def stair_poly(n, color=YELLOW_, width=5):
    return Polygon(*stair_pts(n), color=color, stroke_width=width, fill_opacity=0)


def square_taxi_pts(n, x0, y0, side):
    """Open staircase (right, then up) from (x0,y0) to (x0+side, y0+side) with n steps."""
    h = side / n
    pts = []
    for i in range(n):
        pts.append(pt(x0 + i * h, y0 + i * h))
        pts.append(pt(x0 + (i + 1) * h, y0 + i * h))
    pts.append(pt(x0 + side, y0 + side))
    return pts


class PiFourStaircase(MovingCameraScene):
    def construct(self):
        self.t = 0.0
        self.timeline = []
        self._beat = None
        self.beats = {name: dur for name, dur in load_beats()}

        self.brand = Text(HANDLE, font_size=30, color=GREY_).move_to(pt(0, -6.4))
        self.add(self.brand)

        # ============================================================ 1 hook
        self.next_beat("hook")
        self.title = MathTex(r"\pi = 4\,?", font_size=120, color=WHITE).move_to(pt(0, 0))
        self.play_t(FadeIn(self.title, scale=0.6), run_time=0.7)
        self.play_t(Indicate(self.title, color=YELLOW_, scale_factor=1.15), run_time=0.8)
        self.play_t(self.title.animate.scale(0.5).move_to(pt(0, TITLE_Y)), run_time=0.8)

        # ============================================================ 2 setup
        self.next_beat("setup")
        self.sq = Square(side_length=S, color=WHITE, stroke_width=4).move_to(pt(CX, CY))
        self.circ = Circle(radius=R, color=BLUE_, stroke_width=4).move_to(pt(CX, CY))
        self.side_lbl = MathTex("1", font_size=44).move_to(pt(CX, CY - R - 0.45))
        self.d_lbl = MathTex(r"d = 1", color=BLUE_, font_size=40).move_to(pt(CX, CY))
        self.perim = MathTex(r"1 + 1 + 1 + 1 = 4", font_size=46).move_to(pt(0, -1.2))
        self.play_t(Create(self.sq), Create(self.circ), run_time=1.6)
        self.play_t(Write(self.side_lbl), Write(self.d_lbl), run_time=0.9)
        self.play_t(Write(self.perim), run_time=1.0)

        # ============================================================ 3 fold
        self.next_beat("fold")
        self.stage = MathTex(r"n = 1", font_size=42).move_to(pt(0, -0.85))
        self.L_lbl = MathTex(r"L_n = 4", font_size=52).move_to(pt(0, -2.0))
        self.play_t(
            Transform(self.perim, MathTex(r"L_n = 4", font_size=52).move_to(pt(0, -2.0))),
            Write(self.stage),
            run_time=0.9,
        )
        self.L_lbl = self.perim
        self.shape = self.sq
        for n in (2, 4, 8):
            new_shape = stair_poly(n)
            new_stage = MathTex(rf"n = {n}", font_size=42).move_to(pt(0, -0.85))
            self.play_t(Transform(self.shape, new_shape), Transform(self.stage, new_stage), run_time=1.1)
            self.wait_t(0.3)

        # ============================================================ 4 converge
        self.next_beat("converge")
        for n in (16, 32):
            new_shape = stair_poly(n, width=4)
            new_stage = MathTex(rf"n = {n}", font_size=42).move_to(pt(0, -0.85))
            self.play_t(Transform(self.shape, new_shape), Transform(self.stage, new_stage), run_time=0.9)
        corner = pt(CX + R * 0.72, CY + R * 0.72)
        self.play_t(self.camera.frame.animate.set_width(1.5).move_to(corner), run_time=2.0)
        self.wait_t(0.6)
        self.play_t(self.camera.frame.animate.set_width(8.0).move_to(ORIGIN), run_time=1.6)

        # ============================================================ 5 paradox
        self.next_beat("paradox")
        stair_txt = MathTex(r"\text{staircase: } L_n = 4", color=YELLOW_, font_size=46).move_to(pt(0, -2.0))
        circ_txt = MathTex(r"\text{circle: } \pi \approx 3.14", color=BLUE_, font_size=46).move_to(pt(0, -2.85))
        q = MathTex("?", color=RED_, font_size=110).move_to(pt(3.0, -2.4))
        self.play_t(Transform(self.L_lbl, stair_txt), Write(circ_txt), run_time=1.2)
        self.play_t(FadeIn(q, scale=0.5), run_time=0.6)
        self.play_t(Indicate(q, color=RED_, scale_factor=1.3), run_time=0.9)
        self.circ_txt = circ_txt
        self.q = q

        # ============================================================ 6 taxi_sibling
        self.next_beat("taxi_sibling")
        self.play_t(
            FadeOut(self.shape, self.stage, self.L_lbl, self.circ_txt, self.circ, self.sq,
                    self.side_lbl, self.d_lbl, self.perim, self.q),
            run_time=0.8,
        )
        x0, y0 = CX - S / 2, CY - S / 2
        grid = VGroup(
            *[Line(pt(x0 + k * S / 4, y0), pt(x0 + k * S / 4, y0 + S), color=GREY_, stroke_width=2,
                   stroke_opacity=0.45) for k in range(5)],
            *[Line(pt(x0, y0 + k * S / 4), pt(x0 + S, y0 + k * S / 4), color=GREY_, stroke_width=2,
                   stroke_opacity=0.45) for k in range(5)],
        )
        frame_sq = Square(side_length=S, color=WHITE, stroke_width=3).move_to(pt(CX, CY))
        stair2 = VMobject(color=YELLOW_, stroke_width=7)
        stair2.set_points_as_corners(square_taxi_pts(4, x0, y0, S))
        diag_path = Line(pt(x0, y0), pt(x0 + S, y0 + S))
        diag = DashedLine(pt(x0, y0), pt(x0 + S, y0 + S), color=BLUE_, stroke_width=5, dash_length=0.14)
        taxi = Dot(pt(x0, y0), color=YELLOW_, radius=0.13)
        bird = Dot(pt(x0, y0), color=BLUE_, radius=0.13)
        lbl_taxi = MathTex(r"\text{taxi} = 2", color=YELLOW_, font_size=44).move_to(pt(1.3, y0 - 0.55))
        lbl_bird = MathTex(r"\text{bird} = \sqrt{2} \approx 1.41", color=BLUE_, font_size=40).move_to(
            pt(0, CY + S / 2 + 0.4))
        self.sib = [grid, frame_sq, stair2, diag, taxi, bird, lbl_taxi, lbl_bird]
        self.play_t(FadeIn(grid), Create(frame_sq), run_time=0.8)
        self.play_t(Create(stair2), run_time=1.4)
        self.play_t(Create(diag), FadeIn(taxi), FadeIn(bird), run_time=0.9)
        self.play_t(Write(lbl_taxi), Write(lbl_bird), run_time=0.9)
        self.play_t(
            MoveAlongPath(taxi, stair2, rate_func=linear),
            MoveAlongPath(bird, diag_path, rate_func=linear),
            run_time=3.2,
        )
        self.play_t(Indicate(lbl_bird, color=BLUE_), run_time=0.8)

        # ============================================================ 7 taxi_circle
        self.next_beat("taxi_circle")
        self.play_t(FadeOut(*self.sib), run_time=0.8)
        circ2 = Circle(radius=R, color=BLUE_, stroke_width=4).move_to(pt(CX, CY))
        big = stair_poly(16, width=4)
        taxi2 = Dot(stair_pts(16)[0], color=YELLOW_, radius=0.11)
        self.play_t(Create(circ2), Create(big), run_time=1.8)
        self.play_t(FadeIn(taxi2), run_time=0.4)
        self.play_t(MoveAlongPath(taxi2, big, rate_func=linear), run_time=4.6)
        f1 = MathTex(r"\text{taxi length} = \sum \left(|\Delta x| + |\Delta y|\right)", font_size=38).move_to(
            pt(0, -2.2))
        f2 = MathTex(r"= 4", color=YELLOW_, font_size=52).move_to(pt(0, -3.0))
        self.play_t(Write(f1), run_time=1.2)
        self.play_t(Write(f2), run_time=0.7)
        # zoom onto one step near 45 degrees to show Δx and Δy
        pts = stair_pts(16)
        A, C, B = pts[16], pts[17], pts[18]
        zoom_c = (A + B) / 2
        seg1 = Line(A, C, color=GREEN_, stroke_width=5)
        seg2 = Line(C, B, color=RED_, stroke_width=5)
        def label_for(seg, p, q):
            dx, dy = abs(q[0] - p[0]), abs(q[1] - p[1])
            return (MathTex(r"|\Delta y|", color=GREEN_, font_size=6) if dy > dx
                    else MathTex(r"|\Delta x|", color=RED_, font_size=6))
        lab1 = label_for(seg1, A, C).move_to(zoom_c + pt(-0.06, 0.04))
        lab2 = label_for(seg2, C, B).move_to(zoom_c + pt(0.04, 0.08))
        self.play_t(self.camera.frame.animate.set_width(1.2).move_to(zoom_c), run_time=1.6)
        self.play_t(Create(seg1), Create(seg2), FadeIn(lab1), FadeIn(lab2), run_time=1.0)
        self.wait_t(0.5)
        self.play_t(FadeOut(seg1, seg2, lab1, lab2), self.camera.frame.animate.set_width(8.0).move_to(ORIGIN),
                    run_time=1.5)
        self.circ2, self.big, self.taxi2, self.f1, self.f2 = circ2, big, taxi2, f1, f2

        # ============================================================ 8 resolution
        self.next_beat("resolution")
        lab4 = MathTex("4", color=YELLOW_, font_size=84).move_to(pt(-2.6, CY + 0.9))
        labpi = MathTex(r"\pi", color=BLUE_, font_size=84).move_to(pt(2.6, CY + 0.9))
        eq = MathTex(r"\pi \times \frac{4}{\pi} = 4", font_size=60).move_to(pt(0, -2.3))
        cap = MathTex(r"\text{taxi length} \div \text{true length} = \frac{4}{\pi}", font_size=40,
                      color=GREY_).move_to(pt(0, -3.3))
        self.play_t(FadeOut(self.f1, self.f2), FadeIn(lab4, shift=RIGHT * 0.3),
                    FadeIn(labpi, shift=LEFT * 0.3), run_time=1.0)
        self.play_t(Write(eq), run_time=1.2)
        self.play_t(FadeIn(cap), run_time=0.7)
        self.lab4, self.labpi, self.eq, self.cap = lab4, labpi, eq, cap

        # ============================================================ 9 lesson
        self.next_beat("lesson")
        self.play_t(FadeOut(self.big, self.circ2, self.taxi2, self.lab4, self.labpi, self.eq, self.cap),
                    run_time=0.9)
        l1 = Text("Shapes can converge", font_size=52, color=WHITE)
        l2 = Text("while their lengths don't.", font_size=52, color=YELLOW_)
        l3 = Text("Check the direction,", font_size=40, color=GREY_)
        l4 = Text("not just the position.", font_size=40, color=GREY_)
        group = VGroup(l1, l2, VGroup(l3, l4).arrange(DOWN, buff=0.2)).arrange(DOWN, buff=0.6)
        group.scale_to_fit_width(6.6).move_to(pt(0, 0.3))
        self.play_t(Write(l1), run_time=1.2)
        self.play_t(Write(l2), run_time=1.2)
        self.play_t(FadeIn(l3, shift=UP * 0.2), FadeIn(l4, shift=UP * 0.2), run_time=1.0)

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
        # record actual end
        for b in self.timeline:
            if b["beat"] == name and "end" not in b:
                b["end"] = round(self.t, 3)
