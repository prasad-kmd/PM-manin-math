# Taylor Series: Polynomials That Hug Curves — Scene Plan

## Overview
- **Topic**: Taylor Series & Maclaurin Polynomial Approximations
- **Hook**: "How does a calculator find $\cos(x)$ when all it can really do is add and multiply?"
- **Target Audience**: General / Undergraduates (familiar with basic derivatives)
- **Estimated Length**: ~82 seconds (target 75–90 s), 9:16 FHD (`1080×1920`, 60 fps)
- **Style**: Classic 3Blue1Brown visual storytelling aligned with `/docs/design-system.md` and `/docs/visual-theme.md`
- **Key Insight**: Matching derivatives of order $0, 1, 2, \dots, n$ at a single point $x = a$ forces coefficients $c_n = f^{(n)}(a)/n!$, making the polynomial hug the curve over a progressively wider interval.

## Color & Symbol Ledger (`/docs/visual-theme.md`)
- `BG` (`#000000`): Pure black background
- `TEXT_PRIMARY` (`#F2F2F2`): Main equations, titles, primary labels
- `TEXT_SECONDARY` (`#B8B8B8`): Supporting notes, secondary labels, `@prasadkmd` watermark
- `GUIDE` (`#666666`): Coordinate axes, tick marks, dashed boundary guides
- `BLUE` (`#4EA5FF`): Target smooth function $f(x) = \cos(x)$
- `YELLOW` (`#FFD166`): Taylor polynomial $P_n(x)$ and key results
- `TEAL` (`#4ECDC4`): First derivative / slope matching
- `GREEN` (`#7BD88F`): Second derivative / curvature & factorial cancellation ($n!$)
- `CORAL` (`#FF6B6B`): Error / divergence barrier ($x = \pm 1$ for $1/(1+x^2)$)
- `PURPLE` (`#B69CFF`): Anchor point $x = a$ / $(0, 1)$

## Beat-by-Beat Storyboard

| # | Beat | Approx. Time | Visual State & Manim Action | Learning Purpose |
|---|---|---|---|---|
| 1 | `hook` | 0–7 s | Question $\cos(x) = \text{?}$ transforms into a polynomial $c_0 + c_1 x + c_2 x^2 + \cdots$ while a yellow curve morphs onto a blue cosine wave. Shrinks to top header. | Motivate Taylor polynomials via how calculators compute smooth functions. |
| 2 | `setup` | 7–16 s | Clean axes in upper-middle canvas; plot blue $\cos(x)$ on $[-2\pi, 2\pi]$; highlight purple anchor dot at $(0,1)$; draw horizontal yellow line $P_0(x) = 1$. | Match the 0th derivative (function value) at $x = 0$. |
| 3 | `slope` | 16–24 s | Show tangent indicator at $(0,1)$; display $f'(0) = -\sin(0) = 0$ in teal; add $+ 0\cdot x$ and collapse back to $P_1(x) = 1$. | Match the 1st derivative (slope) at $x = 0$. |
| 4 | `curvature` | 24–35 s | Show $f''(0) = -\cos(0) = -1$ in green; morph flat line $P_0(x)=1$ into downward parabola $P_2(x) = 1 - \frac{1}{2}x^2$ hugging the peak of $\cos(x)$. | Match the 2nd derivative (rate of bending) at $x = 0$. |
| 5 | `factorial` | 35–46 s | Focus on why $\frac{1}{n!}$ appears: animate power-rule cascade on $x^n \to n x^{n-1} \to \cdots \to n!$ and show dividing by $n!$ cancels the $n!$ factor. | Explain the mechanism behind the factorial denominator. |
| 6 | `hug` | 46–58 s | Smoothly transform $P_2(x) \to P_4(x) \to P_6(x) \to P_8(x) \to P_{10}(x)$ while updating the polynomial terms below and expanding a green interval bar showing where the curve is hugged. | Visually demonstrate how adding terms widens the interval of accurate approximation. |
| 7 | `formula` | 58–67 s | Transition to the general Taylor series formula $\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$ with callout labels for $f^{(n)}(a)$ (derivatives), $n!$ (factorial cancellation), and $(x-a)^n$ (distance from anchor). | Synthesize the concrete pattern into the general Taylor series formula. |
| 8 | `caveat` | 67–76 s | Show $f(x) = \frac{1}{1+x^2}$ (blue) vs its degree-10 Taylor polynomial (yellow) with coral dashed walls at $x = \pm 1$, showing accurate fit inside $(-1, 1)$ and steep divergence outside. | Clarify mathematical integrity: Taylor polynomials only hug within the radius of convergence. |
| 9 | `lesson` | 76–84 s | Return to the high-order polynomial hugging $\cos(x)$ from the anchor dot $(0,1)$ outward, with the closing takeaway statement. | Leave viewers with the core conceptual insight. |
