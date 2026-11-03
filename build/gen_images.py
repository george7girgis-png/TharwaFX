"""Generate the site imagery through the Higgsfield API.

Uses the local client in ~/.higgsfield (key read from ~/.higgsfield/key, never printed).
Prompts come from build/images.json (written by build.py). Images that already exist in
src/assets/img are skipped, so the script can be re-run after a failure.

    python build/gen_images.py               # all missing images
    python build/gen_images.py home-hero     # just these
"""
import json
import os
import pathlib
import sys
import time
import urllib.request

sys.path.insert(0, str(pathlib.Path.home() / ".higgsfield"))
from hf import call  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import STYLE  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "src" / "assets" / "img"
MODEL = "/higgsfield-ai/soul/standard"
RATIOS = {"21:9": "16:9"}  # wide bands are cropped by CSS


def existing(name):
    return any((IMG / f"{name}.{e}").exists() for e in ("webp", "jpg", "png"))


def submit(name, aspect, prompt):
    body = {"prompt": f"{prompt} {STYLE}", "aspect_ratio": RATIOS.get(aspect, aspect)}
    status, text = call("POST", MODEL, body)
    if status >= 300:
        print(f"{name}: submit failed {status}: {text[:300]}", flush=True)
        return None
    rid = json.loads(text)["request_id"]
    print(f"{name}: submitted {rid}", flush=True)
    return rid


def main(only):
    spec = json.loads((ROOT / "build" / "images.json").read_text(encoding="utf-8"))
    IMG.mkdir(parents=True, exist_ok=True)
    todo = {n: s for n, s in spec.items() if (not only or n in only) and not existing(n)}
    jobs = {}
    for name, s in todo.items():
        rid = submit(name, s["aspect"], s["prompt"])
        if rid:
            jobs[name] = rid
    while jobs:
        time.sleep(6)
        for name, rid in list(jobs.items()):
            _, text = call("GET", f"/requests/{rid}/status")
            r = json.loads(text)
            st = r.get("status")
            if st not in ("completed", "failed", "nsfw", "canceled"):
                continue
            del jobs[name]
            if st != "completed" or not r.get("images"):
                print(f"{name}: ended {st} {r.get('error') or ''}", flush=True)
                continue
            url = r["images"][0]["url"]
            ext = url.split("?")[0].rsplit(".", 1)[-1].lower()
            ext = "jpg" if ext == "jpeg" else ext
            urllib.request.urlretrieve(url, IMG / f"{name}.{ext}")
            print(f"{name}: saved {name}.{ext}", flush=True)


if __name__ == "__main__":
    main(set(sys.argv[1:]))
