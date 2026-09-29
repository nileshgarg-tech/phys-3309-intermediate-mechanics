# 08. Conservation of Momentum & Center of Mass

**Foundational Story**: Chapter 3, Sections 3.1 & 3.3  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 3 (pp. 83–85, 87–90)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 18 ("Principles of Conservation") & Ch. 19 ("Center of Mass")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 3

---

## 1. The Multiparticle Problem: From Atoms to Planets

Real objects are not single mathematical points. A baseball contains $\sim 10^{25}$ interacting atoms; the solar system contains a massive central star, 8 major planets, moons, asteroids, and comets, all gravitationally pulling on each other simultaneously.

How can Newtonian mechanics make sense of such enormous systems without solving $10^{25}$ coupled differential equations?

The answer lies in **internal force cancellation** and the **Center of Mass**.

---

## 2. Internal vs. External Forces

Consider an assembly of $N$ particles ($i = 1, 2, \dots, N$), each with mass $m_i$ and position vector $r_i$.
The total force acting on particle $i$ consists of two distinct parts:
```
F_i = F_i^ext + Σ_{j ≠ i} F_ij
```
1. **$F_i^{\text{ext}}$ (External Force)**: Forces exerted by agents outside the system (e.g., Earth's gravity, an external magnetic field).
2. **$F_{ij}$ (Internal Force)**: The force exerted on particle $i$ by particle $j$ inside the system.

Now, write Newton's Second Law for particle $i$:
```
dp_i / dt = F_i^ext + Σ_{j ≠ i} F_ij
```
Sum this equation over all $N$ particles in the system:
```
Σ_i (dp_i / dt) = Σ_i F_i^ext + Σ_i Σ_{j ≠ i} F_ij
```

---

## 3. The Miracle of Newton's Third Law

Look closely at the double summation of internal forces:
```
Σ_i Σ_{j ≠ i} F_ij
```
This sum contains terms like $(F_{12} + F_{21}) + (F_{13} + F_{31}) + \dots$.
By Newton's Third Law of Motion:
```
F_ij = - F_ji   ===>   F_ij + F_ji = 0
```
Every single internal interaction cancels pairwise!
```
Σ_i Σ_{j ≠ i} F_ij = 0
```
Therefore, defining the **Total Linear Momentum** $P = \sum_i p_i$:
```
dP / dt = Σ_i F_i^ext = F_net^ext
```
> **The System Momentum Conservation Theorem**:
> **Internal forces, no matter how violent, complex, or explosive, cannot change the total momentum of a system.**
> Only an external force can alter the total momentum. If $F_{\text{net}}^{\text{ext}} = 0$, then $P = \text{constant}$.

---

## 4. The Center of Mass (CM)

We define the total mass of the system:
```
M = Σ_i m_i
```
The **Center of Mass position vector** $R$ is the mass-weighted average position:
```
R = (1 / M) * Σ_i (m_i * r_i)
```
Differentiating with respect to time gives the Center of Mass velocity $V = dR/dt$:
```
V = (1 / M) * Σ_i (m_i * dr_i/dt) = (1 / M) * Σ_i p_i = P / M
```
Rearranging:
```
P = M * V
```
The total momentum of any complex system is simply the total mass multiplied by the velocity of the Center of Mass!

Differentiating once more with respect to time:
```
M * (d²R / dt²) = dP / dt = F_net^ext
```
> **The Center of Mass Theorem**:
> **The center of mass of any system of particles moves exactly like a single point particle of mass $M$ acted upon by the net external force.**

### Beautiful Physical Example: The Exploding Artillery Shell
Suppose an artillery shell is fired along a graceful parabolic arc under gravity. Midway through its flight, an internal charge detonates, blowing the shell into hundreds of jagged shrapnel fragments traveling in all directions.
* The fragments fly chaotically.
* Yet because the explosion is purely internal ($F_{\text{internal}}$), **the Center of Mass of all the scattered fragments continues along the exact same original parabolic trajectory as if nothing happened!**

---

## 5. Continuous Bodies

For a continuous solid body with density $\rho(r)$, the sum becomes a volume integral:
```
R = (1 / M) * ∫ r dm = (1 / M) * ∫ r * ρ(r) dV
```
where $M = \int \rho(r) dV$.

---

## 6. Summary Cheat Sheet for Module 08

| Concept | Formula | Physical Interpretation |
|---|---|---|
| **Center of Mass (Discrete)** | `R = (1/M) * Σ m_i*r_i` | Mass-weighted geometric center |
| **Center of Mass (Continuous)**| `R = (1/M) * ∫ r dm` | Volume integral over mass distribution |
| **Total Momentum** | `P = M * V_cm` | Equal to whole mass moving at CM velocity |
| **Internal Cancellation** | `Σ F_ij = 0` | By Newton's 3rd Law, internal forces do not change $P$ |
| **Center of Mass Motion** | `M * d²R/dt² = F_net^ext` | CM ignores internal interactions entirely |


---

## 7. Worked Examples & Practice Problems

### Worked Example 8.1: The Man on a Sliding Ice Raft
**Problem**: A man of mass `m = 80 kg` stands at the left end of a flat rectangular wooden raft of mass `M = 120 kg` and length `L = 6.0 meters`. The raft rests on a frictionless sheet of frozen ice.
The man walks steadily from the left end of the raft to the right end and stops.
(a) How far does the raft move across the ice during this walk?
(b) How far does the man move relative to the ice?

**Solution**:
1. **System Identification**:
   Consider the closed system (Man + Raft). 
   Because the ice surface is frictionless, **there is zero net external horizontal force on the system**:
   ```
   F_net_x^ext = 0  ===>  X_cm = constant!
   ```
   The Center of Mass of the entire system cannot move relative to the ice.

2. **Center of Mass Coordinates**:
   Choose the initial position of the left edge of the raft as the coordinate origin `x = 0`.
   * Initial position of the man: `x_m1 = 0`.
   * Initial center of mass of the uniform raft: `x_r1 = L / 2`.
   The initial center of mass of the system is:
   ```
   X_cm = (m * x_m1 + M * x_r1) / (m + M) = (0 + M * (L/2)) / (m + M)
   ```

3. **Final Positions**:
   Let the raft shift to the left by a distance `d` (so its left edge is at `-d`).
   * Final position of the raft's center: `x_r2 = L/2 - d`.
   * The man walked to the right end of the raft, so his final position is: `x_m2 = L - d`.
   The final Center of Mass is:
   ```
   X_cm = [ m * (L - d) + M * (L/2 - d) ] / (m + M)
   ```

4. **Equating Initial and Final CM**:
   ```
   M * (L/2) = m * (L - d) + M * (L/2 - d)
   M * (L/2) = m*L - m*d + M*(L/2) - M*d
   0 = m*L - (m + M)*d
   ```
   Solving for the displacement of the raft `d`:
   ```
   d = [ m / (m + M) ] * L
   ```
   Substitute the numerical values (`m = 80 kg`, `M = 120 kg`, `L = 6.0 m`):
   ```
   d = [ 80 / (80 + 120) ] * 6.0 = (80 / 200) * 6.0 = 0.40 * 6.0 = 2.40 meters
   ```
(a) The raft moves **2.40 meters to the left**.
(b) The man's displacement relative to the ice is:
```
Δx_man = L - d = 6.0 - 2.40 = 3.60 meters to the right.
```
**Physical Insight**: Because internal forces cannot accelerate the Center of Mass, pushing the raft backward with his feet moves the raft by `2.4 m` while moving the man forward by `3.6 m`, keeping the CM pinned in place.

---

### Worked Example 8.2: Center of Mass of a Solid Hemisphere
**Problem**: Calculate the center of mass of a solid, uniform hemisphere of radius `R` and constant mass density `ρ`.

**Solution**:
Place the flat base of the hemisphere on the $xy$-plane centered at the origin, with the dome extending into $z \ge 0$.
By azimuthal symmetry around the $z$-axis:
```
X_cm = 0,   Y_cm = 0
```
We only need to calculate $Z_{	ext{cm}}$:
```
Z_cm = (1 / M) * ∫ z dm
```
Divide the hemisphere into thin horizontal circular slices of thickness $dz$ at height $z$ ($0 \le z \le R$).
The radius of a circular disk at height $z$ is $r(z) = \sqrt{R^2 - z^2}$.
The volume of this disk slice is:
```
dV = π * r(z)² dz = π * (R² - z²) dz
dm = ρ * dV = ρ * π * (R² - z²) dz
```
The total mass of the hemisphere is:
```
M = ρ * (2/3) * π * R³
```
Now compute the numerator integral:
```
∫ z dm = ρ * π * ∫_0^R z * (R² - z²) dz = ρ * π * ∫_0^R (R²*z - z³) dz
       = ρ * π * [ (1/2)*R²*z² - (1/4)*z⁴ ]_0^R
       = ρ * π * [ (1/2)*R⁴ - (1/4)*R⁴ ] = ρ * π * (1/4) * R⁴
```
Divide by total mass $M$:
```
Z_cm = [ ρ * π * (1/4) * R⁴ ] / [ ρ * (2/3) * π * R³ ]
     = (1/4) / (2/3) * R = (3 / 8) * R
```
**Physical Result**: The Center of Mass of a solid hemisphere lies on its symmetry axis at a distance of **`3/8 R = 0.375 R`** from the flat base.

---

### Practice Problem 8.1 (To Solve)
**Statement**: A projectile of mass `M` is fired with launch speed `v_0` at an angle `θ` above the horizontal. At the very apex of its trajectory, the projectile explodes into two equal fragments of mass `m_1 = m_2 = M / 2`. 
One fragment falls vertically downward from rest immediately after the explosion.
How far from the launch point does the second fragment land?
* **Hint**: The internal explosion cannot change the motion of the Center of Mass. The CM lands at the standard range `R_cm = (v_0² * sin(2θ)) / g`. At the moment of landing, fragment 1 is on the ground at `x_1 = R_cm / 2`.
* **Answer**: `X_cm = (x_1 + x_2) / 2 ===> R_cm = (R_cm/2 + x_2) / 2 ===> x_2 = (3/2) * R_cm`. The second fragment lands at 1.5 times the normal range!

---

### Practice Problem 8.2 (To Solve)
**Statement**: Find the center of mass of a thin uniform wire of total mass `M` bent into a semicircle of radius `R` lying in the $xy$-plane (`y ≥ 0`).
* **Hint**: Parametrize the wire in polar coordinates: `x = R*cos(θ)`, `y = R*sin(θ)`, `dl = R*dθ` for `θ ∈ [0, π]`. Mass per unit length `λ = M / (π*R)`.
* **Answer**: `X_cm = 0`, `Y_cm = (1/M) * ∫_0^π (R*sin(θ)) * (M/(π*R)) * R dθ = (R / π) * [-cos(θ)]_0^π = 2*R / π ≈ 0.637 R`.

---

## 8. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 3:
  * Sections 3.1 & 3.3 (pp. 83–85, 87–90): Conservation of Momentum, Center of Mass.
  * Problems 3.1, 3.4, 3.8, 3.11 (pp. 99–101): Center of mass integrations and multi-particle systems.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 18: "Principles of Conservation" (Sections 18.1–18.2).
  * Chapter 19: "Center of Mass; Moment of Inertia" (Section 19.1).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 3: "Forces and Equations of Motion" & Chapter 4: "Momentum" (Sections 4.1–4.4).
