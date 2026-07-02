"""
Maharashtra Board (MSBSHSE) — Standard 8 Physics teaching decks.

Scope: Physics chapters/sessions from the tuitions planner after session 25 —
Measurement & Effects of Heat (S26 Heat & Temperature, S28 part 2), Sound
(S38), Reflection of Light (S67) and Life Cycle of Stars (S77). Concise,
visual teaching style (mhstyle). Content covers the MSBSHSE Std 8 General
Science textbook treatment (subtopics verified against the Balbharati chapter
scope), written in original teaching language with detail in the notes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import diagrams_mh as DM
import mhstyle

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "MH_Grade08"))
os.makedirs(OUT, exist_ok=True)
mhstyle.apply()


# ===========================================================================
# S26 — Heat and Temperature  (Measurement & Effects of Heat, part 1)
# ===========================================================================
def heat1_deck():
    footer = "Measurement and Effects of Heat  •  MSBSHSE Std 8 General Science"
    b = Builder(footer, accent=C["red"])

    states = b.asset("mh8_ht1_states", D.states_of_matter("mh8_ht1_states"))

    b.title("Std 8 • General Science • Heat", "Heat and Temperature",
            "Heat as energy  •  Heat vs temperature  •  Thermometers and "
            "their types", img=states)

    b.objectives([
        "Explain heat as a form of energy and name its sources",
        "Distinguish between heat and temperature",
        "State the effects of heat on a substance",
        "Describe a thermometer and its types",
        "Explain the special features of a clinical thermometer",
        "State the units of temperature",
    ])

    b.divider(1, "Part 1", "Heat, Temperature and Their Effects",
              "What heat is, and how it differs from temperature")

    b.bullets(
        "HEAT", "Heat and Its Sources",
        [("Heat is energy", "Heat is a form of energy that flows from a "
          "hotter body to a colder one."),
         ("Sources of heat", "The Sun, fuels, electricity and chemical "
          "reactions all give out heat."),
         ("Molecular motion", "Heating a body makes its molecules move "
          "faster (more kinetic energy)."),
         ("Flow of heat", "Heat always flows on its own from higher to "
          "lower temperature.")],
        notes="Introduce heat as energy in transit; the molecular view "
              "sets up the difference from temperature on the next "
              "slide.")

    b.text_image(
        "HEAT vs TEMPERATURE", "Heat Is Not the Same as Temperature",
        ["Temperature = average kinetic energy of the molecules",
         "Heat = total energy of all the molecules",
         "Temperature decides the direction of heat flow",
         "A bucket of warm water holds more heat than a hot cup",
         "…even though the cup is at a higher temperature"],
        states, img_side="right", panel_title="Average vs total energy",
        notes="The bucket-vs-cup example is the classic way to separate "
              "temperature (degree of hotness) from heat (total energy).")

    b.bullets(
        "EFFECTS OF HEAT", "Effects of Heat on a Substance",
        [("Rise in temperature", "Adding heat usually raises the "
          "temperature of a body."),
         ("Expansion", "Most substances expand on heating and contract on "
          "cooling."),
         ("Change of state", "Enough heat changes a solid to liquid to "
          "gas."),
         ("Other changes", "Heat can also change colour, or cause "
          "physical/chemical changes.")],
        notes="These effects recur through the chapter — expansion and "
              "change of state are explored in the next session.")

    b.quiz_intro("Quiz 1", "Check — Heat & Temperature", 4)
    b.quiz_q(1, "Heat", "Heat always flows on its own from a body at:",
             ["lower temperature to higher temperature", "higher "
              "temperature to lower temperature", "equal temperature",
              "larger size to smaller size"])
    b.quiz_a(1, "B. higher temperature to lower temperature",
             "Temperature decides the direction of heat flow — from hot "
             "to cold — until both reach the same temperature.")
    b.quiz_q(2, "Temperature", "The temperature of a body is related to "
             "the ___ kinetic energy of its molecules.",
             ["total", "average", "highest", "lowest"])
    b.quiz_a(2, "B. average",
             "Temperature reflects the average kinetic energy of the "
             "molecules; heat is their total energy.")
    b.quiz_q(3, "Heat content", "A bucket of warm water and a cup of "
             "hotter water are compared. The bucket has:",
             ["a higher temperature", "more total heat energy", "no heat",
              "less heat than the cup"])
    b.quiz_a(3, "B. more total heat energy",
             "Its much larger mass means more molecules, so more total "
             "heat energy — even at a lower temperature than the cup.")
    b.quiz_q(4, "Effects", "Which of these is NOT a usual effect of "
             "heating a substance?",
             ["expansion", "change of state", "rise in temperature",
              "decrease in molecular motion"])
    b.quiz_a(4, "D. decrease in molecular motion",
             "Heating increases molecular motion; the other three are all "
             "genuine effects of heat.")

    b.divider(2, "Part 2", "Measuring Temperature",
              "Thermometers and their types")

    b.bullets(
        "THERMOMETER", "The Thermometer",
        [("Purpose", "A thermometer is a device used to measure "
          "temperature."),
         ("How it works", "It uses the expansion of a liquid (mercury or "
          "coloured alcohol) in a thin glass tube."),
         ("Units", "Temperature is measured in degrees Celsius (°C); the "
          "SI unit is the kelvin (K)."),
         ("Fixed points", "The Celsius scale is fixed by ice point (0°C) "
          "and steam point (100°C).")],
        notes="Relate the reading to the earlier idea: expansion of the "
              "liquid is itself an effect of heat.")

    b.cards(
        "TYPES", "Types of Thermometers",
        [("Laboratory thermometer", "Range about −10°C to 110°C; used for "
          "general measurements in the lab."),
         ("Clinical thermometer", "Range 35°C to 42°C; has a kink so the "
          "reading holds until read; measures body temperature."),
         ("Digital thermometer", "Shows the temperature as a number on a "
          "display; mercury-free and safer."),
         ("Maximum–minimum thermometer", "Records the highest and lowest "
          "temperatures reached, used in weather stations.")],
        icons=["thermometer", "thermometer", "gauge", "gauge"],
        notes="The kink (constriction) of the clinical thermometer stops "
              "the mercury falling back before you read it.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Heat", "A form of energy that flows from hot to cold."),
         ("Temperature", "Average KE of molecules; decides heat-flow "
                       "direction."),
         ("Heat vs temperature", "Total energy vs degree of hotness."),
         ("Effects of heat", "Rise in temperature, expansion, change of "
                          "state."),
         ("Thermometer", "Measures temperature via expansion of a "
                       "liquid; unit °C."),
         ("Types", "Laboratory, clinical, digital, maximum–minimum.")],
        notes="Cold-call the range and special feature of a clinical "
              "thermometer.")

    b.quiz_intro("Quiz 2", "Final Check — Thermometers", 4)
    b.quiz_q(1, "Clinical", "The temperature range of a clinical "
             "thermometer is about:",
             ["−10°C to 110°C", "35°C to 42°C", "0°C to 100°C", "0°C to "
              "250°C"])
    b.quiz_a(1, "B. 35°C to 42°C",
             "A clinical thermometer covers the narrow range of human "
             "body temperature.")
    b.quiz_q(2, "Kink", "The kink (constriction) in a clinical "
             "thermometer:",
             ["makes it cheaper", "stops the mercury falling back before "
              "it is read", "measures room temperature", "lets it "
              "measure boiling water"])
    b.quiz_a(2, "B. stops the mercury falling back before it is read",
             "The kink holds the reading after the thermometer is removed, "
             "until it is shaken down.")
    b.quiz_q(3, "Units", "The SI unit of temperature is the:",
             ["degree Celsius", "kelvin", "joule", "calorie"])
    b.quiz_a(3, "B. kelvin",
             "The kelvin (K) is the SI unit of temperature; everyday "
             "measurements use degrees Celsius (°C).")
    b.quiz_q(4, "Weather", "The thermometer that records the highest and "
             "lowest temperatures of a day is the:",
             ["clinical thermometer", "laboratory thermometer",
              "maximum–minimum thermometer", "digital thermometer"])
    b.quiz_a(4, "C. maximum–minimum thermometer",
             "It is used at weather stations to record the day's extreme "
             "temperatures.")

    b.closing("Measuring the Warmth of Things",
              "Heat is energy on the move and temperature its degree of "
              "hotness — and a simple thermometer lets us pin that hotness "
              "down to a number.")
    return b


# ===========================================================================
# S28 — Measurement & Effects of Heat - 2  (expansion, specific heat)
# ===========================================================================
def heat2_deck():
    footer = "Measurement and Effects of Heat  •  MSBSHSE Std 8 General Science"
    b = Builder(footer, accent=C["orange"])

    bimetal = b.asset("mh8_ht2_bimetal", D.bimetallic_strip("mh8_ht2_bimetal"))
    calor = b.asset("mh8_ht2_calor", D.calorimeter("mh8_ht2_calor"))

    b.title("Std 8 • General Science • Heat",
            "Measurement and Effects of Heat — 2",
            "Thermal expansion  •  Specific heat capacity  •  Calorimeter "
            "and calorimetry", img=bimetal)

    b.objectives([
        "Describe the thermal expansion of solids, liquids and gases",
        "Give everyday applications of thermal expansion",
        "Define specific heat capacity",
        "Use the relation heat = mass × specific heat × rise in "
        "temperature",
        "Explain the working of a calorimeter",
        "State the principle of calorimetry (heat exchange)",
    ])

    b.divider(1, "Part 1", "Thermal Expansion",
              "How solids, liquids and gases expand on heating")

    b.text_image(
        "EXPANSION", "Thermal Expansion of Matter",
        ["Almost all substances expand on heating",
         "Gases expand the most, then liquids, then solids",
         "Rails have gaps so they can expand in summer",
         "A tight metal lid loosens under hot water",
         "Expansion happens because molecules move apart"],
        bimetal, img_side="right", panel_title="Solids, liquids, gases",
        notes="A bimetallic strip bends because its two metals expand by "
              "different amounts — used in thermostats and fire alarms.")

    b.bullets(
        "APPLICATIONS", "Everyday Uses of Expansion",
        [("Railway gaps", "Gaps are left between rails so they do not "
          "buckle when they expand."),
         ("Bimetallic strip", "Two metals that expand unequally bend on "
          "heating — used in a thermostat."),
         ("Overhead wires", "Wires are strung with a slight sag so they "
          "do not snap when they contract in winter."),
         ("Opening a lid", "Warming a tight metal lid makes it expand and "
          "loosen.")],
        notes="Each application is really the same physics: materials "
              "change size with temperature.")

    b.quiz_intro("Quiz 1", "Check — Thermal Expansion", 4)
    b.quiz_q(1, "Expansion order", "For the same rise in temperature, the "
             "greatest expansion is shown by a:",
             ["solid", "liquid", "gas", "all expand equally"])
    b.quiz_a(1, "C. gas",
             "Gases expand the most for a given temperature rise, then "
             "liquids, and solids the least.")
    b.quiz_q(2, "Rails", "Gaps are left between railway rails so that "
             "they:",
             ["look neat", "have room to expand in hot weather", "carry "
              "more load", "rust less"])
    b.quiz_a(2, "B. have room to expand in hot weather",
             "Without the gaps, expansion in summer would make the rails "
             "buckle and bend.")
    b.quiz_q(3, "Bimetallic strip", "A bimetallic strip bends on heating "
             "because its two metals:",
             ["melt", "expand by different amounts", "contract equally",
              "change colour"])
    b.quiz_a(3, "B. expand by different amounts",
             "Unequal expansion of the two metals makes the strip bend — "
             "the basis of a thermostat.")
    b.quiz_q(4, "Cause", "On heating, a substance expands because its "
             "molecules:",
             ["disappear", "move farther apart", "come closer together",
              "stop moving"])
    b.quiz_a(4, "B. move farther apart",
             "Heating increases molecular motion, so the molecules move "
             "apart and the substance expands.")

    b.divider(2, "Part 2", "Specific Heat Capacity and Calorimetry",
              "How much heat a substance needs, and how we measure it")

    b.statement(
        "SPECIFIC HEAT CAPACITY", "Specific Heat Capacity",
        "The specific heat capacity of a substance is the amount of heat "
        "needed to raise the temperature of unit mass of it by one "
        "degree.",
        formula="Heat  Q = m × c × ΔT",
        points=[
            "m = mass, c = specific heat capacity, ΔT = rise in "
            "temperature.",
            "Water has a very high specific heat capacity, so it heats up "
            "and cools down slowly.",
            "This is why water is used as a coolant and to moderate "
            "climate."],
        notes="The high specific heat of water explains coastal climates "
              "and its use in radiators — link it to everyday life.")

    b.worked(
        "WORKED EXAMPLE", "Using Q = m c ΔT",
        "How much heat is needed to raise the temperature of 2 kg of "
        "water by 10°C? (Specific heat of water = 4200 J/kg°C)",
        ["Q = m × c × ΔT",
         "Q = 2 × 4200 × 10"],
        "Q = 84,000 J",
        notes="Watch the units: mass in kg, specific heat in J/kg°C, "
              "temperature rise in °C, heat in joules.")

    b.text_image(
        "CALORIMETRY", "Calorimeter and Calorimetry",
        ["A calorimeter measures the heat given out or absorbed",
         "It is a metal vessel inside an insulating jacket",
         "Principle: heat lost by hot body = heat gained by cold body",
         "This is the principle of heat exchange",
         "Used to find specific heats by the method of mixtures"],
        calor, img_side="left", panel_title="Measuring heat exchange",
        notes="The insulating jacket stops heat leaking to the "
              "surroundings, so the heat-exchange balance holds.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Expansion", "Gases > liquids > solids for the same "
                     "temperature rise."),
         ("Applications", "Rail gaps, bimetallic strip, wire sag, "
                        "loosening lids."),
         ("Specific heat capacity", "Heat to raise unit mass by 1°; "
                                  "Q = m c ΔT."),
         ("Water", "Very high specific heat — a good coolant and climate "
                 "moderator."),
         ("Calorimeter", "Measures heat exchange (heat lost = heat "
                       "gained).")],
        notes="Cold-call the Q = m c ΔT formula and why water is used as "
              "a coolant.")

    b.quiz_intro("Quiz 2", "Final Check — Specific Heat & Calorimetry", 4)
    b.quiz_q(1, "Definition", "The specific heat capacity of a substance "
             "is the heat needed to raise the temperature of:",
             ["any mass by any amount", "unit mass by one degree", "one "
              "litre by ten degrees", "the whole body by 100°C"])
    b.quiz_a(1, "B. unit mass by one degree",
             "Specific heat capacity is per unit mass per degree rise — "
             "a property of the material.")
    b.quiz_q(2, "Numerical", "The heat needed to raise 1 kg of water by "
             "5°C is (c = 4200 J/kg°C):",
             ["21,000 J", "4200 J", "840 J", "5 J"])
    b.quiz_a(2, "A. 21,000 J",
             "Q = m c ΔT = 1 × 4200 × 5 = 21,000 J.")
    b.quiz_q(3, "Water", "Water is used as a coolant in car radiators "
             "because it has a:",
             ["low specific heat capacity", "high specific heat "
              "capacity", "low boiling point", "high density only"])
    b.quiz_a(3, "B. high specific heat capacity",
             "Its high specific heat lets water absorb a large amount of "
             "heat with only a small rise in temperature.")
    b.quiz_q(4, "Calorimetry", "The principle of calorimetry states "
             "that:",
             ["heat is destroyed", "heat lost by the hot body = heat "
              "gained by the cold body", "temperature never changes",
              "heat only flows upward"])
    b.quiz_a(4, "B. heat lost by the hot body = heat gained by the cold "
             "body",
             "In an insulated calorimeter, the heat exchange balances — "
             "the basis for measuring specific heats.")

    b.closing("Heat, Measured Exactly",
              "Expansion, specific heat and the calorimeter turn the "
              "vague idea of 'hotness' into quantities we can calculate "
              "and measure.")
    return b


# ===========================================================================
# S38 — Sound
# ===========================================================================
def sound_deck():
    footer = "Sound  •  MSBSHSE Std 8 General Science"
    b = Builder(footer, accent=C["teal"])

    longw = b.asset("mh8_snd_long", D.longitudinal_wave("mh8_snd_long"))
    chars = b.asset("mh8_snd_chars", D.sound_characteristics("mh8_snd_chars"))

    b.title("Std 8 • General Science • Sound", "Sound",
            "Production and propagation  •  Sound waves  •  "
            "Characteristics  •  Music, noise and sound pollution",
            img=longw)

    b.objectives([
        "Explain how sound is produced and propagates",
        "State that sound needs a medium to travel",
        "Describe sound as a wave with compressions and rarefactions",
        "State the characteristics of sound",
        "Distinguish between music and noise",
        "Explain sound pollution and how to reduce it",
    ])

    b.divider(1, "Part 1", "Production and Propagation of Sound",
              "How sound is made and how it travels")

    b.bullets(
        "PRODUCTION", "How Sound Is Produced and Travels",
        [("By vibration", "Sound is produced by a vibrating object — a "
          "string, a membrane, vocal cords."),
         ("Needs a medium", "Sound needs a material medium; it cannot "
          "travel through a vacuum."),
         ("Energy transfer", "Vibrating particles pass the energy on to "
          "the next particles."),
         ("Human voice", "In humans, sound is produced by the vibration "
          "of the vocal cords in the voice box.")],
        notes="A loudspeaker works the same way in reverse: an electrical "
              "signal makes a cone vibrate and produce sound.")

    b.text_image(
        "SOUND WAVES", "Sound Travels as a Wave",
        ["In air, sound is a longitudinal wave",
         "Made of compressions and rarefactions",
         "Compression = crowded, high-pressure region",
         "Rarefaction = spread-out, low-pressure region",
         "Wave carries energy, not the air itself, forward"],
        longw, img_side="right", panel_title="Compressions and "
        "rarefactions",
        notes="Stress that the particles vibrate in place; it is the "
              "disturbance (energy) that travels forward.")

    b.quiz_intro("Quiz 1", "Check — Production & Propagation", 4)
    b.quiz_q(1, "Production", "Sound is produced by a body that is:",
             ["hot", "vibrating", "coloured", "at rest"])
    b.quiz_a(1, "B. vibrating",
             "Every source of sound — a string, a drum, vocal cords — is "
             "vibrating.")
    b.quiz_q(2, "Medium", "Sound cannot travel through:",
             ["water", "iron", "air", "a vacuum"])
    b.quiz_a(2, "D. a vacuum",
             "With no particles to pass on the vibration, sound cannot "
             "travel through a vacuum.")
    b.quiz_q(3, "Wave", "Sound travels through air as a:",
             ["transverse wave", "longitudinal wave", "light wave",
              "water wave"])
    b.quiz_a(3, "B. longitudinal wave",
             "The air particles vibrate along the direction of travel, "
             "forming compressions and rarefactions.")
    b.quiz_q(4, "Voice", "The human voice is produced by the vibration "
             "of the:",
             ["teeth", "vocal cords", "tongue only", "ears"])
    b.quiz_a(4, "B. vocal cords",
             "Air from the lungs makes the vocal cords in the voice box "
             "vibrate, producing sound.")

    b.divider(2, "Part 2", "Characteristics, Music and Noise",
              "What makes sounds different, and sound pollution")

    b.text_image(
        "CHARACTERISTICS", "Characteristics of Sound",
        ["Loudness depends on amplitude",
         "Pitch depends on frequency",
         "Quality (timbre) depends on the waveform",
         "Higher frequency → higher pitch",
         "Larger amplitude → louder sound"],
        chars, img_side="left", panel_title="Loudness, pitch, quality",
        notes="Quality lets us recognise a voice or tell instruments "
              "apart playing the same note.")

    b.cards(
        "MUSIC & NOISE", "Music, Noise and Sound Pollution",
        [("Music", "A pleasant sound with a regular, periodic pattern — "
          "from a flute, violin or piano."),
         ("Noise", "An unpleasant sound with an irregular pattern — like "
          "traffic or machinery."),
         ("Sound pollution", "Unwanted, excessive noise that harms health "
          "and the environment."),
         ("Reducing it", "Limit loudspeakers and horns, plant trees, and "
          "use sound-absorbing materials.")],
        icons=["wave", "wave", "ear", "check"],
        notes="Sound pollution links to social health — a good discussion "
              "point about responsible behaviour.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Production", "Sound comes from a vibrating body."),
         ("Medium", "Sound needs a medium; no sound in a vacuum."),
         ("Sound wave", "Longitudinal — compressions and rarefactions."),
         ("Characteristics", "Loudness (amplitude), pitch (frequency), "
                          "quality (waveform)."),
         ("Music vs noise", "Regular pleasant sound vs irregular "
                         "unpleasant sound."),
         ("Sound pollution", "Excess noise harms health; reduce it.")],
        notes="Cold-call which property changes when a drum is struck "
              "harder versus a smaller drum.")

    b.quiz_intro("Quiz 2", "Final Check — Characteristics & Noise", 4)
    b.quiz_q(1, "Loudness", "The loudness of a sound depends on its:",
             ["frequency", "amplitude", "speed", "wavelength"])
    b.quiz_a(1, "B. amplitude",
             "A larger amplitude of vibration produces a louder sound.")
    b.quiz_q(2, "Pitch", "A high-pitched, shrill sound has a high:",
             ["amplitude", "frequency", "speed", "loudness"])
    b.quiz_a(2, "B. frequency",
             "Pitch depends on frequency — the higher the frequency, the "
             "shriller the sound.")
    b.quiz_q(3, "Music vs noise", "Compared with noise, a musical sound "
             "has a:",
             ["very large amplitude", "regular, periodic waveform", "no "
              "frequency", "no medium"])
    b.quiz_a(3, "B. regular, periodic waveform",
             "Music is pleasant because its waveform is regular; noise is "
             "irregular and unpleasant.")
    b.quiz_q(4, "Sound pollution", "Sound pollution can be reduced by:",
             ["using more loudspeakers", "planting trees and limiting "
              "horns", "increasing traffic", "removing all soft "
              "materials"])
    b.quiz_a(4, "B. planting trees and limiting horns",
             "Trees absorb sound and limiting horns/loudspeakers cuts "
             "unwanted noise at the source.")

    b.closing("The Science of Sound",
              "From a vibrating string to the roar of traffic, sound is a "
              "wave we can describe, enjoy as music, and control when it "
              "becomes noise.")
    return b


# ===========================================================================
# S67 — Reflection of Light
# ===========================================================================
def reflection_deck():
    footer = "Reflection of Light  •  MSBSHSE Std 8 General Science"
    b = Builder(footer, accent=C["purple"])

    law = b.asset("mh8_ref_law", D.reflection_law("mh8_ref_law"))
    plane = b.asset("mh8_ref_plane", D.plane_mirror_image("mh8_ref_plane"))
    peri = b.asset("mh8_ref_peri", DM.periscope("mh8_ref_peri"))

    b.title("Std 8 • General Science • Optics", "Reflection of Light",
            "Reflection and its terms  •  Laws of reflection  •  Types of "
            "reflection  •  Periscope and kaleidoscope", img=law)

    b.objectives([
        "Define reflection and the terms used in it",
        "State the laws of reflection of light",
        "Distinguish regular and irregular reflection",
        "Explain reflection of reflected light (multiple reflection)",
        "Describe the working of a periscope",
        "Explain how a kaleidoscope works",
    ])

    b.divider(1, "Part 1", "Reflection and Its Laws",
              "How light bounces off a surface")

    b.bullets(
        "TERMS", "Reflection and Its Terms",
        [("Reflection", "The bouncing back of light from a polished "
          "surface."),
         ("Incident ray", "The ray of light striking the surface."),
         ("Reflected ray", "The ray that bounces back."),
         ("Normal", "The perpendicular to the surface at the point of "
          "incidence; angles are measured from it.")],
        notes="Draw and label all four terms on the reflection_law "
              "diagram before stating the laws.")

    b.statement(
        "LAWS OF REFLECTION", "The Laws of Reflection of Light",
        "Reflection of light follows three laws.",
        img=law,
        notes="1. The angle of reflection equals the angle of incidence. "
              "2. The incident ray, the reflected ray and the normal lie "
              "in the same plane. 3. The incident ray and the reflected "
              "ray are on opposite sides of the normal.")

    b.text_image(
        "TYPES", "Regular and Irregular Reflection",
        ["Regular reflection: from a smooth, polished surface",
         "Parallel rays stay parallel → a clear image",
         "Irregular (diffuse): from a rough surface",
         "Rays scatter in all directions → no clear image",
         "A mirror gives regular; paper gives irregular reflection"],
        plane, img_side="right", panel_title="Smooth vs rough surfaces",
        notes="This is why we see a clear image in a mirror but only a "
              "lit surface on a wall or a page.")

    b.quiz_intro("Quiz 1", "Check — Reflection & Laws", 4)
    b.quiz_q(1, "Angles", "According to the laws of reflection, the angle "
             "of reflection is:",
             ["greater than the angle of incidence", "equal to the angle "
              "of incidence", "less than the angle of incidence", "always "
              "90°"])
    b.quiz_a(1, "B. equal to the angle of incidence",
             "The angle of reflection always equals the angle of "
             "incidence, both measured from the normal.")
    b.quiz_q(2, "Normal", "In reflection, the angles are measured from "
             "the:",
             ["surface", "normal at the point of incidence", "reflected "
              "object", "edge of the mirror"])
    b.quiz_a(2, "B. normal at the point of incidence",
             "The normal is the perpendicular to the surface at the point "
             "the ray strikes; both angles are measured from it.")
    b.quiz_q(3, "Regular", "Reflection from a smooth, polished surface, "
             "giving a clear image, is:",
             ["irregular reflection", "regular reflection", "diffuse "
              "reflection", "refraction"])
    b.quiz_a(3, "B. regular reflection",
             "A smooth surface reflects parallel rays parallel, forming a "
             "clear image — regular reflection.")
    b.quiz_q(4, "Irregular", "We cannot see our image in a sheet of paper "
             "because it causes:",
             ["regular reflection", "irregular (diffuse) reflection",
              "no reflection", "refraction"])
    b.quiz_a(4, "B. irregular (diffuse) reflection",
             "The rough surface of paper scatters light in all "
             "directions, so no clear image forms.")

    b.divider(2, "Part 2", "Multiple Reflection and Its Uses",
              "Periscope and kaleidoscope")

    b.text_image(
        "PERISCOPE", "The Periscope",
        ["Uses reflection of reflected light (two mirrors)",
         "Two plane mirrors are fixed at 45°, parallel to each other",
         "Light reflects off the top mirror, then the bottom mirror",
         "The emergent ray is parallel to the incident ray",
         "Used to see over walls and from submarines"],
        peri, img_side="right", panel_title="Seeing over an obstacle",
        notes="Trace the ray on the periscope diagram: down the tube and "
              "out to the eye, letting you see over an obstacle.")

    b.bullets(
        "KALEIDOSCOPE", "The Kaleidoscope",
        [("Multiple reflection", "It works on repeated reflection of "
          "reflected light."),
         ("Mirrors at an angle", "Two or three plane mirrors are placed "
          "at an angle inside a tube."),
         ("Beautiful patterns", "Coloured pieces are reflected many times "
          "to form symmetrical patterns."),
         ("Changing view", "Turning the tube rearranges the pieces and "
          "changes the pattern.")],
        notes="Both the periscope and kaleidoscope use multiple "
              "reflection — the difference is the mirror arrangement.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Reflection", "Bouncing back of light from a polished "
                     "surface."),
         ("Laws", "Angle of reflection = angle of incidence; rays and "
                "normal coplanar; on opposite sides of the normal."),
         ("Regular vs irregular", "Smooth surface → clear image; rough "
                               "surface → scattered light."),
         ("Periscope", "Two 45° mirrors let you see over an obstacle."),
         ("Kaleidoscope", "Multiple reflection makes symmetrical "
                        "patterns.")],
        notes="Cold-call the three laws of reflection before the final "
              "quiz.")

    b.quiz_intro("Quiz 2", "Final Check — Periscope & Kaleidoscope", 4)
    b.quiz_q(1, "Periscope", "A periscope uses two plane mirrors fixed "
             "at an angle of:",
             ["30°", "45°", "60°", "90°"])
    b.quiz_a(1, "B. 45°",
             "Each mirror at 45° turns the light through 90°, so the two "
             "together let you see over an obstacle.")
    b.quiz_q(2, "Principle", "Both the periscope and the kaleidoscope "
             "work on the:",
             ["refraction of light", "reflection of reflected light",
              "dispersion of light", "absorption of light"])
    b.quiz_a(2, "B. reflection of reflected light",
             "Both use multiple reflection — light reflected from one "
             "mirror is reflected again by another.")
    b.quiz_q(3, "Periscope ray", "In a periscope, the emergent ray is "
             "___ to the incident ray.",
             ["perpendicular", "parallel", "opposite", "at 45°"])
    b.quiz_a(3, "B. parallel",
             "Because the two mirrors are parallel, the ray leaving the "
             "periscope is parallel to the ray that entered.")
    b.quiz_q(4, "Kaleidoscope", "A kaleidoscope produces symmetrical "
             "patterns using:",
             ["a single lens", "plane mirrors at an angle", "a concave "
              "mirror", "a prism"])
    b.quiz_a(4, "B. plane mirrors at an angle",
             "Coloured pieces are reflected repeatedly by mirrors set at "
             "an angle, forming symmetrical patterns.")

    b.closing("Light That Bounces",
              "The simple laws of reflection, used once or many times "
              "over, give us mirrors, periscopes and the endless patterns "
              "of a kaleidoscope.")
    return b


# ===========================================================================
# S77 — Life Cycle of Stars
# ===========================================================================
def stars_deck():
    footer = "Life Cycle of Stars  •  MSBSHSE Std 8 General Science"
    b = Builder(footer, accent=C["blue"])

    cycle = b.asset("mh8_star_cycle", DM.star_life_cycle("mh8_star_cycle"))

    b.title("Std 8 • General Science • Astronomy", "Life Cycle of Stars",
            "Galaxies and the Milky Way  •  Birth of stars  •  How stars "
            "evolve  •  White dwarfs, neutron stars and black holes",
            img=cycle)

    b.objectives([
        "Describe a galaxy and name the galaxy we live in",
        "Use the light year as a unit of distance",
        "Explain how stars are born from interstellar clouds",
        "Explain what keeps a star stable",
        "Describe how a star evolves depending on its mass",
        "Name the final stages: white dwarf, neutron star and black hole",
    ])

    b.divider(1, "Part 1", "Galaxies and the Birth of Stars",
              "Where stars live, and how they form")

    b.bullets(
        "GALAXY", "Galaxies and the Milky Way",
        [("Galaxy", "A huge collection of stars, gas and dust held "
          "together by gravity."),
         ("Our galaxy", "We live in the Milky Way (Mandakini), which has "
          "about 100 billion stars."),
         ("Light year", "The distance light travels in one year — a unit "
          "for the vast distances in space."),
         ("The Sun", "The Sun is our nearest star and the source of "
          "almost all our energy.")],
        notes="Give a sense of scale: light from the nearest star after "
              "the Sun takes over four years to reach us.")

    b.bullets(
        "BIRTH", "How Stars Are Born",
        [("Interstellar clouds", "Stars are born inside huge clouds of "
          "gas and dust (nebulae)."),
         ("Gravity pulls in", "Gravity makes the cloud contract and heat "
          "up at the centre."),
         ("A star ignites", "When it is hot enough, nuclear reactions "
          "begin and the star starts to shine."),
         ("Stability", "The outward push of these reactions balances the "
          "inward pull of gravity, keeping the star stable.")],
        notes="Stability is a balance of two forces — set this up because "
              "the star's fate depends on it running out of fuel.")

    b.quiz_intro("Quiz 1", "Check — Galaxies & Birth of Stars", 4)
    b.quiz_q(1, "Galaxy", "The galaxy in which we live is called the:",
             ["Andromeda", "Milky Way (Mandakini)", "Solar System", "Great "
              "Bear"])
    b.quiz_a(1, "B. Milky Way (Mandakini)",
             "Our galaxy, the Milky Way (Mandakini), contains about 100 "
             "billion stars.")
    b.quiz_q(2, "Light year", "A light year is a unit of:",
             ["time", "distance", "mass", "temperature"])
    b.quiz_a(2, "B. distance",
             "A light year is the distance light travels in one year — "
             "used for the huge distances between stars.")
    b.quiz_q(3, "Birth", "Stars are born from:",
             ["black holes", "clouds of gas and dust (nebulae)", "planets",
              "comets"])
    b.quiz_a(3, "B. clouds of gas and dust (nebulae)",
             "Gravity pulls together a nebula until its centre is hot "
             "enough for nuclear reactions to start.")
    b.quiz_q(4, "Stability", "A star stays stable because the inward pull "
             "of gravity is balanced by the:",
             ["Earth's gravity", "outward push of its nuclear reactions",
              "solar wind", "magnetic field"])
    b.quiz_a(4, "B. outward push of its nuclear reactions",
             "The energy released inside pushes outward and balances "
             "gravity, keeping the star stable while it has fuel.")

    b.divider(2, "Part 2", "How Stars Evolve",
              "The fate of a star depends on its mass")

    b.text_image(
        "EVOLUTION", "Three Ways a Star Can Evolve",
        ["When the fuel runs low, the star swells up",
         "Low-mass star → red giant → white dwarf",
         "High-mass star → supergiant → supernova",
         "Supernova remnant → neutron star or black hole",
         "The bigger the star, the more dramatic its end"],
        cycle, img_side="right", panel_title="Depends on the star's "
        "mass",
        notes="Walk the flow diagram left to right along both branches; "
              "the split point is the star's initial mass.")

    b.bullets(
        "END STAGES", "White Dwarfs, Neutron Stars and Black Holes",
        [("White dwarf", "The small, dense end stage of a low-mass star "
          "like the Sun."),
         ("Supernova", "The huge explosion that ends a very massive "
          "star's life."),
         ("Neutron star", "An extremely dense remnant left after some "
          "supernovae."),
         ("Black hole", "The end of a very massive star — its gravity is "
          "so strong that not even light escapes.")],
        notes="Emphasise the black hole definition (nothing, not even "
              "light, can escape) — a favourite exam point.")

    b.recap(
        "WRAP UP", "Quick Recap",
        [("Galaxy", "Milky Way (Mandakini); ~100 billion stars; distances "
                  "in light years."),
         ("Birth", "Stars form in nebulae as gravity pulls gas and dust "
                 "together."),
         ("Stability", "Gravity inward balanced by nuclear push "
                     "outward."),
         ("Low-mass star", "Red giant → white dwarf."),
         ("High-mass star", "Supergiant → supernova → neutron star or "
                          "black hole."),
         ("Black hole", "Gravity so strong that not even light "
                      "escapes.")],
        notes="Cold-call the two evolutionary paths and what decides "
              "which one a star follows.")

    b.quiz_intro("Quiz 2", "Final Check — Evolution of Stars", 4)
    b.quiz_q(1, "Sun's fate", "The Sun, a low-mass star, will end its "
             "life as a:",
             ["black hole", "white dwarf", "neutron star", "supernova"])
    b.quiz_a(1, "B. white dwarf",
             "A low-mass star like the Sun becomes a red giant and then "
             "settles into a small, dense white dwarf.")
    b.quiz_q(2, "Big star", "A very massive star ends its life in a huge "
             "explosion called a:",
             ["red giant", "supernova", "white dwarf", "nebula"])
    b.quiz_a(2, "B. supernova",
             "A high-mass star becomes a supergiant and then explodes as "
             "a supernova.")
    b.quiz_q(3, "Black hole", "A black hole is a region where the "
             "gravitational force is so strong that:",
             ["it glows brightly", "not even light can escape", "stars are "
              "born", "sound cannot travel"])
    b.quiz_a(3, "B. not even light can escape",
             "A black hole, the end stage of a very massive star, has "
             "gravity so strong that nothing, not even light, escapes.")
    b.quiz_q(4, "Deciding factor", "Whether a star ends as a white dwarf "
             "or a black hole depends mainly on its:",
             ["colour", "mass", "distance from Earth", "temperature "
              "only"])
    b.quiz_a(4, "B. mass",
             "A star's initial mass decides its evolutionary path and its "
             "final stage.")

    b.closing("The Lives of the Stars",
              "Born in clouds of gas, shining for billions of years, and "
              "ending as white dwarfs, neutron stars or black holes — "
              "every star's story is written by its mass.")
    return b


def build():
    jobs = [
        ("MH08_S26_Heat_and_Temperature.pptx", heat1_deck),
        ("MH08_S28_Measurement_and_Effects_of_Heat_2.pptx", heat2_deck),
        ("MH08_S38_Sound.pptx", sound_deck),
        ("MH08_S67_Reflection_of_Light.pptx", reflection_deck),
        ("MH08_S77_Life_Cycle_of_Stars.pptx", stars_deck),
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
