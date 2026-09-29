# 07. Charged Particles in B Fields & Complex Exponentials

**Foundational Story**: Chapter 2, Sections 2.5–2.7  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 73–84)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 22 ("Algebra") & Vol. 2, Ch. 29 ("Motion of Charges")

---

## 1. The Lorentz Force

When an electric charge $q$ travels through an electric field $E$ and magnetic field $B$, it experiences the **Lorentz Force**:
```
F = q * (E + v x B)
```
Consider the case with **no electric field ($E = 0$)** and a **uniform, constant magnetic field** directed along the $z$-axis:
```
B = B * z_hat
```
Newton's Second Law is:
```
m * (dv/dt) = q * (v x B)
```
Compute the cross product:
```
v x B = | x_hat  y_hat  z_hat |
        | v_x    v_y    v_z   | = (v_y * B) * x_hat - (v_x * B) * y_hat + 0 * z_hat
        |  0      0      B    |
```
Writing component differential equations:
```
m * (dv_x/dt) =  q * B * v_y
m * (dv_y/dt) = -q * B * v_x
m * (dv_z/dt) =  0
```
Notice immediately:
* $v_z(t) = \text{constant}$. Motion along the $z$-axis is completely unaffected by the magnetic field!
* $v_x$ and $v_y$ form a coupled pair of first-order differential equations.

---

## 2. The Cyclotron Frequency

Define the **cyclotron frequency**:
```
ω = (q * B) / m
```
The equations simplify to:
```
dv_x / dt =  ω * v_y
dv_y / dt = -ω * v_x
```
Physical intuition: The acceleration is always perpendicular to velocity ($a \perp v$). 
Therefore, **the magnetic field does no work**:
```
dW/dt = F · v = q * (v x B) · v = 0
```
The kinetic energy and speed $\sqrt{v_x^2 + v_y^2}$ are strictly constant!

---

## 3. The Power of Complex Numbers (Taylor's Method)

Taylor introduces a profound mathematical trick that appears throughout modern physics: **combining two real coordinates into a single complex variable**.

Define the complex velocity:
```
η = v_x + i * v_y      (where i² = -1)
```
Now take the time derivative:
```
dη/dt = dv_x/dt + i * (dv_y/dt)
```
Substitute our equations of motion:
```
dη/dt = ω * v_y + i * (-ω * v_x) = -i * ω * (v_x + i * v_y)
```
Look at that! The two coupled real equations become **one single uncoupled complex ODE**:
```
dη / dt = -i * ω * η
```
The general solution is immediately:
```
η(t) = A * e^(-i * ω * t)
```
where $A$ is an arbitrary complex constant. Writing $A$ in polar form $A = v_{\text{tr}} e^{i\delta}$ (where $v_{\text{tr}}$ is the constant transverse speed in the $xy$-plane):
```
η(t) = v_tr * e^(-i * (ω*t - δ))
```
Using Euler's formula $e^{i\theta} = \cos(\theta) + i\sin(\theta)$:
```
v_x(t) + i * v_y(t) = v_tr * cos(ω*t - δ) - i * v_tr * sin(ω*t - δ)
```
Equating real and imaginary parts:
```
v_x(t) =  v_tr * cos(ω*t - δ)
v_y(t) = -v_tr * sin(ω*t - δ)
```

---

## 4. The Trajectory: Helical Motion

Integrate $v_x(t)$ and $v_y(t)$ to find position:
```
x(t) = X_0 + (v_tr / ω) * sin(ω*t - δ)
y(t) = Y_0 + (v_tr / ω) * cos(ω*t - δ)
z(t) = z_0 + v_z0 * t
```
Notice that:
```
(x - X_0)² + (y - Y_0)² = (v_tr / ω)² = r_L²
```
The projection of motion in the $xy$-plane is a **perfect circle** centered at $(X_0, Y_0)$ with radius:
```
r_L = v_tr / ω = (m * v_tr) / (q * B)     (Larmor Radius / Gyroradius)
```
Combined with constant motion along $z$, the particle traces out a **helix**!

---

## 5. Summary Cheat Sheet for Module 07

| Concept | Mathematical Form | Physical Meaning |
|---|---|---|
| **Lorentz Force** | `F = q * (E + v x B)` | Electromagnetic force on charge |
| **Cyclotron Frequency** | `ω = q*B / m` | Angular frequency of circular gyro-orbit |
| **Complex Velocity** | `η = v_x + i * v_y` | Unifies 2D plane motion into 1D complex space |
| **Complex ODE** | `dη/dt = -i*ω*η` | Solution: `η(t) = A * e^(-i*ω*t)` |
| **Larmor Radius** | `r_L = m*v_tr / (q*B)` | Radius of circular orbit in magnetic field |
| **Overall Motion** | Helix | Circle in $xy$-plane + uniform drift along $z$ |


---

## 6. Worked Examples & Practice Problems

### Worked Example 7.1: Cyclotron Parameters of a Relativistic-Prep Proton
**Problem**: A proton of mass `m = 1.67 x 10^-27 kg` and electric charge `q = +1.60 x 10^-19 C` is injected perpendicularly into a uniform magnetic field `B = 1.50 Tesla` with speed `v = 3.0 x 10^7 m/s` (about 10% the speed of light).
(a) Find the cyclotron frequency `ω` and the period of one complete circular orbit `τ`.
(b) Find the gyroradius (Larmor radius) `r_L`.
(c) Does the orbital period depend on the particle's speed? Why is this profound for accelerator design?

**Solution**:
(a) Cyclotron frequency:
```
ω = (q * B) / m = (1.60 x 10^-19 C * 1.50 T) / (1.67 x 10^-27 kg)
  = 1.437 x 10^8 rad/s
```
Cyclotron frequency in Hertz:
```
f = ω / (2*π) ≈ (1.437 x 10^8) / 6.283 ≈ 22.87 MHz
```
Period of one complete revolution:
```
τ = 1 / f = 2*π / ω ≈ 4.37 x 10^-8 seconds = 43.7 nanoseconds
```
(b) The Larmor radius is:
```
r_L = (m * v) / (q * B) = v / ω = (3.0 x 10^7 m/s) / (1.437 x 10^8 rad/s) ≈ 0.209 meters = 20.9 cm
```
(c) **Independence of Period**:
Notice that `τ = 2*π*m / (q*B)` contains **no velocity term `v`**!
As the proton gains speed, its orbit radius grows linearly (`r_L ∝ v`), so the circumference increases in exact proportion to the speed. It takes the exact same time to complete a large circle as a small circle!
This is the foundational principle of Ernest Lawrence's **Cyclotron**: an oscillating radio-frequency electric field with constant frequency `f` can continuously accelerate charges across the gap on every turn without needing variable frequency control.

---

### Worked Example 7.2: Crossed Electric and Magnetic Fields (E x B Drift)
**Problem**: A particle of mass `m` and charge `q` starts from rest at the origin in uniform crossed fields:
`E = E * y_hat` and `B = B * z_hat`.
Find the complete trajectory of the particle using complex variables, and show that its center of gyration drifts perpendicular to both fields.

**Solution**:
Newton's Second Law with the Lorentz force:
```
m * (dv/dt) = q * (E + v x B)
```
Component equations:
```
m * dv_x/dt = q * B * v_y
m * dv_y/dt = q * E - q * B * v_x
```
Divide by `m` and define `ω = q*B/m`:
```
dv_x/dt = ω * v_y
dv_y/dt = (q*E/m) - ω * v_x
```
Define the complex velocity `η = v_x + i * v_y`:
```
dη/dt = dv_x/dt + i * dv_y/dt = ω * v_y + i * [ (q*E/m) - ω * v_x ]
      = -i * ω * (v_x + i * v_y) + i * (q*E/m)
      = -i * ω * η + i * (q*E/m)
```
Let `v_d = E / B`. Since `q*E/m = ω * (E/B) = ω * v_d`:
```
dη/dt = -i * ω * (η - v_d)
```
Let `u = η - v_d`. Then `du/dt = -i*ω*u`, which integrates to:
```
η(t) - v_d = C * e^(-i*ω*t)
```
At `t = 0`, the particle starts from rest: `η(0) = 0`, so `0 - v_d = C ===> C = -v_d`.
```
η(t) = v_d * ( 1 - e^(-i*ω*t) )
```
Taking real and imaginary parts (`e^(-i*ω*t) = cos(ω*t) - i*sin(ω*t)`):
```
v_x(t) = v_d * ( 1 - cos(ω*t) )
v_y(t) = v_d * sin(ω*t)
```
Integrating to find position with `x(0) = 0, y(0) = 0`:
```
x(t) = v_d * t - (v_d / ω) * sin(ω*t)
y(t) = (v_d / ω) * ( 1 - cos(ω*t) )
```
**Physical Result**: The particle executes a **Cycloid**! 
Notice that along the $x$-axis, the average velocity is:
```
v_drift = v_d * x_hat = (E / B) * x_hat = (E x B) / B²
```
This is the celebrated **E x B Drift**: charges drift perpendicular to both the electric and magnetic fields regardless of their initial position!

---

### Practice Problem 7.1 (To Solve)
**Statement**: An electron moves in a uniform magnetic field `B = 0.20 T * z_hat`. At `t = 0`, its velocity is `v_0 = (3*x_hat + 4*z_hat) x 10^6 m/s`.
(a) Find the pitch of the resulting helical path (the distance traveled along the z-axis during one complete orbit).
(b) Find the radius of the helix.
* **Hint**: `v_z = 4 x 10^6 m/s = const`. `v_perp = 3 x 10^6 m/s`. Period `τ = 2*π*m / (q*B)`. Pitch `p = v_z * τ`.
* **Answer**: `ω = (1.60e-19 * 0.20) / (9.11e-31) ≈ 3.51 x 10^10 rad/s`. `τ = 2*π/ω ≈ 1.79 x 10^-10 s`. Pitch `p = (4e6) * (1.79e-10) ≈ 0.716 mm`. Radius `r_L = (3e6) / (3.51e10) ≈ 0.0855 mm`.

---

### Practice Problem 7.2 (To Solve)
**Statement**: In a velocity selector, perpendicular electric and magnetic fields are adjusted so that particles of charge `q` and velocity `v` pass through without deflection.
Show that the required speed is `v = E / B`, and explain why this condition is independent of both the particle's mass `m` and charge `q`.
* **Hint**: Set net Lorentz force to zero: `q*E - q*v*B = 0`.
* **Answer**: `q*(E - v*B) = 0 ===> v = E / B`. The electric force `q*E` and magnetic force `q*v*B` both scale linearly with `q`, so `q` cancels out completely!

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 2:
  * Sections 2.5–2.7 (pp. 73–84): Motion of a Charge in Uniform B Field, Complex Exponentials.
  * Problems 2.38, 2.42, 2.50, 2.54 (pp. 79–82): Detailed cycloid and helical trajectory problems.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*:
  * Vol. 1, Chapter 22: "Algebra" (complex numbers in physics).
  * Vol. 2, Chapter 29: "Motion of Charges in Electric and Magnetic Fields" (Sections 29.1–29.2).
