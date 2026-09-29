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
