import os

def create_inertial_frame_criteria_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradCrit" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b0f19"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="980" height="400" rx="16" fill="url(#bgGradCrit)"/>

  <!-- Title & Subtitle -->
  <text x="490" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" fill="#f8fafc" text-anchor="middle" letter-spacing="0.5">
    OPERATIONAL CRITERION: HOW TO TEST IF A REFERENCE FRAME IS INERTIAL
  </text>
  <text x="490" y="60" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#a5b4fc" text-anchor="middle">
    Newton's 1st Law is an empirical diagnostic test separating real dynamical frames from accelerated coordinates
  </text>

  <!-- Card 1: Step 1 -->
  <g transform="translate(35, 85)">
    <rect width="280" height="285" rx="12" fill="#1e293b" stroke="#6366f1" stroke-width="1.5"/>
    <circle cx="32" cy="32" r="15" fill="#4f46e5"/>
    <text x="32" y="37" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">1</text>
    <text x="58" y="37" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#818cf8">Isolate the Test Body</text>

    <!-- Content with clean line wrapping -->
    <text x="20" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">Take a test body and eliminate</text>
    <text x="20" y="90" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">all physical interactions:</text>

    <text x="20" y="118" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8">• Zero friction (air-bearing puck)</text>
    <text x="20" y="138" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8">• Zero tension / normal push</text>
    <text x="20" y="158" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8">• Zero gravitational / EM fields</text>
    
    <!-- Criterion Box -->
    <rect x="20" y="195" width="240" height="60" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="140" y="222" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Diagnostic Condition:</text>
    <text x="140" y="242" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#38bdf8" text-anchor="middle">F_real,net = 0</text>
  </g>

  <!-- Card 2: Step 2 -->
  <g transform="translate(350, 85)">
    <rect width="280" height="285" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <circle cx="32" cy="32" r="15" fill="#059669"/>
    <text x="32" y="37" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">2</text>
    <text x="58" y="37" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#34d399">Observe Kinematics</text>

    <text x="20" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">Track position over time using</text>
    <text x="20" y="90" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">synchronized frame clocks:</text>
    
    <!-- Case A Box -->
    <rect x="18" y="112" width="244" height="65" rx="8" fill="#064e3b" fill-opacity="0.45" stroke="#059669" stroke-width="1"/>
    <text x="140" y="134" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#6ee7b7" text-anchor="middle">Case A: a = 0 (v = const)</text>
    <text x="140" y="152" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#a7f3d0" text-anchor="middle">Frame is INERTIAL ✓</text>
    <text x="140" y="167" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="#6ee7b7" text-anchor="middle">Newton's 1st Law Verified</text>

    <!-- Case B Box -->
    <rect x="18" y="190" width="244" height="65" rx="8" fill="#7f1d1d" fill-opacity="0.45" stroke="#dc2626" stroke-width="1"/>
    <text x="140" y="212" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#fca5a5" text-anchor="middle">Case B: a ≠ 0 (accelerates)</text>
    <text x="140" y="230" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#fecaca" text-anchor="middle">Frame is NON-INERTIAL ✗</text>
    <text x="140" y="245" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="#fca5a5" text-anchor="middle">Spontaneous Acceleration</text>
  </g>

  <!-- Card 3: Step 3 -->
  <g transform="translate(665, 85)">
    <rect width="280" height="285" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <circle cx="32" cy="32" r="15" fill="#d97706"/>
    <text x="32" y="37" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">3</text>
    <text x="58" y="37" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#fbbf24">Apply Mechanics</text>

    <text x="20" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">Valid equations of motion you</text>
    <text x="20" y="90" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">are permitted to write:</text>

    <!-- Inertial Form Box -->
    <rect x="18" y="112" width="244" height="65" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="140" y="133" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" fill="#94a3b8" text-anchor="middle">Inertial Form (Real Forces Only):</text>
    <text x="140" y="156" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#4ade80" text-anchor="middle">Σ F_real = m a</text>

    <!-- Non-Inertial Form Box -->
    <rect x="18" y="190" width="244" height="65" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="140" y="211" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" fill="#94a3b8" text-anchor="middle">Non-Inertial (Must Add Fictitious):</text>
    <text x="140" y="234" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#f87171" text-anchor="middle">Σ F_real + F_inertial = m a'</text>
  </g>
</svg>
'''
    with open('d:/UH/PHYS 3309/ch01-04-foundations/visualizations/assets/inertial_frame_criteria.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated inertial_frame_criteria.svg')

def create_coffee_cup_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradTrain" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="cupGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <marker id="arrowRed3" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#ef4444"/>
    </marker>
    <marker id="arrowBlue3" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrowPurple3" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#c084fc"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="980" height="500" rx="16" fill="url(#bgGradTrain)"/>

  <!-- Title Banner -->
  <text x="490" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">
    THE COFFEE CUP PARADOX: INERTIAL VS. NON-INERTIAL OBSERVER
  </text>
  <text x="490" y="60" font-family="system-ui, -apple-system, sans-serif" font-size="12.5" fill="#94a3b8" text-anchor="middle">
    Why Newton's First Law is an operational test for reference frames, not a trivial case of F = ma
  </text>

  <!-- ==================== LEFT CARD: GROUND FRAME S (INERTIAL) ==================== -->
  <g transform="translate(30, 80)">
    <rect width="445" height="395" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    
    <!-- Badge -->
    <rect x="20" y="16" width="200" height="26" rx="6" fill="#0369a1" fill-opacity="0.4"/>
    <text x="30" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#38bdf8">
      FRAME S: GROUND (INERTIAL)
    </text>

    <!-- Subtitle -->
    <text x="20" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">
      Ground observer stands on track. Train accelerates: <tspan fill="#38bdf8" font-weight="700">a_train = +a x̂</tspan>
    </text>

    <!-- SCENE: Track, Observer, Train -->
    <!-- Track line -->
    <line x1="20" y1="210" x2="425" y2="210" stroke="#475569" stroke-width="2"/>
    <line x1="20" y1="214" x2="425" y2="214" stroke="#334155" stroke-width="1" stroke-dasharray="6 4"/>

    <!-- Ground Observer (standing clearly on platform at x = 55, clear of train!) -->
    <g transform="translate(55, 145)">
      <!-- Head -->
      <circle cx="0" cy="0" r="8" fill="#38bdf8"/>
      <!-- Torso -->
      <line x1="0" y1="8" x2="0" y2="38" stroke="#38bdf8" stroke-width="2.5"/>
      <!-- Arms -->
      <line x1="-12" y1="20" x2="12" y2="20" stroke="#38bdf8" stroke-width="2"/>
      <!-- Legs down to track y=210 (offset 65 from 145) -->
      <line x1="0" y1="38" x2="-10" y2="65" stroke="#38bdf8" stroke-width="2.5"/>
      <line x1="0" y1="38" x2="10" y2="65" stroke="#38bdf8" stroke-width="2.5"/>
      <!-- Badge -->
      <rect x="-35" y="70" width="70" height="18" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="0" y="83" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#38bdf8" text-anchor="middle">Observer S</text>
    </g>

    <!-- Train Car (starts at x = 115, ends at x = 415) -->
    <g transform="translate(115, 0)">
      <!-- Train Roof Acceleration Arrow (clear of roof!) -->
      <line x1="160" y1="88" x2="260" y2="88" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrowBlue3)"/>
      <text x="210" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">a_train = +a x̂</text>

      <!-- Car Body -->
      <rect x="0" y="105" width="300" height="95" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 3"/>
      <!-- Wheels resting on rail at y=210 -->
      <circle cx="50" cy="204" r="7" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <circle cx="250" cy="204" r="7" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>

      <!-- Table inside car (accelerating right with train) -->
      <rect x="90" y="165" width="130" height="8" rx="2" fill="#475569"/>
      <line x1="105" y1="173" x2="105" y2="200" stroke="#475569" stroke-width="3"/>
      <line x1="205" y1="173" x2="205" y2="200" stroke="#475569" stroke-width="3"/>

      <!-- Table Motion Cue -->
      <line x1="140" y1="158" x2="175" y2="158" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 2" marker-end="url(#arrowBlue3)"/>
      <text x="157" y="152" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="#38bdf8" text-anchor="middle">table moves right</text>

      <!-- Coffee Cup (Stationary in space at x = 110, so near the rear of moving table!) -->
      <path d="M 100 148 L 103 165 L 123 165 L 126 148 Z" fill="url(#cupGrad2)" stroke="#f59e0b" stroke-width="1.5"/>
      <path d="M 125 151 Q 132 156 124 161" fill="none" stroke="#f59e0b" stroke-width="1.5"/>

      <!-- Vertical Reference Line showing cup stays fixed in space -->
      <line x1="113" y1="135" x2="113" y2="146" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="2 2"/>
      <text x="113" y="130" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#22c55e" text-anchor="middle">a_cup = 0</text>
    </g>

    <!-- FBD & Physics Box -->
    <rect x="20" y="275" width="405" height="100" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="32" y="296" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#22c55e">
      PHYSICAL DYNAMICS IN FRAME S:
    </text>
    <text x="32" y="318" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • Real Forces on cup: Normal force balances gravity (<tspan fill="#38bdf8">N = mg</tspan>).
    </text>
    <text x="32" y="338" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • Net horizontal force: <tspan fill="#22c55e" font-weight="700">F_net,x = 0</tspan> (frictionless table).
    </text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • <tspan fill="#4ade80" font-weight="700">Newton 1 HOLDS</tspan>: Cup stays at rest in space; table slides beneath it!
    </text>
  </g>

  <!-- ==================== RIGHT CARD: TRAIN FRAME S' (NON-INERTIAL) ==================== -->
  <g transform="translate(505, 80)">
    <rect width="445" height="395" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    
    <!-- Badge -->
    <rect x="20" y="16" width="220" height="26" rx="6" fill="#991b1b" fill-opacity="0.4"/>
    <text x="30" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#f87171">
      FRAME S': ACCELERATING TRAIN
    </text>

    <!-- Subtitle -->
    <text x="20" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">
      Observer rides inside carriage. Reference frame accelerates: <tspan fill="#f87171" font-weight="700">+a x̂</tspan>
    </text>

    <!-- SCENE: Train Interior, Seated/Standing Observer S', Sliding Cup -->
    <!-- Car Interior Boundary (solid red to show non-inertial enclosed frame) -->
    <rect x="20" y="105" width="405" height="95" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    
    <!-- Wheels resting below car floor at y=210 -->
    <circle cx="70" cy="204" r="7" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="375" cy="204" r="7" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>

    <!-- Table (Stationary relative to car, located at x = 70 to 230) -->
    <rect x="70" y="165" width="160" height="8" rx="2" fill="#475569"/>
    <line x1="90" y1="173" x2="90" y2="200" stroke="#475569" stroke-width="3"/>
    <line x1="210" y1="173" x2="210" y2="200" stroke="#475569" stroke-width="3"/>
    <text x="150" y="188" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="#64748b" text-anchor="middle">table fixed in train</text>

    <!-- Cup sliding backward (to the left) on the table -->
    <path d="M 115 148 L 118 165 L 138 165 L 141 148 Z" fill="url(#cupGrad2)" stroke="#f59e0b" stroke-width="1.5"/>
    <path d="M 140 151 Q 147 156 139 161" fill="none" stroke="#f59e0b" stroke-width="1.5"/>

    <!-- Acceleration Vector of Cup: Points Left -->
    <line x1="110" y1="145" x2="60" y2="145" stroke="#ef4444" stroke-width="2.5" marker-end="url(#arrowRed3)"/>
    <text x="85" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#ef4444" text-anchor="middle">a' = -a x̂</text>

    <!-- Fictitious Force Vector on Cup: Points Left -->
    <line x1="110" y1="156" x2="45" y2="156" stroke="#c084fc" stroke-width="2" marker-end="url(#arrowPurple3)"/>
    <text x="75" y="169" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#c084fc" text-anchor="middle">F_fict = -ma</text>

    <!-- Passenger Observer S' standing firmly on car floor at x = 330 (completely clear of wheels/borders!) -->
    <g transform="translate(330, 135)">
      <!-- Head -->
      <circle cx="0" cy="0" r="8" fill="#f87171"/>
      <!-- Torso -->
      <line x1="0" y1="8" x2="0" y2="38" stroke="#f87171" stroke-width="2.5"/>
      <!-- Arms outstretched looking at cup -->
      <line x1="-12" y1="20" x2="12" y2="20" stroke="#f87171" stroke-width="2"/>
      <!-- Legs down to car floor y=200 (offset 65 from 135) -->
      <line x1="0" y1="38" x2="-8" y2="65" stroke="#f87171" stroke-width="2.5"/>
      <line x1="0" y1="38" x2="8" y2="65" stroke="#f87171" stroke-width="2.5"/>
      <!-- Label badge positioned cleanly ABOVE passenger, not on floor! -->
      <rect x="-38" y="-25" width="76" height="18" rx="4" fill="#0f172a" stroke="#f87171" stroke-width="1"/>
      <text x="0" y="-12" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#f87171" text-anchor="middle">Passenger S'</text>
    </g>

    <!-- FBD & Physics Box -->
    <rect x="20" y="275" width="405" height="100" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="32" y="296" font-family="system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#f87171">
      NON-INERTIAL BREAKDOWN IN FRAME S':
    </text>
    <text x="32" y="318" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • Real Forces: <tspan fill="#38bdf8">F_real,x = 0</tspan>. Yet cup accelerates backward!
    </text>
    <text x="32" y="338" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • <tspan fill="#ef4444" font-weight="700">Newton 1 FAILS</tspan>: Isolated body does not move with constant velocity.
    </text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • To use F = ma', observer must invoke <tspan fill="#c084fc" font-weight="700">F_fict = -m a_train</tspan>.
    </text>
  </g>
</svg>
'''
    with open('d:/UH/PHYS 3309/ch01-04-foundations/visualizations/assets/coffee_cup_accelerating_frame.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated coffee_cup_accelerating_frame.svg')

def create_carousel_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradRot" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <marker id="arrowRedRot" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#ef4444"/>
    </marker>
    <marker id="arrowGreenRot" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#22c55e"/>
    </marker>
    <marker id="arrowCyanRot" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#06b6d4"/>
    </marker>
    <marker id="arrowAmberRot" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#f59e0b"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="980" height="500" rx="16" fill="url(#bgGradRot)"/>

  <!-- Title Banner -->
  <text x="490" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="700" fill="#f8fafc" text-anchor="middle">
    THE ROTATING CAROUSEL: CORIOLIS &amp; CENTRIFUGAL DEFLECTION
  </text>
  <text x="490" y="60" font-family="system-ui, -apple-system, sans-serif" font-size="12.5" fill="#94a3b8" text-anchor="middle">
    Throwing a ball across a rotating disk viewed from Ground (Inertial) vs Turntable (Non-Inertial)
  </text>

  <!-- ==================== LEFT CARD: GROUND INERTIAL FRAME ==================== -->
  <g transform="translate(30, 80)">
    <rect width="445" height="395" rx="12" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    
    <rect x="20" y="16" width="220" height="26" rx="6" fill="#14532d" fill-opacity="0.4"/>
    <text x="30" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#4ade80">
      INERTIAL FRAME S (FIXED GROUND)
    </text>

    <!-- Turntable Disc -->
    <g transform="translate(222, 175)">
      <circle cx="0" cy="0" r="105" fill="#0f172a" stroke="#334155" stroke-width="2"/>
      
      <!-- Rotation arrow around rim -->
      <path d="M 75 -70 A 105 105 0 0 1 105 0" fill="none" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrowAmberRot)"/>
      <text x="95" y="-80" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#f59e0b">+ω (CCW)</text>

      <!-- Center thrower A -->
      <circle cx="0" cy="0" r="8" fill="#38bdf8"/>
      <text x="-15" y="-12" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#38bdf8">Thrower (A)</text>

      <!-- Target B at t=0 (dashed initial aim point) -->
      <circle cx="0" cy="-105" r="7" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 2"/>
      <text x="0" y="-115" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="#94a3b8" text-anchor="middle">Initial Target Aim (t=0)</text>

      <!-- Target B at t=arrival (rotated CCW by angle ωΔt) -->
      <circle cx="-74" cy="-74" r="8" fill="#ec4899"/>
      <text x="-85" y="-84" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#ec4899" text-anchor="middle">Target at Arrival</text>

      <!-- Ball Straight Line Trajectory -->
      <line x1="0" y1="0" x2="0" y2="-95" stroke="#22c55e" stroke-width="3" marker-end="url(#arrowGreenRot)"/>
      <text x="10" y="-48" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#22c55e">Straight Path</text>
      <text x="10" y="-33" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="#4ade80">(F_net = 0 ⇒ v = const)</text>
    </g>

    <!-- Description Box -->
    <rect x="20" y="295" width="405" height="80" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="32" y="318" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • Ball obeys <tspan fill="#4ade80" font-weight="700">Newton 1</tspan>: zero horizontal force = straight trajectory.
    </text>
    <text x="32" y="338" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • Target catcher simply <tspan fill="#ec4899" font-weight="700">rotates out of the way</tspan> during the ball's flight time.
    </text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • No "mysterious sideways force" exists in the ground frame.
    </text>
  </g>

  <!-- ==================== RIGHT CARD: TURNTABLE NON-INERTIAL FRAME ==================== -->
  <g transform="translate(505, 80)">
    <rect width="445" height="395" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    
    <rect x="20" y="16" width="240" height="26" rx="6" fill="#991b1b" fill-opacity="0.4"/>
    <text x="30" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#f87171">
      ROTATING FRAME S' (ON TURNTABLE)
    </text>

    <!-- Turntable Disc -->
    <g transform="translate(222, 175)">
      <circle cx="0" cy="0" r="105" fill="#0f172a" stroke="#334155" stroke-width="2"/>

      <!-- Center thrower A -->
      <circle cx="0" cy="0" r="8" fill="#38bdf8"/>
      <text x="-15" y="-12" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#38bdf8">Thrower (A)</text>

      <!-- Target B fixed on turntable frame -->
      <circle cx="0" cy="-105" r="8" fill="#ec4899"/>
      <text x="0" y="-115" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#ec4899" text-anchor="middle">Target B (Appears At Rest)</text>

      <!-- Curved Ball Trajectory (deflected rightward) -->
      <path d="M 0 0 Q 35 -50 74 -74" fill="none" stroke="#ef4444" stroke-width="3" marker-end="url(#arrowRedRot)"/>
      <text x="45" y="-28" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#ef4444">Curved Path</text>

      <!-- Coriolis Force Vector Arrow -->
      <line x1="38" y1="-50" x2="65" y2="-40" stroke="#06b6d4" stroke-width="2" marker-end="url(#arrowCyanRot)"/>
      <text x="70" y="-32" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#06b6d4">F_cor</text>

      <!-- Centrifugal Force Vector Arrow -->
      <line x1="38" y1="-50" x2="52" y2="-72" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrowAmberRot)"/>
      <text x="58" y="-76" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#f59e0b">F_cf</text>
    </g>

    <!-- Description Box -->
    <rect x="20" y="295" width="405" height="80" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="32" y="318" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • Ball curves wildly rightward with <tspan fill="#ef4444" font-weight="700">zero physical force</tspan> acting!
    </text>
    <text x="32" y="338" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • To use F = ma', observer must invent <tspan fill="#06b6d4" font-weight="700">F_cor = -2m(ω × v')</tspan>
    </text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">
      • Plus the outward <tspan fill="#f59e0b" font-weight="700">Centrifugal force F_cf = -m ω × (ω × r')</tspan>.
    </text>
  </g>
</svg>
'''
    with open('d:/UH/PHYS 3309/ch01-04-foundations/visualizations/assets/rotating_carousel_coriolis.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated rotating_carousel_coriolis.svg')

if __name__ == '__main__':
    create_inertial_frame_criteria_svg()
    create_coffee_cup_svg()
    create_carousel_svg()
