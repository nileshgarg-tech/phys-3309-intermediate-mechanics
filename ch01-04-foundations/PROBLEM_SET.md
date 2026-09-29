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
A small bead of mass $m$ slides frictionlessly along a straight rigid wire rod. The rod is pivoted at the origin and is forced by an external motor to rotate in a horizontal plane with constant angular speed $\omega$ ($\theta(t) = \omega t$).  
At time $t = 0$, the bead is released from rest relative to the rod at distance $r(0) = r_0$ with $\dot{r}(0) = 0$.
1. Using 2D plane polar coordinates, write down Newton's Second Law for both the radial ($\hat{\mathbf{r}}$) and azimuthal ($\hat{\boldsymbol{\theta}}$) directions.
2. Solve the radial equation of motion to find the bead's distance from the pivot $r(t)$ for all future time.
3. Determine the transverse normal constraint force $N(t) = F_\theta(t)$ exerted by the rod on the bead as a function of time.

### Detailed Solution
1. **Equations of Motion**:  
   In plane polar coordinates, the acceleration vector is:

   $$
   \mathbf{a} = (\ddot{r} - r\dot{\theta}^2)\,\hat{\mathbf{r}} + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\,\hat{\boldsymbol{\theta}}
   $$

   Because the wire rotates at constant angular speed, $\dot{\theta} = \omega = \text{const}$, so $\ddot{\theta} = 0$.  
   The rod is frictionless, meaning it cannot exert any force along its length ($F_r = 0$). The only force on the bead is the transverse normal contact force $N$ exerted perpendicular to the wire ($F_\theta = N$):
   * Radial equation ($F_r = m a_r$):

     $$
     0 = m(\ddot{r} - r\omega^2) \implies \ddot{r} - \omega^2 r = 0
     $$

   * Azimuthal equation ($F_\theta = m a_\theta$):

     $$
     N = m (2\dot{r}\omega)
     $$

2. **Solving the Radial Equation**:  
   The ODE $\ddot{r} - \omega^2 r = 0$ has the general solution:

   $$
   r(t) = A\cosh(\omega t) + B\sinh(\omega t)
   $$

   Apply initial conditions:
   * $r(0) = r_0 \implies A = r_0$
   * $\dot{r}(t) = A\omega\sinh(\omega t) + B\omega\cosh(\omega t)$
   * $\dot{r}(0) = B\omega = 0 \implies B = 0$

   Therefore:

   $$
   r(t) = r_0\cosh(\omega t)
   $$

   $$
   \dot{r}(t) = r_0 \omega\sinh(\omega t)
   $$

3. **The Normal Constraint Force**:  
   Substitute $\dot{r}(t)$ into the azimuthal equation:

   $$
   N(t) = 2m\omega (r_0\omega\sinh(\omega t)) = 2m r_0 \omega^2 \sinh(\omega t)
   $$

**Physical Takeaway**: The bead accelerates outward exponentially ($\cosh(\omega t) \sim e^{\omega t}/2$). The motor must supply a rapidly growing normal torque $N(t)$ to overcome the Coriolis acceleration $2\dot{r}\omega$ and maintain constant rotation.

---

## Problem 2: Linear Drag & The Range Correction (Chapter 2)

### Problem Statement
A cannon fires a projectile of mass $m$ with initial launch speed $v_0$ at an angle $\theta$ above a flat horizontal plain in a medium providing linear air drag $\mathbf{f} = -b\mathbf{v}$.
1. Write down the horizontal and vertical positions $x(t)$ and $y(t)$.
2. Assuming the drag is weak ($t / \tau \ll 1$, where $\tau = m/b$), show via Taylor series expansion that the horizontal range $R$ is approximately given by the vacuum range $R_{\text{vac}}$ minus a first-order drag penalty:

   $$
   R \approx R_{\text{vac}} \left[ 1 - \frac{4}{3} \frac{v_0 \sin\theta}{g\tau} \right]
   $$

### Detailed Solution
1. **Equations of Motion**:  
   With $v_{x0} = v_0 \cos\theta$ and $v_{y0} = v_0 \sin\theta$:

   $$
   x(t) = v_{x0} \tau (1 - e^{-t / \tau})
   $$

   $$
   y(t) = (v_{y0} + v_{\text{ter}}) \tau (1 - e^{-t / \tau}) - v_{\text{ter}} t
   $$

   where $\tau = \frac{m}{b}$ and $v_{\text{ter}} = g\tau$.

2. **Perturbation Expansion**:  
   In a vacuum, the total flight time is $T_{\text{vac}} = \frac{2 v_{y0}}{g}$.  
   Let us expand $y(t)$ for small $t / \tau \ll 1$ using $e^{-t/\tau} \approx 1 - \frac{t}{\tau} + \frac{1}{2}\left(\frac{t}{\tau}\right)^2 - \frac{1}{6}\left(\frac{t}{\tau}\right)^3$:

   $$
   y(t) = (v_{y0} + g\tau) \tau \left[ \frac{t}{\tau} - \frac{1}{2}\left(\frac{t}{\tau}\right)^2 + \frac{1}{6}\left(\frac{t}{\tau}\right)^3 \right] - g\tau t
   $$

   Multiply out and collect powers of $t$:

   $$
   y(t) \approx v_{y0} t - \frac{1}{2} g t^2 - \frac{1}{2\tau} v_{y0} t^2 + \frac{g}{6\tau} t^3
   $$

   Set $y(T) = 0$ to find the landing time $T$. Dividing by $T$:

   $$
   0 = v_{y0} - \frac{1}{2} g T - \frac{1}{2\tau} v_{y0} T + \frac{g}{6\tau} T^2
   $$

   Substitute the zeroth-order landing time $T \approx T_{\text{vac}} = \frac{2 v_{y0}}{g}$ into the small perturbation terms:

   $$
   \frac{1}{2} g T \approx v_{y0} - \frac{v_{y0}^2}{g\tau} + \frac{2}{3} \frac{v_{y0}^2}{g\tau} = v_{y0} \left[ 1 - \frac{1}{3} \frac{v_{y0}}{g\tau} \right]
   $$

   Therefore:

   $$
   T \approx \frac{2v_{y0}}{g} \left[ 1 - \frac{1}{3} \frac{v_{y0}}{g\tau} \right] = T_{\text{vac}} \left[ 1 - \frac{1}{3} \frac{v_0 \sin\theta}{g\tau} \right]
   $$

   Now evaluate horizontal position $x(T)$ using $1 - e^{-T/\tau} \approx \frac{T}{\tau} - \frac{1}{2}\left(\frac{T}{\tau}\right)^2$:

   $$
   x(T) \approx v_{x0} T \left[ 1 - \frac{1}{2} \frac{T}{\tau} \right]
   $$

   Substitute $T \approx T_{\text{vac}} [1 - \frac{1}{3} \frac{T_{\text{vac}}}{2\tau}]$:

   $$
   R \approx v_{x0} T_{\text{vac}} \left[ 1 - \frac{1}{3}\frac{T_{\text{vac}}}{2\tau} \right] \left[ 1 - \frac{1}{2}\frac{T_{\text{vac}}}{\tau} \right] \approx R_{\text{vac}} \left[ 1 - \frac{4}{3}\frac{T_{\text{vac}}}{2\tau} \right]
   $$

   Since $\frac{T_{\text{vac}}}{2} = \frac{v_{y0}}{g} = \frac{v_0 \sin\theta}{g}$:

   $$
   R \approx R_{\text{vac}} \left[ 1 - \frac{4}{3} \frac{v_0 \sin\theta}{g\tau} \right]
   $$

**Physical Takeaway**: The first-order effect of air resistance shortens the range by a term directly proportional to the vertical launch velocity divided by the terminal velocity parameter $g\tau$.

---

## Problem 3: Vertical Fall with Quadratic Drag (Chapter 2)

### Problem Statement
A basketball of mass $m = 0.62\text{ kg}$ and diameter $D = 0.24\text{ m}$ is dropped from the roof of a tall building.  
Taking quadratic drag coefficient $c = \frac{1}{2} C_D \rho A \approx 0.035\text{ N}\cdot\text{s}^2\text{/m}^2$:
1. Calculate the terminal speed $v_{\text{ter}}$ and characteristic time $\tau$.
2. Find the exact time $t_{50}$ and distance $y_{50}$ at which the basketball reaches $50\%$ of its terminal speed.
3. Compare the distance fallen $y_{50}$ with the distance a ball would fall in a vacuum in the same time.

### Detailed Solution
1. **Parameters**:

   $$
   v_{\text{ter}} = \sqrt{\frac{mg}{c}} = \sqrt{\frac{0.62 \times 9.8}{0.035}} = \sqrt{173.6} \approx 20.8\text{ m/s} \quad (\approx 46.5\text{ mph})
   $$

   $$
   \tau = \frac{v_{\text{ter}}}{g} = \frac{20.83}{9.8} \approx 2.126\text{ seconds}
   $$

2. **Time to Reach 50% Speed**:  
   From Module 06: $v(t) = v_{\text{ter}} \tanh(t / \tau)$.  
   We require $v(t_{50}) = 0.50\,v_{\text{ter}}$:

   $$
   \tanh\left(\frac{t_{50}}{\tau}\right) = 0.50 \implies \frac{t_{50}}{\tau} = \operatorname{arctanh}(0.50)
   $$

   Using $\operatorname{arctanh}(z) = \frac{1}{2}\ln\left(\frac{1+z}{1-z}\right)$:

   $$
   \operatorname{arctanh}(0.50) = \frac{1}{2}\ln(3) \approx 0.5493
   $$

   $$
   t_{50} = 2.126 \times 0.5493 \approx 1.168\text{ seconds}
   $$

   Distance fallen:

   $$
   y(t) = \frac{v_{\text{ter}}^2}{g} \ln\left(\cosh\left(\frac{t}{\tau}\right)\right)
   $$

   $$
   \frac{v_{\text{ter}}^2}{g} = 17.71\text{ m}, \quad \cosh(0.5493) \approx 1.1547 \implies \ln(1.1547) \approx 0.1438
   $$

   $$
   y_{50} = 17.71 \times 0.1438 \approx 2.55\text{ meters}
   $$

3. **Comparison with Vacuum**:  
   In a vacuum, after $t = 1.168\text{ s}$:

   $$
   y_{\text{vac}} = \frac{1}{2} g t^2 = (0.5)(9.8)(1.168)^2 \approx 6.68\text{ meters}
   $$

**Physical Takeaway**: In just 2.5 meters of fall, air resistance has already halved the acceleration and reduced distance by more than $60\%$!

---

## Problem 4: Relativistic Velocity Selector & Complex Vectors (Chapter 2)

### Problem Statement
A beam of ions of mass $m$ and charge $q$ enters a region with constant crossed fields $\mathbf{E} = E\,\hat{\mathbf{y}}$ and $\mathbf{B} = B\,\hat{\mathbf{z}}$.  
Show that an ion entering with velocity $\mathbf{v}_0 = \left(\frac{E}{B}\right)\hat{\mathbf{x}}$ travels undeflected in a straight line, and determine the exact trajectory of an ion that enters with a slightly different velocity $\mathbf{v}_0 = \left(\frac{E}{B} + \delta v\right)\hat{\mathbf{x}}$.

### Detailed Solution
1. **Undeflected Case**:  
   Lorentz force: $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$.  
   Compute $\mathbf{v} \times \mathbf{B}$:

   $$
   \mathbf{v} \times \mathbf{B} = \left( \frac{E}{B}\,\hat{\mathbf{x}} \right) \times (B\,\hat{\mathbf{z}}) = -E\,\hat{\mathbf{y}}
   $$

   Therefore:

   $$
   \mathbf{F} = q [ E\,\hat{\mathbf{y}} - E\,\hat{\mathbf{y}} ] = \mathbf{0}
   $$

   Because the net force is identically zero, the particle moves in a straight line at constant velocity $\frac{E}{B}\,\hat{\mathbf{x}}$.

2. **Perturbed Velocity**:  
   Let the initial velocity be $v_x(0) = v_d + \delta v$, $v_y(0) = 0$, where $v_d = \frac{E}{B}$.  
   Using the complex velocity variable from Module 07: $u = (v_x - v_d) + i v_y$.  
   The equation of motion is:

   $$
   \frac{du}{dt} = -i \omega u \quad \left(\text{where } \omega = \frac{qB}{m}\right)
   $$

   The solution with initial condition $u(0) = \delta v$ is:

   $$
   u(t) = \delta v \, e^{-i \omega t} = \delta v [\cos(\omega t) - i\sin(\omega t)]
   $$

   Separating real and imaginary parts:

   $$
   v_x(t) = v_d + \delta v \cos(\omega t)
   $$

   $$
   v_y(t) = -\delta v \sin(\omega t)
   $$

   Integrating with initial position at origin $(0, 0)$:

   $$
   x(t) = v_d t + \left(\frac{\delta v}{\omega}\right) \sin(\omega t)
   $$

   $$
   y(t) = \left(\frac{\delta v}{\omega}\right) [\cos(\omega t) - 1]
   $$

**Physical Takeaway**: Particles with $\delta v \neq 0$ oscillate harmonically about the straight path with amplitude $r_L = |\delta v| / \omega$. This harmonic confinement is the basis of quadrupole mass filters in modern chemistry.

---

## Problem 5: The Tsiolkovsky Rocket with Gravity (Chapter 3)

### Problem Statement
A Saturn V rocket of initial launch mass $m_0 = 2.8 \times 10^6\text{ kg}$ burns fuel at a constant rate $k = -\frac{dm}{dt} = 1.4 \times 10^4\text{ kg/s}$ for a total burn time $t_b = 150\text{ s}$. The engine has an effective exhaust speed $v_{\text{ex}} = 2600\text{ m/s}$.  
Assuming vertical flight in uniform gravity $g = 9.8\text{ m/s}^2$:
1. Find the rocket's velocity $v(t_b)$ at engine burnout.
2. Find the altitude $y(t_b)$ reached at burnout.
3. Calculate the percentage of final speed lost to gravity drag.

### Detailed Solution
1. **Burnout Mass & Velocity**:

   $$
   m_{\text{final}} = m_0 - k t_b = (2.8 \times 10^6) - (1.4 \times 10^4 \times 150) = 0.70 \times 10^6\text{ kg}
   $$

   $$
   \frac{m_0}{m_{\text{final}}} = \frac{2.8 \times 10^6}{0.70 \times 10^6} = 4.0
   $$

   Velocity at burnout:

   $$
   v(t_b) = v_{\text{ex}} \ln\left(\frac{m_0}{m_{\text{final}}}\right) - g t_b = 2600 \ln(4.0) - (9.8 \times 150) = 3604 - 1470 = 2134\text{ m/s} \quad (\approx 2.13\text{ km/s})
   $$

2. **Burnout Altitude**:  
   Integrate $v(t)$ from Module 09:

   $$
   y(t_b) = v_{\text{ex}} t_b - \frac{1}{2} g t_b^2 - \frac{v_{\text{ex}} m_{\text{final}}}{k} \ln\left(\frac{m_0}{m_{\text{final}}}\right)
   $$

   Compute each term:
   * Term 1: $2600 \times 150 = 390,000\text{ m}$
   * Term 2: $(0.5)(9.8)(150)^2 = 110,250\text{ m}$
   * Term 3: $\left[ \frac{2600 \times 0.70 \times 10^6}{1.4 \times 10^4} \right] \times 1.3863 = 130,000 \times 1.3863 \approx 180,219\text{ m}$

   $$
   y(t_b) = 390,000 - 110,250 - 180,219 \approx 99,531\text{ meters} \approx 99.5\text{ km}
   $$

   The rocket reaches the edge of space (the Kármán line, 100 km) right as stage 1 burns out!

3. **Gravity Drag Loss**:  
   Without gravity, $v_{\text{ideal}} = 3604\text{ m/s}$. Speed lost to gravity: $1470\text{ m/s}$.

   $$
   \text{Percentage lost} = \left(\frac{1470}{3604}\right) \times 100\% \approx 40.8\%
   $$

**Physical Takeaway**: Over $40\%$ of the first stage's energy was spent fighting gravity. This illustrates why rockets pitch over into a horizontal trajectory as quickly as atmospheric density permits.

---

## Problem 6: Two Interacting Gliders & Center of Mass (Chapter 3)

### Problem Statement
Two carts of masses $m_1 = 1.0\text{ kg}$ and $m_2 = 3.0\text{ kg}$ rest on a frictionless horizontal air track. Cart 1 has a compressed massless spring attached to its front bumper with spring constant $k = 300\text{ N/m}$.  
Cart 1 is launched with initial speed $v_0 = 4.0\text{ m/s}$ toward stationary cart 2.
1. Find the velocity $V_{\text{cm}}$ of the Center of Mass.
2. Find the maximum compression $x_{\text{max}}$ of the spring during the collision.
3. Find the final velocities of both carts after the spring completely releases.

### Detailed Solution
1. **Center of Mass Velocity**:  
   Total momentum is conserved:

   $$
   P_{\text{total}} = m_1 v_0 + m_2 (0) = (1.0)(4.0) = 4.0\text{ kg}\cdot\text{m/s}
   $$

   $$
   V_{\text{cm}} = \frac{P_{\text{total}}}{m_1 + m_2} = \frac{4.0}{1.0 + 3.0} = 1.0\text{ m/s}
   $$

2. **Maximum Compression**:  
   At maximum compression, both carts move at the exact same velocity $V_{\text{cm}} = 1.0\text{ m/s}$.  
   Total initial kinetic energy:

   $$
   T_{\text{initial}} = \frac{1}{2} m_1 v_0^2 = (0.5)(1.0)(4.0)^2 = 8.0\text{ Joules}
   $$

   Kinetic energy of Center of Mass motion:

   $$
   T_{\text{cm}} = \frac{1}{2} (m_1 + m_2) V_{\text{cm}}^2 = (0.5)(4.0)(1.0)^2 = 2.0\text{ Joules}
   $$

   The remaining energy is internal relative kinetic energy, which converts completely into spring potential energy:

   $$
   \frac{1}{2} k x_{\text{max}}^2 = T_{\text{initial}} - T_{\text{cm}} = 8.0 - 2.0 = 6.0\text{ Joules}
   $$

   $$
   150 x_{\text{max}}^2 = 6.0 \implies x_{\text{max}}^2 = 0.04 \implies x_{\text{max}} = 0.20\text{ meters} = 20\text{ cm}
   $$

3. **Final Velocities**:  
   In the Center of Mass frame, the collision is an elastic rebound:
   * Initial relative velocities in CM frame:  
     $v'_{1,\text{initial}} = v_0 - V_{\text{cm}} = 4.0 - 1.0 = +3.0\text{ m/s}$  
     $v'_{2,\text{initial}} = 0 - V_{\text{cm}} = -1.0\text{ m/s}$
   * Rebound reverses relative velocities:  
     $v'_{1,\text{final}} = -3.0\text{ m/s}$  
     $v'_{2,\text{final}} = +1.0\text{ m/s}$
   * Return to lab frame by adding $V_{\text{cm}} = 1.0\text{ m/s}$:

     $$
     v_{1,\text{final}} = v'_{1,\text{final}} + V_{\text{cm}} = -3.0 + 1.0 = -2.0\text{ m/s} \quad \text{(rebounds backward)}
     $$

     $$
     v_{2,\text{final}} = v'_{2,\text{final}} + V_{\text{cm}} = +1.0 + 1.0 = +2.0\text{ m/s} \quad \text{(moves forward)}
     $$

**Physical Takeaway**: Transforming into the Center of Mass frame reduces a two-body dynamic interaction to simple 1D elastic rebound arithmetic.

---

## Problem 7: Angular Momentum of a Sliding Puck on a String (Chapter 3)

### Problem Statement
A puck of mass $m$ on a frictionless horizontal table is attached to a string passing through a hole in the center. The puck orbits in a circle of radius $r_1$ with speed $v_1$.  
The string is slowly pulled downward through the hole until the radius decreases to $r_2 = r_1 / 3$.
1. Calculate the final speed $v_2$.
2. Compute the work $W$ done by the tension force pulling the string, and show that $W = \Delta T$.

### Detailed Solution
1. **Conservation of Angular Momentum**:  
   The tension force points radially toward the hole, exerting zero torque: $\mathbf{\Gamma} = \mathbf{0}$.  
   Therefore, angular momentum is conserved:

   $$
   l = m r_1 v_1 = m r_2 v_2
   $$

   $$
   v_2 = v_1 \left(\frac{r_1}{r_2}\right) = v_1 \left(\frac{r_1}{r_1 / 3}\right) = 3 v_1
   $$

2. **Work Done & Kinetic Energy**:  
   At any radius $r$, the tension force supplies the centripetal acceleration:

   $$
   T(r) = m \frac{v(r)^2}{r}
   $$

   Since $v(r) = \frac{l}{mr}$:

   $$
   T(r) = m \left( \frac{l^2}{m^2 r^2} \right) \frac{1}{r} = \frac{l^2}{m r^3}
   $$

   The work done pulling the string inward from $r_1$ to $r_2$ is:

   $$
   W = - \int_{r_1}^{r_2} T(r)\,dr = - \int_{r_1}^{r_2} \frac{l^2}{m r^3}\,dr = \frac{l^2}{2m} \left[ \frac{1}{r_2^2} - \frac{1}{r_1^2} \right]
   $$

   Notice that $\frac{1}{2} m v^2 = \frac{l^2}{2mr^2}$! Therefore:

   $$
   W = \frac{1}{2} m v_2^2 - \frac{1}{2} m v_1^2 = \Delta T
   $$

   Substitute $v_2 = 3 v_1$:

   $$
   W = \frac{1}{2} m (9 v_1^2 - v_1^2) = 4 m v_1^2
   $$

**Physical Takeaway**: The tension force does positive work because the radial displacement is inward toward the center in the direction of the tension. This mechanical work directly quadruples the kinetic energy.

---

## Problem 8: The Multivariable Curl Test & Non-Conservative Loops (Chapter 4)

### Problem Statement
Consider the force field:

$$
\mathbf{F}(x, y) = (x^2 + a y)\,\hat{\mathbf{x}} + (2x + y^2)\,\hat{\mathbf{y}}
$$

1. Determine the value of the constant $a$ for which the force field is conservative.
2. For that value of $a$, calculate the potential energy function $U(x, y)$ with $U(0, 0) = 0$.
3. If $a = 5$, compute the work done around a closed unit square path $(0,0) \to (1,0) \to (1,1) \to (0,1) \to (0,0)$.

### Detailed Solution
1. **The Curl Condition**:  
   In 2D, the curl is:

   $$
   (\nabla \times \mathbf{F})_z = \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} = \frac{\partial}{\partial x}(2x + y^2) - \frac{\partial}{\partial y}(x^2 + ay) = 2 - a
   $$

   For the force to be conservative, $\nabla \times \mathbf{F} = \mathbf{0}$ everywhere:

   $$
   2 - a = 0 \implies a = 2
   $$

2. **Finding the Potential Energy**:  
   With $a = 2$:

   $$
   \mathbf{F} = -\nabla U \implies \frac{\partial U}{\partial x} = -(x^2 + 2y), \quad \frac{\partial U}{\partial y} = -(2x + y^2)
   $$

   Integrate $\frac{\partial U}{\partial x}$:

   $$
   U(x, y) = -\frac{1}{3} x^3 - 2xy + g(y)
   $$

   Differentiate with respect to $y$:

   $$
   \frac{\partial U}{\partial y} = -2x + g'(y) = -(2x + y^2) \implies g'(y) = -y^2 \implies g(y) = -\frac{1}{3} y^3
   $$

   Therefore:

   $$
   U(x, y) = -\frac{1}{3} x^3 - 2xy - \frac{1}{3} y^3
   $$

3. **Loop Integral for $a = 5$**:  
   Using Stokes' theorem for the unit square area $S$ ($[0, 1] \times [0, 1]$):

   $$
   W = \oint \mathbf{F} \cdot d\mathbf{r} = \int_S (\nabla \times \mathbf{F})_z \, dA
   $$

   Here $(\nabla \times \mathbf{F})_z = 2 - 5 = -3$:

   $$
   W = \int_0^1 \int_0^1 (-3)\,dx\,dy = -3 \times (1)(1) = -3.0\text{ Joules}
   $$

**Physical Takeaway**: Stokes' theorem allows you to compute the closed loop line integral in one line instead of evaluating four separate edge integrals.

---

## Problem 9: The Lennard-Jones Potential & Oscillation Period (Chapter 4)

### Problem Statement
A diatomic molecule is modeled by the Lennard-Jones potential:

$$
U(r) = U_0 \left[ \left(\frac{r_0}{r}\right)^{12} - 2 \left(\frac{r_0}{r}\right)^6 \right]
$$

1. Calculate the minimum potential energy $U_{\text{min}}$ and the equilibrium radius $r_0$.
2. Expand $U(r)$ to quadratic order about $r = r_0$ to find the effective spring constant $k_{\text{eff}}$.
3. If the reduced mass of the molecule is $\mu = 1.2 \times 10^{-26}\text{ kg}$, $U_0 = 1.0 \times 10^{-20}\text{ J}$, and $r_0 = 0.35\text{ nm}$, find the vibrational frequency in Terahertz (THz).

### Detailed Solution
1. **Equilibrium Point**:

   $$
   \frac{dU}{dr} = \frac{12 U_0}{r} \left[ -\left(\frac{r_0}{r}\right)^{12} + \left(\frac{r_0}{r}\right)^6 \right] = 0 \implies r_{\text{eq}} = r_0
   $$

   $$
   U(r_0) = U_0 [ 1 - 2 ] = -U_0
   $$

2. **Effective Spring Constant**:  
   Compute second derivative:

   $$
   \frac{d^2U}{dr^2} = \frac{U_0}{r^2} \left[ 156 \left(\frac{r_0}{r}\right)^{12} - 84 \left(\frac{r_0}{r}\right)^6 \right]
   $$

   $$
   k_{\text{eff}} = \left. \frac{d^2U}{dr^2} \right|_{r_0} = 72 \frac{U_0}{r_0^2}
   $$

3. **Numerical Frequency**:

   $$
   k_{\text{eff}} = \frac{72 \times (1.0 \times 10^{-20})}{(0.35 \times 10^{-9})^2} = \frac{7.2 \times 10^{-19}}{1.225 \times 10^{-19}} \approx 5.878\text{ N/m}
   $$

   $$
   \omega_0 = \sqrt{\frac{k_{\text{eff}}}{\mu}} = \sqrt{\frac{5.878}{1.2 \times 10^{-26}}} \approx 2.213 \times 10^{13}\text{ rad/s}
   $$

   $$
   f = \frac{\omega_0}{2\pi} \approx \frac{2.213 \times 10^{13}}{6.283} \approx 3.52 \times 10^{12}\text{ Hz} = 3.52\text{ THz}
   $$

**Physical Takeaway**: The simple 1D Taylor expansion accurately predicts molecular infrared absorption peaks.

---

## Problem 10: Central Force Effective Potential & Orbital Stability (Chapter 4)

### Problem Statement
A particle of mass $m$ moves under the influence of an attractive central force:

$$
\mathbf{F}(r) = -\left(\frac{k}{r^n}\right) \hat{\mathbf{r}} \quad (\text{where } k > 0 \text{ and } n \text{ is an arbitrary power})
$$

1. Find the potential energy function $U(r)$.
2. Write down the effective potential $U_{\text{eff}}(r)$ for a particle with angular momentum $l$.
3. Find the radius $r_0$ of a circular orbit.
4. Prove that a stable circular orbit can exist **only if $n < 3$** (Bertrand's Theorem criterion).

### Detailed Solution
1. **Potential Energy**:

   $$
   U(r) = - \int F(r)\,dr = - \int \left(-\frac{k}{r^n}\right) dr = -\frac{k}{(n-1)r^{n-1}} \quad (\text{for } n \neq 1)
   $$

2. **Effective Potential**:

   $$
   U_{\text{eff}}(r) = -\frac{k}{(n-1)r^{n-1}} + \frac{l^2}{2mr^2}
   $$

3. **Circular Orbit Radius**:  
   Set $\frac{dU_{\text{eff}}}{dr} = 0$:

   $$
   \frac{dU_{\text{eff}}}{dr} = -\frac{k}{r^n} + \frac{l^2}{mr^3} = 0 \implies \frac{k}{r^n} = \frac{l^2}{mr^3}
   $$

   $$
   k r_0^{3-n} = \frac{l^2}{m} \implies r_0 = \left( \frac{l^2}{mk} \right)^{1 / (3 - n)}
   $$

4. **Stability Condition**:  
   For stability, the second derivative must be strictly positive at $r = r_0$:

   $$
   \frac{d^2U_{\text{eff}}}{dr^2} = \frac{n k}{r^{n+1}} - \frac{3 l^2}{m r^4}
   $$

   Substitute $\frac{l^2}{m} = k r_0^{3-n}$:

   $$
   \left. \frac{d^2U_{\text{eff}}}{dr^2} \right|_{r_0} = \frac{n k}{r_0^{n+1}} - \frac{3 k r_0^{3-n}}{r_0^4} = (n - 3) \frac{k}{r_0^{n+1}}
   $$

   For $\left. \frac{d^2U_{\text{eff}}}{dr^2} \right|_{r_0} > 0$, we require:

   $$
   n - 3 < 0 \implies n < 3
   $$

**Physical Takeaway**: In any universe where gravitational forces fall off faster than $1/r^3$ (such as $1/r^4$), **planetary orbits are fundamentally unstable!** A tiny meteorite impact would cause the Earth to either spiral into the Sun or fly off into dark space. Stable solar systems are mathematically possible only because gravity is an inverse-square force ($n = 2 < 3$).\n