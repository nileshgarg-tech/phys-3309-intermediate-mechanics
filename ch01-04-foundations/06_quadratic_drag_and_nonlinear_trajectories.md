# 06. Quadratic Drag & Nonlinear Trajectories

**Foundational Story**: Chapter 2, Section 2.4  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 60–73)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 9 & Ch. 41

---

## 1. The Coupling Dilemma: Why 2D Quadratic Drag is Difficult

Recall the quadratic drag law:
```
f = -c * |v| * v
```
In two dimensions ($x$ horizontal, $y$ vertical), the speed is $|v| = \sqrt{v_x^2 + v_y^2}$.
Writing Newton's Second Law component-wise:
```
m * (dv_x/dt) = -c * sqrt(v_x² + v_y²) * v_x
m * (dv_y/dt) = -m*g - c * sqrt(v_x² + v_y²) * v_y
```
Look at these equations: **they are coupled nonlinear differential equations.**
The horizontal acceleration depends on the vertical velocity, and the vertical acceleration depends on the horizontal velocity!
Because of this coupling, **no closed-form analytical solution exists in elementary functions for 2D quadratic drag.** 
(This is why Chapter 2 introduces numerical Runge-Kutta / Euler integration for artillery shells and baseballs).

However, **pure vertical 1D motion** can be solved analytically with elegant calculus!

---

## 2. Vertical Drop from Rest with Quadratic Drag

Let a body drop from rest at $t = 0$ ($y$ pointing downward so gravity is positive):
```
m * (dv/dt) = m*g - c * v²
```
Terminal velocity occurs when acceleration vanishes:
```
0 = m*g - c * v_ter²   ===>   v_ter = sqrt(m*g / c)
```
We can rewrite the equation of motion in terms of $v_{\text{ter}}$:
```
dv/dt = g * [ 1 - (v / v_ter)² ]
```
Separate variables:
```
∫ dv / (1 - (v / v_ter)²) = g ∫ dt
```
Recall the standard hyperbolic substitution:
```
∫ du / (1 - u²) = arctanh(u)
```
Let $u = v / v_{\text{ter}}$, so $dv = v_{\text{ter}} du$:
```
v_ter * arctanh(v / v_ter) = g * t
```
Solving for $v(t)$:
```
v(t) = v_ter * tanh(g * t / v_ter) = v_ter * tanh(t / τ)
```
where the characteristic time is:
```
τ = v_ter / g = sqrt(m / (g * c))
```

### Position $y(t)$
Integrate $v(t) = dy/dt$:
```
y(t) = ∫_0^t v_ter * tanh(t' / τ) dt'
```
Since $\int \tanh(z) dz = \ln(\cosh(z))$:
```
y(t) = (v_ter² / g) * ln(cosh(t / τ))
```

### Limiting Behaviors:
1. **Short times ($t \ll \tau$)**:
   Since $\cosh(z) \approx 1 + z^2/2$ and $\ln(1 + u) \approx u$:
   ```
   y(t) ≈ (v_ter² / g) * (1/2) * (t / τ)² = (1/2) * g * t²
   ```
   *(Freely falling body in vacuum!)*
2. **Long times ($t \gg \tau$)**:
   Since $\cosh(z) \approx e^z / 2$:
   ```
   y(t) ≈ v_ter * t - (v_ter² / g) * ln(2)
   ```
   *(Uniform linear motion at constant terminal speed $v_{\text{ter}}$!)*

---

## 3. Projectile Thrown Straight Up

If an object is launched straight upward with initial speed $v_0$, both gravity and drag point downward:
```
m * (dv/dt) = -m*g - c * v² = -g * [ 1 + (v / v_ter)² ]
```
Separation of variables gives:
```
∫ dv / (1 + (v / v_ter)²) = -g ∫ dt   ===>   v_ter * arctan(v / v_ter) = -g*t + C
```
Using $v(0) = v_0$:
```
v(t) = v_ter * tan[ arctan(v_0 / v_ter) - (g * t / v_ter) ]
```
The particle reaches its maximum height when $v(t_{\text{top}}) = 0$:
```
t_top = (v_ter / g) * arctan(v_0 / v_ter)
```
Notice that $t_{\text{top}} < v_0 / g$. **Air drag shortens the time required to reach the peak compared to a vacuum.**

---

## 4. Summary Cheat Sheet for Module 06

| Situation | Velocity Solution | Characteristic Parameter |
|---|---|---|
| **Terminal Speed** | `v_ter = sqrt(m*g / c)` | Force balance `m*g = c*v_ter²` |
| **Vertical Drop** | `v(t) = v_ter * tanh(t / τ)` | `τ = v_ter / g` |
| **Drop Distance** | `y(t) = (v_ter²/g) * ln(cosh(t/τ))` | Approaches `v_ter * t` as $t \to \infty$ |
| **Upward Launch** | `v(t) = v_ter * tan(arctan(v_0/v_ter) - t/τ)` | Reaches peak faster than vacuum |
| **2D Trajectory** | Coupled nonlinear ODEs | Must be solved numerically (Euler/RK4) |


---

## 5. Worked Examples & Practice Problems

### Worked Example 6.1: Free-Fall of a Skydiver under Quadratic Drag
**Problem**: An 80 kg skydiver jumps from an airplane. In a spread-eagle belly-to-earth posture, quadratic drag is dominant with `c ≈ 0.25 N·s²/m²`.
(a) What is the skydiver's terminal speed `v_ter`?
(b) What is the characteristic time `τ`?
(c) How fast is the skydiver falling after `t = 5.0 s`?
(d) How far has the skydiver fallen after `t = 5.0 s`?

**Solution**:
(a) Terminal velocity:
```
v_ter = sqrt(m * g / c) = sqrt( (80 * 9.8) / 0.25 ) = sqrt( 784 / 0.25 ) = sqrt(3136) = 56.0 m/s  (approx 125 mph)
```
(b) Characteristic time:
```
τ = v_ter / g = 56.0 / 9.8 ≈ 5.71 seconds
```
(c) Speed after 5.0 seconds:
```
v(t) = v_ter * tanh(t / τ)
t / τ = 5.0 / 5.71 ≈ 0.875
tanh(0.875) ≈ 0.704
v(5) = 56.0 * 0.704 ≈ 39.4 m/s  (approx 88 mph, about 70% of terminal speed)
```
(d) Distance fallen after 5.0 seconds:
```
y(t) = (v_ter² / g) * ln(cosh(t / τ))
v_ter² / g = 3136 / 9.8 = 320 meters
cosh(0.875) ≈ 1.408
ln(1.408) ≈ 0.342
y(5) = 320 * 0.342 ≈ 109.4 meters
```
*(In a vacuum, the skydiver would have fallen `(1/2)*g*t² = (0.5)*(9.8)*(25) = 122.5 m` and reached speed `49 m/s`)*.

---

### Worked Example 6.2: Maximum Height of an Upward Launch with Quadratic Drag
**Problem**: A baseball is popped straight up into the air with initial speed `v_0 = 35 m/s`. Its terminal speed when dropped from a high tower is measured to be `v_ter = 35 m/s`. 
Find the maximum height `y_max` reached by the ball, and compare it to the vacuum height `y_vac = v_0² / (2*g)`.

**Solution**:
For upward vertical motion under gravity and quadratic drag:
```
m * v * (dv/dy) = -m*g - c*v² = -m*g * [ 1 + (v / v_ter)² ]
```
Divide by `m`:
```
v * (dv/dy) = -g * [ 1 + (v / v_ter)² ]
```
Separate variables:
```
∫_{v_0}^0 [ v / (1 + (v / v_ter)²) ] dv = -g ∫_0^y_max dy
```
Let `u = 1 + (v / v_ter)²`, then `du = (2 / v_ter²) * v dv`:
```
(1/2) * v_ter² * ∫_{1 + (v_0/v_ter)²}^1 (du / u) = -g * y_max
-(1/2) * v_ter² * ln( 1 + (v_0 / v_ter)² ) = -g * y_max
```
Solving for `y_max`:
```
y_max = (v_ter² / (2*g)) * ln( 1 + (v_0 / v_ter)² )
```
Substitute `v_0 = 35 m/s`, `v_ter = 35 m/s`, `g = 9.8 m/s²`:
```
y_max = (35² / (2 * 9.8)) * ln( 1 + (35 / 35)² )
      = (1225 / 19.6) * ln(2) ≈ 62.5 * 0.6931 ≈ 43.3 meters
```
In a vacuum:
```
y_vac = v_0² / (2*g) = 1225 / 19.6 = 62.5 meters
```
**Physical Insight**: Quadratic air resistance reduces the maximum height from 62.5 m to 43.3 m—a 31% reduction!

---

### Practice Problem 6.1 (To Solve)
**Statement**: An object is launched straight downward with an initial speed `v_0` that is *greater* than its terminal speed (`v_0 > v_ter`).
Set up the differential equation and solve for `v(t)`. Show that the speed decreases asymptotically toward `v_ter`.
* **Hint**: The drag force is upward and exceeds gravity: `m * dv/dt = m*g - c*v² = -g * [(v/v_ter)² - 1]`. Use `∫ du / (u² - 1) = -arctanh(1/u) = -arccoth(u)`.
* **Answer**: `v(t) = v_ter * coth( t/τ + arccoth(v_0 / v_ter) )`. As `t -> ∞`, `coth -> 1`, so `v(t) -> v_ter`.

---

### Practice Problem 6.2 (To Solve)
**Statement**: For a projectile launched vertically upward with initial speed `v_0` in quadratic drag:
Show that the time `t_top` required to reach the peak is strictly less than the vacuum time `t_vac = v_0 / g`.
* **Hint**: Recall `t_top = (v_ter / g) * arctan(v_0 / v_ter)`. Use the inequality `arctan(z) < z` for all `z > 0`.
* **Answer**: Letting `z = v_0 / v_ter`, `t_top = (v_ter / g) * arctan(z) < (v_ter / g) * z = v_0 / g = t_vac`.

---

## 6. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 2:
  * Section 2.4 (pp. 60–73): Quadratic Air Resistance, Vertical Drop, Upward Launch.
  * Problems 2.20, 2.24, 2.28 (pp. 76–78): Analytical hyperbolic solutions for quadratic drag.
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 2: "Newton's Laws" (Section 2.5 on terminal velocity).
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 9: "Newton's Laws of Dynamics" (Section 9.6 on numerical solutions of nonlinear drag).
