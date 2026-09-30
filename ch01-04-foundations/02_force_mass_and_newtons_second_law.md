# 02. Force, Mass, and Newton's Second & Third Laws

**Foundational Story**: Chapter 1, Sections 1.3–1.5  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 1 (pp. 11–23)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 9 ("Newton's Laws of Dynamics") & Ch. 11 ("Vectors")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 2 ("Newton's Laws")

---

## 1. The Operational Definition of Mass via Collisions

Ernst Mach and later Robert Woodhouse provided the operational definition that rescues Newtonian mechanics from circularity:

Imagine two isolated particles, Particle 1 and Particle 2, floating in deep space with zero external forces acting on them. We allow them to interact—perhaps by a compressed spring between them, or an elastic collision.

Experimentally, we measure their instantaneous accelerations $\mathbf{a}_1$ and $\mathbf{a}_2$. We discover two universal facts:
1. Their accelerations are always directed in opposite directions:

$$
\mathbf{a}_1 \parallel -\mathbf{a}_2
$$

2. The ratio of their acceleration magnitudes is strictly constant:

$$
\frac{|\mathbf{a}_1|}{|\mathbf{a}_2|} = \text{constant}
$$

We define this constant as the ratio of their **inertial masses**:

$$
\frac{m_2}{m_1} = \frac{|\mathbf{a}_1|}{|\mathbf{a}_2|}
$$

**Mass is an intrinsic, scalar property of matter that quantifies its inertial reluctance to a change in velocity.**

---

## 2. Momentum and Newton's Second Law

Linear momentum is defined as (Taylor, Eq. 1.18):

$$
\mathbf{p} = m\mathbf{v} = m\dot{\mathbf{r}}
$$

Newton's Second Law is fundamentally a statement about momentum (Taylor, Eq. 1.19):
> **The time rate of change of momentum of a body is equal to the net applied force:**

$$
\mathbf{F} = \dot{\mathbf{p}}
$$

For a body with constant mass $m$ (Taylor, Eq. 1.17 & Eq. 1.30):

$$
\mathbf{F} = \dot{\mathbf{p}} = m\dot{\mathbf{v}} = m\ddot{\mathbf{r}} = m\mathbf{a}
$$

### Second-Order Differential Equation
Because acceleration is the second time derivative of position ($\ddot{\mathbf{r}}$), Newton's second law is fundamentally a system of second-order differential equations for the particle's trajectory $\mathbf{r}(t)$ (Taylor, Sec. 1.4 & Sec. 1.6):

$$
m\ddot{\mathbf{r}} = \mathbf{F}\left(\mathbf{r}, \dot{\mathbf{r}}, t\right)
$$

To solve for the trajectory $\mathbf{r}(t)$ uniquely, mathematics requires **two initial boundary conditions**:
1. Initial position: $\mathbf{r}(0) = \mathbf{r}_0$
2. Initial velocity: $\mathbf{v}(0) = \dot{\mathbf{r}}(0) = \mathbf{v}_0$

> [!TIP]
> 📖 **Deep-Dive Companion Guide**:  
> For an in-depth breakdown of what forces can physically depend on ($\mathbf{r}$, $\dot{\mathbf{r}}$, $t$), why force never depends on acceleration ($\ddot{\mathbf{r}}$), the 3D coupled component system, and why two initial conditions are mathematically and physically required, see:  
> 👉 **[Deep Dive: Newton's Second Law as a Differential Equation](explanations/02_newtons_second_law_differential_equations.md)**

---

## 3. Newton's Third Law & Conservation of Momentum

Newton's Third Law states (Taylor, Eq. 1.22):

$$
\mathbf{F}_{12} = -\mathbf{F}_{21}
$$

Following Taylor (Sec. 1.5), let us define the **Total Linear Momentum** of a two-particle isolated system:

$$
\mathbf{P} = \mathbf{p}_1 + \mathbf{p}_2
$$

Taking the time derivative (Taylor, Eq. 1.25):

$$
\dot{\mathbf{P}} = \dot{\mathbf{p}}_1 + \dot{\mathbf{p}}_2 = \mathbf{F}_{12} + \mathbf{F}_{21} = \mathbf{0}
$$

Therefore:

$$
\mathbf{P} = \text{constant}
$$

> **The Principle of Conservation of Linear Momentum**:
> **If the net external force on a system of particles is zero, the total linear momentum of the system remains strictly constant for all time.**
> (In Chapter 7, Noether's Theorem will reveal that linear momentum is conserved because space is homogeneous under spatial translations).

---

## 4. Summary Cheat Sheet for Module 02

| Concept | Formula | Core Takeaway |
|---|---|---|
| **Operational Mass** | $\frac{m_2}{m_1} = \frac{\vert\mathbf{a}_1\vert}{\vert\mathbf{a}_2\vert}$ | Defined by mutually interacting acceleration ratios |
| **Linear Momentum** | $\mathbf{p} = m\mathbf{v} = m\dot{\mathbf{r}}$ | Vector quantity of motion (Taylor, Eq. 1.18) |
| **Newton's 2nd Law** | $\mathbf{F} = \dot{\mathbf{p}} = m\ddot{\mathbf{r}}$ | 2nd-order ODE; requires $\mathbf{r}_0$ and $\mathbf{v}_0$ to solve (Taylor, Eq. 1.30) |
| **Newton's 3rd Law** | $\mathbf{F}_{12} = -\mathbf{F}_{21}$ | Mutual forces are equal and opposite (Taylor, Eq. 1.22) |
| **Momentum Conservation**| $\dot{\mathbf{P}} = \mathbf{F}^{\text{ext}} = \mathbf{0}$ | Direct consequence of the 3rd Law (Taylor, Eq. 1.25) |

---

## 5. Worked Examples & Practice Problems

### Worked Example 2.1: Operational Mass Ratio on an Air Track
**Problem**: Two gliders of unknown masses $m_1$ and $m_2$ rest on a frictionless horizontal air track. A compressed spring is placed between them and released. Photogates measure their accelerations: glider 1 accelerates at $a_1 = -4.5\text{ m/s}^2$, while glider 2 accelerates at $a_2 = +1.5\text{ m/s}^2$. 
(a) What is the mass ratio $m_2 / m_1$?
(b) If glider 1 is calibrated at $m_1 = 0.200\text{ kg}$, what is $m_2$?

**Solution**:
By Newton's Third Law and Mach's definition:

$$
m_1 a_1 = -m_2 a_2
$$

(a) Taking magnitudes:

$$
\frac{m_2}{m_1} = \frac{|a_1|}{|a_2|} = \frac{4.5}{1.5} = 3.0
$$

Glider 2 is precisely three times as massive as glider 1.
(b) Since $m_1 = 0.200\text{ kg}$:

$$
m_2 = 3.0 \times 0.200\text{ kg} = 0.600\text{ kg}
$$

---

### Worked Example 2.2: Integrating a Time-Dependent Force
**Problem**: A particle of mass $m$ is at rest at the origin ($x = 0, v = 0$) at time $t = 0$. It is subjected to a force $F(t) = F_0\sin(\omega t)$. 
Find the velocity $v(t)$ and position $x(t)$ for all future time.

**Solution**:
Newton's Second Law:

$$
m\frac{dv}{dt} = F_0\sin(\omega t)
$$

Integrating with $v(0) = 0$:

$$
v(t) = \frac{F_0}{m}\int_0^t \sin(\omega t')\,dt' = \frac{F_0}{m\omega}\Big[ -\cos(\omega t') \Big]_0^t = \frac{F_0}{m\omega}(1 - \cos(\omega t))
$$

Notice that since $1 - \cos(\omega t) \ge 0$, the velocity is **always positive or zero**—the particle never reverses direction.
Now integrate velocity to find position with $x(0) = 0$:

$$
x(t) = \int_0^t v(t')\,dt' = \frac{F_0}{m\omega}\int_0^t (1 - \cos(\omega t'))\,dt' = \frac{F_0}{m\omega}\left[ t - \frac{1}{\omega}\sin(\omega t) \right]
$$

---

### Practice Problem 2.1 (To Solve)
**Statement**: A block of mass $m$ slides on a flat surface with initial velocity $v_0$ at $t = 0$ against a quadratic retarding force $F = -k v^2$. 
Find the velocity $v(t)$ as a function of time, and determine if it stops in finite time.

**Hint**: Separate variables:

$$
m\frac{dv}{dt} = -kv^2 \implies \int v^{-2} dv = -\frac{k}{m}\int dt
$$

**Answer**:

$$
v(t) = \frac{v_0}{1 + \frac{kv_0}{m}t}
$$

As $t \to \infty$, $v(t) \to 0$, but it technically never reaches zero in finite time.

---

### Practice Problem 2.2 (To Solve)
**Statement**: Following Taylor (Sec. 1.5, pp. 21–23), three interacting particles with masses $m_1, m_2, m_3$ exert mutual gravitational forces on each other: 

$$
\mathbf{F}_{\alpha\beta} = -\frac{G m_\alpha m_\beta}{|\mathbf{r}_\alpha - \mathbf{r}_\beta|^3}(\mathbf{r}_\alpha - \mathbf{r}_\beta)
$$

Prove explicitly that the sum of all internal forces $\sum_\alpha \sum_{\beta \ne \alpha} \mathbf{F}_{\alpha\beta}$ vanishes.

**Hint**: Expand the sum for $\alpha, \beta \in \{1, 2, 3\}$ and group the action-reaction pairs:

$$
(\mathbf{F}_{12} + \mathbf{F}_{21}) + (\mathbf{F}_{13} + \mathbf{F}_{31}) + (\mathbf{F}_{23} + \mathbf{F}_{32})
$$

**Answer**: Because the relative displacement vector satisfies:

$$
\mathbf{r}_\alpha - \mathbf{r}_\beta = -(\mathbf{r}_\beta - \mathbf{r}_\alpha)
$$

Newton's Third Law gives:

$$
\mathbf{F}_{\alpha\beta} = -\mathbf{F}_{\beta\alpha}
$$

Therefore, each pair cancels to zero identically:

$$
\mathbf{F}_{\alpha\beta} + \mathbf{F}_{\beta\alpha} = \mathbf{0}
$$

---

## 6. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 1:
  * Sections 1.3–1.5 (pp. 11–23): Mass, Force, Newton's 2nd and 3rd Laws, Momentum Conservation.
  * Problems 1.12, 1.18, 1.22 (pp. 37–39).
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 9: "Newton's Laws of Dynamics" (Sections 9.1–9.4).
  * Chapter 11: "Vectors" (Section 11.4).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 2: "Newton's Laws" (Sections 2.1–2.4).
