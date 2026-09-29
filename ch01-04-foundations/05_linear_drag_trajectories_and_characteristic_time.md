# 05. Linear Air Drag: Exact Trajectories & Characteristic Time

**Foundational Story**: Chapter 2, Sections 2.2–2.3  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 48–60)
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 2

---

## 1. The Equations of Motion for Linear Drag

When drag is proportional to velocity:
```
f = -b * v
```
Newton's Second Law for a particle under gravity and linear drag is:
```
m * (dv/dt) = m*g_vec - b*v
```
Because the linear drag force components decouple:
```
m * (dv_x/dt) = -b * v_x
m * (dv_y/dt) = -m*g - b * v_y
```
Notice the tremendous mathematical advantage of linear drag: **the horizontal motion $x(t)$ and vertical motion $y(t)$ are completely decoupled!** We can solve them independently.

---

## 2. Horizontal Motion (Pure Drag, No Gravity)

Consider a projectile fired horizontally with initial speed $v_{x0}$:
```
m * (dv_x/dt) = -b * v_x
```
Divide by $m$ and define the **characteristic time** $\tau$:
```
τ = m / b
```
The differential equation becomes:
```
dv_x / dt = - (1 / τ) * v_x
```
Separate variables and integrate:
```
∫ (1 / v_x) dv_x = - (1 / τ) ∫ dt   ===>   ln(v_x / v_x0) = -t / τ
```
Exponentiate:
```
v_x(t) = v_x0 * e^(-t / τ)
```

### Position $x(t)$
Integrate velocity to find position:
```
x(t) = ∫_0^t v_x(t') dt' = v_x0 * ∫_0^t e^(-t' / τ) dt'
     = v_x0 * [-τ * e^(-t' / τ)]_0^t
```
```
x(t) = v_x0 * τ * (1 - e^(-t / τ))
```

> **The Finite Range Limit**:
> As $t \to \infty$, $e^{-t/\tau} \to 0$. The particle never travels infinitely far!
> It approaches a finite horizontal boundary:
> ```
> x_max = v_x0 * τ = (m * v_x0) / b
> ```

---

## 3. Vertical Motion & Terminal Velocity

Now consider vertical fall under gravity ($y$ axis positive upward):
```
m * (dv_y/dt) = -m*g - b*v_y
```
Divide by $m$:
```
dv_y/dt = -g - (v_y / τ) = -(1 / τ) * (g*τ + v_y)
```
Notice that when $dv_y/dt = 0$, the drag force exactly balances gravity:
```
0 = -m*g - b*v_y   ===>   v_y = - (m*g / b) = - g*τ
```
We define the **terminal speed** $v_{\text{ter}}$:
```
v_ter = g * τ = (m * g) / b
```
Rewrite the ODE:
```
dv_y / dt = - (1 / τ) * (v_y + v_ter)
```
Separate variables from initial condition $v_y(0) = v_{y0}$:
```
∫_{v_y0}^{v_y} d(v_y + v_ter) / (v_y + v_ter) = - (1 / τ) ∫_0^t dt
```
Integrating yields:
```
v_y(t) = -v_ter + (v_y0 + v_ter) * e^(-t / τ)
```
If dropped from rest ($v_{y0} = 0$):
```
v_y(t) = -v_ter * (1 - e^(-t / τ))
```
* At $t = 0$: $v_y = 0$, acceleration is $-g$.
* At $t = \tau$: $v_y = -0.632 \cdot v_{\text{ter}}$.
* At $t = 3\tau$: $v_y = -0.95 \cdot v_{\text{ter}}$ (essentially at terminal velocity).

Integrating $v_y(t)$ gives position:
```
y(t) = y_0 - v_ter * t + (v_y0 + v_ter) * τ * (1 - e^(-t / τ))
```

---

## 4. The 2D Trajectory and Recovery of Vacuum Physics

Combining $x(t)$ and $y(t)$ gives the trajectory curve $y(x)$.
From $x(t) = v_{x0} \tau (1 - e^{-t/\tau})$, solve for $e^{-t/\tau}$:
```
e^(-t / τ) = 1 - (x / (v_x0 * τ))
```
Taking the natural logarithm:
```
t = -τ * ln(1 - x / (v_x0 * τ))
```
Substitute $t$ and $e^{-t/\tau}$ into $y(t)$ (with $y_0 = 0$):
```
y(x) = (v_y0 + v_ter) / v_x0 * x + v_ter * τ * ln(1 - x / (v_x0 * τ))
```

### The Perturbation Test: Do We Recover Galileo?
When drag is very weak ($b \to 0$, meaning $\tau = m/b \to \infty$), $x / (v_{x0}\tau) \ll 1$.
We Taylor-expand the logarithm: $\ln(1 - u) = -u - u^2/2 - u^3/3 - \dots$:
```
ln(1 - x / (v_x0 * τ)) ≈ - (x / (v_x0*τ)) - (1/2) * (x / (v_x0*τ))² - ...
```
Substitute this expansion:
```
y(x) ≈ ( (v_y0 + v_ter)/v_x0 ) * x + v_ter * τ * [ - x/(v_x0*τ) - x²/(2*v_x0²*τ²) ]
     = (v_y0 / v_x0) * x - (v_ter / (2 * v_x0² * τ)) * x²
```
Since $v_{\text{ter}} / \tau = (g\tau)/\tau = g$:
```
y(x) ≈ (v_y0 / v_x0) * x - (g / (2 * v_x0²)) * x²
```
**This is the exact elementary vacuum parabola!** 
Taylor highlights this sanity check: any valid drag theory must smoothly reproduce standard Galilean physics in the zero-drag limit.

---

## 5. Summary Cheat Sheet for Module 05

| Quantity | Formula | Meaning |
|---|---|---|
| **Characteristic Time** | `τ = m / b` | Time scale to lose $1/e \approx 63\%$ of speed |
| **Terminal Velocity** | `v_ter = g * τ = m*g / b` | Maximum steady-state falling speed |
| **Horizontal Velocity** | `v_x(t) = v_x0 * e^(-t/τ)` | Exponential decay |
| **Maximum Range** | `x_max = v_x0 * τ` | Absolute horizontal wall |
| **Zero-Drag Limit** | Expand `ln(1 - u)` | Recovers vacuum parabola `y = (v_y0/v_x0)x - (g/2v_x0²)x²` |


---

## 6. Worked Examples & Practice Problems

### Worked Example 5.1: The Linear Stopping Distance
**Problem**: A motorboat of mass `m = 500 kg` is traveling at speed `v_0 = 20 m/s` when its engine is suddenly cut off. The water exerts a viscous linear drag force with coefficient `b = 50 N·s/m`.
(a) What is the characteristic time `τ` of the boat?
(b) How long does it take for the boat's speed to drop to `1 m/s`?
(c) What is the maximum distance the boat can travel after the engine is cut?

**Solution**:
(a) Characteristic time:
```
τ = m / b = 500 kg / (50 N·s/m) = 10.0 seconds
```
(b) Speed decays exponentially: `v(t) = v_0 * e^(-t / τ)`.
Setting `v(t) = 1 m/s`:
```
1 = 20 * e^(-t / 10)  ===>  e^(t / 10) = 20
t = 10 * ln(20) ≈ 10 * 2.9957 ≈ 29.96 seconds
```
(c) The position as a function of time is `x(t) = v_0 * τ * (1 - e^(-t / τ))`.
As `t -> ∞`, `e^(-t/τ) -> 0`:
```
x_max = v_0 * τ = (20 m/s) * (10.0 s) = 200 meters
```
The boat will never coast farther than 200 meters regardless of how long it drifts!

---

### Worked Example 5.2: Terminal Speed of a Heavy Mist Droplet
**Problem**: A spherical water droplet of diameter `D = 0.10 mm = 10^-4 m` falls vertically through air.
Its mass is `m = ρ_water * (π/6) * D³ = (1000 kg/m³) * (π/6) * (10^-4)³ ≈ 5.24 x 10^-10 kg`.
The linear drag coefficient is `b = 3 * π * η * D ≈ 3 * π * (1.8 x 10^-5) * (10^-4) ≈ 1.70 x 10^-8 N·s/m`.
(a) Calculate its terminal velocity `v_ter`.
(b) Calculate the time required to reach 99% of its terminal velocity.

**Solution**:
(a) Terminal velocity:
```
v_ter = (m * g) / b = (5.24 x 10^-10 kg * 9.8 m/s²) / (1.70 x 10^-8 N·s/m) ≈ 0.302 m/s (approx 30 cm/s)
```
(b) Speed starting from rest: `v_y(t) = v_ter * (1 - e^(-t / τ))`.
Characteristic time:
```
τ = m / b = (5.24 x 10^-10) / (1.70 x 10^-8) ≈ 0.0308 seconds
```
We require `v_y(t) = 0.99 * v_ter`:
```
1 - e^(-t / τ) = 0.99  ===>  e^(-t / τ) = 0.01  ===>  t = τ * ln(100)
t = 0.0308 * 4.605 ≈ 0.142 seconds
```
The droplet reaches 99% of its terminal speed in less than 0.15 seconds and falls less than 3 cm before reaching terminal velocity!

---

### Practice Problem 5.1 (To Solve)
**Statement**: A projectile is launched horizontally with initial speed `v_0` from a cliff of height `h` in a medium with linear drag.
Find the horizontal distance `x` traveled by the projectile by the time it has lost half its initial horizontal speed (`v_x = v_0 / 2`).
* **Hint**: `v_x(t) = v_0 * e^(-t/τ) = v_0 / 2  ===>  e^(-t/τ) = 1/2`. Then substitute into `x(t) = v_0 * τ * (1 - e^(-t/τ))`.
* **Answer**: `x = (1/2) * v_0 * τ = (m * v_0) / (2 * b) = (1/2) * x_max`.

---

### Practice Problem 5.2 (To Solve)
**Statement**: A ball is thrown vertically upward with initial speed `v_0` under linear air drag with terminal speed `v_ter`.
Prove that the maximum height reached is:
`y_max = v_ter * τ * [ (v_0 / v_ter) - ln(1 + v_0 / v_ter) ]`.
* **Hint**: Use `m * v * (dv/dy) = -m*g - b*v = -b*(v + v_ter)` and integrate from `v = v_0` to `v = 0`.
* **Answer**: `∫_{v_0}^0 [ v / (v + v_ter) ] dv = -(b/m) y_max = - (1/τ) y_max`. Evaluating the integral directly gives the formula.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 2:
  * Sections 2.2–2.3 (pp. 48–60): Linear Air Resistance, Horizontal and Vertical Motion, Trajectory Analysis.
  * Problems 2.7, 2.11, 2.15, 2.18 (pp. 74–76): Detailed linear drag problem sets.
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 2: "Newton's Laws" (Section 2.5 on drag forces).
* **Morin, David**, *Introduction to Classical Mechanics*, Chapter 3:
  * Example 3.4 (pp. 68–71): Detailed derivation of linear drag asymptotic expansions.
