# 11. Work, Kinetic Energy & The Work-Energy Theorem

**Foundational Story**: Chapter 4, Section 4.1  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 114–119)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 13 ("Work and Potential Energy (A)")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 4

---

## 1. Why Energy? The Scalar Advantage

Up to this point, our tools have been **vector quantities**: force, momentum, acceleration, torque.
Working with vectors requires resolving components into coordinate systems ($x, y, z$ or $r, \theta$), handling signs, and managing moving unit vectors.

**Energy introduces a scalar quantity.** 
Energy has no direction in space. If a particle starts at point 1 and moves to point 2, the **Work-Kinetic Energy Theorem** connects its beginning and end speeds without requiring knowledge of the detailed time-dependent trajectory in between!

---

## 2. Work Defined as a Line Integral

In elementary physics, work is described as "force times distance": $W = F \cdot d$.
In realistic mechanics, however:
* The force $F(r)$ changes in both magnitude and direction along the path.
* The trajectory curve $C$ twists arbitrarily through 3D space.

To find the total work done on a particle as it moves along curve $C$ from point $r_1$ to point $r_2$, we divide the path into infinitesimal displacement vectors $dr$:
```
W(1 -> 2) = ∫_1^2 F · dr
```
In Cartesian coordinates, where $dr = dx\,\hat{x} + dy\,\hat{y} + dz\,\hat{z}$:
```
W(1 -> 2) = ∫_1^2 [ F_x(x,y,z) dx + F_y(x,y,z) dy + F_z(x,y,z) dz ]
```

```
           Point 2 (r2)
             o
            / 
           /  ^ F(r)
          /   |
         |    +---> dr
                              o Point 1 (r1)
```

---

## 3. The Work-Kinetic Energy Theorem (Complete 3D Derivation)

Let us evaluate the line integral using Newton's Second Law: $F = m \cdot a = m \cdot (dv/dt)$.
```
W(1 -> 2) = ∫_1^2 F · dr = ∫_{t_1}^{t_2} [ m * (dv/dt) ] · (dr/dt * dt)
           = m * ∫_{t_1}^{t_2} (dv/dt) · v dt
```
Now consider the derivative of the scalar speed squared $v^2 = v \cdot v$:
```
d(v²)/dt = d(v · v)/dt = (dv/dt · v) + (v · dv/dt) = 2 * (v · dv/dt)
```
Therefore:
```
(dv/dt) · v = (1/2) * d(v²)/dt
```
Substitute this directly back into our integral:
```
W(1 -> 2) = m * ∫_{t_1}^{t_2} (1/2) * [ d(v²)/dt ] dt
           = (1/2) * m * ∫_{v_1²}^{v_2²} d(v²)
           = (1/2) * m * v_2² - (1/2) * m * v_1²
```
We define the **Kinetic Energy** $T$:
```
T = (1/2) * m * v² = p² / (2 * m)
```
> **The Work-Kinetic Energy Theorem**:
> ```
> W_net(1 -> 2) = ΔT = T_2 - T_1
> ```
> The net work done by all forces acting on a particle equals the change in its kinetic energy.

---

## 4. Power: The Rate of Doing Work

The instantaneous time rate at which work is performed on a particle is called **Power** ($P$):
```
P = dW / dt = (F · dr) / dt = F · (dr/dt) = F · v
```
Notice:
* If force is perpendicular to velocity ($F \perp v$, such as magnetic forces $q(v \times B)$ or normal forces on a frictionless track), then $F \cdot v = 0$. 
* **Zero power is delivered, and kinetic energy is strictly constant!**

---

## 5. Summary Cheat Sheet for Module 11

| Quantity | Formula | Meaning |
|---|---|---|
| **Work (Line Integral)**| `W = ∫_1^2 F · dr` | Accumulation of force along displacement path |
| **Kinetic Energy** | `T = (1/2) * m * v²` | Scalar measure of motion energy |
| **Work-Energy Theorem** | `W_net = ΔT` | Net work directly dictates speed change |
| **Instantaneous Power** | `P = dW/dt = F · v` | Rate of energy transfer |
| **Perpendicular Forces** | If `F ⊥ v`, then `P = 0` | Cannot change speed (e.g. magnetic fields) |


---

## 6. Worked Examples & Practice Problems

### Worked Example 11.1: Path-Dependent Work (Non-Conservative Force)
**Problem**: A particle in the $xy$-plane is acted upon by a 2D force field:
```
F(x, y) = y * x_hat + 2*x * y_hat
```
Calculate the work done by this force in moving the particle from the origin `(0, 0)` to the point `(1, 1)` along two different paths:
(a) Path 1: A straight line `y = x`.
(b) Path 2: A parabola `y = x²`.
Is this force conservative?

**Solution**:
The work integral is:
```
W = ∫ F · dr = ∫ (F_x dx + F_y dy) = ∫ (y dx + 2*x dy)
```

(a) **Path 1 (Straight line `y = x`, so `dy = dx`)**:
Substitute `y = x` and `dy = dx` as `x` goes from 0 to 1:
```
W_1 = ∫_0^1 [ (x) dx + 2*x (dx) ] = ∫_0^1 3*x dx = [ (3/2)*x² ]_0^1 = 3 / 2 = 1.5 Joules
```

(b) **Path 2 (Parabola `y = x²`, so `dy = 2*x dx`)**:
Substitute `y = x²` and `dy = 2*x dx` as `x` goes from 0 to 1:
```
W_2 = ∫_0^1 [ (x²) dx + 2*x (2*x dx) ] = ∫_0^1 (x² + 4*x²) dx = ∫_0^1 5*x² dx
    = [ (5/3)*x³ ]_0^1 = 5 / 3 ≈ 1.67 Joules
```
**Conclusion**:
Because `W_1 ≠ W_2` (1.5 J vs 1.67 J), **the work depends explicitly on the path taken!**
Therefore, the force is **non-conservative**. 
*(In Module 12 we confirm this via the curl: `(∇ x F)_z = ∂F_y/∂x - ∂F_x/∂y = 2 - 1 = 1 ≠ 0`)*.

---

### Worked Example 11.2: Accelerating Under Constant Power
**Problem**: An electric vehicle of mass `m` accelerates from rest along a straight horizontal track. The motor delivers a constant mechanical power output `P`. 
Assuming no friction or drag, find the vehicle's speed `v(t)` and distance `x(t)` as functions of time.

**Solution**:
Power is the time rate of change of kinetic energy:
```
P = dT / dt = d/dt [ (1/2) * m * v² ]
```
Since power `P` is constant, integrate with respect to time starting from rest (`v(0) = 0`):
```
(1/2) * m * v(t)² = P * t  ===>  v(t)² = (2 * P * t) / m
```
Taking the square root:
```
v(t) = sqrt( (2 * P / m) ) * t^(1/2)
```
Now integrate velocity `v = dx/dt` to find distance `x(t)` with `x(0) = 0`:
```
x(t) = ∫_0^t v(t') dt' = sqrt(2*P / m) * ∫_0^t (t')^(1/2) dt'
     = sqrt(2*P / m) * (2/3) * t^(3/2) = (2/3) * sqrt( (2 * P / m) ) * t^(3/2)
```
**Physical Insight**: Unlike constant force acceleration (where `v ∝ t` and `x ∝ t²`), constant power gives `v ∝ t^(1/2)` and `x ∝ t^(3/2)`. The acceleration is infinite at `t = 0` and decreases over time as speed builds up.

---

### Practice Problem 11.1 (To Solve)
**Statement**: A particle of mass `m` moves in 3D under the linear restoring force `F = -k * r = -k*(x*x_hat + y*y_hat + z*z_hat)`.
Calculate the work done along a helical path given by `r(t) = (R*cos(t), R*sin(t), c*t)` as `t` goes from `0` to `2*π`.
* **Hint**: `dr = (-R*sin(t), R*cos(t), c) dt`. Compute `F · dr = -k * (x dx + y dy + z dz) = -k * d( (x² + y² + z²)/2 )`.
* **Answer**: `W = -k/2 * [ (R² + c²*(2π)²) - (R² + 0) ] = -2 * π² * k * c²`. (Work depends only on the endpoints!).

---

### Practice Problem 11.2 (To Solve)
**Statement**: A block of mass `m = 2.0 kg` is pressed against a non-linear spring with restoring force `F(x) = -k*x - β*x³`, where `k = 400 N/m` and `β = 1000 N/m³`. 
The spring is compressed by `x_0 = 0.10 m` and released. Find the launch speed `v` of the block as it leaves the spring at `x = 0`.
* **Hint**: Use the Work-Energy Theorem: `(1/2)*m*v² = W_spring = ∫_{-x_0}^0 (-k*x - β*x³) dx`.
* **Answer**: `W = (1/2)*k*x_0² + (1/4)*β*x_0⁴ = (0.5)*(400)*(0.01) + (0.25)*(1000)*(0.0001) = 2.0 + 0.025 = 2.025 J`. Launch speed `v = sqrt(2 * 2.025 / 2.0) ≈ 1.423 m/s`.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Section 4.1 (pp. 114–119): Kinetic Energy and Work, Line Integrals, 3D Work-Energy Theorem.
  * Problems 4.2, 4.5, 4.9 (pp. 164–165): Line integral work calculations along various geometric paths.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 13: "Work and Potential Energy (A)" (Sections 13.1–13.3).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.1–5.3).
