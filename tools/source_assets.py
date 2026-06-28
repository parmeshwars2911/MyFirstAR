"""
Source better images for the Grade-10 diagrams, in the order the user asked:
  web (Wikimedia Commons, strictly vision-vetted) -> Qwen (strictly reviewed)
  -> SVG fallback (left to the deck builder).

Only images that PASS the strict diagram review are saved into assets/img/.
Anything that fails leaves no asset, so the deck keeps its accurate SVG.

Run:  QWEN_API_KEY=... python3 tools/source_assets.py
Re-runnable: already-sourced keys are skipped.
"""
import os
import sys
import time
import shutil

sys.path.insert(0, os.path.dirname(__file__))
import images

# concept -> (commons_query, strict_brief, [keys that share this image])
CONCEPTS = [
    ("refraction_boundary",
     "refraction of light at boundary diagram angle of incidence refraction normal",
     "a labelled ray diagram of light refracting at the boundary between two "
     "media, showing the incident ray, refracted ray, the normal and angles "
     "i and r",
     ["g10r1_bend_denser", "g10r1_bend_rarer", "g10r1_snell", "g10r2_bend"]),
    ("glass_slab",
     "refraction through rectangular glass slab lateral displacement diagram",
     "a labelled ray diagram of light passing through a rectangular glass "
     "slab, showing the emergent ray parallel to the incident ray and the "
     "lateral shift",
     ["g10r1_block"]),
    ("prism_dispersion",
     "dispersion of white light through prism spectrum diagram",
     "a labelled diagram of white light passing through a triangular glass "
     "prism and splitting into the spectrum of colours",
     ["g10r2_prism", "g10sp_prism", "g10sp_disp"]),
    ("apparent_depth",
     "real and apparent depth refraction water diagram",
     "a labelled diagram showing why an object under water appears raised "
     "(real depth and apparent depth)",
     ["g10r2_depth"]),
    ("tir",
     "total internal reflection critical angle diagram",
     "a labelled diagram of total internal reflection showing the critical "
     "angle and a ray reflected inside a denser medium",
     ["g10r2_tir"]),
    ("optical_fibre",
     "optical fibre total internal reflection diagram",
     "a labelled diagram of light travelling along an optical fibre by "
     "repeated total internal reflection",
     ["g10r2_fibre"]),
    ("reflecting_prism",
     "total internal reflection prism 45 degrees periscope diagram",
     "a labelled diagram of a 45-45-90 totally reflecting prism turning a "
     "ray of light through 90 degrees",
     ["g10r2_rprism"]),
    ("convex_ray",
     "convex lens ray diagram image formation labelled F 2F",
     "a labelled convex-lens ray diagram with an object beyond 2F forming a "
     "real inverted diminished image, showing F and 2F on the principal axis",
     ["g10l_convex", "g10l_convex2"]),
    ("magnifier_ray",
     "magnifying glass convex lens virtual image ray diagram",
     "a labelled ray diagram of a convex lens used as a magnifying glass, "
     "object within the focal length giving a virtual erect magnified image",
     ["g10l_magnifier", "g10l_magnifier2"]),
    ("concave_ray",
     "concave lens ray diagram virtual diminished image",
     "a labelled concave-lens ray diagram showing a virtual, erect, "
     "diminished image",
     ["g10l_concave"]),
    ("lens_prisms",
     "convex lens as set of prisms diagram",
     "a diagram showing a convex lens behaving like a set of prisms that "
     "converge light to a focus",
     ["g10l_prisms"]),
    ("em_spectrum",
     "electromagnetic spectrum chart radio microwave infrared visible "
     "ultraviolet x-ray gamma",
     "a labelled chart of the electromagnetic spectrum from radio waves to "
     "gamma rays with the visible band marked",
     ["g10sp_em", "g10sp_em2"]),
    ("scattering",
     "scattering of light blue sky red sunset diagram",
     "a labelled diagram explaining why the sky is blue and sunsets are red "
     "by the scattering of sunlight",
     ["g10sp_scatter"]),
    ("long_wave",
     "longitudinal wave compression rarefaction sound diagram",
     "a labelled diagram of a longitudinal sound wave showing compressions "
     "and rarefactions and one wavelength",
     ["g10so_wave"]),
    ("echo",
     "echo reflection of sound cliff diagram",
     "a labelled diagram of an echo: sound travelling to a cliff and "
     "reflecting back to a listener",
     ["g10so_echo"]),
    ("sound_chars",
     "sound waveform amplitude loudness frequency pitch diagram",
     "labelled waveforms comparing loud and soft (amplitude) and high and "
     "low pitch (frequency)",
     ["g10so_chars"]),
    ("resonance",
     "resonance tuning fork sympathetic vibration diagram",
     "a labelled diagram illustrating resonance, for example two tuning forks "
     "on resonance boxes or coupled pendulums",
     ["g10so_reson"]),
    ("ohm_circuit",
     "circuit diagram ohms law ammeter voltmeter resistor rheostat cell",
     "a correct, complete circuit diagram to verify Ohm's law with a cell, "
     "ammeter in series, a resistor, a rheostat and a voltmeter in parallel",
     ["g10ce_circ"]),
    ("vi_graph",
     "voltage current graph ohms law straight line",
     "a labelled V-I graph for Ohm's law: a straight line through the origin",
     ["g10ce_graph", "g10ce_graph2"]),
    ("series_parallel",
     "resistors in series and parallel circuit diagram",
     "labelled circuit diagrams of resistors connected in series and in "
     "parallel",
     ["g10ce_combo"]),
    ("transmission",
     "electric power transmission generation transformer distribution diagram",
     "a labelled block diagram of electric power transmission from the "
     "generating station through step-up and step-down transformers to homes",
     ["g10hc_trans"]),
    ("plug",
     "three pin plug live neutral earth wiring diagram",
     "a labelled diagram of a three-pin plug showing the live, neutral and "
     "earth pins, their wire colours and the fuse",
     ["g10hc_plug1", "g10hc_plug2"]),
    ("field_wire",
     "magnetic field around straight current carrying wire concentric circles",
     "a labelled diagram of the concentric magnetic field lines around a "
     "straight current-carrying wire, with the right-hand rule",
     ["g10em_wire"]),
    ("solenoid",
     "solenoid electromagnet magnetic field lines north south poles diagram",
     "a labelled diagram of the magnetic field of a current-carrying solenoid "
     "(electromagnet) behaving like a bar magnet with N and S poles",
     ["g10em_sol"]),
    ("dc_motor",
     "simple dc electric motor diagram coil magnet commutator",
     "a labelled diagram of a simple DC motor: a coil between magnet poles "
     "with a split-ring commutator and brushes",
     ["g10em_motor"]),
    ("induction",
     "electromagnetic induction magnet coil galvanometer diagram",
     "a labelled diagram of electromagnetic induction: a magnet moved into a "
     "coil connected to a galvanometer which deflects",
     ["g10em_emi"]),
    ("heating_curve",
     "heating curve of water temperature time graph melting boiling",
     "a labelled heating-curve graph of temperature against heat for ice "
     "melting to water and water boiling to steam, with two flat plateaus",
     ["g10cal_curve2", "g10cal_curve3"]),
    ("calorimeter",
     "calorimeter diagram copper vessel thermometer stirrer",
     "a labelled diagram of a calorimeter showing the copper vessel, "
     "stirrer, thermometer and insulating jacket",
     ["g10cal_calo"]),
]


def run():
    done, svg = [], []
    for concept, query, brief, keys in CONCEPTS:
        primary = keys[0]
        if images.find_asset(primary):
            done.append(primary)
        else:
            print(f"\n### {concept}")
            try:
                res = images.best_image(primary, query, brief,
                                        svg_fallback=None, mode="diagram")
            except Exception as e:
                print(f"  error: {e}")
                res = None
            if res and images.find_asset(primary):
                done.append(primary)
            else:
                svg.append(primary)
            time.sleep(4)  # be gentle with rate limits
        # copy the sourced image (if any) to the alias keys
        src = images.find_asset(primary)
        if src:
            for k in keys[1:]:
                if not images.find_asset(k):
                    ext = os.path.splitext(src)[1]
                    shutil.copy(src, images.asset_path(k, ext.lstrip(".")))
    print(f"\nSOURCED (web/qwen): {len(done)} -> {done}")
    print(f"KEPT AS SVG: {len(svg)} -> {svg}")


if __name__ == "__main__":
    run()
