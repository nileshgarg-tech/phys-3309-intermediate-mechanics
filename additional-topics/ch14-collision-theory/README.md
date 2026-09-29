# Chapter 14: Collision Theory & Scattering

Impact parameters, cross sections, Rutherford scattering, and CM vs. Laboratory frame transformations.

---

## Key Topics & Roadmap

* **Scattering Geometry & Impact Parameter**:
  * An incident projectile approaches a target with initial speed `v` at an offset perpendicular distance **impact parameter** `b`.
  * The force deflects the particle into a final **scattering angle** `θ`.

* **Differential Scattering Cross Section (`dσ/dΩ`)**:
  * Definition: The number of particles scattered into solid angle `dΩ = sin(θ) dθ dϕ` per unit time, divided by the incident flux `I`:
    * `dσ/dΩ = (b / sin(θ)) * |db/dθ|`
  * **Total Cross Section**:
    * `σ_tot = ∫ (dσ/dΩ) dΩ = 2*π * ∫ (dσ/dΩ) * sin(θ) dθ`
    * Represents the effective target area presented by the scatterer.

* **Hard-Sphere Scattering (Benchmark Example)**:
  * For elastic collision with an impenetrable sphere of radius `R`:
    * `b = R * cos(θ/2)`
    * `dσ/dΩ = R² / 4` (isotropic scattering).
    * `σ_tot = π * R²` (matches geometric cross-sectional area).

* **Rutherford Scattering (Coulomb Potential `U(r) = k / r`)**:
  * Trajectory is hyperbolic with impact parameter:
    * `b = (k / (2*E)) * cot(θ/2)`
  * **Rutherford Cross Section Formula**:
    * `dσ/dΩ = (k / (4*E))² * (1 / sin⁴(θ/2))`
  * Strong forward peaking (`θ → 0`); total cross section diverges due to long-range `1/r` potential.

* **Center of Mass (CM) vs. Laboratory (Lab) Frames**:
  * Theoretical calculations are performed in the CM frame where total momentum is zero.
  * Laboratory frame (target initially at rest):
    * Relation between angles: `tan(θ_lab) = sin(θ_cm) / (cos(θ_cm) + m_1/m_2)`.
    * Transforming differential cross sections:
      * `(dσ/dΩ)_lab = (dσ/dΩ)_cm * |d(cos θ_cm) / d(cos θ_lab)|`.
