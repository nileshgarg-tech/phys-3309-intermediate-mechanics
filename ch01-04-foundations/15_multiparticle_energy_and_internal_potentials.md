# 15. Multiparticle Energy, Internal Potentials & Thermodynamics

**Foundational Story**: Chapter 4, Sections 4.9–4.10  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 152–163)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 14
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 5

---

## 1. Two Interacting Particles: Relative vs. Center-of-Mass Motion

Consider two isolated particles of masses $m_1$ and $m_2$ interacting via a mutual central potential that depends only on their separation $r = |r_1 - r_2|$ (e.g., Earth and Moon, or a diatomic molecule).

Their positions can be mapped to:
1. **Center of Mass (CM)**: $R = (m_1 r_1 + m_2 r_2) / (m_1 + m_2)$
2. **Relative Separation**: $r = r_1 - r_2$

The total kinetic energy is:
```
T = (1/2) * m_1 * v_1² + (1/2) * m_2 * v_2²
```
Substituting $v_1 = V + (m_2/M) \dot{r}$ and $v_2 = V - (m_1/M) \dot{r}$ (where $M = m_1 + m_2$):
```
T = (1/2) * M * V_cm² + (1/2) * μ * (r_dot)²
```
where $\mu$ is the **Reduced Mass**:
```
μ = (m_1 * m_2) / (m_1 + m_2)
```
> **The Kinetic Energy Decoupling**:
> Total kinetic energy cleanly splits into:
> 1. Motion of the entire system as a single particle of mass $M$ moving at $V_{\text{cm}}$.
> 2. Relative internal motion of a fictitious single particle of reduced mass $\mu$.

---

## 2. Total Potential Energy for $N$ Particles

For an arbitrary system of $N$ particles, forces arise from two origins:
1. **External potentials**: $U_i^{\text{ext}}(r_i)$ (e.g., uniform gravity $m_i g z_i$).
2. **Internal pairwise interactions**: $U_{jk}(|r_j - r_k|)$ (e.g., interatomic forces, springs between masses).

The **Total Potential Energy** is:
```
U_total = Σ_i U_i^ext(r_i) + Σ_{j < k} U_jk(|r_j - r_k|)
```
*(Notice the summation condition $j < k$: this guarantees each interacting pair is counted exactly once!)*

### The Total Energy Conservation Law
If all external and internal forces are conservative:
```
E_total = T + U_total = Σ_i (1/2)*m_i*v_i² + Σ_i U_i^ext + Σ_{j < k} U_jk = constant!
```

---

## 3. The Rigid Body Simplification

What happens when we apply this equation to a **rigid body** (such as a spinning top or a flying wrench)?
By definition, in a perfectly rigid body, the distances between all pairs of particles are permanently fixed:
```
|r_j - r_k| = c_jk = constant
```
Because the relative distances never change:
```
Σ_{j < k} U_jk(c_jk) = constant
```
The internal potential energy is a constant number!
Since an additive constant has no effect on dynamics (recall $F = -\nabla U$), **internal potential energy can be completely ignored for rigid bodies**.

---

## 4. Non-Conservative Forces & The Bridge to Thermodynamics

In macroscopic real-world systems, non-conservative forces like friction, air drag, and inelastic collisions do work:
```
ΔE_mechanical = W_nc < 0
```
Does this mean energy is destroyed?
**No!** Feynman emphasized that energy conservation is absolute:
* When a sliding block comes to rest due to friction, its macroscopic kinetic energy does not vanish.
* The macroscopic work $W_{\text{nc}}$ was transferred into the random microscopic vibrations of the atoms in the block and table.
* The sum of microscopic kinetic and internal potential energies is called **Internal Thermal Energy** ($E_{\text{thermal}}$).
```
ΔE_mechanical + ΔE_thermal = 0   ===>   ΔE_total = 0
```
This is the First Law of Thermodynamics, born directly from the multiparticle mechanics of Newton.

---

## 5. Summary Cheat Sheet for Module 15

| Concept | Mathematical Expression | Physical Takeaway |
|---|---|---|
| **Two-Body Kinetic Energy** | `T = (1/2)M*V_cm² + (1/2)μ*v_rel²` | Decouples CM translation from internal vibration |
| **Reduced Mass** | `μ = m_1*m_2 / (m_1 + m_2)` | Effective mass for relative orbit |
| **Multiparticle Potential**| `U = Σ U_ext + Σ_{j<k} U_jk` | Pairwise internal interaction sum |
| **Rigid Body Limit** | `|r_j - r_k| = const ===> U_int = const` | Rigid bodies ignore internal potentials |
| **First Law of Thermo** | `W_nc = ΔE_thermal` | Dissipation is conversion to microscopic kinetic energy |


---

## 6. Worked Examples & Practice Problems

### Worked Example 15.1: Vibrations of a Diatomic Molecule
**Problem**: A diatomic molecule (such as Carbon Monoxide, CO) consists of two atoms of masses `m_1 = 12 amu` and `m_2 = 16 amu` bonded by an effective spring of stiffness `k = 1900 N/m`. (`1 amu ≈ 1.66 x 10^-27 kg`).
(a) Find the reduced mass `μ` of the molecule.
(b) Find the natural vibrational frequency `f` (in Hertz) of the molecule.

**Solution**:
(a) Reduced mass:
```
μ = (m_1 * m_2) / (m_1 + m_2) = (12 * 16) / (12 + 16) = 192 / 28 ≈ 6.857 amu
μ = 6.857 * (1.66 x 10^-27 kg) ≈ 1.138 x 10^-26 kg
```
Notice that the reduced mass `μ` is smaller than either individual atomic mass!

(b) Vibrational frequency:
By the two-body decoupling theorem, the internal relative motion is identical to a single particle of mass `μ` attached to a fixed wall by spring `k`:
```
ω = sqrt( k / μ ) = sqrt( 1900 / (1.138 x 10^-26) ) = sqrt( 1.67 x 10^29 ) ≈ 6.43 x 10^14 rad/s
```
Frequency in Hertz:
```
f = ω / (2*π) ≈ (6.43 x 10^14) / 6.283 ≈ 1.02 x 10^14 Hz
```
This frequency lies in the **infrared spectrum** ($\lambda = c/f pprox 2.9\,\mu	ext{m}$), exactly matching experimental infrared absorption spectroscopy!

---

### Worked Example 15.2: Inelastic Collision & Thermal Dissipation
**Problem**: A block of mass `m_1 = 2.0 kg` moving at `v_1 = 6.0 m/s` collides head-on with a stationary block of mass `m_2 = 4.0 kg`. The blocks stick together upon impact.
(a) Find their final common velocity `V_f`.
(b) Calculate the mechanical energy lost during the collision.
(c) Where did this lost mechanical energy go?

**Solution**:
(a) Conservation of linear momentum:
```
m_1 * v_1 + m_2 * (0) = (m_1 + m_2) * V_f
V_f = (m_1 * v_1) / (m_1 + m_2) = (2.0 * 6.0) / (2.0 + 4.0) = 12.0 / 6.0 = 2.0 m/s
```

(b) Mechanical Energy calculation:
* Initial kinetic energy:
  ```
  T_initial = (1/2) * m_1 * v_1² = (0.5) * (2.0) * (6.0)² = 36.0 Joules
  ```
* Final kinetic energy:
  ```
  T_final = (1/2) * (m_1 + m_2) * V_f² = (0.5) * (6.0) * (2.0)² = 12.0 Joules
  ```
* Lost mechanical energy:
  ```
  ΔE_mech = T_final - T_initial = 12.0 - 36.0 = - 24.0 Joules
  ```
Exactly **24 Joules (66.7%) of mechanical kinetic energy was lost!**

(c) **Thermal Dissipation**:
By the First Law of Thermodynamics, the total energy of the universe is conserved:
`ΔE_thermal = -ΔE_mech = +24.0 J`.
The mechanical bulk kinetic energy was transferred into random thermal vibration of the lattice atoms, slightly warming the combined block!

---

### Practice Problem 15.1 (To Solve)
**Statement**: Three equal point stars of mass `m` are located at the vertices of an equilateral triangle of side length `L`.
Find the total gravitational potential energy `U_total` of the three-star system.
* **Hint**: Use `U_total = Σ_{j < k} U_jk = U_12 + U_13 + U_23`.
* **Answer**: All 3 pairs have separation `L`. `U_total = - (G*m² / L) - (G*m² / L) - (G*m² / L) = - 3 * (G*m² / L)`.

---

### Practice Problem 15.2 (To Solve)
**Statement**: Two carts of masses `m_1` and `m_2` are connected by a spring of stiffness `k` and placed on a frictionless horizontal air track. Cart 1 is given an initial velocity `v_0` towards cart 2 which is at rest.
Find the maximum compression `x_max` of the spring during the subsequent motion.
* **Hint**: At maximum compression, both carts move with the same Center of Mass velocity `V_cm = m_1*v_0 / (m_1 + m_2)`. The kinetic energy of relative motion `(1/2)*μ*v_rel²` is completely converted into spring potential energy `(1/2)*k*x_max²`.
* **Answer**: `x_max = v_0 * sqrt(μ / k) = v_0 * sqrt( (m_1 * m_2) / (k * (m_1 + m_2)) )`.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Sections 4.9–4.10 (pp. 152–163): Energy of Interaction of Two Particles, Multiparticle Systems, Rigid Body Potential Energy.
  * Problems 4.48, 4.52, 4.55 (pp. 172–174): Two-body reduced mass energy and thermal dissipation.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 14: "Work and Potential Energy (Conclusion)" (Section 14.6 on thermal energy conservation).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.10–5.11).
