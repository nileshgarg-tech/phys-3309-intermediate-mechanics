# 11. Work, Kinetic Energy & The Work-Energy Theorem

**Foundational Story**: Chapter 4, Section 4.1  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 114–119)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 13 ("Work and Potential Energy (A)")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 4

---

## 1. Why Energy? The Scalar Advantage

Up to this point, our tools have been **vector quantities**: force, momentum, acceleration, torque.  
Working with vectors requires resolving components into coordinate systems ($x, y, z$ or $r, \theta$), handling signs, and managing moving unit vectors.

**Energy introduces a scalar quantity.**  
Energy has no direction in space. If a particle starts at point 1 and moves to point 2, the **Work-Kinetic Energy Theorem** connects its beginning and end speeds without requiring knowledge of the detailed time-dependent trajectory in between!

---

## 2. Work Defined as a Line Integral

In elementary physics, work is described as "force times distance": $W = F d$.  
In realistic mechanics, however:
* The force $\mathbf{F}(\mathbf{r})$ changes in both magnitude and direction along the path.
* The trajectory curve $C$ twists arbitrarily through 3D space.

To find the total work done on a particle as it moves along curve $C$ from point $\mathbf{r}_1$ to point $\mathbf{r}_2$, we divide the path into infinitesimal displacement vectors $d\mathbf{r}$:

$$
W(1 \to 2) = \int_1^2 \mathbf{F} \cdot d\mathbf{r}
$$

In Cartesian coordinates, where $d\mathbf{r} = dx\,\hat{\mathbf{x}} + dy\,\hat{\mathbf{y}} + dz\,\hat{\mathbf{z}}$:

$$
W(1 \to 2) = \int_1^2 \left[ F_x(x,y,z)\,dx + F_y(x,y,z)\,dy + F_z(x,y,z)\,dz \right]
$$

---

## 3. The Work-Kinetic Energy Theorem (Complete 3D Derivation)

Let us evaluate the line integral using Newton's Second Law: $\mathbf{F} = m \mathbf{a} = m \frac{d\mathbf{v}}{dt}$.

$$
W(1 \to 2) = \int_1^2 \mathbf{F} \cdot d\mathbf{r} = \int_{t_1}^{t_2} \left( m \frac{d\mathbf{v}}{dt} \right) \cdot \left( \frac{d\mathbf{r}}{dt} \, dt \right) = m \int_{t_1}^{t_2} \frac{d\mathbf{v}}{dt} \cdot \mathbf{v} \, dt
$$

Now consider the time derivative of the scalar speed squared $v^2 = \mathbf{v} \cdot \mathbf{v}$:

$$
\frac{d(v^2)}{dt} = \frac{d}{dt}(\mathbf{v} \cdot \mathbf{v}) = \frac{d\mathbf{v}}{dt} \cdot \mathbf{v} + \mathbf{v} \cdot \frac{d\mathbf{v}}{dt} = 2 \left( \frac{d\mathbf{v}}{dt} \cdot \mathbf{v} \right)
$$

Therefore:

$$
\frac{d\mathbf{v}}{dt} \cdot \mathbf{v} = \frac{1}{2} \frac{d(v^2)}{dt}
$$

Substitute this directly back into our integral:

$$
W(1 \to 2) = m \int_{t_1}^{t_2} \frac{1}{2} \frac{d(v^2)}{dt} \, dt = \frac{1}{2} m \int_{v_1^2}^{v_2^2} d(v^2) = \frac{1}{2} m v_2^2 - \frac{1}{2} m v_1^2
$$

We define the **Kinetic Energy** $T$:

$$
T = \frac{1}{2} m v^2 = \frac{p^2}{2m}
$$

> **The Work-Kinetic Energy Theorem**:
> 
> $$
> W_{\text{net}}(1 \to 2) = \Delta T = T_2 - T_1
> $$
> 
> The net work done by all forces acting on a particle equals the change in its kinetic energy.

---

## 4. Power: The Rate of Doing Work

The instantaneous time rate at which work is performed on a particle is called **Power** ($P$):

$$
P = \frac{dW}{dt} = \frac{\mathbf{F} \cdot d\mathbf{r}}{dt} = \mathbf{F} \cdot \frac{d\mathbf{r}}{dt} = \mathbf{F} \cdot \mathbf{v}
$$

Notice:
* If force is perpendicular to velocity ($\mathbf{F} \perp \mathbf{v}$, such as magnetic Lorentz forces $q(\mathbf{v} \times \mathbf{B})$ or normal forces on a frictionless track), then $\mathbf{F} \cdot \mathbf{v} = 0$.
* **Zero power is delivered, and kinetic energy is strictly constant!**

---

## 5. Summary Cheat Sheet for Module 11

| Quantity | Formula | Meaning |
|---|---|---|
| **Work (Line Integral)**| $W = \int_1^2 \mathbf{F} \cdot d\mathbf{r}$ | Accumulation of force along displacement path |
| **Kinetic Energy** | $T = \frac{1}{2} m v^2$ | Scalar measure of motion energy |
| **Work-Energy Theorem** | $W_{\text{net}} = \Delta T$ | Net work directly dictates speed change |
| **Instantaneous Power** | $P = \frac{dW}{dt} = \mathbf{F} \cdot \mathbf{v}$ | Rate of energy transfer |
| **Perpendicular Forces** | If $\mathbf{F} \perp \mathbf{v}$, then $P = 0$ | Cannot change speed (e.g. magnetic fields) |

---

## 6. Worked Examples & Practice Problems

### Worked Example 11.1: Path-Dependent Work (Non-Conservative Force)
**Problem**: A particle in the $xy$-plane is acted upon by a 2D force field:

$$
\mathbf{F}(x, y) = y\,\hat{\mathbf{x}} + 2x\,\hat{\mathbf{y}}
$$

Calculate the work done by this force in moving the particle from the origin $(0, 0)$ to the point $(1, 1)$ along two different paths:  
(a) Path 1: A straight line $y = x$.  
(b) Path 2: A parabola $y = x^2$.  
Is this force conservative?

**Solution**:  
The work integral is:

$$
W = \int \mathbf{F} \cdot d\mathbf{r} = \int (F_x\,dx + F_y\,dy) = \int (y\,dx + 2x\,dy)
$$

(a) **Path 1 (Straight line $y = x$, so $dy = dx$)**:  
Substitute $y = x$ and $dy = dx$ as $x$ goes from 0 to 1:

$$
W_1 = \int_0^1 (x\,dx + 2x\,dx) = \int_0^1 3x\,dx = \left[ \frac{3}{2}x^2 \right]_0^1 = \frac{3}{2} = 1.5\text{ Joules}
$$

(b) **Path 2 (Parabola $y = x^2$, so $dy = 2x\,dx$)**:  
Substitute $y = x^2$ and $dy = 2x\,dx$ as $x$ goes from 0 to 1:

$$
W_2 = \int_0^1 [ (x^2)\,dx + 2x (2x\,dx) ] = \int_0^1 5x^2\,dx = \left[ \frac{5}{3}x^3 \right]_0^1 = \frac{5}{3} \approx 1.67\text{ Joules}
$$

**Conclusion**:  
Because $W_1 \neq W_2$ ($1.5\text{ J}$ vs $1.67\text{ J}$), **the work depends explicitly on the path taken!**  
Therefore, the force is **non-conservative**.  
*(In Module 12 we confirm this via the curl: $(\nabla \times \mathbf{F})_z = \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} = 2 - 1 = 1 \neq 0$)*.

---

### Worked Example 11.2: Accelerating Under Constant Power
**Problem**: An electric vehicle of mass $m$ accelerates from rest along a straight horizontal track. The motor delivers a constant mechanical power output $P$. Assuming no friction or drag, find the vehicle's speed $v(t)$ and distance $x(t)$ as functions of time.

**Solution**:  
Power is the time rate of change of kinetic energy:

$$
P = \frac{dT}{dt} = \frac{d}{dt} \left( \frac{1}{2} m v^2 \right)
$$

Since power $P$ is constant, integrate with respect to time starting from rest ($v(0) = 0$):

$$
\frac{1}{2} m v(t)^2 = P t \implies v(t)^2 = \frac{2 P t}{m}
$$

Taking the square root:

$$
v(t) = \sqrt{\frac{2 P}{m}} \, t^{1/2}
$$

Now integrate velocity $v = \frac{dx}{dt}$ to find distance $x(t)$ with $x(0) = 0$:

$$
x(t) = \int_0^t v(t')\,dt' = \sqrt{\frac{2P}{m}} \int_0^t (t')^{1/2}\,dt' = \frac{2}{3} \sqrt{\frac{2 P}{m}} \, t^{3/2}
$$

**Physical Insight**: Unlike constant force acceleration (where $v \propto t$ and $x \propto t^2$), constant power gives $v \propto t^{1/2}$ and $x \propto t^{3/2}$. The acceleration is infinite at $t = 0$ and decreases over time as speed builds up.

---

### Practice Problem 11.1 (To Solve)
**Statement**: A particle of mass $m$ moves in 3D under the linear restoring force $\mathbf{F} = -k \mathbf{r} = -k(x\,\hat{\mathbf{x}} + y\,\hat{\mathbf{y}} + z\,\hat{\mathbf{z}})$. Calculate the work done along a helical path given by $\mathbf{r}(t) = (R\cos t, R\sin t, c t)$ as $t$ goes from $0$ to $2\pi$.
* **Hint**: $d\mathbf{r} = (-R\sin t, R\cos t, c)\,dt$. Compute $\mathbf{F} \cdot d\mathbf{r} = -k (x\,dx + y\,dy + z\,dz) = -k \, d\left(\frac{x^2 + y^2 + z^2}{2}\right)$.
* **Answer**: $W = -\frac{k}{2} [ (R^2 + c^2(2\pi)^2) - (R^2 + 0) ] = -2 \pi^2 k c^2$. (The work depends strictly on the endpoints!).

---

### Practice Problem 11.2 (To Solve)
**Statement**: A block of mass $m = 2.0\text{ kg}$ is pressed against a non-linear spring with restoring force $F(x) = -k x - \beta x^3$, where $k = 400\text{ N/m}$ and $\beta = 1000\text{ N/m}^3$. The spring is compressed by $x_0 = 0.10\text{ m}$ and released. Find the launch speed $v$ of the block as it leaves the spring at $x = 0$.
* **Hint**: Use the Work-Energy Theorem: $\frac{1}{2} m v^2 = W_{\text{spring}} = \int_{-x_0}^0 (-k x - \beta x^3)\,dx$.
* **Answer**: $W = \frac{1}{2} k x_0^2 + \frac{1}{4} \beta x_0^4 = (0.5)(400)(0.01) + (0.25)(1000)(0.0001) = 2.0 + 0.025 = 2.025\text{ J}$. Launch speed $v = \sqrt{\frac{2 \times 2.025}{2.0}} \approx 1.423\text{ m/s}$.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Section 4.1 (pp. 114–119): Kinetic Energy and Work, Line Integrals, 3D Work-Energy Theorem.
  * Problems 4.2, 4.5, 4.9 (pp. 164–165): Line integral work calculations along various geometric paths.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 13: "Work and Potential Energy (A)" (Sections 13.1–13.3).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.1–5.3).\n
