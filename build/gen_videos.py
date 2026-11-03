"""Generate the ambient video loops through the Higgsfield API (Kling 4.0, image to video).

Each loop starts from one of the site's stills (content.VIDEOS names it). The still is uploaded to
Higgsfield's file store, animated for 5 seconds at 1080p, then ffmpeg makes it web-ready: 1280 px wide,
H.264, no audio, and played forward then backward so it loops without a jump.

    python build/gen_videos.py               # all missing loops
    python build/gen_videos.py hero-loop     # just these

Raw downloads stay in design/video-originals; web files go to src/assets/video. Existing files are skipped.
"""
import io
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.request

sys.path.insert(0, str(pathlib.Path.home() / ".higgsfield"))
from hf import call  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import VIDEOS  # noqa: E402

from PIL import Image  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "src" / "assets" / "img"
OUT = ROOT / "src" / "assets" / "video"
RAW = ROOT / "design" / "video-originals"
# Kling 4.0 by default (not in the public docs yet; it takes image_url, prompt, duration and resolution).
# LTX-2.5 Fast is the cheaper fallback: python build/gen_videos.py --ltx
KLING = "/kling-video/v4.0/image-to-video"
LTX = "/lightricks/ltx-2.5/image-to-video/fast"
# Kling 2.5 Turbo keeps fine detail (like on-screen UI) steadier: python build/gen_videos.py --k25 phone-loop
K25 = "/kling-video/v2.5-turbo/pro/image-to-video"


def still(name):
    for ext in ("webp", "png", "jpg"):
        if (IMG / f"{name}.{ext}").exists():
            return IMG / f"{name}.{ext}"
    sys.exit(f"No still named {name} in {IMG}")


def upload(path):
    """Upload a still as JPEG and return its public URL."""
    buf = io.BytesIO()
    Image.open(path).convert("RGB").save(buf, "JPEG", quality=92)
    status, text = call("POST", "/files/generate-upload-url", {"content_type": "image/jpeg"})
    if status >= 300:
        sys.exit(f"upload url failed {status}: {text[:300]}")
    up = json.loads(text)
    req = urllib.request.Request(up["upload_url"], data=buf.getvalue(), method="PUT", headers=up.get("upload_headers") or {})
    with urllib.request.urlopen(req, timeout=120) as r:
        if r.status >= 300:
            sys.exit(f"upload failed {r.status}")
    return up["public_url"]


def web_loop(src, dst):
    """Forward then reversed, 1280 px, 24 fps, H.264 without audio, ready to stream."""
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
        "-filter_complex", "[0:v]scale=1280:-2:flags=lanczos,fps=24,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,format=yuv420p[v]",
        "-map", "[v]", "-c:v", "libx264", "-preset", "slow", "-crf", "26", "-movflags", "+faststart", "-an", str(dst),
    ], check=True)


def main(only, ltx=False, k25=False):
    OUT.mkdir(parents=True, exist_ok=True)
    RAW.mkdir(parents=True, exist_ok=True)
    jobs = {}
    for name, (image, prompt) in VIDEOS.items():
        if (only and name not in only) or (OUT / f"{name}.mp4").exists():
            continue
        url = upload(still(image))
        if ltx:
            body = {"prompt": prompt, "image_url": url, "duration": 6, "resolution": "720p", "generate_audio": False,
                    "aspect_ratio": "9:16" if image == "auth-panel" else "16:9", "camera_movement": "dolly_in"}
        elif k25:
            body = {"prompt": prompt, "image_url": url, "duration": 5}
        else:
            body = {"prompt": prompt, "image_url": url, "duration": 5, "resolution": "1080p", "sound": "off"}
        status, text = call("POST", LTX if ltx else K25 if k25 else KLING, body)
        if status >= 300:
            print(f"{name}: submit failed {status}: {text[:300]}", flush=True)
            continue
        jobs[name] = json.loads(text)["request_id"]
        print(f"{name}: submitted {jobs[name]}", flush=True)
    while jobs:
        time.sleep(10)
        for name, rid in list(jobs.items()):
            _, text = call("GET", f"/requests/{rid}/status")
            r = json.loads(text)
            if r.get("status") not in ("completed", "failed", "nsfw", "canceled"):
                continue
            del jobs[name]
            if r["status"] != "completed" or not r.get("video"):
                print(f"{name}: ended {r['status']} {r.get('error') or ''}", flush=True)
                continue
            raw = RAW / f"{name}.mp4"
            urllib.request.urlretrieve(r["video"]["url"], raw)
            web_loop(raw, OUT / f"{name}.mp4")
            print(f"{name}: saved video/{name}.mp4 ({(OUT / f'{name}.mp4').stat().st_size // 1024} KB)", flush=True)


if __name__ == "__main__":
    args = set(sys.argv[1:])
    main(args - {"--ltx", "--k25"}, "--ltx" in args, "--k25" in args)
