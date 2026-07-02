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

    b.title("Class 10 • Optics", "The Human Eye & Optical Instruments",
            "Structure of the eye  •  Accommodation  •  Defects of vision  •  "
            "Microscope & telescope", img=eye)
    b.objectives([
        "Describe the structure of the human eye and the function of each part",
        "Explain accommodation and the near and far points of the eye",
        "Identify the defects of vision and how each is corrected",
        "Calculate the power of a corrective lens",
        "Describe the simple and compound microscope",
        "Describe the astronomical telescope",
    ])
    b.divider(1, "Part 1", "The Human Eye",
              "How the eye forms an image and adjusts focus")
    b.text_image("STRUCTURE", "Structure of the Human Eye",
                 ["The eye focuses light to form a real, inverted image on the "
                  "retina — like a natural camera.",
                  "Most bending of light happens at the cornea; the lens makes "
                  "the fine adjustment.",
                  "The retina has rods (dim light) and cones (colour) that "
                  "signal the brain along the optic nerve.",
                  "The figure shows the eye in section, from the cornea in "
                  "front to the optic nerve behind."],
                 eye, img_side="right", img_w=4.9, img_h=4.2,
                 panel_title="A living optical instrument",
                 caption="Vertical section of the human eye",
                 notes="Walk the light path: cornea → aqueous humour → pupil → "
                       "lens → vitreous humour → retina. Image on the retina is "
                       "real and inverted; the brain re-inverts it.")
    b.cards("PARTS & FUNCTIONS", "Parts of the Eye and What They Do", [
        ("Cornea", "The transparent front layer where most refraction of "
         "light takes place."),
        ("Iris & pupil", "The iris controls the size of the pupil, adjusting "
         "how much light enters."),
        ("Eye lens & ciliary muscles", "A flexible lens whose focal length the "
         "ciliary muscles change to focus."),
        ("Retina, rods & cones, optic nerve", "The screen where the image "
         "forms; rods/cones convert it to signals for the brain."),
    ], notes="Cornea = fixed refraction; iris/pupil = light control; "
             "lens+ciliary = focusing; retina+optic nerve = detection. "
             "Yellow spot = sharpest vision, blind spot = no receptors.")
    b.statement("ACCOMMODATION", "Power of Accommodation",
                "The ability of the eye to change the focal length of its lens "
                "so as to focus objects at different distances is called "
                "accommodation.",
                formula="Near point = 25 cm   •   Far point = infinity (normal "
                        "eye)",
                points=["Distant object: ciliary muscles relax, the lens is "
                        "thin (long focal length).",
                        "Near object: ciliary muscles contract, the lens "
                        "becomes thick (short focal length).",
                        "The least distance of distinct vision for a normal eye "
                        "is 25 cm."],
                notes="Accommodation = the lens changing focal length via the "
                      "ciliary muscles. Near point 25 cm, far point infinity. "
                      "The lens cannot focus objects closer than the near "
                      "point.")
    b.bullets("PERSISTENCE", "A Couple of Key Facts", [
        ("Persistence of vision", "An image stays on the retina for about "
         "1/16 s after the object is removed — the basis of cinema."),
        ("Real, inverted image", "The retinal image is real and inverted; the "
         "brain interprets it as upright."),
        ("Two eyes", "Binocular vision gives a wider field of view and helps "
         "us judge distance (depth)."),
    ], panel_title="Good to remember",
       notes="Persistence of vision (~1/16 s) underlies moving pictures. Retinal "
             "image is inverted; binocular vision gives depth perception.")
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
    b.cards("DEFECTS", "Common Defects of Vision", [
        ("Myopia (short sight)", "Distant objects blur; the image forms IN "
         "FRONT of the retina. Corrected by a concave (diverging) lens."),
        ("Hypermetropia (long sight)", "Near objects blur; the image forms "
         "BEYOND the retina. Corrected by a convex (converging) lens."),
        ("Presbyopia", "The lens hardens with age and the near point recedes; "
         "corrected by bifocal (or progressive) lenses."),
        ("Astigmatism", "Uneven curvature of the cornea blurs some directions; "
         "corrected by a cylindrical lens."),
    ], notes="Four defects. Myopia → concave; hypermetropia → convex; "
             "presbyopia → bifocal; astigmatism → cylindrical. Tie each to "
             "where the image forms relative to the retina.")
    b.statement("MYOPIA vs HYPERMETROPIA", "Where the Image Forms",
                "A defect is named by where the image of the object falls "
                "relative to the retina.",
                formula="Myopia: image before the retina  •  Hypermetropia: "
                        "image behind the retina",
                points=["Myopia — eyeball too long or lens too converging; a "
                        "concave lens moves the image back onto the retina.",
                        "Hypermetropia — eyeball too short or lens too weak; a "
                        "convex lens moves the image forward onto the retina.",
                        "The corrective lens supplies exactly the missing (or "
                        "excess) converging power."],
                notes="Concave lens diverges light first, correcting myopia; "
                      "convex lens adds convergence, correcting hypermetropia. "
                      "Power of the lens P = 1/f (f in metres).")
    b.worked("WORKED EXAMPLE", "Power of a Corrective Lens",
             "A short-sighted person cannot see beyond 2 m. Find the power of "
             "the spectacle lens that lets them see distant objects. (The lens "
             "must form the image of a distant object at their far point, 2 m.)",
             ["The concave lens forms a virtual image at the far point: "
              "v = −2 m, u = −∞",
              "1/f = 1/v − 1/u = (−1/2) − 0 = −0.5",
              "f = −2 m",
              "P = 1/f = 1/(−2)"],
             "P = −0.5 D  (a concave lens, as expected for myopia)",
             notes="For distant objects u → ∞, so 1/f = 1/v. The negative power "
                   "confirms a concave (diverging) lens is needed for myopia.")
    b.cards("MICROSCOPE", "Microscopes", [
        ("Simple microscope", "A single convex lens of short focal length used "
         "as a magnifying glass; gives a virtual, erect, magnified image."),
        ("Compound microscope", "Two convex lenses — an objective and an "
         "eyepiece — to see very small, near objects."),
        ("How it magnifies", "The objective forms a real magnified image, "
         "which the eyepiece magnifies further like a simple microscope."),
        ("Total magnification", "m = m(objective) × m(eyepiece) — the two "
         "magnifications multiply."),
    ], notes="Simple microscope = one convex lens (magnifier). Compound "
             "microscope = objective + eyepiece; magnifications multiply. Used "
             "for tiny nearby objects.")
    b.cards("TELESCOPE", "The Astronomical Telescope", [
        ("Purpose", "To see distant objects such as stars and planets."),
        ("Two lenses", "A large objective (long focal length) and an eyepiece "
         "(short focal length)."),
        ("Image", "The objective forms a real image of the distant object; the "
         "eyepiece magnifies it."),
        ("Magnification", "In normal adjustment, m = f(objective) / "
         "f(eyepiece)."),
    ], notes="Astronomical telescope: long-focus objective + short-focus "
             "eyepiece. m = f_o/f_e. Contrast with the microscope's short-focus "
             "objective for near objects.")
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
