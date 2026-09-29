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
