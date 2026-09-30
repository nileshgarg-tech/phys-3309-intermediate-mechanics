# 05. Linear Air Drag: Exact Trajectories & Characteristic Time

**Foundational Story**: Chapter 2, Sections 2.2–2.3  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 48–60)
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 2

---

## 1. Decoupled Equations of Motion

With linear drag $\mathbf{f} = -b\mathbf{v}$ (Taylor, Eq. 2.5):

$$
m\dot{\mathbf{v}} = m\mathbf{g} - b\mathbf{v}
$$

In components ($x$ horizontal, $y$ vertical upward; Taylor, Eq. 2.21):

$$
m\dot{v}_x = -b v_x
$$

$$
m\dot{v}_y = -mg - b v_y
$$

The horizontal and vertical motions are completely decoupled!

---

## 2. Horizontal Motion & The Characteristic Time

Following Taylor (Eq. 2.22), define the characteristic time $\tau$:

$$
\tau = \frac{m}{b}
$$

The horizontal ODE becomes (Taylor, Eq. 2.23):

$$
\dot{v}_x = -\frac{1}{\tau}v_x \implies v_x(t) = v_{x0}e^{-t/\tau}
$$

Integrating to find position (Taylor, Eq. 2.26):

$$
x(t) = \int_0^t v_x(t')\,dt' = v_{x0}\tau(1 - e^{-t/\tau})
$$

As $t \to \infty$, the particle approaches a finite maximum range:

$$
x_{\text{max}} = v_{x0}\tau = \frac{mv_{x0}}{b}
$$

---

## 3. Vertical Motion & Terminal Velocity

For vertical motion (Taylor, Eq. 2.29):

$$
\dot{v}_y = -g - \frac{v_y}{\tau} = -\frac{1}{\tau}(v_y + v_{\text{ter}})
$$

where the **terminal speed** is:

$$
v_{\text{ter}} = g\tau = \frac{mg}{b}
$$

Integrating from rest ($v_{y0} = 0$):

$$
v_y(t) = -v_{\text{ter}}(1 - e^{-t/\tau})
$$

Integrating position:

$$
y(t) = -v_{\text{ter}}t + v_{\text{ter}}\tau(1 - e^{-t/\tau})
$$

---

## 4. The 2D Trajectory Equation

Eliminating time $t$:

$$
y(x) = \frac{v_{y0} + v_{\text{ter}}}{v_{x0}}x + v_{\text{ter}}\tau\ln\left(1 - \frac{x}{v_{x0}\tau}\right)
$$

Expanding the logarithm for weak drag ($x / (v_{x0}\tau) \ll 1$) using $\ln(1 - u) \approx -u - \frac{u^2}{2}$:

$$
y(x) \approx \frac{v_{y0}}{v_{x0}}x - \frac{g}{2v_{x0}^2}x^2
$$

This smoothly recovers the standard Galilean vacuum parabola!

---

## 5. Summary Cheat Sheet for Module 05

| Quantity | Formula | Meaning |
|---|---|---|
| **Characteristic Time** | $\tau = \frac{m}{b}$ | Time scale to lose $1/e \approx 63\%$ of speed |
| **Terminal Velocity** | $v_{\text{ter}} = g\tau = \frac{mg}{b}$ | Maximum steady-state falling speed |
| **Horizontal Velocity** | $v_x(t) = v_{x0}e^{-t/\tau}$ | Exponential velocity decay |
| **Maximum Range** | $x_{\text{max}} = v_{x0}\tau$ | Finite horizontal boundary |
| **Vacuum Recovery** | Expand $\ln(1 - u)$ | Recovers $y = \frac{v_{y0}}{v_{x0}}x - \frac{g}{2v_{x0}^2}x^2$ |

---

## 6. Worked Examples & Practice Problems

### Worked Example 5.1: Stopping Distance of a Boat
**Problem**: A boat of mass $m = 500\text{ kg}$ has speed $v_0 = 20\text{ m/s}$ when the engine cuts. The water drag is linear with $b = 50\text{ N}\cdot\text{s/m}$.
(a) Find $\tau$.
(b) Find the time to slow down to $1\text{ m/s}$.
(c) Find maximum coasting distance $x_{\text{max}}$.

**Solution**:
(a) $\tau = m / b = 500 / 50 = 10.0\text{ seconds}$.
(b) $v(t) = v_0 e^{-t/\tau} \implies 1 = 20e^{-t/10} \implies t = 10\ln(20) \approx 29.96\text{ s}$.
(c) $x_{\text{max}} = v_0\tau = (20\text{ m/s})(10\text{ s}) = 200\text{ meters}$.

---

### Practice Problem 5.1 (To Solve)
**Statement**: Prove that the horizontal distance traveled when speed drops to half its initial value ($v_x = v_0 / 2$) is $x = x_{\text{max}} / 2$.
* **Hint**: $v_x = v_0 e^{-t/\tau} = v_0/2 \implies e^{-t/\tau} = 1/2$. Substitute into $x(t) = v_0\tau(1 - e^{-t/\tau})$.
* **Answer**: $x = v_0\tau(1 - 1/2) = \frac{1}{2}x_{\text{max}}$.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 2:
  * Sections 2.2–2.3 (pp. 48–60).
  * Problems 2.7, 2.11, 2.15, 2.18 (pp. 74–76).
* **Morin, David**, *Introduction to Classical Mechanics*, Chapter 3 (Example 3.4).
