# Kirchhoff's Laws — Titles, Description, Hashtags

## Titles (pick one)

**Recommended — hook + payoff, 70 chars**
> Kirchhoff's Laws: why current and voltage always balance

**Alternatives**

| Style | Title | Chars |
|---|---|---|
| Question hook | Why does current always balance at a junction? | 46 |
| Two-laws framing | The two rules that solve any circuit — and why they're true | 59 |
| Conservation angle | Kirchhoff's laws are just conservation in disguise | 50 |
| Short/punchy | Kirchhoff's laws, explained in 90 seconds | 40 |
| Intrigue | The two laws hiding inside every circuit | 42 |

For YouTube Shorts the first ~40 characters are what viewers see in the feed, so
front-load the concept: prefer the recommended title or the question hook.

## Description

> Kirchhoff's current law says the current arriving at a node equals the current
> leaving it. Kirchhoff's voltage law says the voltages around any closed loop sum
> to zero. They are the two rules behind all circuit analysis — and neither is an
> arbitrary formula.
>
> In this video we take one circuit with a 12 V battery, a 4 Ω resistor, and a 12 Ω
> and 6 Ω branch in parallel, and use it to see both rules happen. Watch the current
> split at a node and stay balanced. Watch a loop's rises and drops cancel exactly.
> Then see why: the current law is conservation of charge, and the voltage law is
> conservation of energy. Change the components and the same two laws still hold —
> that is what makes them laws, not shortcuts.
>
> Timestamps
> 0:00  Six unknown currents, two rules
> 0:06  The circuit, the node, and the loop
> 0:19  KCL — the junction
> 0:35  Why: charge is conserved
> 0:48  KVL — the loop
> 1:03  Why: energy is conserved
> 1:14  Two conservation laws
>
> Background assumed: you have met current, voltage and resistance. No calculus.
>
> The drawings are schematic, not to scale — the printed values carry the numbers.
> For DC and low frequencies. Animated with Manim Community Edition.

## Hashtags

Vary the sets between uploads rather than posting an identical block every time.

**Primary set (10)**
```
#kirchhoff #circuits #physics #electronics #electricalengineering #KCL #KVL #mathematics #manim #shorts
```

**Shorts/algorithm set**
```
#shorts #physics #circuitanalysis #ohmslaw #voltage #current #stem #maths #engineering #learnphysics
```

**Concept-led set**
```
#conservationofcharge #conservationofenergy #NodalAnalysis #MeshAnalysis #DCcircuits #physicstutor #stemeducation #3blue1brown #mathanimation #sciencetok
```

Notes on tag choice: `#KCL` and `#KVL` are the topical abbreviations students
actually search. `#manim` and `#3blue1brown` reach the animation/maths audience,
not the circuits audience — worth one slot each, not more. `#sciencetok` and
`#physicstok` are TikTok-native, so drop them if the upload targets YouTube only.

## Platform notes

- **Runtime** 86 s — fits YouTube Shorts (3 min limit) and Reels.
- **Format** 1080×1920, 60 fps, H.264 + AAC.
- Upload `kirchhoff_laws_final_1080x1920.mp4`; attach `kirchhoff_laws_captions.srt`
  as a caption track. The `.srt` text is the narration verbatim.
- No burned-in subtitles are present, so the caption file is the only subtitle
  source — if the target platform does not accept sidecar `.srt`, burn them in
  from `kirchhoff_laws_captions.srt` before uploading.
- The video is silent for the last ~1.3 s so the closing frame can be read.

## Accuracy statement (for a pinned comment or reply)

Both laws are exact for DC circuits and for AC at frequencies where the circuit is
small compared with the wavelength. They come from the lumped-element model: KVL
assumes the magnetic flux through the loop is contained inside the components, and
the classical `∇·J = 0` form of KCL neglects displacement current. Deliberately not
raised in the video — it would cost a scene at 86 s — but it is the honest caveat if
someone asks.
