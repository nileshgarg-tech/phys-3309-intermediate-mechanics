# 07. Charged Particles in B Fields & Complex Exponentials

**Foundational Story**: Chapter 2, Sections 2.5–2.7  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 73–84)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 22 & Vol. 2, Ch. 29

---

## 1. The Lorentz Force in a Uniform B Field

For a charge $q$ moving in a uniform magnetic field $\mathbf{B} = B\hat{\mathbf{z}}$ (Taylor, Eq. 2.65):

$$
m\dot{\mathbf{v}} = q(\mathbf{v} \times \mathbf{B})
$$

Component equations (Taylor, Eq. 2.67):

$$
m\dot{v}_x = q B v_y
$$

$$
m\dot{v}_y = -q B v_x
$$

$$
m\dot{v}_z = 0 \implies v_z(t) = \text{constant}
$$

---

## 2. Cyclotron Frequency & The Complex Velocity

Define the **cyclotron frequency** (Taylor, Eq. 2.68):

$$
\omega = \frac{qB}{m}
$$

Following Taylor (Sec. 2.5), define the **complex velocity**:

$$
\eta = v_x + i v_y \qquad (i^2 = -1)
$$

Differentiating $\eta$ with respect to time:

$$
\dot{\eta} = \dot{v}_x + i\dot{v}_y = \omega v_y - i\omega v_x = -i\omega(v_x + i v_y) = -i\omega\eta
$$

The two coupled real equations collapse into a single 1st-order complex ODE (Taylor, Eq. 2.70):

$$
\dot{\eta} = -i\omega\eta
$$

General solution:

$$
\eta(t) = v_{\text{tr}} e^{-i(\omega t - \delta)}
$$

where $v_{\text{tr}}$ is transverse speed. Using Euler's formula $e^{-i\theta} = \cos\theta - i\sin\theta$:

$$
v_x(t) = v_{\text{tr}}\cos(\omega t - \delta)
$$

$$
v_y(t) = -v_{\text{tr}}\sin(\omega t - \delta)
$$

---

## 3. Helical Motion & The Larmor Radius

Integrating velocities yields:

$$
(x - X_0)^2 + (y - Y_0)^2 = r_L^2
$$

where the **Larmor Radius** is:

$$
r_L = \frac{v_{\text{tr}}}{\omega} = \frac{m v_{\text{tr}}}{qB}
$$

Combined with uniform motion along $z$ ($z(t) = z_0 + v_{z0}t$), the particle executes a **helix**.

---

## 4. Summary Cheat Sheet for Module 07

| Concept | Mathematical Form | Meaning |
|---|---|---|
| **Cyclotron Frequency** | $\omega = \frac{qB}{m}$ | Gyration frequency |
| **Complex ODE** | $\dot{\eta} = -i\omega\eta$ | Unifies 2D vector kinematics |
| **Larmor Radius** | $r_L = \frac{mv_{\text{tr}}}{qB}$ | Orbit radius in $xy$-plane |
| **E x B Drift** | $\mathbf{v}_d = \frac{\mathbf{E} \times \mathbf{B}}{B^2}$ | Constant drift velocity |

---

## 5. Worked Examples & Practice Problems

### Worked Example 7.1: Proton Cyclotron Frequency
**Problem**: A proton ($m = 1.67 \times 10^{-27}\text{ kg}$, $q = 1.60 \times 10^{-19}\text{ C}$) enters $B = 1.50\text{ T}$ at $v = 3.0 \times 10^7\text{ m/s}$. Find frequency $f$ and radius $r_L$.

**Solution**:

$$
\omega = \frac{qB}{m} = \frac{(1.60 \times 10^{-19})(1.50)}{1.67 \times 10^{-27}} \approx 1.437 \times 10^8\text{ rad/s}
$$

$$
f = \frac{\omega}{2\pi} \approx 22.9\text{ MHz}
$$

$$
r_L = \frac{v}{\omega} = \frac{3.0 \times 10^7}{1.437 \times 10^8} \approx 0.209\text{ meters}
$$

---

## 6. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 2:
  * Sections 2.5–2.7 (pp. 73–84).
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1, Ch. 22 & Vol. 2, Ch. 29.
