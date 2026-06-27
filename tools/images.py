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
    "https://ws-qomife91njyip4db.cn-beijing.maas.aliyuncs.com")
QWEN_MODEL = os.environ.get("QWEN_MODEL", "wan2.2-t2i-flash")


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


def qwen_generate(key, prompt, ext="jpg", size="1280*720"):
    """Generate an illustration with the Qwen/DashScope text-to-image model.

    Uses the DashScope async text2image task API. Requires env QWEN_API_KEY.
    """
    api = os.environ.get("QWEN_API_KEY")
    if not api:
        raise RuntimeError("set QWEN_API_KEY in the environment first")
    create = f"{QWEN_BASE}/api/v1/services/aigc/text2image/image-synthesis"
    payload = {"model": QWEN_MODEL,
               "input": {"prompt": prompt},
               "parameters": {"size": size, "n": 1}}
    req = urllib.request.Request(
        create, data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api}",
                 "Content-Type": "application/json",
                 "X-DashScope-Async": "enable"})
    with urllib.request.urlopen(req, timeout=60) as r:
        task = json.loads(r.read())
    tid = task["output"]["task_id"]
    poll = f"{QWEN_BASE}/api/v1/tasks/{tid}"
    for _ in range(40):
        time.sleep(3)
        req = urllib.request.Request(
            poll, headers={"Authorization": f"Bearer {api}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            st = json.loads(r.read())
        status = st["output"]["task_status"]
        if status == "SUCCEEDED":
            img_url = st["output"]["results"][0]["url"]
            return download(key, img_url, ext)
        if status in ("FAILED", "CANCELED", "UNKNOWN"):
            raise RuntimeError(f"qwen task {status}: {st['output']}")
    raise TimeoutError("qwen generation timed out")


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
