# 03. Curvilinear Kinematics & 2D Polar Coordinates

**Foundational Story**: Chapter 1, Sections 1.6–1.7  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 1 (pp. 23–35)
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 1 (pp. 27–38)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 11 ("Vectors")

---

## 1. Plane Polar Coordinates and Moving Unit Vectors

In *Classical Mechanics* (Section 1.7), John R. Taylor designates the 2D plane polar coordinates of any point $P$ in the $xy$-plane as $(r, \phi)$:
* $r$: Radial distance from the origin ($r \ge 0$).
* $\phi$: Azimuthal angle measured counterclockwise up from the positive $x$-axis.

> [!NOTE]
> **Taylor's Notation Convention**:  
> Taylor explicitly uses $\phi$ (rather than $\theta$) for plane polar coordinates so that it maps consistently onto spherical polar coordinates $(r, \theta, \phi)$ in Chapter 4 and Chapter 8, where $\phi$ is the azimuthal angle in the $xy$-plane and $\theta$ is the polar angle down from the $z$-axis.

The transformation between Cartesian and polar coordinates is:

$$
x = r\cos\phi, \qquad y = r\sin\phi
$$

$$
r = \sqrt{x^2 + y^2}, \qquad \phi = \arctan(y/x)
$$

We introduce two local orthonormal unit vectors:
1. $\hat{\mathbf{r}}$: Points in the direction of increasing $r$ with $\phi$ fixed (radially outward).
2. $\hat{\boldsymbol{\phi}}$: Points in the direction of increasing $\phi$ with $r$ fixed (tangentially counterclockwise).

Projecting onto the Cartesian basis ($\hat{\mathbf{x}}, \hat{\mathbf{y}}$):

$$
\hat{\mathbf{r}} = \cos\phi \hat{\mathbf{x}} + \sin\phi \hat{\mathbf{y}}
$$

$$
\hat{\boldsymbol{\phi}} = -\sin\phi \hat{\mathbf{x}} + \cos\phi \hat{\mathbf{y}}
$$

Unlike the constant Cartesian unit vectors ($\dot{\hat{\mathbf{x}}} = \mathbf{0}, \dot{\hat{\mathbf{y}}} = \mathbf{0}$), the polar unit vectors **change their spatial directions as the particle moves**!

---

## 2. Time Derivatives of Moving Unit Vectors

Differentiating with respect to time using the chain rule:

$$
\frac{d\hat{\mathbf{r}}}{dt} = \frac{d}{dt}(\cos\phi \hat{\mathbf{x}} + \sin\phi \hat{\mathbf{y}}) = -\sin\phi \dot{\phi} \hat{\mathbf{x}} + \cos\phi \dot{\phi} \hat{\mathbf{y}} = \dot{\phi} \hat{\boldsymbol{\phi}}
$$

$$
\frac{d\hat{\boldsymbol{\phi}}}{dt} = \frac{d}{dt}(-\sin\phi \hat{\mathbf{x}} + \cos\phi \hat{\mathbf{y}}) = -\cos\phi \dot{\phi} \hat{\mathbf{x}} - \sin\phi \dot{\phi} \hat{\mathbf{y}} = -\dot{\phi} \hat{\mathbf{r}}
$$

> **Taylor's Fundamental Derivative Rules for Polar Unit Vectors** (Taylor eq. 1.42 & 1.46):
> 
> $$
> \frac{d\hat{\mathbf{r}}}{dt} = \dot{\phi} \hat{\boldsymbol{\phi}} \qquad \text{and} \qquad \frac{d\hat{\boldsymbol{\phi}}}{dt} = -\dot{\phi} \hat{\mathbf{r}}
> $$

---

## 3. Velocity in Polar Coordinates

In polar coordinates, the position vector from the origin to particle $P$ is remarkably compact:

$$
\mathbf{r} = r \hat{\mathbf{r}}
$$

Differentiating with the product rule:

$$
\mathbf{v} = \dot{\mathbf{r}} = \frac{d}{dt}(r \hat{\mathbf{r}}) = \dot{r} \hat{\mathbf{r}} + r\frac{d\hat{\mathbf{r}}}{dt} = \dot{r} \hat{\mathbf{r}} + r\dot{\phi} \hat{\boldsymbol{\phi}}
$$

Reading off the polar components of velocity (Taylor eq. 1.43–1.44):
* **Radial velocity component**: $v_r = \dot{r}$
* **Tangential (azimuthal) velocity component**: $v_\phi = r\dot{\phi} = r\omega$ (where $\omega = \dot{\phi}$ is angular velocity)
* **Speed squared**:

$$
v^2 = |\mathbf{v}|^2 = \dot{r}^2 + r^2\dot{\phi}^2
$$

---

## 4. Acceleration in Polar Coordinates (Taylor Section 1.7)

Differentiating velocity with respect to time:

$$
\mathbf{a} = \dot{\mathbf{v}} = \frac{d}{dt}\left( \dot{r} \hat{\mathbf{r}} + r\dot{\phi} \hat{\boldsymbol{\phi}} \right)
$$

Applying the product rule term by term:

$$
\frac{d}{dt}(\dot{r} \hat{\mathbf{r}}) = \ddot{r} \hat{\mathbf{r}} + \dot{r}\frac{d\hat{\mathbf{r}}}{dt} = \ddot{r} \hat{\mathbf{r}} + \dot{r}\dot{\phi} \hat{\boldsymbol{\phi}}
$$

$$
\frac{d}{dt}(r\dot{\phi} \hat{\boldsymbol{\phi}}) = \dot{r}\dot{\phi} \hat{\boldsymbol{\phi}} + r\ddot{\phi} \hat{\boldsymbol{\phi}} + r\dot{\phi}\frac{d\hat{\boldsymbol{\phi}}}{dt} = \dot{r}\dot{\phi} \hat{\boldsymbol{\phi}} + r\ddot{\phi} \hat{\boldsymbol{\phi}} - r\dot{\phi}^2 \hat{\mathbf{r}}
$$

Collecting terms along $\hat{\mathbf{r}}$ and $\hat{\boldsymbol{\phi}}$ (Taylor eq. 1.47):

$$
\mathbf{a} = \left( \ddot{r} - r\dot{\phi}^2 \right)\hat{\mathbf{r}} + \left( r\ddot{\phi} + 2\dot{r}\dot{\phi} \right)\hat{\boldsymbol{\phi}}
$$

### Physical Breakdown of the Four Terms:
1. **$\ddot{r}$**: Direct linear radial acceleration (speeding up or slowing down radially).
2. **$-r\dot{\phi}^2 = -r\omega^2 = -v_\phi^2 / r$ (Centripetal Acceleration)**: Inward radial acceleration required to bend the velocity vector into a curved path.
3. **$r\ddot{\phi} = r\alpha$ (Tangential Acceleration)**: Azimuthal acceleration caused by angular acceleration $\alpha = \ddot{\phi}$.
4. **$2\dot{r}\dot{\phi}$ (Coriolis Acceleration)**: The kinematic cross-term arising because radial motion brings the particle to a radius with a different tangential coordinate speed.

---

## 5. Newton's Second Law in Polar Coordinates

Resolving $\mathbf{F} = m\mathbf{a}$ into polar components (Taylor eq. 1.48):

$$
\begin{cases}
F_r = m\left(\ddot{r} - r\dot{\phi}^2\right) \\[8pt]
F_\phi = m\left(r\ddot{\phi} + 2\dot{r}\dot{\phi}\right) = \dfrac{m}{r}\dfrac{d}{dt}\left(r^2\dot{\phi}\right)
\end{cases}
$$

Notice the remarkable identity for the azimuthal equation:
$$\frac{1}{r}\frac{d}{dt}(r^2\dot{\phi}) = \frac{1}{r}(2r\dot{r}\dot{\phi} + r^2\ddot{\phi}) = r\ddot{\phi} + 2\dot{r}\dot{\phi}$$
This reveals that if there is zero tangential force ($F_\phi = 0$, as in any central force like planetary gravity), the quantity $m r^2 \dot{\phi} = \ell$ (angular momentum) is strictly constant!

---

## 6. Summary Cheat Sheet for Module 03

| Quantity | Taylor's Notation | Mathematical Expression | Physical Interpretation |
|---|---|---|---|
| **Coordinates** | $(r, \phi)$ | $x = r\cos\phi, \quad y = r\sin\phi$ | Radius and azimuthal angle |
| **Unit Vectors** | $\hat{\mathbf{r}}, \hat{\boldsymbol{\phi}}$ | $\hat{\mathbf{r}} = \cos\phi\hat{\mathbf{x}} + \sin\phi\hat{\mathbf{y}}$ | Local moving basis vectors |
| **Unit Derivatives** | $\dot{\hat{\mathbf{r}}}, \dot{\hat{\boldsymbol{\phi}}}$ | $\frac{d\hat{\mathbf{r}}}{dt} = \dot{\phi}\hat{\boldsymbol{\phi}}, \quad \frac{d\hat{\boldsymbol{\phi}}}{dt} = -\dot{\phi}\hat{\mathbf{r}}$ | Rotate as particle moves |
| **Position** | $\mathbf{r}$ | $\mathbf{r} = r \hat{\mathbf{r}}$ | Radial vector |
| **Velocity** | $\mathbf{v}$ | $\mathbf{v} = \dot{r} \hat{\mathbf{r}} + r\dot{\phi} \hat{\boldsymbol{\phi}}$ | $v_r = \dot{r}, \quad v_\phi = r\dot{\phi} = r\omega$ |
| **Speed Squared** | $v^2$ | $v^2 = \dot{r}^2 + r^2\dot{\phi}^2$ | Metric in polar coordinates |
| **Acceleration** | $\mathbf{a}$ | $\mathbf{a} = (\ddot{r} - r\dot{\phi}^2)\hat{\mathbf{r}} + (r\ddot{\phi} + 2\dot{r}\dot{\phi})\hat{\boldsymbol{\phi}}$ | Centripetal $-r\dot{\phi}^2$, Coriolis $2\dot{r}\dot{\phi}$ |
| **Azimuthal Law** | $F_\phi$ | $F_\phi = \frac{m}{r}\frac{d}{dt}(r^2\dot{\phi})$ | Conservation of $\ell = mr^2\dot{\phi}$ when $F_\phi = 0$ |

---

## 7. Worked Examples & Practice Problems

### Worked Example 3.1: Kinematics on an Archimedean Spiral
**Problem**: A particle moves outward along an Archimedean spiral:

$$
r(t) = bt, \qquad \phi(t) = \omega t
$$

Find the velocity and acceleration vectors, and identify each component in Taylor's notation.

**Solution**:
1. **Derivatives**:
   $\dot{r} = b, \quad \ddot{r} = 0$  
   $\dot{\phi} = \omega, \quad \ddot{\phi} = 0$

2. **Velocity**:

$$
\mathbf{v}(t) = \dot{r} \hat{\mathbf{r}} + r\dot{\phi} \hat{\boldsymbol{\phi}} = b \hat{\mathbf{r}} + b\omega t \hat{\boldsymbol{\phi}}
$$

$$
|\mathbf{v}| = \sqrt{b^2 + b^2\omega^2 t^2} = b\sqrt{1 + \omega^2 t^2}
$$

3. **Acceleration**:

$$
a_r = \ddot{r} - r\dot{\phi}^2 = 0 - (bt)\omega^2 = -b\omega^2 t \quad \text{(Centripetal)}
$$

$$
a_\phi = r\ddot{\phi} + 2\dot{r}\dot{\phi} = 0 + 2(b)(\omega) = 2b\omega \quad \text{(Coriolis)}
$$

$$
\mathbf{a}(t) = (-b\omega^2 t)\hat{\mathbf{r}} + (2b\omega)\hat{\boldsymbol{\phi}}
$$

---

### Worked Example 3.2: The Conical Pendulum
**Problem**: A bob of mass $m$ hangs on a string of length $L$ making constant angle $\alpha$ with the vertical, revolving in a horizontal circle of radius $R = L\sin\alpha$. Find the orbital speed and period.

**Solution**:
Here $r = R = \text{const}$, so $\dot{r} = 0, \ddot{r} = 0$. Let the azimuthal angle be $\phi(t)$ with angular speed $\dot{\phi} = \omega$.  
Vertical equilibrium:

$$
T\cos\alpha = mg \implies T = \frac{mg}{\cos\alpha}
$$

Horizontal radial Newton's Second Law ($F_r = m a_r$ where $a_r = -R\dot{\phi}^2$):

$$
-T\sin\alpha = -mR\dot{\phi}^2
$$

$$
\left(\frac{mg}{\cos\alpha}\right)\sin\alpha = m(L\sin\alpha)\dot{\phi}^2 \implies \dot{\phi}^2 = \frac{g}{L\cos\alpha}
$$

Orbital period:

$$
\tau = \frac{2\pi}{\dot{\phi}} = 2\pi\sqrt{\frac{L\cos\alpha}{g}}
$$

---

### Practice Problem 3.1 (To Solve)
**Statement**: A bead slides along a frictionless rod rotating horizontally at constant angular speed $\omega$ ($\dot{\phi} = \omega$).  
Show that $r(t) = r_0\cosh(\omega t)$ given $r(0) = r_0$ and $\dot{r}(0) = 0$.
* **Hint**: $F_r = 0 \implies \ddot{r} - r\omega^2 = 0$.
* **Answer**: $\ddot{r} - \omega^2 r = 0 \implies r(t) = r_0\cosh(\omega t)$.

---

### Practice Problem 3.2 (To Solve)
**Statement**: A particle moves in the plane with $r(t) = r_0 e^{kt}$ and $\phi(t) = ct$.  
Show that the angle $\psi$ between the velocity vector and the radial direction is constant.
* **Hint**: $\tan\psi = v_\phi / v_r = (r\dot{\phi}) / \dot{r}$.
* **Answer**: $\tan\psi = (c r) / (k r) = c / k \implies \psi = \arctan(c / k) = \text{const}$.

---

## 8. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 1:
  * Section 1.7 (pp. 26–35): Two-Dimensional Polar Coordinates, Kinematics, eq. (1.37)–(1.48).
  * Problems 1.41–1.48 (pp. 41–42).
