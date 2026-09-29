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
