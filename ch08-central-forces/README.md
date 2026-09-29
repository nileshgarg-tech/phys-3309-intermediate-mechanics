# Chapter 8: Two-Body Central-Force Problems

Planetary orbits, Kepler's laws, reduced mass, and effective potential.

---

## Key Topics & Roadmap

* **Two-Body Reduction**:
  * Decoupling into Center of Mass (CM) motion (uniform) and relative motion `r = r_1 - r_2`.
  * **Reduced Mass**: `μ = (m_1 * m_2) / (m_1 + m_2)`.

* **Conservation of Angular Momentum**:
  * Because central forces exert zero torque (`r x F(r) = 0`), angular momentum `l = μ * r² * dθ/dt` is constant, confining motion to a single plane.

* **The Equivalent 1D Problem & Effective Potential**:
  * Radial energy equation: `E = (1/2) * μ * (dr/dt)² + U_eff(r)`.
  * **Effective Potential**: `U_eff(r) = U(r) + l² / (2 * μ * r²)`.
  * The centrifugal barrier term `l² / (2 * μ * r²)` prevents collapse into the center for non-zero angular momentum.

* **Kepler Orbits (Inverse-Square Force: `U(r) = -k/r`)**:
  * Equation of the orbit: `r(θ) = c / (1 + ε * cos(θ))`.
  * Eccentricity `ε`:
    * `ε = 0`: Circle (`E = E_min`)
    * `0 < ε < 1`: Ellipse (`E < 0`)
    * `ε = 1`: Parabola (`E = 0`)
    * `ε > 1`: Hyperbola (`E > 0`)
  * Kepler's 3rd Law: `τ² = (4 * π² * a³) / (G * (m_1 + m_2))`.

* **Orbital Transfers**:
  * Hohmann transfer orbits: calculating impulse velocity boosts `Δv` to transfer between circular orbits.
