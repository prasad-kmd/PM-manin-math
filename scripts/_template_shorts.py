"""
Starter template — 9:16 vertical FHD explainer (YouTube Shorts / Reels).
Branding: @prasadkmd

Render (final):
  manim -qh --fps 60 -r 1080,1920 scripts/<file>.py <SceneName>
Output: videos/<file>/1920p60/<SceneName>.mp4
"""
from manim import *

# ---- Format (FHD 9:16) -------------------------------------------------
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8.0
config.frame_height = 14.22

# ---- Palette / branding ------------------------------------------------
config.background_color = "#0F1115"
FG = "#F6F7FB"
MUTED = "#8A93A6"
ACCENT = "#FFD166"   # finite change / highlight
BLUE = "#4CC9F0"     # primary objects
GREEN = "#80ED99"    # results
HANDLE = "@prasadkmd"


class ShortsTemplate(Scene):
    def construct(self):
        title = Text("Title goes here", font_size=40, color=FG).to_edge(UP, buff=0.9)
        handle = Text(HANDLE, font_size=26, color=MUTED).to_edge(DOWN, buff=0.6)
        self.play(Write(title))
        self.play(FadeIn(handle))
        self.wait(1)
