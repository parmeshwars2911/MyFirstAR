"""
webimg — fetch real reference photographs/diagrams from openly-licensed
sources for the teaching decks.

Purpose: for "very general" concept visuals (e.g. dispersion of light, a
nebula, a solar eclipse) a hand-drawn vector ray diagram is easy to get
physically wrong, so we drop in a real reference image instead. These are
pulled from open/CC/public-domain providers so the graphic designer has an
accurate reference to recreate from, with the licence and source recorded
next to every file.

Sources searched:
  * Openverse   (api.openverse.org) — aggregates ~800M CC / public-domain
                 images from Flickr, museums, Rawpixel, science archives, …
  * NASA images (images-api.nasa.gov) — public-domain astronomy imagery.

Usage:
    # download up to 6 candidates for a query into build/web/<slug>/
    python3 tools/webimg.py candidates "dispersion of light prism" dispersion
    python3 tools/webimg.py candidates "orion nebula" nebula --nasa

    # after picking, promote one candidate to the name the deck loads
    python3 tools/webimg.py pick dispersion 02 dispersion_prism

Each downloaded file gets a sibling <file>.txt with title / creator / licence /
source URL for attribution and for the designer.
"""
import os
import re
import sys
import json
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WEB = os.path.join(ROOT, "build", "web")
UA = "Mozilla/5.0 (teaching-deck reference fetch; contact via repo)"


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())


def _download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def _slugdir(slug):
    d = os.path.join(WEB, slug)
    os.makedirs(d, exist_ok=True)
    return d


def _openverse(query, n):
    q = urllib.parse.quote(query)
    url = (f"https://api.openverse.org/v1/images/?q={q}"
           f"&license_type=all-cc,commercial&page_size={n}&mature=false")
    try:
        data = _get(url)
    except Exception as e:  # noqa: BLE001
        print("  openverse error:", e)
        return []
    out = []
    for r in data.get("results", []):
        out.append({
            "url": r.get("url"),
            "title": r.get("title") or "",
            "creator": r.get("creator") or "",
            "license": f"{r.get('license', '')} {r.get('license_version', '')}"
                       .strip(),
            "source": r.get("foreign_landing_url") or r.get("url"),
            "provider": r.get("source") or "openverse",
        })
    return out


def _nasa(query, n):
    q = urllib.parse.quote(query)
    url = f"https://images-api.nasa.gov/search?q={q}&media_type=image"
    try:
        data = _get(url)
    except Exception as e:  # noqa: BLE001
        print("  nasa error:", e)
        return []
    out = []
    for item in data.get("collection", {}).get("items", [])[:n]:
        links = item.get("links", [])
        dat = (item.get("data") or [{}])[0]
        if not links:
            continue
        out.append({
            "url": links[0].get("href"),
            "title": dat.get("title") or "",
            "creator": dat.get("photographer") or dat.get("center") or "NASA",
            "license": "Public Domain (NASA)",
            "source": dat.get("nasa_id", ""),
            "provider": "nasa",
        })
    return out


def candidates(query, slug, use_nasa=False, n=6):
    d = _slugdir(slug)
    results = _nasa(query, n) if use_nasa else _openverse(query, n)
    if not results:
        print("no results")
        return
    print(f"{len(results)} candidates for '{query}' -> {d}")
    for i, r in enumerate(results):
        if not r["url"]:
            continue
        ext = os.path.splitext(urllib.parse.urlparse(r["url"]).path)[1]
        ext = ext if ext.lower() in (".jpg", ".jpeg", ".png", ".gif",
                                     ".webp") else ".jpg"
        base = f"{i:02d}"
        dest = os.path.join(d, base + ext)
        try:
            sz = _download(r["url"], dest)
        except Exception as e:  # noqa: BLE001
            print(f"  [{base}] download failed: {e}")
            continue
        with open(os.path.join(d, base + ".txt"), "w") as f:
            f.write(f"title:   {r['title']}\ncreator: {r['creator']}\n"
                    f"license: {r['license']}\nprovider:{r['provider']}\n"
                    f"source:  {r['source']}\nurl:     {r['url']}\n")
        print(f"  [{base}] {sz//1024} KB  {r['license']:24.24}  {r['title'][:48]}")


def pick(slug, cand, outname):
    """Copy build/web/<slug>/<cand>.* to build/web/<outname>.png for the deck."""
    d = _slugdir(slug)
    src = None
    for fn in os.listdir(d):
        if fn.startswith(cand + ".") and not fn.endswith(".txt"):
            src = os.path.join(d, fn)
            break
    if not src:
        sys.exit(f"candidate {cand} not found in {d}")
    from PIL import Image
    im = Image.open(src).convert("RGB")
    dest = os.path.join(WEB, outname + ".png")
    im.save(dest)
    # carry the attribution across
    txt = os.path.join(d, cand + ".txt")
    if os.path.exists(txt):
        with open(txt) as f:
            meta = f.read()
        with open(os.path.join(WEB, outname + ".txt"), "w") as f:
            f.write(meta)
    print(f"picked {src} -> {dest}")


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd = argv[0]
    if cmd == "candidates":
        query, slug = argv[1], argv[2]
        use_nasa = "--nasa" in argv[3:]
        candidates(query, slug, use_nasa=use_nasa)
    elif cmd == "pick":
        pick(argv[1], argv[2], argv[3])
    else:
        sys.exit(f"unknown command {cmd}")


if __name__ == "__main__":
    main(sys.argv[1:])
