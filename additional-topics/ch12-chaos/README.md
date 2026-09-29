# Chapter 12: Nonlinear Mechanics & Chaos

Linearity vs. nonlinearity, the driven damped pendulum, bifurcations, state space, and deterministic chaos.

---

## Key Topics & Roadmap

* **Linearity vs. Nonlinearity**:
  * In linear systems, the principle of superposition holds (`x_total = x_1 + x_2`).
  * In nonlinear systems (like the true pendulum where `sin(φ) ≠ φ`), superposition fails, enabling frequency mixing, harmonics, and chaotic dynamics.

* **The Driven Damped Pendulum (DDP)**:
  * Differential equation:
    * `d²φ/dt² + 2*β*dφ/dt + ω_0²*sin(φ) = γ * ω_0² * cos(ω*t)`
  * Drive strength parameter: `γ = F_0 / (m * g)`.
  * As `γ` increases from small to moderate values, motion transitions from simple periodic oscillation to period-doubling, and finally to chaos.

* **Route to Chaos & Period Doubling**:
  * **Period-Doubling Cascade**: The period of the stable orbit doubles from `T → 2T → 4T → 8T → ...` at critical values of `γ_n`.
  * **Feigenbaum Constant**: The ratio of successive bifurcation intervals approaches a universal constant:
    * `δ = lim (γ_n - γ_{n-1}) / (γ_{n+1} - γ_n) ≈ 4.6692...`

* **State Space & Poincaré Sections**:
  * State space coordinates: position and angular velocity `(φ, ω)`.
  * **Poincaré Section**: Sampling the state space stroboscopically once every drive period `τ = 2*π / ω`. Periodic orbits appear as a finite number of points, while chaotic orbits form fractal "strange attractors".

* **Sensitivity to Initial Conditions & Lyapunov Exponents**:
  * Two trajectories starting with infinitesimal initial separation `|Δφ_0|` diverge exponentially:
    * `|Δφ(t)| ~ |Δφ_0| * e^(λ*t)`
  * A positive **Lyapunov exponent** (`λ > 0`) is the mathematical hallmark of deterministic chaos.

* **The Logistic Map**:
  * Simple 1D model displaying the exact same universal period-doubling route to chaos:
    * `x_{n+1} = r * x_n * (1 - x_n)`
