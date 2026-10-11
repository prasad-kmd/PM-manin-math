"""
Why the sum of the first n odd numbers is always a perfect square — 9:16 FHD explainer (@prasadkmd)

Style: classic 3Blue1Brown look (dark #1C1C1C, morphs, colour-coded terms).
Proof: gnomons. Each L-shaped border around an n×n square holds 2n−1 tiles,
so the k-th border adds the k-th odd number and the total after n borders is n².
Algebra check: k² − (k−1)² = 2k − 1, so the sum telescopes to n².

Final render:
  manim -qh --fps 60 -r 1080,1920 scripts/odd_squares.py OddSquares

Beat durations are read from research/odd_squares/beats.json (narration-driven).
Actual beat timings are written to research/odd_squares/timeline.json.
"""
import json
import os

import numpy as np
from manim import *

# ---------------------------------------------------------------- format
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#1C1C1C"

# ---------------------------------------------------------------- palette (classic 3b1b)
BG = "#1C1C1C"
BLUE_ = "#58C4DD"
YELLOW_ = "#FFFF00"
GREEN_ = "#83C167"
RED_ = "#FF6666"
ORANGE_ = "#FF8C42"
GREY_ = "#888888"
TILE_COLORS = [BLUE_, YELLOW_, GREEN_, ORANGE_]  # gnomon 1..4
HANDLE = "@prasadkmd"

# ---------------------------------------------------------------- geometry
N = 4          # final square is 4×4 (1+3+5+7 = 16)
T = 0.66       # tile size
CX, CY = 0.0, 2.3   # grid centre
EQ_Y = -0.75        # running equation line

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BEATS_FILE = os.path.join(ROOT, "research", "odd_squares", "beats.json")
TIMELINE_FILE = os.path.join(ROOT, "research", "odd_squares", "timeline.json")

DEFAULT_BEATS = [
    ("hook", 8.0),
    ("setup", 4.0),
    ("gnomon", 10.0),
    ("result", 5.0),
    ("algebra", 8.0),
    ("caveat", 6.0),
    ("close", 7.0),
]


def load_beats():
    if os.path.exists(BEATS_FILE):
        with open(BEATS_FILE) as f:
            data = json.load(f)
        return [(b["name"], float(b["dur"])) for b in data]
    return DEFAULT_BEATS


def pt(x, y):
    return np.array([x, y, 0.0])


def tile_centre(i, j):
    """Centre of tile at row i (from top), column j (from left) of the N×N grid."""
    x0 = CX - N * T / 2
    y_top = CY + N * T / 2
    return pt(x0 + (j + 0.5) * T, y_top - (i + 0.5) * T)


def make_tile(i, j, color):
    return Square(side_length=T * 0.94, stroke_width=0, fill_opacity=0.95, fill_color=color).move_to(
        tile_centre(i, j))


def gnomon_cells(k):
    """Tiles of the k-th border: the L-shape where max(row, col) == k-1 (2k-1 tiles)."""
    return [(i, j) for i in range(k) for j in range(k) if max(i, j) == k - 1]


def gnomon_group(k):
    return VGroup(*[make_tile(i, j, TILE_COLORS[k - 1]) for i, j in gnomon_cells(k)])


def sum_tex(k, final_sq=True):
    """MathTex for 1 + 3 + ... + (2k-1) = k^2, with the newest term at index 2k-1."""
    parts = ["1"]
    for j in range(2, k + 1):
        parts += ["+", str(2 * j - 1)]
    parts += ["=", f"{k}^2"]
    eq = MathTex(*parts, font_size=50)
    eq.move_to(pt(CX, EQ_Y))
    newest = 0 if k == 1 else 2 * k - 1
    eq[newest].set_color(TILE_COLORS[k - 1])
    return eq


class OddSquares(Scene):
    def construct(self):
        self.t = 0.0
        self.timeline = []
        self._beat = None
        self.beats = {name: dur for name, dur in load_beats()}

        self.brand = Text(HANDLE, font_size=30, color=GREY_).move_to(pt(0, -6.4))
        self.add(self.brand)

        # ============================================================ hook
        self.next_beat("hook")
        title = Text("Sum of odd numbers", font_size=40, color=GREY_).move_to(pt(0, 5.4))
        self.play_t(FadeIn(title), run_time=0.6)
        lines = VGroup()
        totals = [("1", "1"), ("1+3", "4"), ("1+3+5", "9"), ("1+3+5+7", "16")]
        for k, (lhs, rhs) in enumerate(totals):
            lines.add(MathTex(lhs, "=", rhs, font_size=60))
        lines.arrange(DOWN, buff=0.45).move_to(pt(0, 1.2))
        for ln in lines:
            ln.set_color_by_tex("16", YELLOW_)
            ln.set_color_by_tex("9", YELLOW_)
        self.play_t(Write(lines[0]), run_time=0.8)
        self.play_t(Write(lines[1]), run_time=0.8)
        self.play_t(Write(lines[2]), run_time=0.8)
        self.play_t(Write(lines[3]), run_time=0.8)
        q = MathTex(r"\text{always a square?}", font_size=44, color=RED_).move_to(pt(0, -1.9))
        self.play_t(FadeIn(q, shift=UP * 0.2), run_time=0.9)
        self.wait_t(0.8)
        self.play_t(FadeOut(title, lines, q), run_time=0.7)

        # ============================================================ setup
        self.next_beat("setup")
        outline = Square(side_length=N * T, color=GREY_, stroke_width=2).move_to(pt(CX, CY))
        first = gnomon_group(1)
        self.play_t(Create(outline), run_time=0.8)
        self.play_t(FadeIn(first, scale=0.4), run_time=0.7)
        eq = sum_tex(1)
        self.play_t(Write(eq), run_time=0.8)
        self.current_eq = eq
        self.grid = VGroup(first)

        # ============================================================ gnomon
        self.next_beat("gnomon")
        for k in (2, 3, 4):
            g = gnomon_group(k)
            new_eq = sum_tex(k)
            self.play_t(FadeIn(g, lag_ratio=0.15), run_time=1.1)
            self.play_t(Transform(self.current_eq, new_eq), run_time=0.7)
            self.grid.add(g)
            self.current_eq = self.current_eq
            self.wait_t(0.3)

        # ============================================================ result
        self.next_beat("result")
        res = MathTex(r"1+3+\cdots+(2n-1)", "=", r"n^2", font_size=54, color=WHITE)
        res.move_to(pt(CX, -2.0))
        res[2].set_color(YELLOW_)
        self.play_t(FadeIn(res, shift=UP * 0.2), run_time=1.0)
        self.play_t(Indicate(res[2], color=YELLOW_, scale_factor=1.4), run_time=0.9)
        self.wait_t(0.4)
        self.play_t(FadeOut(self.grid, outline, self.current_eq, res), run_time=0.9)

        # ============================================================ algebra
        self.next_beat("algebra")
        a1 = MathTex(r"k^2 - (k-1)^2 = 2k - 1", font_size=56).move_to(pt(0, 2.4))
        a2 = MathTex(r"(1^2 - 0^2) + (2^2 - 1^2) + \cdots + (n^2 - (n-1)^2)", font_size=40).move_to(pt(0, 0.6))
        a3 = MathTex(r"= \sum_{k=1}^{n} (2k-1) = n^2", font_size=56, color=YELLOW_).move_to(pt(0, -0.9))
        a2.scale_to_fit_width(7.0)
        self.play_t(Write(a1), run_time=1.2)
        self.play_t(Write(a2), run_time=1.6)
        self.play_t(Write(a3), run_time=1.2)
        self.play_t(Indicate(a3, color=YELLOW_), run_time=0.8)
        self.wait_t(0.4)
        self.play_t(FadeOut(a1, a2, a3), run_time=0.8)

        # ============================================================ caveat
        self.next_beat("caveat")
        bad = MathTex(r"3 + 5 = 8", font_size=72, color=RED_).move_to(pt(0, 1.5))
        bad_note = Text("not a square", font_size=40, color=RED_).move_to(pt(0, 0.3))
        cross = Cross(bad, stroke_color=RED_, stroke_width=8)
        self.play_t(Write(bad), run_time=1.0)
        self.play_t(Create(cross), FadeIn(bad_note), run_time=1.0)
        good = MathTex(r"1 + 3 + 5 = 9", font_size=72, color=GREEN_).move_to(pt(0, -1.6))
        good_note = Text("starts at one: always works", font_size=40, color=GREEN_).move_to(pt(0, -2.6))
        self.play_t(Write(good), run_time=1.0)
        self.play_t(FadeIn(good_note), run_time=0.8)
        self.wait_t(0.5)
        self.play_t(FadeOut(bad, bad_note, cross, good, good_note), run_time=0.8)

        # ============================================================ close
        self.next_beat("close")
        full = VGroup()
        for k in (1, 2, 3, 4):
            full.add(gnomon_group(k))
        self.play_t(FadeIn(full, lag_ratio=0.05), run_time=2.0)
        self.wait_t(0.4)
        closing = Text("Every perfect square is a stack of odd numbers.", font_size=44, color=WHITE)
        closing.scale_to_fit_width(6.8).move_to(pt(0, -1.8))
        self.play_t(Write(closing), run_time=2.0)
        self.wait_t(0.5)

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
