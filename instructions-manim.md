# Manim Workspace Setup Instructions

This document describes exactly how this Manim Community Edition workspace was set up, so you can reproduce it on another AI agent / container / VM.

---

## 1. Environment Overview

- **OS:** Debian trixie (tested in e2b sandbox, works on Ubuntu/Debian)
- **Python:** 3.13.16 (any 3.10+ works)
- **Manim:** Community Edition v0.22.0 (latest stable as of Oct 2026)
- **Key system deps:** `ffmpeg`, `cairo`, `pango`, `latex` + `dvisvgm`
- **Final check:** `manim checkhealth` must show 4 PASSED

Tested final output:
```
- Checking whether manim is on your PATH ... PASSED
- Checking whether the executable belongs to manim ... PASSED
- Checking whether latex is available ... PASSED
- Checking whether dvisvgm is available ... PASSED
```

---

## 2. System Dependencies

### 2.1 Check existing tools
```bash
python3 --version
pip3 --version
which ffmpeg; ffmpeg -version | head -n 5
apt list --installed | grep -E "cairo|pango|ffmpeg"
```

### 2.2 Install ffmpeg (requires sudo in this sandbox)
```bash
# If apt lock error, use sudo
sudo apt-get update
sudo apt-get install -y ffmpeg
which ffmpeg
```

In this environment we needed sudo. The install pulled ~140 packages (319 MB) including libavcodec, etc.

### 2.3 Install LaTeX + dvisvgm for MathTex
Manim needs LaTeX for `Tex` and `MathTex`. Minimal set:

```bash
# First attempt - base + recommended (378 MB)
sudo apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-latex-recommended dvisvgm

# Check
manim checkhealth
```

**Troubleshooting:**
- On first try we got hash mismatch for texlive-base:
  `E: Failed to fetch ... texlive-base ... Hash Sum mismatch`
- Fix: `sudo apt-get update && sudo apt-get install -y --fix-missing ...`

After base install, `latex` and `dvisvgm` PASSED, but rendering MathTex still failed with:
```
! LaTeX Error: File `standalone.cls' not found.
```
Solution: need extra packages:

```bash
# Adds standalone.cls and many fonts (981 MB, may need --fix-missing)
sudo apt-get install -y texlive-latex-extra texlive-fonts-extra
# Or retry with:
sudo apt-get update && sudo apt-get install -y --fix-missing texlive-latex-extra texlive-fonts-extra

# Verify
kpsewhich standalone.cls
# Should return: /usr/share/texlive/texmf-dist/tex/latex/standalone/standalone.cls
```

Full LaTeX stack installed here was ~1GB.

---

## 3. Python Dependencies

### 3.1 Install Manim
```bash
python3 -m pip install manim --quiet
manim --version
# Manim Community v0.22.0
```

### 3.2 Optional requirements.txt
Create `requirements.txt`:
```
manim==0.22.0
numpy
```

Install:
```bash
pip install -r requirements.txt
```

---

## 4. Manim Configuration

### 4.1 Minimal manim.cfg
We initially created a cfg with `quality = medium` which failed (expects `medium_quality`). Fixed to minimal working config:

```ini
# manim.cfg
[CLI]
preview = False
verbosity = INFO
media_dir = ./media
log_dir = ./media/logs
```

Manim will use defaults for rest:
- `video_dir = {media_dir}/videos/{module_name}/{quality}`
- `tex_dir = {media_dir}/Tex`
- etc.

Reference default.cfg:
```bash
cat /usr/local/lib/python3.13/site-packages/manim/_config/default.cfg | head -n 100
```

### 4.2 Workspace Structure
```
/home/user/
├── main.py                 # Example scenes
├── template.py             # Starter templates
├── shorts_derivative.py    # Vertical 9:16 example
├── manim.cfg               # Config
├── quick_render.sh         # Helper script
├── requirements.txt
├── media/                  # Generated (gitignore)
│   ├── videos/
│   ├── Tex/
│   ├── texts/
│   └── logs/
├── README.md
└── instructions-manim.md   # This file
```

### 4.3 Example Scenes (main.py)
We created 4 test scenes to verify everything:
- `CircleToSquare` - basic shape morph (no LaTeX)
- `MathEquation` - LaTeX test with MathTex
- `SineWave` - Axes + plot
- `MatrixTransformation` - linear algebra

Test them:
```bash
manim -ql main.py CircleToSquare
manim -ql main.py MathEquation
manim -ql -a main.py   # all scenes
```

If all 4 render to `media/videos/main/480p15/*.mp4`, setup is good.

---

## 5. Vertical Video (YouTube Shorts / Reels) Setup

For 9:16 vertical, configure at top of Python file:

```python
from manim import *

config.background_color = "#1e1e1e"
config.frame_width = 8.0
config.frame_height = 14.22
config.pixel_width = 1080
config.pixel_height = 1920
```

Then render with explicit resolution override:

```bash
# Low quality fast test (15fps)
manim -ql -r 1080,1920 shorts_derivative.py ShortsMathScene

# Final high quality 60fps
manim -qh --fps 60 -r 1080,1920 shorts_derivative.py ShortsMathScene
```

Result: `media/videos/shorts_derivative/1920p60/ShortsMathScene.mp4`
- Verified: 1080x1920, 60fps, 22.6s, h264

Key design for vertical:
- Move Axes to upper 2/3: `axes.move_to(UP*1.2)`
- Title at top edge: `Text(...).to_edge(UP, buff=0.8)`
- Equation at bottom: `MathTex(...).next_to(axes, DOWN, buff=0.9)`
- Leave safe margins for platform UI

---

## 6. Skills Installation (Manim-Specific Agent Skills)

We added two community skills using `skills` CLI (https://skills.sh):

### 6.1 Check Node / npx
```bash
node --version  # v20.20.2
npm --version   # 10.8.2
npx --version
npx skills --help
```

### 6.2 Add manim-explainer-animation skill
Source: https://github.com/calesthio/generative-media-skills
Skill: `manim-explainer-animation`

```bash
npx skills add https://github.com/calesthio/generative-media-skills --skill manim-explainer-animation -y -a '*'
```

- `-y` = skip confirmation prompts
- `-a '*'` = install to all 73 supported agents
- Installs to:
  - Global: `~/.agents/skills/manim-explainer-animation/`
  - Project: `.agents/skills/manim-explainer-animation/` and `.claude/skills/manim-explainer-animation/`
  - Tracked in `skills-lock.json`

Skill description: Production workflow for Manim explainer animations (storyboard, scene architecture, formulas, coordinate systems, voiceover timing, accessibility, etc.)

### 6.3 Add manim-composer skill
Source: https://github.com/adithya-s-k/manim_skill
Skill: `manim-composer`

```bash
npx skills add https://github.com/adithya-s-k/manim_skill --skill manim-composer -y -a '*'
```

Skill description: Transforms vague video ideas into detailed scene-by-scene plans (scenes.md). Conducts research, asks clarifying questions, outputs comprehensive specs ready for ManimCE.

### 6.4 Verify Installation
```bash
ls -R ~/.agents/skills
ls -R .agents/skills
ls -R .claude/skills
cat skills-lock.json
npx skills list --json
npx skills list -g --json
```

Expected `skills-lock.json`:
```json
{
  "version": 1,
  "skills": {
    "manim-composer": {
      "source": "adithya-s-k/manim_skill",
      "sourceType": "github",
      "skillPath": "skills/manim-composer/SKILL.md"
    },
    "manim-explainer-animation": {
      "source": "calesthio/generative-media-skills",
      "sourceType": "github",
      "skillPath": "skills/production/runtime-assembly/manim-explainer-animation/SKILL.md"
    }
  }
}
```

---

## 7. Helper Scripts

### quick_render.sh
```bash
#!/bin/bash
FILE=${1:-main.py}
SCENE=${2:-CircleToSquare}
QUALITY=${3:-l}
case $QUALITY in
  l) QUALITY_FLAG="-ql" ;;
  m) QUALITY_FLAG="-qm" ;;
  h) QUALITY_FLAG="-qh" ;;
  k) QUALITY_FLAG="-qk" ;;
  *) QUALITY_FLAG="-ql" ;;
esac
manim $QUALITY_FLAG $FILE $SCENE
```

Usage:
```bash
chmod +x quick_render.sh
./quick_render.sh main.py CircleToSquare l
./quick_render.sh shorts_derivative.py ShortsMathScene h
```

---

## 8. Full Setup Script (One-Shot for New Agent)

For a fresh Debian/Ubuntu container, run this sequence:

```bash
# 1. System update + ffmpeg
sudo apt-get update
sudo apt-get install -y ffmpeg

# 2. LaTeX (may need --fix-missing on hash mismatch)
sudo apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-latex-recommended dvisvgm
sudo apt-get install -y texlive-latex-extra texlive-fonts-extra || sudo apt-get install -y --fix-missing texlive-latex-extra texlive-fonts-extra

# 3. Python deps
pip install manim==0.22.0

# 4. Verify
manim checkhealth
# Should show 4 PASSED

# 5. Create minimal manim.cfg
cat > manim.cfg << 'EOF'
[CLI]
preview = False
verbosity = INFO
media_dir = ./media
log_dir = ./media/logs
EOF

# 6. Test render (create a test file first)
cat > test.py << 'PY'
from manim import *
class Test(Scene):
    def construct(self):
        self.play(Create(Circle()))
PY
manim -ql test.py Test

# 7. Install skills (requires Node 20+)
npx skills add https://github.com/calesthio/generative-media-skills --skill manim-explainer-animation -y -a '*'
npx skills add https://github.com/adithya-s-k/manim_skill --skill manim-composer -y -a '*'
npx skills list -g --json

# 8. Done - ready for vertical renders
# manim -qh --fps 60 -r 1080,1920 your_file.py YourScene
```

---

## 9. Troubleshooting

| Issue | Symptom | Fix |
|-------|---------|-----|
| **ffmpeg missing** | `FileNotFoundError: ffmpeg` | `sudo apt-get install -y ffmpeg` |
| **latex not found** | `checkhealth FAILED latex` | Install texlive base packages |
| **standalone.cls not found** | `LaTeX Error: File standalone.cls not found` | `sudo apt-get install -y texlive-latex-extra` |
| **Hash Sum mismatch** | `E: Failed to fetch texlive-base Hash Sum mismatch` | `sudo apt-get update && sudo apt-get install -y --fix-missing <pkg>` |
| **quality KeyError** | `KeyError: quality must be one of [...]` | Use `low_quality` etc. or remove quality from cfg; use CLI flags `-ql/-qm/-qh` |
| **Text font issues** | Text not rendering | Use default font or install fonts; Text uses Pango, usually works |
| **Vertical cropped** | 16:9 instead of 9:16 | Must set both `config.frame_height` and render with `-r 1080,1920` |
| **Skills interactive prompt** | Stuck at agent selection | Use `-y -a '*'` flags |

---

## 10. References

- Manim Community Docs: https://docs.manim.community/
- Installation: https://docs.manim.community/en/stable/installation.html
- Config Guide: https://docs.manim.community/en/stable/guides/configuration.html
- Manim GitHub: https://github.com/ManimCommunity/manim
- Skills Registry: https://skills.sh/
- manim-explainer-animation skill: https://github.com/calesthio/generative-media-skills
- manim-composer skill: https://github.com/adithya-s-k/manim_skill
- Vertical video example in this workspace: `shorts_derivative.py` -> `ShortsMathScene`

---

## 11. What Was Built in This Workspace

- ✅ Full Manim 0.22.0 environment with LaTeX
- ✅ 4 example scenes (main.py) + templates
- ✅ Vertical 9:16 derivative intuition video (1080x1920, 60fps, 22.6s) demonstrating secant → tangent
- ✅ 2 agent skills installed globally and project-level
- ✅ Documentation (README.md, this file)

You can now create any mathematical animation with `manim -qh --fps 60 -r 1080,1920 file.py Scene`.
