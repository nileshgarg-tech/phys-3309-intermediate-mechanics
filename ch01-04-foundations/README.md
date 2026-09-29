# Chapters 1–4: Foundations & Review

Quick review of introductory mechanics foundations. Use this folder to drop summary sheets, refresher notes, or early problem sets.

---

## Key Concepts & Rapid Review

### Chapter 1: Newton's Laws & Vector Kinematics
* **Inertial Reference Frames**: Frames where Newton's 1st law holds without fictitious forces.
* **Newton's 2nd Law in 2D Polar Coordinates**:
  * Position: `r = r * r_hat`
  * Velocity: `v = dr/dt * r_hat + r * dθ/dt * θ_hat`
  * Acceleration: `a = (d²r/dt² - r*(dθ/dt)²) * r_hat + (r*d²θ/dt² + 2*(dr/dt)*(dθ/dt)) * θ_hat`

### Chapter 2: Drag Forces & Magnetic Deflection
* **Linear Air Drag (`f_lin = -b*v`)**: Significant at low Reynolds numbers (tiny droplets, viscous fluids). Characteristic time: `τ = m/b`.
* **Quadratic Air Drag (`f_quad = -c*v*|v|`)**: Dominates macroscopic objects at typical speeds. Terminal speed: `v_ter = sqrt(m*g / c)`.
* **Charged Particles in Magnetic Fields**: Cyclotron frequency `ω = q*B / m`.

### Chapter 3: Momentum, Rockets & Center of Mass
* **Center of Mass**: `R_cm = (1/M) * Σ (m_i * r_i)`.
* **Rocket Equation (Variable Mass)**: `m * dv/dt = -v_ex * dm/dt + F_ext`. Velocity gain: `v - v_0 = v_ex * ln(m_0 / m)`.
* **Angular Momentum**: For a single particle `l = r x p`. For a system, `L = L_orbital(CM) + L_spin(about CM)`.

### Chapter 4: Energy & 1D Potential Wells
* **Work-Energy Theorem**: `ΔT = W_net`.
* **Conservative Forces**: `F = -∇U` (equivalent to `∇ x F = 0` in simply-connected domains).
* **1D Potential Graphs**: Turning points occur where `E = U(x)`. Equilibrium points occur where `dU/dx = 0` (stable if `d²U/dx² > 0`).
