"""
Grade 9 Physics — Chapter: Magnetism.
S122 (induced magnetism, magnetic field lines & properties, Earth's field) and
S123 (plotting a bar magnet's field, neutral points, electromagnets vs
permanent magnets, uses).  ICSE Class 9 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Magnetism  •  ICSE Class 9 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    bar = b.asset("g9mg_bar", D.bar_magnet_field("g9mg_bar"))
    hero = b.asset("g9_magnet_hero", bar)

    b.title("ICSE • Class 9 • Magnetism", "Magnetic Fields",
            "Magnets & induced magnetism  •  Magnetic field lines  •  "
            "Properties  •  The Earth's field", img=hero)
    b.objectives([
        "Recall the basic properties of magnets",
        "Explain induced magnetism",
        "Describe magnetic field lines",
        "State the properties of magnetic field lines",
        "Describe the Earth's magnetic field",
        "Plot the uniform field lines of the Earth",
    ])
    b.divider(1, "Part 1", "Magnets & Induced Magnetism",
              "Poles, forces and how magnetism is induced")
    b.cards("BASICS", "Basic Properties of Magnets", [
        ("Two poles", "Every magnet has a north and a south pole."),
        ("Poles in pairs", "Poles always occur in pairs — you cannot get a "
         "single pole."),
        ("Attraction & repulsion", "Like poles repel; unlike poles attract."),
        ("Directive property", "A freely suspended magnet sets itself north–"
         "south."),
    ], notes="Recap the fundamental magnet properties. The directive property "
             "(points N–S) leads to the compass and Earth's field.")
    b.cards("MATERIALS", "Magnetic and Non-Magnetic Materials", [
        ("Magnetic materials", "Attracted by a magnet — iron, cobalt, nickel "
         "and steel."),
        ("Non-magnetic", "Not attracted — wood, plastic, copper, glass and "
         "aluminium."),
        ("Soft magnetic", "Soft iron magnetises and demagnetises easily — "
         "used in electromagnets."),
        ("Hard magnetic", "Steel keeps its magnetism — used for permanent "
         "magnets."),
    ], notes="Sort materials into magnetic vs non-magnetic, and soft (iron) "
             "vs hard (steel) magnetic materials.")
    b.bullets("INDUCED MAGNETISM", "Induced Magnetism", [
        ("What it is", "A magnetic material becomes a magnet when placed near "
         "a magnet, without touching it."),
        ("Temporary", "Soft iron loses this induced magnetism as soon as the "
         "magnet is removed."),
        ("Nearer pole", "The induced pole nearest the magnet is always "
         "opposite to it, so attraction results."),
        ("Why iron sticks", "Pins cling to a magnet because each becomes a "
         "tiny induced magnet."),
    ], panel_title="Magnetism without contact",
       notes="Induced magnetism explains why unmagnetised iron is attracted: "
             "it temporarily becomes a magnet with an opposite near-pole.")
    b.bullets("MOLECULAR THEORY", "The Molecular Theory of Magnetism", [
        ("Tiny molecular magnets", "Every molecule of a magnetic material is "
         "itself a tiny magnet."),
        ("Unmagnetised", "Normally these point in all directions, so their "
         "effects cancel out."),
        ("Magnetised", "In a magnet they line up the same way, adding together "
         "to give net poles."),
        ("It explains", "Why breaking a magnet gives two magnets, and why "
         "heating or hammering (jumbling them) demagnetises it."),
    ], panel_title="Magnets made of tiny magnets",
       notes="The molecular/domain theory: aligned molecular magnets give "
             "magnetism. Explains induced magnetism, breaking, and "
             "demagnetisation by heat/hammering.")
    b.text_image("FIELD LINES", "Magnetic Field Lines",
                 ["A magnetic field is the region around a magnet where its "
                  "force can be felt.",
                  "We picture it using magnetic field lines.",
                  "Outside the magnet, the lines run from the North pole to "
                  "the South pole.",
                  "Where the lines are crowded the field is strong; where they "
                  "are spread out it is weak."],
                 bar, img_side="right", img_w=5.6, img_h=4.0,
                 panel_title="Picturing the field",
                 caption="Lines run from N to S outside the magnet",
                 notes="Field lines visualise the field. Direction N→S outside; "
                       "spacing shows strength.")
    b.cards("PROPERTIES", "Properties of Magnetic Field Lines", [
        ("Direction", "Run from North to South outside, and South to North "
         "inside the magnet."),
        ("Never cross", "Two field lines never intersect."),
        ("Closed loops", "Each line is a continuous closed loop."),
        ("Spacing = strength", "Closer lines mean a stronger field; they are "
         "densest at the poles."),
    ], notes="The four standard properties. 'Never cross' and 'closed loops' "
             "are commonly asked.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Sure Test", "The surest test that a bar of steel is a magnet "
             "is that it:", ["Attracts iron", "Repels one end of a known "
              "magnet", "Is shiny", "Is heavy"])
    b.quiz_a(1, "B. Repels one end of a known magnet",
             "Attraction can happen with ordinary iron too (by induction). "
             "Only a magnet can REPEL another magnet, so repulsion is the sure "
             "test of magnetism.")
    b.quiz_q(2, "Pin on a Magnet", "An iron pin clings to a magnet and a "
             "second pin then clings to the first. This shows:",
             ["The pins are already magnets", "Induced magnetism — each pin "
              "becomes a temporary magnet", "The magnet is losing strength",
              "The pins are glued"])
    b.quiz_a(2, "B. Induced magnetism",
             "The magnet induces magnetism in the first pin, which in turn "
             "induces it in the second. Each becomes a temporary magnet, so "
             "they cling in a chain.")
    b.quiz_q(3, "Field Lines Cross?", "Two magnetic field lines can never "
             "cross because at the crossing point the field would have:",
             ["Zero strength", "Two directions at once, which is impossible",
              "Too many poles", "Infinite strength"])
    b.quiz_a(3, "B. Two directions at once",
             "A field line shows the field's direction at each point. If two "
             "crossed, the field would point two ways at once there — "
             "impossible — so lines never intersect.")
    b.quiz_q(4, "Strongest Field", "On a field-line diagram, the magnetic "
             "field is strongest where the lines are:", ["Furthest apart",
              "Closest together", "Straight", "Coloured"])
    b.quiz_a(4, "B. Closest together",
             "Crowded (closely spaced) field lines indicate a strong field. "
             "That is why the lines bunch up at the poles, where the field is "
             "strongest.")
    b.quiz_q(5, "Not Magnetic", "Which of these materials is NOT attracted by "
             "a magnet?", ["Iron", "Cobalt", "Nickel", "Copper"])
    b.quiz_a(5, "D. Copper",
             "Iron, cobalt and nickel are magnetic materials, attracted by a "
             "magnet. Copper, like wood and plastic, is non-magnetic and is "
             "not attracted.")
    b.divider(2, "Part 2", "The Earth's Magnetic Field",
              "Why a compass points north")
    b.bullets("EARTH'S FIELD", "The Earth as a Magnet", [
        ("A giant magnet", "The Earth behaves as if it has a huge bar magnet "
         "inside it."),
        ("Compass points north", "A freely suspended magnet (compass) aligns "
         "with the Earth's field, pointing north–south."),
        ("Poles are opposite", "The Earth's magnetic south pole lies near the "
         "geographic North — which is why a compass north is attracted to "
         "it."),
        ("Uses", "Compasses guide ships, aircraft and hikers."),
    ], panel_title="A planet-sized bar magnet",
       notes="The Earth acts like a bar magnet; the compass aligns with its "
             "field. Note the magnetic-geographic pole swap.")
    b.statement("UNIFORM FIELD", "Plotting the Earth's Uniform Field",
                "Over a small area, the Earth's magnetic field is nearly "
                "uniform — the same strength and direction everywhere.",
                points=["Plot it with a compass on paper, marking the needle "
                        "direction at many points.",
                        "The field lines come out parallel and equally "
                        "spaced.",
                        "Parallel, evenly spaced lines are the signature of a "
                        "uniform field."],
                notes="A uniform field = parallel, evenly spaced lines. The "
                      "Earth's field is uniform over a small region.")
    b.cards("MAGNETIC vs GEOGRAPHIC", "Two Kinds of North", [
        ("Geographic north", "The direction of the Earth's axis (true "
         "north)."),
        ("Magnetic north", "The direction a compass needle points."),
        ("Declination", "The small angle between them at a place."),
        ("They differ", "Magnetic north and true north are not exactly the "
         "same direction."),
    ], notes="Distinguish geographic (true) north from magnetic north; the "
             "angle between is the declination.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Magnet basics", "two poles; like repel, unlike attract; points N–S"),
        ("Induced magnetism", "iron becomes a temporary magnet near a magnet"),
        ("Field lines", "run N→S outside; show field direction and strength"),
        ("Properties", "never cross; closed loops; closest at the poles"),
        ("Earth's field", "Earth acts like a bar magnet; compass aligns N–S"),
        ("Uniform field", "parallel, equally spaced lines"),
    ], notes="Rapid recap; field-line properties and the Earth's field are the "
             "key points.")
    b.quiz_intro("Quiz 2", "Final Check — Fields & the Earth", 5)
    b.quiz_q(1, "Compass Needle", "A compass needle points north because it:",
             ["Is attracted to the Sun", "Aligns itself with the Earth's "
              "magnetic field", "Is heavier at one end", "Repels all metals"])
    b.quiz_a(1, "B. Aligns with the Earth's magnetic field",
             "The compass needle is a tiny magnet free to turn. It lines up "
             "with the Earth's magnetic field, coming to rest pointing north–"
             "south.")
    b.quiz_q(2, "Uniform Field", "Parallel, equally spaced magnetic field "
             "lines represent a field that is:", ["Getting stronger",
              "Uniform (same everywhere)", "Zero", "Circular"])
    b.quiz_a(2, "B. Uniform (same everywhere)",
             "When field lines are parallel and evenly spaced, the field has "
             "the same strength and direction at every point — a uniform "
             "field, like the Earth's over a small area.")
    b.quiz_q(3, "Single Pole?", "Breaking a bar magnet in half produces:",
             ["One N pole and one S pole separately", "Two complete magnets, "
              "each with N and S poles", "A magnet with no poles",
              "A non-magnet"])
    b.quiz_a(3, "B. Two complete magnets, each with both poles",
             "Poles always exist in pairs. Cutting a magnet simply makes two "
             "smaller magnets, each with its own north and south pole — you "
             "can never isolate a single pole.")
    b.quiz_q(4, "Inside the Magnet", "Inside a bar magnet, the field lines run "
             "from:", ["North to South", "South to North",
              "They stop at the surface", "In circles"])
    b.quiz_a(4, "B. South to North",
             "Field lines are closed loops. Outside the magnet they go N→S, "
             "and inside the magnet they continue from S→N to complete each "
             "loop.")
    b.quiz_q(5, "Two Norths", "The angle between the geographic north and the "
             "magnetic north at a place is called the:", ["Latitude",
              "Magnetic declination", "Longitude", "Field strength"])
    b.quiz_a(5, "B. Magnetic declination",
             "Declination is the small angle between true (geographic) north "
             "and the direction a compass points (magnetic north) at a given "
             "place.")
    b.closing("Fields All Around",
              "From a fridge magnet to the whole planet, invisible magnetic "
              "fields shape the space around every magnet.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    bar = b.asset("g9mg_bar2", D.bar_magnet_field("g9mg_bar2"))
    neut = b.asset("g9mg_neutral", D.neutral_points("g9mg_neutral"))
    sol = b.asset("g9mg_sol", D.solenoid_field("g9mg_sol"))
    hero = b.asset("g9_compass_hero", neut)

    b.title("ICSE • Class 9 • Magnetism", "Plotting Fields & Electromagnets",
            "Plotting a magnet's field  •  Neutral points  •  Electromagnets  "
            "•  Uses", img=hero)
    b.objectives([
        "Plot the non-uniform field of a strong bar magnet",
        "Explain what a neutral point is",
        "Describe an electromagnet",
        "Compare an electromagnet with a permanent magnet",
        "State the advantages of an electromagnet",
        "List the uses of electromagnets",
    ])
    b.divider(1, "Part 1", "Plotting Fields & Neutral Points",
              "Mapping a magnet's field with a compass")
    b.text_image("PLOTTING", "Plotting a Bar Magnet's Field",
                 ["Place a bar magnet on paper and mark its outline.",
                  "Put a plotting compass near one pole and mark the two ends "
                  "of the needle.",
                  "Move the compass so its tail sits on the last dot; repeat "
                  "to trace a line.",
                  "Joining the dots gives a curved field line; the field is "
                  "non-uniform (it varies in strength and direction)."],
                 bar, img_side="right", img_w=5.6, img_h=4.0,
                 panel_title="Following the compass",
                 caption="Curved lines: a non-uniform field",
                 notes="The compass plotting method traces field lines. A bar "
                       "magnet's field is non-uniform — curved, unevenly "
                       "spaced lines.")
    b.text_image("NEUTRAL POINTS", "Neutral Points",
                 ["A neutral point is where the magnet's field exactly cancels "
                  "the Earth's field.",
                  "The net magnetic field there is zero.",
                  "A compass placed at a neutral point can point in any "
                  "direction.",
                  "Their position depends on how the magnet is laid relative "
                  "to north."],
                 neut, img_side="left", img_w=5.8, img_h=3.8,
                 panel_title="Where the field is zero",
                 caption="The magnet's field cancels the Earth's field",
                 notes="At a neutral point the magnet's field and the Earth's "
                       "field are equal and opposite, so they cancel to zero.")
    b.bullets("WHERE", "Where Neutral Points Appear", [
        ("N pointing north", "With the magnet's N pole toward geographic "
         "north, the neutral points lie to the east and west (on the "
         "equatorial line)."),
        ("N pointing south", "With the N pole toward the south, the neutral "
         "points lie on the axis, beyond the poles."),
        ("Always in pairs", "Neutral points occur symmetrically, one on each "
         "side."),
        ("Field is zero", "A plotting compass there is not deflected in any "
         "particular direction."),
    ], panel_title="Position depends on the magnet's setting",
       notes="The two cases (N to north vs N to south) move the neutral points "
             "from the sides to the axis — a classic ICSE point.")
    b.cards("MAKING MAGNETS", "Ways to Make a Magnet", [
        ("Stroking", "Rub a steel bar repeatedly with one pole of a magnet, "
         "always in the same direction."),
        ("Electrical method", "Pass a direct current through a coil wound on "
         "the steel bar (the strongest method)."),
        ("Induction", "Place a magnetic material near a magnet to magnetise it "
         "temporarily."),
        ("Demagnetising", "Heating, hammering or an alternating current can "
         "remove magnetism."),
    ], notes="Methods of making (and destroying) magnets. The electrical "
             "method using a DC coil is the most effective.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Neutral Point", "At a neutral point near a bar magnet, the "
             "total magnetic field is:", ["Very strong", "Zero",
              "Always pointing north", "Twice the Earth's field"])
    b.quiz_a(1, "B. Zero",
             "A neutral point is where the magnet's field and the Earth's "
             "field are equal in size but opposite in direction, so they "
             "cancel and the net field is zero.")
    b.quiz_q(2, "Compass There", "A plotting compass placed exactly at a "
             "neutral point will:", ["Point firmly north", "Point firmly "
              "south", "Rest in no definite direction", "Spin forever"])
    b.quiz_a(2, "C. Rest in no definite direction",
             "With no net field to align to, the compass needle has nothing to "
             "turn it, so it can settle pointing any way — the test for a "
             "neutral point.")
    b.quiz_q(3, "Non-Uniform", "The field lines plotted around a single bar "
             "magnet are curved and unevenly spaced, showing the field is:",
             ["Uniform", "Non-uniform", "Zero everywhere", "Straight"])
    b.quiz_a(3, "B. Non-uniform",
             "Curved lines that crowd near the poles and spread out further "
             "away show that the field changes in both strength and direction "
             "— a non-uniform field.")
    b.quiz_q(4, "Plotting Tool", "The instrument used to plot the field lines "
             "of a magnet on paper is a:", ["Voltmeter", "Plotting compass",
              "Thermometer", "Ammeter"])
    b.quiz_a(4, "B. Plotting compass",
             "A small plotting compass shows the field's direction at each "
             "point; moving it step by step and joining the marks traces out "
             "the field lines.")
    b.quiz_q(5, "Strongest Method", "The most effective way to make a strong "
             "permanent magnet from a steel bar is to:",
             ["Stroke it once with a magnet", "Pass a direct current through "
              "a coil wound around it", "Leave it in sunlight",
              "Hammer it repeatedly"])
    b.quiz_a(5, "B. Pass a direct current through a coil around it",
             "The electrical method — winding a coil round the steel and "
             "passing a direct current — magnetises it strongly and uniformly, "
             "far better than a few strokes. Hammering would actually "
             "demagnetise it.")
    b.divider(2, "Part 2", "Electromagnets",
              "Magnets you can switch on and off")
    b.text_image("ELECTROMAGNET", "The Electromagnet",
                 ["A current-carrying coil (solenoid) behaves like a bar "
                  "magnet.",
                  "Winding the coil on a soft-iron core makes a strong "
                  "electromagnet.",
                  "It is a magnet only while the current flows.",
                  "Stronger with more current, more turns and a soft-iron "
                  "core."],
                 sol, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="A switchable magnet",
                 caption="A coil + soft-iron core = electromagnet",
                 notes="An electromagnet is a solenoid with a soft-iron core. "
                       "Strength rises with current, turns and the core.")
    b.cards("ELECTRO vs PERMANENT", "Electromagnet vs Permanent Magnet", [
        ("Switchable", "An electromagnet can be turned on and off; a permanent "
         "magnet is always magnetic."),
        ("Adjustable", "Its strength changes with the current; a permanent "
         "magnet's is fixed."),
        ("Reversible poles", "Reversing the current swaps its poles."),
        ("Very strong", "It can be made far stronger than a permanent "
         "magnet."),
    ], notes="The advantages of an electromagnet: switchable, adjustable, "
             "reversible, can be very strong.")
    b.cards("USES", "Uses of Electromagnets", [
        ("Lifting cranes", "Switch on to lift scrap iron, off to drop it."),
        ("Electric bell", "Repeatedly pulls a clapper to strike the gong."),
        ("Relays & motors", "Switch large circuits and drive electric "
         "motors."),
        ("Loudspeakers & maglev", "Make sound, and lift maglev trains."),
    ], notes="Uses exploit switchable, controllable magnetism. The lifting "
             "crane and electric bell are the classic examples.")
    b.cards("CARE OF MAGNETS", "Storing and Caring for Permanent Magnets", [
        ("They weaken", "Rough handling, heating, hammering and stray fields "
         "gradually weaken a magnet."),
        ("Use keepers", "Store bar magnets in pairs with soft-iron 'keepers' "
         "across their ends."),
        ("Unlike poles together", "Lay the pair with unlike poles adjacent, "
         "joined by the keepers."),
        ("Why it helps", "The keepers form closed loops for the field, keeping "
         "the molecular magnets aligned."),
    ], notes="Care of magnets: avoid heat/shock; store in pairs with soft-iron "
             "keepers across unlike poles to preserve magnetism.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Plotting", "use a plotting compass to trace field lines"),
        ("Bar magnet field", "non-uniform: curved, unevenly spaced lines"),
        ("Neutral point", "magnet's field cancels Earth's; net field zero"),
        ("Electromagnet", "solenoid + soft-iron core; switchable"),
        ("Vs permanent", "switchable, adjustable, reversible, very strong"),
        ("Uses", "cranes, electric bell, relays, motors, loudspeakers"),
    ], notes="Rapid recap; neutral points and the electromagnet advantages are "
             "the key points.")
    b.quiz_intro("Quiz 2", "Final Check — Electromagnets", 5)
    b.quiz_q(1, "Why Soft Iron?", "An electromagnet's core is made of soft "
             "iron rather than steel because soft iron:",
             ["Stays magnetic permanently", "Loses its magnetism as soon as "
              "the current stops", "Conducts electricity better",
              "Is lighter"])
    b.quiz_a(1, "B. Loses its magnetism when the current stops",
             "Soft iron magnetises and demagnetises easily, so the "
             "electromagnet can be switched off. Steel would keep its "
             "magnetism and could not be turned off.")
    b.quiz_q(2, "Make It Stronger", "Which change would NOT strengthen an "
             "electromagnet?", ["More turns on the coil",
              "A larger current", "A soft-iron core",
              "Using a wooden core instead of iron"])
    b.quiz_a(2, "D. Using a wooden core",
             "Wood is non-magnetic and adds nothing. An electromagnet is made "
             "stronger by more turns, a larger current and a soft-iron core.")
    b.quiz_q(3, "Scrapyard Crane", "A scrapyard prefers an electromagnet to a "
             "permanent magnet for moving iron because it can:",
             ["Never be switched off", "Be switched off to release the load",
              "Work without electricity", "Lift plastic too"])
    b.quiz_a(3, "B. Be switched off to release the load",
             "The crane grabs the scrap when the current is on and drops it "
             "when the current is switched off — control a permanent magnet "
             "could never provide.")
    b.quiz_q(4, "Reverse Current", "Reversing the current through an "
             "electromagnet:", ["Switches it off", "Swaps its north and south "
              "poles", "Doubles its strength", "Has no effect"])
    b.quiz_a(4, "B. Swaps its north and south poles",
             "The poles of an electromagnet depend on the current's direction. "
             "Reversing the current reverses the field, so the north and south "
             "ends interchange.")
    b.quiz_q(5, "Which Is Stronger Controllable", "Compared with an ordinary "
             "permanent magnet, an electromagnet's strength is:",
             ["Always fixed", "Adjustable by changing the current",
              "Always weaker", "Impossible to change"])
    b.quiz_a(5, "B. Adjustable by changing the current",
             "An electromagnet's strength can be increased or decreased simply "
             "by changing the current through its coil — a permanent magnet's "
             "strength cannot be adjusted.")
    b.closing("Magnetism on Demand",
              "Wind a coil, add a current, and you have a magnet you can "
              "switch, strengthen and reverse at will.")
    return b


def build():
    for fname, fn in [("G9_S122_Magnetism_1.pptx", deck1),
                      ("G9_S123_Magnetism_2.pptx", deck2)]:
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
