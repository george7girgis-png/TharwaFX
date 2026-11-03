"""Copy the built site for hosting under a sub-path, such as GitHub Pages' /TharwaFX/.

The site links everything from the domain root (/assets/..., /en/...), which only works when it is
served at the root of a domain. This copies site/ to an output folder and puts the prefix in front
of every root link in the HTML, CSS, JavaScript and JSON, so the copy works under the sub-path.

    python build/pages.py /TharwaFX _pages
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

# A root link: "/" followed by a path character, never "//" (protocol-relative) or a bare "/".
PATH = r"/(?=[A-Za-z0-9_.-])"


def rewrite(text, kind, prefix):
    if kind == ".html":
        text = re.sub(r'((?:href|src|poster|action|data-href)=")' + PATH, r"\1" + prefix + "/", text)
        text = re.sub(r"(url=)" + PATH, r"\1" + prefix + "/", text)
        text = re.sub(r"(url\((?:&quot;|[\"'])?)" + PATH, r"\1" + prefix + "/", text)
    elif kind == ".css":
        text = re.sub(r"(url\([\"']?)" + PATH, r"\1" + prefix + "/", text)
    elif kind in (".js", ".json"):
        # Path strings start with /en, /ar or /assets; regex literals like "/g" are left alone.
        text = re.sub(r"([\"'`])/(?=(?:en|ar|assets)(?:[/\"'`]))", r"\1" + prefix + "/", text)
    return text


def main(prefix, out):
    prefix = "/" + prefix.strip("/")
    out = ROOT / out
    shutil.rmtree(out, ignore_errors=True)
    shutil.copytree(SITE, out)
    for f in out.rglob("*"):
        if f.suffix in (".html", ".css", ".js", ".json"):
            f.write_text(rewrite(f.read_text(encoding="utf-8"), f.suffix, prefix), encoding="utf-8")
    (out / ".nojekyll").write_text("")
    print(f"site copied to {out.name}/ for {prefix}/")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "_pages")
