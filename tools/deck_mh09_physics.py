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

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "MH_Grade09"))
os.makedirs(OUT, exist_ok=True)


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
