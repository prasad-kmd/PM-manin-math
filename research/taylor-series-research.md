# Research Notes — Taylor Series: Polynomials That Hug Smooth Curves

Target: 75–90 s, 9:16 FHD (`1080x1920`, 60 fps), `@prasadkmd`. Audience: general / undergraduate.
Style: Classic 3Blue1Brown conceptual clarity, aligned with the repository `/docs` design system.

## 1. Core Mathematical Idea & Intuition
- **The Problem / Hook**: Computers and calculators at the hardware level only perform basic arithmetic (addition, subtraction, multiplication, division). How do they evaluate transcendental functions like $\cos(x)$, $\sin(x)$, or $e^x$? They approximate smooth curves using polynomials.
- **Derivative Matching at an Anchor Point ($x = a$)**:
  - Suppose we want a polynomial $P(x) = c_0 + c_1 x + c_2 x^2 + c_3 x^3 + \cdots$ to mimic $f(x) = \cos(x)$ near $x = 0$.
  - **0th derivative (value/height)**: $P(0) = c_0 = \cos(0) = 1 \implies P_0(x) = 1$.
  - **1st derivative (slope/velocity)**: $P'(0) = c_1 = -\sin(0) = 0 \implies$ tangent line is flat; no $x$ term needed ($P_1(x) = 1$).
  - **2nd derivative (curvature/acceleration)**: $P''(x) = 2 c_2$. To match $\cos''(0) = -\cos(0) = -1$, we need $2 c_2 = -1 \implies c_2 = -\frac{1}{2}$. This yields the parabola $P_2(x) = 1 - \frac{x^2}{2}$, which bends at the exact same rate as $\cos(x)$ at $x = 0$.

## 2. Why the Factorial Denominator ($n!$)?
- When differentiating $x^n$ repeatedly $n$ times using the power rule:
  $$\frac{d^n}{dx^n}\left(x^n\right) = n \cdot (n-1) \cdot (n-2) \cdots 2 \cdot 1 = n!$$
- Meanwhile, lower-degree terms $x^k$ ($k < n$) vanish after $n$ derivatives, and higher-degree terms $x^k$ ($k > n$) still contain a factor of $x$ and vanish when evaluated at $x = 0$.
- Therefore, at $x = 0$, the $n$-th derivative of $P(x)$ isolates the $n$-th term:
  $$P^{(n)}(0) = n! \, c_n$$
- Setting $P^{(n)}(0) = f^{(n)}(0)$ forces:
  $$c_n = \frac{f^{(n)}(0)}{n!}$$
- Dividing by $n!$ explicitly cancels the power-rule cascade. Since $n!$ grows rapidly ($2! = 2, 4! = 24, 6! = 720, 8! = 40320$), higher-degree terms remain tiny near $x = 0$ (so they don't ruin the fit near the center) while taking over farther away to bend the polynomial back onto the curve.

## 3. Hugging the Curve Over a Wider Interval
- For $f(x) = \cos(x)$, the derivatives at $x = 0$ cycle every 4 steps: $(1, 0, -1, 0, 1, 0, -1, 0, \dots)$.
- Successive Taylor polynomials around $x = 0$ (Maclaurin polynomials):
  - $P_0(x) = 1$
  - $P_2(x) = 1 - \frac{x^2}{2!}$
  - $P_4(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!}$
  - $P_6(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!}$
  - $P_8(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!}$
  - $P_{10}(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - \frac{x^{10}}{10!}$
- Visually, as degree $2k$ increases from $0 \to 2 \to 4 \to 6 \to 8 \to 10$, the yellow polynomial curve peels off later and later, hugging the blue $\cos(x)$ wave across more oscillations.

## 4. General Formula & Radius of Convergence Caveat
- Centered at any anchor point $x = a$:
  $$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$$
- **Important Mathematical Distinction / Caveat** (per `mathematical-visualization.md`):
  - For analytic functions like $\cos(x)$, $\sin(x)$, and $e^x$, the Taylor series converges to $f(x)$ for **all** real $x$ (infinite radius of convergence $R = \infty$).
  - For other smooth functions like $f(x) = \frac{1}{1+x^2} = 1 - x^2 + x^4 - x^6 + \cdots$, the Taylor series centered at $0$ only converges inside a finite radius $|x| < 1$ (because of singularities at $x = \pm i$ in the complex plane).

## 5. Narrative Structure (75–90s, 9 Beats)
1. **hook (~7s)**: How calculators compute $\cos(x)$ using only addition and multiplication — faking curves with polynomials.
2. **setup (~9s)**: Plot $\cos(x)$ and anchor point $(0,1)$. Degree-0 constant approximation $P_0(x) = 1$.
3. **slope (~8s)**: Match 1st derivative at $x=0$: $\cos'(0) = 0 \implies c_1 = 0$, tangent stays flat.
4. **curvature (~11s)**: Match 2nd derivative at $x=0$: $\cos''(0) = -1 \implies P_2(x) = 1 - \frac{1}{2}x^2$ bends with the curve.
5. **factorial (~11s)**: Why $\frac{1}{2!}$, $\frac{1}{3!}$, $\frac{1}{n!}$? Power-rule cascade on $x^n$ pulls down $n!$; dividing by $n!$ cancels it.
6. **hug (~12s)**: Morph through $P_4(x), P_6(x), P_8(x), P_{10}(x)$ — watch the polynomial hug $\cos(x)$ over a wider and wider interval.
7. **formula (~9s)**: Reveal the full Taylor series $\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$ with color-coded roles.
8. **caveat (~9s)**: Contrast $\cos(x)$ ($R = \infty$) with $\frac{1}{1+x^2}$ where convergence stops at the barriers $x = \pm 1$.
9. **lesson (~8s)**: Takeaway — all derivatives at a single point encode the function's behavior far away.

## 6. Sources
- 3Blue1Brown (Grant Sanderson), *Essence of Calculus, Chapter 11: Taylor series* (2017): https://www.3blue1brown.com/lessons/taylor-series/
- Stewart, J., *Calculus: Early Transcendentals*, Section 11.10: Taylor and Maclaurin Series.
- Spivak, M., *Calculus*, Chapter 20: Approximation by Polynomial Functions (Taylor's Theorem and Remainder).
