# Master Problem Set: Chapters 1–4 (Foundations of Classical Mechanics)

**Course**: UH PHYS 3309 — Intermediate Mechanics  
**Textbook**: *Classical Mechanics* (2005) by John R. Taylor  
**Supplementary References**:
* Richard P. Feynman, *The Feynman Lectures on Physics*, Vol. 1 (Ch. 8–14, 18–20, 22, 41)
* Daniel Kleppner & Robert Kolenkow, *An Introduction to Mechanics* (Ch. 1–6)
* David Morin, *Introduction to Classical Mechanics* (Ch. 1–5)

---

## Overview

This master problem set consolidates the fundamental concepts from **Chapters 1 through 4**. 
Each problem has been chosen to reflect realistic junior-level exam questions at the level of PHYS 3309, challenging your physical intuition and mathematical mastery of:
1. Polar kinematics and moving coordinate bases
2. Viscous (linear) and turbulent (quadratic) drag dynamics
3. Magnetic forces and complex coordinate representations
4. Variable-mass systems (rockets and mass accumulation)
5. Multi-particle momentum and Center of Mass theorems
6. Angular momentum, torque, and planar central-force conservation
7. Work, line integrals, and the curl test for conservative forces
8. 1D potential wells, energy diagrams, and small-oscillation approximations
9. Central-force effective potentials and two-body reduced mass decoupling

Complete, rigorous solutions are provided immediately following each problem.

---

## Problem 1: Polar Kinematics & The Rotating Wire (Chapter 1)

### Problem Statement
A small bead of mass `m` slides frictionlessly along a straight rigid wire rod. The rod is pivoted at the origin and is forced by an external motor to rotate in a horizontal plane with constant angular speed `ω` (`θ(t) = ω*t`). 
At time `t = 0`, the bead is released from rest relative to the rod at distance `r(0) = r_0` with `r_dot(0) = 0`.
1. Using 2D plane polar coordinates, write down Newton's Second Law for both the radial (r_hat) and azimuthal (θ_hat) directions.
2. Solve the radial equation of motion to find the bead's distance from the pivot `r(t)` for all future time.
3. Determine the transverse normal constraint force `N(t) = F_θ(t)` exerted by the rod on the bead as a function of time.

### Detailed Solution
1. **Equations of Motion**:
   In plane polar coordinates, the acceleration vector is:
   ```
   a = [ r_ddot - r*(θ_dot)² ] * r_hat + [ r*θ_ddot + 2*r_dot*θ_dot ] * θ_hat
   ```
   Because the wire rotates at constant angular speed, `θ_dot = ω = const`, so `θ_ddot = 0`.
   The rod is frictionless, meaning it cannot exert any force along its length (`F_r = 0`). The only force on the bead is the transverse normal contact force `N` exerted perpendicular to the wire (`F_θ = N`):
   * Radial equation (`F_r = m * a_r`):
     ```
     0 = m * [ r_ddot - r*ω² ]  ===>  r_ddot - ω²*r = 0
     ```
   * Azimuthal equation (`F_θ = m * a_θ`):
     ```
     N = m * [ 2 * r_dot * ω ]
     ```

2. **Solving the Radial Equation**:
   The ODE `r_ddot - ω²*r = 0` has the general solution:
   ```
   r(t) = A * cosh(ω*t) + B * sinh(ω*t)
   ```
   Apply initial conditions:
   * `r(0) = r_0  ===>  A = r_0`
   * `r_dot(t) = A*ω*sinh(ω*t) + B*ω*cosh(ω*t)`
   * `r_dot(0) = B*ω = 0  ===>  B = 0`
   Therefore:
   ```
   r(t) = r_0 * cosh(ω*t)
   r_dot(t) = r_0 * ω * sinh(ω*t)
   ```

3. **The Normal Constraint Force**:
   Substitute `r_dot(t)` into the azimuthal equation:
   ```
   N(t) = 2 * m * ω * (r_0 * ω * sinh(ω*t)) = 2 * m * r_0 * ω² * sinh(ω*t)
   ```
**Physical Takeaway**: The bead accelerates outward exponentially (`cosh(ω*t) ~ e^(ω*t)/2`). The motor must supply a rapidly growing normal torque `N(t)` to overcome the Coriolis acceleration `2*r_dot*ω` and maintain constant rotation.

---

## Problem 2: Linear Drag & The Range Correction (Chapter 2)

### Problem Statement
A cannon fires a projectile of mass `m` with initial launch speed `v_0` at an angle `θ` above a flat horizontal plain in a medium providing linear air drag `f = -b*v`.
1. Write down the horizontal and vertical positions `x(t)` and `y(t)`.
2. Assuming the drag is weak (`t / τ ≪ 1`, where `τ = m/b`), show via Taylor series expansion that the horizontal range `R` is approximately given by the vacuum range `R_vac` minus a first-order drag penalty:
   ```
   R ≈ R_vac * [ 1 - (4/3) * (v_0 * sin(θ)) / (g * τ) ]
   ```

### Detailed Solution
1. **Equations of Motion**:
   With `v_{x0} = v_0 * cos(θ)` and `v_{y0} = v_0 * sin(θ)`:
   ```
   x(t) = v_{x0} * τ * (1 - e^(-t / τ))
   y(t) = (v_{y0} + v_ter) * τ * (1 - e^(-t / τ)) - v_ter * t
   ```
   where `τ = m / b` and `v_ter = g * τ`.

2. **Perturbation Expansion**:
   In a vacuum, the total flight time is `T_vac = 2 * v_{y0} / g`.
   Let us expand `y(t)` for small `t / τ ≪ 1` using `e^(-t/τ) ≈ 1 - (t/τ) + (t/τ)²/2 - (t/τ)³/6 + ...`:
   ```
   y(t) = (v_{y0} + g*τ) * τ * [ (t/τ) - (t/τ)²/2 + (t/τ)³/6 ] - g*τ*t
   ```
   Multiply out and collect powers of `t`:
   ```
   y(t) ≈ v_{y0}*t - (1/2)*g*t² - (1 / (2*τ)) * v_{y0}*t² + (g / (6*τ)) * t³
   ```
   Set `y(T) = 0` to find the landing time `T = T_vac + ΔT`.
   Dividing by `t`:
   ```
   0 = v_{y0} - (1/2)*g*T - (1 / (2*τ)) * v_{y0}*T + (g / (6*τ)) * T²
   ```
   Substitute `T ≈ T_vac = 2*v_{y0} / g`:
   ```
   (1/2)*g*T ≈ v_{y0} - (1 / (2*τ)) * v_{y0} * (2*v_{y0} / g) + (g / (6*τ)) * (4*v_{y0}² / g²)
             = v_{y0} * [ 1 - (v_{y0} / (g*τ)) + (2/3) * (v_{y0} / (g*τ)) ]
             = v_{y0} * [ 1 - (1/3) * (v_{y0} / (g*τ)) ]
   ```
   Therefore:
   ```
   T ≈ (2 * v_{y0} / g) * [ 1 - (1/3) * (v_{y0} / (g*τ)) ] = T_vac * [ 1 - (1/3) * (v_0 * sin(θ)) / (g * τ) ]
   ```
   Now evaluate horizontal position `x(T)` using `1 - e^(-T/τ) ≈ (T/τ) - (T/τ)²/2`:
   ```
   x(T) ≈ v_{x0} * T * [ 1 - (1/2) * (T / τ) ]
   ```
   Substitute `T ≈ T_vac * [ 1 - (1/3) * (T_vac / (2*τ)) ]`:
   ```
   R ≈ v_{x0} * T_vac * [ 1 - (1/3) * (T_vac / (2*τ)) ] * [ 1 - (1/2) * (T_vac / τ) ]
     ≈ R_vac * [ 1 - (4/3) * (T_vac / (2*τ)) ]
   ```
   Since `T_vac / 2 = v_{y0} / g = (v_0 * sin(θ)) / g`:
   ```
   R ≈ R_vac * [ 1 - (4/3) * (v_0 * sin(θ)) / (g * τ) ]
   ```
**Physical Takeaway**: The first-order effect of air resistance shortens the range by a term directly proportional to the vertical launch velocity divided by the terminal velocity parameter `g*τ`.

---

## Problem 3: Vertical Fall with Quadratic Drag (Chapter 2)

### Problem Statement
A basketball of mass `m = 0.62 kg` and diameter `D = 0.24 m` is dropped from the roof of a tall building.
Taking quadratic drag coefficient `c = (1/2) * C_D * ρ * A ≈ 0.035 N·s²/m²`:
1. Calculate the terminal speed `v_ter` and characteristic time `τ`.
2. Find the exact time `t_{50}` and distance `y_{50}` at which the basketball reaches 50% of its terminal speed.
3. Compare the distance fallen `y_{50}` with the distance a ball would fall in a vacuum in the same time.

### Detailed Solution
1. **Parameters**:
   ```
   v_ter = sqrt( m * g / c ) = sqrt( (0.62 * 9.8) / 0.035 ) = sqrt( 6.076 / 0.035 ) = sqrt(173.6) ≈ 20.8 m/s  (approx 46.5 mph)
   τ = v_ter / g = 20.83 / 9.8 ≈ 2.126 seconds
   ```

2. **Time to Reach 50% Speed**:
   From Module 06: `v(t) = v_ter * tanh(t / τ)`.
   We require `v(t_{50}) = 0.50 * v_ter`:
   ```
   tanh(t_{50} / τ) = 0.50  ===>  t_{50} / τ = arctanh(0.50)
   ```
   Using the identity `arctanh(z) = (1/2) * ln((1 + z)/(1 - z))`:
   ```
   arctanh(0.50) = (1/2) * ln(1.5 / 0.5) = (1/2) * ln(3) ≈ (0.5) * (1.0986) ≈ 0.5493
   t_{50} = 2.126 * 0.5493 ≈ 1.168 seconds
   ```
   Distance fallen:
   ```
   y(t) = (v_ter² / g) * ln(cosh(t / τ))
   v_ter² / g = 173.6 / 9.8 = 17.71 meters
   cosh(0.5493) ≈ 1.1547  ===>  ln(1.1547) ≈ 0.1438
   y_{50} = 17.71 * 0.1438 ≈ 2.55 meters
   ```

3. **Comparison with Vacuum**:
   In a vacuum, after `t = 1.168 s`:
   ```
   y_vac = (1/2) * g * t² = (0.5) * (9.8) * (1.168)² ≈ 6.68 meters
   ```
**Physical Takeaway**: In just 2.5 meters of fall, air resistance has already halved the acceleration and reduced distance by more than 60%!

---

## Problem 4: Relativistic Velocity Selector & Complex Vectors (Chapter 2)

### Problem Statement
A beam of ions of mass `m` and charge `q` enters a region with constant crossed fields `E = E * y_hat` and `B = B * z_hat`.
Show that an ion entering with velocity `v_0 = (E / B) * x_hat` travels undeflected in a straight line, and determine the exact trajectory of an ion that enters with a slightly different velocity `v_0 = (E / B + δv) * x_hat`.

### Detailed Solution
1. **Undeflected Case**:
   Lorentz force: `F = q * (E + v x B)`.
   Compute `v x B`:
   ```
   v x B = ( (E / B) * x_hat ) x ( B * z_hat ) = - E * y_hat
   ```
   Therefore:
   ```
   F = q * [ E * y_hat - E * y_hat ] = 0
   ```
   Because the net force is identically zero, the particle moves in a straight line at constant velocity `(E/B) * x_hat`.

2. **Perturbed Velocity**:
   Let the initial velocity be `v_x(0) = v_d + δv`, `v_y(0) = 0`, where `v_d = E / B`.
   Using the complex velocity variable from Module 07: `u = (v_x - v_d) + i*v_y`.
   The equation of motion is:
   ```
   du / dt = -i * ω * u     (where ω = q*B / m)
   ```
   The solution with initial condition `u(0) = δv + i*(0) = δv` is:
   ```
   u(t) = δv * e^(-i * ω * t) = δv * [ cos(ω*t) - i*sin(ω*t) ]
   ```
   Separating real and imaginary parts:
   ```
   v_x(t) = v_d + δv * cos(ω*t)
   v_y(t) = - δv * sin(ω*t)
   ```
   Integrating with initial position at origin `(0, 0)`:
   ```
   x(t) = v_d * t + (δv / ω) * sin(ω*t)
   y(t) = (δv / ω) * [ cos(ω*t) - 1 ]
   ```
**Physical Takeaway**: Particles with `δv ≠ 0` oscillate harmonically about the straight path with amplitude `r_L = |δv| / ω`. This harmonic confinement is the basis of quadrupole mass filters in modern chemistry.

---

## Problem 5: The Tsiolkovsky Rocket with Gravity (Chapter 3)

### Problem Statement
A Saturn V rocket of initial launch mass `m_0 = 2.8 x 10^6 kg` burns fuel at a constant rate `k = -dm/dt = 1.4 x 10^4 kg/s` for a total burn time `t_b = 150 s`. The engine has an effective exhaust speed `v_ex = 2600 m/s`.
Assuming vertical flight in uniform gravity `g = 9.8 m/s²`:
1. Find the rocket's velocity `v(t_b)` at engine burnout.
2. Find the altitude `y(t_b)` reached at burnout.
3. Calculate the percentage of final speed lost to gravity drag.

### Detailed Solution
1. **Burnout Mass & Velocity**:
   ```
   m_final = m_0 - k * t_b = (2.8 x 10^6) - (1.4 x 10^4 * 150) = (2.8 x 10^6) - (2.1 x 10^6) = 0.70 x 10^6 kg
   m_0 / m_final = (2.8 x 10^6) / (0.70 x 10^6) = 4.0
   ```
   Velocity at burnout:
   ```
   v(t_b) = v_ex * ln(m_0 / m_final) - g * t_b
          = 2600 * ln(4.0) - (9.8 * 150)
          = 2600 * (1.3863) - 1470 = 3604 - 1470 = 2134 m/s  (approx 2.13 km/s)
   ```

2. **Burnout Altitude**:
   Integrate `v(t)` from Module 09:
   ```
   y(t_b) = v_ex * t_b - (1/2)*g*t_b² - (v_ex * m_final / k) * ln(m_0 / m_final)
   ```
   Compute each term:
   * Term 1: `2600 * 150 = 390,000 m`
   * Term 2: `(0.5) * (9.8) * (150)² = 110,250 m`
   * Term 3: `[ (2600 * 0.70 x 10^6) / (1.4 x 10^4) ] * 1.3863 = [ 130,000 ] * 1.3863 ≈ 180,219 m`
   ```
   y(t_b) = 390,000 - 110,250 - 180,219 ≈ 99,531 meters ≈ 99.5 km
   ```
   The rocket reaches the edge of space (the Karman line, 100 km) right as stage 1 burns out!

3. **Gravity Drag Loss**:
   Without gravity, `v_ideal = 3604 m/s`.
   Speed lost to gravity: `1470 m/s`.
   ```
   Percentage lost = (1470 / 3604) * 100% ≈ 40.8%
   ```
**Physical Takeaway**: Over 40% of the first stage's energy was spent fighting gravity. This illustrates why rockets pitch over into a horizontal trajectory as quickly as atmospheric density permits.

---

## Problem 6: Two Interacting Gliders & Center of Mass (Chapter 3)

### Problem Statement
Two carts of masses `m_1 = 1.0 kg` and `m_2 = 3.0 kg` rest on a frictionless horizontal air track. Cart 1 has a compressed massless spring attached to its front bumper with spring constant `k = 300 N/m`.
Cart 1 is launched with initial speed `v_0 = 4.0 m/s` toward stationary cart 2.
1. Find the velocity `V_cm` of the Center of Mass.
2. Find the maximum compression `x_max` of the spring during the collision.
3. Find the final velocities of both carts after the spring completely releases.

### Detailed Solution
1. **Center of Mass Velocity**:
   Total momentum is conserved:
   ```
   P_total = m_1 * v_0 + m_2 * (0) = (1.0) * (4.0) = 4.0 kg·m/s
   V_cm = P_total / (m_1 + m_2) = 4.0 / (1.0 + 3.0) = 1.0 m/s
   ```

2. **Maximum Compression**:
   At maximum compression, both carts move at the exact same velocity `V_cm = 1.0 m/s`.
   Total initial kinetic energy:
   ```
   T_initial = (1/2) * m_1 * v_0² = (0.5) * (1.0) * (4.0)² = 8.0 Joules
   ```
   Kinetic energy of Center of Mass motion:
   ```
   T_cm = (1/2) * (m_1 + m_2) * V_cm² = (0.5) * (4.0) * (1.0)² = 2.0 Joules
   ```
   The remaining energy is internal relative kinetic energy, which converts completely into spring potential energy:
   ```
   (1/2) * k * x_max² = T_initial - T_cm = 8.0 - 2.0 = 6.0 Joules
   (1/2) * (300) * x_max² = 6.0  ===>  150 * x_max² = 6.0
   x_max² = 6.0 / 150 = 0.04  ===>  x_max = 0.20 meters = 20 cm
   ```

3. **Final Velocities**:
   In the Center of Mass frame, the collision is an elastic rebound:
   * Initial relative velocities in CM frame:
     `v'_1_initial = v_0 - V_cm = 4.0 - 1.0 = +3.0 m/s`
     `v'_2_initial = 0 - V_cm = -1.0 m/s`
   * Rebound reverses relative velocities:
     `v'_1_final = -3.0 m/s`
     `v'_2_final = +1.0 m/s`
   * Return to lab frame by adding `V_cm = 1.0 m/s`:
     ```
     v_1_final = v'_1_final + V_cm = -3.0 + 1.0 = - 2.0 m/s  (rebounds backward)
     v_2_final = v'_2_final + V_cm = +1.0 + 1.0 = + 2.0 m/s  (moves forward)
     ```
**Physical Takeaway**: Transforming into the Center of Mass frame reduces a two-body dynamic interaction to simple 1D elastic rebound arithmetic.

---

## Problem 7: Angular Momentum of a Sliding Puck on a String (Chapter 3)

### Problem Statement
A puck of mass `m` on a frictionless horizontal table is attached to a string passing through a hole in the center. The puck orbits in a circle of radius `r_1` with speed `v_1`.
The string is slowly pulled downward through the hole until the radius decreases to `r_2 = r_1 / 3`.
1. Calculate the final speed `v_2`.
2. Compute the work `W` done by the tension force pulling the string, and show that `W = ΔT`.

### Detailed Solution
1. **Conservation of Angular Momentum**:
   The tension force points radially toward the hole, exerting zero torque: `Γ = 0`.
   Therefore, angular momentum is conserved:
   ```
   l = m * r_1 * v_1 = m * r_2 * v_2
   v_2 = v_1 * (r_1 / r_2) = v_1 * (r_1 / (r_1 / 3)) = 3 * v_1
   ```

2. **Work Done & Kinetic Energy**:
   At any radius `r`, the tension force supplies the centripetal acceleration:
   ```
   T(r) = m * (v(r)² / r)
   ```
   Since `v(r) = l / (m*r)`:
   ```
   T(r) = m * [ l² / (m² * r²) ] * (1 / r) = l² / (m * r³)
   ```
   The work done pulling the string inward from `r_1` to `r_2` is:
   ```
   W = - ∫_{r_1}^{r_2} T(r) dr = - ∫_{r_1}^{r_2} (l² / (m*r³)) dr = (l² / (2*m)) * [ 1/r_2² - 1/r_1² ]
   ```
   Notice that `(1/2) * m * v² = l² / (2*m*r²)`!
   Therefore:
   ```
   W = (1/2)*m*v_2² - (1/2)*m*v_1² = ΔT
   ```
   Substitute `v_2 = 3*v_1`:
   ```
   W = (1/2)*m*(9*v_1² - v_1²) = 4 * m * v_1²
   ```
**Physical Takeaway**: The tension force does positive work because the radial displacement is inward toward the center in the direction of the tension. This mechanical work directly quadruples the kinetic energy.

---

## Problem 8: The Multivariable Curl Test & Non-Conservative Loops (Chapter 4)

### Problem Statement
Consider the force field:
```
F(x, y) = (x² + a*y)*x_hat + (2*x + y²)*y_hat
```
1. Determine the value of the constant `a` for which the force field is conservative.
2. For that value of `a`, calculate the potential energy function `U(x, y)` with `U(0, 0) = 0`.
3. If `a = 5`, compute the work done around a closed unit square path `(0,0) -> (1,0) -> (1,1) -> (0,1) -> (0,0)`.

### Detailed Solution
1. **The Curl Condition**:
   In 2D, the curl is:
   ```
   (∇ x F)_z = ∂F_y/∂x - ∂F_x/∂y = ∂(2*x + y²)/∂x - ∂(x² + a*y)/∂y = 2 - a
   ```
   For the force to be conservative, `∇ x F = 0` everywhere:
   ```
   2 - a = 0  ===>  a = 2
   ```

2. **Finding the Potential Energy**:
   With `a = 2`:
   ```
   F = -∇U  ===>  ∂U/∂x = -(x² + 2*y)   and   ∂U/∂y = -(2*x + y²)
   ```
   Integrate `∂U/∂x`:
   ```
   U(x, y) = - (1/3)*x³ - 2*x*y + g(y)
   ```
   Differentiate with respect to `y`:
   ```
   ∂U/∂y = - 2*x + g'(y) = -(2*x + y²)  ===>  g'(y) = - y²  ===>  g(y) = - (1/3)*y³
   ```
   Therefore:
   ```
   U(x, y) = - (1/3)*x³ - 2*x*y - (1/3)*y³
   ```

3. **Loop Integral for `a = 5`**:
   Using Stokes' theorem for the unit square area `S` (`[0, 1] x [0, 1]`):
   ```
   W = ∮ F · dr = ∫_S (∇ x F)_z dA
   ```
   Here `(∇ x F)_z = 2 - 5 = -3`:
   ```
   W = ∫_0^1 ∫_0^1 (-3) dx dy = -3 * (1) * (1) = - 3.0 Joules
   ```
**Physical Takeaway**: Stokes' theorem allows you to compute the closed loop line integral in one line instead of evaluating four separate edge integrals.

---

## Problem 9: The Lennard-Jones Potential & Oscillation Period (Chapter 4)

### Problem Statement
A diatomic molecule is modeled by the Lennard-Jones potential:
```
U(r) = U_0 * [ (r_0 / r)^12 - 2 * (r_0 / r)^6 ]
```
1. Calculate the minimum potential energy `U_min` and the equilibrium radius `r_0`.
2. Expand `U(r)` to quadratic order about `r = r_0` to find the effective spring constant `k_eff`.
3. If the reduced mass of the molecule is `μ = 1.2 x 10^-26 kg`, `U_0 = 1.0 x 10^-20 J`, and `r_0 = 0.35 nm`, find the vibrational frequency in Terahertz (THz).

### Detailed Solution
1. **Equilibrium Point**:
   ```
   dU/dr = (12 * U_0 / r) * [ -(r_0 / r)^12 + (r_0 / r)^6 ] = 0  ===>  r_eq = r_0
   U(r_0) = U_0 * [ 1 - 2 ] = - U_0
   ```

2. **Effective Spring Constant**:
   Compute second derivative:
   ```
   d²U/dr² = (U_0 / r²) * [ 156*(r_0/r)^12 - 84*(r_0/r)^6 ]
   k_eff = d²U/dr² |_{r_0} = 72 * U_0 / r_0²
   ```

3. **Numerical Frequency**:
   ```
   k_eff = 72 * (1.0 x 10^-20) / (0.35 x 10^-9)² = (7.2 x 10^-19) / (1.225 x 10^-19) ≈ 5.878 N/m
   ω_0 = sqrt( k_eff / μ ) = sqrt( 5.878 / (1.2 x 10^-26) ) = sqrt( 4.898 x 10^26 ) ≈ 2.213 x 10^13 rad/s
   f = ω_0 / (2*π) ≈ (2.213 x 10^13) / 6.283 ≈ 3.52 x 10^12 Hz = 3.52 THz
   ```
**Physical Takeaway**: The simple 1D Taylor expansion accurately predicts molecular infrared absorption peaks.

---

## Problem 10: Central Force Effective Potential & Orbital Stability (Chapter 4)

### Problem Statement
A particle of mass `m` moves under the influence of an attractive central force:
```
F(r) = - (k / r^n) * r_hat    (where k > 0 and n is an arbitrary power)
```
1. Find the potential energy function `U(r)`.
2. Write down the effective potential `U_eff(r)` for a particle with angular momentum `l`.
3. Find the radius `r_0` of a circular orbit.
4. Prove that a stable circular orbit can exist **only if `n < 3`** (Bertrand's Theorem criterion).

### Detailed Solution
1. **Potential Energy**:
   ```
   U(r) = - ∫ F(r) dr = - ∫ (-k / r^n) dr = - k / ((n - 1) * r^(n-1))    (for n ≠ 1)
   ```

2. **Effective Potential**:
   ```
   U_eff(r) = - k / ((n - 1) * r^(n-1)) + l² / (2 * m * r²)
   ```

3. **Circular Orbit Radius**:
   Set `dU_eff/dr = 0`:
   ```
   dU_eff/dr = - k / r^n + l² / (m * r³) = 0  ===>  k / r^n = l² / (m * r³)
   k * r_0^(3 - n) = l² / m  ===>  r_0 = [ l² / (m * k) ]^(1 / (3 - n))
   ```

4. **Stability Condition**:
   For stability, the second derivative must be strictly positive at `r = r_0`:
   ```
   d²U_eff/dr² = n * k / r^(n+1) - 3 * l² / (m * r⁴)
   ```
   Substitute `l² / m = k * r_0^(3 - n)`:
   ```
   d²U_eff/dr² |_{r_0} = n * k / r_0^(n+1) - 3 * [ k * r_0^(3 - n) ] / r_0⁴
                       = n * k / r_0^(n+1) - 3 * k / r_0^(n+1)
                       = (n - 3) * (k / r_0^(n+1))
   ```
   For `d²U_eff/dr² > 0`, we require:
   ```
   (n - 3) < 0  ===>  n < 3
   ```
**Physical Takeaway**: In any universe where gravitational forces fall off faster than `1/r³` (such as `1/r⁴`), **planetary orbits are fundamentally unstable!** A tiny meteorite impact would cause the Earth to either spiral into the Sun or fly off into dark space. Stable solar systems are mathematically possible only because gravity is an inverse-square force (xyn = 2n < 3).
