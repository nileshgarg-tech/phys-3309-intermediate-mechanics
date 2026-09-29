# Chapter 5: Oscillations

Linear oscillations, damping, driven resonance, and Fourier analysis.

---

## Key Topics & Roadmap

* **Simple Harmonic Motion (SHM)**:
  * Differential equation: `d²x/dt² + ω_0² * x = 0`, where `ω_0 = sqrt(k / m)`.
  * General solution: `x(t) = A * cos(ω_0*t - δ) = C_1 * e^(i*ω_0*t) + C_2 * e^(-i*ω_0*t)`.

* **Damped Oscillations (`d²x/dt² + 2*β*dx/dt + ω_0² * x = 0`)**:
  * Damping parameter: `β = b / (2*m)`.
  * **Underdamped** (`β < ω_0`): Oscillates with decaying amplitude at frequency `ω_1 = sqrt(ω_0² - β²)`.
  * **Critically damped** (`β = ω_0`): Fastest return to equilibrium without oscillating (`x(t) = (c_1 + c_2*t)*e^(-β*t)`).
  * **Overdamped** (`β > ω_0`): Sluggish exponential decay without oscillations.

* **Driven Damped Oscillations & Resonance**:
  * Driving force: `F(t) = F_0 * cos(ω*t)`.
  * Steady-state amplitude: `A(ω) = (f_0) / sqrt((ω_0² - ω²)² + 4*β²*ω²)`.
  * Resonance frequency: `ω_res = sqrt(ω_0² - 2*β²)`.
  * Quality factor: `Q = ω_0 / (2*β)`.

* **Fourier Series**:
  * Decomposing arbitrary periodic drive forces `F(t)` into harmonic components to solve the response via superposition.
