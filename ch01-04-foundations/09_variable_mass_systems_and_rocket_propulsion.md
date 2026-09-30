# 09. Variable-Mass Systems & The Rocket Equation

**Foundational Story**: Chapter 3, Section 3.2  
**Cross-References**: 
* Taylor, *Classical Mechanics*, Ch. 3 (pp. 85–87)
* Kleppner & Kolenkow, *An Introduction to Mechanics*, Ch. 3 (pp. 136–144)
* Feynman, *Lectures on Physics*, Vol. 1, Ch. 10

---

## 1. The Common Fallacy: Why $F = \frac{d(mv)}{dt}$ Fails for Open Systems

A common textbook mistake is trying to calculate rocket thrust by expanding the product rule:

$$
F_{\text{ext}} = \frac{d(m v)}{dt} = m \frac{dv}{dt} + v \frac{dm}{dt} \quad \text{\textbf{(WARNING: WRONG FOR OPEN SYSTEMS!)}}
$$

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

At time $t$, the total momentum of the rocket is:

$$
P(t) = m v
$$

During the time interval $dt$, the rocket burns and ejects a small mass $-dm > 0$ (since $m$ decreases, $dm < 0$).
* The rocket's mass becomes $m + dm$.
* The rocket's velocity increases to $v + dv$.
* The velocity of the expelled fuel in the **inertial frame** is $v - v_{\text{ex}}$.

The total momentum of the system (rocket + ejected gas) at $t + dt$ is:

$$
P(t + dt) = (m + dm)(v + dv) + (-dm)(v - v_{\text{ex}})
$$

Expand this product:

$$
P(t + dt) = mv + m\,dv + v\,dm + dm\,dv - v\,dm + v_{\text{ex}}\,dm
$$

Neglect the second-order infinitesimal $dm \cdot dv \approx 0$, and notice that $v \cdot dm$ cancels:

$$
P(t + dt) = mv + m\,dv + v_{\text{ex}}\,dm
$$

Now compute the change in momentum $dP = P(t + dt) - P(t)$:

$$
dP = m\,dv + v_{\text{ex}}\,dm
$$

By Newton's Second Law, $\frac{dP}{dt} = F_{\text{ext}}$:

$$
m \frac{dv}{dt} + v_{\text{ex}} \frac{dm}{dt} = F_{\text{ext}}
$$

Rearranging into standard form:

$$
m \frac{dv}{dt} = -v_{\text{ex}} \frac{dm}{dt} + F_{\text{ext}}
$$

> **The Equation of Motion for a Rocket**:  
> The term $-v_{\text{ex}} \frac{dm}{dt}$ is the **Thrust Force** ($F_{\text{thrust}}$).  
> Since $\frac{dm}{dt} < 0$ (fuel is being expelled), the thrust is positive and accelerates the rocket forward!

---

## 3. The Tsiolkovsky Rocket Equation (Deep Space, Zero Gravity)

In deep space far from gravitational bodies, $F_{\text{ext}} = 0$:

$$
m \frac{dv}{dt} = -v_{\text{ex}} \frac{dm}{dt}
$$

Multiply by $dt$ and divide by $m$:

$$
dv = -v_{\text{ex}} \frac{dm}{m}
$$

Integrate from initial state $(m_0, v_0)$ to final empty-tank state $(m_{\text{final}}, v_{\text{final}})$:

$$
\int_{v_0}^{v_{\text{final}}} dv = -v_{\text{ex}} \int_{m_0}^{m_{\text{final}}} \frac{dm}{m}
$$

$$
v_{\text{final}} - v_0 = -v_{\text{ex}} \ln\left(\frac{m_{\text{final}}}{m_0}\right) = v_{\text{ex}} \ln\left(\frac{m_0}{m_{\text{final}}}\right)
$$

> **The Tsiolkovsky Rocket Equation**:
> 
> $$
> \Delta v = v_{\text{ex}} \ln\left(\frac{m_0}{m_{\text{final}}}\right)
> $$

---

## 4. The Tyranny of the Rocket Equation

Inverting Tsiolkovsky's equation to find the required initial mass ratio:

$$
\frac{m_0}{m_{\text{final}}} = e^{\Delta v / v_{\text{ex}}}
$$

Because unspent fuel must carry the fuel that burns later, the required mass ratio **grows exponentially** with the required velocity change $\Delta v$!

### Concrete Real-World Example
To reach low Earth orbit, a rocket needs $\Delta v \approx 8.0\text{ km/s}$.  
A top-tier chemical rocket engine (liquid hydrogen/oxygen) has an exhaust velocity of roughly $v_{\text{ex}} \approx 4.0\text{ km/s}$.

$$
\frac{m_0}{m_{\text{final}}} = e^{8.0 / 4.0} = e^2 \approx 7.4
$$

This means at least $86\%$ of the rocket's launch mass must be pure propellant, leaving only $14\%$ for tanks, engines, structure, and payload!

If the exhaust speed were only $2.0\text{ km/s}$:

$$
\frac{m_0}{m_{\text{final}}} = e^{8.0 / 2.0} = e^4 \approx 54.6
$$

Now $98.2\%$ must be fuel—a structural engineering impossibility for a single stage!  
**This exponential penalty is the fundamental reason modern rockets (Saturn V, Falcon 9, Starship) must use multiple staging**, discarding dead empty tank mass along the ascent.

---

## 5. Rocket Climbing in a Uniform Gravitational Field

If the rocket launches vertically against Earth's gravity, $F_{\text{ext}} = -m g$:

$$
m \frac{dv}{dt} = -v_{\text{ex}} \frac{dm}{dt} - m g
$$

Divide by $m$ and integrate with respect to time:

$$
dv = -v_{\text{ex}} \frac{dm}{m} - g\,dt
$$

Assuming fuel is consumed at a constant rate $k = -\frac{dm}{dt}$, the burn lasts a time $t$:

$$
v(t) = v_0 + v_{\text{ex}} \ln\left(\frac{m_0}{m(t)}\right) - g t
$$

The term $-g t$ is **Gravity Drag**: the longer the rocket takes to burn its fuel, the more velocity it loses fighting Earth's gravitational pull.

---

## 6. Summary Cheat Sheet for Module 09

| Concept | Formula | Key Insight |
|---|---|---|
| **Thrust Force** | $F_{\text{thrust}} = -v_{\text{ex}} \frac{dm}{dt}$ | Pushing gas backward pushes rocket forward |
| **Rocket Equation** | $\Delta v = v_{\text{ex}} \ln\left(\frac{m_0}{m_{\text{final}}}\right)$ | Velocity gain depends logarithmically on mass ratio |
| **Mass Ratio Trap** | $\frac{m_0}{m_{\text{final}}} = e^{\Delta v / v_{\text{ex}}}$ | Exponential scaling demands multistage designs |
| **Gravity Drag** | $-g t_{\text{burn}}$ | Fast high-thrust burns minimize gravitational velocity loss |

---

## 7. Worked Examples & Practice Problems

### Worked Example 9.1: Orbit Insertion & The Multistage Advantage
**Problem**: A spacecraft must achieve an orbital boost of $\Delta v = 9.0\text{ km/s} = 9000\text{ m/s}$ to escape into an interplanetary transfer orbit. The rocket engine uses hydrocarbon-liquid oxygen propellant with an effective exhaust velocity $v_{\text{ex}} = 3000\text{ m/s}$.  
(a) If executed with a single-stage rocket, what percentage of the launch mass must be fuel?  
(b) Now consider a two-stage rocket, where each stage provides $\Delta v_1 = \Delta v_2 = 4500\text{ m/s}$. Compute the mass ratio required for each stage and explain why staging delivers superior payload capability.

**Solution**:  
(a) **Single Stage**:  
Apply the Tsiolkovsky Rocket Equation:

$$
\Delta v = v_{\text{ex}} \ln\left(\frac{m_0}{m_{\text{final}}}\right) \implies \frac{m_0}{m_{\text{final}}} = e^{\Delta v / v_{\text{ex}}}
$$

$$
\frac{m_0}{m_{\text{final}}} = e^{9000 / 3000} = e^3 \approx 20.086
$$

This means:

$$
m_{\text{final}} = \frac{m_0}{20.086} \approx 0.0498\,m_0
$$

The fuel consumed is:

$$
m_{\text{fuel}} = m_0 - m_{\text{final}} = m_0 (1 - 0.0498) = 0.9502\,m_0 \implies 95.02\% \text{ fuel!}
$$

If empty tanks, engines, and plumbing weigh more than $5\%$ of the rocket, **a single stage cannot carry even 1 gram of payload!**

(b) **Two-Stage Rocket**:  
For each stage:

$$
\frac{m_{\text{initial},i}}{m_{\text{final},i}} = e^{4500 / 3000} = e^{1.5} \approx 4.482
$$

Each stage requires a mass ratio of only $4.5$ instead of $20.1$!  
By discarding the huge empty stage-1 fuel tanks and heavy engines midway through the ascent, stage 2 does not have to waste propellant accelerating dead metal. This dramatic reduction in dead weight is what makes orbital spaceflight physically achievable.

---

### Worked Example 9.2: The Falling Chain on a Scale
**Problem**: A flexible heavy chain of total length $L$ and total mass $M$ is held vertically by its upper end so that its lower end just touches the pan of a weighing scale. At $t = 0$, the upper end is released from rest.  
Find the reading on the scale as a function of the distance $y$ that the top end has fallen. What does the scale read right as the last link hits the pan?

**Solution**:  
Let linear mass density be $\lambda = M / L$.  
At time $t$, the top has fallen a distance $y$. The velocity of the falling links just before hitting the table is:

$$
v = \sqrt{2gy}
$$

The scale reading $F_{\text{scale}}$ consists of two distinct physical parts:
1. **Static weight of the chain already resting on the table**:  
   A length $y$ is on the table, so its weight is:

$$
W_{\text{resting}} = (\lambda y) g
$$

2. **Dynamic impact force of incoming chain links losing momentum**:  
   In time $dt$, a small mass $dm = \lambda \, dy = \lambda (v\,dt)$ strikes the table and comes to an instantaneous stop. The rate of momentum transferred to the scale is:

$$
F_{\text{impact}} = \frac{dp}{dt} = v \frac{dm}{dt} = v (\lambda v) = \lambda v^2
$$

   Substitute $v^2 = 2gy$:

$$
F_{\text{impact}} = \lambda (2gy) = 2(\lambda y) g
$$

The total force recorded by the scale is the sum of static weight and dynamic impact:

$$
F_{\text{scale}} = W_{\text{resting}} + F_{\text{impact}} = \lambda y g + 2 \lambda y g = 3 \lambda g y
$$

At the exact instant the final link strikes the table ($y = L$):

$$
F_{\text{scale}} = 3 \lambda g L = 3 M g
$$

**Physical Insight**: The scale temporarily registers **three times the total weight of the chain**! Two-thirds of the force is dynamic impact momentum absorption, and one-third is static gravity.

---

### Practice Problem 9.1 (To Solve)
**Statement**: A freight flatcar of initial mass $M_0$ rolls frictionlessly along a horizontal track with speed $v_0$. Rain begins falling vertically into the open bed at a constant rate of $\sigma\text{ kg/s}$. Find the velocity of the flatcar $v(t)$ as a function of time.
* **Hint**: The rain has zero horizontal velocity before entering the car. Horizontal momentum of the closed system is strictly conserved:

$$
P_x = (M_0 + \sigma t) v(t) = M_0 v_0
$$

* **Answer**: $v(t) = \frac{M_0 v_0}{M_0 + \sigma t}$.

---

### Practice Problem 9.2 (To Solve)
**Statement**: A rocket launches vertically upward from rest in a uniform gravitational field $g$. The burn rate $k = -\frac{dm}{dt}$ is constant, and the exhaust speed is $v_{\text{ex}}$. Find the formula for the height $y(t)$ achieved at engine burnout time $t_b$.
* **Hint**: Integrate velocity $v(t) = -v_{\text{ex}} \ln\left(1 - \frac{kt}{m_0}\right) - gt$ using $\int \ln(u)\,du = u\ln(u) - u$.
* **Answer**:

$$
y(t_b) = v_{\text{ex}} t_b - \frac{1}{2} g t_b^2 - \frac{v_{\text{ex}} m_{\text{final}}}{k} \ln\left(\frac{m_0}{m_{\text{final}}}\right)
$$

---

## 8. Exact Primary References
* **Taylor, John R.**, *Classical Mechanics*, Chapter 3:
  * Section 3.2 (pp. 85–87): Rockets, Variable Mass Systems.
  * Problems 3.12, 3.14, 3.19 (pp. 100–102): Rocket launches with gravity and variable drag.
* **Kleppner, Daniel & Kolenkow, Robert**, *An Introduction to Mechanics* (2nd ed.):
  * Chapter 3: "Forces and Equations of Motion" (Section 3.5: Variable Mass Systems, Examples 3.12–3.14 on falling chains and freight cars).
* **Morin, David**, *Introduction to Classical Mechanics*, Chapter 3:
  * Section 3.5 (pp. 79–86): Complete rigorous treatment of rocket kinematics and falling ropes.\n
