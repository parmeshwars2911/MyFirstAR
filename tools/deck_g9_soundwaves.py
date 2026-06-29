"""
Grade 9 Physics — Chapter: Propagation of Sound Waves.
S101 (production, medium, propagation, wave terms, v = f λ) and
S102 (factors affecting speed of sound, comparison with light, speed
determination, infrasonic/ultrasonic, ultrasound uses).  ICSE Class 9.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Propagation of Sound Waves  •  ICSE Class 9 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    wave = b.asset("g9sw_long", D.longitudinal_wave("g9sw_long"))
    terms = b.asset("g9sw_terms", D.wave_terms("g9sw_terms"))
    hero = b.asset("g9_soundwave_hero", wave)

    b.title("ICSE • Class 9 • Sound", "How Sound Travels",
            "Production by vibration  •  Sound needs a medium  •  Wave terms  "
            "•  v = f λ", img=hero)
    b.objectives([
        "Explain how sound is produced by vibrations",
        "Show that sound needs a material medium to travel",
        "Describe how sound propagates through a medium",
        "Define the terms of wave motion",
        "Use the relation v = f λ",
        "Distinguish wavelength, frequency and amplitude",
    ])
    b.divider(1, "Part 1", "Producing & Propagating Sound",
              "What makes sound, and what carries it")
    b.bullets("PRODUCTION", "Sound Is Produced by Vibrations", [
        ("Vibrating sources", "A ringing bell, a plucked string and our vocal "
         "cords all vibrate to make sound."),
        ("Feel it", "Touch a sounding tuning fork or speaker and you feel the "
         "vibration."),
        ("Stops when still", "Damp the vibration and the sound stops at "
         "once."),
        ("Energy transfer", "The vibrating source passes energy to the "
         "surrounding medium."),
    ], panel_title="No vibration, no sound",
       notes="Anchor that ALL sound comes from vibration. The tuning-fork-in-"
             "water splash is a great demo.")
    b.statement("NEEDS A MEDIUM", "Sound Needs a Material Medium",
                "Sound cannot travel through a vacuum — it needs particles of "
                "a medium to pass the vibration along.",
                points=["A bell ringing in a jar grows silent as the air is "
                        "pumped out.",
                        "Sound travels through solids, liquids and gases.",
                        "It is fastest in solids and slowest in gases.",
                        "Light, by contrast, can cross a vacuum."],
                notes="The bell-jar experiment proves a medium is needed. "
                      "Order of speed: solids > liquids > gases.")
    b.text_image("PROPAGATION", "How Sound Travels in a Medium",
                 ["A vibrating source pushes the nearby particles together, "
                  "making a compression.",
                  "As it moves back it leaves them spread out, making a "
                  "rarefaction.",
                  "Compressions and rarefactions move outward — a longitudinal "
                  "wave.",
                  "The particles only vibrate to and fro; they do not travel "
                  "with the wave."],
                 wave, img_side="right", img_w=6.0, img_h=3.2,
                 panel_title="Compressions & rarefactions",
                 caption="A longitudinal wave of pressure",
                 notes="Sound is a longitudinal pressure wave. Stress that the "
                       "particles oscillate in place; the disturbance "
                       "travels.")
    b.text_image("WAVE TERMS", "Terms of Wave Motion",
                 ["Wavelength (λ): the distance for one complete wave "
                  "(compression + rarefaction).",
                  "Frequency (f): the number of waves per second, in hertz "
                  "(Hz).",
                  "Time period (T): the time for one wave; T = 1/f.",
                  "Amplitude: the maximum displacement, which sets the "
                  "loudness."],
                 terms, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="λ, f, T and amplitude",
                 caption="Wavelength, amplitude, crest and trough",
                 notes="Define each term. T = 1/f is essential. Amplitude → "
                       "loudness, frequency → pitch.")
    b.cards("WAVE TYPES", "Longitudinal vs Transverse Waves", [
        ("Longitudinal", "Particles vibrate along the direction of travel; made "
         "of compressions and rarefactions — e.g. sound."),
        ("Transverse", "Particles vibrate at right angles to the travel; made "
         "of crests and troughs — e.g. light, water ripples."),
        ("Sound is longitudinal", "It needs a medium and travels as pressure "
         "variations."),
        ("Both carry energy", "In each, energy moves forward while the "
         "particles only oscillate in place."),
    ], notes="Contrast the two wave types. Sound is longitudinal; light and "
             "ripples are transverse. Particles never travel with the wave.")
    b.bullets("SPEED IN MEDIA", "Sound Travels Fastest in Solids", [
        ("Solids", "Particles are tightly packed, so a vibration passes on "
         "almost at once — fastest (e.g. ~5000 m/s in steel)."),
        ("Liquids", "Particles are close but freer, so sound is slower (~1500 "
         "m/s in water)."),
        ("Gases", "Particles are far apart, so sound is slowest (~340 m/s in "
         "air)."),
        ("The rule", "The closer the particles, the faster sound travels: "
         "solids > liquids > gases."),
    ], panel_title="Closer particles → faster sound",
       notes="Order and rough values. Closely packed particles pass on the "
             "vibration quickly, so solids win.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Bell in a Jar", "As air is pumped out of a jar containing a "
             "ringing electric bell, the sound:",
             ["Gets louder", "Fades away to nothing", "Changes pitch only",
              "Stays the same"])
    b.quiz_a(1, "B. Fades away to nothing",
             "Removing the air takes away the medium that carries the sound. "
             "With fewer and fewer particles to pass on the vibration, the "
             "sound fades — proving sound needs a material medium.")
    b.quiz_q(2, "Particles Move?", "As a sound wave passes through air, the "
             "air particles:", ["Travel along with the wave to your ear",
              "Vibrate to and fro about fixed positions",
              "Stay completely still", "Move only upward"])
    b.quiz_a(2, "B. Vibrate to and fro about fixed positions",
             "In a longitudinal wave the particles merely oscillate back and "
             "forth; it is the disturbance (compressions and rarefactions) "
             "that travels, not the particles themselves.")
    b.quiz_q(3, "Time Period", "A sound wave has a frequency of 250 Hz. Its "
             "time period is:", ["250 s", "0.004 s", "0.04 s", "2.5 s"])
    b.quiz_a(3, "B. 0.004 s",
             "T = 1/f = 1/250 = 0.004 s. The time period is just the "
             "reciprocal of the frequency.")
    b.quiz_q(4, "Fastest Medium", "Sound travels fastest through:",
             ["Air", "Water", "Steel", "A vacuum"])
    b.quiz_a(4, "C. Steel",
             "Sound is fastest in solids, where the tightly packed particles "
             "pass the vibration on quickly; slower in liquids, slowest in "
             "gases, and impossible in a vacuum.")
    b.quiz_q(5, "Which Is Longitudinal?", "In which wave do the particles of "
             "the medium vibrate along the same direction as the wave travels?",
             ["A water ripple", "A light wave", "A sound wave",
              "All transverse waves"])
    b.quiz_a(5, "C. A sound wave",
             "Sound is a longitudinal wave — its particles oscillate back and "
             "forth along the direction of travel, forming compressions and "
             "rarefactions. Light and ripples are transverse.")
    b.divider(2, "Part 2", "The Wave Equation",
              "Linking speed, frequency and wavelength")
    b.statement("v = f λ", "Speed, Frequency and Wavelength",
                "The speed of a wave equals its frequency multiplied by its "
                "wavelength.",
                formula="v  =  f × λ",
                points=["v is the wave speed, f the frequency, λ the "
                        "wavelength.",
                        "In a given medium the speed is fixed, so a higher "
                        "frequency means a shorter wavelength.",
                        "It applies to all waves, including sound and light."],
                notes="v = fλ is the central equation. In one medium v is "
                      "constant, so f and λ trade off.")
    b.worked("WORKED EXAMPLE", "Using v = f λ",
             "A sound wave of frequency 170 Hz travels through air at 340 m/s. "
             "Find its wavelength.",
             ["v = f × λ   →   λ = v / f",
              "λ = 340 / 170",
              "λ = 2 m"],
             "Wavelength = 2 m",
             notes="Rearrange v = fλ for λ. A 170 Hz note has a 2 m "
                   "wavelength in air.")
    b.worked("WORKED EXAMPLE", "Finding the Frequency",
             "Ripples on water travel at 0.5 m/s with a wavelength of 0.1 m. "
             "Find their frequency.",
             ["v = f × λ   →   f = v / λ",
              "f = 0.5 / 0.1",
              "f = 5 Hz"],
             "Frequency = 5 Hz",
             notes="Same equation, different unknown. Reinforces that v = fλ "
                   "works for any wave.")
    b.cards("LOUDNESS & PITCH", "What Amplitude and Frequency Decide", [
        ("Amplitude → loudness", "A bigger amplitude carries more energy and "
         "sounds louder."),
        ("Frequency → pitch", "A higher frequency sounds higher in pitch."),
        ("Independent", "A sound can be loud and low, or soft and high."),
        ("Energy", "Loud sounds transfer more energy to the ear."),
    ], notes="Keep amplitude (loudness) and frequency (pitch) separate — a "
             "frequent confusion.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Production", "all sound comes from a vibrating source"),
        ("Medium", "sound needs a medium; fastest in solids"),
        ("Propagation", "longitudinal wave of compressions & rarefactions"),
        ("Terms", "wavelength, frequency, time period (T = 1/f), amplitude"),
        ("Wave equation", "v = f λ"),
        ("Loudness & pitch", "amplitude → loudness; frequency → pitch"),
    ], notes="Rapid recap; v = fλ and T = 1/f are the must-know relations.")
    b.quiz_intro("Quiz 2", "Final Check — The Wave Equation", 5)
    b.quiz_q(1, "Find the Wavelength", "A tuning fork of frequency 512 Hz "
             "sounds in air where the speed of sound is 340 m/s. Its "
             "wavelength is about:", ["0.66 m", "1.5 m", "174 m", "0.0015 m"])
    b.quiz_a(1, "A. 0.66 m",
             "λ = v/f = 340/512 ≈ 0.66 m. A higher-frequency note has a "
             "shorter wavelength.")
    b.quiz_q(2, "Higher Note", "In the same air, a higher-pitched note "
             "compared with a lower one has a:", ["Greater speed",
              "Shorter wavelength", "Larger amplitude", "Longer time period"])
    b.quiz_a(2, "B. Shorter wavelength",
             "The speed of sound in the air is fixed, so by v = fλ a higher "
             "frequency must have a shorter wavelength.")
    b.quiz_q(3, "Same Medium", "Two sounds of different frequencies travel "
             "through the same air. They have the same:", ["Wavelength",
              "Speed", "Pitch", "Time period"])
    b.quiz_a(3, "B. Speed",
             "All sounds travel at the same speed in a given medium. They can "
             "differ in frequency and wavelength, but v stays the same — so "
             "their speeds are equal.")
    b.quiz_q(4, "Louder Sound", "Striking a drum harder makes a louder sound "
             "because it increases the wave's:", ["Frequency", "Speed",
              "Amplitude", "Wavelength"])
    b.quiz_a(4, "C. Amplitude",
             "A harder hit makes the drum skin vibrate with a larger "
             "amplitude. Greater amplitude carries more energy and is heard as "
             "a louder sound; the pitch is unchanged.")
    b.quiz_q(5, "Period and Frequency", "A wave has a time period of 0.02 s. "
             "Its frequency is:", ["0.02 Hz", "20 Hz", "50 Hz", "500 Hz"])
    b.quiz_a(5, "C. 50 Hz",
             "f = 1/T = 1/0.02 = 50 Hz. Frequency and time period are "
             "reciprocals of each other.")
    b.closing("Sound on the Move",
              "Vibrations become travelling waves of pressure — and v = f λ "
              "ties their speed, pitch and wavelength together.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    echo = b.asset("g9sw_echo", D.echo_diagram("g9sw_echo"))
    hero = b.asset("g9_ultrasound_hero", echo)

    b.title("ICSE • Class 9 • Sound", "Speed of Sound & Ultrasound",
            "What changes the speed  •  Sound vs light  •  Measuring the "
            "speed  •  Ultrasound", img=hero)
    b.objectives([
        "List the factors that affect the speed of sound in a gas",
        "List the factors that do NOT affect it",
        "Compare the speed of sound with the speed of light",
        "Describe how the speed of sound in air is measured",
        "Distinguish infrasonic, sonic and ultrasonic sounds",
        "State the uses of ultrasound",
    ])
    b.divider(1, "Part 1", "The Speed of Sound",
              "What does — and does not — change it")
    b.cards("AFFECTS SPEED", "Factors That Affect the Speed in a Gas", [
        ("Temperature", "Sound travels faster in warmer air (about 0.6 m/s "
         "faster per °C)."),
        ("Humidity", "Sound travels faster in moist (humid) air than in dry "
         "air."),
        ("Nature of the gas", "It travels faster in a lighter, less dense "
         "gas."),
        ("Wind", "Wind blowing toward the listener adds to the apparent "
         "speed."),
    ], notes="Speed of sound in a gas rises with temperature and humidity, and "
             "in lighter gases. These are commonly examined.")
    b.cards("DOES NOT AFFECT", "Factors That Do NOT Affect the Speed", [
        ("Pressure", "Changing the pressure of a gas (at fixed temperature) "
         "does not change the speed."),
        ("Loudness (amplitude)", "A loud and a soft sound travel at the same "
         "speed."),
        ("Frequency / pitch", "High and low notes travel at the same speed — "
         "or music would arrive jumbled."),
        ("Wavelength", "Follows frequency; it does not change the speed in a "
         "given gas."),
    ], notes="Crucial list: pressure, loudness, frequency and wavelength do "
             "NOT change the speed. The 'music not jumbled' argument is "
             "memorable.")
    b.statement("SOUND vs LIGHT", "Sound Compared With Light",
                "Light travels almost a million times faster than sound, which "
                "is why we see distant events before we hear them.",
                formula="v(light) = 3 × 10⁸ m/s   ≫   v(sound) ≈ 340 m/s",
                points=["We see lightning before we hear the thunder.",
                        "Light can travel through a vacuum; sound cannot.",
                        "Light is a transverse wave; sound is longitudinal."],
                notes="The huge speed gap explains the lightning-then-thunder "
                      "delay. Also contrast medium and wave type.")
    b.text_image("MEASURE", "Measuring the Speed of Sound (Echo Method)",
                 ["Stand a measured distance d from a large wall.",
                  "Clap and measure the time t for the echo to return.",
                  "The sound travels 2d (to the wall and back) in time t.",
                  "Speed of sound v = 2d / t — repeat and average."],
                 echo, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="v = 2d / t",
                 caption="Time the echo from a distant wall",
                 notes="The echo method: remember 2d for the round trip and "
                       "average several readings to reduce error.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Hot Day", "On a hot afternoon compared with a cold morning, "
             "the speed of sound in the air is:", ["Lower", "Higher",
              "Unchanged", "Zero"])
    b.quiz_a(1, "B. Higher",
             "Sound travels faster in warmer air — roughly 0.6 m/s faster for "
             "each degree Celsius rise — because the particles move and "
             "collide more rapidly.")
    b.quiz_q(2, "No Effect", "Which of these does NOT change the speed of "
             "sound in a gas?", ["Temperature", "Humidity", "Pressure (at "
              "constant temperature)", "The type of gas"])
    b.quiz_a(2, "C. Pressure (at constant temperature)",
             "At a fixed temperature, changing a gas's pressure does not alter "
             "the speed of sound, because density changes in proportion. "
             "Temperature, humidity and the gas itself do affect it.")
    b.quiz_q(3, "Thunder Delay", "You see a flash of lightning and hear the "
             "thunder 3 seconds later. This delay occurs because:",
             ["Thunder happens after lightning", "Light travels far faster "
              "than sound", "Sound is louder than light", "The storm is "
              "moving"])
    b.quiz_a(3, "B. Light travels far faster than sound",
             "Light reaches you almost instantly, but sound at ~340 m/s takes "
             "time to arrive. The 3 s gap is the time the thunder's sound "
             "needs to cover the distance.")
    b.quiz_q(4, "Echo Distance", "An echo from a cliff returns in 2 s when the "
             "speed of sound is 340 m/s. The cliff is:", ["680 m away",
              "340 m away", "170 m away", "1020 m away"])
    b.quiz_a(4, "B. 340 m away",
             "The sound travels 2d = 340 × 2 = 680 m for the round trip, so "
             "the cliff is 680 / 2 = 340 m away.")
    b.quiz_q(5, "Humid Air", "Sound travels slightly faster on a humid day "
             "than on a dry day because moist air is:",
             ["Denser", "Slightly less dense than dry air", "Hotter",
              "At higher pressure"])
    b.quiz_a(5, "B. Slightly less dense than dry air",
             "Water vapour is lighter than the nitrogen and oxygen it "
             "replaces, so humid air is a little less dense — and sound "
             "travels faster in a less dense gas.")
    b.cards("REFLECTION & ECHO", "Reflection of Sound and the Echo", [
        ("Sound reflects", "Sound bounces off hard surfaces, obeying the same "
         "laws as light (angle in = angle out)."),
        ("Echo", "A reflected sound heard separately from the original is an "
         "echo."),
        ("Condition", "The reflector must be far enough that the echo returns "
         "at least 0.1 s later (about 17 m away)."),
        ("Uses", "Echoes are used in SONAR and depth-sounding, and to measure "
         "the speed of sound."),
    ], notes="Sound reflects like light; a distinct echo needs the reflector "
             "≥ ~17 m away (0.1 s gap). Basis of the echo method and SONAR.")
    b.cards("CHARACTERISTICS", "Characteristics of a Musical Sound", [
        ("Loudness", "Set by the amplitude — a bigger vibration sounds "
         "louder."),
        ("Pitch", "Set by the frequency — a higher frequency sounds "
         "higher-pitched."),
        ("Quality (timbre)", "Lets us tell two instruments apart even at the "
         "same pitch and loudness."),
        ("Musical note vs noise", "A note has a regular, pleasant waveform; "
         "noise is irregular and jarring."),
    ], notes="The three characteristics — loudness, pitch, quality — plus the "
             "music-vs-noise distinction.")
    b.divider(2, "Part 2", "Infrasound, Ultrasound & Uses",
              "Sounds beyond our hearing")
    b.cards("RANGE", "Infrasonic, Sonic and Ultrasonic", [
        ("Audible (sonic)", "Frequencies we can hear: about 20 Hz to "
         "20,000 Hz."),
        ("Infrasonic", "Below 20 Hz — too low to hear; from earthquakes and "
         "large animals like elephants."),
        ("Ultrasonic", "Above 20,000 Hz — too high to hear; produced and heard "
         "by bats and dolphins."),
        ("With age", "The upper limit of human hearing drops as we grow "
         "older."),
    ], notes="The three ranges around the 20 Hz–20 kHz audible band. "
             "Infrasonic below, ultrasonic above.")
    b.bullets("ULTRASOUND", "Uses of Ultrasound", [
        ("Medical scans", "Ultrasound builds images of a baby or internal "
         "organs safely."),
        ("SONAR", "Ships find the depth of the sea and locate shoals or "
         "wrecks."),
        ("Cleaning", "Ultrasonic vibrations clean delicate items like "
         "jewellery and instruments."),
        ("Flaw detection", "Reveals hidden cracks inside metal castings and "
         "welds."),
    ], panel_title="High-frequency sound at work",
       notes="Ultrasound's short wavelength gives fine detail and a narrow "
             "beam — ideal for imaging, SONAR, cleaning and testing.")
    b.cards("WHY ULTRASOUND", "Why Ultrasound Is So Useful", [
        ("Narrow beam", "Its short wavelength can be sent as a focused, "
         "directed beam."),
        ("Fine detail", "Short wavelengths resolve small features in scans and "
         "tests."),
        ("Harmless", "At the levels used, it does not damage living tissue "
         "like X-rays can."),
        ("Echoes", "It reflects clearly off boundaries, so echoes can be "
         "timed and imaged."),
    ], notes="The advantages flow from the short wavelength: directed beam, "
             "fine detail, plus it is non-ionising and safe.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Affects speed", "temperature, humidity, the gas itself, wind"),
        ("No effect", "pressure, loudness, frequency, wavelength"),
        ("Sound vs light", "light ≈ 3 × 10⁸ m/s ≫ sound ≈ 340 m/s"),
        ("Measuring speed", "echo method, v = 2d / t"),
        ("Ranges", "infrasonic < 20 Hz < audible < 20 kHz < ultrasonic"),
        ("Ultrasound uses", "scans, SONAR, cleaning, flaw detection"),
    ], notes="Rapid recap; the affects/does-not-affect lists and ultrasound "
             "uses are the key exam points.")
    b.quiz_intro("Quiz 2", "Final Check — Speed & Ultrasound", 5)
    b.quiz_q(1, "Bat Navigation", "A bat finds insects in the dark by emitting "
             "and listening for:", ["Infrasound", "Ultrasound",
              "Visible light", "Radio waves"])
    b.quiz_a(1, "B. Ultrasound",
             "Bats emit ultrasonic squeaks (above 20,000 Hz) and listen for "
             "the echoes to locate insects and obstacles — echolocation using "
             "ultrasound.")
    b.quiz_q(2, "Why Not X-rays?", "Ultrasound is preferred over X-rays for "
             "scanning an unborn baby because ultrasound:",
             ["Is cheaper only", "Does not harm living tissue at the levels "
              "used", "Travels faster", "Is visible"])
    b.quiz_a(2, "B. Does not harm living tissue",
             "Ultrasound is non-ionising, so at scanning levels it is safe for "
             "the baby and mother — unlike X-rays, which can damage living "
             "cells.")
    b.quiz_q(3, "Music Arrives Together", "We know that all frequencies of "
             "sound travel at the same speed in air because, otherwise, a "
             "distant band's music would:", ["Be louder",
              "Arrive jumbled, with high and low notes out of step",
              "Travel faster", "Not be heard at all"])
    b.quiz_a(3, "B. Arrive jumbled",
             "If high and low notes travelled at different speeds, they would "
             "reach a distant listener at different times and the tune would "
             "be scrambled. Since music stays in tune, all frequencies share "
             "one speed.")
    b.quiz_q(4, "Infrasonic", "A sound of frequency 10 Hz is:",
             ["Audible", "Infrasonic (below hearing)", "Ultrasonic (above "
              "hearing)", "The loudest possible"])
    b.quiz_a(4, "B. Infrasonic (below hearing)",
             "10 Hz is below the 20 Hz lower limit of human hearing, so it is "
             "infrasonic — the kind of low rumble produced by earthquakes.")
    b.quiz_q(5, "SONAR Depth", "A ship's SONAR pulse returns from the seabed "
             "in 0.5 s. If sound travels at 1500 m/s in water, the depth is:",
             ["750 m", "375 m", "3000 m", "1500 m"])
    b.quiz_a(5, "B. 375 m",
             "Total path = 1500 × 0.5 = 750 m for the round trip, so the depth "
             "is 750 / 2 = 375 m. Always halve the echo distance.")
    b.closing("Beyond What We Can Hear",
              "From a clap's echo to a baby's first scan, understanding the "
              "speed and range of sound puts it to work for us.")
    return b


def build():
    for fname, fn in [("G9_S101_Propagation_of_Sound_1.pptx", deck1),
                      ("G9_S102_Propagation_of_Sound_2.pptx", deck2)]:
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
