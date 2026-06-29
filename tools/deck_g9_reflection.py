"""
Grade 9 Physics — Chapter: Reflection of Light.
S87 (reflection, laws, plane-mirror images, lateral inversion, inclined
mirrors) and S88 (spherical mirrors, focus, ray diagrams, uses).
ICSE Class 9 (Selina Concise Physics) — fuller coverage incl. regular vs
irregular reflection and images in two inclined mirrors (n = 360/θ − 1).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Reflection of Light  •  ICSE Class 9 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    law = b.asset("g9rf_law", D.reflection_law("g9rf_law"))
    pm = b.asset("g9rf_plane", D.plane_mirror_image("g9rf_plane"))
    hero = b.asset("g9_mirror_hero", pm)

    b.title("ICSE • Class 9 • Light", "Reflection of Light",
            "Laws of reflection  •  Plane-mirror images  •  Lateral inversion "
            " •  Images in inclined mirrors", img=hero)
    b.objectives([
        "Define reflection and the terms used to describe it",
        "Distinguish regular from irregular reflection",
        "State and verify the laws of reflection",
        "Describe the image formed by a plane mirror",
        "Explain lateral inversion",
        "Find the number of images formed by two inclined mirrors",
    ])
    b.divider(1, "Part 1", "Reflection & the Laws",
              "How light bounces off a surface")
    b.bullets("TERMS", "Reflection — the Key Terms", [
        ("Reflection", "the bouncing back of light when it strikes a "
         "surface."),
        ("Incident & reflected ray", "the ray going to, and the ray coming "
         "back from, the surface."),
        ("Normal", "the line drawn at 90° to the surface at the point of "
         "incidence."),
        ("Angle of incidence (i) & reflection (r)", "measured between the rays "
         "and the normal."),
    ], panel_title="The vocabulary of reflection",
       notes="Define each term against a diagram. Angles are always from the "
             "normal, never the surface.")
    b.cards("TYPES", "Regular vs Irregular Reflection", [
        ("Regular reflection", "From a smooth, polished surface like a mirror "
         "— parallel rays stay parallel."),
        ("Irregular (diffuse)", "From a rough surface like paper — parallel "
         "rays scatter in all directions."),
        ("Why we see objects", "Diffuse reflection from objects sends light to "
         "our eyes from every angle."),
        ("Same laws", "Both kinds still obey the laws of reflection at each "
         "tiny point."),
    ], notes="Regular = mirror (clear image); irregular = paper (no image, but "
             "lets us see things). Both obey the laws locally.")
    b.text_image("LAWS", "The Laws of Reflection",
                 ["Law 1: the angle of incidence equals the angle of "
                  "reflection (i = r).",
                  "Law 2: the incident ray, the reflected ray and the normal "
                  "all lie in the same plane.",
                  "Both angles are measured from the normal.",
                  "They hold for every reflecting surface, flat or curved."],
                 law, img_side="right", img_w=5.4, img_h=3.6,
                 panel_title="i = r",
                 caption="Angle of incidence = angle of reflection",
                 notes="State both laws. The equality i = r is the workhorse "
                       "for all reflection problems.")
    b.bullets("VERIFICATION", "Verifying the Laws of Reflection", [
        "Fix a plane mirror upright on a sheet of paper and draw the normal.",
        "Shine a ray of light (or use pins) at the mirror at a chosen angle.",
        "Mark the incident and reflected rays and measure i and r with a "
        "protractor.",
        "Repeat for several angles — each time i = r, confirming the first "
        "law.",
    ], panel_title="The pin-and-protractor method",
       notes="Standard practical: measure i and r for several angles and show "
             "they are equal.")
    b.statement("ROTATING MIRROR", "When the Mirror Turns",
                "If the mirror is rotated while the incident ray is kept fixed, "
                "the reflected ray turns through twice that angle.",
                formula="mirror rotates by θ  →  reflected ray rotates by 2θ",
                points=["Turning the mirror by θ increases the angle of "
                        "incidence by θ.",
                        "The angle of reflection also increases by θ, so the "
                        "reflected ray swings by 2θ.",
                        "This is used in the optical lever and in moving-mirror "
                        "galvanometers."],
                notes="A favourite ICSE result: for a fixed incident ray, "
                      "rotating the mirror by θ turns the reflected ray by 2θ. "
                      "Basis of the optical lever.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Angle of Reflection", "A ray strikes a mirror so that it "
             "makes an angle of 30° with the mirror surface. The angle of "
             "reflection is:", ["30°", "60°", "90°", "15°"])
    b.quiz_a(1, "B. 60°",
             "Angles are measured from the normal, not the surface. If the ray "
             "is 30° from the surface, the angle of incidence is 90 − 30 = "
             "60°, and the angle of reflection equals it: 60°.")
    b.quiz_q(2, "Why See Paper?", "We can see a sheet of white paper from any "
             "direction because it produces:",
             ["Regular reflection", "Irregular (diffuse) reflection",
              "No reflection", "Refraction"])
    b.quiz_a(2, "B. Irregular (diffuse) reflection",
             "The rough surface of paper scatters light in all directions "
             "(diffuse reflection), so some reaches your eye wherever you "
             "stand — unlike a mirror's regular reflection.")
    b.quiz_q(3, "Normal Incidence", "A ray of light strikes a plane mirror "
             "along the normal (i = 0°). It is reflected:",
             ["At 90°", "Straight back along the same path",
              "Along the mirror", "Not at all"])
    b.quiz_a(3, "B. Straight back along the same path",
             "With i = 0°, the law i = r gives r = 0° too, so the ray returns "
             "straight back along its original path — normal incidence.")
    b.quiz_q(4, "Both Rays", "According to the second law of reflection, the "
             "incident ray, reflected ray and normal all lie:",
             ["In different planes", "In the same plane", "On the mirror",
              "Parallel to each other"])
    b.quiz_a(4, "B. In the same plane",
             "The second law states that the incident ray, the reflected ray "
             "and the normal at the point of incidence are all in one plane.")
    b.quiz_q(5, "Turn the Mirror", "A fixed ray of light strikes a mirror. If "
             "the mirror is rotated by 10°, the reflected ray turns by:",
             ["5°", "10°", "20°", "0°"])
    b.quiz_a(5, "C. 20°",
             "For a fixed incident ray, rotating the mirror by an angle turns "
             "the reflected ray by twice that angle. So a 10° turn of the "
             "mirror swings the reflected ray by 20°.")
    b.divider(2, "Part 2", "Plane-Mirror Images",
              "What a flat mirror does to light")
    b.text_image("IMAGE", "Image in a Plane Mirror",
                 ["Light from the object reflects off the mirror into the eye.",
                  "The brain traces the rays back to form a virtual image "
                  "behind the mirror.",
                  "The image is as far behind the mirror as the object is in "
                  "front.",
                  "It is virtual, erect and the same size as the object."],
                 pm, img_side="left", img_w=5.6, img_h=3.8,
                 panel_title="Virtual, erect, same size",
                 caption="Image is as far behind as the object is in front",
                 notes="The four characteristics: virtual, erect, same size, "
                       "as far behind. Plus laterally inverted (next slide).")
    b.cards("CHARACTERISTICS", "Characteristics of the Image", [
        ("Virtual", "Cannot be caught on a screen; it only appears to be "
         "behind the mirror."),
        ("Erect", "The right way up, same as the object."),
        ("Same size", "Exactly as large as the object."),
        ("Laterally inverted", "Left and right are swapped over."),
    ], notes="List all characteristics. Lateral inversion is the one students "
             "most often forget.")
    b.bullets("LATERAL INVERSION", "Lateral Inversion", [
        ("What it is", "The sideways swapping of left and right in a mirror "
         "image."),
        ("Your right hand", "Looks like the image's left hand."),
        ("AMBULANCE", "Written reversed on the front of the vehicle so it "
         "reads correctly in a driver's mirror."),
        ("Clock in a mirror", "Appears to run anticlockwise."),
    ], panel_title="Why left and right swap",
       notes="Lateral inversion: left↔right. The AMBULANCE lettering is the "
             "classic real-world example.")
    b.statement("INCLINED MIRRORS", "Images in Two Inclined Mirrors",
                "Two plane mirrors placed at an angle θ form several images of "
                "an object between them.",
                formula="Number of images  n  =  (360° / θ)  −  1",
                points=["At 90°, n = 360/90 − 1 = 3 images.",
                        "At 60°, n = 360/60 − 1 = 5 images.",
                        "Parallel mirrors (θ = 0°) form infinitely many "
                        "images.",
                        "Used in the kaleidoscope and the periscope."],
                notes="The inclined-mirror formula is a signature ICSE result. "
                      "Drill 90°→3 and 60°→5, and parallel→infinite.")
    b.cards("USES", "Uses of Plane Mirrors", [
        ("Looking glass", "The everyday mirror for seeing ourselves."),
        ("Periscope", "Two parallel mirrors at 45° let us see over walls or "
         "from a submarine."),
        ("Kaleidoscope", "Inclined mirrors make colourful, symmetric "
         "patterns."),
        ("Instruments", "Used in solar cookers and to read fine scales "
         "(galvanometers)."),
    ], notes="Real uses of plane mirrors. The periscope (parallel mirrors) and "
             "kaleidoscope (inclined mirrors) tie back to the chapter.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Reflection", "light bounces back; angles measured from the normal"),
        ("Regular vs irregular", "smooth mirror vs rough paper"),
        ("Laws", "i = r; incident, reflected & normal in one plane"),
        ("Plane-mirror image", "virtual, erect, same size, as far behind"),
        ("Lateral inversion", "left and right are swapped"),
        ("Inclined mirrors", "n = 360/θ − 1; parallel → infinite"),
    ], notes="Rapid recap; i = r and the inclined-mirror formula are the key "
             "exam points.")
    b.quiz_intro("Quiz 2", "Final Check — Plane Mirrors", 5)
    b.quiz_q(1, "Step Back", "You stand 1 m in front of a plane mirror. The "
             "distance between you and your image is:",
             ["1 m", "0.5 m", "2 m", "4 m"])
    b.quiz_a(1, "C. 2 m",
             "The image is as far behind the mirror as you are in front — 1 m "
             "behind. So you and your image are 1 + 1 = 2 m apart.")
    b.quiz_q(2, "Walk Toward It", "You walk toward a plane mirror at 1 m/s. "
             "Your image approaches you at:", ["1 m/s", "0.5 m/s", "2 m/s",
              "It stays still"])
    b.quiz_a(2, "C. 2 m/s",
             "As you move 1 m closer, the image also moves 1 m closer (staying "
             "level with you behind the glass). So the gap between you closes "
             "at 1 + 1 = 2 m/s.")
    b.quiz_q(3, "AMBULANCE", "The word AMBULANCE is painted reversed on the "
             "front of the vehicle so that:",
             ["It looks decorative", "It reads correctly in the rear-view "
              "mirror of the car ahead", "It is harder to read",
              "It glows at night"])
    b.quiz_a(3, "B. It reads correctly in a mirror",
             "A driver ahead sees the ambulance in their mirror, which "
             "laterally inverts it. Writing it reversed means the mirror image "
             "appears the right way round and is easy to read.")
    b.quiz_q(4, "Right Angle Mirrors", "Two plane mirrors are placed at 90° to "
             "each other. The number of images of an object between them is:",
             ["1", "2", "3", "Infinite"])
    b.quiz_a(4, "C. 3",
             "Using n = 360/θ − 1 with θ = 90°: n = 360/90 − 1 = 4 − 1 = 3 "
             "images.")
    b.quiz_q(5, "Barber's Mirrors", "Why do two parallel mirrors in a barber's "
             "shop show a seemingly endless row of images?",
             ["The light speeds up", "θ = 0°, so n = 360/θ − 1 is infinite",
              "The mirrors are curved", "The light changes colour"])
    b.quiz_a(5, "B. θ = 0°, so the number of images is infinite",
             "For parallel mirrors the angle between them is zero, and "
             "360/0 is infinite. Each mirror keeps re-reflecting the other's "
             "image, giving an endless series.")
    b.closing("Mirror, Mirror",
              "From i = r to a barber's endless reflections, the simple laws "
              "of reflection explain every image in a flat mirror.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    cc = b.asset("g9rf_concave", D.concave_mirror_image("g9rf_concave"))
    cx = b.asset("g9rf_convex", D.convex_mirror_image("g9rf_convex"))
    hero = b.asset("g9_spherical_hero", cc)

    b.title("ICSE • Class 9 • Light", "Spherical Mirrors",
            "Concave & convex mirrors  •  Focus & focal length  •  Ray "
            "diagrams  •  Uses", img=hero)
    b.objectives([
        "Identify concave and convex spherical mirrors",
        "Define the terms used for spherical mirrors",
        "Relate focal length to radius of curvature (f = R/2)",
        "Use the convenient rays to construct ray diagrams",
        "Describe images formed by concave and convex mirrors",
        "State the uses of concave and convex mirrors",
    ])
    b.divider(1, "Part 1", "Spherical Mirrors & Their Terms",
              "Curved reflecting surfaces")
    b.cards("TWO TYPES", "Concave and Convex Mirrors", [
        ("Spherical mirror", "A mirror that is part of a hollow sphere."),
        ("Concave", "Reflecting surface curves inward; it converges light (a "
         "converging mirror)."),
        ("Convex", "Reflecting surface bulges outward; it diverges light (a "
         "diverging mirror)."),
        ("Everywhere", "Shaving and make-up mirrors are concave; vehicle "
         "rear-view mirrors are convex."),
    ], notes="Concave = caves in, converges; convex = bulges out, diverges. "
             "Anchor each with a real mirror.")
    b.bullets("TERMS", "Terms for a Spherical Mirror", [
        ("Pole (P)", "the centre of the mirror's reflecting surface."),
        ("Centre of curvature (C)", "the centre of the sphere the mirror is "
         "part of."),
        ("Radius of curvature (R)", "the radius of that sphere (distance PC)."),
        ("Principal focus (F)", "where rays parallel to the axis meet (or "
         "appear to)."),
        ("Focal length (f)", "the distance from the pole to the focus, PF."),
    ], panel_title="Pole, centre, focus, focal length",
       notes="Define each term against a diagram. These feed straight into the "
             "ray diagrams and f = R/2.")
    b.cards("MORE TERMS", "Principal Axis, Aperture & the Normal", [
        ("Principal axis", "The straight line through the pole P and the centre "
         "of curvature C."),
        ("Aperture", "The width of the mirror — the part that actually "
         "reflects light."),
        ("Normal at a point", "The line joining that point to the centre of "
         "curvature C."),
        ("Small aperture", "We assume a small aperture so the rays focus "
         "sharply at a single point."),
    ], notes="Round out the terms: principal axis (P–C line), aperture (mirror "
             "width), and that the normal at any point passes through C.")
    b.statement("f = R/2", "Focus and Focal Length",
                "For a spherical mirror, the principal focus lies exactly "
                "halfway between the pole and the centre of curvature.",
                formula="focal length  f  =  R / 2",
                points=["Rays parallel to the principal axis converge at F "
                        "(concave) or appear to come from F (convex).",
                        "So the focal length is half the radius of curvature.",
                        "A more sharply curved mirror has a shorter focal "
                        "length."],
                notes="f = R/2 is a key relation. Concave focus is real; "
                      "convex focus is virtual (behind the mirror).")
    b.cards("RAY RULES", "Convenient Rays for Ray Diagrams", [
        ("Parallel ray", "A ray parallel to the axis reflects through the "
         "focus F."),
        ("Focal ray", "A ray through F reflects back parallel to the axis."),
        ("Central-of-curvature ray", "A ray through C hits the mirror normally "
         "and returns along itself."),
        ("Two are enough", "Any two of these locate the image; the third is a "
         "check."),
    ], notes="The standard rays for mirror ray diagrams. Two rays fix the "
             "image position.")
    b.worked("WORKED EXAMPLE", "Focal Length and Radius",
             "A concave mirror forms a sharp image of a distant tree on a "
             "screen 15 cm from the mirror. Find its radius of curvature.",
             ["A distant object focuses at the principal focus, so f = 15 cm",
              "f = R / 2   →   R = 2 f",
              "R = 2 × 15 = 30 cm"],
             "Radius of curvature R = 30 cm",
             notes="A distant object images at F, so the screen distance is f. "
                   "Then R = 2f. A neat way to find R experimentally.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Which Converges?", "Which spherical mirror converges a "
             "parallel beam of light to a real focus?",
             ["Convex mirror", "Concave mirror", "Plane mirror",
              "Neither"])
    b.quiz_a(1, "B. Concave mirror",
             "A concave mirror curves inward and brings parallel rays together "
             "at a real focus in front of it — a converging mirror. A convex "
             "mirror spreads them out.")
    b.quiz_q(2, "Focal Length", "A concave mirror has a radius of curvature of "
             "40 cm. Its focal length is:", ["80 cm", "40 cm", "20 cm",
              "10 cm"])
    b.quiz_a(2, "C. 20 cm",
             "f = R/2 = 40/2 = 20 cm. The focus lies halfway between the pole "
             "and the centre of curvature.")
    b.quiz_q(3, "Centre Ray", "A ray of light passing through the centre of "
             "curvature of a concave mirror, after reflection:",
             ["Passes through the focus", "Returns along the same path",
              "Goes parallel to the axis", "Is not reflected"])
    b.quiz_a(3, "B. Returns along the same path",
             "A ray through C strikes the mirror along the normal (i = 0°), so "
             "it reflects straight back on itself.")
    b.quiz_q(4, "Convex Focus", "The principal focus of a convex mirror is:",
             ["Real, in front of the mirror", "Virtual, behind the mirror",
              "At the pole", "At infinity"])
    b.quiz_a(4, "B. Virtual, behind the mirror",
             "A convex mirror diverges parallel rays; they only appear to come "
             "from a point behind the mirror, so its focus is virtual.")
    b.quiz_q(5, "Same-Size Image", "An object placed at the centre of curvature "
             "of a concave mirror gives an image that is the same size as the "
             "object. The image is at:", ["The focus F", "The pole P",
              "The centre of curvature C", "Infinity"])
    b.quiz_a(5, "C. The centre of curvature C",
             "With the object at C, the rays return to C, forming a real, "
             "inverted image of the same size right at the centre of "
             "curvature.")
    b.divider(2, "Part 2", "Images and Uses",
              "What curved mirrors do, and where we use them")
    b.text_image("CONCAVE IMAGES", "Images in a Concave Mirror",
                 ["The image depends on where the object is placed.",
                  "Object beyond C: real, inverted and diminished.",
                  "Object between F and C: real, inverted and magnified.",
                  "Object between F and the pole: virtual, erect and "
                  "magnified."],
                 cc, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Depends on object position",
                 caption="Object beyond C → real, inverted, diminished",
                 notes="Concave mirror images change with object position — "
                       "real & inverted for far objects, virtual & magnified "
                       "when close (within F).")
    b.cards("CONCAVE TABLE", "Concave Mirror: All Object Positions", [
        ("At infinity / beyond C", "Image at F or between F and C — real, "
         "inverted, diminished (used in a reflecting telescope)."),
        ("At C", "Image at C — real, inverted, the same size as the object."),
        ("Between C and F", "Image beyond C — real, inverted, magnified (a "
         "projector)."),
        ("At F / within F", "At F the image is at infinity; within F it is "
         "virtual, erect and magnified (a shaving mirror)."),
    ], notes="The full set of concave-mirror cases. Note the cross-over: within "
             "F the image becomes virtual, erect and magnified.")
    b.text_image("CONVEX IMAGES", "Images in a Convex Mirror",
                 ["A convex mirror always forms the same kind of image.",
                  "The image is virtual, erect and diminished.",
                  "It lies behind the mirror, between the pole and F.",
                  "Because the image is small, a convex mirror gives a wide "
                  "field of view."],
                 cx, img_side="right", img_w=5.8, img_h=3.4,
                 panel_title="Always virtual, erect, diminished",
                 caption="A wide field of view in a small mirror",
                 notes="Convex mirror: always virtual, erect, diminished, with "
                       "a wide view — why it is used for rear-view and "
                       "security mirrors.")
    b.cards("USES", "Uses of Curved Mirrors", [
        ("Concave — shaving/make-up", "Held close, it gives a magnified, erect "
         "image of the face."),
        ("Concave — reflectors", "In torches, headlights and search-lights to "
         "throw a parallel beam."),
        ("Convex — rear-view", "In vehicles for a wide field of view behind."),
        ("Convex — security", "In shops and at blind corners to watch a large "
         "area."),
    ], notes="Match mirror to use: concave magnifies/focuses; convex gives a "
             "wide view. The dentist's mirror and solar concentrator are also "
             "concave.")
    b.cards("DISTINCTION", "Plane vs Concave vs Convex", [
        ("Plane", "Image always virtual, erect, same size."),
        ("Concave", "Image real or virtual, depending on object position; can "
         "magnify."),
        ("Convex", "Image always virtual, erect, diminished; wide view."),
        ("Quick test", "Look in it: concave can magnify, convex always makes "
         "things smaller."),
    ], notes="Side-by-side comparison of the three mirror types — a common "
             "summary question.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Spherical mirrors", "concave converges, convex diverges"),
        ("Terms", "pole, centre of curvature, focus, focal length"),
        ("f = R/2", "focus is halfway to the centre of curvature"),
        ("Ray rules", "parallel→F, through F→parallel, through C→back"),
        ("Images", "concave varies with position; convex always virtual/"
         "diminished"),
        ("Uses", "concave: shaving, headlights; convex: rear-view, security"),
    ], notes="Rapid recap; f = R/2 and the concave image cases are the key "
             "exam points.")
    b.quiz_intro("Quiz 2", "Final Check — Spherical Mirrors", 5)
    b.quiz_q(1, "Rear-View Choice", "A convex mirror is used as a vehicle's "
             "rear-view mirror mainly because it:",
             ["Magnifies the traffic", "Gives an erect image and a wide field "
              "of view", "Shows a real image", "Reverses the image"])
    b.quiz_a(1, "B. Gives an erect image and a wide field of view",
             "A convex mirror always forms a small, erect (right-way-up) image "
             "and covers a wide area behind, letting the driver see much more "
             "traffic at a glance.")
    b.quiz_q(2, "Shaving Mirror", "To see an enlarged, erect image of your "
             "face, you should use a concave mirror with your face:",
             ["Beyond C", "At C", "Between the focus and the mirror",
              "At the focus"])
    b.quiz_a(2, "C. Between the focus and the mirror",
             "When the object (face) is closer than the focus of a concave "
             "mirror, the image is virtual, erect and magnified — exactly what "
             "a shaving or make-up mirror needs.")
    b.quiz_q(3, "Headlight", "A car headlight places its bulb at the focus of "
             "a concave reflector so that the reflected light:",
             ["Spreads out widely", "Comes out as a strong parallel beam",
              "Forms an image of the bulb", "Is dimmed"])
    b.quiz_a(3, "B. Comes out as a strong parallel beam",
             "Rays from a source at the focus of a concave mirror reflect "
             "parallel to the axis, producing the powerful straight beam a "
             "headlight needs.")
    b.quiz_q(4, "Object at C", "An object placed at the centre of curvature of "
             "a concave mirror forms an image that is:",
             ["Virtual and magnified", "Real, inverted and the same size, at "
              "C", "Diminished and erect", "At infinity"])
    b.quiz_a(4, "B. Real, inverted, same size, at C",
             "With the object at C, the concave mirror forms a real, inverted "
             "image of the same size, also located at C.")
    b.quiz_q(5, "Identify the Mirror", "Looking into a mirror, you always see "
             "a small, upright image of yourself, however far away you stand. "
             "The mirror is:", ["Plane", "Concave", "Convex",
              "Cannot be decided"])
    b.quiz_a(5, "C. Convex",
             "Only a convex mirror gives an image that is always erect AND "
             "diminished for every object distance. A plane mirror keeps the "
             "same size; a concave one can magnify or invert.")
    b.closing("Curved Mirrors, Curved Light",
              "Concave mirrors gather light to a focus; convex mirrors spread "
              "the view — geometry doing useful work.")
    return b


def build():
    for fname, fn in [("G9_S87_Reflection_of_Light_1.pptx", deck1),
                      ("G9_S88_Reflection_of_Light_2.pptx", deck2)]:
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
