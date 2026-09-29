# 04. Air Resistance: Linear vs. Quadratic Drag

**Foundational Story**: Chapter 2, Section 2.1  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 2 (pp. 43–48)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 41 ("The Flow of Wet Water")
* Purcell, *Life at Low Reynolds Number* (American Journal of Physics)

---

## 1. The Real-World Illusion: The Vacuum Fallacy

Introductory physics routinely begins with the caveat: *"neglecting air resistance"*. 
In a pure vacuum:
* A cannonball and a goose feather fall at identical rates ($g = 9.8\text{ m/s}^2$).
* Projectile trajectories are symmetric parabolas extending indefinitely as launch speed increases.

In the real atmosphere, however, drag forces dominate high-speed motion:
* A skydiver in free-fall does not accelerate forever; they reach a terminal velocity of roughly 120 mph (54 m/s).
* A driven baseball flies along an asymmetric trajectory: the descent is steeper and shorter than the ascent.
* Raindrops hit the ground at 10–20 mph instead of bullet-like speeds of hundreds of miles per hour.

---

## 2. The Microscopic Origins of Drag

When an object of diameter $D$ moves through a fluid of density $\rho$ and viscosity $\eta$ at velocity $v$, it experiences a retarding force opposing its velocity:
```
f(v) = -f(v) * v_hat
```
Taylor explains that for an enormous range of practical speeds, the magnitude of the drag force can be modeled as the sum of two terms:
```
f(v) = f_lin + f_quad = b*v + c*v²
```

### The Linear Term: Viscous Shear (Stokes' Drag)
```
f_lin = b * v
```
* **Origin**: As the object glides forward, the thin layer of fluid directly in contact with its surface sticks to it (the "no-slip" boundary condition). Neighboring fluid layers slide past one another. The internal friction (viscosity $\eta$) between these sliding fluid layers resists motion.
* For a sphere of diameter $D$, George Stokes famously derived:
  ```
  b = 3 * π * η * D = β * D
  ```
  In air at standard temperature and pressure: $\beta \approx 1.6 \times 10^{-4}\text{ N}\cdot\text{s/m}^2$.

### The Quadratic Term: Turbulent Pressure Drag
```
f_quad = c * v²
```
* **Origin**: At higher speeds, the fluid cannot smoothly flow around the body and close behind it. The fluid separates from the surface, creating a chaotic, low-pressure turbulent wake trailing the object.
* The body must literally shovel away mass. The mass of air accelerated out of the path per second is proportional to $\rho \cdot A \cdot v$. Multiplying this mass flow rate by the velocity imparted ($v$) yields a drag force scaling as $v^2$:
  ```
  f_quad = (1/2) * C_D * ρ * A * v² = c * v²
  ```
  *(where $C_D$ is the dimensionless drag coefficient, typically $\sim 0.5$ for spheres, and $A = \pi D^2 / 4$ is cross-sectional area)*.
* In air: $c = \gamma \cdot D^2$, where $\gamma \approx 0.25\text{ N}\cdot\text{s}^2\text{/m}^4$.

---

## 3. Which Force Wins? The Reynolds Number

To determine whether linear or quadratic drag dominates in any given physical problem, we compare their ratio:
```
f_quad / f_lin = (c * v²) / (b * v) = (c / b) * v = (γ / β) * D * v
```
Using the atmospheric constants:
```
f_quad / f_lin ≈ (0.25 / 1.6e-4) * D * v ≈ 1.6 x 10³ * D * v   (in SI units)
```
Fluid dynamicists formalize this ratio as the dimensionless **Reynolds Number** ($R$):
```
R = (ρ * D * v) / η
```
* **Low Reynolds Number ($R \ll 1$)**: Viscous forces dominate. Motion is smooth and laminar. Linear Stokes drag applies.
* **High Reynolds Number ($R \gg 1000$)**: Inertial and turbulent forces dominate. Viscous skin friction is negligible compared to the turbulent wake. Quadratic drag applies.

---

## 4. Real-World Crossover Scales

Let us compute the ratio for three familiar objects in air:

1. **A Baseballs ($D \approx 7\text{ cm} = 0.07\text{ m}$, $v \approx 20\text{ m/s}$)**:
   ```
   f_quad / f_lin ≈ 1.6e3 * (0.07) * (20) ≈ 2,240
   ```
   **Quadratic drag dominates by more than 2,000 to 1!** Linear drag can be completely ignored.

2. **A Raindrop ($D \approx 1\text{ mm} = 10^{-3}\text{ m}$, $v \approx 5\text{ m/s}$)**:
   ```
   f_quad / f_lin ≈ 1.6e3 * (10^-3) * (5) ≈ 8
   ```
   Both terms contribute, but quadratic drag is still primary.

3. **A Tiny Dust Particle / Oil Droplet ($D \approx 10^{-6}\text{ m}$, $v \approx 1\text{ mm/s} = 10^{-3}\text{ m/s}$)**:
   ```
   f_quad / f_lin ≈ 1.6e3 * (10^-6) * (10^-3) ≈ 1.6 x 10^-6
   ```
   **Linear drag dominates by a factor of 600,000!** (This is the physics behind Millikan's Oil Drop Experiment).

---

## 5. Summary Cheat Sheet for Module 04

| Drag Type | Force Formula | Physics Mechanism | Dominant Regime |
|---|---|---|---|
| **Linear Drag** | `f_lin = b * v` | Viscous shearing of laminar fluid layers | Microscopic objects, low speeds, thick liquids ($R \ll 1$) |
| **Quadratic Drag**| `f_quad = c * v²` | Pushing fluid mass aside; turbulent trailing wake | Macroscopic projectiles, sports balls, vehicles ($R \gg 1000$) |
| **Ratio** | `f_quad / f_lin ≈ 1600 * D * v` | Compares inertial to viscous forces | Crossover occurs at `D * v ≈ 6 x 10^-4 m²/s` |
