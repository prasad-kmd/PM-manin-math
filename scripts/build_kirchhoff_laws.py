"""
Build the final Kirchhoff's Laws video: mux narration at the real beat start
times (from research/kirchhoff_laws/timeline.json) and write the SRT captions.

Usage (after the Manim render):
  python3 scripts/build_kirchhoff_laws.py

Follows the same convention as build_pi4_staircase.py so the pipeline stays
consistent: each clip is delayed to its beat start with a small lead-in, the
result is transcoded to H.264/AAC with faststart, and an .srt whose text
matches the narration exactly is written alongside.
"""
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "research", "kirchhoff_laws")
VID_IN = os.path.join(ROOT, "videos", "kirchhoff_laws", "1920p60", "KirchhoffLaws.mp4")
OUT_DIR = os.path.join(ROOT, "videos", "kirchhoff_laws")
VID_OUT = os.path.join(OUT_DIR, "kirchhoff_laws_final_1080x1920.mp4")
SRT_OUT = os.path.join(OUT_DIR, "kirchhoff_laws_captions.srt")

LEAD_IN = 0.3  # voice starts just after the visual cut, so visuals lead slightly

beats = json.load(open(os.path.join(RES, "beats.json")))
timeline = {b["beat"]: b for b in
            json.load(open(os.path.join(RES, "timeline.json")))["beats"]}

inputs, filters, labels, starts = ["-i", VID_IN], [], [], {}
for i, b in enumerate(beats):
    name = b["name"]
    start = timeline[name]["start"] + LEAD_IN
    starts[name] = start
    inputs += ["-i", os.path.join(RES, b["audio"])]
    filters.append(f"[{i+1}:a]adelay={int(round(start * 1000))}:all=1,volume=1.0[a{i}]")
    labels.append(f"[a{i}]")

# mix the delayed clips, then pad with silence to the exact video length so the
# audio track spans the whole video (whole_dur is finite: an unbounded apad would
# stream forever and get the process killed), then normalise loudness.
# docs/additional/video-design.md specifies a final mix around -14 LUFS; the raw
# TTS mix sits near -19.4 LUFS, so loudnorm brings it into spec and the TP ceiling
# keeps the gain from clipping.
total = float(json.load(open(os.path.join(RES, "timeline.json")))["total"])
filters.append("".join(labels) +
               f"amix=inputs={len(beats)}:normalize=0:duration=longest[aout]")
filters.append(f"[aout]apad=whole_dur={total}[apadout]")
filters.append("[apadout]loudnorm=I=-14:TP=-1.5:LRA=11[a2]")

cmd = ["ffmpeg", "-y", "-v", "error", *inputs,
       "-filter_complex", ";".join(filters),
       "-map", "0:v", "-map", "[a2]",
       "-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-pix_fmt", "yuv420p", "-r", "60",
       "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
       "-movflags", "+faststart", VID_OUT]
subprocess.run(cmd, check=True)


def ts(sec):
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",")


with open(SRT_OUT, "w") as f:
    for i, b in enumerate(beats, 1):
        s = starts[b["name"]]
        e = s + b["audio_dur"]
        # caption text is the narration verbatim, so .srt and audio agree
        f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{b['text']}\n\n")

print("wrote", VID_OUT)
print("wrote", SRT_OUT)
print("beats:", len(beats))
