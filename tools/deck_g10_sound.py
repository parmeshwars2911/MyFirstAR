"""
Grade 10 Physics — Chapter: Sound.
Session 62 (Lesson 1: sound waves, reflection, echo, speed by echo, uses) and
Session 63 (Lesson 2: vibrations, resonance, characteristics, music vs noise).
ICSE Class 10 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Sound  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    wave = b.asset("g10so_wave", D.longitudinal_wave("g10so_wave"))
    echo = b.asset("g10so_echo", D.echo_diagram("g10so_echo"))
    hero = b.asset("g10_sound_hero", wave)

    b.title("ICSE • Class 10 • Sound", "Sound Waves & Echo",
            "How sound travels  •  Reflection of sound  •  Echo  •  Speed of "
            "sound by echo", img=hero)
    b.objectives([
        "Describe sound as a longitudinal wave needing a medium",
        "State the laws governing the reflection of sound",
        "Define an echo and the condition for hearing one",
        "Calculate distances using the echo method",
        "Determine the speed of sound by an echo experiment",
        "List practical uses of the echo (SONAR, depth-finding)",
    ])
    b.divider(1, "Part 1", "Sound Waves & Reflection",
              "What sound is and how it bounces")
    b.text_image("SOUND WAVES", "Sound Is a Longitudinal Wave",
                 ["Sound travels as compressions and rarefactions of the "
                  "medium.",
                  "The particles vibrate back and forth along the direction "
                  "the wave travels.",
                  "Sound needs a material medium — it cannot travel through a "
                  "vacuum.",
                  "It travels fastest in solids, slower in liquids, slowest in "
                  "gases."],
                 wave, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="Compressions & rarefactions",
                 caption="Particles vibrate along the wave direction",
                 notes="Contrast with light (transverse, no medium needed). A "
                       "ringing bell in a vacuum jar goes silent — sound needs "
                       "matter.")
    b.cards("REFLECTION", "Sound Reflects Like Light", [
        ("Same laws", "The angle of incidence equals the angle of reflection, "
         "and all lie in one plane."),
        ("Hard surfaces", "Smooth, hard walls reflect sound well; soft "
         "surfaces absorb it."),
        ("Echo", "A reflected sound heard distinctly after the original is an "
         "echo."),
        ("Reverberation", "Many quick overlapping reflections in a hall are "
         "heard as reverberation."),
    ], notes="Sound obeys the same reflection laws as light. Distinguish a "
             "clean echo from blurred reverberation.")
    b.text_image("ECHO", "What Is an Echo?",
                 ["An echo is sound heard again after being reflected from a "
                  "distant surface.",
                  "The ear can separate two sounds only if they arrive at "
                  "least 0.1 s apart.",
                  "In that time sound travels about 34 m (there and back), so "
                  "the reflector must be at least ~17 m away.",
                  "Closer than this, the reflection merges with the original "
                  "sound."],
                 echo, img_side="right", img_w=5.8, img_h=3.6,
                 panel_title="Reflected sound, heard again",
                 caption="Echo needs a gap of at least 0.1 s",
                 notes="Derive the 17 m minimum from 0.1 s and 340 m/s. This "
                       "0.1 s 'persistence of hearing' is key to echo "
                       "problems.")
    b.statement("MINIMUM DISTANCE", "Why 17 Metres?",
                "To hear a distinct echo the reflecting surface must be far "
                "enough that the echo returns at least 0.1 s later.",
                formula="d  =  (v × t) / 2  =  (340 × 0.1) / 2  =  17 m",
                points=["The sound travels to the wall and back — twice the "
                        "distance.",
                        "Using v = 340 m/s and t = 0.1 s gives a minimum of "
                        "17 m.",
                        "This is why echoes are heard in large empty halls and "
                        "valleys, not small rooms."],
                notes="Show the factor of 2 for the round trip. Reinforce that "
                      "small rooms give reverberation, not echo.")
    b.worked("WORKED EXAMPLE", "Distance From an Echo",
             "A person shouts toward a cliff and hears the echo 3 seconds "
             "later. If the speed of sound is 340 m/s, how far away is the "
             "cliff?",
             ["Total distance travelled = v × t = 340 × 3 = 1020 m",
              "This is to the cliff AND back, so it is twice the distance.",
              "Distance to cliff = 1020 / 2 = 510 m"],
             "The cliff is 510 m away",
             notes="The classic trap: the echo time covers the round trip, so "
                   "divide by 2. Students who forget this double their answer.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Through a Vacuum", "An astronaut on the airless Moon strikes "
             "a bell. A nearby astronaut hears nothing because:",
             ["The bell is too quiet", "Sound cannot travel without a "
              "medium", "The Moon absorbs all sound",
              "Sound travels too fast there"])
    b.quiz_a(1, "B. Sound cannot travel without a medium",
             "Sound is a mechanical wave that needs particles to vibrate. The "
             "Moon has no air, so there is nothing to carry the sound — unlike "
             "light, which crosses the vacuum freely.")
    b.quiz_q(2, "Echo or Not?", "Why do you hear an echo in a large empty "
             "hall but not in a small bedroom?",
             ["Bedrooms have no walls",
              "In a small room the reflection returns in under 0.1 s and "
              "merges with the original",
              "Sound is louder in halls", "Bedrooms absorb all sound"])
    b.quiz_a(2, "B. The reflection returns in under 0.1 s",
             "An echo needs the reflected sound to arrive at least 0.1 s "
             "later, i.e. the wall must be ≥ 17 m away. A bedroom wall is far "
             "closer, so the reflection overlaps the original sound.")
    b.quiz_q(3, "Find the Distance", "A boy claps and hears the echo from a "
             "wall after 0.8 s. Taking the speed of sound as 340 m/s, the "
             "wall is:", ["272 m away", "136 m away", "425 m away",
              "68 m away"])
    b.quiz_a(3, "B. 136 m away",
             "Total path = 340 × 0.8 = 272 m. That is to the wall and back, so "
             "the wall is 272 / 2 = 136 m away.")
    b.quiz_q(4, "Speed Changes", "Sound travels fastest through which of "
             "these?", ["Air", "Water", "A steel rail", "A vacuum"])
    b.quiz_a(4, "C. A steel rail",
             "Sound travels fastest in solids, where particles are tightly "
             "packed and pass on the vibration quickly. It is slower in water, "
             "slower still in air, and impossible in a vacuum.")
    b.divider(2, "Part 2", "Speed of Sound & Uses of Echo",
              "Measuring sound and putting echoes to work")
    b.bullets("EXPERIMENT", "Speed of Sound by the Echo Method", [
        "Stand a measured distance d from a large reflecting wall (say 80 m).",
        "Clap and start timing; listen for the echo and stop timing.",
        "The sound has travelled 2d (to the wall and back) in time t.",
        "Speed of sound v = 2d / t.",
        "Repeat several times and average to reduce error.",
    ], panel_title="v = 2d / t",
       notes="A doable open-ground experiment. Stress 2d for the round trip "
             "and averaging to cut timing error.")
    b.worked("WORKED EXAMPLE", "Speed of Sound From an Echo",
             "A girl stands 170 m from a cliff, claps, and hears the echo "
             "after 1.0 s. Find the speed of sound.",
             ["Distance travelled by sound = 2 × 170 = 340 m",
              "v = distance / time = 340 / 1.0",
              "v = 340 m/s"],
             "Speed of sound ≈ 340 m/s",
             notes="Reinforces 2d again. The answer matches the standard speed "
                   "of sound in air at room temperature.")
    b.cards("USES OF ECHO", "Putting Echoes to Work", [
        ("SONAR", "Ships send sound pulses and time the echo from the seabed "
         "to measure depth and find shoals or wrecks."),
        ("Depth sounding", "Depth = (v × t) / 2, using the echo's round-trip "
         "time."),
        ("Ultrasound scans", "High-frequency echoes build images of a baby or "
         "internal organs."),
        ("Bats & dolphins", "They navigate and hunt by echolocation — natural "
         "SONAR."),
    ], notes="Each use is the echo principle applied. The depth/SONAR formula "
             "is the same 'divide by 2' idea.")
    b.text_image("SONAR", "How SONAR Finds the Seabed",
                 ["A ship sends a pulse of sound straight down into the water.",
                  "The pulse reflects off the seabed and returns as an echo.",
                  "The time t for the round trip is measured.",
                  "Depth = (speed of sound in water × t) / 2."],
                 echo, img_side="left", img_w=5.6, img_h=3.6,
                 panel_title="Echo-sounding under water",
                 caption="Depth from the echo's round-trip time",
                 notes="Note the speed of sound in water (~1500 m/s) is much "
                       "greater than in air. Same halving idea for depth.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Sound wave", "longitudinal; needs a medium; fastest in solids"),
        ("Reflection", "obeys the same laws as light"),
        ("Echo", "reflected sound heard ≥ 0.1 s later; wall ≥ 17 m away"),
        ("Round trip", "echo distance covers 2d — always divide by 2"),
        ("Speed by echo", "v = 2d / t"),
        ("Uses", "SONAR, depth-sounding, ultrasound, echolocation"),
    ], notes="Rapid recap; the '2d / divide by 2' idea is the through-line.")
    b.quiz_intro("Quiz 2", "Final Check — Speed & Uses", 5)
    b.quiz_q(1, "SONAR Depth", "A SONAR pulse returns from the seabed after "
             "0.4 s. If sound travels at 1500 m/s in water, the sea is:",
             ["600 m deep", "300 m deep", "1200 m deep", "150 m deep"])
    b.quiz_a(1, "B. 300 m deep",
             "Total path = 1500 × 0.4 = 600 m for the round trip, so the depth "
             "is 600 / 2 = 300 m. Always halve the echo distance.")
    b.quiz_q(2, "Why High Frequency?", "Ultrasound (not ordinary sound) is "
             "used for medical scans and SONAR mainly because it:",
             ["Travels faster", "Can be directed in a narrow beam and gives "
              "finer detail", "Is louder", "Is audible to humans"])
    b.quiz_a(2, "B. Forms a narrow beam with finer detail",
             "High-frequency ultrasound has a short wavelength, so it can be "
             "sent as a narrow beam and resolve small details — ideal for "
             "imaging and precise echo-location.")
    b.quiz_q(3, "Hall Design", "Concert halls are lined with soft curtains and "
             "carpets to:", ["Make sound travel faster",
              "Absorb sound and reduce excessive reverberation",
              "Create more echoes", "Increase the pitch"])
    b.quiz_a(3, "B. Absorb sound and reduce reverberation",
             "Soft, porous materials absorb sound instead of reflecting it. "
             "This cuts down repeated reflections (reverberation) that would "
             "otherwise blur the music or speech.")
    b.quiz_q(4, "Two Claps", "Standing between two parallel cliffs, a climber "
             "claps once but hears several echoes. This is because:",
             ["The clap was very loud",
              "Sound reflects back and forth repeatedly between the cliffs",
              "Sound speeds up between cliffs", "Echoes change pitch"])
    b.quiz_a(4, "B. Sound reflects back and forth repeatedly",
             "Each cliff reflects the sound to the other, which reflects it "
             "back again. These multiple reflections reach the ear at "
             "successive intervals, heard as a series of echoes.")
    b.quiz_q(5, "Estimate the Time", "For an echo to be heard, the reflecting "
             "wall must be at least about 17 m away. This distance comes from "
             "requiring the echo to return after at least:",
             ["0.01 s", "0.1 s", "1 s", "10 s"])
    b.quiz_a(5, "B. 0.1 s",
             "The ear separates two sounds only if they are ≥ 0.1 s apart. In "
             "0.1 s sound covers 34 m round-trip, i.e. a wall 17 m away — the "
             "minimum distance for a distinct echo.")
    b.closing("The Physics of Echoes",
              "From a shout in a valley to a ship mapping the seabed — every "
              "echo is just reflection, timed.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    chars = b.asset("g10so_chars", D.sound_characteristics("g10so_chars"))
    reson = b.asset("g10so_reson", D.resonance_pendulums("g10so_reson"))
    hero = b.asset("g10_resonance_hero", reson)

    b.title("ICSE • Class 10 • Sound", "Vibrations & Sound Quality",
            "Free, damped & forced vibrations  •  Resonance  •  Loudness, "
            "pitch & quality", img=hero)
    b.objectives([
        "Distinguish free, damped and forced vibrations",
        "Define resonance and give everyday examples",
        "Relate loudness to amplitude",
        "Relate pitch to frequency",
        "Explain the quality (timbre) of a sound",
        "Distinguish music from noise",
    ])
    b.divider(1, "Part 1", "Vibrations & Resonance",
              "How objects vibrate and when they sing")
    b.bullets("FREE VIBRATIONS", "Natural (Free) Vibrations", [
        ("Natural frequency", "Every object has its own frequency at which it "
         "vibrates when disturbed."),
        ("Free vibration", "Vibration at the natural frequency with no outside "
         "force, e.g. a struck tuning fork."),
        ("Depends on the body", "The natural frequency depends on the object's "
         "size, shape, tension and material."),
        ("In a vacuum", "Free vibrations would continue unchanged with no air "
         "resistance to slow them."),
    ], panel_title="Every object has a natural frequency",
       notes="Define natural frequency and free vibration. A pendulum or "
             "tuning fork left alone vibrates at its own rate.")
    b.cards("TYPES", "Free, Damped & Forced Vibrations", [
        ("Free", "At the natural frequency, with constant amplitude (ideal, "
         "no friction)."),
        ("Damped", "Amplitude steadily dies away as friction/air resistance "
         "removes energy."),
        ("Forced", "An outside periodic force drives the object at the "
         "force's frequency."),
        ("Everyday", "A guitar string left to ring is damped; a sewing machine "
         "shaking the table is forced."),
    ], notes="Three categories. Damped = dying away; forced = driven by an "
             "external periodic push.")
    b.text_image("RESONANCE", "Resonance",
                 ["Resonance occurs when the driving frequency equals the "
                  "object's natural frequency.",
                  "The object then absorbs energy efficiently and vibrates "
                  "with a large amplitude.",
                  "In coupled pendulums, only the one matching the driver's "
                  "length swings strongly.",
                  "Resonance can be useful — or destructive if amplitudes grow "
                  "too large."],
                 reson, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="Matching frequencies",
                 caption="Only the matching pendulum resonates",
                 notes="Define resonance as a frequency match giving large "
                       "amplitude. The pendulum demo makes it visual.")
    b.cards("EXAMPLES", "Resonance Around Us", [
        ("Tuning a radio", "We match the circuit's frequency to the station's "
         "to pick out one signal."),
        ("Pushing a swing", "Pushing in time with the swing's natural rhythm "
         "builds a big swing."),
        ("Musical instruments", "Air columns and strings resonate to amplify "
         "particular notes."),
        ("Bridges", "Marching in step can resonate a bridge dangerously — "
         "soldiers break step."),
    ], notes="Mix useful (radio, instruments) and dangerous (bridge) "
             "resonance. The swing is the most intuitive example.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Identify the Vibration", "A child on a swing is given a small "
             "push exactly once each time the swing returns. The swing's "
             "amplitude grows larger and larger. This is an example of:",
             ["Damped vibration", "Resonance", "Free vibration",
              "An echo"])
    b.quiz_a(1, "B. Resonance",
             "The pushes are timed to match the swing's natural frequency, so "
             "energy is added in step every cycle. The amplitude builds up — "
             "the defining feature of resonance.")
    b.quiz_q(2, "Dying Away", "A plucked guitar string gradually becomes "
             "quieter and finally stops. Its vibration is best described as:",
             ["Forced", "Resonant", "Damped", "Free and unending"])
    b.quiz_a(2, "C. Damped",
             "Friction and air resistance, plus energy passed to the sound, "
             "steadily remove energy from the string, so its amplitude decays. "
             "That is damping.")
    b.quiz_q(3, "Break Step", "Soldiers are ordered to 'break step' when "
             "crossing a footbridge to avoid:",
             ["Tiring their legs", "Driving the bridge at its natural "
              "frequency and resonating it", "Making too much noise",
              "Slipping on the bridge"])
    b.quiz_a(3, "B. Resonating the bridge",
             "If their rhythmic marching happened to match the bridge's "
             "natural frequency, resonance could build dangerously large "
             "oscillations. Breaking step keeps the force out of time.")
    b.quiz_q(4, "Same Note", "Two identical tuning forks stand side by side. "
             "One is struck, and soon the other begins to hum. This happens "
             "because they:", ["Are touching",
              "Have the same natural frequency, so the second resonates",
              "Are made of magnets", "Share the same air pressure"])
    b.quiz_a(4, "B. Have the same natural frequency",
             "Sound from the struck fork drives the second at exactly its "
             "natural frequency, so it resonates and starts to vibrate audibly "
             "— sympathetic resonance.")
    b.quiz_q(5, "Mismatched Fork", "If the second tuning fork had a small "
             "lump of wax added to one prong, striking the first fork would "
             "now make the second:",
             ["Resonate even more strongly", "Barely respond, because their "
              "frequencies no longer match", "Melt the wax",
              "Change to a higher pitch"])
    b.quiz_a(5, "B. Barely respond — frequencies no longer match",
             "The wax changes the second fork's natural frequency, so the "
             "driving sound is no longer in tune with it. Without a frequency "
             "match there is no resonance, and it stays almost silent.")
    b.divider(2, "Part 2", "Characteristics of Sound",
              "Loudness, pitch and quality — and music vs noise")
    b.text_image("LOUDNESS & PITCH", "Loudness and Pitch",
                 ["Loudness depends on the amplitude of the wave — bigger "
                  "amplitude, louder sound.",
                  "Pitch depends on the frequency — higher frequency, higher "
                  "pitch.",
                  "A drum gives a loud, low-pitched sound; a whistle a "
                  "high-pitched one.",
                  "Loudness and pitch are independent: a sound can be loud and "
                  "low, or soft and high."],
                 chars, img_side="right", img_w=6.0, img_h=3.2,
                 panel_title="Amplitude vs frequency",
                 caption="Amplitude → loudness; frequency → pitch",
                 notes="Keep loudness (amplitude) and pitch (frequency) "
                       "strictly separate — a common confusion.")
    b.bullets("AUDIBLE RANGE", "What We Can — and Cannot — Hear", [
        ("Audible range", "Humans hear roughly 20 Hz to 20,000 Hz."),
        ("Infrasonic", "Below 20 Hz — too low to hear; produced by "
         "earthquakes and large machines. Elephants use it."),
        ("Ultrasonic", "Above 20,000 Hz — too high to hear; used in SONAR, "
         "scans and cleaning. Bats and dogs hear it."),
        ("With age", "The upper limit of hearing falls as we grow older."),
    ], panel_title="20 Hz – 20,000 Hz",
       notes="Anchor the 20 Hz–20 kHz range, then place infrasonic below and "
             "ultrasonic above it, each with examples.")
    b.cards("QUALITY", "Quality (Timbre) of Sound", [
        ("Why instruments differ", "A piano and a violin playing the same "
         "note still sound different."),
        ("Quality / timbre", "This difference is the quality, set by the "
         "mixture of overtones in the sound."),
        ("Same pitch, same loudness", "Quality is what remains different even "
         "when pitch and loudness match."),
        ("Recognising voices", "We recognise people by the quality of their "
         "voices."),
    ], notes="Quality explains why the same note differs between instruments. "
             "It comes from the blend of harmonics.")
    b.cards("MUSIC vs NOISE", "Music and Noise", [
        ("Music", "A pleasant sound from regular, periodic vibrations."),
        ("Noise", "An unpleasant sound from irregular, non-periodic "
         "vibrations."),
        ("Regularity", "Music has a steady, repeating waveform; noise is "
         "jumbled."),
        ("It can vary", "Very loud 'music' can become noise; context matters "
         "too."),
    ], notes="Music = regular/periodic; noise = irregular. Tie back to "
             "waveform shape.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Free vibration", "at the natural frequency, no outside force"),
        ("Damped", "amplitude dies away as energy is lost"),
        ("Forced & resonance", "driven externally; resonance when frequencies "
         "match"),
        ("Loudness", "depends on amplitude"),
        ("Pitch", "depends on frequency"),
        ("Quality & music", "timbre from overtones; music is regular, noise "
         "irregular"),
    ], notes="Rapid recap; cold-call the amplitude/frequency/quality "
             "distinctions.")
    b.quiz_intro("Quiz 2", "Final Check — Characteristics", 5)
    b.quiz_q(1, "Turn It Up", "Turning up the volume on a speaker, without "
             "changing the song, increases the sound's:",
             ["Frequency", "Pitch", "Amplitude (loudness)", "Speed"])
    b.quiz_a(1, "C. Amplitude (loudness)",
             "Volume controls how much the speaker cone moves — the amplitude. "
             "Greater amplitude means a louder sound, while the pitch "
             "(frequency) of the notes is unchanged.")
    b.quiz_q(2, "Same Note, Different Sound", "A flute and a violin play the "
             "exactly same note equally loudly, yet sound different. They "
             "differ in:", ["Pitch", "Loudness", "Quality (timbre)", "Speed"])
    b.quiz_a(2, "C. Quality (timbre)",
             "Same note means same pitch; equally loud means same amplitude. "
             "The remaining difference is the quality, set by each "
             "instrument's particular mix of overtones.")
    b.quiz_q(3, "Higher Pitch", "To make a guitar string play a higher-pitched "
             "note you should:", ["Pluck it harder",
              "Tighten the string (increase its frequency)",
              "Use a thicker string", "Make the string longer"])
    b.quiz_a(3, "B. Tighten the string",
             "Pitch depends on frequency. Tightening (or shortening, or "
             "thinning) a string raises its frequency and so its pitch. "
             "Plucking harder only changes loudness.")
    b.quiz_q(4, "Music or Noise?", "Physically, the main difference between a "
             "musical note and noise is that a musical note has a:",
             ["Louder sound", "Regular, periodic waveform",
              "Higher pitch", "Faster speed"])
    b.quiz_a(4, "B. Regular, periodic waveform",
             "Music comes from regular, repeating vibrations that the ear "
             "finds pleasant; noise comes from irregular, non-periodic "
             "vibrations. Loudness and pitch are not the deciding factor.")
    b.quiz_q(5, "Bat in the Dark", "A bat flying in total darkness avoids "
             "obstacles by emitting high-pitched sound and listening for "
             "echoes. The property it relies on is that sound:",
             ["Travels faster in the dark", "Reflects off surfaces",
              "Changes colour", "Needs no medium"])
    b.quiz_a(5, "B. Reflects off surfaces",
             "Echolocation uses the reflection of sound. The bat times the "
             "echoes of its calls to judge how far away objects are — natural "
             "SONAR.")
    b.closing("The Music in Physics",
              "Amplitude, frequency and timbre turn simple vibrations into "
              "every sound you have ever heard.")
    return b


def build():
    for fname, fn in [("G10_S62_Sound_1.pptx", deck1),
                      ("G10_S63_Sound_2.pptx", deck2)]:
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
