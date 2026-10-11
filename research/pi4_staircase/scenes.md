# The π = 4 Staircase Paradox — Scene Plan

## Overview
- Topic: Limits of curves do not preserve arc length (staircase paradox, circle version)
- Hook: "Can π really equal four?"
- Audience: general / undergraduate
- Length: ~80 s (target 75–90 s), 9:16 FHD (1080×1920), 60 fps
- Style: classic 3Blue1Brown look (dark #1C1C1C, morphs, color-coded symbols)
  + city-block (taxicab) metaphor + Shorts-style punchy hook
- Key insight: a staircase measures length with |dx|+|dy| (taxicab), not √(dx²+dy²).
  The taxicab length of a diameter-1 circle is 4; the true length is π. 4 = π · (4/π).

## Color ledger
- WHITE: square (the setup), text
- BLUE #58C4DD: true circle, Euclidean (bird) length, π
- YELLOW #FFFF00: staircase, taxicab (taxi) length, "4"
- GREEN #83C167: |Δy| steps, final identity
- RED #FF6666: |Δx| steps, doubt marks
- GREY: grid (city blocks), brand

## Scenes (beats)
| # | Beat | Time (approx) | Visual | Learning purpose |
|---|------|------|--------|------------------|
| 1 | hook | 0–4 s | "π = 4?" punch, then shrinks to top title | Hook |
| 2 | setup | 4–11 s | Square side 1 wraps circle diameter 1; perimeter 1+1+1+1 = 4 | Establish the claim |
| 3 | fold | 11–21 s | Square → staircases n = 2, 4, 8 (steps per quarter); L_n = 4 stays | Show the fold; length constant |
| 4 | converge | 21–28 s | n = 16, 32; zoom into one corner | Shape converges (points get close) |
| 5 | paradox | 28–35 s | Staircase L = 4 vs circle π ≈ 3.14; red "?" | Contradiction |
| 6 | taxi_sibling | 35–47 s | Unit square: taxi on 4-block staircase (2) vs bird on diagonal (√2 ≈ 1.41) | Taxicab idea, simplest case |
| 7 | taxi_circle | 47–61 s | Taxi drives around circle staircase; Σ(|Δx|+|Δy|) = 4; zoom on one step | Compute taxicab length |
| 8 | resolution | 61–69 s | "4" (staircase) vs "π" (circle); π × 4/π = 4 | Resolve the paradox |
| 9 | lesson | 69–77 s | "Shapes can converge while lengths don't." | Takeaway |

## Narration (final text; durations are set from generated audio)
See `research/pi4_staircase/beats.json` (generated from narration.json after TTS).

## Accuracy checks
- Staircase perimeter for diameter 1 = 4 at every n (verified numerically).
- Taxicab length of diameter-1 circle = 4; Euclidean = π (verified numerically; ratio 4/π).
- Unit-square staircase = 2; diagonal = √2 (Wikipedia: Staircase paradox).

## Implementation
- Script: `scripts/pi4_staircase.py` (scene class `PiFourStaircase`)
- Beat timing: `research/pi4_staircase/beats.json`
- Output: `videos/pi4_staircase/1920p60/PiFourStaircase.mp4` → final mux with narration
