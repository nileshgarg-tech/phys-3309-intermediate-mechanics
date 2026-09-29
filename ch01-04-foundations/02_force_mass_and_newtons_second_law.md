# 02. Force, Mass, and Newton's Second & Third Laws

**Foundational Story**: Chapter 1, Sections 1.3–1.5  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 1 (pp. 11–23)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 9 ("Newton's Laws of Dynamics") & Ch. 11 ("Vectors")
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 2 ("Newton's Laws")

---

## 1. The Operational Definition of Mass via Collisions

Ernst Mach and later Robert Woodhouse provided the operational definition that rescues Newtonian mechanics from circularity:

Imagine two isolated particles, Particle 1 and Particle 2, floating in deep space with zero external forces acting on them. We allow them to interact—perhaps by a compressed spring between them, or an elastic collision.

Experimentally, we measure their instantaneous accelerations `a_1` and `a_2`. We discover two universal facts:
1. Their accelerations are always directed in opposite directions:
   ```
   a_1 is anti-parallel to a_2
   ```
2. The ratio of their acceleration magnitudes is strictly constant:
   ```
   |a_1| / |a_2| = constant
   ```

We define this constant as the ratio of their **inertial masses**:
```
m_2 / m_1 = |a_1| / |a_2|
```
**Mass is an intrinsic, scalar property of matter that quantifies its inertial reluctance to change velocity.**

---

## 2. Momentum and Newton's Second Law

Linear momentum is defined as:
```
p = m * v = m * (dr/dt)
```
Newton's Second Law is fundamentally a statement about momentum:
> **The time rate of change of momentum of a body is proportional to and in the direction of the net external impressed force:**
> ```
> F_net = dp/dt
> ```

For a body with constant mass $m$:
```
F_net = d(m*v)/dt = m * (dv/dt) = m * (d²r/dt²) = m * a
```

### Second-Order Differential Equation
Because acceleration is the second time derivative of position, Newton's second law is a system of second-order differential equations:
```
m * (d²r/dt²) = F(r, dr/dt, t)
```
To solve for the trajectory $r(t)$ uniquely, mathematics requires **two initial boundary conditions**:
1. Initial position: `r(0) = r_0`
2. Initial velocity: `v(0) = v_0`

---

## 3. Newton's Third Law & Conservation of Momentum

Newton's Third Law states:
```
F_12 = - F_21
```
Let us define the **Total Linear Momentum** of a two-particle isolated system:
```
P_total = p_1 + p_2
```
Taking the time derivative:
```
dP_total / dt = dp_1/dt + dp_2/dt = F_12 + F_21 = 0
```
Therefore:
```
P_total = constant
```
> **The Principle of Conservation of Linear Momentum**:
> **If the net external force on a system of particles is zero, the total linear momentum of the system remains strictly constant for all time.**
> (In Chapter 7, Noether's Theorem will reveal that linear momentum is conserved because space is homogeneous under spatial translations).

---

## 4. Summary Cheat Sheet for Module 02

| Concept | Formula | Core Takeaway |
|---|---|---|
| **Operational Mass** | `m_2 / m_1 = |a_1| / |a_2|` | Defined by mutually interacting acceleration ratios |
| **Linear Momentum** | `p = m * v` | Vector quantity of motion |
| **Newton's 2nd Law** | `F = dp/dt = m*d²r/dt²` | 2nd-order ODE; requires `r_0` and `v_0` to solve |
| **Newton's 3rd Law** | `F_12 = -F_21` | Mutual forces are equal and opposite |
| **Momentum Conservation**| `dP/dt = F_ext = 0` | Direct consequence of the 3rd Law |


---

## 5. Worked Examples & Practice Problems

### Worked Example 2.1: Operational Mass Ratio on an Air Track
**Problem**: Two gliders of unknown masses `m_1` and `m_2` rest on a frictionless horizontal air track. A compressed spring is placed between them and released. High-speed photogates measure their accelerations during the release: glider 1 accelerates at `a_1 = -4.5 m/s²`, while glider 2 accelerates at `a_2 = +1.5 m/s²`. 
(a) What is the mass ratio `m_2 / m_1`?
(b) If glider 1 is a standard calibrated mass of `m_1 = 0.200 kg`, what is the exact mass `m_2`?

**Solution**:
By Mach's operational definition of inertial mass and Newton's Third Law:
The force exerted by the spring on glider 1 is `F_12` and on glider 2 is `F_21`.
Since the spring is massless, `F_12 = -F_21`.
Applying Newton's Second Law:
```
m_1 * a_1 = - m_2 * a_2
```
(a) Taking the magnitudes:
```
m_2 / m_1 = |a_1| / |a_2| = 4.5 / 1.5 = 3.0
```
Glider 2 is precisely three times as massive as glider 1.
(b) Since `m_1 = 0.200 kg`:
```
m_2 = 3.0 * m_1 = 3.0 * 0.200 kg = 0.600 kg
```
**Physical Insight**: Notice that we did not need to know the spring constant `k`, the duration of contact, or the force in Newtons. Mass is purely the reciprocal ratio of mutual accelerations.

---

### Worked Example 2.2: Integrating a Time-Dependent Force
**Problem**: A particle of mass `m` is at rest at the origin (`x = 0, v = 0`) at time `t = 0`. It is subjected to a time-dependent force `F(t) = F_0 * sin(ω*t)`. 
Find the velocity `v(t)` and position `x(t)` for all future time.

**Solution**:
Newton's Second Law is:
```
m * (dv/dt) = F_0 * sin(ω*t)
```
Separate variables and integrate with initial condition `v(0) = 0`:
```
v(t) = (F_0 / m) * ∫_0^t sin(ω*t') dt' = (F_0 / (m*ω)) * [ -cos(ω*t') ]_0^t
v(t) = (F_0 / (m*ω)) * ( 1 - cos(ω*t) )
```
Notice that since `1 - cos(ω*t) ≥ 0`, the velocity is **always positive or zero**—the particle never moves backward!
Now integrate velocity to find position `x(t)` with `x(0) = 0`:
```
x(t) = ∫_0^t v(t') dt' = (F_0 / (m*ω)) * ∫_0^t (1 - cos(ω*t')) dt'
x(t) = (F_0 / (m*ω)) * [ t - (1/ω)*sin(ω*t) ]
```
The motion consists of a constant average drift velocity `v_avg = F_0 / (m*ω)` plus an oscillatory ripple!

---

### Practice Problem 2.1 (To Solve)
**Statement**: A block of mass `m` slides on a flat surface. It experiences an initial velocity `v_0` at `t = 0` and a velocity-dependent retarding force `F = -k * v²` (where `k` is a positive constant). 
(a) Find the velocity `v(t)` as a function of time.
(b) Does the block come to rest in a finite time? Explain physically.
* **Hint**: Separate variables: `m * dv/dt = -k * v²  ===>  ∫ v^(-2) dv = -(k/m) ∫ dt`.
* **Answer**: `v(t) = v_0 / (1 + (k*v_0 / m)*t)`. As `t -> ∞`, `v(t) -> 0`, but it technically never reaches zero in finite time because as speed drops, the retarding force decreases quadratically!

---

### Practice Problem 2.2 (To Solve)
**Statement**: Three interacting particles with masses `m_1, m_2, m_3` exert mutual gravitational forces on each other: `F_ij = -G*m_i*m_j*(r_i - r_j) / |r_i - r_j|³`.
Prove explicitly that the sum of all internal forces `Σ_i Σ_{j≠i} F_ij` equals zero, confirming that total linear momentum is strictly conserved.
* **Hint**: Expand the sum for `i, j ∈ {1, 2, 3}` and pair `F_12 + F_21`, `F_13 + F_31`, and `F_23 + F_32`.
* **Answer**: Each pair has `(r_i - r_j) = -(r_j - r_i)` and `|r_i - r_j| = |r_j - r_i|`, so each pair sums identically to the zero vector.

---

## 6. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 1:
  * Sections 1.3–1.5 (pp. 11–23): Mass, Force, Newton's 2nd and 3rd Laws, Momentum Conservation.
  * Problems 1.12, 1.18, 1.22 (pp. 37–39): Forces, equations of motion, momentum conservation.
* **Feynman, Richard P.**, *The Feynman Lectures on Physics*, Vol. 1:
  * Chapter 9: "Newton's Laws of Dynamics" (Sections 9.1–9.4 on force and acceleration).
  * Chapter 11: "Vectors" (Section 11.4 on the 3rd law and momentum).
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 2: "Newton's Laws" (Sections 2.1–2.4).
