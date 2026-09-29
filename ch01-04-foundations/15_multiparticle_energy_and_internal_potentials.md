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
