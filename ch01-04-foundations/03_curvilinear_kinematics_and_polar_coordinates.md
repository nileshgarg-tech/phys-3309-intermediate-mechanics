# 03. Curvilinear Kinematics & 2D Polar Coordinates

**Foundational Story**: Chapter 1, Sections 1.6–1.7  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 1 (pp. 23–35)
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 1 (pp. 27–38)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 11 ("Vectors")

---

## 1. Plane Polar Coordinates and Moving Unit Vectors

Any point $P$ in the $xy$-plane can be located by:
* $r$: The radial distance from the origin ($r \ge 0$).
* $\theta$: The counterclockwise angle made with the positive $x$-axis.

We define two local orthonormal unit vectors:
1. **r_hat**: Points radially outward from the origin.
2. **θ_hat**: Points in the direction of increasing $\theta$ (counterclockwise rotation).

Projecting onto Cartesian axes:
```
r_hat =  cos(θ)*x_hat + sin(θ)*y_hat
θ_hat = -sin(θ)*x_hat + cos(θ)*y_hat
```

---

## 2. Time Derivatives of Moving Unit Vectors

Differentiating with respect to time using the chain rule:
```
d(r_hat)/dt = -sin(θ)*θ_dot*x_hat + cos(θ)*θ_dot*y_hat = θ_dot * θ_hat
d(θ_hat)/dt = -cos(θ)*θ_dot*x_hat - sin(θ)*θ_dot*y_hat = -θ_dot * r_hat
```
> **The Golden Kinematic Rules for Polar Unit Vectors**:
> ```
> d(r_hat)/dt =  θ_dot * θ_hat
> d(θ_hat)/dt = -θ_dot * r_hat
> ```

---

## 3. Velocity in Polar Coordinates

Position is:
```
r = r * r_hat
```
Differentiating with the product rule:
```
v = dr/dt = (r_dot)*r_hat + r * [d(r_hat)/dt] = (r_dot)*r_hat + (r * θ_dot)*θ_hat
```
* **Radial velocity**: `v_r = r_dot`
* **Azimuthal velocity**: `v_θ = r * θ_dot`
* **Speed squared**: `v² = (r_dot)² + (r * θ_dot)²`

---

## 4. Acceleration in Polar Coordinates (Step-by-Step)

Differentiating velocity with respect to time:
```
a = dv/dt = d/dt [ (r_dot)*r_hat + (r * θ_dot)*θ_hat ]
```
Applying the product rule:
```
d/dt [(r_dot)*r_hat] = (r_ddot)*r_hat + (r_dot)*(θ_dot)*θ_hat
d/dt [(r*θ_dot)*θ_hat] = (r_dot*θ_dot + r*θ_ddot)*θ_hat - r*(θ_dot)²*r_hat
```
Collecting terms:
```
a = [ r_ddot - r*(θ_dot)² ] * r_hat + [ r*θ_ddot + 2*(r_dot)*(θ_dot) ] * θ_hat
```

### Physical Meaning of Acceleration Components:
* **`-r*(θ_dot)²` (Centripetal Acceleration)**: Inward acceleration maintaining curved path.
* **`r*θ_ddot` (Tangential Acceleration)**: Angular acceleration changing rotation speed.
* **`2*(r_dot)*(θ_dot)` (Coriolis Acceleration)**: Cross-coupling between radial expansion and coordinate rotation.

---

## 5. Summary Cheat Sheet for Module 03

| Vector | Polar Representation | Key Derivatives / Notes |
|---|---|---|
| **Unit Vectors** | `r_hat = cos(θ)x + sin(θ)y`, `θ_hat = -sin(θ)x + cos(θ)y` | `d(r_hat)/dt = θ_dot θ_hat`, `d(θ_hat)/dt = -θ_dot r_hat` |
| **Position** | `r = r * r_hat` | Magnitude $r$, orientation $\theta$ |
| **Velocity** | `v = (r_dot)*r_hat + (r*θ_dot)*θ_hat` | `v² = (r_dot)² + (r*θ_dot)²` |
| **Acceleration** | `a = [r_ddot - r*θ_dot²]*r_hat + [r*θ_ddot + 2*r_dot*θ_dot]*θ_hat` | Centripetal `-r*θ_dot²`, Coriolis `2*r_dot*θ_dot` |
| **Central Force Form** | `F_θ = (m/r)*d/dt(r²*θ_dot)` | When `F_θ = 0`, angular momentum `l = m*r²*θ_dot = const` |


---

## 6. Worked Examples & Practice Problems

### Worked Example 3.1: Kinematics on an Archimedean Spiral
**Problem**: A particle moves outward along an Archimedean spiral such that its polar coordinates as functions of time are:
```
r(t) = b * t
θ(t) = ω * t
```
where `b` and `ω` are positive constants.
(a) Find the velocity vector `v(t)` in polar coordinates and compute the particle's speed `|v(t)|`.
(b) Find the acceleration vector `a(t)` and identify each of the four physical acceleration components.

**Solution**:
1. **Derivatives**:
   `r_dot = b`, `r_ddot = 0`
   `θ_dot = ω`, `θ_ddot = 0`

2. **Velocity**:
   ```
   v = (r_dot)*r_hat + (r * θ_dot)*θ_hat = b * r_hat + (b*t * ω) * θ_hat
   ```
   The speed is:
   ```
   |v| = sqrt( (r_dot)² + (r*θ_dot)² ) = sqrt( b² + b²*ω²*t² ) = b * sqrt(1 + ω²*t²)
   ```
   At `t = 0`, the speed is purely radial: `|v| = b`. As `t -> ∞`, the tangential speed dominates.

3. **Acceleration**:
   Recall the general polar acceleration formula:
   ```
   a = [ r_ddot - r*(θ_dot)² ] * r_hat + [ r*θ_ddot + 2*r_dot*θ_dot ] * θ_hat
   ```
   Substitute our values:
   * Radial component: `a_r = 0 - (b*t)*(ω)² = -b*ω²*t` (Pure centripetal acceleration!)
   * Azimuthal component: `a_θ = (b*t)*(0) + 2*(b)*(ω) = 2*b*ω` (Pure Coriolis acceleration!)
   ```
   a(t) = (-b*ω²*t) * r_hat + (2*b*ω) * θ_hat
   ```
**Physical Insight**: Even though the particle's angular acceleration is zero (`θ_ddot = 0`), there is a constant non-zero tangential acceleration `2*b*ω`. This is the Coriolis term: as the particle moves radially outward at speed `b`, the coordinate axis rotates beneath it at rate `ω`, requiring a tangential force to increase its tangential speed!

---

### Worked Example 3.2: The Conical Pendulum in Polar Coordinates
**Problem**: A bob of mass `m` hangs from a light string of length `L` and moves in a horizontal circle at constant height. The string makes a constant angle `α` with the vertical. 
Use polar coordinates in the horizontal plane to determine the orbital speed `v` and period `τ`.

**Solution**:
In the horizontal plane, the radius of the circular orbit is `R = L * sin(α)`.
Because the path is circular with constant radius, `r = R = const`, so `r_dot = 0` and `r_ddot = 0`.
The forces acting on the bob are:
* Gravity downward: `F_g = m*g`
* Tension `T`: vertical component `T*cos(α)`, inward horizontal radial component `T*sin(α)`.

Vertical equilibrium (`a_z = 0`):
```
T * cos(α) = m * g  ===>  T = m*g / cos(α)
```
Horizontal radial Newton's Second Law (`F_r = m * a_r`):
```
-T * sin(α) = m * [ r_ddot - r*(θ_dot)² ] = -m * R * (θ_dot)²
```
Substitute `T = m*g / cos(α)` and `R = L*sin(α)`:
```
(m*g / cos(α)) * sin(α) = m * (L*sin(α)) * (θ_dot)²
g * tan(α) = L * sin(α) * (θ_dot)²  ===>  θ_dot² = g / (L * cos(α))
```
The angular speed is `ω = θ_dot = sqrt( g / (L * cos(α)) )`.
The orbital period is:
```
τ = 2*π / ω = 2*π * sqrt( (L * cos(α)) / g )
```

---

### Practice Problem 3.1 (To Solve)
**Statement**: A bead slides along a smooth horizontal rod that rotates in a horizontal plane with constant angular velocity `ω` about a vertical pivot at one end. 
(a) Set up the radial equation of motion for the bead.
(b) Solve for `r(t)` given initial conditions `r(0) = r_0` and `r_dot(0) = 0`.
* **Hint**: The rod is frictionless, so `F_r = 0`. Hence `r_ddot - r*ω² = 0`. The general solution is a sum of exponentials or hyperbolic cosine.
* **Answer**: `r_ddot - ω²*r = 0 ===> r(t) = r_0 * cosh(ω*t)`.

---

### Practice Problem 3.2 (To Solve)
**Statement**: A particle moves in a plane with position given by `r(t) = r_0 * e^(k*t)` and `θ(t) = c*t`.
Find the angle `ψ` between the velocity vector `v` and the radial unit vector `r_hat`. Show that this angle is constant in time.
* **Hint**: `v_r = r_dot = k*r`, `v_θ = r*θ_dot = c*r`. Then `tan(ψ) = v_θ / v_r`.
* **Answer**: `tan(ψ) = (c*r) / (k*r) = c / k = const  ===>  ψ = arctan(c / k)`. (This defines an equiangular logarithmic spiral).

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 1:
  * Sections 1.6–1.7 (pp. 23–35): 2D Polar Coordinates, Kinematics, Centripetal & Coriolis terms.
  * Problems 1.35, 1.40, 1.47 (pp. 40–42): Polar velocity and acceleration derivations.
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 1: "Vectors and Kinematics" (Sections 1.8–1.9, Examples 1.10–1.12).
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 11: "Vectors" (Section 11.6 on circular and polar kinematics).
