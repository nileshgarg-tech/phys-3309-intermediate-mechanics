# 15. Multiparticle Energy, Internal Potentials & Thermodynamics

**Foundational Story**: Chapter 4, Sections 4.9–4.10  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 152–163)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 14
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 5

---

## 1. Two Interacting Particles: Relative vs. Center-of-Mass Motion

Consider two isolated particles of masses $m_1$ and $m_2$ interacting via a mutual central potential that depends only on their separation $r = |\mathbf{r}_1 - \mathbf{r}_2|$ (e.g., Earth and Moon, or a diatomic molecule).

Their positions can be mapped to:
1. **Center of Mass (CM)**: $\mathbf{R} = \frac{m_1 \mathbf{r}_1 + m_2 \mathbf{r}_2}{m_1 + m_2}$
2. **Relative Separation**: $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$

The total kinetic energy is:

$$
T = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2
$$

Substituting $\mathbf{v}_1 = \mathbf{V}_{\text{cm}} + \frac{m_2}{M}\dot{\mathbf{r}}$ and $\mathbf{v}_2 = \mathbf{V}_{\text{cm}} - \frac{m_1}{M}\dot{\mathbf{r}}$ (where $M = m_1 + m_2$):

$$
T = \frac{1}{2} M V_{\text{cm}}^2 + \frac{1}{2} \mu \dot{r}^2
$$

where $\mu$ is the **Reduced Mass**:

$$
\mu = \frac{m_1 m_2}{m_1 + m_2}
$$

> **The Kinetic Energy Decoupling**:  
> Total kinetic energy cleanly splits into:
> 1. Motion of the entire system as a single particle of mass $M$ moving at $\mathbf{V}_{\text{cm}}$.
> 2. Relative internal motion of a fictitious single particle of reduced mass $\mu$.

---

## 2. Total Potential Energy for $N$ Particles

For an arbitrary system of $N$ particles, forces arise from two origins:
1. **External potentials**: $U_i^{\text{ext}}(\mathbf{r}_i)$ (e.g., uniform gravity $m_i g z_i$).
2. **Internal pairwise interactions**: $U_{jk}(|\mathbf{r}_j - \mathbf{r}_k|)$ (e.g., interatomic forces, springs between masses).

The **Total Potential Energy** is:

$$
U_{\text{total}} = \sum_{i=1}^N U_i^{\text{ext}}(\mathbf{r}_i) + \sum_{j < k} U_{jk}(|\mathbf{r}_j - \mathbf{r}_k|)
$$

*(Notice the summation condition $j < k$: this guarantees each interacting pair is counted exactly once!)*

### The Total Energy Conservation Law
If all external and internal forces are conservative:

$$
E_{\text{total}} = T + U_{\text{total}} = \sum_{i=1}^N \frac{1}{2} m_i v_i^2 + \sum_{i=1}^N U_i^{\text{ext}} + \sum_{j < k} U_{jk} = \text{constant}
$$

---

## 3. The Rigid Body Simplification

What happens when we apply this equation to a **rigid body** (such as a spinning top or a flying wrench)?  
By definition, in a perfectly rigid body, the distances between all pairs of particles are permanently fixed:

$$
|\mathbf{r}_j - \mathbf{r}_k| = c_{jk} = \text{constant}
$$

Because the relative distances never change:

$$
\sum_{j < k} U_{jk}(c_{jk}) = \text{constant}
$$

The internal potential energy is a constant number!  
Since an additive constant has no effect on dynamics (recall $\mathbf{F} = -\nabla U$), **internal potential energy can be completely ignored for rigid bodies**.

---

## 4. Non-Conservative Forces & The Bridge to Thermodynamics

In macroscopic real-world systems, non-conservative forces like friction, air drag, and inelastic collisions do work:

$$
\Delta E_{\text{mechanical}} = W_{\text{nc}} < 0
$$

Does this mean energy is destroyed?  
**No!** Feynman emphasized that energy conservation is absolute:
* When a sliding block comes to rest due to friction, its macroscopic kinetic energy does not vanish.
* The macroscopic work $W_{\text{nc}}$ was transferred into the random microscopic vibrations of the atoms in the block and table.
* The sum of microscopic kinetic and internal potential energies is called **Internal Thermal Energy** ($E_{\text{thermal}}$).

$$
\Delta E_{\text{mechanical}} + \Delta E_{\text{thermal}} = 0 \implies \Delta E_{\text{total}} = 0
$$

This is the First Law of Thermodynamics, born directly from the multiparticle mechanics of Newton.

---

## 5. Summary Cheat Sheet for Module 15

| Concept | Mathematical Expression | Physical Takeaway |
|---|---|---|
| **Two-Body Kinetic Energy** | $T = \frac{1}{2}M V_{\text{cm}}^2 + \frac{1}{2}\mu v_{\text{rel}}^2$ | Decouples CM translation from internal vibration |
| **Reduced Mass** | $\mu = \frac{m_1 m_2}{m_1 + m_2}$ | Effective mass for relative orbit |
| **Multiparticle Potential**| $U = \sum U_{\text{ext}} + \sum_{j<k} U_{jk}$ | Pairwise internal interaction sum |
| **Rigid Body Limit** | $|\mathbf{r}_j - \mathbf{r}_k| = \text{const} \implies U_{\text{int}} = \text{const}$ | Rigid bodies ignore internal potentials |
| **First Law of Thermo** | $W_{\text{nc}} = -\Delta E_{\text{thermal}}$ | Dissipation is conversion to microscopic thermal energy |

---

## 6. Worked Examples & Practice Problems

### Worked Example 15.1: Vibrations of a Diatomic Molecule
**Problem**: A diatomic molecule (such as Carbon Monoxide, CO) consists of two atoms of masses $m_1 = 12\text{ amu}$ and $m_2 = 16\text{ amu}$ bonded by an effective spring of stiffness $k = 1900\text{ N/m}$. ($1\text{ amu} \approx 1.66 \times 10^{-27}\text{ kg}$).  
(a) Find the reduced mass $\mu$ of the molecule.  
(b) Find the natural vibrational frequency $f$ (in Hertz) of the molecule.

**Solution**:  
(a) Reduced mass:

$$
\mu = \frac{m_1 m_2}{m_1 + m_2} = \frac{12 \times 16}{12 + 16} = \frac{192}{28} \approx 6.857\text{ amu}
$$

$$
\mu = 6.857 \times (1.66 \times 10^{-27}\text{ kg}) \approx 1.138 \times 10^{-26}\text{ kg}
$$

Notice that the reduced mass $\mu$ is smaller than either individual atomic mass!

(b) Vibrational frequency:  
By the two-body decoupling theorem, the internal relative motion is identical to a single particle of mass $\mu$ attached to a fixed wall by spring $k$:

$$
\omega = \sqrt{\frac{k}{\mu}} = \sqrt{\frac{1900}{1.138 \times 10^{-26}}} = \sqrt{1.67 \times 10^{29}} \approx 6.43 \times 10^{14}\text{ rad/s}
$$

Frequency in Hertz:

$$
f = \frac{\omega}{2\pi} \approx \frac{6.43 \times 10^{14}}{6.283} \approx 1.02 \times 10^{14}\text{ Hz}
$$

This frequency lies in the **infrared spectrum** ($\lambda = c/f \approx 2.9\,\mu\text{m}$), exactly matching experimental infrared absorption spectroscopy!

---

### Worked Example 15.2: Inelastic Collision & Thermal Dissipation
**Problem**: A block of mass $m_1 = 2.0\text{ kg}$ moving at $v_1 = 6.0\text{ m/s}$ collides head-on with a stationary block of mass $m_2 = 4.0\text{ kg}$. The blocks stick together upon impact.  
(a) Find their final common velocity $V_f$.  
(b) Calculate the mechanical energy lost during the collision.  
(c) Where did this lost mechanical energy go?

**Solution**:  
(a) Conservation of linear momentum:

$$
m_1 v_1 + m_2 (0) = (m_1 + m_2) V_f \implies V_f = \frac{m_1 v_1}{m_1 + m_2} = \frac{2.0 \times 6.0}{2.0 + 4.0} = 2.0\text{ m/s}
$$

(b) Mechanical Energy calculation:
* Initial kinetic energy:

$$
T_{\text{initial}} = \frac{1}{2} m_1 v_1^2 = (0.5)(2.0)(6.0)^2 = 36.0\text{ Joules}
$$

* Final kinetic energy:

$$
T_{\text{final}} = \frac{1}{2} (m_1 + m_2) V_f^2 = (0.5)(6.0)(2.0)^2 = 12.0\text{ Joules}
$$

* Lost mechanical energy:

$$
\Delta E_{\text{mech}} = T_{\text{final}} - T_{\text{initial}} = 12.0 - 36.0 = -24.0\text{ Joules}
$$

Exactly **$24\text{ Joules}$ ($66.7\%$) of mechanical kinetic energy was lost!**

(c) **Thermal Dissipation**:  
By the First Law of Thermodynamics, the total energy of the universe is conserved:

$$
\Delta E_{\text{thermal}} = -\Delta E_{\text{mech}} = +24.0\text{ J}
$$

The mechanical bulk kinetic energy was transferred into random thermal vibration of the lattice atoms, slightly warming the combined block!

---

### Practice Problem 15.1 (To Solve)
**Statement**: Three equal point stars of mass $m$ are located at the vertices of an equilateral triangle of side length $L$. Find the total gravitational potential energy $U_{\text{total}}$ of the three-star system.
* **Hint**: Use $U_{\text{total}} = \sum_{j < k} U_{jk} = U_{12} + U_{13} + U_{23}$.
* **Answer**: All 3 pairs have separation $L$.

$$
U_{\text{total}} = -\frac{Gm^2}{L} - \frac{Gm^2}{L} - \frac{Gm^2}{L} = -3 \frac{Gm^2}{L}
$$

---

### Practice Problem 15.2 (To Solve)
**Statement**: Two carts of masses $m_1$ and $m_2$ are connected by a spring of stiffness $k$ and placed on a frictionless horizontal air track. Cart 1 is given an initial velocity $v_0$ towards cart 2 which is at rest. Find the maximum compression $x_{\text{max}}$ of the spring during the subsequent motion.
* **Hint**: At maximum compression, both carts move with the same Center of Mass velocity $V_{\text{cm}} = \frac{m_1 v_0}{m_1 + m_2}$. The kinetic energy of relative motion $\frac{1}{2}\mu v_{\text{rel}}^2$ is completely converted into spring potential energy $\frac{1}{2}k x_{\text{max}}^2$.
* **Answer**: $x_{\text{max}} = v_0 \sqrt{\frac{\mu}{k}} = v_0 \sqrt{\frac{m_1 m_2}{k (m_1 + m_2)}}$.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Sections 4.9–4.10 (pp. 152–163): Energy of Interaction of Two Particles, Multiparticle Systems, Rigid Body Potential Energy.
  * Problems 4.48, 4.52, 4.55 (pp. 172–174): Two-body reduced mass energy and thermal dissipation.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 14: "Work and Potential Energy (Conclusion)" (Section 14.6 on thermal energy conservation).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.10–5.11).\n
