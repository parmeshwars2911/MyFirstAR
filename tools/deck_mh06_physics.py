"""
Maharashtra Board (MSBSHSE) — Standard 6 General Science physics decks.

Physics chapters of the Balbharati Std 6 General Science textbook covered here
(the post-session-25 tuitions scope): Work and Energy, Simple Machines, Sound,
Light and the Formation of Shadows, Fun with Magnets, and The Universe.

These are full teaching decks: each has ~20 concept slides (about ten per part)
that go into detail — definitions, everyday examples, applications, comparisons
and diagrams — plus two moderate-to-difficult quizzes, a recap and a close.
Content follows the Balbharati chapter treatment (subtopics checked against the
chapter scope), written in original teaching language with the full detail in
the speaker notes. Concise, visual teaching style (mhstyle).

Images: physics schematics are clean vector diagrams (diagrams_mh06 + reused
primitives); for the "very general" astronomy visuals (the Sun, a galaxy, a
nebula, the Milky Way) real public-domain NASA reference photographs are used
instead of hand-drawn art — loaded from build/web/ when present (see
tools/webimg.py) with a vector fallback.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import diagrams_extra as DE
import diagrams_mh as DM
import diagrams_mh06 as D6
import mhstyle

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "MH_Grade06"))
WEB = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "build",
                                   "web"))
os.makedirs(OUT, exist_ok=True)
mhstyle.apply()


def web(b, key, name, vector=None):
    """Prefer a real reference image build/web/<name>.png; else a vector."""
    p = os.path.join(WEB, name + ".png")
    if os.path.exists(p):
        return b.asset(key, p)
    return b.asset(key, vector) if vector else None


# ===========================================================================
# S25 — Work and Energy
# ===========================================================================
def work_energy_deck():
    footer = "Work and Energy  •  MSBSHSE Std 6 General Science"
    b = Builder(footer, accent=C["green"])
    pk = b.asset("mh6_we_pk", D6.potential_kinetic("mh6_we_pk"))
    forms = b.asset("mh6_we_forms", D6.energy_forms("mh6_we_forms"))
    conv = b.asset("mh6_we_conv", D6.energy_conversion("mh6_we_conv"))

    b.title("Std 6 • General Science • Work and Energy", "Work and Energy",
            "When is work done?  •  Energy  •  Potential and kinetic  •  "
            "Forms of energy  •  Sources of energy", img=pk)
    b.objectives([
        "State clearly when work is said to be done",
        "Explain that energy is the capacity to do work",
        "Tell potential energy apart from kinetic energy",
        "Name and describe the main forms of energy",
        "Trace how energy changes from one form to another",
        "Tell conventional from non-conventional energy sources",
    ])

    # ---- Part 1 : Work and Energy -------------------------------------------
    b.divider(1, "Part 1", "Work and Energy",
              "What 'work' means in science, and what energy is")
    b.statement("WORK", "What is Work?",
                "In science, work is done only when a force is applied to an "
                "object AND the object moves in the direction of the force.",
                points=[
                    "A force alone is not enough — the object must move.",
                    "Movement alone is not enough — a force must cause it.",
                    "Both together — a force and a movement — mean work is "
                    "done.",
                ],
                notes="Nail the scientific definition of work: a force AND a "
                      "displacement caused by it. This is different from the "
                      "everyday sense of 'work'.")
    b.cards("WORK OR NOT?", "Is Work Being Done?", [
        ("Lifting a bag ✔", "You apply an upward force and the bag moves up — "
         "work is done."),
        ("Pushing a moving cart ✔", "Your push moves the cart forward — work "
         "is done."),
        ("Pushing a still wall ✗", "You push hard but the wall does not move — "
         "no work is done."),
        ("Holding a suitcase ✗", "You hold it still; it does not move, so no "
         "scientific work is done."),
    ], notes="Sort clear cases of work from no-work. The key check every time: "
             "did the object actually move because of the force?")
    b.bullets("EVERYDAY vs SCIENCE", "Two Meanings of 'Work'", [
        ("Everyday meaning", "Anything that makes us tired — studying, "
         "standing guard, thinking hard."),
        ("Scientific meaning", "Only a force that moves an object through a "
         "distance."),
        ("Reading a book", "May tire us, but nothing is moved by a force, so "
         "no scientific work is done."),
        ("Why it matters", "Science needs one exact meaning so that work can "
         "be measured and compared."),
    ], notes="Separate the tiring, everyday sense of work from the precise "
             "scientific one. Only the scientific meaning can be measured.")
    b.statement("ENERGY", "Energy — the Capacity to Do Work",
                "Energy is the capacity, or the ability, to do work. Anything "
                "that can do work has energy.",
                points=[
                    "We get our energy from the food we eat.",
                    "Machines get energy from fuel, electricity or wind.",
                    "The more energy a body has, the more work it can do.",
                ],
                notes="Define energy as the capacity to do work, and connect it "
                      "to familiar sources — food for us, fuel and electricity "
                      "for machines.")
    b.bullets("UNIT", "Measuring Work and Energy", [
        ("Same unit", "Work and energy are measured in the same unit — the "
         "joule (J)."),
        ("Why the same", "Doing work uses up energy, so both are measured "
         "alike."),
        ("Small and large", "One joule is small; lifting a school bag uses "
         "many joules."),
        ("Never destroyed", "Energy is never lost — it only changes from one "
         "form into another."),
    ], notes="Both work and energy share the unit joule, because doing work "
             "spends energy. Introduce the idea that energy only changes form.")
    b.text_image("MECHANICAL ENERGY", "Potential and Kinetic Energy",
                 ["Mechanical energy has two kinds: potential and kinetic.",
                  "Potential energy is stored because of position or state.",
                  "Kinetic energy is the energy of a moving object.",
                  "As stored energy is released, it turns into energy of "
                  "motion."],
                 pk, img_side="right", panel_title="Stored vs moving",
                 caption="Potential energy → kinetic energy",
                 notes="Mechanical energy = potential + kinetic. Stored energy "
                       "becomes energy of motion when it is released.")
    b.bullets("POTENTIAL ENERGY", "Energy That is Stored", [
        ("Because of height", "Water held high in a dam and a stone on a hill "
         "have potential energy."),
        ("Because of state", "A stretched bow and a wound-up spring store "
         "potential energy."),
        ("Ready to act", "This stored energy can do work the moment it is "
         "released."),
        ("Example", "Release the bow and the stored energy shoots the "
         "arrow."),
    ], notes="Potential energy is stored by position (height) or by state "
             "(stretched/compressed). It is 'ready' energy waiting to act.")
    b.bullets("KINETIC ENERGY", "Energy of Motion", [
        ("Any moving body", "A running child, a moving bus and a spinning fan "
         "all have kinetic energy."),
        ("Flowing water", "A river and a waterfall carry large kinetic "
         "energy."),
        ("Blowing wind", "Moving air has kinetic energy that can turn a "
         "windmill."),
        ("More speed, more energy", "The faster a body moves, the more kinetic "
         "energy it has."),
    ], notes="Kinetic energy belongs to anything in motion — vehicles, water, "
             "wind. Faster motion means more kinetic energy.")
    b.cards("PE ↔ KE", "Watching Energy Change Kind", [
        ("A falling stone", "Loses height (potential) and speeds up "
         "(kinetic) as it falls."),
        ("A swinging swing", "Highest point is all potential; lowest point is "
         "all kinetic."),
        ("Dam water", "Stored high (potential), it rushes down (kinetic) to "
         "the turbine."),
        ("A drawn bow", "Stored in the bent bow (potential), released into the "
         "flying arrow (kinetic)."),
    ], notes="Everyday examples where potential and kinetic energy swap back "
             "and forth — swing, dam, bow, falling stone.")

    b.cards("WORK IN LIFE", "Work We Do Every Day", [
        ("Lifting", "Raising a bucket of water from a well against gravity."),
        ("Pushing & pulling", "Moving a cart or dragging a box across the "
         "floor."),
        ("Climbing", "Walking up a staircase lifts our body — that is work."),
        ("Throwing", "Giving a ball a push sets it moving — work is done on "
         "it."),
    ], notes="Ground the idea of work in everyday actions — lifting, pushing, "
             "climbing, throwing — where a force clearly moves something.")

    b.quiz_intro("Quiz 1", "Check — Work, Energy & Its Two Kinds", 4)
    b.quiz_q(1, "When is work done", "In science, work is done only when a "
             "force:", ["Is very large", "Moves an object through a distance",
              "Is applied by a machine", "Makes us tired"])
    b.quiz_a(1, "B. Moves an object through a distance",
             "Work needs both a force and a movement (displacement). If nothing "
             "moves, no scientific work is done.")
    b.quiz_q(2, "No work", "In which case is no scientific work done?",
             ["Lifting a bucket of water", "Pushing a car that starts moving",
              "Pushing hard against a wall that does not move",
              "Kicking a ball"])
    b.quiz_a(2, "C. Pushing hard against a wall that does not move",
             "However hard we push, if the wall does not move there is no "
             "displacement, so no work is done in the scientific sense.")
    b.quiz_q(3, "Potential energy", "Which of these has potential energy stored "
             "because of its position?", ["A running boy",
              "Water held high in a dam", "A moving bus", "A spinning fan"])
    b.quiz_a(3, "B. Water held high in a dam",
             "Water stored high in a dam has potential energy because of its "
             "raised position; the others are examples of kinetic energy.")
    b.quiz_q(4, "Unit", "Work and energy are both measured in the same unit, "
             "the:", ["Metre", "Joule", "Second", "Newton"])
    b.quiz_a(4, "B. Joule",
             "Energy is the capacity to do work, so it is measured in the same "
             "unit as work — the joule (J).")

    # ---- Part 2 : Forms of Energy -------------------------------------------
    b.divider(2, "Part 2", "Forms of Energy",
              "The many forms of energy, how they change, and where they "
              "come from")
    b.text_image("FORMS", "Forms of Energy",
                 ["Energy appears in many different forms around us.",
                  "Light, heat, sound, chemical, electrical and mechanical are "
                  "some forms.",
                  "The Sun is our greatest source of light and heat energy.",
                  "Food and fuels store chemical energy for later use."],
                 forms, img_side="left", img_w=5.6, img_h=3.1,
                 panel_title="Many forms",
                 caption="Some everyday forms of energy",
                 notes="Name the main forms of energy. The Sun is the chief "
                       "source; food and fuels hold chemical energy.")
    b.cards("FORMS I", "A Closer Look — Four Forms", [
        ("Light energy", "Lets us see; comes from the Sun, a lamp or a "
         "flame."),
        ("Heat energy", "Warms things and cooks food; comes from the Sun and "
         "from burning fuel."),
        ("Sound energy", "Carried by vibrations; reaches us as music, speech "
         "and noise."),
        ("Chemical energy", "Stored in food, fuels and cells, and released "
         "when they are used."),
    ], notes="Describe light, heat, sound and chemical energy with an everyday "
             "source for each.")
    b.cards("FORMS II", "A Closer Look — More Forms", [
        ("Mechanical energy", "The energy of position and motion — potential "
         "plus kinetic."),
        ("Electrical energy", "Flows through wires to run our lights, fans and "
         "gadgets."),
        ("Solar energy", "Energy from the Sun, caught by solar panels and "
         "cookers."),
        ("Wind & water", "Moving air and flowing water carry energy we can "
         "harness."),
    ], notes="Describe mechanical, electrical, solar and wind/water energy — "
             "the forms we most often turn into useful work.")
    b.text_image("CONVERSION", "Energy Changes its Form",
                 ["Energy can change from one form into another.",
                  "In a hydro-power dam, stored water starts to fall.",
                  "Its potential energy becomes kinetic, which spins a "
                  "turbine.",
                  "The turning turbine runs a generator, giving electrical "
                  "energy."],
                 conv, img_side="right", img_w=5.6, img_h=2.6,
                 panel_title="One form to another",
                 caption="Potential → kinetic → mechanical → electrical",
                 notes="Trace the energy conversion chain in a hydro-electric "
                       "dam: potential → kinetic → mechanical → electrical.")
    b.cards("CONVERSIONS", "Energy Conversions Around Us", [
        ("Electric bulb", "Electrical energy → light energy (and some heat)."),
        ("Loudspeaker", "Electrical energy → sound energy."),
        ("Burning candle", "Chemical energy → light and heat energy."),
        ("Solar cooker", "Light/heat from the Sun → heat energy that cooks "
         "food."),
    ], notes="Everyday devices are energy converters. Ask students to name the "
             "'before' and 'after' form for each.")
    b.statement("CONSERVATION", "Energy is Never Lost",
                "Energy can change from one form to another, but it is never "
                "created out of nothing and never destroyed.",
                points=[
                    "Every device simply changes energy from one form to "
                    "another.",
                    "The total amount of energy always stays the same.",
                    "Because of this, we must use our energy sources wisely.",
                ],
                notes="Introduce the conservation idea at a Std 6 level: energy "
                      "only changes form, the total stays the same — which is "
                      "why saving energy matters.")
    b.cards("SOURCES", "Two Kinds of Energy Sources", [
        ("Conventional", "Long-used sources — coal, petroleum and natural gas "
         "(the fossil fuels)."),
        ("They run out", "Fossil fuels took millions of years to form and will "
         "one day be used up."),
        ("Non-conventional", "Renewable sources — the Sun, wind, flowing water "
         "and biogas."),
        ("They renew", "These sources keep being replaced by nature and do "
         "not run out."),
    ], notes="Conventional (fossil, limited) vs non-conventional (renewable). "
             "The key contrast is 'runs out' vs 'renews'.")
    b.bullets("CLEAN ENERGY", "Why We Turn to Clean Energy", [
        ("Fossil fuels pollute", "Burning coal and petrol dirties the air and "
         "warms the planet."),
        ("They are limited", "There is only so much coal, oil and gas left in "
         "the Earth."),
        ("Sun and wind are clean", "Solar and wind energy give power without "
         "polluting."),
        ("Can be reused", "Renewable sources are available again and again, "
         "day after day."),
    ], notes="The case for non-conventional energy: fossil fuels are limited "
             "and polluting; solar and wind are clean and renewable.")
    b.bullets("SAVE ENERGY", "Using Energy Wisely", [
        ("Switch off", "Turn off lights and fans when they are not needed."),
        ("Natural light", "Use daylight and natural air where you can."),
        ("Walk or cycle", "Save fuel by walking or cycling for short trips."),
        ("Choose efficient", "Use star-rated, energy-saving appliances at "
         "home."),
    ], notes="Simple, practical energy-saving habits students can adopt, "
             "linking back to conservation.")

    b.statement("THE SUN", "The Sun — the Source of Most Energy",
                "Almost all the energy we use can be traced back to the Sun, "
                "our nearest star.",
                points=[
                    "Plants trap the Sun's energy; our food comes from "
                    "plants.",
                    "Coal and petroleum formed from plants and animals of long "
                    "ago.",
                    "The Sun's heat also stirs the winds and lifts water into "
                    "the clouds.",
                ],
                notes="Tie the forms and sources together: the Sun is the "
                      "ultimate source of food energy, fossil fuels, wind and "
                      "the water cycle.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Work", "force × movement; no movement, no work"),
        ("Energy", "the capacity to do work; unit joule"),
        ("Potential", "stored energy — dam water, stretched bow"),
        ("Kinetic", "energy of motion — falling water, running"),
        ("Forms", "light, heat, sound, chemical, electrical…"),
        ("Sources", "conventional (fossil) vs non-conventional (clean)"),
    ], notes="Recap work, energy, its two mechanical kinds, the forms and the "
             "sources.")
    b.quiz_intro("Quiz 2", "Final Check — Forms of Energy", 4)
    b.quiz_q(1, "Kinetic energy", "A waterfall's rushing water is an example "
             "of:", ["Potential energy", "Kinetic energy", "Chemical energy",
              "No energy"])
    b.quiz_a(1, "B. Kinetic energy",
             "The falling, moving water has kinetic energy — the energy an "
             "object has because of its motion.")
    b.quiz_q(2, "Conversion", "In a hydro-power station, the potential energy "
             "of stored water is finally changed into ___ energy.",
             ["Sound", "Chemical", "Electrical", "Light"])
    b.quiz_a(2, "C. Electrical",
             "Falling water (kinetic) spins a turbine (mechanical), which runs "
             "a generator to give electrical energy.")
    b.quiz_q(3, "Chemical energy", "The energy stored in food and fuels is "
             "mainly:", ["Sound energy", "Chemical energy", "Light energy",
              "Mechanical energy"])
    b.quiz_a(3, "B. Chemical energy",
             "Food and fuels store chemical energy, which is released when they "
             "are used up by our body or burnt.")
    b.quiz_q(4, "Non-conventional", "Which of these is a non-conventional "
             "(renewable) source of energy?", ["Coal", "Petroleum",
              "Solar energy", "Natural gas"])
    b.quiz_a(4, "C. Solar energy",
             "Solar energy comes from the Sun and does not run out, so it is a "
             "non-conventional, renewable source; the others are fossil fuels.")
    b.closing("Energy Everywhere",
              "From lifting a bag to lighting a city, work and energy explain "
              "how everything gets done — and why we must use energy wisely.")
    return b


# ===========================================================================
# S31 — Simple Machines
# ===========================================================================
def simple_machines_deck():
    footer = "Simple Machines  •  MSBSHSE Std 6 General Science"
    b = Builder(footer, accent=C["orange"])
    incl = b.asset("mh6_sm_incl", D6.inclined_plane("mh6_sm_incl"))
    wedge = b.asset("mh6_sm_wedge", D6.wedge_and_screw("mh6_sm_wedge"))
    lever = b.asset("mh6_sm_lever", D6.lever_types("mh6_sm_lever"))
    pulley = b.asset("mh6_sm_pulley", D6.pulley("mh6_sm_pulley"))
    wheel = b.asset("mh6_sm_wheel", D6.wheel_and_axle("mh6_sm_wheel"))

    b.title("Std 6 • General Science • Simple Machines", "Simple Machines",
            "Machines make work easier  •  Inclined plane • wedge • screw  •  "
            "Lever • pulley • wheel and axle  •  Care of machines", img=lever)
    b.objectives([
        "Explain how a machine makes work easier",
        "Tell simple machines from complex machines",
        "Describe the inclined plane, the wedge and the screw",
        "Describe a lever and name its three classes",
        "Explain a pulley and a wheel and axle",
        "See why machines need care and maintenance",
    ])

    # ---- Part 1 : Machines and the inclined-plane family --------------------
    b.divider(1, "Part 1", "Machines and the Inclined Plane",
              "What a machine does, and the inclined-plane family")
    b.statement("MACHINE", "What is a Machine?",
                "A machine is a device that makes our work easier, faster or "
                "more convenient to do.",
                points=[
                    "It may let us use a smaller effort to move a big load.",
                    "It may let us apply the force in a handier direction.",
                    "It may simply help us work faster or more safely.",
                ],
                notes="Define a machine by what it does for us — less effort, a "
                      "better direction, or faster/safer work.")
    b.cards("SIMPLE vs COMPLEX", "Two Kinds of Machines", [
        ("Simple machine", "Has few or no moving parts — a lever, pulley, "
         "ramp, wheel and axle, wedge or screw."),
        ("Complex machine", "Made by joining several simple machines "
         "together."),
        ("A bicycle", "A complex machine — it uses levers, wheels-and-axles "
         "and more."),
        ("A sewing machine", "Also complex, built from many simple machines "
         "working together."),
    ], notes="Simple machines are the building blocks; complex machines like a "
             "bicycle or sewing machine combine several of them.")
    b.bullets("THE SIX", "The Six Simple Machines", [
        ("Inclined plane", "A sloping surface, such as a ramp."),
        ("Wedge and screw", "Two special forms of the inclined plane."),
        ("Lever", "A rigid bar that turns about a fixed point."),
        ("Pulley and wheel-and-axle", "Turning machines that lift and drive "
         "loads."),
    ], notes="Preview the six simple machines that the rest of the chapter "
             "explains one by one.")
    b.statement("HOW THEY HELP", "A Machine Changes the Force",
                "A simple machine changes the size or the direction of the "
                "force we apply — but it cannot do the work for free.",
                points=[
                    "Smaller effort: a ramp lets us push a load up gently.",
                    "Handier direction: a pulley lets us pull down to lift "
                    "up.",
                    "There is always a trade — usually a longer distance to "
                    "move.",
                ],
                notes="Machines change the size or direction of force. Hint at "
                      "the trade-off: a smaller effort over a longer distance.")
    b.text_image("INCLINED PLANE", "The Inclined Plane",
                 ["An inclined plane is a slanting, sloping surface.",
                  "It lets us raise a load with a smaller effort.",
                  "A ramp, a staircase and a slide are inclined planes.",
                  "The gentler (longer) the slope, the smaller the effort "
                  "needed."],
                 incl, img_side="right", panel_title="A sloping surface",
                 caption="A ramp raises a load with less effort",
                 notes="The inclined plane trades a longer push for a smaller "
                       "effort. Ramps, stairs and slides are examples.")
    b.cards("RAMPS AT WORK", "Inclined Planes Around Us", [
        ("Loading ramp", "Heavy drums are rolled up a plank into a truck."),
        ("Wheelchair ramp", "A gentle slope replaces steps for easy access."),
        ("Hill roads", "Winding roads climb a hill gradually, not straight "
         "up."),
        ("Staircase", "A staircase is a folded-up inclined plane."),
    ], notes="Real inclined planes: loading ramps, wheelchair ramps, hill "
             "roads and staircases — all trade distance for easier effort.")
    b.text_image("WEDGE & SCREW", "The Wedge and the Screw",
                 ["A wedge is two inclined planes joined to a sharp edge.",
                  "A wedge cuts or splits — an axe, a knife, a needle.",
                  "A screw is an inclined plane wound round a rod.",
                  "Both are really the inclined plane in another form."],
                 wedge, img_side="left", img_w=5.4, img_h=2.9,
                 panel_title="Two clever ramps",
                 caption="The wedge splits; the screw grips",
                 notes="The wedge (axe, knife) and the screw are both forms of "
                       "the inclined plane — a good way to link the three.")
    b.cards("WEDGE & SCREW USES", "Where We Meet Them", [
        ("The wedge cuts", "Axes, knives, chisels and needles all have a wedge "
         "edge."),
        ("The wedge holds", "A door wedge slipped under a door holds it open."),
        ("The screw joins", "Screws fasten pieces of wood or metal firmly "
         "together."),
        ("The screw lifts", "A screw jack raises a car; a bottle's cap is a "
         "screw."),
    ], notes="The wedge cuts, splits and holds; the screw joins and lifts. "
             "Both come from the humble inclined plane.")
    b.statement("NO FREE WORK", "Machines Make Work Easier — Not Less",
                "A simple machine makes a job easier to do, but we still have "
                "to put in the work; it is not created for free.",
                points=[
                    "A ramp needs a smaller push, but over a longer path.",
                    "The effort is smaller; the distance is larger.",
                    "So a machine spreads the same work into an easier form.",
                ],
                notes="Correct the common idea that machines reduce the work "
                      "itself. They reduce the effort, but you move a longer "
                      "distance.")

    b.cards("WHY MACHINES", "Why We Use Machines", [
        ("Less effort", "They let a small effort move a big load."),
        ("Save time", "Jobs get done faster than by bare hands."),
        ("Reach & convenience", "They let us work from a handy position or "
         "direction."),
        ("Hard jobs possible", "Some jobs simply cannot be done without a "
         "machine."),
    ], notes="Sum up the benefits of machines — less effort, saved time, "
             "convenience, and making hard jobs possible — before the quiz.")

    b.quiz_intro("Quiz 1", "Check — Machines & the Inclined Plane", 4)
    b.quiz_q(1, "Purpose", "The main purpose of a simple machine is to:",
             ["Make work harder", "Make our work easier or faster",
              "Use more energy", "Slow us down"])
    b.quiz_a(1, "B. Make our work easier or faster",
             "A machine lets us do a job with less effort, or in a more "
             "convenient way — it makes work easier.")
    b.quiz_q(2, "Inclined plane", "Which of these is an example of an inclined "
             "plane?", ["A pair of scissors", "A ramp for wheelchairs",
              "A pulley on a well", "A see-saw"])
    b.quiz_a(2, "B. A ramp for wheelchairs",
             "A ramp is a slanting surface — an inclined plane — that lets a "
             "load be raised with a smaller effort.")
    b.quiz_q(3, "The wedge", "An axe used to split wood works as a:",
             ["Pulley", "Wheel and axle", "Wedge", "Lever only"])
    b.quiz_a(3, "C. Wedge",
             "The sharp blade of an axe is a wedge — two inclined planes meeting "
             "at an edge — that splits the wood apart.")
    b.quiz_q(4, "The screw", "A screw is best described as:",
             ["A straight rod", "An inclined plane wound round a rod",
              "A kind of pulley", "A first-class lever"])
    b.quiz_a(4, "B. An inclined plane wound round a rod",
             "If you imagine unwinding the thread of a screw, it forms a long "
             "inclined plane — that is exactly what a screw is.")

    # ---- Part 2 : Levers, pulleys, wheel & axle -----------------------------
    b.divider(2, "Part 2", "Levers, Pulleys and the Wheel & Axle",
              "The turning and lifting machines, and caring for them")
    b.text_image("LEVER", "The Lever",
                 ["A lever is a rigid bar that can turn about a fixed point.",
                  "The fixed point is called the fulcrum.",
                  "The load is the weight we want to move.",
                  "The effort is the force we apply to move it."],
                 lever, img_side="right", img_w=5.4, img_h=3.4,
                 panel_title="Fulcrum • load • effort",
                 caption="The three parts of every lever",
                 notes="Define the three parts of a lever — fulcrum, load and "
                       "effort — before sorting the three classes.")
    b.bullets("CLASS 1", "First-Class Lever", [
        ("Fulcrum in the middle", "The fulcrum lies between the load and the "
         "effort."),
        ("See-saw", "The pivot is in the centre, with a child on each side."),
        ("Scissors", "Two first-class levers joined at a central pivot."),
        ("Also", "A crowbar and a pair of pliers work this way."),
    ], notes="First-class lever: fulcrum between load and effort — see-saw, "
             "scissors, crowbar, pliers.")
    b.bullets("CLASS 2", "Second-Class Lever", [
        ("Load in the middle", "The load lies between the fulcrum and the "
         "effort."),
        ("Wheelbarrow", "The wheel is the fulcrum; the load sits in the "
         "middle."),
        ("Bottle opener", "Lifts the cap with the load between hinge and "
         "hand."),
        ("Nutcracker", "Cracks the nut placed between the pivot and your "
         "grip."),
    ], notes="Second-class lever: load between fulcrum and effort — "
             "wheelbarrow, bottle opener, nutcracker.")
    b.bullets("CLASS 3", "Third-Class Lever", [
        ("Effort in the middle", "The effort is applied between the fulcrum "
         "and the load."),
        ("A pair of tongs", "You press in the middle to grip food at the "
         "end."),
        ("Fishing rod", "Your hand lifts in the middle to raise the far "
         "tip."),
        ("Forearm", "Even our own forearm lifting a weight is a third-class "
         "lever."),
    ], notes="Third-class lever: effort between fulcrum and load — tongs, "
             "fishing rod, our forearm.")
    b.text_image("PULLEY", "The Pulley",
                 ["A pulley is a grooved wheel with a rope over it.",
                  "A single fixed pulley changes the direction of the force.",
                  "We pull down on the rope to raise a load up.",
                  "Pulling down is easier because we can use our body "
                  "weight."],
                 pulley, img_side="left", img_w=3.6, img_h=4.0,
                 panel_title="Pull down to lift up",
                 caption="A fixed pulley changes direction",
                 notes="A fixed pulley does not reduce the effort but changes "
                       "its direction, so pulling down (easy) raises the load "
                       "up.")
    b.cards("PULLEYS AT WORK", "Where Pulleys Help", [
        ("Water from a well", "A rope over a pulley lifts the bucket up "
         "easily."),
        ("Hoisting a flag", "The flag rides up the pole on a pulley rope."),
        ("A crane", "Big pulleys let cranes lift very heavy loads."),
        ("Lifts and cranes", "Several pulleys together can share a huge "
         "load."),
    ], notes="Pulleys at work: wells, flagpoles, cranes and lifts. Combined "
             "pulleys can even reduce the effort needed.")
    b.text_image("WHEEL & AXLE", "The Wheel and Axle",
                 ["A large wheel is fixed to a thin rod called the axle.",
                  "Turning the big wheel easily turns the axle with force.",
                  "A steering wheel, a screwdriver and a doorknob use it.",
                  "It makes turning and twisting jobs much easier."],
                 wheel, img_side="right", img_w=3.8, img_h=4.0,
                 panel_title="Big wheel, small axle",
                 caption="Turn the wheel to turn the axle",
                 notes="In the wheel and axle a large wheel turns a small axle, "
                       "giving a turning advantage — steering wheels, "
                       "screwdrivers, doorknobs.")
    b.cards("MAINTENANCE", "Taking Care of Machines", [
        ("Oiling", "Oil and grease reduce friction between moving parts."),
        ("Cleaning", "Dust and dirt wear parts out, so keep machines clean."),
        ("Preventing rust", "Paint or oil stops iron parts from rusting."),
        ("Regular checks", "Timely repairs keep a machine safe and "
         "long-lasting."),
    ], notes="Machines need maintenance — oiling, cleaning, rust-proofing and "
             "checks — to reduce friction, last longer and stay safe.")

    b.bullets("COMPARE LEVERS", "The Three Lever Classes at a Glance", [
        ("Class 1", "Fulcrum in the middle — see-saw, scissors, crowbar."),
        ("Class 2", "Load in the middle — wheelbarrow, bottle opener, "
         "nutcracker."),
        ("Class 3", "Effort in the middle — tongs, fishing rod, our forearm."),
        ("The trick", "Just ask which part — F, L or E — sits in the middle."),
    ], notes="A single comparison slide for the three lever classes, with the "
             "quick trick: identify which part is in the middle.")
    b.cards("WHEEL & AXLE USES", "The Wheel and Axle Around Us", [
        ("Steering wheel", "Turns the thin steering shaft of a vehicle."),
        ("Screwdriver", "The fat handle (wheel) turns the thin blade (axle)."),
        ("Doorknob & tap", "A round knob or tap turns a thin spindle inside."),
        ("Pencil sharpener", "The handle turns the small cutting axle."),
    ], notes="More wheel-and-axle examples from daily life — steering wheel, "
             "screwdriver, doorknob, tap, sharpener.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Machine", "a device that makes work easier"),
        ("Inclined plane", "a slope; ramp, stairs, slide"),
        ("Wedge & screw", "inclined planes in other shapes"),
        ("Lever", "bar on a fulcrum; three classes"),
        ("Pulley", "grooved wheel; changes force direction"),
        ("Wheel & axle", "big wheel turns a small axle"),
    ], notes="Recap the six simple machines and how each helps us work.")
    b.quiz_intro("Quiz 2", "Final Check — Levers, Pulleys & Wheels", 4)
    b.quiz_q(1, "Fulcrum", "The fixed point about which a lever turns is "
             "called the:", ["Load", "Effort", "Fulcrum", "Axle"])
    b.quiz_a(1, "C. Fulcrum",
             "A lever turns about a fixed point called the fulcrum; the load is "
             "what we move and the effort is the force we apply.")
    b.quiz_q(2, "Class of lever", "In a see-saw, the fulcrum lies between the "
             "load and the effort. This makes it a:", ["Class 1 lever",
              "Class 2 lever", "Class 3 lever", "Not a lever"])
    b.quiz_a(2, "A. Class 1 lever",
             "When the fulcrum is in the middle, between the load and the "
             "effort, the lever is a first-class lever — like a see-saw or "
             "scissors.")
    b.quiz_q(3, "Second-class lever", "In which of these is the load between "
             "the fulcrum and the effort?", ["A see-saw", "A wheelbarrow",
              "A pair of tongs", "A fishing rod"])
    b.quiz_a(3, "B. A wheelbarrow",
             "In a wheelbarrow the wheel is the fulcrum and the load sits "
             "between it and your hands (the effort) — a second-class lever.")
    b.quiz_q(4, "Wheel and axle", "Which everyday device is an example of a "
             "wheel and axle?", ["A knife", "A ramp",
              "A steering wheel", "A see-saw"])
    b.quiz_a(4, "C. A steering wheel",
             "A steering wheel (the large wheel) turns a thin shaft (the axle), "
             "so it is a wheel-and-axle machine.")
    b.closing("Work Made Easy",
              "From a simple ramp to a turning wheel, simple machines let a "
              "small effort do a big job — and clever machines just combine "
              "them.")
    return b


# ===========================================================================
# S51 — Sound
# ===========================================================================
def sound_deck():
    footer = "Sound  •  MSBSHSE Std 6 General Science"
    b = Builder(footer, accent=C["purple"])
    vib = b.asset("mh6_sd_vib", D6.vibrating_sources("mh6_sd_vib"))
    med = b.asset("mh6_sd_med", D6.sound_needs_medium("mh6_sd_med"))
    wave = b.asset("mh6_sd_wave", D.longitudinal_wave("mh6_sd_wave"))

    b.title("Std 6 • General Science • Sound", "Sound",
            "Sound from vibrations  •  How sound travels  •  Sound needs a "
            "medium  •  The ear  •  Noise and its control", img=vib)
    b.objectives([
        "Explain that sound is produced by vibrations",
        "Describe how sound travels through a medium as a wave",
        "Show that sound cannot travel through a vacuum",
        "Compare how fast sound travels in solids, liquids and gases",
        "Tell a pleasant sound from noise",
        "Explain noise pollution and how to reduce it",
    ])

    # ---- Part 1 : Making sound and how it travels ---------------------------
    b.divider(1, "Part 1", "Making Sound and How It Travels",
              "Vibrations, the medium, the ear and the sound wave")
    b.text_image("PRODUCTION", "Sound is Made by Vibrations",
                 ["Every sound is produced by a vibrating object.",
                  "A vibration is a fast to-and-fro movement.",
                  "A drum, a bell, a string and our vocal cords all vibrate.",
                  "As long as the object vibrates, we keep hearing the "
                  "sound."],
                 vib, img_side="right", img_w=5.4, img_h=2.9,
                 panel_title="Vibration makes sound",
                 caption="Vibrating bodies make sound",
                 notes="Sound always begins with a vibration — a fast to-and-fro "
                       "motion. Touch a ringing bell to feel it vibrate.")
    b.statement("KEY IDEA", "No Vibration, No Sound",
                "A body makes a sound only while it is vibrating. The moment "
                "the vibration stops, the sound stops too.",
                points=[
                    "Pluck a stretched rubber band — it vibrates and hums.",
                    "Touch it to stop the vibration — the sound stops at "
                    "once.",
                    "Strike a bell, then hold it — the ringing dies away.",
                ],
                notes="Reinforce the direct link: sound lasts exactly as long "
                      "as the vibration. Damping the vibration kills the "
                      "sound.")
    b.bullets("VIBRATING SOURCES", "Things That Vibrate to Make Sound", [
        ("Musical instruments", "A drum skin, a sitar string and a flute's air "
         "column all vibrate."),
        ("Our voice", "Air from the lungs makes the vocal cords in the larynx "
         "vibrate."),
        ("A bell", "The metal of a struck bell vibrates and rings."),
        ("A buzzing insect", "A bee's fast-beating wings vibrate the air."),
    ], notes="Survey the many vibrating sources — instruments, voice, bells, "
             "insect wings — to show vibration is behind every sound.")
    b.bullets("OUR VOICE", "How We Produce Sound", [
        ("The voice box", "We have a voice box, the larynx, at the top of the "
         "windpipe."),
        ("Vocal cords", "Two thin vocal cords stretch across the larynx."),
        ("Air makes them vibrate", "Air pushed up from the lungs sets the cords "
         "vibrating."),
        ("Speech and song", "We shape this sound with the mouth and tongue "
         "into words."),
    ], notes="Explain human sound production: lungs push air, vocal cords in "
             "the larynx vibrate, mouth and tongue shape it into speech.")
    b.text_image("PROPAGATION", "How Sound Travels",
                 ["Sound spreads out from its source as a wave.",
                  "It travels through a medium — a solid, a liquid or a gas.",
                  "The wave passes the vibration from particle to particle.",
                  "In this way the sound energy reaches our ears."],
                 wave, img_side="left", panel_title="A wave through a medium",
                 caption="Sound spreads as a wave",
                 notes="Sound travels as a wave through a material medium, "
                       "passing the vibration particle to particle until it "
                       "reaches the listener.")
    b.statement("THE MEDIUM", "Sound Travels Through a Medium",
                "The substance through which sound travels from its source to "
                "our ears is called the medium.",
                points=[
                    "Air is the most common medium for the sounds we hear.",
                    "Sound also travels through water and through solids.",
                    "Fish and whales hear sounds carried through water.",
                ],
                notes="Define the medium and show it can be a gas, a liquid or "
                      "a solid — air, water, or the ground/rails.")
    b.text_image("NEEDS A MEDIUM", "Sound Needs a Medium",
                 ["Sound cannot travel through empty space (a vacuum).",
                  "In a bell-jar, as the air is pumped out the ringing "
                  "fades.",
                  "With no air at all, no sound reaches us.",
                  "This is why there is complete silence in outer space."],
                 med, img_side="right", img_w=3.6, img_h=4.0,
                 panel_title="No medium, no sound",
                 caption="Remove the air and the bell falls silent",
                 notes="The bell-jar experiment proves sound needs a medium: "
                       "removing the air silences the bell. Space is a vacuum, "
                       "so it is silent.")
    b.bullets("THE EAR", "How We Hear — The Human Ear", [
        ("Outer ear", "Collects the sound and funnels it into the ear "
         "canal."),
        ("Eardrum", "A thin skin that vibrates when the sound reaches it."),
        ("Middle ear", "Tiny bones pass the vibrations further inward."),
        ("Inner ear", "Sends the message to the brain, and we hear the "
         "sound."),
    ], notes="Trace the path of sound through the ear: outer ear → eardrum → "
             "middle-ear bones → inner ear → brain.")
    b.cards("SOUND IS ENERGY", "Sound Carries Energy", [
        ("It does work", "A loud sound can rattle windows and shake our "
         "chest."),
        ("From the source", "The vibrating body gives its energy to the "
         "medium."),
        ("Spreads out", "The energy travels outward in all directions as a "
         "wave."),
        ("Fades with distance", "Sound grows fainter as its energy spreads "
         "thinner."),
    ], notes="Sound is a form of energy: it can shake objects, it spreads out "
             "from the source, and it weakens with distance as the energy "
             "spreads.")

    b.cards("USES OF SOUND", "Why Sound Matters to Us", [
        ("Talking", "Speech lets us share ideas and feelings."),
        ("Music", "Songs and instruments give us joy."),
        ("Warnings", "Horns, bells and alarms keep us alert and safe."),
        ("Animals too", "Animals call to warn, find mates and stay "
         "together."),
    ], notes="Show why sound is useful — communication, music, warnings, and "
             "the calls animals use — before the first quiz.")

    b.quiz_intro("Quiz 1", "Check — Producing & Carrying Sound", 4)
    b.quiz_q(1, "Source of sound", "Sound is produced by a body that is:",
             ["Hot", "Vibrating", "Coloured", "Heavy"])
    b.quiz_a(1, "B. Vibrating",
             "Every sound comes from a vibrating object; the moment the "
             "vibration stops, the sound stops as well.")
    b.quiz_q(2, "Medium", "The substance through which sound travels from its "
             "source to our ears is called the:", ["Wave", "Vacuum",
              "Medium", "Echo"])
    b.quiz_a(2, "C. Medium",
             "Sound needs a material — a solid, liquid or gas — to travel "
             "through. This material is called the medium.")
    b.quiz_q(3, "Vacuum", "Sound cannot travel through a vacuum because a "
             "vacuum has:", ["Too much air", "No particles to carry it",
              "Very cold air", "Bright light"])
    b.quiz_a(3, "B. No particles to carry it",
             "A vacuum is empty space with no particles, so there is nothing to "
             "pass the vibrations along — hence no sound.")
    b.quiz_q(4, "The voice", "Human sound is produced by the vibration of "
             "the:", ["Teeth", "Vocal cords in the larynx", "Tongue only",
              "Nose"])
    b.quiz_a(4, "B. Vocal cords in the larynx",
             "Air from the lungs makes the vocal cords in the larynx (voice "
             "box) vibrate, and the mouth shapes this into speech.")

    # ---- Part 2 : Speed, noise and its control ------------------------------
    b.divider(2, "Part 2", "Speed of Sound, Noise and Its Control",
              "Where sound travels fastest, and taming noise")
    b.cards("SPEED", "How Fast Sound Travels", [
        ("Fastest in solids", "The tightly-packed particles of a solid pass "
         "the vibration on quickest."),
        ("Slower in liquids", "In a liquid the particles are a little farther "
         "apart, so sound is slower."),
        ("Slowest in gases", "In a gas such as air the particles are far "
         "apart, so sound travels slowest."),
        ("An old trick", "An ear on a railway track hears a train through the "
         "steel before the air."),
    ], notes="Sound is fastest in solids, slower in liquids, slowest in gases — "
             "because of how closely the particles are packed.")
    b.bullets("WHY THE DIFFERENCE", "Why Speed Depends on the Medium", [
        ("Closely packed", "In solids the particles are tightly packed and "
         "pass vibrations on at once."),
        ("A little apart", "In liquids the particles are farther apart, so it "
         "takes longer."),
        ("Far apart", "In gases the particles are very far apart, slowing the "
         "sound most."),
        ("Compare", "So the same sound reaches us fastest through a solid, "
         "slowest through air."),
    ], notes="The closer the particles, the faster they hand the vibration on "
             "— so solid > liquid > gas for the speed of sound.")
    b.bullets("PLEASANT vs NOISE", "Pleasant Sound and Noise", [
        ("Pleasant sound", "A soft, regular, tuneful sound — like music — is "
         "pleasant to hear."),
        ("Noise", "A loud, harsh, unwanted sound — like a blaring horn — is "
         "noise."),
        ("It depends", "The same sound can please one person and disturb "
         "another."),
        ("Too loud harms", "Any sound that is too loud becomes harmful to the "
         "ears."),
    ], notes="Distinguish pleasant (regular, tuneful) sound from noise (loud, "
             "harsh, unwanted) — and note that any sound too loud is harmful.")
    b.cards("SOURCES OF NOISE", "Where Noise Comes From", [
        ("Traffic", "Vehicle horns and engines on busy roads."),
        ("Loudspeakers", "Very loud music at functions and festivals."),
        ("Crackers", "Firecrackers make sudden, very loud bangs."),
        ("Machines", "Factory machines, generators and construction work."),
    ], notes="Common sources of noise pollution — traffic, loudspeakers, "
             "crackers and machinery — mostly human-made.")
    b.statement("NOISE POLLUTION", "What is Noise Pollution?",
                "Unwanted, loud and continuous sound that disturbs us and "
                "harms our health is called noise pollution.",
                points=[
                    "It is a real form of pollution, like air or water "
                    "pollution.",
                    "It is worst in crowded cities and near busy roads.",
                    "It builds up from many everyday sources together.",
                ],
                notes="Define noise pollution as harmful, unwanted, continuous "
                      "loud sound — a genuine pollutant, worst in cities.")
    b.cards("HARMFUL EFFECTS", "How Noise Harms Us", [
        ("Hearing loss", "Very loud noise can damage the ears and dull our "
         "hearing."),
        ("Poor sleep", "Continuous noise disturbs rest and sleep."),
        ("Stress", "It causes headaches, tiredness and irritation."),
        ("Poor focus", "It makes it hard to study, read or concentrate."),
    ], notes="The health effects of noise: hearing damage, disturbed sleep, "
             "stress and headaches, and difficulty concentrating.")
    b.bullets("CONTROL", "Reducing Noise Pollution", [
        ("Avoid needless horns", "Do not blow vehicle horns unnecessarily, "
         "especially near hospitals and schools."),
        ("Lower the volume", "Keep the TV, radio and loudspeakers at a "
         "reasonable volume."),
        ("Maintain vehicles", "Well-serviced engines and silencers run more "
         "quietly."),
        ("Plan wisely", "Keep noisy factories and stations away from homes, "
         "and plant trees to absorb sound."),
    ], notes="Practical ways to cut noise pollution — horns, volume, vehicle "
             "upkeep, planning and green cover.")
    b.cards("OUR PART", "What We Can Do", [
        ("Silence zones", "Respect no-horn zones near hospitals and "
         "schools."),
        ("Speak softly", "Keep our own voices and music down indoors."),
        ("Say no to crackers", "Enjoy festivals with fewer, quieter "
         "crackers."),
        ("Grow trees", "Trees around homes and roads soak up a lot of "
         "noise."),
    ], notes="Personal and community actions students can take: honour silence "
             "zones, keep volumes low, avoid crackers and plant trees.")

    b.bullets("LOUD & SOFT", "Loud and Soft Sounds", [
        ("A bigger hit", "Strike a drum harder and it sounds louder."),
        ("A gentle touch", "Tap it softly and the sound is faint."),
        ("More energy", "A louder sound simply carries more energy."),
        ("Fades with distance", "Even a loud sound grows softer far away."),
    ], notes="Introduce loudness at a Std 6 level: a harder hit gives a louder "
             "sound because it carries more energy, and sound fades with "
             "distance.")
    b.cards("SAFE EARS", "Keeping Our Ears Safe", [
        ("Avoid very loud sound", "Stay away from blaring speakers and loud "
         "crackers."),
        ("Turn volume down", "Keep earphones and music at a gentle level."),
        ("Cover your ears", "Block your ears near a sudden very loud noise."),
        ("Rest in quiet", "Give your ears quiet time to recover."),
    ], notes="Practical ear-care habits, linking the harm of loud noise to "
             "simple protective steps.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Production", "sound comes from vibrations"),
        ("Propagation", "travels as a wave through a medium"),
        ("Medium", "solid, liquid or gas; none in a vacuum"),
        ("Speed", "fastest in solids, slowest in gases"),
        ("Noise", "loud, harsh, unwanted sound"),
        ("Control", "fewer horns, lower volume, upkeep, trees"),
    ], notes="Recap production, propagation, the need for a medium, speed, and "
             "noise control.")
    b.quiz_intro("Quiz 2", "Final Check — Speed & Noise", 4)
    b.quiz_q(1, "Fastest medium", "Sound travels fastest through a:",
             ["Gas", "Liquid", "Solid", "Vacuum"])
    b.quiz_a(1, "C. Solid",
             "The closely-packed particles of a solid pass vibrations along "
             "quickest, so sound travels fastest in solids.")
    b.quiz_q(2, "Slowest medium", "Of these, sound travels slowest through:",
             ["Iron", "Water", "Air", "Wood"])
    b.quiz_a(2, "C. Air",
             "Air is a gas, whose particles are far apart, so sound travels "
             "slowest through it compared with liquids and solids.")
    b.quiz_q(3, "Noise pollution", "Continuous, loud, unwanted sound that harms "
             "our health is called:", ["Music", "An echo",
              "Noise pollution", "A vibration"])
    b.quiz_a(3, "C. Noise pollution",
             "Loud, harsh sound that goes on and on and damages health is noise "
             "pollution — a real form of pollution.")
    b.quiz_q(4, "Control", "Which of these helps to reduce noise pollution?",
             ["Blowing horns often", "Playing music at full volume",
              "Planting trees along roads", "Running unserviced engines"])
    b.quiz_a(4, "C. Planting trees along roads",
             "Trees absorb and block a lot of sound, so a green belt along "
             "roads helps reduce noise pollution.")
    b.closing("The World of Sound",
              "Every sound is a vibration set travelling through a medium — "
              "knowing how it works helps us enjoy music and keep noise in "
              "check.")
    return b


# ===========================================================================
# S59 — Light and the Formation of Shadows
# ===========================================================================
def light_deck():
    footer = "Light and the Formation of Shadows  •  MSBSHSE Std 6 Gen. Sci."
    b = Builder(footer, accent=C["orange"])
    mats = b.asset("mh6_li_mats", D6.transparent_opaque("mh6_li_mats"))
    rect = b.asset("mh6_li_rect", DE.rectilinear_propagation("mh6_li_rect"))
    shadow = b.asset("mh6_li_shadow", DE.shadow_formation("mh6_li_shadow"))

    b.title("Std 6 • General Science • Light", "Light and the Formation "
            "of Shadows",
            "Luminous objects  •  Transparent, translucent, opaque  •  "
            "Straight-line light  •  Shadows  •  The pinhole camera", img=shadow)
    b.objectives([
        "Tell luminous objects from non-luminous ones",
        "Classify materials as transparent, translucent or opaque",
        "State that light travels in straight lines",
        "Explain how a shadow is formed and what it needs",
        "Explain why shadows change in size and length",
        "See how straight-line light forms a pinhole image",
    ])

    # ---- Part 1 : Light and materials ---------------------------------------
    b.divider(1, "Part 1", "Light and Materials",
              "Sources of light and how materials treat it")
    b.bullets("SOURCES", "Luminous and Non-Luminous Objects", [
        ("Luminous", "Objects that give out their own light — the Sun, a star, "
         "a burning candle, a bulb."),
        ("Non-luminous", "Objects that do not make their own light — the Moon, "
         "a book, a table."),
        ("We see by light", "We see non-luminous things only when light falls "
         "on them and bounces to our eyes."),
        ("The Moon", "The Moon shines only because it reflects the Sun's "
         "light — it is non-luminous."),
    ], notes="Luminous objects make their own light; non-luminous ones only "
             "reflect it. The Moon is the classic non-luminous example.")
    b.cards("EXAMPLES", "Sorting Light Sources", [
        ("Luminous — natural", "The Sun and the other stars, and a "
         "firefly."),
        ("Luminous — man-made", "A bulb, a tube-light, a candle and a torch."),
        ("Non-luminous — natural", "The Moon, the planets, trees and "
         "rocks."),
        ("Non-luminous — man-made", "A mirror, a book, a wall and a car."),
    ], notes="Sort objects into luminous (natural/man-made) and non-luminous "
             "(natural/man-made) to sharpen the distinction.")
    b.statement("HOW WE SEE", "Why We Can See Things",
                "We see a luminous object by the light it gives out, and a "
                "non-luminous object by the light it reflects into our eyes.",
                points=[
                    "In complete darkness we cannot see anything at all.",
                    "Light must leave an object and reach the eye.",
                    "That is why a dark room lights up the moment a bulb is "
                    "switched on.",
                ],
                notes="Seeing needs light to travel from the object to the eye. "
                      "No light, no sight — hence darkness in an unlit room.")
    b.text_image("MATERIALS", "Transparent, Translucent, Opaque",
                 ["Transparent materials let light pass fully — clear glass, "
                  "water.",
                  "Translucent materials let light pass partly — frosted glass, "
                  "oiled paper.",
                  "Opaque materials do not let light pass — wood, metal, a "
                  "book.",
                  "Only opaque objects can cast a clear, dark shadow."],
                 mats, img_side="right", img_w=5.6, img_h=2.9,
                 panel_title="How much light passes",
                 caption="Full, partial or no light through",
                 notes="Three material types by how much light they let "
                       "through. Only opaque objects cast a clear shadow.")
    b.cards("MATERIALS IN LIFE", "These Materials Around Us", [
        ("Transparent use", "Clear window glass and spectacles let us see "
         "through."),
        ("Translucent use", "Frosted bathroom glass gives light but "
         "privacy."),
        ("Opaque use", "Walls, doors and curtains block light for shade and "
         "privacy."),
        ("Choosing wisely", "We pick a material for how much light we want "
         "through it."),
    ], notes="Everyday uses of each material type — clear glass, frosted glass, "
             "walls/curtains — chosen for how much light should pass.")
    b.text_image("STRAIGHT LINE", "Light Travels in Straight Lines",
                 ["Light travels in straight lines, called rays.",
                  "We see this in a sunbeam through a gap or in dusty air.",
                  "Because it goes straight, light cannot bend around a "
                  "corner.",
                  "This straight-line travel is what lets shadows form."],
                 rect, img_side="left", panel_title="Rectilinear propagation",
                 caption="A straight beam of light",
                 notes="Establish rectilinear propagation — light's "
                       "straight-line travel is the reason opaque objects cast "
                       "shadows.")
    b.bullets("EVIDENCE", "How We Know Light Goes Straight", [
        ("A sunbeam", "A ray through a window or through leaves is dead "
         "straight."),
        ("Line up the holes", "You can see through three cards only when their "
         "holes are in a straight line."),
        ("Cannot see round corners", "We cannot see what is behind a wall — "
         "light will not bend to it."),
        ("Sharp shadows", "The clean edge of a shadow shows light travelled "
         "straight to it."),
    ], notes="Give the classic evidence for rectilinear propagation: sunbeams, "
             "the three-card experiment, not seeing round corners, sharp "
             "shadow edges.")
    b.bullets("RAYS & BEAMS", "Rays and Beams of Light", [
        ("A ray", "A ray is the straight path along which light travels."),
        ("A beam", "A group of rays travelling together is a beam of light."),
        ("Arrows show direction", "In diagrams we draw a ray as a straight "
         "line with an arrow."),
        ("From the source out", "Rays spread outward from the light source in "
         "straight lines."),
    ], notes="Define a ray (the straight path of light) and a beam (a bundle of "
             "rays), and how we draw them — the language for the rest of "
             "optics.")

    b.statement("LIGHT IS ENERGY", "Light is a Form of Energy",
                "Light is a form of energy that lets us see, and that plants "
                "use to make their food.",
                points=[
                    "Our eyes need light to see the world around us.",
                    "Green plants use sunlight to prepare their food.",
                    "Solar panels turn light energy into electricity.",
                ],
                notes="Frame light as a form of energy — essential for sight, "
                      "for plants making food, and for solar electricity.")
    b.cards("LIGHT IN LIFE", "Light at Work Around Us", [
        ("To see", "We need light to read, walk and do our daily work."),
        ("For plants", "Sunlight lets green leaves make food for all life."),
        ("Solar power", "Sunlight is caught by panels to make electricity."),
        ("Signals", "Traffic lights and lamps guide and warn us."),
    ], notes="Everyday roles of light — seeing, plant food, solar power and "
             "signals — reinforcing that light is useful energy.")

    b.quiz_intro("Quiz 1", "Check — Light & Materials", 4)
    b.quiz_q(1, "Luminous", "Which of these is a luminous object?",
             ["The Moon", "A burning candle", "A mirror", "A page of a book"])
    b.quiz_a(1, "B. A burning candle",
             "A burning candle gives out its own light, so it is luminous. The "
             "Moon and a mirror only reflect light.")
    b.quiz_q(2, "Transparent", "A material through which we can see clearly "
             "because light passes fully is:", ["Opaque", "Translucent",
              "Transparent", "A shadow"])
    b.quiz_a(2, "C. Transparent",
             "Transparent materials such as clear glass let light pass right "
             "through, so we can see clearly through them.")
    b.quiz_q(3, "Translucent", "Frosted (ground) glass, which lets light pass "
             "only partly, is:", ["Transparent", "Translucent", "Opaque",
              "Luminous"])
    b.quiz_a(3, "B. Translucent",
             "Frosted glass lets some light through but we cannot see clearly "
             "through it — that makes it translucent.")
    b.quiz_q(4, "Straight line", "Shadows can form because light travels:",
             ["In curved paths", "Around corners", "In straight lines",
              "Only at night"])
    b.quiz_a(4, "C. In straight lines",
             "Because light travels in straight lines, it cannot bend around an "
             "opaque object, so a shadow forms behind it.")

    # ---- Part 2 : Shadows ---------------------------------------------------
    b.divider(2, "Part 2", "The Formation of Shadows",
              "How shadows form, why they change, and the pinhole camera")
    b.text_image("SHADOWS", "How a Shadow Forms",
                 ["A shadow forms when an opaque object blocks the light.",
                  "Light cannot bend around the object, so a dark patch is "
                  "left.",
                  "The dark patch appears on the far side of the object.",
                  "This dark patch is the shadow of the object."],
                 shadow, img_side="right", panel_title="Light blocked → shadow",
                 caption="An opaque object blocks the light",
                 notes="A shadow is the dark region left where an opaque object "
                       "blocks straight-travelling light.")
    b.bullets("THREE THINGS", "What a Shadow Needs", [
        ("A source of light", "There must be light — the Sun, a lamp or a "
         "torch."),
        ("An opaque object", "Something that blocks the light must be in the "
         "way."),
        ("A screen", "A surface — a wall, the ground — for the shadow to fall "
         "on."),
        ("All three together", "Remove any one and the shadow disappears."),
    ], notes="A shadow needs exactly three things: a light source, an opaque "
             "object and a screen. Missing any one, and there is no shadow.")
    b.cards("SHADOW FACTS", "Properties of a Shadow", [
        ("Always dark", "A shadow is always black — it has no colour of its "
         "own."),
        ("Only the outline", "It shows just the shape of the object, not its "
         "colour or detail."),
        ("On the far side", "It always forms on the side away from the "
         "light."),
        ("Same shape", "The shadow has the same outline as the object facing "
         "the light."),
    ], notes="Key properties: a shadow is black, shows only the outline, forms "
             "on the far side, and matches the object's facing shape.")
    b.bullets("SIZE OF SHADOW", "Why a Shadow Changes Size", [
        ("Nearer the light", "Move the object closer to the lamp and its "
         "shadow grows larger."),
        ("Nearer the screen", "Move it closer to the wall and the shadow "
         "shrinks and sharpens."),
        ("Distance decides", "The size depends on the distances between light, "
         "object and screen."),
        ("Hand shadows", "This is why hand-shadow figures grow huge near a "
         "torch."),
    ], notes="Shadow size depends on the distances involved: closer to the "
             "light makes it bigger, closer to the screen makes it smaller and "
             "sharper.")
    b.text_image("CHANGING SHADOWS", "Why Shadows Change Through the Day",
                 ["The Sun appears to move across the sky during the day.",
                  "In the morning and evening the Sun is low, so shadows are "
                  "long.",
                  "At noon the Sun is high overhead, so shadows are short.",
                  "The direction of a shadow also changes as the Sun moves."],
                 rect, img_side="left", panel_title="Long or short",
                 caption="The Sun's height sets the shadow length",
                 notes="The Sun's changing height changes the length and "
                       "direction of shadows — long when the Sun is low, short "
                       "at noon.")
    b.cards("SHADOW FUN", "Shadows at Work and Play", [
        ("The sundial", "An old clock that tells time from the Sun's moving "
         "shadow."),
        ("Shadow play", "Hand and puppet shadows entertain us on a lit "
         "screen."),
        ("Eclipses", "Even eclipses are giant shadows cast in space."),
        ("Finding direction", "A shadow's direction hints at where the Sun, "
         "and so the east and west, lie."),
    ], notes="Fun and useful shadows: the sundial, shadow play, eclipses as "
             "space-shadows, and using shadow direction to find your "
             "bearings.")
    b.statement("PINHOLE CAMERA", "Straight-Line Light Makes an Image",
                "Because light travels in straight lines, a tiny pinhole can "
                "form an upside-down image of a bright object on a screen.",
                points=[
                    "Rays from the top of the object cross to the bottom of "
                    "the image.",
                    "Rays from the bottom cross to the top — so the image is "
                    "inverted.",
                    "A pinhole camera is a simple box that shows this "
                    "effect.",
                ],
                notes="The pinhole camera is a lovely proof of straight-line "
                      "light: rays cross at the hole, giving an inverted image "
                      "on the screen.")
    b.bullets("MAKE ONE", "A Simple Pinhole Camera", [
        ("A closed box", "Take a box with a tiny pinhole on one side."),
        ("A screen", "Replace the opposite side with tracing (butter) "
         "paper."),
        ("Point at a bright object", "Aim the pinhole at a bright window or "
         "lamp."),
        ("See the image", "A small, upside-down image appears on the "
         "paper."),
    ], notes="A hands-on activity: build a pinhole camera from a box, a pinhole "
             "and tracing paper, and observe the inverted image.")

    b.cards("SHADOWS AROUND US", "Shadows in Everyday Life", [
        ("Under a tree", "A tree's shadow gives cool shade on a sunny day."),
        ("Buildings", "Tall buildings throw long shadows across a street."),
        ("Our own shadow", "It walks with us, changing length through the "
         "day."),
        ("Shadow of the Earth", "Even a lunar eclipse is the Earth's shadow on "
         "the Moon."),
    ], notes="Familiar shadows — shade under a tree, building shadows, our own "
             "shadow, and the Earth's shadow in a lunar eclipse.")
    b.statement("SUNDIAL", "Telling Time by a Shadow",
                "Because a shadow moves in a steady way as the Sun crosses the "
                "sky, it can be used to tell the time — this is a sundial.",
                points=[
                    "A rod casts a shadow onto a marked dial.",
                    "As the Sun moves, the shadow sweeps across the marks.",
                    "The position of the shadow shows the hour of the day.",
                ],
                notes="The sundial turns the daily march of a shadow into a "
                      "clock — a neat, historical application of shadows.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Luminous", "makes its own light — Sun, bulb, candle"),
        ("Transparent", "light passes fully — clear glass"),
        ("Translucent", "light passes partly — frosted glass"),
        ("Opaque", "light blocked — casts a shadow"),
        ("Shadow", "needs source, opaque object and screen"),
        ("Pinhole", "straight-line light → inverted image"),
    ], notes="Recap light sources, the three material types, how shadows form "
             "and change, and the pinhole camera.")
    b.quiz_intro("Quiz 2", "Final Check — Shadows", 4)
    b.quiz_q(1, "What forms a shadow", "A clear shadow is cast by an object "
             "that is:", ["Transparent", "Translucent", "Opaque", "Luminous"])
    b.quiz_a(1, "C. Opaque",
             "Only an opaque object blocks the light fully, so only an opaque "
             "object casts a clear, dark shadow.")
    b.quiz_q(2, "Needed for a shadow", "Which three things are needed to form "
             "a shadow?", ["Source, mirror, lens",
              "Source, opaque object, screen", "Water, air, light",
              "Sun, Moon, Earth"])
    b.quiz_a(2, "B. Source, opaque object, screen",
             "A shadow needs a source of light, an opaque object to block it, "
             "and a screen on which the shadow falls.")
    b.quiz_q(3, "Pinhole image", "The image formed by a pinhole camera is "
             "always:", ["The right way up", "Upside down (inverted)",
              "Coloured brightly", "Larger than life"])
    b.quiz_a(3, "B. Upside down (inverted)",
             "Straight rays from the object cross over at the pinhole, so the "
             "top goes to the bottom — the image is inverted.")
    b.quiz_q(4, "Shortest shadow", "A vertical pole casts its shortest shadow "
             "when the Sun is:", ["Rising at the horizon", "Low in the "
              "evening", "High overhead at noon", "Below the horizon"])
    b.quiz_a(4, "C. High overhead at noon",
             "When the noon Sun is high overhead, its rays fall almost "
             "straight down, so the pole's shadow is at its shortest.")
    b.closing("Light and Shadow",
              "Because light travels straight and some things block it, we get "
              "shadows — long at dawn, short at noon, and always telling the "
              "shape of what stands in the way.")
    return b


# ===========================================================================
# S62 — Fun with Magnets
# ===========================================================================
def magnet_deck():
    footer = "Fun with Magnets  •  MSBSHSE Std 6 General Science"
    b = Builder(footer, accent=C["teal"])
    matsort = b.asset("mh6_mg_sort", D6.magnetic_nonmagnetic("mh6_mg_sort"))
    poles = b.asset("mh6_mg_poles", DE.like_unlike_poles("mh6_mg_poles"))
    make = b.asset("mh6_mg_make", D6.making_a_magnet("mh6_mg_make"))
    field = b.asset("mh6_mg_field", DE.bar_magnet_field("mh6_mg_field"))

    b.title("Std 6 • General Science • Magnets", "Fun with Magnets",
            "Magnetic materials  •  Poles of a magnet  •  Laws of magnetism  •  "
            "Making, caring for and using magnets", img=field)
    b.objectives([
        "Tell magnetic materials from non-magnetic ones",
        "Describe the two poles of a magnet and the magnetic field",
        "State the laws of magnetism (attraction and repulsion)",
        "Explain that a free magnet points north–south",
        "Make a magnet by the stroking method",
        "List the uses and the proper care of magnets",
    ])

    # ---- Part 1 : Magnets, materials and poles ------------------------------
    b.divider(1, "Part 1", "Magnets, Materials and Poles",
              "What magnets attract, their poles and their field")
    b.bullets("MAGNETS", "What is a Magnet?", [
        ("Attracts iron", "A magnet is an object that attracts iron and a few "
         "other materials."),
        ("The discovery", "Long ago, a natural stone called lodestone "
         "(magnetite) was found to attract iron."),
        ("A natural magnet", "Lodestone is a natural magnet found in the "
         "Earth."),
        ("Artificial magnets", "The bar and horseshoe magnets we use are made "
         "by people."),
    ], notes="A magnet attracts iron. Tell the story of lodestone (natural "
             "magnet) and note that our everyday magnets are artificial.")
    b.cards("SHAPES", "Magnets Come in Many Shapes", [
        ("Bar magnet", "A straight rectangular bar — the one we use most in "
         "class."),
        ("Horseshoe / U", "Bent into a U so both poles face the same way and "
         "pull harder."),
        ("Ring magnet", "A round magnet with a hole, used in many gadgets."),
        ("Magnetic needle", "A slim magnet that can swing freely, as in a "
         "compass."),
    ], notes="Introduce the common magnet shapes — bar, horseshoe, ring and "
             "needle — and where each is used.")
    b.text_image("SORTING", "Magnetic vs Non-Magnetic Materials",
                 ["Some materials are pulled by a magnet; many are not.",
                  "Magnetic: iron, nickel and cobalt are attracted.",
                  "Non-magnetic: wood, plastic, paper and copper are not.",
                  "A magnet can sort magnetic things out of a mixture."],
                 matsort, img_side="right", img_w=5.6, img_h=3.1,
                 panel_title="What sticks and what does not",
                 caption="A magnet picks out the magnetic materials",
                 notes="Magnetic materials (iron, nickel, cobalt) are "
                       "attracted; non-magnetic ones (wood, plastic, copper) "
                       "are not. A magnet can separate them.")
    b.cards("THE TWO GROUPS", "Sorting Materials", [
        ("Magnetic materials", "Iron, steel, nickel and cobalt — attracted by "
         "a magnet."),
        ("Non-magnetic materials", "Wood, plastic, paper, glass, copper and "
         "aluminium — not attracted."),
        ("A useful test", "Bring a magnet near an object to check which group "
         "it is in."),
        ("Sorting scrap", "Big magnets pull iron out of mixed scrap and "
         "rubbish."),
    ], notes="List the two groups with clear examples, and note the practical "
             "use of magnets to separate iron scrap.")
    b.text_image("POLES", "The Poles of a Magnet",
                 ["Every magnet has two poles — north (N) and south (S).",
                  "The pull of a magnet is strongest at its poles.",
                  "Iron filings cluster most thickly at the two ends.",
                  "Break a magnet in two and each piece still has both "
                  "poles."],
                 poles, img_side="left", panel_title="North & south",
                 caption="Two poles, strongest at the ends",
                 notes="Every magnet has an N and an S pole, strongest at the "
                       "ends. Poles cannot be separated — breaking gives two "
                       "smaller magnets.")
    b.statement("POLES COME IN PAIRS", "You Cannot Get a Single Pole",
                "Every magnet always has two poles. If you break a bar magnet, "
                "each piece becomes a full magnet with its own N and S pole.",
                points=[
                    "Cut it again, and every new piece still has both poles.",
                    "There is no such thing as a lone north or south pole.",
                    "The pull is always strongest at these two poles.",
                ],
                notes="Poles always exist in pairs — breaking a magnet never "
                      "isolates a single pole, it just makes more complete "
                      "magnets.")
    b.bullets("DIRECTIVE PROPERTY", "A Free Magnet Points North–South", [
        ("Hang it freely", "Suspend a bar magnet by a thread so it can turn."),
        ("It settles N–S", "It always comes to rest pointing north–south."),
        ("Same every time", "Turn it and let go — it swings back to "
         "north–south."),
        ("The north pole", "The end that points north is called the north "
         "pole."),
    ], notes="The directive property: a freely suspended magnet always aligns "
             "north–south. This defines which end is the north pole.")
    b.cards("FINDING DIRECTION", "The Magnetic Compass", [
        ("A tiny magnet", "A compass is a small magnetic needle that turns "
         "freely."),
        ("Points north", "Its coloured end always settles pointing north."),
        ("Ancient help", "Sailors and travellers have used it for centuries."),
        ("Still used", "Hikers, ships and planes use compasses even today."),
    ], notes="The compass puts the directive property to work — a free needle "
             "points north, guiding travellers for centuries.")
    b.text_image("MAGNETIC FIELD", "The Magnetic Field",
                 ["The space around a magnet where its force acts is the "
                  "magnetic field.",
                  "Iron filings near a magnet line up along curved paths.",
                  "These paths show the invisible field around the magnet.",
                  "The field is strongest close to the poles."],
                 field, img_side="right", panel_title="An invisible region",
                 caption="Iron filings reveal the field",
                 notes="Introduce the magnetic field as the region of "
                       "influence around a magnet, revealed by iron filings and "
                       "strongest at the poles.")

    b.cards("PROPERTIES", "The Main Properties of a Magnet", [
        ("Attracts iron", "It pulls iron, nickel and cobalt towards it."),
        ("Has two poles", "Every magnet has a north and a south pole."),
        ("Strongest at poles", "The pulling force is greatest at the two "
         "ends."),
        ("Points north–south", "A free magnet always settles pointing "
         "north–south."),
    ], notes="Gather the key properties of a magnet into one summary card set "
             "before the first quiz.")

    b.quiz_intro("Quiz 1", "Check — Materials & Poles", 4)
    b.quiz_q(1, "Magnetic material", "Which of these is a magnetic material?",
             ["Copper", "Iron", "Plastic", "Wood"])
    b.quiz_a(1, "B. Iron",
             "Iron (like nickel and cobalt) is attracted by a magnet, so it is "
             "a magnetic material; copper, plastic and wood are not.")
    b.quiz_q(2, "Strongest part", "The pull of a bar magnet is strongest at "
             "its:", ["Centre", "Two poles", "Top edge", "Flat sides"])
    b.quiz_a(2, "B. Two poles",
             "A magnet's force is strongest at its poles — the two ends — where "
             "iron filings cluster most thickly.")
    b.quiz_q(3, "Free magnet", "A bar magnet hung so that it can turn freely "
             "finally comes to rest pointing:", ["East–west",
              "North–south", "Straight up", "In any random way"])
    b.quiz_a(3, "B. North–south",
             "A freely suspended magnet always settles pointing north–south — "
             "the very property used in a compass.")
    b.quiz_q(4, "Breaking a magnet", "If a bar magnet is broken into two "
             "pieces, each piece will have:", ["Only a north pole",
              "Only a south pole", "Both a north and a south pole", "No poles"])
    b.quiz_a(4, "C. Both a north and a south pole",
             "Poles never exist alone. Break a magnet and each new piece "
             "becomes a complete magnet with both an N and an S pole.")

    # ---- Part 2 : Laws, making, care and uses -------------------------------
    b.divider(2, "Part 2", "Laws, Making, Care and Uses",
              "How poles behave, and putting magnets to work")
    b.bullets("LAWS", "The Laws of Magnetism", [
        ("Like poles repel", "Two north poles, or two south poles, brought "
         "together push each other apart."),
        ("Unlike poles attract", "A north pole and a south pole pull towards "
         "each other."),
        ("Try it", "Bring two bar magnets close in different ways to feel "
         "both."),
        ("The basic rule", "This push-and-pull is the fundamental law of "
         "magnets."),
    ], notes="State the laws of magnetism clearly: like poles repel, unlike "
             "poles attract — the basis of everything magnets do.")
    b.statement("SURE TEST", "Repulsion is the Real Test",
                "A magnet attracts plain iron too, so attraction alone is not "
                "proof. Only repulsion proves that both objects are magnets.",
                points=[
                    "If two bars attract, one of them might just be iron.",
                    "If two bars repel, both must certainly be magnets.",
                    "So repulsion is the sure test of magnetism.",
                ],
                notes="A subtle but important point: attraction can be caused "
                      "by ordinary iron, so only mutual repulsion is a sure "
                      "test that both bars are magnets.")
    b.text_image("MAKING A MAGNET", "Making a Magnet by Stroking",
                 ["Lay an iron bar flat on the table.",
                  "Stroke it with one pole of a magnet, always the same way.",
                  "Lift the magnet at the end of each stroke and start again.",
                  "After many strokes the iron bar becomes a magnet."],
                 make, img_side="right", img_w=5.4, img_h=3.1,
                 panel_title="The single-touch method",
                 caption="Stroke the same way, again and again",
                 notes="The stroking (single-touch) method: repeatedly stroke "
                       "the iron in one direction with one pole, lifting away "
                       "between strokes.")
    b.bullets("OTHER WAYS", "Other Ways to Make a Magnet", [
        ("By stroking", "Rubbing with a magnet, as we just saw — a simple "
         "method."),
        ("By electricity", "A current in a coil of wire around iron makes an "
         "electromagnet."),
        ("Temporary or permanent", "Soft iron makes a temporary magnet; steel "
         "keeps its magnetism."),
        ("Losing it", "A magnet can also lose its magnetism if treated "
         "roughly."),
    ], notes="Beyond stroking, magnets can be made electrically. Note the "
             "difference between temporary (soft iron) and permanent (steel) "
             "magnets.")
    b.cards("LOSING MAGNETISM", "How a Magnet Loses its Power", [
        ("Heating", "Strong heat disturbs a magnet and weakens it."),
        ("Hammering", "Repeated hammering or banging destroys magnetism."),
        ("Dropping", "Dropping a magnet hard can leave it much weaker."),
        ("Careless storage", "Storing magnets wrongly slowly weakens them."),
    ], notes="Magnets lose strength through heat, hammering, dropping and "
             "careless storage — which motivates the care rules next.")
    b.bullets("CARE & STORAGE", "Caring for Magnets", [
        ("Store in pairs", "Keep two bar magnets together with unlike poles "
         "side by side."),
        ("Use keepers", "Place soft-iron pieces (keepers) across the ends."),
        ("Handle gently", "Do not heat, hammer or drop a magnet."),
        ("Keep them apart", "Store away from devices that magnets could "
         "harm."),
    ], notes="Proper care: store bar magnets in pairs with keepers across the "
             "poles, and avoid heat, shock and dropping.")
    b.cards("USES", "Magnets at Work", [
        ("Everyday", "Compass, fridge and cupboard doors, pencil boxes, pin "
         "holders."),
        ("In machines", "Electric bells, cranes, loudspeakers and MRI "
         "machines."),
        ("Sorting", "Big magnets lift and drop heavy iron scrap in "
         "junkyards."),
        ("Data & cards", "The strip on an ATM or metro card is magnetic."),
    ], notes="Round up the uses of magnets — everyday, in machines, for sorting "
             "scrap, and in cards and data storage.")

    b.bullets("ELECTROMAGNET", "The Electromagnet — a Magnet from Electricity", [
        ("Current in a coil", "A current in a coil of wire makes a magnetic "
         "field."),
        ("An iron core", "Winding the coil on soft iron makes it much "
         "stronger."),
        ("Only when 'on'", "It is magnetic only while the current flows."),
        ("Switchable", "It can be switched on and off — its great advantage."),
    ], notes="Introduce the electromagnet: a temporary magnet made by a current "
             "in a coil around iron, whose big advantage is that it can be "
             "switched on and off.")
    b.cards("ELECTROMAGNET USES", "Electromagnets at Work", [
        ("Electric bell", "An electromagnet makes the hammer strike the "
         "gong."),
        ("Cranes", "Powerful electromagnets lift and drop heavy iron scrap."),
        ("Loudspeakers", "They turn electrical signals into the sound we "
         "hear."),
        ("MRI machines", "Huge electromagnets help doctors see inside the "
         "body."),
    ], notes="Show where electromagnets are used — bells, cranes, loudspeakers "
             "and MRI machines — all relying on being switchable.")
    b.statement("MODERN LIFE", "Magnets in Our Modern World",
                "From the compass that guides travellers to the machines in "
                "our homes and hospitals, magnets quietly serve us everywhere.",
                points=[
                    "They store data on cards and in computers.",
                    "They run motors in fans, mixers and toys.",
                    "They help doctors, sailors, builders and engineers.",
                ],
                notes="Close Part 2 by placing magnets in the wider modern "
                      "world — data, motors, medicine, navigation and "
                      "construction.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Magnetic", "iron, nickel, cobalt are attracted"),
        ("Poles", "every magnet has N and S; strongest there"),
        ("Free magnet", "rests pointing north–south"),
        ("Laws", "like poles repel, unlike attract"),
        ("Making", "stroke iron one way, again and again"),
        ("Care", "store in pairs; no heat, hammering or dropping"),
    ], notes="Recap magnetic materials, poles, the field, the laws, making a "
             "magnet and caring for it.")
    b.quiz_intro("Quiz 2", "Final Check — Laws, Making & Uses", 4)
    b.quiz_q(1, "Like poles", "When the north poles of two magnets are brought "
             "close together, they:", ["Attract", "Repel", "Do nothing",
              "Join firmly"])
    b.quiz_a(1, "B. Repel",
             "Like poles repel. Two north poles (or two south poles) push each "
             "other away; only unlike poles attract.")
    b.quiz_q(2, "Sure test", "The only sure test that a bar of iron is really a "
             "magnet is:", ["Attraction of the ends",
              "Repulsion between two poles", "Its colour", "Its weight"])
    b.quiz_a(2, "B. Repulsion between two poles",
             "A magnet attracts plain iron too, so attraction is not proof. "
             "Only repulsion shows that both objects are magnets.")
    b.quiz_q(3, "Stroking", "In the stroking method of making a magnet, the "
             "iron bar should be stroked:", ["Back and forth quickly",
              "In one direction, again and again", "Only once",
              "With both poles at once"])
    b.quiz_a(3, "B. In one direction, again and again",
             "The magnet is stroked along the bar in the same direction "
             "repeatedly, lifting it away between strokes, until the bar "
             "becomes magnetised.")
    b.quiz_q(4, "Losing magnetism", "A magnet is likely to lose its magnetism "
             "if it is:", ["Stored with a keeper",
              "Kept away from heat", "Heated or hammered", "Kept in a pair"])
    b.quiz_a(4, "C. Heated or hammered",
             "Strong heating, hammering or dropping disturbs a magnet and makes "
             "it lose its magnetism, so magnets must be handled gently.")
    b.closing("The Magic of Magnets",
              "Magnets attract, point the way and drive our machines — a little "
              "care keeps their invisible force working for us.")
    return b


# ===========================================================================
# S65 — The Universe
# ===========================================================================
def universe_deck():
    footer = "The Universe  •  MSBSHSE Std 6 General Science"
    b = Builder(footer, accent=C["blue"])
    milky = web(b, "mh6_un_milky", "mh7_milkyway",
                DM.galaxy_types("mh6_un_milky_v"))
    galaxy = web(b, "mh6_un_galaxy", "mh7_galaxy",
                 DM.galaxy_types("mh6_un_galaxy_v"))
    nebula = web(b, "mh6_un_nebula", "mh7_nebula", None)
    sun = web(b, "mh6_un_sun", "mh6_sun", None)
    solar = b.asset("mh6_un_solar", D6.solar_system("mh6_un_solar"))
    const = b.asset("mh6_un_const", DM.constellation("mh6_un_const"))
    gtypes = b.asset("mh6_un_gtypes", DM.galaxy_types("mh6_un_gtypes"))

    b.title("Std 6 • General Science • Astronomy", "The Universe",
            "The universe  •  Galaxies  •  Stars and the Sun  •  Our solar "
            "system  •  Other heavenly bodies", img=milky)
    b.objectives([
        "Describe what the universe contains",
        "Explain what a galaxy is and name its shapes",
        "Describe stars, their types and where they are born",
        "Name the Sun as our nearest star",
        "List the members of the solar system",
        "Name the eight planets in order from the Sun",
    ])

    # ---- Part 1 : The universe and galaxies ---------------------------------
    b.divider(1, "Part 1", "The Universe and Galaxies",
              "Everything there is, and the great islands of stars")
    b.text_image("THE UNIVERSE", "The Universe",
                 ["The universe is everything that exists — all of space and "
                  "all it holds.",
                  "It contains countless stars, planets, gas and dust.",
                  "It is unimaginably huge and still being explored.",
                  "Our Earth is a tiny part of this vast universe."],
                 milky, img_side="right", panel_title="Everything there is",
                 caption="The Milky Way arching over Earth",
                 notes="Set the scale of the universe — everything that exists, "
                       "vast beyond imagining, with Earth a tiny part of it.")
    b.bullets("WHAT IT HOLDS", "What the Universe Contains", [
        ("Stars", "Countless glowing balls of hot gas, like our Sun."),
        ("Planets & moons", "Worlds that orbit stars, and moons that orbit "
         "planets."),
        ("Galaxies", "Enormous groups of stars, spread across space."),
        ("Gas and dust", "Vast clouds from which new stars are born."),
    ], notes="Inventory of the universe: stars, planets and moons, galaxies, "
             "and the gas-and-dust clouds that form new stars.")
    b.statement("LIGHT YEAR", "Measuring Huge Distances",
                "Distances in the universe are so vast that we measure them in "
                "light years — the distance light travels in one year.",
                points=[
                    "Light is the fastest thing there is.",
                    "In a whole year it covers an enormous distance — one "
                    "light year.",
                    "Even the nearest stars are several light years away.",
                ],
                notes="Introduce the light year as the unit of astronomical "
                      "distance — the distance light travels in one year — "
                      "because ordinary units are far too small.")
    b.text_image("GALAXIES", "Galaxies",
                 ["A galaxy is a group of countless stars and their planetary "
                  "systems.",
                  "Gravity holds all the stars, gas and dust together.",
                  "There are billions of galaxies in the universe.",
                  "Each galaxy is like a giant island of stars in space."],
                 galaxy, img_side="left", panel_title="Islands of stars",
                 caption="A spiral galaxy",
                 notes="A galaxy is a gravitationally bound island of countless "
                       "stars; the universe holds billions of them.")
    b.text_image("GALAXY SHAPES", "The Shapes of Galaxies",
                 ["Galaxies are seen in several shapes.",
                  "Spiral: a bright centre with curving arms.",
                  "Elliptical: a smooth oval or ball of stars.",
                  "Barred spiral and irregular are the other shapes."],
                 gtypes, img_side="right", img_w=5.8, img_h=2.7,
                 panel_title="Spiral • elliptical • irregular",
                 caption="Galaxies come in different shapes",
                 notes="Name the galaxy shapes — spiral, elliptical, barred "
                       "spiral and irregular — using the diagram.")
    b.bullets("OUR GALAXY", "The Milky Way", [
        ("Our home galaxy", "Our Sun and its planets lie in the Milky Way "
         "galaxy."),
        ("A spiral", "The Milky Way is a huge spiral galaxy."),
        ("Countless stars", "It contains hundreds of billions of stars."),
        ("Nearest neighbour", "Andromeda is the galaxy nearest to our Milky "
         "Way."),
    ], notes="Place ourselves: the Sun sits in the Milky Way, a spiral galaxy "
             "of hundreds of billions of stars, with Andromeda as its nearest "
             "neighbour.")
    b.text_image("NEBULA", "Nebulae — Where Stars are Born",
                 ["A nebula is a vast cloud of gas and dust in space.",
                  "Under gravity, parts of it clump together and heat up.",
                  "When hot and dense enough, a new star begins to shine.",
                  "So the huge nebulae are the birthplaces of stars."],
                 nebula, img_side="left", panel_title="Clouds of gas & dust",
                 caption="A star-forming nebula",
                 notes="Nebulae are the birthplaces of stars — a real NASA "
                       "image gives a sense of their scale and colour.")
    b.bullets("BIRTH OF A STAR", "How a Star is Born", [
        ("A giant cloud", "It begins in a huge nebula of gas and dust."),
        ("Gravity pulls in", "Gravity draws the gas together into a dense "
         "clump."),
        ("It heats up", "As it shrinks, the clump grows hotter and hotter."),
        ("A star shines", "When hot enough, it starts to glow — a new star is "
         "born."),
    ], notes="Walk through star birth step by step: nebula → gravity gathers "
             "gas → it heats → it shines. A gentle first look at stellar "
             "formation.")
    b.cards("TYPES OF STARS", "Stars Come in Different Kinds", [
        ("Sun-like stars", "Medium stars that shine steadily, like our own "
         "Sun."),
        ("Red giants", "Huge, cooler stars that glow red."),
        ("Binary stars", "Two stars that circle around each other."),
        ("Variable stars", "Stars whose brightness keeps changing."),
    ], notes="Introduce the star types from the chapter — Sun-like, red giant, "
             "binary and variable — to show stars are not all alike.")

    b.cards("STUDYING THE SKY", "How We Study the Universe", [
        ("The naked eye", "On a clear dark night we can see stars, planets and "
         "the Moon."),
        ("Telescopes", "They gather more light to show faint, far-off "
         "objects."),
        ("Observatories", "Giant telescopes on hills study the sky night after "
         "night."),
        ("Space missions", "Satellites and probes explore beyond the Earth."),
    ], notes="Show the tools of astronomy — the naked eye, telescopes, "
             "observatories and space missions — that let us study the "
             "universe.")

    b.quiz_intro("Quiz 1", "Check — Universe & Galaxies", 4)
    b.quiz_q(1, "Light year", "A light year is a unit of:",
             ["Time", "Distance", "Mass", "Brightness"])
    b.quiz_a(1, "B. Distance",
             "A light year is the distance that light travels in one year — a "
             "handy way to measure the huge gaps between stars.")
    b.quiz_q(2, "Galaxy", "A galaxy is best described as a huge group of:",
             ["Only planets", "Countless stars held together by gravity",
              "Water and ice", "Comets only"])
    b.quiz_a(2, "B. Countless stars held together by gravity",
             "A galaxy is an enormous collection of stars, along with gas and "
             "dust, all bound together by gravity.")
    b.quiz_q(3, "Our galaxy", "The galaxy in which our Sun lies is called "
             "the:", ["Andromeda", "Milky Way", "Orion", "Solar System"])
    b.quiz_a(3, "B. Milky Way",
             "Our Sun is just one of the countless stars that make up the Milky "
             "Way galaxy; Andromeda is our nearest neighbouring galaxy.")
    b.quiz_q(4, "Birthplace of stars", "New stars are born inside a:",
             ["Comet", "Nebula (cloud of gas and dust)", "Crater",
              "Planet"])
    b.quiz_a(4, "B. Nebula (cloud of gas and dust)",
             "Stars form when parts of a nebula — a huge cloud of gas and "
             "dust — collapse under gravity and grow hot enough to shine.")

    # ---- Part 2 : Stars, the Sun and the solar system -----------------------
    b.divider(2, "Part 2", "Stars, the Sun and the Solar System",
              "Our own star and its family of worlds")
    b.text_image("STARS & THE SUN", "Stars and the Sun",
                 ["A star is a huge ball of hot, glowing gas.",
                  "The Sun is our nearest star — that is why it looks so big.",
                  "Stars differ in size, brightness and colour.",
                  "The Sun gives the Earth the light and heat that support "
                  "life."],
                 sun, img_side="left", img_w=4.6, img_h=3.5,
                 panel_title="Our nearest star",
                 caption="The Sun — a star seen close up",
                 notes="A star is a glowing ball of gas. The Sun is the nearest "
                       "star and looks huge only because it is so close; it "
                       "sustains life on Earth.")
    b.bullets("THE SUN", "More About the Sun", [
        ("A medium star", "The Sun is a medium-sized, Sun-like star."),
        ("Gives light & heat", "It pours out the light and heat that warm the "
         "Earth."),
        ("The centre", "All the planets move around the Sun."),
        ("Supports life", "Without the Sun there would be no life on Earth."),
    ], notes="The Sun is a medium star at the centre of our system, the source "
             "of the light and heat that make life on Earth possible.")
    b.text_image("SOLAR SYSTEM", "Our Solar System",
                 ["The solar system is the Sun and everything that orbits it.",
                  "Eight planets travel around the Sun in fixed paths.",
                  "Moons, asteroids and comets are also part of it.",
                  "The Sun's gravity holds the whole system together."],
                 solar, img_side="right", img_w=5.8, img_h=2.7,
                 panel_title="The Sun's family",
                 caption="The Sun and its eight planets",
                 notes="The solar system = the Sun plus all that orbits it, "
                       "held together by the Sun's gravity.")
    b.bullets("THE PLANETS", "The Eight Planets in Order", [
        ("Nearest four", "Mercury, Venus, Earth and Mars are closest to the "
         "Sun."),
        ("Farthest four", "Jupiter, Saturn, Uranus and Neptune are far out."),
        ("Fixed paths", "Each planet moves around the Sun in its own path, "
         "called an orbit."),
        ("A memory phrase", "Try: 'My Very Easy Method Just Speeds Up "
         "Naming'."),
    ], notes="List the eight planets in order and give a mnemonic. Stress that "
             "each moves in its own fixed orbit around the Sun.")
    b.cards("INNER PLANETS", "The Inner (Rocky) Planets", [
        ("Mercury", "The closest planet to the Sun and the smallest."),
        ("Venus", "The hottest planet, wrapped in thick clouds."),
        ("Earth", "Our home — the only planet known to have life."),
        ("Mars", "The 'red planet', with reddish, dusty ground."),
    ], notes="The four inner planets are small and rocky. Give each a memorable "
             "tag — closest, hottest, home, red planet.")
    b.cards("OUTER PLANETS", "The Outer (Giant) Planets", [
        ("Jupiter", "The largest planet in the solar system."),
        ("Saturn", "Famous for its beautiful bright rings."),
        ("Uranus", "A cold, bluish-green giant that spins on its side."),
        ("Neptune", "The farthest planet, deep blue and very cold."),
    ], notes="The four outer planets are giants. Tag each — largest, ringed, "
             "tilted, farthest.")
    b.cards("OTHER BODIES", "Other Members of the Solar System", [
        ("Satellites (moons)", "Natural satellites orbit planets — the Moon "
         "orbits the Earth."),
        ("Asteroids", "Small rocky bodies, most in a belt between Mars and "
         "Jupiter."),
        ("Comets", "Icy bodies that grow a bright glowing tail near the Sun."),
        ("Meteors", "Bits of rock that burn up in our air as a bright "
         "streak."),
    ], notes="Round out the solar-system family: moons, asteroids, comets and "
             "meteors, with a familiar example of each.")
    b.text_image("CONSTELLATIONS", "Patterns in the Night Sky",
                 ["A constellation is a group of stars forming a pattern.",
                  "People named them after animals, people and objects.",
                  "The Great Bear (Saptarshi) and Orion are easy to spot.",
                  "They help us find our way around the night sky."],
                 const, img_side="right", panel_title="Star patterns",
                 caption="A recognisable star pattern",
                 notes="A constellation is a memorable star pattern used to "
                       "navigate the sky — name a couple visible from India.")

    b.bullets("SPECIAL EARTH", "Earth — Our Special Planet", [
        ("Just right", "The Earth is neither too hot nor too cold for life."),
        ("Air to breathe", "It has an atmosphere with the oxygen we need."),
        ("Liquid water", "It is the only planet with plenty of liquid water."),
        ("The only home", "So far, Earth is the only place known to have "
         "life."),
    ], notes="Highlight why the Earth is special among the planets — right "
             "temperature, air, water and life — and worth protecting.")
    b.statement("EXPLORING SPACE", "Reaching Out into Space",
                "People have always wondered about the sky, and today rockets "
                "and satellites let us explore space for real.",
                points=[
                    "Rockets carry satellites and astronauts above the "
                    "Earth.",
                    "Satellites help with weather, television and phones.",
                    "India's space agency, ISRO, has reached the Moon and "
                    "Mars.",
                ],
                notes="End on an inspiring note: space exploration by rockets "
                      "and satellites, and India's own achievements through "
                      "ISRO.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Universe", "everything that exists; measured in light years"),
        ("Galaxy", "countless stars bound by gravity; ours is the Milky Way"),
        ("Nebula", "gas-and-dust cloud where stars are born"),
        ("Star", "a huge ball of hot glowing gas; the Sun is nearest"),
        ("Solar system", "the Sun and its eight orbiting planets"),
        ("Planets", "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, "
         "Neptune"),
    ], notes="Recap from the universe down through galaxies, stars and the "
             "solar system.")
    b.quiz_intro("Quiz 2", "Final Check — Stars & the Solar System", 4)
    b.quiz_q(1, "What is a star", "A star is a huge ball of:",
             ["Cold rock", "Hot glowing gas", "Ice", "Liquid water"])
    b.quiz_a(1, "B. Hot glowing gas",
             "A star is an enormous ball of hot gas that gives out its own "
             "light and heat — just like our Sun.")
    b.quiz_q(2, "Nearest star", "The star nearest to the Earth is the:",
             ["Pole Star", "Sun", "Sirius", "Moon"])
    b.quiz_a(2, "B. Sun",
             "The Sun is our nearest star. It looks far bigger and brighter "
             "than the others only because it is so much closer.")
    b.quiz_q(3, "Order of planets", "Which planet is nearest to the Sun?",
             ["Earth", "Mercury", "Jupiter", "Neptune"])
    b.quiz_a(3, "B. Mercury",
             "Mercury is the closest planet to the Sun. The order outward is "
             "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.")
    b.quiz_q(4, "Comet", "A body of ice and dust that grows a glowing tail "
             "when it nears the Sun is a:", ["Planet", "Comet",
              "Satellite", "Star"])
    b.quiz_a(4, "B. Comet",
             "A comet is an icy body; as it nears the Sun it warms up and "
             "forms a long, bright, glowing tail.")
    b.closing("Looking Up",
              "From our own Sun to the farthest galaxy, the universe is vast "
              "beyond imagining — and its story begins with a look at the "
              "night sky.")
    return b


def build():
    jobs = [
        ("MH06_S25_Work_and_Energy.pptx", work_energy_deck),
        ("MH06_S31_Simple_Machines.pptx", simple_machines_deck),
        ("MH06_S51_Sound.pptx", sound_deck),
        ("MH06_S59_Light_and_the_Formation_of_Shadows.pptx", light_deck),
        ("MH06_S62_Fun_with_Magnets.pptx", magnet_deck),
        ("MH06_S65_The_Universe.pptx", universe_deck),
    ]
    for fname, fn in jobs:
        b = fn()
        issues = b.qa()
        b.save(os.path.join(OUT, fname))
        concept = len(b.prs.slides._sldIdLst) - 12  # minus chrome/quiz slides
        print(f"\n=== {fname} ===")
        print(f"slides: {len(b.prs.slides._sldIdLst)}  (~{concept} concept)")
        if issues:
            print("QA ISSUES:")
            for i in issues:
                print("  -", i)
        else:
            print("QA: no overlaps / off-slide shapes detected")


if __name__ == "__main__":
    build()
