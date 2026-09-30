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

Linear momentum is defined as:

$$
\mathbf{p} = m\mathbf{v} = m\frac{d\mathbf{r}}{dt}
$$

Newton's Second Law is fundamentally a statement about momentum:
> **The time rate of change of momentum of a body is proportional to and in the direction of the net external impressed force:**

$$
\mathbf{F}_{\text{net}} = \frac{d\mathbf{p}}{dt}
$$

For a body with constant mass $m$:

$$
\mathbf{F}_{\text{net}} = \frac{d(m\mathbf{v})}{dt} = m\frac{d\mathbf{v}}{dt} = m\frac{d^2\mathbf{r}}{dt^2} = m\mathbf{a}
$$

### Newton's Second Law as a Second-Order Differential Equation

Because acceleration is the second time derivative of position ($\mathbf{a} = \ddot{\mathbf{r}} = \frac{d^2\mathbf{r}}{dt^2}$), Newton's Second Law is fundamentally an equation for the unknown trajectory function $\mathbf{r}(t)$:

$$
m\frac{d^2\mathbf{r}}{dt^2} = \mathbf{F}\left(\mathbf{r}, \dot{\mathbf{r}}, t\right)
$$

#### What Can Force Physically Depend On? Understanding $\mathbf{F}(\mathbf{r}, \dot{\mathbf{r}}, t)$

In introductory physics, forces often appear as simple constants ($mg$) or single-variable formulas ($-kx$). But in general mechanics, the net force acting on a particle at any instant can depend on three distinct physical variables:

1. **Position Dependence ($\mathbf{r}$)**: *"Where is the particle located in space?"*  
   Most fundamental static and potential forces depend purely on where the particle is relative to the sources of force:
   * **Universal Gravitation**: $\mathbf{F}_g(\mathbf{r}) = -\frac{G M m}{r^2}\hat{\mathbf{r}}$ (Taylor Ch. 8). The gravitational force exerted by the Sun on a planet depends strictly on the distance and direction $\mathbf{r}$ from the Sun.
   * **Hooke's Law (Elastic Restoring Force)**: $\mathbf{F}_{\text{spring}}(\mathbf{r}) = -k(x - x_0)\hat{\mathbf{x}}$ (Taylor Ch. 5). The tension or compression force of a spring depends only on how far it is displaced from equilibrium.
   * **Coulomb Electrostatics**: $\mathbf{F}_e(\mathbf{r}) = \frac{k_e q_1 q_2}{r^2}\hat{\mathbf{r}}$.
   * **Conservative Force Fields**: In general, any conservative force is derived from the spatial gradient of a potential energy function: $\mathbf{F}(\mathbf{r}) = -\nabla U(\mathbf{r})$ (Taylor Ch. 4).

2. **Velocity Dependence ($\dot{\mathbf{r}} = \mathbf{v} = \frac{d\mathbf{r}}{dt}$)**: *"How fast and in what direction is the particle moving?"*  
   Some forces vanish when a particle is at rest and only appear when it moves through a medium or magnetic field:
   * **Fluid & Atmospheric Resistance**: $\mathbf{F}_{\text{drag}}(\mathbf{v}) = -b\mathbf{v}$ (linear/Stokes drag) or $-c v^2 \hat{\mathbf{v}}$ (quadratic drag) (Taylor Ch. 2). A baseball sitting on a table feels zero air drag; the moment it is pitched, a retarding force opposes its instantaneous velocity $\mathbf{v}$.
   * **Magnetic Lorentz Force**: $\mathbf{F}_{\text{mag}}(\mathbf{v}) = q(\mathbf{v} \times \mathbf{B})$ (Taylor Ch. 2 & Ch. 3). A stationary electric charge in a static magnetic field feels no force; only a moving charge experiences magnetic deflection.
   * **Viscous Damping**: Damping in shock absorbers and oscillators: $\mathbf{F}_{\text{damp}} = -\gamma \dot{x}$ (Taylor Ch. 5).

3. **Explicit Time Dependence ($t$)**: *"What time is it on the external clock?"*  
   A force depends explicitly on $t$ when external driving agents or time-dependent fields act on the system independently of the particle's own position or velocity:
   * **Driven / Forced Oscillators**: $\mathbf{F}_{\text{drive}}(t) = F_0 \cos(\omega t)\hat{\mathbf{x}}$ (Taylor Ch. 5), where an external motor or shaker table oscillates at a prescribed frequency $\omega$.
   * **Time-Varying Electromagnetic Fields**: An AC electric field $\mathbf{E}(t) = \mathbf{E}_0 \sin(\omega t)$ produced by an external alternating current source.
   * **Wind Gusts & Transient Loads**: External forces that pulse or turn on and off over a scheduled duration.

> [!NOTE]
> **Why doesn't force depend on acceleration ($\ddot{\mathbf{r}}$) or higher derivatives ($\dddot{\mathbf{r}}$)?**  
> Force is the physical **cause** of acceleration, not the result of it. If force were allowed to depend directly on acceleration $\ddot{\mathbf{r}}$, Newton's Second Law ($m\ddot{\mathbf{r}} = \mathbf{F}$) would become a circular identity rather than a predictive dynamical law. In classical mechanics, the instantaneous physical state of the universe is completely defined by coordinates $\mathbf{r}$ and velocities $\dot{\mathbf{r}}$ at time $t$; the laws of physics then specify the resulting force $\mathbf{F}$, which in turn dictates the second derivative $\ddot{\mathbf{r}}$.

---

#### Component Form: A System of Three Coupled Second-Order ODEs

Because $\mathbf{r} = (x, y, z)$ is a 3D vector, the vector equation $m\ddot{\mathbf{r}} = \mathbf{F}(\mathbf{r}, \dot{\mathbf{r}}, t)$ represents **three simultaneous second-order differential equations**:

$$
\begin{cases}
m\dfrac{d^2 x}{dt^2} = F_x(x, y, z, \dot{x}, \dot{y}, \dot{z}, t) \\[8pt]
m\dfrac{d^2 y}{dt^2} = F_y(x, y, z, \dot{x}, \dot{y}, \dot{z}, t) \\[8pt]
m\dfrac{d^2 z}{dt^2} = F_z(x, y, z, \dot{x}, \dot{y}, \dot{z}, t)
\end{cases}
$$

These equations are often **coupled**: for instance, in the magnetic force $\mathbf{F} = q(\mathbf{v} \times \mathbf{B})$, the $x$-acceleration depends on the $y$-velocity ($m\ddot{x} = q B_z \dot{y}$), tying motion across multiple dimensions together.

---

#### Why Two Initial Conditions are Required per Coordinate

Because each component equation involves a **second derivative** with respect to time ($d^2/dt^2$), solving for the trajectory requires **integrating twice**:

1. **First Integration**: Determines the velocity $\mathbf{v}(t) = \dot{\mathbf{r}}(t)$ and introduces one vector constant of integration ($\mathbf{C}_1 = \mathbf{v}_0$).
2. **Second Integration**: Determines the position $\mathbf{r}(t)$ and introduces a second vector constant of integration ($\mathbf{C}_2 = \mathbf{r}_0$).

To fix these integration constants uniquely, mathematics requires **two initial boundary conditions per degree of freedom** (a total of 6 scalar constants for 3D motion):

1. **Initial Position**: $\mathbf{r}(0) = \mathbf{r}_0 = (x_0, y_0, z_0)$ *(Where did the particle start?)*
2. **Initial Velocity**: $\mathbf{v}(0) = \dot{\mathbf{r}}(0) = \mathbf{v}_0 = (v_{x0}, v_{y0}, v_{z0})$ *(In what direction and how fast was it moving?)*

**Physical Intuition**: If you hold a ball at the top of a building, knowing only its initial height $y(0) = h$ tells you nothing about where it will land. Did you drop it from rest ($v_0 = 0$), throw it straight down ($v_0 < 0$), or launch it horizontally ($v_{x0} > 0$)? Only when **both** where it is and how fast it is moving at $t = 0$ are specified does Newton's Second Law uniquely predict its entire future path $\mathbf{r}(t)$ for all time (Laplacian determinism).

---

## 3. Newton's Third Law & Conservation of Momentum

Newton's Third Law states:

$$
\mathbf{F}_{12} = -\mathbf{F}_{21}
$$

Let us define the **Total Linear Momentum** of a two-particle isolated system:

$$
\mathbf{P}_{\text{total}} = \mathbf{p}_1 + \mathbf{p}_2
$$

Taking the time derivative:

$$
\frac{d\mathbf{P}_{\text{total}}}{dt} = \frac{d\mathbf{p}_1}{dt} + \frac{d\mathbf{p}_2}{dt} = \mathbf{F}_{12} + \mathbf{F}_{21} = \mathbf{0}
$$

Therefore:

$$
\mathbf{P}_{\text{total}} = \text{constant}
$$

> **The Principle of Conservation of Linear Momentum**:
> **If the net external force on a system of particles is zero, the total linear momentum of the system remains strictly constant for all time.**
> (In Chapter 7, Noether's Theorem will reveal that linear momentum is conserved because space is homogeneous under spatial translations).

---

## 4. Summary Cheat Sheet for Module 02

| Concept | Formula | Core Takeaway |
|---|---|---|
| **Operational Mass** | $\frac{m_2}{m_1} = \frac{\vert\mathbf{a}_1\vert}{\vert\mathbf{a}_2\vert}$ | Defined by mutually interacting acceleration ratios |
| **Linear Momentum** | $\mathbf{p} = m\mathbf{v}$ | Vector quantity of motion |
| **Newton's 2nd Law** | $\mathbf{F} = \frac{d\mathbf{p}}{dt} = m\ddot{\mathbf{r}}$ | 2nd-order ODE; requires $\mathbf{r}_0$ and $\mathbf{v}_0$ to solve |
| **Newton's 3rd Law** | $\mathbf{F}_{12} = -\mathbf{F}_{21}$ | Mutual forces are equal and opposite |
| **Momentum Conservation**| $\frac{d\mathbf{P}}{dt} = \mathbf{F}_{\text{ext}} = \mathbf{0}$ | Direct consequence of the 3rd Law |

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
* **Hint**: Separate variables: $m\frac{dv}{dt} = -kv^2 \implies \int v^{-2} dv = -\frac{k}{m}\int dt$.
* **Answer**: $v(t) = \frac{v_0}{1 + \frac{kv_0}{m}t}$. As $t \to \infty$, $v(t) \to 0$, but it technically never reaches zero in finite time.

---

### Practice Problem 2.2 (To Solve)
**Statement**: Three interacting particles with masses $m_1, m_2, m_3$ exert mutual gravitational forces on each other: 

$$
\mathbf{F}_{ij} = -\frac{Gm_i m_j}{|\mathbf{r}_i - \mathbf{r}_j|^3}(\mathbf{r}_i - \mathbf{r}_j)
$$

Prove explicitly that the sum of all internal forces $\sum_i \sum_{j \ne i} \mathbf{F}_{ij}$ vanishes.
* **Hint**: Expand the sum for $i, j \in \{1, 2, 3\}$ and group action-reaction pairs $\mathbf{F}_{12} + \mathbf{F}_{21}$.
* **Answer**: Because $(\mathbf{r}_i - \mathbf{r}_j) = -(\mathbf{r}_j - \mathbf{r}_i)$, each pair cancels to zero identically.

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
