"""
ICSE Class 9 Physics — Chapter 4 "Pressure in Fluids and Atmospheric
Pressure", PART A: Pressure in Fluids and its Transmission.

Two teaching decks, faithful to the supplied textbook chapter and covering
every section:

  Deck 1  (Sections 4.1 – 4.4)
      Thrust & pressure, units of pressure, factors affecting pressure,
      increasing/decreasing pressure, pressure in fluids, the demonstration
      of liquid pressure, P = hρg (with proof and factors), total pressure,
      and the five laws of liquid pressure.

  Deck 2  (Sections 4.5 – 4.8 + solved numericals)
      Consequences of P = hρg, transmission of pressure & Pascal's law,
      application of Pascal's law (hydraulic machine as a force multiplier),
      the hydraulic press, jack and brakes, MA/VR, and all six solved
      numerical examples from the chapter.

Figures: every textbook figure is recreated (Fig 4.1 – 4.9). The images are
loaded from build/qwen/<name>.png when present (Qwen-Image output produced by
tools/qwen_images.py) and otherwise fall back to the offline vector figures in
diagrams_pressure.py — so AI images can be swapped in later without touching
this file.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams_pressure as P

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
QWEN = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "build",
                                    "qwen"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Pressure in Fluids  •  ICSE Class 9 Physics  •  Chapter 4"


def fig(b, name):
    """Prefer a Qwen-Image PNG (build/qwen/<name>.png); else the vector figure."""
    qpath = os.path.join(QWEN, f"{name}.png")
    if os.path.exists(qpath):
        return b.asset(f"pr_{name}", qpath)
    return b.asset(f"pr_{name}", getattr(P, name)(f"pr_{name}"))


# ===========================================================================
# DECK 1 — Thrust, Pressure and Pressure in Liquids  (4.1 – 4.4)
# ===========================================================================
def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    f41 = fig(b, "fig_4_1")
    f42 = fig(b, "fig_4_2")
    f43 = fig(b, "fig_4_3")
    hero = fig(b, "hero1") if os.path.exists(
        os.path.join(QWEN, "hero1.png")) else f42

    b.title("ICSE • Class 9 • Chapter 4", "Pressure in Fluids",
            "Thrust & pressure  •  Units  •  Pressure in a liquid (P = hρg)  •  "
            "Laws of liquid pressure", img=hero)
    b.objectives([
        "Define thrust and pressure and state their units",
        "Explain how area and thrust decide the pressure",
        "Give everyday ways of increasing and decreasing pressure",
        "Show that a fluid exerts pressure in all directions",
        "Derive and use the relation P = h ρ g",
        "State the five laws of liquid pressure",
    ])

    # ---- 4.1 Thrust and Pressure -----------------------------------------
    b.divider(1, "Section 4.1", "Thrust and Pressure",
              "Force on a surface, and how it is shared over the area")
    b.statement("THRUST", "Thrust",
                "Thrust is the force acting normally (perpendicular) on a "
                "surface.",
                formula="Thrust exerted by a body  =  weight of the body",
                points=["Thrust is a force, so it is a vector quantity.",
                        "SI unit: newton (N).  CGS unit: dyne (1 N = 10⁵ dyne).",
                        "Gravitational units: kgf and gf, where "
                        "1 kgf = 9.8 N and 1 gf = 980 dyne."],
                notes="Thrust is just the normal force on a surface; for a body "
                      "resting on a surface it equals the body's weight, "
                      "whatever face it rests on.")
    b.statement("PRESSURE", "Pressure",
                "Pressure is the thrust acting on unit area of the surface.",
                formula="Pressure  P  =  Thrust / Area  =  F / A",
                points=["Pressure is a scalar quantity.",
                        "Same thrust on a smaller area gives a greater "
                        "pressure — a foot sinks into sand but a lying body "
                        "does not.",
                        "For a given thrust, pressure is less on a large area "
                        "and more on a small area."],
                notes="Distinguish thrust (total force) from pressure (force "
                      "per unit area). The loose-sand example makes area "
                      "intuitive.")
    b.bullets("UNITS OF PRESSURE", "Units of Pressure", [
        ("SI unit — pascal (Pa)", "1 pascal = 1 newton per square metre "
         "(N m⁻²); the pressure of 1 N acting normally on 1 m²."),
        ("Other SI form", "kgf m⁻² when thrust is in kgf."),
        ("CGS unit", "dyne cm⁻² (or gf cm⁻²);  1 N m⁻² = 10 dyne cm⁻²."),
        ("Bar and millibar", "1 bar = 10⁵ N m⁻²,  1 millibar = 10² N m⁻²."),
        ("Atmosphere & torr", "1 atm = 0.76 m of Hg = 1.013 × 10⁵ Pa;  "
         "1 torr = 1 mm of Hg, and 1 atm = 760 torr."),
    ], panel_title="Named after Blaise Pascal",
       notes="Walk through the family of pressure units. The pascal is the SI "
             "unit; bar/millibar appear on weather maps; atmosphere and torr "
             "measure air pressure.")
    b.text_image("FACTORS", "Factors Affecting Pressure",
                 ["The pressure on a surface depends on two things: the "
                  "thrust, and the area it acts on.",
                  "Larger the area for a given thrust, smaller the pressure "
                  "(brick lying flat).",
                  "Larger the thrust on a given area, greater the pressure "
                  "(stacking a second brick doubles it).",
                  "The same brick therefore gives different pressures in "
                  "different positions."],
                 f41, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="P = F / A",
                 caption="Fig 4.1 — same brick, two positions",
                 notes="Use the brick figure: weight (thrust) is the same in "
                       "every position, but the contact area changes, so the "
                       "pressure changes.")
    b.cards("USING AREA", "Changing Pressure by Changing Area", [
        ("Increase pressure: sharp point", "Nails, pins and needles are "
         "pointed — a tiny area gives large pressure, so they pierce easily."),
        ("Increase pressure: sharp edge", "Knives and cutting tools are given "
         "sharp edges so a small thrust makes a large pressure and cuts."),
        ("Decrease pressure: wide base", "Railway sleepers are broad so the "
         "rails press on the ground with less pressure."),
        ("Decrease pressure: foundations", "Building foundations are made "
         "wider than the walls to lower the pressure on the soil."),
    ], notes="Two mirror-image ideas: reduce area to raise pressure (sharp "
             "tools); increase area to lower it (sleepers, foundations, camel "
             "feet, snow shoes).")

    # ---- 4.2 Pressure in Fluids ------------------------------------------
    b.divider(2, "Section 4.2", "Pressure in Fluids",
              "Why liquids and gases press on everything they touch")
    b.statement("FLUIDS", "Fluids Exert Pressure in All Directions",
                "A fluid contained in a vessel exerts pressure at all points "
                "and in all directions.",
                formula="A substance that can flow (a liquid or a gas) is a "
                        "fluid",
                points=["A solid presses only on the surface it rests on; a "
                        "fluid presses on the base and on the walls too.",
                        "A fluid exerts pressure because of its own weight.",
                        "Because it tends to flow, this pressure acts in every "
                        "direction, not just downward."],
                notes="Fluids (liquids and gases) flow, so their weight presses "
                      "outward in all directions — on the base and the sides "
                      "of the container alike.")
    b.text_image("DEMONSTRATION", "Liquid Pressure Increases with Depth",
                 ["Make several small holes down the side of a water-filled "
                  "vessel.",
                  "Water spurts out of every hole — the liquid presses at "
                  "each point on the wall.",
                  "A finger on a hole feels a thrust — the liquid exerts "
                  "thrust at all points.",
                  "The lower the hole, the farther the water reaches — "
                  "pressure grows with depth."],
                 f42, img_side="right", img_w=5.0, img_h=3.8,
                 panel_title="Deeper → greater pressure",
                 caption="Fig 4.2 — the lowest jet travels farthest",
                 notes="Classic leaking-can demonstration: jets from lower "
                       "holes travel farther, proving pressure increases with "
                       "depth below the free surface.")

    # ---- 4.3 Pressure exerted by a liquid column -------------------------
    b.divider(3, "Section 4.3", "Pressure of a Liquid Column",
              "The formula P = h ρ g and where it comes from")
    b.text_image("P = hρg", "Pressure at a Depth in a Liquid",
                 ["The pressure at depth h in a liquid of density ρ is "
                  "P = h ρ g.",
                  "In words: pressure = depth × density × acceleration due to "
                  "gravity.",
                  "So pressure rises with depth and with the density of the "
                  "liquid.",
                  "It does NOT depend on the area of the surface or the shape "
                  "of the vessel."],
                 f43, img_side="left", img_w=5.4, img_h=3.9,
                 panel_title="P = h ρ g",
                 caption="Fig 4.3 — column PQRS of area A at depth h",
                 notes="Introduce P = hρg and stress the three factors (h, ρ, "
                       "g). Independence from area/shape is a favourite exam "
                       "point.")
    b.worked("PROOF", "Deriving P = h ρ g",
             "Find the pressure on a horizontal surface PQ of area A at a "
             "depth h below the free surface of a liquid of density ρ.",
             ["Thrust on PQ = weight of the liquid column PQRS above it",
              "= volume × density × g = (A × h) × ρ × g",
              "Pressure = Thrust / Area = (A h ρ g) / A",
              "P = h ρ g"],
             "P = h ρ g  — the area A cancels, so pressure is independent of A",
             notes="The column's weight divided by its base area gives hρg; "
                   "the area cancels, which is why pressure depends only on "
                   "depth, density and g.")
    b.statement("TOTAL PRESSURE", "Total Pressure at a Depth",
                "The free surface of a liquid also carries the atmosphere's "
                "pressure, which must be added to the liquid's own pressure.",
                formula="P_total  =  P₀  +  h ρ g",
                points=["h ρ g is the pressure due to the liquid column alone "
                        "(the gauge pressure).",
                        "P₀ is the atmospheric pressure pushing down on the "
                        "free surface.",
                        "Their sum is the total (absolute) pressure at that "
                        "depth."],
                notes="Separate gauge pressure (hρg) from total pressure "
                      "(P₀ + hρg). Numericals state which one is wanted.")
    b.cards("FACTORS", "What the Pressure at a Point Depends On", [
        ("Depth (h)", "Directly proportional — twice the depth, twice the "
         "liquid pressure."),
        ("Density (ρ)", "Directly proportional — a denser liquid presses "
         "harder at the same depth."),
        ("Gravity (g)", "Depends on g, which is nearly constant at a place."),
        ("NOT on shape or area", "The pressure is independent of the shape and "
         "size of the vessel and the area of the surface."),
    ], notes="Pressure at a point in a liquid depends on h, ρ and g only — "
             "never on the container's shape or the area chosen.")

    # ---- 4.4 Laws of liquid pressure -------------------------------------
    b.divider(4, "Section 4.4", "Laws of Liquid Pressure",
              "Five rules that follow from P = h ρ g")
    b.bullets("FIVE LAWS", "The Laws of Liquid Pressure", [
        ("1 — Increases with depth", "Inside a liquid, the pressure increases "
         "with depth below the free surface."),
        ("2 — Same on a level", "In a stationary liquid the pressure is the "
         "same at all points on the same horizontal plane."),
        ("3 — Same in all directions", "At a point, the pressure is the same "
         "in every direction."),
        ("4 — Depends on density", "At the same depth, a denser liquid exerts "
         "a greater pressure than a lighter one."),
        ("5 — Seeks its own level", "A liquid always settles to the same level "
         "in connected vessels, whatever their shape."),
    ], panel_title="All five follow from P = h ρ g",
       notes="The five laws. Laws 2 and 3 (same on a level / same in all "
             "directions) and law 5 (own level) are the most commonly tested.")

    # ---- Quiz 1 -----------------------------------------------------------
    b.quiz_intro("Quiz 1", "Check — Thrust, Pressure & Units", 5)
    b.quiz_q(1, "Thrust vs pressure", "A brick is placed once on its broad "
             "face and once on its narrow end. Compared with lying flat, "
             "standing on its end gives:",
             ["The same pressure and the same thrust",
              "A greater pressure but the same thrust",
              "A smaller pressure but a greater thrust",
              "A greater thrust and a greater pressure"])
    b.quiz_a(1, "B. Greater pressure, same thrust",
             "The weight (thrust) is unchanged, but the end face has a smaller "
             "area. Since P = F/A, the smaller area gives a greater pressure.")
    b.quiz_q(2, "Unit check", "Which of the following equals 1 N m⁻²?",
             ["1 dyne cm⁻²", "10 dyne cm⁻²", "0.1 dyne cm⁻²",
              "100 dyne cm⁻²"])
    b.quiz_a(2, "B. 10 dyne cm⁻²",
             "1 N = 10⁵ dyne and 1 m² = 10⁴ cm², so 1 N m⁻² = 10⁵/10⁴ = "
             "10 dyne cm⁻². (Equivalently 1 dyne cm⁻² = 0.1 N m⁻².)")
    b.quiz_q(3, "Sharp tools", "Cutting and piercing tools are given sharp "
             "edges or points because a small area:",
             ["Reduces the thrust needed", "Gives a large pressure for a "
              "small thrust", "Increases the total force", "Lowers the "
              "pressure at the edge"])
    b.quiz_a(3, "B. Gives a large pressure for a small thrust",
             "A sharp edge concentrates the thrust on a tiny area, so P = F/A "
             "is very large even for a modest force — enough to cut or pierce.")
    b.quiz_q(4, "One atmosphere", "Normal atmospheric pressure of 0.76 m of "
             "mercury is equal to:", ["760 torr", "1 bar exactly",
              "10² N m⁻²", "76 torr"])
    b.quiz_a(4, "A. 760 torr",
             "1 torr = 1 mm of Hg, and 0.76 m of Hg = 760 mm of Hg = 760 torr "
             "(≈ 1.013 × 10⁵ Pa). This is defined as 1 atmosphere.")
    b.quiz_q(5, "Wide foundations", "The foundations of a building are made "
             "wider than its walls in order to:",
             ["Increase the thrust on the soil",
              "Reduce the pressure on the soil so it does not sink",
              "Make the building heavier", "Increase the pressure on the soil"])
    b.quiz_a(5, "B. Reduce the pressure on the soil",
             "A wider base spreads the same weight (thrust) over a larger "
             "area, lowering the pressure so the ground can bear the building "
             "without giving way.")

    # ---- Quiz 2 -----------------------------------------------------------
    b.quiz_intro("Quiz 2", "Check — Liquid Pressure & Laws", 5)
    b.quiz_q(1, "P = hρg", "The pressure due to a liquid column depends on:",
             ["The area of the base of the column",
              "The depth, the density and g",
              "The total volume of liquid", "The shape of the vessel"])
    b.quiz_a(1, "B. The depth, the density and g",
             "P = h ρ g. Only depth, density and g matter; the area, volume "
             "and shape of the container do not affect the pressure at a "
             "point.")
    b.quiz_q(2, "Find the pressure", "The pressure due to a 4 m column of "
             "water (ρ = 1000 kg m⁻³, g = 10 m s⁻²) is:",
             ["4000 Pa", "40,000 Pa", "400 Pa", "4 × 10⁵ Pa"])
    b.quiz_a(2, "B. 40,000 Pa",
             "P = h ρ g = 4 × 1000 × 10 = 40,000 Pa (= 4 × 10⁴ N m⁻²). "
             "Multiply depth, density and g.")
    b.quiz_q(3, "Same level", "Two points inside a stationary liquid lie on "
             "the same horizontal level. The pressure at them is:",
             ["Greater at the point nearer the wall",
              "Exactly the same", "Greater at the point nearer the centre",
              "Different, depending on direction"])
    b.quiz_a(3, "B. Exactly the same",
             "By the laws of liquid pressure, all points on the same "
             "horizontal plane in a stationary liquid are at the same depth, "
             "so they are at the same pressure.")
    b.quiz_q(4, "Total pressure", "At a depth h in an open tank of liquid, the "
             "total pressure is:", ["h ρ g only", "P₀ only",
              "P₀ + h ρ g", "P₀ − h ρ g"])
    b.quiz_a(4, "C. P₀ + h ρ g",
             "The atmosphere presses P₀ on the free surface and the liquid "
             "column adds h ρ g, so the total (absolute) pressure at depth h "
             "is P₀ + h ρ g.")
    b.quiz_q(5, "Denser liquid", "At the same depth, the pressure in sea water "
             "is greater than in river water because sea water:",
             ["Is deeper", "Is denser", "Flows faster", "Is colder"])
    b.quiz_a(5, "B. Is denser",
             "Pressure at a depth is h ρ g. At the same depth h, the denser "
             "sea water (larger ρ) exerts a greater pressure than the less "
             "dense river water.")

    b.recap("WRAP UP", "Quick Recap — Part 1", [
        ("Thrust", "the normal force on a surface (= weight of the body); "
         "unit newton"),
        ("Pressure", "P = thrust / area (scalar); SI unit pascal, 1 Pa = "
         "1 N m⁻²"),
        ("Area effect", "sharp points raise pressure; wide bases lower it"),
        ("Fluids", "press in all directions; pressure grows with depth"),
        ("Liquid column", "P = h ρ g; total pressure = P₀ + h ρ g"),
        ("Five laws", "depth, level, all directions, density, own level"),
    ], notes="Recap of 4.1–4.4. P = hρg and the five laws lead into the "
             "consequences and Pascal's law in Part 2.")
    b.closing("From a Pinpoint to the Deep Sea",
              "Pressure is simply force shared over area — and in a liquid it "
              "grows steadily with depth, exactly as P = h ρ g predicts.")
    return b


# ===========================================================================
# DECK 2 — Consequences, Pascal's Law & Hydraulic Machines (4.5 – 4.8)
# ===========================================================================
def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    f44 = fig(b, "fig_4_4")
    f45 = fig(b, "fig_4_5")
    f46 = fig(b, "fig_4_6")
    f47 = fig(b, "fig_4_7")
    f48 = fig(b, "fig_4_8")
    f49 = fig(b, "fig_4_9")
    hero = fig(b, "hero2") if os.path.exists(
        os.path.join(QWEN, "hero2.png")) else f46

    b.title("ICSE • Class 9 • Chapter 4", "Pascal's Law & Hydraulics",
            "Consequences of P = hρg  •  Pascal's law  •  Hydraulic press, "
            "jack & brakes  •  Numericals", img=hero)
    b.objectives([
        "Explain everyday consequences of P = h ρ g",
        "State Pascal's law of transmission of pressure",
        "Show how a hydraulic machine multiplies force",
        "Describe the hydraulic press, jack and brakes",
        "Relate mechanical advantage and velocity ratio",
        "Solve numerical problems on fluid pressure",
    ])

    # ---- 4.5 Consequences -------------------------------------------------
    b.divider(1, "Section 4.5", "Consequences of P = h ρ g",
              "Everyday effects of pressure growing with depth")
    b.text_image("DAM WALL", "Why a Dam is Thicker at the Bottom",
                 ["Water pressure on a dam increases with depth (P = h ρ g).",
                  "The deepest part of the wall must withstand the greatest "
                  "pressure.",
                  "So the wall is built thin at the top and much thicker at "
                  "the base.",
                  "The lengthening arrows show the pressure rising toward the "
                  "bottom."],
                 f44, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="Deepest = strongest",
                 caption="Fig 4.4 — wall thickens toward the base",
                 notes="The dam is the classic consequence: pressure at the "
                       "base is largest, so the wall is thickest there.")
    b.cards("MORE CONSEQUENCES", "Other Consequences of Liquid Pressure", [
        ("Sea vs river water", "At the same depth the pressure is greater in "
         "the sea because sea water is denser than river water."),
        ("Overhead water tank", "A supply tank is placed high so the large "
         "depth gives enough pressure for water to reach the taps."),
        ("Diver's suit", "Deep-sea divers wear a strong suit kept at about one "
         "atmosphere, because the water pressure deep down is far above their "
         "blood pressure."),
        ("Rising gas bubble", "A bubble grows as it rises: less depth means "
         "less pressure, so by Boyle's law its volume increases."),
    ], notes="Each effect follows from P = hρg (or, for the bubble, from "
             "pressure falling as depth decreases). The diver's suit and the "
             "high water tank are common exam contexts.")

    # ---- 4.6 Pascal's law -------------------------------------------------
    b.divider(2, "Section 4.6", "Transmission of Pressure — Pascal's Law",
              "Passing pressure on through a confined liquid")
    b.statement("PASCAL'S LAW", "Pascal's Law",
                "The pressure exerted anywhere in a confined liquid is "
                "transmitted equally and undiminished in all directions "
                "throughout the liquid.",
                formula="Increase the pressure at one point  →  it rises "
                        "equally everywhere",
                points=["The pressure difference between two points depends "
                        "only on their difference in height (Δh).",
                        "So raising the pressure at one point raises it by the "
                        "same amount at every other point.",
                        "This works because a liquid is almost "
                        "incompressible."],
                notes="State Pascal's law precisely. It is the basis of every "
                      "hydraulic machine that follows.")
    b.text_image("DEMONSTRATION", "Demonstrating Pascal's Law",
                 ["A glass flask has several narrow tubes and a piston at its "
                  "mouth.",
                  "Filled with water, the level in each tube is the same to "
                  "begin with.",
                  "Pushing the piston in makes water jet from every tube to "
                  "the SAME height.",
                  "The applied pressure has been passed on equally to all "
                  "parts of the liquid."],
                 f45, img_side="right", img_w=4.6, img_h=3.9,
                 panel_title="Equal jets everywhere",
                 caption="Fig 4.5 — jets rise equally in all tubes",
                 notes="The equal jet heights show the applied pressure reaches "
                       "every part of the enclosed liquid equally.")

    # ---- 4.7 Application: hydraulic machine principle --------------------
    b.divider(3, "Section 4.7", "Application — The Hydraulic Machine",
              "Turning a small force into a large one")
    b.text_image("FORCE MULTIPLIER", "Principle of a Hydraulic Machine",
                 ["Two connected cylinders of areas A₁ (small) and A₂ (large) "
                  "hold a liquid.",
                  "A force F₁ on the small piston makes a pressure "
                  "P₁ = F₁ / A₁.",
                  "By Pascal's law this pressure reaches the big piston "
                  "unchanged, so P₂ = P₁.",
                  "Since P₂ = F₂ / A₂, we get F₂ / F₁ = A₂ / A₁ — a large "
                  "force on the big piston."],
                 f46, img_side="left", img_w=6.0, img_h=3.5,
                 panel_title="F₂ / F₁ = A₂ / A₁",
                 caption="Fig 4.6 — a small F₁ balances a large F₂",
                 notes="Derive the force-multiplier relation step by step: "
                       "P₁ = F₁/A₁, P₂ = P₁ (Pascal), P₂ = F₂/A₂, hence "
                       "F₂/F₁ = A₂/A₁.")
    b.worked("WORKED EXAMPLE", "How Much Force is Multiplied?",
             "In a hydraulic machine the small piston has area 0.01 m² and the "
             "large piston 0.50 m². A force of 50 N is applied to the small "
             "piston. Find the force on the large piston.",
             ["F₂ / F₁ = A₂ / A₁   →   F₂ = F₁ × A₂ / A₁",
              "F₂ = 50 × 0.50 / 0.01",
              "F₂ = 50 × 50 = 2500 N"],
             "F₂ = 2500 N — the force is multiplied 50 times",
             notes="The area ratio (0.50/0.01 = 50) is the force multiplier. "
                   "The output force is 50× the input force.")
    b.statement("NO FREE LUNCH", "Force Multiplier, Not Energy Multiplier",
                "A hydraulic machine multiplies force, but the small piston "
                "must move much farther than the load rises.",
                formula="work by effort  =  work by load   (in the ideal "
                        "case)",
                points=["Mechanical advantage MA = Load / Effort > 1.",
                        "Velocity ratio VR = distance moved by effort / "
                        "distance moved by load > 1.",
                        "Energy is conserved: extra force is paid for with "
                        "extra distance."],
                notes="Stress that hydraulics trade distance for force — the "
                      "effort moves a long way to raise the load a little; "
                      "work in equals work out.")

    # ---- 4.8 Examples of hydraulic machines ------------------------------
    b.divider(4, "Section 4.8", "Hydraulic Machines in Use",
              "The press, the jack and the brakes")
    b.text_image("HYDRAULIC PRESS", "The Hydraulic (Bramah) Press",
                 ["A small pump plunger A in a narrow cylinder P is worked by "
                  "a lever.",
                  "It drives liquid through a pipe to a large ram B in a wide "
                  "cylinder Q.",
                  "The large area makes a huge upward force that presses "
                  "goods against a fixed plate.",
                  "Uses: pressing cotton bales and books, extracting juice or "
                  "oil, and engraving."],
                 f47, img_side="left", img_w=6.2, img_h=3.7,
                 panel_title="Small plunger, big ram",
                 caption="Fig 4.7 — the Bramah press",
                 notes="Construction and working of the press; the ram's large "
                       "area gives the pressing force. List the everyday uses.")
    b.text_image("HYDRAULIC JACK", "The Hydraulic Jack / Lift",
                 ["Pressing the handle raises the pressure in the narrow "
                  "cylinder P.",
                  "Liquid is forced through valve V into the wide cylinder Q.",
                  "The large piston B rises and lifts a car on its platform.",
                  "A small effort at the handle raises a very heavy load — a "
                  "force multiplier."],
                 f48, img_side="right", img_w=6.2, img_h=3.7,
                 panel_title="Lifting a car by hand",
                 caption="Fig 4.8 — the hydraulic jack",
                 notes="The jack lifts vehicles for repair; the valve lets the "
                       "load be raised step by step and holds it up.")
    b.text_image("HYDRAULIC BRAKES", "The Hydraulic Brakes",
                 ["The foot pedal pushes piston A in the master cylinder P.",
                  "Brake fluid carries the pressure equally along pipe R to "
                  "every wheel.",
                  "At each wheel, pistons B₁ and B₂ push the brake shoes "
                  "against the rim.",
                  "One light push on the pedal brakes all the wheels together."],
                 f49, img_side="left", img_w=6.2, img_h=3.6,
                 panel_title="One pedal, all wheels",
                 caption="Fig 4.9 — a hydraulic brake",
                 notes="Pascal's law shares the pedal pressure equally to all "
                       "wheels; releasing the pedal lets the spring pull the "
                       "shoes back.")

    # ---- Quiz 1 -----------------------------------------------------------
    b.quiz_intro("Quiz 1", "Check — Consequences & Pascal's Law", 5)
    b.quiz_q(1, "Dam design", "A dam wall is built much thicker at its base "
             "than at its top because water pressure:",
             ["Is greatest at the surface",
              "Increases with depth, so it is greatest at the base",
              "Is the same at every depth", "Acts only sideways at the top"])
    b.quiz_a(1, "B. Increases with depth",
             "Since P = h ρ g, the pressure is largest at the deepest point of "
             "the wall, so the base must be thickest to withstand it.")
    b.quiz_q(2, "Rising bubble", "As an air bubble rises from the bottom of a "
             "lake to the surface, its size:",
             ["Decreases", "Stays the same", "Increases",
              "First increases then decreases"])
    b.quiz_a(2, "C. Increases",
             "Higher up, the depth and hence the pressure on the bubble fall. "
             "By Boyle's law, less pressure means more volume, so the bubble "
             "grows as it rises.")
    b.quiz_q(3, "Pascal's law", "Pascal's law states that pressure applied to "
             "an enclosed liquid is:", ["Lost as it spreads out",
              "Transmitted equally and undiminished in all directions",
              "Greatest near the piston", "Halved at each point"])
    b.quiz_a(3, "B. Transmitted equally and undiminished",
             "An enclosed, almost incompressible liquid passes the applied "
             "pressure on to every point equally — the basis of all hydraulic "
             "machines.")
    b.quiz_q(4, "Force multiplier", "In a hydraulic machine the pistons have "
             "areas 2 cm² and 80 cm². A force of 30 N on the small piston can "
             "balance a load of:", ["30 N", "600 N", "1200 N", "120 N"])
    b.quiz_a(4, "C. 1200 N",
             "F₂ = F₁ × A₂/A₁ = 30 × 80/2 = 30 × 40 = 1200 N. The area ratio "
             "of 40 multiplies the force 40 times.")
    b.quiz_q(5, "Why a liquid?", "Hydraulic machines are filled with a liquid "
             "(oil) rather than a gas because a liquid:",
             ["Is lighter", "Is almost incompressible, so it transmits "
              "pressure at once", "Is cheaper", "Evaporates easily"])
    b.quiz_a(5, "B. Is almost incompressible",
             "A liquid barely compresses, so the applied pressure is passed on "
             "immediately and in full. A gas would simply be squashed, "
             "absorbing the effort instead of transmitting it.")

    # ---- Solved numericals (all six from the chapter) --------------------
    b.divider(5, "Solved Problems", "Numericals from the Chapter",
              "Working through every solved example")
    b.worked("EXAMPLE 1", "Comparing Two Pressures",
             "A boy of 60 kgf wears shoes with heel area 20 cm²; a girl of "
             "45 kgf wears sandals with heel area 1.5 cm². Compare the "
             "pressures they exert on one heel.",
             ["Boy:  P₁ = F₁ / A₁ = 60 / 20 = 3 kgf cm⁻²",
              "Girl: P₂ = F₂ / A₂ = 45 / 1.5 = 30 kgf cm⁻²",
              "Ratio P₂ : P₁ = 30 : 3"],
             "P₂ : P₁ = 10 : 1 — the girl's heel presses 10 times harder",
             notes="Despite weighing less, the girl's tiny heel area gives a "
                   "far greater pressure — the same reason stilettos dent "
                   "floors.")
    b.worked("EXAMPLE 2", "Pressure of a Water Column",
             "Calculate the pressure due to a water column of height 100 m. "
             "(g = 10 m s⁻², density of water = 10³ kg m⁻³.)",
             ["P = h ρ g",
              "P = 100 × 10³ × 10",
              "P = 10⁶ N m⁻²"],
             "P = 10⁶ N m⁻² (= 10 × 10⁵ Pa)",
             notes="Straight substitution into P = hρg with the given values.")
    b.worked("EXAMPLE 3", "Depth for Twice Atmospheric Pressure",
             "At what depth in water is the pressure equal to twice the "
             "atmospheric pressure? (P₀ = 10 N cm⁻² = 10⁵ N m⁻², "
             "ρ = 10³ kg m⁻³, g = 9.8 m s⁻².)",
             ["Total pressure at depth h = P₀ + h ρ g",
              "For twice atmospheric: 2P₀ = P₀ + h ρ g,  so  h ρ g = P₀",
              "h = P₀ / (ρ g) = 10⁵ / (10³ × 9.8)"],
             "h = 10.2 m — a 10.2 m water column adds one more atmosphere",
             notes="Set the liquid's own pressure hρg equal to P₀, so the "
                   "total becomes 2P₀. Solve for h.")
    b.worked("EXAMPLE 4", "Thrust on a Face of a Cube",
             "A cube of side 5 cm is placed in a liquid. The pressure at the "
             "centre of one face is 10 Pa. Find the thrust on that face.",
             ["Area A = 5 cm × 5 cm = 25 × 10⁻⁴ m²",
              "Thrust F = P × A = 10 × 25 × 10⁻⁴",
              "F = 250 × 10⁻⁴ N"],
             "F = 2.5 × 10⁻² N",
             notes="Convert the area to m² first, then use thrust = pressure × "
                   "area.")
    b.worked("EXAMPLE 5", "Total Thrust on a Submerged Plate",
             "A square plate of side 10 m lies horizontally 1 m below a water "
             "surface. Find the total thrust on it. (P₀ = 1.013 × 10⁵ N m⁻², "
             "ρ = 10³ kg m⁻³, g = 9.8 m s⁻².)",
             ["Total pressure = P₀ + h ρ g = 1.013 × 10⁵ + (10³ × 9.8 × 1)",
              "= 1.013 × 10⁵ + 0.098 × 10⁵ = 1.111 × 10⁵ N m⁻²",
              "Thrust = pressure × area = 1.111 × 10⁵ × (10 × 10)"],
             "Total thrust = 1.111 × 10⁷ N",
             notes="Remember to add atmospheric pressure to hρg before "
                   "multiplying by the 100 m² area.")
    b.worked("EXAMPLE 6", "Vessel of Liquid — Several Parts",
             "A vessel of base 100 cm × 60 cm and height 200 cm is full of "
             "liquid of density 1.1 × 10³ kg m⁻³ (g = 9.8 m s⁻²). Ignoring the "
             "atmosphere, find the pressure at the bottom and at a depth of "
             "5 cm.",
             ["Pressure at bottom = h ρ g = 2.00 × 1.1 × 10³ × 9.8",
              "= 2.156 × 10⁴ ≈ 2.16 × 10⁴ N m⁻²",
              "At depth 5 cm (0.05 m): P = 0.05 × 1.1 × 10³ × 9.8"],
             "Bottom ≈ 2.16 × 10⁴ N m⁻²;  at 5 cm ≈ 539 N m⁻²",
             notes="Apply P = hρg at each depth. A metal foil inside feels "
                   "equal and opposite thrusts on its two faces, so the NET "
                   "force on it is zero.")

    # ---- Quiz 2 -----------------------------------------------------------
    b.quiz_intro("Quiz 2", "Final Check — Hydraulics & Numericals", 5)
    b.quiz_q(1, "Hydraulic brakes", "When you press a car's brake pedal, all "
             "the wheels brake together because the brake fluid:",
             ["Heats up", "Transmits the pressure equally to every wheel "
              "cylinder", "Freezes at the wheels", "Evaporates in the pipe"])
    b.quiz_a(1, "B. Transmits the pressure equally",
             "The enclosed brake fluid obeys Pascal's law, carrying the "
             "pedal's pressure equally along the pipes to every wheel cylinder "
             "so all wheels brake at once.")
    b.quiz_q(2, "The jack's cost", "A hydraulic jack multiplies the effort "
             "40 times. To raise the load, the effort piston must move:",
             ["The same distance as the load rises",
              "40 times farther than the load rises",
              "40 times less than the load rises", "Not at all"])
    b.quiz_a(2, "B. 40 times farther than the load rises",
             "Work is conserved: gaining 40× the force costs 40× the distance. "
             "The effort piston travels a long way to lift the load a little.")
    b.quiz_q(3, "Numerical", "The pressure due to a 5 m column of a liquid of "
             "density 800 kg m⁻³ (g = 10 m s⁻²) is:",
             ["4000 Pa", "40,000 Pa", "400 Pa", "4 × 10⁵ Pa"])
    b.quiz_a(3, "B. 40,000 Pa",
             "P = h ρ g = 5 × 800 × 10 = 40,000 Pa (4 × 10⁴ N m⁻²).")
    b.quiz_q(4, "Foil in a liquid", "A thin metal foil is held vertically "
             "inside a liquid. The net force the liquid exerts on it is:",
             ["Large and downward", "Zero, because the two faces feel equal "
              "and opposite thrusts", "Large and upward",
              "Equal to the foil's weight"])
    b.quiz_a(4, "B. Zero — equal and opposite thrusts",
             "At a given depth the pressure is the same in all directions, so "
             "the two faces of the foil feel equal and opposite thrusts that "
             "cancel, giving zero net force.")
    b.quiz_q(5, "Press uses", "The hydraulic press is NOT normally used for:",
             ["Pressing cotton bales", "Extracting oil from seeds",
              "Lifting a car for servicing", "Engraving monograms on goods"])
    b.quiz_a(5, "C. Lifting a car for servicing",
             "Lifting vehicles is the job of the hydraulic jack/lift. The "
             "press is used for pressing bales and books, extracting oil or "
             "juice, and engraving.")

    b.recap("WRAP UP", "Quick Recap — Part 2", [
        ("Consequences", "dam walls, high tanks, diver's suit, rising bubble"),
        ("Pascal's law", "pressure in a confined liquid is transmitted "
         "equally"),
        ("Hydraulic machine", "F₂/F₁ = A₂/A₁ — a force multiplier"),
        ("Press, jack, brakes", "small effort → large useful force"),
        ("MA & VR", "both > 1; work by effort = work by load"),
        ("Numericals", "P = hρg, total = P₀ + hρg, thrust = P × A"),
    ], notes="Recap of 4.5–4.8 and the numericals. Pascal's law and "
             "F₂/F₁ = A₂/A₁ are the key results.")
    b.closing("Multiplying Force with a Fluid",
              "Pascal's law lets a gentle push move mountains of cotton, lift "
              "a car, and stop it again — the quiet power of a confined "
              "liquid.")
    return b


def build():
    for fname, fn in [("ICSE9_Pressure_PartA_1_Thrust_and_Liquid_Pressure.pptx",
                       deck1),
                      ("ICSE9_Pressure_PartA_2_Pascal_and_Hydraulics.pptx",
                       deck2)]:
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
