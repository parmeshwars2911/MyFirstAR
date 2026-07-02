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
import mhstyle
import diagrams_mh as DM

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "MH_Grade10"))
os.makedirs(OUT, exist_ok=True)
mhstyle.apply()


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
    prism = b.asset("mh10_refr_prism", D.prism_refraction("mh10_refr_prism"))

    b.title("Std 10 • Science Part 1 • Light", "Refraction of Light",
            "Laws of refraction  •  Refractive index  •  Total internal "
            "reflection  •  Dispersion  •  Twinkling of stars", img=bend)

    b.objectives([
        "Explain refraction, the laws of refraction and refractive index",
        "Trace a ray through a rectangular glass slab and define lateral "
        "displacement",
        "Distinguish partial internal reflection from total internal "
        "reflection and use the critical angle",
        "Describe how TIR explains optical fibres, mirage and diamond "
        "sparkle",
        "Explain refraction and dispersion of light through a prism",
        "Explain atmospheric refraction: advance sunrise, delayed sunset "
        "and the twinkling of stars",
    ])

    # ---- Part 1 : refraction, laws, refractive index ----
    b.divider(1, "Part 1", "Refraction and Refractive Index",
              "Why light bends, and how we measure the bending")

    b.text_image(
        "REFRACTION", "What Is Refraction?",
        ["Light bends when it crosses between two media — refraction",
         "Into a denser medium → bends towards the normal",
         "Into a rarer medium → bends away from the normal",
         "Along the normal → no bending",
         "Cause: light travels at a different speed in each medium"],
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

    b.text_image(
        "GLASS SLAB", "Refraction Through a Rectangular Glass Slab",
        ["Refracts twice — on entering and on leaving",
         "Parallel faces bend it back by an equal amount",
         "Emergent ray stays parallel to the incident ray",
         "But shifted sideways — lateral displacement",
         "Shift grows with slab thickness and angle of incidence"],
        block, img_side="right", panel_title="Emergent ray is parallel "
        "but shifted",
        notes="Stress the two key facts examiners look for: the emergent "
              "ray is parallel to the incident ray, and it is laterally "
              "displaced.")

    b.quiz_intro("Quiz 1", "Check — Laws, Refractive Index & Glass Slab", 5)
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
    b.quiz_q(5, "Glass slab", "After passing through a rectangular glass "
             "slab, the emergent ray is:",
             ["bent towards the normal", "parallel to the incident ray "
              "but laterally displaced", "reflected straight back", "split "
              "into seven colours"])
    b.quiz_a(5, "B. parallel to the incident ray but laterally displaced",
             "The two equal-and-opposite refractions at the parallel "
             "faces keep the emergent ray parallel to the incident ray, "
             "but shift it sideways (lateral displacement).")

    # ---- Part 2 : partial & total internal reflection, prism, dispersion,
    # atmospheric refraction ----
    b.divider(2, "Part 2", "Internal Reflection, Prism & Atmospheric "
              "Refraction", "Critical angle, the prism, dispersion and "
              "sky phenomena")

    b.bullets(
        "PARTIAL & TOTAL", "Partial and Total Internal Reflection",
        [("Partial internal reflection", "When light travels from a "
          "denser to a rarer medium at a small angle of incidence, most "
          "of it refracts out (bending away from the normal) while a "
          "small part is reflected back into the denser medium — this is "
          "partial internal reflection."),
         ("As the angle increases", "As the angle of incidence in the "
          "denser medium is increased, the refracted ray bends more and "
          "more towards the boundary and grows fainter, while the "
          "reflected ray grows brighter."),
         ("At the critical angle", "The critical angle (C) is the angle "
          "of incidence in the denser medium for which the angle of "
          "refraction becomes 90°; the refracted ray just grazes along "
          "the surface."),
         ("Beyond the critical angle", "If the angle of incidence exceeds "
          "the critical angle, no light refracts out at all — all of it "
          "is reflected back into the denser medium. This is total "
          "internal reflection (TIR).")],
        notes="Emphasise the progression: partial internal reflection "
              "always accompanies refraction, but TIR is a special "
              "case that only begins once the critical angle is "
              "exceeded.")

    b.text_image(
        "CONDITIONS FOR TIR", "The Two Conditions for Total Internal "
        "Reflection",
        ["Both conditions must hold together:",
         "1. Denser medium → rarer medium (e.g. glass → air)",
         "2. Angle of incidence > critical angle",
         "Then no light refracts out — all is reflected",
         "The boundary acts like a perfect mirror"],
        tir, img_side="left", panel_title="When the surface acts as a "
        "mirror",
        notes="Contrast with the previous slide: below the critical "
              "angle you get refraction plus partial reflection; only "
              "above it do you get true total internal reflection.")

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
        ["Hot day → air near the ground is hot and rarer",
         "Sky-light bends more through each hotter layer",
         "It undergoes total internal reflection upward",
         "We see an inverted patch of sky on the road",
         "It looks just like a pool of water"],
        mirage, img_side="right", panel_title="The 'water' that isn't "
        "there",
        notes="Link back to the critical-angle condition: TIR happens "
              "here even though there is no sharp single boundary — the "
              "air's density changes gradually with height.")

    b.text_image(
        "PRISM", "Refraction of Light Through a Prism",
        ["Two refractions at two non-parallel faces",
         "Angle between the faces = refracting angle",
         "Emergent ray is NOT parallel to the incident ray",
         "The ray bends towards the base of the prism",
         "This bending is the angle of deviation"],
        prism, img_side="right", panel_title="Bending towards the base",
        notes="Set up the contrast: a slab keeps the ray parallel, a "
              "prism deviates it towards the base — this deviation, being "
              "different for each colour, is what produces dispersion on "
              "the next slide.")

    b.text_image(
        "DISPERSION", "Dispersion of Light Through a Prism",
        ["White light = seven colours (VIBGYOR)",
         "A prism bends each colour by a different amount",
         "Violet bends the most, red the least",
         "The colours emerge as a band — a spectrum",
         "This splitting of white light is called dispersion"],
        disp, img_side="left", panel_title="Splitting white light",
        notes="A rainbow is a natural example of dispersion combined with "
              "internal reflection inside raindrops.")

    b.bullets(
        "ATMOSPHERIC REFRACTION", "Advance Sunrise and Delayed Sunset",
        [("Denser air near the ground", "The Earth's atmosphere is "
          "denser near the surface and gradually becomes rarer with "
          "height, so sunlight bends continuously as it passes down "
          "through it."),
         ("Advance sunrise", "Because of this bending, the Sun's light "
          "reaches us even when the Sun is still slightly below the "
          "horizon, so we see the Sun about two minutes before it "
          "actually rises."),
         ("Delayed sunset", "For the same reason, we continue to see the "
          "Sun for about two minutes after it has actually set below the "
          "horizon — giving roughly four extra minutes of daylight each "
          "day."),
         ("Oval-shaped Sun", "Near the horizon, light from the lower "
          "edge of the Sun is refracted more than that from the upper "
          "edge, so the Sun appears slightly flattened (oval) at sunrise "
          "and sunset.")],
        notes="This is the same atmospheric refraction that causes "
              "twinkling; here it shifts the Sun's apparent position "
              "rather than making it flicker.")

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
        [("Refraction & Snell's law", "Light bends at a boundary; "
                                      "sin i / sin r = refractive index; "
                                      "n = c / v."),
         ("Glass slab", "Emergent ray is parallel to the incident ray "
                        "but laterally displaced."),
         ("Partial vs total reflection", "Below the critical angle: "
                                         "refraction + partial reflection; "
                                         "beyond it (sin C = 1/n): total "
                                         "internal reflection."),
         ("TIR applications", "Optical fibres, diamond sparkle, mirage, "
                              "totally reflecting prisms."),
         ("Prism & dispersion", "A prism deviates light towards its base "
                                "and splits white light into the VIBGYOR "
                                "spectrum."),
         ("Atmospheric refraction", "Advance sunrise, delayed sunset and "
                                    "the twinkling of stars.")],
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


# ===========================================================================
# S43 — Effects of Electric Current - 2  (loop/solenoid field, force on
# a conductor, Fleming's left-hand rule)
# ===========================================================================
def eec2_deck():
    footer = "Effects of Electric Current  •  MSBSHSE Std 10 Science Part 1"
    b = Builder(footer, accent=C["red"])

    solenoid = b.asset("mh10_eec2_solenoid", D.solenoid_field("mh10_eec2_solenoid"))
    motor_force = b.asset("mh10_eec2_motor", D.dc_motor("mh10_eec2_motor"))
    fleming_l = b.asset("mh10_eec2_flh", DM.flemings_rule("mh10_eec2_flh",
                        left=True))

    b.title("Std 10 • Science Part 1 • Electricity", "Effects of Electric "
            "Current — 2", "Field of a circular loop and a solenoid  •  "
            "Force on a current-carrying conductor  •  Fleming's "
            "left-hand rule", img=solenoid)

    b.objectives([
        "Describe the magnetic field due to a circular loop of current",
        "Describe the magnetic field pattern of a solenoid and compare it "
        "with a bar magnet",
        "Explain how the strength of a solenoid's field can be increased",
        "State the factors on which the force on a current-carrying "
        "conductor in a magnetic field depends",
        "Apply Fleming's left-hand rule to find the direction of this "
        "force",
        "Relate this force to the working principle of an electric motor",
    ])

    # ---- Part 1 : loop and solenoid ----
    b.divider(1, "Part 1", "Field of a Loop and a Solenoid",
              "From a single loop to a coil that behaves like a magnet")

    b.bullets(
        "CIRCULAR LOOP", "Magnetic Field Due to a Circular Loop",
        [("Field lines at the loop", "Applying the right-hand thumb rule "
          "at every point of a circular loop shows that the field lines "
          "are circles near the wire, but they become nearly straight "
          "and parallel as you move toward the centre of the loop."),
         ("Field at the centre", "At the centre of the loop, all the "
          "field contributions add up in the same direction, giving the "
          "strongest and most uniform field in that region."),
         ("Increasing the field", "The field at the centre can be "
          "increased by increasing the current or by using a coil of "
          "many turns instead of a single loop — each turn adds its own "
          "contribution."),
         ("Polarity of the loop face", "One face of the current loop "
          "behaves like a north pole and the other like a south pole, "
          "found using the right-hand rule (curl fingers along the "
          "current, thumb gives the north face).")],
        notes="Build up from the straight-wire field of the previous "
              "session: a loop is just a straight wire bent into a "
              "circle, so the same field lines now reinforce at the "
              "centre.")

    b.text_image(
        "SOLENOID", "Magnetic Field of a Solenoid",
        ["A solenoid is a long coil of insulated wire wound in many "
         "closely spaced circular turns.",
         "When current flows through it, the field of each turn adds up "
         "so that the field inside the solenoid is strong and nearly "
         "uniform, directed along its axis.",
         "Outside the solenoid, the field pattern is very similar to "
         "that of a bar magnet — one end behaves like a north pole and "
         "the other like a south pole.",
         "The polarity of the ends is found by the same right-hand rule: "
         "curl the fingers in the direction of the current in the turns, "
         "and the thumb points towards the north-pole end."],
        solenoid, img_side="right", panel_title="A coil that behaves "
        "like a bar magnet",
        notes="This is the working principle of the electromagnet, "
              "already met earlier in the syllabus — connect the two "
              "ideas explicitly.")

    b.cards(
        "STRENGTH OF THE FIELD", "Increasing the Strength of a Solenoid's "
        "Field",
        [("More turns", "Winding more turns of wire in the same length "
          "increases the field, since each turn contributes its own "
          "magnetic field in the same direction."),
         ("More current", "Increasing the current through the solenoid "
          "directly increases the strength of the field it produces."),
         ("Soft-iron core", "Placing a soft-iron core inside the "
          "solenoid greatly increases the field strength, because the "
          "core itself becomes strongly magnetised — this combination "
          "is an electromagnet.")],
        icons=["gear", "bolt", "magnet"],
        notes="These three factors are exactly the ones used to design "
              "strong electromagnets for cranes, bells and motors.")

    b.quiz_intro("Quiz 1", "Check — Loop & Solenoid Fields", 3)
    b.quiz_q(1, "Circular loop", "The magnetic field is strongest and "
             "most uniform at the:",
             ["edge of the loop", "centre of the loop", "far outside the "
              "loop", "nowhere in particular"])
    b.quiz_a(1, "B. centre of the loop",
             "At the centre, the field contributions from every part of "
             "the loop add up in the same direction, giving the "
             "strongest field there.")
    b.quiz_q(2, "Solenoid", "Outside a current-carrying solenoid, the "
             "magnetic field pattern closely resembles that of a:",
             ["straight wire", "bar magnet", "single point charge",
              "circular loop with no current"])
    b.quiz_a(2, "B. bar magnet",
             "A solenoid's external field lines look just like those of "
             "a bar magnet, with one end acting as north and the other "
             "as south.")
    b.quiz_q(3, "Strength", "Which of these will NOT increase the "
             "strength of a solenoid's magnetic field?",
             ["increasing the number of turns", "increasing the current",
              "inserting a soft-iron core", "using a longer connecting "
              "wire outside the solenoid"])
    b.quiz_a(3, "D. using a longer connecting wire outside the solenoid",
             "Only turns, current and a magnetic core (inside the "
             "solenoid) affect its field strength — the length of "
             "ordinary connecting wire outside it makes no difference.")

    # ---- Part 2 : force on a conductor, Fleming's left-hand rule ----
    b.divider(2, "Part 2", "Force on a Current-Carrying Conductor",
              "The motor effect and Fleming's left-hand rule")

    b.text_image(
        "MOTOR EFFECT", "Force on a Conductor in a Magnetic Field",
        ["When a current-carrying conductor is placed in a magnetic "
         "field (not parallel to it), it experiences a force — this is "
         "called the motor effect.",
         "The force is zero when the conductor is parallel to the "
         "field, and maximum when the conductor is perpendicular to the "
         "field.",
         "The magnitude of the force depends on the strength of the "
         "magnetic field, the current in the conductor, and the length "
         "of the conductor in the field.",
         "This force is what makes an electric motor turn, and is used "
         "in loudspeakers and moving-coil meters."],
        motor_force, img_side="left", panel_title="Current + field = "
        "force",
        notes="This is the reverse idea of Oersted's experiment: instead "
              "of current producing a field, here a current in an "
              "external field feels a force.")

    b.statement(
        "FLEMING'S LEFT-HAND RULE", "Finding the Direction of the Force",
        "Fleming's left-hand rule gives the direction of the force on a "
        "current-carrying conductor placed in a magnetic field.",
        img=fleming_l,
        notes="Stretch the thumb, first finger and second finger of the "
              "left hand mutually perpendicular: First finger = Field, "
              "seCond finger = Current, thuMb = Motion (force). "
              "Mnemonic: FBI (Field, current, thrust) or FCM.")

    b.bullets(
        "FLEMING'S LEFT-HAND RULE", "How to Apply the Rule",
        [("First finger", "Point the first finger in the direction of "
          "the magnetic field (B)."),
         ("Second finger", "Point the second finger, held perpendicular "
          "to the first, in the direction of the conventional current "
          "(I)."),
         ("Thumb", "The thumb, held perpendicular to both, then gives "
          "the direction of the force (F) on the conductor — this is "
          "the direction it will move."),
         ("Left hand only", "This rule always uses the left hand; the "
          "right-hand thumb rule and Fleming's right-hand rule (used "
          "for generators, next session) are entirely different rules.")],
        notes="Have the whole class physically form the rule with their "
              "left hand and check it against the diagram just shown.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Circular loop", "Field is strongest and most uniform at the "
                           "centre; each face acts like a magnetic "
                           "pole."),
         ("Solenoid", "Behaves like a bar magnet outside; field can be "
                      "strengthened by more turns, more current or a "
                      "soft-iron core."),
         ("Motor effect", "A current-carrying conductor in a magnetic "
                          "field experiences a force, maximum when "
                          "perpendicular to the field."),
         ("Fleming's left-hand rule", "First finger = Field, second "
                                      "finger = Current, thumb = Force "
                                      "(motion).")],
        notes="Ask students to distinguish the right-hand thumb rule "
              "(field due to current) from Fleming's left-hand rule "
              "(force on a current in a field) — a very common mix-up.")

    b.quiz_intro("Quiz 2", "Final Check — Motor Effect", 4)
    b.quiz_q(1, "Motor effect", "A current-carrying conductor placed "
             "parallel to a magnetic field experiences a force that is:",
             ["maximum", "zero", "constant but not zero", "infinite"])
    b.quiz_a(1, "B. zero",
             "The force is zero when the current is parallel to the "
             "field and maximum when it is perpendicular to the field.")
    b.quiz_q(2, "Fleming's left-hand rule", "In Fleming's left-hand rule, "
             "the second finger represents:",
             ["the magnetic field", "the current", "the resulting "
              "force", "the resistance"])
    b.quiz_a(2, "B. the current",
             "First finger = Field, seCond finger = Current, thuMb = "
             "Motion (force) — the classic FCM mnemonic.")
    b.quiz_q(3, "Factors", "The force on a current-carrying conductor in "
             "a magnetic field does NOT depend on:",
             ["the current in the conductor", "the strength of the "
              "magnetic field", "the colour of the insulation on the "
              "wire", "the length of the conductor in the field"])
    b.quiz_a(3, "C. the colour of the insulation on the wire",
             "The force depends only on the physical quantities current, "
             "field strength and length (and the angle between them) — "
             "not on the wire's appearance.")
    b.quiz_q(4, "Application", "The force on a current-carrying "
             "conductor in a magnetic field is the basic working "
             "principle of a/an:",
             ["electric motor", "electric fuse", "resistor", "voltmeter"])
    b.quiz_a(4, "A. electric motor",
             "An electric motor uses this force, acting on the two "
             "sides of a current-carrying coil, to produce a turning "
             "effect (torque).")

    b.closing("Current Feels a Push",
              "Field around a wire, force on a wire in a field — these "
              "two effects, tied together by Fleming's left-hand rule, "
              "are what spin every electric motor.")
    return b


# ===========================================================================
# S45 — Effects of Electric Current - 3  (motor, EMI, galvanometer,
# Faraday's law, Fleming's right-hand rule, AC/DC, generator)
# ===========================================================================
def eec3_deck():
    footer = "Effects of Electric Current  •  MSBSHSE Std 10 Science Part 1"
    b = Builder(footer, accent=C["purple"])

    motor = b.asset("mh10_eec3_motor", D.dc_motor("mh10_eec3_motor"))
    emi = b.asset("mh10_eec3_emi", D.emi_coil("mh10_eec3_emi"))
    fleming_r = b.asset("mh10_eec3_frh", DM.flemings_rule("mh10_eec3_frh",
                        left=False))

    b.title("Std 10 • Science Part 1 • Electricity", "Effects of Electric "
            "Current — 3", "Electric motor  •  Electromagnetic induction  "
            "•  Faraday's laws  •  AC/DC generators", img=motor)

    b.objectives([
        "Describe the construction and working of a simple DC electric "
        "motor",
        "Explain the principle and working of a moving-coil galvanometer",
        "Describe Faraday's experiments and state Faraday's laws of "
        "electromagnetic induction",
        "Apply Fleming's right-hand rule to find the direction of an "
        "induced current",
        "Distinguish between alternating current (AC) and direct "
        "current (DC)",
        "Describe the construction and working of an AC generator",
    ])

    # ---- Part 1 : motor, galvanometer ----
    b.divider(1, "Part 1", "The Electric Motor and the Galvanometer",
              "Turning electrical energy into motion, and detecting "
              "current")

    b.text_image(
        "ELECTRIC MOTOR", "Construction and Working of a DC Motor",
        ["A simple DC motor has a rectangular coil (the armature) "
         "mounted between the poles of a permanent magnet, connected to "
         "the circuit through a split-ring commutator and brushes.",
         "When current flows through the coil, the two sides of the "
         "coil carry current in opposite directions; by Fleming's "
         "left-hand rule, they experience forces in opposite "
         "directions.",
         "These two opposite forces form a couple that rotates the "
         "coil.",
         "The split-ring commutator reverses the current in the coil "
         "every half rotation, so the forces keep acting in a "
         "direction that continues the rotation instead of reversing "
         "it."],
        motor, img_side="right", panel_title="Turning current into "
        "rotation",
        notes="Emphasise the role of the commutator specifically — "
              "without it, the coil would rotate only a quarter turn "
              "and then oscillate back and forth.")

    b.bullets(
        "GALVANOMETER", "The Moving-Coil Galvanometer",
        [("Purpose", "A galvanometer is a sensitive instrument used to "
          "detect the presence and direction of a small electric "
          "current in a circuit."),
         ("Principle", "It works on the same motor-effect principle as "
          "an electric motor: a current-carrying coil placed in a "
          "magnetic field experiences a torque (turning force)."),
         ("Construction", "A coil is wound on a light aluminium frame, "
          "suspended between the poles of a permanent magnet, attached "
          "to a pointer moving over a scale."),
         ("Reading", "The coil rotates by an amount proportional to the "
          "current flowing through it, so the pointer's deflection "
          "indicates both the size and the direction of the current.")],
        notes="Contrast with the motor: a motor is designed to keep "
              "spinning continuously and do mechanical work, while a "
              "galvanometer is designed to rotate only slightly and "
              "settle at a reading.")

    b.quiz_intro("Quiz 1", "Check — Motor & Galvanometer", 3)
    b.quiz_q(1, "DC motor", "In a simple DC motor, the split-ring "
             "commutator's job is to:",
             ["increase the magnetic field", "reverse the current in the "
              "coil every half rotation so it keeps turning one way",
              "stop the coil from rotating", "convert AC to DC before "
              "it enters the motor"])
    b.quiz_a(1, "B. reverse the current in the coil every half rotation "
             "so it keeps turning one way",
             "Without this reversal, the forces on the coil would "
             "reverse direction each half turn and the coil would just "
             "oscillate instead of spinning continuously.")
    b.quiz_q(2, "Motor principle", "The rotation of a DC motor's coil is "
             "a direct result of:",
             ["Faraday's law of induction", "the force on a "
              "current-carrying conductor in a magnetic field",
              "the heating effect of current", "static electricity"])
    b.quiz_a(2, "B. the force on a current-carrying conductor in a "
             "magnetic field",
             "The two sides of the coil feel oppositely directed forces "
             "(Fleming's left-hand rule), forming a couple that turns "
             "the coil.")
    b.quiz_q(3, "Galvanometer", "A galvanometer is used to:",
             ["produce a magnetic field", "detect the presence and "
              "direction of a small current", "generate electricity",
              "store electric charge"])
    b.quiz_a(3, "B. detect the presence and direction of a small "
             "current",
             "Its pointer deflection, caused by the motor-effect torque "
             "on its coil, shows both the size and the direction of the "
             "current.")

    # ---- Part 2 : EMI, Faraday, Fleming's right-hand rule, AC/DC ----
    b.divider(2, "Part 2", "Electromagnetic Induction and Generators",
              "Producing current from a changing magnetic field")

    b.text_image(
        "ELECTROMAGNETIC INDUCTION", "Faraday's Experiments",
        ["Michael Faraday found that moving a bar magnet in and out of "
         "a coil of wire connected to a galvanometer causes the "
         "galvanometer's needle to deflect — showing a current is "
         "induced in the coil.",
         "The needle deflects only while the magnet is moving; it shows "
         "no deflection when the magnet is held still inside or outside "
         "the coil.",
         "Moving the magnet faster produces a larger deflection, and "
         "reversing the direction of motion reverses the direction of "
         "deflection.",
         "This production of an electromotive force (EMF), and hence a "
         "current, by a changing magnetic field is called "
         "electromagnetic induction (EMI)."],
        emi, img_side="left", panel_title="A moving magnet induces "
        "current",
        notes="Point out this is the reverse process of the motor "
              "effect: there, current + field gave motion; here, "
              "relative motion between field and coil gives current.")

    b.statement(
        "FARADAY'S LAWS", "Faraday's Laws of Electromagnetic Induction",
        "First law: whenever the magnetic flux linked with a coil "
        "changes, an EMF is induced in the coil; this induced EMF lasts "
        "only as long as the flux is changing.",
        points=[
            "Second law: the magnitude of the induced EMF is directly "
            "proportional to the rate of change of magnetic flux linked "
            "with the coil.",
            "A faster change in flux (e.g. moving the magnet faster, or "
            "using more turns) induces a larger EMF.",
            "If the coil forms a closed circuit, this induced EMF drives "
            "an induced current through it."],
        notes="Flux can change either by moving the magnet, moving the "
              "coil, or changing the current in a nearby coil — all "
              "three are used in different generators and transformers.")

    b.statement(
        "FLEMING'S RIGHT-HAND RULE", "Finding the Direction of the "
        "Induced Current",
        "Fleming's right-hand rule gives the direction of the induced "
        "current when a conductor moves through a magnetic field.",
        img=fleming_r,
        notes="Stretch the thumb, first finger and second finger of the "
              "RIGHT hand mutually perpendicular this time: First "
              "finger = Field, thuMb = Motion, seCond finger = induced "
              "Current. Contrast explicitly with the left-hand rule "
              "from the previous session.")

    b.cards(
        "AC vs DC", "Alternating Current and Direct Current",
        [("Direct current (DC)", "Current that flows in only one "
          "direction, with a magnitude that may be steady or varying, "
          "but never reverses — supplied by cells and batteries."),
         ("Alternating current (AC)", "Current that regularly reverses "
          "its direction and changes magnitude, repeating this pattern "
          "at a fixed frequency — this is what mains electricity "
          "supplies to homes."),
         ("Why AC for transmission", "AC can be easily stepped up or "
          "down in voltage using a transformer, making it far more "
          "efficient to transmit over long distances than DC.")],
        icons=["battery", "bolt", "circuit"],
        notes="Note that household supply in India is AC at 50 Hz, "
              "meaning the current reverses direction 100 times every "
              "second.")

    b.bullets(
        "AC GENERATOR", "Construction and Working of an AC Generator",
        ["An AC generator has a rectangular coil (armature) that is "
         "mechanically rotated between the poles of a magnet.",
         "As the coil rotates, the magnetic flux linked with it "
         "continuously changes, so by Faraday's law an EMF is induced "
         "in the coil.",
         "The ends of the coil are connected to the external circuit "
         "through two separate slip rings and brushes (not a split-ring "
         "commutator), so the induced current is allowed to reverse "
         "direction — giving alternating current.",
         "The direction of the induced current at any instant is given "
         "by Fleming's right-hand rule."],
        notes="Contrast the slip rings of an AC generator with the "
              "split-ring commutator of a DC motor — this is the key "
              "construction difference students often confuse.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("DC motor", "Current-carrying coil in a field turns due to a "
                      "couple of forces; a commutator keeps it "
                      "rotating one way."),
         ("Galvanometer", "Same motor-effect principle, used to detect "
                          "small currents."),
         ("Faraday's laws", "A changing magnetic flux induces an EMF, "
                            "proportional to its rate of change."),
         ("Fleming's right-hand rule", "First finger = Field, thumb = "
                                       "Motion, second finger = induced "
                                       "Current."),
         ("AC generator", "Rotating coil + slip rings gives an "
                          "alternating induced current.")],
        notes="Ask students to state, in one sentence each, the "
              "difference between a motor and a generator (energy "
              "conversion runs in opposite directions).")

    b.quiz_intro("Quiz 2", "Final Check — EMI & Generators", 4)
    b.quiz_q(1, "Faraday's experiment", "In Faraday's coil-and-magnet "
             "experiment, the galvanometer shows a deflection only "
             "when the magnet is:",
             ["held still inside the coil", "moving relative to the "
              "coil", "held still far away from the coil", "made of "
              "iron"])
    b.quiz_a(1, "B. moving relative to the coil",
             "An EMF is induced only while the magnetic flux through "
             "the coil is changing, which requires relative motion.")
    b.quiz_q(2, "Faraday's second law", "According to Faraday's second "
             "law, the induced EMF is directly proportional to the:",
             ["resistance of the coil", "rate of change of magnetic "
              "flux", "number of cells in the circuit", "colour of the "
              "wire"])
    b.quiz_a(2, "B. rate of change of magnetic flux",
             "A faster-changing flux (faster motion, more turns) "
             "induces a larger EMF.")
    b.quiz_q(3, "Fleming's right-hand rule", "Fleming's right-hand rule "
             "is used to find the direction of:",
             ["the force on a current-carrying conductor", "the "
              "induced current due to motion in a magnetic field", "the "
              "magnetic field around a straight wire", "the resistance "
              "of a conductor"])
    b.quiz_a(3, "B. the induced current due to motion in a magnetic "
             "field",
             "It is the generator-effect rule: First finger = Field, "
             "thuMb = Motion, seCond finger = induced Current.")
    b.quiz_q(4, "AC generator", "An AC generator uses slip rings, "
             "instead of a split-ring commutator, because this allows "
             "the:",
             ["coil to rotate faster", "current in the external circuit "
              "to reverse direction periodically, giving AC", "coil to "
              "stop rotating smoothly", "magnet to become stronger"])
    b.quiz_a(4, "B. current in the external circuit to reverse "
             "direction periodically, giving AC",
             "Slip rings maintain continuous contact without reversing "
             "the connection, so the naturally alternating induced "
             "current is passed on unchanged as AC.")

    b.closing("From Motion to Current, and Back Again",
              "A motor turns current into motion using one hand's rule; "
              "a generator turns motion into current using the other. "
              "Between them lies almost every machine that moves us.")
    return b


def build():
    jobs = [
        ("MH10_S28_Refraction_of_Light.pptx", refraction_deck),
        ("MH10_S41_Effects_of_Electric_Current_1.pptx", eec1_deck),
        ("MH10_S43_Effects_of_Electric_Current_2.pptx", eec2_deck),
        ("MH10_S45_Effects_of_Electric_Current_3.pptx", eec3_deck),
        ("MH10_S64_Lenses.pptx", lenses_deck),
        ("MH10_S71_Space_Missions.pptx", space_deck),
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




# ===========================================================================
# S64 — Lenses
# ===========================================================================
def lenses_deck():
    footer = "Lenses  •  MSBSHSE Std 10 Science Part 1"
    b = Builder(footer, accent=C["blue"])

    types = b.asset("mh10_lens_types", D.lens_types("mh10_lens_types"))
    convex = b.asset("mh10_lens_convex", D.convex_lens_image("mh10_lens_convex"))
    concave = b.asset("mh10_lens_concave",
                      D.concave_lens_image("mh10_lens_concave"))
    magnifier = b.asset("mh10_lens_mag", D.convex_magnifier("mh10_lens_mag"))

    b.title("Std 10 • Science Part 1 • Optics", "Lenses",
            "Types of lenses  •  Images and ray diagrams  •  Lens formula "
            "and power  •  The human eye and defects of vision",
            img=types)

    b.objectives([
        "Identify convex and concave lenses and the terms related to them",
        "Draw ray diagrams for images formed by convex and concave "
        "lenses",
        "Apply the sign convention and the lens formula 1/v − 1/u = 1/f",
        "Calculate magnification and the power of a lens",
        "Describe the human eye and the idea of persistence of vision",
        "Explain the defects of vision and how lenses correct them",
    ])

    # ---- Part 1 : lenses, terms, images ----
    b.divider(1, "Part 1", "Lenses and the Images They Form",
              "Types of lenses, key terms and ray diagrams")

    b.cards(
        "TYPES OF LENSES", "Convex and Concave Lenses",
        [("Convex (converging) lens", "Thicker at the middle than at the "
          "edges. A parallel beam of light passing through it converges "
          "to a real point — the principal focus. It can be seen as a "
          "set of prisms with bases towards the centre."),
         ("Concave (diverging) lens", "Thinner at the middle than at the "
          "edges. A parallel beam passing through it diverges, appearing "
          "to come from a virtual focus on the same side. It behaves "
          "like prisms with bases towards the edges.")],
        icons=["eye", "eye"],
        notes="Use the lens_types diagram to show the cross-section "
              "shapes; connect the converging/diverging behaviour to the "
              "prism model of a lens.")

    b.bullets(
        "KEY TERMS", "Terms Related to a Lens",
        [("Centres of curvature (C₁, C₂)", "The centres of the two "
          "spheres whose surfaces form the two faces of the lens."),
         ("Radii of curvature (R₁, R₂)", "The radii of those two "
          "spheres."),
         ("Principal axis", "The straight line passing through both "
          "centres of curvature (and the optical centre)."),
         ("Optical centre (O)", "The central point of the lens; a ray "
          "passing through it goes straight, without any deviation."),
         ("Principal focus (F)", "The point on the principal axis where "
          "rays parallel to the axis converge (convex) or appear to "
          "diverge from (concave)."),
         ("Focal length (f)", "The distance between the optical centre "
          "and the principal focus.")],
        notes="A lens has two principal foci, one on each side, "
              "equidistant from the optical centre for a thin lens.")

    b.bullets(
        "RAY RULES", "Rules for Drawing Ray Diagrams",
        [("Ray parallel to the principal axis", "After refraction it "
          "passes through the principal focus F (convex) or appears to "
          "come from F (concave)."),
         ("Ray through the optical centre", "Passes straight through "
          "without any deviation."),
         ("Ray through the principal focus", "A ray passing through F "
          "(convex) emerges parallel to the principal axis after "
          "refraction."),
         ("Locating the image", "Any two of these rays are drawn from "
          "the top of the object; the point where they meet (or appear "
          "to meet) locates the image.")],
        notes="Only two rays are needed to fix the image; the third is a "
              "useful check.")

    b.text_image(
        "CONVEX LENS", "Images Formed by a Convex Lens",
        ["The nature, position and size of the image depend on where the "
         "object is placed relative to the focus F and 2F.",
         "For a distant object the image is real, inverted and very "
         "small, formed at F; as the object moves closer the real image "
         "moves out and grows.",
         "When the object is between F and the lens, the image becomes "
         "virtual, erect and magnified — this is how a magnifying glass "
         "works.",
         "A convex lens can therefore form both real images (object "
         "beyond F) and a virtual image (object within F)."],
        convex, img_side="right", panel_title="Real or virtual, "
        "depending on position",
        notes="Walk the object from infinity inward, calling out the "
              "image nature at each stage (at 2F: same size; between F "
              "and 2F: magnified real; within F: magnified virtual).")

    b.text_image(
        "CONCAVE LENS", "Images Formed by a Concave Lens",
        ["A concave lens always diverges the light passing through it.",
         "Whatever the position of the object, a concave lens forms an "
         "image that is always virtual, erect and diminished (smaller "
         "than the object).",
         "The image is always formed on the same side as the object, "
         "between the optical centre and the focus.",
         "Because the image is always the same kind, a concave lens is "
         "easy to identify by the small, upright image it forms."],
        concave, img_side="left", panel_title="Always virtual, erect "
        "and small",
        notes="Contrast sharply with the convex lens, whose image "
              "changes with object position — the concave lens image "
              "never changes in nature.")

    b.quiz_intro("Quiz 1", "Check — Lenses & Images", 4)
    b.quiz_q(1, "Types", "A lens that is thicker at the middle than at "
             "the edges is a:",
             ["concave (diverging) lens", "convex (converging) lens",
              "plane glass slab", "prism"])
    b.quiz_a(1, "B. convex (converging) lens",
             "A convex lens is thicker in the middle and converges a "
             "parallel beam to its principal focus.")
    b.quiz_q(2, "Optical centre", "A ray of light passing through the "
             "optical centre of a thin lens:",
             ["bends towards the focus", "goes straight through without "
              "deviation", "is totally reflected", "emerges parallel to "
              "the axis"])
    b.quiz_a(2, "B. goes straight through without deviation",
             "The optical centre is the one point through which a ray "
             "passes undeviated, which is why it is used in ray "
             "diagrams.")
    b.quiz_q(3, "Concave lens image", "The image formed by a concave "
             "lens is always:",
             ["real, inverted and magnified", "virtual, erect and "
              "diminished", "real and the same size", "virtual and "
              "magnified"])
    b.quiz_a(3, "B. virtual, erect and diminished",
             "A concave (diverging) lens forms a virtual, erect and "
             "smaller image for every position of the object.")
    b.quiz_q(4, "Convex lens application", "A convex lens is used as a "
             "magnifying glass when the object is placed:",
             ["beyond 2F", "at 2F", "between the focus F and the lens",
              "at the focus F"])
    b.quiz_a(4, "C. between the focus F and the lens",
             "With the object within the focal length, a convex lens "
             "forms a virtual, erect and magnified image — the "
             "magnifying-glass action.")

    # ---- Part 2 : formula, power, eye, defects ----
    b.divider(2, "Part 2", "Lens Formula, Power and the Human Eye",
              "Calculations, the eye and defects of vision")

    b.statement(
        "SIGN CONVENTION & LENS FORMULA", "The Lens Formula",
        "Using the Cartesian sign convention (distances measured from "
        "the optical centre; those in the direction of incident light "
        "positive, opposite negative), the object distance u, image "
        "distance v and focal length f are related by the lens formula.",
        formula="1/v − 1/u = 1/f",
        points=[
            "For a convex lens f is positive; for a concave lens f is "
            "negative.",
            "A real image has a positive v; a virtual image has a "
            "negative v.",
            "The object distance u is taken as negative (object on the "
            "left of the lens)."],
        notes="Insist on the sign convention before any numerical — most "
              "errors come from wrong signs, not wrong arithmetic.")

    b.statement(
        "MAGNIFICATION", "Magnification Produced by a Lens",
        "The magnification is the ratio of the height of the image to "
        "the height of the object, and also equals the ratio of image "
        "distance to object distance.",
        formula="m = h′/h = v/u",
        points=[
            "If m is positive, the image is virtual and erect; if "
            "negative, the image is real and inverted.",
            "If |m| > 1 the image is magnified; if |m| < 1 it is "
            "diminished; if |m| = 1 it is the same size as the object."],
        notes="Tie the sign of m back to the sign convention: a real "
              "image (positive v, negative u) gives a negative m, "
              "i.e. inverted.")

    b.worked(
        "WORKED EXAMPLE", "Using the Lens Formula",
        "An object is placed 30 cm in front of a convex lens of focal "
        "length 20 cm. Find the position and nature of the image.",
        ["1/v − 1/u = 1/f, with u = −30 cm, f = +20 cm",
         "1/v = 1/f + 1/u = 1/20 + 1/(−30) = (3 − 2)/60 = 1/60",
         "v = +60 cm (positive → real, inverted image)",
         "m = v/u = 60/(−30) = −2  (real, inverted, magnified 2×)"],
        "v = 60 cm; real, inverted, magnified image",
        notes="Show the substitution of signs explicitly; the positive "
              "v confirms a real image on the far side of the lens.")

    b.statement(
        "POWER OF A LENS", "Power of a Lens and Combination of Lenses",
        "The power of a lens is the reciprocal of its focal length (in "
        "metres); it measures the lens's ability to converge or diverge "
        "light.",
        formula="P = 1 / f (in metres)   •   unit: dioptre (D)",
        points=[
            "A convex lens has positive power; a concave lens has "
            "negative power.",
            "A lens of focal length 20 cm (0.2 m) has power "
            "P = 1/0.2 = +5 D.",
            "When thin lenses are placed in contact, their powers add: "
            "P = P₁ + P₂ + P₃ + ..."],
        notes="Opticians prescribe spectacles in dioptres — connect the "
              "sign of the power to the type of correcting lens needed.")

    b.bullets(
        "THE HUMAN EYE", "The Human Eye and Persistence of Vision",
        [("Eye lens and cornea", "Light enters through the cornea and "
          "the convex eye lens, which together form a real, inverted "
          "image on the retina."),
         ("Accommodation", "The ciliary muscles change the focal length "
          "of the eye lens — thinner for distant objects, thicker for "
          "near ones — so objects at different distances stay in focus."),
         ("Least distance of distinct vision", "The closest distance at "
          "which a normal eye can see an object clearly and without "
          "strain is about 25 cm (the near point)."),
         ("Persistence of vision", "An image continues to be sensed by "
          "the eye for about 1/16 of a second after the object is "
          "removed; rapidly changing still pictures therefore appear as "
          "continuous motion, as in films.")],
        notes="Persistence of vision is the physics behind cinema and "
              "animation — a memorable everyday link.")

    b.cards(
        "DEFECTS OF VISION", "Defects of Vision and Their Correction",
        [("Myopia (short-sightedness)", "The eye can see near objects "
          "clearly but not distant ones; the image of a distant object "
          "forms in front of the retina. Corrected using a concave "
          "(diverging) lens of suitable power."),
         ("Hypermetropia (long-sightedness)", "The eye can see distant "
          "objects clearly but not near ones; the image of a near "
          "object forms behind the retina. Corrected using a convex "
          "(converging) lens."),
         ("Presbyopia", "With age the ciliary muscles weaken and the eye "
          "lens hardens, so both near and distant vision are affected. "
          "Corrected using bifocal lenses (concave upper part, convex "
          "lower part)."),
         ("Cause in general", "These defects arise from the eyeball "
          "being too long or too short, or the eye lens losing its "
          "ability to change focal length.")],
        icons=["eye", "eye", "eye", "eye"],
        notes="Have students match each defect to its correcting lens "
              "and state where the image forms relative to the retina.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Two types of lens", "Convex converges light; concave diverges "
                              "it."),
         ("Ray rules", "Parallel ray → through F; ray through O → "
                       "straight; ray through F → parallel."),
         ("Lens formula", "1/v − 1/u = 1/f, using the sign convention."),
         ("Magnification & power", "m = v/u; P = 1/f in dioptres, + for "
                                  "convex, − for concave."),
         ("Human eye", "Ciliary muscles focus the eye lens; near point "
                      "25 cm; persistence of vision ≈ 1/16 s."),
         ("Vision defects", "Myopia → concave lens; hypermetropia → "
                           "convex lens; presbyopia → bifocals.")],
        notes="Cold-call the correcting lens for each defect and the "
              "unit of lens power.")

    b.quiz_intro("Quiz 2", "Final Check — Formula, Power & the Eye", 4)
    b.quiz_q(1, "Power", "A convex lens has a focal length of 25 cm. Its "
             "power is:",
             ["+4 D", "+0.25 D", "−4 D", "+25 D"])
    b.quiz_a(1, "A. +4 D",
             "P = 1/f(in m) = 1/0.25 = +4 D; the power is positive "
             "because the lens is convex.")
    b.quiz_q(2, "Magnification", "If the magnification produced by a "
             "lens is −2, the image is:",
             ["virtual, erect and magnified", "real, inverted and "
              "magnified", "virtual and diminished", "the same size as "
              "the object"])
    b.quiz_a(2, "B. real, inverted and magnified",
             "A negative magnification means a real, inverted image; "
             "its magnitude of 2 means it is twice the object's size.")
    b.quiz_q(3, "Near point", "The least distance of distinct vision for "
             "a normal human eye is about:",
             ["25 cm", "25 m", "2.5 cm", "1 m"])
    b.quiz_a(3, "A. 25 cm",
             "A normal eye can focus comfortably on objects as close as "
             "about 25 cm — the near point.")
    b.quiz_q(4, "Myopia", "A short-sighted (myopic) person cannot see "
             "distant objects clearly. This defect is corrected using "
             "a:",
             ["convex lens", "concave lens", "prism", "plane mirror"])
    b.quiz_a(4, "B. concave lens",
             "A concave (diverging) lens moves the image of a distant "
             "object back onto the retina, correcting myopia.")

    b.closing("Lenses: Bending Light to See",
              "From a magnifying glass to the lens in your own eye, the "
              "same simple rules of refraction let us focus light, form "
              "images and correct how we see the world.")
    return b


# ===========================================================================
# S71 — Space Missions
# ===========================================================================
def space_deck():
    footer = "Space Missions  •  MSBSHSE Std 10 Science Part 1"
    b = Builder(footer, accent=C["purple"])

    orbit = b.asset("mh10_space_orbit", DM.satellite_orbit("mh10_space_orbit"))
    rocket = b.asset("mh10_space_rocket",
                     DM.launch_vehicle_stages("mh10_space_rocket"))

    b.title("Std 10 • Science Part 1 • Space", "Space Missions",
            "Artificial satellites and orbits  •  Escape velocity  •  "
            "Launch vehicles  •  India's space programme", img=orbit)

    b.objectives([
        "Explain what a space mission and an artificial satellite are",
        "Classify satellites by their use and by their orbits",
        "Define orbital velocity and escape velocity",
        "Describe how a multi-stage launch vehicle places a satellite in "
        "orbit",
        "Outline India's major space missions and achievements",
        "Explain what space debris is and why its management matters",
    ])

    # ---- Part 1 : satellites, orbits, velocities ----
    b.divider(1, "Part 1", "Satellites, Orbits and Velocities",
              "What keeps a satellite up, and what it takes to get there")

    b.bullets(
        "SPACE MISSIONS", "Space Missions and Artificial Satellites",
        [("Space mission", "A planned journey or project to send a "
          "spacecraft, satellite or probe into space to study the "
          "Earth, other bodies or space itself."),
         ("Artificial satellite", "A man-made object deliberately placed "
          "into orbit around the Earth (or another body) to perform a "
          "specific task."),
         ("Why it stays in orbit", "The satellite moves fast enough "
          "along its path that the Earth's gravity, acting as the "
          "centripetal force, keeps bending it into a closed orbit "
          "instead of pulling it straight down."),
         ("Uses of satellites", "Communication, weather forecasting, "
          "broadcasting, navigation (GPS), remote sensing, and "
          "scientific research.")],
        notes="Link back to the Gravitation chapter: an orbiting "
              "satellite is in continuous free fall, with gravity "
              "providing exactly the centripetal force it needs.")

    b.cards(
        "TYPES OF SATELLITE", "Classifying Satellites by Their Orbit",
        [("Geostationary satellite", "Orbits about 36,000 km above the "
          "equator with a period of 24 hours, so it appears fixed over "
          "one spot on Earth. Ideal for communication and "
          "broadcasting."),
         ("Polar (sun-synchronous) satellite", "Orbits at a much lower "
          "height (a few hundred km) passing over the poles, scanning "
          "different strips of the Earth on each pass. Used for weather "
          "and remote sensing."),
         ("Low, medium and high orbits", "Satellites are also grouped by "
          "orbit height as Low Earth Orbit (LEO), Medium Earth Orbit "
          "(MEO) and geostationary/high orbit, each suited to different "
          "tasks."),
         ("By purpose", "Communication, weather, navigation, "
          "earth-observation (remote sensing), military and scientific "
          "satellites.")],
        icons=["compass", "compass", "star", "star"],
        notes="Contrast the geostationary satellite (fixed over one "
              "point, high orbit) with the polar satellite (low, "
              "scanning) — a very common comparison question.")

    b.statement(
        "ORBITAL & ESCAPE VELOCITY", "Two Important Speeds",
        "A satellite must be given exactly the right speed to stay in a "
        "circular orbit — its orbital velocity — while a body needs a "
        "much larger speed to leave the Earth's gravity altogether.",
        points=[
            "Orbital velocity is the horizontal speed a satellite needs "
            "so that gravity keeps it in a stable orbit; it decreases "
            "as the orbit's height increases.",
            "Escape velocity is the minimum speed a body must be given "
            "to escape the Earth's gravitational field completely.",
            "For the Earth, the escape velocity is about 11.2 km/s.",
            "Escape velocity depends on the mass and radius of the "
            "planet, not on the mass of the escaping body."],
        notes="Emphasise that escape velocity is independent of the "
              "escaping object's mass — a common conceptual question.")

    b.quiz_intro("Quiz 1", "Check — Satellites & Orbits", 4)
    b.quiz_q(1, "Geostationary", "A geostationary satellite appears to "
             "stay fixed above one point on the Earth because its "
             "orbital period is:",
             ["1 hour", "12 hours", "24 hours", "1 month"])
    b.quiz_a(1, "C. 24 hours",
             "A geostationary satellite orbits over the equator with a "
             "period of 24 hours, matching the Earth's rotation, so it "
             "stays above the same point.")
    b.quiz_q(2, "Polar satellite", "Compared with a geostationary "
             "satellite, a polar satellite orbits at a:",
             ["much greater height", "much lower height, passing over "
              "the poles", "fixed point over the equator", "height of "
              "exactly 36,000 km"])
    b.quiz_a(2, "B. much lower height, passing over the poles",
             "Polar satellites orbit only a few hundred kilometres up "
             "and pass over the poles, scanning fresh strips of the "
             "Earth — ideal for weather and remote sensing.")
    b.quiz_q(3, "Orbit force", "The force that keeps an artificial "
             "satellite moving in its orbit around the Earth is:",
             ["magnetic force", "the Earth's gravitational force acting "
              "as centripetal force", "air resistance", "the satellite's "
              "own thrust"])
    b.quiz_a(3, "B. the Earth's gravitational force acting as "
             "centripetal force",
             "Gravity continuously pulls the satellite towards the "
             "Earth, providing the centripetal force that bends its "
             "path into an orbit.")
    b.quiz_q(4, "Escape velocity", "The escape velocity of a body from "
             "the Earth's surface is about:",
             ["9.8 m/s", "11.2 km/s", "3 × 10⁸ m/s", "300 km/s"])
    b.quiz_a(4, "B. 11.2 km/s",
             "About 11.2 km/s is the minimum speed needed to escape the "
             "Earth's gravity completely; it does not depend on the "
             "mass of the escaping body.")

    # ---- Part 2 : launch vehicles, India's missions, debris ----
    b.divider(2, "Part 2", "Launch Vehicles and India's Space Programme",
              "Getting to orbit, and what India has achieved")

    b.text_image(
        "LAUNCH VEHICLES", "Satellite Launch Vehicles",
        ["A satellite is carried into orbit by a launch vehicle (rocket) "
         "that works on the principle of conservation of momentum — hot "
         "gases are thrown out backwards, pushing the rocket forwards.",
         "A single rocket cannot carry enough fuel, so multi-stage "
         "launch vehicles are used: each stage burns its fuel and then "
         "separates, so the remaining rocket becomes lighter.",
         "The lowest, largest stage fires first and is dropped once "
         "empty; the upper stages then fire in turn to reach the "
         "required speed and height.",
         "India's ISRO has developed launch vehicles such as the PSLV "
         "(Polar Satellite Launch Vehicle) and the GSLV (Geosynchronous "
         "Satellite Launch Vehicle)."],
        rocket, img_side="right", panel_title="Why rockets have stages",
        notes="Connect the staging idea to efficiency: dropping empty "
              "stages means the engine no longer has to accelerate dead "
              "weight.")

    b.cards(
        "INDIA IN SPACE", "India's Major Space Missions",
        [("Chandrayaan-1 (2008)", "India's first mission to the Moon; it "
          "confirmed the presence of water molecules on the lunar "
          "surface."),
         ("Mangalyaan (2013)", "The Mars Orbiter Mission made India the "
          "first country to reach Mars orbit on its very first "
          "attempt, and at remarkably low cost."),
         ("Chandrayaan-2 & 3", "Follow-up Moon missions; Chandrayaan-3 "
          "achieved a successful soft landing near the Moon's south "
          "pole, a world first for that region."),
         ("India and space technology", "ISRO launches communication, "
          "weather and remote-sensing satellites for India and for "
          "other countries, making India a major space-faring "
          "nation.")],
        icons=["moon", "star", "moon", "compass"],
        notes="Keep the dates approximate; the key learning outcome is "
              "the significance of each mission, not rote memorisation.")

    b.bullets(
        "SPACE DEBRIS", "Space Debris and Its Management",
        [("What it is", "Space debris is the collection of non-working "
          "man-made objects orbiting the Earth — spent rocket stages, "
          "dead satellites and fragments from collisions."),
         ("Why it is dangerous", "Debris travels at very high speed, so "
          "even a small piece can seriously damage or destroy a working "
          "satellite or spacecraft it strikes."),
         ("Growing problem", "As more satellites are launched, the "
          "amount of debris grows, increasing the risk of collisions "
          "and threatening the future use of near-Earth space."),
         ("Management", "Agencies track debris, design satellites to "
          "de-orbit and burn up at the end of their life, and plan "
          "missions to remove large pieces of debris.")],
        notes="A modern, discussion-friendly topic — ask students why "
              "clearing space debris is an international responsibility.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Artificial satellite", "A man-made body orbiting the Earth, "
                                 "held in orbit by gravity acting as "
                                 "centripetal force."),
         ("Types", "Geostationary (24 h, fixed over equator) vs polar "
                   "(low, over the poles); grouped by orbit and by "
                   "purpose."),
         ("Two speeds", "Orbital velocity keeps a satellite in orbit; "
                       "escape velocity (≈ 11.2 km/s) lets a body leave "
                       "Earth."),
         ("Launch vehicles", "Multi-stage rockets (PSLV, GSLV) work by "
                            "conservation of momentum."),
         ("India's missions", "Chandrayaan-1/2/3 and Mangalyaan — Moon "
                             "and Mars achievements."),
         ("Space debris", "Dangerous orbiting junk that must be tracked "
                          "and managed.")],
        notes="Cold-call students for the difference between orbital "
              "and escape velocity and one Indian mission's "
              "significance.")

    b.quiz_intro("Quiz 2", "Final Check — Launch Vehicles & Missions", 4)
    b.quiz_q(1, "Staging", "Multi-stage rockets are used to launch "
             "satellites because:",
             ["they look impressive", "dropping each empty stage means "
              "the rocket no longer has to carry and accelerate dead "
              "weight", "a single stage is illegal", "they need no "
              "fuel"])
    b.quiz_a(1, "B. dropping each empty stage means the rocket no longer "
             "has to carry and accelerate dead weight",
             "Shedding spent stages makes the remaining rocket lighter, "
             "so the same thrust can accelerate it to the high speed "
             "needed for orbit.")
    b.quiz_q(2, "Rocket principle", "A launch vehicle moves forward by "
             "throwing hot gases backwards. This is an application of:",
             ["Ohm's law", "conservation of momentum", "Snell's law",
              "the lens formula"])
    b.quiz_a(2, "B. conservation of momentum",
             "The backward momentum given to the exhaust gases is "
             "balanced by an equal forward momentum of the rocket.")
    b.quiz_q(3, "Indian missions", "India's Mars Orbiter Mission is also "
             "known as:",
             ["Chandrayaan", "Mangalyaan", "Aryabhata", "PSLV"])
    b.quiz_a(3, "B. Mangalyaan",
             "Mangalyaan (the Mars Orbiter Mission) made India the first "
             "country to reach Mars orbit on its first attempt.")
    b.quiz_q(4, "Space debris", "Space debris is a serious hazard mainly "
             "because it:",
             ["blocks sunlight", "travels at very high speed and can "
              "damage working satellites on impact", "is radioactive",
              "increases the Earth's gravity"])
    b.quiz_a(4, "B. travels at very high speed and can damage working "
             "satellites on impact",
             "Even a tiny fragment moving at orbital speed carries "
             "enough energy to cripple a satellite it strikes, so debris "
             "must be tracked and managed.")

    b.closing("Reaching for the Stars",
              "From understanding why a satellite stays up to landing "
              "near the Moon's south pole, space missions turn the "
              "physics of gravity and motion into humanity's journey "
              "beyond the Earth.")
    return b


if __name__ == "__main__":
    build()
