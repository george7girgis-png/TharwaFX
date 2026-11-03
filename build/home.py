"""Home page (P01) redesigns layered over the book markup: the platforms phone, the sign-up roadmap,
the deposit methods and the safety cards. Each function finds its section in the built HTML, reads the
copy out of it (so English and Arabic stay in step with the book) and swaps in the new markup."""
import re

import build as B

ICONS = {
    "user": '<path d="M15 19a6 6 0 0 0-12 0M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM19 8v6M22 11h-6"/>',
    "id": '<path d="M3 5h18v14H3zM7 15c.6-1.4 1.7-2 3-2s2.4.6 3 2M10 11a1.8 1.8 0 1 0 0-3.6 1.8 1.8 0 0 0 0 3.6zM15 9h3M15 12h3"/>',
    "wallet": '<path d="M3 7h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7l13-3v3M16 13h2"/>',
    "chart": '<path d="M7 4v16M17 4v16M4 8h6v7H4zM14 7h6v9h-6z"/>',
}
CTA = {"en": "Start with step 1", "ar": "ابدأ بالخطوة الأولى"}
KICK = {"en": ("// Four steps", "// Funding", "// Safety"), "ar": ("أربع خطوات", "التمويل", "الأمان")}


def svg(name, size=22):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def block(s, start):
    """End index of the <div> that opens at start."""
    depth, i = 0, start
    for m in re.compile(r"<div\b|</div>").finditer(s, start):
        depth += 1 if m.group(0) == "<div" else -1
        if depth == 0:
            return m.end()
    raise ValueError("unbalanced div")


def platforms(s, lang):
    """The coded phone becomes the 3D phone render with the real site on its screen, animated by Kling 2.5."""
    a = s.index('<div><div class="phone" style="min-height:520px;width:300px;margin:0 auto">')
    suffix = "-ar" if lang == "ar" else ""
    visual = (f'<div class="phone3d">{B.media("phone-loop" + suffix, "phone-mock" + suffix, "phone3d-media")}'
              '<span class="phone3d-ring" aria-hidden="true"></span></div>')
    s = s[:a] + visual + s[block(s, a):]
    return s.replace('<div class="g2 mt32"><div class="card s row sb">', '<div class="g2 mt32 plat"><div class="card s row sb">', 1)


def roadmap(s, lang):
    m = re.search(r'<section class="sec "><div class="wrap"><h2 class="mb48">([^<]*)</h2><div style="position:relative"><svg.*?</section>', s, re.S)
    steps = re.findall(r'<div class="sn">(\d)</div><h3 class="mt8">(.*?)</h3><p class="sm mut mt8">(.*?)</p>', m.group(0))
    icons = ["user", "id", "wallet", "chart"]
    items = "".join(
        f'<li class="road-step" style="--n:{i}"><div class="road-node">{svg(icons[i])}<span class="mono">0{n}</span></div>'
        f'<div class="road-card"><span class="road-no mono" aria-hidden="true">0{n}</span><h3>{h}</h3><p class="sm mut mt8">{p}</p></div></li>'
        for i, (n, h, p) in enumerate(steps))
    html = (f'<section class="sec road"><div class="road-grid" aria-hidden="true"></div><div class="wrap">'
            f'<span class="mono k">{KICK[lang][0]}</span><h2 class="mt16">{m.group(1)}</h2>'
            f'<div class="road-wrap mt48" data-road><div class="road-rail" aria-hidden="true"><i class="road-fill"></i><i class="road-pulse"></i></div>'
            f'<ol class="road-track">{items}</ol></div>'
            f'<a class="b p lg2 mt48" href="{B.localize("/register", lang)}">{CTA[lang]} <span aria-hidden="true">→</span></a></div></section>')
    return s[:m.start()] + html + s[m.end():]


def deposits_and_safety(s, lang):
    m = re.search(r'<section class="sec t" style="border-top:1px solid #1e1e1e"><div class="wrap row sb wr"><h3>([^<]*)</h3>'
                  r'<div class="row wr">((?:<span class="chip">[^<]*</span>)+)</div></div></section>', s)
    chips = re.findall(r'<span class="chip">([^<]*)</span>', m.group(2))
    run = "".join(f'<span class="pay-chip"><i></i>{c}</span>' for c in chips)
    pay = (f'<section class="pay"><div class="wrap pay-in"><div class="pay-h"><span class="mono k">{KICK[lang][1]}</span><h3 class="mt8">{m.group(1)}</h3></div>'
           f'<div class="pay-mq"><div class="pay-track">{run}<span class="pay-dup" aria-hidden="true">{run}</span></div></div></div></section>')
    s = s[:m.start()] + pay + s[m.end():]

    t = re.compile(r'<section class="sec "><div class="wrap"><h2 class="mb32">([^<]*)</h2><div class="g3">(.*?)</div></div></section>', re.S)
    m = t.search(s, s.index('class="pay"'))
    cards = re.findall(r'<div class="card">(<svg.*?</svg>)<h3 class="mt16">(.*?)</h3><p class="mut sm mt8">(.*?)</p></div>', m.group(2), re.S)
    out = "".join(
        f'<div class="vault-card"><div class="vault-top"><span class="vault-ico">{ico.replace(" stroke=\"#34E834\"", " stroke=\"currentColor\"")}</span>'
        f'<span class="mono xs mut3">0{i + 1}</span></div><h3 class="mt24">{h}</h3><p class="mut sm mt8">{p}</p><i class="vault-scan" aria-hidden="true"></i></div>'
        for i, (ico, h, p) in enumerate(cards))
    safe = (f'<section class="sec vault"><div class="wrap"><span class="mono k">{KICK[lang][2]}</span><h2 class="mt16 mb32">{m.group(1)}</h2>'
            f'<div class="vault-g">{out}</div></div></section>')
    return s[:m.start()] + safe + s[m.end():]


def redesign(s, lang):
    return deposits_and_safety(roadmap(platforms(s, lang), lang), lang)
