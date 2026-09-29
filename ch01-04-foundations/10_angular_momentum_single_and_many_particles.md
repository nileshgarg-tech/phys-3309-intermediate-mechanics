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
