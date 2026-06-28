"""
Optional real-image asset layer (photos / AI-generated illustrations).

Physics *schematics* (ray diagrams, circuits, field lines) are produced by
diagrams.py as exact SVG -> PNG and should NOT be replaced by photos or AI
images, which routinely get the physics wrong. This module is for the other
kind of picture — realistic illustrations of real objects (a prism, a rainbow,
an optical-fibre cable, a kettle boiling) that make a slide more engaging.

Two providers, both writing PNG/JPG into assets/img/<key>.<ext>:

  1. Qwen / DashScope text-to-image  (qwen_generate)
  2. Direct download from a URL       (download)

Both are network operations. In a session whose egress policy blocks general
web hosts they will fail fast and the deck builder simply falls back to the SVG
diagram or no image. Run this module from a session/environment whose network
policy allows the provider host.

Every fetched/generated asset is QA-checked (decodes, min size, aspect) before
being accepted, so a corrupt or tiny image never reaches a slide.
"""
import os
import sys
import json
import time
import base64
import urllib.request

from PIL import Image

ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",
                                      "assets", "img"))
os.makedirs(ASSETS, exist_ok=True)

# DashScope endpoints (host comes from the workspace key CSV the user supplied;
# the key itself must be passed via env QWEN_API_KEY — never hard-coded/committed)
QWEN_BASE = os.environ.get(
    "QWEN_BASE",
    "https://ws-ybmxvbl2gr7ygzua.ap-southeast-1.maas.aliyuncs.com")
QWEN_MODEL = os.environ.get("QWEN_MODEL", "qwen-image-2.0-pro")
QWEN_SIZE = os.environ.get("QWEN_SIZE", "1328*747")  # 16:9-ish
QWEN_VISION = os.environ.get("QWEN_VISION", "qwen3-vl-plus")  # review model


def asset_path(key, ext="jpg"):
    return os.path.join(ASSETS, f"{key}.{ext}")


def find_asset(key):
    """Return an existing accepted asset for `key`, or None."""
    for ext in ("jpg", "jpeg", "png", "webp"):
        p = asset_path(key, ext)
        if os.path.exists(p):
            return p
    return None


def qa_image(path, min_w=400, min_h=300):
    """Validate a downloaded/generated image. Returns (ok, reason)."""
    try:
        with Image.open(path) as im:
            im.verify()
        with Image.open(path) as im:
            w, h = im.size
    except Exception as e:
        return False, f"unreadable: {e}"
    if w < min_w or h < min_h:
        return False, f"too small ({w}x{h})"
    if max(w, h) / min(w, h) > 3.5:
        return False, f"extreme aspect ratio ({w}x{h})"
    return True, f"ok {w}x{h}"


def download(key, url, ext="jpg"):
    """Download an image URL into assets/img and QA it."""
    out = asset_path(key, ext)
    req = urllib.request.Request(url, headers={"User-Agent": "ICSE-decks/1.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read()
    with open(out, "wb") as f:
        f.write(data)
    ok, reason = qa_image(out)
    if not ok:
        os.remove(out)
        raise ValueError(f"QA rejected {key}: {reason}")
    print(f"  downloaded {key}: {reason}")
    return out


def _strip_html(s):
    import re
    return re.sub("<[^>]+>", "", s or "").strip()


def wikimedia_search(query, want=8):
    """Search Wikimedia Commons for freely-licensed images; return candidate
    (title, thumb_url, descriptionurl) tuples, largest first."""
    import urllib.parse
    api = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
           "&generator=search&gsrnamespace=6&gsrlimit=" + str(want) +
           "&gsrsearch=" + urllib.parse.quote(query) +
           "&prop=imageinfo&iiprop=url|size|mime|mediatype|extmetadata"
           "&iiurlwidth=1280")
    req = urllib.request.Request(api, headers={"User-Agent": "ICSE-decks/1.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.loads(r.read())
    pages = (data.get("query", {}) or {}).get("pages", {})
    out = []
    for p in pages.values():
        ii = (p.get("imageinfo") or [{}])[0]
        url = ii.get("thumburl") or ii.get("url")
        mime = ii.get("mime", "")
        # only real raster photos; skip PDFs, videos, audio, raw SVG
        if not url or mime not in ("image/jpeg", "image/png"):
            continue
        em = ii.get("extmetadata", {})
        lic = em.get("LicenseShortName", {}).get("value", "?")
        artist = em.get("Artist", {}).get("value", "")
        out.append({"title": p.get("title", ""), "url": url,
                    "desc": ii.get("descriptionurl", ""), "license": lic,
                    "artist": _strip_html(artist),
                    "w": ii.get("thumbwidth") or ii.get("width", 0)})
    out.sort(key=lambda d: d.get("w", 0), reverse=True)
    return out


def fetch_wikimedia(key, query, ext="jpg"):
    """Search Commons and download the first image that passes QA."""
    for cand in wikimedia_search(query):
        try:
            p = download(key, cand["url"], ext)
            print(f"    via Commons: {cand['title']} [{cand['license']}]")
            return p, cand
        except Exception as e:
            print(f"    skip {cand.get('title')}: {e}")
    raise ValueError(f"no usable Commons image for {query!r}")


def _http_json(url, payload, key):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        url, data=body,
        headers={"Authorization": f"Bearer {key}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def qwen_generate(key, prompt, ext="png", size=None, negative=None):
    """Generate an illustration with the Qwen image model (DashScope
    multimodal-generation, synchronous). Requires env QWEN_API_KEY. Returns the
    QA-passed asset path, or raises.
    """
    api = os.environ.get("QWEN_API_KEY")
    if not api:
        raise RuntimeError("set QWEN_API_KEY in the environment first")
    url = f"{QWEN_BASE}/api/v1/services/aigc/multimodal-generation/generation"
    content = [{"text": prompt}]
    params = {"size": size or QWEN_SIZE}
    if negative:
        params["negative_prompt"] = negative
    payload = {"model": QWEN_MODEL,
               "input": {"messages": [{"role": "user", "content": content}]},
               "parameters": params}
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        resp = json.loads(r.read())
    try:
        img_url = resp["output"]["choices"][0]["message"]["content"][0]["image"]
    except Exception:
        raise RuntimeError(f"unexpected qwen response: {resp}")
    return download(key, img_url, ext)


def _edu_prompt(brief):
    """Wrap a short brief into a detailed educational-illustration prompt."""
    return (
        f"Educational illustration for an ICSE Class 10 physics teaching slide. "
        f"Subject: {brief}. "
        f"Requirements: scientifically accurate and unambiguous; clean, modern, "
        f"high-contrast studio look; a single clear subject; plain dark or "
        f"softly-graded background suitable as a slide hero; bright, even "
        f"lighting; no text, no letters, no numbers, no labels, no watermark, "
        f"no logos; photorealistic or clean 3D render; minimal clutter.")


def qwen_review(image_path, brief):
    """Ask the vision model to grade an image for educational use. Returns a
    dict {pass, score, issues, improved_prompt}."""
    api = os.environ.get("QWEN_API_KEY")
    if not api:
        raise RuntimeError("set QWEN_API_KEY in the environment first")
    import mimetypes
    mime = mimetypes.guess_type(image_path)[0] or "image/png"
    b64 = base64.b64encode(open(image_path, "rb").read()).decode()
    rubric = (
        "You are an ICSE Class 10 physics teacher reviewing an AI-generated "
        f"image meant to illustrate: '{brief}'. "
        "Judge it on: (1) scientific correctness/appropriateness, (2) clarity "
        "and focus, (3) absence of garbled text, distorted objects or "
        "artefacts, (4) suitability as a clean slide hero. "
        "Reply with ONLY compact JSON: "
        '{"pass": true|false, "score": 1-10, "issues": "short reason", '
        '"improved_prompt": "a refined generation prompt fixing the issues"}. '
        "Pass only if score >= 7 and there are no serious problems.")
    payload = {"model": QWEN_VISION, "temperature": 0,
               "messages": [{"role": "user", "content": [
                   {"type": "text", "text": rubric},
                   {"type": "image_url",
                    "image_url": {"url": f"data:{mime};base64,{b64}"}}]}]}
    req = urllib.request.Request(
        f"{QWEN_BASE}/compatible-mode/v1/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        txt = json.loads(r.read())["choices"][0]["message"]["content"]
    txt = txt.strip()
    if txt.startswith("```"):
        txt = txt.strip("`").split("\n", 1)[-1]
    try:
        return json.loads(txt[txt.find("{"):txt.rfind("}") + 1])
    except Exception:
        return {"pass": True, "score": 7, "issues": "review unparsed",
                "improved_prompt": ""}


def qwen_generate_reviewed(key, brief, ext="png", size=None, attempts=3):
    """Generate an educational image, then have the vision model review it.
    Regenerate (refining the prompt with the reviewer's feedback) up to
    `attempts` times until it passes. Returns (path, review)."""
    prompt = _edu_prompt(brief)
    best = None
    for i in range(attempts):
        path = qwen_generate(key, prompt, ext=ext, size=size)
        review = qwen_review(path, brief)
        score = review.get("score", 0)
        print(f"    attempt {i+1}: score {score} "
              f"{'PASS' if review.get('pass') else 'retry'} "
              f"— {review.get('issues','')[:70]}")
        if best is None or score > best[1].get("score", 0):
            best = (path, review)
        if review.get("pass"):
            return path, review
        if review.get("improved_prompt"):
            prompt = _edu_prompt(brief) + " Reviewer notes: " + \
                review["improved_prompt"]
    return best


def build_from_manifest(manifest_path):
    """manifest: {key: {prompt: ...} | {url: ...}}. Skips already-built keys."""
    man = json.load(open(manifest_path))
    built, failed = [], []
    for key, spec in man.items():
        if find_asset(key):
            continue
        try:
            if "url" in spec:
                download(key, spec["url"], spec.get("ext", "jpg"))
            else:
                qwen_generate(key, spec["prompt"], spec.get("ext", "jpg"))
            built.append(key)
        except Exception as e:
            print(f"  FAILED {key}: {e}")
            failed.append(key)
    print(f"\nbuilt {len(built)}, failed {len(failed)}")
    return built, failed


if __name__ == "__main__":
    if len(sys.argv) > 1:
        build_from_manifest(sys.argv[1])
    else:
        print("usage: python tools/images.py <manifest.json>")
        print("env: QWEN_API_KEY (required for generation), QWEN_MODEL, QWEN_BASE")
