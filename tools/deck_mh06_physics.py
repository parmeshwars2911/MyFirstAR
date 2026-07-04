"""
Maharashtra Board (MSBSHSE) — Standard 6 General Science physics decks.

Physics chapters of the Balbharati Std 6 General Science textbook covered here
(the post-session-25 tuitions scope): Work and Energy, Simple Machines, Sound,
Light and the Formation of Shadows, Fun with Magnets, and The Universe.
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
            "Forms of energy", img=pk)
    b.objectives([
        "State when work is said to be done",
        "Explain that energy is the capacity to do work",
        "Tell potential energy apart from kinetic energy",
        "Name the main forms of energy",
        "Describe how energy changes from one form to another",
        "Tell conventional from non-conventional energy sources",
    ])

    b.divider(1, "Part 1", "Work and Energy",
              "What 'work' means in science, and what energy is")
    b.bullets("WORK", "When is Work Done?", [
        ("Force + movement", "Work is done only when a force moves an object "
         "through some distance."),
        ("No movement, no work", "Pushing hard against a wall that does not "
         "move means no work is done, in the scientific sense."),
        ("Everyday vs science", "Reading a book may tire us, but as nothing is "
         "moved by a force, no scientific work is done."),
        ("Lifting a bag", "Lifting a school bag onto a table is work — a force "
         "moves it upward."),
    ], notes="In science, work needs a force AND a displacement. Contrast "
             "'holding a wall' (no work) with 'lifting a bag' (work).")
    b.bullets("ENERGY", "Energy — the Capacity to Do Work", [
        ("Definition", "Energy is the capacity, or ability, to do work."),
        ("From food & fuel", "We get energy from food; machines get it from "
         "fuel or electricity."),
        ("Measured in joules", "Both work and energy are measured in the same "
         "unit — the joule (J)."),
        ("Never lost", "Energy is not destroyed; it only changes from one form "
         "to another."),
    ], notes="Energy is the capacity to do work, measured in joules — the same "
             "unit as work. Introduce that energy only changes form.")
    b.text_image("MECHANICAL ENERGY", "Potential and Kinetic Energy",
                 ["Mechanical energy has two kinds: potential and kinetic.",
                  "Potential energy is stored because of position or state.",
                  "Water in a dam and a stretched bow have potential energy.",
                  "Kinetic energy is the energy of a moving object."],
                 pk, img_side="right", panel_title="Stored vs moving",
                 caption="Potential energy → kinetic energy",
                 notes="Mechanical energy = potential + kinetic. Stored energy "
                       "(dam water, stretched bow) becomes kinetic as it is "
                       "released.")

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

    b.divider(2, "Part 2", "Forms of Energy",
              "The many forms of energy and how they change")
    b.text_image("FORMS", "Forms of Energy",
                 ["Energy appears in many forms around us.",
                  "Light, heat, sound, chemical, electrical and mechanical are "
                  "some forms.",
                  "The Sun is our greatest source of light and heat energy.",
                  "Food and fuels store chemical energy."],
                 forms, img_side="left", img_w=5.6, img_h=3.1,
                 panel_title="Many forms",
                 caption="Some everyday forms of energy",
                 notes="Name the main forms of energy. The Sun is the chief "
                       "source; food and fuels hold chemical energy.")
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
    b.cards("SOURCES", "Conventional and Non-Conventional Sources", [
        ("Conventional", "Long-used sources such as coal, petroleum and natural "
         "gas — they will run out one day."),
        ("Non-conventional", "Renewable sources such as the Sun, wind and "
         "flowing water — they do not run out."),
        ("Why it matters", "Fossil fuels are limited and cause pollution, so we "
         "must save energy."),
        ("The clean choice", "Solar and wind energy are cleaner and can be used "
         "again and again."),
    ], notes="Conventional (fossil) vs non-conventional (renewable) sources. "
             "Stress conservation and the shift to clean energy.")

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
            "Lever • pulley • wheel and axle", img=lever)
    b.objectives([
        "Explain how a machine makes work easier",
        "Tell simple machines from complex machines",
        "Describe the inclined plane, the wedge and the screw",
        "Describe a lever and name its three classes",
        "Explain a pulley and a wheel and axle",
        "See why machines need care and maintenance",
    ])

    b.divider(1, "Part 1", "Machines and the Inclined Plane",
              "What a machine does, and the inclined-plane family")
    b.bullets("MACHINES", "What is a Machine?", [
        ("Makes work easier", "A machine is a device that makes our work "
         "easier or faster."),
        ("Simple machines", "Simple machines have few or no moving parts — a "
         "lever, pulley, ramp, wheel and axle, wedge or screw."),
        ("Complex machines", "A complex machine, such as a bicycle or a sewing "
         "machine, is made of several simple machines."),
        ("Applies force cleverly", "A machine lets us apply a smaller effort, "
         "or apply it in a handier direction."),
    ], notes="A machine makes work easier. Simple machines are the building "
             "blocks; complex machines combine several of them.")
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

    b.divider(2, "Part 2", "Levers, Pulleys and the Wheel & Axle",
              "The turning and lifting machines")
    b.text_image("LEVER", "The Lever and its Three Classes",
                 ["A lever is a rigid bar that turns about a fixed point, the "
                  "fulcrum.",
                  "It also has a load to move and an effort we apply.",
                  "Class 1: fulcrum in the middle — a see-saw, scissors.",
                  "Class 2: load in the middle — a bottle opener, wheelbarrow. "
                  "Class 3: effort in the middle — tongs."],
                 lever, img_side="right", img_w=5.4, img_h=3.4,
                 panel_title="Fulcrum • load • effort",
                 caption="Where the fulcrum, load and effort sit",
                 notes="Define fulcrum, load and effort, then the three classes "
                       "by which part is in the middle. Give a common example "
                       "of each.")
    b.text_image("PULLEY", "The Pulley",
                 ["A pulley is a grooved wheel with a rope over it.",
                  "A single fixed pulley changes the direction of the force.",
                  "We pull down on the rope to raise a load up.",
                  "Pulleys lift water from a well and hoist a flag up a pole."],
                 pulley, img_side="left", img_w=3.6, img_h=4.0,
                 panel_title="Pull down to lift up",
                 caption="A fixed pulley changes direction",
                 notes="A fixed pulley does not reduce the effort but changes "
                       "its direction, so pulling down (easy) raises the load "
                       "up.")
    b.text_image("WHEEL & AXLE", "The Wheel and Axle",
                 ["A large wheel is fixed to a thin rod called the axle.",
                  "Turning the big wheel easily turns the axle with force.",
                  "A steering wheel, a screwdriver and a doorknob use it.",
                  "It makes turning jobs much easier."],
                 wheel, img_side="right", img_w=3.8, img_h=4.0,
                 panel_title="Big wheel, small axle",
                 caption="Turn the wheel to turn the axle",
                 notes="In the wheel and axle a large wheel turns a small axle, "
                       "giving a turning advantage — steering wheels, "
                       "screwdrivers, doorknobs.")

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
    b.quiz_q(3, "Fixed pulley", "A single fixed pulley helps us mainly "
             "because it:", ["Reduces the load to zero",
              "Changes the direction of the force",
              "Removes the need for a rope", "Makes the load heavier"])
    b.quiz_a(3, "B. Changes the direction of the force",
             "A single fixed pulley lets us pull down — which is easy — to "
             "raise a load upward; it changes the direction of our effort.")
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
            "medium  •  Noise and its control", img=vib)
    b.objectives([
        "Explain that sound is produced by vibrations",
        "Describe how sound travels through a medium as a wave",
        "Show that sound cannot travel through a vacuum",
        "Compare how fast sound travels in solids, liquids and gases",
        "Tell a pleasant sound from noise",
        "Explain noise pollution and how to reduce it",
    ])

    b.divider(1, "Part 1", "Making Sound and How It Travels",
              "Vibrations, the medium and the sound wave")
    b.text_image("PRODUCTION", "Sound is Made by Vibrations",
                 ["Every sound is produced by a vibrating object.",
                  "A drum, a bell, a string and our vocal cords all vibrate.",
                  "As long as the object vibrates, we keep hearing the sound.",
                  "When the vibration stops, the sound stops too."],
                 vib, img_side="right", img_w=5.4, img_h=2.9,
                 panel_title="Vibration makes sound",
                 caption="Vibrating bodies make sound",
                 notes="Sound always begins with a vibration. Touch a ringing "
                       "bell to feel it vibrate; stop the vibration and the "
                       "sound stops.")
    b.text_image("PROPAGATION", "How Sound Travels",
                 ["Sound spreads out from its source as a wave.",
                  "It travels through a medium — a solid, a liquid or a gas.",
                  "The wave carries the sound energy to our ears.",
                  "The substance the sound travels through is the medium."],
                 wave, img_side="left", panel_title="A wave through a medium",
                 caption="Sound spreads as a wave",
                 notes="Sound travels as a wave through a material medium, "
                       "carrying energy from the source to the listener.")
    b.text_image("NEEDS A MEDIUM", "Sound Needs a Medium",
                 ["Sound needs a medium — it cannot travel through empty "
                  "space.",
                  "In a bell-jar, as the air is pumped out the ringing fades.",
                  "With no air (a vacuum), no sound reaches us at all.",
                  "This is why there is silence in outer space."],
                 med, img_side="right", img_w=3.6, img_h=4.0,
                 panel_title="No medium, no sound",
                 caption="Remove the air and the bell falls silent",
                 notes="The bell-jar experiment proves sound needs a medium: "
                       "removing the air silences the bell. Space is a vacuum, "
                       "so it is silent.")

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
    b.quiz_q(4, "Bell jar", "In the bell-jar experiment, as more and more air "
             "is pumped out, the sound of the bell:", ["Grows louder",
              "Stays the same", "Grows fainter and fainter", "Turns into light"])
    b.quiz_a(4, "C. Grows fainter and fainter",
             "As the air (the medium) is removed, less and less sound can "
             "travel out, so the ringing grows fainter — showing sound needs a "
             "medium.")

    b.divider(2, "Part 2", "Speed of Sound, Noise and Its Control",
              "Where sound travels fastest, and taming noise")
    b.cards("SPEED", "How Fast Sound Travels", [
        ("Fastest in solids", "The tightly-packed particles of a solid pass the "
         "vibration on quickest."),
        ("Slower in liquids", "In a liquid the particles are a little farther "
         "apart, so sound is slower."),
        ("Slowest in gases", "In a gas such as air the particles are far apart, "
         "so sound travels slowest."),
        ("An old trick", "Putting an ear to a railway track lets you hear a "
         "train through the steel before the air."),
    ], notes="Sound is fastest in solids, slower in liquids, slowest in gases — "
             "because of how closely the particles are packed.")
    b.cards("NOISE", "Pleasant Sound and Noise", [
        ("Pleasant sound", "A soft, regular sound like music is pleasant to the "
         "ear."),
        ("Noise", "A loud, harsh, unwanted sound like a blaring horn is noise."),
        ("Noise pollution", "Continuous, loud noise that harms us is called "
         "noise pollution."),
        ("Its harm", "It can cause tiredness, poor sleep, headaches and even "
         "loss of hearing."),
    ], notes="Distinguish pleasant sound from noise, and define noise pollution "
             "as harmful continuous loud sound.")
    b.bullets("CONTROL", "Reducing Noise Pollution", [
        ("Avoid needless horns", "Do not blow vehicle horns unnecessarily, "
         "especially near hospitals and schools."),
        ("Lower the volume", "Keep the TV, radio and loudspeakers at a "
         "reasonable volume."),
        ("Maintain vehicles", "Well-serviced engines and silencers run more "
         "quietly."),
        ("Plan wisely", "Keep noisy factories, airports and stations away from "
         "homes, and plant trees to absorb sound."),
    ], panel_title="Keep the noise down",
       notes="Practical ways to cut noise pollution — horns, volume, vehicle "
             "upkeep, planning and green cover.")

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
            "Straight-line light  •  Shadows", img=shadow)
    b.objectives([
        "Tell luminous objects from non-luminous ones",
        "Classify materials as transparent, translucent or opaque",
        "State that light travels in straight lines",
        "Explain how a shadow is formed",
        "List what is needed to form a shadow",
        "Explain why shadows change length through the day",
    ])

    b.divider(1, "Part 1", "Light and Materials",
              "Sources of light and how materials treat it")
    b.bullets("SOURCES", "Luminous and Non-Luminous Objects", [
        ("Luminous", "Objects that give out their own light are luminous — the "
         "Sun, a star, a burning candle, a bulb."),
        ("Non-luminous", "Objects that do not make their own light are "
         "non-luminous — the Moon, a book, a table."),
        ("We see by light", "We see non-luminous things only when light from a "
         "source falls on them and reaches our eyes."),
        ("The Moon", "The Moon shines only because it reflects the Sun's "
         "light — it is non-luminous."),
    ], notes="Luminous objects make their own light; non-luminous ones only "
             "reflect it. The Moon is the classic non-luminous example.")
    b.text_image("MATERIALS", "Transparent, Translucent, Opaque",
                 ["Transparent materials let light pass fully — clear glass, "
                  "water.",
                  "Translucent materials let light pass partly — frosted glass, "
                  "oiled paper.",
                  "Opaque materials do not let light pass — wood, metal, a "
                  "book.",
                  "Only opaque objects can cast a clear shadow."],
                 mats, img_side="right", img_w=5.6, img_h=2.9,
                 panel_title="How much light passes",
                 caption="Full, partial or no light through",
                 notes="Three material types by how much light they let "
                       "through. The link to shadows: only opaque objects cast "
                       "a clear shadow.")
    b.text_image("STRAIGHT LINE", "Light Travels in Straight Lines",
                 ["Light travels in straight lines, called rays.",
                  "We see this in a sunbeam through a gap or in dusty air.",
                  "Because it goes straight, light cannot bend around a "
                  "corner.",
                  "This straight-line travel is what lets shadows form."],
                 rect, img_side="left", panel_title="Rectilinear propagation",
                 caption="A straight beam of light",
                 notes="Establish rectilinear propagation — the straight-line "
                       "travel of light is the reason opaque objects cast "
                       "shadows.")

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

    b.divider(2, "Part 2", "The Formation of Shadows",
              "How shadows form and why they change")
    b.text_image("SHADOWS", "How a Shadow Forms",
                 ["A shadow forms when an opaque object blocks the light.",
                  "It needs three things: a source, an opaque object and a "
                  "screen.",
                  "The screen is the surface on which the shadow falls.",
                  "Light cannot reach behind the object, so that part stays "
                  "dark."],
                 shadow, img_side="right", panel_title="Source • object • "
                 "screen", caption="Light blocked → shadow",
                 notes="A shadow needs a light source, an opaque object and a "
                       "screen. The blocked region behind the object is the "
                       "shadow.")
    b.cards("SHADOW FACTS", "More About Shadows", [
        ("Always dark", "A shadow is always black — it has no colour of its "
         "own."),
        ("Shape, not detail", "A shadow shows only the outline of an object, "
         "not its colour or features."),
        ("Same side", "The shadow always forms on the side away from the light "
         "source."),
        ("Size changes", "Moving the object nearer the light makes its shadow "
         "larger."),
    ], notes="Shadows are colourless outlines on the far side of the object; "
             "the size depends on the distances involved.")
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

    b.recap("WRAP UP", "Quick Recap", [
        ("Luminous", "makes its own light — Sun, bulb, candle"),
        ("Transparent", "light passes fully — clear glass"),
        ("Translucent", "light passes partly — frosted glass"),
        ("Opaque", "light blocked — casts a shadow"),
        ("Shadow", "needs source, opaque object and screen"),
        ("Length", "long when Sun is low, short at noon"),
    ], notes="Recap light sources, the three material types and how shadows "
             "form and change.")
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
    b.quiz_q(3, "Colour of a shadow", "The colour of a shadow is always:",
             ["The colour of the object", "Black", "White", "Grey and "
              "coloured"])
    b.quiz_a(3, "B. Black",
             "A shadow is simply a region where light has been blocked, so it "
             "is always dark (black), whatever the object's colour.")
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
            "Making and using magnets", img=field)
    b.objectives([
        "Tell magnetic materials from non-magnetic ones",
        "Describe the two poles of a magnet",
        "State the laws of magnetism (attraction and repulsion)",
        "Explain that a free magnet points north–south",
        "Make a magnet by the stroking method",
        "List the uses and the proper care of magnets",
    ])

    b.divider(1, "Part 1", "Magnets, Materials and Poles",
              "What magnets attract, and their two poles")
    b.bullets("MAGNETS", "Magnets and Magnetic Materials", [
        ("A magnet", "A magnet is an object that attracts iron and a few other "
         "materials."),
        ("Natural & artificial", "Lodestone is a natural magnet; the bar and "
         "horseshoe magnets we use are artificial."),
        ("Magnetic materials", "Iron, nickel and cobalt are attracted by a "
         "magnet — they are magnetic materials."),
        ("Non-magnetic materials", "Wood, plastic, paper and copper are not "
         "attracted — they are non-magnetic."),
    ], notes="A magnet attracts iron, nickel and cobalt (magnetic materials) "
             "but not wood, plastic or copper (non-magnetic).")
    b.text_image("SORTING", "Magnetic vs Non-Magnetic",
                 ["Bring a magnet near a mixed heap of small objects.",
                  "Iron nails, steel pins and nickel coins jump to the magnet.",
                  "Plastic, wood and copper pieces are left behind.",
                  "This simple test sorts magnetic from non-magnetic "
                  "materials."],
                 matsort, img_side="right", img_w=5.6, img_h=3.1,
                 panel_title="What sticks and what does not",
                 caption="A magnet picks out the magnetic materials",
                 notes="A magnet attracts only magnetic materials, so it can be "
                       "used to sort them out of a mixture (e.g. iron from "
                       "sand).")
    b.text_image("POLES", "The Poles of a Magnet",
                 ["Every magnet has two poles — north (N) and south (S).",
                  "The pull of a magnet is strongest at its poles.",
                  "A freely hung magnet always rests pointing north–south.",
                  "Break a magnet in two and each piece still has both poles."],
                 poles, img_side="left", panel_title="North & south",
                 caption="Two poles, strongest at the ends",
                 notes="Every magnet has an N and an S pole, strongest at the "
                       "ends. A free magnet aligns N–S; poles cannot be "
                       "separated.")

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

    b.divider(2, "Part 2", "Laws, Making, Care and Uses",
              "How poles behave, and putting magnets to work")
    b.bullets("LAWS", "The Laws of Magnetism", [
        ("Like poles repel", "Two north poles, or two south poles, brought "
         "together push each other apart."),
        ("Unlike poles attract", "A north pole and a south pole pull towards "
         "each other."),
        ("Test for a magnet", "Only repulsion is a sure test that both objects "
         "are magnets."),
        ("Magnetic field", "The space around a magnet where its force acts is "
         "its magnetic field."),
    ], notes="Laws of magnetism: like poles repel, unlike attract. Repulsion is "
             "the only sure test of magnetism. Introduce the field.")
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
    b.cards("CARE & USES", "Caring for Magnets and Their Uses", [
        ("Store in pairs", "Keep bar magnets in pairs with unlike poles "
         "together and soft-iron keepers across the ends."),
        ("Handle gently", "Do not heat, hammer or drop a magnet — it loses its "
         "magnetism."),
        ("Everyday uses", "Compass, fridge and cupboard doors, pencil boxes and "
         "pin holders use magnets."),
        ("In machines", "Electromagnets work in electric bells, cranes, "
         "loudspeakers and MRI machines."),
    ], notes="Care: store in pairs with keepers, avoid heat/shock. Uses: from "
             "the compass and fridge doors to electromagnets in bells, cranes "
             "and MRI.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Magnetic", "iron, nickel, cobalt are attracted"),
        ("Poles", "every magnet has N and S; strongest there"),
        ("Free magnet", "rests pointing north–south"),
        ("Laws", "like poles repel, unlike attract"),
        ("Making", "stroke iron one way, again and again"),
        ("Care", "store in pairs; no heat, hammering or dropping"),
    ], notes="Recap magnetic materials, poles, the laws, making a magnet and "
             "caring for it.")
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

    b.title("Std 6 • General Science • Astronomy", "The Universe",
            "The universe  •  Galaxies  •  Stars and the Sun  •  Our solar "
            "system", img=milky)
    b.objectives([
        "Describe what the universe contains",
        "Explain what a galaxy is and name its shapes",
        "Describe stars and where they are born",
        "Name the Sun as our nearest star",
        "List the members of the solar system",
        "Name the eight planets in order from the Sun",
    ])

    b.divider(1, "Part 1", "The Universe and Galaxies",
              "Everything there is, and the great islands of stars")
    b.text_image("THE UNIVERSE", "The Universe",
                 ["The universe is everything that exists — all of space and "
                  "all it holds.",
                  "It contains countless stars, planets, gas and dust.",
                  "Distances in it are so huge we measure them in light "
                  "years.",
                  "A light year is the distance light travels in one year."],
                 milky, img_side="right", panel_title="Everything there is",
                 caption="The Milky Way arching over Earth",
                 notes="Set the scale of the universe and introduce the light "
                       "year as the unit of astronomical distance.")
    b.text_image("GALAXIES", "Galaxies",
                 ["A galaxy is a group of countless stars and their planetary "
                  "systems.",
                  "Gravity holds all the stars, gas and dust together.",
                  "Galaxies have shapes — spiral, elliptical, barred spiral and "
                  "irregular.",
                  "Our galaxy is the Milky Way; Andromeda is the nearest to "
                  "it."],
                 galaxy, img_side="left", panel_title="Islands of stars",
                 caption="A spiral galaxy",
                 notes="A galaxy is a gravitationally bound group of countless "
                       "stars. Name the four shapes; ours is the Milky Way, "
                       "with Andromeda nearest.")
    b.text_image("NEBULA", "Nebulae — Where Stars are Born",
                 ["A nebula is a vast cloud of gas and dust in space.",
                  "Under gravity, parts of it clump together and heat up.",
                  "When hot and dense enough, a new star begins to shine.",
                  "So the huge nebulae are the birthplaces of stars."],
                 nebula, img_side="right", panel_title="Clouds of gas & dust",
                 caption="A star-forming nebula",
                 notes="Nebulae are the birthplaces of stars — a real NASA "
                       "image gives a sense of their scale and colour.")

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

    b.divider(2, "Part 2", "Stars, the Sun and the Solar System",
              "Our own star and its family")
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
    b.text_image("SOLAR SYSTEM", "Our Solar System",
                 ["The solar system is the Sun and everything that orbits it.",
                  "Eight planets travel around the Sun in fixed paths.",
                  "In order from the Sun: Mercury, Venus, Earth, Mars, "
                  "Jupiter, Saturn, Uranus, Neptune.",
                  "Asteroids, comets and moons are also part of the family."],
                 solar, img_side="right", img_w=5.8, img_h=2.7,
                 panel_title="The Sun's family",
                 caption="The Sun and its eight planets",
                 notes="The solar system = the Sun plus all that orbits it. "
                       "Name the eight planets in order; add asteroids, comets "
                       "and moons.")
    b.cards("OTHER BODIES", "Other Members of the Solar System", [
        ("Satellites (moons)", "Natural satellites orbit planets — the Moon "
         "orbits the Earth."),
        ("Asteroids", "Small rocky bodies, most orbiting in a belt between Mars "
         "and Jupiter."),
        ("Comets", "Icy bodies that grow a bright glowing tail when they come "
         "near the Sun."),
        ("Meteors", "Bits of rock that burn up in our air as a bright streak — "
         "a 'shooting star'."),
    ], notes="Round out the solar-system family: moons, asteroids, comets and "
             "meteors, with a familiar example of each.")

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
