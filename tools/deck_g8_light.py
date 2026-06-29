"""
Grade 8 Physics — Chapter: Light Energy.
S43 (refraction, laws, effects, glass block, prism, dispersion) and
S44 (cause of dispersion, spherical mirrors, ray diagrams, images, uses).
ICSE Class 8 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade08"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Light Energy  •  ICSE Class 8 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    bend = b.asset("g8li_bend", D.refraction_bending("g8li_bend", True))
    block = b.asset("g8li_block", D.glass_block("g8li_block"))
    disp = b.asset("g8li_disp", D.dispersion_spectrum("g8li_disp"))
    hero = b.asset("g8_light_hero", bend)

    b.title("ICSE • Class 8 • Light", "Refraction of Light",
            "Speed of light  •  Refraction & its laws  •  The glass block  •  "
            "Dispersion", img=hero)
    b.objectives([
        "Compare the speed of light in different media",
        "Define refraction and the terms used",
        "State the laws of refraction",
        "Explain everyday effects of refraction",
        "Trace light through a glass block and a prism",
        "Describe the dispersion of white light",
    ])
    b.divider(1, "Part 1", "Refraction of Light",
              "Why light bends when it changes medium")
    b.cards("SPEED OF LIGHT", "Speed of Light in Different Media", [
        ("Fastest in vacuum/air", "Light travels at 3 × 10⁸ m/s in a vacuum."),
        ("Slower in water", "Light slows down on entering water."),
        ("Slower still in glass", "Denser media slow light down more."),
        ("Why it matters", "This change of speed is what causes refraction."),
    ], notes="Light is fastest in vacuum, slower in denser media. The change "
             "of speed is the cause of bending.")
    b.text_image("REFRACTION", "What Is Refraction?",
                 ["Refraction is the bending of light as it passes from one "
                  "medium into another.",
                  "It happens because light changes speed at the boundary.",
                  "Going into a denser medium (air → glass), light bends "
                  "toward the normal.",
                  "Going into a rarer medium (glass → air), it bends away from "
                  "the normal."],
                 bend, img_side="right", img_w=5.4, img_h=3.8,
                 panel_title="Bending at the boundary",
                 caption="Air → glass: bends toward the normal",
                 notes="Define refraction and the toward/away rule. Bending "
                       "only happens at the surface.")
    b.bullets("TERMS & LAWS", "Terms and Laws of Refraction", [
        ("Incident & refracted ray", "the ray arriving at, and the ray "
         "leaving, the surface."),
        ("Angle of incidence (i) & refraction (r)", "measured from the "
         "normal."),
        ("Law 1", "the incident ray, refracted ray and normal lie in one "
         "plane."),
        ("Law 2 (Snell's law)", "sin i / sin r is a constant for two given "
         "media."),
    ], panel_title="The rules of bending",
       notes="Introduce the terms and the two laws. Angles always from the "
             "normal.")
    b.cards("EFFECTS", "Everyday Effects of Refraction", [
        ("Bent pencil", "A pencil in water looks bent at the surface."),
        ("Shallow pool", "Water looks shallower than it really is."),
        ("Early sunrise", "We see the Sun a little before it rises, as light "
         "bends through the air."),
        ("Mirage", "Hot air over a road bends light, showing a watery "
         "shimmer."),
    ], notes="Everyday refraction effects. The bent pencil and mirage are "
             "memorable examples.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Why Bend?", "Light bends when it passes from air into water "
             "because it:", ["Changes colour", "Changes speed at the "
              "boundary", "Gets brighter", "Stops momentarily"])
    b.quiz_a(1, "B. Changes speed at the boundary",
             "Refraction happens because light travels at different speeds in "
             "different media. The change of speed at the surface makes the "
             "ray bend.")
    b.quiz_q(2, "Which Way?", "A ray of light passing from air into glass "
             "bends:", ["Away from the normal", "Toward the normal",
              "Along the surface", "Straight back"])
    b.quiz_a(2, "B. Toward the normal",
             "Glass is denser than air, so light slows down on entering it and "
             "bends toward the normal — the angle of refraction is smaller "
             "than the angle of incidence.")
    b.quiz_q(3, "Bent Pencil", "A pencil dipped in a glass of water looks bent "
             "at the water surface because of:", ["Reflection", "Refraction",
              "Dispersion", "Shadow formation"])
    b.quiz_a(3, "B. Refraction",
             "Light from the underwater part of the pencil bends as it leaves "
             "the water, so the pencil appears broken or bent at the surface "
             "— an effect of refraction.")
    b.quiz_q(4, "Measured From", "The angle of incidence and the angle of "
             "refraction are both measured from the:", ["Surface", "Normal",
              "Refracted ray", "Horizontal"])
    b.quiz_a(4, "B. Normal",
             "Both angles are measured between the ray and the normal (the "
             "line at 90° to the surface) — never from the surface itself.")
    b.quiz_q(5, "Shallow Pool", "A swimming pool always looks shallower than "
             "it really is because of:", ["Reflection", "Refraction of light "
              "from the bottom", "Dispersion", "The colour of the water"])
    b.quiz_a(5, "B. Refraction of light from the bottom",
             "Light from the pool floor bends away from the normal as it "
             "leaves the water, so our eyes trace it back to a raised "
             "position. The bottom looks nearer the surface — the pool seems "
             "shallower.")
    b.divider(2, "Part 2", "Glass Block, Prism & Dispersion",
              "Light through glass, and the colours within")
    b.text_image("GLASS BLOCK", "Light Through a Glass Block",
                 ["Light refracts twice — entering and leaving the block.",
                  "It bends toward the normal on entering and away on "
                  "leaving.",
                  "The two faces are parallel, so the emergent ray is parallel "
                  "to the incident ray.",
                  "The ray is simply shifted sideways (lateral "
                  "displacement)."],
                 block, img_side="left", img_w=5.6, img_h=3.8,
                 panel_title="Emergent ray is parallel",
                 caption="Parallel emergent ray, shifted sideways",
                 notes="Through a glass block: parallel emergent ray, only "
                       "shifted sideways. Contrast with the prism next.")
    b.text_image("DISPERSION", "Dispersion of White Light",
                 ["A prism splits white light into seven colours.",
                  "Each colour bends by a slightly different amount.",
                  "Violet bends most and red bends least.",
                  "The band of colours produced is called the spectrum "
                  "(VIBGYOR)."],
                 disp, img_side="right", img_w=5.8, img_h=3.8,
                 panel_title="White light → a spectrum",
                 caption="Violet bends most, red least",
                 notes="Dispersion: white light splits into VIBGYOR because "
                       "each colour refracts differently. A rainbow is natural "
                       "dispersion.")
    b.cards("DISPERSION FACTS", "Understanding Dispersion", [
        ("Why it splits", "White light is a mixture of seven colours that bend "
         "by different amounts."),
        ("Order", "Violet, Indigo, Blue, Green, Yellow, Orange, Red "
         "(VIBGYOR)."),
        ("Rainbow", "Raindrops act as tiny prisms to make a rainbow."),
        ("Recombine", "A second prism can recombine the colours into white "
         "light."),
    ], notes="Dispersion facts: cause, VIBGYOR order, the rainbow, and "
             "recombination proving white is a mixture.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Speed of light", "fastest in vacuum; slower in denser media"),
        ("Refraction", "bending when light changes speed between media"),
        ("Toward/away", "toward the normal into denser; away into rarer"),
        ("Laws", "rays & normal in one plane; sin i / sin r constant"),
        ("Glass block", "emergent ray parallel, shifted sideways"),
        ("Dispersion", "prism splits white light into VIBGYOR"),
    ], notes="Rapid recap; the toward/away rule and dispersion are the key "
             "ideas.")
    b.quiz_intro("Quiz 2", "Final Check — Glass Block & Dispersion", 5)
    b.quiz_q(1, "Emergent Ray", "After passing through a parallel-sided glass "
             "block, the emergent ray is:", ["Bent toward the normal",
              "Parallel to the incident ray but shifted sideways",
              "Turned back", "Split into colours"])
    b.quiz_a(1, "B. Parallel to the incident ray but shifted",
             "Because the block's faces are parallel, the bending on entering "
             "is undone on leaving. The emergent ray comes out parallel to the "
             "incident ray, only displaced sideways.")
    b.quiz_q(2, "Most Bent Colour", "When white light passes through a prism, "
             "the colour that bends the most is:", ["Red", "Green", "Yellow",
              "Violet"])
    b.quiz_a(2, "D. Violet",
             "Violet light is slowed and bent the most by the prism, so it "
             "emerges nearest the base. Red bends the least.")
    b.quiz_q(3, "Rainbow", "A rainbow in the sky is formed when sunlight is "
             "dispersed by:", ["Clouds", "Raindrops acting as tiny prisms",
              "The Moon", "Dust only"])
    b.quiz_a(3, "B. Raindrops acting as tiny prisms",
             "Each raindrop refracts and disperses sunlight into its colours "
             "and reflects them back, so millions of drops together produce "
             "the arc of a rainbow.")
    b.quiz_q(4, "White Again", "Passing the spectrum from one prism through a "
             "second, inverted prism produces:", ["More colours",
              "White light again", "Only red", "Darkness"])
    b.quiz_a(4, "B. White light again",
             "The second prism recombines the seven colours back into white "
             "light, proving that white light was a mixture of those colours "
             "all along.")
    b.quiz_q(5, "Block vs Prism", "Unlike a glass block, a prism makes the "
             "emergent light:", ["Parallel to the incident ray",
              "Change direction (deviate) and spread into colours",
              "Disappear", "Travel faster"])
    b.quiz_a(5, "B. Deviate and spread into colours",
             "A prism's faces are inclined, not parallel, so the light is bent "
             "into a new direction and, being white, is also dispersed into a "
             "spectrum.")
    b.closing("Bending and Splitting Light",
              "Refraction bends light and reveals the rainbow of colours "
              "hidden inside ordinary white light.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    cc = b.asset("g8li_concave", D.concave_mirror_image("g8li_concave"))
    cx = b.asset("g8li_convex", D.convex_mirror_image("g8li_convex"))
    hero = b.asset("g8_mirror8_hero", cc)

    b.title("ICSE • Class 8 • Light", "Spherical Mirrors",
            "Concave & convex mirrors  •  Focus & focal length  •  Ray "
            "diagrams  •  Images & uses", img=hero)
    b.objectives([
        "Identify concave and convex spherical mirrors",
        "Define the terms used for spherical mirrors",
        "State the rules for making ray diagrams",
        "Distinguish real from virtual images",
        "Describe images formed by a concave mirror",
        "State the uses of a concave mirror",
    ])
    b.divider(1, "Part 1", "Reflection & Spherical Mirrors",
              "Bouncing light, and curved reflecting surfaces")
    b.cards("LAWS OF REFLECTION", "Reflection of Light", [
        ("Reflection", "The bouncing back of light when it strikes a polished "
         "surface like a mirror."),
        ("First law", "The angle of incidence equals the angle of reflection "
         "(i = r)."),
        ("Second law", "The incident ray, reflected ray and the normal all lie "
         "in one plane."),
        ("Regular vs irregular", "Smooth surfaces reflect regularly (clear "
         "image); rough ones scatter light (diffuse)."),
    ], notes="Recap the laws of reflection (i = r) and regular vs irregular "
             "reflection before moving to curved mirrors.")
    b.cards("PLANE MIRROR", "Image in a Plane Mirror", [
        ("Virtual & erect", "The image cannot be caught on a screen and is the "
         "right way up."),
        ("Same size", "It is exactly as large as the object."),
        ("As far behind", "The image is as far behind the mirror as the object "
         "is in front."),
        ("Laterally inverted", "Left and right are swapped — as in the word "
         "AMBULANCE on vehicles."),
    ], notes="Plane-mirror image: virtual, erect, same size, as far behind, and "
             "laterally inverted. The AMBULANCE example sticks.")
    b.cards("TWO KINDS", "Kinds of Spherical Mirror", [
        ("Spherical mirror", "A mirror that is part of a hollow sphere."),
        ("Concave", "Curves inward; it converges light (a converging "
         "mirror)."),
        ("Convex", "Bulges outward; it diverges light (a diverging mirror)."),
        ("Everyday", "Shaving mirrors are concave; vehicle mirrors are "
         "convex."),
    ], notes="Concave caves in and converges; convex bulges and diverges. "
             "Anchor with real mirrors.")
    b.bullets("TERMS", "Terms for a Spherical Mirror", [
        ("Pole (P)", "the centre of the mirror's surface."),
        ("Centre of curvature (C)", "the centre of the sphere the mirror is "
         "part of."),
        ("Principal focus (F)", "where rays parallel to the axis meet (or "
         "appear to)."),
        ("Focal length (f)", "the distance from the pole to the focus; "
         "f = R/2."),
    ], panel_title="Pole, centre, focus, focal length",
       notes="Define the terms and f = R/2. These feed the ray diagrams.")
    b.cards("RAY RULES", "Rules for Making Ray Diagrams", [
        ("Parallel ray", "reflects through the focus F."),
        ("Focal ray", "a ray through F reflects parallel to the axis."),
        ("Central-of-curvature ray", "a ray through C returns along "
         "itself."),
        ("Two rays", "any two of these locate the image."),
    ], notes="The standard rays for mirror ray diagrams. Two rays fix the "
             "image.")
    b.cards("REAL vs VIRTUAL", "Real and Virtual Images", [
        ("Real image", "Formed where reflected rays actually meet; can be "
         "caught on a screen; inverted."),
        ("Virtual image", "Formed where rays appear to meet; cannot be caught "
         "on a screen; erect."),
        ("Concave", "Can form real images, or a virtual one when the object is "
         "close."),
        ("Convex", "Always forms a virtual, erect, diminished image."),
    ], notes="Real (on a screen, inverted) vs virtual (behind the mirror, "
             "erect). The screen test is the clearest distinction.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Which Converges?", "A mirror that converges a parallel beam "
             "of light to a focus is:", ["A convex mirror", "A concave "
              "mirror", "A plane mirror", "Any mirror"])
    b.quiz_a(1, "B. A concave mirror",
             "A concave mirror curves inward and brings parallel rays together "
             "at a real focus in front of it. A convex mirror spreads them "
             "out.")
    b.quiz_q(2, "Focal Length", "A concave mirror has a radius of curvature of "
             "30 cm. Its focal length is:", ["60 cm", "30 cm", "15 cm",
              "10 cm"])
    b.quiz_a(2, "C. 15 cm",
             "f = R/2 = 30/2 = 15 cm. The focus lies halfway between the pole "
             "and the centre of curvature.")
    b.quiz_q(3, "On a Screen", "An image that can be caught on a screen is "
             "always:", ["Virtual and erect", "Real and inverted",
              "Diminished only", "Behind the mirror"])
    b.quiz_a(3, "B. Real and inverted",
             "Only a real image is formed by rays that actually meet, so it "
             "can fall on a screen — and real images from a single mirror are "
             "inverted.")
    b.quiz_q(4, "Centre Ray", "A ray passing through the centre of curvature "
             "of a concave mirror, after reflection:", ["Goes parallel to the "
              "axis", "Returns along the same path", "Passes through the "
              "focus", "Is not reflected"])
    b.quiz_a(4, "B. Returns along the same path",
             "A ray through C hits the mirror along the normal, so it reflects "
             "straight back on itself.")
    b.quiz_q(5, "Parallel Ray", "A ray of light travelling parallel to the "
             "principal axis of a concave mirror, after reflection, passes "
             "through the:", ["Pole", "Centre of curvature", "Focus",
              "Edge of the mirror"])
    b.quiz_a(5, "C. Focus",
             "By the first ray rule, a ray parallel to the principal axis "
             "reflects off a concave mirror and passes through its principal "
             "focus F.")
    b.divider(2, "Part 2", "Concave-Mirror Images & Uses",
              "What a concave mirror does, and where we use it")
    b.text_image("CONCAVE IMAGES", "Images in a Concave Mirror",
                 ["The image depends on where the object is placed.",
                  "Object far away (beyond C): real, inverted and "
                  "diminished.",
                  "Object between F and C: real, inverted and magnified.",
                  "Object closer than F: virtual, erect and magnified."],
                 cc, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Depends on object position",
                 caption="Object beyond C → real, inverted, diminished",
                 notes="Concave mirror images change with object position. "
                       "Within F gives the magnified, erect (shaving-mirror) "
                       "image.")
    b.text_image("CONVEX IMAGES", "Images in a Convex Mirror",
                 ["A convex mirror always forms the same kind of image.",
                  "The image is virtual, erect and diminished.",
                  "It lies behind the mirror.",
                  "Being small, it gives a wide field of view."],
                 cx, img_side="right", img_w=5.8, img_h=3.4,
                 panel_title="Always virtual, erect, diminished",
                 caption="A wide field of view",
                 notes="Convex mirror: always virtual, erect, diminished, wide "
                       "view — used for rear-view and security mirrors.")
    b.cards("USES", "Uses of Concave (and Convex) Mirrors", [
        ("Shaving mirror", "A concave mirror gives a magnified, erect image of "
         "the face."),
        ("Torch & headlight", "A concave reflector throws a strong parallel "
         "beam."),
        ("Dentist's mirror", "A concave mirror magnifies the teeth."),
        ("Convex — rear-view", "Gives a wide, erect view of traffic behind."),
    ], notes="Match mirror to use: concave magnifies/focuses; convex gives a "
             "wide view.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Spherical mirrors", "concave converges; convex diverges"),
        ("Terms", "pole, centre of curvature, focus, focal length (f = R/2)"),
        ("Ray rules", "parallel→F, through F→parallel, through C→back"),
        ("Real vs virtual", "on a screen & inverted vs behind & erect"),
        ("Concave images", "vary with position; magnified & erect within F"),
        ("Uses", "shaving, headlights, dentist; convex for rear-view"),
    ], notes="Rapid recap; f = R/2 and the concave image cases are the key "
             "points.")
    b.quiz_intro("Quiz 2", "Final Check — Mirror Images", 5)
    b.quiz_q(1, "Shaving Mirror", "To get a magnified, erect image of your "
             "face, you use a concave mirror with your face:", ["Beyond C",
              "At C", "Closer than the focus", "At the focus"])
    b.quiz_a(1, "C. Closer than the focus",
             "When the object is nearer than the focal length of a concave "
             "mirror, the image is virtual, erect and magnified — just what a "
             "shaving or make-up mirror needs.")
    b.quiz_q(2, "Wide View", "A convex mirror is used as a rear-view mirror "
             "because it gives an image that is:", ["Magnified and inverted",
              "Erect with a wide field of view", "Real and large",
              "Upside down"])
    b.quiz_a(2, "B. Erect with a wide field of view",
             "A convex mirror always gives a small, erect image and covers a "
             "wide area, letting the driver see much more of the road behind "
             "at a glance.")
    b.quiz_q(3, "Torch Beam", "A torch produces a parallel beam by placing its "
             "bulb at the concave reflector's:", ["Pole", "Focus",
              "Centre of curvature", "Edge"])
    b.quiz_a(3, "B. Focus",
             "A source at the focus of a concave mirror reflects its rays "
             "parallel to the axis, giving the strong straight beam a torch "
             "needs.")
    b.quiz_q(4, "Always Smaller", "A mirror that always gives an erect, "
             "diminished image whatever the object distance is:", ["Plane",
              "Concave", "Convex", "None"])
    b.quiz_a(4, "C. Convex",
             "Only a convex mirror forms an image that is always erect AND "
             "smaller for every object position. A plane mirror keeps the same "
             "size; a concave mirror can magnify or invert.")
    b.quiz_q(5, "Object at C", "An object at the centre of curvature of a "
             "concave mirror gives an image that is:", ["Virtual and erect",
              "Real, inverted and the same size", "Diminished and erect",
              "At infinity"])
    b.quiz_a(5, "B. Real, inverted and the same size",
             "With the object at C, a concave mirror forms a real, inverted "
             "image of the same size, also located at C.")
    b.closing("Mirrors That Shape Light",
              "Concave mirrors gather light to a point; convex mirrors widen "
              "the view — curved glass put to clever use.")
    return b


def build():
    for fname, fn in [("G8_S43_Light_Energy_1.pptx", deck1),
                      ("G8_S44_Light_Energy_2.pptx", deck2)]:
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
