"""
Grade 10 Physics — Chapter: Refraction of Light at Plane Surfaces.
Builds two teaching decks (Session 34 = Lesson 1, Session 35 = Lesson 2).

Content scoped to the ICSE Class 10 (Selina / Concise Physics) treatment of
the chapter, matching the topic list in the planner.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt", "Grade10"))
os.makedirs(OUT, exist_ok=True)

FOOTER1 = "Refraction of Light at Plane Surfaces  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER1, accent=C["teal"])
    # diagrams
    bend1 = D.refraction_bending("g10r1_bend_denser", denser_below=True)
    bend2 = D.refraction_bending("g10r1_bend_rarer", denser_below=False)
    snell = D.refraction_bending("g10r1_snell", denser_below=True)
    block = D.glass_block("g10r1_block")

    # 1 title
    b.title("ICSE • Class 10 • Optics", "Refraction of Light",
            "Bending of light at plane surfaces  •  Laws of refraction  •  "
            "Refractive index  •  The glass block", img=bend1)
    # 2 objectives
    b.objectives([
        "Explain what refraction is and why it happens",
        "State and apply the two laws of refraction (Snell's law)",
        "Define refractive index and relate it to the speed of light",
        "Use n = c / v for the speed of light in a medium",
        "Trace a ray through a rectangular glass block",
        "Describe lateral displacement and multiple images in thick glass",
    ])
    # 3 part 1
    b.divider(1, "Part 1", "What Refraction Is",
              "Bending of light when it changes medium")
    # 4 definition
    b.text_image("REFRACTION", "What Is Refraction?",
                 ["Refraction is the bending of light as it passes from one "
                  "transparent medium into another.",
                  "It happens because the speed of light is different in "
                  "different media.",
                  "The bending takes place only at the boundary (surface) "
                  "separating the two media.",
                  "A ray entering along the normal does not bend."],
                 bend1, img_side="left", panel_title="Definition",
                 caption="Air → glass: ray bends toward the normal",
                 notes="Define refraction, then ask students why a straw in a "
                       "glass of water looks bent. Emphasise the change in "
                       "speed is the cause, and bending only happens at the "
                       "surface.")
    # 5 cause / rules
    b.cards("WHICH WAY DOES IT BEND?", "The Two Rules of Bending", [
        ("Rarer → Denser", "Going into a denser medium (air → glass), light "
         "slows down and bends TOWARD the normal."),
        ("Denser → Rarer", "Going into a rarer medium (glass → air), light "
         "speeds up and bends AWAY from the normal."),
        ("Along the normal", "A ray that strikes the surface at 90° (along the "
         "normal) passes straight through, un-bent."),
        ("At the boundary", "Bending happens only at the surface; inside a "
         "uniform medium the ray travels in a straight line."),
    ], notes="Drill the toward/away rule — it is the single most tested idea. "
             "Use the swimmer-in-mud analogy: the part of the line that "
             "enters the denser medium first slows, swinging the ray toward "
             "the normal.")
    # 6 second bending diagram
    b.text_image("DENSER → RARER", "Bending Away From the Normal",
                 ["When light leaves a denser medium for a rarer one it speeds "
                  "up.",
                  "The refracted ray bends away from the normal.",
                  "So the angle of refraction is larger than the angle of "
                  "incidence.",
                  "This is exactly the reverse of the air → glass case."],
                 bend2, img_side="right", panel_title="Glass → Air",
                 caption="Glass → air: ray bends away from the normal",
                 notes="Contrast directly with the previous slide. Stress that "
                       "the path is reversible — same diagram, arrows flipped.")
    # 7 refractive index
    b.statement("REFRACTIVE INDEX", "Refractive Index (n)",
                "The refractive index of a medium measures how much it bends "
                "light — how much it slows light down compared with vacuum.",
                formula="n  =  speed of light in vacuum (c)  /  speed of "
                        "light in medium (v)",
                points=["Refractive index has no unit (it is a ratio).",
                        "A higher n means light travels slower and bends more.",
                        "For air n ≈ 1.0; the denser the medium, the larger n.",
                        "It also equals sin i / sin r (from Snell's law)."],
                notes="Define absolute refractive index. Make the link: bigger "
                      "n → slower light → more bending. Mention n is a pure "
                      "ratio, hence no unit.")
    # 8 speed in media
    b.bullets("SPEED OF LIGHT", "Speed of Light in Different Media", [
        ("Vacuum / air", "c = 3 × 10⁸ m/s — the fastest light can travel."),
        ("Water", "v ≈ 2.25 × 10⁸ m/s, so n ≈ 1.33."),
        ("Glass", "v ≈ 2.0 × 10⁸ m/s, so n ≈ 1.5."),
        ("Diamond", "v ≈ 1.24 × 10⁸ m/s, so n ≈ 2.42 — bends light the most."),
        ("Key relation", "n = c / v  →  the smaller the speed v, the larger n."),
    ], panel_title="Light slows down in a denser medium",
       notes="Read the table as a story: as we move to denser media the speed "
             "falls and n rises. Diamond's huge n is why it sparkles.")
    # 9 laws of refraction
    b.statement("LAWS OF REFRACTION", "The Two Laws of Refraction",
                "Snell's law: the ratio of sin i to sin r is constant for a "
                "given pair of media.",
                formula="sin i  /  sin r  =  n   (a constant)",
                points=["Law 1: The incident ray, the refracted ray and the "
                        "normal at the point of incidence all lie in one "
                        "plane.",
                        "Law 2 (Snell's law): sin i / sin r = constant = the "
                        "refractive index of the second medium w.r.t. the "
                        "first.",
                        "i = angle of incidence, r = angle of refraction, both "
                        "measured from the normal."],
                notes="State both laws precisely. Snell's law is the workhorse "
                      "for numericals — make sure angles are taken from the "
                      "normal, never the surface.")
    # 10 snell diagram
    b.text_image("SNELL'S LAW", "Reading the Angles",
                 ["Always measure i and r from the normal, not the surface.",
                  "Air → glass: i > r (ray bends toward the normal).",
                  "The constant sin i / sin r is the refractive index n.",
                  "If you know any three of i, r and n you can find the "
                  "fourth."],
                 snell, img_side="left", panel_title="i and r",
                 caption="Angles of incidence (i) and refraction (r)",
                 notes="Point at the diagram: identify the normal first, then "
                       "i, then r. Common error: measuring from the surface.")
    # 11 worked example
    b.worked("WORKED EXAMPLE", "Applying Snell's Law",
             "A ray strikes a glass surface at i = 45°. If the refractive "
             "index of glass is 1.5, find sin r (and hence r).",
             ["Snell's law:  sin i / sin r = n",
              "sin 45° / sin r = 1.5",
              "sin r = sin 45° / 1.5 = 0.707 / 1.5 = 0.471",
              "r = sin⁻¹(0.471) ≈ 28°"],
             "r ≈ 28°  (the ray bends toward the normal, as expected)",
             notes="Set up Snell's law, substitute, solve for sin r, then take "
                   "the inverse sine. Sanity check: r < i because air → glass.")
    # 12 refractive index values + reversibility
    b.text_image("REVERSIBILITY", "Principle of Reversibility",
                 ["If a ray of light retraces its path, it travels back along "
                  "exactly the same route.",
                  "Reverse the refracted ray and it comes out along the "
                  "original incident ray.",
                  "This gives the useful relation:  ₁n₂ × ₂n₁ = 1.",
                  "So the refractive index of glass w.r.t. air is the "
                  "reciprocal of air w.r.t. glass."],
                 bend2, img_side="right", panel_title="Light's path is reversible",
                 caption="Reverse the arrows — the path is unchanged",
                 notes="Demonstrate with the diagram by flipping the arrowheads. "
                       "Introduce the reciprocal relation ₁n₂ = 1 / ₂n₁.")
    # 13 QUIZ 1
    b.quiz_intro("Quiz 1", "Check Your Understanding", 3)
    b.quiz_q(1, "Crossing a Boundary", "A ray of light passes from water "
             "(n = 1.33) into glass (n = 1.5). On entering the glass the ray "
             "will:", ["Bend toward the normal and slow down",
                       "Bend away from the normal and speed up",
                       "Go straight through without bending",
                       "Bend toward the normal and speed up"])
    b.quiz_a(1, "A. Bend toward the normal and slow down",
             "Glass is optically denser than water (higher n), so light slows "
             "down on entering it and bends toward the normal — even though "
             "neither medium is air. Density, not 'air vs glass', decides the "
             "direction of bending.")
    b.quiz_q(2, "What Changes?", "When light passes from air into a glass "
             "block, which of these does NOT change?",
             ["Its speed", "Its wavelength", "Its frequency", "Its direction"])
    b.quiz_a(2, "C. Its frequency",
             "Inside the glass the light slows down and its wavelength "
             "shortens, and at the surface its direction changes. Only the "
             "frequency (set by the source) stays the same — a common exam "
             "trap.")
    b.quiz_q(3, "Comparing Media", "Light travels fastest in the medium with "
             "the:", ["Highest refractive index",
                      "Lowest refractive index",
                      "Largest angle of refraction",
                      "Greatest density"])
    b.quiz_a(3, "B. Lowest refractive index",
             "Since n = c/v, a smaller n means a larger speed v. So light is "
             "fastest in the optically rarest medium (lowest n) — for example "
             "it travels faster in water than in diamond.")
    # 20 part 2
    b.divider(2, "Part 2", "Through a Glass Block",
              "Lateral shift, experiments and thick-glass images")
    # 21 glass block
    b.text_image("GLASS BLOCK", "Through a Rectangular Glass Block",
                 ["The ray refracts twice — once entering and once leaving the "
                  "block.",
                  "At entry (air → glass) it bends toward the normal; at exit "
                  "(glass → air) it bends away.",
                  "The two surfaces are parallel, so the emergent ray is "
                  "parallel to the incident ray.",
                  "But the emergent ray is shifted sideways — this is the "
                  "lateral displacement."],
                 block, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="Two refractions",
                 caption="Emergent ray is parallel but shifted sideways",
                 notes="Trace the ray surface by surface. The headline result: "
                       "emergent ray parallel to incident ray, displaced "
                       "sideways by the lateral shift.")
    # 22 lateral displacement factors
    b.cards("LATERAL SHIFT", "What the Lateral Shift Depends On", [
        ("Thickness", "A thicker glass block gives a larger lateral "
         "displacement."),
        ("Angle of incidence", "A larger angle of incidence increases the "
         "lateral shift."),
        ("Refractive index", "A higher refractive index (denser glass) "
         "increases the shift."),
        ("Zero shift", "At normal incidence (i = 0) there is no bending and no "
         "lateral displacement."),
    ], notes="List the three factors that increase lateral shift, then the "
             "special case of normal incidence giving zero shift.")
    # 23 experiment
    b.bullets("EXPERIMENT", "Finding the Refractive Index of Glass", [
        "Place the glass block on paper and trace its outline.",
        "Draw a normal and an incident ray; fix two pins on it.",
        "Looking from the other side, fix two more pins so all four appear in "
        "a straight line.",
        "Remove the block and join the pin marks to draw the emergent ray and "
        "the refracted ray inside the block.",
        "Measure the angles i and r, then compute n = sin i / sin r.",
    ], panel_title="Pin-and-tracing method",
       notes="Walk through the standard ICSE practical. Emphasise the "
             "four-pins-in-a-line condition and that n is found from "
             "sin i / sin r.")
    # 24 multiple images
    b.bullets("THICK GLASS", "Multiple Images in a Thick Mirror", [
        ("Why it happens", "A thick glass mirror reflects light at both the "
         "front glass surface and the silvered back surface."),
        ("Faint first image", "A weak image forms by reflection at the front "
         "surface of the glass."),
        ("Brightest image", "The brightest image is formed by the silvered "
         "back surface — this is the one we use."),
        ("More faint images", "Repeated internal reflections create several "
         "fainter images behind it."),
    ], panel_title="Several images from one object",
       notes="Explain why a thick mirror shows a faint extra image. The "
             "brightest is from the silvered back; partial reflections make "
             "the rest.")
    # 25 real life
    b.cards("REAL LIFE", "Refraction Around Us", [
        ("Bent straw", "A straw in water looks bent at the surface because "
         "light from it refracts on leaving the water."),
        ("Shallow pool", "A pool looks shallower than it is — refraction "
         "raises the apparent position of the bottom."),
        ("Twinkling stars", "Starlight refracts through moving air layers, so "
         "stars appear to twinkle."),
        ("Lenses & prisms", "Spectacles, cameras and prisms all work by "
         "refracting light in a controlled way."),
    ], notes="Connect the physics to everyday sights. Invite students to add "
             "their own examples of bent or raised objects in water.")
    # 26 worked example 2
    b.worked("WORKED EXAMPLE", "Speed of Light in a Medium",
             "The refractive index of water is 1.33. Find the speed of light "
             "in water. (c = 3 × 10⁸ m/s)",
             ["n = c / v   →   v = c / n",
              "v = (3 × 10⁸) / 1.33",
              "v = 2.256 × 10⁸ m/s"],
             "v ≈ 2.26 × 10⁸ m/s  (slower than in air, as expected)",
             notes="Rearrange n = c/v for v. Reinforce that light is slower in "
                   "the denser medium.")
    # 27 recap
    b.recap("WRAP UP", "Quick Recap", [
        ("Refraction", "bending of light when its speed changes between media"),
        ("Toward / away", "to the normal entering denser; away entering rarer"),
        ("Refractive index", "n = c / v = sin i / sin r, no unit"),
        ("Snell's law", "sin i / sin r = constant, angles from the normal"),
        ("Glass block", "emergent ray parallel to incident, shifted sideways"),
        ("Reversibility", "light retraces its path; ₁n₂ × ₂n₁ = 1"),
    ], notes="Rapid recap. Cold-call students to give each result before "
             "revealing it.")
    # 28 QUIZ 2
    b.quiz_intro("Quiz 2", "Final Check — Applying It", 4)
    b.quiz_q(1, "Glass Block", "A ray enters a rectangular glass slab at an "
             "angle of incidence of 50°. What is the angle of emergence as it "
             "leaves the opposite, parallel face?",
             ["Less than 50°", "Exactly 50°", "More than 50°",
              "It depends on the glass thickness"])
    b.quiz_a(1, "B. Exactly 50°",
             "Because the two faces are parallel, the bending on entering is "
             "exactly undone on leaving. The angle of emergence equals the "
             "angle of incidence (50°); the ray is only shifted sideways, not "
             "rotated. Thickness changes the shift, not the angle.")
    b.quiz_q(2, "Refractive Index", "Light travels at 2 × 10⁸ m/s in a "
             "medium. Its refractive index is (c = 3 × 10⁸ m/s):",
             ["0.67", "1.5", "2.0", "6 × 10¹⁶"])
    b.quiz_a(2, "B. 1.5",
             "n = c / v = (3 × 10⁸) / (2 × 10⁸) = 1.5. The refractive index is "
             "a ratio of speeds, so it has no unit.")
    b.quiz_q(3, "Lateral Shift", "The lateral displacement produced by a glass "
             "block is zero when the angle of incidence is:",
             ["45°", "90°", "0° (normal incidence)", "60°"])
    b.quiz_a(3, "C. 0° (normal incidence)",
             "A ray along the normal does not bend, so there is no sideways "
             "displacement. Lateral shift increases as the angle of incidence "
             "increases.")
    b.quiz_q(4, "Reversibility", "If the refractive index of glass with "
             "respect to air is 1.5, the refractive index of air with respect "
             "to glass is:", ["1.5", "0.67", "2.25", "3.0"])
    b.quiz_a(4, "B. 0.67",
             "By the principle of reversibility, ₁n₂ × ₂n₁ = 1. So air w.r.t. "
             "glass = 1 / 1.5 = 0.67.")
    # closing
    b.closing("Light Bends — With Rules",
              "Remember: speed change causes bending, measure angles from the "
              "normal, and n = c / v = sin i / sin r.")
    return b


def deck2():
    """Session 35 — Lesson 2: prism, real & apparent depth, critical angle,
    total internal reflection."""
    b = Builder(FOOTER1, accent=C["purple"])
    prism = D.prism_refraction("g10r2_prism")
    depth = D.real_apparent_depth("g10r2_depth")
    tir = D.total_internal_reflection("g10r2_tir")
    bend = D.refraction_bending("g10r2_bend", denser_below=False)
    fibre = D.optical_fibre("g10r2_fibre")
    rprism = D.reflecting_prism("g10r2_rprism")

    b.title("ICSE • Class 10 • Optics", "Refraction — Prisms & T.I.R.",
            "The prism  •  Real and apparent depth  •  Critical angle  •  "
            "Total internal reflection", img=prism)
    b.objectives([
        "Trace a ray of light through a triangular prism",
        "Define the angle of deviation produced by a prism",
        "Distinguish real depth from apparent depth",
        "Explain everyday effects of refraction",
        "Define the critical angle and relate it to refractive index",
        "State the conditions for total internal reflection and its uses",
    ])
    b.divider(1, "Part 1", "The Prism & Apparent Depth",
              "Deviation, and why things look raised in water")
    b.text_image("THE PRISM", "Refraction Through a Prism",
                 ["A prism has two refracting surfaces inclined at an angle A "
                  "(the angle of the prism).",
                  "Light refracts at both surfaces and bends toward the base "
                  "of the prism.",
                  "The angle between the incident and emergent directions is "
                  "the angle of deviation, δ.",
                  "Unlike a glass block, the emergent ray is NOT parallel to "
                  "the incident ray."],
                 prism, img_side="left", img_w=5.4, img_h=4.0,
                 panel_title="Angle of deviation",
                 caption="Light bends toward the base; deviation = δ",
                 notes="Contrast with the glass block: the surfaces are NOT "
                       "parallel, so the ray is deviated and emerges in a new "
                       "direction.")
    b.bullets("DEVIATION", "What Affects the Deviation", [
        ("Angle of the prism (A)", "A larger refracting angle gives more "
         "deviation."),
        ("Refractive index", "A denser prism material deviates light more."),
        ("Angle of incidence", "Deviation first decreases, reaches a minimum, "
         "then increases."),
        ("Minimum deviation", "At one special angle of incidence the deviation "
         "is least — the angle of minimum deviation."),
    ], panel_title="Deviation δ depends on three things",
       notes="Introduce the idea of minimum deviation qualitatively; the full "
             "formula is not required, but the U-shaped trend is.")
    b.text_image("APPARENT DEPTH", "Real Depth vs Apparent Depth",
                 ["Light from an object under water bends away from the normal "
                  "as it leaves the water.",
                  "Our eyes trace these rays back in straight lines, so the "
                  "object looks raised.",
                  "The apparent depth is always less than the real depth.",
                  "Refractive index = real depth / apparent depth."],
                 depth, img_side="right", panel_title="Things look raised",
                 caption="A coin appears nearer the surface than it is",
                 notes="Use the coin-in-a-mug demo. Give the formula "
                       "n = real depth / apparent depth and note apparent "
                       "depth is always the smaller one.")
    b.worked("WORKED EXAMPLE", "Apparent Depth",
             "A coin lies at the bottom of a tank of water 1.33 m deep. "
             "How deep does it appear? (n_water = 1.33)",
             ["n = real depth / apparent depth",
              "apparent depth = real depth / n",
              "apparent depth = 1.33 / 1.33 = 1.0 m"],
             "Apparent depth = 1.0 m  (the tank looks 0.33 m shallower)",
             notes="Rearrange the depth formula. Stress the answer is smaller "
                   "than the real depth.")
    b.cards("PRISM vs BLOCK", "Prism Compared With a Glass Block", [
        ("Glass block", "Opposite faces are parallel — the emergent ray is "
         "parallel to the incident ray, only shifted sideways."),
        ("Prism", "Faces are inclined at angle A — the emergent ray is "
         "deviated into a new direction."),
        ("Net bending", "A block gives zero net deviation; a prism gives a "
         "definite angle of deviation δ."),
        ("Toward", "A block shifts light sideways; a prism bends light toward "
         "its base."),
    ], notes="Use this side-by-side to cement the difference between parallel "
             "faces (block) and inclined faces (prism).")
    b.cards("CONSEQUENCES", "Everyday Effects of Refraction", [
        ("Early sunrise", "We see the Sun a little before it actually rises, "
         "because light bends through the atmosphere."),
        ("Late sunset", "For the same reason the Sun is seen briefly after it "
         "has actually set."),
        ("Stars twinkle", "Light from stars refracts through moving air "
         "layers, so their brightness flickers."),
        ("Bent / raised look", "Objects in water look bent at the surface and "
         "raised from the bottom."),
    ], notes="Each is a consequence of atmospheric or water refraction. Ask "
             "students which ones they have noticed.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 3)
    b.quiz_q(1, "Prism vs Slab", "How does a prism differ from a parallel-"
             "sided glass slab in its effect on a ray of light?",
             ["Both leave the ray parallel to the incident ray",
              "A prism deviates the ray; a slab only shifts it sideways",
              "A slab deviates the ray; a prism only shifts it",
              "Neither changes the ray's direction"])
    b.quiz_a(1, "B. A prism deviates; a slab only shifts",
             "A slab's faces are parallel, so the emergent ray is parallel to "
             "the incident ray (just shifted). A prism's faces are inclined, "
             "so the ray emerges in a new direction — deviated toward the "
             "base by the angle δ.")
    b.quiz_q(2, "Apparent Depth", "A fish is 2.0 m below the surface of a "
             "pond (n = 1.33). To a person looking straight down, the fish "
             "appears to be about how deep?",
             ["2.66 m", "2.0 m", "1.5 m", "1.33 m"])
    b.quiz_a(2, "C. 1.5 m",
             "Apparent depth = real depth / n = 2.0 / 1.33 ≈ 1.5 m. Refraction "
             "raises the apparent position, so the fish looks shallower than "
             "it really is.")
    b.quiz_q(3, "Atmospheric Refraction", "We can see the Sun for a few "
             "minutes before it has actually risen above the horizon because:",
             ["The Sun moves faster at dawn",
              "Light from the Sun is refracted by the atmosphere",
              "The Sun is closer at sunrise",
              "Clouds reflect the sunlight"])
    b.quiz_a(3, "B. Light is refracted by the atmosphere",
             "Air is denser nearer the ground, so sunlight bends as it passes "
             "through the atmosphere. This lifts the Sun's apparent position, "
             "letting us see it slightly before it actually rises (and after "
             "it sets).")
    b.divider(2, "Part 2", "Critical Angle & T.I.R.",
              "When light cannot escape a denser medium")
    b.text_image("CRITICAL ANGLE", "The Critical Angle",
                 ["As light goes denser → rarer, it bends away from the "
                  "normal.",
                  "Increase the angle of incidence and the refracted ray bends "
                  "more and more toward the surface.",
                  "At the critical angle (C) the refracted ray grazes along "
                  "the surface (r = 90°).",
                  "Relation:  n = 1 / sin C, so a larger n gives a smaller "
                  "critical angle."],
                 tir, img_side="left", img_w=5.4, img_h=4.0,
                 panel_title="Definition of C",
                 caption="At i = C the refracted ray grazes the surface",
                 notes="Build up the critical angle by imagining the angle of "
                       "incidence growing. Give n = 1/sin C and the values "
                       "(water ≈ 49°, glass ≈ 42°, diamond ≈ 24°).")
    b.statement("T.I.R.", "Total Internal Reflection",
                "When light travelling in a denser medium hits the surface at "
                "an angle greater than the critical angle, it is completely "
                "reflected back into the denser medium.",
                formula="Condition:  denser → rarer   AND   i  >  C",
                points=["No light is refracted out — the surface acts like a "
                        "perfect mirror.",
                        "Both conditions must hold: light must go from denser "
                        "to rarer, and i must exceed the critical angle.",
                        "T.I.R. loses no light, unlike an ordinary mirror."],
                notes="State both conditions clearly. Highlight that T.I.R. is "
                      "a perfect, loss-free reflection — the basis of its many "
                      "uses.")
    b.bullets("CRITICAL ANGLE", "Critical Angle of Common Media", [
        ("Water", "n ≈ 1.33, so critical angle C ≈ 49°."),
        ("Ordinary glass", "n ≈ 1.5, so critical angle C ≈ 42°."),
        ("Dense flint glass", "n ≈ 1.65, so critical angle C ≈ 37°."),
        ("Diamond", "n ≈ 2.42, so critical angle C ≈ 24° — the smallest, so "
         "light is trapped most easily."),
        ("Rule", "Larger refractive index  →  smaller critical angle  →  "
         "easier T.I.R."),
    ], panel_title="n = 1 / sin C",
       notes="Have students notice the inverse trend: the denser the medium, "
             "the smaller its critical angle, the more readily it traps light.")
    b.cards("USES OF T.I.R.", "Where Total Internal Reflection Is Used", [
        ("Optical fibres", "Light bounces along the fibre by repeated T.I.R., "
         "carrying internet and phone signals."),
        ("Totally reflecting prisms", "45°–45°–90° prisms turn light through "
         "90° or 180° in periscopes and binoculars."),
        ("Mirage", "Hot air near a road bends light by T.I.R., showing a "
         "shimmering 'puddle' that is really sky."),
        ("Sparkle of diamond", "Diamond's tiny critical angle (≈ 24°) traps "
         "light by repeated T.I.R., making it sparkle."),
    ], notes="Connect each use back to the two conditions. Optical fibres and "
             "the reflecting prism are the most examined.")
    b.text_image("OPTICAL FIBRES", "How an Optical Fibre Works",
                 ["A fibre has a glass core surrounded by a cladding of lower "
                  "refractive index.",
                  "Light enters one end and strikes the core walls beyond the "
                  "critical angle.",
                  "It undergoes total internal reflection again and again, "
                  "zig-zagging down the fibre.",
                  "Almost no light escapes, so signals travel long distances "
                  "with very little loss."],
                 fibre, img_side="right", img_w=5.6, img_h=3.7,
                 panel_title="Light trapped by T.I.R.",
                 caption="Repeated T.I.R. guides the light along the core",
                 notes="Stress the core/cladding refractive-index condition. "
                       "This is the most important real-world application.")
    b.text_image("REFLECTING PRISMS", "Totally Reflecting Prisms",
                 ["A 45°–45°–90° glass prism has a critical angle (≈ 42°) "
                  "smaller than 45°.",
                  "Light hitting the long face at 45° therefore exceeds the "
                  "critical angle and is totally reflected.",
                  "One reflection turns light through 90°; two reflections turn "
                  "it through 180°.",
                  "These prisms replace mirrors in periscopes, binoculars and "
                  "cameras because they lose no light."],
                 rprism, img_side="left", img_w=4.6, img_h=4.0,
                 panel_title="A perfect mirror from glass",
                 caption="45° incidence > critical angle → 90° turn",
                 notes="Explain why 45° works: it beats glass's 42° critical "
                       "angle. Contrast with a silvered mirror, which absorbs "
                       "some light.")
    b.worked("WORKED EXAMPLE", "Critical Angle from Refractive Index",
             "The refractive index of glass is 1.5. Find its critical angle.",
             ["n = 1 / sin C   →   sin C = 1 / n",
              "sin C = 1 / 1.5 = 0.667",
              "C = sin⁻¹(0.667) ≈ 42°"],
             "Critical angle of glass ≈ 42°",
             notes="Apply n = 1/sin C. Note the result (~42°) is the standard "
                   "value students should remember for glass.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Prism", "two inclined faces; light bends toward the base, deviation δ"),
        ("Apparent depth", "n = real depth / apparent depth; things look raised"),
        ("Consequences", "early sunrise, late sunset, twinkling stars"),
        ("Critical angle", "r = 90° at i = C; n = 1 / sin C"),
        ("T.I.R.", "denser → rarer and i > C; perfect, loss-free reflection"),
        ("Uses", "optical fibres, reflecting prisms, mirage, diamond sparkle"),
    ], notes="Rapid recap; cold-call for each result.")
    b.quiz_intro("Quiz 2", "Final Check — Critical Angle & T.I.R.", 4)
    b.quiz_q(1, "Will It Escape?", "Light inside glass (critical angle 42°) "
             "strikes the glass–air surface at 40°. What happens?",
             ["It is totally internally reflected",
              "It refracts and passes out into the air",
              "It travels along the surface",
              "It is absorbed by the glass"])
    b.quiz_a(1, "B. It refracts and passes out",
             "40° is less than the critical angle of 42°, so the ray is still "
             "refracted out of the glass (bending away from the normal). T.I.R. "
             "would only happen if the angle exceeded 42°.")
    b.quiz_q(2, "Diamond vs Glass", "A diamond (critical angle ≈ 24°) sparkles "
             "more than a glass crystal (critical angle ≈ 42°) because:",
             ["Diamond reflects all colours equally",
              "Light meets its surfaces beyond the critical angle more often",
              "Diamond is a better conductor",
              "Glass absorbs more light"])
    b.quiz_a(2, "B. Light exceeds the critical angle more often",
             "A smaller critical angle means more rays strike the inner "
             "surfaces beyond it and undergo total internal reflection. So "
             "diamond traps and bounces light around far more than glass, "
             "giving its sparkle.")
    b.quiz_q(3, "Refractive Index", "If the critical angle of a medium is 30°, "
             "its refractive index is:", ["0.5", "1.5", "2.0", "1.0"])
    b.quiz_a(3, "C. 2.0",
             "n = 1 / sin C = 1 / sin 30° = 1 / 0.5 = 2.0.")
    b.quiz_q(4, "Application", "Optical fibres carry light signals mainly by "
             "using:", ["Dispersion", "Total internal reflection",
                        "Diffraction", "Ordinary reflection"])
    b.quiz_a(4, "B. Total internal reflection",
             "Light entering a fibre strikes the walls beyond the critical "
             "angle and undergoes repeated T.I.R., travelling along the fibre "
             "with almost no loss.")
    b.closing("Trapping Light",
              "Beyond the critical angle, light cannot escape — that is how "
              "optical fibres carry the world's data.")
    return b


def build():
    results = []
    for fname, fn in [("G10_S34_Refraction_at_Plane_Surfaces_1.pptx", deck1),
                      ("G10_S35_Refraction_at_Plane_Surfaces_2.pptx", deck2)]:
        b = fn()
        issues = b.qa()
        path = os.path.join(OUT, fname)
        b.save(path)
        results.append((fname, len(b.prs.slides.__iter__.__self__._sldIdLst), issues))
        print(f"\n=== {fname} ===")
        print(f"slides: {len(b.prs.slides._sldIdLst)}")
        if issues:
            print("QA ISSUES:")
            for i in issues:
                print("  -", i)
        else:
            print("QA: no overlaps / off-slide shapes detected")
    return results


if __name__ == "__main__":
    build()
