# 10. Angular Momentum: Single & Multiparticle Systems

**Foundational Story**: Chapter 3, Sections 3.4–3.5  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 3 (pp. 90–99)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 18 & Ch. 20 ("Rotation in Space")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 6

---

## 1. Defining Angular Momentum for a Single Particle

Linear momentum ($p = m \cdot v$) measures motion along a line.
**Angular momentum** ($l$) measures rotational motion about a designated origin $O$.

For a particle of mass $m$ with position vector $r$ and linear momentum $p$:
```
l = r x p = r x (m * v)
```
Angular momentum is an **axial vector** perpendicular to both the position vector and the velocity vector.
The magnitude is:
```
|l| = r * p * sin(θ) = r_perp * p = r * p_perp
```

```
                 p = m*v
                ^
               / 
              / θ
             .-----------+
            /                      r /                         /                          /                           O                     ```

---

## 2. Torque and the Fundamental Rotational Law

What causes angular momentum to change?
Let us differentiate $l$ with respect to time:
```
dl / dt = d(r x p) / dt = (dr/dt x p) + (r x dp/dt)
```
Examine the first term:
```
dr/dt x p = v x (m * v) = m * (v x v) = 0
```
*(The cross product of any vector with itself is identically zero!)*
Now examine the second term: by Newton's Second Law, $dp/dt = F_{\text{net}}$. Therefore:
```
dl / dt = r x F_net
```
We define the **Torque** (or moment of force) $\Gamma$:
```
Γ = r x F
```
> **The Rotational Form of Newton's Second Law**:
> ```
> Γ_net = dl / dt
> ```
> Torque is the time rate of change of angular momentum.

---

## 3. Central Forces and Kepler's Second Law

A force is called a **Central Force** if it always points directly toward or away from the origin:
```
F(r) = f(r) * r_hat
```
Examples include Newtonian gravity ($F = -G M m / r^2 \hat{r}$) and Coulomb electrostatics ($F = k q_1 q_2 / r^2 \hat{r}$).

Compute the torque exerted by a central force:
```
Γ = r x F = r x [ f(r) * r_hat ] = f(r) * [ r * (r_hat x r_hat) ] = 0
```
Because $\Gamma = 0$:
```
dl / dt = 0   ===>   l = r x (m * v) = constant vector!
```

### Consequences of Angular Momentum Conservation:
1. **Planar Motion**: Since $l$ is a fixed vector in space, and $r(t) \perp l$ at all times, the particle's entire trajectory is permanently trapped in a 2D plane perpendicular to $l$.
2. **Kepler's Second Law (Equal Areas in Equal Times)**:
   The area swept out by the position vector in time $dt$ is a triangle of area:
   ```
   dA = (1/2) * |r x dr| = (1/2) * |r x (v dt)| = (1 / (2*m)) * |l| dt
   ```
   Dividing by $dt$:
   ```
   dA / dt = |l| / (2 * m) = constant!
   ```
   A planet sweeps out equal orbital areas in equal intervals of time.

---

## 4. Total Angular Momentum of a Multiparticle System

For a collection of $N$ particles:
```
L_total = Σ_i l_i = Σ_i (r_i x p_i)
```
Differentiate with respect to time:
```
dL_total / dt = Σ_i (r_i x F_i) = Σ_i (r_i x F_i^ext) + Σ_i Σ_{j ≠ i} (r_i x F_ij)
```
Let us inspect the internal torque sum. Grouping mutual action-reaction pairs:
```
r_i x F_ij + r_j x F_ji = r_i x F_ij - r_j x F_ij = (r_i - r_j) x F_ij
```
If the internal forces obey the **Strong Form of Newton's Third Law**, $F_{ij}$ acts along the relative displacement vector $(r_i - r_j)$.
Therefore:
```
(r_i - r_j) x F_ij = 0
```
All internal torques vanish identically!
```
dL_total / dt = Σ_i (r_i x F_i^ext) = Γ_net^ext
```
If the net external torque is zero, the total angular momentum of the system is strictly conserved!

---

## 5. The Orbital vs. Spin Decomposition

Here is one of the most elegant and profound theorems in classical mechanics:
Let $R$ be the Center of Mass position, and let $r'_i$ be the position of particle $i$ **relative to the Center of Mass**:
```
r_i = R + r'_i
v_i = V_cm + v'_i
```
Substitute this into the total angular momentum formula:
```
L = Σ_i [ (R + r'_i) x m_i * (V_cm + v'_i) ]
  = Σ_i (R x m_i * V_cm) + Σ_i (R x m_i * v'_i) + Σ_i (r'_i x m_i * V_cm) + Σ_i (r'_i x m_i * v'_i)
```
Notice that by definition of Center of Mass, $\sum_i m_i r'_i = 0$ and $\sum_i m_i v'_i = 0$.
The two cross-terms vanish! We are left with:
```
L_total = ( R x M * V_cm ) + Σ_i ( r'_i x m_i * v'_i )
```
> **The Two-Component Angular Momentum Theorem**:
> ```
> L_total = L_orbital(CM) + L_spin(about CM)
> ```
> 1. **Orbital Angular Momentum ($L_{\text{orbital}} = R \times P$)**: The angular momentum of the Center of Mass moving through space around the external origin.
> 2. **Spin Angular Momentum ($L_{\text{spin}} = \sum r'_i \times p'_i$)**: The intrinsic rotational angular momentum of the system spinning around its own Center of Mass.

**Example**: The Earth has:
* An **orbital angular momentum** revolving around the Sun once per 365 days.
* A **spin angular momentum** rotating around its polar axis once every 24 hours.

---

## 6. Summary Cheat Sheet for Module 10

| Quantity | Formula | Physical Meaning |
|---|---|---|
| **Angular Momentum** | `l = r x p` | Measure of rotational momentum about origin |
| **Torque** | `Γ = r x F` | Moment of force; causes $l$ to change |
| **Rotational Law** | `Γ_net = dl/dt` | Angular counterpart to $F = dp/dt$ |
| **Central Forces** | `Γ = 0 ===> l = const` | Produces planar motion & Kepler's 2nd Law |
| **Internal Torques** | `Σ (r_i x F_ij) = 0` | Cancel out if forces lie along connecting lines |
| **Orbital + Spin Split** | `L = (R x P_cm) + L_relative`| Total rotation decomposes into orbit + spin |


---

## 7. Worked Examples & Practice Problems

### Worked Example 10.1: Angular Momentum of a Conical Pendulum
**Problem**: A bob of mass `m` hangs from a fixed pivot by a string of length `L`. It moves in a horizontal circle of radius `R = L*sin(α)` at constant angular speed `ω`.
(a) Find the angular momentum vector `l` of the bob calculated about the **suspension pivot point O**.
(b) Compute the torque `Γ` about point O, and verify that `dl/dt = Γ`.

**Solution**:
1. **Coordinates**:
   Let the pivot point be the origin `O`. The position of the bob is:
   ```
   r(t) = R*cos(ω*t)*x_hat + R*sin(ω*t)*y_hat - h*z_hat
   ```
   where `h = L*cos(α)`.
   The velocity of the bob is:
   ```
   v(t) = -R*ω*sin(ω*t)*x_hat + R*ω*cos(ω*t)*y_hat + 0*z_hat
   ```

2. **Angular Momentum `l = r x (m*v)`**:
   ```
   l = m * |  x_hat           y_hat          z_hat  |
           |  R*cos(ω*t)      R*sin(ω*t)     -h     |
           | -R*ω*sin(ω*t)    R*ω*cos(ω*t)    0     |
     = m * [ (h*R*ω*cos(ω*t))*x_hat + (h*R*ω*sin(ω*t))*y_hat + (R²*ω)*z_hat ]
   ```
   Notice that `l` has a **constant vertical component** `l_z = m * R² * ω`, but its horizontal components rotate continuously in a circle!

3. **Rate of Change `dl/dt`**:
   ```
   dl/dt = m * h * R * ω² * [ -sin(ω*t)*x_hat + cos(ω*t)*y_hat ]
   ```

4. **Torque `Γ = r x F`**:
   The net force on the bob is the horizontal centripetal force:
   ```
   F = -m * R * ω² * [ cos(ω*t)*x_hat + sin(ω*t)*y_hat ]
   ```
   Compute torque about pivot `O`:
   ```
   Γ = r x F = (r_perp + r_z) x F = (-h * z_hat) x F
     = (-h * z_hat) x [ -m * R * ω² * (cos(ω*t)*x_hat + sin(ω*t)*y_hat) ]
     = m * h * R * ω² * [ -sin(ω*t)*x_hat + cos(ω*t)*y_hat ]
   ```
   Look at that: **`dl/dt = Γ` matches perfectly!**
**Physical Insight**: The angular momentum vector is tilted relative to the vertical axis and sweeps out a cone in space (precesses) at frequency `ω`, driven by the gravitational torque acting about the pivot point!

---

### Worked Example 10.2: Orbital and Spin Angular Momentum of a Dumbbell
**Problem**: Two equal masses `m` are attached to the ends of a rigid massless rod of length `2b`. The center of the rod moves along the $x$-axis with speed `V`, while the rod spins in the $xy$-plane at constant angular rate `ω` about its center.
Find the total angular momentum `L` about the origin.

**Solution**:
Apply the Two-Component Angular Momentum Theorem:
```
L_total = L_orbital(CM) + L_spin(about CM)
```
1. **Orbital Component**:
   Total mass: `M = 2*m`.
   Center of Mass position: `R = (V*t)*x_hat + 0*y_hat + 0*z_hat`.
   Center of Mass velocity: `V_cm = V * x_hat`.
   ```
   L_orbital = R x (M * V_cm) = (V*t * x_hat) x (2*m * V * x_hat) = 0
   ```
   *(Since CM position and velocity are collinear, orbital angular momentum about the origin is zero!)*

2. **Spin Component**:
   Relative to the Center of Mass, the two masses are at:
   `r'_1 = b*cos(ω*t)*x_hat + b*sin(ω*t)*y_hat`
   `r'_2 = -r'_1`
   Their relative velocities are:
   `v'_1 = -b*ω*sin(ω*t)*x_hat + b*ω*cos(ω*t)*y_hat`
   `v'_2 = -v'_1`
   Compute spin angular momentum:
   ```
   l'_1 = r'_1 x (m * v'_1) = m * b² * ω * z_hat
   l'_2 = (-r'_1) x [m * (-v'_1)] = m * b² * ω * z_hat
   ```
   Summing over both particles:
   ```
   L_spin = l'_1 + l'_2 = 2 * m * b² * ω * z_hat
   ```
Therefore:
```
L_total = 2 * m * b² * ω * z_hat
```

---

### Practice Problem 10.1 (To Solve)
**Statement**: A planet of mass `m` moves in an elliptical Keplerian orbit around a sun of mass `M`. At perihelion (closest approach), its distance is `r_p` and its speed is `v_p`. At aphelion (farthest distance), its distance is `r_a`.
Find the speed `v_a` at aphelion in terms of `v_p, r_p, r_a`.
* **Hint**: At both perihelion and aphelion, velocity is purely perpendicular to the position vector (`r ⊥ v`). Angular momentum is conserved: `m * r_p * v_p = m * r_a * v_a`.
* **Answer**: `v_a = v_p * (r_p / r_a)`.

---

### Practice Problem 10.2 (To Solve)
**Statement**: A particle of mass `m` slides on a frictionless horizontal table attached to a light string passing through a small hole in the center. The particle initially orbits in a circle of radius `r_1` with speed `v_1`. The string is slowly pulled downward through the hole until the radius decreases to `r_2 = r_1 / 2`.
(a) What is the new orbital speed `v_2`?
(b) How does the kinetic energy change? What supplied the work?
* **Hint**: The tension force is purely radial, exerting zero torque about the hole. Hence angular momentum is conserved: `m * r_1 * v_1 = m * r_2 * v_2`.
* **Answer**: (a) `v_2 = v_1 * (r_1 / r_2) = 2 * v_1`. (b) `T_2 = (1/2)*m*v_2² = 4 * T_1`. The kinetic energy quadrupled; the work was performed by the person pulling the tension string inward against the centrifugal force!

---

## 8. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 3:
  * Sections 3.4–3.5 (pp. 90–99): Angular Momentum, Central Forces, Orbital and Spin Decomposition.
  * Problems 3.21, 3.27, 3.33, 3.37 (pp. 102–104): Angular momentum theorems and torque proofs.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 18: "Principles of Conservation" (Sections 18.3–18.4 on angular momentum).
  * Chapter 20: "Rotation in Space" (Sections 20.1–20.3 on torque and precession).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 6: "Angular Momentum" (Sections 6.1–6.5).
