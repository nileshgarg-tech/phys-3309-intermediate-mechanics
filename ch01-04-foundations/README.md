# Chapters 1–4: Foundations & Thematic Story Series

This directory compresses the 160 pages of Chapters 1 to 4 into **15 pedagogical story modules**.
Each module connects physical intuition (inspired by Richard Feynman's *Lectures on Physics*) with full step-by-step mathematical rigor, without unrendered LaTeX artifacts.

---

## Comprehensive Master Problem Set

* **[Master Problem Set: Chapters 1–4](PROBLEM_SET.md)** — 10 high-yield, exam-caliber practice problems spanning the entire foundations curriculum.
* **[Master Problem Set Solutions](PROBLEM_SET_SOLUTIONS.md)** — Complete step-by-step analytical derivations, calculations, and Feynman-inspired physical takeaways for all 10 problems.

---

## The 15-Module Story Roadmap

### Part I: Space, Time & Newton's Laws (Chapter 1)
1. [01. Space, Time, and Inertial Reference Frames](01_space_time_and_inertial_frames.md)
   *What is space and time? Operational definition of inertia, Galileo's relativity, Newton's 1st law, inertial vs. non-inertial frames.*
2. [02. Force, Mass, and Newton's Second & Third Laws](02_force_mass_and_newtons_second_law.md)
   *The operational definition of mass via collision ratios, momentum, 2nd-order ODEs, Newton's 3rd law, and conservation of linear momentum.*
3. [03. Curvilinear Kinematics & 2D Polar Coordinates](03_curvilinear_kinematics_and_polar_coordinates.md)
   *Kinematics beyond Cartesian: moving unit vectors, step-by-step velocity and acceleration derivatives in 2D polar coordinates, centripetal and Coriolis terms.*

---

### Part II: The Real World — Drag Forces & Fields (Chapter 2)
4. [04. Air Resistance: Linear vs. Quadratic Drag](04_air_resistance_linear_vs_quadratic.md)
   *Microscopic origins of drag: viscous skin friction (Stokes' linear drag) vs. turbulent pressure wake (quadratic drag), Reynolds number criterion.*
5. [05. Linear Air Drag: Exact Trajectories & Characteristic Time](05_linear_drag_trajectories_and_characteristic_time.md)
   *Analytical solutions for linear drag: characteristic time `τ = m/b`, terminal speed `v_ter`, 2D trajectory equation, and perturbation expansion to vacuum.*
6. [06. Quadratic Drag & Nonlinear Trajectories](06_quadratic_drag_and_nonlinear_trajectories.md)
   *Coupling of x and y in 2D drag; exact hyperbolic solutions (`tanh`, `cosh`) for 1D vertical drops, and upward projectile peaks.*
7. [07. Charged Particles in B Fields & Complex Exponentials](07_charges_in_magnetic_fields_and_complex_numbers.md)
   *Lorentz force, cyclotron frequency `ω = q*B/m`, Larmor radius, and solving 2D vector ODEs via complex exponentials (`η = v_x + i*v_y`).*

---

### Part III: Many Bodies, Rockets & Rotation (Chapter 3)
8. [08. Conservation of Momentum & Center of Mass](08_conservation_of_momentum_and_center_of_mass.md)
   *Internal vs. external forces, pairwise Newton's 3rd law cancellation, definition and theorem of the Center of Mass (CM).*
9. [09. Variable-Mass Systems & The Rocket Equation](09_variable_mass_systems_and_rocket_propulsion.md)
   *Why `F = d(mv)/dt` fails for open systems; first-principles derivation of the Tsiolkovsky Rocket Equation, mass ratio trap, and multistage staging.*
10. [10. Angular Momentum: Single & Multiparticle Systems](10_angular_momentum_single_and_many_particles.md)
   *Torque as moment of force, central force conservation (Kepler's 2nd law), and the fundamental decomposition into orbital and spin angular momentum.*

---

### Part IV: Energy, Potentials & Conservative Fields (Chapter 4)
11. [11. Work, Kinetic Energy & The Work-Energy Theorem](11_work_kinetic_energy_and_line_integrals.md)
   *Work as a line integral `W = ∫ F · dr`, rigorous 3D derivation of the Work-Kinetic Energy Theorem, and instantaneous power.*
12. [12. Potential Energy & Conservative Forces](12_potential_energy_and_conservative_forces.md)
   *Definition of conservative force, potential energy `U(r)`, force as steepest descent `F = -∇U`, and the curl test `∇ x F = 0` via Stokes' theorem.*
13. [13. One-Dimensional Systems & Potential Wells](13_one_dimensional_systems_and_potential_wells.md)
   *Reading energy diagrams `U(x)`, turning points, equilibrium stability (`d²U/dx²`), universal harmonic approximation, and the 1D time integral.*
14. [14. Curvilinear 1D Systems & Central Forces](14_curvilinear_motion_and_central_forces.md)
   *Constraint forces doing zero work (`N · dr = 0`), polar kinetic energy, angular momentum elimination, and the effective potential `U_eff(r)`.*
15. [15. Multiparticle Energy, Internal Potentials & Thermodynamics](15_multiparticle_energy_and_internal_potentials.md)
   *Two-body kinetic energy decoupling (CM + reduced mass `μ`), pairwise internal potentials, rigid body simplification, and the bridge to thermodynamics.*

---

## Primary & Supplementary References

1. **John R. Taylor**, *Classical Mechanics* (University Science Books, 2005) — Chapters 1–4.
2. **Richard P. Feynman, Robert B. Leighton, Matthew Sands**, *The Feynman Lectures on Physics*, Vol. 1:
   * **Chapters 8–10**: Description of motion, Newton's dynamical laws, and momentum conservation.
   * **Chapter 11**: Vectors and polar coordinates.
   * **Chapters 13–14**: Work, potential energy, conservative fields, and work-energy theorem.
   * **Chapters 18–20**: Center of mass, rotation, and angular momentum.
   * **Chapter 22**: Algebra, complex numbers, and simple harmonic oscillations.
   * **Chapter 41**: Fluid resistance, viscosity, and Stokes' drag.
3. **Daniel Kleppner & Robert Kolenkow**, *An Introduction to Mechanics* (Cambridge University Press) — Chapters 1–6.
4. **David Morin**, *Introduction to Classical Mechanics: With Problems and Solutions* (Cambridge University Press) — Chapters 1–5.
5. **L.D. Landau & E.M. Lifshitz**, *Mechanics (Course of Theoretical Physics, Vol. 1)* — Chapters 1–2.
