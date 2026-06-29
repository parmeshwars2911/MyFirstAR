"""
Grade 8 Physics — Chapter: Sound.
S61 (production of sound, propagation, need for a medium, longitudinal
waves, representation of a wave) and S62 (characteristics of a sound wave:
amplitude/loudness, frequency/pitch, quality/timbre, noise vs music).
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
FOOTER = "Sound  •  ICSE Class 8 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["purple"])
    longw = b.asset("g8snd_long", D.longitudinal_wave("g8snd_long"))
    waveterms = b.asset("g8snd_waveterms", D.wave_terms("g8snd_waveterms"))
    hero = b.asset("g8_sound_hero", longw)

    b.title("ICSE • Class 8 • Sound", "How Sound is Made & Travels",
            "Vibrations  •  A medium to travel  •  Longitudinal waves  •  "
            "Picturing a wave", img=hero)
    b.objectives([
        "Explain that sound is produced by vibrating bodies",
        "Show that sound needs a material medium to travel",
        "Explain why sound cannot travel through a vacuum",
        "Describe a sound wave as a longitudinal wave",
        "Identify compressions and rarefactions in a sound wave",
        "Represent a wave and compare speeds of sound in different media",
    ])
    b.divider(1, "Part 1", "Producing & Carrying Sound",
              "Vibrations and the medium they travel through")
    b.cards("PRODUCTION", "Sound Comes From Vibrations", [
        ("Vibration", "The rapid to-and-fro motion of a body is called "
         "vibration."),
        ("Every sound source", "A plucked string, a struck drum, a ringing "
         "bell — all are vibrating."),
        ("Feel it", "Touch your throat while you speak — the vibrating vocal "
         "cords can be felt."),
        ("Stop the vibration", "Hold a struck tuning fork or bell and the "
         "sound dies at once."),
    ], notes="Core idea: sound is produced by vibrating bodies. Demonstrations: "
             "throat, tuning fork, drum, bell. Stop the vibration → stop the "
             "sound.")
    b.statement("A MEDIUM", "Sound Needs a Material Medium",
                "Sound cannot travel on its own — it needs particles of a "
                "solid, liquid or gas to pass the vibration along.",
                points=["The vibrating source pushes the particles next to it, "
                        "which push the next, and so on.",
                        "The disturbance travels outward, but the particles "
                        "only move to and fro about their places.",
                        "Solids carry sound best, then liquids, then gases."],
                notes="Sound is a mechanical wave: it needs a medium. Particles "
                      "pass the disturbance along without travelling "
                      "themselves.")
    b.text_image("NO VACUUM", "Why There Is No Sound in a Vacuum",
                 ["A vacuum has no particles to carry the vibration.",
                  "In the classic bell-jar experiment, an electric bell rings "
                  "inside a jar.",
                  "As the air is pumped out, the sound grows fainter and "
                  "fainter.",
                  "When the jar is nearly empty, the bell is seen striking but "
                  "is no longer heard."],
                 waveterms, img_side="right", img_w=6.0, img_h=3.0,
                 panel_title="The bell-jar experiment",
                 caption="No medium, no sound",
                 notes="Bell-jar experiment proves sound needs a medium: remove "
                       "the air and the sound fades to nothing, even though the "
                       "bell still moves.")
    b.text_image("LONGITUDINAL", "A Sound Wave is a Longitudinal Wave",
                 ["The particles vibrate back and forth along the same "
                  "direction the sound travels.",
                  "Where particles crowd together we get a compression (high "
                  "pressure).",
                  "Where they spread apart we get a rarefaction (low "
                  "pressure).",
                  "A sound wave is a moving pattern of compressions and "
                  "rarefactions."],
                 longw, img_side="right", img_w=6.2, img_h=3.0,
                 panel_title="Compressions & rarefactions",
                 caption="Particles vibrate along the direction of travel",
                 notes="Longitudinal wave: particle motion is parallel to the "
                       "direction of travel. Compressions (crowded) and "
                       "rarefactions (spread out) alternate.")
    b.cards("MANY MEDIA", "Sound Through Solids, Liquids and Gases", [
        ("Through air", "We hear most everyday sounds carried to us by the "
         "air."),
        ("Through water", "A swimmer underwater can hear sounds; whales call "
         "across the sea."),
        ("Through solids", "Put an ear to a desk and a gentle tap at the far "
         "end is heard clearly."),
        ("Why it differs", "Closely packed particles in solids pass the "
         "vibration on best, gases the least."),
    ], notes="Sound travels through all three states of matter. Solids carry it "
             "best because their particles are closely packed.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Silent Bell", "An electric bell rings inside a glass jar. As "
             "the air is slowly pumped out, the sound:",
             ["Grows louder", "Fades until it can no longer be heard",
              "Stays the same", "Turns into an echo"])
    b.quiz_a(1, "B. Fades until it can no longer be heard",
             "Sound needs particles to travel. As the air is removed there are "
             "fewer particles to carry the vibration, so the sound fades — even "
             "though the bell is still seen striking.")
    b.quiz_q(2, "Source of Sound", "Every source of sound has one thing in "
             "common — it is:", ["Hot", "Vibrating", "Glowing", "Heavy"])
    b.quiz_a(2, "B. Vibrating",
             "Whether it is a string, a drum skin or vocal cords, a body must "
             "vibrate to make sound. Stop the vibration and the sound stops "
             "instantly.")
    b.quiz_q(3, "Particle Motion", "In a sound wave travelling through air, the "
             "air particles:", ["Travel all the way with the sound",
              "Vibrate to and fro about fixed positions", "Stay perfectly "
              "still", "Move at right angles to the wave"])
    b.quiz_a(3, "B. Vibrate to and fro about fixed positions",
             "The disturbance moves forward, but each particle only swings back "
             "and forth about its own place, passing the energy to the next "
             "particle. That is why it is a longitudinal wave.")
    b.quiz_q(4, "Best Carrier", "Through which medium does sound usually travel "
             "fastest?", ["Air", "Water", "Steel", "Vacuum"])
    b.quiz_a(4, "C. Steel",
             "Particles in a solid are packed tightly and pass vibrations on "
             "quickly, so sound travels fastest in solids like steel, slower in "
             "liquids, and slowest in gases.")
    b.divider(2, "Part 2", "Picturing & Speeding Sound",
              "Representing a wave and how fast it moves")
    b.text_image("REPRESENTATION", "Representing a Wave",
                 ["A sound wave is hard to draw, so we picture it as a smooth "
                  "curve.",
                  "The crests stand for compressions and the troughs for "
                  "rarefactions.",
                  "This makes it easy to mark the wavelength and amplitude.",
                  "The curve is only a picture — the real sound is still a "
                  "longitudinal wave."],
                 waveterms, img_side="right", img_w=6.2, img_h=3.0,
                 panel_title="A wave on paper",
                 caption="Crest = compression, trough = rarefaction",
                 notes="We represent the longitudinal sound wave as a curve so "
                       "wavelength and amplitude are easy to mark. Remind "
                       "students it is only a representation.")
    b.cards("SPEED", "The Speed of Sound", [
        ("Depends on the medium", "Sound travels at different speeds in "
         "solids, liquids and gases."),
        ("Fastest in solids", "Tightly packed particles pass on the vibration "
         "quickly."),
        ("In air", "About 330–340 m/s at ordinary temperature."),
        ("Much slower than light", "We see lightning before we hear the "
         "thunder, though both start together."),
    ], notes="Speed of sound: fastest in solids, slowest in gases, ~340 m/s in "
             "air. Far slower than light — hence the lightning-then-thunder "
             "gap.")
    echo = b.asset("g8snd_echo", D.echo_diagram("g8snd_echo"))
    b.text_image("ECHO", "Reflection of Sound — the Echo",
                 ["Sound bounces off a hard surface just as a ball bounces off "
                  "a wall.",
                  "A reflected sound heard separately from the original is "
                  "called an echo.",
                  "We hear a distinct echo only if the reflecting surface is "
                  "far enough away.",
                  "Echoes are used to find the depth of the sea and to locate "
                  "objects under water."],
                 echo, img_side="right", img_w=6.0, img_h=3.0,
                 panel_title="Sound that comes back",
                 caption="The reflected sound returns to the listener",
                 notes="Reflection of sound gives an echo. A distinct echo "
                       "needs a distant surface. Used in depth-sounding and "
                       "locating underwater objects.")
    b.cards("EVERYDAY", "Sound in Everyday Life", [
        ("Talking & music", "Vocal cords and instruments turn vibrations into "
         "the sounds we share."),
        ("Telephones", "Speech is changed to signals, sent far away, then "
         "turned back into sound."),
        ("Warnings", "Horns, bells and sirens use loud sound to alert us."),
        ("Finding things", "Ships use reflected sound (sonar) to measure depth "
         "and spot objects."),
    ], notes="Everyday roles of sound: communication, music, warnings and "
             "sonar. Connects the physics to students' lives.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Production", "sound is made by vibrating bodies"),
        ("Medium", "sound needs particles — solid, liquid or gas"),
        ("Vacuum", "no particles, so no sound"),
        ("Longitudinal", "compressions and rarefactions along the travel"),
        ("Representation", "drawn as a curve: crest = compression"),
        ("Speed", "fastest in solids, ~340 m/s in air, slower than light"),
    ], notes="Rapid recap of production, the need for a medium, the "
             "longitudinal nature and the speed of sound.")
    b.quiz_intro("Quiz 2", "Final Check — Producing & Carrying Sound", 5)
    b.quiz_q(1, "Thunder Delay", "We see a flash of lightning several seconds "
             "before we hear the thunder because:", ["Light is louder",
              "Light travels much faster than sound", "Sound is blocked by "
              "clouds", "Thunder starts later"])
    b.quiz_a(1, "B. Light travels much faster than sound",
             "Light reaches us almost instantly, while sound crawls along at "
             "about 340 m/s. Both begin together, but the sound arrives "
             "noticeably later, giving the delay.")
    b.quiz_q(2, "Crowded Particles", "The region of a sound wave where the air "
             "particles are crowded together is called a:",
             ["Rarefaction", "Compression", "Crest", "Vacuum"])
    b.quiz_a(2, "B. Compression",
             "Where the particles bunch up the air pressure is high — this is a "
             "compression. Where they spread apart the pressure is low — that "
             "is a rarefaction.")
    b.quiz_q(3, "Astronauts Talk", "Two astronauts in open space cannot hear "
             "each other speak directly because space is:",
             ["Too cold", "A vacuum with no medium to carry sound", "Too "
              "bright", "Too far"])
    b.quiz_a(3, "B. A vacuum with no medium to carry sound",
             "Open space has almost no particles, so there is nothing to carry "
             "the vibrations of speech. The astronauts must use radio, which "
             "travels as electromagnetic waves needing no medium.")
    b.quiz_q(4, "Direction of Vibration", "In a longitudinal wave the particles "
             "of the medium vibrate:", ["At right angles to the wave",
              "Along the same direction the wave travels", "In circles",
              "Not at all"])
    b.quiz_a(4, "B. Along the same direction the wave travels",
             "A longitudinal wave has its particle motion parallel to the "
             "direction of travel, producing compressions and rarefactions. "
             "Sound in air is exactly this kind of wave.")
    b.quiz_q(5, "Ear to the Rail", "Putting an ear to a steel railway track "
             "lets us hear an approaching train sooner than through the air "
             "because sound travels:", ["Slower in steel", "Faster in steel "
              "than in air", "Only in air", "Backwards"])
    b.quiz_a(5, "B. Faster in steel than in air",
             "Sound travels much faster through a solid like steel than through "
             "air, so the vibrations along the rail reach the ear before the "
             "sound carried by the air.")
    b.closing("Sound on the Move",
              "A vibration sets the particles of matter dancing — passing the "
              "sound from one to the next, but never through empty space.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["orange"])
    chars = b.asset("g8snd_chars", D.sound_characteristics("g8snd_chars"))
    waveterms = b.asset("g8snd_waveterms", D.wave_terms("g8snd_waveterms"))
    hero = b.asset("g8_sound2_hero", chars)

    b.title("ICSE • Class 8 • Sound", "Characteristics of Sound",
            "Amplitude & loudness  •  Frequency & pitch  •  Quality  •  "
            "Noise vs music", img=hero)
    b.objectives([
        "Define amplitude, frequency, time period and wavelength",
        "Relate amplitude to the loudness of a sound",
        "Relate frequency to the pitch of a sound",
        "Explain quality (timbre) and why instruments sound different",
        "Distinguish a musical note from noise",
        "Give everyday examples of the characteristics of sound",
    ])
    b.divider(1, "Part 1", "Measuring a Wave",
              "Amplitude, frequency, time period and wavelength")
    b.bullets("WAVE QUANTITIES", "Quantities That Describe a Wave", [
        ("Amplitude", "The greatest distance a particle moves from its rest "
         "position."),
        ("Frequency", "The number of vibrations made in one second, measured "
         "in hertz (Hz)."),
        ("Time period", "The time taken for one complete vibration; it is "
         "1 ÷ frequency."),
        ("Wavelength", "The distance covered by one complete wave."),
    ], panel_title="The four key terms",
       notes="Define the four wave quantities. Stress frequency (Hz) and that "
             "time period = 1/frequency.")
    b.text_image("AMPLITUDE", "Amplitude Decides Loudness",
                 ["A bigger vibration carries more energy.",
                  "Larger amplitude means a louder sound.",
                  "Striking a drum harder makes a bigger vibration and a louder "
                  "beat.",
                  "Loudness also falls off as we move away from the source."],
                 chars, img_side="right", img_w=6.4, img_h=3.0,
                 panel_title="Bigger swing = louder",
                 caption="Loud and soft waves have the same pitch but different "
                         "amplitude",
                 notes="Amplitude → loudness. Harder strike = bigger amplitude "
                       "= louder. Loudness also depends on distance from the "
                       "source.")
    b.statement("INTENSITY", "Loudness and Intensity",
                "Loudness is how loud a sound seems to our ears, while "
                "intensity is the sound energy actually arriving each second on "
                "a given area.",
                points=["Greater amplitude → greater intensity → louder "
                        "sound.",
                        "Loudness depends on intensity but also on how "
                        "sensitive the listener's ear is.",
                        "Loudness is measured in a unit called the decibel "
                        "(dB)."],
                notes="Distinguish loudness (perceived) from intensity "
                      "(energy/area). Decibel is the unit of loudness.")
    b.cards("HOW LOUD?", "Everyday Sound Levels", [
        ("Whisper", "A soft rustle of about 10–20 dB, barely heard across a "
         "quiet room."),
        ("Normal talk", "Ordinary conversation is around 60 dB."),
        ("Busy traffic", "City traffic reaches roughly 80–90 dB."),
        ("Jet engine", "A jet taking off is well over 120 dB — painfully loud "
         "and harmful."),
    ], notes="Give a feel for the decibel scale with familiar examples. Sounds "
             "above about 85 dB for long periods can damage hearing.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Louder Drum", "Hitting a drum harder makes a louder sound "
             "because it increases the vibration's:",
             ["Frequency", "Amplitude", "Pitch", "Speed"])
    b.quiz_a(1, "B. Amplitude",
             "A harder strike makes the drum skin swing further from its rest "
             "position — a larger amplitude. More amplitude carries more "
             "energy, so the sound is louder. The pitch is unchanged.")
    b.quiz_q(2, "Time Period", "A vibrating body has a frequency of 50 Hz. Its "
             "time period is:", ["50 s", "1/50 s = 0.02 s", "100 s",
              "5 s"])
    b.quiz_a(2, "B. 1/50 s = 0.02 s",
             "Time period is the time for one vibration and equals 1 ÷ "
             "frequency. With 50 vibrations each second, one vibration takes "
             "1/50 s, which is 0.02 s.")
    b.quiz_q(3, "Same Note, Softer", "Two sounds have the same pitch but one is "
             "much softer. The softer one has a smaller:",
             ["Frequency", "Amplitude", "Wavelength", "Speed"])
    b.quiz_a(3, "B. Amplitude",
             "Same pitch means the same frequency. The difference in loudness "
             "must come from amplitude — the softer sound is made by a smaller "
             "vibration.")
    b.quiz_q(4, "Unit of Loudness", "The loudness of a sound is measured in:",
             ["Hertz", "Decibel", "Metre", "Second"])
    b.quiz_a(4, "B. Decibel",
             "Loudness is measured in decibels (dB). Hertz measures frequency, "
             "not loudness. A whisper is a few decibels; a jet engine is well "
             "over a hundred.")
    b.divider(2, "Part 2", "Pitch, Quality & Noise",
              "What makes sounds high, low and different")
    b.text_image("PITCH", "Frequency Decides Pitch",
                 ["Pitch is how high or low a sound seems.",
                  "A higher frequency gives a higher pitch.",
                  "A thin, tight or short string vibrates faster and sounds "
                  "shrill.",
                  "A woman's voice is usually higher-pitched than a man's."],
                 chars, img_side="right", img_w=6.4, img_h=3.0,
                 panel_title="Faster vibration = higher pitch",
                 caption="High and low pitch waves have the same amplitude but "
                         "different frequency",
                 notes="Pitch → frequency. Higher frequency = higher pitch. "
                       "Thin/short/tight strings vibrate faster and sound "
                       "shriller.")
    b.cards("QUALITY", "Quality (Timbre)", [
        ("What it is", "The characteristic that lets us tell two sources "
         "apart, even at the same pitch and loudness."),
        ("Why it differs", "Each source adds its own mix of extra "
         "frequencies, giving a different wave shape."),
        ("Recognising voices", "Quality lets us know a friend's voice on the "
         "phone without seeing them."),
        ("Instruments", "A flute and a violin playing the same note still "
         "sound clearly different."),
    ], notes="Quality / timbre distinguishes sources at the same pitch and "
             "loudness, because each has a different waveform. Lets us tell "
             "voices and instruments apart.")
    b.cards("NOISE vs MUSIC", "Musical Note and Noise", [
        ("Musical note", "A pleasant sound with a regular, smooth pattern of "
         "vibrations."),
        ("Noise", "An unpleasant sound with an irregular, jumbled pattern."),
        ("Monotone", "A sound of a single unchanging frequency."),
        ("Noise pollution", "Too much loud, unwanted sound that can harm "
         "hearing and health."),
    ], notes="Music = regular waveform (pleasant); noise = irregular "
             "(unpleasant). Monotone = single frequency. Mention noise "
             "pollution.")
    b.bullets("RANGE OF HEARING", "Sounds We Can and Cannot Hear", [
        ("Audible range", "A healthy human ear hears from about 20 Hz to "
         "20,000 Hz."),
        ("Infrasonic", "Sounds below 20 Hz are too low for us — elephants use "
         "them to communicate."),
        ("Ultrasonic", "Sounds above 20,000 Hz are too high for us — dogs and "
         "bats can hear them."),
        ("Uses of ultrasound", "Cleaning, medical scans and sonar all use "
         "ultrasonic sound."),
    ], panel_title="20 Hz to 20,000 Hz",
       notes="Audible range 20–20,000 Hz. Below = infrasonic, above = "
             "ultrasonic. Ultrasound has many practical uses.")
    b.cards("NOISE CONTROL", "Noise Pollution and Its Control", [
        ("What it is", "Unwanted, excessive sound that disturbs and can harm "
         "health."),
        ("Effects", "It causes stress, poor sleep, and can damage hearing over "
         "time."),
        ("At the source", "Quieter machines, silencers on vehicles and bans on "
         "needless horns help."),
        ("Around us", "Trees, sound barriers and thick walls absorb and block "
         "unwanted sound."),
    ], notes="Noise pollution: causes and control. Tackle it at the source and "
             "by absorbing/blocking sound. Plant trees, use barriers.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Amplitude", "decides loudness — bigger swing, louder sound"),
        ("Frequency", "decides pitch — faster vibration, higher pitch"),
        ("Time period", "time for one vibration = 1 / frequency"),
        ("Quality", "tells two sources apart at the same pitch"),
        ("Loudness", "measured in decibels; depends on intensity"),
        ("Music vs noise", "regular pattern vs irregular jumble"),
    ], notes="Rapid recap of the three characteristics — loudness, pitch, "
             "quality — plus music vs noise.")
    b.quiz_intro("Quiz 2", "Final Check — Characteristics of Sound", 5)
    b.quiz_q(1, "Two Flutes", "A flute and a violin play exactly the same note "
             "at the same loudness, yet we can still tell them apart because "
             "they differ in:", ["Pitch", "Loudness", "Quality (timbre)",
              "Speed"])
    b.quiz_a(1, "C. Quality (timbre)",
             "Same note means same pitch; same loudness means same amplitude. "
             "The remaining difference is quality — each instrument produces a "
             "different waveform, so they sound distinct.")
    b.quiz_q(2, "Higher Pitch", "Tightening a guitar string and plucking it "
             "raises the pitch because the string now vibrates with a higher:",
             ["Amplitude", "Frequency", "Wavelength", "Loudness"])
    b.quiz_a(2, "B. Frequency",
             "A tighter string vibrates faster — more vibrations per second, a "
             "higher frequency. Since pitch rises with frequency, the note "
             "sounds higher.")
    b.quiz_q(3, "Shrill Voice", "A child's voice sounds shriller than an "
             "adult's mainly because the child's vocal cords vibrate at a:",
             ["Lower frequency", "Higher frequency", "Larger amplitude",
              "Slower speed"])
    b.quiz_a(3, "B. Higher frequency",
             "Shrillness is high pitch, and pitch rises with frequency. A "
             "child's shorter, thinner vocal cords vibrate faster, giving a "
             "higher frequency and a shriller voice.")
    b.quiz_q(4, "Jumbled Sound", "A sound made of an irregular, jumbled pattern "
             "of vibrations is best described as:", ["A musical note",
              "Noise", "A monotone", "An echo"])
    b.quiz_a(4, "B. Noise",
             "Pleasant musical notes come from regular, repeating vibrations. "
             "An irregular, jumbled pattern is heard as noise, which is "
             "generally unpleasant.")
    b.quiz_q(5, "100 Hz vs 200 Hz", "Two strings sound at 100 Hz and 200 Hz "
             "with equal amplitude. Compared with the 100 Hz string, the "
             "200 Hz string sounds:", ["Louder", "Higher in pitch", "Softer",
              "Exactly the same"])
    b.quiz_a(5, "B. Higher in pitch",
             "Equal amplitude means equal loudness, so the difference is pitch. "
             "The 200 Hz string vibrates twice as fast, so it sounds higher in "
             "pitch than the 100 Hz string.")
    b.closing("The Colours of Sound",
              "Amplitude sets how loud, frequency sets how high, and quality "
              "gives each voice and instrument its own signature.")
    return b


def build():
    for fname, fn in [("G8_S61_Sound_1.pptx", deck1),
                      ("G8_S62_Sound_2.pptx", deck2)]:
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
