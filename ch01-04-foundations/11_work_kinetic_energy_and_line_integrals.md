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
