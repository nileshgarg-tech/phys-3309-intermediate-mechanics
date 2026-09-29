# 13. One-Dimensional Systems & Potential Wells

**Foundational Story**: Chapter 4, Section 4.6  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 135–142)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 13 & Ch. 14
* Morin, *Introduction to Classical Mechanics*, Ch. 4

---

## 1. The Power of the 1D Energy Equation

In one dimension, Newton's Second Law is a second-order ODE:
```
m * (d²x/dt²) = F(x)
```
Because any 1D position-dependent force $F(x)$ is automatically conservative (its curl is trivially zero!), we can always define:
```
U(x) = - ∫_{x_0}^x F(x') dx'   ===>   F(x) = - dU/dx
```
Conservation of energy gives a first-order differential equation:
```
E = (1/2) * m * (dx/dt)² + U(x) = constant
```
Solve directly for the velocity $\dot{x} = dx/dt$:
```
dx/dt = ± sqrt( (2 / m) * (E - U(x)) )
```
Separate variables:
```
t = ∫_{x_0}^x dx' / sqrt( (2 / m) * (E - U(x')) )
```
> **Taylor's Principle of 1D Mechanics**:
> **Any 1D conservative problem can be completely solved by a single quadrature (integral)!**

---

## 2. Reading Energy Diagrams Like a Map

One of the most essential skills in intermediate physics is extracting the qualitative behavior of a system directly from a plot of $U(x)$ vs. $x$ without solving any integrals.

```
       Energy
         ^
         |                    U(x)
       E |----+--------------------+-------- Energy Level E
         |     \                  /
         |      \    Allowed     /
         |       \   Region     /
         |        \            /
         +---------x1---------x2------------> Position x
                   Turning   Turning
                   Point     Point
```

### 1. Allowed vs. Forbidden Regions
* Because kinetic energy $T = (1/2) m v^2 \ge 0$, total energy must satisfy:
  ```
  E ≥ U(x)
  ```
* **Classically Allowed Region**: Where $E \ge U(x)$. The particle can move here. Its speed is $v = \sqrt{2(E - U)/m}$.
* **Classically Forbidden Region**: Where $E < U(x)$. The particle can never enter here in classical mechanics (kinetic energy cannot be negative).

### 2. Turning Points
The boundary points $x_1$ and $x_2$ where $E = U(x)$ are called **Turning Points**:
* At these points, $T = 0$, so the speed is instantaneously zero ($v = 0$).
* The force $F = -dU/dx$ accelerates the particle back into the allowed region, causing it to reverse direction.

---

## 3. Equilibrium Classifications

An **equilibrium point** occurs wherever the net force is zero:
```
F(x_0) = 0   <===>   dU/dx |_{x_0} = 0
```
To determine stability, Taylor-expand $U(x)$ in a small displacement $u = x - x_0$:
```
U(x) = U(x_0) + U'(x_0)*u + (1/2)*U''(x_0)*u² + ...
```
Since $U'(x_0) = 0$:
```
U(x) ≈ U(x_0) + (1/2) * k_eff * u²     (where k_eff = d²U/dx² |_{x_0})
```

```
     STABLE              UNSTABLE               NEUTRAL
     d²U/dx² > 0         d²U/dx² < 0            d²U/dx² = 0
        \   /                 ^                 -------------
         \_/                 /       (Valley)             (Hilltop)             (Flat Plain)
```

1. **Stable Equilibrium ($d^2U/dx^2 > 0$)**: Local minimum (valley bottom). Small displacements experience a restoring force $F = -k_{\text{eff}} u$. The particle oscillates around $x_0$.
2. **Unstable Equilibrium ($d^2U/dx^2 < 0$)**: Local maximum (hilltop peak). Small displacements experience a repelling force pushing the particle away.
3. **Neutral Equilibrium ($d^2U/dx^2 = 0$)**: Flat region. No restoring force exists to second order.

---

## 4. Small Oscillations About Stable Equilibrium

For any smooth potential well near a stable minimum $x_0$, the restoring force is linear:
```
F = - dU/dx ≈ - k_eff * (x - x_0)
```
Newton's Second Law becomes:
```
m * (d²u/dt²) = - k_eff * u   ===>   d²u/dt² + (k_eff / m) * u = 0
```
> **The Universal Harmonic Approximation**:
> **Every smooth system near a stable equilibrium executes Simple Harmonic Motion (SHM)!**
> The natural angular frequency is given by:
> ```
> ω_0 = sqrt( k_eff / m ) = sqrt( (1 / m) * d²U/dx² |_{x_0} )
> ```
> This is why harmonic oscillators dominate all of physics: from molecular vibrations to acoustic phonons in solids.

---

## 5. Summary Cheat Sheet for Module 13

| Feature | Equation / Criterion | Physical Interpretation |
|---|---|---|
| **1D Velocity** | `v(x) = ± sqrt(2(E - U(x))/m)` | Determined entirely by potential gap $E - U$ |
| **Turning Points** | `E = U(x)` | Particle stops ($v = 0$) and reverses direction |
| **Equilibrium** | `dU/dx = 0` | Net force is zero |
| **Stable Minimum** | `d²U/dx² > 0` | Valley; executes harmonic oscillations |
| **Natural Frequency** | `ω_0 = sqrt( (d²U/dx²)/m )` | Small oscillation frequency about any minimum |
