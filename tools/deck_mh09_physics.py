"""
Maharashtra Board (MSBSHSE) — Standard 9 Physics teaching decks.

Scope: Physics chapters/sessions from the tuitions planner after session 25 —
Current Electricity (S30, S32), Reflection of Light (S44, S46), Study of Sound
(S58, S60) and Observing Space: Telescopes (S75). One deck per concept session,
matching the house style. Content covers the full MSBSHSE Std 9 Science &
Technology textbook treatment of each chapter (subtopics verified against the
Balbharati chapter scope), written in original teaching language.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import diagrams_mh as DM
import mhstyle

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "MH_Grade09"))
os.makedirs(OUT, exist_ok=True)
mhstyle.apply()


# ===========================================================================
# S30 — Current Electricity - 1  (charge & current, circuit, PD, Ohm's law)
# ===========================================================================
def ce1_deck():
    footer = "Current Electricity  •  MSBSHSE Std 9 Science & Technology"
    b = Builder(footer, accent=C["blue"])

    circuit = b.asset("mh9_ce1_circuit", D.simple_circuit("mh9_ce1_circuit"))
    symbols = b.asset("mh9_ce1_symbols", D.circuit_symbols("mh9_ce1_symbols"))
    ohmc = b.asset("mh9_ce1_ohmc", D.ohm_circuit("mh9_ce1_ohmc"))
    ohmg = b.asset("mh9_ce1_ohmg", D.ohm_graph("mh9_ce1_ohmg"))

    b.title("Std 9 • Science & Technology • Electricity",
            "Current Electricity — 1",
            "Electric current  •  Circuits and symbols  •  Potential "
            "difference  •  Ohm's law", img=circuit)

    b.objectives([
        "Explain electric current as the rate of flow of charge and give "
        "its unit",
        "Describe conduction in solids in terms of free electrons",
        "Draw an electric circuit using standard symbols and state each "
        "component's function",
        "Define potential difference and its unit, the volt",
        "State Ohm's law and verify it experimentally",
        "Connect an ammeter and a voltmeter correctly in a circuit",
    ])

    # ---- Part 1 : current, conduction, circuit ----
    b.divider(1, "Part 1", "Electric Current and Circuits",
              "What flows, how it flows, and how we draw it")

    b.statement(
        "ELECTRIC CURRENT", "What Is Electric Current?",
        "Electric current is the rate of flow of electric charge through "
        "a conductor — the amount of charge passing through any "
        "cross-section of the conductor per unit time.",
        formula="I = Q / t",
        points=[
            "The SI unit of current is the ampere (A); 1 A = 1 coulomb "
            "per second.",
            "Charge Q is measured in coulombs (C); the charge on one "
            "electron is 1.6 x 10⁻¹⁹ C.",
            "Current is measured with an ammeter, connected in series in "
            "the circuit."],
        notes="Emphasise the definition I = Q/t; a steady current of 1 A "
              "means 1 coulomb of charge flows every second.")

    b.bullets(
        "CONDUCTION", "Electrical Conduction in Solids",
        [("Free electrons", "In a metal, the outermost electrons of the "
          "atoms are loosely bound and can move freely through the "
          "metal — these are called free electrons."),
         ("Random motion without a cell", "Normally these free electrons "
          "move about randomly, so there is no net flow of charge in any "
          "one direction."),
         ("Drift under a cell", "When a cell is connected, it sets up a "
          "potential difference that makes the free electrons drift in a "
          "definite direction — this drift is the electric current."),
         ("Conventional current", "By convention, the direction of "
          "current is taken as the direction in which positive charge "
          "would flow — opposite to the actual direction of electron "
          "flow.")],
        notes="Clarify the historical convention: current direction is "
              "opposite to electron flow, a frequent point of "
              "confusion.")

    b.text_image(
        "CIRCUIT SYMBOLS", "Components of an Electric Circuit",
        ["An electric circuit is a closed conducting path through which "
         "an electric current flows.",
         "Standard symbols are used to draw circuit diagrams so that "
         "they are understood everywhere — a cell, a battery, a switch "
         "(key), a bulb, a resistor, an ammeter and a voltmeter each "
         "have their own symbol.",
         "The cell/battery drives the current; the switch makes or "
         "breaks the circuit; the resistor controls the current; the "
         "ammeter measures current and the voltmeter measures potential "
         "difference.",
         "Current flows only when the circuit is complete (closed); if "
         "the circuit is broken (open) at any point, no current flows."],
        symbols, img_side="right", panel_title="Reading a circuit "
        "diagram",
        notes="Have students copy the key symbols; they will use them in "
              "every circuit diagram for the rest of the syllabus.")

    b.quiz_intro("Quiz 1", "Check — Current & Circuits", 4)
    b.quiz_q(1, "Current", "Electric current is defined as the:",
             ["charge stored in a conductor", "rate of flow of electric "
              "charge", "resistance of a conductor", "work done by a "
              "cell"])
    b.quiz_a(1, "B. rate of flow of electric charge",
             "I = Q/t — current is the charge passing through a "
             "cross-section per unit time, measured in amperes.")
    b.quiz_q(2, "Unit", "One ampere of current is equal to:",
             ["one volt per second", "one coulomb per second", "one ohm "
              "per second", "one joule per second"])
    b.quiz_a(2, "B. one coulomb per second",
             "1 A = 1 C/s: a current of one ampere means one coulomb of "
             "charge flows each second.")
    b.quiz_q(3, "Conduction", "Electric current in a metal wire is due to "
             "the drift of:",
             ["protons", "free electrons", "neutrons", "positive ions"])
    b.quiz_a(3, "B. free electrons",
             "The loosely bound free electrons of the metal atoms drift "
             "under the applied potential difference, carrying the "
             "current.")
    b.quiz_q(4, "Conventional current", "The conventional direction of "
             "current is:",
             ["the same as the electron flow", "opposite to the electron "
              "flow", "always from low to high potential", "undefined"])
    b.quiz_a(4, "B. opposite to the electron flow",
             "Conventional current is taken in the direction positive "
             "charge would move — opposite to the actual electron "
             "drift.")

    # ---- Part 2 : potential difference, Ohm's law ----
    b.divider(2, "Part 2", "Potential Difference and Ohm's Law",
              "What drives the current, and how current depends on it")

    b.statement(
        "POTENTIAL DIFFERENCE", "Potential Difference",
        "The potential difference between two points of a conductor is "
        "the work done to carry a unit charge from one point to the "
        "other.",
        formula="V = W / Q",
        points=[
            "The SI unit of potential difference is the volt (V); "
            "1 volt = 1 joule per coulomb.",
            "A cell or battery maintains the potential difference that "
            "drives the current through a circuit.",
            "Potential difference is measured with a voltmeter, "
            "connected in parallel across the two points."],
        notes="Contrast the ammeter (series) with the voltmeter "
              "(parallel) — a very common practical/diagram question.")

    b.statement(
        "OHM'S LAW", "Ohm's Law",
        "Ohm's law: the current through a conductor is directly "
        "proportional to the potential difference across it, provided "
        "its temperature and other physical conditions remain constant.",
        formula="V = I R",
        points=[
            "The constant of proportionality R is the resistance of the "
            "conductor; its SI unit is the ohm (Ω).",
            "A conductor that obeys Ohm's law is called an ohmic "
            "conductor.",
            "1 ohm is the resistance of a conductor through which a "
            "current of 1 A flows when a potential difference of 1 V is "
            "applied across it."],
        notes="Stress the condition 'temperature constant' — Ohm's law "
              "holds only while the physical conditions do not change.")

    b.text_image(
        "VERIFICATION", "Experimental Verification of Ohm's Law",
        ["Connect a resistance wire, an ammeter (in series), a voltmeter "
         "(in parallel across the wire), a battery, a rheostat and a "
         "key in a circuit.",
         "Using the rheostat, change the current through the wire in "
         "steps and note the corresponding ammeter (I) and voltmeter (V) "
         "readings each time.",
         "Calculate the ratio V/I for each pair of readings — it is "
         "found to be constant, which is the resistance R of the wire.",
         "A graph of V against I is a straight line through the origin, "
         "confirming that V is directly proportional to I — this "
         "verifies Ohm's law."],
        ohmg, img_side="left", panel_title="A straight-line V–I graph",
        notes="The straight line through the origin is the signature of "
              "an ohmic conductor; its slope equals the resistance.")

    b.worked(
        "WORKED EXAMPLE", "Applying Ohm's Law",
        "A potential difference of 6 V is applied across a resistor and "
        "a current of 0.5 A flows through it. Find the resistance.",
        ["V = I R",
         "6 = 0.5 x R",
         "R = 6 / 0.5"],
        "R = 12 Ω",
        notes="Rearranging V = IR for R is the most common numerical; "
              "check units (V in volts, I in amperes, R in ohms).")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Electric current", "Rate of flow of charge, I = Q/t, unit "
                             "ampere; measured by an ammeter in series."),
         ("Conduction", "Free electrons drift under a potential "
                       "difference; conventional current is opposite to "
                       "electron flow."),
         ("Circuit & symbols", "A closed conducting path; components have "
                             "standard symbols and functions."),
         ("Potential difference", "V = W/Q, unit volt; measured by a "
                                "voltmeter in parallel."),
         ("Ohm's law", "V = I R at constant temperature; a straight-line "
                     "V–I graph verifies it.")],
        notes="Cold-call the correct way to connect an ammeter and a "
              "voltmeter before ending.")

    b.quiz_intro("Quiz 2", "Final Check — Potential Difference & Ohm's "
                 "Law", 4)
    b.quiz_q(1, "Potential difference", "The potential difference "
             "between two points is the work done to move a unit ___ "
             "between them.",
             ["mass", "charge", "current", "resistance"])
    b.quiz_a(1, "B. charge",
             "V = W/Q — potential difference is the work done per unit "
             "charge, measured in volts (joules per coulomb).")
    b.quiz_q(2, "Meters", "In a circuit, the voltmeter and ammeter are "
             "connected respectively in:",
             ["series and series", "parallel and series", "series and "
              "parallel", "parallel and parallel"])
    b.quiz_a(2, "B. parallel and series",
             "A voltmeter is connected in parallel across the component; "
             "an ammeter is connected in series so the whole current "
             "passes through it.")
    b.quiz_q(3, "Ohm's law", "According to Ohm's law, at constant "
             "temperature the current through a conductor is:",
             ["inversely proportional to the potential difference",
              "directly proportional to the potential difference",
              "independent of the potential difference", "proportional "
              "to the square of the potential difference"])
    b.quiz_a(3, "B. directly proportional to the potential difference",
             "V ∝ I (V = IR) as long as temperature and other physical "
             "conditions stay constant.")
    b.quiz_q(4, "Numerical", "A 12 V battery drives a current of 3 A "
             "through a resistor. The resistance is:",
             ["4 Ω", "36 Ω", "0.25 Ω", "15 Ω"])
    b.quiz_a(4, "A. 4 Ω",
             "R = V/I = 12/3 = 4 Ω.")

    b.closing("Charge in Motion",
              "A cell sets electrons drifting, Ohm's law tells us how "
              "much current flows, and a few standard symbols let us "
              "design and read any circuit.")
    return b


# ===========================================================================
# S32 — Current Electricity - 2  (resistance, resistivity, series/parallel)
# ===========================================================================
def ce2_deck():
    footer = "Current Electricity  •  MSBSHSE Std 9 Science & Technology"
    b = Builder(footer, accent=C["teal"])

    combo = b.asset("mh9_ce2_combo", D.resistors_combo("mh9_ce2_combo"))
    ohmc = b.asset("mh9_ce2_ohmc", D.ohm_circuit("mh9_ce2_ohmc"))
    plug = b.asset("mh9_ce2_plug", D.three_pin_plug("mh9_ce2_plug"))

    b.title("Std 9 • Science & Technology • Electricity",
            "Current Electricity — 2",
            "Resistance and resistivity  •  Resistors in series and "
            "parallel  •  Domestic circuits and safety", img=combo)

    b.objectives([
        "Define resistance and resistivity of a conductor",
        "State the factors on which the resistance of a wire depends",
        "Derive and use the formula for resistors in series",
        "Derive and use the formula for resistors in parallel",
        "Describe domestic electrical connections",
        "State the safety precautions to be taken while using "
        "electricity",
    ])

    # ---- Part 1 : resistance & resistivity ----
    b.divider(1, "Part 1", "Resistance and Resistivity",
              "What opposes the current, and what it depends on")

    b.statement(
        "RESISTANCE", "Resistance of a Conductor",
        "The resistance of a conductor is the opposition it offers to "
        "the flow of electric current through it.",
        formula="R = V / I",
        points=[
            "The SI unit of resistance is the ohm (Ω).",
            "Resistance arises because the drifting electrons collide "
            "with the atoms of the conductor, losing energy as heat.",
            "A good conductor has low resistance; an insulator has very "
            "high resistance."],
        notes="Connect to Ohm's law from the previous session: R = V/I "
              "is the same relation rearranged.")

    b.text_image(
        "FACTORS", "Factors Affecting the Resistance of a Wire",
        ["Length: the resistance of a wire is directly proportional to "
         "its length — a longer wire has more resistance.",
         "Area of cross-section: the resistance is inversely "
         "proportional to the area of cross-section — a thicker wire "
         "has less resistance.",
         "Material: different materials have different resistances for "
         "the same dimensions, described by a property called "
         "resistivity.",
         "Temperature: for most conductors the resistance increases as "
         "the temperature rises."],
        ohmc, img_side="right", panel_title="Length, thickness, material "
        "and temperature",
        notes="Give the everyday link: thin, long wires (like a heater "
              "coil) have high resistance; thick, short copper wires "
              "have low resistance.")

    b.statement(
        "RESISTIVITY", "Resistivity (Specific Resistance)",
        "Combining the effects of length (l) and area of cross-section "
        "(A) gives the resistance in terms of a material constant called "
        "resistivity (ρ).",
        formula="R = ρ l / A",
        points=[
            "Resistivity is the resistance of a wire of that material of "
            "unit length and unit area of cross-section.",
            "Its SI unit is the ohm-metre (Ω·m); it depends only on the "
            "material (and temperature), not on the wire's dimensions.",
            "Metals such as silver and copper have very low resistivity "
            "(good conductors); alloys such as nichrome have high "
            "resistivity (used in heating elements)."],
        notes="Distinguish resistance (depends on the specific wire) "
              "from resistivity (a property of the material).")

    b.quiz_intro("Quiz 1", "Check — Resistance & Resistivity", 4)
    b.quiz_q(1, "Resistance", "The resistance of a conductor is the:",
             ["ease with which current flows", "opposition it offers to "
              "the flow of current", "charge stored in it", "potential "
              "difference across it"])
    b.quiz_a(1, "B. opposition it offers to the flow of current",
             "Resistance opposes current; it arises from collisions of "
             "drifting electrons with the conductor's atoms.")
    b.quiz_q(2, "Length", "If the length of a wire is doubled (keeping "
             "everything else the same), its resistance:",
             ["halves", "doubles", "stays the same", "becomes four "
              "times"])
    b.quiz_a(2, "B. doubles",
             "Resistance is directly proportional to length (R = ρl/A), "
             "so doubling the length doubles the resistance.")
    b.quiz_q(3, "Thickness", "A thicker wire (larger area of "
             "cross-section) of the same material and length has:",
             ["more resistance", "less resistance", "the same "
              "resistance", "zero resistance"])
    b.quiz_a(3, "B. less resistance",
             "Resistance is inversely proportional to the area of "
             "cross-section, so a thicker wire offers less resistance.")
    b.quiz_q(4, "Resistivity", "The resistivity of a material depends "
             "on:",
             ["the length of the wire", "the thickness of the wire",
              "the material and its temperature", "the current through "
              "it"])
    b.quiz_a(4, "C. the material and its temperature",
             "Resistivity is a property of the material (and its "
             "temperature); it does not depend on the wire's dimensions.")

    # ---- Part 2 : series, parallel, domestic circuits ----
    b.divider(2, "Part 2", "Combinations of Resistors and Domestic "
              "Circuits", "Adding resistances, and using electricity "
              "safely at home")

    b.statement(
        "SERIES", "Resistors in Series",
        "When resistors are joined end to end so that the same current "
        "flows through each, they are said to be connected in series.",
        formula="Rs = R₁ + R₂ + R₃ + ...",
        points=[
            "The same current flows through every resistor in a series "
            "combination.",
            "The total potential difference is shared among the "
            "resistors and equals the sum of the individual potential "
            "differences.",
            "The equivalent (total) resistance is larger than the "
            "largest individual resistance."],
        notes="Everyday link: old decorative light strings are in "
              "series, so if one bulb fails the whole string goes off.")

    b.text_image(
        "PARALLEL", "Resistors in Parallel",
        ["When resistors are connected between the same two points so "
         "that the same potential difference acts across each, they are "
         "in parallel.",
         "The potential difference is the same across every resistor, "
         "while the main current is shared among the branches.",
         "The reciprocal of the equivalent resistance equals the sum of "
         "the reciprocals of the individual resistances: "
         "1/Rp = 1/R₁ + 1/R₂ + 1/R₃ + ...",
         "The equivalent resistance of a parallel combination is smaller "
         "than the smallest individual resistance."],
        combo, img_side="left", panel_title="Same voltage, shared "
        "current",
        notes="Household appliances are wired in parallel so each gets "
              "the full mains voltage and can be switched independently.")

    b.worked(
        "WORKED EXAMPLE", "Series and Parallel Combinations",
        "Two resistors of 6 Ω and 3 Ω are connected (i) in series and "
        "(ii) in parallel. Find the equivalent resistance in each case.",
        ["Series: Rs = R₁ + R₂ = 6 + 3 = 9 Ω",
         "Parallel: 1/Rp = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2",
         "Rp = 2 Ω"],
        "Series = 9 Ω; Parallel = 2 Ω",
        notes="Note the parallel result (2 Ω) is less than the smaller "
              "resistor (3 Ω) — a good check on the arithmetic.")

    b.bullets(
        "DOMESTIC CIRCUITS & SAFETY", "Domestic Connections and Safety",
        [("Parallel wiring at home", "Appliances in a house are "
          "connected in parallel across the live and neutral wires, so "
          "each receives the full supply voltage and works "
          "independently."),
         ("Live, neutral and earth", "The supply reaches a house through "
          "the live and neutral wires; a separate earth wire safely "
          "carries away leakage current."),
         ("Fuse and MCB", "A fuse or a miniature circuit breaker (MCB) "
          "is placed in the live wire; it breaks the circuit if the "
          "current becomes dangerously large."),
         ("Safety precautions", "Never touch switches or appliances with "
          "wet hands, use properly earthed three-pin plugs for heavy "
          "appliances, and use wires and fuses of the correct rating.")],
        notes="Tie the fuse action back to the heating effect of "
              "current: an overload heats and melts the fuse wire, "
              "breaking the circuit.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Resistance", "Opposition to current, R = V/I, unit ohm."),
         ("Factors", "R increases with length, decreases with thickness; "
                   "depends on material and temperature."),
         ("Resistivity", "R = ρl/A; ρ is a material property, unit "
                        "ohm-metre."),
         ("Series", "Same current; Rs = R₁ + R₂ + ... (larger than any "
                   "one)."),
         ("Parallel", "Same voltage; 1/Rp = 1/R₁ + 1/R₂ + ... (smaller "
                     "than any one)."),
         ("Domestic safety", "Parallel wiring, earthing, fuse/MCB in the "
                           "live wire, correct ratings.")],
        notes="Ask students to predict whether combining resistors in "
              "parallel raises or lowers the total resistance, and why.")

    b.quiz_intro("Quiz 2", "Final Check — Combinations & Domestic "
                 "Circuits", 4)
    b.quiz_q(1, "Series", "Three resistors of 2 Ω, 3 Ω and 5 Ω are "
             "connected in series. Their equivalent resistance is:",
             ["10 Ω", "0.97 Ω", "3.3 Ω", "1 Ω"])
    b.quiz_a(1, "A. 10 Ω",
             "In series, Rs = R₁ + R₂ + R₃ = 2 + 3 + 5 = 10 Ω.")
    b.quiz_q(2, "Parallel", "Two 4 Ω resistors are connected in "
             "parallel. Their equivalent resistance is:",
             ["8 Ω", "4 Ω", "2 Ω", "0.5 Ω"])
    b.quiz_a(2, "C. 2 Ω",
             "1/Rp = 1/4 + 1/4 = 1/2, so Rp = 2 Ω — for two equal "
             "resistors in parallel, the result is half of one.")
    b.quiz_q(3, "Home wiring", "Electrical appliances in a house are "
             "connected in parallel mainly so that:",
             ["they use less current", "each gets the full supply "
              "voltage and can be operated independently", "the wiring is "
              "cheaper", "the fuse never blows"])
    b.quiz_a(3, "B. each gets the full supply voltage and can be "
             "operated independently",
             "Parallel wiring gives every appliance the full mains "
             "voltage and lets each be switched on or off without "
             "affecting the others.")
    b.quiz_q(4, "Safety", "In domestic wiring, the fuse or MCB is "
             "connected in the ___ wire.",
             ["earth", "neutral", "live", "any"])
    b.quiz_a(4, "C. live",
             "The fuse/MCB is placed in the live wire so that, when it "
             "breaks, the appliance is disconnected from the live "
             "supply and is safe to handle.")

    b.closing("Controlling the Current",
              "Resistance and resistivity decide how much current flows; "
              "series and parallel rules let us combine resistors, and "
              "safe domestic wiring puts it all to everyday use.")
    return b


def build():
    jobs = [
        ("MH09_S30_Current_Electricity_1.pptx", ce1_deck),
        ("MH09_S32_Current_Electricity_2.pptx", ce2_deck),
        ("MH09_S44_Reflection_of_Light_1.pptx", refl1_deck),
        ("MH09_S46_Reflection_of_Light_2.pptx", refl2_deck),
        ("MH09_S58_Study_of_Sound_1.pptx", sound1_deck),
        ("MH09_S60_Study_of_Sound_2.pptx", sound2_deck),
        ("MH09_S75_Observing_Space_Telescopes.pptx", telescope_deck),
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
# S44 — Reflection of Light - 1  (mirrors, spherical mirrors, terms)
# ===========================================================================
def refl1_deck():
    footer = "Reflection of Light  •  MSBSHSE Std 9 Science & Technology"
    b = Builder(footer, accent=C["purple"])

    law = b.asset("mh9_refl1_law", D.reflection_law("mh9_refl1_law"))
    plane = b.asset("mh9_refl1_plane", D.plane_mirror_image("mh9_refl1_plane"))
    concave = b.asset("mh9_refl1_concave",
                      D.concave_mirror_image("mh9_refl1_concave"))
    convex = b.asset("mh9_refl1_convex",
                     D.convex_mirror_image("mh9_refl1_convex"))

    b.title("Std 9 • Science & Technology • Optics",
            "Reflection of Light — 1",
            "Reflection and mirrors  •  Spherical mirrors  •  Terms and "
            "the R = 2f relation  •  Convergence & divergence", img=concave)

    b.objectives([
        "State the laws of reflection of light",
        "Distinguish between plane, concave and convex mirrors",
        "Explain how concave mirrors converge and convex mirrors diverge "
        "light",
        "Define the terms related to spherical mirrors",
        "Relate the focal length and radius of curvature (R = 2f)",
        "Identify real and virtual foci for the two kinds of mirror",
    ])

    # ---- Part 1 : reflection & mirrors ----
    b.divider(1, "Part 1", "Reflection and Types of Mirrors",
              "The laws of reflection and the two spherical mirrors")

    b.statement(
        "LAWS OF REFLECTION", "The Laws of Reflection of Light",
        "When light falls on a polished (reflecting) surface, it bounces "
        "back following two laws of reflection.",
        img=law,
        notes="First law: the angle of incidence equals the angle of "
              "reflection. Second law: the incident ray, the reflected "
              "ray and the normal at the point of incidence all lie in "
              "the same plane. These laws hold for every reflecting "
              "surface, plane or curved.")

    b.cards(
        "SPHERICAL MIRRORS", "Plane and Spherical Mirrors",
        [("Plane mirror", "A flat reflecting surface; it forms a virtual, "
          "erect image of the same size as the object, as far behind "
          "the mirror as the object is in front."),
         ("Concave mirror", "A spherical mirror whose reflecting surface "
          "is the inner (caved-in) surface of the sphere; it converges a "
          "parallel beam of light to a real focus, so it is a "
          "converging mirror."),
         ("Convex mirror", "A spherical mirror whose reflecting surface "
          "is the outer (bulging) surface; it diverges a parallel beam, "
          "which appears to come from a virtual focus behind the mirror "
          "— a diverging mirror."),
         ("Where they come from", "A spherical mirror is a small part of "
          "a hollow sphere; silvering the outside gives a concave "
          "mirror and silvering the inside gives a convex mirror.")],
        icons=["eye", "eye", "eye", "star"],
        notes="Use a shiny spoon: the inner side (concave) inverts your "
              "image, the back (convex) gives a small upright image.")

    b.text_image(
        "CONVERGENCE", "Converging and Diverging Mirrors",
        ["A concave mirror reflects a parallel beam of light so that the "
         "rays actually meet at a single point in front of the mirror — "
         "its principal focus. This is convergence.",
         "Because the rays really meet, a concave mirror has a real "
         "focus and can form real images.",
         "A convex mirror reflects a parallel beam so that the rays "
         "spread out (diverge); when produced backwards they appear to "
         "come from a point behind the mirror — a virtual focus.",
         "A convex mirror therefore always forms a virtual, erect and "
         "diminished image, whatever the position of the object."],
        convex, img_side="right", panel_title="Real vs virtual focus",
        notes="This convergence/divergence distinction decides "
              "everything about the images each mirror forms in the next "
              "session.")

    b.quiz_intro("Quiz 1", "Check — Reflection & Mirrors", 4)
    b.quiz_q(1, "Laws", "According to the first law of reflection, the "
             "angle of incidence is:",
             ["greater than the angle of reflection", "equal to the "
              "angle of reflection", "less than the angle of "
              "reflection", "always 90°"])
    b.quiz_a(1, "B. equal to the angle of reflection",
             "The angle of incidence always equals the angle of "
             "reflection, both measured from the normal at the point of "
             "incidence.")
    b.quiz_q(2, "Concave mirror", "A concave mirror reflects a parallel "
             "beam of light so that the rays:",
             ["diverge", "converge to a real focus", "are absorbed",
              "pass straight through"])
    b.quiz_a(2, "B. converge to a real focus",
             "A concave (converging) mirror brings a parallel beam "
             "together at its real principal focus in front of the "
             "mirror.")
    b.quiz_q(3, "Convex mirror", "The image formed by a convex mirror is "
             "always:",
             ["real and inverted", "virtual, erect and diminished",
              "real and magnified", "the same size as the object"])
    b.quiz_a(3, "B. virtual, erect and diminished",
             "A convex (diverging) mirror always forms a small, upright, "
             "virtual image, whatever the object's position.")
    b.quiz_q(4, "Focus", "A convex mirror is said to have a virtual focus "
             "because the reflected parallel rays:",
             ["actually meet in front of it", "only appear to come from "
              "a point behind it", "are absorbed at the surface", "never "
              "leave the mirror"])
    b.quiz_a(4, "B. only appear to come from a point behind it",
             "The diverging reflected rays, produced backwards, seem to "
             "start from a virtual focus behind the convex mirror.")

    # ---- Part 2 : terms, R = 2f ----
    b.divider(2, "Part 2", "Terms Related to Spherical Mirrors",
              "The vocabulary you need for ray diagrams and formulae")

    b.bullets(
        "KEY TERMS", "Terms Related to a Spherical Mirror",
        [("Pole (P)", "The central point of the reflecting surface of "
          "the mirror."),
         ("Centre of curvature (C)", "The centre of the hollow sphere of "
          "which the mirror is a part."),
         ("Radius of curvature (R)", "The radius of that sphere — the "
          "distance PC."),
         ("Principal axis", "The straight line passing through the pole "
          "P and the centre of curvature C."),
         ("Principal focus (F)", "The point on the principal axis where "
          "rays parallel to the axis meet (concave) or appear to come "
          "from (convex) after reflection."),
         ("Focal length (f)", "The distance between the pole P and the "
          "principal focus F.")],
        notes="Draw and label all six terms on one clear diagram; "
              "students reuse this vocabulary throughout the chapter.")

    b.statement(
        "R = 2f", "Relation Between Focal Length and Radius of Curvature",
        "For a spherical mirror, the principal focus lies exactly midway "
        "between the pole and the centre of curvature.",
        formula="R = 2f     (so f = R / 2)",
        points=[
            "The radius of curvature is twice the focal length of the "
            "mirror.",
            "So a mirror with a radius of curvature of 20 cm has a focal "
            "length of 10 cm.",
            "This relation lets us find one quantity if the other is "
            "known."],
        notes="A frequently used relation in numericals; derive it "
              "quickly from a ray parallel to the axis reflecting through "
              "F.")

    b.worked(
        "WORKED EXAMPLE", "Using R = 2f",
        "The radius of curvature of a concave mirror is 30 cm. Find its "
        "focal length.",
        ["R = 2f",
         "f = R / 2 = 30 / 2"],
        "f = 15 cm",
        notes="Trivial arithmetic, but check the sign convention will be "
              "applied later — here we just relate the magnitudes.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Laws of reflection", "Angle of incidence = angle of "
                              "reflection; incident ray, reflected ray "
                              "and normal are coplanar."),
         ("Concave mirror", "Converging; real focus; can form real "
                          "images."),
         ("Convex mirror", "Diverging; virtual focus; always a virtual, "
                         "erect, diminished image."),
         ("Terms", "Pole, centre of curvature, radius, principal axis, "
                 "focus, focal length."),
         ("R = 2f", "The focus is midway between the pole and the centre "
                  "of curvature.")],
        notes="Cold-call each term and the R = 2f relation before the "
              "final quiz.")

    b.quiz_intro("Quiz 2", "Final Check — Terms & R = 2f", 4)
    b.quiz_q(1, "Pole", "The central point of the reflecting surface of a "
             "spherical mirror is called its:",
             ["centre of curvature", "pole", "focus", "principal axis"])
    b.quiz_a(1, "B. pole",
             "The pole (P) is the central point of the mirror's "
             "reflecting surface.")
    b.quiz_q(2, "Centre of curvature", "The centre of the sphere of "
             "which a spherical mirror forms a part is the:",
             ["pole", "principal focus", "centre of curvature", "focal "
              "point"])
    b.quiz_a(2, "C. centre of curvature",
             "The centre of curvature (C) is the centre of the hollow "
             "sphere; the distance PC is the radius of curvature.")
    b.quiz_q(3, "R = 2f", "A concave mirror has a focal length of 12 cm. "
             "Its radius of curvature is:",
             ["6 cm", "12 cm", "24 cm", "36 cm"])
    b.quiz_a(3, "C. 24 cm",
             "R = 2f = 2 × 12 = 24 cm.")
    b.quiz_q(4, "Focus location", "The principal focus of a spherical "
             "mirror lies:",
             ["at the pole", "at the centre of curvature", "midway "
              "between the pole and the centre of curvature", "at "
              "infinity"])
    b.quiz_a(4, "C. midway between the pole and the centre of curvature",
             "Because R = 2f, the focus F is exactly halfway between the "
             "pole P and the centre of curvature C.")

    b.closing("Mirrors That Bend Light to a Point",
              "Concave mirrors gather light to a real focus and convex "
              "mirrors spread it from a virtual one — the same two laws "
              "of reflection behind every curved mirror.")
    return b


# ===========================================================================
# S46 — Reflection of Light - 2  (ray diagrams, images, mirror formula)
# ===========================================================================
def refl2_deck():
    footer = "Reflection of Light  •  MSBSHSE Std 9 Science & Technology"
    b = Builder(footer, accent=C["orange"])

    concave = b.asset("mh9_refl2_concave",
                      D.concave_mirror_image("mh9_refl2_concave"))
    convex = b.asset("mh9_refl2_convex",
                     D.convex_mirror_image("mh9_refl2_convex"))

    b.title("Std 9 • Science & Technology • Optics",
            "Reflection of Light — 2",
            "Ray diagrams  •  Images by concave & convex mirrors  •  "
            "Sign convention  •  Mirror formula & magnification",
            img=concave)

    b.objectives([
        "State the rules for drawing ray diagrams for spherical mirrors",
        "Draw and describe images formed by a concave mirror for "
        "different object positions",
        "Describe the image formed by a convex mirror",
        "Apply the Cartesian sign convention for spherical mirrors",
        "Use the mirror formula 1/v + 1/u = 1/f",
        "Calculate magnification and state the uses of spherical mirrors",
    ])

    # ---- Part 1 : ray diagrams & images ----
    b.divider(1, "Part 1", "Ray Diagrams and Images",
              "Locating images formed by spherical mirrors")

    b.bullets(
        "RAY RULES", "Rules for Drawing Ray Diagrams",
        [("Ray parallel to the principal axis", "After reflection it "
          "passes through the principal focus F (concave) or appears to "
          "come from F (convex)."),
         ("Ray through the principal focus", "A ray passing through F "
          "(concave) is reflected parallel to the principal axis."),
         ("Ray through the centre of curvature", "A ray passing through "
          "(or directed towards) C strikes the mirror normally and is "
          "reflected back along the same path."),
         ("Ray to the pole", "A ray striking the pole P is reflected "
          "making an equal angle with the principal axis.")],
        notes="Any two of these rays are enough to locate the image; "
              "the others are useful checks.")

    b.text_image(
        "CONCAVE IMAGES", "Images Formed by a Concave Mirror",
        ["The nature of the image depends on where the object is placed "
         "relative to F and C.",
         "Object beyond C: image is real, inverted and diminished, "
         "formed between F and C.",
         "Object at C: image is real, inverted and the same size, "
         "formed at C; object between C and F: real, inverted and "
         "magnified, beyond C.",
         "Object between F and the pole: image is virtual, erect and "
         "magnified — the principle of a shaving/make-up mirror."],
        concave, img_side="right", panel_title="Depends on the object's "
        "position",
        notes="Walk the object from far away inward, naming the image "
              "type at each stage; this table is a very common exam "
              "question.")

    b.text_image(
        "CONVEX IMAGES", "Images Formed by a Convex Mirror",
        ["For a convex mirror the image is always of the same nature, "
         "whatever the object's position.",
         "The image is always virtual, erect and diminished, formed "
         "between the pole and the focus behind the mirror.",
         "As the object moves closer, the image grows a little but "
         "always stays smaller than the object.",
         "Because it gives a wide, upright field of view, a convex "
         "mirror is used as a rear-view mirror and as a security mirror "
         "in shops."],
        convex, img_side="left", panel_title="Always small, upright and "
        "virtual",
        notes="Contrast strongly with the concave mirror, whose image "
              "changes; the convex mirror's image never changes in "
              "nature.")

    b.quiz_intro("Quiz 1", "Check — Ray Diagrams & Images", 4)
    b.quiz_q(1, "Ray rule", "A ray parallel to the principal axis, after "
             "reflection from a concave mirror, passes through the:",
             ["pole", "centre of curvature", "principal focus", "object"])
    b.quiz_a(1, "C. principal focus",
             "A ray parallel to the axis reflects through the principal "
             "focus F of a concave mirror.")
    b.quiz_q(2, "Concave image", "An object placed between the focus and "
             "the pole of a concave mirror gives an image that is:",
             ["real, inverted and diminished", "virtual, erect and "
              "magnified", "real and the same size", "virtual and "
              "diminished"])
    b.quiz_a(2, "B. virtual, erect and magnified",
             "With the object within the focus, a concave mirror forms a "
             "magnified, upright, virtual image — used in shaving and "
             "make-up mirrors.")
    b.quiz_q(3, "Object at C", "When an object is placed at the centre "
             "of curvature of a concave mirror, the image is:",
             ["diminished", "the same size as the object", "magnified",
              "virtual"])
    b.quiz_a(3, "B. the same size as the object",
             "At C the image is real, inverted and exactly the same size "
             "as the object, also formed at C.")
    b.quiz_q(4, "Convex use", "A convex mirror is preferred as a vehicle "
             "rear-view mirror because it:",
             ["magnifies vehicles behind", "gives a wide, upright field "
              "of view", "forms real images", "reverses left and right"])
    b.quiz_a(4, "B. gives a wide, upright field of view",
             "Its always-diminished, erect virtual image covers a large "
             "area behind the vehicle, so more traffic is visible.")

    # ---- Part 2 : sign convention, mirror formula, magnification ----
    b.divider(2, "Part 2", "Mirror Formula and Magnification",
              "Calculating image position, size and nature")

    b.bullets(
        "SIGN CONVENTION", "Cartesian Sign Convention for Mirrors",
        [("Origin at the pole", "All distances are measured from the "
          "pole P of the mirror, along the principal axis."),
         ("Direction of incident light", "Distances measured in the "
          "direction of the incident light (to the right) are positive; "
          "those against it (to the left) are negative."),
         ("Object distance", "The object is always placed to the left, "
          "so the object distance u is negative."),
         ("Heights", "Heights measured upwards (above the axis) are "
          "positive; heights measured downwards are negative.")],
        notes="Getting the signs right is the whole battle in mirror "
              "numericals; insist students write signs before "
              "substituting.")

    b.statement(
        "MIRROR FORMULA", "The Mirror Formula and Magnification",
        "The mirror formula relates the object distance (u), image "
        "distance (v) and focal length (f) of a spherical mirror, valid "
        "for all mirrors and all object positions with the sign "
        "convention.",
        formula="1/v + 1/u = 1/f     •     m = h₂/h₁ = −v/u",
        points=[
            "For a concave mirror f is negative; for a convex mirror f "
            "is positive.",
            "A negative magnification means a real, inverted image; a "
            "positive magnification means a virtual, erect image.",
            "|m| > 1 means magnified, |m| < 1 means diminished."],
        notes="Note the mirror formula uses 1/v + 1/u (a plus), unlike "
              "the lens formula which uses a minus — a classic slip.")

    b.worked(
        "WORKED EXAMPLE", "Using the Mirror Formula",
        "An object is placed 30 cm in front of a concave mirror of focal "
        "length 20 cm. Find the image distance and magnification.",
        ["Sign convention: u = −30 cm, f = −20 cm",
         "1/v = 1/f − 1/u = 1/(−20) − 1/(−30) = −3/60 + 2/60 = −1/60",
         "v = −60 cm (negative → real image, in front of the mirror)",
         "m = −v/u = −(−60)/(−30) = −2  (real, inverted, magnified 2×)"],
        "v = −60 cm; real, inverted, magnified image",
        notes="Show every sign substitution; the negative v tells us the "
              "image is real and formed in front of the mirror.")

    b.cards(
        "USES", "Uses of Spherical Mirrors",
        [("Concave — shaving/make-up mirror", "With the face within the "
          "focus, it gives an enlarged, erect image."),
         ("Concave — headlamps & torches", "A bulb at the focus produces "
          "a strong parallel beam of light."),
         ("Concave — solar devices & floodlights", "Concentrate sunlight "
          "at the focus, or give a bright beam when the source is beyond "
          "C."),
         ("Convex — rear-view & security mirrors", "Give a wide, upright "
          "field of view so a large area is visible.")],
        icons=["eye", "bulb", "sun", "eye"],
        notes="Link each use back to the image property that makes it "
              "work — magnification, parallel beam or wide field.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Ray rules", "Parallel→F; through F→parallel; through C→back "
                     "along itself."),
         ("Concave images", "Vary with object position — real/inverted "
                          "far off, virtual/magnified within F."),
         ("Convex images", "Always virtual, erect and diminished."),
         ("Sign convention", "Distances from the pole; incident-light "
                           "direction positive; object distance "
                           "negative."),
         ("Mirror formula", "1/v + 1/u = 1/f; m = −v/u."),
         ("Uses", "Headlamps, shaving mirrors, solar devices, rear-view "
                "mirrors.")],
        notes="Ask students to contrast the concave and convex image "
              "tables one more time.")

    b.quiz_intro("Quiz 2", "Final Check — Formula & Magnification", 4)
    b.quiz_q(1, "Sign convention", "In the Cartesian sign convention for "
             "mirrors, the object distance u is always taken as:",
             ["positive", "negative", "zero", "equal to f"])
    b.quiz_a(1, "B. negative",
             "The object is placed to the left of the pole, against the "
             "incident-light direction, so u is negative.")
    b.quiz_q(2, "Mirror formula", "The mirror formula relating u, v and "
             "f is:",
             ["1/v − 1/u = 1/f", "1/v + 1/u = 1/f", "v + u = f", "1/f = "
              "1/v × 1/u"])
    b.quiz_a(2, "B. 1/v + 1/u = 1/f",
             "The mirror formula is 1/v + 1/u = 1/f (a plus sign, unlike "
             "the lens formula).")
    b.quiz_q(3, "Magnification", "A magnification of −3 produced by a "
             "concave mirror means the image is:",
             ["virtual, erect and magnified", "real, inverted and "
              "magnified", "virtual and diminished", "real and the same "
              "size"])
    b.quiz_a(3, "B. real, inverted and magnified",
             "A negative magnification indicates a real, inverted image; "
             "its magnitude of 3 means it is three times the object's "
             "size.")
    b.quiz_q(4, "Uses", "The mirror used in vehicle headlamps to produce "
             "a powerful parallel beam is a:",
             ["plane mirror", "convex mirror", "concave mirror", "flat "
              "glass sheet"])
    b.quiz_a(4, "C. concave mirror",
             "A bulb placed at the focus of a concave mirror produces a "
             "strong parallel beam, ideal for a headlamp.")

    b.closing("From Rays to Images",
              "A few ray rules, a careful sign convention and one mirror "
              "formula let us predict exactly where a spherical mirror "
              "forms its image and how big it will be.")
    return b




# ===========================================================================
# S58 — Study of Sound - 1  (nature, propagation, waves, characteristics)
# ===========================================================================
def sound1_deck():
    footer = "Study of Sound  •  MSBSHSE Std 9 Science & Technology"
    b = Builder(footer, accent=C["teal"])

    longw = b.asset("mh9_snd1_long", D.longitudinal_wave("mh9_snd1_long"))
    terms = b.asset("mh9_snd1_terms", D.wave_terms("mh9_snd1_terms"))
    chars = b.asset("mh9_snd1_chars", D.sound_characteristics("mh9_snd1_chars"))

    b.title("Std 9 • Science & Technology • Sound",
            "Study of Sound — 1",
            "Sound waves  •  Longitudinal & transverse  •  Wave terms  •  "
            "Characteristics of sound", img=longw)

    b.objectives([
        "Explain how sound is produced and why it needs a medium",
        "Distinguish longitudinal and transverse waves",
        "Describe compressions and rarefactions in a sound wave",
        "Define the terms of a wave and use v = f λ",
        "Relate loudness to amplitude and pitch to frequency",
        "Explain the quality (timbre) of a sound",
    ])

    # ---- Part 1 : nature & propagation ----
    b.divider(1, "Part 1", "Nature and Propagation of Sound",
              "What sound is and how it travels")

    b.bullets(
        "PRODUCTION", "How Sound Is Produced and Travels",
        [("Produced by vibration", "A vibrating body produces sound."),
         ("Needs a medium", "Sound travels through a medium; it cannot "
          "travel through a vacuum."),
         ("Travels as a wave", "The vibration passes energy from particle "
          "to particle without the particles moving along."),
         ("Longitudinal in air", "In air, sound travels as a "
          "longitudinal wave.")],
        notes="Recall the bell-jar experiment: as air is pumped out the "
              "sound fades, proving sound needs a material medium.")

    b.text_image(
        "WAVE TYPES", "Longitudinal and Transverse Waves",
        ["Longitudinal: particles vibrate along the direction of travel",
         "Made of compressions (crowded) and rarefactions (spread out)",
         "Transverse: particles vibrate across the direction of travel",
         "Transverse waves have crests and troughs",
         "Sound in air is a longitudinal wave"],
        longw, img_side="right", panel_title="Two kinds of wave",
        notes="Compressions are high-pressure, high-density regions; "
              "rarefactions are low-pressure, low-density regions.")

    b.text_image(
        "WAVE TERMS", "Terms and the Wave Relation",
        ["Wavelength (λ): distance between two compressions",
         "Frequency (f): vibrations per second, unit hertz (Hz)",
         "Time period (T): time for one vibration, T = 1/f",
         "Amplitude: maximum displacement of a particle",
         "Wave relation: v = f λ"],
        terms, img_side="left", panel_title="Describing a wave",
        notes="v = f λ ties speed, frequency and wavelength together; it "
              "is used in almost every sound numerical.")

    b.quiz_intro("Quiz 1", "Check — Nature of Sound", 4)
    b.quiz_q(1, "Medium", "Sound cannot travel through:",
             ["a solid", "a liquid", "a gas", "a vacuum"])
    b.quiz_a(1, "D. a vacuum",
             "Sound needs a material medium; with no particles to pass on "
             "the vibration, it cannot travel through a vacuum.")
    b.quiz_q(2, "Wave type", "Sound travels through air as a:",
             ["transverse wave", "longitudinal wave", "water wave", "light "
              "wave"])
    b.quiz_a(2, "B. longitudinal wave",
             "In air the particles vibrate back and forth along the "
             "direction of travel, forming compressions and "
             "rarefactions.")
    b.quiz_q(3, "Regions", "The region of a sound wave where the "
             "particles are crowded together is a:",
             ["rarefaction", "compression", "crest", "trough"])
    b.quiz_a(3, "B. compression",
             "A compression is a region of high density and high "
             "pressure; a rarefaction is the opposite.")
    b.quiz_q(4, "Numerical", "A sound wave has frequency 500 Hz and "
             "wavelength 0.66 m. Its speed is:",
             ["330 m/s", "500 m/s", "0.66 m/s", "757 m/s"])
    b.quiz_a(4, "A. 330 m/s",
             "v = f λ = 500 × 0.66 = 330 m/s.")

    # ---- Part 2 : characteristics of sound ----
    b.divider(2, "Part 2", "Characteristics of Sound",
              "Loudness, pitch and quality")

    b.text_image(
        "CHARACTERISTICS", "The Three Characteristics of Sound",
        ["Loudness depends on the amplitude of the wave",
         "Larger amplitude → louder sound",
         "Pitch depends on the frequency of the wave",
         "Higher frequency → higher pitch (shriller)",
         "Quality (timbre) depends on the waveform"],
        chars, img_side="right", panel_title="What makes sounds "
        "different",
        notes="Quality lets us tell the same note apart on a flute and a "
              "violin, and lets us recognise a familiar voice.")

    b.bullets(
        "CONTRAST", "Loudness vs Pitch vs Quality",
        [("Loudness", "Set by amplitude; measured in decibels (dB)."),
         ("Pitch", "Set by frequency; a high-pitch sound is shrill, a "
          "low-pitch sound is deep."),
         ("Quality (timbre)", "Set by the shape of the waveform; "
          "identifies the source of the sound."),
         ("Independent", "Two sounds can have the same loudness but "
          "different pitch, or the same pitch but different quality.")],
        notes="Stress that loudness (amplitude) and pitch (frequency) are "
              "independent — a common confusion.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Production", "Sound is made by vibration and needs a "
                      "medium."),
         ("Longitudinal wave", "Compressions and rarefactions travel "
                             "through the medium."),
         ("Wave terms", "Wavelength, frequency, time period, amplitude; "
                      "v = f λ."),
         ("Loudness", "Depends on amplitude."),
         ("Pitch", "Depends on frequency."),
         ("Quality", "Depends on the waveform — identifies the "
                   "source.")],
        notes="Cold-call which property changes when a guitar string is "
              "plucked harder (amplitude → loudness) versus tightened "
              "(frequency → pitch).")

    b.quiz_intro("Quiz 2", "Final Check — Characteristics", 4)
    b.quiz_q(1, "Loudness", "The loudness of a sound depends on its:",
             ["frequency", "amplitude", "wavelength", "speed"])
    b.quiz_a(1, "B. amplitude",
             "A larger amplitude of vibration produces a louder sound.")
    b.quiz_q(2, "Pitch", "A shrill (high-pitched) sound has a high:",
             ["amplitude", "frequency", "speed", "loudness"])
    b.quiz_a(2, "B. frequency",
             "Pitch depends on frequency; the higher the frequency, the "
             "higher the pitch.")
    b.quiz_q(3, "Quality", "We can tell a flute from a violin playing the "
             "same note because of the sound's:",
             ["loudness", "pitch", "quality (timbre)", "speed"])
    b.quiz_a(3, "C. quality (timbre)",
             "Quality, set by the waveform, distinguishes the same note "
             "produced by different sources.")
    b.quiz_q(4, "Period", "A tuning fork vibrates with a frequency of "
             "250 Hz. Its time period is:",
             ["0.004 s", "250 s", "4 s", "0.25 s"])
    b.quiz_a(4, "A. 0.004 s",
             "T = 1/f = 1/250 = 0.004 s.")

    b.closing("The Physics of What We Hear",
              "A vibrating source, a medium to carry it, and three simple "
              "properties — loudness, pitch and quality — explain every "
              "sound we hear.")
    return b


# ===========================================================================
# S60 — Study of Sound - 2  (speed, range, reflection, echo, SONAR)
# ===========================================================================
def sound2_deck():
    footer = "Study of Sound  •  MSBSHSE Std 9 Science & Technology"
    b = Builder(footer, accent=C["orange"])

    echo = b.asset("mh9_snd2_echo", D.echo_diagram("mh9_snd2_echo"))
    longw = b.asset("mh9_snd2_long", D.longitudinal_wave("mh9_snd2_long"))

    b.title("Std 9 • Science & Technology • Sound",
            "Study of Sound — 2",
            "Speed of sound  •  Audible range  •  Reflection & echo  •  "
            "Reverberation, SONAR and sonography", img=echo)

    b.objectives([
        "State the speed of sound and how it varies with the medium",
        "Classify sounds as infrasonic, audible and ultrasonic",
        "State the laws of reflection of sound",
        "Explain echo and the condition for hearing one",
        "Distinguish echo from reverberation",
        "Describe SONAR and sonography as uses of ultrasound",
    ])

    # ---- Part 1 : speed & range ----
    b.divider(1, "Part 1", "Speed and Range of Sound",
              "How fast sound travels and what we can hear")

    b.bullets(
        "SPEED", "Speed of Sound in Different Media",
        [("In air", "About 340 m/s at ordinary room temperature."),
         ("Fastest in solids", "Sound travels fastest in solids, slower "
          "in liquids, slowest in gases."),
         ("Why", "The more closely packed the particles, the faster the "
          "vibration is passed on."),
         ("Temperature", "In a gas, the speed of sound increases as the "
          "temperature rises.")],
        notes="Contrast with light: sound is far slower, which is why we "
              "see lightning before we hear thunder.")

    b.text_image(
        "RANGE", "Audible Range and Beyond",
        ["Audible sound: about 20 Hz to 20,000 Hz",
         "Infrasonic: below 20 Hz (e.g. earthquakes)",
         "Ultrasonic: above 20,000 Hz (e.g. bats, SONAR)",
         "The audible range narrows with age",
         "Many animals hear beyond the human range"],
        longw, img_side="right", panel_title="Infrasonic, audible, "
        "ultrasonic",
        notes="Dogs and bats hear ultrasonic frequencies; whales and "
              "elephants use infrasonic sound over long distances.")

    b.quiz_intro("Quiz 1", "Check — Speed & Range", 4)
    b.quiz_q(1, "Speed", "Sound travels fastest in:",
             ["air", "water", "steel (a solid)", "a vacuum"])
    b.quiz_a(1, "C. steel (a solid)",
             "Closely packed particles pass on the vibration quickest, so "
             "sound is fastest in solids and cannot travel in a vacuum.")
    b.quiz_q(2, "Air speed", "The speed of sound in air at ordinary room "
             "temperature is about:",
             ["34 m/s", "340 m/s", "3400 m/s", "3 × 10⁸ m/s"])
    b.quiz_a(2, "B. 340 m/s",
             "Sound travels at roughly 340 m/s in air; the exact value "
             "rises a little as temperature increases.")
    b.quiz_q(3, "Ultrasonic", "Sounds of frequency above 20,000 Hz are "
             "called:",
             ["infrasonic", "audible", "ultrasonic", "supersonic"])
    b.quiz_a(3, "C. ultrasonic",
             "Above the human audible limit of 20,000 Hz, sound is "
             "ultrasonic — used by bats and in SONAR.")
    b.quiz_q(4, "Infrasonic", "A sound of frequency 10 Hz is:",
             ["audible", "ultrasonic", "infrasonic", "supersonic"])
    b.quiz_a(4, "C. infrasonic",
             "Below 20 Hz the sound is infrasonic, beyond the lower limit "
             "of human hearing.")

    # ---- Part 2 : reflection, echo, SONAR ----
    b.divider(2, "Part 2", "Reflection of Sound and Its Uses",
              "Echo, reverberation, SONAR and sonography")

    b.bullets(
        "REFLECTION & ECHO", "Reflection of Sound and Echo",
        [("Laws of reflection", "Sound obeys the laws of reflection: "
          "angle of incidence = angle of reflection."),
         ("Echo", "An echo is a sound heard again after reflection from a "
          "distant surface."),
         ("Condition for an echo", "The reflecting surface must be far "
          "enough that the echo returns at least 0.1 s later — about "
          "17 m or more away."),
         ("Distance formula", "For an echo heard after time t, distance "
          "= (v × t) / 2.")],
        notes="0.1 s is the minimum gap the ear can separate; hence the "
              "~17 m minimum distance for a distinct echo at 340 m/s.")

    b.worked(
        "WORKED EXAMPLE", "Finding Distance from an Echo",
        "A person claps and hears the echo from a cliff after 2 s. If the "
        "speed of sound is 340 m/s, how far away is the cliff?",
        ["distance = (v × t) / 2",
         "= (340 × 2) / 2"],
        "= 340 m",
        notes="The factor of 2 is because the sound travels to the cliff "
              "and back; always halve for the one-way distance.")

    b.cards(
        "USES", "Reverberation, SONAR and Sonography",
        [("Reverberation", "Repeated reflections of sound in a closed "
          "hall make it persist; too much reverberation is reduced with "
          "soft, absorbing materials."),
         ("SONAR", "Ships send ultrasonic pulses and time the reflected "
          "echo to measure the depth of the sea or locate objects "
          "underwater."),
         ("Sonography", "Ultrasound is used in medicine to form images of "
          "internal organs and of a developing baby."),
         ("Other uses of ultrasound", "Cleaning delicate parts and "
          "detecting flaws (cracks) inside metal blocks.")],
        icons=["wave", "wave", "ear", "star"],
        notes="Reverberation is many overlapping reflections, unlike a "
              "single distinct echo — a common distinction question.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Speed", "≈ 340 m/s in air; fastest in solids, slowest in "
                 "gases."),
         ("Range", "Infrasonic < 20 Hz; audible 20–20,000 Hz; ultrasonic "
                 "> 20,000 Hz."),
         ("Echo", "Reflected sound; needs ~17 m; distance = v t / 2."),
         ("Reverberation", "Many overlapping reflections in a hall."),
         ("SONAR", "Ultrasonic echo-ranging to find depth/objects "
                 "underwater."),
         ("Sonography", "Medical imaging using ultrasound.")],
        notes="Ask students to distinguish an echo (one reflection) from "
              "reverberation (many).")

    b.quiz_intro("Quiz 2", "Final Check — Echo & Ultrasound", 4)
    b.quiz_q(1, "Echo", "An echo is heard when sound is ___ from a "
             "distant surface.",
             ["absorbed", "reflected", "refracted", "produced"])
    b.quiz_a(1, "B. reflected",
             "An echo is simply the original sound heard again after it "
             "has been reflected back.")
    b.quiz_q(2, "Echo distance", "A boy hears the echo of his shout from "
             "a wall 1 s later. If sound travels at 340 m/s, the wall "
             "is:",
             ["340 m away", "170 m away", "680 m away", "34 m away"])
    b.quiz_a(2, "B. 170 m away",
             "distance = (v × t)/2 = (340 × 1)/2 = 170 m.")
    b.quiz_q(3, "Reverberation", "The persistence of sound in a hall due "
             "to repeated reflections is called:",
             ["an echo", "reverberation", "refraction", "resonance"])
    b.quiz_a(3, "B. reverberation",
             "Many overlapping reflections make the sound linger — "
             "reverberation, reduced using sound-absorbing materials.")
    b.quiz_q(4, "SONAR", "SONAR measures the depth of the sea using:",
             ["infrasonic waves", "ultrasonic waves", "light waves", "radio "
              "waves"])
    b.quiz_a(4, "B. ultrasonic waves",
             "SONAR sends ultrasonic pulses and times their echo from the "
             "sea-bed to calculate the depth.")

    b.closing("Sound Put to Work",
              "From the echo off a cliff to the SONAR of a ship and the "
              "sonography of a hospital, the reflection of sound turns a "
              "simple wave into a powerful tool.")
    return b


# ===========================================================================
# S75 — Observing Space: Telescopes
# ===========================================================================
def telescope_deck():
    footer = "Observing Space: Telescopes  •  MSBSHSE Std 9 Science & Technology"
    b = Builder(footer, accent=C["purple"])

    refr = b.asset("mh9_tel_refr", DM.refracting_telescope("mh9_tel_refr"))
    refl = b.asset("mh9_tel_refl", DM.reflecting_telescope("mh9_tel_refl"))
    radio = b.asset("mh9_tel_radio", DM.radio_telescope("mh9_tel_radio"))

    b.title("Std 9 • Science & Technology • Astronomy",
            "Observing Space: Telescopes",
            "Observing space  •  Optical telescopes  •  Radio telescopes  "
            "•  Space telescopes and ISRO", img=refr)

    b.objectives([
        "Explain why telescopes are needed to observe space",
        "Describe the working of a refracting telescope",
        "Describe the working of a reflecting telescope",
        "Explain how a radio telescope observes space",
        "State why some telescopes are placed in space",
        "Name Indian contributions such as the GMRT and AstroSat",
    ])

    # ---- Part 1 : optical telescopes ----
    b.divider(1, "Part 1", "Optical Telescopes",
              "Seeing the universe with lenses and mirrors")

    b.bullets(
        "WHY TELESCOPES", "Observing Space",
        [("Faint and far", "Objects in space are very far away and their "
          "light is very faint."),
         ("Gather more light", "A telescope collects far more light than "
          "the eye, so faint objects become visible."),
         ("Magnify", "It also produces a larger image of a distant "
          "object."),
         ("Different forms of light", "Space objects also send radio "
          "waves, X-rays and more, so different telescopes are needed "
          "for different radiations.")],
        notes="Set up the two families coming next: optical telescopes "
              "for visible light, radio telescopes for radio waves.")

    b.text_image(
        "REFRACTING", "Refracting Telescope",
        ["Made of lenses",
         "A large objective lens gathers light from the object",
         "It forms a small real image inside the tube",
         "The eyepiece magnifies that image for the eye",
         "Bigger objective → brighter, sharper view"],
        refr, img_side="right", panel_title="Two lenses: objective + "
        "eyepiece",
        notes="The objective is made as large as possible to collect the "
              "maximum light from faint, distant objects.")

    b.text_image(
        "REFLECTING", "Reflecting Telescope",
        ["Uses a concave mirror instead of an objective lens",
         "The concave primary mirror gathers and converges the light",
         "A small secondary mirror sends it to the eyepiece",
         "Newtonian: concave + plane mirror",
         "Cassegrain: concave + convex mirror"],
        refl, img_side="left", panel_title="Mirrors gather the light",
        notes="Large mirrors are easier and cheaper to make than large "
              "lenses, so the biggest telescopes are reflectors.")

    b.quiz_intro("Quiz 1", "Check — Optical Telescopes", 4)
    b.quiz_q(1, "Purpose", "The main reason a telescope helps us see "
             "faint space objects is that it:",
             ["makes them hotter", "collects much more light than the "
              "eye", "slows the light down", "changes their colour"])
    b.quiz_a(1, "B. collects much more light than the eye",
             "A large objective lens or mirror gathers far more light "
             "than the pupil, making faint objects visible and "
             "magnified.")
    b.quiz_q(2, "Refracting", "A refracting telescope is made using:",
             ["mirrors", "lenses", "radio dishes", "prisms only"])
    b.quiz_a(2, "B. lenses",
             "A refracting telescope uses a large objective lens and a "
             "smaller eyepiece lens.")
    b.quiz_q(3, "Reflecting", "In a reflecting telescope, the light is "
             "first gathered by a:",
             ["convex lens", "concave mirror", "plane mirror", "prism"])
    b.quiz_a(3, "B. concave mirror",
             "The concave primary mirror collects and converges the "
             "light; a secondary mirror directs it to the eyepiece.")
    b.quiz_q(4, "Objective", "The objective of a telescope is made large "
             "mainly to:",
             ["magnify more", "gather the maximum light", "reduce its "
              "cost", "make it lighter"])
    b.quiz_a(4, "B. gather the maximum light",
             "A larger objective collects more light from faint, distant "
             "objects, giving a brighter and clearer image.")

    # ---- Part 2 : radio & space telescopes ----
    b.divider(2, "Part 2", "Radio and Space Telescopes",
              "Beyond visible light, and above the atmosphere")

    b.text_image(
        "RADIO", "Radio Telescope",
        ["Many space objects emit radio waves, not just light",
         "A large parabolic dish reflects the radio waves",
         "They converge to a receiver at the focus",
         "A computer builds an image from the signal",
         "India's GMRT (near Pune) is one of the largest"],
        radio, img_side="right", panel_title="Listening to the "
        "universe",
        notes="The GMRT (Giant Metrewave Radio Telescope) at Narayangaon "
              "near Pune is a major Indian radio-astronomy facility.")

    b.bullets(
        "SPACE TELESCOPES", "Telescopes in Space and Indian Missions",
        [("Why go to space", "The atmosphere blurs and absorbs light, so "
          "telescopes placed in space give much clearer views."),
         ("Above the air", "Space telescopes also observe X-rays and "
          "ultraviolet rays that the atmosphere blocks."),
         ("AstroSat", "India's AstroSat is a space observatory that "
          "studies the sky in several kinds of radiation at once."),
         ("ISRO", "The Indian Space Research Organisation builds and "
          "launches these observatories and satellites.")],
        notes="Link back to the different forms of light: some radiations "
              "can only be observed from above the atmosphere.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Why telescopes", "Gather more light and magnify faint, distant "
                          "objects."),
         ("Refracting", "Objective lens + eyepiece lens."),
         ("Reflecting", "Concave primary mirror + secondary mirror "
                      "(Newtonian, Cassegrain)."),
         ("Radio telescope", "Parabolic dish focuses radio waves onto a "
                           "receiver; GMRT near Pune."),
         ("Space telescopes", "Placed above the atmosphere for clearer "
                           "views; India's AstroSat.")],
        notes="Cold-call the difference between a refracting and a "
              "reflecting telescope, and one Indian facility.")

    b.quiz_intro("Quiz 2", "Final Check — Radio & Space", 4)
    b.quiz_q(1, "Radio telescope", "A radio telescope collects radio "
             "waves using a large:",
             ["convex lens", "parabolic dish", "concave lens", "prism"])
    b.quiz_a(1, "B. parabolic dish",
             "The dish reflects the incoming radio waves to a receiver at "
             "its focus, where a computer builds an image.")
    b.quiz_q(2, "GMRT", "The Giant Metrewave Radio Telescope (GMRT) is "
             "located near:",
             ["Bengaluru", "Pune", "Chennai", "Delhi"])
    b.quiz_a(2, "B. Pune",
             "The GMRT, one of the world's largest radio telescopes, is "
             "at Narayangaon near Pune.")
    b.quiz_q(3, "Space telescope", "Telescopes are placed in space mainly "
             "because:",
             ["space is closer to the stars", "the atmosphere blurs and "
              "absorbs light", "it is cheaper", "there is no gravity"])
    b.quiz_a(3, "B. the atmosphere blurs and absorbs light",
             "Above the atmosphere the view is much clearer, and "
             "radiations that the air blocks can also be observed.")
    b.quiz_q(4, "AstroSat", "India's dedicated space observatory that "
             "studies several radiations at once is:",
             ["Chandrayaan", "AstroSat", "Mangalyaan", "GMRT"])
    b.quiz_a(4, "B. AstroSat",
             "AstroSat is India's multi-wavelength space observatory, "
             "launched by ISRO.")

    b.closing("Windows on the Universe",
              "Lenses, mirrors and giant dishes — on the ground and in "
              "space — let us gather faint light and radio waves from "
              "across the cosmos.")
    return b


if __name__ == "__main__":
    build()
