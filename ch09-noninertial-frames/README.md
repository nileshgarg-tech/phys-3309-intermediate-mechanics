# Chapter 9: Mechanics in Non-Inertial Frames

Accelerating and rotating frames, centrifugal force, Coriolis force, and tidal phenomena.

---

## Key Topics & Roadmap

* **Time Derivatives in a Rotating Frame**:
  * Transformation relation for any vector `Q`:
    * `(dQ/dt)_space = (dQ/dt)_body + Ω x Q`
  * Here `Ω` is the angular velocity of the rotating frame relative to the inertial frame.

* **Newton's Second Law in a Rotating Frame**:
  * `m * a_rot = F_real + F_fictitious`
  * `m * a_rot = F_real + 2 * m * (v_rot x Ω) + m * (Ω x r) x Ω - m * (dΩ/dt x r) - m * A_frame`

* **The Fictitious Forces**:
  1. **Centrifugal Force**: `F_cf = m * (Ω x r) x Ω = m * Ω² * ρ * ρ_hat` (directed outward perpendicular to rotation axis).
  2. **Coriolis Force**: `F_cor = 2 * m * v_rot x Ω` (acts perpendicular to the velocity of the particle in the rotating frame).
  3. **Euler Force**: `-m * (dΩ/dt x r)` (present only when the angular velocity is accelerating).

* **Physical Consequences of the Coriolis Force**:
  * **Free Fall Deflection**: Eastward deflection of a falling mass on Earth (`Δy ~ (2/3) * Ω * cos(latitude) * sqrt(8*h³ / g)`).
  * **Atmospheric Circulation**: Counterclockwise cyclones in the Northern Hemisphere, clockwise in the Southern Hemisphere.
  * **Foucault Pendulum**: Slow precession of the swing plane with rate `Ω_precess = Ω_earth * sin(latitude)`.

* **Tides**:
  * Differential gravitational attraction of the Moon and Sun causing ocean bulges.
