"""
Maharashtra Board (MSBSHSE) — Standard 10 Physics teaching decks.

Scope: only the Physics chapters/sessions from the tuitions planner that fall
after session 25 — Refraction of Light (S28), Effects of Electric Current
1/2/3 (S41, S43, S45), Lenses (S64), Space Missions (S71). One deck per
concept session (35-40 slides), matching the established house style: title
-> objectives -> Part 1 -> content -> Quiz 1 -> Part 2 -> content -> recap ->
Quiz 2 -> closing. Content covers the full MSBSHSE Science & Technology
Part 1 textbook treatment of each topic (not just the planner's keyword
list) so every session is complete on its own.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import diagrams_mh as DM

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "MH_Grade10"))
os.makedirs(OUT, exist_ok=True)


# ===========================================================================
# S28 — Refraction of Light
# ===========================================================================
def refraction_deck():
    footer = "Refraction of Light  •  MSBSHSE Std 10 Science Part 1"
    b = Builder(footer, accent=C["teal"])

    bend = b.asset("mh10_refr_bend", D.refraction_bending("mh10_refr_bend",
                   denser_below=True))
    block = b.asset("mh10_refr_block", D.glass_block("mh10_refr_block"))
    tir = b.asset("mh10_refr_tir", D.total_internal_reflection("mh10_refr_tir"))
    fibre = b.asset("mh10_refr_fibre", D.optical_fibre("mh10_refr_fibre"))
    mirage = b.asset("mh10_refr_mirage", D.mirage("mh10_refr_mirage"))
    disp = b.asset("mh10_refr_disp", D.dispersion_spectrum("mh10_refr_disp"))

    b.title("Std 10 • Science Part 1 • Light", "Refraction of Light",
            "Laws of refraction  •  Refractive index  •  Total internal "
            "reflection  •  Dispersion  •  Twinkling of stars", img=bend)

    b.objectives([
        "Explain what refraction is and why light bends at a boundary",
        "State the two laws of refraction and apply Snell's law",
        "Define absolute and relative refractive index",
        "Explain critical angle and the conditions for total internal "
        "reflection",
        "Describe how TIR explains optical fibres, mirage and diamond "
        "sparkle",
        "Explain dispersion of light and the twinkling of stars",
    ])

    # ---- Part 1 : refraction, laws, refractive index ----
    b.divider(1, "Part 1", "Refraction and Refractive Index",
              "Why light bends, and how we measure the bending")

    b.text_image(
        "REFRACTION", "What Is Refraction?",
        ["When light passes from one transparent medium into another, it "
         "changes speed and bends at the boundary — this is refraction.",
         "Light bends towards the normal when it enters a denser medium "
         "(e.g. air to glass), and away from the normal when it enters a "
         "rarer medium (e.g. glass to air).",
         "A ray travelling exactly along the normal does not bend at all, "
         "though its speed still changes.",
         "Refraction happens because the speed of light is different in "
         "different media; the frequency stays the same but the "
         "wavelength changes."],
        bend, img_side="right", panel_title="Bending at a boundary",
        notes="Demonstrate with a pencil in a glass of water appearing "
              "bent. Stress: refraction is a change in speed and direction, "
              "not a change in frequency.")

    b.statement(
        "LAWS OF REFRACTION", "The Two Laws of Refraction",
        "First law: the incident ray, the refracted ray and the normal at "
        "the point of incidence all lie in the same plane.",
        points=[
            "Second law (Snell's law): the ratio of the sine of the angle "
            "of incidence to the sine of the angle of refraction is "
            "constant for a given pair of media.",
            "This constant is called the refractive index of the second "
            "medium with respect to the first.",
            "Snell's law is written as: sin i / sin r = constant = ₁n₂"],
        notes="Write Snell's law on the board and label i and r on the "
              "refraction_bending diagram already shown.")

    b.statement(
        "REFRACTIVE INDEX", "Absolute Refractive Index",
        "The absolute refractive index of a medium is the ratio of the "
        "speed of light in vacuum (or air) to its speed in that medium.",
        formula="n = c / v",
        notes="c = speed of light in vacuum = 3 x 10^8 m/s. n has no unit "
              "since it is a ratio of two speeds. The denser the medium, "
              "the smaller v, and so the larger n.")

    b.cards(
        "REFERENCE VALUES", "Absolute Refractive Indices of Common Media",
        [("Air", "n ≈ 1.0003 (taken as 1 for most calculations)"),
         ("Water", "n = 1.33 — light travels at about 2.26 x 10⁸ m/s"),
         ("Glass (crown)", "n = 1.5 — light travels at about 2 x 10⁸ m/s"),
         ("Diamond", "n = 2.42 — the highest of common transparent "
                     "materials, which is why it sparkles so brilliantly")],
        notes="A higher n means light slows down more and bends more "
              "strongly on entering that medium.")

    b.statement(
        "RELATIVE REFRACTIVE INDEX", "Refractive Index Between Two Media",
        "When light travels from medium 1 into medium 2, the refractive "
        "index of medium 2 with respect to medium 1 relates their "
        "absolute indices and speeds.",
        formula="₁n₂ = n₂ / n₁ = v₁ / v₂ = sin i / sin r",
        points=[
            "If medium 2 is denser than medium 1, ₁n₂ > 1 and the ray "
            "bends towards the normal.",
            "If medium 2 is rarer than medium 1, ₁n₂ < 1 and the ray "
            "bends away from the normal.",
            "₁n₂ and ₂n₁ are reciprocals of each other: ₁n₂ = 1 / ₂n₁"],
        notes="Work through both directions (air-to-glass and "
              "glass-to-air) so students see the reciprocal relationship.")

    b.worked(
        "WORKED EXAMPLE", "Finding the Speed of Light in Glass",
        "The absolute refractive index of glass is 1.5. Find the speed of "
        "light in glass. (Speed of light in vacuum = 3 x 10⁸ m/s.)",
        ["n = c / v",
         "1.5 = (3 x 10⁸) / v",
         "v = (3 x 10⁸) / 1.5"],
        "v = 2 x 10⁸ m/s",
        notes="A very common numerical style in the MSBSHSE textbook — "
              "always rearrange n = c/v for whichever quantity is asked.")

    b.quiz_intro("Quiz 1", "Check — Laws & Refractive Index", 4)
    b.quiz_q(1, "Refraction", "Light bends towards the normal when it "
             "passes from:",
             ["a denser medium to a rarer medium", "a rarer medium to a "
              "denser medium", "air into air", "vacuum into vacuum"])
    b.quiz_a(1, "B. a rarer medium to a denser medium",
             "Entering a denser medium slows the light down, and it bends "
             "towards the normal; entering a rarer medium it speeds up and "
             "bends away from the normal.")
    b.quiz_q(2, "Snell's Law", "Snell's law states that, for a given pair "
             "of media, sin i / sin r is:",
             ["always equal to 1", "constant", "equal to the speed of "
              "light", "always greater than 90°"])
    b.quiz_a(2, "B. constant",
             "This constant ratio is the refractive index of the second "
             "medium with respect to the first.")
    b.quiz_q(3, "Absolute refractive index", "The absolute refractive "
             "index of a medium is defined as:",
             ["v / c", "c / v", "c x v", "sin i / sin r for any two media"])
    b.quiz_a(3, "B. c / v",
             "n = speed of light in vacuum / speed of light in the medium. "
             "Since v is always less than c inside a medium, n is always "
             "greater than 1.")
    b.quiz_q(4, "Numerical", "The refractive index of water is 1.33. The "
             "approximate speed of light in water is:",
             ["3 x 10⁸ m/s", "2.26 x 10⁸ m/s", "4 x 10⁸ m/s", "1.33 x 10⁸ "
              "m/s"])
    b.quiz_a(4, "B. 2.26 x 10⁸ m/s",
             "v = c / n = (3 x 10⁸) / 1.33 ≈ 2.26 x 10⁸ m/s.")

    # ---- Part 2 : TIR, dispersion, twinkling ----
    b.divider(2, "Part 2", "Total Internal Reflection, Dispersion & "
              "Twinkling of Stars", "Critical angle, everyday applications "
              "and why stars twinkle")

    b.text_image(
        "CRITICAL ANGLE", "Critical Angle and Total Internal Reflection",
        ["When light travels from a denser medium to a rarer medium, the "
         "refracted ray bends away from the normal, so the angle of "
         "refraction is larger than the angle of incidence.",
         "As the angle of incidence increases, the refracted ray bends "
         "closer and closer to the boundary surface.",
         "The critical angle (C) is the angle of incidence in the denser "
         "medium for which the angle of refraction becomes exactly 90°.",
         "If the angle of incidence exceeds the critical angle, the light "
         "does not refract out at all — it is completely reflected back "
         "into the denser medium. This is total internal reflection "
         "(TIR)."],
        tir, img_side="left", panel_title="Beyond the critical angle",
        notes="Emphasise the two conditions for TIR: (1) light must travel "
              "from a denser to a rarer medium, (2) angle of incidence "
              "must exceed the critical angle.")

    b.statement(
        "CRITICAL ANGLE FORMULA", "Relating Critical Angle and Refractive "
        "Index",
        "For light travelling from a denser medium into air, the critical "
        "angle C is related to the absolute refractive index of the "
        "denser medium.",
        formula="sin C = 1 / n",
        notes="Derived by setting the angle of refraction to 90° in "
              "Snell's law: n = sin 90° / sin C = 1 / sin C.")

    b.worked(
        "WORKED EXAMPLE", "Critical Angle of Water",
        "The refractive index of water is 1.33. Find its critical angle. "
        "(sin 48.8° ≈ 0.75)",
        ["sin C = 1 / n = 1 / 1.33",
         "sin C = 0.75"],
        "C ≈ 48.8°",
        notes="This is why, looking up from underwater, the entire sky "
              "outside a cone of about 97° (2C) is compressed into that "
              "circle — beyond it, the water surface acts like a mirror.")

    b.cards(
        "APPLICATIONS OF TIR", "Everyday Uses of Total Internal Reflection",
        [("Optical fibres", "Light entering a thin glass fibre strikes the "
          "inner wall beyond the critical angle again and again, so it "
          "travels the whole length by repeated TIR with almost no loss — "
          "used in telecommunication and medical endoscopes."),
         ("Sparkle of a diamond", "Diamond has a very high refractive "
          "index (2.42) and hence a very small critical angle (about "
          "24.4°). Light entering a cut diamond undergoes TIR "
          "repeatedly before emerging, giving it its brilliance."),
         ("Mirage", "On a hot road, air near the ground is much hotter "
          "and rarer than the air above. Light from the sky bends more "
          "and more as it grazes the hot layer until it undergoes TIR, "
          "reaching the eye as if reflected from a pool of water."),
         ("Totally reflecting prisms", "A right-angled prism can turn or "
          "invert light by TIR at its hypotenuse face, used in "
          "periscopes and binoculars instead of ordinary mirrors.")],
        icons=["camera", "star", "sun", "eye"],
        notes="Show the optical-fibre and mirage diagrams alongside this "
              "slide; both are direct consequences of the same TIR "
              "condition just derived.")

    b.text_image(
        "MIRAGE", "Mirage: TIR in the Open Air",
        ["On a very hot day, the layer of air just above a road or a "
         "desert surface becomes much hotter — and hence much less dense "
         "— than the air above it.",
         "Light from the sky travelling towards the ground is refracted "
         "more and more as it enters progressively rarer layers of hot "
         "air, bending it away from the normal at each layer.",
         "Eventually the ray undergoes total internal reflection at the "
         "hottest layer and travels back up to an observer's eye.",
         "The observer sees an inverted image of the sky on the road, "
         "which looks exactly like a pool of water."],
        mirage, img_side="right", panel_title="The 'water' that isn't "
        "there",
        notes="Link back to the critical-angle condition: TIR happens "
              "here even though there is no sharp single boundary — the "
              "air's density changes gradually with height.")

    b.text_image(
        "DISPERSION", "Dispersion of Light Through a Prism",
        ["White light is a mixture of seven colours: violet, indigo, "
         "blue, green, yellow, orange and red (VIBGYOR).",
         "Each colour has a different wavelength, and a glass prism has a "
         "slightly different refractive index for each wavelength — "
         "violet is bent the most and red the least.",
         "When white light passes through a prism, the different colours "
         "are refracted by different amounts and emerge separated as a "
         "band of colours called a spectrum.",
         "This splitting of white light into its component colours is "
         "called dispersion."],
        disp, img_side="left", panel_title="Splitting white light",
        notes="A rainbow is a natural example of dispersion combined with "
              "internal reflection inside raindrops.")

    b.bullets(
        "TWINKLING OF STARS", "Why Do Stars Twinkle?",
        [("Atmospheric refraction", "Starlight enters the Earth's "
          "atmosphere and passes through air layers of continuously "
          "changing density and temperature before reaching our eyes."),
         ("Continuous bending", "Because the atmosphere has no sharp "
          "boundaries, the light bends gradually and does not travel in "
          "a single straight line — it follows a slightly curved path."),
         ("Fluctuating refractive index", "Air currents constantly change "
          "the density of the layers, so the amount of bending keeps "
          "changing from moment to moment."),
         ("Apparent flickering", "This makes the star's apparent position "
          "and brightness fluctuate rapidly, which we see as "
          "twinkling."),
         ("Planets do not twinkle noticeably", "Planets are much closer "
          "and appear as extended sources (a collection of many points), "
          "so the twinkling from different points averages out.")],
        notes="Contrast with why stars appear steady when viewed from "
              "space (no atmosphere) — reinforces that twinkling is "
              "purely an atmospheric refraction effect.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Refraction", "Bending of light at a boundary due to a change "
                        "in speed."),
         ("Snell's law", "sin i / sin r = constant = refractive index."),
         ("n = c / v", "Absolute refractive index compares speed in "
                       "vacuum to speed in the medium."),
         ("Critical angle", "sin C = 1/n; beyond it, light undergoes "
                            "total internal reflection."),
         ("TIR applications", "Optical fibres, diamond sparkle, mirage, "
                              "totally reflecting prisms."),
         ("Dispersion & twinkling", "Prisms split white light by "
                                    "wavelength; the atmosphere's "
                                    "changing density makes starlight "
                                    "flicker.")],
        notes="Cold-call each recap point; ask students to state the "
              "formula for critical angle from memory.")

    b.quiz_intro("Quiz 2", "Final Check — TIR, Dispersion & Twinkling", 4)
    b.quiz_q(1, "Critical angle", "The critical angle is the angle of "
             "incidence in the denser medium for which the angle of "
             "refraction is:",
             ["0°", "45°", "90°", "equal to the critical angle"])
    b.quiz_a(1, "C. 90°",
             "At the critical angle the refracted ray grazes along the "
             "boundary surface, making an angle of refraction of exactly "
             "90°.")
    b.quiz_q(2, "TIR condition", "Total internal reflection can occur "
             "only when light travels:",
             ["from a rarer to a denser medium", "from a denser to a "
              "rarer medium, beyond the critical angle", "along the "
              "normal", "through a vacuum"])
    b.quiz_a(2, "B. from a denser to a rarer medium, beyond the critical "
             "angle",
             "Both conditions are needed together: denser-to-rarer travel, "
             "and an angle of incidence greater than the critical angle.")
    b.quiz_q(3, "Diamond", "A diamond sparkles brilliantly mainly because "
             "it has:",
             ["a very low refractive index", "a very high refractive "
              "index and hence a small critical angle", "no refractive "
              "index", "a rough, unpolished surface"])
    b.quiz_a(3, "B. a very high refractive index and hence a small "
             "critical angle",
             "With C ≈ 24.4°, light entering a cut diamond undergoes TIR "
             "repeatedly before it can escape, producing its brilliance.")
    b.quiz_q(4, "Twinkling", "Stars appear to twinkle mainly because of:",
             ["their own changing brightness", "continuously changing "
              "refraction in the Earth's atmosphere", "dispersion by a "
              "prism", "total internal reflection in the star itself"])
    b.quiz_a(4, "B. continuously changing refraction in the Earth's "
             "atmosphere",
             "Air layers of constantly changing density bend starlight by "
             "varying amounts, making its apparent position and "
             "brightness flicker.")

    b.closing("Bending Light, Understanding Nature",
              "From a straw that looks bent in water to the sparkle of a "
              "diamond and the twinkle of a star, refraction explains it "
              "all — one law, endless everyday effects.")
    return b


# ===========================================================================
# S41 — Effects of Electric Current - 1  (heating effect, magnetic effect intro)
# ===========================================================================
def eec1_deck():
    footer = "Effects of Electric Current  •  MSBSHSE Std 10 Science Part 1"
    b = Builder(footer, accent=C["orange"])

    circuit = b.asset("mh10_eec1_circuit", D.simple_circuit("mh10_eec1_circuit"))
    straight = b.asset("mh10_eec1_straight",
                       DM.right_hand_thumb_rule("mh10_eec1_straight"))
    field_wire = b.asset("mh10_eec1_fieldwire",
                         D.field_straight_wire("mh10_eec1_fieldwire"))

    b.title("Std 10 • Science Part 1 • Electricity", "Effects of Electric "
            "Current — 1", "Energy transfer in a circuit  •  Heating "
            "effect  •  Magnetic effect  •  Right-hand thumb rule",
            img=circuit)

    b.objectives([
        "Explain how electrical energy is transferred and used up in a "
        "circuit",
        "State Joule's law of heating and use H = I²Rt",
        "Describe everyday uses of the heating effect of current",
        "State Oersted's discovery of the magnetic effect of current",
        "Apply the right-hand thumb rule to a straight current-carrying "
        "conductor",
        "Describe the magnetic field pattern of a straight wire",
    ])

    # ---- Part 1 : heating effect ----
    b.divider(1, "Part 1", "Energy Transfer and the Heating Effect",
              "How electrical work becomes heat")

    b.text_image(
        "ENERGY TRANSFER", "Energy Transfer in an Electric Circuit",
        ["A cell (or battery) does work to push charge around a circuit; "
         "this electrical energy is converted into other forms by the "
         "components in the circuit.",
         "The work done in moving a charge Q through a potential "
         "difference V is W = VQ; since Q = It, the work done in time t "
         "is W = VIt.",
         "In a purely resistive component (like a heater coil or a bulb "
         "filament), all of this electrical energy is converted into "
         "heat.",
         "This conversion of electrical energy into heat because of the "
         "resistance in the circuit is called the heating effect of "
         "electric current."],
        circuit, img_side="right", panel_title="From battery to heat",
        notes="Link back to V = W/Q from the current-electricity chapter; "
              "this is the same relation used to derive Joule's law.")

    b.statement(
        "JOULE'S LAW", "Joule's Law of Heating",
        "Using Ohm's law (V = IR) in W = VIt gives the heat produced in a "
        "resistor carrying a current for a given time.",
        formula="H = I² R t",
        points=[
            "The heat produced is directly proportional to the square of "
            "the current.",
            "The heat produced is directly proportional to the "
            "resistance.",
            "The heat produced is directly proportional to the time for "
            "which the current flows.",
            "H is in joules when I is in amperes, R in ohms and t in "
            "seconds."],
        notes="Emphasise the squared dependence on current — doubling the "
              "current quadruples the heat produced, not just doubles it.")

    b.worked(
        "WORKED EXAMPLE", "Heat Produced in a Resistor",
        "A current of 2 A flows through a resistor of 10 Ω for 5 minutes. "
        "Calculate the heat produced.",
        ["H = I² R t",
         "t = 5 x 60 = 300 s",
         "H = (2)² x 10 x 300"],
        "H = 12000 J = 12 kJ",
        notes="Remind students to convert time to seconds before "
              "substituting — a very common slip.")

    b.cards(
        "USES", "Everyday Uses of the Heating Effect",
        [("Electric heater / iron", "A coil of high-resistance wire "
          "(nichrome) glows and produces heat when current flows through "
          "it, used for room heaters, electric irons and geysers."),
         ("Incandescent bulb", "A thin tungsten filament heats up so much "
          "that it glows white-hot and emits light; tungsten is used "
          "because it has a very high melting point."),
         ("Electric fuse", "A thin wire of low melting point is placed in "
          "series in a circuit; if the current becomes too large, the "
          "fuse wire heats up, melts and breaks the circuit, protecting "
          "the appliance."),
         ("Soldering iron", "A high-resistance heating element converts "
          "electrical energy to heat to melt solder for joining wires "
          "and components.")],
        icons=["fire", "bulb", "bolt", "gear"],
        notes="Ask students to name the common factor in all four devices "
              "— each deliberately uses a high-resistance element to "
              "maximise I²Rt heating.")

    b.quiz_intro("Quiz 1", "Check — Energy Transfer & Heating", 4)
    b.quiz_q(1, "Energy transfer", "The work done in moving a charge Q "
             "through a potential difference V is given by:",
             ["W = V / Q", "W = VQ", "W = Q / V", "W = V + Q"])
    b.quiz_a(1, "B. W = VQ",
             "Potential difference is defined as work done per unit "
             "charge, so W = VQ (and since Q = It, W = VIt).")
    b.quiz_q(2, "Joule's law", "According to Joule's law of heating, the "
             "heat produced in a resistor is proportional to:",
             ["I and R only", "I², R and t", "I and t only", "R² and I"])
    b.quiz_a(2, "B. I², R and t",
             "H = I²Rt — heat depends on the square of the current, and "
             "directly on resistance and time.")
    b.quiz_q(3, "Numerical", "A current of 3 A flows through a 4 Ω "
             "resistor for 10 s. The heat produced is:",
             ["120 J", "360 J", "40 J", "12 J"])
    b.quiz_a(3, "B. 360 J",
             "H = I²Rt = (3)² x 4 x 10 = 9 x 4 x 10 = 360 J.")
    b.quiz_q(4, "Fuse", "An electric fuse protects a circuit because its "
             "wire:",
             ["has a very high melting point so it never melts",
              "has a low melting point and melts to break the circuit "
              "when current is too high", "is a perfect conductor",
              "increases the current when it gets hot"])
    b.quiz_a(4, "B. has a low melting point and melts to break the "
             "circuit when current is too high",
             "A fuse wire is deliberately chosen to melt (via I²Rt "
             "heating) and break the circuit before the current can "
             "damage the appliance or wiring.")

    # ---- Part 2 : magnetic effect, right-hand thumb rule ----
    b.divider(2, "Part 2", "The Magnetic Effect of Electric Current",
              "Oersted's discovery and the right-hand thumb rule")

    b.bullets(
        "OERSTED'S EXPERIMENT", "Discovery of the Magnetic Effect",
        ["In 1820, Hans Christian Oersted found that a compass needle "
         "placed near a current-carrying wire is deflected.",
         "The needle deflects only when current flows in the wire, and "
         "returns to normal when the current is switched off.",
         "Reversing the direction of the current reverses the direction "
         "of the deflection.",
         "This showed that an electric current produces a magnetic field "
         "around itself — the magnetic effect of electric current, the "
         "basis of electromagnetism."],
        notes="This experiment is historically important: it was the "
              "first evidence linking electricity and magnetism, which "
              "later led to Maxwell's unified theory.")

    b.text_image(
        "STRAIGHT CONDUCTOR", "Field Around a Straight Current-Carrying "
        "Wire",
        ["A long straight wire carrying current produces a magnetic "
         "field whose field lines are concentric circles centred on the "
         "wire, lying in a plane perpendicular to it.",
         "The field is stronger closer to the wire and weaker farther "
         "away — the circles are more crowded near the wire.",
         "Reversing the current reverses the direction of the field "
         "lines (clockwise becomes anticlockwise, viewed from a fixed "
         "end)."],
        field_wire, img_side="right", panel_title="Concentric field "
        "circles",
        notes="Have students trace the field-line circles with their "
              "finger around a pencil representing the wire.")

    b.text_image(
        "RIGHT-HAND THUMB RULE", "Finding the Direction of the Field",
        ["Maxwell's right-hand thumb rule gives a quick way to find the "
         "direction of the magnetic field around a straight conductor.",
         "Hold the current-carrying conductor in your right hand with "
         "the thumb pointing in the direction of the conventional "
         "current.",
         "Your curled fingers then point in the direction of the "
         "magnetic field lines around the wire.",
         "By convention, a dot (⊙) shows the field or current coming out "
         "of the page, and a cross (⊗) shows it going into the page."],
        straight, img_side="right", panel_title="Thumb = current, curl = "
        "field",
        notes="Demonstrate physically with your own hand and the "
              "diagram side by side; this rule is used repeatedly "
              "through the rest of the chapter.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Heating effect", "Electrical energy converts to heat in a "
                            "resistor: H = I²Rt."),
         ("Uses", "Heaters, bulb filaments, fuses and soldering irons all "
                 "use the heating effect."),
         ("Oersted's experiment", "A current-carrying wire deflects a "
                                  "nearby compass needle — proof of the "
                                  "magnetic effect."),
         ("Straight wire field", "Concentric circular field lines around "
                                 "the wire."),
         ("Right-hand thumb rule", "Thumb along the current, curled "
                                   "fingers show the field direction.")],
        notes="Ask a student to physically demonstrate the right-hand "
              "thumb rule for the class.")

    b.quiz_intro("Quiz 2", "Final Check — Magnetic Effect", 4)
    b.quiz_q(1, "Oersted", "Oersted's experiment showed that a "
             "current-carrying wire:",
             ["repels a nearby wire", "deflects a nearby compass needle",
              "heats up a nearby magnet", "has no effect on a compass"])
    b.quiz_a(1, "B. deflects a nearby compass needle",
             "The deflection, seen only while current flows, proved that "
             "current produces a magnetic field.")
    b.quiz_q(2, "Field pattern", "The magnetic field lines around a "
             "long straight current-carrying wire are:",
             ["straight lines parallel to the wire", "concentric circles "
              "centred on the wire", "radial lines pointing away from "
              "the wire", "randomly scattered"])
    b.quiz_a(2, "B. concentric circles centred on the wire",
             "The field forms circles in a plane perpendicular to the "
             "wire, crowded closer to the wire where the field is "
             "stronger.")
    b.quiz_q(3, "Right-hand thumb rule", "In the right-hand thumb rule, "
             "the thumb points along the:",
             ["magnetic field", "current", "force on the wire", "normal "
              "to the wire"])
    b.quiz_a(3, "B. current",
             "Thumb = direction of conventional current; curled fingers "
             "= direction of the magnetic field.")
    b.quiz_q(4, "Reversal", "If the current in a straight wire is "
             "reversed, the magnetic field around it:",
             ["disappears completely", "also reverses direction",
              "stays exactly the same", "becomes twice as strong"])
    b.quiz_a(4, "B. also reverses direction",
             "Reversing the thumb direction in the right-hand rule "
             "reverses the curl of the fingers, so the field direction "
             "flips too.")

    b.closing("Current in Motion, Heat and Magnetism",
              "The same flowing charge that warms a heater coil also "
              "conjures a magnetic field around every wire — two effects, "
              "one current.")
    return b


def build():
    jobs = [
        ("MH10_S28_Refraction_of_Light.pptx", refraction_deck),
        ("MH10_S41_Effects_of_Electric_Current_1.pptx", eec1_deck),
    ]
    for fname, fn in jobs:
        b = fn()
        issues = b.qa()
        path = os.path.join(OUT, fname)
        b.save(path)
        print(f"\n=== {fname} ===")
        print(f"slides: {len(b.prs.slides._sldIdLst)}")
        if issues:
            print("QA ISSUES:")
            for i in issues:
                print("  -", i)
        else:
            print("QA: no overlaps / off-slide shapes detected")


if __name__ == "__main__":
    build()
