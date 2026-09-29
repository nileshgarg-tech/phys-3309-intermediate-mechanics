# Chapter 7: Lagrange's Equations

Lagrangian mechanics using generalized coordinates and energy.

---

## Key Topics & Roadmap

* **Hamilton's Principle (Principle of Least Action)**:
  * The actual motion makes the action `S = ∫ L dt` stationary, where `L = T - U`.

* **Lagrange's Equations**:
  * For each generalized coordinate `q_i`:
    * `d/dt (∂L/∂q_dot_i) - ∂L/∂q_i = 0`

* **Generalized Momentum & Conservation**:
  * Canonical / generalized momentum: `p_i = ∂L/∂q_dot_i`.
  * **Ignorable (Cyclic) Coordinates**: If `L` does not depend on `q_i` explicitly (`∂L/∂q_i = 0`), then `p_i` is strictly conserved: `dp_i/dt = 0`.

* **Noether's Theorem & Symmetries**:
  * Spatial translational invariance → Conservation of total linear momentum.
  * Rotational invariance → Conservation of total angular momentum.
  * Time translation invariance → Conservation of total energy (Hamiltonian `H = Σ p_i * q_dot_i - L = const`).

* **Constrained Systems & Lagrange Multipliers**:
  * Incorporating holonomic constraints `f(q_1, ..., q_n) = 0` via multipliers `λ` to determine constraint forces without solving Newton's equations vectorially.
