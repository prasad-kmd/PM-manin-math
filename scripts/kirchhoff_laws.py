"""
Kirchhoff's Laws — KCL & KVL, 9:16 FHD explainer (@prasadkmd)

Style: classic 3Blue1Brown — pure black, one idea per beat, algebra earned
after the physical picture.
Plan:  research/kirchhoff_laws/scenes.md
Facts: research/kirchhoff-laws-research.md

Final render:
  manim -qh --fps 60 -r 1080,1920 scripts/kirchhoff_laws.py KirchhoffLaws

One circuit carries the whole video (scenes.md, "Recurring Visual Motifs"):
same wires, same nodes, same colours, so the viewer keeps their bearings.
Objects are transformed and re-focused, never replaced.

PACING CONTRACT — each beat ends by *holding its payoff*, and the next beat
does the clearing. Nothing is faded out before its beat ends, so the padding
after the last animation always lands on something worth looking at rather
than an empty frame. Holds are placed deliberately between reveals
(docs/animation-style.md, "Use pauses after major transformations").

Numeric example is exact in fractions — 12 V, 4/12/6 ohm:
  R2||R3 = 4, R_total = 8, I_total = 1.5 A, V_AB = 6 V, I2 = 0.5 A, I3 = 1.0 A
Everything printed on screen is one of those exact values.

Beat durations come from research/kirchhoff_laws/beats.json (narration-driven);
the timeline actually produced is written to .../timeline.json.

LAYOUT (frame 8.0 x 14.2222, so x in [-4, 4], y in [-7.11, 7.11]):
  y = 4.85  beat heading
  y = 3.30  top rail (YT)
  y = 1.70  lower branch (YM)
  y = 0.45  bottom rail / battery (YB)
  y < -1.2  equation bands, clear of the circuit
  y = -6.4  watermark (@prasadkmd)
"""
import json
import os

import numpy as np
from manim import *

from _layout import use_vertical
from _theme import (
    AUX,
    BG,
    BLUE,
    CONTRAST,
    EMPHASIS,
    FS_LABEL,
    FS_MATH,
    GREEN,
    GUIDE,
    RESULT,
    SECONDARY,
    SW_GUIDE,
    SW_PRIMARY,
    SW_SECONDARY,
    TEXT,
    TEXT_DIM,
    apply_theme,
    brand,
    label,
)

# --------------------------------------------------------------- format
use_vertical()  # 1080x1920, frame 8.0 x 14.2222 (135 px/unit)

# --------------------------------------------------------------- geometry
X0, XA, XB, X1 = -3.40, -0.65, 1.25, 3.40   # rail columns, inside |x| <= 3.68
YT, YM, YB = 3.30, 1.70, 0.45               # top rail, lower branch, bottom rail

R_W, R_H = 0.50, 0.28                       # resistor symbol footprint
R1X = (X0 + XA) / 2
R2X = R3X = (XA + XB) / 2

BAT_X = -2.30                               # battery centre, bottom rail
BAT_GAP = (BAT_X - 0.20, BAT_X + 0.20)      # wire gap the battery occupies

HEADING_Y = 4.85
EQ_RULE = -1.35
EQ_NUM = -2.25
EQ_LESSON = -3.15

# hook + resolve mesh: two cells, 7 branches, 6 of them unknown currents
MX = [-2.60, 0.00, 2.60]
MY = [3.50, 1.20]

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RES = os.path.join(ROOT, "research", "kirchhoff_laws")
BEATS_FILE = os.path.join(RES, "beats.json")
TIMELINE_FILE = os.path.join(RES, "timeline.json")

# word-count estimates; replaced by real audio durations once TTS exists
DEFAULT_BEATS = [
    ("hook", 6.6),
    ("build", 13.8),
    ("kcl", 15.8),
    ("kcl_why", 14.2),
    ("kvl", 15.4),
    ("kvl_why", 11.4),
    ("resolve", 12.6),
]


def load_beats():
    if os.path.exists(BEATS_FILE):
        with open(BEATS_FILE) as f:
            return [(b["name"], float(b["dur"])) for b in json.load(f)]
    return DEFAULT_BEATS


def pt(x, y):
    return np.array([x, y, 0.0])


# --------------------------------------------------------------- builders
def wire(*pts, color=BLUE, width=SW_PRIMARY):
    """Polyline conductor, square corners (schematic convention)."""
    m = VMobject(color=color, stroke_width=width)
    m.set_points_as_corners([np.asarray(p, dtype=float) for p in pts])
    return m


def polyline(points):
    """Path mobject for MoveAlongPath — same geometry, invisible stroke."""
    m = VMobject()
    m.set_points_as_corners([np.asarray(p, dtype=float) for p in points])
    return m


def resistor_h(center, color=BLUE):
    """Horizontal resistor symbol; fills with the background to mask the wire."""
    return Rectangle(
        width=R_W, height=R_H, color=color, stroke_width=SW_SECONDARY,
        fill_color=BG, fill_opacity=1.0,
    ).move_to(center)


def battery(x=BAT_X, y=YB):
    """Battery on a horizontal rail: long plate = + (left), short plate = -.

    Oriented so current leaves the + terminal leftward, making node A the
    splitting node, matching the narration.
    """
    return VGroup(
        Line(pt(x - 0.12, y - 0.34), pt(x - 0.12, y + 0.34),
             color=EMPHASIS, stroke_width=SW_PRIMARY),
        Line(pt(x + 0.12, y - 0.19), pt(x + 0.12, y + 0.19),
             color=EMPHASIS, stroke_width=SW_PRIMARY),
    )


def current_arrow(start, end, amps, color):
    """Branch arrow whose shaft weight is proportional to the current.

    Proportional stroke is a quantitative cue (docs/mathematical-visualization.md:
    represent quantities proportionally when the visual suggests a comparison).
    """
    return Arrow(
        start, end, buff=0, color=color,
        stroke_width=max(3.0, 5.0 * amps),
        tip_length=0.24, max_tip_length_to_length_ratio=0.5,
    )


def tag(text, pos, color, size=FS_LABEL):
    """Numeric annotation at (x, y). Accepts a 2-tuple for readability."""
    return MathTex(text, font_size=size, color=color).move_to(pt(*pos))


def heading(*parts):
    """Beat heading from (text, colour) pairs."""
    return VGroup(*[label(t, 34, c) for t, c in parts]).arrange(
        RIGHT, buff=0.16
    ).move_to(pt(0, HEADING_Y))


class KirchhoffLaws(MovingCameraScene):
    # ----------------------------------------------------------- machinery
    def construct(self):
        apply_theme(self)
        self.t = 0.0
        self.timeline = []
        self._beat = None
        self.head = None
        self.beats = {n: d for n, d in load_beats()}

        self.add(brand())

        self.beat_hook()
        self.beat_build()
        self.beat_kcl()
        self.beat_kcl_why()
        self.beat_kvl()
        self.beat_kvl_why()
        self.beat_resolve()
        self.end_beat()

        with open(TIMELINE_FILE, "w") as f:
            json.dump({"beats": self.timeline, "total": round(self.t, 3)}, f, indent=2)

    def play_t(self, *anims, run_time=1.0, **kw):
        self.play(*anims, run_time=run_time, **kw)
        self.t += run_time

    def wait_t(self, d):
        self.wait(d)
        self.t += d

    def next_beat(self, name):
        if self._beat is not None:
            self.end_beat()
        dur = self.beats.get(name, 6.0)
        self._beat = (name, dur, self.t)
        self.timeline.append({"beat": name, "start": round(self.t, 3), "dur": dur})

    def end_beat(self):
        """Close the beat, padding to its narration duration.

        `pad` is recorded in the timeline: a large pad means the animation is
        running ahead of the narration and the beat is holding too long.
        """
        name, dur, start = self._beat
        pad = start + dur - self.t
        if pad < -0.05:
            print(f"WARNING: beat '{name}' overruns its target by {-pad:.2f}s")
        if pad > 0.0:
            self.wait_t(pad)
        for b in self.timeline:
            if b["beat"] == name and "end" not in b:
                b["end"] = round(self.t, 3)
                b["pad"] = round(pad, 3)
        self._beat = None

    def set_heading(self, *parts, first=False):
        """Introduce or cross-fade the beat heading (never a hard cut)."""
        new = heading(*parts)
        if self.head is None:
            self.head = new
            self.play_t(FadeIn(new, shift=0.12 * DOWN), run_time=0.6)
        else:
            self.play_t(Transform(self.head, new), run_time=0.6)

    def clear_heading(self):
        if self.head is not None:
            self.play_t(FadeOut(self.head), run_time=0.4)
            self.head = None

    # ----------------------------------------------------------- the circuit
    def build_circuit(self):
        """The one circuit. Built once, reused by every circuit beat."""
        P = {}

        P["left_rail"] = wire(pt(X0, YB), pt(X0, YT))
        P["top_left"] = wire(pt(X0, YT), pt(XA, YT))       # R1 lives here
        P["upper"] = wire(pt(XA, YT), pt(XB, YT))          # R2 lives here
        P["top_right"] = wire(pt(XB, YT), pt(X1, YT))
        P["right_rail"] = wire(pt(X1, YT), pt(X1, YB))
        P["bot_right"] = wire(pt(BAT_GAP[1], YB), pt(X1, YB))
        P["bot_left"] = wire(pt(X0, YB), pt(BAT_GAP[0], YB))
        P["drop_a"] = wire(pt(XA, YT), pt(XA, YM))
        P["lower"] = wire(pt(XA, YM), pt(XB, YM))          # R3 lives here
        P["rise_b"] = wire(pt(XB, YM), pt(XB, YT))

        P["r1"] = resistor_h(pt(R1X, YT))
        P["r2"] = resistor_h(pt(R2X, YT))
        P["r3"] = resistor_h(pt(R3X, YM))
        P["bat"] = battery()

        P["a"] = Dot(pt(XA, YT), radius=0.10, color=EMPHASIS)
        P["b"] = Dot(pt(XB, YT), radius=0.10, color=EMPHASIS)
        P["lbl_a"] = label("A", FS_LABEL, EMPHASIS).move_to(pt(XA, YT + 0.44))
        P["lbl_b"] = label("B", FS_LABEL, EMPHASIS).move_to(pt(XB, YT + 0.44))

        # component values sit just below their symbols
        P["v_bat"] = label("12 V", FS_LABEL, EMPHASIS).move_to(pt(BAT_X, YB - 0.58))
        P["v_r1"] = MathTex(r"R_1 = 4\,\Omega", font_size=28, color=TEXT_DIM)
        P["v_r1"].move_to(pt(R1X - 0.10, YT - 0.50))
        P["v_r2"] = MathTex(r"R_2 = 12\,\Omega", font_size=28, color=TEXT_DIM)
        P["v_r2"].move_to(pt(R2X, YT - 0.50))
        P["v_r3"] = MathTex(r"R_3 = 6\,\Omega", font_size=28, color=TEXT_DIM)
        P["v_r3"].move_to(pt(R3X, YM - 0.50))

        # sustained current-direction arrows (kept through the middle of the video)
        P["f_left"] = current_arrow(pt(X0, 0.95), pt(X0, 2.30), 1.5, BLUE)
        P["f_r1"] = current_arrow(pt(R1X + R_W + 0.08, YT), pt(XA - 0.14, YT), 1.5, BLUE)
        P["f_r2"] = current_arrow(pt(XA + 0.32, YT), pt(R2X - R_W - 0.08, YT), 0.5, SECONDARY)
        P["f_r3"] = current_arrow(pt(XA, YT - 0.42), pt(XA, YM - 0.14), 1.0, SECONDARY)

        return VGroup(*P.values()), P

    def make_mesh(self):
        """The opening network: 2 cells, 7 branches, 6 unknown currents."""
        lines = VGroup(
            wire(pt(MX[0], MY[0]), pt(MX[2], MY[0]), color=GUIDE, width=SW_SECONDARY),
            wire(pt(MX[0], MY[1]), pt(MX[2], MY[1]), color=GUIDE, width=SW_SECONDARY),
            wire(pt(MX[1], MY[0]), pt(MX[1], MY[1]), color=GUIDE, width=SW_SECONDARY),
            wire(pt(MX[2], MY[0]), pt(MX[2], MY[1]), color=GUIDE, width=SW_SECONDARY),
            wire(pt(MX[0], MY[0]), pt(MX[0], MY[1]), color=EMPHASIS, width=SW_PRIMARY),
        )
        mid = (MY[0] + MY[1]) / 2
        arrows = VGroup(
            current_arrow(pt(MX[0] + 0.45, MY[0]), pt(MX[0] + 1.45, MY[0]), 1.0, BLUE),
            current_arrow(pt(MX[1] + 0.45, MY[0]), pt(MX[1] + 1.45, MY[0]), 1.0, BLUE),
            current_arrow(pt(MX[1] - 0.45, MY[1]), pt(MX[1] - 1.45, MY[1]), 1.0, BLUE),
            current_arrow(pt(MX[2] - 0.45, MY[1]), pt(MX[2] - 1.45, MY[1]), 1.0, BLUE),
            current_arrow(pt(MX[1], mid - 0.45), pt(MX[1], mid + 0.45), 1.0, BLUE),
            current_arrow(pt(MX[2], mid - 0.45), pt(MX[2], mid + 0.45), 1.0, BLUE),
        )
        spots = [
            pt(MX[0] + 0.95, MY[0] + 0.36),
            pt(MX[1] + 0.95, MY[0] + 0.36),
            pt(MX[1] - 0.95, MY[1] - 0.38),
            pt(MX[2] - 0.95, MY[1] - 0.38),
            pt(MX[1] - 0.44, mid),
            pt(MX[2] - 0.44, mid),
        ]
        labs = VGroup(*[
            MathTex(n, font_size=FS_LABEL, color=BLUE).move_to(s)
            for n, s in zip([r"i_1", r"i_2", r"i_3", r"i_4", r"i_5", r"i_6"], spots)
        ])
        return VGroup(lines, arrows, labs), lines, arrows, labs

    # ----------------------------------------------------------- 1 hook
    def beat_hook(self):
        self.next_beat("hook")
        self.set_heading(("a circuit with six unknowns", TEXT_DIM))

        mesh, lines, arrows, labs = self.make_mesh()
        self.mesh, self.mesh_labs = mesh, labs

        self.play_t(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.12), run_time=1.2)
        self.play_t(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.10), run_time=1.3)
        self.wait_t(0.5)
        self.play_t(LaggedStart(*[FadeIn(l, shift=0.1 * UP) for l in labs], lag_ratio=0.10),
                    run_time=1.2)
        # hold the tangle: the next beat clears it
        self.wait_t(0.8)

    # ----------------------------------------------------------- 2 build
    def beat_build(self):
        self.next_beat("build")
        # clearing happens here, so the hook's payoff held until its last frame
        self.play_t(FadeOut(self.mesh), run_time=0.6)

        self.set_heading(("one node", TEXT_DIM), ("·", GUIDE), ("one loop", TEXT_DIM))

        circuit, P = self.build_circuit()
        self.circuit, self.P = circuit, P

        wires = VGroup(P["left_rail"], P["top_left"], P["upper"], P["top_right"],
                       P["right_rail"], P["bot_right"], P["bot_left"],
                       P["drop_a"], P["lower"], P["rise_b"])
        comps = VGroup(P["r1"], P["r2"], P["r3"], P["bat"])
        self.flow = VGroup(P["f_left"], P["f_r1"], P["f_r2"], P["f_r3"])

        self.play_t(LaggedStart(*[Create(w) for w in wires], lag_ratio=0.06), run_time=1.5)
        self.wait_t(0.4)
        self.play_t(FadeIn(comps), run_time=0.6)
        self.wait_t(0.3)
        self.play_t(LaggedStart(*[GrowArrow(a) for a in self.flow], lag_ratio=0.15),
                    run_time=1.2)
        self.wait_t(0.3)
        self.play_t(Write(P["v_bat"]), Write(P["v_r1"]), Write(P["v_r2"]), Write(P["v_r3"]),
                    run_time=1.2)
        self.wait_t(0.3)
        self.play_t(FadeIn(P["a"]), FadeIn(P["b"]), Write(P["lbl_a"]), Write(P["lbl_b"]),
                    run_time=0.9)
        self.wait_t(0.4)

        self.loop_ring = wire(
            pt(BAT_X, YB), pt(X0, YB), pt(X0, YT), pt(XA, YT), pt(XA, YM),
            pt(XB, YM), pt(XB, YT), pt(X1, YT), pt(X1, YB), pt(BAT_X, YB),
            color=AUX, width=SW_GUIDE,
        )
        self.loop_lbl = label("a loop", 30, AUX).move_to(pt(0.30, YM + 0.52))
        self.play_t(Create(self.loop_ring), FadeIn(self.loop_lbl), run_time=1.0)
        self.wait_t(0.6)
        self.play_t(FadeOut(self.loop_ring, self.loop_lbl), run_time=0.5)
        self.wait_t(0.8)

    # ----------------------------------------------------------- 3 kcl
    def beat_kcl(self):
        self.next_beat("kcl")
        P = self.P
        self.set_heading(("KCL", EMPHASIS), ("—  the junction", TEXT_DIM))

        # the node dot is the star; the supporting values step back
        self.play_t(
            P["v_r1"].animate.set_opacity(0.22), P["v_r2"].animate.set_opacity(0.22),
            P["v_r3"].animate.set_opacity(0.22), P["v_bat"].animate.set_opacity(0.22),
            FadeOut(P["lbl_a"]), FadeOut(P["lbl_b"]),
            run_time=0.5,
        )
        zone = Circle(radius=0.88, color=EMPHASIS, stroke_width=SW_GUIDE)
        zone.move_to(pt(XA, YT))
        self.play_t(Create(zone), run_time=0.6)
        self.wait_t(0.4)
        self.play_t(Indicate(P["a"], color=EMPHASIS, scale_factor=1.7), run_time=0.7)

        # current values sit above the rail; component values are below it
        l_in = tag(r"1.5", (XA - 0.72, YT + 0.50), BLUE)
        l_r2 = tag(r"0.5", ((XA + R2X) / 2 - 0.12, YT + 0.50), SECONDARY)
        l_r3 = tag(r"1.0", (XA - 0.60, YM + 0.62), SECONDARY)
        self.cur_labels = VGroup(l_in, l_r2, l_r3)

        self.play_t(FadeIn(l_in, shift=0.15 * UP), run_time=0.6)
        self.wait_t(0.4)
        self.play_t(FadeIn(l_r2, shift=0.15 * UP), run_time=0.6)
        self.wait_t(0.3)
        self.play_t(FadeIn(l_r3, shift=0.15 * UP), run_time=0.6)
        self.wait_t(0.4)

        rule = MathTex(r"\sum I_{\text{in}} = \sum I_{\text{out}}", font_size=FS_MATH,
                       color=TEXT).move_to(pt(0, EQ_RULE))
        self.play_t(Write(rule), run_time=1.4)
        self.wait_t(0.6)

        num = MathTex(r"1.5 = 0.5 + 1.0", font_size=FS_MATH, color=RESULT)
        num.move_to(pt(0, EQ_NUM))
        self.play_t(Write(num), run_time=1.2)
        self.play_t(Indicate(num, color=RESULT, scale_factor=1.08), run_time=0.7)
        self.rule_kcl, self.num_kcl, self.zone_kcl = rule, num, zone

        # the same accounting holds at B
        self.play_t(Indicate(P["b"], color=EMPHASIS, scale_factor=1.7), run_time=0.9)
        self.wait_t(0.6)
        # hold the KCL payoff: the why-beat clears it

    # ----------------------------------------------------------- 4 kcl_why
    def beat_kcl_why(self):
        self.next_beat("kcl_why")
        self.play_t(FadeOut(self.flow, self.cur_labels, self.zone_kcl, self.num_kcl),
                    run_time=0.6)
        self.set_heading(("why?  ", TEXT_DIM), ("charge is conserved", GREEN))

        # discrete charge markers: the viewer counts them, rather than watching a fluid.
        # The chain starts clear of R1's symbol so no marker sits on a component.
        in_marks = [Dot(pt(XA - 1.05 + k * 0.26, YT), radius=0.075, color=BLUE)
                    for k in range(5)]
        out_r2 = [Dot(pt(XA + 0.36 + k * 0.30, YT), radius=0.075, color=SECONDARY)
                  for k in range(2)]
        out_r3 = [Dot(pt(XA, YT - 0.55 - k * 0.30), radius=0.075, color=SECONDARY)
                  for k in range(3)]
        grp = VGroup(*in_marks, *out_r2, *out_r3)

        self.play_t(LaggedStart(*[GrowFromCenter(m) for m in in_marks], lag_ratio=0.10),
                    run_time=1.0)
        self.wait_t(0.4)
        self.play_t(LaggedStart(*[GrowFromCenter(m) for m in out_r2 + out_r3], lag_ratio=0.10),
                    run_time=1.2)
        self.wait_t(0.4)
        self.play_t(Indicate(VGroup(*in_marks), color=BLUE, scale_factor=1.15), run_time=0.7)
        self.play_t(Indicate(VGroup(*out_r2, *out_r3), color=SECONDARY, scale_factor=1.15),
                    run_time=0.7)

        cap = label("charge cannot pile up at a point", 30, TEXT_DIM).move_to(pt(0, EQ_NUM))
        self.play_t(FadeIn(cap), run_time=0.7)
        self.wait_t(0.8)
        self.play_t(Transform(cap, label("charge is conserved", 34, GREEN)
                              .move_to(pt(0, EQ_NUM))), run_time=0.9)
        self.keep_charge = VGroup(cap, grp)
        # hold: rule + particles + takeaway, cleared by the KVL beat
        self.wait_t(1.2)

    # ----------------------------------------------------------- 5 kvl
    def beat_kvl(self):
        self.next_beat("kvl")
        P = self.P
        self.play_t(FadeOut(self.rule_kcl, self.keep_charge), run_time=0.6)
        self.set_heading(("KVL", EMPHASIS), ("—  the loop", TEXT_DIM))

        p_neg, p_pos = pt(BAT_X + 0.12, YB), pt(BAT_X - 0.12, YB)
        r1_l, r1_r = pt(R1X - R_W, YT), pt(R1X + R_W, YT)
        r3_l, r3_r = pt(R3X - R_W, YM), pt(R3X + R_W, YM)

        # the component values have done their job; the voltage tags replace them
        self.play_t(FadeOut(P["v_bat"], P["v_r1"], P["v_r2"], P["v_r3"]), run_time=0.5)

        marker = Dot(p_neg, radius=0.11, color=EMPHASIS)
        self.marker = marker
        self.play_t(FadeIn(marker), run_time=0.3)

        # Walk the loop in ordered chunks so each tag lands exactly on its
        # crossing, in step with the narration. linear: a continuous process.
        rise = tag(r"+12", (BAT_X - 0.95, YB - 0.42), GREEN)
        self.play_t(MoveAlongPath(marker, polyline([p_neg, p_pos])),
                    run_time=0.7, rate_func=linear)
        self.play_t(FadeIn(rise, shift=0.15 * UP), run_time=0.6)

        self.play_t(MoveAlongPath(marker, polyline(
            [p_pos, pt(X0, YB), pt(X0, YT), r1_l])), run_time=2.3, rate_func=linear)

        # tag sits below-left of R1, clear of the symbol and of the wire
        drop1 = tag(r"-6", (R1X + 0.70, YT - 0.62), CONTRAST)
        self.play_t(MoveAlongPath(marker, polyline([r1_l, r1_r])),
                    run_time=0.8, rate_func=linear)
        self.play_t(FadeIn(drop1, shift=0.15 * UP), run_time=0.6)

        self.play_t(MoveAlongPath(marker, polyline(
            [r1_r, pt(XA, YT), pt(XA, YM), r3_l])), run_time=1.9, rate_func=linear)

        drop2 = tag(r"-6", (R3X + 0.62, YM - 0.52), CONTRAST)
        self.play_t(MoveAlongPath(marker, polyline([r3_l, r3_r])),
                    run_time=0.8, rate_func=linear)
        self.play_t(FadeIn(drop2, shift=0.15 * UP), run_time=0.6)

        self.play_t(MoveAlongPath(marker, polyline([
            r3_r, pt(XB, YM), pt(XB, YT), pt(X1, YT), pt(X1, YB), p_neg,
        ])), run_time=2.4, rate_func=linear)

        num = MathTex(r"12 - 6 - 6 = 0", font_size=FS_MATH, color=RESULT)
        num.move_to(pt(0, EQ_NUM))
        self.play_t(Write(num), run_time=1.2)
        self.play_t(Indicate(num, color=RESULT, scale_factor=1.08), run_time=0.7)

        self.tags_kvl = VGroup(rise, drop1, drop2)
        self.num_kvl = num
        self.wait_t(0.4)
        # hold the closed loop with its zero sum

    # ----------------------------------------------------------- 6 kvl_why
    def beat_kvl_why(self):
        self.next_beat("kvl_why")
        self.play_t(FadeOut(self.circuit, self.tags_kvl, self.marker, self.num_kvl),
                    run_time=0.7)
        self.set_heading(("why?  ", TEXT_DIM), ("energy is conserved", GREEN))

        # potential as height: rise 12, drop 6, drop 6, home to zero.
        # Heights are proportional to the printed voltages. base/scale chosen so
        # the profile is vertically centred in the canvas zone (docs/layout-guidelines.md).
        base, scale = -1.55, 0.34
        xs = [-2.95, -2.25, -1.05, -0.35, 0.55, 1.25, 2.95]
        ys = [base, base + 12 * scale, base + 12 * scale,
              base + 6 * scale, base + 6 * scale, base, base]
        pts = [pt(x, y) for x, y in zip(xs, ys)]
        prof = wire(*pts, color=AUX, width=SW_PRIMARY)

        floor = DashedLine(pt(-3.00, base), pt(3.00, base), color=GUIDE,
                           stroke_width=SW_GUIDE, dash_length=0.14)
        zero = MathTex(r"0", font_size=FS_LABEL, color=TEXT_DIM).move_to(pt(-3.28, base))
        plus = MathTex(r"+12", font_size=FS_LABEL, color=GREEN).move_to(
            pt(-1.65, base + 12 * scale + 0.44))
        # each drop tag is offset clear of the edges it labels, in open space
        d1 = MathTex(r"-6", font_size=FS_LABEL, color=CONTRAST).move_to(pt(-3.15, -0.30))
        d2 = MathTex(r"-6", font_size=FS_LABEL, color=CONTRAST).move_to(pt(2.25, -0.30))

        self.play_t(Create(floor), FadeIn(zero), run_time=0.6)
        self.play_t(Create(prof), run_time=1.6)
        self.play_t(FadeIn(plus), run_time=0.5)
        self.play_t(FadeIn(d1), run_time=0.4)
        self.play_t(FadeIn(d2), run_time=0.4)

        walker = Dot(pts[0], radius=0.11, color=EMPHASIS)
        self.play_t(FadeIn(walker), run_time=0.3)
        self.play_t(MoveAlongPath(walker, polyline(pts)), run_time=2.8, rate_func=linear)

        note = label("every volt gained is spent", 30, TEXT_DIM).move_to(pt(0, base - 0.95))
        self.play_t(FadeIn(note), run_time=0.7)
        self.wait_t(0.8)
        # hold the profile with the walker home; the resolve beat clears it
        self.leaving = VGroup(prof, floor, zero, plus, d1, d2, walker, note)

    # ----------------------------------------------------------- 7 resolve
    def beat_resolve(self):
        self.next_beat("resolve")
        # clear the previous beat's stage — nothing may leak into the ending
        self.play_t(FadeOut(self.leaving), run_time=0.7)
        self.set_heading(("two conservation laws", TEXT_DIM))

        mesh, lines, arrows, labs = self.make_mesh()
        self.play_t(FadeIn(mesh), run_time=1.2)
        self.play_t(LaggedStart(*[Indicate(l, color=BLUE, scale_factor=1.4)
                                  for l in labs], lag_ratio=0.10), run_time=1.6)
        self.wait_t(0.8)

        # the two laws, each paired with the conservation principle it expresses
        kcl = VGroup(
            MathTex(r"\sum I = 0", font_size=FS_MATH, color=EMPHASIS),
            label("charge", 30, TEXT_DIM),
        ).arrange(DOWN, buff=0.30).move_to(pt(0, -1.60))

        kvl = VGroup(
            MathTex(r"\sum V = 0", font_size=FS_MATH, color=EMPHASIS),
            label("energy", 30, TEXT_DIM),
        ).arrange(DOWN, buff=0.30).move_to(pt(0, -3.60))

        self.play_t(Write(kcl[0]), run_time=1.0)
        self.play_t(FadeIn(kcl[1]), run_time=0.5)
        self.wait_t(0.7)
        self.play_t(Write(kvl[0]), run_time=1.0)
        self.play_t(FadeIn(kvl[1]), run_time=0.5)
        self.wait_t(0.5)
        # final hold on the two laws: nothing animates after the insight
