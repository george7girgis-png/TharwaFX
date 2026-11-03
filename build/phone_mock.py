"""Make the 3D phone mockup that shows the real site on its screen.

The phone itself is a Higgsfield Soul render with a flat magenta screen (design/img-originals/phone-mock-b.png).
This script screenshots the live home page at phone size with headless Edge (cookie banner hidden), warps the
screenshot onto the magenta screen with a perspective fit, adds a faint glass sheen and saves the result as
src/assets/img/phone-mock.webp (English) and phone-mock-ar.webp (Arabic). The site must be served on :8080.

    python build/phone_mock.py
"""
import pathlib
import subprocess
import tempfile

import numpy as np
from PIL import Image, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
PHONE = ROOT / "design" / "img-originals" / "phone-mock-b.png"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
SHOT_PAGE = """<!doctype html><html><body style="margin:0;background:#000"><iframe id="f" src="/{lang}/" style="border:0;width:390px;height:844px;display:block"></iframe>
<script>document.getElementById("f").onload=function(){{var c=this.contentDocument.getElementById("cookie");if(c)c.hidden=true;}};</script></body></html>"""


def screenshot(lang, out):
    """390x844 at 3x, through an iframe so the viewport is exactly phone width."""
    helper = ROOT / "site" / "_shot.html"
    helper.write_text(SHOT_PAGE.format(lang=lang), encoding="utf-8")
    raw = pathlib.Path(tempfile.gettempdir()) / f"tfx-shot-{lang}.png"
    try:
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=3",
                        "--window-size=600,844", "--virtual-time-budget=6000", f"--screenshot={raw}",
                        "http://localhost:8080/_shot.html"], check=True, capture_output=True)
    finally:
        helper.unlink(missing_ok=True)
    Image.open(raw).crop((0, 0, 1170, 2532)).save(out)


def coeffs(dst, src):
    a, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        a += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        b += [u, v]
    return tuple(np.linalg.solve(np.array(a, float), np.array(b, float)))


def composite(shot_path, out):
    ph = Image.open(PHONE).convert("RGB")
    px = np.asarray(ph).astype(float)
    r, g, b = px[..., 0], px[..., 1], px[..., 2]
    mag = (r > 150) & (b > 90) & (g < 110) & (r - g > 90)
    ys, _ = np.nonzero(mag)
    top, bot = ys.min(), ys.max()

    # Fit the four screen edges as lines (away from the rounded corners), then intersect them.
    y1, y2 = top + 120, bot - 120
    l1, r1 = np.nonzero(mag[y1])[0][[0, -1]]
    l2, r2 = np.nonzero(mag[y2])[0][[0, -1]]
    side = lambda y, p, q: p + (q - p) * (y - y1) / (y2 - y1)
    cx1, cx2 = int(side((top + bot) / 2, l1, l2)) + 80, int(side((top + bot) / 2, r1, r2)) - 80
    t1, b1 = np.nonzero(mag[:, cx1])[0][[0, -1]]
    t2, b2 = np.nonzero(mag[:, cx2])[0][[0, -1]]
    edge = lambda x, p, q: p + (q - p) * (x - cx1) / (cx2 - cx1)

    def corner(ty, tb, left):
        y = edge(l1 if left else r1, ty, tb)
        x = side(y, l1, l2) if left else side(y, r1, r2)
        return x, edge(x, ty, tb)

    tl, tr = corner(t1, t2, True), corner(t1, t2, False)
    bl, br = corner(b1, b2, True), corner(b1, b2, False)
    pad = 3
    dst = [(tl[0] - pad, tl[1] - pad), (tr[0] + pad, tr[1] - pad), (br[0] + pad, br[1] + pad), (bl[0] - pad, bl[1] + pad)]
    shot = Image.open(shot_path).convert("RGB")
    sw, sh = shot.size
    warped = shot.transform(ph.size, Image.PERSPECTIVE, coeffs(dst, [(0, 0), (sw, 0), (sw, sh), (0, sh)]), Image.BICUBIC)

    # Alpha from how magenta each pixel is, grown a little to swallow the pink fringe.
    m = np.clip(((r - g) - 40) / 90, 0, 1) * np.clip((b - 40) / 80, 0, 1)
    alpha = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
    img = ph.copy()
    img.paste(warped, (0, 0), alpha)

    yy, xx = np.mgrid[0:ph.size[1], 0:ph.size[0]]
    sheen = np.clip(1 - np.abs((xx - tl[0]) * 0.9 - (yy - tl[1]) * 0.45 - 120) / 140, 0, 1) * 18
    sheen = Image.composite(Image.fromarray(sheen.astype("uint8")), Image.new("L", ph.size, 0), alpha)
    img = Image.composite(Image.new("RGB", ph.size, (255, 255, 255)), img, sheen)
    img.save(out.with_suffix(".png").as_posix().replace("/src/assets/img/", "/design/img-originals/"))
    img.save(out, "WEBP", quality=86)


if __name__ == "__main__":
    for lang, name in (("en", "phone-mock"), ("ar", "phone-mock-ar")):
        shot = pathlib.Path(tempfile.gettempdir()) / f"tfx-phone-{lang}.png"
        screenshot(lang, shot)
        composite(shot, ROOT / "src" / "assets" / "img" / f"{name}.webp")
        print(f"saved img/{name}.webp")
