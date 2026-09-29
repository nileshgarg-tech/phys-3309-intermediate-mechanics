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


---

## 6. Worked Examples & Practice Problems

### Worked Example 13.1: The Lennard-Jones Interatomic Potential
**Problem**: The interaction potential between two neutral noble gas atoms (such as Argon) is modeled by the **Lennard-Jones (6-12) Potential**:
```
U(r) = U_0 * [ (r_0 / r)^12 - 2 * (r_0 / r)^6 ]
```
where `U_0` and `r_0` are positive constants.
(a) Find the equilibrium separation distance `r_eq` where the net force is zero.
(b) What is the binding energy (the depth of the potential well at equilibrium)?
(c) Find the effective spring constant `k_eff` and the frequency `ω_0` of small oscillations for an atom of mass `m` vibrating about equilibrium.

**Solution**:
(a) **Equilibrium Separation**:
Equilibrium occurs where force vanishes: `F(r) = -dU/dr = 0`.
```
dU/dr = U_0 * [ -12 * (r_0^12 / r^13) + 12 * (r_0^6 / r^7) ] = (12 * U_0 / r) * [ -(r_0 / r)^12 + (r_0 / r)^6 ]
```
Setting `dU/dr = 0`:
```
(r_0 / r)^12 = (r_0 / r)^6  ===>  (r_0 / r)^6 = 1  ===>  r_eq = r_0
```
The equilibrium distance is simply `r_0`!

(b) **Well Depth (Binding Energy)**:
Evaluate `U(r_0)`:
```
U(r_0) = U_0 * [ (1)^12 - 2 * (1)^6 ] = U_0 * [ 1 - 2 ] = - U_0
```
The minimum potential energy is `-U_0`. It requires an input of energy `+U_0` to separate the two atoms to infinity!

(c) **Small Oscillations Frequency**:
Compute the second derivative:
```
d²U/dr² = U_0 * [ 12*13 * (r_0^12 / r^14) - 12*7 * (r_0^6 / r^8) ]
```
Evaluate at `r = r_0`:
```
k_eff = d²U/dr² |_{r_0} = (U_0 / r_0²) * [ 156 - 84 ] = 72 * (U_0 / r_0²)
```
Since `k_eff > 0`, the equilibrium is **stable**.
The small-oscillation angular frequency is:
```
ω_0 = sqrt( k_eff / m ) = sqrt( 72 * U_0 / (m * r_0²) ) = (6 * sqrt(2) / r_0) * sqrt( U_0 / m )
```

---

### Worked Example 13.2: Exact Time Integral for a Harmonic Oscillator
**Problem**: For a 1D spring potential `U(x) = (1/2)*k*x²`, a particle of mass `m` is released from rest at `x = A`.
Use the general 1D time integral to find the exact period of oscillation `τ`.

**Solution**:
Total energy is `E = (1/2)*k*A²`.
The turning points are `-A` and `+A`.
The time required to travel from `x = 0` to the turning point `x = A` is one quarter of the period (`τ / 4`):
```
τ / 4 = ∫_0^A dx / sqrt( (2/m) * (E - U(x)) )
      = ∫_0^A dx / sqrt( (2/m) * [ (1/2)*k*A² - (1/2)*k*x² ] )
      = sqrt(m / k) * ∫_0^A dx / sqrt( A² - x² )
```
Let `x = A * sin(θ)`, then `dx = A * cos(θ) dθ`, and `sqrt(A² - x²) = A * cos(θ)`:
```
τ / 4 = sqrt(m / k) * ∫_0^(π/2) (A * cos(θ) dθ) / (A * cos(θ))
      = sqrt(m / k) * ∫_0^(π/2) dθ = (π / 2) * sqrt(m / k)
```
Multiplying by 4:
```
τ = 2 * π * sqrt(m / k)   ===>   ω_0 = 2*π / τ = sqrt(k / m)
```
Matches elementary physics exactly, confirming the power of the 1D time integral technique.

---

### Practice Problem 13.1 (To Solve)
**Statement**: A particle moves in the quartic potential `U(x) = - (1/2)*a*x² + (1/4)*b*x⁴`, where `a, b > 0`.
(a) Find all equilibrium points and classify their stability.
(b) Find the angular frequency `ω_0` of small oscillations about the stable equilibria.
* **Hint**: `dU/dx = -a*x + b*x³ = x*(-a + b*x²) = 0`. Compute `d²U/dx² = -a + 3*b*x²` at each root.
* **Answer**: `x = 0` is unstable (`d²U/dx² = -a < 0`). `x = ± sqrt(a/b)` are stable minima (`d²U/dx² = +2a > 0`). Small oscillation frequency: `ω_0 = sqrt(2*a / m)`.

---

### Practice Problem 13.2 (To Solve)
**Statement**: A particle of mass `m` moves in the potential `U(x) = U_0 * tan²(x / a)` for `|x| < π*a/2`.
Find the frequency of small oscillations about `x = 0`.
* **Hint**: Taylor-expand `tan(u) ≈ u + u³/3` so `tan²(u) ≈ u²`. Then `U(x) ≈ U_0 * (x/a)² = (1/2) * (2*U_0 / a²) * x²`.
* **Answer**: `k_eff = 2*U_0 / a² ===> ω_0 = sqrt(2*U_0 / (m*a²))`.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Section 4.6 (pp. 135–142): Energy for One-Dimensional Systems, Potential Wells, Small Oscillations.
  * Problems 4.27, 4.31, 4.36, 4.38 (pp. 168–170): Equilibrium classification and period integrals.
* **Morin, David**, *Introduction to Classical Mechanics*, Chapter 4:
  * Section 4.1–4.4 (pp. 101–114): Superb graphical treatment of 1D potential wells.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 13: "Work and Potential Energy (A)" (Section 13.4 on potential graphs).
