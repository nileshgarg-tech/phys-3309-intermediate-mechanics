# Chapter 13: Hamiltonian Mechanics

The canonical Hamiltonian framework, phase-space dynamics, and Liouville's theorem.

---

## Key Topics & Roadmap

* **Canonical Variables & The Legendre Transformation**:
  * Generalized coordinates: `q_i` (positions)
  * Generalized / canonical momenta: `p_i = ∂L/∂q_dot_i`
  * The **Hamiltonian function** `H` is obtained via Legendre transformation:
    * `H(q_1, ..., q_n, p_1, ..., p_n, t) = Σ (p_i * q_dot_i) - L`
  * For standard systems where potential energy `U = U(q)` and kinetic energy `T` is quadratic in velocities, `H = T + U = E_total`.

* **Hamilton's Equations of Motion**:
  * For each degree of freedom `i = 1, ..., n`:
    * `dq_i/dt = ∂H/∂p_i`
    * `dp_i/dt = -∂H/∂q_i`
  * This replaces `n` second-order differential equations (Lagrange) with `2n` first-order symmetric differential equations.

* **Lagrangian vs. Hamiltonian Formulation**:
  * **Lagrangian**: Natural setting is the `n`-dimensional *configuration space* `(q_1, ..., q_n)`.
  * **Hamiltonian**: Natural setting is the `2n`-dimensional *phase space* `(q_1, ..., q_n, p_1, ..., p_n)`.
  * Serves as the direct mathematical stepping-stone to Quantum Mechanics (Schrödinger equation and operator observables) and Statistical Mechanics.

* **Conservation Laws & Ignorable Coordinates**:
  * If coordinate `q_i` is cyclic/ignorable (`∂H/∂q_i = 0`), its conjugate momentum is strictly conserved: `dp_i/dt = 0`.
  * Total time derivative of the Hamiltonian:
    * `dH/dt = ∂H/∂t`
  * If `H` does not explicitly depend on time (`∂H/∂t = 0`), total energy is conserved.

* **Phase Space & Liouville's Theorem**:
  * Trajectories in phase space never intersect (guaranteed by uniqueness of solutions to first-order ODEs).
  * **Liouville's Theorem**: The phase-space volume `V` occupied by a collection of microstates is invariant under Hamiltonian time evolution (`dV/dt = 0`). The flow of phase-space points behaves like an incompressible fluid.
