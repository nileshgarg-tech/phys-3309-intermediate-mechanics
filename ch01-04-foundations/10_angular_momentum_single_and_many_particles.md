# 10. Angular Momentum: Single & Multiparticle Systems

**Foundational Story**: Chapter 3, Sections 3.4–3.5  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 3 (pp. 90–99)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 18 & Ch. 20 ("Rotation in Space")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 6

---

## 1. Defining Angular Momentum for a Single Particle

Linear momentum ($\mathbf{p} = m \mathbf{v}$) measures motion along a straight line.  
**Angular momentum** ($\boldsymbol{\ell}$) measures rotational motion about a designated reference origin $O$ (Taylor, Eq. 3.21):

$$
\boldsymbol{\ell} = \mathbf{r} \times \mathbf{p} = \mathbf{r} \times (m\mathbf{v})
$$

Angular momentum is an **axial vector** perpendicular to both the position vector and the velocity vector.  
Its magnitude $\ell = |\boldsymbol{\ell}|$ is:

$$
\ell = r p \sin\theta = r_\perp p = r p_\perp
$$

where $\theta$ is the angle between $\mathbf{r}$ and $\mathbf{p}$, $r_\perp = r\sin\theta$ is the lever arm (or impact parameter), and $p_\perp = p\sin\theta$ is the transverse momentum.

---

## 2. Torque and the Fundamental Rotational Law

What causes angular momentum to change?  
Following Taylor (Sec. 3.4), let us differentiate $\boldsymbol{\ell}$ with respect to time:

$$
\dot{\boldsymbol{\ell}} = \frac{d}{dt}(\mathbf{r} \times \mathbf{p}) = (\dot{\mathbf{r}} \times \mathbf{p}) + (\mathbf{r} \times \dot{\mathbf{p}})
$$

Examine the first term:

$$
\dot{\mathbf{r}} \times \mathbf{p} = \mathbf{v} \times (m\mathbf{v}) = m (\mathbf{v} \times \mathbf{v}) = \mathbf{0}
$$

*(The cross product of any vector with itself is identically zero!)*  
Now examine the second term: by Newton's Second Law, $\dot{\mathbf{p}} = \mathbf{F}$. Therefore:

$$
\dot{\boldsymbol{\ell}} = \mathbf{r} \times \mathbf{F}
$$

Following Taylor (Eq. 3.23), we define the **Torque** (or moment of force) $\boldsymbol{\Gamma}$:

$$
\boldsymbol{\Gamma} = \mathbf{r} \times \mathbf{F}
$$

> **The Rotational Form of Newton's Second Law (Taylor, Eq. 3.24)**:
> 
> $$
> \dot{\boldsymbol{\ell}} = \boldsymbol{\Gamma}
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
\boldsymbol{\Gamma} = \mathbf{r} \times \mathbf{F} = \mathbf{r} \times [f(r)\,\hat{\mathbf{r}}] = f(r)\,[r (\hat{\mathbf{r}} \times \hat{\mathbf{r}})] = \mathbf{0}
$$

Because $\boldsymbol{\Gamma} = \mathbf{0}$:

$$
\dot{\boldsymbol{\ell}} = \mathbf{0} \implies \boldsymbol{\ell} = \mathbf{r} \times (m\mathbf{v}) = \text{constant vector!}
$$

### Consequences of Angular Momentum Conservation:
1. **Planar Motion**: Since $\boldsymbol{\ell}$ is a fixed vector in space, and $\mathbf{r}(t) \cdot \boldsymbol{\ell} = 0$ at all times, the particle's entire trajectory is permanently confined to a 2D plane perpendicular to $\boldsymbol{\ell}$.
2. **Kepler's Second Law (Equal Areas in Equal Times, Taylor Eq. 3.26)**:  
   The area swept out by the position vector in time $dt$ is a triangle of area:

$$
dA = \frac{1}{2} |\mathbf{r} \times d\mathbf{r}| = \frac{1}{2} |\mathbf{r} \times (\mathbf{v}\,dt)| = \frac{\ell}{2m}\,dt
$$

   Dividing by $dt$:

$$
\frac{dA}{dt} = \frac{\ell}{2m} = \text{constant}
$$

   A planet sweeps out equal orbital areas in equal intervals of time.

---

## 4. Total Angular Momentum of a Multiparticle System

Following Taylor (Sec. 3.5), for a collection of $N$ particles indexed by $\alpha = 1, \dots, N$, the **Total Angular Momentum** $\mathbf{L}$ is defined as:

$$
\mathbf{L} = \sum_{\alpha=1}^N \boldsymbol{\ell}_\alpha = \sum_{\alpha=1}^N (\mathbf{r}_\alpha \times \mathbf{p}_\alpha)
$$

Differentiate with respect to time:

$$
\dot{\mathbf{L}} = \sum_{\alpha=1}^N (\mathbf{r}_\alpha \times \dot{\mathbf{p}}_\alpha) = \sum_{\alpha=1}^N (\mathbf{r}_\alpha \times \mathbf{F}_\alpha^{\text{ext}}) + \sum_{\alpha=1}^N \sum_{\beta \neq \alpha} (\mathbf{r}_\alpha \times \mathbf{F}_{\alpha\beta})
$$

Let us inspect the internal torque sum. Grouping mutual action-reaction pairs:

$$
\mathbf{r}_\alpha \times \mathbf{F}_{\alpha\beta} + \mathbf{r}_\beta \times \mathbf{F}_{\beta\alpha} = \mathbf{r}_\alpha \times \mathbf{F}_{\alpha\beta} - \mathbf{r}_\beta \times \mathbf{F}_{\alpha\beta} = (\mathbf{r}_\alpha - \mathbf{r}_\beta) \times \mathbf{F}_{\alpha\beta}
$$

If the internal forces obey Newton's Third Law in its strong form (meaning the mutual forces are central and act along the relative displacement vector $\mathbf{r}_\alpha - \mathbf{r}_\beta$):

$$
(\mathbf{r}_\alpha - \mathbf{r}_\beta) \times \mathbf{F}_{\alpha\beta} = \mathbf{0}
$$

All internal torques cancel pairwise! Defining the net external torque $\boldsymbol{\Gamma}^{\text{ext}} = \sum_\alpha (\mathbf{r}_\alpha \times \mathbf{F}_\alpha^{\text{ext}})$:

$$
\dot{\mathbf{L}} = \boldsymbol{\Gamma}^{\text{ext}}
$$

> **The Multiparticle Angular Momentum Theorem (Taylor, Eq. 3.39)**:  
> If the net external torque is zero ($\boldsymbol{\Gamma}^{\text{ext}} = \mathbf{0}$), the total angular momentum $\mathbf{L}$ of the system is strictly conserved:
> 
> $$
> \mathbf{L} = \text{constant}
> $$

---

## 5. The CM Decomposition: Motion of CM vs. Motion Relative to CM

Here is one of the most elegant theorems in classical mechanics (Taylor, Sec. 3.5, pp. 97–99).  
Let $\mathbf{R}$ be the Center of Mass position, and let $\mathbf{r}'_\alpha$ be the position of particle $\alpha$ **relative to the Center of Mass**:

$$
\mathbf{r}_\alpha = \mathbf{R} + \mathbf{r}'_\alpha
$$

$$
\dot{\mathbf{r}}_\alpha = \dot{\mathbf{R}} + \dot{\mathbf{r}}'_\alpha
$$

Substitute this into the total angular momentum formula:

$$
\mathbf{L} = \sum_{\alpha=1}^N \left[ (\mathbf{R} + \mathbf{r}'_\alpha) \times m_\alpha (\dot{\mathbf{R}} + \dot{\mathbf{r}}'_\alpha) \right]
$$

Expanding the cross products:

$$
\mathbf{L} = (\mathbf{R} \times M\dot{\mathbf{R}}) + \mathbf{R} \times \left(\sum_{\alpha=1}^N m_\alpha \dot{\mathbf{r}}'_\alpha\right) + \left(\sum_{\alpha=1}^N m_\alpha \mathbf{r}'_\alpha\right) \times \dot{\mathbf{R}} + \sum_{\alpha=1}^N (\mathbf{r}'_\alpha \times m_\alpha \dot{\mathbf{r}}'_\alpha)
$$

Notice that by definition of the Center of Mass, $\sum_\alpha m_\alpha \mathbf{r}'_\alpha = \mathbf{0}$ and $\sum_\alpha m_\alpha \dot{\mathbf{r}}'_\alpha = \mathbf{0}$. The two cross-terms vanish identically! We are left with:

$$
\mathbf{L} = (\mathbf{R} \times \mathbf{P}) + \sum_{\alpha=1}^N (\mathbf{r}'_\alpha \times \mathbf{p}'_\alpha)
$$

where $\mathbf{P} = M\dot{\mathbf{R}}$ and $\mathbf{p}'_\alpha = m_\alpha \dot{\mathbf{r}}'_\alpha$.

> **Taylor's Angular Momentum Decomposition Theorem (Eq. 3.42)**:
> 
> $$
> \mathbf{L} = \mathbf{L}(\text{motion of CM}) + \mathbf{L}(\text{motion relative to CM})
> $$
> 
> 1. **$\mathbf{L}(\text{motion of CM}) = \mathbf{R} \times \mathbf{P}$**: The angular momentum of the Center of Mass moving through space about the origin $O$.
> 2. **$\mathbf{L}(\text{motion relative to CM}) = \sum_\alpha (\mathbf{r}'_\alpha \times \mathbf{p}'_\alpha)$**: The intrinsic angular momentum of the system relative to its Center of Mass.

**Example**: The Earth has:
* An orbital angular momentum $\mathbf{R} \times \mathbf{P}$ revolving around the Sun once per 365 days.
* An intrinsic angular momentum relative to its CM rotating around its polar axis once every 24 hours.

---

## 6. Summary Cheat Sheet for Module 10

| Quantity | Formula | Physical Meaning |
|---|---|---|
| **Angular Momentum** | $\boldsymbol{\ell} = \mathbf{r} \times \mathbf{p}$ | Measure of rotational momentum about origin (Taylor, Eq. 3.21) |
| **Torque** | $\boldsymbol{\Gamma} = \mathbf{r} \times \mathbf{F}$ | Moment of force; causes $\boldsymbol{\ell}$ to change (Taylor, Eq. 3.23) |
| **Rotational Law** | $\dot{\boldsymbol{\ell}} = \boldsymbol{\Gamma}$ | Angular counterpart to $\dot{\mathbf{p}} = \mathbf{F}$ (Taylor, Eq. 3.24) |
| **Central Forces** | $\boldsymbol{\Gamma} = \mathbf{0} \implies \boldsymbol{\ell} = \text{const}$ | Produces planar motion & Kepler's 2nd Law ($\dot{A} = \frac{\ell}{2m}$) |
| **Internal Torques** | $\sum_{\alpha < \beta} (\mathbf{r}_\alpha - \mathbf{r}_\beta) \times \mathbf{F}_{\alpha\beta} = \mathbf{0}$ | Cancel out if internal forces are central |
| **CM Decomposition** | $\mathbf{L} = (\mathbf{R} \times \mathbf{P}) + \sum_\alpha (\mathbf{r}'_\alpha \times \mathbf{p}'_\alpha)$ | Motion of CM plus motion relative to CM (Taylor, Eq. 3.42) |

---

## 7. Worked Examples & Practice Problems

### Worked Example 10.1: Angular Momentum of a Conical Pendulum
**Problem**: A bob of mass $m$ hangs from a fixed pivot by a string of length $L$. It moves in a horizontal circle of radius $R = L\sin\alpha$ at constant angular speed $\omega$.  
(a) Find the angular momentum vector $\boldsymbol{\ell}$ of the bob calculated about the **suspension pivot point O**.  
(b) Compute the torque $\boldsymbol{\Gamma}$ about point O, and verify that $\dot{\boldsymbol{\ell}} = \boldsymbol{\Gamma}$.

**Solution**:  
1. **Coordinates**:  
   Let the pivot point be the origin $O$. The position of the bob is:

$$
\mathbf{r}(t) = R\cos(\omega t)\,\hat{\mathbf{x}} + R\sin(\omega t)\,\hat{\mathbf{y}} - h\,\hat{\mathbf{z}}
$$

   where $h = L\cos\alpha$.  
   The velocity of the bob is:

$$
\mathbf{v}(t) = \dot{\mathbf{r}}(t) = -R\omega\sin(\omega t)\,\hat{\mathbf{x}} + R\omega\cos(\omega t)\,\hat{\mathbf{y}}
$$

2. **Angular Momentum $\boldsymbol{\ell} = \mathbf{r} \times (m\mathbf{v})$**:

$$
\boldsymbol{\ell} = m \begin{vmatrix}
\hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\
R\cos(\omega t) & R\sin(\omega t) & -h \\
-R\omega\sin(\omega t) & R\omega\cos(\omega t) & 0
\end{vmatrix}
$$

$$
\boldsymbol{\ell} = m \left[ h R \omega \cos(\omega t)\,\hat{\mathbf{x}} + h R \omega \sin(\omega t)\,\hat{\mathbf{y}} + R^2 \omega\,\hat{\mathbf{z}} \right]
$$

   Notice that $\boldsymbol{\ell}$ has a **constant vertical component** $\ell_z = m R^2 \omega$, but its horizontal components rotate continuously in a circle!

3. **Rate of Change $\dot{\boldsymbol{\ell}}$**:

$$
\dot{\boldsymbol{\ell}} = m h R \omega^2 \left[ -\sin(\omega t)\,\hat{\mathbf{x}} + \cos(\omega t)\,\hat{\mathbf{y}} \right]
$$

4. **Torque $\boldsymbol{\Gamma} = \mathbf{r} \times \mathbf{F}$**:  
   The net force on the bob is the horizontal centripetal force:

$$
\mathbf{F} = -m R \omega^2 \left[ \cos(\omega t)\,\hat{\mathbf{x}} + \sin(\omega t)\,\hat{\mathbf{y}} \right]
$$

   Compute torque about pivot $O$:

$$
\boldsymbol{\Gamma} = \mathbf{r} \times \mathbf{F} = (-h\,\hat{\mathbf{z}}) \times \mathbf{F} = m h R \omega^2 \left[ -\sin(\omega t)\,\hat{\mathbf{x}} + \cos(\omega t)\,\hat{\mathbf{y}} \right]
$$

   **$\dot{\boldsymbol{\ell}} = \boldsymbol{\Gamma}$ matches perfectly!**  
**Physical Insight**: The angular momentum vector is tilted relative to the vertical axis and sweeps out a cone in space (precesses) at frequency $\omega$, driven by the torque acting about the pivot point!

---

### Worked Example 10.2: Angular Momentum Decomposition of a Dumbbell
**Problem**: Two equal masses $m$ are attached to the ends of a rigid massless rod of length $2b$. The center of the rod moves along the $x$-axis with speed $V$, while the rod spins in the $xy$-plane at constant angular rate $\omega$ about its center.  
Find the total angular momentum $\mathbf{L}$ about the origin.

**Solution**:  
Apply Taylor's Angular Momentum Decomposition Theorem (Eq. 3.42):

$$
\mathbf{L} = \mathbf{L}(\text{motion of CM}) + \mathbf{L}(\text{motion relative to CM})
$$

1. **Motion of CM**:  
   Total mass: $M = 2m$.  
   Center of Mass position: $\mathbf{R} = (Vt)\,\hat{\mathbf{x}}$.  
   Center of Mass velocity: $\dot{\mathbf{R}} = V\,\hat{\mathbf{x}}$.

$$
\mathbf{L}(\text{motion of CM}) = \mathbf{R} \times (M\dot{\mathbf{R}}) = (Vt\,\hat{\mathbf{x}}) \times (2mV\,\hat{\mathbf{x}}) = \mathbf{0}
$$

   *(Since CM position and velocity are collinear, the angular momentum of the CM about the origin is zero!)*

2. **Motion Relative to CM**:  
   Relative to the Center of Mass, the two masses ($\alpha = 1, 2$) are at:

$$
\mathbf{r}'_1 = b\cos(\omega t)\,\hat{\mathbf{x}} + b\sin(\omega t)\,\hat{\mathbf{y}}, \quad \mathbf{r}'_2 = -\mathbf{r}'_1
$$

   Their relative velocities are:

$$
\dot{\mathbf{r}}'_1 = -b\omega\sin(\omega t)\,\hat{\mathbf{x}} + b\omega\cos(\omega t)\,\hat{\mathbf{y}}, \quad \dot{\mathbf{r}}'_2 = -\dot{\mathbf{r}}'_1
$$

   Compute angular momentum relative to the CM for each particle:

$$
\boldsymbol{\ell}'_1 = \mathbf{r}'_1 \times (m\dot{\mathbf{r}}'_1) = m b^2 \omega\,\hat{\mathbf{z}}
$$

$$
\boldsymbol{\ell}'_2 = (-\mathbf{r}'_1) \times [m(-\dot{\mathbf{r}}'_1)] = m b^2 \omega\,\hat{\mathbf{z}}
$$

   Summing over both particles:

$$
\mathbf{L}(\text{motion relative to CM}) = \boldsymbol{\ell}'_1 + \boldsymbol{\ell}'_2 = 2 m b^2 \omega\,\hat{\mathbf{z}}
$$

Therefore, the total angular momentum is:

$$
\mathbf{L} = 2 m b^2 \omega\,\hat{\mathbf{z}}
$$

---

### Practice Problem 10.1 (To Solve)
**Statement**: A planet of mass $m$ moves in an elliptical Keplerian orbit around a sun of mass $M$. At perihelion (closest approach), its distance is $r_p$ and its speed is $v_p$. At aphelion (farthest distance), its distance is $r_a$. Find the speed $v_a$ at aphelion in terms of $v_p, r_p, r_a$.

**Hint**: At both perihelion and aphelion, velocity is purely perpendicular to the position vector ($\mathbf{r} \perp \mathbf{v}$). The angular momentum magnitude $\ell = |\boldsymbol{\ell}|$ is conserved:

$$
m r_p v_p = m r_a v_a
$$

**Answer**:

$$
v_a = v_p \left(\frac{r_p}{r_a}\right)
$$

---

### Practice Problem 10.2 (To Solve)
**Statement**: A particle of mass $m$ slides on a frictionless horizontal table attached to a light string passing through a small hole in the center. The particle initially orbits in a circle of radius $r_1$ with speed $v_1$. The string is slowly pulled downward through the hole until the radius decreases to $r_2 = r_1 / 2$.  
(a) What is the new orbital speed $v_2$?  
(b) How does the kinetic energy change? What supplied the work?

**Hint**: The tension force is purely radial, exerting zero torque about the hole ($\boldsymbol{\Gamma} = \mathbf{0}$). Hence angular momentum magnitude is conserved:

$$
\ell = m r_1 v_1 = m r_2 v_2
$$

**Answer**:
(a) New speed:

$$
v_2 = v_1 \left(\frac{r_1}{r_2}\right) = 2 v_1
$$

(b) Kinetic energy:

$$
T_2 = \frac{1}{2}m v_2^2 = 4 T_1
$$

The kinetic energy quadrupled; the work was performed by the external tension pulling the string inward against centrifugal inertia!

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
