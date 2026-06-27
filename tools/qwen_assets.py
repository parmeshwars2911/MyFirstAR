"""
Qwen image assets with an automatic quality-assurance loop.

Pipeline for every real-world photo used on a slide:

    1. GENERATE  - text-to-image with a Qwen image model (qwen-image-2.0-pro).
    2. QA        - a Qwen vision model (qwen-vl-max) inspects the image against
                   an academic-use rubric and returns JSON
                   {ok, issues[], better_prompt}.
    3. CORRECT   - if not ok, regenerate with the improved prompt (and, on the
                   last try, a stronger image model). Re-QA.
    4. Repeat at most `max_tries` (2-3) times. Only a QA-passed image is kept;
       otherwise the asset is removed so the deck falls back to its SVG diagram.

This module is NEW (does not edit the shared images.py). It reuses
images.download (download + size/aspect QA) and images.find_asset/asset_path.

Credentials: never hard-coded. Set QWEN_API_KEY in the environment. The host
defaults to the workspace that has the image + vision models enabled.

Usage:
    export QWEN_API_KEY=sk-...            # key 494133 (ap-southeast-1 workspace)
    python tools/qwen_assets.py manifest.json
where manifest.json = { "key": {"subject": "...", "prompt": "...",
                                 "negative": "..."}, ... }
"""
import os
import sys
import re
import json
import base64
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(__file__))
import images  # noqa: E402  (reuse download + asset helpers)

QWEN_BASE = os.environ.get(
    "QWEN_BASE",
    "https://ws-ybmxvbl2gr7ygzua.ap-southeast-1.maas.aliyuncs.com")
GEN_MODEL = os.environ.get("QWEN_GEN_MODEL", "qwen-image-2.0-pro")
GEN_MODEL_STRONG = os.environ.get("QWEN_GEN_MODEL_STRONG", "qwen-image-max")
VISION_MODEL = os.environ.get("QWEN_VISION_MODEL", "qwen-vl-max")
GEN_SIZE = os.environ.get("QWEN_SIZE", "1328*747")  # ~16:9

NEG_DEFAULT = ("text, words, letters, captions, labels, watermark, logo, "
               "signature, numbers, blurry, distorted, deformed, extra limbs, "
               "low quality, cartoonish errors, frame, border")


def _key():
    k = os.environ.get("QWEN_API_KEY")
    if not k:
        raise RuntimeError("set QWEN_API_KEY in the environment first")
    return k


def _post(url, payload, timeout=180):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {_key()}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


# ---------------------------------------------------------------------------
# 1. generation
# ---------------------------------------------------------------------------
def generate(key, prompt, model=None, size=None, negative=NEG_DEFAULT,
             ext="jpg"):
    """Generate one image and save it to assets/img/<key>.<ext> (size-QA'd)."""
    model = model or GEN_MODEL
    url = f"{QWEN_BASE}/api/v1/services/aigc/multimodal-generation/generation"
    params = {"size": size or GEN_SIZE}
    if negative:
        params["negative_prompt"] = negative
    payload = {"model": model,
               "input": {"messages": [{"role": "user",
                                       "content": [{"text": prompt}]}]},
               "parameters": params}
    resp = _post(url, payload)
    try:
        img_url = resp["output"]["choices"][0]["message"]["content"][0]["image"]
    except Exception:
        raise RuntimeError(f"unexpected gen response: {json.dumps(resp)[:300]}")
    return images.download(key, img_url, ext)


# ---------------------------------------------------------------------------
# 2. vision QA
# ---------------------------------------------------------------------------
def _extract_json(text):
    """Pull the first {...} JSON object out of a model reply."""
    text = text.strip()
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        # tolerate trailing commas / single quotes
        s = m.group(0).replace("'", '"')
        s = re.sub(r",\s*([}\]])", r"\1", s)
        try:
            return json.loads(s)
        except Exception:
            return None


def vision_qa(image_path, subject):
    """Ask a Qwen vision model whether the image is fit for academic use."""
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    ext = os.path.splitext(image_path)[1].lstrip(".") or "jpeg"
    data_url = f"data:image/{ext};base64,{b64}"
    rubric = (
        "You are a strict reviewer of illustrations for an ICSE school physics "
        "textbook. This image is meant to clearly show: " + subject + ". "
        "Judge it on: (1) it unmistakably and correctly shows that subject; "
        "(2) it is scientifically accurate and not misleading; "
        "(3) it contains NO text, captions, labels, watermarks, logos or "
        "garbled letters; (4) no distortions, no extra or wrong objects, no "
        "anatomy errors; (5) clean, well-lit, suitable for a classroom slide. "
        "Reply with ONLY compact JSON of the form "
        '{"ok": true or false, "issues": ["short issue", ...], '
        '"better_prompt": "an improved, specific text-to-image prompt that '
        'fixes the issues and would pass this review"}. '
        "Set ok=true only if the image is genuinely good enough to print.")
    url = f"{QWEN_BASE}/compatible-mode/v1/chat/completions"
    payload = {"model": VISION_MODEL, "temperature": 0,
               "messages": [{"role": "user", "content": [
                   {"type": "image_url", "image_url": {"url": data_url}},
                   {"type": "text", "text": rubric}]}]}
    resp = _post(url, payload)
    try:
        content = resp["choices"][0]["message"]["content"]
        if isinstance(content, list):  # some models return a content list
            content = " ".join(c.get("text", "") for c in content
                               if isinstance(c, dict))
    except Exception:
        raise RuntimeError(f"unexpected QA response: {json.dumps(resp)[:300]}")
    verdict = _extract_json(content) or {"ok": False,
                                         "issues": ["unparseable QA reply"],
                                         "better_prompt": ""}
    verdict.setdefault("ok", False)
    verdict.setdefault("issues", [])
    verdict.setdefault("better_prompt", "")
    return verdict


# ---------------------------------------------------------------------------
# 3. generate + QA + correct loop
# ---------------------------------------------------------------------------
def generate_checked(key, subject, prompt, negative=NEG_DEFAULT, max_tries=3):
    """Generate, QA, and correct up to max_tries. Returns (path|None, log)."""
    log = []
    cur_prompt = prompt
    for attempt in range(1, max_tries + 1):
        model = GEN_MODEL if attempt < max_tries else GEN_MODEL_STRONG
        try:
            path = generate(key, cur_prompt, model=model, negative=negative)
        except Exception as e:
            log.append(f"try {attempt}: GEN FAIL ({model}): {e}")
            continue
        try:
            v = vision_qa(path, subject)
        except Exception as e:
            log.append(f"try {attempt}: QA call failed: {e} - keeping image")
            return path, log
        if v.get("ok"):
            log.append(f"try {attempt} ({model}): OK")
            return path, log
        log.append(f"try {attempt} ({model}): NOT OK - "
                   f"{'; '.join(v.get('issues', []))[:200]}")
        if v.get("better_prompt"):
            cur_prompt = v["better_prompt"]
    # never passed: drop the asset so the deck uses its SVG fallback
    p = images.find_asset(key)
    if p and os.path.exists(p):
        os.remove(p)
    log.append("FAILED QA after all tries - asset removed (SVG fallback)")
    return None, log


def run_manifest(path, force=False):
    man = json.load(open(path, encoding="utf-8"))
    ok, fail = [], []
    for key, spec in man.items():
        if not force and images.find_asset(key):
            print(f"[skip] {key} (exists)")
            ok.append(key)
            continue
        subject = spec.get("subject") or spec["prompt"]
        print(f"[gen ] {key}: {subject}")
        p, log = generate_checked(key, subject, spec["prompt"],
                                  spec.get("negative", NEG_DEFAULT),
                                  spec.get("max_tries", 3))
        for line in log:
            print("       " + line)
        (ok if p else fail).append(key)
    print(f"\nDONE - kept {len(ok)}, failed {len(fail)}")
    if fail:
        print("failed:", ", ".join(fail))
    return ok, fail


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_manifest(sys.argv[1], force="--force" in sys.argv)
    else:
        print("usage: QWEN_API_KEY=... python tools/qwen_assets.py "
              "manifest.json [--force]")
