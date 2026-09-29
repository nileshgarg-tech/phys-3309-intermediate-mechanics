# 04. Air Resistance: Linear vs. Quadratic Drag

**Foundational Story**: Chapter 2, Section 2.1  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 43–48)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 41 ("The Flow of Wet Water")
* Purcell, *Life at Low Reynolds Number* (American Journal of Physics)

---

## 1. The Microscopic Origins of Drag

When an object of diameter $D$ moves through a fluid of density $\rho$ and viscosity $\eta$ at velocity $\mathbf{v}$, it experiences a retarding force opposing its motion:

$$
\mathbf{f}(\mathbf{v}) = -f(v)\,\hat{\mathbf{v}}
$$

For an enormous range of practical speeds, the magnitude of the drag force can be modeled as the sum of linear and quadratic components:

$$
f(v) = f_{\text{lin}} + f_{\text{quad}} = bv + cv^2
$$

### The Linear Term: Viscous Shear (Stokes' Drag)

$$
f_{\text{lin}} = bv
$$

* **Physical Origin**: Arises from direct viscous friction between sliding fluid layers in laminar flow (no-slip boundary layer).
* For a sphere of diameter $D$ in a medium of dynamic viscosity $\eta$:

$$
b = 3\pi\eta D = \beta D
$$

In air at STP, $\beta \approx 1.6 \times 10^{-4}\text{ N}\cdot\text{s/m}^2$.

### The Quadratic Term: Turbulent Pressure Drag

$$
f_{\text{quad}} = cv^2
$$

* **Physical Origin**: Arises from accelerating fluid mass out of the path, leaving a low-pressure turbulent wake trailing the projectile.

$$
f_{\text{quad}} = \frac{1}{2} C_D \rho A v^2 = cv^2
$$

where $C_D$ is the dimensionless drag coefficient and $A = \pi D^2 / 4$.
In air at STP, $c = \gamma D^2$, where $\gamma \approx 0.25\text{ N}\cdot\text{s}^2\text{/m}^4$.

---

## 2. The Reynolds Number & Force Ratio

Comparing the two drag terms:

$$
\frac{f_{\text{quad}}}{f_{\text{lin}}} = \frac{cv^2}{bv} = \frac{\gamma}{\beta}Dv \approx 1.6 \times 10^3\, Dv \quad \text{(in SI units)}
$$

In fluid mechanics, this ratio is characterized by the dimensionless **Reynolds Number** ($R$):

$$
R = \frac{\rho D v}{\eta}
$$

* **$R \ll 1$**: Viscous laminar flow dominates. Stokes' linear drag applies.
* **$R \gg 1000$**: Inertial turbulent wake dominates. Quadratic drag applies.

---

## 3. Summary Cheat Sheet for Module 04

| Drag Type | Force Formula | Physics Mechanism | Dominant Regime |
|---|---|---|---|
| **Linear Drag** | $f_{\text{lin}} = bv$ | Viscous shearing of laminar fluid layers | Microscopic objects, low speeds, thick liquids ($R \ll 1$) |
| **Quadratic Drag**| $f_{\text{quad}} = cv^2$ | Pushing fluid mass aside; turbulent trailing wake | Macroscopic projectiles, sports balls, vehicles ($R \gg 1000$) |
| **Ratio** | $\frac{f_{\text{quad}}}{f_{\text{lin}}} \approx 1600\,Dv$ | Compares inertial to viscous forces | Crossover occurs at $Dv \approx 6 \times 10^{-4}\text{ m}^2\text{/s}$ |

---

## 4. Worked Examples & Practice Problems

### Worked Example 4.1: Reynolds Number Comparison
**Problem**: Calculate the ratio $f_{\text{quad}} / f_{\text{lin}}$ in air for:
(a) A regulation baseball ($D = 0.074\text{ m}$) thrown at $v = 40\text{ m/s}$ (90 mph).
(b) A tiny mist droplet ($D = 10\,\mu\text{m} = 10^{-5}\text{ m}$) settling at $v = 1\text{ mm/s} = 10^{-3}\text{ m/s}$.

**Solution**:
Using $\frac{f_{\text{quad}}}{f_{\text{lin}}} \approx 1560\,Dv$:
(a) For the baseball:

$$
\frac{f_{\text{quad}}}{f_{\text{lin}}} \approx 1560(0.074\text{ m})(40\text{ m/s}) \approx 4,618
$$

Quadratic drag dominates by more than **4,600 to 1**!

(b) For the mist droplet:

$$
\frac{f_{\text{quad}}}{f_{\text{lin}}} \approx 1560(10^{-5}\text{ m})(10^{-3}\text{ m/s}) \approx 1.56 \times 10^{-5}
$$

Linear drag dominates by a factor of **64,000 to 1**!

---

### Worked Example 4.2: Coasting Distance with Quadratic Drag
**Problem**: A cyclist of mass $m = 75\text{ kg}$ coasts on a level road with quadratic drag $c = 0.20\text{ N}\cdot\text{s}^2\text{/m}^2$. Initial speed is $v_0 = 15\text{ m/s}$. Find distance $x$ to slow down to $v = 5\text{ m/s}$.

**Solution**:

$$
m v \frac{dv}{dx} = -cv^2 \implies m\frac{dv}{dx} = -cv
$$

$$
\int_{v_0}^v \frac{1}{v'}\,dv' = -\frac{c}{m}\int_0^x dx' \implies \ln\left(\frac{v}{v_0}\right) = -\frac{c}{m}x
$$

$$
x = \frac{m}{c}\ln\left(\frac{v_0}{v}\right) = \frac{75}{0.20}\ln\left(\frac{15}{5}\right) = 375\ln(3) \approx 412\text{ meters}
$$

---

### Practice Problem 4.1 (To Solve)
**Statement**: Find the critical diameter $D_{\text{crit}}$ at which linear and quadratic drag forces are exactly equal at $v = 1\text{ m/s}$ in air.
* **Hint**: Set $f_{\text{lin}} = f_{\text{quad}} \implies \beta D = \gamma D^2 v$.
* **Answer**: $D_{\text{crit}} = \frac{\beta}{\gamma v} \approx \frac{1.6 \times 10^{-4}}{0.25(1.0)} \approx 0.64\text{ mm}$.

---

## 5. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 2:
  * Section 2.1 (pp. 43–48): Air Resistance, Linear vs. Quadratic Drag.
  * Problems 2.1, 2.4, 2.6 (pp. 73–74).
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 41: "The Flow of Wet Water" (Section 41.1).
