# 15. Multiparticle Energy, Internal Potentials & Thermodynamics

**Foundational Story**: Chapter 4, Sections 4.9–4.10  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 152–163)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 14
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 5

---

## 1. Two Interacting Particles: Relative vs. Center-of-Mass Motion

Consider two isolated particles of masses $m_1$ and $m_2$ interacting via a mutual central potential that depends only on their separation $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$ (e.g., Earth and Moon, or a diatomic molecule), so $U = U(\mathbf{r})$.

Following Taylor (Sec. 4.9), their positions can be decomposed into:
1. **Center of Mass (CM)**: $\mathbf{R} = \frac{m_1 \mathbf{r}_1 + m_2 \mathbf{r}_2}{m_1 + m_2} = \frac{m_1 \mathbf{r}_1 + m_2 \mathbf{r}_2}{M}$
2. **Relative Separation**: $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$

Inverting these gives:

$$
\mathbf{r}_1 = \mathbf{R} + \frac{m_2}{M}\mathbf{r}, \quad \mathbf{r}_2 = \mathbf{R} - \frac{m_1}{M}\mathbf{r}
$$

Differentiating with respect to time gives the velocities:

$$
\dot{\mathbf{r}}_1 = \dot{\mathbf{R}} + \frac{m_2}{M}\dot{\mathbf{r}}, \quad \dot{\mathbf{r}}_2 = \dot{\mathbf{R}} - \frac{m_1}{M}\dot{\mathbf{r}}
$$

The total kinetic energy is:

$$
T = \frac{1}{2} m_1 \dot{\mathbf{r}}_1^2 + \frac{1}{2} m_2 \dot{\mathbf{r}}_2^2
$$

Substituting the velocities, the cross terms cancel identically (Taylor, Eq. 4.87):

$$
T = \frac{1}{2} M \dot{\mathbf{R}}^2 + \frac{1}{2} \mu \dot{\mathbf{r}}^2
$$

where $\mu$ is the **Reduced Mass** (Taylor, Eq. 4.88):

$$
\mu = \frac{m_1 m_2}{m_1 + m_2}
$$

The total mechanical energy becomes (Taylor, Eq. 4.89):

$$
E = T + U = \frac{1}{2} M \dot{\mathbf{R}}^2 + \left[ \frac{1}{2} \mu \dot{\mathbf{r}}^2 + U(\mathbf{r}) \right]
$$

> **The Kinetic Energy Decoupling (Taylor, Eq. 4.87)**:  
> Total kinetic energy cleanly splits into:
> 1. Motion of the entire system as a single particle of mass $M$ moving with the CM velocity $\dot{\mathbf{R}}$.
> 2. Relative internal motion of a fictitious single particle of reduced mass $\mu$ moving with relative velocity $\dot{\mathbf{r}}$.

---

## 2. Total Potential Energy for $N$ Particles

For an arbitrary system of $N$ particles indexed by $\alpha = 1, \dots, N$ (Taylor, Sec. 4.10), forces arise from two origins:
1. **External potentials**: $U_\alpha^{\text{ext}}(\mathbf{r}_\alpha)$ (e.g., uniform gravity $m_\alpha g z_\alpha$).
2. **Internal pairwise interactions**: $U_{\alpha\beta}(|\mathbf{r}_\alpha - \mathbf{r}_\beta|)$ (e.g., interatomic forces, springs between masses).

The **Total Potential Energy** is (Taylor, Eq. 4.103):

$$
U = U^{\text{ext}} + U^{\text{int}} = \sum_{\alpha=1}^N U_\alpha^{\text{ext}}(\mathbf{r}_\alpha) + \sum_{\alpha < \beta} U_{\alpha\beta}(|\mathbf{r}_\alpha - \mathbf{r}_\beta|)
$$

*(Notice the summation condition $\alpha < \beta$: this guarantees each interacting pair is counted exactly once!)*

### The Total Energy Conservation Law
Following Taylor (Eq. 4.96), total kinetic energy decomposes about the CM:

$$
T = \sum_{\alpha=1}^N \frac{1}{2} m_\alpha \dot{\mathbf{r}}_\alpha^2 = \frac{1}{2} M \dot{\mathbf{R}}^2 + \sum_{\alpha=1}^N \frac{1}{2} m_\alpha (\dot{\mathbf{r}}'_\alpha)^2
$$

If all external and internal forces are conservative, total mechanical energy is conserved (Taylor, Eq. 4.104):

$$
E = T + U = \text{constant}
$$

---

## 3. The Rigid Body Simplification

What happens when we apply this equation to a **rigid body** (such as a spinning top or a flying wrench)?  
By definition, in a perfectly rigid body, the distances between all pairs of particles are permanently fixed:

$$
|\mathbf{r}_\alpha - \mathbf{r}_\beta| = c_{\alpha\beta} = \text{constant}
$$

Because the relative distances never change:

$$
U^{\text{int}} = \sum_{\alpha < \beta} U_{\alpha\beta}(c_{\alpha\beta}) = \text{constant}
$$

The internal potential energy is an unchanging constant number!  
Since an additive constant has no effect on dynamics (recall $\mathbf{F} = -\nabla U$), **internal potential energy can be completely ignored for rigid bodies** (Taylor, Sec. 4.10).

---

## 4. Non-Conservative Forces & The Bridge to Thermodynamics

In macroscopic real-world systems, non-conservative forces like friction, air drag, and inelastic collisions do work:

$$
\Delta E_{\text{mechanical}} = W_{\text{nc}} < 0
$$

Does this mean energy is destroyed?  
**No!** Feynman and Taylor emphasize that energy conservation is absolute:
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
| **Two-Body Kinetic Energy** | $T = \frac{1}{2}M \dot{\mathbf{R}}^2 + \frac{1}{2}\mu \dot{\mathbf{r}}^2$ | Decouples CM translation from internal vibration (Taylor, Eq. 4.87) |
| **Reduced Mass** | $\mu = \frac{m_1 m_2}{m_1 + m_2}$ | Effective mass for relative motion (Taylor, Eq. 4.88) |
| **Multiparticle Potential**| $U = \sum_\alpha U_\alpha^{\text{ext}} + \sum_{\alpha < \beta} U_{\alpha\beta}$ | Pairwise internal interaction sum (Taylor, Eq. 4.103) |
| **Rigid Body Limit** | $|\mathbf{r}_\alpha - \mathbf{r}_\beta| = \text{const} \implies U^{\text{int}} = \text{const}$ | Rigid bodies ignore internal potentials |
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
**Statement**: Three equal point stars of mass $m$ are located at the vertices of an equilateral triangle of side length $L$. Find the total gravitational potential energy $U$ of the three-star system.

**Hint**: Sum the pairwise interaction potential over all unique pairs:

$$
U = \sum_{\alpha < \beta} U_{\alpha\beta} = U_{12} + U_{13} + U_{23}
$$

**Answer**: All 3 pairs have separation $L$:

$$
U = -\frac{Gm^2}{L} - \frac{Gm^2}{L} - \frac{Gm^2}{L} = -3 \frac{Gm^2}{L}
$$

---

### Practice Problem 15.2 (To Solve)
**Statement**: Two carts of masses $m_1$ and $m_2$ are connected by a spring of stiffness $k$ and placed on a frictionless horizontal air track. Cart 1 is given an initial velocity $v_0$ towards cart 2 which is at rest. Find the maximum compression $x_{\text{max}}$ of the spring during the subsequent motion.

**Hint**: At maximum compression, both carts move with the same Center of Mass velocity $V_{\text{cm}} = \frac{m_1 v_0}{m_1 + m_2}$. The kinetic energy of relative motion is completely converted into spring potential energy:

$$
\frac{1}{2}\mu v_{\text{rel}}^2 = \frac{1}{2}k x_{\text{max}}^2
$$

**Answer**:

$$
x_{\text{max}} = v_0 \sqrt{\frac{\mu}{k}} = v_0 \sqrt{\frac{m_1 m_2}{k (m_1 + m_2)}}
$$

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Sections 4.9–4.10 (pp. 152–163): Energy of Interaction of Two Particles, Multiparticle Systems, Rigid Body Potential Energy.
  * Problems 4.48, 4.52, 4.55 (pp. 172–174): Two-body reduced mass energy and thermal dissipation.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 14: "Work and Potential Energy (Conclusion)" (Section 14.6 on thermal energy conservation).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.10–5.11).\n
