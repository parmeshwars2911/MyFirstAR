"""
Grade 7 Physics teaching decks (ICSE / Selina Concise Physics).

Chapters covered (teach-sessions after day 29 in the planner):
  - Light Energy            : S37 (Lesson 1), S38 (Lesson 2)
  - Heat                    : S55 (Lesson 1), S56 (Lesson 2), S57 (Lesson 3)
  - Sound                   : S66 (Lesson 1), S67 (Lesson 2)
  - Electricity & Magnetism : S76 (Lesson 1), S77 (Lesson 2), S78 (Lesson 3)

Language is pitched for Class 7. Schematics come from diagrams.py /
diagrams_extra.py (SVG -> PNG). Feature cards use slidekit.cards() so each card
carries a small white pictogram (icon). Optional real photos are picked up by
b.asset(key, fallback) when they have been generated into assets/img/ (see
manifest_g7.json + tools/qwen_assets.py); otherwise the SVG schematic is used.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import diagrams_g7 as DX  # Grade-7 schematics (kept separate from G6's diagrams_extra)
import slidekit as SK

# House style for every deck below (no footer/branding on slides, neutral
# title eyebrows, and quiz answer slides that mirror the question slide with
# the correct option selected). Applied via a one-time monkeypatch so none of
# the b.title / b.quiz_q / b.quiz_a call sites need editing.
SK.apply_house_style()

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade07"))
os.makedirs(OUT, exist_ok=True)


# ===========================================================================
# LIGHT ENERGY  (S37, S38)
# ===========================================================================
def light_deck1():
    """S37 — Light Energy 1: reflection, terms, laws of reflection +
    verification, normal incidence, image formation by a plane mirror."""
    b = Builder("Light Energy  •  ICSE Class 7 Physics", accent=C["orange"])
    law = D.reflection_law("g7l1_law")
    law2 = D.reflection_law("g7l1_law2")
    normal = DX.normal_incidence("g7l1_normal")
    mirror = DX.plane_mirror_image("g7l1_mirror")

    b.title("ICSE • Class 7 • Optics", "Light & Reflection",
            "How light bounces back  •  The laws of reflection  •  Images in a "
            "plane mirror", img=b.asset("g7_mirror_photo", law))
    b.objectives([
        "Recall that light is a form of energy that travels in straight lines",
        "Define reflection and the terms used to describe it",
        "State the two laws of reflection of light",
        "Describe an experiment to verify the laws of reflection",
        "Explain what happens at normal incidence",
        "Explain how a plane mirror forms an image",
    ])

    # ---- Part 1 : Reflection and its laws ----
    b.divider(1, "Part 1", "Reflection of Light",
              "How light bounces off a surface, and the rules it obeys")
    b.statement("REFLECTION", "What Is Reflection?",
                "Reflection is the bouncing back of light into the same medium "
                "when it falls on a smooth, polished surface such as a mirror.",
                points=["Light is a form of energy that travels in straight "
                        "lines.",
                        "When light strikes a surface, part of it bounces back "
                        "— this bouncing back is called reflection.",
                        "A highly polished surface (a mirror) reflects almost "
                        "all the light that falls on it.",
                        "We see most objects by the light they reflect into "
                        "our eyes."],
                notes="Open from what students already know: light travels "
                      "straight and lets us see. Then sharpen 'reflection' as "
                      "the bouncing back of light at a polished surface. Stress "
                      "we see non-luminous things by reflected light.")
    b.text_image("THE TERMS", "The Words We Use for Reflection",
                 ["The ray that strikes the mirror is the incident ray.",
                  "The ray that bounces back is the reflected ray.",
                  "The line drawn at 90° to the mirror at the point of "
                  "incidence is the normal.",
                  "The angle of incidence (i) and angle of reflection (r) are "
                  "both measured from the normal."],
                 law, img_side="left", panel_title="Key terms",
                 caption="Incident ray, reflected ray and the normal",
                 notes="Point to each part on the diagram: incident ray, point "
                       "of incidence, normal, reflected ray. Insist that i and "
                       "r are always measured from the NORMAL, never from the "
                       "mirror surface — this is the commonest error.")
    SK.cards(b, "TERMS AT A GLANCE", "Four Terms to Remember", [
        ("Incident ray", "The ray of light that travels toward and strikes the "
         "reflecting surface."),
        ("Reflected ray", "The ray of light that bounces back from the surface "
         "into the same medium."),
        ("Normal", "The line drawn perpendicular (at 90°) to the surface at the "
         "point of incidence."),
        ("Angles i and r", "The angle of incidence and angle of reflection, "
         "each measured from the normal."),
    ], icons=["force", "force", "ruler", "target"],
       notes="Drill the four terms with the diagram still on screen. Ask "
             "students to come up and label a fresh ray diagram on the board.")
    b.statement("LAWS OF REFLECTION", "The Two Laws of Reflection",
                "The angle of incidence is always equal to the angle of "
                "reflection.",
                formula="Angle of incidence (i)  =  Angle of reflection (r)",
                points=["Law 1: The incident ray, the reflected ray and the "
                        "normal at the point of incidence all lie in the same "
                        "plane.",
                        "Law 2: The angle of incidence is equal to the angle of "
                        "reflection (i = r).",
                        "These two laws are obeyed at every reflecting surface, "
                        "flat or curved.",
                        "Both angles are measured between the ray and the "
                        "normal."],
                notes="State both laws precisely. Law 2 (i = r) is the one used "
                      "in numericals; Law 1 is about everything lying in one "
                      "plane. Emphasise the laws hold for ALL surfaces.")
    b.text_image("READING THE ANGLES", "Measuring i and r",
                 ["First draw the normal at the point where the ray hits.",
                  "Measure the angle of incidence i between the incident ray "
                  "and the normal.",
                  "Measure the angle of reflection r between the reflected ray "
                  "and the normal.",
                  "For a plane mirror you will always find i = r."],
                 law2, img_side="right", panel_title="i = r",
                 caption="Both angles are measured from the normal",
                 notes="Walk through the measuring steps in order: normal "
                       "first, then i, then r. A protractor placed against the "
                       "surface (not the normal) is the classic mistake to "
                       "warn against.")
    b.bullets("EXPERIMENT", "Verifying the Laws of Reflection", [
        "Fix a sheet of white paper on a drawing board and draw a straight "
        "line MM′ for the mirror; stand a plane mirror on it.",
        "Draw a normal at a point O on the mirror line, then draw an incident "
        "ray and fix two pins P and Q on it.",
        "Look into the mirror and fix two more pins R and S so that they appear "
        "in a straight line with the images of P and Q.",
        "Remove the mirror and pins, join the marks to get the reflected ray, "
        "and measure the angles i and r with a protractor.",
    ], panel_title="Pin-and-mirror method",
       notes="Describe the standard ICSE practical. The 'four pins appear in "
             "one straight line' condition is the heart of it. The result: i = "
             "r within experimental error, verifying the second law.")
    b.text_image("NORMAL INCIDENCE", "When Light Hits Head-On",
                 ["If a ray falls along the normal, the angle of incidence is "
                  "0°.",
                  "By the law of reflection the angle of reflection is also "
                  "0°.",
                  "So the ray is reflected straight back along its own path.",
                  "This special case is called normal incidence."],
                 normal, img_side="left", img_w=5.2, img_h=3.8,
                 panel_title="i = r = 0°",
                 caption="A head-on ray returns along the same line",
                 notes="Use this as a neat check of the law: with i = 0 the "
                       "reflected ray must also make 0° with the normal, so it "
                       "retraces its path. This is how a mirror at the back of "
                       "a torch sends light straight back.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Reflection", 4)
    b.quiz_q(1, "Definition", "Reflection of light is best described as light:",
             ["Passing through a medium", "Bouncing back from a surface",
              "Being absorbed by a surface", "Bending at a surface"])
    b.quiz_a(1, "B. Bouncing back from a surface",
             "Reflection is the bouncing back of light into the same medium "
             "when it strikes a smooth, polished surface such as a mirror.")
    b.quiz_q(2, "Terms", "The angle of incidence is measured between the "
             "incident ray and the:", ["Mirror surface", "Reflected ray",
                                        "Normal", "Horizontal"])
    b.quiz_a(2, "C. The normal",
             "Both the angle of incidence and the angle of reflection are "
             "measured from the normal — the line drawn at 90° to the surface "
             "at the point of incidence — never from the surface itself.")
    b.quiz_q(3, "Laws", "According to the second law of reflection:",
             ["i is greater than r", "i is less than r", "i is equal to r",
              "i and r are unrelated"])
    b.quiz_a(3, "C. i is equal to r",
             "The second law of reflection states that the angle of incidence "
             "equals the angle of reflection (i = r) at every reflecting "
             "surface.")
    b.quiz_q(4, "Normal incidence", "A ray of light strikes a plane mirror "
             "along the normal. The reflected ray will:",
             ["Travel along the mirror", "Return along the same path",
              "Bend by 45°", "Be absorbed"])
    b.quiz_a(4, "B. Return along the same path",
             "At normal incidence i = 0°, so r = 0° too. The ray is reflected "
             "straight back along its own path.")

    # ---- Part 2 : The plane mirror and its image ----
    b.divider(2, "Part 2", "Images in a Plane Mirror",
              "How a flat mirror builds the picture you see")
    SK.cards(b, "PLANE MIRROR", "The Plane Mirror", [
        ("What it is", "A plane mirror is a flat, smooth reflecting surface — "
         "usually a glass sheet silvered on the back."),
        ("Regular reflection", "Its smooth surface reflects parallel rays as "
         "parallel rays, so it forms a clear image."),
        ("The image", "Look into it and you see an image that seems to lie "
         "behind the mirror."),
        ("Everyday use", "The looking-glass on a wall and a dressing-table "
         "mirror are plane mirrors."),
    ], icons=["eye", "eye", "camera", "star"],
       notes="Define the plane mirror and remind students its surface is very "
             "smooth, which is why the image is sharp. Set up the question: "
             "where exactly is the image and what is it like?")
    b.text_image("IMAGE FORMATION", "How the Image Is Formed",
                 ["Two rays leave a point on the object and reflect from the "
                  "mirror, obeying i = r.",
                  "The reflected rays spread out (diverge) as they enter the "
                  "eye.",
                  "Our brain assumes light travels straight, so it traces the "
                  "rays back behind the mirror.",
                  "The rays appear to meet behind the mirror — that is where "
                  "the image is seen."],
                 mirror, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="Rays traced back",
                 caption="The image lies as far behind as the object is in "
                         "front",
                 notes="Trace two rays from one point of the object. The "
                       "reflected rays only seem to come from behind the "
                       "mirror — there is no real light there, so the image is "
                       "virtual. Measure: image distance equals object "
                       "distance.")
    b.bullets("THE IMAGE", "Where the Image Is", [
        ("As far behind", "The image is formed as far behind the mirror as the "
         "object is in front of it."),
        ("Same size", "The image is exactly the same size as the object."),
        ("Erect", "The image is upright (erect), the same way up as the "
         "object."),
        ("Virtual", "The image cannot be caught on a screen, because the rays "
         "only appear to meet behind the mirror."),
    ], panel_title="First look at the image",
       notes="Introduce the key facts about the plane-mirror image here; the "
             "full list of characteristics, including lateral inversion, comes "
             "in the next lesson. Stress 'virtual = cannot be caught on a "
             "screen'.")
    b.worked("WORKED EXAMPLE", "Angle Between the Rays",
             "A ray of light strikes a plane mirror so that the angle of "
             "incidence is 35°. Find (a) the angle of reflection and (b) the "
             "angle between the incident and reflected rays.",
             ["By the law of reflection, angle of reflection r = i = 35°.",
              "The incident and reflected rays lie on opposite sides of the "
              "normal.",
              "Angle between them = i + r = 35° + 35°.",
              "Angle between the rays = 70°."],
             "(a) r = 35°   (b) angle between the rays = 70°",
             notes="Apply i = r, then add the two angles because they sit on "
                   "either side of the normal. A good follow-up: ask what the "
                   "angle would be at normal incidence (answer: 0°).")
    b.text_image("MOVING MIRRORS", "A Quick Consequence",
                 ["If you walk toward a plane mirror, your image walks toward "
                  "you at the same speed.",
                  "If you move away, the image moves away by the same amount.",
                  "Because image distance always equals object distance.",
                  "The image is always the same size — it never grows or "
                  "shrinks as you move."],
                 mirror, img_side="right", img_w=5.6, img_h=4.0,
                 panel_title="Image keeps pace",
                 caption="Image distance always equals object distance",
                 notes="A nice everyday check: the image keeps pace with you "
                       "because the equal-distance rule holds at every moment. "
                       "Many students wrongly think the image gets bigger as "
                       "you approach — it does not.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Reflection", "light bounces back from a smooth, polished surface"),
        ("Terms", "incident ray, reflected ray, normal; i and r from the "
         "normal"),
        ("Laws", "all rays + normal in one plane; i = r"),
        ("Verifying", "pin-and-mirror method shows i = r"),
        ("Normal incidence", "i = 0° so the ray returns along its own path"),
        ("Plane-mirror image", "virtual, erect, same size, equally far "
         "behind"),
    ], notes="Rapid recap; cold-call students for each point. Spend the most "
             "time on i = r and the equal-distance rule for the image.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Mirrors & Images", 4)
    b.quiz_q(1, "Image distance", "An object is placed 8 cm in front of a "
             "plane mirror. Its image is formed:",
             ["4 cm behind the mirror", "8 cm behind the mirror",
              "8 cm in front of the mirror", "16 cm behind the mirror"])
    b.quiz_a(1, "B. 8 cm behind the mirror",
             "The image in a plane mirror is formed as far behind the mirror "
             "as the object is in front, so it is 8 cm behind the mirror.")
    b.quiz_q(2, "Nature of image", "The image formed by a plane mirror is:",
             ["Real and inverted", "Real and erect", "Virtual and erect",
              "Virtual and inverted"])
    b.quiz_a(2, "C. Virtual and erect",
             "A plane mirror forms a virtual image (it cannot be caught on a "
             "screen) that is erect and the same size as the object.")
    b.quiz_q(3, "Angles", "A ray hits a plane mirror at an angle of incidence "
             "of 50°. The angle between the incident and reflected rays is:",
             ["50°", "90°", "100°", "130°"])
    b.quiz_a(3, "C. 100°",
             "The angle of reflection equals the angle of incidence (50°). The "
             "rays lie on opposite sides of the normal, so the angle between "
             "them is 50° + 50° = 100°.")
    b.quiz_q(4, "Reasoning", "We can move a plane-mirror image but never catch "
             "it on a screen because the image is:",
             ["Real", "Virtual", "Larger than the object", "Inverted"])
    b.quiz_a(4, "B. Virtual",
             "The reflected rays only appear to meet behind the mirror, where "
             "no real light reaches, so the image is virtual and cannot be "
             "formed on a screen.")

    b.closing("Light Obeys the Rules",
              "Reflection is simple but exact: i = r at every surface, and a "
              "plane mirror builds a virtual, equal-size image just behind the "
              "glass.")
    return b


def light_deck2():
    """S38 — Light Energy 2: real vs virtual images, lateral inversion,
    characteristics of a plane-mirror image, regular vs irregular reflection,
    uses of a plane mirror, speed of light, colours of white light."""
    b = Builder("Light Energy  •  ICSE Class 7 Physics", accent=C["orange"])
    lat = DX.lateral_inversion("g7l2_lateral")
    mirror = DX.plane_mirror_image("g7l2_mirror")
    regirr = DX.regular_irregular_reflection("g7l2_regirr")
    spectrum = DX.dispersion_spectrum("g7l2_spectrum")
    cadd = DX.colour_addition("g7l2_cadd")
    csub = DX.colour_subtraction("g7l2_csub")

    b.title("ICSE • Class 7 • Optics", "Images & Colour",
            "Real vs virtual images  •  Lateral inversion  •  Uses of mirrors "
            "•  The colours of white light", img=b.asset("g7_rainbow_photo", spectrum))
    b.objectives([
        "Distinguish a real image from a virtual image",
        "Explain lateral inversion in a plane mirror",
        "List the characteristics of an image in a plane mirror",
        "Tell regular reflection apart from irregular reflection",
        "State everyday uses of a plane mirror",
        "Describe the colours that make up white light",
    ])

    # ---- Part 1 : Images and the plane mirror ----
    b.divider(1, "Part 1", "Images & Reflection",
              "Real vs virtual, lateral inversion and the uses of mirrors")
    SK.cards(b, "TWO KINDS OF IMAGE", "Real and Virtual Images", [
        ("Real image", "Formed where reflected or refracted rays actually meet; "
         "it CAN be caught on a screen."),
        ("Virtual image", "Formed where rays only appear to meet; it CANNOT be "
         "caught on a screen."),
        ("Real example", "The image on a cinema screen and the image in a "
         "pinhole camera are real."),
        ("Virtual example", "The image you see in a plane mirror is virtual — "
         "it seems to be behind the glass."),
    ], icons=["camera", "eye", "camera", "eye"],
       notes="Set up the real/virtual distinction with the screen test: a real "
             "image can be thrown on a screen, a virtual one cannot. The "
             "plane-mirror image is the key example of a virtual image.")
    b.text_image("LATERAL INVERSION", "Left Becomes Right",
                 ["In a plane mirror the left and right of the image are "
                  "swapped over.",
                  "This swapping of left and right is called lateral "
                  "inversion.",
                  "Your right hand looks like a left hand in the mirror.",
                  "The word AMBULANCE is written reversed on vehicles so it "
                  "reads correctly in a driver's mirror."],
                 lat, img_side="left", img_w=5.4, img_h=3.6,
                 panel_title="Left ↔ right",
                 caption="The letter F is flipped left-to-right, not top-to-"
                         "bottom",
                 notes="Demonstrate by holding up a hand or a printed word. "
                       "Stress that only left and right are swapped — top and "
                       "bottom stay put. The AMBULANCE example always lands "
                       "well.")
    b.bullets("CHARACTERISTICS", "The Plane-Mirror Image", [
        ("Virtual", "It cannot be caught on a screen."),
        ("Erect", "It is the same way up as the object."),
        ("Same size", "It is exactly as large as the object."),
        ("Equally far behind", "Its distance behind the mirror equals the "
         "object's distance in front."),
        ("Laterally inverted", "Its left and right are interchanged."),
    ], panel_title="Five things to remember",
       notes="This is the most examined list in the chapter. Have students "
             "chant the five characteristics. Link each to the ray diagram "
             "from the previous lesson.")
    b.text_image("SMOOTH OR ROUGH?", "Regular vs Irregular Reflection",
                 ["A smooth surface reflects parallel rays as parallel rays — "
                  "this is regular reflection and gives a clear image.",
                  "A rough surface reflects parallel rays in many directions — "
                  "this is irregular (diffuse) reflection.",
                  "Each tiny part of a rough surface still obeys i = r; the "
                  "surface itself is just uneven.",
                  "Irregular reflection from walls and paper is how we see "
                  "non-shiny objects from all around."],
                 regirr, img_side="right", img_w=5.8, img_h=3.7,
                 panel_title="Same law, different surface",
                 caption="Parallel in: parallel out (smooth) or scattered "
                         "(rough)",
                 notes="The crucial point: the laws of reflection are NEVER "
                       "broken — even a rough wall obeys i = r at each point. "
                       "It only looks scattered because the surface is uneven. "
                       "Diffuse reflection is why we can read a page from any "
                       "angle.")
    SK.cards(b, "USES", "Everyday Uses of a Plane Mirror", [
        ("Looking glass", "The common mirror at home for seeing ourselves, "
         "erect and life-size."),
        ("Periscope", "Two plane mirrors let submarines and soldiers see over "
         "obstacles."),
        ("Kaleidoscope", "Mirrors set at an angle make beautiful repeated "
         "patterns."),
        ("Shop & safety", "Mirrors widen the view in shops, lifts and at blind "
         "road corners."),
    ], icons=["eye", "eye", "star", "target"],
       notes="Go round the uses, drawing the two-mirror periscope quickly on "
             "the board. The kaleidoscope and shop-corner mirror connect the "
             "physics to things students have actually used.")
    b.bullets("REAL OR VIRTUAL?", "Telling the Two Apart", [
        ("Can it land on a screen?", "If yes, the image is real; if no, it is "
         "virtual."),
        ("Which way up?", "Real images are usually inverted; the plane-mirror "
         "virtual image is erect."),
        ("Where do the rays meet?", "Real images form where rays actually "
         "cross; virtual images where rays only seem to cross."),
        ("Plane mirror", "Always gives a virtual, erect image — never a real "
         "one, however far the object is."),
    ], panel_title="A quick test",
       notes="Give students a simple decision rule — the screen test — and "
             "practise it on a few examples (cinema screen, mirror, shadow, "
             "pinhole image).")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Images", 4)
    b.quiz_q(1, "Images", "An image that can be caught on a screen is called:",
             ["A virtual image", "A real image", "An erect image",
              "A laterally inverted image"])
    b.quiz_a(1, "B. A real image",
             "A real image is formed where light rays actually meet, so it can "
             "be caught on a screen — unlike a virtual image, which cannot.")
    b.quiz_q(2, "Lateral inversion", "In a plane mirror, lateral inversion "
             "means that:", ["Top and bottom are swapped",
                              "Left and right are swapped",
                              "The image shrinks", "The image turns upside "
                              "down"])
    b.quiz_a(2, "B. Left and right are swapped",
             "Lateral inversion is the interchange of left and right in a "
             "plane-mirror image. Top and bottom are not affected.")
    b.quiz_q(3, "Reflection types", "Reflection from a rough, uneven surface "
             "is called:", ["Regular reflection", "Irregular reflection",
                             "Total reflection", "No reflection"])
    b.quiz_a(3, "B. Irregular reflection",
             "A rough surface scatters parallel rays in many directions — this "
             "is irregular (diffuse) reflection. Each point still obeys i = r.")
    b.quiz_q(4, "Uses", "Two plane mirrors are used to see over obstacles in "
             "a:", ["Telescope", "Microscope", "Periscope", "Camera"])
    b.quiz_a(4, "C. Periscope",
             "A periscope uses two plane mirrors, usually at 45°, to let the "
             "viewer see over walls or above the water from a submarine.")

    # ---- Part 2 : Light, speed and colour ----
    b.divider(2, "Part 2", "Speed & Colour of Light",
              "How fast light travels and the colours hidden in white light")
    b.statement("SPEED OF LIGHT", "How Fast Does Light Travel?",
                "Light is the fastest thing in the universe; nothing travels "
                "faster than light.",
                formula="Speed of light in air  ≈  3 × 10⁸ metres per second",
                points=["At this speed light would circle the Earth about "
                        "seven times in one second.",
                        "Sunlight takes about 8 minutes to reach the Earth.",
                        "Light travels fastest in vacuum and a little slower in "
                        "air, water or glass.",
                        "Sound is far slower, which is why we see lightning "
                        "before we hear thunder."],
                notes="Give a sense of scale (seven times round the Earth a "
                      "second). The lightning-before-thunder fact compares the "
                      "speed of light with the speed of sound and previews the "
                      "Sound chapter.")
    b.text_image("WHITE LIGHT", "The Colours of White Light",
                 ["White light is not a single colour — it is a mixture of "
                  "several colours.",
                  "A glass prism splits white light into a band of colours "
                  "called a spectrum.",
                  "The seven colours are red, orange, yellow, green, blue, "
                  "indigo and violet (VIBGYOR).",
                  "This splitting of white light into its colours is called "
                  "dispersion."],
                 spectrum, img_side="left", img_w=5.8, img_h=3.7,
                 panel_title="Dispersion → VIBGYOR",
                 caption="A prism spreads white light into seven colours",
                 notes="Define dispersion and the order VIBGYOR (red bends "
                       "least, violet most). A rainbow is nature's own "
                       "dispersion of sunlight by raindrops.")
    b.text_image("PRIMARY COLOURS", "Primary & Secondary Colours of Light",
                 ["The three primary colours of light are red, green and blue.",
                  "Mixing (adding) two primary colours gives a secondary "
                  "colour.",
                  "Red + green = yellow; green + blue = cyan; blue + red = "
                  "magenta.",
                  "Adding all three primary colours together gives white "
                  "light."],
                 cadd, img_side="right", img_w=5.8, img_h=3.7,
                 panel_title="Adding lights",
                 caption="Red, green and blue add to make white",
                 notes="Be careful: these are the primary colours of LIGHT "
                       "(adding), which differ from the primary colours of "
                       "paint. Adding all three lights gives white — the "
                       "opposite of mixing paints.")
    b.text_image("SUBTRACTING COLOUR", "How a Filter Makes Colour",
                 ["A coloured filter lets its own colour pass and absorbs the "
                  "rest.",
                  "A red filter held up to white light lets only red light "
                  "through.",
                  "Removing colours from white light this way is called "
                  "subtraction of colours.",
                  "A red object looks red because it reflects red light and "
                  "absorbs the other colours."],
                 csub, img_side="left", img_w=5.6, img_h=3.4,
                 panel_title="Absorb the rest",
                 caption="A red filter transmits red and absorbs other colours",
                 notes="Connect filters and coloured objects: both work by "
                       "absorbing some colours and passing/reflecting others. "
                       "This 'subtraction' explains why a green leaf looks "
                       "green in white light but black in pure red light.")
    SK.cards(b, "COLOUR AROUND US", "Colour in Everyday Life", [
        ("Rainbow", "Raindrops disperse sunlight into a curved band of seven "
         "colours — dispersion in nature."),
        ("Why things look coloured", "An object shows the colour it reflects "
         "and absorbs the rest of the white light."),
        ("Stage & traffic lights", "Coloured filters over white lamps give "
         "red, green and other coloured beams."),
        ("A white object", "It reflects all colours equally, so it looks "
         "white; a black object absorbs them all."),
    ], icons=["star", "eye", "bulb", "sun"],
       notes="Tie the colour ideas to things students see daily. The rainbow "
             "is dispersion; the colour of an object is subtraction by "
             "reflection. Invite students to explain the colour of their own "
             "clothes.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Real vs virtual", "real can be caught on a screen; virtual cannot"),
        ("Lateral inversion", "a plane mirror swaps left and right"),
        ("Plane-mirror image", "virtual, erect, same size, equally far behind, "
         "laterally inverted"),
        ("Regular vs irregular", "smooth keeps rays parallel; rough scatters "
         "them"),
        ("Speed of light", "about 3 × 10⁸ m/s — the fastest in the universe"),
        ("White light", "a mix of seven colours (VIBGYOR); R, G, B are "
         "primary"),
    ], notes="Rapid recap; cold-call for each. Spend extra time on the five "
             "image characteristics and the primary colours of light.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Speed & Colour", 4)
    b.quiz_q(1, "Image", "Which of these is the correct list of plane-mirror "
             "image characteristics?", ["Real, inverted, magnified",
             "Virtual, erect, same size", "Real, erect, diminished",
             "Virtual, inverted, same size"])
    b.quiz_a(1, "B. Virtual, erect, same size",
             "A plane-mirror image is virtual, erect, the same size as the "
             "object, equally far behind the mirror and laterally inverted.")
    b.quiz_q(2, "Dispersion", "The splitting of white light into seven colours "
             "by a prism is called:", ["Reflection", "Refraction",
                                        "Dispersion", "Absorption"])
    b.quiz_a(2, "C. Dispersion",
             "Dispersion is the splitting of white light into its seven "
             "constituent colours (VIBGYOR) as it passes through a prism.")
    b.quiz_q(3, "Primary colours", "The three primary colours of light are:",
             ["Red, yellow, blue", "Red, green, blue",
              "Cyan, magenta, yellow", "Red, white, black"])
    b.quiz_a(3, "B. Red, green, blue",
             "The primary colours of light are red, green and blue. Added "
             "together in equal amounts they produce white light.")
    b.quiz_q(4, "Filters", "A red filter is held in front of white light. The "
             "light that passes through is:", ["White", "Green", "Red",
                                                "Blue"])
    b.quiz_a(4, "C. Red",
             "A red filter transmits only red light and absorbs the other "
             "colours, so only red light passes through — an example of the "
             "subtraction of colours.")

    b.closing("Mirrors, Speed & Colour",
              "A plane mirror gives a virtual, laterally inverted image; light "
              "races at 3 × 10⁸ m/s; and white light hides all the colours of "
              "the rainbow.")
    return b


# ===========================================================================
# HEAT  (S55, S56, S57)
# ===========================================================================
def heat_deck1():
    """S55 — Heat 1: heat as energy, units of heat, temperature, scales of
    temperature, measurement of temperature."""
    b = Builder("Heat  •  ICSE Class 7 Physics", accent=C["red"])
    motion = DX.states_of_matter("g7h1_motion")
    scales = DX.thermometer_scales("g7h1_scales")
    scales2 = DX.thermometer_scales("g7h1_scales2")

    b.title("ICSE • Class 7 • Heat", "Heat & Temperature",
            "Heat as a form of energy  •  Units of heat  •  Temperature and "
            "its scales  •  The thermometer", img=b.asset("g7_thermometer_photo", scales))
    b.objectives([
        "Explain that heat is a form of energy",
        "State the units of heat and relate the calorie to the joule",
        "Distinguish clearly between heat and temperature",
        "Define temperature as the degree of hotness of a body",
        "Name the scales of temperature and their fixed points",
        "Convert a temperature between the Celsius and Fahrenheit scales",
    ])

    # ---- Part 1 : Heat as energy ----
    b.divider(1, "Part 1", "Heat as Energy",
              "What heat is, its units, and how it differs from temperature")
    b.statement("HEAT", "What Is Heat?",
                "Heat is a form of energy that flows from a hotter body to a "
                "colder body because of the temperature difference between "
                "them.",
                points=["Heat always flows on its own from the hotter to the "
                        "colder body, never the other way.",
                        "When a body is heated, the energy of its particles "
                        "increases.",
                        "Heat is sometimes called energy 'in transit' because "
                        "it is energy on the move.",
                        "Adding heat can warm a body, expand it, or change its "
                        "state."],
                notes="Anchor heat as ENERGY, not a substance. Stress the "
                      "one-way flow (hot → cold) and that 'in transit' means it "
                      "is energy being transferred. Foreshadow its effects.")
    b.text_image("HEAT & PARTICLES", "Heat and Moving Particles",
                 ["Every substance is made of tiny particles that are always "
                  "moving.",
                  "Heating a body makes its particles move (or vibrate) "
                  "faster.",
                  "The faster the particles move, the hotter the body becomes.",
                  "This is why heat can melt a solid or boil a liquid — the "
                  "particles gain enough energy to break free."],
                 motion, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="Energy of particles",
                 caption="Particles move faster as a body is heated",
                 notes="Link heat to particle motion: more heat → faster "
                       "particles → higher temperature. This picture explains "
                       "melting and boiling and prepares the change-of-state "
                       "ideas of the next lesson.")
    SK.cards(b, "SOURCES OF HEAT", "Where Heat Comes From", [
        ("The Sun", "Our greatest natural source of heat, reaching us across "
         "space as radiation."),
        ("Burning fuels", "Wood, coal, kerosene and gas release heat when they "
         "burn."),
        ("Electricity", "Heaters, irons and geysers turn electrical energy "
         "into heat."),
        ("Friction", "Rubbing two surfaces together produces heat — rub your "
         "palms to feel it."),
    ], icons=["sun", "fire", "bolt", "force"],
       notes="List the everyday sources of heat. The friction example is a "
             "nice hands-on moment — students rub their palms and feel the "
             "warmth they have created.")
    b.statement("UNITS OF HEAT", "Units of Heat",
                "Because heat is energy, it is measured in the same unit as "
                "energy — the joule (J).",
                formula="1 calorie  =  4.2 joule",
                points=["The SI unit of heat is the joule (J).",
                        "An older unit is the calorie (cal): the heat needed to "
                        "raise 1 g of water by 1°C.",
                        "1 calorie = 4.2 joule, and 1 kilocalorie = 1000 "
                        "calories.",
                        "Food energy is often given in kilocalories (written "
                        "Calorie with a capital C)."],
                notes="Give the joule as the SI unit, then the calorie and the "
                      "conversion 1 cal = 4.2 J. The food-Calorie aside makes "
                      "the unit feel real to students.")
    SK.cards(b, "HEAT vs TEMPERATURE", "Heat Is Not the Same as Temperature", [
        ("Heat", "The total energy of all the moving particles in a body; "
         "measured in joules."),
        ("Temperature", "The degree of hotness of a body — how hot or cold it "
         "is; measured in °C."),
        ("A big vs small cup", "A bucket of warm water holds more heat than a "
         "cup at the same temperature."),
        ("Flow", "Heat flows from high temperature to low temperature until "
         "both are equal."),
    ], icons=["fire", "thermometer", "drop", "force"],
       notes="This is the most confused pair in the chapter. The "
             "bucket-vs-cup example shows two bodies at the SAME temperature "
             "can hold very different amounts of heat.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Heat & Its Units", 4)
    b.quiz_q(1, "Nature of heat", "Heat is best described as:",
             ["A kind of matter", "A form of energy", "A type of force",
              "A liquid"])
    b.quiz_a(1, "B. A form of energy",
             "Heat is a form of energy that flows from a hotter body to a "
             "colder one. It is measured in joules, the unit of energy.")
    b.quiz_q(2, "Direction", "Heat always flows on its own from a body at:",
             ["Low to high temperature", "High to low temperature",
              "Large to small size", "Solid to gas"])
    b.quiz_a(2, "B. High to low temperature",
             "Heat flows by itself from the hotter body (higher temperature) "
             "to the colder body (lower temperature) until their temperatures "
             "become equal.")
    b.quiz_q(3, "Units", "One calorie of heat is equal to:",
             ["0.42 J", "4.2 J", "42 J", "420 J"])
    b.quiz_a(3, "B. 4.2 J",
             "1 calorie = 4.2 joule. The calorie is the heat needed to raise "
             "the temperature of 1 g of water by 1°C.")
    b.quiz_q(4, "Heat vs temperature", "Two bodies at the same temperature "
             "may still contain different amounts of:",
             ["Temperature", "Heat", "Coldness", "Hotness"])
    b.quiz_a(4, "B. Heat",
             "Temperature is the degree of hotness, but heat is the total "
             "energy of the particles. A larger body at the same temperature "
             "holds more heat.")

    # ---- Part 2 : Temperature and its measurement ----
    b.divider(2, "Part 2", "Temperature & Its Scales",
              "Measuring how hot a body is")
    b.statement("TEMPERATURE", "What Is Temperature?",
                "Temperature is the degree of hotness or coldness of a body, "
                "and it decides the direction in which heat will flow.",
                points=["A body at a higher temperature feels hotter than one "
                        "at a lower temperature.",
                        "Heat flows from the body at higher temperature to the "
                        "one at lower temperature.",
                        "Temperature is measured with a thermometer.",
                        "Our sense of touch is unreliable, so we need a "
                        "thermometer to measure temperature accurately."],
                notes="Define temperature as degree of hotness. The "
                      "hand-in-warm-then-cold-water demo shows why touch is an "
                      "unreliable judge of temperature and why we need a "
                      "thermometer.")
    b.text_image("SCALES", "Scales of Temperature",
                 ["A thermometer is marked using two fixed points: the ice "
                  "point and the steam point.",
                  "On the Celsius scale the ice point is 0°C and the steam "
                  "point is 100°C.",
                  "On the Fahrenheit scale they are 32°F and 212°F.",
                  "On the Kelvin (SI) scale they are 273 K and 373 K."],
                 scales, img_side="right", img_w=4.6, img_h=4.4,
                 panel_title="Fixed points",
                 caption="0–100 on Celsius, 32–212 on Fahrenheit",
                 notes="Explain that a scale needs two fixed reference "
                       "temperatures. The ice point and steam point are the "
                       "same physical temperatures on every scale — only the "
                       "numbers differ.")
    b.statement("CONVERTING", "Relating the Scales",
                "The same temperature has different numbers on different "
                "scales, but they are linked by a simple relation.",
                formula="(C / 5)  =  (F − 32) / 9  =  (K − 273) / 5",
                points=["There are 100 Celsius degrees between the fixed "
                        "points, but 180 Fahrenheit degrees.",
                        "To go from Celsius to Kelvin, simply add 273.",
                        "Use the relation to change a reading from one scale to "
                        "another.",
                        "Normal human body temperature is 37°C, which is "
                        "98.6°F."],
                notes="Walk through the relation slowly. The key facts: 100 "
                      "Celsius divisions equal 180 Fahrenheit divisions, and "
                      "K = C + 273. The body-temperature numbers anchor it.")
    b.worked("WORKED EXAMPLE", "Celsius to Fahrenheit",
             "Normal body temperature is 37°C. Express this on the Fahrenheit "
             "scale.",
             ["Use  C / 5 = (F − 32) / 9",
              "37 / 5 = (F − 32) / 9",
              "(F − 32) = 9 × 37 / 5 = 66.6",
              "F = 66.6 + 32 = 98.6"],
             "37°C = 98.6°F  (normal body temperature)",
             notes="Substitute into the relation and solve for F. Point out the "
                   "answer is the familiar 98.6°F shown on a clinical "
                   "thermometer.")
    b.worked("WORKED EXAMPLE", "Fahrenheit to Celsius",
             "A hot day reads 104°F on a Fahrenheit thermometer. What is this "
             "on the Celsius scale?",
             ["Use  C / 5 = (F − 32) / 9",
              "C / 5 = (104 − 32) / 9 = 72 / 9 = 8",
              "C = 8 × 5",
              "C = 40"],
             "104°F = 40°C  (a very hot day)",
             notes="Now run the relation the other way: find (F − 32)/9 first, "
                   "then multiply by 5. Sanity-check that 40°C is a believable "
                   "hot-day temperature.")
    SK.cards(b, "THERMOMETERS", "Measuring Temperature", [
        ("Laboratory thermometer", "Reads a wide range, about −10°C to 110°C; "
         "used in experiments."),
        ("Clinical thermometer", "Reads a narrow range around body heat "
         "(35–42°C) with a kink to hold the reading."),
        ("How it works", "A liquid (mercury or coloured alcohol) expands up a "
         "thin tube as the temperature rises."),
        ("Reading it", "Place the bulb in contact, wait until the liquid "
         "stops moving, then read at eye level."),
    ], icons=["thermometer", "thermometer", "drop", "eye"],
       notes="Compare the laboratory and clinical thermometers — range and the "
             "clinical kink that holds the reading. Reinforce that a "
             "thermometer works by the expansion of a liquid.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Heat", "a form of energy that flows from hot to cold; unit joule"),
        ("Calorie", "1 cal = 4.2 J; heat to warm 1 g water by 1°C"),
        ("Heat vs temperature", "total particle energy vs degree of hotness"),
        ("Temperature", "degree of hotness; measured with a thermometer"),
        ("Scales", "Celsius 0–100, Fahrenheit 32–212, Kelvin 273–373"),
        ("Relating", "C/5 = (F−32)/9; K = C + 273"),
    ], notes="Rapid recap; cold-call for each. Spend extra time on heat vs "
             "temperature and the scale relation.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Temperature", 4)
    b.quiz_q(1, "Definition", "Temperature is the measure of the:",
             ["Total heat in a body", "Degree of hotness of a body",
              "Mass of a body", "Speed of a body"])
    b.quiz_a(1, "B. Degree of hotness of a body",
             "Temperature is the degree of hotness or coldness of a body. It "
             "decides the direction in which heat flows.")
    b.quiz_q(2, "Fixed points", "On the Celsius scale, the steam point is "
             "marked as:", ["0°C", "32°C", "100°C", "273°C"])
    b.quiz_a(2, "C. 100°C",
             "The Celsius scale takes the ice point as 0°C and the steam point "
             "as 100°C, with 100 equal divisions between them.")
    b.quiz_q(3, "Kelvin", "A temperature of 27°C on the Kelvin scale is:",
             ["27 K", "246 K", "300 K", "327 K"])
    b.quiz_a(3, "C. 300 K",
             "K = C + 273 = 27 + 273 = 300 K. To convert Celsius to Kelvin we "
             "simply add 273.")
    b.quiz_q(4, "Clinical thermometer", "A clinical thermometer has a narrow "
             "range of about:", ["−10°C to 110°C", "0°C to 100°C",
                                  "35°C to 42°C", "0°C to 500°C"])
    b.quiz_a(4, "C. 35°C to 42°C",
             "A clinical thermometer reads only around body temperature "
             "(35–42°C) and has a kink that keeps the reading until it is "
             "shaken down.")

    b.closing("Heat on the Move",
              "Heat is energy flowing from hot to cold; temperature, measured "
              "on the Celsius, Fahrenheit or Kelvin scale, tells us how hot a "
              "body is.")
    return b


def heat_deck2():
    """S56 — Heat 2: effects of heat and thermal expansion."""
    b = Builder("Heat  •  ICSE Class 7 Physics", accent=C["red"])
    motion = DX.states_of_matter("g7h2_motion")
    ballring = DX.thermal_expansion_ball_ring("g7h2_ballring")
    bimetal = DX.bimetallic_strip("g7h2_bimetal")

    b.title("ICSE • Class 7 • Heat", "Effects of Heat",
            "What heat does to a body  •  Change of state  •  Thermal "
            "expansion of solids, liquids and gases", img=b.asset("g7_kettle_photo", ballring))
    b.objectives([
        "List the main effects produced when a body is heated",
        "Explain change of state in terms of heating and cooling",
        "State that solids, liquids and gases expand on heating",
        "Compare the expansion of solids, liquids and gases",
        "Describe the ball-and-ring and bimetallic-strip experiments",
        "Give everyday applications and problems of thermal expansion",
    ])

    # ---- Part 1 : Effects of heat ----
    b.divider(1, "Part 1", "Effects of Heat",
              "How adding heat changes a body")
    b.statement("EFFECTS", "What Heat Does to a Body",
                "When a body is heated it can change in several ways — its "
                "temperature, its size and even its state can change.",
                points=["The temperature of the body usually rises.",
                        "The body expands — it increases in size.",
                        "The state may change: a solid can melt, a liquid can "
                        "boil into vapour.",
                        "Heating can also change properties such as colour, or "
                        "drive a chemical change."],
                notes="Give the big picture of heat's effects before the "
                      "details. The three you will test most are: temperature "
                      "rise, expansion, and change of state.")
    SK.cards(b, "THREE MAIN EFFECTS", "Three Effects to Know Well", [
        ("Rise in temperature", "Heating a body usually makes it hotter — its "
         "temperature goes up."),
        ("Expansion", "Almost every substance gets a little bigger when "
         "heated and shrinks when cooled."),
        ("Change of state", "A solid melts to a liquid, and a liquid boils to "
         "a gas, on strong heating."),
        ("Reversible by cooling", "Cooling reverses these: a gas condenses, a "
         "liquid freezes, a body contracts."),
    ], icons=["thermometer", "ruler", "drop", "snow"],
       notes="Walk the three effects with examples — a warming spoon, a "
             "melting ice cube, boiling water. Stress that cooling reverses "
             "each effect.")
    b.text_image("CHANGE OF STATE", "Melting, Boiling and Back Again",
                 ["Heating a solid gives its particles enough energy to break "
                  "free, so it melts into a liquid.",
                  "Heating the liquid further turns it into a gas (boiling or "
                  "evaporation).",
                  "Cooling reverses the journey: a gas condenses and a liquid "
                  "freezes.",
                  "During a change of state the heat goes into changing the "
                  "state, not raising the temperature."],
                 motion, img_side="right", img_w=6.0, img_h=3.4,
                 panel_title="Solid → liquid → gas",
                 caption="Particles gain energy and break apart on heating",
                 notes="Use the particle picture: heat loosens the particles "
                       "until they can flow (liquid) or fly free (gas). The "
                       "subtle point — temperature pauses during melting and "
                       "boiling — can be mentioned simply.")
    SK.cards(b, "NAMING THE CHANGES", "Changes of State Have Names", [
        ("Melting", "Solid → liquid on heating, as ice becomes water."),
        ("Boiling / evaporation", "Liquid → gas on heating, as water becomes "
         "steam."),
        ("Condensation", "Gas → liquid on cooling, as steam wets a cold lid."),
        ("Freezing", "Liquid → solid on cooling, as water becomes ice."),
    ], icons=["drop", "fire", "snow", "snow"],
       notes="Give each change its proper name and a homely example. Heating "
             "drives the forward changes (melting, boiling); cooling drives "
             "the reverse ones (condensation, freezing).")
    b.bullets("EVERYDAY EFFECTS", "Effects of Heat Around Us", [
        ("Cooking", "Heat changes food by raising its temperature and causing "
         "chemical changes."),
        ("Ice to water", "A warm day melts ice and snow — a change of state."),
        ("Drying clothes", "Heat from the Sun turns water into vapour, drying "
         "wet clothes."),
        ("Cracking glass", "Sudden, uneven heating can expand glass unevenly "
         "and crack it."),
    ], panel_title="Heat at work every day",
       notes="Connect the effects to daily life. The cracked-glass example "
             "previews why uneven expansion matters — the theme of Part 2.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Effects of Heat", 4)
    b.quiz_q(1, "Effects", "Which of these is NOT a usual effect of heating a "
             "body?", ["Rise in temperature", "Expansion",
                       "Change of state", "Decrease in size"])
    b.quiz_a(1, "D. Decrease in size",
             "Heating usually makes a body expand (increase in size), not "
             "shrink. A body contracts only when it is cooled.")
    b.quiz_q(2, "Change of state", "When a solid is heated strongly it first:",
             ["Freezes", "Melts into a liquid", "Condenses", "Contracts"])
    b.quiz_a(2, "B. Melts into a liquid",
             "Heating gives the particles of a solid enough energy to break "
             "free of their fixed positions, so the solid melts into a "
             "liquid.")
    b.quiz_q(3, "Particles", "On heating, the particles of a substance:",
             ["Stop moving", "Move faster", "Get heavier", "Disappear"])
    b.quiz_a(3, "B. Move faster",
             "Heat is energy, so the particles move or vibrate faster when a "
             "body is heated. This is what raises its temperature and can "
             "change its state.")
    b.quiz_q(4, "Reversing", "The change of state from gas back to liquid on "
             "cooling is called:", ["Melting", "Boiling", "Condensation",
                                    "Expansion"])
    b.quiz_a(4, "C. Condensation",
             "Cooling a gas removes energy from its particles until they come "
             "together as a liquid — this is condensation, the reverse of "
             "boiling.")

    # ---- Part 2 : Thermal expansion ----
    b.divider(2, "Part 2", "Thermal Expansion",
              "Why heated things grow, and how we use it")
    b.statement("THERMAL EXPANSION", "Heat Makes Things Expand",
                "Almost all substances — solids, liquids and gases — expand on "
                "heating and contract on cooling.",
                points=["Heating makes the particles move more and take up "
                        "more space, so the body expands.",
                        "For the same rise in temperature, gases expand the "
                        "most and solids the least.",
                        "So the order of expansion is: gases > liquids > "
                        "solids.",
                        "The expansion is small for solids but large enough to "
                        "matter in bridges and railway lines."],
                notes="State the rule and the order gas > liquid > solid. "
                      "Explain it through particle spacing: the freer the "
                      "particles, the more room the extra motion needs.")
    b.text_image("BALL & RING", "The Ball-and-Ring Experiment",
                 ["When cold, a metal ball just passes through a metal ring.",
                  "Heat the ball and it expands, becoming slightly larger.",
                  "Now the same ball will no longer pass through the ring.",
                  "Cool the ball again and it contracts, so it passes through "
                  "once more — proving solids expand on heating."],
                 ballring, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Solids expand",
                 caption="The heated ball is too large for the ring",
                 notes="Describe the classic demonstration. The fairness of "
                       "the test (same ball, same ring) makes it convincing. "
                       "It proves a solid really does grow when heated.")
    SK.cards(b, "WHICH EXPANDS MOST?", "Comparing Solids, Liquids and Gases", [
        ("Solids", "Expand the least; the particles are tightly held in "
         "place."),
        ("Liquids", "Expand more than solids; their particles are looser."),
        ("Gases", "Expand the most; their particles are far apart and move "
         "freely."),
        ("The order", "For the same heating: gases > liquids > solids."),
    ], icons=["atom", "drop", "wave", "ruler"],
       notes="Reinforce the order with the particle picture. A gas in a "
             "warmed flask pushes a liquid index along a tube far more than a "
             "solid rod lengthens — a quick way to compare.")
    b.text_image("BIMETALLIC STRIP", "The Bimetallic Strip",
                 ["Two different metals, such as brass and iron, are riveted "
                  "together into one strip.",
                  "When heated, brass expands more than iron.",
                  "The unequal expansion makes the strip bend, with brass on "
                  "the outside of the curve.",
                  "This bending is used in thermostats and fire alarms to "
                  "switch a circuit on or off."],
                 bimetal, img_side="right", img_w=5.6, img_h=3.6,
                 panel_title="Two metals, unequal expansion",
                 caption="Brass expands more, so the strip curls",
                 notes="Explain the cause: different metals expand by "
                       "different amounts, so a bonded strip must bend. The "
                       "thermostat and fire-alarm uses make it relevant.")
    SK.cards(b, "USES & PROBLEMS", "Expansion in Everyday Life", [
        ("Railway lines", "Small gaps are left between rails so they can "
         "expand in summer without buckling."),
        ("Bridges", "One end of a bridge rests on rollers to allow for "
         "expansion and contraction."),
        ("Overhead wires", "Telephone and power wires are left slightly slack "
         "so they do not snap when they contract in winter."),
        ("Fitting metal", "A hot iron rim shrinks tightly onto a wooden wheel "
         "as it cools — used in carts and wheels."),
    ], icons=["force", "ramp", "bolt", "gear"],
       notes="These are the standard ICSE applications. Each one either makes "
             "room for expansion (gaps, rollers, slack) or uses contraction on "
             "cooling (shrink-fitting). Have students spot rail gaps near "
             "home.")
    SK.cards(b, "EXPANSION AT WORK", "Putting Expansion to Use", [
        ("Liquid thermometer", "A thermometer works because its liquid "
         "expands up the tube as it warms."),
        ("Hot-air balloon", "Heated air expands, becomes lighter and lifts the "
         "balloon."),
        ("Gaps and rollers", "Builders leave room so expansion does not crack "
         "or buckle structures."),
        ("Shrink-fitting", "A heated metal ring slipped on, then cooled, grips "
         "tightly as it contracts."),
    ], icons=["thermometer", "wave", "ramp", "gear"],
       notes="Show expansion is not just a problem to design around but also "
             "something useful — thermometers and hot-air balloons both rely "
             "on it.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Effects of heat", "temperature rise, expansion, change of state"),
        ("Change of state", "solid → liquid → gas on heating; reversed on "
         "cooling"),
        ("Expansion", "almost everything expands on heating, contracts on "
         "cooling"),
        ("Order", "gases expand most, solids least"),
        ("Bimetallic strip", "two metals bend on heating — thermostats, "
         "alarms"),
        ("Applications", "rail gaps, bridge rollers, slack wires, "
         "shrink-fitting"),
    ], notes="Rapid recap; cold-call for each. The order of expansion and the "
             "bimetallic strip are the most examined points.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Thermal Expansion", 4)
    b.quiz_q(1, "Order", "For the same rise in temperature, the greatest "
             "expansion is shown by:", ["Solids", "Liquids", "Gases",
                                        "All equally"])
    b.quiz_a(1, "C. Gases",
             "Gas particles are far apart and move freely, so for the same "
             "heating a gas expands the most. The order is gases > liquids > "
             "solids.")
    b.quiz_q(2, "Ball and ring", "In the ball-and-ring experiment, the heated "
             "ball does not pass through the ring because it has:",
             ["Shrunk", "Expanded", "Melted", "Cooled"])
    b.quiz_a(2, "B. Expanded",
             "Heating makes the metal ball expand, so it becomes slightly too "
             "large to pass through the ring — proof that solids expand on "
             "heating.")
    b.quiz_q(3, "Bimetallic strip", "A bimetallic strip bends on heating "
             "because the two metals:", ["Have the same length",
             "Expand by different amounts", "Do not expand at all",
             "Melt together"])
    b.quiz_a(3, "B. Expand by different amounts",
             "The two metals expand unequally for the same heating, so the "
             "bonded strip must bend — with the metal that expands more on the "
             "outside of the curve.")
    b.quiz_q(4, "Applications", "Gaps are left between railway lines mainly "
             "to:", ["Save metal", "Allow for expansion in summer",
                     "Reduce noise", "Make joining easier"])
    b.quiz_a(4, "B. Allow for expansion in summer",
             "On a hot day the steel rails expand. The gaps give them room to "
             "lengthen without buckling and bending out of shape.")

    b.closing("Heat Changes Everything",
              "Heat warms, expands and even melts a body — and the small "
              "expansion of solids is large enough to shape how we build "
              "rails, bridges and wheels.")
    return b


def heat_deck3():
    """S57 — Heat 3: three modes of heat transfer, conductors & insulators,
    convection examples, black/white surfaces, the thermos flask."""
    b = Builder("Heat  •  ICSE Class 7 Physics", accent=C["red"])
    cond = DX.conduction("g7h3_cond")
    conv = DX.convection("g7h3_conv")
    rad = DX.radiation("g7h3_rad")
    bw = DX.black_white_surfaces("g7h3_bw")
    flask = DX.thermos_flask("g7h3_flask")

    b.title("ICSE • Class 7 • Heat", "Transfer of Heat",
            "Conduction  •  Convection  •  Radiation  •  Conductors and "
            "insulators  •  The vacuum flask", img=b.asset("g7_thermos_photo", flask))
    b.objectives([
        "Name the three ways in which heat travels",
        "Explain conduction and tell conductors from insulators",
        "Explain convection and give everyday examples",
        "Explain radiation and how it differs from the other two",
        "Describe how surface colour affects absorbing and emitting heat",
        "Explain how a vacuum flask reduces all three kinds of heat loss",
    ])

    # ---- Part 1 : Conduction and convection ----
    b.divider(1, "Part 1", "Conduction & Convection",
              "How heat travels through solids and fluids")
    b.statement("THREE MODES", "Three Ways Heat Travels",
                "Heat can travel from one place to another in three ways: "
                "conduction, convection and radiation.",
                points=["Conduction: heat passes through a solid without the "
                        "solid moving as a whole.",
                        "Convection: heat is carried by the actual movement of "
                        "a heated liquid or gas.",
                        "Radiation: heat travels as waves and needs no medium "
                        "at all.",
                        "More than one mode can act at the same time, as in a "
                        "pan of water on a flame."],
                notes="Preview all three modes so students have a map. The key "
                      "distinction to build: conduction and convection need a "
                      "material, radiation does not.")
    b.text_image("CONDUCTION", "Heat Through Solids: Conduction",
                 ["In conduction, heat passes from particle to particle "
                  "through a solid.",
                  "The particles vibrate faster and pass the energy along, but "
                  "do not move from their places.",
                  "Hold a metal spoon in hot tea and the handle soon feels "
                  "hot — that is conduction.",
                  "Metals are good conductors; this is why a metal rod heats "
                  "along its length."],
                 cond, img_side="left", img_w=5.8, img_h=3.3,
                 panel_title="Particle to particle",
                 caption="Heat flows along the rod from the hot end",
                 notes="Explain conduction with the rod-and-pins picture: pins "
                       "fall off in order from the hot end as heat travels "
                       "along. Stress the particles stay put — only energy "
                       "moves.")
    SK.cards(b, "CONDUCTORS & INSULATORS", "Good and Poor Conductors", [
        ("Conductors", "Materials that let heat pass easily — metals such as "
         "copper, aluminium and iron."),
        ("Insulators", "Materials that hardly let heat pass — wood, plastic, "
         "air, wool and glass."),
        ("In the kitchen", "Pans are metal to conduct heat, but handles are "
         "plastic or wood so they stay cool."),
        ("Keeping warm", "Woollen clothes and air gaps trap heat by being "
         "poor conductors."),
    ], icons=["bolt", "snow", "fire", "check"],
       notes="Sort everyday materials into conductors and insulators. The "
             "metal-pan-with-plastic-handle example shows both used together "
             "for a sensible reason.")
    b.bullets("CONDUCTION AT HOME", "Conductors and Insulators in Daily Life", [
        ("Cooking pans", "Metal bases conduct heat to the food; handles of "
         "wood or plastic stay cool."),
        ("Warm clothes", "Wool and quilts trap air, a poor conductor, so body "
         "heat is not lost."),
        ("Tiles feel cold", "A tiled floor conducts heat away from your feet "
         "faster than a carpet does."),
        ("Handles & holders", "We use cloth or plastic holders to lift hot "
         "vessels because they do not conduct heat."),
    ], panel_title="Choosing the right material",
       notes="Reinforce conductors vs insulators with familiar choices. The "
             "tile-vs-carpet point explains why the same-temperature floor can "
             "feel colder underfoot.")
    b.text_image("CONVECTION", "Heat Through Fluids: Convection",
                 ["In a liquid or gas, the heated part expands, becomes "
                  "lighter and rises.",
                  "Cooler, denser fluid sinks to take its place and is heated "
                  "in turn.",
                  "This sets up a circulating convection current that carries "
                  "heat through the fluid.",
                  "Convection cannot happen in a solid, because the particles "
                  "cannot move about."],
                 conv, img_side="right", img_w=5.0, img_h=4.0,
                 panel_title="The fluid carries the heat",
                 caption="Hot fluid rises; cool fluid sinks",
                 notes="Trace the convection current in the beaker. The "
                       "essential idea: the heated fluid itself moves, "
                       "carrying heat with it — unlike conduction.")
    SK.cards(b, "CONVECTION AROUND US", "Everyday Convection", [
        ("Sea breeze", "By day, land heats faster than the sea, so cool air "
         "blows in from the sea."),
        ("Land breeze", "By night, the sea stays warmer, so the breeze blows "
         "from land out to sea."),
        ("Room heating", "Warm air from a heater rises and circulates, warming "
         "the whole room."),
        ("Ventilators", "Hot, stale air rises and escapes through high "
         "windows and ventilators."),
    ], icons=["wave", "wave", "fire", "force"],
       notes="Sea and land breezes are the classic convection examples — "
             "explain them with day/night heating of land vs sea. Ventilators "
             "placed high let hot air escape.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Conduction", 4)
    b.quiz_q(1, "Modes", "Heat travels through a solid metal mainly by:",
             ["Convection", "Conduction", "Radiation", "Evaporation"])
    b.quiz_a(1, "B. Conduction",
             "In a solid, heat passes from particle to particle by conduction. "
             "The particles vibrate faster and pass energy along without "
             "leaving their places.")
    b.quiz_q(2, "Insulators", "Which of these is the best heat insulator?",
             ["Copper", "Aluminium", "Wood", "Iron"])
    b.quiz_a(2, "C. Wood",
             "Wood is a poor conductor (a good insulator) of heat, which is "
             "why pan handles are made of wood or plastic. The others are "
             "metals and conduct heat well.")
    b.quiz_q(3, "Convection", "Convection currents can be set up in:",
             ["Solids only", "Liquids and gases", "Vacuum only",
              "Metals only"])
    b.quiz_a(3, "B. Liquids and gases",
             "Convection needs particles that are free to move and carry heat "
             "with them, so it happens in fluids (liquids and gases), not in "
             "solids.")
    b.quiz_q(4, "Sea breeze", "A cool sea breeze blows toward the land during "
             "the:", ["Night", "Day", "Winter only", "Rain"])
    b.quiz_a(4, "B. Day",
             "By day the land heats faster than the sea. The warm air over the "
             "land rises and cooler air flows in from the sea — the sea "
             "breeze.")

    # ---- Part 2 : Radiation and applications ----
    b.divider(2, "Part 2", "Radiation & the Flask",
              "Heat that needs no medium, and how to trap it")
    b.text_image("RADIATION", "Heat as Waves: Radiation",
                 ["Radiation is the transfer of heat as waves, without any "
                  "medium.",
                  "This is how the Sun's heat reaches us across empty space.",
                  "Radiation travels in straight lines at the speed of light "
                  "and warms whatever absorbs it.",
                  "We feel it instantly when we stand near a fire or in "
                  "sunshine."],
                 rad, img_side="left", img_w=5.8, img_h=3.2,
                 panel_title="No medium needed",
                 caption="The Sun's heat crosses empty space by radiation",
                 notes="Radiation is the odd one out — it needs no material. "
                       "The Sun-to-Earth example is the clincher, since space "
                       "is a vacuum. It travels at the speed of light.")
    b.text_image("SURFACES", "Black and White Surfaces",
                 ["Dull, black surfaces are the best absorbers of heat "
                  "radiation.",
                  "Shiny, white surfaces are poor absorbers; they reflect most "
                  "radiation away.",
                  "A good absorber is also a good emitter, so black surfaces "
                  "also radiate heat fastest.",
                  "This is why we wear light colours in summer and why "
                  "radiators are often painted dull black."],
                 bw, img_side="right", img_w=5.8, img_h=3.4,
                 panel_title="Colour matters",
                 caption="Black absorbs and emits best; white least",
                 notes="The rule: good absorbers are good emitters. Light "
                       "summer clothes (reflect) and black radiators/cooking "
                       "vessels (absorb and emit) bring it home.")
    SK.cards(b, "RADIATION AROUND US", "Radiation in Everyday Life", [
        ("Solar water heater", "A black absorbing panel soaks up the Sun's "
         "radiation to heat water."),
        ("Light summer clothes", "Pale clothes reflect heat radiation and keep "
         "us cooler in the Sun."),
        ("Cooling fins & radiators", "Painted dull black to radiate away "
         "unwanted heat quickly."),
        ("A parked car", "Sunlight radiated in through the glass makes the "
         "inside very hot."),
    ], icons=["sun", "snow", "fire", "bolt"],
       notes="Each example is the absorb/emit rule in action: black absorbs "
             "(solar heater) or emits (radiator) well, while pale, shiny "
             "surfaces reflect.")
    b.text_image("THE FLASK", "The Vacuum (Thermos) Flask",
                 ["A vacuum flask keeps a drink hot or cold by stopping all "
                  "three kinds of heat transfer.",
                  "The vacuum between its double walls stops conduction and "
                  "convection.",
                  "The silvered walls reflect radiation back, stopping heat "
                  "loss by radiation.",
                  "The stopper on top stops convection and conduction through "
                  "the mouth."],
                 flask, img_side="left", img_w=4.4, img_h=4.2,
                 panel_title="Blocking all three",
                 caption="Vacuum, silvering and a stopper cut every heat path",
                 notes="The flask is the perfect summary of the chapter: each "
                       "feature blocks one mode of heat transfer. Ask students "
                       "to match each feature to the mode it stops.")
    SK.cards(b, "APPLICATIONS", "Using What We Know About Heat", [
        ("Cooking vessels", "Made of metal (good conductors) with insulating "
         "handles that stay cool to hold."),
        ("Warm clothing", "Wool and layered clothes trap air, a poor "
         "conductor, to keep body heat in."),
        ("Room comfort", "Ventilators high on walls let hot air escape; "
         "light-coloured roofs stay cooler."),
        ("Land & sea breezes", "Convection of air between land and sea gives "
         "coastal places their daily winds."),
    ], icons=["fire", "snow", "force", "wave"],
       notes="Pull the chapter together with applications. Each one chooses a "
             "conductor, an insulator, or a convection/radiation effect for a "
             "sensible reason.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Three modes", "conduction, convection and radiation"),
        ("Conduction", "particle to particle through a solid; metals are best"),
        ("Convection", "heated fluid rises, cool sinks — only in liquids/"
         "gases"),
        ("Radiation", "heat as waves, needs no medium; Sun to Earth"),
        ("Surfaces", "dull black absorbs and emits best; shiny white least"),
        ("Vacuum flask", "vacuum, silvering and stopper block all three"),
    ], notes="Rapid recap; cold-call for each. The flask is a great closing "
             "question — name the feature that blocks each mode.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Radiation", 4)
    b.quiz_q(1, "Radiation", "The mode of heat transfer that needs no medium "
             "is:", ["Conduction", "Convection", "Radiation", "All three"])
    b.quiz_a(1, "C. Radiation",
             "Radiation transfers heat as waves and needs no material medium. "
             "That is how the Sun's heat reaches the Earth across empty "
             "space.")
    b.quiz_q(2, "Surfaces", "The best absorber of heat radiation is a surface "
             "that is:", ["Shiny and white", "Dull and black",
                          "Smooth and silver", "Polished and bright"])
    b.quiz_a(2, "B. Dull and black",
             "Dull, black surfaces absorb radiation best (and also emit it "
             "best). Shiny, white surfaces reflect most radiation away.")
    b.quiz_q(3, "The flask", "The vacuum between the double walls of a thermos "
             "flask stops heat loss by:", ["Radiation only",
             "Conduction and convection", "Radiation and convection",
             "None of these"])
    b.quiz_a(3, "B. Conduction and convection",
             "There are no particles in a vacuum to carry heat, so the vacuum "
             "stops both conduction and convection. The silvering deals with "
             "radiation.")
    b.quiz_q(4, "Everyday", "A cooking pan is made of metal but its handle of "
             "plastic because metal is a good:", ["Insulator",
             "Conductor of heat", "Reflector", "Radiator"])
    b.quiz_a(4, "B. Conductor of heat",
             "Metal conducts heat well, so it heats the food quickly. The "
             "plastic handle is an insulator and stays cool enough to hold.")

    b.closing("Heat on the Move — Three Ways",
              "Conduction, convection and radiation carry heat everywhere — "
              "and a vacuum flask shows real mastery by blocking all three at "
              "once.")
    return b


# ===========================================================================
# SOUND  (S66, S67)
# ===========================================================================
def sound_deck1():
    """S66 — Sound 1: sound, production by vibrations, sources, sound needs a
    medium, longitudinal waves in air."""
    b = Builder("Sound  •  ICSE Class 7 Physics", accent=C["purple"])
    fork = DX.sound_vibration("g7s1_fork")
    jar = DX.bell_jar("g7s1_jar")
    longwave = DX.longitudinal_wave("g7s1_long")

    b.title("ICSE • Class 7 • Sound", "How Sound Is Made",
            "Sound from vibrations  •  Sources of sound  •  Sound needs a "
            "medium  •  Longitudinal waves", img=b.asset("g7_guitar_photo", fork))
    b.objectives([
        "Explain that sound is a form of energy produced by vibrations",
        "Identify the vibrating part in everyday sources of sound",
        "Show that sound needs a material medium to travel",
        "Describe the bell-jar experiment and its conclusion",
        "Explain how sound travels through air as a longitudinal wave",
        "Compare how fast sound travels in solids, liquids and gases",
    ])

    # ---- Part 1 : Producing sound ----
    b.divider(1, "Part 1", "Producing Sound",
              "How vibrations make the sound we hear")
    b.statement("SOUND", "What Is Sound?",
                "Sound is a form of energy that produces in us the sensation "
                "of hearing.",
                points=["Sound is always produced by a vibrating body — "
                        "something moving rapidly to and fro.",
                        "When the vibration stops, the sound stops too.",
                        "Sound, like all energy, can do work — a loud sound can "
                        "rattle a window.",
                        "Our ears detect sound and the brain lets us hear it."],
                notes="Establish sound as energy linked to vibration. The "
                      "simple test: touch a ringing bell or your throat while "
                      "humming — feel the vibration, and it stops when the "
                      "sound stops.")
    b.text_image("VIBRATIONS", "Sound Comes From Vibrations",
                 ["Strike a tuning fork and its prongs vibrate quickly to and "
                  "fro.",
                  "The vibrating prongs push and pull the air next to them.",
                  "This sends out a sound wave that travels to our ears.",
                  "Touch the vibrating fork to water and it splashes — proof "
                  "that it is moving."],
                 fork, img_side="left", img_w=5.4, img_h=3.8,
                 panel_title="To and fro",
                 caption="A vibrating tuning fork disturbs the air around it",
                 notes="Use the tuning fork as the cleanest example: you can "
                       "see and feel the vibration, and dipping it in water "
                       "throws up a splash. The vibration is the source of the "
                       "sound.")
    b.statement("ENERGY", "Sound Carries Energy",
                "Because sound is a form of energy, it can travel outward from "
                "its source and make other things move.",
                points=["A very loud sound can rattle window panes and even "
                        "crack glass.",
                        "Standing near a large loudspeaker, you can feel the "
                        "sound thump in your chest.",
                        "The energy of sound spreads out in all directions "
                        "from the source.",
                        "The energy came originally from whatever set the "
                        "source vibrating."],
                notes="Reinforce that sound is energy by its effects — rattling "
                      "windows, the thump of a bass speaker. The energy "
                      "spreads out, getting weaker with distance.")
    SK.cards(b, "SOURCES", "Sources of Sound", [
        ("Stringed instruments", "A vibrating string makes the sound in a "
         "guitar, sitar or violin."),
        ("Wind instruments", "A vibrating column of air makes the sound in a "
         "flute or whistle."),
        ("Drums & membranes", "A stretched, vibrating skin makes the sound of "
         "a drum or tabla."),
        ("Our voice", "Vibrating vocal cords in the throat produce the human "
         "voice."),
    ], icons=["wave", "wave", "wave", "ear"],
       notes="For each source, name the part that actually vibrates — string, "
             "air column, membrane or vocal cords. Ask students to find the "
             "vibrating part of instruments they know.")
    b.bullets("FIND THE VIBRATION", "Spotting the Vibrating Part", [
        ("Bell", "The metal body of the bell vibrates when struck."),
        ("Loudspeaker", "Its paper cone vibrates in and out very fast."),
        ("Insects", "A mosquito's buzz comes from its rapidly beating wings."),
        ("Your throat", "Place a hand on your throat and hum — you feel the "
         "vocal cords vibrating."),
    ], panel_title="Vibration is always there",
       notes="Drive home the universal rule: wherever there is sound, "
             "something is vibrating. The throat-humming check is a memorable, "
             "personal demonstration.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Making Sound", 4)
    b.quiz_q(1, "Source", "Sound is always produced by a body that is:",
             ["At rest", "Vibrating", "Hot", "Charged"])
    b.quiz_a(1, "B. Vibrating",
             "Every sound is produced by a vibrating body. When the vibration "
             "stops, the sound stops too.")
    b.quiz_q(2, "Nature", "Sound is a form of:",
             ["Matter", "Energy", "Force", "Light"])
    b.quiz_a(2, "B. Energy",
             "Sound is a form of energy that produces the sensation of "
             "hearing and can do work, such as rattling a window pane.")
    b.quiz_q(3, "Instruments", "In a flute, the sound is produced by the "
             "vibration of:", ["A string", "A column of air", "A membrane",
                               "A metal bar"])
    b.quiz_a(3, "B. A column of air",
             "In wind instruments like the flute, it is the column of air "
             "inside that vibrates to produce the sound.")
    b.quiz_q(4, "Voice", "The human voice is produced by the vibration of "
             "the:", ["Tongue", "Teeth", "Vocal cords", "Lips"])
    b.quiz_a(4, "C. Vocal cords",
             "Air from the lungs makes the vocal cords in the throat vibrate, "
             "producing the human voice — you can feel it with a hand on your "
             "throat.")

    # ---- Part 2 : Sound needs a medium ----
    b.divider(2, "Part 2", "How Sound Travels",
              "Why sound needs a medium and how it moves through air")
    b.statement("A MEDIUM", "Sound Needs a Material Medium",
                "Sound can travel only through a material medium — a solid, a "
                "liquid or a gas. It cannot travel through a vacuum.",
                points=["Sound needs particles of matter to pass the vibration "
                        "along.",
                        "In empty space (a vacuum) there are no particles, so "
                        "sound cannot travel.",
                        "Light, however, can travel through a vacuum — which is "
                        "why we see the Sun but hear nothing from space.",
                        "Astronauts in space must use radios because their "
                        "voices cannot carry."],
                notes="Contrast sound with light: sound must have a medium, "
                      "light need not. The 'no sound in space' fact and the "
                      "astronaut radio example make the point vividly.")
    b.text_image("BELL-JAR", "The Bell-Jar Experiment",
                 ["An electric bell is hung inside a glass jar and switched "
                  "on; we hear it ringing.",
                  "Air is slowly pumped out of the jar.",
                  "As the air thins, the sound grows fainter and fainter.",
                  "When almost all the air is gone the bell is seen striking "
                  "but is barely heard — proving sound needs a medium."],
                 jar, img_side="right", img_w=4.8, img_h=4.2,
                 panel_title="Pump out the air",
                 caption="The bell is seen but not heard in a vacuum",
                 notes="Walk through the experiment: the bell is visible "
                       "(light needs no medium) but inaudible (sound does). "
                       "This is the classic proof that sound requires matter "
                       "to travel through.")
    b.text_image("LONGITUDINAL", "Sound as a Longitudinal Wave",
                 ["A vibrating body pushes the air into regions where "
                  "particles crowd together — compressions.",
                  "In between, the particles spread apart — rarefactions.",
                  "These compressions and rarefactions move outward, carrying "
                  "the sound.",
                  "The air particles vibrate back and forth along the same "
                  "line the wave travels — a longitudinal wave."],
                 longwave, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="Compressions & rarefactions",
                 caption="Particles vibrate along the direction of travel",
                 notes="Define compression and rarefaction, then the key idea: "
                       "in a longitudinal wave the particles move along the "
                       "same direction as the wave, unlike the up-and-down of "
                       "a water (transverse) wave.")
    SK.cards(b, "SPEED IN MEDIA", "Sound Travels at Different Speeds", [
        ("Fastest in solids", "Particles are packed close, so they pass the "
         "vibration on quickly (steel ≈ 5000 m/s)."),
        ("Slower in liquids", "Particles are a little further apart (water ≈ "
         "1500 m/s)."),
        ("Slowest in gases", "Particles are far apart, so sound is slowest in "
         "air (≈ 340 m/s)."),
        ("Rule", "The closer the particles, the faster sound travels: solids > "
         "liquids > gases."),
    ], icons=["atom", "drop", "wave", "gauge"],
       notes="The order solids > liquids > gases follows from particle "
             "spacing. A nice example: putting your ear to a rail lets you "
             "hear a train through the steel before you hear it through the "
             "air.")
    SK.cards(b, "THROUGH SOLIDS & LIQUIDS", "Hearing Through Other Media", [
        ("String telephone", "Two cups joined by a taut string carry your "
         "voice as vibrations along the string."),
        ("Ear to the rail", "Put an ear to a steel rail and you hear an "
         "approaching train sooner than through the air."),
        ("Underwater sound", "Whales and dolphins call to each other across "
         "huge distances through water."),
        ("Knock on a table", "A gentle tap heard with your ear on the table is "
         "louder than through the air."),
    ], icons=["wave", "bolt", "drop", "force"],
       notes="These everyday examples show sound travels — often better — "
             "through solids and liquids, because their particles are closer "
             "together than in air.")
    b.bullets("LIGHT vs SOUND", "Sound Compared With Light", [
        ("Needs a medium?", "Sound must have a medium; light can travel "
         "through empty space."),
        ("Speed", "Light (3 × 10⁸ m/s) is about a million times faster than "
         "sound (≈ 340 m/s)."),
        ("Type of wave", "Sound is a longitudinal wave; light behaves as a "
         "transverse wave."),
        ("Everyday clue", "We see lightning first and hear the thunder later, "
         "because light far outruns sound."),
    ], panel_title="Two kinds of energy",
       notes="A compare-and-contrast slide that ties the Sound chapter back to "
             "Light. The thunder-and-lightning gap is the memorable takeaway.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Sound", "a form of energy produced by a vibrating body"),
        ("Sources", "string, air column, membrane or vocal cords vibrate"),
        ("Needs a medium", "travels through solids, liquids, gases — not "
         "vacuum"),
        ("Bell jar", "bell seen but not heard when the air is removed"),
        ("Longitudinal wave", "compressions and rarefactions along the "
         "direction of travel"),
        ("Speed", "fastest in solids, slowest in gases"),
    ], notes="Rapid recap; cold-call for each. The two essentials: sound comes "
             "from vibration, and sound needs a medium.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — How Sound Travels", 4)
    b.quiz_q(1, "Medium", "Sound cannot travel through:",
             ["Air", "Water", "Steel", "A vacuum"])
    b.quiz_a(1, "D. A vacuum",
             "Sound needs particles of matter to pass on the vibration. A "
             "vacuum has no particles, so sound cannot travel through it.")
    b.quiz_q(2, "Bell jar", "In the bell-jar experiment, as air is pumped out "
             "the sound of the bell:", ["Grows louder", "Stays the same",
                                        "Grows fainter", "Changes pitch"])
    b.quiz_a(2, "C. Grows fainter",
             "With fewer air particles to carry the sound, it grows fainter "
             "and almost disappears in a vacuum — though the bell is still "
             "seen striking.")
    b.quiz_q(3, "Wave type", "A sound wave in air is a:",
             ["Transverse wave", "Longitudinal wave", "Water wave",
              "Light wave"])
    b.quiz_a(3, "B. Longitudinal wave",
             "Sound travels as a longitudinal wave: the air particles vibrate "
             "back and forth along the same direction in which the wave "
             "travels, forming compressions and rarefactions.")
    b.quiz_q(4, "Speed", "Sound travels fastest in:",
             ["Air", "Water", "Steel", "A vacuum"])
    b.quiz_a(4, "C. Steel",
             "Sound travels fastest in solids because their particles are "
             "packed closely and pass the vibration on quickly. The order is "
             "solids > liquids > gases.")

    b.closing("Good Vibrations",
              "Sound is energy from a vibrating body, and it needs a medium — "
              "travelling as compressions and rarefactions, fastest where the "
              "particles are closest.")
    return b


def sound_deck2():
    """S67 — Sound 2: wave terms, audible/ultrasonic/infrasonic,
    characteristics of sound, speed of sound, reflection & absorption."""
    b = Builder("Sound  •  ICSE Class 7 Physics", accent=C["purple"])
    terms = DX.wave_terms("g7s2_terms")
    spectrum = DX.sound_spectrum("g7s2_spectrum")
    echo = DX.echo_reflection("g7s2_echo")

    b.title("ICSE • Class 7 • Sound", "Describing Sound",
            "Wave terms  •  Audible range  •  Loudness, pitch & quality  •  "
            "Speed, echo and absorption", img=b.asset("g7_drum_photo", terms))
    b.objectives([
        "Define wavelength, amplitude, frequency and time period",
        "State the audible range and define ultrasonic and infrasonic sound",
        "Relate loudness to amplitude and pitch to frequency",
        "State the speed of sound and compare it with the speed of light",
        "Explain the reflection of sound and how an echo forms",
        "Describe absorption of sound and its everyday uses",
    ])

    # ---- Part 1 : Wave terms and characteristics ----
    b.divider(1, "Part 1", "Describing a Sound Wave",
              "The words that measure a wave, and what we hear")
    b.text_image("WAVE TERMS", "The Language of Waves",
                 ["A wave has crests (highest points) and troughs (lowest "
                  "points).",
                  "Wavelength is the distance between two successive "
                  "compressions (or two crests).",
                  "Amplitude is the maximum displacement of a particle from "
                  "its rest position.",
                  "Frequency is the number of waves produced per second, "
                  "measured in hertz (Hz)."],
                 terms, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="Wavelength, amplitude, frequency",
                 caption="Crest, trough, amplitude and wavelength on a wave",
                 notes="Define each term against the diagram. Use a graph of a "
                       "wave to make the longitudinal sound wave easier to "
                       "picture; the same words apply.")
    b.statement("FREQUENCY & PERIOD", "Frequency and Time Period",
                "Frequency tells us how many vibrations happen each second; "
                "the time period is the time taken for one vibration.",
                formula="frequency  f  =  1 / time period (T)",
                points=["Frequency is measured in hertz (Hz); 1 Hz means one "
                        "vibration per second.",
                        "The time period T is the time for one complete "
                        "vibration, measured in seconds.",
                        "Frequency and time period are reciprocals: a high "
                        "frequency means a short period.",
                        "A sound of 256 Hz means the source makes 256 "
                        "vibrations every second."],
                notes="Establish f = 1/T with the 256 Hz example (middle C-ish "
                      "on a tuning fork). High frequency ↔ short period is the "
                      "idea to lock in.")
    b.text_image("WHAT WE HEAR", "Audible, Ultrasonic & Infrasonic",
                 ["The human ear can hear sounds between about 20 Hz and "
                  "20,000 Hz — the audible range.",
                  "Sounds below 20 Hz are infrasonic; we cannot hear them.",
                  "Sounds above 20,000 Hz are ultrasonic; we cannot hear them "
                  "either.",
                  "Dogs, bats and dolphins can hear ultrasonic sounds that we "
                  "cannot."],
                 spectrum, img_side="right", img_w=6.0, img_h=2.8,
                 panel_title="20 Hz to 20 kHz",
                 caption="Humans hear only the middle, audible band",
                 notes="Fix the audible range 20 Hz–20 kHz, then define "
                       "infrasonic (below) and ultrasonic (above). Animals "
                       "such as bats and dogs hear beyond our range — a "
                       "favourite exam point.")
    SK.cards(b, "CHARACTERISTICS", "Loudness, Pitch and Quality", [
        ("Loudness", "How loud or soft a sound is; it depends on the amplitude "
         "— bigger amplitude, louder sound."),
        ("Pitch", "How shrill or flat a sound is; it depends on the frequency "
         "— higher frequency, higher pitch."),
        ("Quality (timbre)", "What lets us tell a flute from a violin playing "
         "the same note."),
        ("Examples", "A drum is loud (large amplitude); a whistle is "
         "high-pitched (high frequency)."),
    ], icons=["gauge", "wave", "star", "bulb"],
       notes="Separate the two commonly confused ideas: loudness ↔ amplitude, "
             "pitch ↔ frequency. Quality (timbre) explains why instruments "
             "sound different on the same note.")
    SK.cards(b, "MUSIC vs NOISE", "Pleasant and Unpleasant Sounds", [
        ("Musical sound", "A pleasant sound made by regular, smooth "
         "vibrations — a flute or a sitar."),
        ("Noise", "An unpleasant sound made by irregular, sudden vibrations — "
         "a slamming door or traffic."),
        ("The difference", "Music has a steady pattern of vibration; noise "
         "does not."),
        ("Noise pollution", "Too much loud, unwanted sound harms hearing and "
         "should be reduced."),
    ], icons=["wave", "bolt", "star", "ear"],
       notes="Distinguish musical sound (regular vibrations, pleasant) from "
             "noise (irregular, unpleasant). Touch on noise pollution as a "
             "real-world concern students will recognise.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Wave Terms", 4)
    b.quiz_q(1, "Frequency", "The number of vibrations made in one second is "
             "the:", ["Amplitude", "Wavelength", "Frequency", "Time period"])
    b.quiz_a(1, "C. Frequency",
             "Frequency is the number of vibrations (or waves) per second, "
             "measured in hertz (Hz). It is the reciprocal of the time "
             "period.")
    b.quiz_q(2, "Audible range", "The audible range of the human ear is about:",
             ["2 Hz to 200 Hz", "20 Hz to 20,000 Hz",
              "200 Hz to 2000 Hz", "20,000 Hz to 200,000 Hz"])
    b.quiz_a(2, "B. 20 Hz to 20,000 Hz",
             "Humans can normally hear frequencies from about 20 Hz to 20,000 "
             "Hz. Below this is infrasonic and above it is ultrasonic.")
    b.quiz_q(3, "Loudness", "The loudness of a sound depends mainly on its:",
             ["Frequency", "Amplitude", "Speed", "Wavelength"])
    b.quiz_a(3, "B. Amplitude",
             "A larger amplitude means the source vibrates through a bigger "
             "distance, carrying more energy and producing a louder sound.")
    b.quiz_q(4, "Pitch", "A sound of higher frequency is heard as one of "
             "higher:", ["Loudness", "Pitch", "Speed", "Quality"])
    b.quiz_a(4, "B. Pitch",
             "Pitch depends on frequency: the higher the frequency, the higher "
             "(more shrill) the pitch of the sound.")

    # ---- Part 2 : Speed, echo and absorption ----
    b.divider(2, "Part 2", "Speed, Echo & Absorption",
              "How fast sound goes and what happens when it hits a surface")
    b.statement("SPEED OF SOUND", "The Speed of Sound",
                "Sound travels much more slowly than light — about 340 metres "
                "per second in air at room temperature.",
                formula="speed  =  distance / time   (v = d / t)",
                points=["In air the speed of sound is roughly 330–340 m/s.",
                        "It is far faster in water (≈ 1500 m/s) and in solids "
                        "(steel ≈ 5000 m/s).",
                        "Light is about a million times faster than sound.",
                        "That is why we see a lightning flash before we hear "
                        "the thunder."],
                notes="Anchor 340 m/s in air and the much higher speeds in "
                      "water and steel. The lightning-before-thunder gap is the "
                      "everyday proof that light far outruns sound.")
    b.worked("WORKED EXAMPLE", "How Far Is the Cliff?",
             "A boy claps his hands and hears the echo from a cliff 1.5 s "
             "later. If the speed of sound is 340 m/s, how far away is the "
             "cliff?",
             ["The sound travels to the cliff and back, so it covers 2 × d.",
              "Total distance = speed × time = 340 × 1.5 = 510 m",
              "This is the to-and-fro distance, so 2 × d = 510 m",
              "d = 510 / 2 = 255 m"],
             "The cliff is 255 m away",
             notes="Stress the to-and-fro point: the sound covers twice the "
                   "distance to the cliff. Find the total path first, then "
                   "halve it to get the distance to the cliff.")
    b.text_image("ECHO", "Reflection of Sound and the Echo",
                 ["Sound bounces back (reflects) when it strikes a hard, "
                  "distant surface.",
                  "A reflected sound heard separately from the original is "
                  "called an echo.",
                  "To hear a clear echo the reflecting surface must be far "
                  "enough away (at least about 17 m).",
                  "Echoes are used in ships' SONAR to measure the depth of the "
                  "sea."],
                 echo, img_side="left", img_w=5.8, img_h=3.4,
                 panel_title="Reflected sound",
                 caption="Sound returns from a distant wall as an echo",
                 notes="Define an echo as a distinctly heard reflected sound, "
                       "and give the minimum-distance condition (~17 m so the "
                       "echo arrives at least 0.1 s after the original). SONAR "
                       "is the standard application.")
    b.bullets("A CLEAR ECHO", "When Do We Hear an Echo?", [
        ("Far enough away", "The reflecting surface must be at least about "
         "17 m away."),
        ("Why 17 m", "The ear keeps a sound for about 0.1 s, so the echo must "
         "arrive at least that much later."),
        ("Hard surface", "A hard, smooth surface like a cliff or wall reflects "
         "sound well; soft surfaces absorb it."),
        ("Loud enough", "The original sound must be loud enough for the "
         "reflected sound to still be heard."),
    ], panel_title="Conditions for an echo",
       notes="Spell out the conditions: minimum ~17 m (from the 0.1 s "
             "persistence of hearing) and a hard reflecting surface. This is a "
             "common short-answer question.")
    SK.cards(b, "ULTRASOUND AT WORK", "Uses of Reflected Sound", [
        ("SONAR", "Ships send sound pulses to the seabed and time the echo to "
         "measure the sea's depth."),
        ("Medical scans", "Ultrasound echoes build images of a baby or organs "
         "inside the body."),
        ("Cleaning", "Ultrasonic vibrations shake dirt off delicate parts and "
         "jewellery."),
        ("Megaphone", "A cone reflects sound forward into a narrow beam so it "
         "carries further."),
    ], icons=["wave", "drop", "gear", "force"],
       notes="Show how reflection and ultrasound are put to work — SONAR, "
             "medical scanning, cleaning and the megaphone. Each relies on "
             "sending and reflecting sound.")
    SK.cards(b, "REFLECTION & ABSORPTION", "Bouncing and Soaking Up Sound", [
        ("Echo", "A single reflected sound heard after the original, as from "
         "a cliff or empty hall."),
        ("Reverberation", "Many quick reflections in a room make the sound "
         "drag on; soft surfaces reduce it."),
        ("Absorption", "Soft, porous materials like curtains and carpets soak "
         "up sound instead of reflecting it."),
        ("Soundproofing", "Cinemas and studios use soft panels to absorb sound "
         "and stop echoes."),
    ], icons=["wave", "ear", "snow", "book"],
       notes="Contrast hard surfaces (reflect → echo, reverberation) with "
             "soft, porous ones (absorb). This is why a bare hall echoes but a "
             "curtained cinema does not.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Wave terms", "wavelength, amplitude, frequency (Hz), time period"),
        ("f and T", "f = 1/T; high frequency means short period"),
        ("Audible range", "20 Hz–20 kHz; below = infrasonic, above = "
         "ultrasonic"),
        ("Loudness & pitch", "loudness ↔ amplitude; pitch ↔ frequency"),
        ("Speed", "≈ 340 m/s in air; far faster in water and solids"),
        ("Echo", "reflected sound; needs a far, hard surface; used in SONAR"),
    ], notes="Rapid recap; cold-call for each. The two pairs to nail: "
             "loudness/amplitude and pitch/frequency.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Speed & Echo", 4)
    b.quiz_q(1, "Speed", "The speed of sound in air at room temperature is "
             "about:", ["34 m/s", "340 m/s", "3400 m/s",
                        "3 × 10⁸ m/s"])
    b.quiz_a(1, "B. 340 m/s",
             "Sound travels at roughly 340 m/s in air — far slower than light "
             "(3 × 10⁸ m/s), which is why we see lightning before we hear "
             "thunder.")
    b.quiz_q(2, "Echo", "A reflected sound heard separately from the original "
             "sound is called:", ["A vibration", "An echo", "A frequency",
                                  "An overtone"])
    b.quiz_a(2, "B. An echo",
             "An echo is sound reflected from a distant hard surface and heard "
             "clearly after the original sound.")
    b.quiz_q(3, "Echo distance", "A boy hears the echo of his clap from a wall "
             "after 2 s. If sound travels at 340 m/s, the wall is:",
             ["170 m away", "340 m away", "680 m away", "1360 m away"])
    b.quiz_a(3, "B. 340 m away",
             "Total distance = 340 × 2 = 680 m. This is to the wall and back, "
             "so the wall is 680 / 2 = 340 m away.")
    b.quiz_q(4, "Absorption", "Curtains and carpets are used in halls to:",
             ["Reflect sound", "Absorb sound", "Speed up sound",
              "Increase echoes"])
    b.quiz_a(4, "B. Absorb sound",
             "Soft, porous materials such as curtains and carpets absorb "
             "sound, reducing echoes and reverberation in a room.")

    b.closing("Sound, Measured",
              "Frequency sets the pitch and amplitude the loudness; sound "
              "travels at about 340 m/s and returns from far surfaces as an "
              "echo.")
    return b


# ===========================================================================
# ELECTRICITY & MAGNETISM  (S76, S77, S78)
# ===========================================================================
def em_deck1():
    """S76 — E&M 1: law of magnetism, repulsion is the sure test, magnetic
    field, electromagnet, making one, uses of electromagnets."""
    b = Builder("Electricity & Magnetism  •  ICSE Class 7 Physics",
                accent=C["blue"])
    poles = DX.magnet_poles("g7e1_poles")
    field = DX.bar_magnet_field("g7e1_field")
    emag = DX.electromagnet("g7e1_emag")

    b.title("ICSE • Class 7 • Magnetism", "Magnets & Electromagnets",
            "The law of magnetism  •  Magnetic fields  •  Making an "
            "electromagnet  •  Its uses", img=b.asset("g7_magnet_filings_photo", field))
    b.objectives([
        "State the law of magnetism for like and unlike poles",
        "Explain why repulsion is the only sure test of a magnet",
        "Describe the magnetic field and its lines of force",
        "Explain how an electric current can produce magnetism",
        "Describe how to make an electromagnet and increase its strength",
        "List important uses of electromagnets",
    ])

    # ---- Part 1 : Magnets and the law of magnetism ----
    b.divider(1, "Part 1", "Magnets & Their Field",
              "Poles, the law of magnetism and lines of force")
    b.statement("MAGNETS", "Magnets and Their Poles",
                "A magnet is a body that attracts magnetic materials like iron "
                "and points north–south when freely suspended.",
                points=["Every magnet has two poles: a north (N) pole and a "
                        "south (S) pole.",
                        "The poles are where the magnetism is strongest.",
                        "A freely hanging magnet always comes to rest pointing "
                        "north–south.",
                        "The two poles always occur together — you cannot have "
                        "a single pole on its own."],
                notes="Recall the idea of a magnet from earlier grades. The two "
                      "key facts: a magnet has two poles, and freely suspended "
                      "it points north–south, which is why it is called a "
                      "'magnet' (and how a compass works).")
    SK.cards(b, "MAGNETIC MATERIALS", "What a Magnet Attracts", [
        ("Magnetic materials", "Iron, steel, nickel and cobalt are attracted "
         "by a magnet."),
        ("Non-magnetic materials", "Wood, plastic, copper, glass and paper are "
         "not attracted."),
        ("Test it", "Pass a magnet over a mixture and only the magnetic pieces "
         "jump to it."),
        ("Use it", "This is how scrap iron is separated from rubbish with a "
         "magnet."),
    ], icons=["magnet", "book", "target", "gear"],
       notes="Sort materials into magnetic (iron, steel, nickel, cobalt) and "
             "non-magnetic. The separation of iron from a mixture is a neat "
             "demonstration and links to scrap recycling.")
    b.text_image("LAW OF MAGNETISM", "Like Repel, Unlike Attract",
                 ["Bring two north poles close and they push apart — they "
                  "repel.",
                  "Bring a north pole near a south pole and they pull together "
                  "— they attract.",
                  "So: like poles repel, and unlike poles attract.",
                  "This is the law of magnetism, the basic rule for how "
                  "magnets behave."],
                 poles, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Like repel, unlike attract",
                 caption="N–N and S–S repel; N–S attract",
                 notes="State the law clearly and show it with two bar "
                       "magnets. Like poles repel, unlike poles attract — the "
                       "single most important rule of the chapter.")
    b.statement("THE SURE TEST", "Repulsion Is the Sure Test",
                "Repulsion — not attraction — is the only sure test of whether "
                "a bar is a magnet.",
                points=["A magnet attracts both another magnet and an "
                        "unmagnetised iron bar.",
                        "So attraction alone cannot prove the other bar is a "
                        "magnet.",
                        "Only another magnet can be repelled.",
                        "If a bar repels a known magnet, it must itself be a "
                        "magnet."],
                notes="This is a classic exam point. Attraction is ambiguous "
                      "(iron is also attracted), but repulsion happens only "
                      "between two magnets — so repulsion is the sure test.")
    b.text_image("MAGNETIC FIELD", "The Magnetic Field",
                 ["The space around a magnet where its force can be felt is "
                  "its magnetic field.",
                  "We picture the field using magnetic lines of force.",
                  "Outside the magnet, these lines run from the north pole to "
                  "the south pole.",
                  "The lines are closest together near the poles, where the "
                  "field is strongest."],
                 field, img_side="right", img_w=5.8, img_h=3.6,
                 panel_title="Lines of force",
                 caption="Field lines run from N to S outside the magnet",
                 notes="Define the magnetic field and lines of force. Iron "
                       "filings sprinkled around a magnet line up along these "
                       "lines — a demonstration worth describing.")
    SK.cards(b, "FIELD LINES", "Properties of Magnetic Field Lines", [
        ("Direction", "Outside the magnet they run from the north pole to the "
         "south pole."),
        ("Never cross", "Two field lines never cross each other."),
        ("Crowding", "They are crowded near the poles, where the field is "
         "strongest."),
        ("Closed loops", "Each line forms a closed loop, passing through the "
         "magnet from S to N inside."),
    ], icons=["compass", "target", "magnet", "gear"],
       notes="List the properties of field lines. The 'never cross' and "
             "'crowded at the poles' points are commonly tested. Iron filings "
             "reveal the pattern beautifully.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Magnets & Fields", 4)
    b.quiz_q(1, "Law of magnetism", "When two north poles are brought close "
             "together, they:", ["Attract", "Repel", "Do nothing",
                                  "Join into one"])
    b.quiz_a(1, "B. Repel",
             "Like poles repel. Two north poles (or two south poles) push each "
             "other apart, while unlike poles attract.")
    b.quiz_q(2, "Sure test", "The only sure test of whether a bar is a magnet "
             "is that it shows:", ["Attraction", "Repulsion", "Rusting",
                                    "Heating"])
    b.quiz_a(2, "B. Repulsion",
             "A magnet attracts both magnets and unmagnetised iron, so "
             "attraction is not proof. Only two magnets repel, so repulsion is "
             "the sure test.")
    b.quiz_q(3, "Field lines", "Outside a bar magnet, the magnetic field lines "
             "run from:", ["South to north pole", "North to south pole",
                           "Pole to pole inside only", "Nowhere"])
    b.quiz_a(3, "B. North to south pole",
             "Outside the magnet, field lines are taken to run from the north "
             "pole to the south pole; inside, they run from S to N to form "
             "closed loops.")
    b.quiz_q(4, "Poles", "How many poles does a single bar magnet have?",
             ["One", "Two", "Three", "Four"])
    b.quiz_a(4, "B. Two",
             "Every magnet has two poles, a north and a south. They always "
             "occur in pairs — a single isolated pole does not exist.")

    # ---- Part 2 : Electromagnets ----
    b.divider(2, "Part 2", "Electromagnets",
              "Magnetism made from an electric current")
    b.statement("ELECTROMAGNET", "Magnetism From Electricity",
                "An electric current flowing through a coil of wire produces a "
                "magnetic field; with a soft-iron core this makes an "
                "electromagnet.",
                points=["A current-carrying wire behaves like a magnet around "
                        "it.",
                        "Winding the wire into a coil (solenoid) makes the "
                        "field much stronger.",
                        "Placing a soft-iron core inside the coil makes a "
                        "powerful electromagnet.",
                        "Switch the current off and the magnetism almost "
                        "completely disappears."],
                notes="Introduce the link between electricity and magnetism: a "
                      "current makes a magnetic field. A coil concentrates it, "
                      "and an iron core boosts it — that is an electromagnet.")
    b.text_image("MAKING ONE", "Making an Electromagnet",
                 ["Wind insulated copper wire into many turns around a "
                  "soft-iron nail or rod.",
                  "Connect the ends of the coil to a cell through a switch.",
                  "When the switch is closed, the iron becomes a strong "
                  "magnet and picks up pins.",
                  "Open the switch and the iron loses almost all its "
                  "magnetism."],
                 emag, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Coil + core + cell",
                 caption="Current in the coil magnetises the iron core",
                 notes="Walk through building one: coil, soft-iron core, cell, "
                       "switch. The fact that it switches on and off is its "
                       "great advantage over a permanent magnet.")
    SK.cards(b, "STRENGTH", "Making an Electromagnet Stronger", [
        ("More turns", "Increasing the number of turns in the coil makes the "
         "electromagnet stronger."),
        ("More current", "Using a larger current through the coil increases "
         "the strength."),
        ("Soft-iron core", "A soft-iron core greatly increases the strength "
         "and loses magnetism when switched off."),
        ("Shorter, thicker", "A short, thick coil gives a stronger field than "
         "a long, thin one."),
    ], icons=["gear", "bolt", "magnet", "force"],
       notes="Three controllable factors: number of turns, size of current, "
             "and the soft-iron core. These are standard short-answer points.")
    SK.cards(b, "USES", "Uses of Electromagnets", [
        ("Lifting cranes", "Powerful electromagnets lift heavy iron scrap and "
         "drop it by switching off."),
        ("Electric bell", "An electromagnet repeatedly pulls an iron armature "
         "to strike the gong."),
        ("Separating iron", "Electromagnets pull iron pieces out of mixed "
         "scrap and rubbish."),
        ("Relays & devices", "They switch circuits in relays, and work in "
         "motors, loudspeakers and maglev trains."),
    ], icons=["magnet", "bell", "gear", "bolt"],
       notes="Connect each use to the switch-on/switch-off advantage. The "
             "scrap-yard crane is the clearest example of why an electromagnet "
             "beats a permanent magnet.")
    b.bullets("TWO KINDS OF MAGNET", "Electromagnet vs Permanent Magnet", [
        ("Switchable", "An electromagnet can be turned on and off; a permanent "
         "magnet is always magnetic."),
        ("Strength", "An electromagnet's strength can be changed; a permanent "
         "magnet's cannot."),
        ("Needs power", "An electromagnet works only while current flows; a "
         "permanent magnet needs none."),
        ("Reversible poles", "Reversing the current swaps an electromagnet's "
         "poles; a permanent magnet's poles are fixed."),
    ], panel_title="Compare and choose",
       notes="Draw out the trade-offs: the electromagnet is controllable but "
             "needs power; the permanent magnet is simple but fixed. The right "
             "choice depends on the job.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Poles", "every magnet has N and S poles; points north–south"),
        ("Law of magnetism", "like poles repel, unlike poles attract"),
        ("Sure test", "repulsion is the only sure test of a magnet"),
        ("Magnetic field", "space around a magnet; lines run N to S outside"),
        ("Electromagnet", "coil + current + soft-iron core"),
        ("Strength & uses", "more turns/current/iron; cranes, bells, relays"),
    ], notes="Rapid recap; cold-call for each. The sure test and the recipe "
             "for a strong electromagnet are the must-know points.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Electromagnets", 4)
    b.quiz_q(1, "Source", "An electromagnet produces magnetism from:",
             ["A permanent magnet", "An electric current", "Heat", "Sunlight"])
    b.quiz_a(1, "B. An electric current",
             "An electromagnet works only while a current flows through its "
             "coil. The current's magnetic field magnetises the soft-iron "
             "core.")
    b.quiz_q(2, "Core", "The core of a strong electromagnet is made of:",
             ["Steel", "Soft iron", "Copper", "Plastic"])
    b.quiz_a(2, "B. Soft iron",
             "Soft iron is used because it becomes strongly magnetic when the "
             "current flows and loses almost all its magnetism when the "
             "current is switched off.")
    b.quiz_q(3, "Strength", "The strength of an electromagnet can be increased "
             "by:", ["Fewer turns", "A smaller current",
                     "More turns in the coil", "Removing the core"])
    b.quiz_a(3, "C. More turns in the coil",
             "More turns, a larger current and a soft-iron core all make an "
             "electromagnet stronger. Fewer turns or a smaller current weaken "
             "it.")
    b.quiz_q(4, "Uses", "Electromagnets are preferred over permanent magnets "
             "in cranes because they:", ["Are cheaper",
             "Can be switched on and off", "Never lose strength",
             "Are lighter"])
    b.quiz_a(4, "B. Can be switched on and off",
             "An electromagnet can be switched on to grip iron scrap and "
             "switched off to release it — something a permanent magnet "
             "cannot do.")

    b.closing("Magnets, Made to Order",
              "Magnets obey one rule — like repel, unlike attract — and a "
              "current-carrying coil lets us switch magnetism on and off at "
              "will.")
    return b


def em_deck2():
    """S77 — E&M 2: electric bell, magnetic declination, sources & uses of
    electricity, dry cells in a torch, flow in a circuit, conductors &
    insulators."""
    b = Builder("Electricity & Magnetism  •  ICSE Class 7 Physics",
                accent=C["blue"])
    bell = DX.electric_bell("g7e2_bell")
    decl = DX.magnetic_declination("g7e2_decl")
    torch = DX.torch("g7e2_torch")
    circuit = DX.simple_circuit("g7e2_circuit")

    b.title("ICSE • Class 7 • Electricity", "Electricity in Use",
            "The electric bell  •  Earth's magnetism  •  Sources of "
            "electricity  •  Cells and circuits", img=b.asset("g7_bell_photo", bell))
    b.objectives([
        "Explain how an electric bell works",
        "Describe Earth's magnetism and magnetic declination",
        "Name the main sources and uses of electricity",
        "Explain how dry cells are connected in a torch",
        "Describe the flow of current in a simple circuit",
        "Distinguish electrical conductors from insulators",
    ])

    # ---- Part 1 : The electric bell and Earth's magnetism ----
    b.divider(1, "Part 1", "The Bell & the Earth",
              "An electromagnet at work and the Earth as a magnet")
    b.text_image("ELECTRIC BELL", "How an Electric Bell Works",
                 ["Pressing the switch completes the circuit, so current "
                  "flows through the electromagnet.",
                  "The electromagnet pulls the soft-iron armature, and the "
                  "hammer strikes the gong.",
                  "Moving across breaks the contact, the current stops and the "
                  "spring pulls the armature back.",
                  "Contact is made again, so the hammer strikes repeatedly and "
                  "the bell rings."],
                 bell, img_side="left", img_w=4.8, img_h=4.2,
                 panel_title="Make and break",
                 caption="The armature vibrates, striking the gong again and "
                         "again",
                 notes="Trace the make-and-break cycle: current → magnet pulls "
                       "armature → contact breaks → spring returns it → "
                       "contact remakes. This rapid cycle makes the continuous "
                       "ringing.")
    b.statement("EARTH'S MAGNETISM", "The Earth Is a Magnet",
                "The Earth behaves as if it has a huge bar magnet inside it, "
                "which is why a compass needle points north–south.",
                points=["A freely suspended magnet (a compass) sets itself "
                        "along the Earth's field.",
                        "The Earth's magnetic poles are close to, but not "
                        "exactly at, its geographic poles.",
                        "This lets travellers and sailors find direction with "
                        "a compass.",
                        "The compass has guided explorers for hundreds of "
                        "years."],
                notes="Introduce the Earth as a giant magnet. The compass "
                      "works because the needle aligns with the Earth's field. "
                      "Lead into the small offset between magnetic and "
                      "geographic north.")
    b.text_image("DECLINATION", "Magnetic Declination",
                 ["A compass points to the magnetic north, not the true "
                  "(geographic) north.",
                  "The angle between the magnetic north and the geographic "
                  "north is the magnetic declination.",
                  "Its value is small and differs from place to place on the "
                  "Earth.",
                  "Sailors and pilots must allow for declination to steer an "
                  "accurate course."],
                 decl, img_side="right", img_w=5.0, img_h=4.0,
                 panel_title="True vs magnetic north",
                 caption="Declination is the angle between the two norths",
                 notes="Define declination as the angle between magnetic and "
                       "geographic north. It is small but matters for accurate "
                       "navigation, so maps note the local declination.")
    SK.cards(b, "MAGNETS AT WORK", "Where Magnets Help Us", [
        ("Compass", "A tiny pivoted magnet that always points north–south for "
         "finding direction."),
        ("Fridge & catches", "Small magnets hold doors shut and stick notes to "
         "the fridge."),
        ("Recording & cards", "Magnetic strips store information on cards and "
         "tapes."),
        ("Motors & speakers", "Magnets are vital parts of electric motors and "
         "loudspeakers."),
    ], icons=["compass", "magnet", "book", "bolt"],
       notes="A quick tour of everyday magnet uses to broaden the picture "
             "before moving on to electricity. The compass links back to "
             "Earth's magnetism.")
    b.bullets("THE COMPASS", "More About the Compass", [
        ("What it is", "A small magnetised needle balanced on a pivot so it "
         "can turn freely."),
        ("How it works", "The needle lines up with the Earth's magnetic field, "
         "pointing north–south."),
        ("Marking north", "The north-seeking end is usually coloured or "
         "marked to show direction."),
        ("Keep it away", "Keep iron and other magnets away from a compass, or "
         "it will give a wrong reading."),
    ], panel_title="Finding the way",
       notes="Explain the compass as a tiny pivoted magnet aligning with the "
             "Earth's field. Warn that nearby iron or magnets disturb it — a "
             "practical point for using one.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Bell & Compass", 4)
    b.quiz_q(1, "Electric bell", "The electric bell rings continuously because "
             "the armature:", ["Stays still", "Vibrates back and forth",
                                "Melts", "Heats up"])
    b.quiz_a(1, "B. Vibrates back and forth",
             "The make-and-break of the contact makes the armature vibrate "
             "rapidly, so the hammer strikes the gong again and again.")
    b.quiz_q(2, "Bell part", "The part of an electric bell that becomes "
             "magnetic when current flows is the:", ["Gong", "Hammer",
                                                      "Electromagnet",
                                                      "Spring"])
    b.quiz_a(2, "C. Electromagnet",
             "When current flows, the electromagnet becomes magnetic and pulls "
             "the soft-iron armature toward it, swinging the hammer to the "
             "gong.")
    b.quiz_q(3, "Compass", "A compass needle comes to rest pointing roughly:",
             ["East–west", "North–south", "Up–down", "In a circle"])
    b.quiz_a(3, "B. North–south",
             "A compass is a small freely pivoted magnet. It aligns with the "
             "Earth's magnetic field and so points north–south.")
    b.quiz_q(4, "Declination", "The angle between the geographic north and the "
             "magnetic north is called:", ["The latitude",
             "The magnetic declination", "The longitude", "The dip"])
    b.quiz_a(4, "B. The magnetic declination",
             "Magnetic declination is the angle between the direction a "
             "compass points (magnetic north) and true geographic north.")

    # ---- Part 2 : Sources and flow of electricity ----
    b.divider(2, "Part 2", "Electricity & Circuits",
              "Where electricity comes from and how it flows")
    SK.cards(b, "SOURCES", "Sources of Electricity", [
        ("Cells & batteries", "Chemical cells, like the dry cell in a torch, "
         "give a steady small supply."),
        ("Generators", "Power stations spin huge generators to make the "
         "mains electricity we use at home."),
        ("Solar cells", "Solar panels turn sunlight directly into "
         "electricity."),
        ("Mains supply", "Electricity reaches homes through wires from the "
         "power station."),
    ], icons=["battery", "bolt", "sun", "plug"],
       notes="Sort sources into chemical cells, generators (mains) and solar. "
             "The dry cell is the portable source; the mains is generated far "
             "away and carried by wires.")
    SK.cards(b, "USES", "Uses of Electricity", [
        ("Light", "Bulbs and tube lights turn electrical energy into light."),
        ("Heat", "Irons, geysers and heaters turn electricity into heat."),
        ("Motion", "Fans, mixers and pumps use electric motors to make "
         "things move."),
        ("Sound & screens", "Radios, televisions and phones run on "
         "electricity."),
    ], icons=["bulb", "fire", "gear", "wave"],
       notes="Show the variety of energy changes electricity makes possible — "
             "light, heat, motion and sound. Ask students to name an appliance "
             "for each.")
    b.text_image("DRY CELLS", "Dry Cells in a Torch",
                 ["A torch is powered by one or more dry cells.",
                  "The cells are joined in a line, the (+) of one touching the "
                  "(−) of the next — this is a series connection.",
                  "Connecting cells in series gives a larger total voltage to "
                  "light the bulb brightly.",
                  "Sliding the switch completes the circuit and the bulb "
                  "lights."],
                 torch, img_side="left", img_w=5.8, img_h=3.4,
                 panel_title="Cells in series",
                 caption="Two dry cells in series power the torch bulb",
                 notes="Show how the cells stack in series (+ to −) to add "
                       "their voltages. The torch is a complete everyday "
                       "circuit: cells, switch, bulb and connecting strips.")
    b.text_image("THE CIRCUIT", "Flow of Current in a Circuit",
                 ["An electric current is a flow of charge around a complete "
                  "(closed) circuit.",
                  "The cell pushes the current through the connecting wires, "
                  "switch and bulb.",
                  "If there is any break in the circuit, the current stops "
                  "and the bulb goes out.",
                  "The conventional current is taken to flow from the (+) "
                  "terminal of the cell, round to the (−)."],
                 circuit, img_side="right", img_w=5.6, img_h=3.6,
                 panel_title="A complete loop",
                 caption="Current flows only in a complete circuit",
                 notes="Stress that the circuit must be complete for current "
                       "to flow — a single break (an open switch) stops "
                       "everything. Introduce the conventional direction "
                       "(+ to −).")
    SK.cards(b, "CONDUCTORS & INSULATORS", "Conductors and Insulators of "
             "Electricity", [
        ("Conductors", "Let current pass easily — metals such as copper, "
         "aluminium and iron."),
        ("Insulators", "Hardly let current pass — rubber, plastic, glass, dry "
         "wood and air."),
        ("In the home", "Wires are copper (a conductor) coated in plastic (an "
         "insulator) for safety."),
        ("Why it matters", "Insulators on plugs and tools protect us from "
         "electric shock."),
    ], icons=["bolt", "plug", "circuit", "check"],
       notes="Sort materials into conductors and insulators of electricity. "
             "The copper-wire-in-plastic-sheath example shows both used "
             "together — one to carry current, one to protect us.")
    b.bullets("USE IT WISELY", "Using Electricity Wisely", [
        ("Switch off", "Turn off lights and fans when leaving a room to save "
         "electricity."),
        ("Efficient devices", "Use LED bulbs and efficient appliances that do "
         "the same job with less energy."),
        ("Don't waste", "Electricity from the mains costs money and uses up "
         "fuel at the power station."),
        ("Use daylight", "Make the most of sunlight during the day instead of "
         "switching on lights."),
    ], panel_title="Save energy, save money",
       notes="End Part 2 with the responsible-use message: saving electricity "
             "saves money and the fuel burned to generate it. Simple habits "
             "make a real difference.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Electric bell", "an electromagnet makes the armature vibrate and "
         "ring"),
        ("Earth's magnetism", "the Earth acts as a magnet; a compass points "
         "N–S"),
        ("Declination", "angle between magnetic north and true north"),
        ("Sources", "cells, generators (mains) and solar cells"),
        ("Circuit", "current flows only in a complete loop, + to −"),
        ("Conductors/insulators", "metals carry current; plastic and rubber "
         "do not"),
    ], notes="Rapid recap; cold-call for each. The complete-circuit idea and "
             "the conductor/insulator pairing are key for the next lesson.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Sources & Circuits", 4)
    b.quiz_q(1, "Sources", "Which of these is a portable chemical source of "
             "electricity?", ["A generator", "A dry cell", "A solar panel",
                              "The mains"])
    b.quiz_a(1, "B. A dry cell",
             "A dry cell is a chemical source of electricity that is small and "
             "portable, used in torches, clocks and remote controls.")
    b.quiz_q(2, "Cells in a torch", "The dry cells in a torch are usually "
             "joined:", ["In series", "In parallel", "Side by side",
                         "Not connected"])
    b.quiz_a(2, "A. In series",
             "The cells are joined end to end, the (+) of one to the (−) of "
             "the next — a series connection that adds their voltages.")
    b.quiz_q(3, "Circuit", "A bulb will light only when the circuit is:",
             ["Broken", "Open", "Complete (closed)", "Very long"])
    b.quiz_a(3, "C. Complete (closed)",
             "Current flows only around a complete, unbroken loop. Any break — "
             "such as an open switch — stops the current and the bulb goes "
             "out.")
    b.quiz_q(4, "Conductors", "Which material is the best conductor of "
             "electricity?", ["Rubber", "Copper", "Glass", "Plastic"])
    b.quiz_a(4, "B. Copper",
             "Copper is a metal and a very good conductor of electricity, "
             "which is why connecting wires are made of it. The others are "
             "insulators.")

    b.closing("Electricity at Your Command",
              "From the electric bell to the torch in your hand, electricity "
              "and magnetism work together — and current flows only when the "
              "circuit is complete.")
    return b


def em_deck3():
    """S78 — E&M 3: charges constitute current, circuit symbols & functions,
    series vs parallel circuits, safety precautions."""
    b = Builder("Electricity & Magnetism  •  ICSE Class 7 Physics",
                accent=C["blue"])
    symbols = DX.circuit_symbols("g7e3_symbols")
    circuit = DX.simple_circuit("g7e3_circuit")
    sp = DX.series_parallel("g7e3_sp")

    b.title("ICSE • Class 7 • Electricity", "Current & Circuits",
            "Charges and current  •  Circuit symbols  •  Series and parallel "
            "•  Electrical safety", img=b.asset("g7_circuit_photo", symbols))
    b.objectives([
        "Explain that an electric current is a flow of charge",
        "State the direction of conventional current",
        "Recognise the standard circuit symbols and their functions",
        "Draw a simple circuit using symbols",
        "Compare series and parallel circuits",
        "List safety precautions when using electricity",
    ])

    # ---- Part 1 : Current and circuit symbols ----
    b.divider(1, "Part 1", "Current & Symbols",
              "What flows in a circuit, and how we draw it")
    b.statement("ELECTRIC CURRENT", "Charges Make the Current",
                "An electric current is the flow of tiny electric charges "
                "through a conductor.",
                points=["Metals contain charges that are free to move.",
                        "When a cell is connected, it pushes these charges "
                        "around the circuit — that flow is the current.",
                        "The conventional current is taken to flow from the "
                        "(+) terminal of the cell to the (−) terminal.",
                        "Current is measured in amperes (A) with an "
                        "ammeter."],
                notes="Define current as a flow of charge. Keep it simple at "
                      "Class 7: charges in the metal move when the cell pushes "
                      "them. Give the conventional direction (+ to −) and the "
                      "unit, the ampere.")
    b.text_image("SYMBOLS", "Circuit Symbols",
                 ["Drawing real cells and bulbs is slow, so we use simple "
                  "symbols instead.",
                  "Each component has its own standard symbol.",
                  "A circuit diagram drawn with these symbols is quick to "
                  "draw and easy to read.",
                  "Everyone uses the same symbols, so a diagram means the same "
                  "thing to all."],
                 symbols, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="A shared language",
                 caption="Standard symbols for cell, bulb, switch and wires",
                 notes="Introduce circuit symbols as a shared shorthand. Have "
                       "students copy the cell, bulb, switch and wire symbols "
                       "into their notebooks — they will use them constantly.")
    SK.cards(b, "FUNCTIONS", "What Each Component Does", [
        ("Cell / battery", "Pushes the current around the circuit — the source "
         "of electrical energy."),
        ("Bulb / lamp", "Glows when current passes, turning electrical energy "
         "into light and heat."),
        ("Switch", "Opens or closes the circuit to stop or start the "
         "current."),
        ("Connecting wires", "Carry the current from one component to the "
         "next, usually copper."),
    ], icons=["battery", "bulb", "circuit", "plug"],
       notes="Match each symbol to its job. The cell is the 'pump', the switch "
             "the 'tap', the wires the 'pipes' and the bulb the device that "
             "uses the energy.")
    b.bullets("WHAT CURRENT DOES", "Effects of an Electric Current", [
        ("Heating effect", "Current heats a wire — used in heaters, irons and "
         "the filament of a bulb."),
        ("Lighting effect", "A heated filament glows white-hot and gives out "
         "light."),
        ("Magnetic effect", "A current produces a magnetic field — the basis "
         "of the electromagnet and bell."),
        ("Chemical effect", "Current passed through some liquids causes "
         "chemical changes, as in electroplating."),
    ], panel_title="Current at work",
       notes="List the effects of a current: heating, lighting, magnetic and "
             "chemical. Each is the basis of useful devices, from the heater "
             "to the electromagnet.")
    b.text_image("DRAWING A CIRCUIT", "Reading a Circuit Diagram",
                 ["A simple circuit needs a cell, a switch, a bulb and "
                  "connecting wires.",
                  "Close the switch and the circuit is complete, so the bulb "
                  "lights.",
                  "Open the switch and the circuit is broken, so the bulb goes "
                  "off.",
                  "The same diagram can be built with real components on the "
                  "bench."],
                 circuit, img_side="right", img_w=5.6, img_h=3.6,
                 panel_title="From symbols to circuit",
                 caption="A cell, switch and bulb in a complete loop",
                 notes="Read the diagram together: trace the loop from the "
                       "cell through the switch and bulb and back. Open and "
                       "closed switch decide whether the bulb lights.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Current & Symbols", 4)
    b.quiz_q(1, "Current", "An electric current is a flow of:",
             ["Heat", "Light", "Electric charge", "Air"])
    b.quiz_a(1, "C. Electric charge",
             "An electric current is the flow of tiny electric charges through "
             "a conductor when a cell pushes them around the circuit.")
    b.quiz_q(2, "Direction", "The conventional current flows from the cell's:",
             ["(−) to (+) terminal", "(+) to (−) terminal",
              "Middle outwards", "It does not flow"])
    b.quiz_a(2, "B. (+) to (−) terminal",
             "By convention, current is taken to flow from the positive "
             "terminal of the cell, around the circuit, back to the negative "
             "terminal.")
    b.quiz_q(3, "Symbol", "A circle with a cross inside it is the symbol "
             "for a:", ["Cell", "Switch", "Bulb / lamp", "Wire"])
    b.quiz_a(3, "C. Bulb / lamp",
             "A circle with a cross inside is the standard symbol for a bulb "
             "or lamp in a circuit diagram.")
    b.quiz_q(4, "Switch", "The job of a switch in a circuit is to:",
             ["Store energy", "Light up", "Open or close the circuit",
              "Measure current"])
    b.quiz_a(4, "C. Open or close the circuit",
             "A switch opens the circuit to stop the current or closes it to "
             "let the current flow, turning the device on or off.")

    # ---- Part 2 : Series, parallel and safety ----
    b.divider(2, "Part 2", "Series, Parallel & Safety",
              "Two ways to connect, and how to stay safe")
    b.text_image("SERIES vs PARALLEL", "Series and Parallel Circuits",
                 ["In a series circuit the components are joined one after "
                  "another in a single loop.",
                  "The same current flows through every part, so if one bulb "
                  "fails they all go out.",
                  "In a parallel circuit the components are on separate "
                  "branches.",
                  "Each branch works on its own, so if one bulb fails the "
                  "others stay lit."],
                 sp, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="One loop vs many branches",
                 caption="Series: one path. Parallel: separate paths",
                 notes="Contrast the two clearly: series = one path (one "
                       "failure stops all); parallel = separate paths (others "
                       "keep working). This explains why house wiring is "
                       "parallel.")
    SK.cards(b, "COMPARING", "Series vs Parallel at a Glance", [
        ("Series path", "One single path; the same current passes through "
         "every component."),
        ("Series fault", "If one component fails or is removed, the whole "
         "circuit breaks."),
        ("Parallel path", "Several branches; each gets its own share of the "
         "current."),
        ("Parallel fault", "If one branch fails, the others keep working — so "
         "homes are wired in parallel."),
    ], icons=["circuit", "bolt", "plug", "check"],
       notes="Summarise the comparison in a table-like grid. The headline "
             "reason homes use parallel wiring: each light and socket works "
             "independently of the others.")
    SK.cards(b, "IN USE", "Where Series and Parallel Are Used", [
        ("Series — torch", "Cells in a torch are in series so their voltages "
         "add up to light the bulb."),
        ("Series — old lights", "Some decorative light strings are in series; "
         "one failed bulb darkens them all."),
        ("Parallel — homes", "House lights and sockets are in parallel so each "
         "can be used on its own."),
        ("Parallel — appliances", "Every appliance gets the full supply "
         "voltage and switches independently."),
    ], icons=["bolt", "bulb", "plug", "gear"],
       notes="Give real examples of each connection. The torch (series) and "
             "house wiring (parallel) make the abstract comparison concrete.")
    SK.cards(b, "SAFETY", "Staying Safe With Electricity", [
        ("Dry hands", "Never touch switches or appliances with wet hands — "
         "water helps electricity flow through you."),
        ("Insulation", "Use plugs and tools with sound plastic or rubber "
         "insulation; replace frayed wires."),
        ("Don't overload", "Avoid plugging too many appliances into one "
         "socket."),
        ("Mains is dangerous", "Never poke fingers or metal into a socket; "
         "mains electricity can be fatal."),
    ], icons=["drop", "plug", "bolt", "target"],
       notes="Stress real safety rules: dry hands, good insulation, no "
             "overloading and never tamper with sockets. These can save a "
             "life — give the rules seriously.")
    b.statement("THE FUSE", "The Fuse — A Safety Device",
                "A fuse is a short piece of thin wire that melts and breaks "
                "the circuit if too large a current flows through it.",
                points=["Too large a current overheats the wires and can start "
                        "a fire.",
                        "The thin fuse wire melts first, breaking the circuit "
                        "before any harm is done.",
                        "After the fault is fixed, the blown fuse is replaced "
                        "with one of the correct rating.",
                        "A fuse must always be connected in the live wire of "
                        "the circuit."],
                notes="Explain the fuse as a deliberate weak link: it melts "
                      "first to protect the rest of the circuit. Stress using "
                      "the correct rating — too high a fuse gives no "
                      "protection.")
    b.bullets("GOLDEN RULES", "Electrical Safety — Golden Rules", [
        ("Switch off first", "Turn off the supply before touching or repairing "
         "anything electrical."),
        ("No water near electricity", "Keep water and wet hands away from "
         "electrical points."),
        ("Use the right fuse", "A correct fuse breaks the circuit safely if "
         "too much current flows."),
        ("Earth metal appliances", "Earthing carries away dangerous leakage "
         "current and prevents shocks."),
    ], panel_title="Stay safe, always",
       notes="End with a memorable set of golden rules. The fuse and earthing "
             "points preview the Class 8 work on household electricity.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Current", "a flow of electric charge; conventional flow + to −"),
        ("Symbols", "standard signs for cell, bulb, switch and wires"),
        ("Functions", "cell pushes, switch opens/closes, bulb lights"),
        ("Series", "one path; one failure breaks the whole circuit"),
        ("Parallel", "separate branches; others keep working — used in homes"),
        ("Safety", "dry hands, good insulation, correct fuse, earthing"),
    ], notes="Rapid recap; cold-call for each. Series vs parallel and the "
             "safety rules are the most important takeaways.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Circuits & Safety", 4)
    b.quiz_q(1, "Series", "In a series circuit of two bulbs, if one bulb "
             "fuses, the other:", ["Glows brighter", "Also goes out",
                                   "Stays the same", "Explodes"])
    b.quiz_a(1, "B. Also goes out",
             "A series circuit has a single path. If one bulb fails, the path "
             "is broken and the current stops, so the other bulb goes out too.")
    b.quiz_q(2, "Parallel", "Homes are wired in parallel mainly so that:",
             ["Less wire is used", "Each appliance works independently",
              "The current is larger", "The bill is higher"])
    b.quiz_a(2, "B. Each appliance works independently",
             "In a parallel circuit each branch works on its own, so one light "
             "can be switched off or fail without affecting the others.")
    b.quiz_q(3, "Safety", "Why should you never touch a switch with wet "
             "hands?", ["Water is a good insulator",
             "Water helps electricity flow through you", "It wastes water",
             "It is bad manners"])
    b.quiz_a(3, "B. Water helps electricity flow through you",
             "Wet skin conducts electricity far more easily than dry skin, so "
             "touching a switch with wet hands risks a dangerous shock.")
    b.quiz_q(4, "Symbols", "Two long-and-short plate symbols joined together "
             "represent a:", ["Single cell", "Battery", "Bulb", "Switch"])
    b.quiz_a(4, "B. Battery",
             "A battery is two or more cells joined together, shown as several "
             "long-and-short plate symbols in a row.")

    b.closing("Circuits, Understood",
              "Current is moving charge, circuit symbols are its shorthand, "
              "and choosing series or parallel — safely — puts electricity to "
              "work for us.")
    return b


# ---------------------------------------------------------------------------
def build():
    jobs = [
        ("G07_S37_Light_Energy_1.pptx", light_deck1),
        ("G07_S38_Light_Energy_2.pptx", light_deck2),
        ("G07_S55_Heat_1.pptx", heat_deck1),
        ("G07_S56_Heat_2.pptx", heat_deck2),
        ("G07_S57_Heat_3.pptx", heat_deck3),
        ("G07_S66_Sound_1.pptx", sound_deck1),
        ("G07_S67_Sound_2.pptx", sound_deck2),
        ("G07_S76_Electricity_and_Magnetism_1.pptx", em_deck1),
        ("G07_S77_Electricity_and_Magnetism_2.pptx", em_deck2),
        ("G07_S78_Electricity_and_Magnetism_3.pptx", em_deck3),
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
