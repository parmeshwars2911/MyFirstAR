"""
Grade 8 Physics — Chapter: Electricity.
S71 (static electricity: charge, charging by friction, types & interaction
of charges, transfer of charge, electroscope, lightning) and
S72 (practical electricity: cells & circuits, dangers, wire colour codes,
earthing, fuse, household circuit, electric meter & the unit of energy).
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
FOOTER = "Electricity  •  ICSE Class 8 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["purple"])
    elec = b.asset("g8el_electroscope",
                   D.gold_leaf_electroscope("g8el_electroscope"))
    charges = b.asset("g8el_charges", D.charge_interaction("g8el_charges"))
    hero = b.asset("g8_static_hero", charges)

    b.title("ICSE • Class 8 • Electricity", "Static Electricity",
            "Electric charge  •  Charging by friction  •  Two kinds of charge  "
            "•  Lightning", img=hero)
    b.objectives([
        "Explain what electric charge is in terms of electrons",
        "Describe how a body is charged by friction",
        "State the two kinds of charge and how they interact",
        "Distinguish conductors from insulators",
        "Describe an electroscope and how it detects charge",
        "Explain lightning and simple lightning safety",
    ])
    b.divider(1, "Part 1", "Electric Charge",
              "Where charge comes from and how it behaves")
    b.statement("WHAT IS CHARGE", "Electric Charge",
                "Every atom contains positive protons and negative electrons. "
                "Charge appears when a body gains or loses electrons.",
                points=["Equal protons and electrons → the body is neutral "
                        "(uncharged).",
                        "Lose electrons → fewer negatives → positively "
                        "charged.",
                        "Gain electrons → extra negatives → negatively "
                        "charged."],
                notes="Charge is about electrons. Neutral = balanced. Losing "
                      "electrons leaves a positive body; gaining them makes it "
                      "negative. Only electrons move, not protons.")
    b.cards("BY FRICTION", "Charging by Friction", [
        ("Rubbing", "Rubbing two suitable materials transfers electrons from "
         "one to the other."),
        ("Glass & silk", "Glass rubbed with silk loses electrons and becomes "
         "positively charged."),
        ("Ebonite & fur", "Ebonite rubbed with fur gains electrons and becomes "
         "negatively charged."),
        ("Comb in hair", "A comb run through dry hair picks up electrons and "
         "can then lift bits of paper."),
    ], notes="Charging by friction transfers electrons between materials. "
             "Standard examples: glass+silk (positive), ebonite+fur "
             "(negative), comb in hair.")
    b.text_image("TWO KINDS", "Two Kinds of Charge and How They Interact",
                 ["There are just two kinds of charge: positive and "
                  "negative.",
                  "Two like charges (both + or both –) push each other apart.",
                  "Two unlike charges (+ and –) pull each other together.",
                  "A charged body can also attract a light, uncharged object "
                  "for a short while."],
                 charges, img_side="right", img_w=6.0, img_h=3.2,
                 panel_title="Like repel, unlike attract",
                 caption="The basic rule of charges",
                 notes="The fundamental rule: like charges repel, unlike "
                       "attract. A charged body can also attract a neutral "
                       "object by inducing opposite charge.")
    b.bullets("CONDUCTORS", "Conductors and Insulators", [
        ("Conductors", "Materials that let charge flow through them — metals, "
         "the human body, the earth."),
        ("Insulators", "Materials that do not let charge flow — plastic, "
         "rubber, glass, dry wood."),
        ("Why", "Conductors have free electrons; insulators hold their "
         "electrons tightly."),
        ("Use", "Wires use copper to carry charge and plastic to keep it "
         "safely inside."),
    ], panel_title="Letting charge move or not",
       notes="Conductors (free electrons: metals) vs insulators (tightly held: "
             "plastic, rubber). A wire combines both — copper core, plastic "
             "sheath.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Comb Trick", "A plastic comb rubbed on dry hair picks up tiny "
             "bits of paper because rubbing has made the comb:",
             ["Hotter", "Electrically charged", "Magnetic", "Wet"])
    b.quiz_a(1, "B. Electrically charged",
             "Rubbing transfers electrons to the comb, giving it a charge. The "
             "charged comb then attracts the light, uncharged paper bits — a "
             "static-electricity effect, not magnetism.")
    b.quiz_q(2, "Lost Electrons", "A glass rod rubbed with silk loses some "
             "electrons. The rod therefore becomes:", ["Negatively charged",
              "Positively charged", "Neutral", "A conductor"])
    b.quiz_a(2, "B. Positively charged",
             "Losing electrons leaves the rod with more protons than electrons, "
             "so it carries a net positive charge. The silk, which gains those "
             "electrons, becomes negative.")
    b.quiz_q(3, "Two Balloons", "Two balloons rubbed on the same wool both "
             "gain the same kind of charge. Brought near each other they will:",
             ["Attract", "Repel", "Do nothing", "Stick together"])
    b.quiz_a(3, "B. Repel",
             "Rubbed on the same material, both balloons carry like charges. "
             "Like charges repel, so the balloons push apart when brought "
             "close.")
    b.quiz_q(4, "Safe Wire", "A copper wire is given a plastic covering "
             "because copper is a good conductor and plastic is a good:",
             ["Conductor", "Insulator", "Magnet", "Fuel"])
    b.quiz_a(4, "B. Insulator",
             "The copper core carries the charge, while the plastic sheath is "
             "an insulator that stops the charge escaping and keeps us safe "
             "from shocks.")
    b.divider(2, "Part 2", "Detecting Charge & Lightning",
              "The electroscope and electricity in the sky")
    b.text_image("ELECTROSCOPE", "The Gold-Leaf Electroscope",
                 ["An electroscope detects whether a body is charged.",
                  "It has a metal disc and rod ending in two thin gold "
                  "leaves.",
                  "Touch it with a charged body and the leaves gain like "
                  "charge.",
                  "Like charges repel, so the leaves diverge — the more "
                  "charge, the wider they spread."],
                 elec, img_side="right", img_w=5.4, img_h=3.4,
                 panel_title="Leaves diverge when charged",
                 caption="Diverging leaves reveal a charge",
                 notes="Electroscope detects charge. Charge spreads to the gold "
                       "leaves; like charges repel so they diverge. Wider "
                       "divergence = more charge.")
    b.cards("TRANSFER", "Transferring Charge", [
        ("By contact", "Touching a charged body to a conductor shares the "
         "charge between them."),
        ("By earthing", "Connecting a charged conductor to the earth lets its "
         "charge flow away."),
        ("The earth", "The earth is a huge conductor that can give or take "
         "almost any amount of charge."),
        ("Why it matters", "Earthing safely removes unwanted static charge "
         "from a body."),
    ], notes="Charge can be shared by contact and removed by earthing. The "
             "earth acts as an unlimited reservoir of charge.")
    b.statement("LIGHTNING", "Lightning",
                "Lightning is a giant spark of static electricity. Charges "
                "build up in storm clouds until they jump suddenly to another "
                "cloud or to the ground.",
                points=["Rising air rubs water and ice, charging the cloud.",
                        "When the charge is large enough it leaps as a brilliant "
                        "flash.",
                        "The flash heats the air, which expands and bangs as "
                        "thunder."],
                notes="Lightning = large-scale static discharge. Cloud charges "
                      "build, then jump as a spark. Thunder is the sound of the "
                      "suddenly heated air.")
    b.cards("STAY SAFE", "Lightning Safety", [
        ("Get indoors", "A building or a car is far safer than open ground."),
        ("Avoid tall, lone objects", "Do not shelter under a single tall tree "
         "in a field."),
        ("Lightning conductor", "A metal rod on a building guides the charge "
         "safely to the earth."),
        ("Keep low", "In the open, crouch low and keep away from water and "
         "metal."),
    ], notes="Lightning safety: shelter indoors/in a car, avoid lone tall "
             "objects, lightning conductors protect buildings.")
    b.cards("ALL AROUND US", "Static Electricity Around Us", [
        ("Crackling clothes", "Synthetic clothes rub and charge up, crackling "
         "and sparking as you undress."),
        ("Clinging wrap", "Charged plastic wrap clings to a bowl because of "
         "attraction to opposite charge."),
        ("Dusty screens", "A charged TV or computer screen pulls fine dust "
         "particles onto it."),
        ("A shock from a doorknob", "Charge picked up while walking jumps as a "
         "tiny spark when you touch metal."),
    ], notes="Everyday static effects: crackling clothes, clinging wrap, dusty "
             "screens, doorknob sparks. Relates the topic to daily life.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Charge", "from gaining or losing electrons"),
        ("Friction", "rubbing transfers electrons between materials"),
        ("Two kinds", "like charges repel, unlike attract"),
        ("Conductors", "let charge flow; insulators do not"),
        ("Electroscope", "diverging leaves reveal a charge"),
        ("Lightning", "a huge static spark; shelter and use conductors"),
    ], notes="Rapid recap of charge, friction, the two-charge rule, conductors, "
             "the electroscope and lightning.")
    b.quiz_intro("Quiz 2", "Final Check — Static Electricity", 5)
    b.quiz_q(1, "Wider Leaves", "When a more strongly charged rod touches an "
             "electroscope, its gold leaves diverge more widely. This is "
             "because the leaves now carry:", ["Opposite charges that attract",
              "More like charge, so they repel harder", "No charge", "Heat"])
    b.quiz_a(1, "B. More like charge, so they repel harder",
             "The extra charge spreads onto both leaves, which then carry the "
             "same kind of charge. Greater like charge means a stronger "
             "repulsion, so the leaves spread further apart.")
    b.quiz_q(2, "Thunder Sound", "We hear thunder after a lightning flash "
             "because the flash suddenly:", ["Cools the air",
              "Heats the air, which expands and makes a loud sound",
              "Freezes the cloud", "Stops the wind"])
    b.quiz_a(2, "B. Heats the air, which expands and makes a sound",
             "The lightning spark heats the surrounding air violently. The air "
             "expands with a sharp bang we hear as thunder. We see the flash "
             "first because light travels faster than sound.")
    b.quiz_q(3, "Earthing", "Connecting a charged metal sphere to the ground "
             "with a wire makes it lose its charge because the earth:",
             ["Is an insulator", "Is a huge conductor that absorbs the charge",
              "Is positively charged", "Heats the sphere"])
    b.quiz_a(3, "B. Is a huge conductor that absorbs the charge",
             "The earth is an enormous conductor. A wire lets the sphere's "
             "excess charge flow away into the ground, leaving the sphere "
             "neutral — this is earthing.")
    b.quiz_q(4, "Attracting Paper", "A charged rod attracts tiny uncharged "
             "paper bits. The rod can do this because it:",
             ["Is magnetic", "Induces an opposite charge on the nearby paper",
              "Is hot", "Is heavy"])
    b.quiz_a(4, "B. Induces an opposite charge on the nearby paper",
             "The charged rod pulls opposite charge to the near side of each "
             "paper bit. Since unlike charges attract and the opposite charge "
             "is closer, the light paper is drawn to the rod.")
    b.quiz_q(5, "Lightning Conductor", "A metal lightning conductor on a tall "
             "building protects it by:", ["Attracting clouds",
              "Carrying the lightning's charge safely to the earth",
              "Making thunder louder", "Storing the charge"])
    b.quiz_a(5, "B. Carrying the lightning's charge safely to the earth",
             "The conductor offers an easy metal path from the highest point "
             "of the building down to the ground, so the lightning's charge "
             "flows harmlessly to earth instead of damaging the building.")
    b.closing("Charge in Action",
              "From a crackling comb to a bolt of lightning, static "
              "electricity is simply electrons on the move — and balanced "
              "again.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["teal"])
    plug = b.asset("g8el_plug", D.three_pin_plug("g8el_plug"))
    circ = b.asset("g8el_circuit", D.simple_circuit("g8el_circuit"))
    hero = b.asset("g8_current_hero", circ)

    b.title("ICSE • Class 8 • Electricity", "Electricity in the Home",
            "Cells & circuits  •  Wire colour codes  •  Earthing & fuse  •  "
            "The electricity meter", img=hero)
    b.objectives([
        "Describe a cell and a simple electric circuit",
        "State the dangers of electricity",
        "Give the colour code of the wires in a cable",
        "Explain the purpose of earthing and of a fuse",
        "Describe a simple household circuit",
        "Explain the unit in which electrical energy is sold",
    ])
    b.divider(1, "Part 1", "Cells, Circuits & Safety",
              "Making a current flow and using it safely")
    b.text_image("CIRCUITS", "Cells and Circuits",
                 ["A cell pushes electric charge around a circuit.",
                  "A circuit is a closed path of conductors for the current.",
                  "Current flows only when the path is complete and the switch "
                  "is on.",
                  "A switch simply makes or breaks the path to turn things on "
                  "or off."],
                 circ, img_side="right", img_w=6.0, img_h=3.2,
                 panel_title="A complete path",
                 caption="Cell, switch and bulb in a closed loop",
                 notes="A cell drives current; a circuit is a closed conducting "
                       "path. Current flows only when the loop is complete. The "
                       "switch makes/breaks the path.")
    b.cards("DANGERS", "The Dangers of Electricity", [
        ("Electric shock", "A current through the body can injure or even "
         "kill."),
        ("Overheating", "Too much current heats wires and can start a fire."),
        ("Damaged wires", "Bare or frayed wires expose live conductors."),
        ("Water", "Wet hands or floors make shocks far more likely — water "
         "conducts."),
    ], notes="Main dangers: shock, fire from overheating, exposed wires, and "
             "water. These motivate the safety devices that follow.")
    b.bullets("COLOUR CODE", "The Colour Code of Wires", [
        ("Live wire", "Brown (older cables red) — carries the dangerous "
         "current to the appliance."),
        ("Neutral wire", "Blue (older cables black) — completes the circuit "
         "back to the supply."),
        ("Earth wire", "Green-and-yellow — a safety wire connected to the "
         "earth."),
        ("Why it matters", "Correct colours make sure each wire is connected "
         "to the right pin."),
    ], panel_title="Live, neutral and earth",
       notes="Three-wire colour code: live (brown/red), neutral (blue/black), "
             "earth (green-yellow). Correct wiring is a safety essential.")
    b.text_image("THREE-PIN PLUG", "The Three-Pin Plug and Earthing",
                 ["A three-pin plug connects an appliance to the mains "
                  "safely.",
                  "The longest, thickest pin is the earth pin.",
                  "Earthing connects the metal body of an appliance to the "
                  "ground.",
                  "If a fault makes the body live, the current escapes to "
                  "earth instead of through us."],
                 plug, img_side="right", img_w=5.6, img_h=3.4,
                 panel_title="The earth pin protects you",
                 caption="Live, neutral and earth pins",
                 notes="Three-pin plug: the long top pin is earth. Earthing "
                       "sends fault current safely to ground, protecting the "
                       "user from a shock via a metal body.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "No Light", "A torch bulb will not light even though the cell "
             "is good. The most likely reason is that the circuit is:",
             ["Too short", "Broken somewhere, so the path is open", "Too "
              "cold", "Earthed"])
    b.quiz_a(1, "B. Broken somewhere, so the path is open",
             "Current flows only around a complete, closed loop. A loose "
             "connection or open switch breaks the path, so no current reaches "
             "the bulb and it stays dark.")
    b.quiz_q(2, "Green-Yellow", "In a modern cable, the wire coloured green and "
             "yellow is the:", ["Live wire", "Neutral wire", "Earth wire",
              "Heating wire"])
    b.quiz_a(2, "C. Earth wire",
             "Green-and-yellow always marks the earth wire — the safety wire "
             "that carries fault current to the ground. Brown is live and blue "
             "is neutral.")
    b.quiz_q(3, "Wet Hands", "Touching a switch with wet hands is dangerous "
             "because water:", ["Is an insulator", "Conducts electricity, "
              "making a shock more likely", "Cools the wire", "Stops the "
              "current"])
    b.quiz_a(3, "B. Conducts electricity, making a shock more likely",
             "Water is a conductor, so wet skin lets current pass through the "
             "body much more easily. That is why we must keep electrical "
             "switches and appliances away from water.")
    b.quiz_q(4, "Earth Pin Job", "The earth pin of a three-pin plug protects "
             "us by:", ["Carrying the normal current",
              "Sending fault current from the metal body safely to the ground",
              "Lighting a bulb", "Saving energy"])
    b.quiz_a(4, "B. Sending fault current safely to the ground",
             "If a fault makes an appliance's metal body live, the earth wire "
             "gives that current an easy path to the ground. It flows to earth "
             "instead of through anyone who touches the body.")
    b.divider(2, "Part 2", "Household Circuit & Energy",
              "Fuses, the meter and the unit of energy")
    b.statement("THE FUSE", "The Fuse",
                "A fuse is a short piece of thin wire that melts and breaks the "
                "circuit if the current grows dangerously large.",
                points=["It is joined in the live wire of a circuit.",
                        "A large fault current heats the thin wire until it "
                        "melts.",
                        "The broken circuit cuts off the supply, preventing "
                        "fire."],
                notes="The fuse is a deliberate weak link in the live wire. "
                      "Excess current melts it, breaking the circuit and "
                      "preventing overheating and fire.")
    b.cards("HOUSEHOLD CIRCUIT", "A Simple Household Circuit", [
        ("From the meter", "Supply enters the house through the electricity "
         "meter and a main fuse."),
        ("Parallel connection", "Lights and sockets are joined in parallel, so "
         "each works on its own."),
        ("Switches in the live", "Switches are placed in the live wire to make "
         "appliances safe when off."),
        ("Each circuit fused", "Separate circuits for lights and power each "
         "have their own fuse."),
    ], notes="Household wiring: meter + main fuse, appliances in parallel, "
             "switches in the live wire, separate fused circuits.")
    b.statement("UNIT OF ENERGY", "Measuring Electrical Energy",
                "An electricity meter records how much electrical energy a home "
                "uses, measured in kilowatt-hours (kWh).",
                formula="1 unit = 1 kilowatt-hour (kWh) = energy used by a "
                        "1 kW appliance in 1 hour",
                points=["The meter counts the units used over time.",
                        "The electricity bill charges for these units.",
                        "Using fewer, more efficient appliances lowers the "
                        "bill."],
                notes="Commercial unit of electrical energy = kilowatt-hour "
                      "(kWh). The meter records units; the bill charges per "
                      "unit. 1 kWh = a 1 kW device for 1 hour.")
    b.bullets("FUSE vs MCB", "The Fuse and Its Modern Cousin", [
        ("Rating", "A fuse is marked with a safe current, such as 5 A or "
         "15 A."),
        ("Right value", "A lighting circuit uses a low-rated fuse; a heater "
         "needs a higher one."),
        ("After it blows", "A blown fuse wire must be replaced before the "
         "circuit works again."),
        ("Circuit breaker (MCB)", "A switch that trips on a large current and "
         "can simply be switched back on."),
    ], panel_title="Choosing the right protection",
       notes="Fuses are rated in amperes; pick the right value for the "
             "circuit. Modern homes use MCBs (resettable circuit breakers) in "
             "place of fuse wire.")
    b.cards("BE SAFE", "Precautions While Using Electricity", [
        ("Dry hands", "Never touch switches or plugs with wet hands."),
        ("Good wiring", "Replace frayed wires and use correctly rated fuses."),
        ("Don't overload", "Avoid plugging many appliances into one socket."),
        ("Earth appliances", "Use three-pin plugs so metal-bodied appliances "
         "are earthed."),
    ], notes="Everyday safety precautions: dry hands, sound wiring, correct "
             "fuses, no overloading, proper earthing.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Circuit", "current flows in a complete, switched path"),
        ("Dangers", "shock, fire, bare wires, water"),
        ("Colour code", "live brown, neutral blue, earth green-yellow"),
        ("Earthing", "fault current goes safely to the ground"),
        ("Fuse", "thin wire melts to break a dangerous current"),
        ("Energy unit", "the kilowatt-hour (kWh) — the billed unit"),
    ], notes="Rapid recap of circuits, dangers, colour codes, earthing, the "
             "fuse and the kilowatt-hour.")
    b.quiz_intro("Quiz 2", "Final Check — Electricity at Home", 5)
    b.quiz_q(1, "Why a Fuse Melts", "A fuse protects a circuit by melting when "
             "the current is too large. It is therefore connected:",
             ["In the earth wire", "In the live wire", "Across the bulb",
              "Outside the house"])
    b.quiz_a(1, "B. In the live wire",
             "The fuse is placed in the live wire so that, when it melts, it "
             "cuts off the dangerous live supply to the whole circuit, stopping "
             "the excess current and preventing a fire.")
    b.quiz_q(2, "One Unit", "One 'unit' on an electricity bill is the energy "
             "used by a 1 kilowatt appliance running for:", ["One minute",
              "One hour", "One day", "One second"])
    b.quiz_a(2, "B. One hour",
             "One unit is one kilowatt-hour: the energy a 1 kW appliance uses "
             "in 1 hour. The meter counts these units and the bill charges for "
             "them.")
    b.quiz_q(3, "Parallel Homes", "House lights are wired in parallel so "
             "that:", ["They share one switch", "Each can be switched on or "
              "off on its own", "They use less wire", "They glow dimmer"])
    b.quiz_a(3, "B. Each can be switched on or off on its own",
             "In parallel, every light gets the full supply voltage and has its "
             "own path. So one lamp can be switched off without affecting the "
             "others — unlike a series chain.")
    b.quiz_q(4, "Overloaded Socket", "Plugging many high-power appliances into "
             "one socket is dangerous because it draws a large current that "
             "can:", ["Cool the wires", "Overheat the wiring and start a "
              "fire", "Save energy", "Stop the meter"])
    b.quiz_a(4, "B. Overheat the wiring and start a fire",
             "Each appliance adds to the current in the same wire. A very large "
             "current heats the wiring beyond its safe limit, which can melt "
             "insulation and start a fire — so we avoid overloading.")
    b.quiz_q(5, "Metal Body", "An earthed metal-bodied appliance is safer "
             "because, if a live wire touches the body, the current will:",
             ["Stay in the body", "Flow harmlessly to earth through the earth "
              "wire", "Light a bulb", "Increase the bill"])
    b.quiz_a(5, "B. Flow harmlessly to earth through the earth wire",
             "The earth wire connects the body to the ground. A fault current "
             "takes this easy path to earth rather than passing through a "
             "person who touches the appliance, preventing a shock.")
    b.closing("Power Used Wisely",
              "From a single cell to the wiring of a whole house, electricity "
              "serves us best when it is understood — and treated with "
              "respect.")
    return b


def build():
    for fname, fn in [("G8_S71_Electricity_1.pptx", deck1),
                      ("G8_S72_Electricity_2.pptx", deck2)]:
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
