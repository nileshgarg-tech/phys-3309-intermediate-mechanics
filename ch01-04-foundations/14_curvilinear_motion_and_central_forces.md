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
1. Applied active force $F_{\text{applied}}$ (e.g. gravity).
2. Normal constraint force $N$ exerted by the track perpendicular to the wire.

What makes constraint problems so simple in energy mechanics?
```
N ⊥ dr   ===>   N · dr = 0
```
> **The Constraint Force Principle**:
> **Frictionless constraint forces do zero work!**
> Therefore, normal forces can be completely ignored when computing mechanical energy conservation:
> ```
> E = (1/2) * m * (ds/dt)² + U(s) = constant
> ```
> Any 1D constrained motion reduces mathematically to the exact same energy equation we analyzed in Module 13!

---

## 2. Central Forces: Kinetic Energy in Polar Coordinates

Now consider a particle of mass $m$ subject to a central force $F = f(r) \hat{r}$.
In Module 03, we derived the velocity in plane polar coordinates:
```
v = (r_dot)*r_hat + (r * θ_dot)*θ_hat
```
The kinetic energy is:
```
T = (1/2) * m * v² = (1/2) * m * [ (r_dot)² + (r * θ_dot)² ]
```
The potential energy depends only on radial distance $r$: $U = U(r)$.
Total energy is:
```
E = (1/2) * m * (r_dot)² + (1/2) * m * r² * (θ_dot)² + U(r)
```
At first glance, this equation contains two variables: $r(t)$ and $\theta(t)$.
How do we reduce it to a one-dimensional problem?

---

## 3. The Effective Potential $U_{\text{eff}}(r)$

Recall from Module 10 that for any central force, **angular momentum is strictly conserved**:
```
l = m * r² * θ_dot = constant   ===>   θ_dot = l / (m * r²)
```
Now, substitute this expression for $\dot{\theta}$ into the kinetic energy:
```
T_angular = (1/2) * m * r² * (θ_dot)² = (1/2) * m * r² * [ l / (m * r²) ]²
          = l² / (2 * m * r²)
```
Substitute this back into the total energy equation:
```
E = (1/2) * m * (r_dot)² + [ l² / (2 * m * r²) + U(r) ]
```
Look at this equation carefully:
* The first term $(1/2) m \dot{r}^2$ is the **pure radial kinetic energy**.
* The remaining terms depend **only on $r$**!

We define the **Effective Potential**:
```
U_eff(r) = U(r) + l² / (2 * m * r²)
```
The total energy equation becomes:
```
E = (1/2) * m * (r_dot)² + U_eff(r) = constant
```
> **The Central Force Reduction**:
> **A two-dimensional central-force problem is mathematically identical to a one-dimensional particle moving in the effective potential $U_{\text{eff}}(r)$!**

---

## 4. The Centrifugal Barrier

The term:
```
U_cf(r) = l² / (2 * m * r²)
```
is called the **Centrifugal Potential**.
Taking its negative derivative with respect to $r$:
```
F_cf = - d/dr [ l² / (2 * m * r²) ] = + l² / (m * r³) = m * r * (θ_dot)²
```
This is the outward centrifugal force!
As $r \to 0$, $U_{\text{cf}} \to +\infty$ scaling as $1/r^2$.
* For an attractive gravitational potential $U(r) = -G M m / r$, as $r \to 0$, the centrifugal barrier $+l^2/(2mr^2)$ diverges faster than $-1/r$.
* **The centrifugal barrier prevents any particle with non-zero angular momentum ($l \ne 0$) from crashing into the center of attraction!**

---

## 5. Summary Cheat Sheet for Module 14

| Concept | Mathematical Statement | Core Takeaway |
|---|---|---|
| **Constraint Work** | `N · dr = 0` | Frictionless track forces do zero work |
| **Polar Kinetic Energy** | `T = (1/2)m*r_dot² + (1/2)m*r²*θ_dot²` | Split into radial + angular parts |
| **Angular Momentum** | `θ_dot = l / (m*r²)` | Eliminates angular velocity from energy |
| **Effective Potential** | `U_eff(r) = U(r) + l²/(2*m*r²)` | Absorbs angular kinetic energy into potential |
| **Equivalent 1D Problem**| `E = (1/2)m*r_dot² + U_eff(r)` | Radial motion mapped to standard 1D well |


---

## 6. Worked Examples & Practice Problems

### Worked Example 14.1: The Vertical Loop-the-Loop Roller Coaster
**Problem**: A small roller coaster car of mass `m` slides frictionlessly along a track that loops vertically in a circle of radius `R`. The car is released from rest at height `h` above the bottom of the loop.
(a) What is the minimum release height `h_min` so that the car maintains contact with the track at the very top of the loop?
(b) If released from `h = 3*R`, what normal force does the track exert on the car at the bottom of the loop?

**Solution**:
1. **At the Top of the Loop (Height `2*R`)**:
   By energy conservation between release at height `h` and the top of the loop:
   ```
   m * g * h = m * g * (2*R) + (1/2) * m * v_top²  ===>  v_top² = 2 * g * (h - 2*R)
   ```
   At the top, both gravity and the normal track force `N` point downward:
   ```
   m * g + N = m * (v_top² / R)  ===>  N = m * (v_top² / R) - m * g
   ```
   To maintain contact without falling, the normal force must be non-negative (`N ≥ 0`):
   ```
   m * (v_top² / R) ≥ m * g  ===>  v_top² ≥ g * R
   ```
   Substitute `v_top²`:
   ```
   2 * g * (h_min - 2*R) = g * R  ===>  2*h_min - 4*R = R  ===>  h_min = (5 / 2) * R = 2.5 * R
   ```

2. **At the Bottom of the Loop (Height `0`, with `h = 3*R`)**:
   Energy conservation:
   ```
   m * g * (3*R) = (1/2) * m * v_bot²  ===>  v_bot² = 6 * g * R
   ```
   At the bottom, normal force points upward, gravity downward:
   ```
   N - m*g = m * (v_bot² / R)  ===>  N = m*g + m * (6*g*R / R) = 7 * m * g
   ```
**Physical Insight**: The track must push upward with a colossal force of `7 times the car's weight` at the bottom of the loop!

---

### Worked Example 14.2: Effective Potential of a Planetary Orbit
**Problem**: For a planet of mass `m` orbiting the Sun of mass `M` with angular momentum `l`:
The gravitational potential is `U(r) = - k / r`, where `k = G * M * m`.
(a) Write down the effective potential `U_eff(r)`.
(b) Find the radius `r_0` of a circular orbit.
(c) Show that this circular orbit is stable against small radial perturbations.

**Solution**:
(a) The effective potential is:
```
U_eff(r) = - (k / r) + l² / (2 * m * r²)
```
(b) Circular orbit occurs at the minimum of `U_eff(r)` where `dU_eff/dr = 0`:
```
dU_eff / dr = + (k / r²) - (2 * l²) / (2 * m * r³) = (k / r²) - l² / (m * r³) = 0
```
Multiply by `r³`:
```
k * r_0 - l² / m = 0  ===>  r_0 = l² / (m * k) = l² / (G * M * m²)
```
(c) Check stability via second derivative:
```
d²U_eff / dr² = - (2 * k / r³) + 3 * l² / (m * r⁴)
```
Evaluate at `r = r_0 = l² / (m*k)`:
```
d²U_eff / dr² |_{r_0} = - (2 * k / r_0³) + 3 * (k * r_0) / r_0⁴ = + k / r_0³ > 0
```
Because `d²U_eff/dr² > 0`, the circular orbit corresponds to a **stable potential valley**. A small tap causes the planet to oscillate radially around `r_0` (elliptical orbit!).

---

### Practice Problem 14.1 (To Solve)
**Statement**: A bead of mass `m` slides on a frictionless wire bent in the shape of a parabola `y = c * x²` in a uniform vertical gravitational field `g`.
Find the frequency `ω` of small oscillations about the bottom of the wire at `x = 0`.
* **Hint**: Near `x = 0`, arc length `ds = sqrt(1 + (dy/dx)²) dx = sqrt(1 + 4*c²*x²) dx ≈ dx`. Potential energy `U(x) = m*g*y = m*g*c*x² = (1/2)*(2*m*g*c)*x²`.
* **Answer**: `k_eff = 2*m*g*c ===> ω = sqrt(k_eff / m) = sqrt(2 * g * c)`.

---

### Practice Problem 14.2 (To Solve)
**Statement**: A particle of mass `m` moves in an attractive central force `F(r) = - k / r³` (inverse-cube force).
Show that circular orbits exist only if `l² = m * k`, and prove that such orbits are neutrally stable or unstable for any slight radial nudge.
* **Hint**: `U(r) = -k / (2*r²)`. Effective potential `U_eff(r) = -k/(2*r²) + l²/(2*m*r²) = (l² - m*k) / (2*m*r²)`.
* **Answer**: If `l² = m*k`, then `U_eff(r) = 0` everywhere (flat line). If nudged, the particle either spirals directly into the origin or flies away to infinity. No bound stable orbits can exist in an inverse-cube force!

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Sections 4.7–4.8 (pp. 142–152): Curvilinear 1D Systems, Central Forces, Effective Potential.
  * Problems 4.38, 4.43, 4.45 (pp. 170–172): Central force effective potential problems.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 14: "Work and Potential Energy (Conclusion)" (Section 14.5 on central force fields).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.8–5.9).
