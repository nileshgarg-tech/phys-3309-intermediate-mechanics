# 10. Angular Momentum: Single & Multiparticle Systems

**Foundational Story**: Chapter 3, Sections 3.4–3.5  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 3 (pp. 90–99)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 18 & Ch. 20 ("Rotation in Space")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 6

---

## 1. Defining Angular Momentum for a Single Particle

Linear momentum ($\mathbf{p} = m \mathbf{v}$) measures motion along a straight line.  
**Angular momentum** ($\mathbf{l}$) measures rotational motion about a designated reference origin $O$.

For a particle of mass $m$ with position vector $\mathbf{r}$ and linear momentum $\mathbf{p}$:

$$
\mathbf{l} = \mathbf{r} \times \mathbf{p} = \mathbf{r} \times (m\mathbf{v})
$$

Angular momentum is an **axial vector** perpendicular to both the position vector and the velocity vector.  
Its magnitude is:

$$
|\mathbf{l}| = r p \sin\theta = r_\perp p = r p_\perp
$$

---

## 2. Torque and the Fundamental Rotational Law

What causes angular momentum to change?  
Let us differentiate $\mathbf{l}$ with respect to time:

$$
\frac{d\mathbf{l}}{dt} = \frac{d}{dt}(\mathbf{r} \times \mathbf{p}) = \left(\frac{d\mathbf{r}}{dt} \times \mathbf{p}\right) + \left(\mathbf{r} \times \frac{d\mathbf{p}}{dt}\right)
$$

Examine the first term:

$$
\frac{d\mathbf{r}}{dt} \times \mathbf{p} = \mathbf{v} \times (m\mathbf{v}) = m (\mathbf{v} \times \mathbf{v}) = \mathbf{0}
$$

*(The cross product of any vector with itself is identically zero!)*  
Now examine the second term: by Newton's Second Law, $\frac{d\mathbf{p}}{dt} = \mathbf{F}_{\text{net}}$. Therefore:

$$
\frac{d\mathbf{l}}{dt} = \mathbf{r} \times \mathbf{F}_{\text{net}}
$$

We define the **Torque** (or moment of force) $\mathbf{\Gamma}$:

$$
\mathbf{\Gamma} = \mathbf{r} \times \mathbf{F}
$$

> **The Rotational Form of Newton's Second Law**:
> 
> $$
> \mathbf{\Gamma}_{\text{net}} = \frac{d\mathbf{l}}{dt}
> $$
> 
> Torque is the instantaneous time rate of change of angular momentum.

---

## 3. Central Forces and Kepler's Second Law

A force is called a **Central Force** if it always points directly toward or away from the origin:

$$
\mathbf{F}(\mathbf{r}) = f(r)\,\hat{\mathbf{r}}
$$

Examples include Newtonian gravity ($\mathbf{F} = -\frac{GMm}{r^2}\hat{\mathbf{r}}$) and Coulomb electrostatics ($\mathbf{F} = \frac{kq_1q_2}{r^2}\hat{\mathbf{r}}$).

Compute the torque exerted by a central force:

$$
\mathbf{\Gamma} = \mathbf{r} \times \mathbf{F} = \mathbf{r} \times [f(r)\,\hat{\mathbf{r}}] = f(r)\,[r (\hat{\mathbf{r}} \times \hat{\mathbf{r}})] = \mathbf{0}
$$

Because $\mathbf{\Gamma} = \mathbf{0}$:

$$
\frac{d\mathbf{l}}{dt} = \mathbf{0} \implies \mathbf{l} = \mathbf{r} \times (m\mathbf{v}) = \text{constant vector!}
$$

### Consequences of Angular Momentum Conservation:
1. **Planar Motion**: Since $\mathbf{l}$ is a fixed vector in space, and $\mathbf{r}(t) \cdot \mathbf{l} = 0$ at all times, the particle's entire trajectory is permanently confined to a 2D plane perpendicular to $\mathbf{l}$.
2. **Kepler's Second Law (Equal Areas in Equal Times)**:  
   The area swept out by the position vector in time $dt$ is a triangle of area:

$$
dA = \frac{1}{2} |\mathbf{r} \times d\mathbf{r}| = \frac{1}{2} |\mathbf{r} \times (\mathbf{v}\,dt)| = \frac{|\mathbf{l}|}{2m}\,dt
$$

   Dividing by $dt$:

$$
\frac{dA}{dt} = \frac{|\mathbf{l}|}{2m} = \text{constant}
$$

   A planet sweeps out equal orbital areas in equal intervals of time.

---

## 4. Total Angular Momentum of a Multiparticle System

For a collection of $N$ particles:

$$
\mathbf{L}_{\text{total}} = \sum_{i=1}^N \mathbf{l}_i = \sum_{i=1}^N (\mathbf{r}_i \times \mathbf{p}_i)
$$

Differentiate with respect to time:

$$
\frac{d\mathbf{L}_{\text{total}}}{dt} = \sum_{i=1}^N (\mathbf{r}_i \times \mathbf{F}_i^{\text{ext}}) + \sum_{i=1}^N \sum_{j \neq i} (\mathbf{r}_i \times \mathbf{F}_{ij})
$$

Let us inspect the internal torque sum. Grouping mutual action-reaction pairs:

$$
\mathbf{r}_i \times \mathbf{F}_{ij} + \mathbf{r}_j \times \mathbf{F}_{ji} = \mathbf{r}_i \times \mathbf{F}_{ij} - \mathbf{r}_j \times \mathbf{F}_{ij} = (\mathbf{r}_i - \mathbf{r}_j) \times \mathbf{F}_{ij}
$$

If the internal forces obey the **Strong Form of Newton's Third Law**, $\mathbf{F}_{ij}$ acts along the relative displacement vector $(\mathbf{r}_i - \mathbf{r}_j)$. Therefore:

$$
(\mathbf{r}_i - \mathbf{r}_j) \times \mathbf{F}_{ij} = \mathbf{0}
$$

All internal torques vanish identically!

$$
\frac{d\mathbf{L}_{\text{total}}}{dt} = \sum_{i=1}^N (\mathbf{r}_i \times \mathbf{F}_i^{\text{ext}}) = \mathbf{\Gamma}_{\text{net}}^{\text{ext}}
$$

If the net external torque is zero, the total angular momentum of the system is strictly conserved!

---

## 5. The Orbital vs. Spin Decomposition

Here is one of the most elegant theorems in classical mechanics:  
Let $\mathbf{R}$ be the Center of Mass position, and let $\mathbf{r}'_i$ be the position of particle $i$ **relative to the Center of Mass**:

$$
\mathbf{r}_i = \mathbf{R} + \mathbf{r}'_i
$$

$$
\mathbf{v}_i = \mathbf{V}_{\text{cm}} + \mathbf{v}'_i
$$

Substitute this into the total angular momentum formula:

$$
\mathbf{L} = \sum_{i=1}^N \left[ (\mathbf{R} + \mathbf{r}'_i) \times m_i (\mathbf{V}_{\text{cm}} + \mathbf{v}'_i) \right]
$$

Expanding the cross products:

$$
\mathbf{L} = \left(\mathbf{R} \times M\mathbf{V}_{\text{cm}}\right) + \mathbf{R} \times \sum_{i=1}^N m_i \mathbf{v}'_i + \left(\sum_{i=1}^N m_i \mathbf{r}'_i\right) \times \mathbf{V}_{\text{cm}} + \sum_{i=1}^N (\mathbf{r}'_i \times m_i \mathbf{v}'_i)
$$

Notice that by definition of Center of Mass, $\sum_i m_i \mathbf{r}'_i = \mathbf{0}$ and $\sum_i m_i \mathbf{v}'_i = \mathbf{0}$. The two cross-terms vanish! We are left with:

$$
\mathbf{L}_{\text{total}} = (\mathbf{R} \times M\mathbf{V}_{\text{cm}}) + \sum_{i=1}^N (\mathbf{r}'_i \times m_i \mathbf{v}'_i)
$$

> **The Two-Component Angular Momentum Theorem**:
> 
> $$
> \mathbf{L}_{\text{total}} = \mathbf{L}_{\text{orbital}}(\text{CM}) + \mathbf{L}_{\text{spin}}(\text{about CM})
> $$
> 
> 1. **Orbital Angular Momentum ($\mathbf{L}_{\text{orbital}} = \mathbf{R} \times \mathbf{P}$)**: The angular momentum of the Center of Mass moving through space around the external origin.
> 2. **Spin Angular Momentum ($\mathbf{L}_{\text{spin}} = \sum \mathbf{r}'_i \times \mathbf{p}'_i$)**: The intrinsic rotational angular momentum of the system spinning around its own Center of Mass.

**Example**: The Earth has:
* An **orbital angular momentum** revolving around the Sun once per 365 days.
* A **spin angular momentum** rotating around its polar axis once every 24 hours.

---

## 6. Summary Cheat Sheet for Module 10

| Quantity | Formula | Physical Meaning |
|---|---|---|
| **Angular Momentum** | $\mathbf{l} = \mathbf{r} \times \mathbf{p}$ | Measure of rotational momentum about origin |
| **Torque** | $\mathbf{\Gamma} = \mathbf{r} \times \mathbf{F}$ | Moment of force; causes $\mathbf{l}$ to change |
| **Rotational Law** | $\mathbf{\Gamma}_{\text{net}} = \frac{d\mathbf{l}}{dt}$ | Angular counterpart to $\mathbf{F} = \frac{d\mathbf{p}}{dt}$ |
| **Central Forces** | $\mathbf{\Gamma} = \mathbf{0} \implies \mathbf{l} = \text{const}$ | Produces planar motion & Kepler's 2nd Law |
| **Internal Torques** | $\sum (\mathbf{r}_i \times \mathbf{F}_{ij}) = \mathbf{0}$ | Cancel out if forces lie along connecting lines |
| **Orbital + Spin Split** | $\mathbf{L} = (\mathbf{R} \times \mathbf{P}_{\text{cm}}) + \mathbf{L}_{\text{relative}}$| Total rotation decomposes into orbit + spin |

---

## 7. Worked Examples & Practice Problems

### Worked Example 10.1: Angular Momentum of a Conical Pendulum
**Problem**: A bob of mass $m$ hangs from a fixed pivot by a string of length $L$. It moves in a horizontal circle of radius $R = L\sin\alpha$ at constant angular speed $\omega$.  
(a) Find the angular momentum vector $\mathbf{l}$ of the bob calculated about the **suspension pivot point O**.  
(b) Compute the torque $\mathbf{\Gamma}$ about point O, and verify that $\frac{d\mathbf{l}}{dt} = \mathbf{\Gamma}$.

**Solution**:  
1. **Coordinates**:  
   Let the pivot point be the origin $O$. The position of the bob is:

$$
\mathbf{r}(t) = R\cos(\omega t)\,\hat{\mathbf{x}} + R\sin(\omega t)\,\hat{\mathbf{y}} - h\,\hat{\mathbf{z}}
$$

   where $h = L\cos\alpha$.  
   The velocity of the bob is:

$$
\mathbf{v}(t) = -R\omega\sin(\omega t)\,\hat{\mathbf{x}} + R\omega\cos(\omega t)\,\hat{\mathbf{y}}
$$

2. **Angular Momentum $\mathbf{l} = \mathbf{r} \times (m\mathbf{v})$**:

$$
\mathbf{l} = m \begin{vmatrix}
\hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\
R\cos(\omega t) & R\sin(\omega t) & -h \\
-R\omega\sin(\omega t) & R\omega\cos(\omega t) & 0
\end{vmatrix}
$$

$$
\mathbf{l} = m \left[ h R \omega \cos(\omega t)\,\hat{\mathbf{x}} + h R \omega \sin(\omega t)\,\hat{\mathbf{y}} + R^2 \omega\,\hat{\mathbf{z}} \right]
$$

   Notice that $\mathbf{l}$ has a **constant vertical component** $l_z = m R^2 \omega$, but its horizontal components rotate continuously in a circle!

3. **Rate of Change $\frac{d\mathbf{l}}{dt}$**:

$$
\frac{d\mathbf{l}}{dt} = m h R \omega^2 \left[ -\sin(\omega t)\,\hat{\mathbf{x}} + \cos(\omega t)\,\hat{\mathbf{y}} \right]
$$

4. **Torque $\mathbf{\Gamma} = \mathbf{r} \times \mathbf{F}$**:  
   The net force on the bob is the horizontal centripetal force:

$$
\mathbf{F} = -m R \omega^2 \left[ \cos(\omega t)\,\hat{\mathbf{x}} + \sin(\omega t)\,\hat{\mathbf{y}} \right]
$$

   Compute torque about pivot $O$:

$$
\mathbf{\Gamma} = \mathbf{r} \times \mathbf{F} = (-h\,\hat{\mathbf{z}}) \times \mathbf{F} = m h R \omega^2 \left[ -\sin(\omega t)\,\hat{\mathbf{x}} + \cos(\omega t)\,\hat{\mathbf{y}} \right]
$$

   **$\frac{d\mathbf{l}}{dt} = \mathbf{\Gamma}$ matches perfectly!**  
**Physical Insight**: The angular momentum vector is tilted relative to the vertical axis and sweeps out a cone in space (precesses) at frequency $\omega$, driven by the torque acting about the pivot point!

---

### Worked Example 10.2: Orbital and Spin Angular Momentum of a Dumbbell
**Problem**: Two equal masses $m$ are attached to the ends of a rigid massless rod of length $2b$. The center of the rod moves along the $x$-axis with speed $V$, while the rod spins in the $xy$-plane at constant angular rate $\omega$ about its center.  
Find the total angular momentum $\mathbf{L}$ about the origin.

**Solution**:  
Apply the Two-Component Angular Momentum Theorem:

$$
\mathbf{L}_{\text{total}} = \mathbf{L}_{\text{orbital}}(\text{CM}) + \mathbf{L}_{\text{spin}}(\text{about CM})
$$

1. **Orbital Component**:  
   Total mass: $M = 2m$.  
   Center of Mass position: $\mathbf{R} = (Vt)\,\hat{\mathbf{x}}$.  
   Center of Mass velocity: $\mathbf{V}_{\text{cm}} = V\,\hat{\mathbf{x}}$.

$$
\mathbf{L}_{\text{orbital}} = \mathbf{R} \times (M\mathbf{V}_{\text{cm}}) = (Vt\,\hat{\mathbf{x}}) \times (2mV\,\hat{\mathbf{x}}) = \mathbf{0}
$$

   *(Since CM position and velocity are collinear, orbital angular momentum about the origin is zero!)*

2. **Spin Component**:  
   Relative to the Center of Mass, the two masses are at:

$$
\mathbf{r}'_1 = b\cos(\omega t)\,\hat{\mathbf{x}} + b\sin(\omega t)\,\hat{\mathbf{y}}, \quad \mathbf{r}'_2 = -\mathbf{r}'_1
$$

   Their relative velocities are:

$$
\mathbf{v}'_1 = -b\omega\sin(\omega t)\,\hat{\mathbf{x}} + b\omega\cos(\omega t)\,\hat{\mathbf{y}}, \quad \mathbf{v}'_2 = -\mathbf{v}'_1
$$

   Compute spin angular momentum:

$$
\mathbf{l}'_1 = \mathbf{r}'_1 \times (m\mathbf{v}'_1) = m b^2 \omega\,\hat{\mathbf{z}}
$$

$$
\mathbf{l}'_2 = (-\mathbf{r}'_1) \times [m(-\mathbf{v}'_1)] = m b^2 \omega\,\hat{\mathbf{z}}
$$

   Summing over both particles:

$$
\mathbf{L}_{\text{spin}} = \mathbf{l}'_1 + \mathbf{l}'_2 = 2 m b^2 \omega\,\hat{\mathbf{z}}
$$

Therefore:

$$
\mathbf{L}_{\text{total}} = 2 m b^2 \omega\,\hat{\mathbf{z}}
$$

---

### Practice Problem 10.1 (To Solve)
**Statement**: A planet of mass $m$ moves in an elliptical Keplerian orbit around a sun of mass $M$. At perihelion (closest approach), its distance is $r_p$ and its speed is $v_p$. At aphelion (farthest distance), its distance is $r_a$. Find the speed $v_a$ at aphelion in terms of $v_p, r_p, r_a$.
* **Hint**: At both perihelion and aphelion, velocity is purely perpendicular to the position vector ($\mathbf{r} \perp \mathbf{v}$). Angular momentum is conserved: $m r_p v_p = m r_a v_a$.
* **Answer**: $v_a = v_p \left(\frac{r_p}{r_a}\right)$.

---

### Practice Problem 10.2 (To Solve)
**Statement**: A particle of mass $m$ slides on a frictionless horizontal table attached to a light string passing through a small hole in the center. The particle initially orbits in a circle of radius $r_1$ with speed $v_1$. The string is slowly pulled downward through the hole until the radius decreases to $r_2 = r_1 / 2$.  
(a) What is the new orbital speed $v_2$?  
(b) How does the kinetic energy change? What supplied the work?
* **Hint**: The tension force is purely radial, exerting zero torque about the hole. Hence angular momentum is conserved: $m r_1 v_1 = m r_2 v_2$.
* **Answer**: (a) $v_2 = v_1 \left(\frac{r_1}{r_2}\right) = 2 v_1$. (b) $T_2 = \frac{1}{2}m v_2^2 = 4 T_1$. The kinetic energy quadrupled; the work was performed by the external tension pulling the string inward against the centrifugal inertia!

---

## 8. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 3:
  * Sections 3.4–3.5 (pp. 90–99): Angular Momentum, Central Forces, Orbital and Spin Decomposition.
  * Problems 3.21, 3.27, 3.33, 3.37 (pp. 102–104): Angular momentum theorems and torque proofs.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 18: "Principles of Conservation" (Sections 18.3–18.4 on angular momentum).
  * Chapter 20: "Rotation in Space" (Sections 20.1–20.3 on torque and precession).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 6: "Angular Momentum" (Sections 6.1–6.5).\n
