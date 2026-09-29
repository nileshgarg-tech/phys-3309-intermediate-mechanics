# 03. Curvilinear Kinematics & 2D Polar Coordinates

**Foundational Story**: Chapter 1, Sections 1.6–1.7  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 1 (pp. 23–35)
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 1 (pp. 27–38)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 11 ("Vectors")

---

## 1. Plane Polar Coordinates and Moving Unit Vectors

Any point $P$ in the $xy$-plane can be located by:
* $r$: Radial distance from the origin ($r \ge 0$).
* $\theta$: Counterclockwise angle from the positive $x$-axis.

We define two local orthonormal unit vectors:
1. $\hat{\mathbf{r}}$: Points radially outward from the origin.
2. $\hat{\boldsymbol{\theta}}$: Points in the direction of increasing $\theta$ (counterclockwise rotation).

Projecting onto the Cartesian basis:

$$
\hat{\mathbf{r}} = \cos\theta\,\hat{\mathbf{x}} + \sin\theta\,\hat{\mathbf{y}}
$$

$$
\hat{\boldsymbol{\theta}} = -\sin\theta\,\hat{\mathbf{x}} + \cos\theta\,\hat{\mathbf{y}}
$$

---

## 2. Time Derivatives of Moving Unit Vectors

Differentiating with respect to time using the chain rule:

$$
\frac{d\hat{\mathbf{r}}}{dt} = -\sin\theta\,\dot{\theta}\,\hat{\mathbf{x}} + \cos\theta\,\dot{\theta}\,\hat{\mathbf{y}} = \dot{\theta}\,\hat{\boldsymbol{\theta}}
$$

$$
\frac{d\hat{\boldsymbol{\theta}}}{dt} = -\cos\theta\,\dot{\theta}\,\hat{\mathbf{x}} - \sin\theta\,\dot{\theta}\,\hat{\mathbf{y}} = -\dot{\theta}\,\hat{\mathbf{r}}
$$

> **The Golden Kinematic Rules for Polar Unit Vectors**:
> 
> $$
> \frac{d\hat{\mathbf{r}}}{dt} = \dot{\theta}\,\hat{\boldsymbol{\theta}}, \qquad \frac{d\hat{\boldsymbol{\theta}}}{dt} = -\dot{\theta}\,\hat{\mathbf{r}}
> $$

---

## 3. Velocity in Polar Coordinates

Position is:

$$
\mathbf{r} = r\,\hat{\mathbf{r}}
$$

Differentiating with the product rule:

$$
\mathbf{v} = \frac{d\mathbf{r}}{dt} = \dot{r}\,\hat{\mathbf{r}} + r\frac{d\hat{\mathbf{r}}}{dt} = \dot{r}\,\hat{\mathbf{r}} + r\dot{\theta}\,\hat{\boldsymbol{\theta}}
$$

* **Radial velocity**: $v_r = \dot{r}$
* **Azimuthal velocity**: $v_\theta = r\dot{\theta}$
* **Speed squared**:

$$
v^2 = \dot{r}^2 + r^2\dot{\theta}^2
$$

---

## 4. Acceleration in Polar Coordinates (Step-by-Step)

Differentiating velocity with respect to time:

$$
\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}\left( \dot{r}\,\hat{\mathbf{r}} + r\dot{\theta}\,\hat{\boldsymbol{\theta}} \right)
$$

Applying the product rule to each term:

$$
\frac{d}{dt}(\dot{r}\,\hat{\mathbf{r}}) = \ddot{r}\,\hat{\mathbf{r}} + \dot{r}\dot{\theta}\,\hat{\boldsymbol{\theta}}
$$

$$
\frac{d}{dt}(r\dot{\theta}\,\hat{\boldsymbol{\theta}}) = (\dot{r}\dot{\theta} + r\ddot{\theta})\,\hat{\boldsymbol{\theta}} - r\dot{\theta}^2\,\hat{\mathbf{r}}
$$

Collecting terms:

$$
\mathbf{a} = \left( \ddot{r} - r\dot{\theta}^2 \right)\hat{\mathbf{r}} + \left( r\ddot{\theta} + 2\dot{r}\dot{\theta} \right)\hat{\boldsymbol{\theta}}
$$

### Physical Meaning of Acceleration Components:
* $-r\dot{\theta}^2$ (Centripetal Acceleration): Inward radial acceleration maintaining curved path.
* $r\ddot{\theta}$ (Tangential Acceleration): Caused by angular acceleration speeding up rotation.
* $2\dot{r}\dot{\theta}$ (Coriolis Acceleration): Cross-coupling between radial motion and coordinate rotation.

---

## 5. Summary Cheat Sheet for Module 03

| Vector | Polar Representation | Key Derivatives |
|---|---|---|
| **Unit Vectors** | $\hat{\mathbf{r}} = \cos\theta\hat{\mathbf{x}} + \sin\theta\hat{\mathbf{y}}$ | $\frac{d\hat{\mathbf{r}}}{dt} = \dot{\theta}\hat{\boldsymbol{\theta}}, \quad \frac{d\hat{\boldsymbol{\theta}}}{dt} = -\dot{\theta}\hat{\mathbf{r}}$ |
| **Position** | $\mathbf{r} = r\,\hat{\mathbf{r}}$ | Magnitude $r$, orientation $\theta$ |
| **Velocity** | $\mathbf{v} = \dot{r}\,\hat{\mathbf{r}} + r\dot{\theta}\,\hat{\boldsymbol{\theta}}$ | $v^2 = \dot{r}^2 + r^2\dot{\theta}^2$ |
| **Acceleration** | $\mathbf{a} = (\ddot{r} - r\dot{\theta}^2)\hat{\mathbf{r}} + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{\boldsymbol{\theta}}$ | Centripetal $-r\dot{\theta}^2$, Coriolis $2\dot{r}\dot{\theta}$ |
| **Central Force Form** | $F_\theta = \frac{m}{r}\frac{d}{dt}(r^2\dot{\theta})$ | When $F_\theta = 0$, $l = mr^2\dot{\theta} = \text{const}$ |

---

## 6. Worked Examples & Practice Problems

### Worked Example 3.1: Kinematics on an Archimedean Spiral
**Problem**: A particle moves outward along an Archimedean spiral:

$$
r(t) = bt, \qquad \theta(t) = \omega t
$$

Find the velocity and acceleration vectors, and identify each component.

**Solution**:
1. **Derivatives**:
   $\dot{r} = b, \quad \ddot{r} = 0$
   $\dot{\theta} = \omega, \quad \ddot{\theta} = 0$

2. **Velocity**:

$$
\mathbf{v}(t) = b\,\hat{\mathbf{r}} + b\omega t\,\hat{\boldsymbol{\theta}}
$$

$$
|\mathbf{v}| = \sqrt{b^2 + b^2\omega^2 t^2} = b\sqrt{1 + \omega^2 t^2}
$$

3. **Acceleration**:

$$
a_r = \ddot{r} - r\dot{\theta}^2 = 0 - (bt)\omega^2 = -b\omega^2 t \quad \text{(Centripetal)}
$$

$$
a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta} = 0 + 2(b)(\omega) = 2b\omega \quad \text{(Coriolis)}
$$

$$
\mathbf{a}(t) = (-b\omega^2 t)\,\hat{\mathbf{r}} + (2b\omega)\,\hat{\boldsymbol{\theta}}
$$

---

### Worked Example 3.2: The Conical Pendulum
**Problem**: A bob of mass $m$ hangs on a string of length $L$ making constant angle $\alpha$ with the vertical, revolving in a horizontal circle of radius $R = L\sin\alpha$. Find orbital speed and period.

**Solution**:
Here $r = R = \text{const}$, so $\dot{r} = 0, \ddot{r} = 0$.
Vertical equilibrium:

$$
T\cos\alpha = mg \implies T = \frac{mg}{\cos\alpha}
$$

Horizontal radial Newton's Second Law ($F_r = m a_r$):

$$
-T\sin\alpha = -mR\dot{\theta}^2
$$

$$
\left(\frac{mg}{\cos\alpha}\right)\sin\alpha = m(L\sin\alpha)\dot{\theta}^2 \implies \dot{\theta}^2 = \frac{g}{L\cos\alpha}
$$

Orbital period:

$$
\tau = \frac{2\pi}{\dot{\theta}} = 2\pi\sqrt{\frac{L\cos\alpha}{g}}
$$

---

### Practice Problem 3.1 (To Solve)
**Statement**: A bead slides along a frictionless rod rotating horizontally at constant angular speed $\omega$.
Show that $r(t) = r_0\cosh(\omega t)$ given $r(0) = r_0$ and $\dot{r}(0) = 0$.
* **Hint**: $F_r = 0 \implies \ddot{r} - \omega^2 r = 0$.
* **Answer**: $\ddot{r} - \omega^2 r = 0 \implies r(t) = r_0\cosh(\omega t)$.

---

### Practice Problem 3.2 (To Solve)
**Statement**: A particle moves in the plane with $r(t) = r_0 e^{kt}$ and $\theta(t) = ct$.
Show that the angle $\psi$ between the velocity vector and the radial direction is constant.
* **Hint**: $\tan\psi = v_\theta / v_r = (r\dot{\theta}) / \dot{r}$.
* **Answer**: $\tan\psi = (c r) / (k r) = c / k \implies \psi = \arctan(c / k) = \text{const}$.

---

## 7. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 1:
  * Sections 1.6–1.7 (pp. 23–35): 2D Polar Coordinates, Kinematics.
  * Problems 1.35, 1.40, 1.47 (pp. 40–42).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 1: "Vectors and Kinematics" (Sections 1.8–1.9).
