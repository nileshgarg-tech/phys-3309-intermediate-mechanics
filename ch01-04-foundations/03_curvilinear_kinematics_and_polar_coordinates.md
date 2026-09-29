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
