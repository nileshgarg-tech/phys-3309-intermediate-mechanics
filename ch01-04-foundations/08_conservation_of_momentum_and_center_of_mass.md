# 08. Conservation of Momentum & Center of Mass

**Foundational Story**: Chapter 3, Sections 3.1 & 3.3  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 3 (pp. 83–85, 87–90)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 18 ("Principles of Conservation") & Ch. 19 ("Center of Mass")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 3

---

## 1. The Multiparticle Problem: From Atoms to Planets

Real objects are not single mathematical points. A baseball contains $\sim 10^{25}$ interacting atoms; the solar system contains a massive central star, 8 major planets, moons, asteroids, and comets, all gravitationally pulling on each other simultaneously.

How can Newtonian mechanics make sense of such enormous systems without solving $10^{25}$ coupled differential equations?

The answer lies in **internal force cancellation** and the **Center of Mass**.

---

## 2. Internal vs. External Forces

Consider an assembly of $N$ particles ($\alpha = 1, 2, \dots, N$), each with mass $m_\alpha$ and position vector $\mathbf{r}_\alpha$.
The total force acting on particle $\alpha$ consists of two distinct parts:

$$
\mathbf{F}_\alpha = \mathbf{F}_\alpha^{\text{ext}} + \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta}
$$

1. **$\mathbf{F}_\alpha^{\text{ext}}$ (External Force)**: Forces exerted on particle $\alpha$ by agents outside the system (e.g., Earth's gravity, an external magnetic field).
2. **$\mathbf{F}_{\alpha\beta}$ (Internal Force)**: The force exerted on particle $\alpha$ by particle $\beta$ inside the system.

Now, write Newton's Second Law for particle $\alpha$:

$$
\dot{\mathbf{p}}_\alpha = \mathbf{F}_\alpha^{\text{ext}} + \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta}
$$

Sum this equation over all $N$ particles in the system:

$$
\sum_{\alpha=1}^N \dot{\mathbf{p}}_\alpha = \sum_{\alpha=1}^N \mathbf{F}_\alpha^{\text{ext}} + \sum_{\alpha=1}^N \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta}
$$

---

## 3. The Miracle of Newton's Third Law

Look closely at the double summation of internal forces:

$$
\sum_{\alpha=1}^N \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta}
$$

This sum contains terms like $(\mathbf{F}_{12} + \mathbf{F}_{21}) + (\mathbf{F}_{13} + \mathbf{F}_{31}) + \dots$.
By Newton's Third Law of Motion:

$$
\mathbf{F}_{\alpha\beta} = -\mathbf{F}_{\beta\alpha} \implies \mathbf{F}_{\alpha\beta} + \mathbf{F}_{\beta\alpha} = \mathbf{0}
$$

Every single internal interaction cancels pairwise!

$$
\sum_{\alpha=1}^N \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta} = \mathbf{0}
$$

Therefore, defining the **Total Linear Momentum** $\mathbf{P} = \sum_{\alpha=1}^N \mathbf{p}_\alpha$ and the total external force $\mathbf{F}^{\text{ext}} = \sum_{\alpha=1}^N \mathbf{F}_\alpha^{\text{ext}}$:

$$
\dot{\mathbf{P}} = \mathbf{F}^{\text{ext}}
$$

> **The System Momentum Conservation Theorem (Taylor, Eq. 3.7)**:  
> **Internal forces, no matter how violent, complex, or explosive, cannot change the total momentum of a system.**  
> Only an external force can alter the total momentum. If $\mathbf{F}^{\text{ext}} = \mathbf{0}$, then $\mathbf{P} = \text{constant}$.

---

## 4. The Center of Mass (CM)

Following Taylor (Sec. 3.3), we define the total mass of the system:

$$
M = \sum_{\alpha=1}^N m_\alpha
$$

The **Center of Mass position vector** $\mathbf{R}$ is the mass-weighted average position:

$$
\mathbf{R} = \frac{1}{M} \sum_{\alpha=1}^N m_\alpha \mathbf{r}_\alpha
$$

Differentiating with respect to time gives the Center of Mass velocity $\dot{\mathbf{R}}$:

$$
\dot{\mathbf{R}} = \frac{1}{M} \sum_{\alpha=1}^N m_\alpha \dot{\mathbf{r}}_\alpha = \frac{1}{M} \sum_{\alpha=1}^N \mathbf{p}_\alpha = \frac{\mathbf{P}}{M}
$$

Rearranging:

$$
\mathbf{P} = M \dot{\mathbf{R}}
$$

The total momentum of any complex system is simply the total mass multiplied by the velocity of the Center of Mass!

Differentiating once more with respect to time:

$$
M \ddot{\mathbf{R}} = \dot{\mathbf{P}} = \mathbf{F}^{\text{ext}}
$$

> **The Center of Mass Theorem (Taylor, Eq. 3.12)**:  
> **The center of mass of any system of particles moves exactly like a single point particle of mass $M$ acted upon by the net external force $\mathbf{F}^{\text{ext}}$.**

### Physical Example: The Exploding Artillery Shell
Suppose an artillery shell is fired along a parabolic arc under gravity. Midway through its flight, an internal charge detonates, blowing the shell into hundreds of jagged shrapnel fragments traveling in all directions.
* The fragments fly chaotically.
* Yet because the explosion is purely internal ($\mathbf{F}_{\alpha\beta}$), **the Center of Mass of all the scattered fragments continues along the exact same original parabolic trajectory as if nothing happened!**

---

## 5. Continuous Bodies

For a continuous solid body with mass density $\varrho(\mathbf{r})$ (or $\rho(\mathbf{r})$), the sum becomes an integral (Taylor, Eq. 3.14):

$$
\mathbf{R} = \frac{1}{M} \int \mathbf{r} \, dm = \frac{1}{M} \int \mathbf{r} \varrho \, dV
$$

where $M = \int dm = \int \varrho \, dV$.

---

## 6. Summary Cheat Sheet for Module 08

| Concept | Formula | Physical Interpretation |
|---|---|---|
| **Center of Mass (Discrete)** | $\mathbf{R} = \frac{1}{M} \sum_\alpha m_\alpha \mathbf{r}_\alpha$ | Mass-weighted geometric center |
| **Center of Mass (Continuous)**| $\mathbf{R} = \frac{1}{M} \int \mathbf{r} \, dm$ | Volume integral over mass distribution |
| **Total Momentum** | $\mathbf{P} = M \dot{\mathbf{R}}$ | Total mass moving at CM velocity |
| **Internal Cancellation** | $\sum_{\alpha} \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta} = \mathbf{0}$ | By Newton's 3rd Law, internal forces cannot alter $\mathbf{P}$ |
| **Center of Mass Motion** | $M \ddot{\mathbf{R}} = \mathbf{F}^{\text{ext}}$ | CM ignores internal interactions entirely |

---

## 7. Worked Examples & Practice Problems

### Worked Example 8.1: The Man on a Sliding Ice Raft
**Problem**: A man of mass $m = 80\text{ kg}$ stands at the left end of a flat rectangular wooden raft of mass $M = 120\text{ kg}$ and length $L = 6.0\text{ meters}$. The raft rests on a frictionless sheet of frozen ice.  
The man walks steadily from the left end of the raft to the right end and stops.  
(a) How far does the raft move across the ice during this walk?  
(b) How far does the man move relative to the ice?

**Solution**:  
1. **System Identification**:  
   Consider the closed system (Man + Raft). Because the ice surface is frictionless, **there is zero net external horizontal force on the system**:

$$
F_{\text{net},x}^{\text{ext}} = 0 \implies X_{\text{cm}} = \text{constant}
$$

   The Center of Mass of the entire system cannot move relative to the ice.

2. **Center of Mass Coordinates**:  
   Choose the initial position of the left edge of the raft as the coordinate origin $x = 0$.
   * Initial position of the man: $x_{m1} = 0$.
   * Initial center of mass of the uniform raft: $x_{r1} = L / 2$.

   The initial center of mass of the system is:

$$
X_{\text{cm}} = \frac{m x_{m1} + M x_{r1}}{m + M} = \frac{M (L/2)}{m + M}
$$

3. **Final Positions**:  
   Let the raft shift to the left by a distance $d$ (so its left edge is at $-d$).
   * Final position of the raft's center: $x_{r2} = L/2 - d$.
   * The man walked to the right end of the raft, so his final position is: $x_{m2} = L - d$.

   The final Center of Mass is:

$$
X_{\text{cm}} = \frac{m (L - d) + M (L/2 - d)}{m + M}
$$

4. **Equating Initial and Final CM**:

$$
M \left(\frac{L}{2}\right) = m (L - d) + M \left(\frac{L}{2} - d\right)
$$

$$
0 = m L - (m + M) d \implies d = \left(\frac{m}{m + M}\right) L
$$

   Substitute the numerical values ($m = 80\text{ kg}$, $M = 120\text{ kg}$, $L = 6.0\text{ m}$):

$$
d = \left(\frac{80}{80 + 120}\right) \times 6.0 = \frac{80}{200} \times 6.0 = 2.40\text{ meters}
$$

(a) The raft moves **$2.40\text{ meters}$ to the left**.  
(b) The man's displacement relative to the ice is:

$$
\Delta x_{\text{man}} = L - d = 6.0 - 2.40 = 3.60\text{ meters to the right}
$$

**Physical Insight**: Because internal forces cannot accelerate the Center of Mass, pushing the raft backward with his feet moves the raft by $2.4\text{ m}$ while moving the man forward by $3.6\text{ m}$, keeping the CM pinned in place.

---

### Worked Example 8.2: Center of Mass of a Solid Hemisphere
**Problem**: Calculate the center of mass of a solid, uniform hemisphere of radius $R$ and constant mass density $\rho$.

**Solution**:  
Place the flat base of the hemisphere on the $xy$-plane centered at the origin, with the dome extending into $z \ge 0$.  
By azimuthal symmetry around the $z$-axis:

$$
X_{\text{cm}} = 0, \quad Y_{\text{cm}} = 0
$$

We only need to calculate $Z_{\text{cm}}$:

$$
Z_{\text{cm}} = \frac{1}{M} \int z \, dm
$$

Divide the hemisphere into thin horizontal circular slices of thickness $dz$ at height $z$ ($0 \le z \le R$).  
The radius of a circular disk at height $z$ is $r(z) = \sqrt{R^2 - z^2}$. The volume of this disk slice is:

$$
dV = \pi r(z)^2 dz = \pi (R^2 - z^2) dz
$$

$$
dm = \rho \, dV = \rho \pi (R^2 - z^2) dz
$$

The total mass of the hemisphere is:

$$
M = \rho \left(\frac{2}{3}\pi R^3\right)
$$

Now compute the numerator integral:

$$
\int z \, dm = \rho \pi \int_0^R z (R^2 - z^2) \, dz = \rho \pi \left[ \frac{1}{2} R^2 z^2 - \frac{1}{4} z^4 \right]_0^R = \rho \pi \left(\frac{1}{4} R^4\right)
$$

Divide by total mass $M$:

$$
Z_{\text{cm}} = \frac{\rho \pi \frac{1}{4} R^4}{\rho \frac{2}{3} \pi R^3} = \frac{1/4}{2/3} R = \frac{3}{8} R
$$

**Physical Result**: The Center of Mass of a solid hemisphere lies on its symmetry axis at a distance of **$\frac{3}{8} R = 0.375 R$** from the flat base.

---

### Practice Problem 8.1 (To Solve)
**Statement**: A projectile of mass $M$ is fired with launch speed $v_0$ at an angle $\theta$ above the horizontal. At the very apex of its trajectory, the projectile explodes into two equal fragments of mass $m_1 = m_2 = M / 2$. One fragment falls vertically downward from rest immediately after the explosion. How far from the launch point does the second fragment land?
* **Hint**: The internal explosion cannot change the motion of the Center of Mass. The CM lands at the standard range $R_{\text{cm}} = \frac{v_0^2 \sin(2\theta)}{g}$. At the moment of landing, fragment 1 is on the ground at $x_1 = R_{\text{cm}} / 2$.
* **Answer**: $X_{\text{cm}} = \frac{x_1 + x_2}{2} \implies R_{\text{cm}} = \frac{R_{\text{cm}}/2 + x_2}{2} \implies x_2 = \frac{3}{2} R_{\text{cm}}$. The second fragment lands at 1.5 times the normal projectile range!

---

### Practice Problem 8.2 (To Solve)
**Statement**: Find the center of mass of a thin uniform wire of total mass $M$ bent into a semicircle of radius $R$ lying in the $xy$-plane ($y \ge 0$).
* **Hint**: Parametrize the wire in polar coordinates: $x = R\cos\theta$, $y = R\sin\theta$, $dl = R\,d\theta$ for $\theta \in [0, \pi]$. Mass per unit length $\lambda = M / (\pi R)$.
* **Answer**: $X_{\text{cm}} = 0$, and:

$$
Y_{\text{cm}} = \frac{1}{M} \int_0^{\pi} (R\sin\theta) \left(\frac{M}{\pi R}\right) R \, d\theta = \frac{R}{\pi} [-\cos\theta]_0^\pi = \frac{2R}{\pi} \approx 0.637 R
$$

---

## 8. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 3:
  * Sections 3.1 & 3.3 (pp. 83–85, 87–90): Conservation of Momentum, Center of Mass.
  * Problems 3.1, 3.4, 3.8, 3.11 (pp. 99–101): Center of mass integrations and multi-particle systems.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 18: "Principles of Conservation" (Sections 18.1–18.2).
  * Chapter 19: "Center of Mass; Moment of Inertia" (Section 19.1).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 3: "Forces and Equations of Motion" & Chapter 4: "Momentum" (Sections 4.1–4.4).\n
