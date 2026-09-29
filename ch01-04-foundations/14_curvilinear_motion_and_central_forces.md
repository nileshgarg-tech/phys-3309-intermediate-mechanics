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
