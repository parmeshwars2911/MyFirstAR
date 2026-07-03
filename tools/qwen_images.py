"""
Qwen-Image generation pipeline for the ICSE Class 9 "Pressure in Fluids"
decks.

This is a ready-to-run helper. In THIS Claude-on-web session the environment's
network egress policy blocks every Alibaba/DashScope host, so the images cannot
be generated here. Run this on a machine/environment whose network allows
`dashscope-intl.aliyuncs.com` (or your workspace `*.maas.aliyuncs.com` host).

Setup (International / Singapore workspace keys):
    export DASHSCOPE_API_KEY="sk-ws-..."
    # Optional: point at your workspace host instead of the public endpoint
    export DASHSCOPE_BASE="https://ws-xxxx.ap-southeast-1.maas.aliyuncs.com/api/v1"
    python3 tools/qwen_images.py            # generates all figures
    python3 tools/qwen_images.py fig_4_1    # generate a single figure

Output PNGs are written to  build/qwen/<name>.png . The deck build
(deck_icse9_pressure_pdf.py) loads exactly those paths, so once the images
exist you only need to re-run the deck build to embed them.

Uses the DashScope asynchronous text-to-image (image-synthesis) API with the
`qwen-image` model.
"""
import os
import sys
import time
import json
import urllib.request
import urllib.error

BASE = os.environ.get(
    "DASHSCOPE_BASE",
    "https://dashscope-intl.aliyuncs.com/api/v1",
).rstrip("/")
KEY = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("QWEN_API_KEY")
MODEL = os.environ.get("QWEN_IMAGE_MODEL", "qwen-image")
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "build",
                                   "qwen"))

# A house style suffix appended to every prompt so the whole set looks like one
# consistent textbook figure catalog.
STYLE = (
    " Clean flat vector science-textbook illustration, plain white background, "
    "crisp thin black outlines, clear printed labels with leader lines, "
    "muted educational colour palette (teal, slate, soft red, sand), "
    "no photorealism, no clutter, high legibility, 2D schematic diagram."
)

# One tuned prompt per figure in the chapter. Keys match the asset names used
# by deck_icse9_pressure_pdf.py.
PROMPTS = {
    "fig_4_1": (
        "A physics diagram comparing thrust and pressure: the SAME rectangular "
        "brick shown twice on the ground. Left: brick standing on its smallest "
        "face (upright) so it sinks slightly, labelled 'small area = large "
        "pressure'. Right: the same brick lying flat on its largest face, "
        "labelled 'large area = small pressure'. Both labelled 'Thrust = "
        "weight of brick', downward arrows for weight."
    ),
    "fig_4_2": (
        "A tall water container with three small holes stacked vertically in "
        "its side wall. Water jets spurt out horizontally from each hole; the "
        "lowest hole's jet travels the farthest, the top hole's the shortest, "
        "showing pressure increases with depth. Label 'depth increases -> "
        "pressure increases'."
    ),
    "fig_4_3": (
        "A cross-section of a liquid container showing a horizontal circular "
        "surface PQ of area A at depth h below the free surface XY. A shaded "
        "vertical liquid column PQRS of height h stands above PQ. Labels: h "
        "(depth), A (area), free surface XY, column PQRS. Formula caption "
        "'P = h rho g'."
    ),
    "fig_4_4": (
        "Side-view cross-section of a concrete dam holding back water on its "
        "left. The dam wall is thin at the top and grows much thicker toward "
        "the base. Horizontal red arrows in the water, short near the top and "
        "long near the bottom, show pressure increasing with depth. Labels "
        "'WATER', 'WALL OF DAM', 'thickness increases downward'."
    ),
    "fig_4_5": (
        "A glass flask with several narrow open tubes rising from its top and "
        "sides, fitted with a piston at the mouth. Pushing the piston down "
        "makes water jets rise to the SAME height from every tube, "
        "demonstrating Pascal's law. Labels 'PUSH', 'piston', 'jets reach "
        "same height', 'water'."
    ),
    "fig_4_6": (
        "Principle of a hydraulic machine: two connected cylinders joined by a "
        "horizontal tube filled with liquid. A small piston A (area A1) on the "
        "left with a small downward force F1; a large piston B (area A2) on "
        "the right with a large upward force F2. Labels F1, A1, F2, A2, and "
        "'F2/F1 = A2/A1'."
    ),
    "fig_4_7": (
        "A hydraulic (Bramah) press: a small pump plunger A in a narrow "
        "cylinder P operated by a lever handle, connected by a pipe to a large "
        "ram piston B in a wide cylinder Q that presses a bale of cotton "
        "against a fixed top plate. A release valve and a water reservoir with "
        "valves V1 and V2. Labels: lever, pump plunger A, ram B, cylinder P, "
        "cylinder Q, bale of cotton, valves."
    ),
    "fig_4_8": (
        "A hydraulic jack lifting a car: a narrow cylinder P with piston A "
        "operated by a lever handle, connected through a tube with valve V to "
        "a wide cylinder Q with piston B carrying a platform on which a car "
        "sits. Liquid fills both cylinders. Labels: handle H, effort, fulcrum, "
        "piston A, piston B, valve V, tube R, car, platform."
    ),
    "fig_4_9": (
        "A hydraulic brake schematic of one car wheel: a master cylinder P "
        "with piston A pushed by a foot pedal, a fluid-filled pipe line R "
        "leading to a wheel cylinder Q with two pistons B1 and B2 that push "
        "brake shoes outward against the circular rim of the wheel, with a "
        "return spring. Labels: foot pedal, master cylinder P, piston A, pipe "
        "line R, wheel cylinder Q, pistons B1 B2, brake shoes, spring, rim."
    ),
    "hero1": (
        "A friendly conceptual cover illustration for a lesson on pressure in "
        "fluids: a hand pressing a sharp pin into a board beside a deep tank "
        "of blue water with a diver, conveying 'force over area' and 'pressure "
        "grows with depth'."
    ),
    "hero2": (
        "A friendly conceptual cover illustration for a lesson on Pascal's law "
        "and hydraulics: a small hand pushing a small piston that lifts a "
        "heavy car on a large piston through connected liquid-filled "
        "cylinders, conveying 'a small force lifts a big load'."
    ),
}


def _post(path, payload, extra_headers=None):
    url = f"{BASE}{path}"
    data = json.dumps(payload).encode()
    headers = {"Authorization": f"Bearer {KEY}",
               "Content-Type": "application/json"}
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def _get(path):
    url = f"{BASE}{path}"
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {KEY}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def generate(name, prompt, size="1328*1328"):
    """Submit one async text-to-image task and poll until the PNG is saved."""
    full = prompt + STYLE
    submit = _post(
        "/services/aigc/text2image/image-synthesis",
        {"model": MODEL,
         "input": {"prompt": full},
         "parameters": {"size": size, "n": 1, "prompt_extend": True}},
        extra_headers={"X-DashScope-Async": "enable"})
    task_id = submit["output"]["task_id"]
    print(f"  [{name}] task {task_id} submitted; polling…")
    for _ in range(60):
        time.sleep(3)
        st = _get(f"/tasks/{task_id}")
        status = st["output"]["task_status"]
        if status == "SUCCEEDED":
            img_url = st["output"]["results"][0]["url"]
            _download(name, img_url)
            return True
        if status in ("FAILED", "CANCELED", "UNKNOWN"):
            print(f"  [{name}] FAILED: {json.dumps(st['output'])[:300]}")
            return False
    print(f"  [{name}] timed out")
    return False


def _download(name, url):
    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, f"{name}.png")
    with urllib.request.urlopen(url, timeout=120) as r:
        with open(dest, "wb") as f:
            f.write(r.read())
    print(f"  [{name}] saved -> {dest}")


def main(argv):
    if not KEY:
        sys.exit("Set DASHSCOPE_API_KEY (and optionally DASHSCOPE_BASE) first. "
                 "See the module docstring.")
    wanted = argv or list(PROMPTS)
    ok = 0
    for name in wanted:
        if name not in PROMPTS:
            print(f"  unknown figure '{name}' — skipping")
            continue
        print(f"Generating {name}…")
        try:
            if generate(name, PROMPTS[name]):
                ok += 1
        except urllib.error.HTTPError as e:
            print(f"  [{name}] HTTP {e.code}: {e.read().decode()[:300]}")
        except Exception as e:  # noqa: BLE001
            print(f"  [{name}] error: {e}")
    print(f"\nDone: {ok}/{len(wanted)} figures generated into {OUT}")


if __name__ == "__main__":
    main(sys.argv[1:])
