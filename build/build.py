"""Build the TharwaFx public website from the UI/UX book.

Each public screen in design/TharwaFx_Website_UI_UX_Book.html is lifted into a real
page: the book's mock shell is replaced by a working header, mega menu and footer,
fake controls become real links, buttons and inputs, and a few pages the book only
templates (other markets, instruments, Standard account) are generated from it.

    python build/build.py        -> writes ./site
"""
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (ACTIONS, AR_PAGES, BOOK_PAGES, CALC, CALC_OVERRIDES, CLIENT, CONTEXT_LABELS, FAQ,
                     GLOSSARY, IMAGES, INSTR, LINKS, MARKET_NAMES, MARKETS, MEGA)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "design", "TharwaFx_Website_UI_UX_Book.html")
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "site")

book = open(BOOK, encoding="utf-8").read()
# Cache-busting stamp for CSS and JS, from the asset sources.
VERSION = format(int(max(os.path.getmtime(os.path.join(SRC, "assets", f)) for f in ("site.css", "site.js"))), "x")


# ---------------------------------------------------------------- helpers

def div_end(s, start):
    """Index just past the </div> that closes the <div ...> opening at start."""
    depth = 0
    for m in re.finditer(r"<div\b|</div>", s[start:]):
        depth += 1 if m.group(0) == "<div" else -1
        if depth == 0:
            return start + m.end()
    raise ValueError("unbalanced div")


def cut_div(s, marker):
    i = s.find(marker)
    if i < 0:
        return s
    return s[:i] + s[div_end(s, i):]


def text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def localize(path, lang):
    """'/accounts' -> '/en/accounts/'; keeps query and hash."""
    if path.startswith("http") or path.startswith("#"):
        return path
    m = re.match(r"([^?#]*)(.*)", path)
    base, rest = m.group(1), m.group(2)
    if lang == "ar" and base not in AR_PAGES:
        lang = "en"
    url = "/" + lang + base
    if not url.endswith("/"):
        url += "/"
    return url + rest


def img_url(name):
    for ext in ("webp", "jpg", "png"):
        if os.path.exists(os.path.join(SRC, "assets", "img", f"{name}.{ext}")):
            return f"/assets/img/{name}.{ext}"
    return None


def media(video, still, cls, eager=False):
    """Decorative backdrop: the Higgsfield loop when it exists, else the still with a slow CSS drift."""
    img = img_url(still)
    if not img:
        return ""
    clip = f"/assets/video/{video}.mp4"
    has_clip = os.path.exists(os.path.join(SRC, clip.lstrip("/")))
    load = "" if eager else ' loading="lazy"'
    inner = (f'<video muted loop playsinline preload="none" poster="{img}" data-ambient><source src="{clip}" type="video/mp4"></video>'
             if has_clip else f'<img src="{img}" alt=""{load} decoding="async">')
    return f'<div class="media {cls}{"" if has_clip else " still"}" aria-hidden="true">{inner}</div>'


def a_attrs(target, lang):
    if target == "soon":
        return 'href="#" data-soon'
    if target == "chat":
        return f'href="{localize("/contact", lang)}"'
    return f'href="{localize(target, lang)}"'


def instr_path(sym):
    return f"/markets/{sym.lower()}"


# ---------------------------------------------------------------- book parsing

LOGO = re.search(r'<svg width="32" height="32" viewBox="0 0 256 256" fill="none">(.*?)</svg>', book, re.S).group(1)
SEARCH_ICO = re.search(r'<div class="row" style="color:var\(--t2\)">(<svg.*?</svg>)</div>', book, re.S).group(1)


def logo(size=32, word=26, ar=20):
    return (f'<span class="lg"><svg width="{size}" height="{size}" viewBox="0 0 256 256" fill="none" aria-hidden="true">{LOGO}</svg>'
            f'<span class="wm" style="font-size:{word}px;color:#fff">Tharwa<em>Fx</em></span>'
            f'<span class="ar" style="font-size:{ar}px">ثروة</span></span>')


def book_css():
    start = book.find(":root{--g:")
    end = book.find("html{scroll-behavior:smooth")
    return book[start:end]


def screens():
    """Yield (id, lang, main_html) for every public-site screen."""
    for m in re.finditer(r'<section class="pg" id="(P\d\d)-(en|ar)">', book):
        sid, lang = m.group(1), m.group(2)
        body_start = book.find(f'<div dir="{"rtl" if lang == "ar" else "ltr"}" lang="{lang}">', m.end())
        body = book[body_start:div_end(book, body_start)]
        body = body[body.find(">") + 1:-len("</div>")]
        for marker in ('<div class="risk">', '<div class="top">', '<div class="nav">', '<div class="ft">'):
            body = cut_div(body, marker)
        yield sid, lang, body.strip()


# ---------------------------------------------------------------- shell

T = {
    "en": dict(risk="<b>Risk warning:</b> CFDs are leveraged products. You can lose more than you deposit. Trade only with money you can afford to lose.",
               traders="Traders", partners="Partners", cal="Economic calendar", contact="Contact", other="العربية",
               login="Log in", open="Open account", menu="Menu", search="Search", close="Close",
               tagline="Institutional-grade trading, built for the Arab trader.",
               legal="<b style=\"color:#ddd\">Risk warning:</b> Trading CFDs and forex carries a high level of risk and may not suit every investor. You can lose more than your deposit. [Legal entity] is authorised by [Regulator], licence [number], at [registered address, UAE]. Services are not offered in restricted jurisdictions.",
               bottom=["Privacy", "Terms", "Cookies", "Risk disclosure"],
               cols=[("Trading", ["Accounts", "Spreads", "Leverage and margin", "Trading hours", "Swap rates"]),
                     ("Markets", ["Forex", "Gold and metals", "Indices", "Stocks", "Crypto"]),
                     ("Platforms", ["MetaTrader 5", "WebTrader", "Tharwa app", "TradingView", "Trading tools"]),
                     ("Help", ["Help centre", "Calculators", "Glossary", "Deposits", "Withdrawals"]),
                     ("Company", ["About Tharwa", "Regulation", "Legal documents", "Stay safe", "Careers"])],
               cookie_t="We use cookies", cookie_d="Essential cookies keep the site working. Analytics are off until you agree.",
               accept="Accept all", essential="Essential only", skip="Skip to content"),
    "ar": dict(risk="<b>تحذير المخاطر:</b> عقود الفروقات منتجات بالرافعة المالية وقد تخسر أكثر من إيداعك. تداول فقط بأموال يمكنك تحمّل خسارتها.",
               traders="المتداولون", partners="الشركاء", cal="المفكرة الاقتصادية", contact="اتصل بنا", other="English",
               login="تسجيل الدخول", open="افتح حساباً", menu="القائمة", search="بحث", close="إغلاق",
               tagline="تداول بمستوى المؤسسات، مصمَّم للمتداول العربي.",
               legal="<b style=\"color:#ddd\">تحذير المخاطر:</b> ينطوي تداول عقود الفروقات والعملات على مخاطر مرتفعة وقد لا يناسب جميع المستثمرين، وقد تخسر أكثر من إيداعك. [الكيان القانوني] مرخَّص من [الجهة التنظيمية]، ترخيص رقم [الرقم]، وعنوانه [العنوان المسجل، الإمارات]. لا تُقدَّم الخدمات في الدول المحظورة.",
               bottom=["الخصوصية", "الشروط", "ملفات الارتباط", "إفصاح المخاطر"],
               cols=[("التداول", ["الحسابات", "الفروقات السعرية", "الرافعة والهامش", "ساعات التداول", "رسوم التبييت"]),
                     ("الأسواق", ["العملات", "الذهب والمعادن", "المؤشرات", "الأسهم", "العملات الرقمية"]),
                     ("المنصات", ["MetaTrader 5", "WebTrader", "تطبيق ثروة", "TradingView", "أدوات التداول"]),
                     ("المساعدة", ["مركز المساعدة", "الحاسبات", "المصطلحات", "الإيداع", "السحب"]),
                     ("الشركة", ["عن ثروة", "التراخيص", "الوثائق القانونية", "الحماية من الاحتيال", "الوظائف"])],
               cookie_t="نستخدم ملفات الارتباط", cookie_d="ملفات الارتباط الأساسية تُبقي الموقع يعمل. التحليلات متوقفة حتى توافق.",
               accept="قبول الكل", essential="الأساسية فقط", skip="انتقل إلى المحتوى"),
}


def other_lang_url(path, lang):
    if lang == "en":
        return localize(path if path in AR_PAGES else "/", "ar")
    return localize(path, "en")


def header(lang, path):
    t = T[lang]
    groups = MEGA[lang]
    active = next((i for i, (_, cols) in enumerate(groups)
                   if any(path == p or (p != "/" and path.startswith(p + "/")) for _, items in cols for _, p in items)), -1)
    nav_items, panels, drawer = [], [], []
    for i, (label, cols) in enumerate(groups):
        on = " on" if i == active else ""
        nav_items.append(f'<li class="{on.strip()}"><button type="button" class="nav-t" aria-expanded="false" aria-controls="mega-{i}">{label}<span class="chev"></span></button></li>')
        col_html, dr_links = [], []
        for head, items in cols:
            links = "".join(f'<li><a href="{localize(p, lang)}"{" aria-current=\"page\"" if p == path else ""}>{n}</a></li>' for n, p in items)
            col_html.append(f'<div><h5>{head or "&nbsp;"}</h5><ul>{links}</ul></div>')
            dr_links.append(links)
        panels.append(f'<div class="mega" id="mega-{i}" hidden><div class="wrap"><div class="mega-g">{"".join(col_html)}</div></div></div>')
        drawer.append(f'<details{" open" if i == active else ""}><summary>{label}<span class="chev"></span></summary><ul>{"".join(dr_links)}</ul></details>')
    other = other_lang_url(path, lang)
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<div class="risk">{t["risk"]}</div>
<div class="top"><div class="wrap"><ul><li class="cur"><a href="{localize("/", lang)}">{t["traders"]}</a></li><li><a href="{localize("/partners", lang)}">{t["partners"]}</a></li></ul><ul><li class="hide-s"><a href="{localize("/platforms/webtrader", lang)}">WebTrader</a></li><li class="hide-s"><a href="{localize("/tools/calendar", lang)}">{t["cal"]}</a></li><li class="hide-s"><a href="{localize("/contact", lang)}">{t["contact"]}</a></li><li class="lang"><a href="{other}" hreflang="{"ar" if lang == "en" else "en"}" lang="{"ar" if lang == "en" else "en"}">{t["other"]}</a></li></ul></div></div>
<header class="nav" id="nav"><div class="wrap"><a href="{localize("/", lang)}" aria-label="TharwaFx home">{logo()}</a><ul class="nav-l">{"".join(nav_items)}</ul><a class="srch" href="{localize("/search", lang)}" aria-label="{t["search"]}">{SEARCH_ICO}</a><div class="acts"><a class="b o sm" href="{localize("/login", lang)}">{t["login"]}</a><a class="b p sm" href="{localize("/register", lang)}">{t["open"]}</a></div><button type="button" class="burger" aria-expanded="false" aria-controls="drawer" aria-label="{t["menu"]}"><i></i><i></i><i></i></button></div>{"".join(panels)}<div class="drawer" id="drawer" hidden><div class="drawer-b">{"".join(drawer)}<div class="drawer-a"><a class="b o w" href="{localize("/login", lang)}">{t["login"]}</a><a class="b p w" href="{localize("/register", lang)}">{t["open"]}</a><a class="lk" href="{other}">{t["other"]}</a></div></div></div></header>'''


def footer(lang):
    t = T[lang]
    cols = "".join(
        f'<div><h5>{h}</h5><ul>{"".join(f"<li><a href=\"{localize(LINKS[lang].get(i) or LINKS['en'][i], lang)}\">{i}</a></li>" for i in items)}</ul></div>'
        for h, items in t["cols"])
    bottom = " · ".join(f'<a href="{localize(LINKS[lang].get(b) or LINKS["en"][b], lang)}">{b}</a>' for b in t["bottom"])
    return f'''<footer class="ft"><div class="wrap"><div class="grid"><div><a href="{localize("/", lang)}" aria-label="TharwaFx home">{logo(30, 25, 19)}</a><p class="mt16">{t["tagline"]}</p></div>{cols}</div>
<div class="leg">{t["legal"]}<div class="row sb mt16 wr"><span>© 2026 [Legal entity]</span><span>{bottom}</span></div></div></div></footer>
<div class="cookie" id="cookie" hidden role="dialog" aria-labelledby="cookie-t"><div><b id="cookie-t">{t["cookie_t"]}</b><p class="sm mut mt8">{t["cookie_d"]}</p></div><div class="row wr"><button type="button" class="b p sm" data-cookie="all">{t["accept"]}</button><button type="button" class="b q sm" data-cookie="essential">{t["essential"]}</button></div></div>
<div class="toast" id="toast" role="status" aria-live="polite" hidden></div>'''


def page(lang, path, title, desc, main, sid="", shell=True):
    d = "rtl" if lang == "ar" else "ltr"
    full_title = "TharwaFx | " + title if path == "/" else f"{title} | TharwaFx"
    canon = "https://tharwafx.com" + localize(path, lang)
    alt = ""
    if path in AR_PAGES:
        alt = (f'<link rel="alternate" hreflang="en" href="https://tharwafx.com{localize(path, "en")}">'
               f'<link rel="alternate" hreflang="ar" href="https://tharwafx.com{localize(path, "ar")}">')
    og = img_url("home-hero")
    og_tag = f'<meta property="og:image" content="https://tharwafx.com{og}">' if og else ""
    return f'''<!doctype html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">{alt}
<meta property="og:title" content="{html.escape(full_title)}"><meta property="og:description" content="{html.escape(desc)}">{og_tag}
<meta name="theme-color" content="#000000">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/Geist-100-900.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/book.css?v={VERSION}">
<link rel="stylesheet" href="/assets/site.css?v={VERSION}">
<script defer src="/assets/site.js?v={VERSION}"></script>
</head>
<body data-page="{sid.split(":")[0]}">
{header(lang, path) if shell else ""}
<main id="main">
{main}
</main>
{footer(lang) if shell else '<div class="toast" id="toast" role="status" aria-live="polite" hidden></div>'}
</body>
</html>
'''


# ---------------------------------------------------------------- content transforms

OPTIONS = {
    "Account currency": ["USD", "EUR", "AED", "GBP"], "عملة الحساب": ["USD", "EUR", "AED", "GBP"],
    "Instrument": list(INSTR), "الأداة": list(INSTR), "Leverage": ["1:500", "1:400", "1:200", "1:100", "1:50", "1:30"],
    "الرافعة": ["1:500", "1:400", "1:200", "1:100", "1:50", "1:30"],
    "Virtual balance": ["$1,000", "$10,000", "$50,000", "$100,000"],
    "Account type": ["Standard", "Raw Spread", "Islamic"],
    "Topic": ["Choose a topic", "Opening an account", "Verification", "Deposits", "Withdrawals", "MT5 and trading", "Partnerships", "A complaint", "Something else"],
}
VALUE_PAGES = {"P13", "P20", "P30"}
SUBMITS = {"Start demo": "demo", "Send message": "contact"}
HEADING_RE = re.compile(r"<(h[2-4]|b)\b[^>]*>(.*?)</\1>", re.S)


def context_target(label, before, lang):
    heads = HEADING_RE.findall(before[-2500:])
    if not heads:
        return None
    h = text(heads[-1][1])
    if h in INSTR:
        return instr_path(h)
    if label == "PDF":
        return "/legal/risk" if h in ("Risk disclosure",) else "soon"
    return LINKS[lang].get(h) or LINKS["en"].get(h)


def resolve(label, before, lang):
    if label in CONTEXT_LABELS:
        return context_target(label, before, lang)
    if label in ACTIONS[lang]:
        return ACTIONS[lang][label]
    if re.match(r"^(Sell|Buy|بيع|شراء)\b", label):
        return CLIENT + "/register"
    return LINKS[lang].get(label)


def linkify(s, lang, sid):
    def sub(m):
        cls, label = m.group(1), m.group(2)
        plain = text(label)
        if plain in SUBMITS:
            return f'<button type="submit" class="{cls}">{label}</button>'
        if plain in ("Calculate", "احسب"):
            return f'<button type="submit" class="{cls}">{label}</button>'
        if plain in ("Yes", "No"):
            return f'<button type="button" class="{cls}" data-feedback>{label}</button>'
        target = resolve(plain, s[:m.start()], lang)
        if target is None:
            return m.group(0)
        return f'<a class="{cls}" {a_attrs(target, lang)}>{label}</a>'
    return re.sub(r'<span class="(b [^"]*|lk)">([^<]*)</span>', sub, s)


def crumbs(s, lang):
    def sub(m):
        parts = [p.strip() for p in text(m.group(1)).split("/")]
        out = []
        for i, p in enumerate(parts):
            target = LINKS[lang].get(p) or LINKS["en"].get(p)
            if i < len(parts) - 1 and target:
                out.append(f'<a href="{localize(target, lang)}">{p}</a>')
            else:
                out.append(f'<b>{p}</b>' if i == len(parts) - 1 else p)
        return f'<nav class="crumb" aria-label="Breadcrumb">{" / ".join(out)}</nav>'
    return re.sub(r'<div class="crumb">(.*?)</div>', sub, s)


def controls(s, lang, sid):
    # Pills: section links on the academy hub, filters elsewhere, plain tags in articles.
    def pill(m):
        cls, label = m.group(1), m.group(2)
        if sid == "P24" and label in LINKS[lang]:
            cur = ' aria-current="page"' if "on" in cls.split() else ""
            return f'<a class="pill{cls}" href="{localize(LINKS[lang][label], lang)}"{cur}>{label}</a>'
        if sid == "P29":
            return m.group(0)
        return f'<button type="button" class="pill{cls}" aria-pressed="{"true" if "on" in cls.split() else "false"}">{label}</button>'
    s = re.sub(r'<span class="pill([^"]*)">([^<]*)</span>', pill, s)
    # Segmented controls and tabs.
    s = re.sub(r'(<div class="(?:seg|tabs)[^"]*">)(.*?)(</div>)',
               lambda m: m.group(1) + re.sub(r'<span( class="([^"]*)")?>([^<]*)</span>',
                                             lambda t: f'<button type="button" class="{t.group(2) or ""}" aria-pressed="{"true" if t.group(2) == "on" else "false"}">{t.group(3)}</button>',
                                             m.group(2)) + m.group(3), s, flags=re.S)
    # Instrument symbols in tables link to their page.
    s = re.sub(r'<b class="mono">([A-Z0-9]{3,7})</b>',
               lambda m: f'<a class="sym" href="{localize(instr_path(m.group(1)), lang)}"><b class="mono">{m.group(1)}</b></a>' if m.group(1) in INSTR else m.group(0), s)
    return s


def fields(s, lang, sid):
    """Turn the book's drawn fields into real inputs, selects and textareas."""
    def field(m):
        label, cls, style, inner = m.group(1), m.group(2), m.group(3) or "", m.group(4)
        name = re.sub(r"[^a-z0-9]+", "-", text(label).lower()).strip("-") or "f" + str(abs(hash(label)) % 999)
        val = text(re.sub(r"<svg.*?</svg>", "", inner, flags=re.S))
        cid = f"f-{sid.lower()}-{name}"
        req = "" if sid in VALUE_PAGES else " required"
        if "chev" in inner:
            opts = OPTIONS.get(text(label), [val])
            if val and val not in opts:
                opts = [val] + opts
            o = "".join(f'<option{" selected" if x == val else ""}{" value=\"\"" if x.startswith("Choose") else ""}>{x}</option>' for x in opts)
            ctl = f'<select class="i" id="{cid}" name="{name}"{req}>{o}</select>'
        elif "height:120px" in style:
            ctl = f'<textarea class="i" id="{cid}" name="{name}" rows="5" placeholder="{html.escape(val)}"{req}></textarea>'
        else:
            kind = "email" if "mail" in name else "text"
            mode = ' inputmode="decimal"' if sid in VALUE_PAGES else ""
            if sid in VALUE_PAGES:
                ctl = f'<input class="i" id="{cid}" name="{name}" type="text"{mode} value="{html.escape(val)}">'
            else:
                ctl = f'<input class="i" id="{cid}" name="{name}" type="{kind}" placeholder="{html.escape(val)}"{req}>'
        return f'<div class="f"><label for="{cid}">{label}</label>{ctl}</div>'
    s = re.sub(r'<div class="f"><label>(.*?)</label><div class="i([^"]*)"( style="[^"]*")?>(.*?)</div></div>', field, s, flags=re.S)
    # Search boxes drawn as fields.
    def search(m):
        cls, style, ph, icon = m.group(1).replace(" ph", ""), m.group(2) or "", m.group(3), m.group(4)
        action = localize("/search", lang)
        filt = ' data-filter="glossary"' if sid == "P32" else ""
        return (f'<form class="i srchbox{cls}" role="search" action="{action}"{style}{filt}>'
                f'<input type="search" name="q" placeholder="{ph}" aria-label="{ph}">'
                f'<button type="submit" aria-label="{T[lang]["search"]}">{icon}</button></form>')
    s = re.sub(r'<div class="i([^"]*)"( style="[^"]*")?><span[^>]*>([^<]*)</span>(<svg.*?</svg>)</div>', search, s, flags=re.S)
    return s


def faqs(s, lang):
    def sub(m):
        q, a = m.group(1), m.group(3)
        if a:
            a = re.sub(r"^<p[^>]*>|</p>$", "", a)
        else:
            a = FAQ.get(text(q), "")
        return (f'<details class="faq"{" open" if m.group(2) == "−" else ""}><summary class="row sb"><span>{q}</span>'
                f'<span class="grn faq-i" aria-hidden="true"></span></summary><p class="mut">{a}</p></details>')
    return re.sub(r'<div style="padding:18px 0;border-bottom:1px solid var\(--gr\)"><div class="row sb" style="font-weight:600"><span>(.*?)</span><span class="grn">(.)</span></div>(<p[^>]*>.*?</p>)?</div>', sub, s)


def forms(s, sid):
    """Wrap demo, contact and calculator cards in real forms."""
    if sid == "P07":
        s = s.replace('<div class="card col gap16"><h3>', '<form class="card col gap16" data-form="demo" novalidate><h3>', 1)
        s = s.replace('</p></div></div></div></section>', '</p></form></div></div></section>', 1)
    if sid == "P35":
        s = s.replace('<div class="card col gap16"><h3>', '<form class="card col gap16" id="message" data-form="contact" novalidate><h3>', 1)
        s = re.sub(r'(<button type="submit" class="b p ">Send message</button>)</div>', r'\1</form>', s, count=1)
    if sid in ("P30", "P13"):
        s = s.replace('<div class="card col gap16">', '<form class="card col gap16" data-calc>', 1)
        if sid == "P30":
            s = re.sub(r'(<button type="submit" class="b p w">[^<]*</button>)</div>', r'\1</form>', s, count=1)
            s = s.replace('<div class="card dg">', '<div class="card dg" data-calc-out aria-live="polite">', 1)
        else:
            s = re.sub(r'(<b class="mono grn">\$233\.38</b>)</div></div>', r'<output class="mono grn" data-calc-margin>$233.38</output></div></form>', s, count=1)
            s = s.replace('<div class="row sb" style="border-top:1px solid var(--gr);padding-top:14px"><b>Margin required</b><output',
                          '<div class="row sb" style="border-top:1px solid var(--gr);padding-top:14px"><b>Margin required</b><output')
    return s


MARKET_ORDER = ["forex", "metals", "indices", "stocks", "commodities", "crypto"]


def images(s, sid, lang):
    if sid == "P01":
        s = s.replace('#000 70%);border-bottom:1px solid #1e1e1e">',
                      '#000 70%);border-bottom:1px solid #1e1e1e">' + media("hero-loop", "home-hero", "hero-img", eager=True), 1)
        s = s.replace('<div style="border-bottom:1px solid #1e1e1e;padding:28px 0"><div class="wrap g5">', '<div class="stats"><div class="wrap g5">', 1)
        # The hero's way in to the AI page.
        new, label = ("جديد", "تداول بمساعدة الذكاء الاصطناعي") if lang == "ar" else ("New", "Trade with AI")
        pill = (f'<a class="ai-pill" href="{localize("/ai", lang)}"><span class="ai-dot"></span>{new}<b>{label}</b>'
                '<span class="go" aria-hidden="true">→</span></a>')
        s = re.sub(r'<div><h1 style="font-size:\d+px">', lambda m: "<div>" + pill + m.group(0)[5:], s, count=1)
        # The coded phone mockup stands on a lit plinth.
        s = s.replace('<div><div class="phone" style="min-height:520px;width:300px;margin:0 auto">',
                      '<div class="stage">' + media("platform-loop", "platform-stage", "stage-bg") + '<div class="phone" style="min-height:520px;width:300px;margin:0 auto">', 1)
        s += cta_band(lang)
        order = iter(MARKET_ORDER)

        def card(m):
            u = img_url("market-" + next(order))
            if not u:
                return m.group(0)
            return f'<div class="card mkt" style="--img:url({u});{m.group(1)}'
        s = re.sub(r'<div class="card" style="((?:grid-column:span 2;)?min-height:220px;)', card, s)
    if sid == "P09" or sid.startswith("MKT:"):
        key = "forex" if sid == "P09" else sid[4:]
        backdrop = media(f"{key}-loop", "market-" + key, "hero-media", eager=True)
        if backdrop:
            s = s.replace('<div class="hero">', '<div class="hero has-img">' + backdrop, 1)
    if sid == "P27":
        names = iter(["video-first-order", "video-stop-loss", "video-deposit", "video-install-mt5"])

        def thumb(m):
            u = img_url(next(names))
            return f'<div class="thumb" style="--img:url({u});height:150px;' if u else m.group(0)
        s = re.sub(r'<div style="height:150px;', thumb, s)
    if sid == "P28":
        u = img_url("blog-gold-dollar")
        if u:
            s = re.sub(r'(<p class="mut mt16">\[Author name\], \[date\]</p></div>)<svg.*?</svg>',
                       rf'\1<a class="thumb feat" href="{localize("/blog/article", lang)}" style="--img:url({u})" aria-label="Read article"></a>', s, count=1, flags=re.S)
    if sid == "P29":
        u = img_url("blog-gold-dollar")
        if u:
            s = re.sub(r'(<p class="mt24" style="font-size:19px">.*?</p>)', rf'\1<div class="thumb fig mt32" style="--img:url({u})" role="img" aria-label="Gold and the US dollar"></div>', s, count=1)
    for pid, name, alt in (("P36", "about-office", "Tharwa office at night"), ("P39", "careers-team", "Tharwa workspace")):
        if sid == pid:
            u = img_url(name)
            if u:
                hero_end = div_end(s, s.find('<div class="hero">'))
                s = s[:hero_end] + f'<section class="band"><div class="wrap"><div class="band-img" style="--img:url({u})" role="img" aria-label="{alt}"></div></div></section>' + s[hero_end:]
    return s


CTA = {
    "en": ("Ready when the market is.", "Open a live account, or practise first with a free demo.", "Open account", "Try a free demo", "Capital at risk."),
    "ar": ("جاهزون متى تحرّك السوق.", "افتح حساباً حقيقياً، أو تدرّب أولاً بحساب تجريبي مجاني.", "افتح حساباً", "جرّب حساباً تجريبياً مجاناً", "رأس مالك معرّض للخطر."),
}


def cta_band(lang):
    """Closing band on the home page, over the desert loop."""
    h, p, primary, demo, risk = CTA[lang]
    return (f'<section class="cta-band">{media("cta-loop", "cta-desert", "cta-bg")}<div class="wrap">'
            f'<h2>{h}</h2><p class="lead mt16">{p}</p><div class="row wr mt32">'
            f'<a class="b p" href="{localize("/register", lang)}">{primary}</a><a class="b o" href="{localize("/demo", lang)}">{demo}</a></div>'
            f'<p class="xs mut3 mt16">{risk}</p></div></section>')


def glossary(s, sid):
    if sid != "P32":
        return s
    letters = sorted({t[0][0] for t in GLOSSARY})
    chips = "".join(f'<button type="button" class="chip" style="height:36px;padding:0 12px;" data-letter="{c}">{c}</button>' for c in letters)
    s = re.sub(r'<div class="row wr mb24" style="gap:6px">.*?</div>', f'<div class="row wr mb24" style="gap:6px" data-letters>{chips}</div>', s, count=1, flags=re.S)
    items = "".join(f'<div class="term" style="padding:18px 0;border-bottom:1px solid var(--gr)" id="{re.sub(r"[^a-z]+", "-", en.lower())}"><b>{en}</b> <span class="mut3" lang="ar">{ar}</span><p class="mut mt8">{d}</p></div>' for en, ar, d in GLOSSARY)
    start = s.find('<div style="padding:18px 0;border-bottom:1px solid var(--gr)"><b>')
    end = s.rfind("</div></div></section>")
    return s[:start] + f'<div data-terms>{items}</div><p class="mut" data-empty hidden>No terms match your search.</p>' + s[end:]


def results(s, sid):
    if sid != "P43":
        return s
    start = s.find('<div class="row mb16">')
    end = s.rfind("</div></section>")
    box = ('<form class="i srchbox mb32" role="search" action="/en/search/" style="height:58px">'
           '<input type="search" name="q" placeholder="Search accounts, markets and help" aria-label="Search">'
           f'<button type="submit" aria-label="Search">{SEARCH_ICO}</button></form>')
    return s[:start] + box + '<div data-results>' + s[start:end] + '</div>' + s[end:]


def transform(main, sid, lang):
    base = sid.split(":")[0] if ":" in sid else sid
    s = crumbs(main, lang)
    s = faqs(s, lang)
    s = fields(s, lang, base)
    s = controls(s, lang, base)
    s = linkify(s, lang, base)
    s = forms(s, base)
    s = images(s, sid, lang)
    s = glossary(s, base)
    s = results(s, base)
    # The book's absolute-size SVG illustrations scale on small screens.
    s = re.sub(r'<svg width="(\d+(?:\.\d+)?)" height="(\d+)"( viewBox="[^"]+")', r'<svg class="ill" width="\1" height="\2"\3', s)
    s = re.sub(r'<div class="tbl">(<table>.*?</table>)</div>', r'<div class="tbl"><div class="tscroll">\1</div></div>', s, flags=re.S)
    return s


def meta(main):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    lead = re.search(r'<p class="lead[^"]*">(.*?)</p>', main, re.S)
    title = text(re.sub(r"<br>", " ", h1.group(1))) if h1 else "TharwaFx"
    return title, text(lead.group(1)) if lead else "Trade forex, gold, indices and stocks on MetaTrader 5 with TharwaFx."


# ---------------------------------------------------------------- generated pages

def fmt_price(p):
    if p >= 1000:
        return f"{p:,.1f}" if p >= 10000 else f"{p:,.2f}"
    return f"{p:.5f}" if p < 10 else (f"{p:.3f}" if p < 200 else f"{p:.2f}")


def market_page(p09, key):
    m = MARKETS[key]
    s = p09.replace("Home / Markets / Forex", f"Home / Markets / {m['name']}")
    s = s.replace("Trade forex with clear costs", m["title"])
    s = s.replace("The world's most traded market, priced from a deep pool of liquidity providers.", m["lead"])
    pills = "".join(f'<span class="pill{" on" if i == 0 else " "}">{p}</span>' for i, p in enumerate(m["pills"]))
    s = re.sub(r'(<div class="row sb mb24"><div class="row">).*?(</div><span class="tg ol">)', rf"\g<1>{pills}\2", s, count=1, flags=re.S)
    rows = "".join(
        f'<tr><td><b class="mono">{sym}</b><div class="xs mut3">{INSTR[sym][0]}</div></td><td><span class="mono">{INSTR[sym][3]}</span></td>'
        f'<td><span class="mono">{INSTR[sym][4]}</span></td><td><span class="mono">1:{INSTR[sym][6]}</span></td>'
        f'<td><span class="mono">{INSTR[sym][7]}</span></td><td><span class="lk">Details</span></td></tr>'
        for sym in m["syms"])
    table = ('<table><tr><th>Symbol</th><th>Avg spread</th><th>Contract size</th><th>Leverage up to</th>'
             f'<th>Swap long / short</th><th></th></tr>{rows}</table>')
    s = re.sub(r"<table>.*?</table>", table, s, count=1, flags=re.S)
    s = s.replace("<b>24 hours, 5 days</b>", f"<b>{m['hours']}</b>")
    s = s.replace("The market opens Monday in Asia and closes Friday in New York.", m["hours_t"])
    return s


def instrument_page(p10, sym):
    name, cat, price, spread, size, tick, lev, swap, sess = INSTR[sym]
    spr = float(spread) * (0.01 if cat == "metals" and sym == "XAUUSD" else 1)
    bid = price
    ask = price + max(spr * float(tick) * (10 if cat == "forex" else 1), float(tick))
    s = p10.replace("Gold and metals / XAUUSD", f"{MARKET_NAMES[cat]} / {sym}")
    s = s.replace("Gold against the US dollar", name)
    s = s.replace("XAUUSD", sym)
    s = s.replace("Sell 2,398.21", f"Sell {fmt_price(bid)}").replace("Buy 2,398.28", f"Buy {fmt_price(ask)}")
    rows = [("Contract size", size), ("Tick size", tick), ("Spread, average", spread + "*"),
            ("Leverage up to", f"1:{lev}*"), ("Margin, 1 lot", "[calculated]"), ("Swap long / short", swap + "*"),
            ("Session", sess + "*"), ("Restrictions", "[By region]")]
    body = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    s = re.sub(r"(<tr><th[^>]*>Contract specification</th><th[^>]*>[^<]*</th></tr>).*?(</table>)", rf"\1{body}\2", s, count=1, flags=re.S)
    return s


def standard_page(p04):
    s = p04.replace("Home / Trading / Accounts / Raw Spread", "Home / Trading / Accounts / Standard")
    s = s.replace("<h1>Raw Spread account</h1>", "<h1>Standard account</h1>")
    s = s.replace("For active traders who want the tightest pricing and a clear commission.",
                  "Simple pricing with every cost built into the spread. A good first live account.")
    s = s.replace('<th class="">Raw Spread</th>', '<th class="">Standard</th>')
    s = s.replace("0.0 pips*", "0.8 pips*").replace("$3.50 per lot, per side*", "None, the cost is in the spread")
    s = s.replace("Spread 0.1 pip</span><span class=\"mono\">$1.00", "Spread 0.8 pip</span><span class=\"mono\">$8.00")
    s = s.replace("Commission, round turn</span><span class=\"mono\">$7.00", "Commission</span><span class=\"mono\">$0.00")
    return s


# ---------------------------------------------------------------- access pages (register, log in)

AUTH = {"C01": ("/register", "register"), "C02": ("/verify-email", "verify"), "C03": ("/login", "login"),
        "C04": ("/login/2fa", "2fa"), "C05": ("/recover", "recover")}
COUNTRIES = {
    "en": ["United Arab Emirates", "Saudi Arabia", "Qatar", "Kuwait", "Bahrain", "Oman", "Egypt", "Jordan", "Lebanon", "Morocco", "Other"],
    "ar": ["الإمارات العربية المتحدة", "السعودية", "قطر", "الكويت", "البحرين", "عُمان", "مصر", "الأردن", "لبنان", "المغرب", "أخرى"],
}
AUTH_LINKS = {
    "Log in": "/login", "سجّل الدخول": "/login", "Open account": "/register", "افتح حساباً": "/register",
    "Forgot password?": "/recover", "نسيت كلمة المرور؟": "/recover", "Back to log in": "/login",
}
EYE = ('<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
       'stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>')


def auth_screens():
    for m in re.finditer(r'<section class="pg" id="(C0[1-5])-(en|ar)">', book):
        sid, lang = m.group(1), m.group(2)
        start = book.find('<div class="auth">', m.end())
        yield sid, lang, book[start:div_end(book, start)]


def auth_transform(s, sid, lang):
    path, kind = AUTH[sid]
    t = T[lang]
    s = s.replace('<div class="l">', '<div class="l">' + media("auth-loop", "auth-panel", "auth-bg", eager=True), 1)
    # Left panel: logo goes home, plus a language switch.
    s = re.sub(r'<div><span class="lg">(.*?)</span></span></div>',
               lambda m: f'<div class="row sb"><a href="{localize("/", lang)}" aria-label="TharwaFx home"><span class="lg">{m.group(1)}</span></span></a>'
                         f'<a class="lk" href="{other_lang_url(path, lang)}">{t["other"]}</a></div>', s, count=1, flags=re.S)

    def field(m):
        label, inner, hint = m.group(1), m.group(2), m.group(3) or ""
        low = text(label).lower()
        if "country" in low or "بلد" in low:
            val = text(inner)
            opts = "".join(f'<option{" selected" if c == val else ""}>{c}</option>' for c in COUNTRIES[lang])
            return f'<div class="f"><label for="a-country">{label}</label><select class="i" id="a-country" name="country" autocomplete="country-name" required>{opts}</select></div>'
        if "mail" in low or "البريد" in low:
            return (f'<div class="f"><label for="a-email">{label}</label><input class="i" id="a-email" name="email" type="email" '
                    f'autocomplete="email" placeholder="name@example.com" dir="ltr" required></div>')
        new = kind == "register"
        hint_html = re.sub(r'<span class="hint">', '<span class="hint" id="a-pass-hint">', hint)
        return (f'<div class="f"><label for="a-pass">{label}</label><div class="pw"><input class="i" id="a-pass" name="password" type="password" '
                f'autocomplete="{"new-password" if new else "current-password"}" dir="ltr" required{" minlength=\"10\" aria-describedby=\"a-pass-hint\"" if new else ""}>'
                f'<button type="button" class="pw-t" aria-label="{"إظهار كلمة المرور" if lang == "ar" else "Show password"}" aria-pressed="false">{EYE}</button></div>{hint_html}</div>')
    s = re.sub(r'<div class="f"><label>(.*?)</label><div class="i[^"]*"><span>(.*?)</span>(?:<span class="chev"></span>)?</div>(<span class="hint">.*?</span>)?</div>', field, s, flags=re.S)
    s = re.sub(r'<div class="chk[^"]*"><i></i><span>(.*?)</span></div>',
               lambda m: f'<label class="chk"><input type="checkbox" name="{"terms" if kind == "register" else "remember"}"{" required" if kind == "register" else ""}><i></i><span>{m.group(1)}</span></label>', s)
    s = re.sub(r'<div class="otp">.*?</div>',
               '<div class="otp" role="group">' + "".join(
                   f'<input inputmode="numeric" pattern="[0-9]" maxlength="1" aria-label="{"الرقم" if lang == "ar" else "Digit"} {i + 1}"'
                   f'{" autocomplete=\"one-time-code\"" if i == 0 else ""}>' for i in range(6)) + '</div>', s, count=1, flags=re.S)
    s = re.sub(r'<div class="seg"([^>]*)>(.*?)</div>',
               lambda m: f'<div class="seg"{m.group(1)}>' + re.sub(r'<span( class="on")?>([^<]*)</span>',
                                                                   lambda b: f'<button type="button" class="{"on" if b.group(1) else ""}" aria-pressed="{"true" if b.group(1) else "false"}">{b.group(2)}</button>',
                                                                   m.group(2)) + '</div>', s, count=1, flags=re.S)
    s = re.sub(r'<span class="b p w">([^<]*)</span>', lambda m: f'<button type="submit" class="b p w">{m.group(1)}</button>', s)

    def lk(m):
        label = m.group(1)
        if label in AUTH_LINKS:
            return f'<a class="lk" href="{localize(AUTH_LINKS[label], lang)}">{label}</a>'
        if label.startswith("Resend"):
            return '<button type="button" class="lk" data-resend disabled>Resend in <span class="mono">0:45</span></button>'
        return f'<a class="lk" href="#" data-soon>{label}</a>'
    s = re.sub(r'<span class="lk">([^<]*)</span>', lk, s)
    s = s.replace("a••••d@example.com", '<b data-email dir="ltr">your email</b>')
    # Sample-only notices: the device alert is dropped, the reset confirmation waits for a submit.
    s = re.sub(r'<div class="al a"><span>New device:.*?</span></div>', "", s)
    s = s.replace('<div class="al g">', '<div class="al g" data-sent hidden role="status">')
    r = s.find('<div class="r">')
    end = div_end(s, r)
    s = s[:r] + f'<form class="r" data-auth="{kind}" novalidate>' + s[r + len('<div class="r">'):end - 6] + "</form>" + s[end:]
    return s


# ---------------------------------------------------------------- write

def write(lang, path, html_text):
    rel = localize(path, lang).strip("/")
    target = os.path.join(OUT, rel, "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w", encoding="utf-8").write(html_text)


def main():
    os.makedirs(OUT, exist_ok=True)
    # Empty folders bottom-up rather than deleting them: a folder open in a shell cannot be removed on Windows.
    for here, dirs, files in os.walk(OUT, topdown=False):
        for f in files:
            os.remove(os.path.join(here, f))
        for d in dirs:
            try:
                os.rmdir(os.path.join(here, d))
            except OSError:
                pass
    shutil.copytree(os.path.join(SRC, "assets"), os.path.join(OUT, "assets"))
    fonts = """@font-face{font-family:Geist;src:url(fonts/Geist-100-900.woff2) format("woff2");font-weight:100 900;font-display:swap}
@font-face{font-family:GMono;src:url(fonts/GMono-100-900.woff2) format("woff2");font-weight:100 900;font-display:swap}
@font-face{font-family:Plex;src:url(fonts/Plex-400.woff2) format("woff2");font-weight:400;size-adjust:110%;font-display:swap}
@font-face{font-family:Plex;src:url(fonts/Plex-500.woff2) format("woff2");font-weight:500;size-adjust:110%;font-display:swap}
@font-face{font-family:Plex;src:url(fonts/Plex-600.woff2) format("woff2");font-weight:600;size-adjust:110%;font-display:swap}
@font-face{font-family:Plex;src:url(fonts/Plex-700-800.woff2) format("woff2");font-weight:700 800;size-adjust:110%;font-display:swap}
"""
    open(os.path.join(OUT, "assets", "book.css"), "w", encoding="utf-8").write(fonts + book_css())
    open(os.path.join(OUT, "assets", "favicon.svg"), "w", encoding="utf-8").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><rect width="256" height="256" fill="#000"/>{LOGO}</svg>')

    raw = {(sid, lang): main for sid, lang, main in screens() if sid in BOOK_PAGES or sid == "P44"}
    index = []

    def emit(sid, lang, path, main_html):
        out = transform(main_html, sid, lang)
        title, desc = meta(out)
        write(lang, path, page(lang, path, title, desc, out, sid))
        index.append({"t": title, "d": desc, "u": localize(path, lang), "l": lang})

    for (sid, lang), main_html in raw.items():
        if sid == "P44":
            continue
        emit(sid, lang, BOOK_PAGES[sid], main_html)

    p09, p10, p04 = raw[("P09", "en")], raw[("P10", "en")], raw[("P04", "en")]
    for key in MARKETS:
        emit("MKT:" + key, "en", "/markets/" + key, market_page(p09, key))
    for sym in INSTR:
        if sym != "XAUUSD":
            emit("P10", "en", instr_path(sym), instrument_page(p10, sym))
    emit("P04", "en", "/accounts/standard", standard_page(p04))

    # System pages: the book's 404 and 503 cards, each on its own page.
    cards = re.findall(r'<div class="card c" style="padding:56px 32px">.*?</span></div>', raw[("P44", "en")], re.S)
    for code, card in (("404", cards[0]), ("503", cards[1])):
        body = f'<section class="sec"><div class="wrap sys">{card}</div></section>'
        body = linkify(body, "en", "P44")
        title = "Page not found" if code == "404" else "Back shortly"
        doc = page("en", "/" + code, title, title, body, "P44").replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"')
        write("en", "/" + code, doc)
        if code == "404":
            open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(doc)

    import client
    # The book draws register and log in in Arabic; the code and reset steps are translated so the Arabic flow stays Arabic.
    found = list(auth_screens())
    native = {(sid, lang) for sid, lang, _ in found}
    AR_PAGES.update(AUTH[sid][0] for sid, _, _ in found)
    for sid, lang, auth in found + [(sid, "ar", a) for sid, lang, a in found if (sid, "ar") not in native]:
        path, kind = AUTH[sid]
        body = auth_transform(auth, sid, lang)
        if (sid, lang) not in native:
            body = client.translate(body)
        title = text(re.search(r"<h2[^>]*>(.*?)</h2>", body[body.find('class="r"'):], re.S).group(1))
        doc = page(lang, path, title, title, body, sid, shell=False)
        write(lang, path, doc.replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"'))

    apps = client.build_all()
    import ai
    index.extend(ai.build_all())

    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        '<!doctype html><meta charset="utf-8"><title>TharwaFx</title><meta http-equiv="refresh" content="0; url=/en/">'
        '<link rel="canonical" href="https://tharwafx.com/en/"><a href="/en/">TharwaFx</a>')
    calc = {}
    for sym, (name, cat, price, *_rest) in INSTR.items():
        size, pip = CALC_OVERRIDES.get(sym, CALC[cat])
        swap = [float(x.replace("−", "-").replace("+", "")) if "%" not in x else 0 for x in _rest[4].split(" / ")]
        calc[sym] = {"p": price, "c": size, "pip": pip, "q": sym[3:] if cat == "forex" else "USD", "sl": swap[0], "ss": swap[1]}
    json.dump(calc, open(os.path.join(OUT, "assets", "instruments.json"), "w", encoding="utf-8"))
    json.dump(index, open(os.path.join(OUT, "assets", "search.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump({k: {"aspect": a, "prompt": p} for k, (a, p) in IMAGES.items()},
              open(os.path.join(ROOT, "build", "images.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Built {len(index) + 2} pages and {apps} client-area screens into {OUT}")


if __name__ == "__main__":
    main()
