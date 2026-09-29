# 09. Variable-Mass Systems & The Rocket Equation

**Foundational Story**: Chapter 3, Section 3.2  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 3 (pp. 85–87)
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 3 (pp. 136–144)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 10

---

## 1. The Common Fallacy: Why `F = d(mv)/dt` Fails for Open Systems

A common textbook mistake is trying to calculate rocket thrust by expanding the product rule:
```
F_ext = d(m*v) / dt = m * (dv/dt) + v * (dm/dt)   <--- WARNING: WRONG FOR OPEN SYSTEMS!
```
Why is this formula invalid for a rocket? 
Because the velocity $v$ in that derivative is frame-dependent! If you change your reference frame by adding a constant velocity $V_0$, $v$ changes, yet physical forces cannot depend on your choice of inertial observer.

**The Golden Rule of Variable-Mass Mechanics**: 
> **Newton's Second Law applies strictly to a closed, well-defined collection of fixed particles.** 
> To analyze a system losing or gaining mass, you must include the expelled or ingested mass in the momentum budget!

---

## 2. Derivation of the Rocket Equation from First Principles

Consider a rocket in deep space. Let:
* $m(t)$: Mass of the rocket hull + unburned fuel at time $t$.
* $v(t)$: Forward velocity of the rocket relative to an inertial observer.
* $v_{\text{ex}}$: Exhaust speed of expelled gases **relative to the rocket engine** (directed backward).

```
State at time t:
       +------------+
       | Rocket m(t)| ===> v(t)
       +------------+

State at time t + dt:
             +----------------+
 <===        | Rocket m + dm  | ===> v + dv
(exhaust     +----------------+
 -dm at speed
 u_exhaust)
```

At time $t$, the total momentum of the rocket is:
```
P(t) = m * v
```
During the time interval $dt$, the rocket burns and ejects a small mass $-dm > 0$ (since $m$ decreases, $dm < 0$).
* The rocket's mass becomes $m + dm$.
* The rocket's velocity increases to $v + dv$.
* The velocity of the expelled fuel in the **inertial frame** is $v - v_{\text{ex}}$.

The total momentum of the system (rocket + ejected gas) at $t + dt$ is:
```
P(t + dt) = (m + dm) * (v + dv) + (-dm) * (v - v_ex)
```
Expand this product:
```
P(t + dt) = m*v + m*dv + v*dm + dm*dv - v*dm + v_ex*dm
```
Neglect the second-order infinitesimal $dm \cdot dv \approx 0$, and notice that $v \cdot dm$ cancels:
```
P(t + dt) = m*v + m*dv + v_ex*dm
```
Now compute the change in momentum $dP = P(t + dt) - P(t)$:
```
dP = m*dv + v_ex*dm
```
By Newton's Second Law, $dP / dt = F_{\text{ext}}$:
```
m * (dv / dt) + v_ex * (dm / dt) = F_ext
```
Rearranging into standard form:
```
m * (dv / dt) = - v_ex * (dm / dt) + F_ext
```
> **The Equation of Motion for a Rocket**:
> The term `-v_ex * (dm/dt)` is the **Thrust Force** ($F_{\text{thrust}}$). 
> Since $dm/dt < 0$ (fuel is being lost), the thrust is positive and drives the rocket forward!

---

## 3. The Tsiolkovsky Rocket Equation (Deep Space, Zero Gravity)

In deep space far from gravitational bodies, $F_{\text{ext}} = 0$:
```
m * (dv / dt) = - v_ex * (dm / dt)
```
Multiply by $dt$ and divide by $m$:
```
dv = - v_ex * (dm / m)
```
Integrate from initial state $(m_0, v_0)$ to final empty-tank state $(m_{\text{final}}, v_{\text{final}})$:
```
∫_{v_0}^{v_final} dv = - v_ex * ∫_{m_0}^{m_final} (dm / m)
```
```
v_final - v_0 = - v_ex * ln(m_final / m_0) = v_ex * ln(m_0 / m_final)
```

> **The Tsiolkovsky Rocket Equation**:
> ```
> Δv = v_ex * ln(m_0 / m_final)
> ```

---

## 4. The Tyranny of the Rocket Equation

Look at the logarithm in Tsiolkovsky's equation. Inverting it to find the required initial mass ratio:
```
m_0 / m_final = e^(Δv / v_ex)
```
Because the fuel must carry the fuel that burns later, the mass ratio **grows exponentially** with the required velocity change $\Delta v$!

### Concrete Real-World Example
To reach low Earth orbit, a rocket needs $\Delta v \approx 8.0\text{ km/s}$.
A top-tier chemical rocket engine (liquid hydrogen/oxygen) has an exhaust velocity of roughly $v_{\text{ex}} \approx 4.0\text{ km/s}$.
```
m_0 / m_final = e^(8.0 / 4.0) = e² ≈ 7.4
```
This means at least $86\%$ of the rocket's launch mass must be pure propellant, leaving only $14\%$ for tanks, engines, structure, and payload!

If the exhaust speed were only $2.0\text{ km/s}$:
```
m_0 / m_final = e^(8.0 / 2.0) = e⁴ ≈ 54.6
```
Now $98.2\%$ must be fuel—a structural engineering impossibility for a single stage!
**This exponential penalty is the sole reason modern rockets (Saturn V, Falcon 9, Starship) must use multiple staging**, discarding dead empty tank mass along the ascent.

---

## 5. Rocket Climbing in a Uniform Gravitational Field

If the rocket launches vertically against Earth's gravity, $F_{\text{ext}} = -m \cdot g$:
```
m * (dv / dt) = - v_ex * (dm / dt) - m * g
```
Divide by $m$ and integrate with respect to time:
```
dv = - v_ex * (dm / m) - g * dt
```
Assuming fuel is consumed at a constant rate $k = -dm/dt$, the burn lasts a time $t$:
```
v(t) = v_0 + v_ex * ln(m_0 / m(t)) - g * t
```
The term $-g \cdot t$ is **Gravity Drag**: the longer the rocket takes to burn its fuel, the more velocity it loses fighting Earth's pull.

---

## 6. Summary Cheat Sheet for Module 09

| Concept | Formula | Key Insight |
|---|---|---|
| **Thrust Force** | `F_thrust = - v_ex * (dm/dt)` | Pushing gas backward pushes rocket forward |
| **Rocket Equation** | `Δv = v_ex * ln(m_0 / m_final)` | Velocity gain depends logarithmically on mass ratio |
| **Mass Ratio Trap** | `m_0 / m_final = e^(Δv / v_ex)` | Exponential scaling demands multistage designs |
| **Gravity Drag** | `- g * t_burn` | Fast high-thrust burns minimize gravitational velocity loss |


---

## 7. Worked Examples & Practice Problems

### Worked Example 9.1: Orbit Insertion & The Multistage Advantage
**Problem**: A spacecraft must achieve an orbital boost of `Δv = 9.0 km/s = 9000 m/s` to escape into an interplanetary transfer orbit. The rocket engine uses hydrocarbon-liquid oxygen propellant with an effective exhaust velocity `v_ex = 3000 m/s`.
(a) If executed with a single-stage rocket, what percentage of the launch mass must be fuel?
(b) Now consider a two-stage rocket, where each stage provides `Δv_1 = Δv_2 = 4500 m/s`. If each stage has a structural dry-mass fraction of 8% of its total stage mass, compute the payload fraction delivered to orbit and compare it with the single-stage rocket.

**Solution**:
(a) **Single Stage**:
Apply the Tsiolkovsky Rocket Equation:
```
Δv = v_ex * ln(m_0 / m_final)  ===>  m_0 / m_final = e^(Δv / v_ex)
m_0 / m_final = e^(9000 / 3000) = e³ ≈ 20.086
```
This means:
```
m_final = m_0 / 20.086 ≈ 0.0498 * m_0
```
The fuel consumed is:
```
m_fuel = m_0 - m_final = m_0 * (1 - 0.0498) = 0.9502 * m_0  ===>  95.02% fuel!
```
If empty tanks, engines, and plumbing weigh more than 5% of the rocket, **a single stage cannot carry even 1 gram of payload!**

(b) **Two-Stage Rocket**:
For each stage:
```
m_initial_i / m_final_i = e^(4500 / 3000) = e^1.5 ≈ 4.482
```
Each stage requires a mass ratio of only `4.5` instead of `20`! 
By discarding the huge empty stage-1 fuel tanks and heavy engines midway through the ascent, stage 2 does not have to waste fuel accelerating dead metal. This dramatic reduction in dead weight is what makes modern space exploration physically possible.

---

### Worked Example 9.2: The Falling Chain on a Scale
**Problem**: A flexible heavy chain of total length `L` and total mass `M` is held vertically by its upper end so that its lower end just touches the pan of a weighing scale. At `t = 0`, the upper end is released from rest.
Find the reading on the scale as a function of the distance `y` that the top end has fallen. What does the scale read right as the last link hits the pan?

**Solution**:
Let linear mass density be `λ = M / L`.
At time `t`, the top has fallen a distance `y`.
The velocity of the falling links just before hitting the table is:
```
v = sqrt(2 * g * y)
```
The scale reading `F_scale` consists of two distinct physical parts:
1. **Static weight of the chain already resting on the table**:
   A length `y` is on the table, so its weight is:
   ```
   W_resting = (λ * y) * g
   ```
2. **Dynamic impact force of incoming chain links losing momentum**:
   In time `dt`, a small mass `dm = λ * dy = λ * (v dt)` strikes the table and comes to an instantaneous stop.
   The rate of change of momentum delivered to the scale is:
   ```
   F_impact = dp/dt = v * (dm/dt) = v * (λ * v) = λ * v²
   ```
   Substitute `v² = 2*g*y`:
   ```
   F_impact = λ * (2*g*y) = 2 * (λ * y) * g
   ```
The total force recorded by the scale is:
```
F_scale = W_resting + F_impact = (λ * y * g) + 2 * (λ * y * g) = 3 * λ * g * y
```
At the exact instant the final link strikes the table (`y = L`):
```
F_scale = 3 * λ * g * L = 3 * M * g
```
**Physical Insight**: The scale temporarily registers **three times the total weight of the chain**! Two-thirds of the force is dynamic impact momentum absorption, and one-third is static gravity.

---

### Practice Problem 9.1 (To Solve)
**Statement**: A freight flatcar of initial mass `M_0` rolls frictionlessly along a horizontal track with speed `v_0`. Rain begins falling vertically into the open bed at a constant rate of `σ` kg/s.
Find the velocity of the flatcar `v(t)` as a function of time.
* **Hint**: The rain has zero horizontal velocity before entering the car. Horizontal momentum of the system is strictly conserved: `P_x = (M_0 + σ*t) * v(t) = M_0 * v_0`.
* **Answer**: `v(t) = v_0 * M_0 / (M_0 + σ*t)`.

---

### Practice Problem 9.2 (To Solve)
**Statement**: A rocket launches vertically upward from rest in a uniform gravitational field `g`. The burn rate `k = -dm/dt` is constant, and the exhaust speed is `v_ex`.
Find the formula for the height `y(t)` achieved at engine burnout time `t_b`.
* **Hint**: Integrate velocity `v(t) = -v_ex * ln(1 - k*t/m_0) - g*t` using `∫ ln(u) du = u*ln(u) - u`.
* **Answer**: `y(t_b) = v_ex * t_b - (1/2)*g*t_b² - (v_ex * m_final / k) * ln(m_0 / m_final)`.

---

## 8. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 3:
  * Section 3.2 (pp. 85–87): Rockets, Variable Mass Systems.
  * Problems 3.12, 3.14, 3.19 (pp. 100–102): Rocket launches with gravity and variable drag.
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 3: "Forces and Equations of Motion" (Section 3.5: Variable Mass Systems, Examples 3.12–3.14 on falling chains and freight cars).
* **Morin, David**, *Introduction to Classical Mechanics*, Chapter 3:
  * Section 3.5 (pp. 79–86): Complete rigorous treatment of rocket kinematics and falling ropes.
