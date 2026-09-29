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
