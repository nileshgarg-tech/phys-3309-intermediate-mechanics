# Chapter 11: Coupled Oscillators & Normal Modes

Systems with multiple degrees of freedom, matrix methods, and normal coordinates.

---

## Key Topics & Roadmap

* **Lagrangian for Small Oscillations**:
  * Kinetic energy quadratic form: `T = (1/2) * Σ M_jk * q_dot_j * q_dot_k = (1/2) * q_dot^T * M * q_dot`.
  * Potential energy quadratic form (Taylor expanded about equilibrium): `U = (1/2) * Σ K_jk * q_j * q_k = (1/2) * q^T * K * q`.
  * Both mass matrix `M` and stiffness matrix `K` are symmetric and real.

* **Equations of Motion & Secular Equation**:
  * `M * d²q/dt² + K * q = 0`.
  * Proposing normal mode harmonic solutions `q(t) = a * cos(ω*t - δ)` leads to the matrix eigenvalue equation:
    * `(K - ω² * M) * a = 0`.
  * **Secular Equation**: `det(K - ω² * M) = 0` yields the `n` normal frequencies `ω_1, ω_2, ..., ω_n`.

* **Normal Modes & Coordinates**:
  * Each eigenfrequency `ω_r` has a corresponding eigenvector (mode shape) `a^(r)`.
  * General motion is an exact superposition of normal modes:
    * `q(t) = Σ A_r * a^(r) * cos(ω_r*t - δ_r)`.
  * **Normal Coordinates (`ξ_r`)**: Linear combinations of physical coordinates `q_j` that completely decouple the equations of motion:
    * `d²ξ_r/dt² + ω_r² * ξ_r = 0`.

* **Classic Model Systems**:
  * Two equal masses connected by three identical springs (symmetric in-phase mode and antisymmetric out-of-phase mode).
  * Weakly coupled pendulums (phenomenon of beats / energy sloshing).
  * Double pendulum (small oscillations vs. onset of chaos at large angles).
