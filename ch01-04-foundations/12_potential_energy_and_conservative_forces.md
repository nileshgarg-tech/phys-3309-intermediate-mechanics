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
> **Definition**: A force $\mathbf{F}$ is conservative if and only if the work it performs on a particle moving between two points depends **only on the initial and final endpoints**, and is completely independent of the path taken between them.

Equivalently, the work done by a conservative force around **any closed loop** is identically zero:

$$
\oint \mathbf{F} \cdot d\mathbf{r} = 0
$$

---

## 2. Defining the Potential Energy Function $U(\mathbf{r})$

Because the work done by a conservative force depends only on the endpoints, we can define a scalar field called **Potential Energy** $U(\mathbf{r})$.

Choose an arbitrary reference point $\mathbf{r}_0$ (where we declare $U(\mathbf{r}_0) = 0$).  
The potential energy at any point $\mathbf{r}$ is defined as the **negative of the work done by the conservative force** in moving from $\mathbf{r}_0$ to $\mathbf{r}$:

$$
U(\mathbf{r}) = - \int_{\mathbf{r}_0}^{\mathbf{r}} \mathbf{F} \cdot d\mathbf{r}'
$$

Consequently, the work done in going from point 1 to point 2 is:

$$
W_{\text{cons}}(1 \to 2) = - [U(\mathbf{r}_2) - U(\mathbf{r}_1)] = - \Delta U
$$

By the Work-Energy Theorem ($W_{\text{cons}} = \Delta T$):

$$
-\Delta U = \Delta T \implies \Delta T + \Delta U = 0
$$

Defining the **Total Mechanical Energy**:

$$
E = T + U = \text{constant}
$$

The sum of kinetic and potential energy is conserved!

---

## 3. Force as the Gradient of Potential Energy

How do we recover the vector force $\mathbf{F}$ if we are given the scalar potential $U(x, y, z)$?  
Consider an infinitesimal displacement $d\mathbf{r} = dx\,\hat{\mathbf{x}} + dy\,\hat{\mathbf{y}} + dz\,\hat{\mathbf{z}}$. By definition:

$$
dU = -\mathbf{F} \cdot d\mathbf{r} = -(F_x\,dx + F_y\,dy + F_z\,dz)
$$

From multivariable calculus, the total differential of $U(x, y, z)$ is:

$$
dU = \frac{\partial U}{\partial x}\,dx + \frac{\partial U}{\partial y}\,dy + \frac{\partial U}{\partial z}\,dz
$$

Comparing coefficients:

$$
F_x = -\frac{\partial U}{\partial x}, \quad F_y = -\frac{\partial U}{\partial y}, \quad F_z = -\frac{\partial U}{\partial z}
$$

In vector notation, using the **gradient operator** $\nabla$:

$$
\mathbf{F} = -\nabla U = - \left( \frac{\partial U}{\partial x}\,\hat{\mathbf{x}} + \frac{\partial U}{\partial y}\,\hat{\mathbf{y}} + \frac{\partial U}{\partial z}\,\hat{\mathbf{z}} \right)
$$

> **Physical Interpretation**:  
> The gradient $\nabla U$ points in the direction of steepest *ascent* of potential energy.  
> Therefore, **the physical force $\mathbf{F} = -\nabla U$ points in the direction of steepest *descent***.  
> Systems naturally accelerate "downhill" toward lower potential energy!

---

## 4. The Mathematical Test: The Curl Condition

Suppose an instructor hands you a force field $\mathbf{F}(x, y, z)$. How can you prove whether this force is conservative **without** testing infinitely many paths?

Recall **Stokes' Theorem** from vector calculus:

$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = \int_S (\nabla \times \mathbf{F}) \cdot d\mathbf{A}
$$

For $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$ to hold for *every possible loop*, the curl must vanish identically everywhere:

$$
\nabla \times \mathbf{F} = \mathbf{0}
$$

Writing out the curl determinant:

$$
\nabla \times \mathbf{F} = \begin{vmatrix}
\hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix} = \mathbf{0}
$$

Which gives three independent conditions:

$$
\frac{\partial F_z}{\partial y} = \frac{\partial F_y}{\partial z}, \quad \frac{\partial F_x}{\partial z} = \frac{\partial F_z}{\partial x}, \quad \frac{\partial F_y}{\partial x} = \frac{\partial F_x}{\partial y}
$$

If a force passes this curl test everywhere in a simply-connected space, **it is guaranteed to be conservative.**

---

## 5. Summary Cheat Sheet for Module 12

| Property | Mathematical Criterion | Physical Meaning |
|---|---|---|
| **Path Independence** | $\int_A^B \mathbf{F} \cdot d\mathbf{r}$ depends only on $A, B$ | Work is independent of route |
| **Closed Loop Work** | $\oint \mathbf{F} \cdot d\mathbf{r} = 0$ | Moving in a circle returns zero net energy |
| **Potential Function**| $U(\mathbf{r}) = -\int \mathbf{F} \cdot d\mathbf{r}$ | Stored internal energy |
| **Force from Potential** | $\mathbf{F} = -\nabla U$ | Force pushes downhill along steepest descent |
| **Differential Test** | $\nabla \times \mathbf{F} = \mathbf{0}$ | Necessary and sufficient condition for conservation |

---

## 6. Worked Examples & Practice Problems

### Worked Example 12.1: The Curl Test & Constructing the Potential Function
**Problem**: Consider the 3D force field:

$$
\mathbf{F}(x, y, z) = (2xy + z^3)\,\hat{\mathbf{x}} + x^2\,\hat{\mathbf{y}} + 3xz^2\,\hat{\mathbf{z}}
$$

(a) Determine whether this force field is conservative by computing its curl $\nabla \times \mathbf{F}$.  
(b) If it is conservative, find the scalar potential energy function $U(x, y, z)$ choosing $U(0, 0, 0) = 0$.

**Solution**:  
(a) **Curl Calculation**:

$$
\nabla \times \mathbf{F} = \begin{vmatrix}
\hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
2xy + z^3 & x^2 & 3xz^2
\end{vmatrix}
$$

Component by component:
* $(\nabla \times \mathbf{F})_x = \frac{\partial}{\partial y}(3xz^2) - \frac{\partial}{\partial z}(x^2) = 0 - 0 = 0$
* $(\nabla \times \mathbf{F})_y = \frac{\partial}{\partial z}(2xy + z^3) - \frac{\partial}{\partial x}(3xz^2) = 3z^2 - 3z^2 = 0$
* $(\nabla \times \mathbf{F})_z = \frac{\partial}{\partial x}(x^2) - \frac{\partial}{\partial y}(2xy + z^3) = 2x - 2x = 0$

Since $\nabla \times \mathbf{F} = \mathbf{0}$ identically everywhere, **the force is conservative**!

(b) **Finding Potential Energy $U(x, y, z)$**:  
We require $\mathbf{F} = -\nabla U$, which means:
1. $\frac{\partial U}{\partial x} = -(2xy + z^3)$
2. $\frac{\partial U}{\partial y} = -x^2$
3. $\frac{\partial U}{\partial z} = -3xz^2$

Integrate equation (2) with respect to $y$:

$$
U(x, y, z) = -x^2 y + g(x, z)
$$

Differentiate with respect to $z$ and set equal to equation (3):

$$
\frac{\partial U}{\partial z} = \frac{\partial g}{\partial z} = -3xz^2 \implies g(x, z) = -xz^3 + h(x)
$$

$$
U(x, y, z) = -x^2 y - xz^3 + h(x)
$$

Now differentiate with respect to $x$ and set equal to equation (1):

$$
\frac{\partial U}{\partial x} = -2xy - z^3 + h'(x) = -(2xy + z^3) \implies h'(x) = 0 \implies h(x) = C
$$

Using the reference point $U(0, 0, 0) = 0$, we find $C = 0$. Therefore:

$$
U(x, y, z) = -x^2 y - x z^3
$$

---

### Worked Example 12.2: Gravitational Potential Energy from Line Integration
**Problem**: The gravitational force exerted by a mass $M$ at the origin on a mass $m$ is:

$$
\mathbf{F}(\mathbf{r}) = -\frac{GMm}{r^2}\,\hat{\mathbf{r}}
$$

Show that this force is conservative by finding its potential energy $U(r)$ referenced to zero at spatial infinity ($r_0 \to \infty$).

**Solution**:  
The force is purely radial, and the path element is $d\mathbf{r} = dr\,\hat{\mathbf{r}} + r\,d\theta\,\hat{\boldsymbol{\theta}} + r\sin\theta\,d\phi\,\hat{\boldsymbol{\phi}}$.  
Thus $\mathbf{F} \cdot d\mathbf{r} = F_r\,dr = -\frac{GMm}{r^2}\,dr$.  
By definition of potential energy:

$$
U(r) = - \int_{r_0}^r \mathbf{F} \cdot d\mathbf{r}' = - \int_\infty^r \left( -\frac{GMm}{(r')^2} \right) dr' = GMm \left[ -\frac{1}{r'} \right]_\infty^r = -\frac{GMm}{r}
$$

Check gradient:

$$
\mathbf{F} = -\frac{dU}{dr}\,\hat{\mathbf{r}} = -\frac{d}{dr}\left(-\frac{GMm}{r}\right)\hat{\mathbf{r}} = -\frac{GMm}{r^2}\,\hat{\mathbf{r}}
$$

Matches Newton's universal gravitational law exactly!

---

### Practice Problem 12.1 (To Solve)
**Statement**: Test whether the force $\mathbf{F} = y^2\,\hat{\mathbf{x}} + (2xy + z)\,\hat{\mathbf{y}} + y\,\hat{\mathbf{z}}$ is conservative. If conservative, find the potential energy $U(x, y, z)$ with $U(0, 0, 0) = 0$.
* **Hint**: Compute all 3 components of $\nabla \times \mathbf{F}$. If zero, integrate $\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}$.
* **Answer**: $(\nabla \times \mathbf{F})_x = 1 - 1 = 0$, $(\nabla \times \mathbf{F})_y = 0 - 0 = 0$, $(\nabla \times \mathbf{F})_z = 2y - 2y = 0$. The force is conservative! Potential energy: $U(x, y, z) = -x y^2 - y z$.

---

### Practice Problem 12.2 (To Solve)
**Statement**: Prove that any spherically symmetric central force $\mathbf{F}(\mathbf{r}) = f(r)\,\hat{\mathbf{r}}$ is conservative for any arbitrary continuous function $f(r)$.
* **Hint**: Show that $\hat{\mathbf{r}} \cdot d\mathbf{r} = dr$. Thus $\int_A^B \mathbf{F} \cdot d\mathbf{r} = \int_{r_A}^{r_B} f(r)\,dr$.
* **Answer**: Since the line integral depends only on the scalar limits $r_A$ and $r_B$, the work is completely independent of the angular trajectory taken.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 4:
  * Sections 4.2–4.5 (pp. 119–135): Conservative Forces, Potential Energy, Gradient Operator, Curl Test.
  * Problems 4.12, 4.18, 4.23 (pp. 165–168): Detailed curl proofs and potential derivations.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 14: "Work and Potential Energy (Conclusion)" (Sections 14.1–14.4 on conservative fields and curl).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 5: "Work and Energy" (Sections 5.4–5.7).\n