"""
Maharashtra Board (MSBSHSE) — Standard 7 Physics teaching decks.

Physics chapters from the tuitions planner (after session 25 scope, plus the
earlier Heat session requested): Heat (S22/S23), Effects of Light (S27),
Sound (S51), Properties of a Magnetic Field (S59) and In the World of Stars
(S67).

These are full teaching decks: each has 20 concept slides (ten per part) that
go into detail — definitions, everyday examples, applications, comparisons and
diagrams — plus two moderate-to-difficult quizzes, a recap and a close.
Content covers the MSBSHSE Std 7 General Science textbook treatment (subtopics
checked against the Balbharati chapter scope), written in original teaching
language with the full detail carried in the speaker notes. Concise, visual
teaching style (mhstyle).

Images: physics schematics are clean vector diagrams; for the "very general"
astronomy visuals (Milky Way, a galaxy, a nebula, a star cluster) real
public-domain NASA reference photographs are used instead of hand-drawn art —
loaded from build/web/ when present (see tools/webimg.py) with a vector
fallback.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import diagrams_extra as DE
import diagrams_mh as DM
import mhstyle

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "MH_Grade07"))
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
# S22 — Heat
# ===========================================================================
def heat_deck():
    footer = "Heat  •  MSBSHSE Std 7 General Science"
    b = Builder(footer, accent=C["red"])
    states = b.asset("mh7_ht_states", D.states_of_matter("mh7_ht_states"))
    thermo = b.asset("mh7_ht_thermo", DM.thermometer("mh7_ht_thermo"))
    modes = b.asset("mh7_ht_modes", DM.heat_transfer_modes("mh7_ht_modes"))
    flask = b.asset("mh7_ht_flask", DM.thermos_flask("mh7_ht_flask"))

    b.title("Std 7 • General Science • Heat", "Heat",
            "Heat and temperature  •  Effects of heat  •  Conduction, "
            "convection and radiation", img=modes)
    b.objectives([
        "Explain heat as a form of energy and name its sources",
        "Tell heat apart from temperature",
        "Describe the effects of heat, including expansion",
        "Explain conduction, convection and radiation",
        "Give everyday uses of good and bad conductors",
        "Explain how a thermos (vacuum) flask keeps heat in",
    ])

    # ---- Part 1 : Heat, temperature and effects -----------------------------
    b.divider(1, "Part 1", "Heat, Temperature and Their Effects",
              "What heat is and what it does to matter")
    b.bullets("HEAT", "Heat and Temperature", [
        ("Heat is energy", "Heat is a form of energy that flows from a hotter "
         "body to a colder one."),
        ("Temperature", "Temperature tells us how hot or cold a body is; it is "
         "measured with a thermometer."),
        ("Not the same thing", "A cup and a bucket of water at the same "
         "temperature hold very different amounts of heat."),
        ("Units", "Temperature is measured in degrees Celsius (°C); heat is a "
         "form of energy, measured in joules."),
    ], notes="Heat is energy in transit; temperature is the degree of hotness. "
             "Separate the two with the cup-vs-bucket idea.")
    b.statement("HEAT FLOWS", "Heat Always Flows Hot → Cold",
                "Heat energy moves by itself from a hotter body to a colder "
                "one, until both reach the same temperature.",
                points=[
                    "Put a hot spoon in cold water — the spoon cools, the "
                    "water warms.",
                    "They stop changing when both are equally warm.",
                    "Heat never flows on its own from cold to hot.",
                ],
                notes="Establish the one-way, on-its-own flow of heat from hot "
                      "to cold until temperatures equalise (thermal "
                      "equilibrium).")
    b.cards("SOURCES", "Where Heat Comes From", [
        ("The Sun", "Our greatest natural source of heat energy."),
        ("Burning fuel", "Wood, gas and coal release heat when they burn."),
        ("Electricity", "Heaters, irons and geysers turn electricity into "
         "heat."),
        ("Friction", "Rubbing hands together warms them — friction makes "
         "heat."),
    ], notes="Name the everyday sources of heat: the Sun, fuels, electricity "
             "and friction.")
    b.text_image("EFFECTS OF HEAT", "What Heat Does to a Substance",
                 ["Raises temperature and makes molecules move faster.",
                  "Expands solids, liquids and gases (thermal expansion).",
                  "Can change the state — melting and boiling.",
                  "Gaps in railway lines and bridges allow for this "
                  "expansion."],
                 states, img_side="right", panel_title="Heat changes matter",
                 caption="Heating speeds up the molecules",
                 notes="List the effects of heat. Expansion and change of "
                       "state are the key ones; connect expansion to real "
                       "gaps left in rails and bridges.")
    b.bullets("EXPANSION", "Heat Makes Things Expand", [
        ("Solids expand", "A metal ball that just passes through a ring will "
         "not fit once heated."),
        ("Liquids expand", "Water and mercury rise up a tube when warmed."),
        ("Gases expand most", "Air expands the most of all when heated."),
        ("On cooling", "Everything contracts (shrinks) again as it cools "
         "down."),
    ], notes="Thermal expansion in all three states — solids least, gases "
             "most — and the reverse (contraction) on cooling.")
    b.cards("EXPANSION AT WORK", "Expansion in Everyday Life", [
        ("Railway gaps", "Small gaps let rails expand on a hot day without "
         "buckling."),
        ("Bridges", "Rollers and gaps let long bridges expand safely."),
        ("Overhead wires", "Wires are left slightly loose to allow for "
         "shrinking in winter."),
        ("Tight lids", "Warming a metal lid makes it expand and open more "
         "easily."),
    ], notes="Real engineering allowances for expansion — rail gaps, bridge "
             "rollers, sagging wires — plus the loosening-a-lid trick.")
    b.text_image("THERMOMETER", "Measuring Temperature",
                 ["A thermometer measures temperature.",
                  "Most use mercury, which expands evenly on heating.",
                  "The Celsius scale runs 0 °C (melting ice) to 100 °C "
                  "(boiling water).",
                  "A clinical thermometer reads body temperature (around "
                  "37 °C)."],
                 thermo, img_side="left", img_w=3.4, img_h=4.0,
                 panel_title="0 °C to 100 °C",
                 caption="Mercury expands up the fine tube",
                 notes="The thermometer works by the even expansion of "
                       "mercury. Mention the fixed points 0 °C and 100 °C.")
    b.cards("TYPES", "Kinds of Thermometers", [
        ("Laboratory", "Reads a wide range of temperatures for experiments."),
        ("Clinical", "Reads body temperature; has a kink to hold the "
         "reading."),
        ("Digital", "Shows the temperature as numbers on a screen."),
        ("Care", "Handle the glass gently and never shake a lab "
         "thermometer."),
    ], notes="Compare laboratory, clinical and digital thermometers, and note "
             "safe handling of the glass ones.")
    b.bullets("CHANGE OF STATE", "Heat Changes the State of Matter", [
        ("Melting", "A solid becomes a liquid on heating — ice to water."),
        ("Boiling", "A liquid becomes a gas on strong heating — water to "
         "steam."),
        ("Condensation", "A gas becomes a liquid on cooling — steam to "
         "water."),
        ("Freezing", "A liquid becomes a solid on cooling — water to ice."),
    ], notes="The changes of state driven by heating and cooling: melting, "
             "boiling, condensation and freezing.")
    b.statement("HEAT ≠ TEMPERATURE", "Heat and Temperature are Different",
                "Temperature is the degree of hotness; heat is the total "
                "energy. Two bodies at the same temperature can hold very "
                "different amounts of heat.",
                points=[
                    "A cup and a bucket of water may be equally warm.",
                    "The bucket holds far more water, so far more total "
                    "heat.",
                    "Temperature is 'how hot'; heat is 'how much energy'.",
                ],
                notes="Drive home the heat-vs-temperature distinction with the "
                      "cup-and-bucket example — same temperature, different "
                      "total heat.")

    b.quiz_intro("Quiz 1", "Check — Heat, Temperature & Effects", 4)
    b.quiz_q(1, "Flow of heat", "Heat always flows on its own from a body at:",
             ["Lower to higher temperature", "Higher to lower temperature",
              "Equal temperatures only", "Larger to smaller size"])
    b.quiz_a(1, "B. Higher to lower temperature",
             "Heat energy moves by itself from the hotter body to the colder "
             "one, until both reach the same temperature.")
    b.quiz_q(2, "Heat vs temperature", "A cup and a bucket of water are at the "
             "same temperature. Compared with the cup, the bucket has:",
             ["The same total heat", "More total heat energy",
              "Less total heat energy", "No heat at all"])
    b.quiz_a(2, "B. More total heat energy",
             "Temperature is the same, but the bucket holds far more water, so "
             "it contains much more total heat energy.")
    b.quiz_q(3, "Gaps in rails", "Small gaps are left between railway rails "
             "so that the rails can:", ["Contract in summer",
              "Expand in hot weather without buckling",
              "Carry more trains", "Stay cool"])
    b.quiz_a(3, "B. Expand in hot weather without buckling",
             "Metals expand when heated. The gaps give the rails room to "
             "expand on a hot day, so the track does not bend out of shape.")
    b.quiz_q(4, "Thermometer liquid", "Mercury is used in a common "
             "thermometer mainly because it:", ["Is cheap",
              "Expands evenly and is easily seen", "Freezes quickly",
              "Is a gas"])
    b.quiz_a(4, "B. Expands evenly and is easily seen",
             "Mercury expands uniformly with temperature and is shiny, so the "
             "thread is easy to read against the scale.")

    # ---- Part 2 : How heat travels ------------------------------------------
    b.divider(2, "Part 2", "How Heat Travels",
              "Conduction, convection and radiation")
    b.text_image("THREE MODES", "Conduction, Convection, Radiation",
                 ["Conduction: heat passes through a solid, particle to "
                  "particle.",
                  "Convection: hot liquid or gas rises and cold sinks, "
                  "carrying heat.",
                  "Radiation: heat travels as rays, needing no medium — as "
                  "from the Sun.",
                  "Metals are good conductors; air, wood and water are poor "
                  "conductors."],
                 modes, img_side="left", img_w=5.6, img_h=3.2,
                 panel_title="Solid • liquid/gas • no medium",
                 caption="Three ways heat moves",
                 notes="Contrast the three modes: conduction needs a solid "
                       "medium, convection needs a moving fluid, radiation "
                       "needs no medium at all.")
    b.bullets("CONDUCTION", "Heat by Conduction", [
        ("Through solids", "Heat passes from particle to particle without them "
         "moving away."),
        ("A metal spoon", "The end in hot tea soon warms the far end."),
        ("Good conductors", "Metals like copper and iron carry heat "
         "quickly."),
        ("Poor conductors", "Wood, plastic and air carry heat very slowly."),
    ], notes="Conduction: heat handed particle-to-particle through a solid. "
             "Metals conduct well; wood/plastic/air do not.")
    b.bullets("CONVECTION", "Heat by Convection", [
        ("In fluids", "Happens in liquids and gases, which can flow."),
        ("Hot rises", "Warm fluid becomes lighter and rises; cool fluid "
         "sinks."),
        ("A current forms", "This sets up a circulating convection current."),
        ("Sea & land breeze", "Day and night breezes at the coast are "
         "convection currents of air."),
    ], notes="Convection: heat carried by the bulk movement of a fluid. Use "
             "boiling water and sea/land breezes as examples.")
    b.bullets("RADIATION", "Heat by Radiation", [
        ("No medium needed", "Radiation can travel through empty space."),
        ("From the Sun", "The Sun's heat reaches us across empty space by "
         "radiation."),
        ("As rays", "It travels as invisible heat rays at the speed of "
         "light."),
        ("Dark vs shiny", "Dark, dull surfaces absorb radiation; shiny ones "
         "reflect it."),
    ], notes="Radiation needs no medium and reaches us from the Sun. Note that "
             "dark surfaces absorb and shiny surfaces reflect heat rays.")
    b.cards("CONDUCTORS", "Good and Poor Conductors in Daily Life", [
        ("Cooking pans", "Made of metal (good conductor) so heat reaches the "
         "food quickly."),
        ("Handles", "Made of wood or plastic (poor conductors) so they stay "
         "cool to hold."),
        ("Woollen clothes", "Trap air, a poor conductor, keeping body heat in "
         "during winter."),
        ("Sea breeze", "A day-time convection current of air from the cool sea "
         "to the warm land."),
    ], notes="Everyday examples of choosing conductors and insulators, plus "
             "convection in nature (land and sea breezes).")
    b.cards("INSULATORS", "Putting Poor Conductors to Work", [
        ("Warm clothing", "Wool and quilts trap air to hold in body heat."),
        ("Pot holders", "Cloth or wood protects our hands from hot vessels."),
        ("Double walls", "Air between walls keeps rooms and flasks warm."),
        ("Birds fluff up", "Fluffed feathers trap air and keep birds warm in "
         "winter."),
    ], notes="Poor conductors (insulators) at work — clothing, holders, "
             "double walls, even fluffed feathers — all trap air.")
    b.text_image("THERMOS FLASK", "The Vacuum (Thermos) Flask",
                 ["Keeps hot things hot and cold things cold.",
                  "A vacuum between double walls stops conduction and "
                  "convection.",
                  "Shiny silvered walls reflect heat back, stopping "
                  "radiation.",
                  "So all three ways of losing heat are blocked at once."],
                 flask, img_side="right", img_w=3.8, img_h=4.0,
                 panel_title="Blocks all three",
                 caption="Vacuum + silvered walls",
                 notes="The flask is the classic application: the vacuum stops "
                       "conduction/convection and the silvering stops "
                       "radiation.")
    b.bullets("HOW IT WORKS", "How the Flask Blocks Each Mode", [
        ("Vacuum gap", "The empty gap has no particles, so no conduction and "
         "no convection."),
        ("Silvered walls", "Shiny surfaces reflect heat rays back, stopping "
         "radiation."),
        ("Insulating stopper", "The cork or plastic cap stops heat escaping "
         "from the top."),
        ("Works both ways", "It keeps hot drinks hot and cold drinks cold "
         "alike."),
    ], notes="Break down the flask feature by feature against the three modes "
             "of heat transfer — a complete real-world design.")
    b.cards("APPLICATIONS", "Heat Transfer Around Us", [
        ("Cooking", "Metal pans conduct; boiling water convects the heat "
         "through."),
        ("Coastal climate", "Sea and land breezes are giant convection "
         "currents."),
        ("Room heater", "Warms the air, which convects around the room."),
        ("Sunlight", "Radiation warms the Earth from 150 million km away."),
    ], notes="A spread of applications tying each everyday case to conduction, "
             "convection or radiation.")
    b.statement("CHOOSING WISELY", "Choosing Conductors and Insulators",
                "We pick a good conductor where heat must pass quickly, and a "
                "poor conductor (insulator) where heat must be kept in or out.",
                points=[
                    "Cooking vessels — good conductors, for fast heating.",
                    "Handles and clothing — poor conductors, to block heat.",
                    "The right choice makes appliances safe and efficient.",
                ],
                notes="Sum up Part 2 by the design principle: match the "
                      "material's conducting ability to the job.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Heat", "a form of energy; flows hot → cold"),
        ("Temperature", "degree of hotness; measured in °C"),
        ("Effects", "expansion and change of state"),
        ("Conduction", "through solids, particle to particle"),
        ("Convection", "hot fluid rises, cold sinks"),
        ("Radiation", "heat rays, no medium needed"),
    ], notes="Rapid recap of heat, temperature and the three modes of "
             "transfer.")
    b.quiz_intro("Quiz 2", "Final Check — How Heat Travels", 4)
    b.quiz_q(1, "Mode in solids", "Heat travels through a metal spoon placed "
             "in hot tea mainly by:", ["Convection", "Radiation",
              "Conduction", "No transfer"])
    b.quiz_a(1, "C. Conduction",
             "In a solid, heat passes from particle to particle without the "
             "particles moving from place to place — this is conduction.")
    b.quiz_q(2, "Mode in fluids", "Water in a pan gets heated throughout "
             "mainly by:", ["Conduction", "Convection currents",
              "Radiation", "Reflection"])
    b.quiz_a(2, "B. Convection currents",
             "Hot water near the flame rises and cooler water sinks to take "
             "its place, setting up convection currents that heat all the "
             "water.")
    b.quiz_q(3, "No medium", "Heat from the Sun reaches the Earth through "
             "empty space by:", ["Conduction", "Convection", "Radiation",
              "Sound"])
    b.quiz_a(3, "C. Radiation",
             "There is no air in space, so the Sun's heat cannot travel by "
             "conduction or convection — it comes as radiation, which needs "
             "no medium.")
    b.quiz_q(4, "Woollen clothes", "Woollen clothes keep us warm in winter "
             "because the trapped air is:", ["A good conductor",
              "A poor conductor of heat", "A source of heat", "Very heavy"])
    b.quiz_a(4, "B. A poor conductor of heat",
             "Wool traps a lot of air, and air is a poor conductor, so it "
             "slows the escape of body heat and keeps us warm.")
    b.closing("Feeling the Warmth",
              "Heat is energy on the move — understanding how it flows lets us "
              "cook, stay warm, and keep a drink hot for hours.")
    return b


# ===========================================================================
# S27 — Effects of Light
# ===========================================================================
def light_deck():
    footer = "Effects of Light  •  MSBSHSE Std 7 General Science"
    b = Builder(footer, accent=C["orange"])
    rect = b.asset("mh7_li_rect", DE.rectilinear_propagation("mh7_li_rect"))
    shadow = b.asset("mh7_li_shadow", DE.shadow_formation("mh7_li_shadow"))
    solar = b.asset("mh7_li_solar", DE.solar_eclipse("mh7_li_solar"))
    lunar = b.asset("mh7_li_lunar", DE.lunar_eclipse("mh7_li_lunar"))
    scat = b.asset("mh7_li_scat", D.scattering("mh7_li_scat"))

    b.title("Std 7 • General Science • Light", "Effects of Light",
            "Light travels straight  •  Shadows  •  Scattering  •  Eclipses",
            img=shadow)
    b.objectives([
        "State that light travels in straight lines",
        "Explain how a shadow is formed",
        "Describe the scattering of light and a Zero Shadow Day",
        "Explain a solar eclipse and a lunar eclipse",
        "Tell apart the umbra and the penumbra",
        "Relate these effects to everyday sights",
    ])

    # ---- Part 1 : Straight-line light and shadows ---------------------------
    b.divider(1, "Part 1", "Straight-Line Light and Shadows",
              "Why opaque objects cast shadows")
    b.text_image("STRAIGHT LINE", "Light Travels in Straight Lines",
                 ["Light travels in straight lines, called rays.",
                  "We see this in a sunbeam through a gap or dusty air.",
                  "Because light goes straight, it cannot bend around a "
                  "corner.",
                  "This straight-line travel is what makes shadows form."],
                 rect, img_side="right", panel_title="Rectilinear propagation",
                 caption="A straight beam of light",
                 notes="Establish rectilinear propagation with the sunbeam "
                       "example — it is the reason shadows and eclipses "
                       "happen.")
    b.bullets("EVIDENCE", "How We Know Light Goes Straight", [
        ("A sunbeam", "A ray through a window or through leaves is dead "
         "straight."),
        ("Line up the holes", "You see a candle through three cards only when "
         "their holes are in line."),
        ("No seeing round corners", "We cannot see behind a wall — light will "
         "not bend to reach us."),
        ("Sharp shadow edges", "The clean edge of a shadow shows the light "
         "came straight."),
    ], notes="Classic evidence for rectilinear propagation — sunbeams, the "
             "three-card experiment, not seeing round corners, sharp shadows.")
    b.statement("LIGHT IS ENERGY", "Light is a Form of Energy",
                "Light is a form of energy that travels in straight lines and "
                "lets us see the world around us.",
                points=[
                    "It travels extremely fast — faster than anything else.",
                    "It can travel even through the vacuum of space.",
                    "That is how the Sun's light reaches the Earth.",
                ],
                notes="Frame light as a fast-travelling form of energy that, "
                      "unlike sound, can cross empty space.")
    b.text_image("SHADOWS", "How a Shadow Forms",
                 ["A shadow forms where an opaque object blocks the light.",
                  "Needs a light source, an opaque object and a screen.",
                  "The dark centre is the umbra; the lighter edge is the "
                  "penumbra.",
                  "The shadow's size changes with the distance from the "
                  "light."],
                 shadow, img_side="left", panel_title="Umbra & penumbra",
                 caption="Light blocked → shadow",
                 notes="A shadow needs source, opaque object and screen. "
                       "Distinguish the dark umbra from the softer penumbra.")
    b.bullets("UMBRA & PENUMBRA", "Two Parts of a Shadow", [
        ("Umbra", "The dark central region that gets no light at all."),
        ("Penumbra", "The lighter border that gets some light."),
        ("Small source", "A point source gives a sharp shadow, almost all "
         "umbra."),
        ("Large source", "A broad source gives a wide, soft penumbra."),
    ], notes="Define umbra (full shadow) and penumbra (partial), and how the "
             "size of the source changes their proportions.")
    b.bullets("WHAT IT NEEDS", "Three Things a Shadow Needs", [
        ("A light source", "The Sun, a lamp or a torch."),
        ("An opaque object", "Something that blocks the light."),
        ("A screen", "A wall or the ground for the shadow to fall on."),
        ("Straight light", "And, of course, light travelling in straight "
         "lines."),
    ], notes="A shadow needs a source, an opaque object and a screen — and the "
             "straight-line travel of light underlies it all.")
    b.cards("SHADOW FACTS", "More About Shadows", [
        ("Always dark", "A shadow is always black — it has no colour of its "
         "own."),
        ("Shape, not detail", "A shadow shows only the outline of an object, "
         "not its colour or features."),
        ("Changes through the day", "The Sun's changing position makes shadows "
         "long in the morning and short at noon."),
        ("Zero Shadow Day", "Twice a year in the tropics the noon Sun is "
         "overhead and vertical objects cast almost no shadow."),
    ], notes="Shadows are colourless outlines whose length changes with the "
             "Sun's height; Zero Shadow Day is the striking special case.")
    b.statement("ZERO SHADOW DAY", "The Day Shadows Disappear",
                "Twice a year in the tropics, the noon Sun stands exactly "
                "overhead, so a vertical object casts almost no shadow at all.",
                points=[
                    "The Sun's rays fall straight down along the object.",
                    "It happens only between the tropics, not everywhere.",
                    "The two dates depend on the place's latitude.",
                ],
                notes="Explain Zero Shadow Day: the overhead noon Sun means "
                      "vertical objects cast no shadow — a memorable tropical "
                      "event.")
    b.bullets("MATERIALS", "Transparent, Translucent, Opaque", [
        ("Transparent", "Lets light pass fully — clear glass, water; casts no "
         "real shadow."),
        ("Translucent", "Lets light pass partly — frosted glass; a faint "
         "shadow."),
        ("Opaque", "Blocks light fully — wood, metal; a clear, dark shadow."),
        ("Only opaque", "A sharp shadow needs an opaque object."),
    ], notes="Recall the three material types and connect them to shadow "
             "formation — only opaque objects give a clear shadow.")
    b.cards("SHADOWS IN LIFE", "Shadows Around Us", [
        ("The sundial", "Tells time from the moving shadow of a rod."),
        ("Shadow play", "Hand and puppet shadows on a lit screen."),
        ("Long and short", "Our shadow is long at dawn, short at noon."),
        ("Eclipses", "Even eclipses are giant shadows cast in space."),
    ], notes="Everyday and dramatic shadows — sundial, shadow play, our "
             "changing shadow, and eclipses — bridging into Part 2.")

    b.quiz_intro("Quiz 1", "Check — Straight Light & Shadows", 4)
    b.quiz_q(1, "Why shadows", "Shadows are formed because light:",
             ["Bends around objects", "Travels in straight lines and is "
              "blocked", "Is very fast", "Changes colour"])
    b.quiz_a(1, "B. Travels in straight lines and is blocked",
             "Because light travels straight, it cannot go around an opaque "
             "object, so a dark shadow forms behind it.")
    b.quiz_q(2, "Umbra", "The dark, fully shadowed central part of a shadow is "
             "called the:", ["Penumbra", "Umbra", "Corona", "Ray"])
    b.quiz_a(2, "B. Umbra",
             "The umbra is the central region that receives no light at all; "
             "the lighter border around it is the penumbra.")
    b.quiz_q(3, "Shadow colour", "The colour of a shadow is always:",
             ["The colour of the object", "Black", "White", "Red"])
    b.quiz_a(3, "B. Black",
             "A shadow is simply a region where light is blocked, so it is "
             "always dark (black), whatever the colour of the object.")
    b.quiz_q(4, "Zero Shadow Day", "On a Zero Shadow Day, a vertical pole "
             "casts almost no shadow at noon because the Sun is:",
             ["Below the horizon", "Exactly overhead",
              "Very far away", "Behind a cloud"])
    b.quiz_a(4, "B. Exactly overhead",
             "When the noon Sun is directly overhead, its rays fall straight "
             "down along a vertical object, so almost no shadow is cast.")

    # ---- Part 2 : Scattering and eclipses -----------------------------------
    b.divider(2, "Part 2", "Scattering and Eclipses",
              "The blue sky and the shadows of worlds")
    b.text_image("SCATTERING", "Scattering of Light",
                 ["Tiny particles in the air scatter sunlight in all "
                  "directions.",
                  "Blue light scatters the most, so the sky looks blue.",
                  "At sunrise and sunset the Sun looks red, as blue is "
                  "scattered away.",
                  "Scattering is why we see a beam of light in dusty or misty "
                  "air."],
                 scat, img_side="right", panel_title="Why the sky is blue",
                 caption="Air scatters blue light most",
                 notes="Scattering by air molecules makes the sky blue and "
                       "sunsets red. A dusty beam is scattered light reaching "
                       "our eyes.")
    b.bullets("BLUE SKY, RED SUN", "What Scattering Explains", [
        ("Blue sky", "Air scatters blue light most, so the whole sky glows "
         "blue."),
        ("Red sunrise/sunset", "Light travels far through air; blue is "
         "scattered away, leaving red."),
        ("White clouds", "Larger water drops scatter all colours together, so "
         "clouds look white."),
        ("A visible beam", "Dust or mist scatters a torch beam so we can see "
         "its path."),
    ], notes="Scattering explains a family of everyday sights — blue sky, red "
             "sunsets, white clouds and visible dusty beams.")
    b.cards("SCATTERING IN LIFE", "Seeing Scattering Around Us", [
        ("Daytime sky", "Blue overhead because blue scatters most."),
        ("Evening sky", "Orange and red as the Sun sinks low."),
        ("Foggy headlights", "Beams light up the fog by scattering."),
        ("Hazy hills", "Distant hills look bluish through scattered light."),
    ], notes="More scenes where scattering is at work, reinforcing the idea "
             "with familiar observations.")
    b.text_image("SOLAR ECLIPSE", "Solar Eclipse",
                 ["Happens on a new-moon day when the Moon comes between the "
                  "Sun and the Earth.",
                  "The Moon's shadow falls on the Earth, hiding the Sun.",
                  "Seen only from the small region in the Moon's shadow.",
                  "Never look at a solar eclipse with bare eyes."],
                 solar, img_side="left", panel_title="Moon between Sun & Earth",
                 caption="The Moon hides the Sun",
                 notes="Solar eclipse: Sun–Moon–Earth in line at new moon. "
                       "Stress the safety warning about never looking "
                       "directly.")
    b.bullets("SOLAR DETAILS", "More on the Solar Eclipse", [
        ("Only at new moon", "The Moon must lie exactly between the Sun and "
         "Earth."),
        ("A small shadow", "Only places in the Moon's shadow see it."),
        ("Total or partial", "The Sun may be fully or only partly hidden."),
        ("Never look directly", "Use a proper filter — bare eyes can be "
         "harmed."),
    ], notes="Details of the solar eclipse — its timing, the small viewing "
             "region, total/partial, and the crucial safety rule.")
    b.text_image("LUNAR ECLIPSE", "Lunar Eclipse",
                 ["Happens on a full-moon day when the Earth comes between the "
                  "Sun and the Moon.",
                  "The Earth's shadow falls on the Moon.",
                  "The Moon dims and can look coppery-red.",
                  "It is quite safe to watch a lunar eclipse."],
                 lunar, img_side="right", panel_title="Earth between Sun & Moon",
                 caption="Earth's shadow on the Moon",
                 notes="Lunar eclipse: Sun–Earth–Moon in line at full moon. "
                       "Contrast the geometry and the safety with the solar "
                       "eclipse.")
    b.bullets("LUNAR DETAILS", "More on the Lunar Eclipse", [
        ("Only at full moon", "The Earth must lie between the Sun and the "
         "Moon."),
        ("A big shadow", "The Earth's shadow is large, so many people see "
         "it."),
        ("Coppery Moon", "Bent red light gives the Moon a coppery glow."),
        ("Safe to watch", "No harm in watching a lunar eclipse with bare "
         "eyes."),
    ], notes="Details of the lunar eclipse — its timing, the wide viewing "
             "region, the red colour, and that it is safe to watch.")
    b.cards("COMPARE", "Solar vs Lunar Eclipse", [
        ("When", "Solar at new moon; lunar at full moon."),
        ("Line-up", "Sun–Moon–Earth (solar); Sun–Earth–Moon (lunar)."),
        ("Seen by", "Solar from a small area; lunar from a wide area."),
        ("Safety", "Never watch a solar eclipse directly; a lunar one is "
         "safe."),
    ], notes="A side-by-side comparison of the two eclipses across timing, "
             "geometry, viewing region and safety.")
    b.statement("EYE SAFETY", "Watching Eclipses Safely",
                "Never look at a solar eclipse with bare eyes or through "
                "ordinary glasses — the Sun's light can permanently harm the "
                "eyes.",
                points=[
                    "Use special eclipse glasses or a pinhole projection.",
                    "A lunar eclipse, by contrast, is perfectly safe to "
                    "watch.",
                    "When in doubt, view the Sun only indirectly.",
                ],
                notes="A dedicated safety slide — the single most important "
                      "practical message of the eclipse topic.")

    b.bullets("KINDS OF SOLAR", "Kinds of Solar Eclipse", [
        ("Total", "The Moon hides the Sun completely for a short while."),
        ("Partial", "The Moon covers only a part of the Sun's disc."),
        ("Annular", "The Moon looks small and leaves a bright ring of Sun."),
        ("Where you stand", "Which kind you see depends on your place in the "
         "shadow."),
    ], notes="The three kinds of solar eclipse — total, partial and annular — "
             "and that what you see depends on where you are.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Straight light", "light travels in straight-line rays"),
        ("Shadow", "opaque object blocks light; umbra + penumbra"),
        ("Scattering", "air scatters blue most → blue sky, red sunset"),
        ("Zero Shadow Day", "overhead noon Sun → no shadow"),
        ("Solar eclipse", "new moon; Moon hides the Sun"),
        ("Lunar eclipse", "full moon; Earth's shadow on the Moon"),
    ], notes="Recap the effects of light from straight-line travel through to "
             "the two eclipses.")
    b.quiz_intro("Quiz 2", "Final Check — Scattering & Eclipses", 4)
    b.quiz_q(1, "Blue sky", "The sky looks blue during the day because air "
             "particles scatter:", ["Red light most", "Blue light most",
              "All colours equally", "No light"])
    b.quiz_a(1, "B. Blue light most",
             "Blue light is scattered far more than the other colours by the "
             "tiny particles in the air, so the sky all around us looks blue.")
    b.quiz_q(2, "Red sunset", "The Sun looks red at sunset because the blue "
             "light has been:", ["Absorbed by the Sun",
              "Scattered away, leaving red to reach us", "Reflected by the "
              "Moon", "Turned into heat"])
    b.quiz_a(2, "B. Scattered away, leaving red to reach us",
             "At sunset the light travels a long way through air; most of the "
             "blue is scattered out, so mainly red light reaches our eyes.")
    b.quiz_q(3, "Solar eclipse", "A solar eclipse can happen only on a:",
             ["Full-moon day", "New-moon day", "Half-moon day", "Cloudy day"])
    b.quiz_a(3, "B. New-moon day",
             "A solar eclipse needs the Moon between the Sun and Earth, which "
             "only happens at new moon.")
    b.quiz_q(4, "Lunar eclipse", "During a lunar eclipse, the Moon is dark "
             "because it lies in the shadow of the:", ["Sun", "Earth",
              "Clouds", "Another planet"])
    b.quiz_a(4, "B. Earth",
             "At full moon the Earth can come between the Sun and Moon, so the "
             "Earth's shadow falls on the Moon and dims it.")
    b.closing("Light, Shadow and Sky",
              "From the blue of the sky to the shadow of the Moon, the simple "
              "fact that light travels straight explains it all.")
    return b


# ===========================================================================
# S51 — Sound
# ===========================================================================
def sound_deck():
    footer = "Sound  •  MSBSHSE Std 7 General Science"
    b = Builder(footer, accent=C["purple"])
    longw = b.asset("mh7_sd_long", D.longitudinal_wave("mh7_sd_long"))
    chars = b.asset("mh7_sd_char", D.sound_characteristics("mh7_sd_char"))
    osc = b.asset("mh7_sd_osc", D.resonance_pendulums("mh7_sd_osc"))

    b.title("Std 7 • General Science • Sound", "Sound",
            "How sound is made  •  Oscillations  •  How it travels  •  "
            "Characteristics of sound", img=longw)
    b.objectives([
        "Explain that sound is produced by vibrations",
        "Define oscillation, time period and frequency",
        "Describe how sound travels as a wave through a medium",
        "State that sound needs a medium and cannot travel in vacuum",
        "Explain pitch, loudness and quality of sound",
        "Tell apart a musical sound and noise",
    ])

    # ---- Part 1 : Making sound and how it travels ---------------------------
    b.divider(1, "Part 1", "Making Sound and How It Travels",
              "Vibrations, oscillations and the sound wave")
    b.bullets("PRODUCTION", "Sound is Made by Vibrations", [
        ("Vibrating bodies", "Every sound is produced by a vibrating object — "
         "a drum, a string, our vocal cords."),
        ("Oscillation", "One complete to-and-fro movement of a vibrating body "
         "is an oscillation."),
        ("Time period", "The time taken for one oscillation is the time "
         "period."),
        ("Frequency", "The number of oscillations in one second is the "
         "frequency, measured in hertz (Hz)."),
    ], notes="Sound starts with a vibration. Define oscillation, time period "
             "and frequency carefully — frequency = oscillations per second.")
    b.statement("KEY IDEA", "No Vibration, No Sound",
                "A body makes a sound only while it is vibrating. Stop the "
                "vibration and the sound stops at once.",
                points=[
                    "Pluck a stretched wire — it hums while it quivers.",
                    "Touch it to still it, and the sound dies instantly.",
                    "Every source of sound, without exception, is vibrating.",
                ],
                notes="Reinforce the tight link between vibration and sound: "
                      "damping the vibration kills the sound immediately.")
    b.bullets("OSCILLATION TERMS", "Oscillation, Time Period, Frequency", [
        ("Oscillation", "One full to-and-fro swing of the vibrating body."),
        ("Time period", "The time for a single oscillation, in seconds."),
        ("Frequency", "How many oscillations happen in one second (in Hz)."),
        ("They are linked", "Frequency = 1 ÷ time period; faster swings, "
         "higher frequency."),
    ], notes="Carefully lay out the three linked quantities. If a body makes 2 "
             "oscillations per second, its time period is 0.5 s.")
    b.text_image("OSCILLATION", "Oscillatory Motion",
                 ["A swing and a pendulum show oscillatory motion.",
                  "The to-and-fro repeats over equal time periods.",
                  "A faster oscillation means a higher frequency.",
                  "Vibrations too fast to see still make the air carry "
                  "sound."],
                 osc, img_side="left", panel_title="To and fro, again and "
                 "again", caption="Pendulums keeping time",
                 notes="Use the familiar pendulum/swing to make oscillation, "
                       "time period and frequency concrete.")
    b.text_image("PROPAGATION", "How Sound Travels",
                 ["A vibrating body pushes and pulls the air around it.",
                  "This makes the air compress and stretch — a sound wave.",
                  "The wave carries energy outward to our ears.",
                  "Sound needs a medium — it cannot travel through a "
                  "vacuum."],
                 longw, img_side="right", panel_title="A wave through matter",
                 caption="Compressions and rarefactions",
                 notes="Sound travels as a longitudinal wave of compressions "
                       "and rarefactions. A key point: no medium, no sound.")
    b.bullets("THE MEDIUM", "Sound Needs a Medium", [
        ("A material to travel", "Sound travels through a solid, a liquid or a "
         "gas."),
        ("Air, water, solids", "We hear through air; fish hear through water; "
         "sound passes through walls."),
        ("Passes it on", "Particles pass the vibration from one to the next."),
        ("No particles, no sound", "With nothing to carry it, sound cannot "
         "travel."),
    ], notes="Sound needs a material medium whose particles pass the vibration "
             "along — air, water or solids all work.")
    b.statement("VACUUM", "No Sound in a Vacuum",
                "A vacuum is empty space with no particles, so there is nothing "
                "to carry a sound — a vacuum is completely silent.",
                points=[
                    "In a bell-jar, the ringing fades as the air is pumped "
                    "out.",
                    "Outer space is a vacuum, so it is utterly silent.",
                    "This is the great difference between sound and light.",
                ],
                notes="Drive home that sound, unlike light, cannot cross a "
                      "vacuum — hence the silence of space.")
    b.cards("SPEED", "How Fast Sound Travels", [
        ("Fastest in solids", "Closely-packed particles pass the vibration on "
         "quickest."),
        ("Slower in liquids", "Particles a little farther apart, so sound is "
         "slower."),
        ("Slowest in gases", "Particles far apart in air, so sound is "
         "slowest."),
        ("Slower than light", "We see lightning before we hear the thunder."),
    ], notes="Sound is fastest in solids, slowest in gases, and much slower "
             "than light — hence the lightning-then-thunder gap.")
    b.bullets("HUMAN VOICE", "How We Make Sound", [
        ("The larynx", "Our voice box sits at the top of the windpipe."),
        ("Vocal cords", "Air from the lungs makes two vocal cords vibrate."),
        ("Shaping speech", "The mouth, tongue and lips shape it into words."),
        ("Pitch of voice", "Tighter cords vibrate faster, giving a higher "
         "voice."),
    ], notes="Explain human sound production through the vibrating vocal cords "
             "and how the mouth shapes it into speech.")
    b.cards("THE EAR", "How We Hear", [
        ("Outer ear", "Collects sound and funnels it inward."),
        ("Eardrum", "A thin skin that vibrates with the incoming sound."),
        ("Middle ear", "Tiny bones pass the vibrations further in."),
        ("Inner ear", "Sends the signal to the brain, and we hear."),
    ], notes="Trace sound through the ear — outer ear, eardrum, middle-ear "
             "bones, inner ear, brain.")

    b.quiz_intro("Quiz 1", "Check — Producing & Carrying Sound", 4)
    b.quiz_q(1, "Source of sound", "Sound is always produced by a body "
             "that is:", ["Hot", "Vibrating", "Coloured", "Heavy"])
    b.quiz_a(1, "B. Vibrating",
             "Every sound comes from a vibrating object; when the vibration "
             "stops, the sound stops too.")
    b.quiz_q(2, "Frequency", "The number of oscillations made in one second "
             "is called the:", ["Time period", "Frequency", "Amplitude",
              "Wavelength"])
    b.quiz_a(2, "B. Frequency",
             "Frequency is the number of oscillations per second, measured in "
             "hertz (Hz). Its opposite, the time for one oscillation, is the "
             "time period.")
    b.quiz_q(3, "Needs a medium", "Sound cannot travel through:",
             ["Air", "Water", "Iron", "A vacuum"])
    b.quiz_a(3, "D. A vacuum",
             "Sound needs particles of a medium to pass on the vibrations. A "
             "vacuum has no particles, so sound cannot travel through it.")
    b.quiz_q(4, "Time period", "If a pendulum makes 2 oscillations each "
             "second, its time period is:", ["2 s", "1 s", "0.5 s", "4 s"])
    b.quiz_a(4, "C. 0.5 s",
             "Time period = 1 / frequency = 1 / 2 = 0.5 s. Two oscillations a "
             "second means each one takes half a second.")

    # ---- Part 2 : Characteristics of sound ----------------------------------
    b.divider(2, "Part 2", "The Characteristics of Sound",
              "Pitch, loudness, quality — and music versus noise")
    b.text_image("CHARACTERISTICS", "Pitch, Loudness and Quality",
                 ["Pitch depends on frequency — faster vibration, higher "
                  "pitch.",
                  "Loudness depends on the size (amplitude) of the "
                  "vibration.",
                  "Quality lets us tell a violin from a flute at the same "
                  "note.",
                  "Together they describe every sound we hear."],
                 chars, img_side="right", panel_title="Three qualities",
                 caption="What makes sounds differ",
                 notes="Pitch ← frequency; loudness ← amplitude; quality "
                       "(timbre) distinguishes instruments. These are the "
                       "three characteristics of a sound.")
    b.bullets("PITCH", "Pitch — How High or Low", [
        ("Set by frequency", "A faster vibration gives a higher pitch."),
        ("High pitch", "A whistle and a small bird's chirp are high-pitched."),
        ("Low pitch", "A drum and a lion's roar are low-pitched."),
        ("Shorter, tighter", "Shorter or tighter strings vibrate faster and "
         "sound higher."),
    ], notes="Pitch is decided by frequency — high pitch from fast vibrations, "
             "low pitch from slow ones.")
    b.bullets("LOUDNESS", "Loudness — How Strong", [
        ("Set by amplitude", "A bigger to-and-fro (amplitude) gives a louder "
         "sound."),
        ("More energy", "A louder sound simply carries more energy."),
        ("Hit harder", "Strike a drum harder and it booms louder."),
        ("Fades with distance", "Loudness drops as the sound spreads out."),
    ], notes="Loudness is decided by amplitude and the energy carried; it "
             "grows with a harder push and fades with distance.")
    b.bullets("QUALITY", "Quality (Timbre) — the Character", [
        ("Tells sources apart", "It lets us tell a flute from a violin at the "
         "same note."),
        ("Same pitch, different feel", "Two instruments can share a pitch yet "
         "sound different."),
        ("Recognising voices", "It is how we know a friend's voice on the "
         "phone."),
        ("Unique blend", "Each source adds its own mix of tones."),
    ], notes="Quality (timbre) is the character of a sound that distinguishes "
             "sources at the same pitch and loudness.")
    b.cards("AUDIBLE RANGE", "What We Can and Cannot Hear", [
        ("Audible range", "Humans hear about 20 Hz to 20,000 Hz."),
        ("Infrasound", "Below 20 Hz — too low for us; some animals feel it."),
        ("Ultrasound", "Above 20,000 Hz — too high for us; bats and dogs hear "
         "it."),
        ("With age", "The top of our range drops as we grow older."),
    ], notes="Introduce the audible range and the inaudible infrasound and "
             "ultrasound that some animals can sense.")
    b.cards("MUSIC & NOISE", "Musical Sound and Noise", [
        ("Musical sound", "A pleasant, regular sound with a steady pattern — "
         "like a flute or a tuned string."),
        ("Noise", "An unpleasant, irregular sound with no steady pattern — "
         "like a horn or a crash."),
        ("Audible range", "Humans hear roughly 20 Hz to 20,000 Hz; below and "
         "above we cannot hear."),
        ("Sound pollution", "Too much loud noise harms hearing and health — a "
         "form of pollution to control."),
    ], notes="Music is regular and pleasant; noise is irregular. Note the "
             "audible range and the harm of sound (noise) pollution.")
    b.cards("NOISE SOURCES", "Where Noise Comes From", [
        ("Traffic", "Vehicle horns and roaring engines."),
        ("Loudspeakers", "Very loud music at events."),
        ("Machines", "Factories, generators and construction sites."),
        ("Crackers", "Sudden, very loud bangs."),
    ], notes="Common human-made sources of noise pollution, worst in crowded "
             "cities.")
    b.bullets("HARM OF NOISE", "Why Noise Pollution is Harmful", [
        ("Hearing damage", "Very loud sound can dull or damage hearing."),
        ("Sleep and rest", "Continuous noise disturbs sleep and rest."),
        ("Stress", "It causes headaches, tiredness and irritation."),
        ("Poor focus", "It makes studying and concentrating harder."),
    ], notes="The health effects of noise pollution — hearing damage, disturbed "
             "sleep, stress and poor concentration.")
    b.bullets("REDUCING NOISE", "Controlling Sound Pollution", [
        ("Quieter machines", "Well-maintained, quieter engines and horns cut "
         "noise at the source."),
        ("Green cover", "Trees along roads absorb and block a lot of noise."),
        ("Quiet zones", "No-horn zones near hospitals and schools protect "
         "people."),
        ("Personal care", "Avoiding very loud music protects our own "
         "hearing."),
    ], notes="Practical ways to reduce noise pollution — source control, green "
             "belts, silence zones and personal habits.")

    b.statement("SOUND IS ENERGY", "Sound Carries Energy",
                "Sound is a form of energy — the vibrating source hands its "
                "energy to the medium, which carries it to our ears.",
                points=[
                    "A very loud sound can rattle windows and shake our "
                    "chest.",
                    "The energy spreads outward in all directions as a wave.",
                    "It grows fainter with distance as the energy spreads "
                    "thin.",
                ],
                notes="Frame sound as a form of energy — it can do work "
                      "(rattle windows), spreads outward, and weakens with "
                      "distance.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Production", "sound comes from vibrations"),
        ("Oscillation", "one to-and-fro; time period and frequency"),
        ("Propagation", "a wave through a medium; none in vacuum"),
        ("Pitch", "higher frequency → higher pitch"),
        ("Loudness", "bigger amplitude → louder"),
        ("Music vs noise", "regular & pleasant vs irregular & harsh"),
    ], notes="Recap production, propagation and the characteristics of "
             "sound.")
    b.quiz_intro("Quiz 2", "Final Check — Characteristics of Sound", 4)
    b.quiz_q(1, "Pitch", "The pitch of a sound is decided mainly by its:",
             ["Amplitude", "Frequency", "Loudness", "Quality"])
    b.quiz_a(1, "B. Frequency",
             "A higher frequency of vibration gives a higher pitch. Amplitude "
             "affects loudness, not pitch.")
    b.quiz_q(2, "Loudness", "The loudness of a sound depends on the ___ of the "
             "vibration.", ["Frequency", "Amplitude (size)", "Colour",
              "Pitch"])
    b.quiz_a(2, "B. Amplitude (size)",
             "The larger the amplitude of the vibration, the more energy the "
             "wave carries and the louder the sound.")
    b.quiz_q(3, "Audible range", "The usual range of frequencies a human can "
             "hear is about:", ["2 Hz to 200 Hz", "20 Hz to 20,000 Hz",
              "20,000 Hz to 40,000 Hz", "0 Hz to 10 Hz"])
    b.quiz_a(3, "B. 20 Hz to 20,000 Hz",
             "Human ears can normally hear sounds between about 20 Hz and "
             "20,000 Hz; sounds outside this range are inaudible to us.")
    b.quiz_q(4, "Music vs noise", "Which of these is the best description of "
             "a musical sound?", ["Loud and sudden",
              "Regular, pleasant and with a steady pattern",
              "Irregular and harsh", "Always very soft"])
    b.quiz_a(4, "B. Regular, pleasant and with a steady pattern",
             "A musical sound has regular, repeating vibrations that are "
             "pleasant to hear, unlike the irregular pattern of noise.")
    b.closing("The World of Sound",
              "From a whisper to a song, every sound is a vibration set "
              "travelling — and knowing how helps us enjoy it and tame its "
              "noise.")
    return b


# ===========================================================================
# S59 — Properties of a Magnetic Field
# ===========================================================================
def magnet_deck():
    footer = "Properties of a Magnetic Field  •  MSBSHSE Std 7 General Science"
    b = Builder(footer, accent=C["teal"])
    field = b.asset("mh7_mg_field", DE.bar_magnet_field("mh7_mg_field"))
    poles = b.asset("mh7_mg_poles", DE.like_unlike_poles("mh7_mg_poles"))
    emag = b.asset("mh7_mg_emag", DE.electromagnet("mh7_mg_emag"))
    earth = b.asset("mh7_mg_earth", DE.earths_magnetism("mh7_mg_earth"))

    b.title("Std 7 • General Science • Magnetism",
            "Properties of a Magnetic Field",
            "Magnetic field  •  Lines of force  •  Poles  •  The Earth as a "
            "magnet", img=field)
    b.objectives([
        "Describe the magnetic field around a magnet",
        "Draw and read magnetic lines of force",
        "State the properties of magnetic field lines",
        "Explain the force between like and unlike poles",
        "Describe an electromagnet and its uses",
        "Explain the Earth's magnetism and the compass",
    ])

    # ---- Part 1 : The magnetic field and its lines --------------------------
    b.divider(1, "Part 1", "The Magnetic Field and Its Lines",
              "The invisible region of force around a magnet")
    b.text_image("MAGNETIC FIELD", "The Field Around a Magnet",
                 ["The region around a magnet where its force is felt is the "
                  "magnetic field.",
                  "Iron filings near a magnet line up along curved paths.",
                  "These paths are the magnetic lines of force.",
                  "The field is strongest near the poles."],
                 field, img_side="right", panel_title="Lines of force",
                 caption="Iron filings reveal the field",
                 notes="The magnetic field is the region of influence around a "
                       "magnet; iron filings map it as lines of force, densest "
                       "at the poles.")
    b.bullets("PROPERTIES", "Properties of Magnetic Field Lines", [
        ("Come out of N, into S", "Outside the magnet the lines run from the "
         "north pole to the south pole."),
        ("Closed loops", "Each line is a closed curve, continuing inside the "
         "magnet from S to N."),
        ("Never cross", "Two field lines never intersect one another."),
        ("Crowded = strong", "Where the lines are close together the field is "
         "strong — near the poles."),
    ], notes="The four standard properties of field lines. 'Never cross' and "
             "'crowded means strong' are the commonly tested ones.")
    b.bullets("MAPPING", "Mapping the Field with Iron Filings", [
        ("Sprinkle filings", "Scatter iron filings on a card over a magnet."),
        ("Tap gently", "A light tap lets them line up along the field."),
        ("A pattern appears", "They form curved lines from pole to pole."),
        ("Or use a compass", "A small compass shows the field's direction at "
         "each point."),
    ], notes="Two ways to reveal the field — iron filings for the pattern and "
             "a plotting compass for the direction.")
    b.text_image("POLES", "Force Between Poles",
                 ["Every magnet has two poles — north and south.",
                  "Like poles (N–N or S–S) repel each other.",
                  "Unlike poles (N–S) attract each other.",
                  "A freely hung magnet always rests pointing north–south."],
                 poles, img_side="left", panel_title="Like repel, unlike "
                 "attract", caption="The basic law of magnets",
                 notes="State the law of magnetic poles and the fact that a "
                       "free magnet aligns north–south — the basis of the "
                       "compass.")
    b.bullets("POLES & FREE MAGNET", "Poles and the Free Magnet", [
        ("Two poles", "Every magnet has a north and a south pole."),
        ("Like repel", "N–N and S–S push each other apart."),
        ("Unlike attract", "N–S pull towards each other."),
        ("Rests north–south", "A freely hung magnet always settles pointing "
         "north–south."),
    ], notes="Summarise the pole law and the directive property that a free "
             "magnet aligns north–south.")
    b.statement("SURE TEST", "Repulsion is the Real Test",
                "A magnet attracts plain iron too, so attraction is not proof. "
                "Only repulsion proves that both objects are magnets.",
                points=[
                    "If two bars attract, one might just be soft iron.",
                    "If two bars repel, both must certainly be magnets.",
                    "So repulsion is the sure test of magnetism.",
                ],
                notes="The classic subtlety: attraction can be due to ordinary "
                      "iron, so only mutual repulsion proves magnetism.")
    b.cards("TYPES OF MAGNETS", "Kinds of Magnets", [
        ("Bar magnet", "A straight bar — the common classroom magnet."),
        ("Horseshoe magnet", "Bent into a U so both poles pull together."),
        ("Magnetic needle", "A slim magnet that swings freely, as in a "
         "compass."),
        ("Temporary & permanent", "Soft iron loses magnetism easily; steel "
         "keeps it."),
    ], notes="Common magnet shapes and the temporary/permanent distinction "
             "based on the material.")
    b.bullets("MATERIALS", "Magnetic and Non-Magnetic Materials", [
        ("Magnetic", "Iron, nickel and cobalt are attracted by a magnet."),
        ("Non-magnetic", "Wood, plastic, glass and copper are not attracted."),
        ("A simple test", "Bring a magnet near an object to see which group "
         "it is in."),
        ("Sorting scrap", "Magnets pull iron out of mixed scrap."),
    ], notes="Separate magnetic (iron, nickel, cobalt) from non-magnetic "
             "materials, with the sorting-scrap application.")
    b.cards("MAKING MAGNETS", "Ways to Make a Magnet", [
        ("By stroking", "Rub an iron bar the same way with one pole of a "
         "magnet."),
        ("By electricity", "A current in a coil around iron makes an "
         "electromagnet."),
        ("Induction", "Iron near a strong magnet becomes a magnet for a "
         "while."),
        ("Losing it", "Heating, hammering or dropping destroys magnetism."),
    ], notes="Ways to magnetise iron — stroking, electric current, induction — "
             "and how magnetism is lost.")
    b.statement("POLES IN PAIRS", "You Cannot Get a Single Pole",
                "Every magnet has two poles. Break a bar magnet and each piece "
                "becomes a full magnet with its own north and south pole.",
                points=[
                    "Cut it again, and every piece still has both poles.",
                    "A lone north or south pole cannot exist.",
                    "The field lines always run from one pole to the other.",
                ],
                notes="Poles come only in pairs — breaking a magnet just makes "
                      "more complete magnets, never a single pole.")

    b.quiz_intro("Quiz 1", "Check — Field and Lines of Force", 4)
    b.quiz_q(1, "Field lines outside", "Outside a bar magnet, the magnetic "
             "lines of force run from:", ["South to north pole",
              "North to south pole", "Pole to the middle",
              "In no fixed direction"])
    b.quiz_a(1, "B. North to south pole",
             "By convention, outside the magnet the field lines are drawn "
             "coming out of the north pole and going into the south pole.")
    b.quiz_q(2, "Crossing lines", "Two magnetic field lines can never:",
             ["Curve", "Cross each other", "Be close together",
              "Come out of a pole"])
    b.quiz_a(2, "B. Cross each other",
             "If two lines crossed, the field would point in two directions at "
             "one place, which is impossible — so field lines never cross.")
    b.quiz_q(3, "Strong field", "The magnetic field of a bar magnet is "
             "strongest:", ["At the centre", "Near the poles",
              "Far away", "Everywhere the same"])
    b.quiz_a(3, "B. Near the poles",
             "The lines of force are most crowded near the poles, which is "
             "exactly where the field is strongest.")
    b.quiz_q(4, "Like poles", "When the north poles of two magnets are brought "
             "close, they:", ["Attract", "Repel", "Do nothing",
              "Join together"])
    b.quiz_a(4, "B. Repel",
             "Like poles repel. Two north poles push each other apart; only "
             "unlike poles (N and S) attract.")

    # ---- Part 2 : Electromagnets and the Earth ------------------------------
    b.divider(2, "Part 2", "Electromagnets and the Earth",
              "Magnetism from electricity, and the planet as a magnet")
    b.text_image("ELECTROMAGNET", "The Electromagnet",
                 ["A current in a coil of wire produces a magnetic field.",
                  "Winding the coil on an iron core makes a strong "
                  "electromagnet.",
                  "It is magnetic only while the current flows — it can be "
                  "switched off.",
                  "Used in electric bells, cranes and many machines."],
                 emag, img_side="right", panel_title="Magnetism from current",
                 caption="Coil + iron core + current",
                 notes="An electromagnet is a temporary magnet made by a "
                       "current in a coil around iron; its great advantage is "
                       "that it can be switched on and off.")
    b.bullets("HOW IT WORKS", "How an Electromagnet Works", [
        ("Current makes a field", "An electric current in a wire makes a "
         "magnetic field around it."),
        ("A coil concentrates it", "Winding the wire into a coil makes a "
         "stronger field."),
        ("Iron core", "A soft-iron core inside the coil makes it far "
         "stronger."),
        ("Stronger current", "More turns or more current gives a stronger "
         "magnet."),
    ], notes="Explain the electromagnet step by step: current → field → coil "
             "concentrates it → iron core strengthens it.")
    b.cards("EM vs PERMANENT", "Electromagnet vs Permanent Magnet", [
        ("Switchable", "An electromagnet works only while current flows."),
        ("Adjustable", "Its strength can be changed by the current."),
        ("Permanent magnet", "Keeps its magnetism all the time."),
        ("Best use", "Electromagnets suit cranes and bells that switch on and "
         "off."),
    ], notes="Compare the two: the electromagnet's switchable, adjustable "
             "nature versus the always-on permanent magnet.")
    b.cards("EM USES", "Uses of Electromagnets", [
        ("Electric bell", "The electromagnet makes the hammer strike the "
         "gong."),
        ("Cranes", "Lift and drop heavy iron scrap at the flick of a switch."),
        ("Loudspeakers", "Turn electrical signals into the sound we hear."),
        ("MRI machines", "Powerful electromagnets help doctors see inside the "
         "body."),
    ], notes="Where electromagnets are used — bells, cranes, loudspeakers and "
             "MRI — all needing a switchable magnet.")
    b.text_image("EARTH'S MAGNETISM", "The Earth is a Magnet",
                 ["The Earth behaves like a giant bar magnet.",
                  "This is why a freely suspended magnet points north–south.",
                  "A compass needle is a small magnet that lines up with the "
                  "field.",
                  "Sailors and travellers have used it to find direction for "
                  "centuries."],
                 earth, img_side="left", panel_title="A planet-sized magnet",
                 caption="The compass follows the field",
                 notes="Earth's own magnetism aligns a free magnet or compass "
                       "needle north–south, giving us a way to find "
                       "direction.")
    b.bullets("THE COMPASS", "The Magnetic Compass", [
        ("A tiny magnet", "The needle is a small, freely-turning magnet."),
        ("Follows the Earth", "It lines up with the Earth's magnetic field."),
        ("Points north", "Its marked end settles pointing north."),
        ("Still vital", "Hikers, ships and planes rely on it even today."),
    ], notes="The compass uses the Earth's field: a free needle points north "
             "and has guided travellers for centuries.")
    b.cards("USES", "Magnets at Work", [
        ("Compass", "Finds direction using the Earth's magnetic field."),
        ("Electric bell", "An electromagnet makes the hammer strike "
         "repeatedly."),
        ("Cranes", "Powerful electromagnets lift and drop heavy iron "
         "scrap."),
        ("Fridge & gadgets", "Small magnets hold doors and run many "
         "devices."),
    ], notes="Everyday and industrial uses of permanent magnets and "
             "electromagnets.")
    b.bullets("CARE", "Caring for Magnets", [
        ("Store in pairs", "Keep bar magnets with unlike poles together and "
         "keepers across the ends."),
        ("Handle gently", "Do not heat, hammer or drop a magnet."),
        ("Keep apart", "Store away from devices magnets could disturb."),
        ("Why", "Careful handling keeps a magnet strong for years."),
    ], notes="Care and storage of magnets — pairs with keepers, gentle "
             "handling — to preserve their magnetism.")
    b.statement("FROM ELECTRICITY", "Magnetism and Electricity are Linked",
                "A moving electric current always makes a magnetic field — "
                "this deep link between electricity and magnetism runs many of "
                "our machines.",
                points=[
                    "Every electric current is wrapped in a magnetic field.",
                    "This is how motors, bells and cranes work.",
                    "You will meet this link again in higher classes.",
                ],
                notes="Close on the big idea: electricity and magnetism are "
                      "linked, powering motors and many devices — a hook to "
                      "later grades.")

    b.cards("TECHNOLOGY", "Magnets in Modern Technology", [
        ("Electric motors", "Magnets make the motors in fans, mixers and "
         "toys turn."),
        ("Loudspeakers", "A magnet and coil turn signals into sound."),
        ("Data storage", "Magnetic strips on cards and disks store "
         "information."),
        ("Maglev trains", "Powerful magnets can lift and speed a train along "
         "a track."),
    ], notes="Show how magnetism runs modern technology — motors, speakers, "
             "data storage and even maglev trains.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Magnetic field", "region of force around a magnet"),
        ("Lines of force", "N → S outside; never cross"),
        ("Strength", "crowded lines near poles = strong"),
        ("Poles", "like repel, unlike attract"),
        ("Electromagnet", "coil + current; can be switched off"),
        ("Earth", "acts as a magnet; guides the compass"),
    ], notes="Recap the field, its lines, the pole law, the electromagnet and "
             "the Earth's magnetism.")
    b.quiz_intro("Quiz 2", "Final Check — Electromagnets & Earth", 4)
    b.quiz_q(1, "Making an electromagnet", "An electromagnet is made by "
             "passing a current through a coil wound on a core of:",
             ["Copper", "Soft iron", "Plastic", "Wood"])
    b.quiz_a(1, "B. Soft iron",
             "A soft-iron core inside the current-carrying coil greatly "
             "strengthens the magnetic field, making a powerful "
             "electromagnet.")
    b.quiz_q(2, "Switchable", "The main advantage of an electromagnet over a "
             "permanent magnet is that it:", ["Is lighter",
              "Can be switched on and off", "Never loses magnetism",
              "Needs no current"])
    b.quiz_a(2, "B. Can be switched on and off",
             "An electromagnet is magnetic only while current flows, so it can "
             "be turned on and off — ideal for cranes and bells.")
    b.quiz_q(3, "Compass", "A compass needle settles pointing north–south "
             "because it lines up with the magnetic field of the:",
             ["Sun", "Moon", "Earth", "Nearest building"])
    b.quiz_a(3, "C. Earth",
             "The Earth acts as a huge magnet, and the small magnetised "
             "compass needle turns to line up with the Earth's magnetic "
             "field.")
    b.quiz_q(4, "Crane magnet", "Huge electromagnets are used in scrapyards "
             "to:", ["Cut iron", "Lift and drop heavy iron pieces",
              "Paint cars", "Weigh trucks"])
    b.quiz_a(4, "B. Lift and drop heavy iron pieces",
             "Switching the electromagnet on lets the crane lift heavy iron "
             "scrap; switching it off drops the load exactly where wanted.")
    b.closing("The Invisible Field",
              "From iron filings to the whole planet, magnetism reaches out "
              "through an invisible field — and switching it on with "
              "electricity puts it to work.")
    return b


# ===========================================================================
# S67 — In the World of Stars
# ===========================================================================
def stars_deck():
    footer = "In the World of Stars  •  MSBSHSE Std 7 General Science"
    b = Builder(footer, accent=C["blue"])
    milky = web(b, "mh7_st_milky", "mh7_milkyway",
                DM.galaxy_types("mh7_st_milky_v"))
    galaxy = web(b, "mh7_st_galaxy", "mh7_galaxy",
                 DM.galaxy_types("mh7_st_galaxy_v"))
    nebula = web(b, "mh7_st_nebula", "mh7_nebula", None)
    cluster = web(b, "mh7_st_cluster", "mh7_starcluster", None)
    constell = b.asset("mh7_st_const", DM.constellation("mh7_st_const"))
    gtypes = b.asset("mh7_st_gtypes", DM.galaxy_types("mh7_st_gtypes"))

    b.title("Std 7 • General Science • Astronomy", "In the World of Stars",
            "The universe  •  Galaxies  •  Stars and constellations  •  "
            "Watching the sky", img=milky)
    b.objectives([
        "Describe what the universe contains",
        "Explain what a galaxy is and name its types",
        "Describe stars and how they differ",
        "Explain what a constellation is",
        "Understand the vast distances between stars",
        "Enjoy and identify sights in the night sky",
    ])

    # ---- Part 1 : The universe and galaxies ---------------------------------
    b.divider(1, "Part 1", "The Universe and Galaxies",
              "Everything there is, gathered into great islands of stars")
    b.text_image("THE UNIVERSE", "The Universe",
                 ["The universe is everything that exists — space and all it "
                  "holds.",
                  "It contains countless stars, planets, gas and dust.",
                  "Distances are so huge we measure them in light years.",
                  "A light year is the distance light travels in one year."],
                 milky, img_side="right", panel_title="Everything there is",
                 caption="The Milky Way arching over Earth",
                 notes="Set the scale of the universe and introduce the light "
                       "year as the unit of astronomical distance.")
    b.bullets("WHAT IT HOLDS", "What the Universe Contains", [
        ("Stars", "Countless glowing balls of hot gas, like our Sun."),
        ("Planets & moons", "Worlds orbiting stars, and moons orbiting "
         "planets."),
        ("Galaxies", "Vast groups of billions of stars."),
        ("Gas and dust", "Great clouds from which new stars are born."),
    ], notes="Inventory the contents of the universe — stars, planets, "
             "galaxies and the gas-and-dust clouds.")
    b.statement("LIGHT YEAR", "Measuring the Vast Distances",
                "Space is so vast that ordinary units are useless — we measure "
                "distance in light years, the distance light travels in one "
                "year.",
                points=[
                    "Light is the fastest thing there is.",
                    "In one year it covers a truly enormous distance.",
                    "Even the nearest star beyond the Sun is over four light "
                    "years away.",
                ],
                notes="Introduce the light year and give a sense of scale — "
                      "the nearest star is several light years off.")
    b.text_image("GALAXIES", "Galaxies",
                 ["A galaxy is a huge group of stars, gas and dust held by "
                  "gravity.",
                  "Our galaxy is the Milky Way; our Sun is one of its stars.",
                  "Galaxies come in spiral, elliptical and irregular shapes.",
                  "The universe holds billions of galaxies."],
                 galaxy, img_side="left", panel_title="Islands of stars",
                 caption="A spiral galaxy",
                 notes="A galaxy is a gravitationally bound island of billions "
                       "of stars. Name the three shapes and place our Sun in "
                       "the Milky Way.")
    b.text_image("GALAXY SHAPES", "The Shapes of Galaxies",
                 ["Galaxies are seen in several shapes.",
                  "Spiral: a bright centre with curving arms.",
                  "Elliptical: a smooth oval or ball of stars.",
                  "Irregular: no fixed shape at all."],
                 gtypes, img_side="right", img_w=5.8, img_h=2.7,
                 panel_title="Spiral • elliptical • irregular",
                 caption="Galaxies come in different shapes",
                 notes="Name the galaxy shapes using the diagram — spiral, "
                       "elliptical and irregular.")
    b.bullets("OUR GALAXY", "The Milky Way", [
        ("Our home galaxy", "The Sun and its planets lie in the Milky Way."),
        ("A spiral", "It is a huge spiral galaxy of billions of stars."),
        ("A band of light", "On a dark night it appears as a milky band across "
         "the sky."),
        ("Andromeda", "Our nearest large neighbour galaxy."),
    ], notes="Place ourselves in the Milky Way — a spiral galaxy, seen as a "
             "milky band, with Andromeda as its nearest neighbour.")
    b.text_image("NEBULA", "Nebulae — Where Stars are Born",
                 ["A nebula is a giant cloud of gas and dust in space.",
                  "Under gravity, parts of it clump together and heat up.",
                  "When hot and dense enough, a new star begins to shine.",
                  "So nebulae are the nurseries of stars."],
                 nebula, img_side="left", panel_title="Clouds of gas & dust",
                 caption="A star-forming nebula",
                 notes="Introduce nebulae as the birthplaces of stars — a real "
                       "NASA image gives a sense of their scale and colour.")
    b.bullets("BIRTH OF A STAR", "How a Star is Born", [
        ("A giant cloud", "It begins in a huge nebula of gas and dust."),
        ("Gravity gathers it", "Gravity pulls the gas into a dense clump."),
        ("It heats up", "The shrinking clump grows hotter and hotter."),
        ("A star shines", "When hot enough, it glows — a new star is born."),
    ], notes="Walk through star birth: nebula → gravity gathers gas → it heats "
             "→ it shines.")
    b.cards("TYPES OF STARS", "Stars Come in Different Kinds", [
        ("Sun-like stars", "Medium stars that shine steadily, like our Sun."),
        ("Red giants", "Huge, cooler stars that glow red."),
        ("Binary stars", "Two stars circling around each other."),
        ("Variable stars", "Stars whose brightness keeps changing."),
    ], notes="Introduce star types — Sun-like, red giant, binary, variable — "
             "to show stars are not all alike.")

    b.cards("HEAVENLY BODIES", "Objects We See in the Sky", [
        ("Stars", "Distant suns that make their own light."),
        ("Planets", "Worlds that orbit a star and shine by reflected light."),
        ("The Moon", "Our nearest neighbour, orbiting the Earth."),
        ("Comets & meteors", "Icy visitors with tails, and streaks of "
         "'shooting stars'."),
    ], notes="Survey the objects visible in the night sky — stars, planets, "
             "the Moon, comets and meteors — before the quiz.")

    b.quiz_intro("Quiz 1", "Check — Universe & Galaxies", 4)
    b.quiz_q(1, "Light year", "A light year is a unit of:",
             ["Time", "Distance", "Mass", "Brightness"])
    b.quiz_a(1, "B. Distance",
             "A light year is the distance that light travels in one year — a "
             "convenient way to measure the huge gaps between stars.")
    b.quiz_q(2, "Our galaxy", "The galaxy in which our Sun lies is called "
             "the:", ["Andromeda", "Milky Way", "Orion", "Solar System"])
    b.quiz_a(2, "B. Milky Way",
             "Our Sun is just one of the billions of stars that make up the "
             "Milky Way galaxy.")
    b.quiz_q(3, "Galaxy", "A galaxy is best described as a huge collection "
             "of:", ["Only planets", "Stars, gas and dust held by gravity",
              "Water", "Comets only"])
    b.quiz_a(3, "B. Stars, gas and dust held by gravity",
             "A galaxy is an enormous group of stars along with gas and dust, "
             "all bound together by gravity.")
    b.quiz_q(4, "Nebula", "New stars are born inside a:",
             ["Comet", "Nebula (cloud of gas and dust)", "Crater",
              "Rainbow"])
    b.quiz_a(4, "B. Nebula (cloud of gas and dust)",
             "Stars form when parts of a nebula — a vast cloud of gas and "
             "dust — collapse under gravity and heat up until they shine.")

    # ---- Part 2 : Stars and the night sky -----------------------------------
    b.divider(2, "Part 2", "Stars and the Night Sky",
              "The Sun, the constellations and sky-watching")
    b.text_image("STARS", "Stars",
                 ["A star is a huge ball of hot, glowing gas.",
                  "The Sun is our nearest star — that is why it looks so "
                  "big.",
                  "Stars differ in size, brightness and colour.",
                  "They only appear tiny because they are so far away."],
                 cluster, img_side="left", panel_title="Suns beyond counting",
                 caption="A cluster of stars",
                 notes="A star is a glowing ball of gas; the Sun is the "
                       "nearest. Stars vary in size, colour and brightness "
                       "and look tiny only due to distance.")
    b.bullets("THE SUN", "The Sun — Our Star", [
        ("Our nearest star", "The Sun is the star closest to the Earth."),
        ("A medium star", "It is an ordinary, medium-sized, Sun-like star."),
        ("Light and heat", "It gives the Earth the light and heat life needs."),
        ("Looks the biggest", "It seems huge only because it is so close."),
    ], notes="The Sun is our nearest, medium-sized star, the source of the "
             "light and heat that sustain life on Earth.")
    b.bullets("STARS DIFFER", "How Stars Differ", [
        ("Size", "From small dwarfs to enormous giant stars."),
        ("Brightness", "Some shine far more brightly than others."),
        ("Colour", "Hotter stars look bluish; cooler stars look red."),
        ("Distance", "Even bright stars look tiny because they are so far "
         "away."),
    ], notes="Stars differ in size, brightness and colour; distance makes even "
             "giants appear as tiny points.")
    b.text_image("CONSTELLATIONS", "Constellations",
                 ["A constellation is a group of stars forming a pattern.",
                  "People named them after animals, people and objects.",
                  "The Great Bear (Saptarshi) and Orion are easy to spot.",
                  "They help us find our way around the night sky."],
                 constell, img_side="right", panel_title="Patterns in the sky",
                 caption="A recognisable star pattern",
                 notes="A constellation is a memorable pattern of stars used "
                       "to navigate the sky. Name a couple visible from "
                       "India.")
    b.cards("FAMOUS PATTERNS", "Constellations to Spot", [
        ("Great Bear", "The Saptarshi — seven bright stars, easy to find."),
        ("Orion", "The hunter, with a striking three-star belt."),
        ("Scorpion", "A curving line of stars like a scorpion's tail."),
        ("Named long ago", "Ancient peoples named patterns after animals and "
         "heroes."),
    ], notes="Name a few well-known constellations visible from India and how "
             "they got their names.")
    b.bullets("POLE STAR", "The Pole Star and Finding Direction", [
        ("Stays put", "The Pole Star seems fixed while others wheel around "
         "it."),
        ("Marks north", "It lies almost exactly above the North Pole."),
        ("Found via Saptarshi", "The Great Bear's stars point the way to it."),
        ("A natural compass", "Travellers have used it to find north for "
         "ages."),
    ], notes="The Pole Star appears fixed above the north and can be found "
             "using the Great Bear — a natural direction-finder.")
    b.cards("SKY WATCHING", "Watching the Night Sky", [
        ("Best conditions", "A clear, dark night away from city lights shows "
         "the most stars."),
        ("With the eye", "Many stars, the Moon and some planets can be seen "
         "with the naked eye."),
        ("Telescopes", "A telescope reveals fainter, more distant objects."),
        ("Planets vs stars", "Planets shine steadily; stars appear to "
         "twinkle."),
    ], notes="Practical sky-watching tips, and the handy difference that "
             "planets shine steadily while stars twinkle.")
    b.bullets("TWINKLE", "Why Stars Twinkle", [
        ("A tiny point", "A star is so far away it is just a point of light."),
        ("Through moving air", "Its light passes through unsteady layers of "
         "air."),
        ("Light wobbles", "The moving air makes the point seem to twinkle."),
        ("Planets are steady", "Nearer planets show a small disc and shine "
         "steadily."),
    ], notes="Explain twinkling: a star's pinpoint light is disturbed by moving "
             "air, while nearer planets show a steady disc.")
    b.statement("STUDYING THE SKY", "How We Explore the Stars",
                "From the naked eye to giant telescopes and space missions, "
                "people have always reached out to understand the stars.",
                points=[
                    "Telescopes gather more light to reveal faint objects.",
                    "Observatories study the sky night after night.",
                    "India's ISRO has sent missions to the Moon and Mars.",
                ],
                notes="Close Part 2 on how we study the sky — telescopes, "
                      "observatories and space missions, including India's "
                      "ISRO.")

    b.bullets("SKY IN MOTION", "Why the Sky Seems to Turn", [
        ("Stars appear to move", "Through the night, stars seem to drift from "
         "east to west."),
        ("The Earth spins", "It is really our Earth turning on its axis."),
        ("Day and night", "The same spin gives us day and night."),
        ("The Pole Star", "Stays almost still because it lies above the "
         "axis."),
    ], notes="Explain the apparent nightly motion of the sky as a result of "
             "the Earth's rotation, with the Pole Star near the axis staying "
             "put.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Universe", "everything that exists; measured in light years"),
        ("Galaxy", "island of stars, gas and dust; ours is the Milky Way"),
        ("Nebula", "gas-and-dust cloud where stars are born"),
        ("Star", "a huge ball of hot glowing gas; the Sun is nearest"),
        ("Constellation", "a named pattern of stars"),
        ("Sky watching", "dark skies; planets shine, stars twinkle"),
    ], notes="Recap from the universe down to constellations and "
             "sky-watching.")
    b.quiz_intro("Quiz 2", "Final Check — Stars & the Sky", 4)
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
    b.quiz_q(3, "Constellation", "A group of stars that appears to form a "
             "pattern in the sky is a:", ["Galaxy", "Constellation",
              "Nebula", "Comet"])
    b.quiz_a(3, "B. Constellation",
             "A constellation is a recognisable pattern of stars, such as the "
             "Great Bear (Saptarshi) or Orion.")
    b.quiz_q(4, "Twinkle", "In the night sky, planets can usually be told "
             "from stars because planets:", ["Twinkle strongly",
              "Shine with a steady light", "Are always red", "Move very "
              "fast"])
    b.quiz_a(4, "B. Shine with a steady light",
             "Stars twinkle because their tiny points of light are disturbed "
             "by the air, while the nearer planets show a small disc and shine "
             "steadily.")
    b.closing("Looking Up",
              "The night sky is a window on a universe of galaxies and stars — "
              "vast beyond imagining, and free for anyone to explore.")
    return b


def build():
    jobs = [
        ("MH07_S22_Heat.pptx", heat_deck),
        ("MH07_S27_Effects_of_Light.pptx", light_deck),
        ("MH07_S51_Sound.pptx", sound_deck),
        ("MH07_S59_Properties_of_a_Magnetic_Field.pptx", magnet_deck),
        ("MH07_S67_In_the_World_of_Stars.pptx", stars_deck),
    ]
    for fname, fn in jobs:
        b = fn()
        issues = b.qa()
        b.save(os.path.join(OUT, fname))
        total = len(b.prs.slides._sldIdLst)
        print(f"\n=== {fname} ===")
        print(f"slides: {total}  (~{total - 24} concept)")
        if issues:
            print("QA ISSUES:")
            for i in issues:
                print("  -", i)
        else:
            print("QA: no overlaps / off-slide shapes detected")


if __name__ == "__main__":
    build()
