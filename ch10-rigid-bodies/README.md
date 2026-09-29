# Chapter 10: Rotational Motion of Rigid Bodies

3D rotations, moment of inertia tensor, principal axes, and Euler's equations of motion.

---

## Key Topics & Roadmap

* **Angular Momentum & The Inertia Tensor**:
  * For a 3D rigid body rotating with angular velocity `ω`:
    * `L = I * ω`, where `I` is a 3x3 symmetric matrix:
      * Diagonal moments: `I_xx = ∫ (y² + z²) dm`, `I_yy = ∫ (x² + z²) dm`, `I_zz = ∫ (x² + y²) dm`.
      * Products of inertia: `I_xy = -∫ x*y dm`, `I_xz = -∫ x*z dm`, `I_yz = -∫ y*z dm`.

* **Principal Axes of Inertia**:
  * In the principal coordinate basis, `I` is diagonal:
    * `I = diag(λ_1, λ_2, λ_3)`.
  * Finding principal moments and axes requires solving the eigenvalue problem:
    * `det(I - λ * 1) = 0`.

* **Euler's Equations of Motion (In Body Frame)**:
  * Along the principal axes:
    * `λ_1 * dω_1/dt - (λ_2 - λ_3) * ω_2 * ω_3 = Γ_1`
    * `λ_2 * dω_2/dt - (λ_3 - λ_1) * ω_3 * ω_1 = Γ_2`
    * `λ_3 * dω_3/dt - (λ_1 - λ_2) * ω_1 * ω_2 = Γ_3`

* **Torque-Free Precession & Stability**:
  * Symmetric top (`λ_1 = λ_2 ≠ λ_3`): Precession of `ω` around the symmetry axis at rate `Ω_prec = ((λ_1 - λ_3) / λ_1) * ω_3`.
  * Intermediate axis instability (Tennis racket theorem): Rotation about intermediate principal axis `λ_2` is dynamically unstable.

* **Euler Angles (`ϕ, θ, ψ`) & Spinning Tops**:
  * Standard 3-angle sequence describing orientation in space; fast top precession and nutation.
