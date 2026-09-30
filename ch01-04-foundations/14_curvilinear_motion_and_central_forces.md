# 14. Curvilinear 1D Systems & Central Forces

**Foundational Story**: Chapter 4, Sections 4.7–4.8  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 142–152)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 14

---

## 1. Motion Constrained to a Curve: The Bead on a Wire

Consider a bead of mass $m$ sliding frictionlessly along a curved wire in space, or a roller coaster on a track.  
Even though the track bends and twists through 3D space, **the particle has only one degree of freedom**: its distance $s$ measured along the track.

The net force on the bead has two components:
1. Applied active force $\mathbf{F}_{\text{applied}}$ (e.g. gravity).
2. Normal constraint force $\mathbf{N}$ exerted by the track perpendicular to the wire.

What makes constraint problems so simple in energy mechanics?

$$
\mathbf{N} \perp d\mathbf{r} \implies \mathbf{N} \cdot d\mathbf{r} = 0
$$

> **The Constraint Force Principle**:  
> **Frictionless constraint forces do zero work!**  
> Therefore, normal forces can be completely ignored when computing mechanical energy conservation:
> 
> $$
> E = \frac{1}{2} m \left(\frac{ds}{dt}\right)^2 + U(s) = \text{constant}
> $$
> 
> Any 1D constrained motion reduces mathematically to the exact same energy equation we analyzed in Module 13!

---

## 2. Central Forces: Kinetic Energy in Polar Coordinates

Now consider a particle of mass $m$ subject to a central force $\mathbf{F} = f(r)\,\hat{\mathbf{r}}$.  
In Module 03, we derived the velocity in plane polar coordinates:

$$
\mathbf{v} = \dot{r}\,\hat{\mathbf{r}} + r\dot{\theta}\,\hat{\boldsymbol{\theta}}
$$

The kinetic energy is:

$$
T = \frac{1}{2} m v^2 = \frac{1}{2} m (\dot{r}^2 + r^2\dot{\theta}^2)
$$

The potential energy depends only on radial distance $r$: $U = U(r)$.  
Total energy is:

$$
E = \frac{1}{2} m \dot{r}^2 + \frac{1}{2} m r^2 \dot{\theta}^2 + U(r)
$$

At first glance, this equation contains two variables: $r(t)$ and $\theta(t)$.  
How do we reduce it to a one-dimensional problem?

---

## 3. The Effective Potential $U_{\text{eff}}(r)$

Recall from Module 10 that for any central force, **angular momentum is strictly conserved**:

$$
l = m r^2 \dot{\theta} = \text{constant} \implies \dot{\theta} = \frac{l}{m r^2}
$$

Now, substitute this expression for $\dot{\theta}$ into the kinetic energy:

$$
T_{\text{angular}} = \frac{1}{2} m r^2 \dot{\theta}^2 = \frac{1}{2} m r^2 \left( \frac{l}{m r^2} \right)^2 = \frac{l^2}{2 m r^2}
$$

Substitute this back into the total energy equation:

$$
E = \frac{1}{2} m \dot{r}^2 + \left[ \frac{l^2}{2 m r^2} + U(r) \right]
$$

Look at this equation carefully:
* The first term $\frac{1}{2} m \dot{r}^2$ is the **pure radial kinetic energy**.
* The bracketed term depends **only on $r$**!

We define the **Effective Potential**:

$$
U_{\text{eff}}(r) = U(r) + \frac{l^2}{2 m r^2}
$$

The total energy equation becomes:

$$
E = \frac{1}{2} m \dot{r}^2 + U_{\text{eff}}(r) = \text{constant}
$$

> **The Central Force Reduction**:  
> **A two-dimensional central-force problem is mathematically identical to a one-dimensional particle moving in the effective potential $U_{\text{eff}}(r)$!**

---

## 4. The Centrifugal Barrier

The term:

$$
U_{\text{cf}}(r) = \frac{l^2}{2 m r^2}
$$

is called the **Centrifugal Potential**.  
Taking its negative derivative with respect to $r$:

$$
F_{\text{cf}} = -\frac{d}{dr} \left( \frac{l^2}{2 m r^2} \right) = +\frac{l^2}{m r^3} = m r \dot{\theta}^2
$$

This is the outward centrifugal force!  
As $r \to 0$, $U_{\text{cf}} \to +\infty$ scaling as $1/r^2$.
* For an attractive gravitational potential $U(r) = -\frac{GMm}{r}$, as $r \to 0$, the centrifugal barrier $+l^2/(2mr^2)$ diverges faster than $-1/r$.
* **The centrifugal barrier prevents any particle with non-zero angular momentum ($l \neq 0$) from crashing into the center of attraction!**

---

## 5. Summary Cheat Sheet for Module 14

| Concept | Mathematical Statement | Core Takeaway |
|---|---|---|
| **Constraint Work** | $\mathbf{N} \cdot d\mathbf{r} = 0$ | Frictionless track forces do zero work |
| **Polar Kinetic Energy** | $T = \frac{1}{2}m\dot{r}^2 + \frac{1}{2}mr^2\dot{\theta}^2$ | Split into radial + angular parts |
| **Angular Momentum** | $\dot{\theta} = \frac{l}{mr^2}$ | Eliminates angular velocity from energy |
| **Effective Potential** | $U_{\text{eff}}(r) = U(r) + \frac{l^2}{2mr^2}$ | Absorbs angular kinetic energy into potential |
| **Equivalent 1D Problem**| $E = \frac{1}{2}m\dot{r}^2 + U_{\text{eff}}(r)$ | Radial motion mapped to standard 1D well |

---

## 6. Worked Examples & Practice Problems

### Worked Example 14.1: The Vertical Loop-the-Loop Roller Coaster
**Problem**: A small roller coaster car of mass $m$ slides frictionlessly along a track that loops vertically in a circle of radius $R$. The car is released from rest at height $h$ above the bottom of the loop.  
(a) What is the minimum release height $h_{\text{min}}$ so that the car maintains contact with the track at the very top of the loop?  
(b) If released from $h = 3R$, what normal force does the track exert on the car at the bottom of the loop?

**Solution**:  
1. **At the Top of the Loop (Height $2R$)**:  
   By energy conservation between release at height $h$ and the top of the loop:

$$
m g h = m g (2R) + \frac{1}{2} m v_{\text{top}}^2 \implies v_{\text{top}}^2 = 2 g (h - 2R)
$$

   At the top, both gravity and the normal track force $N$ point downward:

$$
m g + N = m \frac{v_{\text{top}}^2}{R} \implies N = m \frac{v_{\text{top}}^2}{R} - m g
$$

   To maintain contact without falling, the normal force must be non-negative ($N \ge 0$):

$$
m \frac{v_{\text{top}}^2}{R} \ge m g \implies v_{\text{top}}^2 \ge g R
$$

   Substitute $v_{\text{top}}^2$:

$$
2 g (h_{\text{min}} - 2R) = g R \implies 2h_{\text{min}} - 4R = R \implies h_{\text{min}} = \frac{5}{2} R = 2.5 R
$$

2. **At the Bottom of the Loop (Height $0$, with $h = 3R$)**:  
   Energy conservation:

$$
m g (3R) = \frac{1}{2} m v_{\text{bot}}^2 \implies v_{\text{bot}}^2 = 6 g R
$$

   At the bottom, normal force points upward, gravity downward:

$$
N - m g = m \frac{v_{\text{bot}}^2}{R} \implies N = m g + m \frac{6 g R}{R} = 7 m g
$$

**Physical Insight**: The track must push upward with a force of **$7$ times the car's weight** at the bottom of the loop!

---

### Worked Example 14.2: Effective Potential of a Planetary Orbit
**Problem**: For a planet of mass $m$ orbiting the Sun of mass $M$ with angular momentum $l$:  
The gravitational potential is $U(r) = -\frac{k}{r}$, where $k = G M m$.  
(a) Write down the effective potential $U_{\text{eff}}(r)$.  
(b) Find the radius $r_0$ of a circular orbit.  
(c) Show that this circular orbit is stable against small radial perturbations.

**Solution**:  
(a) The effective potential is:

$$
U_{\text{eff}}(r) = -\frac{k}{r} + \frac{l^2}{2 m r^2}
$$

(b) Circular orbit occurs at the minimum of $U_{\text{eff}}(r)$ where $\frac{dU_{\text{eff}}}{dr} = 0$:

$$
\frac{dU_{\text{eff}}}{dr} = \frac{k}{r^2} - \frac{l^2}{m r^3} = 0
$$

Multiply by $r^3$:

$$
k r_0 - \frac{l^2}{m} = 0 \implies r_0 = \frac{l^2}{m k} = \frac{l^2}{G M m^2}
$$

(c) Check stability via second derivative:

$$
\frac{d^2U_{\text{eff}}}{dr^2} = -\frac{2k}{r^3} + \frac{3l^2}{m r^4}
$$

Evaluate at $r_0 = \frac{l^2}{mk}$ (so $\frac{l^2}{m r_0^4} = \frac{k}{r_0^3}$):

$$
\left. \frac{d^2U_{\text{eff}}}{dr^2} \right|_{r_0} = -\frac{2k}{r_0^3} + \frac{3k}{r_0^3} = +\frac{k}{r_0^3} > 0
$$

Because $\frac{d^2U_{\text{eff}}}{dr^2} > 0$, the circular orbit corresponds to a **stable potential valley**. A small radial nudge causes the planet to oscillate around $r_0$ (an elliptical orbit!).

---

### Practice Problem 14.1 (To Solve)
**Statement**: A bead of mass $m$ slides on a frictionless wire bent in the shape of a parabola $y = c x^2$ in a uniform vertical gravitational field $g$. Find the frequency $\omega$ of small oscillations about the bottom of the wire at $x = 0$.
* **Hint**: Near $x = 0$, $ds = \sqrt{1 + (dy/dx)^2}\,dx = \sqrt{1 + 4c^2 x^2}\,dx \approx dx$. Potential energy $U(x) = m g y = m g c x^2 = \frac{1}{2}(2 m g c) x^2$.
* **Answer**: $k_{\text{eff}} = 2 m g c \implies \omega = \sqrt{\frac{k_{\text{eff}}}{m}} = \sqrt{2 g c}$.

---

### Practice Problem 14.2 (To Solve)
**Statement**: A particle of mass $m$ moves in an attractive central force $\mathbf{F}(r) = -\frac{k}{r^3}\,\hat{\mathbf{r}}$ (inverse-cube force). Show that circular orbits exist only if $l^2 = m k$, and prove that such orbits are neutrally stable or unstable.
* **Hint**: $U(r) = -\frac{k}{2r^2}$. Effective potential $U_{\text{eff}}(r) = -\frac{k}{2r^2} + \frac{l^2}{2mr^2} = \frac{l^2 - mk}{2mr^2}$.
* **Answer**: If $l^2 = mk$, then $U_{\text{eff}}(r) = 0$ everywhere (flat line). If nudged, the particle either spirals directly into the origin or flies away to infinity. No bound stable orbits exist in an inverse-cube force!

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Sections 4.7–4.8 (pp. 142–152): Curvilinear 1D Systems, Central Forces, Effective Potential.
  * Problems 4.38, 4.43, 4.45 (pp. 170–172): Central force effective potential problems.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 14: "Work and Potential Energy (Conclusion)" (Section 14.5 on central force fields).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.8–5.9).\n
