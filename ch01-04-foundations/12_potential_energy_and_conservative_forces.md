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
