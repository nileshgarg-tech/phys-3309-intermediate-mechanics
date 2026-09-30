# 06. Quadratic Drag & Nonlinear Trajectories

**Foundational Story**: Chapter 2, Section 2.4  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 60–73)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 9 & Ch. 41

---

## 1. The Coupling Dilemma in 2D

With quadratic drag $\mathbf{f} = -c v \mathbf{v}$ (Taylor, Sec. 2.4, pp. 55–60):

$$
m\dot{v}_x = -c\sqrt{v_x^2 + v_y^2}\,v_x
$$

$$
m\dot{v}_y = -mg - c\sqrt{v_x^2 + v_y^2}\,v_y
$$

Because $v_x$ and $v_y$ are nonlinearly coupled through speed $v = \sqrt{v_x^2 + v_y^2}$, **no closed-form analytical solution exists in elementary functions for 2D quadratic drag**. Trajectories must be computed numerically.
However, **pure vertical 1D motion** can be solved analytically!

---

## 2. 1D Vertical Drop from Rest

Choosing $y$ downward so gravity is positive (Taylor, Eq. 2.44):

$$
m\dot{v} = mg - cv^2
$$

Terminal velocity occurs when acceleration vanishes ($\dot{v} = 0$, Taylor Eq. 2.45):

$$
v_{\text{ter}} = \sqrt{\frac{mg}{c}}
$$

Rewriting the ODE (Taylor, Eq. 2.47):

$$
\dot{v} = g\left[ 1 - \left(\frac{v}{v_{\text{ter}}}\right)^2 \right]
$$

Integrating using the substitution $\int \frac{du}{1 - u^2} = \text{arctanh}(u)$ (Taylor, Eq. 2.49):

$$
v(t) = v_{\text{ter}}\tanh\left(\frac{gt}{v_{\text{ter}}}\right) = v_{\text{ter}}\tanh\left(\frac{t}{\tau}\right)
$$

where $\tau = v_{\text{ter}} / g$.
Integrating velocity gives position (Taylor, Eq. 2.51):

$$
y(t) = \frac{v_{\text{ter}}^2}{g}\ln\left( \cosh\left(\frac{t}{\tau}\right) \right)
$$

---

## 3. Upward Launch with Quadratic Drag

For vertical launch upward with speed $v_0$ (Taylor, Eq. 2.54):

$$
m\dot{v} = -mg - cv^2 = -m g\left[ 1 + \left(\frac{v}{v_{\text{ter}}}\right)^2 \right]
$$

Using $\int \frac{du}{1 + u^2} = \arctan(u)$:

$$
v(t) = v_{\text{ter}}\tan\left[ \arctan\left(\frac{v_0}{v_{\text{ter}}}\right) - \frac{gt}{v_{\text{ter}}} \right]
$$

Maximum height reached:

$$
y_{\text{max}} = \frac{v_{\text{ter}}^2}{2g}\ln\left( 1 + \frac{v_0^2}{v_{\text{ter}}^2} \right)
$$

Time to peak:

$$
t_{\text{top}} = \frac{v_{\text{ter}}}{g}\arctan\left(\frac{v_0}{v_{\text{ter}}}\right)
$$

---

## 4. Summary Cheat Sheet for Module 06

| Situation | Formula | Meaning |
|---|---|---|
| **Terminal Speed** | $v_{\text{ter}} = \sqrt{\frac{mg}{c}}$ | Equilibrium where drag equals weight |
| **Drop Velocity** | $v(t) = v_{\text{ter}}\tanh(t/\tau)$ | Hyperbolic velocity buildup |
| **Drop Distance** | $y(t) = \frac{v_{\text{ter}}^2}{g}\ln(\cosh(t/\tau))$ | Asymptotic linear displacement $v_{\text{ter}}t$ |
| **Maximum Height** | $y_{\text{max}} = \frac{v_{\text{ter}}^2}{2g}\ln(1 + v_0^2/v_{\text{ter}}^2)$ | Drag reduces peak altitude |

---

## 5. Worked Examples & Practice Problems

### Worked Example 6.1: Skydiver Terminal Drop
**Problem**: An $80\text{ kg}$ skydiver has $v_{\text{ter}} = 56\text{ m/s}$ ($c = 0.25\text{ N}\cdot\text{s}^2\text{/m}^2$).
Find speed and distance fallen after $t = 5.0\text{ s}$.

**Solution**:
Characteristic time: $\tau = v_{\text{ter}} / g = 56.0 / 9.8 \approx 5.71\text{ s}$.
Speed at $t = 5.0\text{ s}$:

$$
v(5) = 56.0\tanh(5.0 / 5.71) = 56.0\tanh(0.875) \approx 56.0(0.704) \approx 39.4\text{ m/s}
$$

Distance fallen:

$$
y(5) = \frac{56.0^2}{9.8}\ln(\cosh(0.875)) = 320\ln(1.408) \approx 320(0.342) \approx 109.4\text{ meters}
$$

---

## 6. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 2:
  * Section 2.4 (pp. 60–73).
  * Problems 2.20, 2.24, 2.28 (pp. 76–78).
