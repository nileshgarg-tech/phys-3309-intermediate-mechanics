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
