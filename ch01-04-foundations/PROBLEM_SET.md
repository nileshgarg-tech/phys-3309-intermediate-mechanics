# Master Problem Set: Chapters 1–4 (Foundations of Classical Mechanics)

**Course**: UH PHYS 3309 — Intermediate Mechanics  
**Textbook**: *Classical Mechanics* (2005) by John R. Taylor  
**Supplementary References**:
* Richard P. Feynman, *The Feynman Lectures on Physics*, Vol. 1 (Ch. 8–14, 18–20, 22, 41)
* Daniel Kleppner & Robert Kolenkow, *An Introduction to Mechanics* (Ch. 1–6)
* David Morin, *Introduction to Classical Mechanics* (Ch. 1–5)

---

## Overview

This master problem set consolidates the fundamental concepts from **Chapters 1 through 4**. 
Each problem has been chosen to reflect realistic junior-level exam questions at the level of PHYS 3309, challenging your physical intuition and mathematical mastery of:
1. Polar kinematics and moving coordinate bases
2. Viscous (linear) and turbulent (quadratic) drag dynamics
3. Magnetic forces and complex coordinate representations
4. Variable-mass systems (rockets and mass accumulation)
5. Multi-particle momentum and Center of Mass theorems
6. Angular momentum, torque, and planar central-force conservation
7. Work, line integrals, and the curl test for conservative forces
8. 1D potential wells, energy diagrams, and small-oscillation approximations
9. Central-force effective potentials and two-body reduced mass decoupling

> [!TIP]
> **Complete Solutions Document**:  
> Detailed, step-by-step analytical derivations, calculations, and physical takeaways for all problems are available in [PROBLEM_SET_SOLUTIONS.md](PROBLEM_SET_SOLUTIONS.md).

---

## Problem 1: Polar Kinematics & The Rotating Wire (Chapter 1)

### Problem Statement
A small bead of mass $m$ slides frictionlessly along a straight rigid wire rod. The rod is pivoted at the origin and is forced by an external motor to rotate in a horizontal plane with constant angular speed $\omega$ ($\phi(t) = \omega t$).
At time $t = 0$, the bead is released from rest relative to the rod at distance $r(0) = r_0$ with $\dot{r}(0) = 0$.
1. Using 2D plane polar coordinates $(r, \phi)$, write down Newton's Second Law for both the radial ($\hat{\mathbf{r}}$) and azimuthal ($\hat{\boldsymbol{\phi}}$) directions.
2. Solve the radial equation of motion to find the bead's distance from the pivot $r(t)$ for all future time.
3. Determine the transverse normal constraint force $N(t) = F_\phi(t)$ exerted by the rod on the bead as a function of time.


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-1-polar-kinematics-the-rotating-wire-chapter-1)


---

## Problem 2: Linear Drag & The Range Correction (Chapter 2)

### Problem Statement
A cannon fires a projectile of mass $m$ with initial launch speed $v_0$ at an angle $\theta$ above a flat horizontal plain in a medium providing linear air drag $\mathbf{f} = -b\mathbf{v}$.
1. Write down the horizontal and vertical positions $x(t)$ and $y(t)$.
2. Assuming the drag is weak ($t / \tau \ll 1$, where $\tau = m/b$), show via Taylor series expansion that the horizontal range $R$ is approximately given by the vacuum range $R_{\text{vac}}$ minus a first-order drag penalty:

$$
R \approx R_{\text{vac}} \left[ 1 - \frac{4}{3} \frac{v_0 \sin\theta}{g\tau} \right]
$$


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-2-linear-drag-the-range-correction-chapter-2)


---

## Problem 3: Vertical Fall with Quadratic Drag (Chapter 2)

### Problem Statement
A basketball of mass $m = 0.62\text{ kg}$ and diameter $D = 0.24\text{ m}$ is dropped from the roof of a tall building.
Taking quadratic drag coefficient $c = \frac{1}{2} C_D \rho A \approx 0.035\text{ N}\cdot\text{s}^2\text{/m}^2$:
1. Calculate the terminal speed $v_{\text{ter}}$ and characteristic time $\tau$.
2. Find the exact time $t_{50}$ and distance $y_{50}$ at which the basketball reaches $50\%$ of its terminal speed.
3. Compare the distance fallen $y_{50}$ with the distance a ball would fall in a vacuum in the same time.


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-3-vertical-fall-with-quadratic-drag-chapter-2)


---

## Problem 4: Relativistic Velocity Selector & Complex Vectors (Chapter 2)

### Problem Statement
A beam of ions of mass $m$ and charge $q$ enters a region with constant crossed fields $\mathbf{E} = E\,\hat{\mathbf{y}}$ and $\mathbf{B} = B\,\hat{\mathbf{z}}$.
Show that an ion entering with velocity $\mathbf{v}_0 = \left(\frac{E}{B}\right)\hat{\mathbf{x}}$ travels undeflected in a straight line, and determine the exact trajectory of an ion that enters with a slightly different velocity $\mathbf{v}_0 = \left(\frac{E}{B} + \delta v\right)\hat{\mathbf{x}}$.


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-4-relativistic-velocity-selector-complex-vectors-chapter-2)


---

## Problem 5: The Tsiolkovsky Rocket with Gravity (Chapter 3)

### Problem Statement
A Saturn V rocket of initial launch mass $m_0 = 2.8 \times 10^6\text{ kg}$ burns fuel at a constant rate $k = -\dot{m} = 1.4 \times 10^4\text{ kg/s}$ for a total burn time $t_b = 150\text{ s}$. The engine has an effective exhaust speed $v_{\text{ex}} = 2600\text{ m/s}$.
Assuming vertical flight in uniform gravity $g = 9.8\text{ m/s}^2$:
1. Find the rocket's velocity $v(t_b)$ at engine burnout.
2. Find the altitude $y(t_b)$ reached at burnout.
3. Calculate the percentage of final speed lost to gravity drag.


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-5-the-tsiolkovsky-rocket-with-gravity-chapter-3)


---

## Problem 6: Two Interacting Gliders & Center of Mass (Chapter 3)

### Problem Statement
Two carts of masses $m_1 = 1.0\text{ kg}$ and $m_2 = 3.0\text{ kg}$ rest on a frictionless horizontal air track. Cart 1 has a compressed massless spring attached to its front bumper with spring constant $k = 300\text{ N/m}$.
Cart 1 is launched with initial speed $v_0 = 4.0\text{ m/s}$ toward stationary cart 2.
1. Find the velocity $V_{\text{cm}}$ of the Center of Mass.
2. Find the maximum compression $x_{\text{max}}$ of the spring during the collision.
3. Find the final velocities of both carts after the spring completely releases.


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-6-two-interacting-gliders-center-of-mass-chapter-3)


---

## Problem 7: Angular Momentum of a Sliding Puck on a String (Chapter 3)

### Problem Statement
A puck of mass $m$ on a frictionless horizontal table is attached to a string passing through a hole in the center. The puck orbits in a circle of radius $r_1$ with speed $v_1$.
The string is slowly pulled downward through the hole until the radius decreases to $r_2 = r_1 / 3$.
1. Calculate the final speed $v_2$.
2. Compute the work $W$ done by the tension force pulling the string, and show that $W = \Delta T$.


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-7-angular-momentum-of-a-sliding-puck-on-a-string-chapter-3)


---

## Problem 8: The Multivariable Curl Test & Non-Conservative Loops (Chapter 4)

### Problem Statement
Consider the force field:

$$
\mathbf{F}(x, y) = (x^2 + a y)\,\hat{\mathbf{x}} + (2x + y^2)\,\hat{\mathbf{y}}
$$

1. Determine the value of the constant $a$ for which the force field is conservative.
2. For that value of $a$, calculate the potential energy function $U(x, y)$ with $U(0, 0) = 0$.
3. If $a = 5$, compute the work done around a closed unit square path $(0,0) \to (1,0) \to (1,1) \to (0,1) \to (0,0)$.


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-8-the-multivariable-curl-test-non-conservative-loops-chapter-4)


---

## Problem 9: The Lennard-Jones Potential & Oscillation Period (Chapter 4)

### Problem Statement
A diatomic molecule is modeled by the Lennard-Jones potential:

$$
U(r) = U_0 \left[ \left(\frac{r_0}{r}\right)^{12} - 2 \left(\frac{r_0}{r}\right)^6 \right]
$$

1. Calculate the minimum potential energy $U_{\text{min}}$ and the equilibrium radius $r_0$.
2. Expand $U(r)$ to quadratic order about $r = r_0$ to find the effective spring constant $k_{\text{eff}}$.
3. If the reduced mass of the molecule is $\mu = 1.2 \times 10^{-26}\text{ kg}$, $U_0 = 1.0 \times 10^{-20}\text{ J}$, and $r_0 = 0.35\text{ nm}$, find the vibrational frequency in Terahertz (THz).


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-9-the-lennard-jones-potential-oscillation-period-chapter-4)


---

## Problem 10: Central Force Effective Potential & Orbital Stability (Chapter 4)

### Problem Statement
A particle of mass $m$ moves under the influence of an attractive central force:

$$
\mathbf{F}(r) = -\left(\frac{k}{r^n}\right) \hat{\mathbf{r}} \quad (\text{where } k > 0 \text{ and } n \text{ is an arbitrary power})
$$

1. Find the potential energy function $U(r)$.
2. Write down the effective potential $U_{\text{eff}}(r)$ for a particle with angular momentum $\ell$.
3. Find the radius $r_0$ of a circular orbit.
4. Prove that a stable circular orbit can exist **only if $n < 3$** (Bertrand's Theorem criterion).


[View Step-by-Step Solution & Physical Takeaway →](PROBLEM_SET_SOLUTIONS.md#problem-10-central-force-effective-potential-orbital-stability-chapter-4)


---
