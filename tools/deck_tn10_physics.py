"""
Tamil Nadu (Samacheer Kalvi / SSLC) — Standard 10 Science, Physics decks.

Scope: physics concept sessions of the Std-10 tuitions planner from session 22
onward (Thermal Physics S37/S38 already built separately). Chapters: Optics
(Human Eye & Optical Instruments, S22), Electricity (S52/S53/S55), Acoustics
(S80/S81) and Nuclear Physics (S92/S93/S95). Content covers the full Samacheer
Kalvi Science textbook treatment of each topic.

House config: teaching-friendly restyle (mhstyle), reserved logo space, no
footer, two quizzes with mirrored answer reveals, real web/Qwen images (vision
reviewed) for complex figures with clean cards elsewhere, and a compact
10-question homework MCQ section (5 per slide) at the end.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import mhstyle
import tnextra

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "TN_Grade10"))
os.makedirs(OUT, exist_ok=True)
mhstyle.apply()
tnextra.apply()


# ===========================================================================
# S22 — Optics: The Human Eye & Optical Instruments
# ===========================================================================
def human_eye_deck():
    footer = "Optics — The Human Eye  •  Tamil Nadu SSLC Science"
    b = Builder(footer, accent=C["purple"])
    eye = b.asset("tn10_eye_structure", None)
    myo = b.asset("tn10_myopia", None)
    hyp = b.asset("tn10_hypermetropia", None)
    tele = b.asset("tn10_telescope", None)

    b.title("Class 10 • Optics", "The Human Eye & Optical Instruments",
            "Structure of the eye  •  Accommodation  •  Defects of vision  •  "
            "Microscope & telescope", img=eye)
    b.objectives([
        "Describe the structure of the human eye and the function of each part",
        "Explain how the eye forms an image on the retina",
        "Explain accommodation and the near and far points of the eye",
        "Identify the defects of vision and how each is corrected",
        "Calculate the power of a corrective lens",
        "Describe the simple microscope, compound microscope and telescope",
    ])
    # ---------------------------------------------------------------- Part 1
    b.divider(1, "Part 1", "The Human Eye",
              "Its parts, how it forms an image, and how it focuses")
    b.text_image("STRUCTURE", "Structure of the Human Eye",
                 ["The eye is a nearly spherical organ, about 2.3 cm across, "
                  "filled with transparent fluids.",
                  "Light enters through the cornea, passes the pupil and lens, "
                  "and falls on the retina.",
                  "The figure names the main parts from the cornea in front to "
                  "the optic nerve behind.",
                  "It works like a camera: a lens system throwing an image on "
                  "a light-sensitive screen."],
                 eye, img_side="right", img_w=5.2, img_h=4.1,
                 panel_title="A living optical instrument",
                 caption="Labelled section of the human eye",
                 notes="Orient students on the labelled figure. Light path: "
                       "cornea → aqueous humour → pupil → lens → vitreous "
                       "humour → retina.")
    b.cards("THREE COATS", "The Three Layers (Coats) of the Eyeball", [
        ("Sclera (outer)", "The tough, white, protective coat; its "
         "transparent front bulge is the cornea."),
        ("Choroid (middle)", "A dark, blood-rich layer that nourishes the eye "
         "and stops internal reflection of light."),
        ("Retina (inner)", "The light-sensitive screen on which the image is "
         "formed."),
        ("Cornea", "The clear front of the sclera where MOST of the bending "
         "(refraction) of light happens."),
    ], notes="Three coats: sclera (protect), choroid (nourish + absorb stray "
             "light), retina (detect). The cornea is the front window doing "
             "most refraction.")
    b.cards("LIGHT CONTROL & FOCUSING", "Iris, Pupil, Lens & Humours", [
        ("Iris", "The coloured ring that controls the size of the pupil — like "
         "a camera's aperture."),
        ("Pupil", "The central opening that widens in dim light and narrows in "
         "bright light."),
        ("Eye lens & ciliary muscles", "A flexible, jelly-like convex lens "
         "whose focal length the ciliary muscles adjust."),
        ("Aqueous & vitreous humour", "Transparent fluids that keep the eye in "
         "shape and help refract light."),
    ], notes="Iris/pupil = automatic light control; lens+ciliary = focusing; "
             "aqueous (front) and vitreous (back) humours keep shape and "
             "refract.")
    b.cards("THE SCREEN", "The Retina — Where the Image Forms", [
        ("Rods", "Very sensitive cells that work in dim light but see only "
         "shades of grey."),
        ("Cones", "Cells that need bright light and give us colour vision "
         "(sensitive to red, green, blue)."),
        ("Yellow spot (fovea)", "The most sensitive point, where the sharpest "
         "image forms."),
        ("Blind spot", "Where the optic nerve leaves the eye — no rods or "
         "cones, so no image is detected there."),
    ], notes="Retina cells: rods (dim, grey) vs cones (bright, colour). Fovea "
             "= sharpest vision; blind spot = optic-nerve exit, no receptors.")
    b.statement("IMAGE FORMATION", "How the Eye Forms an Image",
                "The cornea and eye lens together act as a convex lens that "
                "forms a real, inverted, diminished image on the retina.",
                formula="Object → cornea + lens → real inverted image on the "
                        "retina",
                points=["Most refraction occurs at the cornea; the lens only "
                        "fine-tunes the focus.",
                        "The image on the retina is real and inverted.",
                        "The brain interprets the signals so that we perceive "
                        "the world upright."],
                notes="Cornea+lens = a convex system → real inverted image on "
                      "retina. The brain re-inverts it. Same optics as a "
                      "camera.")
    b.statement("ACCOMMODATION", "Power of Accommodation",
                "The ability of the eye to change the focal length of its lens "
                "to focus objects at different distances is called "
                "accommodation.",
                formula="near object → lens thick (short f)   •   far object → "
                        "lens thin (long f)",
                points=["For a distant object the ciliary muscles relax and the "
                        "lens becomes thin (long focal length).",
                        "For a near object the ciliary muscles contract and the "
                        "lens becomes thick (short focal length).",
                        "The eye adjusts automatically and almost instantly."],
                notes="Accommodation = ciliary muscles changing the lens's "
                      "focal length. Relaxed → thin lens (far); contracted → "
                      "thick lens (near).")
    b.cards("RANGE OF VISION", "Near Point, Far Point & Range of Vision", [
        ("Near point", "The closest point the eye can focus clearly — about "
         "25 cm for a normal eye."),
        ("Least distance of distinct vision", "The near-point distance, "
         "D = 25 cm; objects nearer than this look blurred."),
        ("Far point", "The farthest point the eye can focus — infinity for a "
         "normal eye."),
        ("Range of vision", "A normal eye sees clearly all the way from 25 cm "
         "to infinity."),
    ], notes="Near point 25 cm (= least distance of distinct vision D), far "
             "point infinity. Range of clear vision = 25 cm → ∞.")
    b.bullets("MORE VISION FACTS", "Persistence of Vision & Binocular Vision", [
        ("Persistence of vision", "An image lingers on the retina for about "
         "1/16 s after the object is removed — this is why rapid still frames "
         "look like a moving film."),
        ("Binocular vision", "Using two eyes gives a wider field of view and "
         "lets us judge distance and depth."),
        ("Colour blindness", "A genetic defect (mostly in males) in which "
         "certain cones are missing, so some colours cannot be told apart."),
    ], panel_title="Good to know",
       notes="Persistence of vision (~1/16 s) → cinema. Binocular vision → "
             "depth perception. Colour blindness = defective/missing cones.")
    b.quiz_intro("Quiz 1", "Check — The Eye & Accommodation", 4)
    b.quiz_q(1, "Most refraction", "In the human eye, most of the refraction "
             "(bending) of incoming light takes place at the:",
             ["Retina", "Cornea", "Iris", "Optic nerve"])
    b.quiz_a(1, "B. Cornea",
             "The greatest change in direction of light happens as it enters "
             "the curved, transparent cornea. The eye lens then makes only the "
             "fine focusing adjustment.")
    b.quiz_q(2, "Focusing", "The eye focuses on objects at different distances "
             "by the ciliary muscles changing the lens's:",
             ["Diameter of the pupil", "Focal length",
              "Colour", "Position on the retina"])
    b.quiz_a(2, "B. Focal length",
             "Accommodation works by the ciliary muscles altering the "
             "curvature — and hence the focal length — of the flexible eye "
             "lens, not by moving it.")
    b.quiz_q(3, "Least distance", "For a normal human eye, the least distance "
             "of distinct vision (near point) is about:",
             ["10 cm", "25 cm", "50 cm", "infinity"])
    b.quiz_a(3, "B. 25 cm",
             "A normal eye can focus objects clearly from 25 cm (the near "
             "point) out to infinity (the far point). Objects closer than "
             "25 cm look blurred.")
    b.quiz_q(4, "Retinal image", "The image formed on the retina of a normal "
             "eye is:", ["Virtual and erect", "Real and inverted",
              "Virtual and inverted", "Real and erect"])
    b.quiz_a(4, "B. Real and inverted",
             "The convex eye-lens system forms a real, inverted image on the "
             "retina; the brain processes it so that we perceive the world the "
             "right way up.")
    b.divider(2, "Part 2", "Defects of Vision & Optical Instruments",
              "Correcting sight, and seeing the very small and very far")
    b.cards("FOUR DEFECTS", "Common Defects of Vision — Overview", [
        ("Myopia (short sight)", "Can see near objects but not distant ones; "
         "image falls in front of the retina."),
        ("Hypermetropia (long sight)", "Can see distant objects but not near "
         "ones; image falls behind the retina."),
        ("Presbyopia", "Age-related loss of accommodation — both near and far "
         "vision weaken."),
        ("Astigmatism", "Uneven curvature of the cornea/lens blurs lines in "
         "certain directions."),
    ], notes="Overview of the four defects. The next slides show myopia and "
             "hypermetropia with corrections; then presbyopia and astigmatism.")
    b.text_image("MYOPIA", "Myopia (Short-sightedness) & Its Correction",
                 ["The eyeball is too long, or the lens too strongly "
                  "converging.",
                  "The image of a distant object forms IN FRONT of the retina, "
                  "so distant objects look blurred.",
                  "A concave (diverging) lens spreads the light out a little "
                  "before it enters the eye.",
                  "This shifts the image back exactly onto the retina — clear "
                  "vision restored."],
                 myo, img_side="right", img_w=5.6, img_h=3.4,
                 panel_title="Corrected by a concave lens",
                 caption="Image forms in front of the retina",
                 notes="Myopia: image before retina (long eyeball / strong "
                       "lens). Concave lens of suitable negative power moves it "
                       "onto the retina.")
    b.text_image("HYPERMETROPIA", "Hypermetropia (Long-sightedness) & Its "
                 "Correction",
                 ["The eyeball is too short, or the lens too weakly "
                  "converging.",
                  "The image of a near object forms BEHIND the retina, so near "
                  "objects look blurred.",
                  "A convex (converging) lens adds the missing converging power "
                  "before light enters the eye.",
                  "This brings the image forward onto the retina."],
                 hyp, img_side="left", img_w=5.6, img_h=3.4,
                 panel_title="Corrected by a convex lens",
                 caption="Image forms behind the retina",
                 notes="Hypermetropia: image behind retina (short eyeball / weak "
                       "lens). Convex lens of positive power brings it forward "
                       "onto the retina.")
    b.cards("PRESBYOPIA & ASTIGMATISM", "Two More Defects", [
        ("Presbyopia — cause", "With age the eye lens hardens and the ciliary "
         "muscles weaken, so accommodation is lost."),
        ("Presbyopia — correction", "The near point recedes; bifocal lenses "
         "(concave top for distance, convex bottom for reading) are used."),
        ("Astigmatism — cause", "The cornea or lens is not perfectly "
         "spherical, so some lines focus while others do not."),
        ("Astigmatism — correction", "A cylindrical lens of the correct axis "
         "corrects the uneven focusing."),
    ], notes="Presbyopia = age loss of accommodation → bifocals. Astigmatism = "
             "uneven curvature → cylindrical lens.")
    b.statement("POWER OF A LENS", "Power of a Corrective Lens",
                "The power of a lens tells us how strongly it converges or "
                "diverges light; it is the reciprocal of the focal length in "
                "metres.",
                formula="P = 1 / f (metres)     •     unit: dioptre (D)",
                points=["A convex (converging) lens has POSITIVE power.",
                        "A concave (diverging) lens has NEGATIVE power.",
                        "The optician's prescription is written directly in "
                        "dioptres."],
                notes="P = 1/f (f in metres), unit dioptre. Convex → +, concave "
                      "→ −. Used to work out the corrective lens needed.")
    b.worked("WORKED EXAMPLE", "Correcting Myopia",
             "A short-sighted person's far point is only 2 m. Find the power of "
             "the spectacle lens that lets them see distant objects clearly.",
             ["The concave lens must form the image of a distant object at the "
              "far point:  v = −2 m, u = −∞",
              "1/f = 1/v − 1/u = (−1/2) − 0",
              "f = −2 m",
              "P = 1/f = 1 / (−2)"],
             "P = −0.5 D  (a concave lens, as expected for myopia)",
             notes="For a distant object u → ∞ so 1/f = 1/v. Negative power "
                   "confirms a concave lens corrects myopia.")
    b.worked("WORKED EXAMPLE", "Correcting Hypermetropia",
             "A long-sighted person's near point is 50 cm. Find the power of "
             "the lens that lets them read at the normal 25 cm.",
             ["The convex lens forms a virtual image of the 25 cm object at the "
              "near point: u = −25 cm, v = −50 cm",
              "1/f = 1/v − 1/u = (−1/50) − (−1/25) = −1/50 + 2/50 = 1/50",
              "f = +50 cm = +0.5 m",
              "P = 1/f = 1 / 0.5"],
             "P = +2.0 D  (a convex lens, as expected for hypermetropia)",
             notes="The lens images the 25 cm object at the 50 cm near point. "
                   "Positive power confirms a convex lens corrects "
                   "hypermetropia.")
    b.cards("SIMPLE MICROSCOPE", "The Simple Microscope (Magnifying Glass)", [
        ("What it is", "A single convex lens of short focal length held close "
         "to the eye."),
        ("Object position", "The object is placed within the focal length of "
         "the lens."),
        ("Image", "A virtual, erect and magnified image is seen on the same "
         "side as the object."),
        ("Magnification", "m = 1 + D/f, where D = 25 cm — a shorter focal "
         "length gives more magnification."),
    ], notes="Simple microscope = one short-focus convex lens; object within f "
             "→ virtual, erect, magnified image. m = 1 + D/f.")
    b.cards("COMPOUND MICROSCOPE", "The Compound Microscope", [
        ("Two lenses", "An objective (short focal length) near the object and "
         "an eyepiece near the eye."),
        ("Stage 1", "The objective forms a real, inverted, magnified image of "
         "the tiny object."),
        ("Stage 2", "The eyepiece magnifies that image again, like a simple "
         "microscope."),
        ("Total magnification", "m = m(objective) × m(eyepiece) — the two "
         "magnifications multiply, giving very high magnification."),
    ], notes="Compound microscope: objective + eyepiece, both convex. Two-stage "
             "magnification multiplies. Used for cells, microbes, tiny "
             "structures.")
    b.cards("TELESCOPE", "The Astronomical (Refracting) Telescope", [
        ("Purpose", "To see distant objects such as stars, planets and the "
         "Moon."),
        ("Objective lens", "A large, long-focal-length lens that collects "
         "light and forms a real image of the distant object."),
        ("Eyepiece", "A short-focal-length lens that magnifies this image for "
         "the eye."),
        ("Magnification", "In normal adjustment m = f(objective) / f(eyepiece) "
         "— the opposite lens choice to the compound microscope."),
    ], notes="Astronomical telescope: long-focus objective + short-focus "
             "eyepiece; m = f_o/f_e. Opposite lens choice to the compound "
             "microscope, which uses a short-focus objective.")
    b.cards("APPLICATIONS", "Optical Instruments Around Us", [
        ("Spectacles", "Correct myopia, hypermetropia, presbyopia and "
         "astigmatism for clear everyday vision."),
        ("Microscopes", "Reveal cells, bacteria and tiny structures in biology "
         "and medicine."),
        ("Telescopes", "Let astronomers study distant stars, planets and "
         "galaxies."),
        ("Cameras & projectors", "Use convex lenses to form real images, just "
         "like the eye does on the retina."),
    ], notes="Tie the physics to real devices: spectacles, microscopes, "
             "telescopes, cameras — all use controlled refraction by lenses.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Structure", "cornea refracts; lens+ciliary focus; retina detects"),
        ("Accommodation", "lens changes focal length; near point 25 cm"),
        ("Myopia", "image before retina → concave lens"),
        ("Hypermetropia", "image behind retina → convex lens"),
        ("Microscope", "simple = one lens; compound = objective + eyepiece"),
        ("Telescope", "m = f(objective) / f(eyepiece)"),
    ], notes="Rapid recap; the defect–correction pairs and the "
             "microscope/telescope distinction are the key exam points.")
    b.quiz_intro("Quiz 2", "Final Check — Defects & Instruments", 5)
    b.quiz_q(1, "Correct myopia", "Myopia (short-sightedness) is corrected "
             "using a:", ["Convex lens", "Concave lens",
              "Cylindrical lens", "Bifocal lens"])
    b.quiz_a(1, "B. Concave lens",
             "In myopia the image forms in front of the retina, so a concave "
             "(diverging) lens is used to push the image back onto the retina.")
    b.quiz_q(2, "Old age", "With advancing age a person finds it hard to read "
             "small print held close. This defect is:",
             ["Myopia", "Astigmatism", "Presbyopia", "Colour blindness"])
    b.quiz_a(2, "C. Presbyopia",
             "Presbyopia is the age-related loss of accommodation as the lens "
             "stiffens; the near point recedes, so close work needs a "
             "converging (often bifocal) lens.")
    b.quiz_q(3, "Power sign", "The power of the lens used to correct "
             "hypermetropia is:", ["Negative (concave)", "Positive (convex)",
              "Zero", "Always −0.5 D"])
    b.quiz_a(3, "B. Positive (convex)",
             "Hypermetropia needs extra converging power to bring the image "
             "forward onto the retina, so a convex lens of positive power is "
             "used.")
    b.quiz_q(4, "Compound microscope", "A compound microscope uses two convex "
             "lenses because it must:",
             ["Correct colour", "Magnify a small near object in two stages",
              "See distant stars", "Reduce the image"])
    b.quiz_a(4, "B. Magnify a small near object in two stages",
             "The objective forms a real, enlarged image of the tiny object, "
             "and the eyepiece magnifies that image again — the two "
             "magnifications multiply for a very high total magnification.")
    b.quiz_q(5, "Telescope magnification", "In normal adjustment the "
             "magnification of an astronomical telescope is:",
             ["f(eyepiece) / f(objective)", "f(objective) × f(eyepiece)",
              "f(objective) / f(eyepiece)", "f(objective) + f(eyepiece)"])
    b.quiz_a(5, "C. f(objective) / f(eyepiece)",
             "A telescope uses a long-focus objective and a short-focus "
             "eyepiece, so m = f_o/f_e — a large ratio gives high "
             "magnification of distant objects.")
    b.closing("Seeing the World",
              "From the near point of the eye to a distant star, lenses — "
              "natural and made — bend light so that we can see.")
    b.homework([
        {"q": "Most of the refraction of light entering the eye occurs at the:",
         "opts": ["lens", "cornea", "retina", "pupil"], "ans": "B. cornea"},
        {"q": "The size of the pupil is controlled by the:",
         "opts": ["cornea", "iris", "retina", "ciliary muscle"],
         "ans": "B. iris"},
        {"q": "The light-sensitive screen of the eye is the:",
         "opts": ["cornea", "iris", "retina", "sclera"], "ans": "C. retina"},
        {"q": "Colour vision is due to the retinal cells called:",
         "opts": ["rods", "cones", "nerves", "muscles"], "ans": "B. cones"},
        {"q": "The near point of a normal human eye is about:",
         "opts": ["10 cm", "25 cm", "50 cm", "100 cm"], "ans": "B. 25 cm"},
        {"q": "In myopia the image of a distant object is formed:",
         "opts": ["on the retina", "in front of the retina",
                  "behind the retina", "at the cornea"],
         "ans": "B. in front of the retina"},
        {"q": "Hypermetropia is corrected using a lens that is:",
         "opts": ["concave", "convex", "cylindrical", "plane"],
         "ans": "B. convex"},
        {"q": "Astigmatism is corrected using a:",
         "opts": ["concave lens", "convex lens", "cylindrical lens",
                  "bifocal lens"], "ans": "C. cylindrical lens"},
        {"q": "A simple microscope is essentially a single:",
         "opts": ["concave lens", "convex lens", "plane mirror", "prism"],
         "ans": "B. convex lens"},
        {"q": "The magnification of an astronomical telescope is:",
         "opts": ["f_e / f_o", "f_o / f_e", "f_o × f_e", "f_o − f_e"],
         "ans": "B. f_o / f_e"},
    ])
    return b


def build():
    for fname, fn in [("TN10_S22_Human_Eye.pptx", human_eye_deck)]:
        b = fn()
        issues = b.qa()
        b.save(os.path.join(OUT, fname))
        print(f"=== {fname} === slides: {len(b.prs.slides._sldIdLst)}")
        for i in issues:
            print("   -", i)
        if not issues:
            print("  QA: clean")


if __name__ == "__main__":
    build()
