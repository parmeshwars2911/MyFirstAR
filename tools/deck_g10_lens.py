"""
Grade 10 Physics — Chapter: Refraction Through a Lens.
Session 43 (Lesson 1: lens basics + image formation in a convex lens) and
Session 44 (Lesson 2: concave lens, lens formula, magnification, power, uses).

ICSE Class 10 (Selina / Concise Physics) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Refraction Through a Lens  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    prisms = b.asset("g10l_prisms", D.lens_as_prisms("g10l_prisms"))
    convex = b.asset("g10l_convex", D.convex_lens_image("g10l_convex"))
    magn = b.asset("g10l_magnifier", D.convex_magnifier("g10l_magnifier"))
    hero = b.asset("g10_lens_hero", convex)

    b.title("ICSE • Class 10 • Optics", "Refraction Through a Lens",
            "Convex & concave lenses  •  Principal rays  •  Image formation "
            "in a convex lens", img=hero)
    b.objectives([
        "Identify convex (converging) and concave (diverging) lenses",
        "Explain a lens as a set of prisms",
        "Define the technical terms: optical centre, focus, focal length",
        "State the three rules for drawing ray diagrams",
        "Locate images formed by a convex lens for any object position",
        "Describe a convex lens used as a magnifying glass",
    ])
    b.divider(1, "Part 1", "Lenses & How They Bend Light",
              "Types of lens, key terms and the ray-diagram rules")
    b.cards("LENSES", "Two Types of Lens", [
        ("Convex (converging)", "Thicker in the middle. It brings parallel "
         "rays together to a real focus."),
        ("Concave (diverging)", "Thinner in the middle. It spreads parallel "
         "rays out as if from a virtual focus."),
        ("Made of two surfaces", "Each lens is bounded by two spherical (or "
         "one flat) refracting surfaces."),
        ("Refraction twice", "Light refracts on entering and on leaving the "
         "lens, bending toward the thicker part."),
    ], notes="Hold up a real convex and concave lens if available. The single "
             "rule behind both: light bends toward the thicker part of the "
             "glass.")
    b.bullets("REFRACTION", "Refraction Through Equi-Convex & Equi-Concave Lenses", [
        ("Equi-convex lens", "Both surfaces bulge outward; a parallel beam "
         "converges to a real focus on the far side."),
        ("Equi-concave lens", "Both surfaces curve inward; a parallel beam "
         "spreads out as if from a virtual focus in front."),
        ("Two refractions", "Light bends once at each surface — toward the "
         "normal entering the glass, away from it on leaving."),
        ("Net effect", "Convex shapes converge light; concave shapes diverge "
         "it, no matter the object."),
    ], panel_title="Parallel light through the two lens types",
       notes="Trace a parallel beam through each lens type. Convex → real "
             "focus behind; concave → virtual focus in front.")
    b.text_image("HOW IT WORKS", "A Lens Is Like a Set of Prisms",
                 ["The top and bottom of a convex lens act like prisms with "
                  "their bases toward the middle.",
                  "Each prism bends light toward its base — i.e. toward the "
                  "principal axis.",
                  "The central part acts like a glass slab and lets light pass "
                  "straight through.",
                  "So a convex lens converges parallel rays to a single "
                  "focus."],
                 prisms, img_side="left", panel_title="Prism model",
                 caption="Each half bends light toward the axis",
                 notes="Use the prism analogy to make convergence intuitive. "
                       "For a concave lens the prisms point the other way, so "
                       "light diverges.")
    b.bullets("KEY TERMS", "Terms You Must Know", [
        ("Optical centre (O)", "the central point of the lens; a ray through "
         "it goes straight on."),
        ("Principal axis", "the line through the centres of curvature of the "
         "two surfaces."),
        ("Principal focus (F)", "the point where parallel rays meet (convex) "
         "or appear to come from (concave)."),
        ("Focal length (f)", "the distance from the optical centre to the "
         "principal focus."),
        ("A lens has two foci", "one on each side, at equal distances, because "
         "light can enter from either side."),
    ], panel_title="The vocabulary of lenses",
       notes="Drill these terms with the diagram. Stress a lens has TWO foci, "
             "equally spaced on both sides.")
    b.statement("FOCAL LENGTH", "Principal Focus & Focal Length",
                "Parallel rays close to the principal axis converge at the "
                "principal focus of a convex lens after refraction.",
                points=["The focal length f is the distance O→F.",
                        "A fatter (more curved) lens has a shorter focal "
                        "length and bends light more strongly.",
                        "2F (or C) marks twice the focal length — important for "
                        "locating images."],
                img=convex,
                notes="Define f via parallel rays. Mention shorter f = more "
                      "powerful lens (links to power later).")
    b.cards("RAY-DIAGRAM RULES", "The Three Rules for a Convex Lens", [
        ("Rule 1 — parallel ray", "A ray parallel to the axis refracts to pass "
         "through the far focus F."),
        ("Rule 2 — central ray", "A ray through the optical centre O goes "
         "straight on, undeviated."),
        ("Rule 3 — focal ray", "A ray through the near focus F refracts to "
         "emerge parallel to the axis."),
        ("Where they meet", "Any two of these rays locate the image; the third "
         "is a useful check."),
    ], notes="These three rules build every ray diagram. Students only need "
             "two rays to find an image; the third confirms it.")
    b.cards("IMAGES", "Real vs Virtual Images", [
        ("Real image", "Formed where refracted rays actually meet; can be "
         "caught on a screen; always inverted."),
        ("Virtual image", "Formed where rays only appear to meet; cannot be "
         "caught on a screen; always erect."),
        ("Convex lens", "Gives a real image for objects beyond F, a virtual "
         "image for objects within F."),
        ("Concave lens", "Gives only a virtual, erect, diminished image."),
    ], notes="Define real vs virtual precisely — the screen test is the "
             "clearest way for students to tell them apart.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Predict the Image", "An object is placed 25 cm from a convex "
             "lens of focal length 10 cm. Without calculating, what is the "
             "image like?", ["Real, inverted and diminished",
             "Real, inverted and magnified", "Virtual, erect and magnified",
             "No image is formed"])
    b.quiz_a(1, "A. Real, inverted and diminished",
             "f = 10 cm, so 2F = 20 cm. The object (25 cm) lies beyond 2F, so "
             "the image is real, inverted and diminished — the camera case. "
             "Knowing the 2F landmark lets you predict this without any "
             "arithmetic.")
    b.quiz_q(2, "Half-Covered Lens", "The lower half of a convex lens is "
             "covered with black paper. The image of an object will be:",
             ["Only the top half of the object",
              "The complete image, but fainter (less bright)",
              "Only the bottom half of the object",
              "Turned the right way up"])
    b.quiz_a(2, "B. The complete image, but fainter",
             "Every part of the lens collects light from the whole object, so "
             "the uncovered half still forms a complete image. With fewer rays "
             "reaching it, the image is simply dimmer — a classic conceptual "
             "trap.")
    b.quiz_q(3, "Which Lens Bends More?", "Two convex lenses are identical in "
             "size, but lens X is fatter (more sharply curved) than lens Y. "
             "Compared with Y, lens X has a:",
             ["Longer focal length", "Shorter focal length",
              "Larger optical centre", "Weaker converging power"])
    b.quiz_a(3, "B. Shorter focal length",
             "A more sharply curved lens bends light more strongly, bringing "
             "parallel rays to a focus closer to the lens. So the fatter lens "
             "X has a shorter focal length and greater power.")
    b.quiz_q(4, "Place the Object", "Where should an object be placed before a "
             "convex lens to get a real image larger than the object (as in a "
             "projector)?", ["Beyond 2F", "At 2F", "Between F and 2F",
              "Within F"])
    b.quiz_a(4, "C. Between F and 2F",
             "With the object between F and 2F, the image forms beyond 2F and "
             "is real, inverted and magnified — exactly how a projector throws "
             "an enlarged picture on the screen.")
    b.divider(2, "Part 2", "Images in a Convex Lens",
              "How the image changes as the object moves")
    b.text_image("IMAGE FORMATION", "Object Beyond 2F",
                 ["Draw the parallel ray (through F) and the central ray "
                  "(straight).",
                  "They meet between F and 2F on the other side.",
                  "The image is real, inverted and diminished.",
                  "This is how a camera forms a small picture of a distant "
                  "scene."],
                 convex, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="Real, inverted, diminished",
                 caption="Object beyond 2F → image between F and 2F",
                 notes="Walk the two rays on the diagram. Tie the result to a "
                       "camera making a small real image on the sensor.")
    b.bullets("IMAGE FORMATION", "As the Object Moves In…", [
        ("At infinity", "Image at F — real, inverted, point-sized."),
        ("Beyond 2F", "Image between F and 2F — real, inverted, diminished."),
        ("At 2F", "Image at 2F — real, inverted, same size as the object."),
        ("Between F and 2F", "Image beyond 2F — real, inverted, magnified "
         "(the projector case)."),
        ("At F", "Image at infinity — rays emerge parallel, no image formed."),
        ("Within F", "Image on the same side — virtual, erect, magnified "
         "(the magnifying glass)."),
    ], panel_title="The six standard cases",
       notes="This table is heavily examined. Have students memorise the trend: "
             "as the object comes closer than 2F the image grows and moves "
             "away, until within F it becomes virtual and erect.")
    b.text_image("IMAGE FORMATION", "Object Between F and 2F — the Projector",
                 ["Place the object between F and 2F.",
                  "The image forms beyond 2F on the other side.",
                  "It is real, inverted and magnified.",
                  "A slide projector uses exactly this to throw a large image "
                  "on the screen."],
                 convex, img_side="right", img_w=5.6, img_h=4.0,
                 panel_title="Real, inverted, magnified",
                 caption="Object between F and 2F → image beyond 2F",
                 notes="Contrast with the camera case: moving the object "
                       "closer (within 2F) flips the image from diminished to "
                       "magnified. This is the projector.")
    b.text_image("MAGNIFIER", "Convex Lens as a Magnifying Glass",
                 ["Place the object closer than the focal length (within F).",
                  "The refracted rays diverge, so no real image forms.",
                  "Tracing them back gives a virtual, erect, magnified image.",
                  "This is the simple microscope or magnifying glass."],
                 magn, img_side="right", img_w=5.6, img_h=4.0,
                 panel_title="Object within F",
                 caption="Within F → virtual, erect, magnified image",
                 notes="Demonstrate with a real magnifying glass over text. "
                       "Emphasise the object must be within the focal length.")
    b.cards("REAL LIFE", "Where Convex Lenses Are Used", [
        ("Camera", "Forms a small real image of the scene on the film/sensor."),
        ("Projector", "Object just beyond F gives a large real image on the "
         "screen."),
        ("Magnifying glass", "Object within F gives an enlarged virtual image."),
        ("Human eye", "The eye lens focuses a real, inverted image on the "
         "retina."),
    ], notes="Each device is just one row of the image table. Ask students to "
             "match each use to an object position.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Convex / concave", "thicker-middle converges; thinner-middle diverges"),
        ("Lens = prisms", "each half bends light toward the thicker centre"),
        ("Key terms", "optical centre, principal focus, focal length, 2F"),
        ("Three rules", "parallel→F, through O straight, through F→parallel"),
        ("Convex images", "real & inverted beyond F; virtual & erect within F"),
        ("Magnifier", "object within F → virtual, erect, magnified"),
    ], notes="Cold-call the six image cases as a rapid recap.")
    b.quiz_intro("Quiz 2", "Final Check — Convex Images", 4)
    b.quiz_q(1, "Camera", "To form a small, real, inverted image (as in a "
             "camera), the object should be:", ["Within F", "At F",
             "Between F and 2F", "Beyond 2F"])
    b.quiz_a(1, "D. Beyond 2F",
             "When the object is beyond 2F, the image is real, inverted and "
             "diminished, formed between F and 2F — exactly what a camera "
             "needs.")
    b.quiz_q(2, "Same Size", "A convex lens forms an image the same size as "
             "the object when the object is placed:", ["At F", "At 2F",
             "Within F", "At infinity"])
    b.quiz_a(2, "B. At 2F",
             "With the object at 2F, the image is also at 2F on the other "
             "side — real, inverted and the same size as the object.")
    b.quiz_q(3, "Magnifier", "When used as a magnifying glass, a convex lens "
             "forms an image that is:", ["Real and inverted",
             "Virtual, erect and magnified", "Real and diminished",
             "Virtual and diminished"])
    b.quiz_a(3, "B. Virtual, erect and magnified",
             "With the object within the focal length, the rays diverge and "
             "the eye sees a virtual, erect, magnified image on the same side "
             "as the object.")
    b.quiz_q(4, "No Image", "A convex lens forms no image (rays emerge "
             "parallel) when the object is placed:", ["Beyond 2F", "At 2F",
             "At the focus F", "Within F"])
    b.quiz_a(4, "C. At the focus F",
             "With the object exactly at F, the refracted rays emerge parallel "
             "and meet only at infinity — so no image is formed on a screen.")
    b.closing("Convex Lenses Shape Our World",
              "From your eye to a camera — placement decides whether the image "
              "is big or small, real or virtual.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    concave = b.asset("g10l_concave", D.concave_lens_image("g10l_concave"))
    convex = b.asset("g10l_convex2", D.convex_lens_image("g10l_convex2"))
    magn = b.asset("g10l_magnifier2", D.convex_magnifier("g10l_magnifier2"))
    hero = b.asset("g10_concave_hero", concave)
    apps = b.asset("g10_eye_optics", None)

    b.title("ICSE • Class 10 • Optics", "Lenses — Formula & Power",
            "Concave-lens images  •  Sign convention  •  Lens formula  •  "
            "Magnification & power", img=hero)
    b.objectives([
        "Locate the image formed by a concave lens",
        "Apply the sign convention for lenses",
        "Use the lens formula 1/v − 1/u = 1/f",
        "Calculate linear magnification m = v/u = hi/ho",
        "Define the power of a lens and its unit, the dioptre",
        "Describe how to find the focal length of a convex lens",
    ])
    b.divider(1, "Part 1", "Concave Lens, Sign Convention & Formula",
              "The diverging lens and the numbers behind images")
    b.text_image("CONCAVE LENS", "Image in a Concave Lens",
                 ["A concave lens diverges the refracted rays.",
                  "Tracing the rays back, they appear to meet on the same side "
                  "as the object.",
                  "The image is always virtual, erect and diminished.",
                  "This is true for every position of the object."],
                 concave, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="Always virtual & erect",
                 caption="Concave lens → virtual, erect, diminished",
                 notes="Key point: a concave lens gives the SAME kind of image "
                       "(virtual, erect, diminished) wherever the object is — "
                       "much simpler than the convex lens.")
    b.cards("CONVEX vs CONCAVE", "Telling the Images Apart", [
        ("Convex", "Image is real & inverted for most positions; virtual & "
         "erect only within F."),
        ("Concave", "Image is always virtual, erect and diminished."),
        ("On a screen", "A convex lens can throw a real image on a screen; a "
         "concave lens cannot."),
        ("Quick test", "Look through it at text: convex can magnify; concave "
         "always makes things look smaller."),
    ], notes="Give the practical 'look through it' test to distinguish the two "
             "lenses in the lab.")
    b.bullets("SIGN CONVENTION", "The New Cartesian Sign Convention", [
        "All distances are measured from the optical centre O.",
        ("Direction of light", "distances measured in the direction of the "
         "incident light are positive; against it, negative."),
        ("Object distance u", "is taken negative (object is on the incoming "
         "side)."),
        ("Convex lens f", "is positive; a concave lens f is negative."),
        ("Heights", "above the axis are positive, below the axis negative."),
    ], panel_title="Get the signs right before the formula",
       notes="Most numerical mistakes come from signs. Drill: u negative, "
             "convex f positive, concave f negative.")
    b.statement("LENS FORMULA", "The Lens Formula",
                "For a thin lens, object distance u, image distance v and "
                "focal length f are related by one equation.",
                formula="1/v  −  1/u  =  1/f",
                points=["Use the sign convention for every quantity.",
                        "Works for both convex and concave lenses.",
                        "Rearrange to find whichever quantity is unknown."],
                notes="State the formula and that the same equation covers "
                      "both lens types — only the signs differ.")
    b.worked("WORKED EXAMPLE", "Using the Lens Formula",
             "An object is placed 30 cm in front of a convex lens of focal "
             "length 20 cm. Find the image distance.",
             ["Sign convention:  u = −30 cm,  f = +20 cm",
              "1/v − 1/u = 1/f   →   1/v = 1/f + 1/u",
              "1/v = 1/20 + 1/(−30) = 3/60 − 2/60 = 1/60",
              "v = +60 cm"],
             "v = +60 cm — a real image 60 cm beyond the lens",
             notes="Show every sign. The positive v means a real image on the "
                   "far side. Cross-check with the image table (object between "
                   "F and 2F → magnified real image beyond 2F).")
    b.quiz_intro("Quiz 1", "Quick Check — Concave & Formula", 3)
    b.quiz_q(1, "Moving the Object", "An object is slowly moved closer to a "
             "concave lens. The image it forms:",
             ["Becomes real and inverted",
              "Stays virtual and erect, getting slightly larger but always "
              "smaller than the object",
              "Disappears at the focus",
              "Becomes magnified and inverted"])
    b.quiz_a(1, "B. Stays virtual & erect, always smaller",
             "A concave lens gives a virtual, erect, diminished image for "
             "every object position. As the object approaches, the image "
             "grows a little but never exceeds the object's size or becomes "
             "real.")
    b.quiz_q(2, "Identify the Lens", "A lens has a power of −2.5 D. This lens "
             "is:", ["A convex lens of focal length 40 cm",
             "A concave lens of focal length 40 cm",
             "A convex lens of focal length 25 cm",
             "A concave lens of focal length 25 cm"])
    b.quiz_a(2, "B. Concave lens, f = 40 cm",
             "P = 1/f, so f = 1/P = 1/(−2.5) = −0.4 m = −40 cm. The negative "
             "sign means it is a diverging (concave) lens, and its focal "
             "length is 40 cm.")
    b.quiz_q(3, "Lens Formula", "The correct lens formula is:",
             ["1/v + 1/u = 1/f", "1/v − 1/u = 1/f", "1/u − 1/v = 1/f",
              "v − u = f"])
    b.quiz_a(3, "B. 1/v − 1/u = 1/f",
             "The thin-lens formula is 1/v − 1/u = 1/f, with all quantities "
             "carrying their proper signs.")
    b.divider(2, "Part 2", "Magnification, Power & Uses",
              "Measuring images, lens strength and applications")
    b.statement("MAGNIFICATION", "Linear Magnification",
                "Magnification tells us how many times bigger (or smaller) the "
                "image is compared with the object.",
                formula="m  =  height of image / height of object  =  v / u",
                points=["m greater than 1 → image magnified; less than 1 → "
                        "diminished.",
                        "A negative m means a real, inverted image; positive m "
                        "means a virtual, erect image.",
                        "It links the image size directly to the distances v "
                        "and u."],
                notes="Define m two ways (heights and distances). The SIGN of m "
                      "encodes real/inverted vs virtual/erect.")
    b.worked("WORKED EXAMPLE", "Finding the Magnification",
             "For the previous lens, u = −30 cm and v = +60 cm. Find the "
             "magnification and describe the image.",
             ["m = v / u = (+60) / (−30)",
              "m = −2",
              "|m| = 2 → image is twice the object's size",
              "negative sign → image is real and inverted"],
             "m = −2 : a real, inverted image, magnified 2×",
             notes="Connect the negative sign to 'real and inverted'. Magnitude "
                   "2 means twice as tall.")
    b.statement("POWER", "Power of a Lens",
                "The power of a lens measures how strongly it converges or "
                "diverges light — the shorter the focal length, the greater "
                "the power.",
                formula="P  =  1 / f (in metres)        unit: dioptre (D)",
                points=["f must be in metres; P is in dioptres (D).",
                        "A convex lens has positive power; a concave lens has "
                        "negative power.",
                        "Example: f = 50 cm = 0.5 m → P = 1/0.5 = +2 D."],
                notes="Stress f in METRES. Power is just the reciprocal; sign "
                      "follows the lens type.")
    b.worked("WORKED EXAMPLE", "Calculating Power",
             "Find the power of a concave lens of focal length 25 cm.",
             ["Sign convention: f = −25 cm = −0.25 m",
              "P = 1 / f = 1 / (−0.25)",
              "P = −4 D"],
             "P = −4 D (negative, because it is a diverging lens)",
             notes="Convert to metres first, keep the negative sign for the "
                   "concave lens.")
    b.text_image("APPLICATIONS", "Lenses Around Us",
                 ["Spectacles correct short sight (concave) and long sight "
                  "(convex).",
                  "Cameras and the eye use convex lenses to form real images.",
                  "Microscopes and telescopes combine lenses to magnify.",
                  "Projectors and magnifying glasses enlarge what we see."],
                 apps or magn, img_side="right", img_w=5.4, img_h=3.6,
                 panel_title="Everyday optics",
                 caption="Eyeglasses and camera lenses in daily life",
                 notes="Link lens power and type to real corrective lenses: "
                       "concave for myopia, convex for hypermetropia.")
    b.cards("EYE DEFECTS", "Correcting Vision With Lenses", [
        ("Short sight (myopia)", "The eye over-converges; distant objects "
         "focus in front of the retina. Corrected with a concave lens."),
        ("Long sight (hypermetropia)", "The eye under-converges; near objects "
         "focus behind the retina. Corrected with a convex lens."),
        ("Concave = negative power", "Diverges light slightly before it enters "
         "the eye."),
        ("Convex = positive power", "Adds converging power to help the eye "
         "focus near objects."),
    ], notes="A favourite application question. Match the defect to the "
             "corrective lens and its sign of power.")
    b.bullets("EXPERIMENT", "Finding the Focal Length of a Convex Lens", [
        "Point the lens at a distant object (a far window or tree).",
        "Move a white screen behind the lens until a sharp image forms.",
        "The object is effectively at infinity, so the image forms at F.",
        "Measure the distance from the lens to the screen.",
        "That distance is the focal length of the convex lens.",
    ], panel_title="Distant-object method",
       notes="A quick, classic ICSE practical. Works because rays from a far "
             "object are nearly parallel, so they focus at F.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Concave lens", "always virtual, erect, diminished image"),
        ("Sign convention", "u negative; convex f positive, concave f negative"),
        ("Lens formula", "1/v − 1/u = 1/f"),
        ("Magnification", "m = v/u = hi/ho; sign gives real/virtual"),
        ("Power", "P = 1/f (metres), unit dioptre; sign follows lens type"),
        ("Focal length", "distant-object method: image of far object forms at F"),
    ], notes="Rapid recap; cold-call the formulae and their sign rules.")
    b.quiz_intro("Quiz 2", "Final Check — Numbers & Power", 5)
    b.quiz_q(1, "Power Unit", "The SI unit of the power of a lens is the:",
             ["Watt", "Dioptre", "Metre", "Newton"])
    b.quiz_a(1, "B. Dioptre",
             "Power P = 1/f with f in metres, so its unit is the dioptre (D). "
             "1 D is the power of a lens of focal length 1 metre.")
    b.quiz_q(2, "Power Value", "A convex lens has a focal length of 20 cm. Its "
             "power is:", ["+0.2 D", "+5 D", "−5 D", "+20 D"])
    b.quiz_a(2, "B. +5 D",
             "f = 20 cm = 0.2 m, so P = 1/0.2 = +5 D. It is positive because "
             "the lens is convex (converging).")
    b.quiz_q(3, "Magnification Sign", "A lens produces a magnification of "
             "m = −3. The image is:", ["Virtual and erect",
             "Real and inverted", "Virtual and diminished",
             "Same size as object"])
    b.quiz_a(3, "B. Real and inverted",
             "A negative magnification means a real, inverted image; the "
             "magnitude 3 means it is three times the object's size.")
    b.quiz_q(4, "Lens Formula", "An object at u = −15 cm gives an image at "
             "v = +30 cm. The focal length is:", ["+10 cm", "+45 cm",
             "−10 cm", "+30 cm"])
    b.quiz_a(4, "A. +10 cm",
             "1/f = 1/v − 1/u = 1/30 − 1/(−15) = 1/30 + 2/30 = 3/30 = 1/10, so "
             "f = +10 cm (a convex lens).")
    b.quiz_q(5, "Eye Defect", "Short sight (myopia) is corrected by using a:",
             ["Convex lens", "Concave lens", "Plane mirror", "Prism"])
    b.quiz_a(5, "B. Concave lens",
             "A short-sighted eye over-converges light, so distant objects "
             "focus in front of the retina. A concave (diverging) lens of "
             "negative power corrects this.")
    b.closing("From Eyeglasses to Telescopes",
              "Sign convention, the lens formula and power turn lenses from "
              "magic into measurable physics.")
    return b


def build():
    for fname, fn in [("G10_S43_Refraction_Through_a_Lens_1.pptx", deck1),
                      ("G10_S44_Refraction_Through_a_Lens_2.pptx", deck2)]:
        b = fn()
        issues = b.qa()
        b.save(os.path.join(OUT, fname))
        n = len(b.prs.slides._sldIdLst)
        print(f"=== {fname} === slides: {n}")
        if issues:
            print("  QA ISSUES:")
            for i in issues:
                print("   -", i)
        else:
            print("  QA: clean")


if __name__ == "__main__":
    build()
