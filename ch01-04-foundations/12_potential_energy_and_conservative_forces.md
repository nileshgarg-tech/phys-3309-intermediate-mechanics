# 12. Potential Energy & Conservative Forces

**Foundational Story**: Chapter 4, Sections 4.2–4.5  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 4 (pp. 119–135)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 14 ("Work and Potential Energy (Conclusion)")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 4 & 5

---

## 1. What Makes a Force "Conservative"?

Friction is dissipative: if you slide a crate from point $A$ to point $B$ along a curvy, meandering path, you do much more work against friction than if you push it along a direct straight line.
Furthermore, if you push the crate in a complete closed loop back to $A$, the work done by friction is strictly negative: mechanical energy was permanently lost to heat.

A **Conservative Force** is fundamentally different:
> **Definition**: A force $F$ is conservative if and only if the work it performs on a particle moving between two points depends **only on the initial and final endpoints**, and is completely independent of the path taken between them.

```
                  Path 1
           +--------------------+
          /                               o Point A                o Point B
          \                      /
           +--------------------+
                  Path 2

    If F is conservative: W_Path1 = W_Path2
```

Equivalently, the work done by a conservative force around **any closed loop** is identically zero:
```
∮ F · dr = 0
```

---

## 2. Defining the Potential Energy Function $U(r)$

Because the work done by a conservative force depends only on the endpoints, we can define a scalar field called **Potential Energy** $U(r)$.

Choose an arbitrary reference point $r_0$ (where we declare $U(r_0) = 0$). 
The potential energy at any point $r$ is defined as the **negative of the work done by the conservative force** in moving from $r_0$ to $r$:
```
U(r) = - ∫_{r_0}^r F · dr'
```
Consequently, the work done in going from point 1 to point 2 is:
```
W_cons(1 -> 2) = - (U(r_2) - U(r_1)) = - ΔU
```
By the Work-Energy Theorem ($W_{\text{cons}} = \Delta T$):
```
- ΔU = ΔT   ===>   ΔT + ΔU = 0
```
Defining the **Total Mechanical Energy**:
```
E = T + U = constant!
```
The sum of kinetic and potential energy is conserved!

---

## 3. Force as the Gradient of Potential Energy

How do we recover the vector force $F$ if we are given the scalar potential $U(x, y, z)$?
Consider an infinitesimal displacement $dr = dx\,\hat{x} + dy\,\hat{y} + dz\,\hat{z}$.
By definition:
```
dU = - F · dr = - (F_x dx + F_y dy + F_z dz)
```
From multivariable calculus, the total differential of $U(x, y, z)$ is:
```
dU = (∂U/∂x) dx + (∂U/∂y) dy + (∂U/∂z) dz
```
Comparing coefficients:
```
F_x = - ∂U/∂x,   F_y = - ∂U/∂y,   F_z = - ∂U/∂z
```
In vector notation, using the **del / gradient operator** $\nabla$:
```
F = - ∇U = - [ (∂U/∂x)*x_hat + (∂U/∂y)*y_hat + (∂U/∂z)*z_hat ]
```
> **Physical Interpretation**: 
> The gradient $\nabla U$ points in the direction of steepest *ascent* of potential energy.
> Therefore, **the physical force $F = -\nabla U$ points in the direction of steepest *descent***.
> Systems naturally accelerate "downhill" toward lower potential energy!

---

## 4. The Mathematical Test: The Curl Condition

Suppose an instructor hands you a force field:
```
F(x, y, z) = (x² + y)*x_hat + (x + z)*y_hat + (y)*z_hat
```
How can you prove whether this force is conservative **without** testing infinitely many paths?

Recall **Stokes' Theorem** from vector calculus:
```
∮_C F · dr = ∫_S (∇ x F) · dA
```
For $\oint_C F \cdot dr = 0$ to hold for *every possible loop*, the integrand on the right must vanish everywhere:
```
∇ x F = 0   (The Curl of F must be zero everywhere)
```
Writing out the curl determinant:
```
∇ x F = |  x_hat    y_hat    z_hat  |
        |  ∂/∂x     ∂/∂y     ∂/∂z   | = 0
        |   F_x      F_y      F_z   |
```
Which gives three independent conditions:
```
∂F_z/∂y = ∂F_y/∂z
∂F_x/∂z = ∂F_z/∂x
∂F_y/∂x = ∂F_x/∂y
```
If a force passes this curl test everywhere in a simply-connected space, **it is guaranteed to be conservative.**

---

## 5. Summary Cheat Sheet for Module 12

| Property | Mathematical Criterion | Physical Meaning |
|---|---|---|
| **Path Independence** | `∫_A^B F · dr` depends only on A, B | Work is independent of route |
| **Closed Loop Work** | `∮ F · dr = 0` | Moving in a circle returns zero net energy |
| **Potential Function**| `U(r) = - ∫ F · dr` | Stored internal energy |
| **Force from Potential** | `F = - ∇U` | Force pushes downhill along steepest descent |
| **Differential Test** | `∇ x F = 0` (Curl = 0) | Necessary and sufficient condition for conservation |


---

## 6. Worked Examples & Practice Problems

### Worked Example 12.1: The Curl Test & Constructing the Potential Function
**Problem**: Consider the 3D force field:
```
F(x, y, z) = (2*x*y + z³)*x_hat + (x²)*y_hat + (3*x*z²)*z_hat
```
(a) Determine whether this force field is conservative by computing its curl `∇ x F`.
(b) If it is conservative, find the scalar potential energy function `U(x, y, z)` choosing `U(0, 0, 0) = 0`.

**Solution**:
(a) **Curl Calculation**:
```
∇ x F = |  x_hat        y_hat        z_hat  |
        |  ∂/∂x         ∂/∂y         ∂/∂z   |
        |  2*x*y + z³   x²           3*x*z² |
```
Component by component:
* `(∇ x F)_x = ∂(3*x*z²)/∂y - ∂(x²)/∂z = 0 - 0 = 0`
* `(∇ x F)_y = ∂(2*x*y + z³)/∂z - ∂(3*x*z²)/∂x = 3*z² - 3*z² = 0`
* `(∇ x F)_z = ∂(x²)/∂x - ∂(2*x*y + z³)/∂y = 2*x - 2*x = 0`
Since `∇ x F = 0` identically everywhere, **the force is conservative**!

(b) **Finding Potential Energy `U(x, y, z)`**:
We require `F = -∇U`, which means:
1. `∂U/∂x = - (2*x*y + z³)`
2. `∂U/∂y = - (x²)`
3. `∂U/∂z = - (3*x*z²)`

Integrate equation (2) with respect to `y`:
```
U(x, y, z) = - x²*y + g(x, z)
```
Differentiate with respect to `z` and set equal to equation (3):
```
∂U/∂z = ∂g/∂z = - 3*x*z²   ===>   g(x, z) = - x*z³ + h(x)
U(x, y, z) = - x²*y - x*z³ + h(x)
```
Now differentiate with respect to `x` and set equal to equation (1):
```
∂U/∂x = - 2*x*y - z³ + dh/dx = - (2*x*y + z³)   ===>   dh/dx = 0  ===>  h(x) = C (constant)
```
Using the reference point `U(0, 0, 0) = 0`, we find `C = 0`.
Therefore:
```
U(x, y, z) = - x²*y - x*z³
```

---

### Worked Example 12.2: Gravitational Potential Energy from Line Integration
**Problem**: The gravitational force exerted by a mass `M` at the origin on a mass `m` is:
```
F(r) = - (G * M * m / r²) * r_hat
```
Show that this force is conservative by finding its potential energy `U(r)` referenced to zero at spatial infinity (`r_0 -> ∞`).

**Solution**:
The force is purely radial, and the path element is `dr = dr*r_hat + r*dθ*θ_hat + r*sin(θ)*dφ*φ_hat`.
Thus `F · dr = F_r dr = -(G*M*m / r²) dr`.
By definition of potential energy:
```
U(r) = - ∫_{r_0}^r F · dr' = - ∫_∞^r [ - (G * M * m / (r')²) ] dr'
     = G * M * m * ∫_∞^r (r')^(-2) dr' = G * M * m * [ - 1 / r' ]_∞^r
```
Evaluating the limits:
```
U(r) = G * M * m * [ - 1 / r - (- 1 / ∞) ] = - (G * M * m) / r
```
Check gradient:
```
F = - dU/dr * r_hat = - d/dr [ -G*M*m/r ] * r_hat = - (G*M*m / r²) * r_hat
```
Matches Newton's universal gravitational law exactly!

---

### Practice Problem 12.1 (To Solve)
**Statement**: Test whether the force `F = (y²)*x_hat + (2*x*y + z)*y_hat + (y)*z_hat` is conservative.
If conservative, find the potential energy `U(x, y, z)` with `U(0, 0, 0) = 0`.
* **Hint**: Compute all 3 components of `∇ x F`. If zero, integrate `∂U/∂x, ∂U/∂y, ∂U/∂z`.
* **Answer**: `(∇ x F)_x = 1 - 1 = 0`, `(∇ x F)_y = 0 - 0 = 0`, `(∇ x F)_z = 2y - 2y = 0`. The force is conservative! Potential energy: `U(x, y, z) = -x*y² - y*z`.

---

### Practice Problem 12.2 (To Solve)
**Statement**: Prove that any spherically symmetric central force `F(r) = f(r) * r_hat` is conservative for any arbitrary continuous function `f(r)`.
* **Hint**: Show that the work around any closed path `∮ f(r) * r_hat · dr = ∮ f(r) dr` is the integral of an exact differential `df(r)/dr`, or use spherical curl: `(∇ x F)_φ = (1/r)*(∂(r*F_θ)/∂r - ∂F_r/∂θ) = 0`.
* **Answer**: Since `r_hat · dr = dr`, the line integral is `∫ f(r) dr`, which depends only on the scalar distance `r` at endpoints, independent of angular coordinates or path.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Sections 4.2–4.5 (pp. 119–135): Conservative Forces, Potential Energy, Gradient Operator, Curl Test.
  * Problems 4.12, 4.18, 4.23 (pp. 165–168): Detailed curl proofs and potential derivations.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 14: "Work and Potential Energy (Conclusion)" (Sections 14.1–14.4 on conservative fields and curl).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.4–5.7).
