"""
Build the final Taylor Series video: mux narration at the real beat start times
(from research/taylor_series/timeline.json) and write SRT captions.

Usage (after the Manim render):
  python3 scripts/build_taylor_series.py
"""
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "research", "taylor_series")
VID_IN = os.path.join(ROOT, "videos", "taylor_series", "1920p60", "TaylorSeries.mp4")
OUT_DIR = os.path.join(ROOT, "videos", "taylor_series")
VID_OUT = os.path.join(OUT_DIR, "taylor_series_final_1080x1920.mp4")
SRT_OUT = os.path.join(OUT_DIR, "taylor_series_captions.srt")

beats = json.load(open(os.path.join(RES, "beats.json")))
timeline = {b["beat"]: b for b in json.load(open(os.path.join(RES, "timeline.json")))["beats"]}
narr = {b["name"]: b["text"] for b in json.load(open(os.path.join(RES, "narration.json")))}

inputs, filters, labels = ["-i", VID_IN], [], []
for i, b in enumerate(beats):
    start_ms = int(round(timeline[b["name"]]["start"] * 1000)) + 250  # 250ms visual lead-in
    inputs += ["-i", os.path.join(RES, b["audio"])]
    filters.append(f"[{i+1}:a]adelay={start_ms}:all=1,volume=1.0[a{i}]")
    labels.append(f"[a{i}]")
filters.append("".join(labels) + f"amix=inputs={len(beats)}:normalize=0:duration=longest[aout]")

cmd = [
    "ffmpeg", "-y", "-v", "error", *inputs,
    "-filter_complex", ";".join(filters),
    "-map", "0:v", "-map", "[aout]",
    "-c:v", "libx264", "-preset", "slow", "-crf", "18",
    "-pix_fmt", "yuv420p", "-r", "60",
    "-c:a", "aac", "-b:a", "192k",
    "-movflags", "+faststart", VID_OUT
]
subprocess.run(cmd, check=True)


def ts(sec):
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",")


with open(SRT_OUT, "w") as f:
    for i, b in enumerate(beats, 1):
        s = timeline[b["name"]]["start"] + 0.25
        e = s + b["audio_dur"]
        f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{narr[b['name']]}\n\n")

print("wrote", VID_OUT, "and", SRT_OUT)
