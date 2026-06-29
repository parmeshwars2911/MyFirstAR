"""
Grade 8 Physics — Chapter: Energy.
S33 (work, units, energy, mechanical energy, potential energy) and
S34 (gravitational PE, kinetic energy, PE↔KE, forms & transformations).
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
FOOTER = "Energy  •  ICSE Class 8 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["orange"])
    pen = b.asset("g8en_pendulum", D.pendulum_energy("g8en_pendulum"))
    hero = b.asset("g8_energy_hero", pen)

    b.title("ICSE • Class 8 • Energy", "Work & Energy",
            "Work and its units  •  Energy  •  Mechanical energy  •  Potential "
            "energy", img=hero)
    b.objectives([
        "Define work and state when work is done",
        "Use the relation work = force × distance",
        "State the units of work and energy",
        "Define energy and mechanical energy",
        "Define potential energy",
        "Give everyday examples of potential energy",
    ])
    b.divider(1, "Part 1", "Work and Its Units",
              "What 'work' means in physics")
    b.statement("WORK", "Work Done by a Force",
                "In physics, work is done when a force moves a body in the "
                "direction of the force.",
                formula="Work  W  =  Force × distance moved   (W = F × d)",
                points=["Both a force AND movement are needed for work.",
                        "If there is no movement, no work is done.",
                        "Work is a scalar quantity."],
                notes="Define work precisely: force × distance in the force's "
                      "direction. No movement → no work, even if you feel "
                      "tired.")
    b.cards("WHEN?", "When Is Work Done — and Not Done?", [
        ("Work is done", "Lifting a box: you apply a force and it moves "
         "upward."),
        ("Pushing a car", "If the car moves, work is done on it."),
        ("No work", "Pushing hard against a wall that does not move — no "
         "movement, no work."),
        ("No work", "Carrying a bag while standing still — it does not move in "
         "the force's direction."),
    ], notes="Contrast cases. The wall and standing-still examples surprise "
             "students: effort without movement is not work in physics.")
    b.statement("UNITS", "Units of Work and Energy",
                "Work and energy are measured in the same unit, the joule.",
                formula="1 joule (J)  =  1 newton × 1 metre  (1 N·m)",
                points=["1 joule of work is done when a force of 1 N moves a "
                        "body 1 m.",
                        "Larger amounts are measured in kilojoules (kJ).",
                        "Energy is the capacity to do work, so it shares the "
                        "same unit."],
                notes="The joule links work and energy. 1 J = 1 N·m. Energy is "
                      "measured in joules because it is the ability to do "
                      "work.")
    b.worked("WORKED EXAMPLE", "Calculating Work",
             "A boy lifts a 5 kg bag through a height of 2 m. How much work "
             "does he do against gravity? (g = 10 m/s²)",
             ["Force needed = weight = m g = 5 × 10 = 50 N",
              "Work = Force × distance = 50 × 2",
              "Work = 100 J"],
             "Work done = 100 J",
             notes="First find the force (the weight), then multiply by the "
                   "height. A clean two-step calculation.")
    b.statement("POWER", "Power — the Rate of Doing Work",
                "Power is the rate at which work is done, or the rate at which "
                "energy is used.",
                formula="Power  =  work done / time taken        (unit: watt, "
                        "W)",
                points=["1 watt = 1 joule of work done in 1 second.",
                        "A more powerful machine does the same work in less "
                        "time.",
                        "Larger powers are measured in kilowatts (1 kW = 1000 "
                        "W)."],
                notes="Power = work/time, measured in watts. Distinguish from "
                      "work: the same job done faster needs more power.")
    b.worked("WORKED EXAMPLE", "Calculating Power",
             "A motor does 600 J of work in 4 seconds. Find its power.",
             ["Power = work done / time taken",
              "Power = 600 / 4",
              "Power = 150 W"],
             "Power = 150 W (150 joules per second)",
             notes="Divide work by time to get power in watts. Reinforces the "
                   "difference between work and power.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Is Work Done?", "In which case is NO work done in the "
             "scientific sense?", ["Lifting a book onto a shelf",
              "Pushing a trolley that rolls forward",
              "Pushing hard against a wall that does not move",
              "Kicking a football"])
    b.quiz_a(1, "C. Pushing a wall that does not move",
             "Work needs movement in the direction of the force. However hard "
             "you push, if the wall does not move, the distance is zero and so "
             "the work done is zero.")
    b.quiz_q(2, "How Much Work?", "A force of 20 N moves a box 3 m in the "
             "direction of the force. The work done is:", ["6.7 J", "23 J",
              "60 J", "17 J"])
    b.quiz_a(2, "C. 60 J",
             "Work = force × distance = 20 × 3 = 60 J. The joule is a "
             "newton-metre.")
    b.quiz_q(3, "Same Unit", "Work and energy are measured in the same unit "
             "because:", ["They are both forces", "Energy is the capacity to "
              "do work", "They are both distances", "They are unrelated"])
    b.quiz_a(3, "B. Energy is the capacity to do work",
             "Energy is defined as the ability to do work, so it is naturally "
             "measured in the same unit as work — the joule.")
    b.quiz_q(4, "Carrying a Bag", "A girl walks along a level road holding a "
             "heavy bag at constant height. The work she does on the bag "
             "is:", ["Very large", "Zero, as the bag does not move in the "
              "direction of the force", "Equal to its weight",
              "Negative"])
    b.quiz_a(4, "B. Zero",
             "She supports the bag with an upward force, but the bag moves "
             "horizontally, not upward. With no movement in the direction of "
             "the force, the work done on it is zero.")
    b.quiz_q(5, "More Work", "Doing the same job in less time means you use "
             "more:", ["Work", "Power", "Force", "Distance"])
    b.quiz_a(5, "B. Power",
             "The work done is the same, but doing it faster means a higher "
             "rate of doing work — that rate is called power. Work depends "
             "only on force and distance, not on the time taken.")
    b.divider(2, "Part 2", "Energy & Potential Energy",
              "The capacity to do work, stored up")
    b.statement("ENERGY", "Energy and Mechanical Energy",
                "Energy is the capacity to do work. Mechanical energy is the "
                "energy a body has due to its motion or its position.",
                points=["A body that can do work possesses energy.",
                        "Mechanical energy comes in two forms: kinetic and "
                        "potential.",
                        "Kinetic energy is due to motion; potential energy is "
                        "due to position or state."],
                notes="Energy = capacity to do work. Mechanical energy splits "
                      "into kinetic (motion) and potential (position) — set up "
                      "for the next slides.")
    b.statement("POTENTIAL ENERGY", "Potential Energy",
                "Potential energy is the energy a body has because of its "
                "position or its state (its condition).",
                points=["A raised body has gravitational potential energy.",
                        "A stretched or compressed spring has elastic "
                        "potential energy.",
                        "The energy is stored, ready to do work when "
                        "released."],
                notes="PE is stored energy from position or state. Raised "
                      "objects and stretched springs are the key examples.")
    b.cards("EXAMPLES", "Examples of Potential Energy", [
        ("Water in a dam", "Stored high up, ready to fall and turn turbines."),
        ("A stretched bow", "A drawn bow stores elastic PE to launch the "
         "arrow."),
        ("A wound spring", "A wound clock spring stores energy to run the "
         "clock."),
        ("A raised hammer", "Lifted up, it stores PE to drive in a nail."),
    ], notes="Everyday stores of potential energy. Each can later do work when "
             "released.")
    b.text_image("PE ⇄ KE", "Potential and Kinetic Energy",
                 ["A swinging pendulum shows energy changing form.",
                  "At the highest points it has maximum potential energy and "
                  "is momentarily still.",
                  "At the lowest point it moves fastest — maximum kinetic "
                  "energy.",
                  "Energy continually converts between PE and KE as it "
                  "swings."],
                 pen, img_side="left", img_w=5.8, img_h=3.8,
                 panel_title="Energy keeps changing form",
                 caption="Top: all PE.  Bottom: all KE.",
                 notes="The pendulum is the classic PE↔KE demo, leading into "
                       "kinetic energy and conservation next lesson.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Work", "force × distance moved in the force's direction"),
        ("No movement", "no work, however large the force"),
        ("Unit", "the joule (J) = 1 newton-metre; same for energy"),
        ("Energy", "the capacity to do work"),
        ("Potential energy", "stored energy due to position or state"),
        ("Examples", "dam water, stretched bow, wound spring, raised hammer"),
    ], notes="Rapid recap; W = F × d and the meaning of potential energy are "
             "the key ideas.")
    b.quiz_intro("Quiz 2", "Final Check — Energy & PE", 5)
    b.quiz_q(1, "Stored Energy", "A stretched rubber band possesses:",
             ["Kinetic energy", "Elastic potential energy", "Heat energy",
              "No energy"])
    b.quiz_a(1, "B. Elastic potential energy",
             "Stretching the band stores energy in it because of its changed "
             "state. This elastic potential energy is released — doing work — "
             "when the band is let go.")
    b.quiz_q(2, "Water in a Tank", "Water stored in a tank on a roof has "
             "potential energy because of its:", ["Motion", "Temperature",
              "Raised position", "Colour"])
    b.quiz_a(2, "C. Raised position",
             "Being lifted to a height gives the water gravitational potential "
             "energy. As it falls it can do work — for example, providing "
             "water pressure or turning a small turbine.")
    b.quiz_q(3, "Pendulum Bottom", "At the lowest point of its swing, a "
             "pendulum bob has:", ["Maximum potential energy",
              "Maximum kinetic energy", "No energy", "Only heat energy"])
    b.quiz_a(3, "B. Maximum kinetic energy",
             "At the bottom the bob moves fastest, so its kinetic energy is "
             "greatest. Its potential energy is least there, having been "
             "converted into motion.")
    b.quiz_q(4, "Lift It Higher", "Lifting the same box twice as high gives it "
             "potential energy that is:", ["Half as much", "The same",
              "Twice as much", "Four times as much"])
    b.quiz_a(4, "C. Twice as much",
             "Gravitational potential energy increases in proportion to the "
             "height. Lifting the box twice as high stores twice the potential "
             "energy.")
    b.quiz_q(5, "Joule", "One joule of work is done when a force of:",
             ["1 N moves a body 1 m", "1 N moves a body 10 m",
              "10 N moves a body 1 m", "1 N is applied without movement"])
    b.quiz_a(5, "A. 1 N moves a body 1 m",
             "By definition, 1 joule = 1 newton × 1 metre — the work done when "
             "a force of one newton moves a body one metre in its direction.")
    b.closing("The Energy to Do Work",
              "Work moves things; energy is the power to do it — and stored "
              "potential energy is just waiting to be released.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["teal"])
    pen = b.asset("g8en_pendulum2", D.pendulum_energy("g8en_pendulum2"))
    hero = b.asset("g8_energy2_hero", pen)

    b.title("ICSE • Class 8 • Energy", "Kinetic Energy & Its Forms",
            "Gravitational PE  •  Kinetic energy  •  PE → KE  •  Forms & "
            "transformations", img=hero)
    b.objectives([
        "Use the expression for gravitational potential energy",
        "Define kinetic energy and what it depends on",
        "Describe the conversion of potential energy into kinetic energy",
        "Recall the different forms of energy",
        "Give examples of energy transformations",
        "State that energy is conserved",
    ])
    b.divider(1, "Part 1", "Gravitational PE & Kinetic Energy",
              "Energy of height and energy of motion")
    b.statement("GRAVITATIONAL PE", "Gravitational Potential Energy",
                "The potential energy of a raised body equals the work done in "
                "lifting it to that height.",
                formula="PE  =  m g h   (mass × gravity × height)",
                points=["m = mass (kg), g = 10 m/s², h = height (m).",
                        "PE increases with both mass and height.",
                        "It is the energy stored by lifting the body."],
                notes="PE = mgh. Larger mass or greater height stores more "
                      "energy. It equals the work done lifting the body.")
    b.worked("WORKED EXAMPLE", "Potential Energy",
             "Find the potential energy gained by a 4 kg block raised to a "
             "height of 3 m. (g = 10 m/s²)",
             ["PE = m g h",
              "PE = 4 × 10 × 3",
              "PE = 120 J"],
             "Potential energy = 120 J",
             notes="Direct substitution into PE = mgh. Reinforce the units "
                   "give joules.")
    b.statement("KINETIC ENERGY", "Kinetic Energy",
                "Kinetic energy is the energy a body has because of its "
                "motion.",
                formula="KE  =  ½ m v²   (half × mass × speed²)",
                points=["KE depends on the mass and on the square of the "
                        "speed.",
                        "Doubling the speed gives four times the kinetic "
                        "energy.",
                        "A moving body can do work — a hammer drives a nail."],
                notes="KE = ½mv². The speed-squared dependence is important: "
                      "double the speed, quadruple the KE.")
    b.text_image("PE → KE", "Conversion of PE into KE",
                 ["Lift a ball: you give it potential energy.",
                  "Let it fall: the PE converts into kinetic energy as it "
                  "speeds up.",
                  "At the moment it lands, almost all the PE has become KE.",
                  "A pendulum swaps PE and KE back and forth on every swing."],
                 pen, img_side="right", img_w=5.8, img_h=3.8,
                 panel_title="Falling turns PE into KE",
                 caption="PE at the top becomes KE at the bottom",
                 notes="A falling body converts PE to KE. The total mechanical "
                       "energy stays the same — energy is conserved.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "PE Calculation", "A 2 kg object is lifted 5 m. Its "
             "gravitational potential energy is (g = 10 m/s²):", ["10 J",
              "100 J", "20 J", "50 J"])
    b.quiz_a(1, "B. 100 J",
             "PE = mgh = 2 × 10 × 5 = 100 J. Multiply mass, g and height.")
    b.quiz_q(2, "Double the Speed", "If a car's speed doubles, its kinetic "
             "energy becomes:", ["Double", "Half", "Four times as great",
              "Unchanged"])
    b.quiz_a(2, "C. Four times as great",
             "KE = ½mv² depends on the square of the speed. Doubling v "
             "multiplies the kinetic energy by 2² = 4 — which is why high "
             "speed is so dangerous in a crash.")
    b.quiz_q(3, "Falling Ball", "As a ball falls from a height, its potential "
             "energy:", ["Increases", "Is converted into kinetic energy",
              "Stays the same", "Disappears completely"])
    b.quiz_a(3, "B. Is converted into kinetic energy",
             "As the ball falls it loses height (PE) and gains speed (KE). The "
             "potential energy is steadily converted into kinetic energy, the "
             "total staying the same.")
    b.quiz_q(4, "Heaviest Hit", "Which moving object has the most kinetic "
             "energy?", ["A light ball moving slowly",
              "A heavy ball moving slowly", "A heavy ball moving fast",
              "A light ball at rest"])
    b.quiz_a(4, "C. A heavy ball moving fast",
             "Kinetic energy grows with both mass and the square of speed. A "
             "heavy ball moving fast has the largest of both, so it carries "
             "the most kinetic energy.")
    b.quiz_q(5, "Top of the Swing", "At the highest point of a pendulum's "
             "swing, its kinetic energy is:", ["Maximum", "Zero",
              "Equal to its potential energy", "Negative"])
    b.quiz_a(5, "B. Zero",
             "At the top of the swing the bob is momentarily at rest before "
             "swinging back, so its speed — and therefore its kinetic energy — "
             "is zero. All its energy is potential there.")
    b.divider(2, "Part 2", "Forms & Transformations of Energy",
              "Energy comes in many forms and changes between them")
    b.cards("FORMS", "Different Forms of Energy", [
        ("Mechanical", "Kinetic and potential energy of moving or raised "
         "bodies."),
        ("Heat & light", "Thermal energy and the energy carried by light."),
        ("Sound & electrical", "Energy of vibrations, and energy carried by "
         "currents."),
        ("Chemical & nuclear", "Stored in fuels and food, and in the nuclei "
         "of atoms."),
    ], notes="Survey the forms of energy. Students should be able to name "
             "several and recognise them in devices.")
    b.cards("TRANSFORMATIONS", "Energy Transformations", [
        ("Torch", "Chemical (cell) → electrical → light and heat."),
        ("Loudspeaker", "Electrical → sound."),
        ("Falling water", "Potential → kinetic → electrical (in a dam)."),
        ("Our bodies", "Chemical energy in food → movement and heat."),
    ], notes="Each device transforms one form of energy into others. Trace the "
             "chain for each example.")
    b.statement("CONSERVATION", "Energy Is Conserved",
                "Energy can be transformed from one form to another, but it can "
                "never be created or destroyed.",
                formula="Total energy always stays the same",
                points=["This is the law of conservation of energy.",
                        "In any change, the energy is only converted, not "
                        "lost.",
                        "Some energy usually becomes heat, which spreads out."],
                notes="The conservation law: energy is only transformed, never "
                      "created or destroyed. Some always ends up as heat.")
    b.cards("SOURCES", "Sources of Energy", [
        ("The Sun", "The ultimate source of almost all energy on Earth."),
        ("Renewable", "Replenished naturally and clean — solar, wind, water "
         "(hydro) and biomass."),
        ("Non-renewable", "Finite and polluting — coal, petroleum and natural "
         "gas (the fossil fuels)."),
        ("Use wisely", "Save energy and prefer renewables, since fossil fuels "
         "will run out."),
    ], notes="Energy sources: the Sun is ultimate; renewables (clean, "
             "replenished) vs non-renewables (finite fossil fuels). Conserve "
             "and shift to renewables.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Gravitational PE", "PE = m g h; grows with mass and height"),
        ("Kinetic energy", "KE = ½ m v²; grows with the square of speed"),
        ("PE → KE", "a falling body converts PE into KE"),
        ("Forms", "mechanical, heat, light, sound, electrical, chemical, "
         "nuclear"),
        ("Transformations", "devices change one form into others"),
        ("Conservation", "energy is never created or destroyed"),
    ], notes="Rapid recap; PE = mgh, KE = ½mv² and conservation are the key "
             "results.")
    b.quiz_intro("Quiz 2", "Final Check — KE & Transformations", 5)
    b.quiz_q(1, "KE Value", "A 2 kg ball moves at 3 m/s. Its kinetic energy "
             "is:", ["3 J", "6 J", "9 J", "18 J"])
    b.quiz_a(1, "C. 9 J",
             "KE = ½ m v² = ½ × 2 × 3² = ½ × 2 × 9 = 9 J. Remember to square "
             "the speed first.")
    b.quiz_q(2, "Hydroelectric", "In a hydroelectric dam, the main energy "
             "transformation is:", ["Heat → light",
              "Potential → kinetic → electrical", "Sound → electrical",
              "Chemical → nuclear"])
    b.quiz_a(2, "B. Potential → kinetic → electrical",
             "Water stored high up has potential energy. Falling, it gains "
             "kinetic energy, which spins turbines and generators to produce "
             "electrical energy.")
    b.quiz_q(3, "Energy Lost?", "A bouncing ball rises a little less after "
             "each bounce. The 'lost' energy has mainly become:",
             ["Destroyed", "Heat and sound", "Light", "Chemical energy"])
    b.quiz_a(3, "B. Heat and sound",
             "Energy is conserved, not destroyed. At each bounce some "
             "mechanical energy is converted into heat (from the impact) and "
             "sound, so less is left to lift the ball.")
    b.quiz_q(4, "Conservation Law", "The law of conservation of energy states "
             "that energy can be:", ["Created but not destroyed",
              "Destroyed but not created", "Transformed but neither created "
              "nor destroyed", "Both created and destroyed"])
    b.quiz_a(4, "C. Transformed but neither created nor destroyed",
             "Energy only changes form. The total amount in a closed system "
             "stays constant — it is never made from nothing or lost to "
             "nothing.")
    b.quiz_q(5, "In a Torch", "The sequence of energy changes in a working "
             "torch is:", ["Light → electrical → chemical",
              "Chemical → electrical → light and heat",
              "Electrical → chemical → sound", "Heat → light → chemical"])
    b.quiz_a(5, "B. Chemical → electrical → light and heat",
             "The cell's chemical energy becomes electrical energy, which the "
             "bulb converts into light (and some heat) — a chain of "
             "transformations with energy conserved.")
    b.closing("Energy Never Lost",
              "From a falling apple to a power station, energy only changes "
              "form — the grand bookkeeping of the universe always balances.")
    return b


def build():
    for fname, fn in [("G8_S33_Energy_1.pptx", deck1),
                      ("G8_S34_Energy_2.pptx", deck2)]:
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
