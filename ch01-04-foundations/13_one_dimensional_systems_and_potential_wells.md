# 13. One-Dimensional Systems & Potential Wells

**Foundational Story**: Chapter 4, Section 4.6  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 135–142)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 13 & Ch. 14
* Morin, *Introduction to Classical Mechanics*, Ch. 4

---

## 1. The Power of the 1D Energy Equation

In one dimension, Newton's Second Law is a second-order ODE (Taylor, Eq. 4.14):

$$
m \ddot{x} = F(x)
$$

Because any 1D position-dependent force $F(x)$ is automatically conservative (its curl is trivially zero!), we can always define the potential energy (Taylor, Eq. 4.12):

$$
U(x) = - \int_{x_0}^x F(x')\,dx' \implies F(x) = -\frac{dU}{dx}
$$

Conservation of energy gives a first-order differential equation (Taylor, Eq. 4.13):

$$
E = \frac{1}{2} m \dot{x}^2 + U(x) = \text{constant}
$$

Solve directly for the velocity $\dot{x}$ (Taylor, Eq. 4.17):

$$
\dot{x} = \pm \sqrt{\frac{2}{m} [E - U(x)]}
$$

Separate variables (Taylor, Eq. 4.19):

$$
t = \int_{x_0}^x \frac{dx'}{\sqrt{\frac{2}{m} [E - U(x')]}}
$$

> **Taylor's Principle of 1D Mechanics (Sec. 4.3)**:  
> **Any 1D conservative problem can be completely solved by a single quadrature (integral)!**

---

## 2. Reading Energy Diagrams Like a Map

One of the most essential skills in intermediate mechanics is extracting the qualitative behavior of a system directly from a plot of $U(x)$ vs. $x$ without solving any integrals.

### 1. Allowed vs. Forbidden Regions
* Because kinetic energy $T = \frac{1}{2} m v^2 \ge 0$, total energy must satisfy:

$$
E \ge U(x)
$$

* **Classically Allowed Region**: Where $E \ge U(x)$. The particle can move here. Its speed is $v = \sqrt{\frac{2(E - U)}{m}}$.
* **Classically Forbidden Region**: Where $E < U(x)$. The particle can never enter here in classical mechanics (kinetic energy cannot be negative).

### 2. Turning Points
The boundary points $x_1$ and $x_2$ where $E = U(x)$ are called **Turning Points**:
* At these points, $T = 0$, so the speed is instantaneously zero ($v = 0$).
* The force $F = -\frac{dU}{dx}$ accelerates the particle back into the allowed region, causing it to reverse direction.

---

## 3. Equilibrium Classifications

An **equilibrium point** occurs wherever the net force is zero:

$$
F(x_0) = 0 \iff \left. \frac{dU}{dx} \right|_{x_0} = 0
$$

To determine stability, Taylor-expand $U(x)$ in a small displacement $u = x - x_0$:

$$
U(x) = U(x_0) + U'(x_0) u + \frac{1}{2} U''(x_0) u^2 + \mathcal{O}(u^3)
$$

Since $U'(x_0) = 0$:

$$
U(x) \approx U(x_0) + \frac{1}{2} k_{\text{eff}} u^2 \quad \text{where } k_{\text{eff}} = \left. \frac{d^2U}{dx^2} \right|_{x_0}
$$

1. **Stable Equilibrium ($\frac{d^2U}{dx^2} > 0$)**: Local minimum (valley bottom). Small displacements experience a restoring force $F = -k_{\text{eff}} u$. The particle oscillates around $x_0$.
2. **Unstable Equilibrium ($\frac{d^2U}{dx^2} < 0$)**: Local maximum (hilltop peak). Small displacements experience a repelling force pushing the particle away.
3. **Neutral Equilibrium ($\frac{d^2U}{dx^2} = 0$)**: Flat region. No restoring force exists to second order.

---

## 4. Small Oscillations About Stable Equilibrium

For any smooth potential well near a stable minimum $x_0$, the restoring force is linear:

$$
F = -\frac{dU}{dx} \approx -k_{\text{eff}} (x - x_0)
$$

Newton's Second Law becomes (Taylor, Eq. 5.3):

$$
m \ddot{u} = -k_{\text{eff}} u \implies \ddot{u} + \left(\frac{k_{\text{eff}}}{m}\right) u = 0
$$

> **The Universal Harmonic Approximation**:  
> **Every smooth system near a stable equilibrium executes Simple Harmonic Motion (SHM)!**  
> The natural angular frequency is given by:
> 
> $$
> \omega_0 = \sqrt{\frac{k_{\text{eff}}}{m}} = \sqrt{\frac{1}{m} \left. \frac{d^2U}{dx^2} \right|_{x_0}}
> $$
> 
> This is why harmonic oscillators dominate all of physics: from molecular vibrations to acoustic phonons in solids.

---

## 5. Summary Cheat Sheet for Module 13

| Feature | Equation / Criterion | Physical Interpretation |
|---|---|---|
| **1D Velocity** | $v(x) = \pm \sqrt{\frac{2}{m}(E - U(x))}$ | Determined entirely by potential gap $E - U$ |
| **Turning Points** | $E = U(x)$ | Particle stops ($v = 0$) and reverses direction |
| **Equilibrium** | $\frac{dU}{dx} = 0$ | Net force is zero |
| **Stable Minimum** | $\frac{d^2U}{dx^2} > 0$ | Valley; executes harmonic oscillations |
| **Natural Frequency** | $\omega_0 = \sqrt{\frac{1}{m}\frac{d^2U}{dx^2}}$ | Small oscillation frequency about any minimum |

---

## 6. Worked Examples & Practice Problems

### Worked Example 13.1: The Lennard-Jones Interatomic Potential
**Problem**: The interaction potential between two neutral noble gas atoms (such as Argon) is modeled by the **Lennard-Jones (6-12) Potential**:

$$
U(r) = U_0 \left[ \left(\frac{r_0}{r}\right)^{12} - 2 \left(\frac{r_0}{r}\right)^6 \right]
$$

where $U_0$ and $r_0$ are positive constants.  
(a) Find the equilibrium separation distance $r_{\text{eq}}$ where the net force is zero.  
(b) What is the binding energy (the depth of the potential well at equilibrium)?  
(c) Find the effective spring constant $k_{\text{eff}}$ and the frequency $\omega_0$ of small oscillations for an atom of mass $m$ vibrating about equilibrium.

**Solution**:  
(a) **Equilibrium Separation**:  
Equilibrium occurs where force vanishes: $F(r) = -\frac{dU}{dr} = 0$.

$$
\frac{dU}{dr} = U_0 \left[ -12 \frac{r_0^{12}}{r^{13}} + 12 \frac{r_0^6}{r^7} \right] = \frac{12 U_0}{r} \left[ -\left(\frac{r_0}{r}\right)^{12} + \left(\frac{r_0}{r}\right)^6 \right]
$$

Setting $\frac{dU}{dr} = 0$:

$$
\left(\frac{r_0}{r}\right)^{12} = \left(\frac{r_0}{r}\right)^6 \implies \left(\frac{r_0}{r}\right)^6 = 1 \implies r_{\text{eq}} = r_0
$$

(b) **Well Depth (Binding Energy)**:  
Evaluate $U(r_0)$:

$$
U(r_0) = U_0 [ 1 - 2 ] = -U_0
$$

The minimum potential energy is $-U_0$. It requires an energy input of $+U_0$ to separate the two atoms to infinity!

(c) **Small Oscillations Frequency**:  
Compute the second derivative:

$$
\frac{d^2U}{dr^2} = U_0 \left[ 12 \times 13 \frac{r_0^{12}}{r^{14}} - 12 \times 7 \frac{r_0^6}{r^8} \right]
$$

Evaluate at $r = r_0$:

$$
k_{\text{eff}} = \left. \frac{d^2U}{dr^2} \right|_{r_0} = \frac{U_0}{r_0^2} [ 156 - 84 ] = 72 \frac{U_0}{r_0^2}
$$

Since $k_{\text{eff}} > 0$, the equilibrium is **stable**.  
The small-oscillation angular frequency is:

$$
\omega_0 = \sqrt{\frac{k_{\text{eff}}}{m}} = \sqrt{\frac{72 U_0}{m r_0^2}} = \frac{6\sqrt{2}}{r_0} \sqrt{\frac{U_0}{m}}
$$

---

### Worked Example 13.2: Exact Time Integral for a Harmonic Oscillator
**Problem**: For a 1D spring potential $U(x) = \frac{1}{2} k x^2$, a particle of mass $m$ is released from rest at $x = A$. Use the general 1D time integral to find the exact period of oscillation $\tau$.

**Solution**:  
Total energy is $E = \frac{1}{2} k A^2$. The turning points are $-A$ and $+A$.  
The time required to travel from $x = 0$ to the turning point $x = A$ is one quarter of the period ($\tau / 4$):

$$
\frac{\tau}{4} = \int_0^A \frac{dx}{\sqrt{\frac{2}{m} [E - U(x)]}} = \int_0^A \frac{dx}{\sqrt{\frac{2}{m} [\frac{1}{2}kA^2 - \frac{1}{2}kx^2]}} = \sqrt{\frac{m}{k}} \int_0^A \frac{dx}{\sqrt{A^2 - x^2}}
$$

Let $x = A\sin\theta$, then $dx = A\cos\theta\,d\theta$, and $\sqrt{A^2 - x^2} = A\cos\theta$:

$$
\frac{\tau}{4} = \sqrt{\frac{m}{k}} \int_0^{\pi/2} \frac{A\cos\theta\,d\theta}{A\cos\theta} = \frac{\pi}{2} \sqrt{\frac{m}{k}}
$$

Multiplying by 4:

$$
\tau = 2\pi \sqrt{\frac{m}{k}} \implies \omega_0 = \frac{2\pi}{\tau} = \sqrt{\frac{k}{m}}
$$

---

### Practice Problem 13.1 (To Solve)
**Statement**: A particle moves in the quartic potential $U(x) = -\frac{1}{2} a x^2 + \frac{1}{4} b x^4$, where $a, b > 0$.  
(a) Find all equilibrium points and classify their stability.  
(b) Find the angular frequency $\omega_0$ of small oscillations about the stable equilibria.
* **Hint**: $U'(x) = -ax + bx^3 = x(-a + bx^2) = 0$. Compute $U''(x) = -a + 3bx^2$ at each root.
* **Answer**: $x = 0$ is unstable ($U''(0) = -a < 0$). $x = \pm \sqrt{a/b}$ are stable minima ($U'' = +2a > 0$). Small oscillation frequency: $\omega_0 = \sqrt{\frac{2a}{m}}$.

---

### Practice Problem 13.2 (To Solve)
**Statement**: A particle of mass $m$ moves in the potential $U(x) = U_0 \tan^2(x / a)$ for $|x| < \pi a / 2$. Find the frequency of small oscillations about $x = 0$.
* **Hint**: Taylor-expand $\tan u \approx u$, so $\tan^2 u \approx u^2$. Then $U(x) \approx U_0 \left(\frac{x}{a}\right)^2 = \frac{1}{2} \left(\frac{2U_0}{a^2}\right) x^2$.
* **Answer**: $k_{\text{eff}} = \frac{2U_0}{a^2} \implies \omega_0 = \sqrt{\frac{2U_0}{m a^2}}$.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Section 4.6 (pp. 135–142): Energy for One-Dimensional Systems, Potential Wells, Small Oscillations.
  * Problems 4.27, 4.31, 4.36, 4.38 (pp. 168–170): Equilibrium classification and period integrals.
* **Morin, David**, *Introduction to Classical Mechanics*, Chapter 4:
  * Section 4.1–4.4 (pp. 101–114): Superb graphical treatment of 1D potential wells.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 13: "Work and Potential Energy (A)" (Section 13.4 on potential graphs).\n
